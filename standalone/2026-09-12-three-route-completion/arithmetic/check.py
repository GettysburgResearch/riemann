"""Reconstruct small native traces and source identities with outward arithmetic.

Python standard library only. The analytic exponent theorem is not machine
proved here. No asymptotic extrapolation or zeta-zero input is accepted.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as F
from math import factorial, isqrt
from pathlib import Path

BITS = 384
UNIT = 1 << BITS


def ceildiv(a: int, b: int) -> int:
    return -((-a) // b)


class Iv:
    def __init__(self, lo: int, hi: int):
        if type(lo) is not int or type(hi) is not int or lo > hi:
            raise ValueError("invalid interval")
        self.lo, self.hi = lo, hi

    @staticmethod
    def rational(x: F | int) -> "Iv":
        x = F(x)
        return Iv(x.numerator * UNIT // x.denominator,
                  ceildiv(x.numerator * UNIT, x.denominator))

    def __add__(self, other: "Iv") -> "Iv":
        return Iv(self.lo + other.lo, self.hi + other.hi)

    def __neg__(self) -> "Iv":
        return Iv(-self.hi, -self.lo)

    def __sub__(self, other: "Iv") -> "Iv":
        return self + (-other)

    def __mul__(self, other: "Iv") -> "Iv":
        products = [a * b for a in (self.lo, self.hi)
                    for b in (other.lo, other.hi)]
        return Iv(min(products) // UNIT, ceildiv(max(products), UNIT))

    def scale(self, x: F | int) -> "Iv":
        return self * Iv.rational(x)

    def power(self, n: int) -> "Iv":
        if n < 0:
            raise ValueError("nonnegative integer powers only")
        result, base = Iv.rational(1), self
        while n:
            if n & 1:
                result = result * base
            base = base * base
            n //= 2
        return result

    def reciprocal(self) -> "Iv":
        if self.lo <= 0:
            raise ValueError("positive interval required")
        return Iv(UNIT * UNIT // self.hi, ceildiv(UNIT * UNIT, self.lo))

    def overlaps(self, other: "Iv") -> bool:
        return max(self.lo, other.lo) <= min(self.hi, other.hi)

    def report(self, places: int = 18) -> dict:
        scale = 10 ** places
        low = self.lo * scale // UNIT
        high = ceildiv(self.hi * scale, UNIT)

        def decimal(v: int) -> str:
            sign = "-" if v < 0 else ""
            v = abs(v)
            return f"{sign}{v // scale}.{v % scale:0{places}d}"

        return {"lower": decimal(low), "upper": decimal(high)}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def arctan_inverse(q: int, terms: int) -> Iv:
    result = Iv.rational(0)
    for k in range(terms):
        term = Iv.rational(F(1, (2 * k + 1) * q ** (2 * k + 1)))
        result = result + term if k % 2 == 0 else result - term
    next_upper = ceildiv(UNIT, (2 * terms + 1) * q ** (2 * terms + 1))
    tail = Iv(0, next_upper) if terms % 2 == 0 else Iv(-next_upper, 0)
    return result + tail


def pi_routes() -> tuple[Iv, Iv]:
    # Machin identity and the distinct atan(1/2)+atan(1/3)=pi/4 identity.
    p = arctan_inverse(5, 128).scale(16) - arctan_inverse(239, 32).scale(4)
    q = (arctan_inverse(2, 256) + arctan_inverse(3, 256)).scale(4)
    require(p.lo > 3 * UNIT and p.hi < 4 * UNIT, "pi range")
    require(p.overlaps(q), "independent pi routes disagree")
    return p, q


def bernoulli(n: int) -> F:
    a: list[F] = []
    for m in range(n + 1):
        a.append(F(1, m + 1))
        for j in range(m, 0, -1):
            a[j - 1] = j * (a[j - 1] - a[j])
    return a[0]


def inv_odd_zeta(s: int, pi: Iv) -> Iv:
    require(s >= 2 and s % 2 == 0, "even zeta argument")
    constant = abs(bernoulli(s)) * F(2 ** s, 2 * factorial(s)) * (1 - F(1, 2 ** s))
    return pi.power(s).scale(constant).reciprocal()


def legendre_polynomials(n: int) -> list[list[F]]:
    result = [[F(1)], [F(0), F(1)]]
    for k in range(2, n + 1):
        p = [F(0)] * (k + 1)
        for j, x in enumerate(result[-1]):
            p[j + 1] += F(2 * k - 1, k) * x
        for j, x in enumerate(result[-2]):
            p[j] -= F(k - 1, k) * x
        result.append(p)
    return result[:n + 1]


def scalar_integral_product(p: list[F], q: list[F], a: int, b: int) -> F:
    return sum((x * y * F(b ** (i + j + 1) - a ** (i + j + 1), i + j + 1)
                for i, x in enumerate(p) for j, y in enumerate(q)), F(0))


def trace_values(max_n: int, pi: Iv) -> dict[int, Iv]:
    polynomials = legendre_polynomials(2 * max_n - 1)
    inverses = {s: inv_odd_zeta(s, pi) for s in range(2, 2 * max_n + 1, 2)}
    result: dict[int, Iv] = {}
    total = Iv.rational(0)
    for j in range(max_n):
        p = polynomials[2 * j + 1]
        out = [Iv.rational(0) for _ in p]
        for r in range(1, len(p), 2):
            out[0] = out[0] + Iv.rational(p[r] / r)
            out[r] = (inverses[r + 1] - Iv.rational(1)).scale(p[r] / r)
        square = Iv.rational(0)
        for r, x in enumerate(out):
            for s, y in enumerate(out):
                square = square + (x * y).scale(F(3 ** (r + s + 1) - 1, r + s + 1))
        square = square.scale(4 * j + 3)
        require(square.lo > 0, "positive full column energy not enclosed")
        total = total + square
        result[j + 1] = total
    return result


def trial_mobius_liouville(n: int) -> tuple[int, int]:
    remaining, p, count, squarefree = n, 2, 0, True
    while p * p <= remaining:
        exponent = 0
        while remaining % p == 0:
            remaining //= p
            exponent += 1
        count += exponent
        squarefree = squarefree and exponent < 2
        p += 1
    if remaining > 1:
        count += 1
    sign = -1 if count % 2 else 1
    return (sign if squarefree else 0), sign


def sieve_mobius(n: int) -> list[int]:
    values = [1] * (n + 1)
    prime = [True] * (n + 1)
    values[0] = 0
    for p in range(2, n + 1):
        if prime[p]:
            for k in range(p, n + 1, p):
                values[k] *= -1
                if k > p:
                    prime[k] = False
            for k in range(p * p, n + 1, p * p):
                values[k] = 0
    return values


def rational_report(value: F) -> dict:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def boundary_error(n: int, m: int, mu: list[int], pi: Iv) -> dict:
    """Complete HS error of the one-channel surrogate, integrated cellwise."""
    d = 2 * n - 1
    require(len(mu) > 3 * m, "boundary Mobius coverage")
    polys = legendre_polynomials(d)
    inverses = {q: inv_odd_zeta(q, pi) for q in range(2, d + 2, 2)}
    total = Iv.rational(0)
    jump_checks = 0
    for k in range(m, 3 * m + 1):
        if k % 2:
            for q in inverses:
                # The two changes at t=k/M cancel, including their signs.
                jump = F(mu[k], k * m ** (q - 1)) - F(k, m) ** (q - 1) * F(mu[k], k ** q)
                require(jump == 0, "boundary moment activation continuity")
                jump_checks += 1
        if k == 3 * m:
            continue
        odd = sum((F(mu[r], r) for r in range(1, k + 1, 2)), F(0))
        tails = {q: inverses[q] - Iv.rational(sum(
            (F(mu[r], r ** q) for r in range(1, k + 1, 2)), F(0)))
                 for q in inverses}
        for j in range(n):
            p = polys[2 * j + 1]
            error = [Iv.rational(0) for _ in p]
            # r=1 is the retained rank-one boundary channel; only r>=3 remains.
            for r in range(3, len(p), 2):
                error[0] = error[0] + Iv.rational(p[r] * odd / (r * m ** r))
                error[r] = tails[r + 1].scale(p[r] / r)
            square = Iv.rational(0)
            for r, x in enumerate(error):
                for s, y in enumerate(error):
                    power = r + s + 1
                    integral = (F(k + 1, m) ** power - F(k, m) ** power) / power
                    square = square + (x * y).scale(integral)
            total = total + square.scale(4 * j + 3)
    bound = F(121 * d ** 7, m ** 6)
    require(total.lo > 0, "positive boundary error not enclosed")
    require(F(total.hi, UNIT) <= bound, "one-channel boundary HS estimate")
    return {"N": n, "M": m, "native_coverage": 3 * m,
            "complete_output_cells": 2 * m,
            "complete_error_column_norms": n,
            "activation_continuity_checks": jump_checks,
            "HS_error_squared": total.report(),
            "theorem_HS_error_squared_upper": rational_report(bound)}


def reconstruct() -> dict:
    pi1, pi2 = pi_routes()
    max_n = 8
    first = trace_values(max_n, pi1)
    second = trace_values(max_n, pi2)
    for n in first:
        require(first[n].overlaps(second[n]), "two full trace reconstructions disagree")

    polys = legendre_polynomials(2 * max_n - 1)
    orthogonal_checks = 0
    for i in range(max_n):
        for j in range(max_n):
            value = scalar_integral_product(polys[2 * i + 1], polys[2 * j + 1], 0, 1)
            require(value == (F(1, 4 * i + 3) if i == j else 0), "Legendre metric")
            orthogonal_checks += 1

    m_cutoffs = {}
    for n in [1, 2, 4, 8]:
        d = 2 * n - 1
        m = isqrt(d ** 3)
        if m * m < d ** 3:
            m += 1
        m_cutoffs[n] = max(2, m)
    coverage = 3 * max(m_cutoffs.values())
    mu = sieve_mobius(coverage)
    for k in range(1, coverage + 1):
        require(mu[k] == trial_mobius_liouville(k)[0], "Mobius construction disagreement")

    harmonic, mertens, energy, work, full = F(0), 0, F(0), F(0), F(0)
    f_values, m_values = {0: F(0)}, {0: F(0)}
    for k in range(1, coverage + 1):
        harmonic += F(mu[k], k)
        mertens += mu[k]
        energy += F(mertens * mertens, k * (k + 1))
        work += F(mertens, k * (k + 1))
        full += harmonic * harmonic
        require(full == energy + (k + 1) * work * work, "finite native energy identity")
        require(abs(harmonic) <= 1, "elementary reciprocal bound")
        odd = sum((F(mu[r], r) for r in range(1, k + 1, 2)), F(0))
        dilation = F(0)
        power = 1
        while power <= k:
            cut = k // power
            dilation += sum((F(mu[r], r) for r in range(1, cut + 1)), F(0)) / power
            power *= 2
        require(odd == dilation, "odd/all source conversion")
        f_values[k], m_values[k] = full, harmonic

    crossing_panels = []
    for y in range(2, min(coverage, 32)):
        if mu[y] == 0 or m_values[y - 1] * m_values[y] > 0:
            continue
        c = {k: F(mu[k]) for k in range(1, y + 1) if mu[k]}
        c[2 * y] = -2 * y * m_values[y]
        require(sum((v / k for k, v in c.items()), F(0)) == 0, "crossing balance")
        require(all(trial_mobius_liouville(k)[1] * v >= 0 for k, v in c.items()),
                "crossing Liouville signs")
        pair_energy = sum((v * w / max(k, l) for k, v in c.items()
                           for l, w in c.items()), F(0))
        expected = f_values[y] + (y - 1) * m_values[y] ** 2
        require(pair_energy == expected, "complete crossing energy")
        require(expected <= f_values[y] + F(1, y), "paid crossing collar")
        crossing_panels.append({"Y": y, "complete_energy": rational_report(expected)})

    trace_panels = []
    for n, m in m_cutoffs.items():
        bound = 26 * f_values[3 * m] + 1296
        require(F(first[n].hi, UNIT) < bound, "finite native adapter")
        require(first[n].hi < 800 * (2 * n - 1) * UNIT, "linear trace ceiling")
        trace_panels.append({"N": n, "S_N": first[n].report(), "M": m,
                             "native_coverage": 3 * m,
                             "F_coverage": rational_report(f_values[3 * m]),
                             "adapter_upper": rational_report(bound)})

    boundary_panel = boundary_error(4, 32, mu, pi1)
    require(boundary_panel == boundary_error(4, 32, mu, pi2),
            "two boundary reconstructions disagree at displayed precision")

    return {
        "status": "bounded directed reconstruction; no RH upper estimate",
        "arithmetic": "384-bit outward integer intervals plus exact Fraction identities",
        "pi_routes": {"machin": pi1.report(), "atan_half_plus_third": pi2.report()},
        "coverage": {"trace_degrees_all": list(range(1, max_n + 1)),
                     "complete_output_column_norms": max_n,
                     "orthogonality_entries": orthogonal_checks,
                     "mobius_trial_sieve_integers": coverage,
                     "complete_source_identity_endpoints": coverage,
                     "odd_all_conversion_endpoints": coverage,
                     "crossing_energy_panels": len(crossing_panels)},
        "trace_panels": trace_panels,
        "crossing_panels": crossing_panels,
        "boundary_channel_panel": boundary_panel,
        "limitations": ["No zeta zero is evaluated.",
                        "No all-degree trace upper saving is tested or proved by this program.",
                        "The two arithmetic paths have the same author.",
                        "No predecessor executable is imported."]
    }


def reject_duplicates(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def canonical(obj) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("ascii")


def main() -> None:
    parser = argparse.ArgumentParser()
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--write", type=Path)
    action.add_argument("--check", type=Path)
    args = parser.parse_args()
    result = reconstruct()
    if args.write:
        args.write.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    else:
        supplied = json.loads(args.check.read_text(encoding="utf-8"), object_pairs_hook=reject_duplicates)
        require(canonical(supplied) == canonical(result), "result does not reconstruct exactly")
    print(json.dumps({"accepted": True, "semantic_sha256": hashlib.sha256(canonical(result)).hexdigest(),
                      "coverage": result["coverage"]}, sort_keys=True))


if __name__ == "__main__":
    main()
