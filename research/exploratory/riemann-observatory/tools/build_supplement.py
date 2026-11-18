#!/usr/bin/env python3
"""Append supplementary candidates (verified seeds not yet triaged, recent-literature scan entries,
unindexed classics needing manual Level-0 verification) WITHOUT renumbering existing CAND ids.

Usage: python3 build_supplement.py SCR ROUND_TAG [SEED_FAMILY_FILTER]
Reads SCR/cand/candidates.jsonl, SCR/pool/pool.jsonl, SCR/seeds/{seeds,seed_matches}.jsonl,
ARCHIVE/corpus/recent_2024_2026_scan.jsonl. Rewrites SCR/cand/candidates.jsonl (attaching seed_ids /
recent-scan flags to existing candidates) and writes SCR/cand/supp_<ROUND>/batch_###.jsonl.
"""
import json, os, re, sys

ARCH = "/home/user/riemann/research/exploratory/riemann-observatory"
sys.path.insert(0, os.path.join(ARCH, "tools"))
from build_pool import stratum

def jl(p):
    return [json.loads(l) for l in open(p)] if os.path.exists(p) else []

def main(scr, tag, famfilter=None):
    C = jl(f"{scr}/cand/candidates.jsonl")
    bykey = {c["key"]: c for c in C}
    pool = {p["key"]: p for p in jl(f"{scr}/pool/pool.jsonl")}
    seeds = {s["seed_id"]: s for s in jl(f"{scr}/seeds/seeds.jsonl")}
    matches = {m["seed_id"]: m for m in jl(f"{scr}/seeds/seed_matches.jsonl")}
    scan = jl(f"{ARCH}/corpus/recent_2024_2026_scan.jsonl")
    maxid = max(int(c["cand_id"].split("-")[1]) for c in C)
    new = {}
    def newcand(key, base):
        nonlocal maxid
        if key in bykey or key in new:
            return bykey.get(key) or new[key]
        maxid += 1
        base.update({"key": key, "cand_id": f"CAND-{maxid:05d}", "supplement_round": tag})
        base.setdefault("stratum", stratum(base.get("year")))
        base.setdefault("score", None)
        base.setdefault("in_pool_citations", 0)
        base.setdefault("seed_ids", [])
        new[key] = base
        return base
    for sid, s in seeds.items():
        if famfilter and s["seed_family_list"] not in famfilter.split(","):
            continue
        m = matches.get(sid, {"status": "unverified"})
        if m["status"] == "verified":
            key = m.get("pool_key") or (f"zb:{m['zbmath_id']}" if m.get("zbmath_id") else None) or (f"ax:{m['arxiv']}" if m.get("arxiv") else None) or (f"doi:{m['doi'].lower()}" if m.get("doi") else None)
            if key in pool:
                c = newcand(key, dict(pool[key]))
            else:
                c = newcand(key, {"zbmath_id": m.get("zbmath_id"), "zbl": m.get("zbl"), "title": s["title"], "title_original": s["title"],
                                  "authors": s["authors"], "year": str(s.get("year")), "venue": m.get("venue") or s.get("venue", ""),
                                  "doi": m.get("doi") or s.get("doi", ""), "arxiv": m.get("arxiv") or s.get("arxiv", ""), "doc_type": "seed",
                                  "msc": [], "keywords": [], "review": "", "queries": [], "l0_source": m.get("source")})
        else:
            key = "seedonly:" + re.sub(r"[^a-z0-9]", "", (s["title"] + str(s.get("year"))).lower())[:60]
            c = newcand(key, {"title": s["title"], "title_original": s["title"], "title_en": s.get("title_en", ""), "authors": s["authors"],
                              "year": str(s.get("year")), "venue": s.get("venue", ""), "doi": s.get("doi", ""), "arxiv": s.get("arxiv", ""),
                              "doc_type": "seed", "msc": [], "keywords": [], "review": "", "queries": [], "needs_manual_L0": True})
        if sid not in c.setdefault("seed_ids", []):
            c["seed_ids"].append(sid)
    for e in scan:
        ident = e.get("identifier", "")
        if re.match(r"^\d{4}\.\d{4,5}(v\d+)?$", ident):
            aid = re.sub(r"v\d+$", "", ident)
            key = f"ax:{aid}"
            zb = next((k for k, p in pool.items() if p.get("arxiv") and p["arxiv"].startswith(aid)), None)
            key = zb or key
            base = dict(pool[key]) if key in pool else {"title": e["title"], "authors": e.get("authors", []), "year": e.get("date", "")[:4],
                                                          "venue": "arXiv preprint", "doi": "", "arxiv": aid, "doc_type": "arxiv", "msc": [], "keywords": [], "review": "", "queries": []}
        else:
            key = "recent:" + re.sub(r"[^a-z0-9]", "", ident.lower())[:80]
            base = {"title": e["title"], "authors": e.get("authors", []) if isinstance(e.get("authors"), list) else [e.get("authors", "")],
                    "year": e.get("date", "")[:4], "venue": e.get("source_type", ""), "doi": ident if ident.startswith("10.") else "",
                    "arxiv": "", "doc_type": e.get("source_type"), "msc": [], "keywords": [], "review": "", "queries": [], "identifier": ident}
        c = newcand(key, base)
        c["recent_scan"] = {k: e.get(k) for k in ("claim", "status", "lean_claimed", "families", "why_relevant", "source_type", "identifier")}
    # write back
    allc = C + list(new.values())
    with open(f"{scr}/cand/candidates.jsonl", "w") as f:
        for c in allc:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    out = f"{scr}/cand/supp_{tag}"
    os.makedirs(out, exist_ok=True)
    items = list(new.values())
    def compact(c):
        return {"cand_id": c["cand_id"], "title": (c.get("title") or "")[:300], "title_en": c.get("title_en", ""), "authors": (c.get("authors") or [])[:6],
                "year": c.get("year"), "venue": (c.get("venue") or "")[:150], "doi": c.get("doi", ""), "arxiv": c.get("arxiv", ""),
                "identifier": c.get("identifier", ""), "msc": c.get("msc", [])[:6], "in_pool_citations": c.get("in_pool_citations", 0),
                "abstract": (c.get("arxiv_abstract") or "")[:900], "zb_review": (c.get("review") or "")[:900],
                "seed_notes": [{"fam": seeds[s].get("families"), "key": seeds[s].get("key_contribution", "")[:300], "type": seeds[s].get("work_type")} for s in c.get("seed_ids", [])[:2]],
                "recent_scan": c.get("recent_scan"), "needs_manual_L0": bool(c.get("needs_manual_L0"))}
    for b in range(0, len(items), 60):
        with open(f"{out}/batch_{b // 60 + 1:03d}.jsonl", "w") as f:
            for c in items[b:b + 60]:
                f.write(json.dumps(compact(c), ensure_ascii=False) + "\n")
    print("new candidates", len(items), "manual L0", sum(1 for c in items if c.get("needs_manual_L0")),
          "recent", sum(1 for c in items if c.get("recent_scan")), "batches", (len(items) + 59) // 60,
          "existing candidates with seeds", sum(1 for c in C if c.get("seed_ids")))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
