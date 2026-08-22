#!/usr/bin/env python3
"""Fail-closed validator for assembly_graph.json (Lane A1).

Implements the union spec of Reviewer B (CROSS_REVIEW_REPORT.md + GRAPH_DEFECTS.tsv,
branch origin/review/2026-08-22/reviewer-b-cross-review-a @ 945a6eec3406cce8f6cd63eba6c69fb60676c41d)
and Reviewer C (INTEGRATION_HANDOFF.md + PROVENANCE_DEFECTS.tsv,
branch origin/review/2026-08-22/coverage-genealogy-delta @ a520556ac7f30290a11e1fcba7b6f6a24269153e):

  - premises encoded as JSON arrays; exact declared arity; nonempty unique entries;
  - every premise, conclusion and alias target must exist as a node;
  - open/conditional/equivalent hypotheses are typed nodes; RH is a declared terminal;
  - exact 40-hex SHAs and repo paths validated BEFORE any reachability computation
    (live `git cat-file -e sha:path`; --offline falls back to recorded_checks.json
    written by the last successful online run — fail-closed if absent);
  - proved-only reachability excludes open/conditional/equivalent/refuted/unreviewed
    material and MUST NOT reach RH;
  - conditional reachability, minimal open cut, and the gate partial order are emitted.

Deterministic; stdlib only. Exit 0 iff PASS."""

import json, os, re, subprocess, sys, itertools

D = os.path.dirname(os.path.abspath(__file__))
REPO = os.environ.get("RIEMANN_REPO", "/home/user/riemann")
GRAPH = os.path.join(D, "assembly_graph.json")
RECORD = os.path.join(D, "recorded_checks.json")
OFFLINE = "--offline" in sys.argv

NODE_KINDS = {"claim", "hypothesis", "terminal"}
STATUSES = {"VERIFIED", "VERIFIED_WITH_FIXES", "CONDITIONAL_EXACT",
            "OPEN_SUFFICIENT_FOR_RH", "OPEN_RH_EQUIVALENT", "REFUTED",
            "DEPOSITED_UNREVIEWED"}
EDGE_TYPES = {"PROVED_REDUCTION", "CONDITIONAL_IMPLICATION",
              "EQUIVALENCE_AFTER_DIAGONAL", "HYPEREDGE"}
TRUST_MODES = {"strict", "deposited"}
# statuses whose statements count as established theorems (mechanism-usable):
PROVED = {"VERIFIED", "VERIFIED_WITH_FIXES", "CONDITIONAL_EXACT"}
SHA_RE = re.compile(r"^[0-9a-f]{40}$")

errors, warnings = [], []
def err(m): errors.append(m)
def warn(m): warnings.append(m)

with open(GRAPH) as f:
    g = json.load(f)

nodes = g["nodes"]; edges = g["edges"]; aliases = g.get("aliases", [])
by_id = {}

# ---------- structural node validation ----------
for n in nodes:
    sid = n.get("semantic_id")
    if not sid or not isinstance(sid, str): err("node without semantic_id: %r" % n)
    if sid in by_id: err("duplicate node id %s" % sid)
    by_id[sid] = n
    if n.get("kind") not in NODE_KINDS: err("%s: bad kind %r" % (sid, n.get("kind")))
    if n.get("status") not in STATUSES: err("%s: bad status %r" % (sid, n.get("status")))
    if not n.get("statement", "").strip(): err("%s: empty statement" % sid)
    c = n.get("coordinates")
    if not isinstance(c, dict) or set(c) != {"claim_id", "path", "branch", "sha"}:
        err("%s: coordinates must have exactly {claim_id,path,branch,sha}" % sid)

terminals = [n for n in nodes if n["kind"] == "terminal"]
if len(terminals) != 1 or terminals[0]["semantic_id"] != "RH":
    err("exactly one terminal node named RH required (G-RH-TERMINAL-001)")

# ---------- structural edge validation ----------
eids = set()
for e in edges:
    eid = e.get("edge_id", "?")
    if eid in eids: err("duplicate edge id %s" % eid)
    eids.add(eid)
    p = e.get("premises")
    if not isinstance(p, list): err("%s: premises must be a JSON array (G-DELIM-001)" % eid); continue
    if len(p) == 0: err("%s: empty premises (G-ARITY-001)" % eid)
    if len(set(p)) != len(p): err("%s: duplicate premises (G-ARITY-001)" % eid)
    if e.get("arity") != len(p): err("%s: declared arity %r != %d (G-ARITY-001)" % (eid, e.get("arity"), len(p)))
    for x in p:
        if x not in by_id: err("%s: dangling premise %s (G-DANGLE-001)" % (eid, x))
        elif by_id[x]["kind"] == "terminal": err("%s: terminal RH used as premise" % eid)
    concl = e.get("conclusion")
    if concl not in by_id: err("%s: dangling conclusion %r (G-DANGLE-001)" % (eid, concl))
    if concl in p: err("%s: conclusion appears among premises" % eid)
    if e.get("type") not in EDGE_TYPES: err("%s: bad type %r" % (eid, e.get("type")))
    if e.get("trust_mode") not in TRUST_MODES: err("%s: bad trust_mode %r" % (eid, e.get("trust_mode")))
    for x in p:
        if x in by_id and by_id[x]["status"] == "REFUTED":
            err("%s: REFUTED node %s used as premise" % (eid, x))

# ---------- alias closure (G-ALIAS-001) ----------
aids = set()
for a in aliases:
    aid = a.get("alias_id", "?")
    if aid in aids: err("duplicate alias_id %s" % aid)
    aids.add(aid)
    if a.get("canonical_semantic_id") not in by_id:
        err("alias %s: dangling canonical_semantic_id %r" % (aid, a.get("canonical_semantic_id")))
    tg = a.get("targets")
    if not isinstance(tg, list) or not tg: err("alias %s: targets must be a nonempty array" % aid)
    else:
        for t in tg:
            if t not in by_id: err("alias %s: dangling target %r" % (aid, t))

# ---------- SHA + path validation BEFORE reachability (G-PROVEN-001 order) ----------
coords = []
for n in nodes:
    c = n.get("coordinates") or {}
    coords.append(("node " + n.get("semantic_id", "?"), c))
for e in edges:
    for c in e.get("source_coordinates", []):
        coords.append(("edge " + e.get("edge_id", "?"), c))

recorded = {}
if os.path.exists(RECORD):
    with open(RECORD) as f: recorded = json.load(f)

def git_path_ok(sha, path):
    r = subprocess.run(["git", "-C", REPO, "cat-file", "-e", "%s:%s" % (sha, path)],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return r.returncode == 0

def git_commit_ok(sha):
    r = subprocess.run(["git", "-C", REPO, "cat-file", "-e", sha + "^{commit}"],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return r.returncode == 0

new_record = {}
for owner, c in coords:
    sha = c.get("sha", ""); path = c.get("path", "")
    if not SHA_RE.match(sha or ""):
        err("%s: SHA %r is not exactly 40 lowercase hex (never normalized silently)" % (owner, sha))
        continue
    if not path: err("%s: empty path" % owner); continue
    key = sha + ":" + path
    if OFFLINE:
        if recorded.get(key) is True:
            new_record[key] = True
        else:
            err("%s: offline mode and %s not in recorded_checks.json (fail-closed)" % (owner, key))
    else:
        if not git_commit_ok(sha):
            err("%s: commit %s not present in repo" % (owner, sha))
        elif not git_path_ok(sha, path):
            err("%s: path %s does not exist at %s" % (owner, path, sha))
        else:
            new_record[key] = True

if errors:
    # fail closed BEFORE any reachability computation
    verdict = {"verdict": "FAIL", "stage": "structural/provenance", "errors": errors, "warnings": warnings}
    with open(os.path.join(D, "verdict.json"), "w") as f: json.dump(verdict, f, indent=1)
    print("FAIL (pre-reachability): %d errors" % len(errors))
    for m in errors: print("  -", m)
    sys.exit(1)

if not OFFLINE:
    with open(RECORD, "w") as f: json.dump(new_record, f, indent=1, sort_keys=True)

# ---------- reachability semantics ----------
HYPS = [n["semantic_id"] for n in nodes if n["kind"] == "hypothesis"]
GATES = g["meta"]["gates"]
for x in GATES:
    if x not in by_id or by_id[x]["kind"] != "hypothesis":
        err("declared gate %s is not a hypothesis node" % x)

def base_facts(mode):
    out = set()
    for n in nodes:
        if n["kind"] == "claim":
            if n["status"] in PROVED: out.add(n["semantic_id"])
            elif n["status"] == "DEPOSITED_UNREVIEWED" and mode == "deposited": out.add(n["semantic_id"])
    return out

def closure(assumed, mode):
    facts = base_facts(mode) | set(assumed)
    changed = True
    while changed:
        changed = False
        for e in edges:
            if e["trust_mode"] == "deposited" and mode != "deposited": continue
            concl = e["conclusion"]
            if concl in facts: continue
            # PROVED_REDUCTION into an open interface never establishes it
            if e["type"] == "PROVED_REDUCTION" and by_id[concl]["kind"] == "hypothesis": continue
            if all(p in facts for p in e["premises"]):
                facts.add(concl); changed = True
    return facts

results = {}

# (i) proved-only reachability: no hypothesis assumed; must not reach RH, and
# must not establish any hypothesis node, in BOTH trust modes.
for mode in ("strict", "deposited"):
    cl = closure(set(), mode)
    results.setdefault("proved_only", {})[mode] = sorted(cl)
    assert "RH" not in cl, "proved-only reachability reached RH (%s mode) — REJECT" % mode
    leaked = [h for h in HYPS if h in cl]
    assert not leaked, "hypotheses established from nothing: %s" % leaked
results["proved_only_reaches_RH"] = False

# (ii) conditional reachability: each gate alone
cond = {}
for h in HYPS:
    cond[h] = {m: ("RH" in closure({h}, m)) for m in ("strict", "deposited")}
results["conditional_rh"] = cond
suff_strict = sorted([h for h in HYPS if cond[h]["strict"]])
assert set(GATES) <= set(suff_strict), \
    "some declared gate does not suffice alone (strict): %s" % (set(GATES) - set(suff_strict))
results["gates_each_sufficient_strict"] = suff_strict

# (iii) minimal open cut (strict mode)
mincut = None
for k in range(1, len(HYPS) + 1):
    sols = [list(c) for c in itertools.combinations(sorted(HYPS), k)
            if "RH" in closure(set(c), "strict")]
    if sols:
        mincut = {"cardinality": k, "solutions": sols}; break
results["minimal_open_cut"] = mincut
assert mincut and mincut["cardinality"] == 1, "minimal open cut is not a single gate"

# (iv) gate partial order (g => h iff h in closure({g}))
def porder(mode):
    rel = {}
    for a in HYPS:
        cl = closure({a}, mode)
        rel[a] = sorted([b for b in HYPS if b != a and b in cl])
    return rel

order = {m: porder(m) for m in ("strict", "deposited")}
results["gate_implications"] = order

def hasse(rel):
    # equivalence classes under mutual implication
    ids = sorted(rel)
    cls = []
    seen = set()
    for a in ids:
        if a in seen: continue
        c = [a] + [b for b in rel[a] if a in rel[b]]
        c = sorted(set(c)); seen |= set(c); cls.append(c)
    rep = {m: c[0] for c in cls for m in c}
    covers = set()
    for a in ids:
        for b in rel[a]:
            ra, rb = rep[a], rep[b]
            if ra != rb: covers.add((ra, rb))
    # transitive reduction on class representatives
    covers = sorted(covers)
    red = []
    for (a, b) in covers:
        if not any((a, m) in covers and (m, b) in covers for m in rel if m not in (a, b) and rep.get(m) == m):
            red.append([a, b])
    return {"equivalence_classes": cls, "cover_relations": red}

results["hasse"] = {m: hasse(order[m]) for m in ("strict", "deposited")}

# sanity assertions on the expected lattice
oS = order["strict"]; oD = order["deposited"]
assert "HYP.HHFE102010" in oS["HYP.BPOE103300"], "BPOE => HHFE missing (strict)"
assert "HYP.HCNC103100" in oS["HYP.HHFE102010"] and "HYP.HHFE102010" in oS["HYP.HCNC103100"], \
    "HHFE <=> HCNC equivalence missing (strict)"
assert "HYP.ROWS23" in oS["HYP.FCHD67"], "FCHD67 => ROWS23 missing (strict)"
assert "HYP.CFBB102100" in oD["HYP.HCNC103100"], "HCNC => CFBB missing (deposited)"
assert "HYP.CFBB102100" not in oS["HYP.HCNC103100"], \
    "HCNC => CFBB must NOT be reviewer-backed (T-102110 unrowed) — honesty check"

verdict = {
    "verdict": "PASS",
    "rh_status": "UNPROVED — proved-only reachability does not reach RH in either trust mode",
    "counts": {"nodes": len(nodes), "edges": len(edges), "aliases": len(aliases),
               "hypotheses": len(HYPS), "coordinates_checked": len(new_record)},
    "offline": OFFLINE,
    "errors": errors, "warnings": warnings,
    "results": results,
}
with open(os.path.join(D, "verdict.json"), "w") as f:
    json.dump(verdict, f, indent=1)

# ---------- REPORT.md ----------
L = []
L.append("# Assembly-graph validator report (Lane A1)\n")
L.append("Verdict: **PASS** (all structural, provenance and reachability asserts green; %s mode)\n" %
         ("offline" if OFFLINE else "online git verification"))
L.append("RH status: **UNPROVED**. Proved-only reachability (open/conditional/equivalent/refuted/"
         "unreviewed material excluded) does NOT reach RH in either trust mode — matching Reviewer B's "
         "strict cross-review parser sanity result (@ 945a6eec).\n")
L.append("## Counts\n- nodes: %d (claims %d, hypotheses %d, terminal 1)\n- edges: %d\n- aliases: %d\n- (sha,path) coordinates verified: %d\n" %
         (len(nodes), sum(1 for n in nodes if n["kind"] == "claim"), len(HYPS), len(edges), len(aliases), len(new_record)))
L.append("## (i) Proved-only reachable set (strict)\n" + ", ".join(results["proved_only"]["strict"]) + "\n")
L.append("\n## (ii) Conditional reachability — gate alone => RH?\n\n| gate | strict (reviewer-backed) | deposited |\n|---|---|---|")
for h in sorted(cond): L.append("| %s | %s | %s |" % (h, cond[h]["strict"], cond[h]["deposited"]))
L.append("\nEvery declared gate suffices ALONE, already in strict mode.\n")
L.append("## (iii) Minimal open cut\nCardinality **1**. Singleton solutions: " +
         ", ".join(s[0] for s in mincut["solutions"]) + "\n")
L.append("## (iv) Gate partial order (proved implications between gates)\n")
for m in ("strict", "deposited"):
    L.append("### %s mode\nEquivalence classes: %s\nCover relations: %s\n" %
             (m, results["hasse"][m]["equivalence_classes"], results["hasse"][m]["cover_relations"]))
L.append("Reading: BPOE103300 => HHFE102010 <=> HCNC103100 (strict); HCNC103100 => CFBB102100 only via the "
         "unrowed T-102110 (deposited mode); FCHD67 => ROWS23; WX53POS, HNM67, CFBB102100 otherwise incomparable islands; every gate => RH.\n")
L.append("## Recorded provenance defects (reported, never silently normalized)\n")
for d in g.get("provenance_defects", []):
    L.append("- **%s** — %s | observed: %s | disposition: %s" % (d["defect_id"], d["artifact"], d["observed"], d["disposition"]))
L.append("")
with open(os.path.join(D, "REPORT.md"), "w") as f:
    f.write("\n".join(L))

print("PASS | nodes=%d edges=%d coords=%d | mincut=1 | sufficient gates: %s" %
      (len(nodes), len(edges), len(new_record), ", ".join(suff_strict)))
