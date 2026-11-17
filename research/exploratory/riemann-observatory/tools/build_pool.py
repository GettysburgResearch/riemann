#!/usr/bin/env python3
"""Build the Riemann Observatory candidate pool from raw harvests.

Inputs  (RAW dir): zbmath/*.jsonl (raw zbMATH API records), arxiv/*.jsonl (parsed arXiv Atom records),
                   zbmath_extra/*.jsonl (records fetched by id during citation expansion; optional)
Outputs (OUT dir): pool.jsonl  — one normalized record per candidate work (zbMATH- or arXiv-keyed)
                   citation_counts.json — in-pool citation counts keyed by zbMATH document id
                   expansion_ids.txt — highly cited referenced zbMATH ids not yet in the pool
Usage: python3 build_pool.py RAW OUT [EXPANSION_MIN_CITES]
"""
import json, os, re, sys, glob, collections, unicodedata

CORE = {"msc_11M26": 3.0, "kw_RH_any": 3.0, "kw_zeta_zeros": 3.0, "kw_li_criterion": 3.0, "kw_nyman": 3.0,
        "kw_robin": 3.0, "kw_debruijn_newman": 3.0, "kw_hilbert_polya": 3.0, "kw_weil_positivity": 2.5,
        "kw_zero_density": 2.5, "kw_zero_free": 2.5, "kw_pair_correlation": 2.5, "kw_laguerre_polya_xi": 2.5,
        "kw_deBranges": 2.5, "kw_trace_formula_zeta": 2.5, "msc_11M50": 2.5, "msc_11M06": 2.0, "msc_11Y35": 2.0,
        "kw_moments_zeta": 2.0, "msc_11M45": 1.5, "msc_11M20": 1.5, "kw_function_field_rh": 2.0,
        "kw_selberg_class": 2.0, "kw_GRH": 1.5, "msc_11M36": 1.5, "msc_11N05": 1.2, "msc_11N56_rh": 2.0}
ARX = {"rh_abs": 3.0, "rh_ti": 3.5, "zeta_zeros": 3.0, "zeta_zeros2": 3.0, "critical_line": 2.5, "zero_density": 2.5,
       "zero_free": 2.5, "debruijn_newman": 3.0, "li_criterion": 3.0, "nyman_beurling": 3.0, "robin": 3.0,
       "weil_explicit": 2.5, "hilbert_polya": 3.0, "berry_keating": 2.5, "de_branges": 2.5, "pair_corr": 2.5,
       "moments_zeta": 2.5, "random_matrix_zeta": 2.0, "jensen_poly": 2.5, "explicit_formula": 1.2, "mollifier": 2.5,
       "selberg_class": 2.0, "grh": 1.5, "large_values_dirichlet": 2.5, "verification_zeros": 3.0, "connes_rh": 2.5,
       "function_field_rh": 2.0, "mertens_conj": 2.5, "universality_zeta": 2.0, "zeta_extreme": 2.5}
MASK = "zbMATH Open Web Interface contents unavailable due to conflicting licenses."

def norm_title(t):
    t = unicodedata.normalize("NFKD", t or "").encode("ascii", "ignore").decode().lower()
    t = re.sub(r"\\[a-z]+\{([^}]*)\}", r"\1", t)
    return re.sub(r"[^a-z0-9]+", " ", t).strip()

def stratum(y):
    try:
        y = int(y)
    except Exception:
        return "S?"
    for lo, hi, s in [(1859, 1900, "S1"), (1901, 1950, "S2"), (1951, 1980, "S3"), (1981, 2000, "S4"),
                      (2001, 2015, "S5"), (2016, 2023, "S6"), (2024, 2026, "S7")]:
        if lo <= y <= hi:
            return s
    return "S?"

def zb_norm(r, qname):
    t = r.get("title") or {}
    title = t.get("title") or t.get("original") or ""
    if title == MASK:
        title = t.get("original") or ""
    authors = [a.get("name") for a in (r.get("contributors") or {}).get("authors", []) if a.get("name")]
    links = r.get("links") or []
    doi = next((l["identifier"] for l in links if l.get("type") == "doi"), "")
    arx = next((l["identifier"] for l in links if l.get("type") == "arxiv"), "")
    src = r.get("source") or {}
    venue = src.get("source") if src.get("source") and src.get("source") != MASK else ""
    if not venue and src.get("series"):
        s0 = src["series"][0]
        venue = f"{s0.get('short_title') or s0.get('title') or ''} {s0.get('volume') or ''}, {s0.get('year') or ''}".strip()
    rev = ""
    for ec in r.get("editorial_contributions") or []:
        if ec.get("text") and ec["text"] != MASK:
            rev = ec["text"]
            break
    refs = [x["zbmath"]["document_id"] for x in (r.get("references") or [])
            if isinstance(x, dict) and x.get("zbmath") and x["zbmath"].get("document_id")]
    return {"key": f"zb:{r['id']}", "zbmath_id": r["id"], "zbl": r.get("identifier"), "database": r.get("database"),
            "title": title, "title_original": t.get("original") or "", "authors": authors, "year": r.get("year"),
            "venue": venue, "doi": doi, "arxiv": arx, "doc_type": (r.get("document_type") or {}).get("code"),
            "msc": [m.get("code") for m in r.get("msc") or []], "keywords": r.get("keywords") or [],
            "language": ((r.get("language") or {}).get("languages") or [""])[0], "review": rev[:4000],
            "refs": refs, "queries": [qname], "zbmath_url": r.get("zbmath_url")}

def main(raw, out, min_cites=6):
    os.makedirs(out, exist_ok=True)
    pool = {}
    for path in sorted(glob.glob(os.path.join(raw, "zbmath", "*.jsonl")) + sorted(glob.glob(os.path.join(raw, "zbmath_extra", "*.jsonl")))):
        q = os.path.basename(path)[:-6]
        for line in open(path):
            try:
                r = json.loads(line)
            except Exception:
                continue
            n = zb_norm(r, q)
            if n["key"] in pool:
                if q not in pool[n["key"]]["queries"]:
                    pool[n["key"]]["queries"].append(q)
            else:
                pool[n["key"]] = n
    by_arxiv = {p["arxiv"].split("v")[0] if re.match(r"^\d{4}\.\d{4,5}v\d+$", p["arxiv"] or "") else p["arxiv"]: k
                for k, p in pool.items() if p.get("arxiv")}
    by_doi = {p["doi"].lower(): k for k, p in pool.items() if p.get("doi")}
    # arXiv records
    for path in sorted(glob.glob(os.path.join(raw, "arxiv", "*.jsonl"))):
        q = "arxiv_" + os.path.basename(path)[:-6]
        for line in open(path):
            a = json.loads(line)
            aid = re.sub(r"v\d+$", "", a["arxiv_id"])
            k = by_arxiv.get(aid) or (by_doi.get(a["doi"].lower()) if a.get("doi") else None)
            if k:
                p = pool[k]
                p.setdefault("arxiv_abstract", a["summary"])
                p["arxiv"] = p.get("arxiv") or aid
                p["arxiv_versions_updated"] = a.get("updated")
                if q not in p["queries"]:
                    p["queries"].append(q)
                continue
            key = f"ax:{aid}"
            if key in pool:
                if q not in pool[key]["queries"]:
                    pool[key]["queries"].append(q)
                continue
            pool[key] = {"key": key, "zbmath_id": None, "title": a["title"], "title_original": "", "authors": a["authors"],
                         "year": a["published"][:4], "venue": a.get("journal_ref") or "arXiv preprint", "doi": a.get("doi") or "",
                         "arxiv": aid, "doc_type": "arxiv", "msc": [], "keywords": [], "language": "English",
                         "review": "", "arxiv_abstract": a["summary"], "refs": [], "queries": [q],
                         "arxiv_primary": a.get("primary_category"), "arxiv_comment": a.get("comment"),
                         "arxiv_versions_updated": a.get("updated")}
    # citation counts (in-pool, from zbMATH resolved references)
    cites = collections.Counter()
    for p in pool.values():
        for rid in set(p.get("refs") or []):
            cites[rid] += 1
    in_pool_ids = {p["zbmath_id"] for p in pool.values() if p.get("zbmath_id")}
    for p in pool.values():
        p["in_pool_citations"] = cites.get(p["zbmath_id"], 0) if p.get("zbmath_id") else 0
        p["stratum"] = stratum(p.get("year"))
        w = [CORE.get(q, 0) for q in p["queries"]] + [ARX.get(q[6:], 0) for q in p["queries"] if q.startswith("arxiv_")]
        p["rel_weight"] = max(w) if w else 0
        p["n_queries"] = len(p["queries"])
    expansion = [(rid, c) for rid, c in cites.most_common() if rid not in in_pool_ids and c >= min_cites]
    with open(os.path.join(out, "pool.jsonl"), "w") as f:
        for p in pool.values():
            q = dict(p)
            q.pop("refs", None)
            q["n_refs_resolved"] = len(p.get("refs") or [])
            f.write(json.dumps(q, ensure_ascii=False) + "\n")
    json.dump({str(k): v for k, v in cites.items()}, open(os.path.join(out, "citation_counts.json"), "w"))
    with open(os.path.join(out, "expansion_ids.txt"), "w") as f:
        for rid, c in expansion:
            f.write(f"{rid}\t{c}\n")
    # citing edges (for knowledge graph): only edges whose both ends are in pool
    with open(os.path.join(out, "citation_edges.tsv"), "w") as f:
        for p in pool.values():
            if p.get("zbmath_id"):
                for rid in set(p.get("refs") or []):
                    f.write(f"{p['zbmath_id']}\t{rid}\n")
    st = collections.Counter(p["stratum"] for p in pool.values())
    print(f"pool={len(pool)} zb={sum(1 for p in pool.values() if p.get('zbmath_id'))} arxiv_only={sum(1 for k in pool if k.startswith('ax:'))} "
          f"expansion_candidates={len(expansion)} strata={dict(sorted(st.items()))}")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 6)
