#!/usr/bin/env python3
from pathlib import Path
import csv, json, hashlib, re, sys
from collections import defaultdict, deque

here = Path(__file__).resolve().parent
root = here.parents[1]  # repository root

def fail(msg):
    print("FAIL_FINAL_INTEGRATION:", msg)
    raise SystemExit(1)

def read_tsv(path):
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))

required_root = [
    "README.md", "STATUS.md", "RESULTS.md", "PROOF_GRAPH.md",
    "OPEN_CUTS.md", "REFUTATIONS.md", "COMPUTATIONS.md", "HISTORY.md",
]
for rel in required_root:
    p = root / rel
    if not p.is_file() or p.stat().st_size == 0:
        fail(f"missing front-door file {rel}")

required_release = [
    "FREEZE.json","REVIEW_SOURCES.tsv","CLAIMS.tsv","EDGES.tsv","ALIASES.tsv",
    "FAMILIES.tsv","REFUTATIONS.tsv","COMPUTATIONS.tsv","PR_DISPOSITIONS.tsv",
    "CONFLICTS.tsv","EXTRACTION_PLAN.tsv","FIXES_REQUIRED.md",
    "REVIEWER_D_OPEN_CUTS.md","ISSUE_ARCHAEOLOGY.md","DIRECT_MAIN_SUMMARY.md",
    "LATE_RESEARCH_QUEUE.md","README.md"
]
for rel in required_release:
    p = here / rel
    if not p.is_file() or p.stat().st_size == 0:
        fail(f"missing release file {rel}")

freeze = json.loads((here / "FREEZE.json").read_text(encoding="utf-8"))
if freeze["frozen_main"]["sha"] != "677203992eb0168920365ee45ae9db76bfa97dcf":
    fail("wrong frozen main")
if freeze["frozen_main"]["tree_sha"] != "701d836331ce59c317f6c6ee8bcd26f2c8e872e9":
    fail("wrong frozen main tree")
if freeze["reviewer_d"]["head"] != "06c8ea18ffe20c7efa01b0fdacb8ebea0a2b5b22":
    fail("wrong Reviewer D head")
if freeze["scientific_status"] != "RH_UNPROVED":
    fail("RH status not unproved")
if freeze["research_census_terminal_pr"] != 707:
    fail("wrong research cutoff")

claims = read_tsv(here / "CLAIMS.tsv")
edges = read_tsv(here / "EDGES.tsv")
aliases = read_tsv(here / "ALIASES.tsv")
families = read_tsv(here / "FAMILIES.tsv")
refs = read_tsv(here / "REFUTATIONS.tsv")
comps = read_tsv(here / "COMPUTATIONS.tsv")
prs = read_tsv(here / "PR_DISPOSITIONS.tsv")
conflicts = read_tsv(here / "CONFLICTS.tsv")
extract = read_tsv(here / "EXTRACTION_PLAN.tsv")

expected_counts = {
    "claims":139, "edges":36, "aliases":19, "families":24,
    "refutations":19, "computations":22, "pr_dispositions":333,
    "conflicts":18, "extraction_plan":139,
}
actual_counts = {
    "claims":len(claims), "edges":len(edges), "aliases":len(aliases),
    "families":len(families), "refutations":len(refs),
    "computations":len(comps), "pr_dispositions":len(prs),
    "conflicts":len(conflicts), "extraction_plan":len(extract),
}
if actual_counts != expected_counts:
    fail(f"count mismatch: {actual_counts}")

def unique(rows, key, name):
    vals = [r[key] for r in rows]
    if len(vals) != len(set(vals)):
        fail(f"duplicate {name}")
unique(claims, "semantic_id", "claim ID")
unique(edges, "edge_id", "edge ID")
unique(aliases, "alias_id", "alias ID")
unique(families, "family_id", "family ID")
unique(refs, "refutation_id", "refutation ID")
unique(comps, "computation_id", "computation ID")
unique(conflicts, "conflict_id", "conflict ID")

allowed_claim_verdicts = {
    "VERIFIED","VERIFIED_WITH_FIXES","CONDITIONAL_EXACT",
    "OPEN_SUFFICIENT_FOR_RH","OPEN_RH_EQUIVALENT",
    "GAP_BLOCKED","FALSE","REFUTED_MECHANISM",
    "RETAINED_HEAVY_CERTIFICATE"
}
for row in claims:
    if row["final_verdict"] not in allowed_claim_verdicts:
        fail(f"invalid claim verdict {row['final_verdict']}")
    sha = row["source_head_sha"]
    if not re.fullmatch(r"[0-9a-f]{40}", sha):
        fail(f"malformed claim SHA {row['semantic_id']}: {sha}")

claim_by_id = {r["semantic_id"]: r for r in claims}
family_ids = {r["family_id"] for r in families}
if set(r["family"] for r in claims) - family_ids:
    fail("claim family missing from FAMILIES.tsv")

# Edges are true JSON hyperedges and referentially closed.
for edge in edges:
    try:
        prem = json.loads(edge["premise_ids"])
    except Exception as exc:
        fail(f"bad premise JSON {edge['edge_id']}: {exc}")
    if not isinstance(prem, list) or not prem or len(prem) != len(set(prem)):
        fail(f"bad premise arity {edge['edge_id']}")
    for p in prem:
        if p not in claim_by_id:
            fail(f"dangling premise {p}")
    if edge["conclusion_id"] != "RH" and edge["conclusion_id"] not in claim_by_id:
        fail(f"dangling conclusion {edge['conclusion_id']}")
    if edge["conclusion_id"] == "RH" and edge["final_verdict"] not in {"FALSE"}:
        # All live/conditional RH edges must display at least one open/gap premise.
        if not any(claim_by_id[p]["final_verdict"] in {
            "OPEN_SUFFICIENT_FOR_RH","OPEN_RH_EQUIVALENT","GAP_BLOCKED"
        } for p in prem):
            fail(f"RH edge hides open premise: {edge['edge_id']}")

# Proven-only closure: only reviewed theorem edges may fire.
proved_claim_status = {"VERIFIED","VERIFIED_WITH_FIXES","RETAINED_HEAVY_CERTIFICATE"}
proved_edge_status = {"VERIFIED","VERIFIED_WITH_FIXES"}
reachable = {r["semantic_id"] for r in claims if r["final_verdict"] in proved_claim_status}
changed = True
rh_reachable = False
while changed:
    changed = False
    for edge in edges:
        if edge["final_verdict"] not in proved_edge_status:
            continue
        prem = json.loads(edge["premise_ids"])
        if all(p in reachable for p in prem):
            c = edge["conclusion_id"]
            if c == "RH":
                rh_reachable = True
            elif c not in reachable:
                reachable.add(c)
                changed = True
if rh_reachable:
    fail("accidental proven-only path to RH")

# Alias closure.
for a in aliases:
    target = a["canonical_semantic_id"]
    if target not in claim_by_id:
        fail(f"unresolved alias target {target}")

# PR range exactly 375..707.
pr_numbers = sorted(int(r["pr"]) for r in prs)
if pr_numbers != list(range(375,708)):
    fail("PR disposition range is not exactly 375..707")
if any(r["final_lifecycle_disposition"] == "TARGETED_REVIEW_REQUIRED" for r in prs):
    fail("targeted review row remains")

# All conflicts resolved.
unresolved = [r for r in conflicts if not r["resolution_status"].startswith("RESOLVED")]
if unresolved:
    fail(f"unresolved conflicts: {[r['conflict_id'] for r in unresolved]}")

# No heavy campaign is described as rerun.
for c in comps:
    status = c["heavy_rerun_status"].upper()
    if "RERUN" in status and "NOT" not in status:
        fail(f"heavy campaign rerun status unsafe: {c['computation_id']}")
    if "RUN" in status and not any(x in status for x in ["NOT","NO_HEAVY","NOT_APPLICABLE"]):
        fail(f"heavy run status unsafe: {c['computation_id']} {status}")

# Canonical tables are byte-identical.
pairs = {
    "CLAIMS.tsv":"canonical/2026-08-22/claims.tsv",
    "EDGES.tsv":"canonical/2026-08-22/edges.tsv",
    "ALIASES.tsv":"canonical/2026-08-22/aliases.tsv",
    "FAMILIES.tsv":"canonical/2026-08-22/families.tsv",
    "REFUTATIONS.tsv":"canonical/2026-08-22/refutations.tsv",
    "COMPUTATIONS.tsv":"canonical/2026-08-22/computations.tsv",
    "PR_DISPOSITIONS.tsv":"canonical/2026-08-22/pr_dispositions.tsv",
    "CONFLICTS.tsv":"canonical/2026-08-22/conflicts.tsv",
    "EXTRACTION_PLAN.tsv":"canonical/2026-08-22/extraction_plan.tsv",
}
for src, dst in pairs.items():
    if (here/src).read_bytes() != (root/dst).read_bytes():
        fail(f"canonical mirror mismatch {src} -> {dst}")

# Family packet coverage.
for f in families:
    fid = f["family_id"]
    if fid in {"terminal","review_infrastructure"}:
        continue
    dest = root / f["canonical_destination"]
    packet = dest / "CLAIMS.tsv"
    readme = dest / "README.md"
    if not packet.is_file() or not readme.is_file():
        fail(f"missing family packet {fid}")
    rows = read_tsv(packet)
    expected = {r["semantic_id"] for r in claims if r["family"] == fid}
    got = {r["semantic_id"] for r in rows}
    if got != expected or len(rows) != int(f["claim_count"]):
        fail(f"family packet mismatch {fid}")

# Mellin consumer.
mellin_validation = root / "canonical/consumers/mellin-landau/validation.json"
if not mellin_validation.is_file():
    fail("Mellin validation missing")
mellin = json.loads(mellin_validation.read_text(encoding="utf-8"))
if mellin.get("status") != "PASS_MELLIN_LANDAU_CONSUMER":
    fail("Mellin consumer validation failed")
if mellin.get("consumer_alone_reaches_rh") is not False:
    fail("Mellin consumer graph typing unsafe")

# Front door literals.
readme = (root/"README.md").read_text(encoding="utf-8")
status = (root/"STATUS.md").read_text(encoding="utf-8")
if "The Riemann Hypothesis remains unproved" not in readme:
    fail("README lacks literal RH status")
if "Reviewed-only path to RH:              NONE" not in status:
    fail("STATUS lacks no-path verdict")
for name in ["RESULTS.md","PROOF_GRAPH.md","OPEN_CUTS.md","REFUTATIONS.md","COMPUTATIONS.md","HISTORY.md"]:
    if f"]({name})" not in readme:
        fail(f"README missing link {name}")

result = {
    "status": "PASS_FINAL_SCIENTIFIC_INTEGRATION",
    "rh_status": "UNPROVED",
    "proven_only_path_to_rh": False,
    "frozen_main": freeze["frozen_main"]["sha"],
    "reviewer_d_head": freeze["reviewer_d"]["head"],
    "research_census_terminal_pr": 707,
    "counts": actual_counts,
    "targeted_review_rows": 0,
    "unresolved_conflicts": 0,
    "heavy_campaigns_rerun": False,
    "family_packets": len(families) - 2,
    "canonical_mirror_tables": len(pairs),
}
(here/"validation.json").write_text(json.dumps(result, indent=2, sort_keys=True)+"\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))
