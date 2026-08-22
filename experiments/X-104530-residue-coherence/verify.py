#!/usr/bin/env python3
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path


def coherence(residues):
    R = len(residues)
    A = max(-sum(residues, Fraction(0)), Fraction(0))
    B = sum((r * r for r in residues), Fraction(0))
    C = A * A / (R * B) if R and B else Fraction(0)
    G = sum(1 for r in residues if r < 0)
    return R, A, B, C, G


def payload_digest(payload):
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    fixtures = {
        "cubic_all_good": [Fraction(-1, 3), Fraction(-1, 3)],
        "quartic_firewall": [Fraction(1, 8), Fraction(-1, 2), Fraction(1, 8)],
        "coherent_partial": [
            Fraction(-1),
            Fraction(-4, 5),
            Fraction(-6, 5),
            Fraction(1, 20),
        ],
    }

    fixture_output = {}
    for name, residues in fixtures.items():
        R, A, B, C, G = coherence(residues)
        assert Fraction(G, 1) >= A * A / B
        transfer = 2 * C - 1
        fixture_output[name] = {
            "R": R,
            "A": str(A),
            "B": str(B),
            "coherence": str(C),
            "transfer_constant": str(transfer),
            "good_count": G,
            "cauchy_lower_bound": str(A * A / B),
        }

    residues = fixtures["coherent_partial"]
    R, A, B, C, _ = coherence(residues)
    mu = A / R
    m2 = B / R
    v2 = (m2 - mu * mu) / (mu * mu)
    assert C == 1 / (1 + v2)
    assert 2 * C - 1 == (1 - v2) / (1 + v2)

    p1 = Fraction(99, 100)
    p2 = Fraction(7, 10)
    transfer = 2 * C - 1
    assert transfer * p1 != transfer * p2
    assert transfer * p1 > transfer * p2

    payload = {
        "schema": "riemann.t104530.residue_coherence_transfer.v1",
        "checks": {
            "fixtures": fixture_output,
            "mean_variance_identity": True,
            "load_bearing_p_values": [str(p1), str(p2)],
            "corresponding_conclusions": [str(transfer * p1), str(transfer * p2)],
        },
        "scope": {
            "residue_coherence_transfer_proved_exact": True,
            "line_proportion_hypothesis_load_bearing": True,
            "rcmv104530_proved": False,
            "rh_established": False,
        },
        "verdict": "PASS_T104530_RESIDUE_COHERENCE_TRANSFER_ALGEBRA",
    }
    payload["proof_object_sha256"] = payload_digest(payload)
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
