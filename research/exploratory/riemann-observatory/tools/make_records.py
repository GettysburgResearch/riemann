#!/usr/bin/env python3
"""Generate corpus files and per-paper records from candidates + triage + Level-1 outputs.

Usage: python3 make_records.py WORKDIR ARCHIVE_ROOT
WORKDIR must contain: candidates.jsonl, triage.jsonl (one item per cand_id), selection.json
  ({"selected": [cand_id,...]} in PAPER order), optional l1.jsonl (L1 records keyed by cand_id),
  optional crossref_updates.jsonl, optional seeds.jsonl.
Writes ARCHIVE_ROOT/corpus/{bibliography.csv,bibliography.jsonl,selection_decisions.csv,access_and_audit_manifest.csv},
ARCHIVE_ROOT/papers/PAPER-####.md, ARCHIVE_ROOT/theorems/{theorems.jsonl,proof_dependencies.jsonl}.
"""
import csv, json, os, sys, re

def load_jsonl(p):
    return [json.loads(l) for l in open(p)] if os.path.exists(p) else []

def md_escape(s):
    return (s or "").replace("\r", "").strip()

def zb_link(c):
    return f"https://zbmath.org/?q=an:{c['zbl']}" if c.get("zbl") else (c.get("zbmath_url") or "")

def main(wd, root):
    cands = {c["cand_id"]: c for c in load_jsonl(os.path.join(wd, "candidates.jsonl"))}
    triage = {t["cand_id"]: t for t in load_jsonl(os.path.join(wd, "triage.jsonl"))}
    l1 = {r["cand_id"]: r for r in load_jsonl(os.path.join(wd, "l1.jsonl"))}
    upd = {u["doi"].lower(): u for u in load_jsonl(os.path.join(wd, "crossref_updates.jsonl"))}
    seeds = {s["seed_id"]: s for s in load_jsonl(os.path.join(wd, "seeds.jsonl"))}
    sel = json.load(open(os.path.join(wd, "selection.json")))
    selected = sel["selected"]
    pid = {cid: f"PAPER-{i:04d}" for i, cid in enumerate(selected, 1)}
    os.makedirs(os.path.join(root, "papers"), exist_ok=True)
    os.makedirs(os.path.join(root, "corpus"), exist_ok=True)
    os.makedirs(os.path.join(root, "theorems"), exist_ok=True)
    bib_rows, man_rows, thm_rows, dep_rows = [], [], [], []
    for cid in selected:
        c, t, r = cands[cid], triage.get(cid, {}), l1.get(cid)
        p = pid[cid]
        level = "L0"
        if t.get("main_result_index") and t.get("basis") in ("arxiv_abstract", "zbmath_review", "both"):
            level = "L0+"
        if r and r.get("access", {}).get("status") in ("fulltext_read", "partial_fulltext"):
            level = "L1" if r["access"]["status"] == "fulltext_read" else "L1-partial"
        fams = sorted(set((r or {}).get("families") or t.get("families") or []))
        doi = (c.get("doi") or "").strip()
        u = upd.get(doi.lower()) if doi else None
        access_url = (r or {}).get("access", {}).get("source_url") or (f"https://arxiv.org/abs/{c['arxiv']}" if c.get("arxiv") else (f"https://doi.org/{doi}" if doi else ""))
        rec = {"paper_id": p, "cand_id": cid, "title": c.get("title"), "title_original": c.get("title_original"),
               "authors": c.get("authors"), "year": c.get("year"), "stratum": c.get("stratum"), "venue": c.get("venue"),
               "doc_type": c.get("doc_type"), "doi": doi, "arxiv": c.get("arxiv", ""), "zbmath_id": c.get("zbmath_id"),
               "zbl": c.get("zbl"), "msc": c.get("msc", []), "language": c.get("language"), "families": fams,
               "work_type": t.get("work_type"), "relevance": t.get("relevance"), "selection_score": c.get("score"),
               "in_pool_citations": c.get("in_pool_citations", 0), "seed_lists": c.get("seed_ids", []),
               "access": {"url": access_url, "fulltext_status": (r or {}).get("access", {}).get("status", "not_attempted")},
               "audit_level": level, "record_path": f"papers/{p}.md",
               "corrections": (u or {}).get("updates", []), "is_referenced_by_count": (u or {}).get("is_referenced_by_count")}
        bib_rows.append(rec)
        man_rows.append({"paper_id": p, "title": (c.get("title") or "")[:120], "year": c.get("year"), "doi": doi,
                         "arxiv": c.get("arxiv", ""), "zbl": c.get("zbl") or "", "fulltext_url": access_url,
                         "fulltext_status": rec["access"]["fulltext_status"], "audit_level": level,
                         "content_basis": ("full text" if level.startswith("L1") else (t.get("basis") or "metadata"))})
        # theorems (only from works whose text was actually read)
        if r and r.get('access', {}).get('status') in ('fulltext_read', 'partial_fulltext'):
            for k, th in enumerate(r.get("main_results") or [], 1):
                tid = f"THM-{p}-{k}"
                thm_rows.append({"thm_id": tid, "paper_id": p, "kind": th.get("kind"), "label_in_source": th.get("label_in_source"),
                                 "statement": th.get("statement"), "hypotheses": th.get("hypotheses", []), "scope": th.get("scope"),
                                 "conditional_on": th.get("conditional_on", []), "location": th.get("location"),
                                 "evidence_level": "fulltext_read" if level == "L1" else "partial_fulltext"})
            for k, lm in enumerate(r.get("principal_lemmas") or [], 1):
                tid = f"THM-{p}-L{k}"
                thm_rows.append({"thm_id": tid, "paper_id": p, "kind": "lemma", "label_in_source": lm.get("label_in_source"),
                                 "statement": lm.get("statement"), "role": lm.get("role"), "location": lm.get("location"),
                                 "evidence_level": "fulltext_read" if level == "L1" else "partial_fulltext"})
            for k, e in enumerate(r.get("dependency_edges") or [], 1):
                dep_rows.append({"edge_id": f"DEP-{p}-{k}", "paper_id": p, "from": e.get("from"), "to": e.get("to"), "relation": e.get("relation")})
        # markdown record
        L = []
        L.append(f"# {p} — {md_escape(c.get('title'))}\n")
        if c.get("title_original") and c.get("title_original") != c.get("title"):
            L.append(f"*Original title:* {md_escape(c.get('title_original'))}\n")
        L.append("| Field | Value |\n|---|---|")
        L.append(f"| Authors | {'; '.join(c.get('authors') or []) or 'not listed in index'} |")
        L.append(f"| Year / stratum | {c.get('year')} / {c.get('stratum')} |")
        L.append(f"| Venue | {md_escape(c.get('venue'))} |")
        ids = []
        if c.get("zbl"):
            ids.append(f"zbMATH [{c['zbl']}]({zb_link(c)})")
        if doi:
            ids.append(f"DOI [{doi}](https://doi.org/{doi})")
        if c.get("arxiv"):
            ids.append(f"arXiv [{c['arxiv']}](https://arxiv.org/abs/{c['arxiv']})")
        L.append(f"| Identifiers | {' · '.join(ids) or 'none resolved'} |")
        L.append(f"| MSC | {', '.join(c.get('msc') or [])} |")
        L.append(f"| Families | {', '.join(fams)} |")
        L.append(f"| Work type | {t.get('work_type', '')} |")
        L.append(f"| Evidence level of this record | **{level}** |")
        L.append(f"| Full text | {rec['access']['fulltext_status']} {('— ' + access_url) if access_url else ''} |")
        L.append(f"| Selection | score {c.get('score')}, in-pool citations {c.get('in_pool_citations', 0)}, seed lists {len(c.get('seed_ids', []))}, triage relevance {t.get('relevance')} |")
        if u and u.get("updates"):
            L.append(f"| Published updates (Crossref) | " + "; ".join(f"{x.get('update_type')} {x.get('doi')}" for x in u["updates"]) + " |")
        L.append("")
        if r and level.startswith("L1"):
            L.append("## Mathematical content (Level 1: full text read)\n")
            L.append(f"**Research question.** {md_escape(r.get('research_question'))}\n")
            if r.get("historical_motivation"):
                L.append(f"**Historical motivation.** {md_escape(r.get('historical_motivation'))}\n")
            L.append("### Main results\n")
            for k, th in enumerate(r.get("main_results") or [], 1):
                cond = f" *Conditional on:* {', '.join(th.get('conditional_on') or [])}." if th.get("conditional_on") else ""
                L.append(f"- **THM-{p}-{k}** ({th.get('label_in_source')}, {th.get('kind')}, scope: {th.get('scope')}; {th.get('location')}). {md_escape(th.get('statement'))}{cond}")
            if r.get("key_definitions"):
                L.append("\n### Key definitions\n")
                L += [f"- {md_escape(d)}" for d in r["key_definitions"]]
            if r.get("principal_lemmas"):
                L.append("\n### Principal lemmas\n")
                for k, lm in enumerate(r["principal_lemmas"], 1):
                    L.append(f"- **THM-{p}-L{k}** ({lm.get('label_in_source')}; {lm.get('location')}). {md_escape(lm.get('statement'))} — *Role:* {md_escape(lm.get('role'))}")
            L.append(f"\n### Proof architecture\n\n{md_escape(r.get('proof_architecture'))}\n")
            if r.get("dependency_edges"):
                L.append("Dependency edges: " + "; ".join(f"{e.get('from')} → {e.get('to')} ({e.get('relation')})" for e in r["dependency_edges"]) + "\n")
            if r.get("imported_results"):
                L.append("**Imported results.** " + "; ".join(md_escape(x) for x in r["imported_results"]) + "\n")
            L.append("**Techniques.** " + "; ".join(md_escape(x) for x in r.get("techniques") or []) + "\n")
            L.append("## Context and interpretation\n")
            L.append(f"**Importance and obstacle overcome.** {md_escape(r.get('importance_and_obstacle_overcome'))}\n")
            L.append(f"**Relation to prior work.** {md_escape(r.get('relation_to_prior_work'))}\n")
            L.append(f"**Limitations and open questions.** {md_escape(r.get('limitations_and_open_questions'))}\n")
            if r.get("hidden_ideas"):
                L.append(f"**Ideas in remarks/appendices/abandoned paths.** {md_escape(r.get('hidden_ideas'))}\n")
            rp = r.get("research_potential") or {}
            L.append("## Research potential\n")
            for key, lab in [("weakenable_hypotheses", "Hypotheses that might be weakened"), ("generalizations", "Generalizations"),
                             ("candidate_connections", "Candidate connections"), ("reusable_lemmas", "Reusable lemmas"),
                             ("experiments", "Possible experiments"), ("risks_barriers", "Risks / barriers")]:
                if rp.get(key):
                    L.append(f"- **{lab}.** {md_escape(rp[key])}")
            L.append(f"\n## Audit notes (Level 1 reader)\n\n{md_escape(r.get('audit_notes'))}\n")
            L.append("*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*\n")
        else:
            L.append("## Content (index-level record — the paper itself was NOT read)\n")
            basis = t.get("basis", "metadata")
            L.append(f"*Basis:* {basis}. This summary is derived from index content (arXiv abstract and/or zbMATH review) or, where marked, the curator's unverified recollection. It is not an audit.\n")
            if t.get("main_result_index"):
                L.append(f"**Main result (as stated in index content).** {md_escape(t.get('main_result_index'))}\n")
            if t.get("techniques"):
                L.append("**Techniques.** " + "; ".join(t["techniques"]) + "\n")
            if t.get("research_potential"):
                L.append(f"**Research potential (curator).** {md_escape(t.get('research_potential'))}\n")
            for sid in c.get("seed_ids", [])[:2]:
                s = seeds.get(sid)
                if s:
                    L.append(f"**Expert seed note ({s.get('family_list', s.get('families'))}; unverified recollection).** {md_escape(s.get('key_contribution'))}\n")
        L.append("## Provenance\n")
        L.append(f"- Candidate `{cid}`; harvest queries: {', '.join(c.get('queries') or []) or 'seed/expansion'}.")
        L.append(f"- Triage decision: {t.get('decision')} — {md_escape(t.get('reason'))}")
        if t.get("l0_source_url"):
            sec = " (secondary source only; authoritative bibliographic source still to be recorded)" if "wikipedia.org" in t["l0_source_url"] else ""
            L.append(f"- Manual Level-0 verification source: {t['l0_source_url']}{sec}")
        if t.get("l0_bibliographic_correction"):
            L.append(f"- Bibliographic correction noted at Level 0: {md_escape(t['l0_bibliographic_correction'])}")
        if sel.get("notes", {}).get(cid, "").startswith("curator override"):
            L.append(f"- Selection: {sel['notes'][cid]}")
        L.append(f"- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.")
        open(os.path.join(root, "papers", f"{p}.md"), "w").write("\n".join(L) + "\n")
    with open(os.path.join(root, "corpus", "bibliography.jsonl"), "w") as f:
        for rec in bib_rows:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    cols = ["paper_id", "cand_id", "year", "stratum", "families", "work_type", "relevance", "audit_level", "title", "authors", "venue", "doi", "arxiv", "zbl", "in_pool_citations", "selection_score"]
    with open(os.path.join(root, "corpus", "bibliography.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for rec in bib_rows:
            w.writerow([";".join(rec[k]) if isinstance(rec.get(k), list) else rec.get(k, "") for k in cols])
    with open(os.path.join(root, "corpus", "access_and_audit_manifest.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(man_rows[0].keys()))
        w.writeheader()
        w.writerows(man_rows)
    # selection decisions for every candidate
    with open(os.path.join(root, "corpus", "selection_decisions.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["cand_id", "paper_id", "decision", "reject_reason", "relevance", "families", "year", "title", "score", "in_pool_citations", "reason"])
        for cid, c in cands.items():
            t = triage.get(cid, {})
            dec = "selected" if cid in pid else ("not_triaged" if not t else ("rejected" if t.get("decision") == "reject" else "not_selected_" + (t.get("decision") or "")))
            w.writerow([cid, pid.get(cid, ""), dec, t.get("reject_reason", ""), t.get("relevance", ""), ";".join(t.get("families") or []),
                        c.get("year"), (c.get("title") or "")[:200], c.get("score"), c.get("in_pool_citations", 0), (t.get("reason") or sel.get("notes", {}).get(cid, ""))[:300]])
    with open(os.path.join(root, "theorems", "theorems.jsonl"), "w") as f:
        for x in thm_rows:
            f.write(json.dumps(x, ensure_ascii=False) + "\n")
    with open(os.path.join(root, "theorems", "proof_dependencies.jsonl"), "w") as f:
        for x in dep_rows:
            f.write(json.dumps(x, ensure_ascii=False) + "\n")
    lv = {}
    for rec in bib_rows:
        lv[rec["audit_level"]] = lv.get(rec["audit_level"], 0) + 1
    print("papers", len(bib_rows), "levels", lv, "theorems", len(thm_rows), "deps", len(dep_rows))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
