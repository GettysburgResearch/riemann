#!/usr/bin/env python3
"""Materialize workflow agent results into the archive files later stages expect.

Some subagent file writes are refused by the harness ("return findings as text"), so each agent's
returned value (journal.jsonl) is rendered to the expected markdown path if that file does not exist.
Files written this way start with a provenance line naming the workflow run and agent label.
Usage: python3 materialize_results.py WORKFLOWS_DIR ARCHIVE_ROOT [--watch]
"""
import json, os, sys, time

RUNS = {
    "wf_724f016e-c10": "campaigns",
    "wf_11b6c7f8-a9a": "quasi_rh",
    "wf_ef96aa0a-8e6": "claims_2026",
}

def md_claims(rows, keys):
    out = []
    for r in rows:
        out.append("- " + " | ".join(f"**{k}:** {str(r.get(k, '')).strip()}" for k in keys if r.get(k) not in (None, "")))
    return "\n".join(out)

def render(kind, label, res, root):
    """Return (relative_path, markdown) or None."""
    prov = f"<!-- materialized from workflow result: {kind} / {label} -->\n"
    if kind == "campaigns":
        stage, k = label.split(":", 1)
        d = f"proposals/independent_campaigns/{k}"
        if stage == "inv" and isinstance(res, dict):
            body = [f"# {k} — investigator report (materialized from structured return)\n",
                    "## Investigator notes / header\n", str(res.get("report_path", "")), "\n## Claims\n",
                    md_claims(res.get("claims", []), ["id", "status", "statement", "evidence", "prior_art"]),
                    "\n## Failed attempts and negative results\n", "\n".join(f"- {x}" for x in res.get("failed_attempts", [])),
                    "\n## Code\n", "\n".join(f"- `{x}`" for x in res.get("code_paths", [])),
                    "\n## Open questions\n", "\n".join(f"- {x}" for x in res.get("open_questions", []))]
            return f"{d}/REPORT.md", prov + "\n".join(body)
        if stage == "skeptic" and isinstance(res, dict):
            body = [f"# {k} — skeptic review (materialized)\n", "## Verdicts\n",
                    md_claims(res.get("verdicts", []), ["claim_id", "verdict", "reasoning", "independent_evidence"]),
                    "\n## General issues\n", "\n".join(f"- {x}" for x in res.get("general_issues", [])),
                    f"\n\n_Reviewer note on file path:_ {res.get('review_path', '')}"]
            return f"{d}/SKEPTIC_REVIEW.md", prov + "\n".join(body)
        if stage == "adjudicate" and isinstance(res, dict):
            body = [f"# {k} — adjudicated final claims (materialized)\n", f"**Headline.** {res.get('headline', '')}\n",
                    md_claims(res.get("final_claims", []), ["id", "final_status", "statement", "significance", "next_step"]),
                    f"\n\n_Adjudicator note on file path:_ {res.get('final_report_path', '')}"]
            return f"{d}/FINAL.md", prov + "\n".join(body)
    if kind == "quasi_rh":
        d = "audits/quasi_rh"
        if label == "map" and isinstance(res, dict):
            st = "\n".join(f"- **{s.get('label')}** (line {s.get('line')}, {s.get('kind')}{', imported' if s.get('imported') else ''}): {s.get('statement')} — depends on: {', '.join(s.get('depends_on') or [])}" for s in res.get("statements", []))
            body = ["# Quasi-RH (11/12) — proof architecture (materialized)\n", "## Load-bearing steps\n",
                    "\n".join(f"{i}. {x}" for i, x in enumerate(res.get("load_bearing_steps", []), 1)),
                    "\n## Imported results\n", "\n".join(f"- {x}" for x in res.get("imported_results", [])),
                    "\n## Numbered statements and dependencies\n", st, f"\n\n_Mapper note:_ {res.get('report_path', '')}"]
            return f"{d}/ARCHITECTURE.md", prov + "\n".join(body)
        if label.startswith("audit:") and isinstance(res, dict):
            s = label.split(":", 1)[1]
            body = [f"# Quasi-RH (11/12) — Level-2 audit of {s} (materialized)\n", "## Checks done\n",
                    "\n".join(f"- {x}" for x in res.get("checks_done", [])), "\n## Numeric checks\n",
                    md_claims(res.get("numeric_checks", []), ["identity", "range", "result", "code_path"]),
                    "\n## Findings\n", md_claims(res.get("findings", []), ["id", "classification", "severity_if_real", "location", "claim", "witness_or_reasoning"]),
                    f"\n\n_Auditor note:_ {res.get('report_path', '')}"]
            return f"{d}/audit_{s}.md", prov + "\n".join(body)
        for pre, suf in (("advocate:", "_advocate.md"), ("skeptic:", "_skeptic.md")):
            if label.startswith(pre):
                fid = label.split(":", 1)[1]
                return f"{d}/adversarial/{fid}{suf}", prov + f"# {pre[:-1].title()} — {fid}\n\n" + (res if isinstance(res, str) else json.dumps(res, indent=1))
        if label.startswith("adjudicate:") and isinstance(res, dict):
            fid = label.split(":", 1)[1]
            return f"{d}/adversarial/{fid}_adjudication.md", prov + f"# Adjudication — {fid}\n\n**Final classification:** {res.get('final_classification')}\n\n**Public characterization allowed:** {res.get('public_characterization_allowed')}\n\n{res.get('rationale')}\n"
        if label == "dossier":
            return f"{d}/DOSSIER.md", prov + (res if isinstance(res, str) else json.dumps(res, indent=1))
    if kind == "claims_2026":
        parts = label.split(":")
        if parts[0] == "map":
            return f"audits/claims_2026/{parts[1]}/ARCHITECTURE.md", prov + (res if isinstance(res, str) else json.dumps(res, indent=1))
        if parts[0] == "audit" and isinstance(res, dict):
            body = [f"# {parts[1]} — Level-2 audit part {parts[2]} (materialized)\n", "## Checks done\n",
                    "\n".join(f"- {x}" for x in res.get("checks_done", [])), "\n## Findings\n",
                    md_claims(res.get("findings", []), ["id", "classification", "severity_if_real", "location", "claim", "witness_or_reasoning"]),
                    f"\n\n_Auditor note:_ {res.get('report_path', '')}"]
            return f"audits/claims_2026/{parts[1]}/audit_part{parts[2]}.md", prov + "\n".join(body)
        if parts[0] == "adj":
            return f"audits/claims_2026/{parts[1]}/adjudication_{parts[2]}.md", prov + (res if isinstance(res, str) else json.dumps(res, indent=1))
        if parts[0] == "dossier":
            return f"audits/claims_2026/{parts[1]}/DOSSIER.md", prov + (res if isinstance(res, str) else json.dumps(res, indent=1))
    return None

def once(wdir, root, done):
    for run, kind in RUNS.items():
        j = os.path.join(wdir, run, "journal.jsonl")
        if not os.path.exists(j):
            continue
        labels = {}
        for line in open(j):
            try:
                x = json.loads(line)
            except Exception:
                continue
            if x.get("type") == "started":
                labels[x["key"]] = x.get("label")
            elif x.get("type") == "result":
                lab = labels.get(x["key"])
                if not lab or (run, lab) in done:
                    continue
                r = render(kind, lab, x.get("result"), root)
                done.add((run, lab))
                if r:
                    path = os.path.join(root, r[0])
                    os.makedirs(os.path.dirname(path), exist_ok=True)
                    if not os.path.exists(path) or os.path.getsize(path) == 0:
                        open(path, "w").write(r[1] + "\n")
                        print("wrote", r[0], flush=True)

if __name__ == "__main__":
    wdir, root = sys.argv[1], sys.argv[2]
    done = set()
    if "--watch" in sys.argv:
        while True:
            once(wdir, root, done)
            time.sleep(4)
    else:
        once(wdir, root, done)
