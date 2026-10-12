#!/usr/bin/env python3
"""Finite rational controls for the outer-strip proof's algebraic adapters.

No actual xi value is evaluated. The complete product, Hurwitz, source moments,
and harmonic/Schwarz--Pick theorems remain analytic proof obligations.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path


def need(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


@dataclass(frozen=True)
class C:
    re: Q = Q(0)
    im: Q = Q(0)

    @staticmethod
    def of(value: C | Q | int) -> C:
        return value if isinstance(value, C) else C(Q(value))

    def __add__(self, other: C | Q | int) -> C:
        other = C.of(other)
        return C(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __neg__(self) -> C:
        return C(-self.re, -self.im)

    def __sub__(self, other: C | Q | int) -> C:
        return self + -C.of(other)

    def __rsub__(self, other: C | Q | int) -> C:
        return C.of(other) - self

    def __mul__(self, other: C | Q | int) -> C:
        other = C.of(other)
        return C(self.re * other.re - self.im * other.im,
                 self.re * other.im + self.im * other.re)

    __rmul__ = __mul__

    def norm2(self) -> Q:
        return self.re**2 + self.im**2

    def __truediv__(self, other: C | Q | int) -> C:
        other = C.of(other)
        denominator = other.norm2()
        need(denominator > 0, "nonzero exact complex denominator")
        return self * C(other.re / denominator, -other.im / denominator)

    def __rtruediv__(self, other: C | Q | int) -> C:
        return C.of(other) / self


I = C(Q(0), Q(1))
ZERO = C()
Polynomial = list[C]


def multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    result = [ZERO] * (len(left) + len(right) - 1)
    for j, a in enumerate(left):
        for k, b in enumerate(right):
            result[j + k] = result[j + k] + a * b
    return result


def derivative(poly: Polynomial) -> Polynomial:
    return [coefficient * j for j, coefficient in enumerate(poly)][1:] or [ZERO]


def at(poly: Polynomial, z: C) -> C:
    result = ZERO
    for coefficient in reversed(poly):
        result = result * z + coefficient
    return result


def companion(poly: Polynomial, lam: Q) -> Polynomial:
    first = derivative(poly)
    return [coefficient - I * lam * (first[j] if j < len(first) else ZERO)
            for j, coefficient in enumerate(poly)]


def strip_product(factors: list[tuple[Q, Q]]) -> tuple[Polynomial, Q]:
    poly = [C(Q(1))]
    strip = max(a for _, a in factors)
    for b, a in factors:
        factor = [C(b*b + a*a), C(-2*b), C(Q(1))]
        # This factor's declared roots are exactly b +/- i a, with multiplicity.
        need(at(factor, C(b, a)) == ZERO, "declared upper factor root")
        need(at(factor, C(b, -a)) == ZERO, "declared lower factor root")
        poly = multiply(poly, factor)
    need(all(coefficient.im == 0 for coefficient in poly), "real polynomial")
    need(all(poly[j] == ZERO for j in range(1, len(poly), 2)), "even polynomial")
    return poly, strip


def polynomial_controls() -> tuple[int, int, int]:
    fixtures = [
        [(Q(0), Q(1, 4)), (Q(2), Q(1, 4)), (Q(-2), Q(1, 4))],
        [(Q(0), Q(1, 2)), (Q(1), Q(1, 3)), (Q(-1), Q(1, 3)),
         (Q(3), Q(1, 4)), (Q(-3), Q(1, 4))],
        [(Q(1), Q(0)), (Q(-1), Q(0)), (Q(3), Q(0)), (Q(-3), Q(0))],
    ]
    count = adapters = schwarz = 0
    epsilon = Q(1, 10**12)
    modifier = [C(Q(1)), ZERO, C(epsilon)]
    modifier1, modifier2 = derivative(modifier), derivative(derivative(modifier))
    alpha = beta = Q(1, 10**6)
    rho_upper = Q(99, 100)
    k_bound = (1 + rho_upper) / (1 - rho_upper)
    need(k_bound**2 * alpha + (k_bound**2 + 1) * beta < 1,
         "strict protected-source budget")
    error_bound = (alpha + beta) / (1 - beta)
    for factors in fixtures:
        poly, strip = strip_product(factors)
        degree = len(poly) - 1
        h = poly
        for order in range(degree):
            h1, h2 = derivative(h), derivative(derivative(h))
            for lam in (Q(1, 10), Q(1, 2), Q(2)):
                e = companion(h, lam)
                e1 = derivative(e)
                anchor_y = strip + 1
                anchor = C(Q(0), -anchor_y)
                qa = at(e1, anchor) / at(e, anchor)
                need(qa.re == 0 and qa.im > 0, "positive rational axis anchor")
                m = qa.im
                for x in (Q(-3), Q(0), Q(1, 3), Q(3)):
                    for offset in (Q(1, 16), Q(1, 4), Q(1), Q(2)):
                        y = strip + offset
                        z = C(x, -y)
                        hv, h1v, h2v = at(h, z), at(h1, z), at(h2, z)
                        ev, e1v = at(e, z), at(e1, z)
                        need(hv.norm2() > 0 and ev.norm2() > 0 and e1v.norm2() > 0,
                             "outer companion and derivative nonvanishing")
                        log_h = h1v / hv
                        log_e = e1v / ev
                        w = I * ev / e1v
                        need(log_h.im > 0 and log_e.im > 0 and w.re > 0,
                             "strict outer polynomial sectors")
                        need((ev / hv).re == 1 + lam * log_h.im,
                             "companion real-part identity")
                        need((ev / hv).re > 1, "strict polynomial zero exclusion")
                        need(w.re == log_e.im / log_e.norm2(), "sector sign adapter")
                        base_ratio = hv / ev
                        need((base_ratio - Q(1, 2)).norm2() < Q(1, 4),
                             "protected base ratio disk")
                        need(base_ratio.norm2() < 1 and (2 - base_ratio).norm2() < 4,
                             "multiplier denominator adapters")
                        count += 1

                        rho2 = (x*x + (y-anchor_y)**2) / (
                            x*x + (y+anchor_y-2*strip)**2)
                        need(0 <= rho2 < 1 and rho2 <= rho_upper**2,
                             "rational half-plane geometry bound")
                        need(((log_e-I*m)/(log_e+I*m)).norm2() <= rho2,
                             "finite exact Schwarz--Pick disk control")
                        need(((w-Q(1)/m)/(w+Q(1)/m)).norm2() <= rho2,
                             "finite exact right-half-plane disk control")
                        need(log_e.im >= m/k_bound and
                             log_e.norm2() <= m*m*k_bound*k_bound and
                             w.re >= Q(1)/(m*k_bound) and
                             w.norm2() <= k_bound*k_bound/(m*m),
                             "finite exact half-plane quantitative adapters")
                        schwarz += 1

                        pv, p1v, p2v = at(modifier, z), at(modifier1, z), at(modifier2, z)
                        modified_h = multiply(modifier, h)
                        modified_e = companion(modified_h, lam)
                        modified_e1 = derivative(modified_e)
                        mev, me1v = at(modified_e, z), at(modified_e1, z)
                        need(mev == pv*ev-I*lam*p1v*hv,
                             "full modified companion identity")
                        need(me1v == pv*e1v+p1v*(hv-2*I*lam*h1v)-I*lam*p2v*hv,
                             "full modified derivative identity")
                        n = (mev-pv*ev)/(pv*ev)
                        d = (me1v-pv*e1v)/(pv*e1v)
                        need(n.norm2() <= alpha**2 and d.norm2() <= beta**2,
                             "exact perturbation budgets")
                        mw = I*mev/me1v
                        need(mw/w == (1+n)/(1+d), "exact relative transport identity")
                        need((mw/w-1).norm2() <= error_bound**2,
                             "relative perturbation inequality")
                        lower_margin = Q(1)/(m*k_bound)-k_bound/m*error_bound
                        need(lower_margin > 0 and mw.re >= lower_margin,
                             "protected positive sector after modification")
                        adapters += 1
            h = derivative(h)
    return count, adapters, schwarz


def sharpness_controls() -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    polynomial_rows = []
    strip = Q(1, 2)
    poly = [C(strip*strip), ZERO, C(Q(1))]
    for y in (Q(1, 4), Q(2, 5), Q(49, 100), Q(499, 1000)):
        lam = (strip*strip-y*y)/(2*y)
        need(0 < y < strip and lam > 0, "inside-strip polynomial fixture")
        e = companion(poly, lam)
        need(at(e, C(Q(0), -y)) == ZERO, "exact lower polynomial companion zero")
        need(at(derivative(e), C(Q(0), -y)).norm2() > 0,
             "simple exact polynomial companion zero")
        polynomial_rows.append({"strip":str(strip), "y":str(y), "lambda":str(lam)})

    source_rows = []
    epsilon = Q(10, 17)  # complete source strip delta=log(2)
    for exp_y in (Q(3, 2), Q(7, 4), Q(15, 8), Q(31, 16), Q(63, 32)):
        ch = (exp_y + 1/exp_y)/2
        sh = (exp_y - 1/exp_y)/2
        ch2 = (exp_y**2 + 1/exp_y**2)/2
        sh2 = (exp_y**2 - 1/exp_y**2)/2
        f = -ch + epsilon*ch2
        g = -sh + 2*epsilon*sh2
        h = -ch + 4*epsilon*ch2
        need(1 < exp_y < 2 and f < 0 < g and h > 0,
             "inside-strip positive Fourier-source fixture")
        lam = -f/g
        need(lam > 0 and f+lam*g == 0 and g+lam*h > 0,
             "exact positive-source companion zero with protected derivative")
        quartic = (epsilon*(1+2*lam)*exp_y**4-(1+lam)*exp_y**3
                   +(lam-1)*exp_y+epsilon*(1-2*lam))
        need(quartic == 0, "exact complete ray-zero quartic")
        need((epsilon-1)/(lam*(4*epsilon-1)) < 0, "negative adjacent real endpoint")
        source_rows.append({"exp_strip": "2", "exp_y":str(exp_y),
                            "epsilon":str(epsilon), "lambda":str(lam)})
    return polynomial_rows, source_rows


def main() -> None:
    polynomial_count, transport_count, schwarz_count = polynomial_controls()
    polynomial_sharpness, source_sharpness = sharpness_controls()
    directory = Path(__file__).resolve().parent
    source_paths = [directory/"THEOREM.md", directory/"SOURCE_TRANSPORT.md",
                    directory.parent/"DERIVATIVE_COUNTEREXAMPLE.md", Path(__file__).resolve()]
    hashes = {str(path.relative_to(directory.parent)): hashlib.sha256(path.read_bytes()).hexdigest()
              for path in source_paths}
    report = {
        "status": "PASS_EXACT_OUTER_STRIP_CONTROLS",
        "arithmetic": "fractions.Fraction; rational real and imaginary components only",
        "strict_acceptance": "Every need() assertion must pass; zero exit status is required.",
        "coverage": "Three explicitly factored strip polynomials; all derivative orders with positive degree; three positive lambdas; sixteen outer points each. Finite synthetic controls only.",
        "polynomial_sector_cases": polynomial_count,
        "quantitative_half_plane_cases": schwarz_count,
        "protected_multiplier_transport_cases": transport_count,
        "exact_polynomial_inside_strip_zeros": polynomial_sharpness,
        "exact_positive_fourier_inside_strip_zeros": source_sharpness,
        "source_sha256": hashes,
        "actual_xi_evaluated": False,
        "actual_theta_moment_integrals_enclosed": False,
        "infinite_product_or_analytic_theorems_authenticated_by_checker": False,
        "all_fixed_order_multiplier_leibniz_transport_checked_numerically": False,
        "rh_proved": False,
    }
    output = directory/"exact_checks.json"
    output.write_text(json.dumps(report, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    print(report["status"], f"sectors={polynomial_count}",
          f"half_plane={schwarz_count}", f"transport={transport_count}",
          f"sharpness={len(polynomial_sharpness)+len(source_sharpness)}")


if __name__ == "__main__":
    main()
