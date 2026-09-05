#!/usr/bin/env python3
from pathlib import Path
import csv,json,re
r=Path(__file__).resolve().parents[1]
req=["FREEZE.json","CLAIMS.tsv","ROUTE_EDGES.tsv","ALIASES.tsv","REFUTATIONS.tsv","COMPUTATIONS.tsv","FIXES.md","REPORT.md","INTEGRATION_HANDOFF.md"]
for n in req: assert (r/n).is_file(),n
f=json.loads((r/"FREEZE.json").read_text());assert f["review_base"]=="677203992eb0168920365ee45ae9db76bfa97dcf"
with (r/"CLAIMS.tsv").open(newline="",encoding="utf8") as h:
 d=list(csv.DictReader(h,delimiter="\t"));assert d and len({x["semantic_id"] for x in d})==len(d)
by={x["semantic_id"]:x for x in d};assert by["ARITH.XD.LPMW_BVD_K0_K1_MISTYPE"]["mathematical_verdict"]=="FALSE";assert by["ARITH.XD.SAME_K1_LPMW_BVD"]["mathematical_verdict"]=="VERIFIED"
with (r/"ROUTE_EDGES.tsv").open(newline="",encoding="utf8") as h:
 e=list(csv.DictReader(h,delimiter="\t"));assert any(x["edge_id"]=="EDGE.XD.OLD_K0_K1" and x["review_verdict"]=="FALSE" for x in e)
t=(r/"REPORT.md").read_text();assert "RH remains unproved" in t and "Proven-only path to RH:** **none" in t and "PR #705" in t
print("PASS_REVIEWER_A_ARITHMETIC_FREEZE")
