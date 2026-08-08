#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
from typing import List, Sequence, Union

Number = Union[int, Fraction]


def mobius_sieve(limit: int) -> List[int]:
    mu = [0] * (limit + 1)
    mu[1] = 1
    primes: List[int] = []
    composite = [False] * (limit + 1)
    for n in range(2, limit + 1):
        if not composite[n]:
            primes.append(n)
            mu[n] = -1
        for p in primes:
            m = n * p
            if m > limit:
                break
            composite[m] = True
            if n % p == 0:
                mu[m] = 0
                break
            mu[m] = -mu[n]
    return mu


def formal_log(n: int) -> int:
    """A completely additive integer-valued stand-in for log(n)."""
    count = 0
    x = n
    p = 2
    while p * p <= x:
        while x % p == 0:
            count += 1
            x //= p
        p += 1 if p == 2 else 2
    if x > 1:
        count += 1
    return count


def convolution(a: Sequence[Number], b: Sequence[Number], limit: int) -> List[Number]:
    out: List[Number] = [0] * (limit + 1)
    nonzero_a = [i for i in range(1, min(limit, len(a) - 1) + 1) if a[i] != 0]
    nonzero_b = [j for j in range(1, min(limit, len(b) - 1) + 1) if b[j] != 0]
    for i in nonzero_a:
        ai = a[i]
        bound = limit // i
        for j in nonzero_b:
            if j > bound:
                break
            out[i * j] += ai * b[j]
    return out


def convolution_power(a: Sequence[Number], exponent: int, limit: int) -> List[Number]:
    out: List[Number] = [0] * (limit + 1)
    out[1] = 1
    for _ in range(exponent):
        out = convolution(out, a, limit)
    return out


def shifted(a: Sequence[Number], q: int, limit: int, coefficient: Number = 1) -> List[Number]:
    out: List[Number] = [0] * (limit + 1)
    for n in range(1, limit // q + 1):
        out[q * n] = coefficient * a[n]
    return out


def add(*arrays: Sequence[Number]) -> List[Number]:
    limit = max(len(a) for a in arrays) - 1
    out: List[Number] = [0] * (limit + 1)
    for a in arrays:
        for i, value in enumerate(a):
            out[i] += value
    return out


def scale(a: Sequence[Number], coefficient: Number) -> List[Number]:
    return [coefficient * value for value in a]


def mismatches(a: Sequence[Number], b: Sequence[Number]) -> int:
    if len(a) != len(b):
        raise ValueError("length mismatch")
    return sum(Fraction(x) != Fraction(y) for x, y in zip(a, b))


def first_nonzero(a: Sequence[Number]) -> int | None:
    for index in range(1, len(a)):
        if a[index] != 0:
            return index
    return None


def geometric_recovery(source: Sequence[Number], q: int, ratio: Fraction, limit: int) -> List[Fraction]:
    out = [Fraction(0) for _ in range(limit + 1)]
    shift = 1
    weight = Fraction(1)
    while shift <= limit:
        row = shifted(source, shift, limit, weight)
        for n in range(limit + 1):
            out[n] += Fraction(row[n])
        shift *= q
        weight *= ratio
    return out


def matrix_multiply(a: Sequence[Sequence[Fraction]], b: Sequence[Sequence[Fraction]]) -> List[List[Fraction]]:
    return [
        [
            sum(a[i][k] * b[k][j] for k in range(len(b)))
            for j in range(len(b[0]))
        ]
        for i in range(len(a))
    ]


def transpose(a: Sequence[Sequence[Fraction]]) -> List[List[Fraction]]:
    return [list(row) for row in zip(*a)]


def matrix_subtract(a: Sequence[Sequence[Fraction]], b: Sequence[Sequence[Fraction]]) -> List[List[Fraction]]:
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def is_psd_2x2(a: Sequence[Sequence[Fraction]]) -> bool:
    return (
        a[0][0] >= 0
        and a[1][1] >= 0
        and a[0][0] * a[1][1] - a[0][1] * a[1][0] >= 0
        and a[0][1] == a[1][0]
    )


def build_case(k: int, v: int) -> dict:
    limit = v ** k
    mu = mobius_sieve(limit)
    one = [0] + [1] * limit
    identity = [0] * (limit + 1)
    identity[1] = 1
    ell = [0] * (limit + 1)
    for n in range(1, limit + 1):
        ell[n] = formal_log(n)

    mu_v = [0] * (limit + 1)
    mu_gt_v = [0] * (limit + 1)
    for n in range(1, limit + 1):
        if n <= v:
            mu_v[n] = mu[n]
        else:
            mu_gt_v[n] = mu[n]

    r_v = add(identity, scale(convolution(one, mu_v, limit), -1))
    lambda_formal = convolution(mu, ell, limit)
    r_top = convolution_power(r_v, k - 1, limit)
    top = convolution(lambda_formal, r_top, limit)

    one_power = convolution_power(one, k - 1, limit)
    large_power = convolution_power(mu_gt_v, k - 1, limit)

    anchor = convolution(lambda_formal, one_power, limit)
    top_normal = convolution(anchor, large_power, limit)

    reciprocal_free_fiber = convolution(
        convolution(ell, one_power, limit),
        large_power,
        limit,
    )

    b_2 = add(mu, scale(shifted(mu, 2, limit), -1))
    dyadic_dipole = add(top, scale(shifted(top, 2, limit), -1))
    dyadic_factorization = convolution(b_2, reciprocal_free_fiber, limit)

    omega_2 = add(
        mu,
        scale(shifted(mu, 2, limit), Fraction(-3, 2)),
        scale(shifted(mu, 4, limit), Fraction(1, 2)),
    )
    parity_filtered = add(
        dyadic_dipole,
        scale(shifted(dyadic_dipole, 2, limit), Fraction(-1, 2)),
    )
    parity_factorization = convolution(omega_2, reciprocal_free_fiber, limit)

    recovered_top = geometric_recovery(dyadic_dipole, 2, Fraction(1), limit)
    recovered_dipole = geometric_recovery(parity_filtered, 2, Fraction(1, 2), limit)

    vacuous_q = v
    vacuous_shift = shifted(top, vacuous_q, limit)

    return {
        "K": k,
        "V": v,
        "limit": limit,
        "first_top": first_nonzero(top),
        "support_lower_bound": 2 * (v + 1) ** (k - 1),
        "top_normal_mismatches": mismatches(top, top_normal),
        "dyadic_factorization_mismatches": mismatches(dyadic_dipole, dyadic_factorization),
        "parity_factorization_mismatches": mismatches(parity_filtered, parity_factorization),
        "top_recovery_mismatches": mismatches(top, recovered_top),
        "dipole_recovery_mismatches": mismatches(dyadic_dipole, recovered_dipole),
        "fixed_fraction_shift_nonzero": sum(value != 0 for value in vacuous_shift),
        "fixed_dyadic_shift_nonzero": sum(value != 0 for value in shifted(top, 2, limit)),
    }


def run() -> dict:
    cases = [
        build_case(3, 4),
        build_case(4, 4),
        build_case(4, 6),
        build_case(4, 10),
        build_case(5, 6),
    ]

    for case in cases:
        assert case["top_normal_mismatches"] == 0
        assert case["dyadic_factorization_mismatches"] == 0
        assert case["parity_factorization_mismatches"] == 0
        assert case["top_recovery_mismatches"] == 0
        assert case["dipole_recovery_mismatches"] == 0
        assert case["fixed_fraction_shift_nonzero"] == 0
        first = case["first_top"]
        if first is not None:
            assert first >= case["support_lower_bound"]

    assert any(case["fixed_dyadic_shift_nonzero"] > 0 for case in cases)

    g = [
        [Fraction(2), Fraction(1)],
        [Fraction(1), Fraction(3)],
    ]
    reserve = [
        [Fraction(1), Fraction(1, 2)],
        [Fraction(1, 2), Fraction(1)],
    ]
    a = [[g[i][j] + reserve[i][j] for j in range(2)] for i in range(2)]
    common_fiber = [
        [Fraction(1), Fraction(2)],
        [Fraction(-1), Fraction(3)],
    ]
    lifted = matrix_multiply(
        transpose(common_fiber),
        matrix_multiply(matrix_subtract(a, g), common_fiber),
    )
    assert is_psd_2x2(reserve)
    assert is_psd_2x2(lifted)

    mutation_tests = {
        "top_normal_form": all(c["top_normal_mismatches"] == 0 for c in cases),
        "fixed_fraction_vacuity": all(c["fixed_fraction_shift_nonzero"] == 0 for c in cases),
        "fixed_dyadic_nonvacuity": any(c["fixed_dyadic_shift_nonzero"] > 0 for c in cases),
        "dyadic_factorization": all(c["dyadic_factorization_mismatches"] == 0 for c in cases),
        "opposite_parity_factorization": all(c["parity_factorization_mismatches"] == 0 for c in cases),
        "two_stable_recoveries": all(
            c["top_recovery_mismatches"] == 0 and c["dipole_recovery_mismatches"] == 0
            for c in cases
        ),
        "common_fiber_psd_congruence": is_psd_2x2(lifted),
    }
    assert all(mutation_tests.values())

    payload = {
        "classification": "EXACT_FIXED_DYADIC_TOP_SOURCE_AND_FIBER_CONGRUENCE_VERIFIED",
        "arithmetic": "INTEGER_AND_FRACTION",
        "cases": cases,
        "common_fiber_lifted_reserve": [
            [str(value) for value in row] for row in lifted
        ],
        "mutation_tests": mutation_tests,
        "scope": {
            "verified": [
                "top prime-anchor normal form on finite controls",
                "vacuity of Q=V shifted top source through V^K",
                "nonvacuity of fixed Q=2 on a finite control",
                "fixed dyadic b_2 factorization",
                "opposite-parity omega_2 factorization",
                "stable dyadic geometric recoveries",
                "finite PSD common-fiber congruence",
            ],
            "not_verified": [
                "physical boundary-commutator source map",
                "fibered factor-five transition certificate",
                "cofinal block recurrence",
                "Riemann Hypothesis",
            ],
        },
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = sha256(canonical).hexdigest()
    return payload


if __name__ == "__main__":
    result = run()
    rendered = json.dumps(result, indent=2, sort_keys=True)
    print("PASS_EXACT_FIXED_DYADIC_TOP_SOURCE_AND_FIBER_CONGRUENCE")
    print(f"cases {len(result['cases'])}")
    print(f"mutation tests {sum(result['mutation_tests'].values())}/{len(result['mutation_tests'])}")
    print(f"proof-object SHA-256 {result['proof_object_sha256']}")
    output_path = Path(__file__).resolve().parent / "results" / "verification.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(rendered + "\n", encoding="utf-8")
