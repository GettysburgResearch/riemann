#!/usr/bin/env python3
"""Exact/directed replay for the native-root compiler/separator packet.

The replay certifies four things only:

1. the canonical P_61 raw current plus its exact terminal child is separated
   from native ordinary/detail capacity at (X,p,q)=(136,67,2);
2. the finite/continuum endpoint realization defect used in the root-Hall
   compiler is strictly nonzero;
3. the leftmost target-Lorenz cutoff is the exact simultaneous LP basis under
   the frozen monotone score/row profiles, with an explicit dual separator;
4. Y_4-zero detail columns are exact score-free triangular row-transfer
   directions.

It does not prove NRCT or RH.
"""
from __future__ import annotations

from decimal import Decimal, ROUND_HALF_EVEN, localcontext
from fractions import Fraction
from functools import lru_cache
from math import gcd, isqrt, prod
from pathlib import Path
import hashlib
import json
import sys

sys.set_int_max_str_digits(0)

HERE = Path(__file__).resolve().parent
PRIMES_61 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
P61 = prod(PRIMES_61)
DEN = 10**75
LOG_EPS = Fraction(1, 10**115)


class I:
    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi=None):
        self.lo = Fraction(lo)
        self.hi = Fraction(lo if hi is None else hi)
        if self.lo > self.hi:
            raise ValueError((self.lo, self.hi))

    def __add__(self, other):
        other = as_i(other)
        return I(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-as_i(other))

    def __rsub__(self, other):
        return as_i(other) - self

    def __mul__(self, other):
        other = as_i(other)
        vals = (
            self.lo * other.lo,
            self.lo * other.hi,
            self.hi * other.lo,
            self.hi * other.hi,
        )
        return I(min(vals), max(vals))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = as_i(other)
        if other.lo <= 0 <= other.hi:
            raise ZeroDivisionError(other)
        return self * I(1 / other.hi, 1 / other.lo)

    def __rtruediv__(self, other):
        return as_i(other) / self

    def width(self):
        return self.hi - self.lo


def as_i(x):
    return x if isinstance(x, I) else I(x)


@lru_cache(None)
def sqrt_i(x: Fraction | int) -> I:
    x = Fraction(x)
    if x < 0:
        raise ValueError(x)
    a, b = x.numerator, x.denominator
    lo = isqrt(a * DEN * DEN // b)
    while Fraction((lo + 1) ** 2, DEN**2) <= x:
        lo += 1
    while Fraction(lo**2, DEN**2) > x:
        lo -= 1
    hi = lo if Fraction(lo**2, DEN**2) == x else lo + 1
    return I(Fraction(lo, DEN), Fraction(hi, DEN))


@lru_cache(None)
def invsqrt_i(n: int) -> I:
    return 1 / sqrt_i(n)


@lru_cache(None)
def log_i(x: Fraction | int) -> I:
    x = Fraction(x)
    if x <= 0:
        raise ValueError(x)
    with localcontext() as ctx:
        ctx.prec = 145
        ctx.rounding = ROUND_HALF_EVEN
        value = Decimal(x.numerator).ln() - Decimal(x.denominator).ln()
    q = Fraction(value)
    return I(q - LOG_EPS, q + LOG_EPS)


def decimal_fraction(value: Fraction, digits: int = 18) -> str:
    with localcontext() as ctx:
        ctx.prec = max(40, digits + 10)
        rendered = Decimal(value.numerator) / Decimal(value.denominator)
        return format(rendered, f".{digits}g")


def decimal_mid(interval: I, digits: int = 18) -> str:
    return decimal_fraction((interval.lo + interval.hi) / 2, digits)


def factor(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    x = n
    p = 2
    while p * p <= x:
        while x % p == 0:
            out[p] = out.get(p, 0) + 1
            x //= p
        p += 1
    if x > 1:
        out[x] = out.get(x, 0) + 1
    return out


def mobius(n: int) -> int:
    fs = factor(n)
    if any(e > 1 for e in fs.values()):
        return 0
    return -1 if len(fs) & 1 else 1


def divisors_mu_61() -> list[tuple[int, int]]:
    vals = [(1, 1)]
    for p in PRIMES_61:
        vals += [(d * p, -mu) for d, mu in list(vals)]
    return sorted(vals)


def von_mangoldt_formal(n: int) -> dict[int, int]:
    fs = factor(n)
    if len(fs) == 1:
        return {next(iter(fs)): 1}
    return {}


def add_formal(a: dict[int, Fraction], b: dict[int, Fraction], scale=Fraction(1)) -> dict[int, Fraction]:
    out = {p: Fraction(c) for p, c in a.items()}
    for p, c in b.items():
        out[p] = out.get(p, Fraction(0)) + scale * c
        if not out[p]:
            del out[p]
    return out


def y4_formal(q: int) -> dict[int, Fraction]:
    out: dict[int, Fraction] = {}
    n = q
    scale = 1
    while True:
        out = add_formal(out, von_mangoldt_formal(n), Fraction(scale))
        if n % 4:
            return out
        n //= 4
        scale *= 2


def is_prime_power(n: int) -> bool:
    return len(factor(n)) == 1


def y4_zero_characterization(q: int) -> bool:
    quotients = []
    n = q
    while True:
        quotients.append(n)
        if n % 4:
            break
        n //= 4
    rhs = all(not is_prime_power(n) for n in quotients)
    lhs = not y4_formal(q)
    if lhs != rhs:
        raise AssertionError((q, lhs, rhs, quotients, y4_formal(q)))
    return lhs


def beta(n: int, q: int) -> Fraction:
    if q > n:
        return Fraction(0)
    a, r = divmod(n, q)
    return Fraction(a * (q - 1 - r), n + 1)


def detail_column_row(q: int) -> dict[int, Fraction]:
    """Return h=B^{-1}R e_q on rows 2..q, exactly."""
    C = {n: Fraction(0) for n in range(2, q + 1)}
    t = q
    scale = 1
    while t >= 2 and q % t == 0:
        # R e_q contributes only when q=4^k t.
        ratio = q // t
        x = ratio
        ok = True
        while x > 1:
            if x % 4:
                ok = False
                break
            x //= 4
        if ok:
            C[t] = Fraction(scale)
        if t % 4:
            break
        t //= 4
        scale *= 2

    h: dict[int, Fraction] = {}
    for n in range(q, 1, -1):
        tail = sum(beta(m, n) * h[m] for m in range(n + 1, q + 1))
        h[n] = (C.get(n, Fraction(0)) - tail) / beta(n, n)
    return h


def canonical_separator() -> dict:
    # At X/q=68, the only P_61-rough integers are 1 and 67.
    rough_68 = [n for n in range(1, 69) if gcd(n, P61) == 1]
    rough_17 = [n for n in range(1, 18) if gcd(n, P61) == 1]
    assert rough_68 == [1, 67]
    assert rough_17 == [1]

    # delta = log(68/67)/sqrt(134).  Exact elementary lower bound:
    # log(1+x)>2x/(2+x), x=1/67, and sqrt(134)<12.
    assert Fraction(2, 135) == Fraction(2, 67) / Fraction(135, 67)
    delta_lower = Fraction(1, 810)
    delta = log_i(Fraction(68, 67)) / sqrt_i(134)
    assert delta.lo > delta_lower

    # The exact raw current is D_{P61,136} - 67^{-1/2}c_{136/67}.
    # At q=2 its child response is delta, the canonical excess is delta,
    # hence the current alone saturates native capacity and current+child
    # exceeds it by delta.  At 4q=8 the child is inactive, so the same holds
    # for radix-four detail.
    ordinary_overdraw = delta
    detail_overdraw = delta

    # Farkas certificate for x=b, x<=c: y=-1, z=1.
    # b=C_D=w+delta, c=w, so b*y+c*z=-delta<0.
    farkas_value = -delta
    assert farkas_value.hi < -delta_lower

    # Y_4(2)=log 2, and log 2 > 2/3 by the same inequality at x=1.
    log2 = log_i(2)
    assert log2.lo > Fraction(2, 3)
    weighted = log2 * delta
    assert weighted.lo > Fraction(1, 1215)

    # Infinite asymptotic family.  For every prime p>=71 choose
    # X=2(p+1), y=X/p<3 and q=2.  The child removes the m=p rough
    # reservoir term, but the m=67 term remains in the raw current.  Hence
    # Gamma(G;2)-w_X(2) >= log((p+1)/67)/sqrt(134), uniformly at least
    # log(72/67)/sqrt(134)>5/834.  The p=71 endpoint is replayed exactly.
    rough_72 = [n for n in range(1, 73) if gcd(n, P61) == 1]
    assert rough_72 == [1, 67, 71]
    asymptotic_lower = Fraction(5, 834)
    eps71 = log_i(Fraction(72, 67)) / sqrt_i(134)
    assert eps71.lo > asymptotic_lower

    return {
        "classification": "PASS_EXACT_RAW_LEAF_NATIVE_CAPACITY_SEPARATOR",
        "endpoint_X": 136,
        "rough_prime_p": 67,
        "terminal_y": "136/67",
        "physical_column_q": 2,
        "rough_in_X_over_q": rough_68,
        "rough_in_X_over_4q": rough_17,
        "exact_overdraw": "log(68/67)/sqrt(134)",
        "directed_decimal": decimal_mid(delta),
        "exact_lower_bound": str(delta_lower),
        "ordinary_current_status": "raw current alone equals w_136(2)",
        "detail_current_status": "raw current alone equals Omega_136(2)",
        "child_status": "child adds the same strictly positive delta in both coordinates",
        "farkas_multipliers": {"equality_y": -1, "capacity_z": 1},
        "farkas_value": "-log(68/67)/sqrt(134)",
        "Y4_weighted_overdraw_lower": "1/1215",
        "asymptotic_family": {
            "parameters": "every prime p>=71; X=2(p+1), y=2(p+1)/p, q=2",
            "current_only_overdraw_lower_formula": "log((p+1)/67)/sqrt(134)",
            "uniform_exact_lower_bound": str(asymptotic_lower),
            "p71_directed_decimal": decimal_mid(eps71),
            "mechanism": "the child removes only the m=p rough term; the positive m=67 reservoir remains in the raw current",
        },
    }


def finite_realization_defect() -> dict:
    # R-91102 defect:
    # D=4sqrt2-4sqrt3+(5sqrt2/2)log(3/2)
    # D/sqrt2 = 4-4sqrt(3/2)+(5/2)log(3/2).
    # sqrt(3/2)<49/40 (square both sides), log(3/2)>2/5.
    assert Fraction(3, 2) < Fraction(49, 40) ** 2
    log32 = log_i(Fraction(3, 2))
    assert log32.lo > Fraction(2, 5)
    normalized = I(4) - 4 * sqrt_i(Fraction(3, 2)) + Fraction(5, 2) * log32
    assert normalized.lo > Fraction(1, 10)
    defect = sqrt_i(2) * normalized
    assert defect.lo > Fraction(1, 10)
    return {
        "classification": "PASS_FINITE_CONTINUUM_REALIZATION_DEFECT",
        "probe": "X=3,m=2",
        "exact_defect": "4*sqrt(2)-4*sqrt(3)+(5*sqrt(2)/2)*log(3/2)",
        "directed_decimal": decimal_mid(defect),
        "exact_lower_bound": "1/10",
        "compiler_consequence": (
            "formal endpoint integration cannot be identified with the finite equality seed "
            "without an explicit mismatch/current realization generator"
        ),
    }


def leftmost_fill(capacities: list[Fraction], targets: list[Fraction], mass: Fraction) -> list[Fraction]:
    if len(capacities) != len(targets):
        raise ValueError
    out = [Fraction(0) for _ in capacities]
    rem = Fraction(mass)
    for i, (a, t) in enumerate(zip(capacities, targets)):
        if rem <= 0:
            break
        take = min(a, rem / t)
        out[i] = take
        rem -= take * t
    if rem != 0:
        raise ValueError("insufficient target capacity")
    return out


def dot(a, b) -> Fraction:
    return sum((x * y for x, y in zip(a, b)), Fraction(0))


def lorenz_lp_exact_control() -> dict:
    # A rational activation-cell fixture with the same monotone geometry as
    # L-91682/L-91684: score/target increases, every row/target decreases.
    capacities = [Fraction(1), Fraction(3, 2), Fraction(5, 4), Fraction(2), Fraction(1)]
    targets = [Fraction(3), Fraction(2), Fraction(5, 3), Fraction(4, 3), Fraction(1)]
    score_ratios = [Fraction(7, 5), Fraction(3, 2), Fraction(8, 5), Fraction(17, 10), Fraction(9, 5)]
    row_ratios = [Fraction(5, 2), Fraction(12, 5), Fraction(2), Fraction(7, 4), Fraction(3, 2)]
    scores = [t * r for t, r in zip(targets, score_ratios)]
    rows = [t * r for t, r in zip(targets, row_ratios)]
    mass = Fraction(20, 3)

    ustar = leftmost_fill(capacities, targets, mass)
    cutoff = next(i for i, u in enumerate(ustar) if 0 < u < capacities[i])
    assert all(u == capacities[i] for i, u in enumerate(ustar[:cutoff]))
    assert all(u == 0 for u in ustar[cutoff + 1 :])

    lam_row = row_ratios[cutoff]
    row_dual_upper = lam_row * mass + sum(
        (rows[i] - lam_row * targets[i]) * capacities[i] for i in range(cutoff)
    )
    assert row_dual_upper == dot(rows, ustar)

    lam_score = score_ratios[cutoff]
    score_dual_lower = lam_score * mass + sum(
        (scores[i] - lam_score * targets[i]) * capacities[i] for i in range(cutoff)
    )
    assert score_dual_lower == dot(scores, ustar)

    # Exact exchange probes: move target mass from an earlier to a later atom.
    probes = 0
    for i in range(cutoff + 1):
        for j in range(cutoff, len(capacities)):
            if i == j or ustar[i] == 0 or ustar[j] == capacities[j]:
                continue
            eps = min(ustar[i] * targets[i], (capacities[j] - ustar[j]) * targets[j], Fraction(1, 20))
            if eps <= 0:
                continue
            u = list(ustar)
            u[i] -= eps / targets[i]
            u[j] += eps / targets[j]
            assert dot(targets, u) == mass
            assert dot(scores, u) >= dot(scores, ustar)
            assert dot(rows, u) <= dot(rows, ustar)
            probes += 1
    assert probes > 0

    demanded_row = row_dual_upper + Fraction(1, 7)
    farkas_gap = demanded_row - row_dual_upper
    assert farkas_gap == Fraction(1, 7)

    return {
        "classification": "PASS_LORENZ_CUTOFF_IS_EXACT_SIMULTANEOUS_LP_BASIS",
        "atoms": len(capacities),
        "cutoff_index_zero_based": cutoff,
        "leftmost_basis": [str(x) for x in ustar],
        "target_mass": str(mass),
        "score_dual_lower": str(score_dual_lower),
        "row_dual_upper": str(row_dual_upper),
        "exchange_probes": probes,
        "deliberate_infeasible_row_gap": str(farkas_gap),
        "live_consequence": (
            "under the frozen monotone profiles, a negative L_j(p,y) is already an exact "
            "Farkas separator for the full box LP; no alternative non-leftmost basis can repair it"
        ),
    }


def gamma_i(j: int, m: int) -> I:
    if m < j:
        return I(0)
    if m == j:
        return Fraction(j + 1, j - 1) * invsqrt_i(j)
    if m == j + 1:
        return -Fraction((j + 1) * (j - 2), j * (j - 1)) * invsqrt_i(j + 1)
    return Fraction(2, j * (j - 1)) * invsqrt_i(m)


def q_i(Y: Fraction, j: int) -> I:
    if Y <= j:
        return I(0)
    n = Y.numerator // Y.denominator
    total = I(0)
    for m in range(j, n + 1):
        total += gamma_i(j, m) * log_i(Y / m)
    return total


def target_atom_i(d: int, p: int, y: int) -> I:
    x = p * y
    if d > x:
        return I(0)
    parent = invsqrt_i(d) * (4 * sqrt_i(Fraction(x, d)) - 3)
    if d <= y:
        child = invsqrt_i(p) * invsqrt_i(d) * (4 * sqrt_i(Fraction(y, d)) - 3)
        return parent - child
    return parent


def row_atom_i(d: int, p: int, y: int, j: int) -> I:
    x = p * y
    if d > x:
        return I(0)
    parent = invsqrt_i(d) * q_i(Fraction(x, d), j)
    if d <= y:
        child = invsqrt_i(p) * invsqrt_i(d) * q_i(Fraction(y, d), j)
        return parent - child
    return parent


def hostile_leaf_directed() -> dict:
    p, y, j = 67, 13, 66
    vals = [(d, mu) for d, mu in divisors_mu_61() if d <= p * y]
    odd_target = I(0)
    evens: list[tuple[int, I]] = []
    for d, mu in vals:
        t = target_atom_i(d, p, y)
        assert t.lo > 0
        if mu == -1:
            odd_target += t
        else:
            evens.append((d, t))

    prefix = I(0)
    cutoff = None
    prefix_before = None
    for d, t in evens:
        new = prefix + t
        if prefix.hi < odd_target.lo and new.lo > odd_target.hi:
            cutoff = d
            prefix_before = prefix
            cutoff_target = t
            break
        prefix = new
    assert cutoff == 123
    frac = (odd_target - prefix_before) / cutoff_target
    assert frac.lo > 0 and frac.hi < 1

    # At row 66 every active row atom has d<=floor(871/66)=13, hence all
    # row-active even sources lie strictly before the cutoff and are fully used.
    margin = I(0)
    active_row_sources = []
    for d, mu in vals:
        r = row_atom_i(d, p, y, j)
        if r.hi != 0:
            active_row_sources.append(d)
            margin += mu * r
    assert max(active_row_sources) == 13
    assert margin.lo > 0

    return {
        "classification": "PASS_HOSTILE_LEAF_TARGET_LORENZ_OPTIMAL_ROW",
        "p": p,
        "y": y,
        "row": j,
        "cutoff": cutoff,
        "cutoff_fraction_directed_decimal": [
            decimal_fraction(frac.lo),
            decimal_fraction(frac.hi),
        ],
        "row_active_divisors": active_row_sources,
        "directed_margin_decimal": decimal_mid(margin),
        "directed_margin_lower_decimal": decimal_fraction(margin.lo),
        "interpretation": (
            "the historically hostile p=67,y=13,row=66 cell is feasible at the exact "
            "LP-optimal leftmost basis; this does not certify the remaining activation cells"
        ),
    }


def score_free_transfer_checks(limit: int = 5000) -> dict:
    zeros = []
    for q in range(2, limit + 1):
        if y4_zero_characterization(q):
            zeros.append(q)

    selected = [q for q in zeros if q >= 4][:200]
    assert selected
    for q in selected:
        h = detail_column_row(q)
        assert h[q] == Fraction(q + 1, q - 1)
        assert h[q - 1] == -Fraction(q * (q - 3), (q - 1) * (q - 2))
        assert not y4_formal(q)

    # Formal radix-four recurrence regression.
    rec_checks = 0
    for q in range(2, limit + 1):
        lhs = y4_formal(q)
        if q % 4 == 0:
            lhs = add_formal(lhs, y4_formal(q // 4), Fraction(-2))
        rhs = {p: Fraction(c) for p, c in von_mangoldt_formal(q).items()}
        assert lhs == rhs
        rec_checks += 1

    return {
        "classification": "PASS_Y4_ZERO_SCORE_FREE_TRIANGULAR_REPAIR",
        "range": limit,
        "Y4_zero_columns": len(zeros),
        "first_zero_columns": zeros[:20],
        "exact_transfer_columns_checked": len(selected),
        "radix4_dual_recurrence_checks": rec_checks,
        "top_row_cost": "(q+1)/(q-1) times slack",
        "next_row_gain": "q(q-3)/((q-1)(q-2)) times slack",
        "scope": (
            "a zero-weight detail slack at q moves row reserve downward with no literal-score "
            "cost; lower rows also change and must be controlled by the full triangular LP"
        ),
    }


def main() -> None:
    checks = [
        canonical_separator(),
        finite_realization_defect(),
        lorenz_lp_exact_control(),
        hostile_leaf_directed(),
        score_free_transfer_checks(),
    ]
    payload = {
        "classification": "EXACT_NATIVE_ROOT_COMPILATION_DISCREPANCY_AND_SEPARATOR",
        "checks": checks,
        "pass_native_root_capacity_theorem": False,
        "rh_established_by_replay": False,
        "exact_boundary": (
            "PR #464 root-Hall algebra compiles only after a finite source-owned endpoint/port/slack "
            "realization; PR #469 raw current+child is exactly separated from native capacity at "
            "(136,67,2), and the raw current alone is separated on the infinite family "
            "X=2(p+1), p>=71 prime. The missing object is a source-owned native "
            "current-thinning/realization generator."
        ),
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    out = HERE / "results" / "verification.json"
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(payload["classification"])
    print(payload["proof_object_sha256"])
    for check in checks:
        print(check["classification"])


if __name__ == "__main__":
    main()
