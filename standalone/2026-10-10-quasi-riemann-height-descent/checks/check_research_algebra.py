#!/usr/bin/env python3
"""Exact controls for the geometric perturbation, envelope limit and causal cost.

Standard library only. No float optimization, physical-height numerics, Lean
build or global analytic theorem is accepted by this checker.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from math import gcd, isqrt
import json

from check_tail_euler import P


PREDICATES = 0


def check(condition, message):
    global PREDICATES
    PREDICATES += 1
    if not condition:
        raise RuntimeError(message)


@dataclass(frozen=True)
class Q:
    """Exact a+b*sqrt(921)."""
    a: F = F(0)
    b: F = F(0)

    @staticmethod
    def of(x):
        return x if isinstance(x, Q) else Q(F(x))

    def __add__(self, other):
        other = Q.of(other)
        return Q(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Q(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-Q.of(other))

    def __rsub__(self, other):
        return Q.of(other) - self

    def __mul__(self, other):
        other = Q.of(other)
        return Q(self.a*other.a + 921*self.b*other.b,
                 self.a*other.b + self.b*other.a)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = Q.of(other)
        norm = other.a*other.a - 921*other.b*other.b
        if norm == 0:
            raise ZeroDivisionError("zero quadratic denominator")
        return self * Q(other.a/norm, -other.b/norm)

    def __rtruediv__(self, other):
        return Q.of(other) / self


def mobius(n):
    remaining = n
    value = 1
    p = 2
    while p*p <= remaining:
        if remaining % p == 0:
            value = -value
            remaining //= p
            if remaining % p == 0:
                return 0
            while remaining % p == 0:
                remaining //= p
        p += 1
    return -value if remaining > 1 else value


def sixth_root_floor(x):
    x = F(x)
    if x < 0:
        raise ValueError("nonnegative horizon required")
    lo, hi = 0, 1
    while F(hi**6) <= x:
        hi *= 2
    while hi-lo > 1:
        mid = (lo+hi)//2
        if F(mid**6) <= x:
            lo = mid
        else:
            hi = mid
    return lo


def run():
    # Authenticate the original nonnegative endpoint certificate as an exact
    # polynomial identity, not a finite-grid sign test.
    y, delta = P.var(0), P.var(1)
    v = 51+41*y
    py = 7+18*y+8*y**2
    jy = 185+170*y+(-138+12*y+96*y**2)*delta
    lhs = v*(2*jy*(1+(3+8*y)*delta)
             -468*(F(5,6)-delta)*delta*py)
    rhs = ((3+5*y)*((4*v*delta-79)**2+49)
           +4*y*(4*v*delta*((1+3*y)*(15+32*y)*delta+9-13*y)
                  +265+3485*y))
    check(not (lhs-rhs).terms, "original endpoint polynomial identity")
    check(F(9)-13*F(1,2) == F(5,2), "nonnegative certificate factor")
    check(not (17*(3+5*y)-v-44*y).terms, "certificate denominator comparison")
    check(F(49,176256)/F(5,2) == F(49,440640), "original uniform margin")

    # Exact new tuple and margins.
    shift = F(1,40000)
    ell, b = F(1,6)+shift, F(1,8)
    lx, ly = (1-ell-b)/2, (1-ell+b)/2
    h, M = (1+3*ell+b)/2, 1-ell
    beta0 = F(11,12)-ell/4
    check((ell,h,lx,ly,beta0) ==
          (F(20003,120000),F(65003,80000),F(84997,240000),
           F(114997,240000),F(139999,160000)), "candidate rational tuple")
    check(lx+ly == M and M+ell == 1 and h == 1-lx+ell,
          "all structural equalities")
    check(beta0+lx/2-1+h/6 == lx/2+b/12, "new low signal equality")
    check(ell < F(1,5), "rescaled low penalty maximizes at zero")
    check(F(-1) < 0 and -1+F(1,8) < 0, "both low penalty slopes")
    check(lx-ell > 0, "shortest x length")
    check(M-2*ell == F(19997,40000), "shortest row length")
    check(ly-ell-F(11,6)*b == F(19991,240000), "Gram domination slack")
    check(ell/h > F(8,39) > F(7,37), "prime capacity supply")
    check(5*ell-h > F(1,48), "frequency extension supply")
    main_margin = F(49,440640)-F(5,2)*shift
    check(main_margin == F(1073,22032000) > 0, "new endpoint margin")
    check(F(7,1200)-F(32,25)*shift > 0, "floor endpoint")
    check(F(49,14400)-F(177,200)*shift > 0, "intermediate endpoint")
    check(F(63,800)-F(51,100)*shift > 0, "small rows")
    check(beta0 > F(437,500), "new boundary inside extended contour box")
    check(ly/20 > 0 and h/600 > 0, "principal contour margins")

    # Exact obstruction in Q(sqrt(921)); no algebraic-number float comparison.
    radical = Q(0,F(1))
    d0 = (49-radical)/48
    check(288*d0*d0-588*d0+185 == Q(), "quadratic equation for delta0")
    Dx, Px = F(37,18), F(7,9)
    J = (F(5,6)-d0)*Dx+d0*Px
    rstar = 1-d0+(F(5,6)-d0)*d0*Px/(2*J)
    check(rstar == Q(F(2,3)), "Rstar is exactly two thirds")
    ellstar = (8*radical+33)/1653
    betastar = (1507-2*radical)/1653
    check((5-6*d0)/(9+18*d0) == ellstar, "exact ell limit")
    check(F(11,12)-ellstar/4 == betastar, "exact beta limit")
    check(Q(F(1,6))-(1-rstar)/2 == Q(), "imbalance b cancels")
    check(-F(5,12)+d0/2+ellstar*(F(3,4)+3*d0/2) == Q(),
          "envelope vanishes at exact ell limit")
    scale = 10**15
    lower_num = isqrt(921*scale*scale)
    root_lo, root_hi = F(lower_num,scale), F(lower_num+1,scale)
    check(root_lo*root_lo < 921 < root_hi*root_hi, "strict radical enclosure")
    bound_lo, bound_hi = (1507-2*root_hi)/1653,(1507-2*root_lo)/1653
    check(F(87495706,10**8) < bound_lo < bound_hi < F(87495708,10**8),
          "certified decimal bracket for envelope limit")
    check(bound_hi < beta0, "safe tuple is above geometry-envelope limit")

    # Causal inversion at c=2/3: coefficients have the rational weight n^-1.
    # This tests the actual finite dilation composition, including horizons
    # between sixth powers, in both orders.
    def source(z):
        return z*z+3*z+1 if z >= 1 else F(0)
    def operator(f,z,inverse):
        return sum((F(mobius(n) if inverse else 1,n)*f(z/F(n**6))
                    for n in range(1,sixth_root_floor(z)+1)),F(0))
    horizons = [F(1),F(63),F(64),F(65),F(127,2),F(192),
                F(729),F(4095),F(4096),F(4097),F(15625)]
    for z in horizons:
        check(operator(lambda u:operator(source,u,False),z,True) == source(z),
              "finite inverse-forward causal composition")
        check(operator(lambda u:operator(source,u,True),z,False) == source(z),
              "finite forward-inverse causal composition")
    check(F(2,3)-F(11,16) == -F(1,48), "absolute causal source floor")
    for theta, expected in [(F(1),F(2,3)),(F(7,8),F(31,48)),
                            (F(1,2),F(7,12))]:
        check((3+theta)/6 == expected, "conditional angular threshold")

    # Conditional higher-moment extraction exponent, not a moment estimate.
    targets = {}
    for k, target in [(1,F(11,12)),(2,F(17,24)),(3,F(23,36))]:
        exponent = F(1,2)+F(5,12*k)
        check(exponent == target, "limiting higher-moment extraction exponent")
        targets[str(2*k)] = str(target)

    # A finite structural model of the exact gcd decomposition. The phases
    # lie in {+1,-1}, a subgroup of the sixth roots of unity, are completely
    # multiplicative in the column, and have the required nonunit zeros.
    # They are not asserted to be the actual Eisenstein sextic symbols.
    def symbol(n,u):
        if gcd(n,u) != 1:
            return 0
        remaining, phase, p = n, 1, 2
        while p*p <= remaining:
            while remaining % p == 0:
                phase *= -1 if (p*u+p+u) % 3 == 0 else 1
                remaining //= p
            p += 1
        if remaining > 1:
            phase *= -1 if (remaining*u+remaining+u) % 3 == 0 else 1
        return phase
    def weight(x):
        return (x-1)**2*(2-x)**2 if 1 < x < 2 else F(0)
    gcd_panels = 0
    for D0 in [2,3,5,9,17]:
        for u in range(1,19):
            original = sum((mobius(n)*symbol(n,u)*weight(F(n,D0))
                            for n in range(1,2*D0+1)),F(0))
            decomposed = F(0)
            for c0 in range(1,2*D0+1):
                if not mobius(c0):
                    continue
                X = F(D0,c0)
                inner = F(0)
                for a0 in range(1,(2*X).__floor__()+1):
                    for b0 in range(1,(2*X).__floor__()+1):
                        if gcd(a0,b0) == 1 and gcd(a0*b0,c0) == 1:
                            inner += (mobius(a0)*mobius(b0)*symbol(a0*b0,u)
                                      *weight(a0/X)*weight(b0/X))
                decomposed += symbol(c0,u)**2*inner
            check(original*original == decomposed,
                  "exact weighted gcd decomposition with zero extensions")
            gcd_panels += 1

    return {
        "status":"PASS",
        "explicit_predicates":PREDICATES,
        "arithmetic":"RATIONAL_POLYNOMIAL_AND_Q_SQRT_921",
        "candidate_boundary":str(beta0),
        "main_high_margin":str(main_margin),
        "geometry_limit_expression":"(1507-2*sqrt(921))/1653",
        "geometry_limit_strict_interval":[str(bound_lo),str(bound_hi)],
        "causal_horizons":[str(z) for z in horizons],
        "conditional_moment_targets":targets,
        "gcd_decomposition_panels":gcd_panels,
        "not_verified":["imported analytic lemmas", "higher moment hypothesis",
                        "local off-diagonal saving", "RH", "Lean kernel build"]
    }


if __name__ == "__main__":
    print(json.dumps(run(),indent=2,sort_keys=True))
