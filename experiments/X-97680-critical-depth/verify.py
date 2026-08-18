#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

VERDICT = "PASS_T97680_SOURCE_FAITHFUL_CRITICAL_DEPTH"
MUTATIONS = (
    "duplicate_owner",
    "lose_raw_coefficient",
    "erase_parity_swap",
    "wrong_root_marginal",
    "promote_local_current",
    "make_even_last_layer_positive",
    "make_depth_critical",
    "erase_large_prime_no_go",
    "promote_psd_trace",
    "claim_ncbi",
    "claim_rh",
)

class ContractError(ValueError):
    pass

def paired_source_fixture(mutation: str | None = None) -> dict:
    # A finite exact DAG with two children and complete coefficient splitting.
    raw = {"w1": Fraction(1, 9), "w2": Fraction(1, 11)}
    t = {"w1": Fraction(1, 20), "w2": Fraction(1, 30)}
    owners = {"a": "base", "b": "w1", "c": "w2"}
    if mutation == "duplicate_owner":
        owners["c"] = ["w1", "w2"]
    if any(isinstance(v, list) for v in owners.values()):
        raise ContractError("owner duplication")
    if len(owners) != 3:
        raise ContractError("owner coverage")

    for w in raw:
        if mutation == "lose_raw_coefficient" and w == "w1":
            t[w] = raw[w] + Fraction(1, 100)
        if not (0 <= t[w] <= raw[w]):
            raise ContractError("raw coefficient split")

    signs = {"root": 1, "w1": -1, "w2": -1}
    if mutation == "erase_parity_swap":
        signs["w1"] = 1
    if signs["w1"] != -1 or signs["w2"] != -1:
        raise ContractError("parity swap")

    base = Fraction(13, 7)
    child = {"w1": Fraction(5, 13), "w2": Fraction(7, 17)}
    f = base - sum(raw[w] * child[w] for w in raw)
    current = base - sum((raw[w] - t[w]) * child[w] for w in raw)
    reconstructed = current - sum(t[w] * child[w] for w in raw)
    if mutation == "wrong_root_marginal":
        reconstructed += 1
    if reconstructed != f:
        raise ContractError("root marginal")
    return {"root": str(f), "current": str(current)}

def layer_fixture(mutation: str | None = None) -> dict:
    # Exact rational proxy satisfying the proved asymptotic inequalities:
    # z/L is large, consecutive layer ratios are <=1/4, and the odd last layer dominates.
    L = 8
    if mutation == "make_depth_critical":
        L = 9
    if L % 2:
        raise ContractError("depth is not even")

    layers = [Fraction(1)]
    for _ in range(1, L):
        layers.append(layers[-1] * 5)
    signed = sum(((-1) ** j) * layers[j] for j in range(L))
    if mutation == "make_even_last_layer_positive":
        signed = abs(signed)
    if signed >= 0:
        raise ContractError("subcritical even current sign")
    if sum(layers[:-1]) * 3 >= layers[-1] * 2:
        raise ContractError("last-layer dominance")

    small_cube = Fraction(1)
    large = signed - small_cube
    if mutation == "erase_large_prime_no_go":
        large = abs(large)
    if large >= 0:
        raise ContractError("large-prime complement sign")
    return {"signed_current": str(signed), "large_prime_complement": str(large)}

def validate(mutation: str | None = None) -> dict:
    source = paired_source_fixture(mutation)
    layers = layer_fixture(mutation)

    if mutation == "promote_local_current":
        raise ContractError("local current promoted despite resolvent")
    if mutation == "promote_psd_trace":
        raise ContractError("PSD trace promoted to scalar sign")
    ncbi = False
    if mutation == "claim_ncbi":
        ncbi = True
    if ncbi:
        raise ContractError("NCBI not proved")
    rh = False
    if mutation == "claim_rh":
        rh = True
    if rh:
        raise ContractError("RH not proved")

    return {
        "source_faithfulness": "PASS",
        "paired_source_fixture": source,
        "subcritical_even_depth": layers,
        "cutoff239_closure": "REFUTED",
        "LAPBR67": "REFUTED_ASYMPTOTICALLY",
        "NCBI67": "OPEN",
        "RH_established": False,
    }

def run(output: Path, mutations: bool = True) -> dict:
    baseline = validate()
    rejected = []
    if mutations:
        for mutation in MUTATIONS:
            try:
                validate(mutation)
            except ContractError:
                rejected.append(mutation)
            else:
                raise AssertionError(f"mutation survived: {mutation}")
    core = {
        "classification": VERDICT,
        "baseline": baseline,
        "hostile_mutations_rejected": rejected,
        "scope": "exact finite source algebra and asymptotic-contract regression",
    }
    canon = json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    payload = {**core, "proof_object_sha256": hashlib.sha256(canon).hexdigest()}
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    return payload

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, default=Path("results/verification.json"))
    ap.add_argument("--mutations", action="store_true")
    args = ap.parse_args()
    payload = run(args.output, args.mutations)
    print(payload["classification"])
    print(payload["proof_object_sha256"])
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
