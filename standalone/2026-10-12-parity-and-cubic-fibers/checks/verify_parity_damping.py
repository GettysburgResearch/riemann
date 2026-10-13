#!/usr/bin/env python3
"""Bounded exact guards for PARITY_DAMPED_MOMENTS.md.

Authenticates primitive sextic symbols, literal zeros, Walsh/centered-sign
identities, and finite rational exponent algebra. It does not prove an
analytic premise, a sieve, an infinite moment estimate, or a zero-free region.
Only the normalized release name and file hashes enter the result, so moving
or renaming the same proof/checker bytes does not change the JSON. Every guard
raises explicitly; Python -O does not disable any predicate.
"""

import argparse
import hashlib
import itertools
import json
import math
from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path


COUNTS = Counter()


def require(condition, label, witness=None):
    COUNTS[label] += 1
    if not condition:
        raise ArithmeticError(f"{label}: {witness!r}")


@dataclass(frozen=True)
class R:
    """Exact a+b*zeta_6; zeta_6^2=zeta_6-1."""

    a: F = F(0)
    b: F = F(0)

    def __add__(self, other):
        other = other if isinstance(other, R) else R(F(other))
        return R(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return R(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        other = other if isinstance(other, R) else R(F(other))
        return R(self.a * other.a - self.b * other.b,
                 self.a * other.b + self.b * other.a + self.b * other.b)

    __rmul__ = __mul__

    def __pow__(self, power):
        require(power >= 0, "nonnegative_ring_power", power)
        out = R(F(1))
        base = self
        while power:
            if power & 1:
                out = out * base
            base = base * base
            power //= 2
        return out

    def conjugate(self):
        return R(self.a + self.b, -self.b)

    def norm(self):
        return self.a * self.a + self.a * self.b + self.b * self.b


ONE = R(F(1))
ZERO = R()
ZETA = R(F(0), F(1))
PRIMES = (7, 13)
PRIMITIVE_IMAGES = (3, 4)
SIGNS = tuple(itertools.product((-1, 1), repeat=2))
MASKS = range(4)
WEIGHTS = (1, 2, -1, 3)
NU_LOCAL = (ZETA, ZETA ** 2)


def bits_product(values, mask):
    out = 1
    for i, value in enumerate(values):
        if mask & (1 << i):
            out = out * value
    return out


def mu(mask):
    return (-1) ** mask.bit_count()


def evaluate(coefficients, signs):
    return sum((c * bits_product(signs, n)
                for n, c in enumerate(coefficients)), ZERO)


def primitive_symbol(p, image, residue):
    if residue % p == 0:
        return ZERO
    target = pow(residue, (p - 1) // 6, p)
    indices = [j for j in range(6) if pow(image, j, p) == target]
    require(len(indices) == 1, "primitive_symbol_lookup", (p, residue))
    return ZETA ** indices[0]


def local_and_walsh():
    for p, image in zip(PRIMES, PRIMITIVE_IMAGES):
        require(len({pow(image, j, p) for j in range(6)}) == 6,
                "primitive_embedding", (p, image))
        require((image * image - image + 1) % p == 0,
                "cyclotomic_embedding", (p, image))
        for x in range(p):
            chi = primitive_symbol(p, image, x)
            require(chi == chi ** 3 * chi ** 4,
                    "quadratic_cubic_factorization", (p, x))
            for left in range(9):
                for right in range(9):
                    if left + right == 0:
                        continue
                    actual = chi ** left * chi.conjugate() ** right
                    reduced = chi ** ((left - right) % 6) if x else ZERO
                    require(actual == reduced, "literal_residual_zero_mask",
                            (p, x, left, right))

    crt_sums = defaultdict(F)
    cubic_fibers = {}
    model_cases = 0
    biased_cases = 0
    zero_rows = 0
    for u in range(math.prod(PRIMES)):
        chi = tuple(primitive_symbol(p, z, u % p)
                    for p, z in zip(PRIMES, PRIMITIVE_IMAGES))
        cubic = tuple(x ** 4 for x in chi)
        quadratic_ring = tuple(x ** 3 for x in chi)
        require(all(x.b == 0 and x.a in (-1, 0, 1) for x in quadratic_ring),
                "literal_quadratic_range", u)
        quadratic = tuple(x.a for x in quadratic_ring)
        zero_rows += any(x == ZERO for x in chi)
        xi = [ONE * bits_product(NU_LOCAL, n) * bits_product(chi, n) for n in MASKS]
        for excluded in MASKS:
            sextic_coeff = [xi[n] * WEIGHTS[n] if not n & excluded else ZERO
                           for n in MASKS]
            cubic_coeff = [ONE * bits_product(NU_LOCAL, n) * bits_product(cubic, n)
                           * WEIGHTS[n] if not n & excluded else ZERO
                           for n in MASKS]
            native = sum((sextic_coeff[n] * mu(n) for n in MASKS), ZERO)
            for k in (1, 2, 3):
                model_cases += 1
                values = [evaluate(cubic_coeff, e).norm() ** k for e in SIGNS]
                walsh = [sum((v * bits_product(e, r)
                              for v, e in zip(values, SIGNS)), F(0)) / 4
                         for r in MASKS]
                rhs = sum((mu(r) * bits_product(quadratic, r) * walsh[r]
                           for r in MASKS), F(0))
                require(native.norm() ** k == rhs, "native_walsh_identity",
                        (u, excluded, k))
                require(walsh[0] >= 0, "positive_walsh_baseline")
                require(all(abs(c) <= walsh[0] for c in walsh),
                        "walsh_coefficient_domination")
                require(sum(c * c for c in walsh) == sum(v * v for v in values) / 4,
                        "walsh_parseval", (u, excluded, k))
                uniform_q = sum((2 * k - 1) ** n.bit_count() * c.norm()
                                for n, c in enumerate(cubic_coeff))
                require(walsh[0] <= uniform_q ** k,
                        "uniform_sign_hypercontractive_guard", (u, excluded, k))
                key = (excluded, k, cubic)
                if key in cubic_fibers:
                    require(cubic_fibers[key] == walsh,
                            "purely_cubic_coefficient_fiber", (u, excluded, k))
                else:
                    cubic_fibers[key] = walsh
                for r in MASKS:
                    if not bits_product(quadratic, r) or r & excluded:
                        require(walsh[r] == 0, "inactive_walsh_coordinate",
                                (u, excluded, k, r))
                    crt_sums[(excluded, k, r)] += bits_product(quadratic, r) * walsh[r]
                for t in (0, 1):
                    biased_cases += 1
                    rho = tuple(F(1, p ** t) for p in PRIMES)
                    means = tuple(-x for x in rho)
                    centered = []
                    for d in MASKS:
                        generic = sum((sextic_coeff[d | m] * bits_product(means, m)
                                       for m in MASKS if not d & m), ZERO)
                        cofactor = sum((xi[m] * mu(m) * bits_product(rho, m)
                                        * WEIGHTS[d | m]
                                        for m in MASKS if not d & m
                                        and not (d | m) & excluded), ZERO) * xi[d]
                        require(generic == cofactor, "native_centered_cofactor",
                                (u, excluded, t, d))
                        centered.append(generic)
                    expectation = F(0)
                    for e in SIGNS:
                        probability = math.prod((1 + e[i] * means[i]) / 2
                                                for i in range(2))
                        z = tuple(e[i] - means[i] for i in range(2))
                        value = evaluate(sextic_coeff, e)
                        require(value == evaluate(centered, z),
                                "centered_polynomial_identity", (u, excluded, t, e))
                        expectation += probability * value.norm() ** k
                    damped = sum((mu(r) * bits_product(rho, r)
                                  * bits_product(quadratic, r) * walsh[r]
                                  for r in MASKS), F(0))
                    require(expectation == damped, "biased_walsh_identity",
                            (u, excluded, k, t))
                    majorant = sum((4 * (2 * k - 1)) ** d.bit_count() * c.norm()
                                   for d, c in enumerate(centered))
                    require(expectation <= majorant ** k,
                            "centered_hypercontractive_guard", (u, excluded, k, t))
    for key, value in crt_sums.items():
        if key[2]:
            require(value == 0, "complete_crt_quadratic_cancellation", key)
    for k in range(1, 13):
        for j in range(k + 1):
            require(math.comb(2 * k, 2 * j) <= math.comb(k, j) * (2 * k - 1) ** j,
                    "one_sign_binomial_coefficient", (k, j))
    return {"crt_residue_rows_including_zero": math.prod(PRIMES),
            "rows_with_a_literal_zero_symbol": zero_rows,
            "moving_exclusion_masks": 4, "moment_orders": [1, 2, 3],
            "native_walsh_cases": model_cases,
            "biased_cases_at_t_zero_and_one": biased_cases,
            "pure_cubic_fibers": len(cubic_fibers)}


def exponents():
    bs = tuple(map(F, ("3/5", "3/4", "5/6", "7/8", "1")))
    hs = tuple(map(F, ("21/20", "6/5", "4/3", "18/11", "7/4", "2", "7/2", "8")))
    records = []
    for b, h in itertools.product(bs, hs):
        a = 2 * b - 1
        c = b - F(1, 2) if b <= F(5, 6) else 3 * b - F(13, 6)
        bound = lambda x: max(x, 2 * x - 5 * h / 6, 5 * x / 3 - h / 3)
        candidates = {1}
        for x in (h / 2, 3 * h / 2):
            candidates.update(n for n in (math.floor(x), math.ceil(x)) if n >= 1)
        best = max(2 * b * j - bound(F(j)) for j in candidates)
        delta = max(a, best)
        require(delta <= max(a, h * c) < h, "integer_envelope_row_budget", (b, h, delta))
        require(best == max(2 * b * j - bound(F(j)) for j in range(1, 65)),
                "finite_integer_envelope_guard", (b, h, candidates))
        for j in range(1, 65):
            x = F(j)
            branch = x if x <= h / 2 else (5 * x / 3 - h / 3
                                          if x <= 3 * h / 2 else 2 * x - 5 * h / 6)
            require(bound(x) == branch, "sextic_piecewise_exponent", (h, j))
            require(2 * b * j - delta <= bound(x), "common_spike_integer_bound", (b, h, j))
        for k in range(math.ceil(3 * h / 2), math.ceil(3 * h / 2) + 5):
            upper = min(2 * b * k - a,
                        *(2 * b * (k - j) + bound(F(j)) for j in range(1, k + 1)))
            require(upper == 2 * b * k - delta, "attained_norm_envelope", (b, h, k))
        if b == F(7, 8):
            require((delta == F(3, 4)) == (h <= F(7, 4)),
                    "seven_eighths_exact_height_endpoint", (h, delta))
        if b == 1:
            require(delta == max(F(1), 5 * h / 6), "counting_exact_envelope", (h, delta))
        for t in (F(0), b - F(1, 2), b, b + 1):
            m = max(F(1), 2 * b - 2 * t)
            for k in (1, 2, 5, 11):
                require(1 + (k - 1) * m == k + (k - 1) * max(F(0), 2 * b - 2 * t - 1),
                        "nm2_refined_damping_exponent", (b, h, t, k))
                if t >= b - F(1, 2):
                    require(m == 1, "damped_diagonal_threshold", (b, t))
        records.append({"b": str(b), "h": str(h), "delta_integer": str(delta)})
    return {"rational_parameter_pairs": len(records), "integer_guard_degrees": [1, 64],
            "finite_envelopes": records}


def cumulants_and_resampling():
    size = 13
    zero = [0] * size
    moments = [zero[:] for _ in range(size)]
    moments[0][0] = 1
    for n in range(2, size, 2):
        moments[n][1] = 1
    cumulants = [zero[:] for _ in range(size)]
    for n in range(1, size):
        current = moments[n][:]
        for j in range(1, n):
            for p in range(size):
                for q in range(size - p):
                    current[p + q] -= (math.comb(n - 1, j - 1)
                                       * cumulants[j][p] * moments[n - j][q])
        cumulants[n] = current
        require(current == zero if n % 2 else current[0] == 0 and current[1] == 1,
                "rare_event_cumulant_leading_term", n)
    height = 5
    rows = [(a, b) for a in range(-6, 7) for b in range(-6, 7)
            if 0 < a * a - a * b + b * b <= height]
    local = ((7, 2), (13, 3), (19, 7))
    for p, omega in local:
        require((omega * omega + omega + 1) % p == 0, "eisenstein_residue_embedding", (p, omega))
        require(math.prod(q for q, _ in local if q != p) > 4 * height,
                "heatbath_injectivity_norm_hypothesis", p)
        projected = {tuple((a + b * w) % q for q, w in local if q != p)
                     for a, b in rows}
        require(len(projected) == len(rows), "full_residue_heatbath_is_identity", p)
    return {"cumulant_orders": [1, 12], "eisenstein_row_height": height,
            "nonzero_eisenstein_rows": len(rows), "resampling_coordinates": len(local)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--note", type=Path, required=True)
    parser.add_argument("--json", type=Path, required=True)
    args = parser.parse_args()
    source_bytes = args.note.read_bytes()
    result = {"status": "PASS", "source_name": "PARITY_DAMPED_MOMENTS.md",
              "source_sha256": hashlib.sha256(source_bytes).hexdigest(),
              "source_bytes": len(source_bytes),
              "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "arithmetic": local_and_walsh(), "exponents": exponents(),
              "structural_guards": cumulants_and_resampling(),
              "scope": "Bounded exact algebra only; not PW_b, NM2_w, a sieve, an infinite moment theorem, or RH.",
              "portability": "Only normalized source name and byte hashes are recorded; no absolute paths or run timestamps.",
              "guard_counts": dict(sorted(COUNTS.items())),
              "total_explicit_guards": sum(COUNTS.values())}
    args.json.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": result["status"], "source_sha256": result["source_sha256"],
                      "total_explicit_guards": result["total_explicit_guards"],
                      "result_sha256": hashlib.sha256(args.json.read_bytes()).hexdigest()}, sort_keys=True))


if __name__ == "__main__":
    main()
