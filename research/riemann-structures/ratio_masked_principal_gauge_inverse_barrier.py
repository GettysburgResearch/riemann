#!/usr/bin/env python3
"""Prime-certified balanced-source embedding of a true ratio-masked gauge inverse."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import permutations
from math import comb, factorial, gcd, isqrt, prod
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
NOTE = HERE / "RATIO_MASKED_PRINCIPAL_GAUGE_INVERSE_BARRIER.md"
FIXTURE = HERE / "ratio_masked_principal_gauge_inverse_barrier.json"
CERTIFICATES = HERE / "masked_gauge_inverse_prime_certificates.json"
SCOUT = HERE / "masked_gauge_inverse_scout.py"
TEST = ROOT / "tests" / "test_ratio_masked_principal_gauge_inverse_barrier.py"
OLD = "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc"
FAMILY = "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b"
SOURCES = {
    (
        OLD,
        "claims/lemmas/L-102706-euler-half-divisor-homotopies-are-subcritically-gauge-equivalent.md",
    ): "6192bec36636e2d35b2aba4fdd64eb4bcf93c2d9",
    (
        FAMILY,
        "claims/lemmas/L-106080-squarefree-boolean-vaughan-keeps-the-balanced-core-literal.md",
    ): "346cc52420ec65457c2a5accc045d4a85635cc24",
    (
        FAMILY,
        "claims/lemmas/L-106090-least-discrepancy-prime-triangularizes-the-coprime-boolean-core.md",
    ): "dadf3a4a65d2575983d692dafc0c94142c9a038d",
    (
        FAMILY,
        "claims/lemmas/L-106120-bilateral-least-prime-phases-form-a-tensor-kummer-family.md",
    ): "a8d829dc10611adb7bfb4853902bdff0ab02a065",
    (
        FAMILY,
        "claims/lemmas/L-106121-bilateral-tensor-moment-has-a-paid-atomic-diagonal.md",
    ): "955c3ed0363ca330439eedbae1bf0041a4c96468",
    (
        FAMILY,
        "claims/theorems/T-106140-wick-centered-additive-kummer-conjunction-frontier.md",
    ): "d5be8e376c88b63de0be19e0d9e8791624e99ae2",
    (
        "1c9b5cf8aefcb9440dd96feea57c950c15a5b290",
        "research/riemann-structures/PHASE_PROTECTED_PRINCIPAL_GAUGE_TRANSFER.md",
    ): "972c51d17923b0f7bc056c0cb28dd35bca871850",
}
MAX_BYTES = 262144
MAX_DIM = 32
P, Q = 31 * 37, 11 * 17
ELL, RHO = 5, 13
A_TAU = Fraction(-1, 16)
ZERO, ONE = Fraction(0), Fraction(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def canonical(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def source_bytes(key):
    require(key in SOURCES, "frozen source identity")
    ref = f"{key[0]}:{key[1]}"
    size = int(
        subprocess.run(
            ["git", "cat-file", "-s", ref],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout
    )
    require(0 < size <= MAX_BYTES, "source byte cap")
    raw = subprocess.run(
        ["git", "show", ref], cwd=ROOT, capture_output=True, check=True
    ).stdout
    require(len(raw) == size, "source byte count")
    digest = sha1(b"blob " + str(size).encode() + b"\0" + raw).hexdigest()
    require(digest == SOURCES[key], "frozen source Git blob")
    return raw


def trial_prime(n: int):
    require(type(n) is int and 2 <= n <= 1000300, "small-prime type/range")
    return all(n % d for d in range(2, isqrt(n) + 1))


def proth_certificate(record):
    require(type(record) is dict, "Proth certificate object")
    fields = ("prime", "odd_multiplier", "power_of_two", "witness")
    require(all(type(record.get(key)) is int for key in fields), "Proth integer fields")
    n, k, exponent, witness = (record[key] for key in fields)
    require(
        2 <= exponent <= 128 and 0 < k < (1 << exponent) and k % 2 == 1,
        "Proth exponent/multiplier range",
    )
    require(
        n == k * (1 << exponent) + 1 and n.bit_length() <= 256,
        "literal Proth factorization",
    )
    require(2 <= witness <= 64 and gcd(witness, n) == 1, "bounded Proth witness")
    require(pow(witness, (n - 1) // 2, n) == n - 1, "Proth primality certificate")
    return n


def certificate_panel(data):
    require(
        type(data) is dict and type(data.get("m")) is int and data["m"] == 3,
        "fixed bounded source panel",
    )
    small = data.get("small_primes")
    require(
        type(small) is list and len(small) == 6 and len(set(small)) == 6,
        "six distinct small labels",
    )
    require(all(trial_prime(p) for p in small), "complete small primality")
    require(
        min(small) > 67 and 300 * (max(small) - min(small)) < min(small),
        "strict narrow prime window",
    )
    t = prod(small)
    require(
        type(data.get("T")) is int and data["T"] == t, "literal variable prime product"
    )
    backgrounds = data.get("backgrounds")
    require(
        type(backgrounds) is dict and set(backgrounds) == {"A", "B", "C", "D"},
        "four background certificates",
    )
    big = {}
    for key, lo, hi in (
        ("A", 1000, 1050),
        ("B", 1050, 1100),
        ("C", 1100, 1150),
        ("D", 1150, 1200),
    ):
        big[key] = proth_certificate(backgrounds[key])
        require(lo * t < big[key] < hi * t, "strict source background window")
    require(len(set(big.values())) == 4, "distinct certified backgrounds")
    return tuple(small[:3]), tuple(small[3:]), big, t


def sixth_root(n: int):
    require(type(n) is int and 1 <= n and n.bit_length() <= 2048, "horizon integer cap")
    lo, hi = 0, 1 << ((n.bit_length() + 5) // 6)
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid**6 <= n:
            lo = mid
        else:
            hi = mid
    return hi if hi**6 <= n else lo


def record(i: int, j: int, r, s, big):
    require(
        type(i) is int and type(j) is int and 0 <= i < 8 and 0 <= j < 8,
        "bounded Boolean coordinates",
    )
    left = (ELL, big["A"], big["B"]) + r + tuple(s[k] for k in range(3) if i >> k & 1)
    right = (RHO, big["C"], big["D"]) + s + tuple(r[k] for k in range(3) if j >> k & 1)
    common = set(left).intersection(right)
    c, d = set(left) - common, set(right) - common
    require(min(c) == ELL and min(d) == RHO, "unchanged native selectors")
    g = prod(common)
    a, b = prod(left), prod(right)
    n, m = P * a * a, Q * b * b
    weight = Fraction(g * g * ELL * RHO * (ELL + 1) * (RHO + 1), (ELL - 1) * (RHO - 1))
    return {
        "I": i,
        "J": j,
        "left": list(left),
        "right": list(right),
        "g": g,
        "N": n,
        "M": m,
        "weight": str(weight),
        "ratio": str(Fraction(n, m)),
        "ranks": [i.bit_count(), j.bit_count()],
    }


def boolean_histories(labels, cutoff):
    require(
        type(labels) is tuple
        and 1 <= len(labels) <= 9
        and len(set(labels)) == len(labels),
        "complete Boolean label cap",
    )
    require(
        all(type(p) is int and p > 1 and p.bit_length() <= 256 for p in labels),
        "bounded physical labels",
    )
    require(
        type(cutoff) is int and 1 <= cutoff and cutoff.bit_length() <= 256,
        "Boolean cutoff cap",
    )
    count = 1 << len(labels)
    products = [1] * count
    for mask in range(1, count):
        bit = mask & -mask
        products[mask] = products[mask ^ bit] * labels[bit.bit_length() - 1]
    a = []
    for mask in range(count):
        total, sub = 0, mask
        while True:
            if products[sub] <= cutoff:
                total += (-1) ** sub.bit_count()
            if sub == 0:
                break
            sub = (sub - 1) & mask
        a.append(int(mask == 0) - total)
    histories, total = [], 0
    full = count - 1
    for first in range(count):
        available = full ^ first
        second = available
        while True:
            third = available ^ second
            value = a[first] * a[second] * (-1) ** third.bit_count()
            total += value
            if value:
                histories.append(
                    {
                        "groups": [
                            [labels[k] for k in range(len(labels)) if mask >> k & 1]
                            for mask in (first, second, third)
                        ],
                        "coefficient": value,
                    }
                )
            if second == 0:
                break
            second = (second - 1) & available
    return {
        "balanced": total,
        "histories": histories,
        "complete_allocations": 3 ** len(labels),
    }


def segre_mu(bound: int):
    require(type(bound) is int and 0 <= bound <= 64, "Möbius recurrence cap")
    values = [1]
    for m in range(1, bound + 1):
        values.append(-sum(comb(m, j) ** 2 * values[j] for j in range(m)))
    return values


def no_common_ascent_count(m: int):
    require(type(m) is int and 1 <= m <= 4, "permutation count cap")
    ascents = []
    for permutation in permutations(range(m)):
        ascents.append(
            sum(1 << i for i in range(m - 1) if permutation[i] < permutation[i + 1])
        )
    return sum(a & b == 0 for a in ascents for b in ascents)


def identity(n):
    require(type(n) is int and 0 < n <= MAX_DIM, "matrix dimension cap")
    return [[Fraction(i == j) for j in range(n)] for i in range(n)]


def multiply(left, right):
    n = len(left)
    require(
        0 < n <= MAX_DIM
        and len(right) == n
        and all(len(row) == n for row in left + right),
        "bounded square matrices",
    )
    return [
        [sum((left[i][k] * right[k][j] for k in range(n)), ZERO) for j in range(n)]
        for i in range(n)
    ]


def inverse_lower(matrix):
    n = len(matrix)
    require(
        0 < n <= MAX_DIM and all(len(row) == n for row in matrix), "inverse matrix cap"
    )
    require(
        all(type(x) is Fraction for row in matrix for x in row),
        "exact inverse arithmetic",
    )
    require(
        all(
            matrix[i][i] == 1 and all(matrix[i][j] == 0 for j in range(i + 1, n))
            for i in range(n)
        ),
        "unit lower-triangular source",
    )
    inverse = identity(n)
    for i in range(n):
        for j in range(i):
            inverse[i][j] = -sum(
                (matrix[i][k] * inverse[k][j] for k in range(j, i)), ZERO
            )
    return inverse


def panel_matrices(r, s, big, t):
    horizon = 31603 * (big["C"] * big["D"] * t) ** 2
    cutoff = sixth_root(horizon)
    require(13 * t < cutoff < min(big.values()), "native balanced cutoff windows")
    records = [record(i, j, r, s, big) for i in range(8) for j in range(8)]
    for row in records:
        require(max(row["N"], row["M"]) <= horizon, "global physical horizon")
        require(
            row["g"] <= t and 4 * row["g"] < cutoff**2,
            "common core stays below native large-core gate",
        )
        for side, first, second in (("left", "A", "B"), ("right", "C", "D")):
            small = prod(row[side]) // (big[first] * big[second])
            require(small <= 13 * t < cutoff, "all small divisors below cutoff")
        passes = Fraction(1, 8) < Fraction(row["ratio"]) < 8
        require(
            passes == (row["ranks"][0] == row["ranks"][1]),
            "literal ratio mask equals Segre ranks",
        )
    selected = sorted(
        (row for row in records if row["ranks"][0] == row["ranks"][1]),
        key=lambda row: (row["ranks"][0], row["I"], row["J"]),
    )
    require(len(selected) == 20, "complete rank-balanced panel")
    matrix = []
    for target in selected:
        row = []
        for origin in selected:
            if (
                origin["I"] & target["I"] != origin["I"]
                or origin["J"] & target["J"] != origin["J"]
            ):
                row.append(ZERO)
                continue
            newly_left = tuple(
                s[k] for k in range(3) if (target["I"] ^ origin["I"]) >> k & 1
            )
            newly_right = tuple(
                r[k] for k in range(3) if (target["J"] ^ origin["J"]) >> k & 1
            )
            inserted = newly_left + newly_right
            raw = prod((A_TAU / p for p in inserted), start=ONE)
            norm_ratio = Fraction(target["g"], origin["g"])
            require(
                Fraction(target["weight"]) / Fraction(origin["weight"])
                == norm_ratio**2,
                "native principal weight ratio",
            )
            weighted = raw * norm_ratio
            require(
                weighted == A_TAU ** len(inserted),
                "all reciprocal-prime activity paid exactly",
            )
            row.append(weighted)
        matrix.append(row)
    inverse = inverse_lower(matrix)
    require(
        multiply(matrix, inverse) == identity(20)
        and multiply(inverse, matrix) == identity(20),
        "true two-sided masked inverse",
    )
    mu = segre_mu(3)
    for i, target in enumerate(selected):
        for j, origin in enumerate(selected):
            comparable = (
                origin["I"] & target["I"] == origin["I"]
                and origin["J"] & target["J"] == origin["J"]
            )
            depth = target["ranks"][0] - origin["ranks"][0]
            expected = mu[depth] * A_TAU ** (2 * depth) if comparable else ZERO
            require(
                inverse[i][j] == expected,
                "all inverse entries equal weighted Segre Möbius",
            )
    return horizon, cutoff, records, selected, matrix, inverse


def build():
    for key in SOURCES:
        source_bytes(key)
    require(CERTIFICATES.stat().st_size <= MAX_BYTES, "certificate artifact cap")
    certificate_data = json.loads(CERTIFICATES.read_text(encoding="utf-8"))
    r, s, big, t = certificate_panel(certificate_data)
    horizon, cutoff, records, selected, matrix, inverse = panel_matrices(r, s, big, t)
    endpoints = {}
    for name, row in (("bottom", selected[0]), ("top", selected[-1])):
        endpoints[name] = {}
        for side in ("left", "right"):
            replay = boolean_histories(tuple(row[side]), cutoff)
            require(
                len(replay["histories"]) == 2 and abs(replay["balanced"]) == 2,
                "complete endpoint Boolean allocation",
            )
            endpoints[name][side] = replay
    mu = segre_mu(64)
    permutation_controls = {str(m): no_common_ascent_count(m) for m in range(1, 5)}
    require(
        all(permutation_controls[str(m)] == (-1) ** m * mu[m] for m in range(1, 5)),
        "independent permutation interpretation",
    )
    for m in range(1, 65):
        require(
            factorial(m) ** 2 <= abs(mu[m]) * 2 ** (m - 1)
            and abs(mu[m]) <= factorial(m) ** 2,
            "finite elementary factorial inequalities",
        )
    lower64 = Fraction(factorial(64) ** 2, 2**63 * 16**128)
    require(lower64 > 1, "factorial lower bound beats all gauge activity")
    require(
        inverse[-1][0] == Fraction(-19, 16**6),
        "exact small physical panel inverse entry",
    )
    hashes = {}
    for path in (NOTE, Path(__file__), CERTIFICATES, SCOUT, TEST):
        raw = path.read_bytes()
        require(len(raw) <= MAX_BYTES, "local source cap")
        hashes[path.relative_to(ROOT).as_posix()] = sha256(
            raw.replace(b"\r\n", b"\n")
        ).hexdigest()
    result = {
        "schema": "riemann.ratio_masked_principal_gauge_inverse.v1",
        "sources": [
            {"commit": key[0], "path": key[1], "git_blob": blob}
            for key, blob in SOURCES.items()
        ],
        "source_hashes": hashes,
        "prime_certificates": certificate_data,
        "horizon": horizon,
        "frozen_Boolean_cutoff": cutoff,
        "all_interval_records": records,
        "ratio_mask_dimension": 20,
        "complete_endpoint_Boolean_replays": endpoints,
        "weighted_true_inverse_bottom_top": str(inverse[-1][0]),
        "matrix_sha256": sha256(
            canonical([[str(x) for x in row] for row in matrix]).encode()
        ).hexdigest(),
        "inverse_sha256": sha256(
            canonical([[str(x) for x in row] for row in inverse]).encode()
        ).hexdigest(),
        "mobius_first_13": mu[:13],
        "permutation_count_controls": permutation_controls,
        "activity_paid_elementary_lower_bound_m64": str(lower64),
        "m64_is_combinatorial_control_not_large_physical_fixture": True,
        "all_records_are_Boolean_balanced_at_one_cutoff": True,
        "common_core_below_cutoff_squared_over_four": True,
        "same_unchanged_narrow_shell_asserted": False,
        "full_canonical_source_vector_counterexample_asserted": False,
        "cofinal_inverse_exponent": "1/12; proved, not fitted",
        "RH_conclusion": False,
    }
    result["proof_object_sha256"] = sha256(canonical(result).encode()).hexdigest()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.write:
        FIXTURE.write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
    else:
        require(FIXTURE.stat().st_size <= MAX_BYTES, "artifact cap")
        candidate = json.loads(FIXTURE.read_text(encoding="utf-8"))
        require(canonical(candidate) == canonical(result), "exact canonical replay")
    print(
        json.dumps(
            {"status": "PASS", "proof_object_sha256": result["proof_object_sha256"]}
        )
    )


if __name__ == "__main__":
    main()
