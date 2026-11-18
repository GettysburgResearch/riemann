#!/usr/bin/env python3
"""Consolidate frontier-ledger and repository-bridge workflow results (draft + independent verification)
into archive files.

Usage: python3 consolidate_ledger_bridge.py WORKFLOWS_DIR ARCHIVE_ROOT LEDGER_RUN BRIDGE_RUN
Writes frontiers/ledger.jsonl, frontiers/records_ledger.md, frontiers/research_programs.md,
connections/repository_bridge.jsonl, connections/repository_bridge.md.
"""
import json, os, sys, collections

def results(path):
    labels, out = {}, []
    for line in open(path):
        x = json.loads(line)
        if x.get("type") == "started":
            labels[x["key"]] = x.get("label")
        elif x.get("type") == "result":
            out.append((labels.get(x["key"]), x["result"]))
    return out

def esc(s):
    return str(s or "").replace("|", "\\|").replace("\n", " ").strip()

def ledger(wdir, root, run):
    R = results(os.path.join(wdir, run, "journal.jsonl"))
    drafts = {lab.split(":")[1]: r for lab, r in R if lab and lab.startswith("draft:")}
    verifs = {lab.split(":")[1]: r for lab, r in R if lab and lab.startswith("verify:")}
    rows, md, prog = [], [], []
    md.append("# Frontier records ledger\n")
    md.append("```text\nStatus: IMPORTED (literature records) with independent re-verification verdicts\nScope: classical zeta unless an entry says otherwise; search cutoff 2026-11-17\nExact sources or dependencies: per entry (source + location)\nWhat was actually run: one drafting agent per area reading primary sources; one independent skeptic per area re-checking each entry\nSmallest remaining gap: entries marked unverifiable / superseded / corrected below\n```\n")
    md.append("Each entry gives the drafting agent's evidence level and the independent verifier's verdict. **Unrefereed and AI-generated claims are labelled as such; a verdict of `confirmed_fulltext` means the statement matches the source, not that the source's proof was checked.**\n")
    for area in sorted(drafts):
        d = drafts[area]
        v = {x["entry_id"]: x for x in (verifs.get(area) or {}).get("verdicts", [])}
        md.append(f"\n## {area}: {esc(d.get('area'))[:200]}\n")
        md.append("| ID | Quantity | Current statement / value | Status | Source (location) | Evidence | Verifier verdict |\n|---|---|---|---|---|---|---|")
        for k, e in enumerate(d.get("entries", []), 1):
            lid = f"LED-{area}-{k}"
            vv = v.get(e.get("id"), {})
            src = e.get("source", {})
            rows.append({"led_id": lid, "area": area, "draft_id": e.get("id"), **{x: e.get(x) for x in ("quantity", "statement", "value", "status", "conditional_on", "location", "evidence_level", "history", "caveats")},
                         "source": src, "verification": {k2: vv.get(k2) for k2 in ("verdict", "checked_against", "correction", "notes")}})
            ident = src.get("arxiv") or src.get("doi") or ""
            md.append(f"| {lid} | {esc(e.get('quantity'))} | {esc(e.get('value'))}: {esc(e.get('statement'))[:500]} | {esc(e.get('status'))}{(' (cond. ' + esc(e.get('conditional_on'))[:80] + ')') if e.get('conditional_on') else ''} | {esc(src.get('authors'))} {esc(src.get('year'))}, *{esc(src.get('title'))[:90]}* {esc(ident)} ({esc(e.get('location'))[:80]}) | {esc(e.get('evidence_level'))} | {esc(vv.get('verdict', 'not verified'))}{(': ' + esc(vv.get('correction'))[:300]) if vv.get('correction') else ''} |")
        if verifs.get(area):
            md.append(f"\n**Verifier critique.** {esc(verifs[area].get('frontier_critique'))}\n")
            if verifs[area].get("missing_records"):
                md.append("**Missing records flagged by verifier.** " + "; ".join(esc(x) for x in verifs[area]["missing_records"]) + "\n")
        f = d.get("frontier", {})
        prog.append(f"\n## {area}\n")
        for key, lab in [("best_established", "1. Best established theorem"), ("historical_improvement", "2. Historical improvement"), ("bottleneck", "3. Exact bottleneck"),
                         ("bottleneck_type", "4. Bottleneck type"), ("negative_results", "5. What negative results rule out"), ("possible_external_ingredients", "6. Possible external ingredients"),
                         ("meaningful_incremental_breakthrough", "7. Meaningful incremental breakthrough"), ("next_concrete_step", "8. Next concrete step")]:
            prog.append(f"**{lab}.** {esc(f.get(key))}\n")
        if d.get("open_questions"):
            prog.append("**Open questions.**\n" + "\n".join(f"- {esc(q)}" for q in d["open_questions"]) + "\n")
        if verifs.get(area):
            prog.append(f"*Independent critique of this frontier analysis:* {esc(verifs[area].get('frontier_critique'))}\n")
        prog.append("*Primary sources opened by the analyst:* " + "; ".join(esc(s) for s in d.get("sources_read", [])) + "\n")
    os.makedirs(os.path.join(root, "frontiers"), exist_ok=True)
    with open(os.path.join(root, "frontiers", "ledger.jsonl"), "w") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    open(os.path.join(root, "frontiers", "records_ledger.md"), "w").write("\n".join(md) + "\n")
    hdr = ["# Research programmes: frontier analysis by area\n",
           "```text\nStatus: SYNTHESIS of IMPORTED results; analysis is the drafting agent's, critique is an independent verifier's\nScope: per area\nExact sources or dependencies: frontiers/records_ledger.md and the sources listed per area\nWhat was actually run: literature reading by agents; no new theorems\nSmallest remaining gap: see each area's critique\n```\n",
           "This file answers, for each area, the eight frontier questions of the Observatory brief (best theorem, improvement history, bottleneck and its type, negative results, external ingredients, meaningful incremental breakthrough, next step). See `frontiers/records_ledger.md` for the sourced records.\n"]
    open(os.path.join(root, "frontiers", "research_programs.md"), "w").write("\n".join(hdr + prog) + "\n")
    vc = collections.Counter(r["verification"]["verdict"] for r in rows)
    print("ledger areas", len(drafts), "verified areas", len(verifs), "entries", len(rows), dict(vc))

def bridge(wdir, root, run):
    R = results(os.path.join(wdir, run, "journal.jsonl"))
    drafts = {lab.split(":")[1]: r for lab, r in R if lab and lab.startswith("bridge:")}
    verifs = {lab.split(":")[1]: r for lab, r in R if lab and lab.startswith("verify:")}
    rows, md = [], []
    md.append("# Repository–literature bridge\n")
    md.append("```text\nStatus: IMPORTED literature pointers with independent verification; no change to integrated repository results is proposed here\nScope: the integrated programmes summarized in research/integrated/CURRENT_RESULTS.md (host repository)\nExact sources or dependencies: per item\nWhat was actually run: one analyst per programme (reading repository files + literature) and one independent verifier per programme\nSmallest remaining gap: items marked unverifiable / relation_overstated; repository maintainers should review before citing\n```\n")
    md.append("This bridge maps each repository programme to (a) prior art for its retained statements, (b) known obstructions, (c) transplantable tools. Per AGENTS.md, any consequence for repository statements is a **proposal for the repository's own review**; repository acceptance never implied external novelty, and this file does not change any repository status.\n")
    for prog in sorted(drafts):
        d = drafts[prog]
        v = {x["item_id"]: x for x in (verifs.get(prog) or {}).get("verdicts", [])}
        md.append(f"\n## {prog}\n\n**Programme scope examined:** {esc(d.get('programme'))[:400]}\n")
        md.append("### Prior art\n\n| ID | Repository statement | Literature result | Citation | Relation | Evidence | Verifier |\n|---|---|---|---|---|---|---|")
        for k, p in enumerate(d.get("prior_art", []), 1):
            bid = f"BRG-{prog}-P{k}"
            vv = v.get(p.get("id"), {})
            rows.append({"brg_id": bid, "programme": prog, "kind": "prior_art", **p, "verification": vv})
            md.append(f"| {bid} | {esc(p.get('repo_statement'))[:300]} | {esc(p.get('literature_result'))[:400]} | {esc(p.get('citation'))[:250]} | {esc(p.get('relation'))} | {esc(p.get('evidence_level'))} | {esc(vv.get('verdict', 'not verified'))}{(': ' + esc(vv.get('correction'))[:250]) if vv.get('correction') else ''} |")
        md.append("\n### Known obstructions\n")
        for k, o in enumerate(d.get("known_obstructions", []), 1):
            bid = f"BRG-{prog}-O{k}"
            vv = v.get(o.get("id"), {})
            rows.append({"brg_id": bid, "programme": prog, "kind": "obstruction", **o, "verification": vv})
            md.append(f"- **{bid}** {esc(o.get('obstruction'))} — *{esc(o.get('citation'))}*. How it constrains: {esc(o.get('how_it_constrains'))} [{esc(o.get('evidence_level'))}; verifier: {esc(vv.get('verdict', 'not verified'))}]")
        md.append("\n### Transplantable tools\n")
        for k, t in enumerate(d.get("transplantable_tools", []), 1):
            bid = f"BRG-{prog}-T{k}"
            rows.append({"brg_id": bid, "programme": prog, "kind": "tool", **t})
            md.append(f"- **{bid}** {esc(t.get('tool'))} (*{esc(t.get('citation'))}*). Target gap: {esc(t.get('target_gap'))}. Next step: {esc(t.get('precise_next_step'))}. Risk: {esc(t.get('risk'))}")
        md.append(f"\n### Novelty assessment\n\n{esc(d.get('novelty_assessment'))}\n")
        md.append("### Recommended actions\n\n" + "\n".join(f"- {esc(a)}" for a in d.get("recommended_actions", [])) + "\n")
        if verifs.get(prog):
            md.append(f"### Independent verifier\n\n{esc(verifs[prog].get('overall_critique'))}\n")
            if verifs[prog].get("missed_prior_art"):
                md.append("**Missed prior art flagged:**\n" + "\n".join(f"- {esc(m)}" for m in verifs[prog]["missed_prior_art"]) + "\n")
    os.makedirs(os.path.join(root, "connections"), exist_ok=True)
    with open(os.path.join(root, "connections", "repository_bridge.jsonl"), "w") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    open(os.path.join(root, "connections", "repository_bridge.md"), "w").write("\n".join(md) + "\n")
    vc = collections.Counter((r.get("verification") or {}).get("verdict") for r in rows if r["kind"] != "tool")
    print("bridge programmes", len(drafts), "verified", len(verifs), "items", len(rows), dict(vc))

if __name__ == "__main__":
    wdir, root, lrun, brun = sys.argv[1:5]
    ledger(wdir, root, lrun)
    bridge(wdir, root, brun)
