"""Read-only exact diagnostics for the frozen singular-limit minor experiment."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction as F
from hashlib import sha1, sha256
from itertools import combinations, product
from math import isqrt
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PREFIX = "research/riemann-structures/native-six-hour/"
MAX_BYTES = 16 * 1024 * 1024
CAPTURE_PROOF = "aa3f9ad57373bb321996f9e5615652ec5322ef8e0147af5fd18c51cf93f0f2a1"
PINS = (
    (
        "utility",
        "63e1742ec319c532baa36f6568809f6a6b32e6e2",
        PREFIX + "native_physical_tail_extension.py",
        "bb69109f81bca6e814a87c82be86ac7b92934d27",
    ),
    (
        "capture",
        "987ccb82d0bf097942389027c6e785925847e6a7",
        PREFIX + "native_physical_tail_extension.extension.json",
        "98e4df4711a418f8ef3c084e5596ba0be7aaa69e",
    ),
    (
        "proof",
        "78918a6f3297d4c88b3b3c42140eba4c0f11778e",
        PREFIX + "NATIVE_FIXED_MINOR_INFINITY_DEFECT.md",
        "70691bb9cca63cb97b08fac1caf3f5b71bbd949c",
    ),
    (
        "local_source",
        "3ba479241acf9db1554af067d5e2bea85533dde5",
        PREFIX + "native_physical_tail_scout.py",
        "24ef243220c8159f78505717d639d88287fbf439",
    ),
)
OWNED = (
    Path(__file__),
    HERE / "NATIVE_FIXED_MINOR_DIAGNOSTIC_REPLAY.md",
    ROOT / "tests/test_native_six_hour_fixed_minor_diagnostic.py",
)
RATIOS = [
    [1, b]
    for b in (2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 25, 30, 40, 45, 50, 60, 75)
]
INDICES = [0, 3, 5, 12, 2, 6, 8, 1, 13, 4, 15, 25, 7, 16, 14, 18, 20, 22, 24, 26]
ROW_INDICES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 20, 21, 23, 25, 28]
COORDINATES = tuple(
    (i, j, *powers)
    for i, j in combinations(range(3), 2)
    for powers in product(*(range(2) if k in (i, j) else range(3) for k in range(3)))
)
INVERSE_BOUND = F(10**14)
LOCAL_BOUND = F(2)
REMAINDER_BOUND = F(3, 10**25)
ENTRY_FLOOR_BOUND = F(1, 10**23)
COMPARISON_FLOOR_BOUND = F(4, 10**7)


class Refusal(ValueError):
    """An authentication or diagnostic refusal, never a new tail outcome."""


def need(condition, message):
    if not condition:
        raise Refusal(message)


def integer(value, low, high):
    need(type(value) is int and low <= value <= high, "literal bounded integer")
    return value


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def equal(actual, expected):
    need(canonical(actual) == canonical(expected), "complete typed comparison")


def rational(value):
    need(type(value) is str and 0 < len(value) <= 2500, "rational string")
    try:
        result = F(value)
    except (ValueError, ZeroDivisionError) as exc:
        raise Refusal("invalid rational") from exc
    need(
        str(result) == value
        and max(abs(result.numerator).bit_length(), result.denominator.bit_length())
        <= 4096,
        "canonical 4096-bit rational",
    )
    return result


def git_bytes(commit, path, expected):
    need(
        type(commit) is str
        and len(commit) == 40
        and all(c in "0123456789abcdef" for c in commit),
        "exact commit",
    )
    blob = subprocess.check_output(
        ["git", "rev-parse", f"{commit}:{path}"], cwd=ROOT, text=True
    ).strip()
    need(expected is None or blob == expected, "frozen blob")
    size = int(subprocess.check_output(["git", "cat-file", "-s", blob], cwd=ROOT))
    need(0 < size <= MAX_BYTES, "bounded frozen bytes")
    raw = subprocess.check_output(["git", "cat-file", "blob", blob], cwd=ROOT)
    need(
        len(raw) == size
        and sha1(b"blob " + str(size).encode() + b"\0" + raw).hexdigest() == blob,
        "actual git object",
    )
    need(
        raw.replace(b"\r\n", b"\n")
        == (ROOT / path).read_bytes().replace(b"\r\n", b"\n"),
        "current frozen LF bytes",
    )
    return raw, {"commit": commit, "path": path, "blob": blob}


def authenticate():
    raw, provenance = {}, []
    for label, commit, path, expected in PINS:
        raw[label], identity = git_bytes(commit, path, expected)
        provenance.append(identity)
    return raw, provenance


def decode(raw, utility):
    need(type(raw) is bytes and 0 < len(raw) <= MAX_BYTES, "bounded capture")
    try:
        payload = utility.read_json(raw)
        utility.body_check(payload)
    except (ValueError, TypeError, KeyError) as exc:
        raise Refusal("typed complete source digest") from exc
    need(payload["proof_object_sha256"] == CAPTURE_PROOF, "exact captured proof")
    return payload


def source():
    raw, provenance = authenticate()
    # No executable compilation or JSON parsing precedes all four authentications.
    namespace = {
        "__name__": "frozen_minor_diagnostic_decoder",
        "__file__": str(ROOT / PINS[0][2]),
    }
    exec(compile(raw["utility"], namespace["__file__"], "exec"), namespace)  # noqa: S102
    utility = SimpleNamespace(**namespace)
    return decode(raw["capture"], utility), provenance, utility


def matrix(raw, nonnegative=False):
    need(type(raw) is list and len(raw) == 20, "twenty matrix rows")
    result = []
    for row in raw:
        need(type(row) is list and len(row) == 20, "twenty matrix columns")
        parsed = [rational(value) for value in row]
        need(
            not nonnegative or all(value >= 0 for value in parsed),
            "nonnegative comparison entries",
        )
        result.append(parsed)
    return result


def scalar_sum(coordinate):
    i, j, *powers = coordinate
    # Literal coefficient sums in D_i N'_j - N'_i D_j.
    return 0 if powers[i] == powers[j] == 1 else 2


def validate_record(payload):
    need(
        type(payload) is dict
        and payload["schema"] == "native-physical-tail-extension-v1"
        and payload["phase"] == "extension"
        and payload["execution_status"] == "PASS",
        "actual frozen campaign identity",
    )
    equal(
        payload["selection"],
        {"coordinate_indices": INDICES, "ratios": RATIOS, "row_indices": ROW_INDICES},
    )
    result = payload["result"]
    integer(result["horizon"], 2**48, 2**48)
    need(result["every_later_partial_prefix_bounded"] is True, "declared tail premise")
    matrix(result["matrix"])
    matrix(result["tail"], True)
    contraction = result["contraction"]
    need(
        contraction["status"] == "UNKNOWN_TAIL_NOT_CONTRACTIVE"
        and contraction["all_future_horizons_certified"] is False
        and contraction["inverse"]["both_products_identity"] is True,
        "unchanged frozen outcome and verified inverse premise",
    )
    inverse = matrix(contraction["inverse"]["matrix"])
    inverse_max = max(abs(value) for row in inverse for value in row)
    need(inverse_max < INVERSE_BOUND, "inverse coarse bound")
    comparison = matrix(contraction["absolute_inverse_times_tail"], True)
    need(
        type(contraction["row_sums"]) is list and len(contraction["row_sums"]) == 20,
        "twenty row sums",
    )
    sums = [rational(value) for value in contraction["row_sums"]]
    need(sums == [sum(row, F()) for row in comparison], "stored comparison row sums")
    need(all(value > 3 for value in sums), "all row sums strictly exceed three")
    theta = rational(contraction["theta"])
    need(theta == max(sums), "recorded maximum norm")
    tables = result["local_tables"]
    need(type(tables) is list and len(tables) == 44, "forty-four frozen local tables")
    keys, uppers, remainders = set(), [], []
    for table in tables:
        prime = integer(table["prime"], 2, 5)
        need(prime in (2, 3, 5), "actual fixed prime")
        alpha = integer(table["alpha"], 0, 0)
        beta = integer(table["beta"], 0, 9)
        kind = integer(table["kind"], 0, 3)
        key = (prime, alpha, beta, kind)
        need(key not in keys, "unique local table")
        keys.add(key)
        terms = table["terms"]
        need(type(terms) is list and len(terms) == 65, "unchanged degree-64 cutoff")
        terms = [rational(value) for value in terms]
        need(all(value >= 0 for value in terms), "positive local majorant")
        partial = rational(table["partial"])
        remainder = rational(table["remainder"])
        upper = rational(table["upper"])
        need(
            partial == sum(terms, F()) and upper == partial + remainder,
            "actual local partial and remainder identity",
        )
        need(
            0 <= upper < LOCAL_BOUND and 0 <= remainder < REMAINDER_BOUND,
            "strict local coarse bounds",
        )
        uppers.append(upper)
        remainders.append(remainder)
    expected_keys = {
        (prime, 0, beta, kind)
        for prime, high in ((2, 4), (3, 2), (5, 2))
        for beta in range(high + 1)
        for kind in range(4)
    }
    need(keys == expected_keys, "complete local shift-kind inventory")
    rows = result["rows"]
    need(type(rows) is list and len(rows) == 20, "twenty actual alias rows")
    maximum_alias, maximum_cutoff, alias_count = 0, 0, 0
    for index, row in enumerate(rows):
        equal(row["ratio"], RATIOS[index])
        aliases = row["alias_indices"]
        need(type(aliases) is list and 0 < len(aliases) <= 4400, "bounded alias list")
        previous = 0
        for value in aliases:
            value = integer(value, 1, 2**24)
            need(
                value > previous and value * value * RATIOS[index][1] <= 2**48,
                "sorted actual hyperbolic aliases",
            )
            smooth = value
            for prime in (2, 3, 5):
                while smooth % prime == 0:
                    smooth //= prime
            need(smooth == 1, "fixed-prime support")
            previous = value
        integer(row["alias_count"], len(aliases), len(aliases))
        cutoff = isqrt(2**48 // RATIOS[index][1])
        integer(row["maximum_alias"], cutoff, cutoff)
        need(previous <= cutoff, "last smooth alias is within the integer cutoff")
        equal(row["tail"], result["tail"][index])
        for field in ("positive_prefix", "infinite_majorant_upper"):
            need(
                type(row[field]) is list and len(row[field]) == 20,
                "twenty prefix/upper entries",
            )
        prefix = [rational(value) for value in row["positive_prefix"]]
        upper = [rational(value) for value in row["infinite_majorant_upper"]]
        tail = [rational(value) for value in row["tail"]]
        need(
            all(
                a >= 0 and b >= a and b - a == c
                for a, b, c in zip(prefix, upper, tail, strict=True)
            ),
            "same-majorant nonnegative subtraction",
        )
        maximum_alias = max(maximum_alias, previous)
        maximum_cutoff = max(maximum_cutoff, cutoff)
        alias_count += len(aliases)
    scalar_max = max(scalar_sum(COORDINATES[index]) for index in INDICES)
    need(scalar_max <= 2, "actual coordinate scalar coefficient bound")
    product_floor = 2 * 3 * LOCAL_BOUND**2 * REMAINDER_BOUND
    need(product_floor < ENTRY_FLOOR_BOUND, "telescoping entry bound")
    need(
        20**2 * INVERSE_BOUND * ENTRY_FLOOR_BOUND == COMPARISON_FLOOR_BOUND,
        "twenty-by-twenty comparison bound",
    )
    return {
        "diagnostic_status": "PASS",
        "source_status_preserved": contraction["status"],
        "capture_proof_object_sha256": CAPTURE_PROOF,
        "horizon": 2**48,
        "matrix_shape": [20, 20],
        "local_cutoff": 64,
        "local_table_count": len(tables),
        "complete_alias_count": alias_count,
        "maximum_smooth_alias": maximum_alias,
        "maximum_alias_cutoff": maximum_cutoff,
        "maximum_scalar_coefficient_sum": scalar_max,
        "exact_extrema": {
            "maximum_absolute_inverse_entry": str(inverse_max),
            "maximum_local_upper": str(max(uppers)),
            "maximum_local_remainder": str(max(remainders)),
            "minimum_comparison_row_sum": str(min(sums)),
            "comparison_theta": str(theta),
        },
        "strict_coarse_bounds": {
            "absolute_inverse_entry_less_than": str(INVERSE_BOUND),
            "local_upper_less_than": str(LOCAL_BOUND),
            "local_remainder_less_than": str(REMAINDER_BOUND),
            "local_floor_entry_less_than": str(ENTRY_FLOOR_BOUND),
            "inverse_amplified_local_floor_less_than": str(COMPARISON_FLOOR_BOUND),
            "every_positive_diagonal_weighted_comparison_norm_greater_than": "3",
        },
        "scope": {
            "new_source_acquisition": False,
            "inverse_reconstructed": False,
            "source_alias_vectors_replayed": False,
            "tail_method_changed": False,
            "earlier_unknown_overturned": False,
            "all_future_rank_certified": False,
            "uses_previously_verified_frozen_inverse_and_comparison": True,
        },
    }


def build():
    payload, provenance, _utility = source()
    result = {
        "schema": "native-fixed-minor-coarse-diagnostic-v1",
        "execution_status": "PASS",
        "source": provenance,
        "owned_sha256_lf": {
            p.relative_to(ROOT).as_posix(): sha256(
                p.read_bytes().replace(b"\r\n", b"\n")
            ).hexdigest()
            for p in OWNED
        },
        "result": validate_record(payload),
    }
    result["proof_object_sha256"] = sha256(canonical(result).encode()).hexdigest()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    payload = build()
    output = HERE / "native_fixed_minor_diagnostic.json"
    if args.write:
        output.write_text(canonical(payload) + "\n", encoding="utf-8")
    else:
        # Authenticate source again before using its strictly typed decoder.
        _capture, _provenance, utility = source()
        raw = output.read_bytes()
        need(0 < len(raw) <= MAX_BYTES, "bounded diagnostic artifact")
        equal(payload, utility.read_json(raw))
    print(
        canonical(
            {
                "execution_status": "PASS",
                "diagnostic_status": payload["result"]["diagnostic_status"],
                "source_status_preserved": payload["result"]["source_status_preserved"],
                "proof_object_sha256": payload["proof_object_sha256"],
            }
        )
    )


if __name__ == "__main__":
    main()
