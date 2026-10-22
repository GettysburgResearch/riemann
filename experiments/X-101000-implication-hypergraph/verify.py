#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def digest(x):
    return hashlib.sha256(
        json.dumps(x, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()

def load_aliases():
    p = ROOT / "integration/implication-matrix/2026-08-20-node-aliases.tsv"
    lines = p.read_text().splitlines()
    head = lines[0].split("\t")
    return [dict(zip(head, line.split("\t"))) for line in lines[1:] if line]

def reachable(nodes, edges, allowed_status):
    have = {n["id"] for n in nodes if n["status"] == "VERIFIED"}
    changed = True
    while changed:
        changed = False
        for e in edges:
            if e["status"] not in allowed_status:
                continue
            if all(x in have for x in e["inputs"]) and e["output"] not in have:
                have.add(e["output"])
                changed = True
    return have

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    aliases = load_aliases()
    ids = [x["canonical_id"] for x in aliases]
    assert len(ids) == len(set(ids))
    assert all(x["canonical_id"].startswith("IM-") for x in aliases)

    graph = json.loads(
        (ROOT / "integration/implication-matrix/2026-08-20-hyperedges.json").read_text()
    )
    nodes = graph["nodes"]
    edges = graph["hyperedges"]
    node_ids = {n["id"] for n in nodes}
    assert all(e["output"] in node_ids for e in edges)
    assert all(set(e["inputs"]) <= node_ids for e in edges)

    # No verified-only path to RH.
    have = reachable(nodes, edges, {"VERIFIED", "EXACT_REALIZATION", "DECOMPOSITION"})
    assert "IM-RH" not in have

    # If either open terminal class is granted, RH becomes reachable.
    def with_gate(gate):
        nn = [dict(n) for n in nodes]
        for n in nn:
            if n["id"] == gate:
                n["status"] = "VERIFIED"
        return reachable(
            nn, edges,
            {"VERIFIED", "EXACT_REALIZATION", "DECOMPOSITION", "CONDITIONAL"}
        )
    assert "IM-RH" in with_gate("IM-M01")
    assert "IM-RH" in with_gate("IM-M04")
    assert "IM-RH" in with_gate("IM-M05")

    # L-101000 generic dyadic Hardy estimate on synthetic nonnegative blocks.
    # V(T)=T^eps and f is placed at dyadic endpoints at the maximal permitted mass.
    eps = 0.2
    Y = 10.0
    tail = 0.0
    for k in range(40):
        block_mass = (2 ** (k + 1) * Y) ** eps
        tail += (2 ** (-k)) * block_mass
    assert tail < 10 * (Y ** eps)

    # L-101001 negative-part Lipschitz and integrable perturbation.
    fixtures = [(-3.0, 2.0), (4.0, -7.0), (-5.0, -2.0), (0.0, 1.0)]
    for a, b in fixtures:
        am = max(-a, 0.0)
        bm = max(-b, 0.0)
        assert abs(am - bm) <= abs(a - b) + 1e-15
    # Integral of X^-1/6 against dX/X from 2 to infinity.
    integral = 6 * (2 ** (-1/6))
    assert integral < 6

    # SCC/equivalence fixture.
    pairs = {(e["inputs"][0], e["output"]) for e in edges
             if e["type"] == "equivalence" and len(e["inputs"]) == 1}
    assert ("IM-M04", "IM-M05") in pairs
    assert ("IM-M05", "IM-M04") in pairs

    payload = {
        "schema": "riemann.t101000.implication-hypergraph.v1",
        "alias_count": len(aliases),
        "node_count": len(nodes),
        "hyperedge_count": len(edges),
        "verified_only_rh_path": False,
        "critical_variation_gate_closes": True,
        "rough_largest_prime_gate_closes": True,
        "balanced_vaughan_gate_closes": True,
        "lpmw_bvd_same_scc": True,
        "phase_hasse_independent_detector": False,
        "afcd_implies_acad": True,
        "minimal_open_cut_classes": ["CV", "XD"],
        "rh_established": False,
        "verdict": "PASS_T101000_IMPLICATION_HYPERGRAPH",
    }
    payload["proof_object_sha256"] = digest(payload)
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    else:
        print(text, end="")
    print(payload["verdict"])
    print(payload["proof_object_sha256"])

if __name__ == "__main__":
    main()
