#!/usr/bin/env python3
"""Exact bounded scalar-trace counterfeits; no arithmetic/RH estimate."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import subprocess
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
NOTE = HERE / "FAMILY_BINDING_PERMUTATION_FIREWALL.md"
FIXTURE = HERE / "family_binding_permutation_firewall.json"
MANIFEST = HERE / "family_binding_permutation_firewall.sources.json"
TEST = ROOT / "tests/test_family_binding_permutation_firewall.py"
BASE = "6675c19f20760301d8c91dedc4a7836170003512"
SCHEMA = "riemann.riemann_structures.family_binding_permutation_firewall.v1"
MAX_N, MAX_ORDER, MAX_BITS, CENSUS_MAX_N = 8, 12, 32, 4
SOURCES = (
    {
        "role": "portfolio_synthetic_counterfeit_target",
        "commit": BASE,
        "path": "research/riemann-structures/RIEMANN_STRUCTURES_WAVE2_PORTFOLIO.md",
        "git_blob": "f5e0eb316f29d5e44cc3c7124401cb3e784fef49",
        "sha256_lf": "23d5a5a7ccdf7669cbbfab6bf4a71d904c71ca5986caecb424d33d67bcd70a8c",
    },
    {
        "role": "labeled_signed_extraction_is_outside_the_no_go",
        "commit": BASE,
        "path": "research/l-families/atlas/function_field/FFPS_PRINCIPAL_ANOMALY_TRANSFER_DICHOTOMY.md",
        "git_blob": "47c148187db578357035926f8ff12419b0cf3652",
        "sha256_lf": "1c2c2159e6cb6f55e4fd3605c1b3181b36d318cb02e67608399b1c4a37cbfd70",
    },
)


def render(value: object) -> str:
    return json.dumps(value, indent=2, sort_keys=True, ensure_ascii=True) + "\n"


def digest(data: bytes) -> str:
    return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()


def exact(value: int | Fraction) -> Fraction:
    if type(value) not in (int, Fraction):
        raise ValueError("values must be exact integers or Fractions, not bool/float")
    value = Fraction(value)
    if max(value.numerator.bit_length(), value.denominator.bit_length()) > MAX_BITS:
        raise ValueError("rational input exceeds the 32-bit numerator/denominator cap")
    return value


def family(values: tuple[int | Fraction, ...]) -> tuple[Fraction, ...]:
    if type(values) is not tuple or not 1 <= len(values) <= MAX_N:
        raise ValueError("family must be a tuple of length 1..8")
    return tuple(exact(value) for value in values)


def principal(index: int, size: int) -> None:
    if type(index) is not int or not 0 <= index < size:
        raise ValueError("principal label is outside the family")


def moment(values: tuple[int | Fraction, ...], order: int) -> Fraction:
    values = family(values)
    if type(order) is not int or not 0 <= order <= MAX_ORDER:
        raise ValueError("moment order must be an integer in 0..12")
    # Order zero is the trace of the one-dimensional identity, also at zero.
    return sum((value**order for value in values), Fraction(0)) / len(values)


def relabel(
    values: tuple[int | Fraction, ...], permutation: tuple[int, ...]
) -> tuple[Fraction, ...]:
    values = family(values)
    if (
        type(permutation) is not tuple
        or any(type(index) is not int for index in permutation)
        or sorted(permutation) != list(range(len(values)))
    ):
        raise ValueError("relabeling must be a permutation of all family labels")
    return tuple(values[index] for index in permutation)


def counterfeit(
    values: tuple[int | Fraction, ...], index: int
) -> tuple[Fraction, ...] | None:
    values = family(values)
    principal(index, len(values))
    for other, value in enumerate(values):
        if value != values[index]:
            permutation = list(range(len(values)))
            permutation[index], permutation[other] = (
                permutation[other],
                permutation[index],
            )
            return relabel(values, tuple(permutation))
    return None


def nonnegative_bound(values: tuple[int | Fraction, ...], index: int) -> Fraction:
    values = family(values)
    principal(index, len(values))
    if min(values) < 0:
        raise ValueError("ordinary mean domination requires nonnegative entries")
    return len(values) * moment(values, 1)


def pair_panel(values: tuple[int | Fraction, ...], index: int) -> dict[str, object]:
    values = family(values)
    other = counterfeit(values, index)
    identifiable = other is None
    other = values if other is None else other
    moments = tuple(moment(values, order) for order in range(MAX_ORDER + 1))
    if sorted(values) != sorted(other) or moments != tuple(
        moment(other, order) for order in range(MAX_ORDER + 1)
    ):
        raise ArithmeticError("relabeling changed invariant data")
    if (values[index] == other[index]) != identifiable:
        raise ArithmeticError("counterfeit failed to contrast the principal values")
    return {
        "N": len(values),
        "principal_label": index,
        "left": list(map(str, values)),
        "right": list(map(str, other)),
        "selected_values": [str(values[index]), str(other[index])],
        "unlabeled_multiset": list(map(str, sorted(values))),
        "common_moments_0_through_12": list(map(str, moments)),
        "identifiable_from_complete_multiset": identifiable,
    }


def exhaustive_census() -> dict[str, object]:
    transcript = []
    tuple_count = 0
    for size in range(1, CENSUS_MAX_N + 1):
        for values in product((-1, 0, 1), repeat=size):
            tuple_count += 1
            orbit = sorted(set(permutations(values)))
            target_moments = [moment(values, order) for order in range(MAX_ORDER + 1)]
            for labeling in orbit:
                if [
                    moment(labeling, order) for order in range(MAX_ORDER + 1)
                ] != target_moments:
                    raise ArithmeticError("finite orbit trace moments disagree")
            for index in range(size):
                possible = sorted({labeling[index] for labeling in orbit})
                identifiable = len(possible) == 1
                if (
                    possible != sorted(set(values))
                    or (counterfeit(values, index) is None) != identifiable
                ):
                    raise ArithmeticError("orbit recovery criterion failed")
                nonnegative = min(values) >= 0
                if nonnegative and values[index] > nonnegative_bound(values, index):
                    raise ArithmeticError("nonnegative domination failed")
                transcript.append(
                    {
                        "values": values,
                        "principal_label": index,
                        "orbit_size": len(orbit),
                        "possible_selected_values": possible,
                        "identifiable": identifiable,
                        "nonnegative": nonnegative,
                    }
                )
    return {
        "alphabet": [-1, 0, 1],
        "lengths": [1, CENSUS_MAX_N],
        "all_distinct_permutations_enumerated": True,
        "tuple_count": tuple_count,
        "marked_tuple_count": len(transcript),
        "identifiable_marked_cases": sum(row["identifiable"] for row in transcript),
        "nonnegative_marked_cases": sum(row["nonnegative"] for row in transcript),
        "transcript_sha256": digest(render(transcript).encode()),
    }


def expected_manifest() -> dict[str, object]:
    return {
        "schema": "riemann.riemann_structures.family_binding_sources.v1",
        "status": "DOCUMENTARY_SOURCE_LOCK_NOT_INTEGRATED",
        "predecessor_commit": BASE,
        "sources": list(SOURCES),
        "authentication": "Exact COMMIT:PATH Git blob ID and LF-normalized SHA-256 content.",
        "boundary": "The sources fix the programme target and signed-extraction escape; no arithmetic estimate is imported.",
    }


def git_bytes(*args: str) -> bytes:
    result = subprocess.run(
        ["git", *args], cwd=ROOT, capture_output=True, check=False, timeout=15
    )
    if result.returncode:
        raise RuntimeError(
            "frozen Git source is unavailable: "
            + result.stderr.decode(errors="replace")
        )
    return result.stdout


def authenticate_sources() -> None:
    if json.loads(MANIFEST.read_text(encoding="utf-8")) != expected_manifest():
        raise ValueError("source manifest differs from the exact source contract")
    for source in SOURCES:
        ref = f"{source['commit']}:{source['path']}"
        if git_bytes("rev-parse", ref).decode().strip() != source["git_blob"]:
            raise ValueError("frozen source Git blob mismatch")
        if digest(git_bytes("show", ref)) != source["sha256_lf"]:
            raise ValueError("frozen source content hash mismatch")


def check_packet_contract() -> None:
    note = NOTE.read_text(encoding="utf-8")
    for anchor in (
        "Theorem 1 (orbit-wise principal recovery)",
        "Theorem 2 (sharp mean-only domination)",
        "first average alone",
        "P=A-K=C-S",
        "not an actual amplifier or inversion, and not a novelty claim",
    ):
        if anchor not in note:
            raise ValueError(f"missing note contract: {anchor}")
    if any(
        isinstance(node, ast.Assert)
        for node in ast.walk(ast.parse(Path(__file__).read_text(encoding="utf-8")))
    ):
        raise ValueError("producer checks must survive Python -O")


def build_report() -> dict[str, object]:
    authenticate_sources()
    check_packet_contract()
    magnitude = Fraction(3, 2)
    signed = [
        pair_panel((magnitude, -magnitude) + (0,) * (size - 2), 0)
        for size in range(2, MAX_N + 1)
    ]
    spikes = []
    for size in range(1, MAX_N + 1):
        values = (magnitude,) + (0,) * (size - 1)
        mean = moment(values, 1)
        bound = nonnegative_bound(values, 0)
        if bound != magnitude or magnitude / mean != size:
            raise ArithmeticError("sharp spike failed")
        panel = pair_panel(values, 0)
        panel.update(
            {
                "mean": str(mean),
                "N_times_mean": str(bound),
                "optimal_mean_only_constant": size,
            }
        )
        spikes.append(panel)
    report = {
        "schema": SCHEMA,
        "status": "EXACT_STRUCTURAL_FIREWALL_NOT_RH_ESTIMATE_NOT_NOVELTY_CLAIM",
        "theorem_scope": {
            "family_size": "every integer N>=1; unrestricted relabeling and a fixed external principal mark",
            "recovery": "complete multiset identifies the principal value on its full orbit iff all entries are equal",
            "trace_moments": "all integer orders r>=0 agree by reindexing; not inferred from the finite checks",
            "mean_only_tax": "optimal constant N for nonnegative entries and the first average alone",
            "signed_mean_failure": "N>=2; a positive selected value can coexist with zero signed average",
            "absolute_mean_tax": "absolute selected value <= N times mean absolute value; N is sharp",
            "stronger_data_escape": "the complete multiset gives the maximum; higher moments may give stronger bounds",
            "signed_source_escape": "P=A-K=C-S retains labeled data; no extra amplifier is imposed after those signed gates",
            "actual_arithmetic_family_or_RH_estimate": False,
        },
        "computation_caps": {
            "max_N": MAX_N,
            "max_moment_order": MAX_ORDER,
            "max_input_bits": MAX_BITS,
            "census_max_N": CENSUS_MAX_N,
        },
        "signed_opposite_pairs": signed,
        "nonnegative_spikes": spikes,
        "edge_controls": {
            "singleton": pair_panel((Fraction(5, 3),), 0),
            "all_equal": pair_panel((2, 2, 2), 1),
            "all_zero": pair_panel((0, 0, 0, 0), 3),
            "repeated_nonconstant": pair_panel((2, 2, -1, 2), 1),
        },
        "exhaustive_census": exhaustive_census(),
        "documentary_sources": list(SOURCES),
        "artifact_sha256_lf": {
            path.relative_to(ROOT).as_posix(): digest(path.read_bytes())
            for path in (NOTE, Path(__file__), TEST, MANIFEST)
        },
    }
    report["payload_sha256"] = digest(render(report).encode())
    return report


def validate_report(report: object) -> None:
    if render(report) != render(build_report()):
        raise ValueError("fixture differs from the independently rebuilt exact report")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    args = parser.parse_args()
    report = build_report()
    rendered = render(report)
    if args.write:
        FIXTURE.write_text(rendered, encoding="utf-8", newline="\n")
    elif FIXTURE.read_text(encoding="utf-8") != rendered:
        raise ValueError("fixture is stale or changed; exact replay failed")
    print(
        "family-binding firewall: exact source locks, counterfeits, N-tax and bounded census passed"
    )


if __name__ == "__main__":
    main()
