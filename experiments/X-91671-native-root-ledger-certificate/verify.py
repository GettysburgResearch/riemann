#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Dict, Mapping

REQUIRED_BASE_LABELS = {"d=1", "d=2", "d=5"}
ALLOWED_CHANNELS = {"hall", "outer", "collar", "mismatch", "omission", "shared_port", "recursive_child", "stop"}


def Q(x: Any) -> Fraction:
    return x if isinstance(x, Fraction) else Fraction(str(x))


def parse_vector(raw: Mapping[str, Any]) -> Dict[str, Fraction]:
    return {k: Q(v) for k, v in raw.items()}


def add_vectors(a: Mapping[str, Fraction], b: Mapping[str, Fraction]) -> Dict[str, Fraction]:
    keys = set(a) | set(b)
    return {k: a.get(k, Fraction(0)) + b.get(k, Fraction(0)) for k in keys}


def scale_vector(c: Fraction, v: Mapping[str, Fraction]) -> Dict[str, Fraction]:
    return {k: c * x for k, x in v.items()}


def assert_nonnegative(vector: Mapping[str, Fraction], label: str) -> None:
    bad = {k: v for k, v in vector.items() if v < 0}
    if bad:
        raise AssertionError(f"negative native coordinates in {label}: {bad}")


def validate_certificate(cert: Mapping[str, Any]) -> Dict[str, Any]:
    checks = 0
    metadata = cert.get("metadata", {})
    assert metadata.get("rough_threshold") == 67
    assert metadata.get("small_prime_product") == 61
    assert metadata.get("child_target_ratio_formula") == "2/(p+sqrt(p))"
    checks += 3

    atoms_raw = cert["atoms"]
    labels = set(atoms_raw)
    missing = REQUIRED_BASE_LABELS - labels
    if missing:
        raise AssertionError(f"missing repaired base labels: {sorted(missing)}")
    checks += len(REQUIRED_BASE_LABELS)

    atom_vectors: Dict[str, Dict[str, Fraction]] = {}
    atom_weights: Dict[str, Fraction] = {}
    residual_weights: Dict[str, Fraction] = {}
    for label, raw in atoms_raw.items():
        weight = Q(raw["weight"])
        residual = Q(raw["residual_weight"])
        vector = parse_vector(raw["unit_native_vector"])
        assert weight >= 0 and residual >= 0
        assert_nonnegative(vector, f"atom {label}")
        atom_weights[label] = weight
        residual_weights[label] = residual
        atom_vectors[label] = vector
        checks += 2 + len(vector)

    allocations = cert["allocations"]
    consumption = {label: Fraction(0) for label in labels}
    source_total: Dict[str, Fraction] = {}
    output_total: Dict[str, Fraction] = {}
    local_remainder_total: Dict[str, Fraction] = {}
    channel_counts: Dict[str, int] = {}

    for label in labels:
        source_total = add_vectors(source_total, scale_vector(atom_weights[label], atom_vectors[label]))

    for idx, raw in enumerate(allocations):
        atom = raw["atom"]
        channel = raw["channel"]
        if atom not in labels:
            raise AssertionError(f"allocation {idx} references unknown atom {atom}")
        if channel not in ALLOWED_CHANNELS:
            raise AssertionError(f"allocation {idx} has unknown channel {channel}")
        coefficient = Q(raw["coefficient"])
        assert coefficient >= 0
        consumption[atom] += coefficient
        channel_counts[channel] = channel_counts.get(channel, 0) + 1

        output = parse_vector(raw["output_native_vector"])
        remainder = parse_vector(raw["local_remainder_vector"])
        assert_nonnegative(output, f"allocation {idx} output")
        assert_nonnegative(remainder, f"allocation {idx} remainder")
        lhs = scale_vector(coefficient, atom_vectors[atom])
        rhs = add_vectors(output, remainder)
        if lhs != rhs:
            raise AssertionError(f"local native identity failed at allocation {idx}: {lhs} != {rhs}")
        output_total = add_vectors(output_total, output)
        local_remainder_total = add_vectors(local_remainder_total, remainder)
        checks += 3 + len(lhs)

    for atom in labels:
        if residual_weights[atom] + consumption[atom] != atom_weights[atom]:
            raise AssertionError(
                f"atomwise partition failed for {atom}: residual {residual_weights[atom]} + "
                f"consumption {consumption[atom]} != source {atom_weights[atom]}"
            )
        checks += 1

    assert "shared_port" in channel_counts
    checks += 1

    leftover_total: Dict[str, Fraction] = {}
    for atom in labels:
        leftover_total = add_vectors(leftover_total, scale_vector(residual_weights[atom], atom_vectors[atom]))

    reconstructed = add_vectors(output_total, local_remainder_total, leftover_total)
    if reconstructed != source_total:
        raise AssertionError(f"global native ledger failed: {reconstructed} != {source_total}")
    checks += len(source_total)

    return {
        "checks": checks,
        "atoms": len(labels),
        "allocations": len(allocations),
        "native_coordinates": len(source_total),
        "channels_seen": sorted(channel_counts),
    }


def synthetic_pass_certificate() -> Dict[str, Any]:
    unit = {"target": "1", "score": "2", "row:2": "3", "ordinary:2": "4", "radix4:2": "5", "port": "1"}
    atoms = {
        "d=1": {"weight": "1", "residual_weight": "1/8", "unit_native_vector": unit},
        "d=2": {"weight": "3/4", "residual_weight": "1/8", "unit_native_vector": unit},
        "d=5": {"weight": "1/2", "residual_weight": "1/8", "unit_native_vector": unit},
    }
    plan = {
        "d=1": [("hall", Fraction(1,4)), ("outer", Fraction(1,8)), ("collar", Fraction(1,8)), ("shared_port", Fraction(1,8)), ("recursive_child", Fraction(1,8)), ("stop", Fraction(1,8))],
        "d=2": [("hall", Fraction(1,8)), ("mismatch", Fraction(1,8)), ("omission", Fraction(1,8)), ("recursive_child", Fraction(1,8)), ("stop", Fraction(1,8))],
        "d=5": [("outer", Fraction(1,8)), ("collar", Fraction(1,8)), ("stop", Fraction(1,8))],
    }
    allocations = []
    parsed_unit = parse_vector(unit)
    for atom, entries in plan.items():
        for channel, coefficient in entries:
            output = scale_vector(coefficient, parsed_unit)
            allocations.append({"atom": atom, "channel": channel, "coefficient": str(coefficient), "output_native_vector": {k: str(v) for k,v in output.items()}, "local_remainder_vector": {k: "0" for k in output}})
    return {"metadata": {"rough_threshold": 67, "small_prime_product": 61, "child_target_ratio_formula": "2/(p+sqrt(p))"}, "atoms": atoms, "allocations": allocations}


def run_controls() -> Dict[str, Any]:
    passing = synthetic_pass_certificate()
    summary = validate_certificate(passing)
    capacity, hall, outer = Fraction(1), Fraction(3,5), Fraction(3,5)
    assert hall <= capacity and outer <= capacity and hall + outer > capacity

    failing = synthetic_pass_certificate()
    failing["atoms"]["d=1"]["residual_weight"] = "0"
    failing["allocations"] = [
        {"atom":"d=1","channel":"hall","coefficient":"3/5","output_native_vector":{"target":"3/5","score":"6/5","row:2":"9/5","ordinary:2":"12/5","radix4:2":"3","port":"3/5"},"local_remainder_vector":{"target":"0","score":"0","row:2":"0","ordinary:2":"0","radix4:2":"0","port":"0"}},
        {"atom":"d=1","channel":"outer","coefficient":"3/5","output_native_vector":{"target":"3/5","score":"6/5","row:2":"9/5","ordinary:2":"12/5","radix4:2":"3","port":"3/5"},"local_remainder_vector":{"target":"0","score":"0","row:2":"0","ordinary:2":"0","radix4:2":"0","port":"0"}},
    ]
    rejected = False
    try:
        validate_certificate(failing)
    except AssertionError:
        rejected = True
    assert rejected

    return {"verdict":"PASS_NATIVE_ROOT_LEDGER_CERTIFICATE","rh_proved":False,"passing_fixture":summary,"separate_bound":"3/5 <= 1","combined_overdraw":"6/5 > 1","overdraw_fixture_rejected":rejected,"scope":"generic certificate theorem and synthetic controls; live L-91659 data absent"}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    if args.certificate:
        cert = json.loads(args.certificate.read_text(encoding="utf-8"))
        result = {"verdict":"PASS_SUPPLIED_NATIVE_ROOT_LEDGER_CERTIFICATE","rh_proved":False,"certificate":str(args.certificate),"summary":validate_certificate(cert)}
    else:
        result = run_controls()
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(rendered, encoding="utf-8")
    print(rendered, end="")

if __name__ == "__main__":
    main()
