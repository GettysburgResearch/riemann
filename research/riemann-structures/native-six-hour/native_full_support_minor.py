"""Fixed positive-shift native minor; exact arithmetic, no adaptive search."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
REL = "research/riemann-structures/native-six-hour/"
OWNED = (
    REL + "native_full_support_minor.py",
    REL + "FULL_SUPPORT_MINOR_PREREGISTRATION.md",
    REL + "FULL_SUPPORT_MINOR_REPLAY.md",
    "tests/test_native_six_hour_full_support_minor.py",
)
PINS = (
    (
        "822646ffea23d906c385f0273a8c45693e982c4d",
        REL + "FIXED_PRIME_INFINITE_HORIZON_COMPLETION.md",
        "851e4331c12d9f3f073ab73dca26baa33bd5e548",
    ),
    (
        "822646ffea23d906c385f0273a8c45693e982c4d",
        REL + "INFINITE_NATIVE_PHYSICAL_FAITHFULNESS.md",
        "f7c42135e276a34d4da00279110666b0f4636080",
    ),
    (
        "3ba479241acf9db1554af067d5e2bea85533dde5",
        REL + "native_physical_tail_scout.py",
        "24ef243220c8159f78505717d639d88287fbf439",
    ),
)
PRIMES = (2, 3, 5)
SHIFTS = (1, 2, 3, 4)
CUTOFF = 64
COEFFICIENT_CAP = 80
BIT_CAP = 4096
ARTIFACT_CAP = 2 * 1024 * 1024
OUT = HERE / "native_full_support_minor.verification.json"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def literal_int(value, low, high):
    require(type(value) is int and low <= value <= high, "literal integer/cap")
    return value


def bounded(value):
    value = Fraction(value)
    require(
        max(abs(value.numerator).bit_length(), value.denominator.bit_length())
        <= BIT_CAP,
        "stored exact-number bit cap",
    )
    return value


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def strict_json(raw):
    def unique_object(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, "duplicate JSON object key")
            result[key] = value
        return result

    def refuse_number(token):
        raise ValueError(f"noninteger JSON number: {token}")

    return json.loads(
        raw,
        object_pairs_hook=unique_object,
        parse_float=refuse_number,
        parse_constant=refuse_number,
    )


def encoded(value):
    if isinstance(value, Fraction):
        bounded(value)
        return [value.numerator, value.denominator]
    if isinstance(value, dict):
        return {key: encoded(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [encoded(item) for item in value]
    return value


def authenticate():
    records = []
    for commit, path, expected in PINS:
        result = subprocess.run(
            ["git", "show", f"{commit}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
        )
        raw = result.stdout
        actual = hashlib.sha1(
            b"blob " + str(len(raw)).encode() + b"\0" + raw
        ).hexdigest()
        require(actual == expected, "frozen source identity")
        records.append({"commit": commit, "path": path, "blob": actual})
    return records


def ownership():
    return {
        path: hashlib.sha256(
            (ROOT / path).read_bytes().replace(b"\r\n", b"\n")
        ).hexdigest()
        for path in OWNED
    }


def coefficients(limit):
    literal_int(limit, 0, COEFFICIENT_CAP)
    c = [Fraction(1)]
    for n in range(1, limit + 1):
        c.append(bounded(c[-1] * Fraction(2 * n - 3, 2 * n)))
    a = [c[n // 2] if n % 2 == 0 else Fraction(0) for n in range(limit + 1)]
    require(all(abs(value) <= 1 for value in a + c), "coefficient bound")
    return a, c


def local_matrix(prime, cutoff=CUTOFF, shifts=SHIFTS):
    require(type(prime) is int and prime in PRIMES, "fixed prime")
    literal_int(cutoff, 0, CUTOFF)
    require(type(shifts) is tuple and shifts == SHIFTS, "fixed shifts only")
    require(all(type(value) is int for value in shifts), "typed shifts")
    f = coefficients(cutoff + max(shifts))
    q = Fraction(1, prime)
    rows = []
    for beta in shifts:
        rows.append(
            [
                bounded(
                    sum(
                        (q**k * f[i][k] * f[j][k + beta] for k in range(cutoff + 1)),
                        Fraction(),
                    )
                )
                for i, j in ((0, 0), (0, 1), (1, 0), (1, 1))
            ]
        )
    return rows


def multiply(left, right):
    require(
        bool(left) and bool(right) and len(left[0]) == len(right), "matrix dimensions"
    )
    return [
        [
            bounded(
                sum((left[i][k] * right[k][j] for k in range(len(right))), Fraction())
            )
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def identity(size):
    return [[Fraction(int(i == j)) for j in range(size)] for i in range(size)]


def inverse(matrix):
    n = len(matrix)
    require(
        1 <= n <= 4 and all(len(row) == n for row in matrix), "inverse dimension cap"
    )
    work = [
        [bounded(value) for value in row] + unit
        for row, unit in zip(matrix, identity(n))
    ]
    for col in range(n):
        pivot = next((row for row in range(col, n) if work[row][col]), None)
        if pivot is None:
            return None
        work[col], work[pivot] = work[pivot], work[col]
        scale = work[col][col]
        work[col] = [bounded(value / scale) for value in work[col]]
        for row in range(n):
            if row != col and work[row][col]:
                scale = work[row][col]
                work[row] = [
                    bounded(x - scale * y) for x, y in zip(work[row], work[col])
                ]
    result = [row[n:] for row in work]
    require(multiply(matrix, result) == identity(n), "right inverse identity")
    require(multiply(result, matrix) == identity(n), "left inverse identity")
    return result


def infinity_norm(matrix):
    return max(sum((abs(value) for value in row), Fraction()) for row in matrix)


def compare_tail(matrix, entry_tail):
    entry_tail = bounded(entry_tail)
    require(entry_tail >= 0, "nonnegative tail")
    inv = inverse(matrix)
    if inv is None:
        return {
            "status": "UNKNOWN_SINGULAR_PARTIAL",
            "inverse": None,
            "entry_tail": entry_tail,
        }
    n = len(matrix)
    row_bounds = [
        bounded(n * entry_tail * sum((abs(value) for value in row), Fraction()))
        for row in inv
    ]
    eta = max(row_bounds)
    result = {
        "status": "CERTIFIED_LOCAL" if eta < 1 else "UNKNOWN_TAIL_NOT_CONTRACTIVE",
        "inverse": inv,
        "entry_tail": entry_tail,
        "comparison_row_sums": row_bounds,
        "eta": eta,
        "partial_inverse_infinity_norm": bounded(infinity_norm(inv)),
    }
    if eta < 1:
        upper = bounded(infinity_norm(inv) / (1 - eta))
        result["infinite_inverse_upper"] = upper
        result["infinite_inverse_integer_upper"] = (
            upper.numerator + upper.denominator - 1
        ) // upper.denominator
    return result


def threshold(inverse_upper):
    inverse_upper = bounded(inverse_upper)
    require(inverse_upper > 0, "positive inverse bound")
    # Unscaled 64-row ratio matrix, in the declared (A,C) tensor basis.
    dimension, coefficient_sum, bmax_sqrt = 64, 64, 900
    tail_constant = dimension * bmax_sqrt * coefficient_sum**2
    square = bounded((2 * inverse_upper * tail_constant) ** 2)
    horizon = square.numerator // square.denominator + 1
    literal_int(horizon, 1, 1 << BIT_CAP)
    bounded(horizon)
    require(Fraction(horizon) > square, "strict half-contraction threshold")
    return {
        "dimension": dimension,
        "source_coefficient_l1_sum": coefficient_sum,
        "largest_denominator": bmax_sqrt**2,
        "global_tail_constant": tail_constant,
        "inverse_infinity_upper": inverse_upper,
        "strict_square_bound": square,
        "all_integer_horizons_at_least": horizon,
        "comparison_strictly_below": Fraction(1, 2),
    }


def validate_record(candidate, fresh):
    require(canonical(candidate) == canonical(fresh), "strict typed canonical replay")


def build():
    sources = authenticate()
    panels = []
    for prime in PRIMES:
        matrix = local_matrix(prime)
        q = Fraction(1, prime)
        tail = bounded(q ** (CUTOFF + 1) / (1 - q))
        panel = {"prime": prime, "q": q, "shifts": SHIFTS, "partial_matrix": matrix}
        panel.update(compare_tail(matrix, tail))
        panels.append(panel)
    certified = all(panel["status"] == "CERTIFIED_LOCAL" for panel in panels)
    result = {
        "schema": "native-fixed-positive-shifts-v1",
        "source": sources,
        "owned_sha256": ownership(),
        "status": "CERTIFIED_FULL_SUPPORT_THRESHOLD"
        if certified
        else "UNKNOWN_FIXED_SHIFTS",
        "cutoff": CUTOFF,
        "coefficient_limit": CUTOFF + max(SHIFTS),
        "column_order": ["AA", "AC", "CA", "CC"],
        "local_panels": panels,
        "rows": [
            {"beta": [a, b, c], "denominator": 2**a * 3**b * 5**c}
            for a in SHIFTS
            for b in SHIFTS
            for c in SHIFTS
        ],
        "scope": {
            "unscaled_ratio_rows": True,
            "physical_row_scaling": "1/sqrt(b)",
            "original_path_tensor": "M_ab=2 integral d(u^a) u^b",
            "declared_basis_path_tensor": (
                "M_AC=T^t M T; T=[[1,0],[-1,1]] tensor power 3; "
                "equivalently 2 integral d(psi_a) psi_b with local psi=(1-u,u)"
            ),
            "old_minor_changed": False,
            "adaptive_shift_selection": False,
            "full_retained_gamma_decoder": False,
        },
    }
    if certified:
        result["finite_horizon_certificate"] = threshold(
            math.prod(panel["infinite_inverse_integer_upper"] for panel in panels)
        )
    result = encoded(result)
    result["proof_object_sha256"] = hashlib.sha256(
        canonical(result).encode()
    ).hexdigest()
    require(len(canonical(result).encode()) <= ARTIFACT_CAP, "artifact byte cap")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args()
    fresh = build()
    if args.write:
        OUT.write_text(
            json.dumps(fresh, sort_keys=True, indent=2, allow_nan=False) + "\n",
            encoding="utf-8",
        )
    else:
        require(OUT.stat().st_size <= ARTIFACT_CAP, "input byte cap")
        validate_record(strict_json(OUT.read_text(encoding="utf-8")), fresh)
    print(
        canonical(
            {
                "status": fresh["status"],
                "proof": fresh["proof_object_sha256"],
                "output": str(OUT),
            }
        )
    )


if __name__ == "__main__":
    main()
