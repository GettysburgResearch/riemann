#!/usr/bin/env python3
"""Exact finite algebra for GCD_FOURTH_COMPONENT.md.

No imported cap, buffered density, moment, or global contour is certified.
All predicates remain active under python -O.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import gcd
from decimal import Decimal, localcontext


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


# Generic coefficient comparison after clearing Delta: variables x,y,P=1/q.
def add(*polys):
    result = {}
    for poly in polys:
        for powers, value in poly.items():
            result[powers] = result.get(powers, F(0)) + value
    return {powers: value for powers, value in result.items() if value}


def scale(poly, scalar):
    return {powers: scalar*value for powers, value in poly.items() if scalar*value}


def mul(*polys):
    result = {(0, 0, 0): F(1)}
    for poly in polys:
        out = {}
        for a, av in result.items():
            for b, bv in poly.items():
                key = tuple(i+j for i, j in zip(a, b))
                out[key] = out.get(key, F(0)) + av*bv
        result = {key: value for key, value in out.items() if value}
    return result


one = {(0, 0, 0): F(1)}
x, y, p = ({tuple(int(i == j) for i in range(3)): F(1)} for j in range(3))
delta_poly = mul(add(one, scale(mul(x, p), -1)),
                 add(one, scale(mul(y, p), -1)))
linear = add(scale(add(x, y), -1), mul(x, y, p),
             mul(delta_poly, add(x, y)))
expected_linear = add(
    scale(mul(add(mul(x, x), mul(x, y), mul(y, y)), p), -1),
    mul(x, y, add(x, y), p, p),
)
quadratic = add(mul(x, y), scale(mul(delta_poly, x, y), -1))
require(linear == expected_linear, "Generic linear correction identity")
require(quadratic == mul(x, y, add(one, scale(delta_poly, -1))),
        "Generic quadratic correction identity")


def local(q, xx, yy):
    dd = (1-xx/q)*(1-yy/q)
    require(dd != 0, "Safe scalar Delta")
    return dd, -(xx+yy-xx*yy/q)/dd, xx*yy/dd


# Direct finite harmonic gcd coefficients versus the normalized Euler
# coefficients, including shifted exponents coming from squarefree k.
primes = (7, 13)
coefficient_cases = 0
modified_factor_negatives = 0
for xx, yy in [(F(1), F(1)), (F(5, 4), F(5, 4)), (F(6, 5), F(4, 3))]:
    locals_ = [local(F(q), xx, yy) for q in primes]
    for punctured in product((0, 1), repeat=2):
        scalar = F(1)
        for flag, loc in zip(punctured, locals_):
            if not flag:
                scalar *= loc[0]
        for kbits in product((0, 1), repeat=2):
            for aexp in product(range(4), repeat=2):
                total_exp = tuple(k+a for k, a in zip(kbits, aexp))
                if any(flag and exponent for flag, exponent in zip(punctured, total_exp)):
                    continue
                direct = F(0)
                for dexp in product(range(3), repeat=2):
                    if any(flag and exponent for flag, exponent in zip(punctured, dexp)):
                        continue
                    term = F(1)
                    for q, ae, de in zip(primes, total_exp, dexp):
                        e = ae+de
                        raw = [F(1), -(xx+yy), xx*yy]
                        term *= (raw[e] if e <= 2 else F(0))/F(q)**de
                    direct += term
                predicted = F(1)
                modified = F(1)
                for flag, kb, ae, loc in zip(punctured, kbits, aexp, locals_):
                    if flag:
                        continue
                    _, bp, bp2 = loc
                    local_values = [F(1), bp, bp2]
                    te = kb+ae
                    predicted *= local_values[te] if te <= 2 else F(0)
                    values = ([bp, bp2, F(0), F(0)] if kb
                              else [F(1), bp, bp2, F(0)])
                    modified *= values[ae]
                    if kb and ae == 1:
                        modified_factor_negatives += bp2 != bp*bp
                require(direct/scalar == predicted == modified,
                        "Direct gcd coefficient and modified Euler local agree")
                coefficient_cases += 1
require(modified_factor_negatives > 0, "p^2 versus squared p mutation exercised")

# A coefficient b_p can vanish on an allowed equal-radius pair.
q, radius = F(7), F(5, 4)
sum_xy, product_xy = F(25, 112), F(25, 16)
require(sum_xy**2 < 4*product_xy, "Conjugate nonreal x,y exist")
require(product_xy == radius**2 and radius**8 < q, "beta >7/8")
dd = 1-sum_xy/q+product_xy/q**2
bp = -(sum_xy-product_xy/q)/dd
bp2 = product_xy/dd
require(dd == 1 and bp == 0 and bp2 == F(25, 16),
        "Modified factor must not be divided by b_p")
dd, bp, bp2 = local(q, radius, radius)
require(bp != -(2*radius)/dd, "Repeated-prime term cannot be dropped")
require(bp2 != bp*bp, "b_(p^2) cannot be replaced by b_p squared")


@lru_cache(None)
def mobius(n):
    ans = 1
    prime = 2
    while prime*prime <= n:
        if n % prime == 0:
            n //= prime
            if n % prime == 0:
                return 0
            ans = -ans
        prime += 1
    return -ans if n > 1 else ans


def cutoff(t):
    if t <= 1:
        return F(1)
    if t >= 2:
        return F(0)
    v = t-1
    return 1-10*v**3+15*v**4-6*v**5


def annulus(t):
    return (t-1)**2*(2-t)**2 if 1 < t < 2 else F(0)


def kernel(t):
    return (1-t)**2 if 0 <= t < 1 else F(0)


phases = ((1, 0), (0, 1), (-1, 0), (0, -1))
logs = {1: 0, 2: 1, 4: 2, 3: 3}


def character(n):
    return phases[logs[n % 5]] if n % 5 else (0, 0)


def conjugate(v):
    return v[0], -v[1]


def multiply(v, w):
    return v[0]*w[0]-v[1]*w[1], v[0]*w[1]+v[1]*w[0]


def plus_weighted(total, phase, weight):
    return total[0]+phase[0]*weight, total[1]+phase[1]*weight


def outer(y1, y2):
    out = {}
    for a in range(1, int(2*y1)+1):
        ma = mobius(a)*cutoff(F(a)/y1)
        if not ma:
            continue
        for b in range(1, int(2*y2)+1):
            mb = mobius(b)*cutoff(F(b)/y2)
            if mb:
                out[a*b] = out.get(a*b, F(0))+ma*mb
    return {n: value for n, value in out.items() if value}


def coefficients(outer_coeff, mask):
    bound = max(outer_coeff)
    return {
        a: sum((value/F(n//a) for n, value in outer_coeff.items()
                if n % a == 0 and gcd(n//a, mask) == 1), F(0))
        for a in range(1, bound+1)
    }


def direct_return(C, mask, scale, D, E):
    total = (F(0), F(0))
    for a, value in C.items():
        eta = annulus(F(a)/scale)
        if not value or not eta or gcd(a, mask) != 1:
            continue
        for b in range(1, int(F(5*a*E)/D)+1):
            if gcd(a, b) != 1:
                continue
            phase = multiply(character(a), conjugate(character(b)))
            weight = value*eta/F(a)*kernel(F(b)*D/(5*a*E))
            total = plus_weighted(total, phase, weight)
    return total


def inverted_return(C, mask, scale, D, E, wrong_weight=False, wrong_mask=False):
    total = (F(0), F(0))
    bound = max(C)
    for k in range(1, bound+1):
        if not mobius(k) or (not wrong_mask and gcd(k, mask) != 1):
            continue
        prefactor = F(mobius(k)) if wrong_weight else F(mobius(k), k)
        for a in range(1, bound//k+1):
            value, eta = C[k*a], annulus(F(k*a)/scale)
            if not value or not eta or gcd(a, mask) != 1:
                continue
            for b in range(1, int(F(5*a*E)/D)+1):
                phase = multiply(character(a), conjugate(character(b)))
                weight = prefactor*value*eta/F(a)*kernel(F(b)*D/(5*a*E))
                total = plus_weighted(total, phase, weight)
    return total


inversion_cases = wrong_weights = wrong_masks = 0
for y1, y2 in [(F(3), F(4)), (F(4), F(5))]:
    oo = outer(y1, y2)
    D = y1*y2/2
    for extra_Q in [1, 2, 3, 6]:
        mask = 5*extra_Q
        C = coefficients(oo, mask)
        for scale, E in product([F(3), F(5), F(8)], [1, 2, 3]):
            expected = direct_return(C, mask, scale, D, E)
            actual = inverted_return(C, mask, scale, D, E)
            require(expected == actual, "Exact coprimality inversion")
            wrong_weights += expected != inverted_return(
                C, mask, scale, D, E, wrong_weight=True)
            wrong_masks += expected != inverted_return(
                C, mask, scale, D, E, wrong_mask=True)
            inversion_cases += 1
require(wrong_weights > 0 and wrong_masks > 0, "Inversion mutations detected")

normalizer_cases = 0
for K, A, E, H, D, Q in product([F(1), F(2), F(7)], [F(1), F(3)],
                               [F(1), F(5)], [F(1), F(9)],
                               [F(2), F(11)], [F(3), F(13)]):
    L = Q*A*E/(D*H)
    normalized_square = 1/(K*K*E*H*A*L)
    original_square = D/(Q*K*K*A*A*E*E)
    require(normalized_square == original_square, "Exact normalized k weight")
    if K > 1:
        require(1/(K*E*H*A*L) != original_square,
                "k^(-1/2) mutation must fail")
    normalizer_cases += 1

scale_cases = 0
for theta, delta, b, r, fraction in product(
        [F(1, 10), F(1, 9), F(7, 60)],
        [F(1, 50), F(1, 3), F(3, 4)],
        [F(1, 4), F(7, 9), F(1)], [F(29, 25), F(117, 100)],
        [F(0), F(1, 4), F(3, 4), F(1)]):
    v = fraction*b
    lhs = -theta*r+theta*v+(theta+delta/2)*(b-v)
    rhs = theta*(b-r)+delta*(b-v)/2
    require(lhs == rhs, "Fixed-k scale cancellation")
    a, beta = (1+delta)/2, 1-theta
    require(a+beta > 1 and 2*a+beta > 1, "Absolute correction convergence")
    scale_cases += 1

b, s, rmin = F(7, 9), F(14, 9), F(29, 25)
Ecap = F(2, 7)+3*s/4
require(s > F(200, 147) and Ecap == F(61, 42), "Capped endpoint envelope")
require(Ecap-(1+s/50) == F(1327, 3150), "Printed floor is retained and smaller")
require(b/4+(1+Ecap)/2 == F(179, 126), "New exponent constant")
saving = (1+5*rmin)/6-(F(179, 126)-rmin/4)
require(saving == F(17, 6300), "Exact uniform saving")
require(saving-F(1, 1000) == F(107, 63000), "Exact consumer reserve")
require((1+5*rmin)/6-(F(9, 14)+F(39, 50)-rmin/4) == F(1, 2100),
        "Larger .78 cutoff has insufficient uniform saving")
require(F(1, 2100) < F(1, 1000), "Negative oversized-cutoff control")

print("Generic cleared-denominator polynomial identities: 2 PASS")
print("Direct gcd / modified Euler coefficient cases:", coefficient_cases, "PASS")
print("Exact b_p=0, b_(p^2)!=0 local configuration: PASS")
print("Exact coherent coprimality inversions:", inversion_cases, "PASS")
print("Wrong-weight and wrong-mask detections:", wrong_weights, wrong_masks)
print("Exact normalization cases:", normalizer_cases, "PASS")
print("Exact scale / convergence cases:", scale_cases, "PASS")
print("Exact smooth-head saving:", saving, "; consumer reserve:", F(107, 63000))
print("Negative repeated-prime, p^2, square-root k, and .78-margin controls: PASS")
with localcontext() as context:
    context.prec = 55
    rcrit = Decimal("1.1639535765090109563152515044677753096657280386958")
    old = (1+5*rcrit)/6
    new = Decimal(179)/126-rcrit/4
    print("DECIMAL DIAGNOSTICS ONLY: critical head exponent =", new)
    print("DECIMAL DIAGNOSTICS ONLY: critical saving =", old-new)
print("No imported theorem, complementary tail, new zero-free region, or RH certified.")

