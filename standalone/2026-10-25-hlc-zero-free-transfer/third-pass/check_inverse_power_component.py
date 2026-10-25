#!/usr/bin/env python3
"""Exact finite checks for INVERSE_POWER_COMPONENT.md.

No imported analytic theorem, character-sum moment, or zero-free region is
certified here. Every predicate remains active under python -O.
"""

from decimal import Decimal, localcontext
from fractions import Fraction as F
from math import gcd, isqrt


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def mobius_sieve(nmax):
    out = [1] * (nmax + 1)
    out[0] = 0
    prime = [True] * (nmax + 1)
    prime[0:2] = [False, False]
    for p in range(2, nmax + 1):
        if prime[p]:
            for n in range(p, nmax + 1, p):
                out[n] = -out[n]
                if n > p:
                    prime[n] = False
            for n in range(p * p, nmax + 1, p * p):
                out[n] = 0
    return out


def convolution(a, b):
    require(len(a) == len(b), "Convolution sizes")
    nmax = len(a) - 1
    out = [F(0)] * (nmax + 1)
    for m in range(1, nmax + 1):
        if not a[m]:
            continue
        for n in range(1, nmax // m + 1):
            if b[n]:
                out[m * n] += a[m] * b[n]
    return out


def algebraic_cutoff(x):
    # Smoothness is irrelevant to the exact identity. These rational
    # values exercise agreement through y and support before 2y.
    if x <= 1:
        return F(1)
    if x >= 2:
        return F(0)
    return 2 - x


hb_cases = 0
for y in [F(n) for n in range(2, 18)] + [F(5, 2), F(7, 2), F(13, 3)]:
    nmax = int(y * y)
    mu = mobius_sieve(nmax)
    my = [F(0)] + [
        mu[n] * algebraic_cutoff(F(n) / y) for n in range(1, nmax + 1)
    ]
    outer = convolution(my, my)
    rhs = convolution(outer, [F(0)] + [F(1)] * nmax)
    for n in range(1, nmax + 1):
        require(mu[n] == 2 * my[n] - rhs[n], "Exact smooth HB identity")
        hb_cases += 1

# The missing repeated-prime term r=2*2 breaks the ordinary identity.
mu = mobius_sieve(4)
my = [F(0)] + [F(mu[n]) if n <= 2 else F(0) for n in range(1, 5)]
bad_outer = [F(0)] * 5
for a in range(1, 5):
    for b in range(1, 4 // a + 1):
        if gcd(a, b) == 1:
            bad_outer[a * b] += my[a] * my[b]
bad_rhs = convolution(bad_outer, [F(0)] + [F(1)] * 4)
require(2 * my[4] - bad_rhs[4] != mu[4],
        "Negative control must detect dropped repeated-prime terms")

# An exact sixth-order toy Dirichlet phase, in Q(omega), with natural zeros.
# This only checks multiplicative zero bookkeeping in finite algebra.
def emul(x, y):
    a, b = x
    c, d = y
    return a * c - b * d, a * d + b * c - b * d


def eadd(x, y):
    return x[0] + y[0], x[1] + y[1]


def escale(a, x):
    return a * x[0], a * x[1]


one, zero, zeta6 = (F(1), F(0)), (F(0), F(0)), (F(1), F(1))
phases = [one]
for _ in range(6):
    phases.append(emul(phases[-1], zeta6))
require(phases[6] == one and phases[3] == (-1, 0), "Exact sixth roots")
log3 = {pow(3, j, 7): j for j in range(6)}


def character(n, puncture):
    if n % 7 == 0 or gcd(n, puncture) != 1:
        return zero
    return phases[log3[n % 7]]


masked_cases = 0
for puncture in [1, 2, 5, 10, 21, 30]:
    for a in range(1, 31):
        for b in range(1, 31):
            require(
                character(a * b, puncture)
                == emul(character(a, puncture), character(b, puncture)),
                "Natural zero extension stays multiplicative",
            )
            masked_cases += 1
    y, nmax = F(7), 49
    mu = mobius_sieve(nmax)
    my = [F(0)] + [
        mu[n] * algebraic_cutoff(F(n) / y) for n in range(1, nmax + 1)
    ]
    outer = convolution(my, my)
    for n in range(1, nmax + 1):
        actual = zero
        for d in range(1, n + 1):
            if n % d == 0:
                actual = eadd(
                    actual,
                    escale(
                        outer[d],
                        emul(character(d, puncture),
                             character(n // d, puncture)),
                    ),
                )
        target = escale(2 * my[n] - mu[n], character(n, puncture))
        require(actual == target, "Masked coherent HB coefficient")
        masked_cases += 1

# Reflection normalizers are positive; squared equalities are exact.
normalizer_cases = 0
normalizer_mutations = 0
for R in [F(1), F(3), F(11)]:
    for Q in [F(1), F(5)]:
        for D in [F(2), F(13)]:
            for E in [F(1), F(2), F(15)]:
                for H in [F(1), F(7), F(49)]:
                    for x in [F(1), F(4, 3), F(2)]:
                        for z in [F(1), F(5, 4)]:
                            r, q, N = R * x, Q * z, F(7)
                            actual_L = q * r * E / (D * H)
                            nominal_L = Q * R * E / (D * H)
                            lhs = 1 / (r * E * H * actual_L)
                            rhs = D / (q * r * r * E * E)
                            require(lhs == rhs, "Natural normalized reflection")
                            if E > 1:
                                require(
                                    1 / (r * H * actual_L) != rhs,
                                    "Negative control detects omitted E^(-1/2)",
                                )
                                normalizer_mutations += 1
                            require(
                                R * N / (r * actual_L)
                                == N / nominal_L / (z * x * x),
                                "Coupled z^(-1/2)x^(-1) profile normalizer",
                            )
                            normalizer_cases += 1

require(normalizer_mutations > 0, "Puncture negative controls were exercised")


def density(delta):
    return (15 - 16 * delta) / (15 - 6 * delta)


def old_inverse(r):
    return (1 + 5 * r) / 6


envelope_cases = 0
for i in range(101):
    delta = F(3 * i, 400)
    den = 15 - 6 * delta
    require(
        -16 * den + 6 * (15 - 16 * delta) == -150,
        "Generic density derivative numerator",
    )
    require(
        density(delta) - (1 - 2 * delta / 3)
        == -4 * delta * delta / den,
        "Density row-volume slack",
    )
    for slope in [F(0), F(1, 3), F(2, 3)]:
        require(density(delta) + slope * delta <= 1,
                "Below-contact envelope")
        envelope_cases += 1

# Rational t=sqrt(6s) parametrizes the complete interior formula exactly.
for i in range(61):
    t = F(2) + F(6, 7) * F(i, 60)
    slope = t * t / 6
    delta_star = F(5, 2) - 5 / t
    value = F(8, 3) + F(5, 12) * t * t - F(5, 3) * t
    require(0 <= delta_star <= F(3, 4), "Interior maximizer interval")
    require(slope == 150 / (15 - 6 * delta_star) ** 2,
            "Stationary slope identity")
    require(value == density(delta_star) + slope * delta_star,
            "Interior envelope formula")
    for j in range(101):
        delta = F(3 * j, 400)
        require(density(delta) + slope * delta <= value,
                "Concave-envelope rational comparison")
        envelope_cases += 1

require(density(F(3, 4)) == F(2, 7), "Top density")
require(F(200, 147) == 150 / (15 - 6 * F(3, 4)) ** 2,
        "Capped envelope slope contact")
for slope in [F(200, 147), F(3, 2), F(2), F(3)]:
    value = F(2, 7) + 3 * slope / 4
    for j in range(101):
        delta = F(3 * j, 400)
        require(density(delta) + slope * delta <= value, "Capped branch")
        envelope_cases += 1

# The fixed .51 floor is below even a legal, nonoptimal competitor.
require(F(1) + F(13, 10) / 50 == F(513, 500), "Printed floor exponent")
require(density(F(1, 2)) + F(13, 20) == F(37, 30),
        "Legal interior competitor")
require(F(37, 30) > F(513, 500), "No adjustable floor needed")
require(F(13, 10) < F(200, 147), "Endpoint in interior branch")
require((F(1) + F(71, 12)) / 2 == F(83, 24),
        "Component exponent rational part")

# Exact radical enclosure and required strict margin.
denom = 10 ** 45
num = isqrt(195 * denom * denom)
sqrt_lo, sqrt_hi = F(num, denom), F(num + 1, denom)
require(sqrt_lo * sqrt_lo < 195 < sqrt_hi * sqrt_hi,
        "Exact square-root enclosure")
gamma_lo = F(83, 24) - sqrt_hi / 6
gamma_hi = F(83, 24) - sqrt_lo / 6
require(195 - F(3489, 250) ** 2 == F(14379, 62500),
        "Exact squared margin")
require(sqrt_lo > F(3489, 250), "Radical gap")
require(old_inverse(F(29, 25)) == F(17, 15), "Left endpoint inverse")
require(F(17, 15) - gamma_hi > F(1, 1000), "Required uniform saving")
require(not (F(17, 15) - gamma_lo > F(1, 100)),
        "Negative control detects unsupported hundredth saving")

# The advertised floor-free contact admits a rational sqrt(r-1)
# parametrization, again avoiding numerical square roots.
contact_cases = 0
for i in range(101):
    v = F(3 * i, 700)
    r = 1 + v * v
    rho = (1 + v) ** 2 / 3
    t = 2 * (1 + v)  # sqrt(6*(2*rho))
    exponent = F(8, 3) + F(5, 12) * t * t - F(5, 3) * t
    require(r <= F(58, 49), "Contact interval")
    require((1 + exponent) / 2 == old_inverse(r), "Generic contact identity")
    contact_cases += 1

# A complete rational enclosure of the critical scalar root and length.
def imul(a, b):
    vals = [a[i] * b[j] for i in (0, 1) for j in (0, 1)]
    return min(vals), max(vals)


def iadd(a, b):
    return a[0] + b[0], a[1] + b[1]


def ipoly(coeffs, interval):
    value = (F(0), F(0))
    for coefficient in coeffs:
        value = iadd(imul(value, interval), (F(coefficient), F(coefficient)))
    return value


def quartic(k):
    return 16686*k**4 - 27405*k**3 + 9936*k**2 + 1290*k - 275


kl, kh = F(7497, 10000), F(3, 4)
require(quartic(kl) > 0 > quartic(kh), "Critical quartic sign bracket")
require(ipoly([66744, -82215, 19872, 1290], (kl, kh))[1] < 0,
        "Critical quartic unique in bracket")
dl, dh = F(469, 1000), F(47, 100)


def critical(d, k):
    return ((3 - 324*k*k)*d*d
            + (756*k*k - 54*k - 5)*d + 40*k - 300*k*k)


for d in [dl, dh]:
    A = -324*d*d + 756*d - 300
    B = -54*d + 40
    require(2*A*kl+B < 0 and 2*A*kh+B < 0,
            "Critical polynomial decreases with kappa")
require(critical(dl, kl) < 0, "Lower delta root bound")
require(critical(dh, kh) > 0, "Upper delta root bound")
k2 = (kl*kl, kh*kh)
aa = iadd((F(3), F(3)), imul((-324, -324), k2))
bb = iadd(iadd(imul((756, 756), k2),
                imul((-54, -54), (kl, kh))), (-5, -5))
delta_derivative = iadd(imul((2*dl, 2*dh), aa), bb)
require(delta_derivative[0] > 0, "Unique critical delta in the bracket")


def cutoff(d, k):
    c = F(2, 3) / k
    f = (4 - c) / (2 * (5 - c))
    return 1 + d*f / (2*(F(5, 6) - d + d*f))


# On this rectangle d<5/6. The derivatives of t in d and f are
# f*(5/6)/(2*den^2)>0 and d*(5/6-d)/(2*den^2)>0.
# f'(c)=-1/(2*(5-c)^2)<0, and c decreases in k.
rlo, rhi = cutoff(dl, kl), cutoff(dh, kh)
require(rlo == F(174882826, 150272989), "Exact critical lower length")
require(rhi == F(6994, 6007), "Exact critical upper length")
require(F(29, 25) < rlo < rhi < F(117, 100),
        "Critical length lies in the consumer interval")
require(old_inverse(rlo) - gamma_hi > F(1, 200),
        "Critical saving exceeds one two-hundredth")

print("EXACT smooth-HB coefficient cases:", hb_cases, "PASS")
print("EXACT zero-extended phase/coefficient cases:", masked_cases, "PASS")
print("EXACT normalized reflection cases:", normalizer_cases, "PASS")
print("EXACT envelope comparison cases:", envelope_cases, "PASS")
print("EXACT contact identities:", contact_cases, "PASS")
print("EXACT printed-floor audit: PASS")
print("EXACT radical margin:", F(14379, 62500), "PASS")
print("EXACT critical length bracket:", rlo, rhi, "PASS")
print("NEGATIVE CONTROLS: repeated primes, puncture factor, excessive margin PASS")


def decimal_bisect(fun, lo, hi, rounds=210):
    flo = fun(lo)
    require(flo * fun(hi) < 0, "Diagnostic sign bracket")
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
    ctx.prec = 65
    D = Decimal
    kap = decimal_bisect(quartic, D(".749773294079928"),
                        D(".749773294079929"))
    delt = decimal_bisect(lambda d: critical(d, kap), D(".469"), D(".47"))
    cc = D(2) / (3*kap)
    ff = (4-cc) / (2*(5-cc))
    cut = 1 + delt*ff / (2*(D(5)/6-delt+delt*ff))
    gamma = D(83)/24 - D(195).sqrt()/6
    old = (1+5*cut)/6
    cap = delt*ff
    count = 1-delt+(D(5)/6-delt)*cap/(2*(D(5)/6-delt+cap))
    rho_contact = (1+(cut-1).sqrt())**2/3
    require(abs(count + delt*cut - old) < D("1e-59"),
            "Diagnostic critical self-contact")
    print("DECIMAL DIAGNOSTICS (not the exact margin proof):")
    for name, value in [
        ("Gamma0", gamma), ("kappa_c", kap), ("delta_c", delt),
        ("r_c", cut), ("old inverse exponent", old),
        ("component saving", old-gamma),
        ("old critical count", count),
        ("low-supplied count", gamma-delt*cut),
        ("outer contact rho", rho_contact),
    ]:
        print(" ", name, "=", value)

print("No imported analytic theorem, full tail, new zero-free region, or RH certified.")
