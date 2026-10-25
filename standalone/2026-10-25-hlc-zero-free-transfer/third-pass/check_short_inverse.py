#!/usr/bin/env python3
"""Exact scalar checks for SHORT_INVERSE.md, plus labeled decimal diagnostics.

This checker proves polynomial identities by coefficient equality and checks
the rational example exactly. It does not test native character sums or
certify any imported analytic theorem.
"""

from decimal import Decimal, localcontext
from fractions import Fraction as F


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


# Sparse two-variable polynomials over Q; equality is coefficient equality.
def clean(p):
    return {ij: v for ij, v in p.items() if v}


def add(p, q):
    out = dict(p)
    for ij, v in q.items():
        out[ij] = out.get(ij, F(0)) + v
    return clean(out)


def neg(p):
    return {ij: -v for ij, v in p.items()}


def sub(p, q):
    return add(p, neg(q))


def mul(p, q):
    out = {}
    for (i, j), v in p.items():
        for (k, l), w in q.items():
            key = (i + k, j + l)
            out[key] = out.get(key, F(0)) + v * w
    return clean(out)


def scale(p, c):
    return clean({ij: c * v for ij, v in p.items()})


def dx(p):
    return clean({(i - 1, j): i * v for (i, j), v in p.items() if i})


def dc(p):
    return clean({(i, j - 1): j * v for (i, j), v in p.items() if j})


one = {(0, 0): F(1)}
x = {(1, 0): F(1)}
c = {(0, 1): F(1)}
Dpoly = sub(scale(one, 3), mul(add(one, c), x))
Ppoly = mul(sub(scale(one, 2), mul(c, x)), sub(one, x))

numerator_dx = sub(mul(dx(Ppoly), Dpoly), mul(Ppoly, dx(Dpoly)))
expected_dx = sub(
    add(neg(add(scale(one, 4), c)), scale(mul(c, x), 6)),
    mul(mul(c, add(one, c)), mul(x, x)),
)
require(numerator_dx == expected_dx, "Derivative identity (7) failed")

expected_gap = mul(x, sub(add(scale(one, 4), c), scale(mul(c, x), 3)))
require(sub(scale(Dpoly, 2), scale(Ppoly, 3)) == expected_gap, "Capacity gap identity")

numerator_dc = sub(mul(dc(Ppoly), Dpoly), mul(Ppoly, dc(Dpoly)))
require(numerator_dc == neg(mul(x, mul(sub(one, x), sub(one, x)))), "Parameter derivative identity")

# Self-contact identity after delta=alpha-A, with x=A, c=C.
contact_polynomial = sub(
    add(scale(mul(add(x, c), x), 2), mul(x, c)),
    mul(x, add(scale(x, 2), scale(c, 3))),
)
require(contact_polynomial == {}, "Generic self-contact identity")

# Negative control: changing the 3C in the crossing to 2C must break contact.
bad_contact = sub(
    add(scale(mul(add(x, c), x), 2), mul(x, c)),
    mul(x, add(scale(x, 2), scale(c, 2))),
)
require(bad_contact != {}, "Negative control failed to detect a wrong crossing")

alpha = F(5, 6)


def source_values(delta, amplitude, kappa):
    cc = 2 / (3 * kappa)
    xx = amplitude / delta
    dp = 3 - (1 + cc) * xx
    pp = (2 - cc * xx) * (1 - xx)
    cap = delta * pp / dp
    aa = alpha - delta
    count = 1 - delta + aa * cap / (2 * (aa + cap))
    cutoff = 1 + cap / (2 * (aa + cap))
    return cap, count, cutoff


def absolute_amplitude_values(delta, amplitude, kappa):
    cc = 2 / (3 * kappa)
    nn = (2 * delta - cc * amplitude) * (delta - amplitude)
    qq = 3 * delta - (1 + cc) * amplitude
    cap = nn / qq
    aa = alpha - delta
    count = 1 - delta + aa * cap / (2 * (aa + cap))
    return cap, count


def old_inverse(r):
    return (1 + 5 * r) / 6


g = F(37, 100)
delta_cap = F(3, 4)
r = F(7, 5)
kappa = F(3, 4)
cap, count = absolute_amplitude_values(delta_cap, g, kappa)
require(cap == F(10013, 34900), "Rational capacity")
require(count == F(87541, 310112), "Rational class count")
new_exponent = count + delta_cap * r
saving = old_inverse(r) - new_exponent
require(saving == F(4861, 4651680), "Exact restricted saving")
contact = (count - F(1, 6)) / (alpha - delta_cap)
require(contact == F(107567, 77528), "Exact first contact")
require(F(67, 49) < contact < F(7, 5) < F(10, 7), "Contact ordering")
require(r - 1 - F(18, 49) == F(8, 245), "Derivative margin")
require(F(6, 25) < g, "Critical amplitude below threshold")

# Rational cross-checks of the two parameterizations and included-line contact.
# These exercise the formulas; the displayed polynomial identities are exact
# generic checks, not inferred from this sample.
cases = 0
for kap in [F(13, 18), F(3, 4), F(4, 5), F(1)]:
    for deltai in range(1, 76):
        delta = F(deltai, 100)
        for xi in range(21):
            xx = F(xi, 40)
            gg = delta * xx
            C1, R1, t1 = source_values(delta, gg, kap)
            C2, R2 = absolute_amplitude_values(delta, gg, kap)
            require(C1 == C2 and R1 == R2, "Parameterizations agree")
            require(R1 + delta * t1 == old_inverse(t1), "Inverse contact")
            require(1 - delta + C1 * (F(3, 2) - t1) == R1, "Short contact")
            require(C1 <= 2 * delta / 3, "Capacity bound")
            require(1 <= t1 <= F(3, 2), "Cutoff range")
            cases += 1

print("EXACT polynomial identities: 4 PASS")
print("EXACT negative crossing mutation: detected")
print("EXACT rational parameterization/contact cases:", cases, "PASS")
print("EXACT restricted exponent:", new_exponent)
print("EXACT saving:", saving)
print("EXACT first contact:", contact)
print("EXACT derivative margin at r=7/5:", F(8, 245))


def bisect_decimal(fun, lo, hi, rounds=180):
    flo = fun(lo)
    fhi = fun(hi)
    require(flo * fhi < 0, "Decimal bisection sign bracket")
    for _ in range(rounds):
        mid = (lo + hi) / 2
        fm = fun(mid)
        if fm == 0 or mid == lo or mid == hi:
            return mid
        if flo * fm < 0:
            hi = mid
        else:
            lo, flo = mid, fm
    return (lo + hi) / 2


with localcontext() as ctx:
    ctx.prec = 60
    Q = Decimal

    def quartic(k):
        return 16686*k**4 - 27405*k**3 + 9936*k**2 + 1290*k - 275

    kap = bisect_decimal(
        quartic, Q("0.749773294079928"), Q("0.749773294079929")
    )

    def critical(delta):
        return (
            (3 - 324*kap*kap)*delta*delta
            + (756*kap*kap - 54*kap - 5)*delta
            + 40*kap - 300*kap*kap
        )

    delta = bisect_decimal(critical, Q(".46"), Q(".48"))
    gg = delta / 2
    aa = Q(5) / 6
    cc = 2 / (3 * kap)

    def cfun(d):
        return (2*d - cc*gg) * (d-gg) / (3*d - (1+cc)*gg)

    def rfun(d):
        A, C = aa-d, cfun(d)
        return 1-d + A*C/(2*(A+C))

    cutoff = 1 + cfun(delta)/(2*(aa-delta+cfun(delta)))
    old = (1+5*cutoff)/6
    require(abs((rfun(delta)+delta*cutoff)-old) < Q("1e-55"), "Decimal contact consistency")

    def derivative(d):
        N = (2*d-cc*gg)*(d-gg)
        Np = 4*d-(2+cc)*gg
        Z = 3*d-(1+cc)*gg
        Cp = (Np*Z-3*N)/(Z*Z)
        C, A = cfun(d), aa-d
        return cutoff-1 + (-C*C+A*A*Cp)/(2*(A+C)**2)

    stationary = bisect_decimal(derivative, delta, kap)
    competitor = rfun(stationary)+stationary*cutoff
    require(competitor > old, "Stationary competitor is above the old exponent")
    print("DECIMAL DIAGNOSTICS ONLY (not a global maximum certificate):")
    for name, value in [
        ("kappa_flat", kap), ("delta_c", delta), ("g_c", gg),
        ("t_c", cutoff), ("R_c", rfun(delta)),
        ("old inverse at t_c", old), ("stationary delta", stationary),
        ("stationary competitor", competitor), ("excess over old", competitor-old),
    ]:
        print(" ", name, "=", value)

print("No native moment, imported theorem, zero-free boundary, or RH certified.")
