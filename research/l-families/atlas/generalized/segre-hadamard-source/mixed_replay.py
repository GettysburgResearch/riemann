"""Grouped Chow canonical-character checks and a collision-free degree jump."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from fractions import Fraction
from math import comb, prod
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
TEST = ROOT / "tests/test_segre_hadamard_mixed.py"
FIXTURE = HERE / "mixed.verification.json"
SOURCE = HERE / "sources/T-108510.md"
SOURCE_BLOB = "f6c22bf9116de00959a7024b62faaf3a370f2754"
OWNED = ("MIXED_RANK_CANONICAL_DEGREE.md", "MIXED_REPLAY.md", "mixed_replay.py")


def need(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value, low, high):
    need(
        type(value) is int and low <= value <= high,
        "integer outside grouped source cap",
    )
    return value


def scalar(value):
    need(
        type(value) in (int, Fraction) and value != 0,
        "nonzero exact rational eigenvalue required",
    )
    return Fraction(value)


def compositions(n, d):
    if d == 1:
        return [(n,)]
    return [(a, *b) for a in range(n + 1) for b in compositions(n - a, d - 1)]


def multiply(left, right, cut):
    integer(cut, 0, 32)
    out = [Fraction(0)] * (cut + 1)
    for i, a in enumerate(left[: cut + 1]):
        for j, b in enumerate(right[: cut + 1 - i]):
            out[i + j] += a * b
    return out


def complete_series(values, cut):
    # Independent route from first packet's composition summation.
    out = [Fraction(1)] + [Fraction(0)] * cut
    for value in values:
        out = multiply(out, [value**r for r in range(cut + 1)], cut)
    return out


def elementary(values):
    out = [Fraction(1)]
    for value in values:
        next_row = [Fraction(0)] * (len(out) + 1)
        for i, coefficient in enumerate(out):
            next_row[i] += coefficient
            next_row[i + 1] += value * coefficient
        out = next_row
    return out


def determinant_poly(values):
    return [(-1) ** i * value for i, value in enumerate(elementary(values))]


def validate_groups(groups):
    need(isinstance(groups, (list, tuple)), "group list required")
    integer(len(groups), 1, 3)
    checked = []
    for entry in groups:
        need(
            isinstance(entry, (tuple, list)) and len(entry) == 2,
            "group must contain eigenvalues and multiplicity",
        )
        values, count = entry
        need(isinstance(values, (tuple, list)), "eigenvalue list required")
        integer(len(values), 2, 4)
        integer(count, 1, 4)
        checked.append((tuple(scalar(v) for v in values), count))
    s = prod(comb(len(values) + count - 1, count) for values, count in checked)
    need(s <= 24, "grouped symmetric generator cap")
    return checked


def grouped_numerator(groups):
    groups = validate_groups(groups)
    s = prod(comb(len(values) + count - 1, count) for values, count in groups)
    dimension = 1 + sum(count * (len(values) - 1) for values, count in groups)
    largest = max(len(values) for values, _ in groups)
    degree, cut = s - largest, s - largest + 3
    group_weights = []
    f = [Fraction(1)] * (cut + 1)
    leading = Fraction((-1) ** (s - dimension))
    leading_dimension = 1
    for values, count in groups:
        d = len(values)
        group_weights.append(
            [
                prod(v**a for v, a in zip(values, weight, strict=True))
                for weight in compositions(count, d)
            ]
        )
        h = complete_series(values, cut)
        f = [a * b**count for a, b in zip(f, h, strict=True)]
        need(count * s % d == 0, "canonical determinant exponent not integral")
        exponent = count * s // d - count
        inverse_h = complete_series(tuple(1 / value for value in values), largest - d)[
            -1
        ]
        leading *= prod(values) ** exponent * inverse_h**count
        leading_dimension *= comb(largest - 1, d - 1) ** count
    weights = [prod(entries) for entries in itertools.product(*group_weights)]
    q = determinant_poly(weights)
    n = multiply(q, f, cut)
    need(not any(n[degree + 1 :]), "mixed numerator exceeded canonical degree bound")
    need(n[degree] == leading, "mixed leading canonical character mismatch")
    actual_degree = max(i for i, value in enumerate(n) if value)
    return {
        "groups": groups,
        "s_D_c_M_generic_degree": [s, dimension, s - dimension, largest, degree],
        "actual_numerator_degree": actual_degree,
        "numerator": n[: actual_degree + 1],
        "denominator": q,
        "distinct_generator_weights": len(set(weights)) == len(weights),
        "canonical_leading_character": leading,
        "fixed_top_tor_dimension_at_identity": leading_dimension,
        "tail_checked_through": cut,
    }


def trim(poly):
    out = list(poly)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def polynomial_remainder(left, right):
    a, b = trim(left), trim(right)
    need(any(b), "polynomial division by zero")
    while any(a) and len(a) >= len(b):
        shift, coefficient = len(a) - len(b), a[-1] / b[-1]
        for i, value in enumerate(b):
            a[i + shift] -= coefficient * value
        a = trim(a)
    return a


def polynomial_gcd(left, right):
    a, b = trim([Fraction(v) for v in left]), trim([Fraction(v) for v in right])
    while any(b):
        a, b = b, polynomial_remainder(a, b)
    return [value / a[-1] for value in a]


def collision_free_degree_drop(values=(5, 7, 11, 13), cut=12):
    need(
        isinstance(values, (tuple, list)) and len(values) == 4,
        "four positive distinct values required",
    )
    values = tuple(scalar(v) for v in values)
    need(
        all(v > 0 for v in values) and len(set(values)) == 4,
        "four positive distinct values required",
    )
    integer(cut, 9, 20)
    h_a = [Fraction(1), Fraction(1)]
    for _ in range(2, cut + 1):
        h_a.append(h_a[-1] - h_a[-2])
    h_b = complete_series(values, cut)
    f = [a * b for a, b in zip(h_a, h_b, strict=True)]
    q = [Fraction(1)]
    for value in values:
        q = multiply(q, [1, -value, value**2], min(len(q) + 1, cut))
    n = multiply(q, f, cut)
    e = elementary(values)
    expected = [1, 0, -e[2], e[3]] + [0] * (cut - 3)
    need(n == expected, "actual companion-source degree-drop identity")
    gcd = polynomial_gcd(q, n)
    need(
        gcd == [1],
        "degree drop incorrectly introduced numerator/denominator cancellation",
    )
    derivative = [i * q[i] for i in range(1, len(q))]
    need(
        polynomial_gcd(q, derivative) == [1], "eight denominator poles are not distinct"
    )
    need(len(q) == 9 and n[3] != 0, "exact denominator/numerator degree")
    return {
        "A": [[0, -1], [1, 1]],
        "B_diagonal": values,
        "source_h_A": h_a,
        "denominator": q,
        "numerator": n[:4],
        "gcd_N_Q": gcd,
        "gcd_Q_derivative": [1],
        "generic_vs_actual_degree_deficit": [4, 5],
        "all_eight_poles_distinct_and_retained": True,
        "source_top_tor_space_removed": False,
    }


def build():
    b = (5, 7, 11)
    first = grouped_numerator([((2, 3), 2), (b, 1)])
    need(first["s_D_c_M_generic_degree"] == [9, 5, 4, 3, 6], "first grouped geometry")
    need(
        first["canonical_leading_character"] == 6**5 * prod(b) ** 2 * 5**2,
        "first explicit leading character",
    )
    reversed_counts = grouped_numerator([((2, 3), 1), (b, 2)])
    need(
        reversed_counts["s_D_c_M_generic_degree"] == [12, 6, 6, 3, 9],
        "heldout grouped geometry",
    )
    need(
        reversed_counts["canonical_leading_character"] == 6**4 * prod(b) ** 6 * 5,
        "heldout explicit leading character",
    )
    trace_zero = grouped_numerator([((1, -1), 2), (b, 1)])
    cut = trace_zero["tail_checked_through"]
    expected = trim(multiply(determinant_poly(b), [1, 0, elementary(b)[2]], cut))
    need(
        trace_zero["numerator"] == expected
        and trace_zero["actual_numerator_degree"] == 5,
        "trace-zero exact lower-degree numerator",
    )
    trace_zero_heldout = grouped_numerator([((1, -1), 1), (b, 2)])
    need(
        trace_zero_heldout["canonical_leading_character"] == 0,
        "heldout top character not zero",
    )
    need(
        all(
            value == 0
            for i, value in enumerate(trace_zero_heldout["numerator"])
            if i % 2
        ),
        "heldout source evenness",
    )
    deformation = []
    for parameter in (-3, -2, -1, 1, 2, 3):
        row = grouped_numerator([((1, parameter), 2), (b, 1)])
        predicted = Fraction(parameter) ** 5 * prod(b) ** 2 * (1 + parameter) ** 2
        need(
            row["canonical_leading_character"] == predicted,
            "deformation's canonical leading character",
        )
        deformation.append(
            {
                "parameter": parameter,
                "leading_character": predicted,
                "actual_degree": row["actual_numerator_degree"],
                "top_space_dimension": row["fixed_top_tor_dimension_at_identity"],
            }
        )
    return {
        "status": "exact bounded grouped-source comparison; all-grade proof separate",
        "generic_comparison": first,
        "multiplicity_reversed_heldout": reversed_counts,
        "trace_zero_comparison": trace_zero,
        "trace_zero_heldout": trace_zero_heldout,
        "deformation": deformation,
        "degree_loss_without_pole_collision": collision_free_degree_drop(),
        "full_resolution_computed": False,
        "scalar_degree_loss_implies_betti_jump": False,
    }


def encode(value):
    if isinstance(value, Fraction):
        return (
            value.numerator
            if value.denominator == 1
            else f"{value.numerator}/{value.denominator}"
        )
    if isinstance(value, dict):
        return {str(k): encode(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [encode(v) for v in value]
    return value


def digest(data):
    return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()


def payload():
    source = SOURCE.read_bytes().replace(b"\r\n", b"\n")
    blob = hashlib.sha1(
        b"blob " + str(len(source)).encode() + b"\0" + source
    ).hexdigest()
    need(blob == SOURCE_BLOB, "frozen degree-deficit source mismatch")
    hashes = {name: digest((HERE / name).read_bytes()) for name in OWNED}
    hashes[str(TEST.relative_to(ROOT)).replace("\\", "/")] = digest(TEST.read_bytes())
    record = encode(
        {
            "source": {
                "commit": "ac1cc5eaf229087b6d805e908897c7c8c99a58b7",
                "path": "claims/theorems/T-108510-defect-codimension-law.md",
                "git_blob": blob,
            },
            "owned_sha256_canonical_lf": hashes,
            "result": build(),
        }
    )
    record["proof_object_sha256"] = hashlib.sha256(
        json.dumps(record, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    return record


def canonical_json(record):
    return json.dumps(record, sort_keys=True, separators=(",", ":"), allow_nan=False)


def check_payload(candidate):
    need(
        canonical_json(candidate) == canonical_json(payload()),
        "mixed source replay differs from fixture",
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    record = payload()
    if args.write:
        FIXTURE.write_text(
            json.dumps(record, sort_keys=True, indent=2) + "\n", encoding="utf-8"
        )
    else:
        need(FIXTURE.exists(), "mixed source fixture missing")
        need(
            canonical_json(json.loads(FIXTURE.read_text(encoding="utf-8")))
            == canonical_json(record),
            "mixed source replay differs from fixture",
        )
    print(f"PASS {record['proof_object_sha256']}")


if __name__ == "__main__":
    main()
