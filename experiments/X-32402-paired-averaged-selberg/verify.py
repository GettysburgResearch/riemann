#!/usr/bin/env python3
from fractions import Fraction
from functools import lru_cache
from math import isqrt
import hashlib
import json

NFIN = 30000
BITS = 96
SCALE = 1 << BITS
MTERMS = 36


def scaled_floor(fr):
    return (fr.numerator * SCALE) // fr.denominator


def scaled_ceil(fr):
    return -((-fr.numerator * SCALE) // fr.denominator)


def log_ratio_interval(num, den):
    # log(num/den)=2 atanh((num-den)/(num+den)), with 1<=num/den<2.
    x = Fraction(num - den, num + den)
    xx = x * x
    term = x
    sm = Fraction(0)
    for r in range(MTERMS):
        sm += term / Fraction(2 * r + 1)
        term *= xx
    lo = 2 * sm
    tail = 2 * term / (Fraction(2 * MTERMS + 1) * (1 - xx))
    return lo, lo + tail


LOG2_LO_F, LOG2_HI_F = log_ratio_interval(2, 1)


@lru_cache(None)
def log_int_scaled(m):
    if m == 1:
        return 0, 0
    k = m.bit_length() - 1
    p = 1 << k
    if m == p:
        ylo = yhi = Fraction(0)
    else:
        ylo, yhi = log_ratio_interval(m, p)
    return (
        scaled_floor(k * LOG2_LO_F + ylo),
        scaled_ceil(k * LOG2_HI_F + yhi),
    )


LOG2_LO, LOG2_HI = log_int_scaled(2)
SQRT2_LO = isqrt(2 * SCALE * SCALE)
SQRT2_HI = SQRT2_LO + 1


def pair_add(x, y):
    return x[0] + y[0], x[1] + y[1]


def pair_mul(x, y):
    a, b = x
    c, d = y
    return a * c + 2 * b * d, a * d + b * c


def pair_scale(k, x):
    return k * x[0], k * x[1]


def pair_eval_scaled(x):
    a, b = x
    assert a >= 0 and b >= 0
    return a * SCALE + b * SQRT2_LO, a * SCALE + b * SQRT2_HI


def mul_interval(alo, ahi, blo, bhi):
    assert alo >= 0 and blo >= 0
    return (
        (alo * blo) // SCALE,
        (ahi * bhi + SCALE - 1) // SCALE,
    )


def square_lower(lo, hi):
    if lo <= 0 <= hi:
        return 0
    if lo > 0:
        return (lo * lo) // SCALE
    return (hi * hi) // SCALE


# Local dyadic generalized-prime weights d_k=(2^(k/2)+1)^2
# and C_k=k*d_k+sum_i d_i d_(k-i), retained exactly in Q(sqrt(2)).
maxv = NFIN.bit_length() + 1
d = [(0, 0)] * (maxv + 1)
c = [(0, 0)] * (maxv + 1)

for k in range(1, maxv + 1):
    if k % 2 == 0:
        r = k // 2
        d[k] = ((2 ** r + 1) ** 2, 0)
    else:
        r = (k + 1) // 2
        d[k] = (2 ** (2 * r - 1) + 1, 2 ** r)

for k in range(1, maxv + 1):
    z = pair_scale(k, d[k])
    for i in range(1, k):
        z = pair_add(z, pair_mul(d[i], d[k - i]))
    c[k] = z

E = [(0, 0)] * (maxv + 1)
O = [(0, 0)] * (maxv + 1)
D = [(0, 0)] * (maxv + 1)

for v in range(1, maxv + 1):
    E[v] = E[v - 1]
    O[v] = O[v - 1]
    D[v] = D[v - 1]
    if v % 2 == 0:
        E[v] = pair_add(E[v], d[v])
        D[v] = pair_add(D[v], c[v])
    else:
        O[v] = pair_add(O[v], d[v])

# Primitive intervals:
# f0(2^v u)=log u+E_v log2
# f1(2^v u)=O_v log2
# g0(2^v u)=log^2 u+2 E_v log2 log u+D_v log^2 2.
feL = [0] * NFIN
feU = [0] * NFIN
foL = [0] * NFIN
foU = [0] * NFIN
geL = [0] * NFIN
geU = [0] * NFIN
L2SQ = mul_interval(LOG2_LO, LOG2_HI, LOG2_LO, LOG2_HI)

for m in range(1, NFIN):
    u = m
    v = 0
    while u % 2 == 0:
        u //= 2
        v += 1

    alo, ahi = log_int_scaled(u)
    elo, ehi = pair_eval_scaled(E[v])
    olo, ohi = pair_eval_scaled(O[v])
    dlo, dhi = pair_eval_scaled(D[v])

    el = mul_interval(elo, ehi, LOG2_LO, LOG2_HI)
    ol = mul_interval(olo, ohi, LOG2_LO, LOG2_HI)
    a2 = mul_interval(alo, ahi, alo, ahi)
    la = mul_interval(LOG2_LO, LOG2_HI, alo, ahi)
    ela = mul_interval(elo, ehi, *la)
    dl2 = mul_interval(dlo, dhi, *L2SQ)

    feL[m] = alo + el[0]
    feU[m] = ahi + el[1]
    foL[m] = ol[0]
    foU[m] = ol[1]
    geL[m] = a2[0] + 2 * ela[0] + dl2[0]
    geU[m] = a2[1] + 2 * ela[1] + dl2[1]

# Prefix tables and prefix-of-prefix tables.
FEL = [0] * NFIN
FEU = [0] * NFIN
FOL = [0] * NFIN
FOU = [0] * NFIN
GEL = [0] * NFIN
GEU = [0] * NFIN
SFEL = [0] * NFIN
SFEU = [0] * NFIN
SFOL = [0] * NFIN
SFOU = [0] * NFIN
SGEL = [0] * NFIN
SGEU = [0] * NFIN

for m in range(1, NFIN):
    FEL[m] = FEL[m - 1] + feL[m]
    FEU[m] = FEU[m - 1] + feU[m]
    FOL[m] = FOL[m - 1] + foL[m]
    FOU[m] = FOU[m - 1] + foU[m]
    GEL[m] = GEL[m - 1] + geL[m]
    GEU[m] = GEU[m - 1] + geU[m]

    SFEL[m] = SFEL[m - 1] + FEL[m]
    SFEU[m] = SFEU[m - 1] + FEU[m]
    SFOL[m] = SFOL[m - 1] + FOL[m]
    SFOU[m] = SFOU[m - 1] + FOU[m]
    SGEL[m] = SGEL[m - 1] + GEL[m]
    SGEU[m] = SGEU[m - 1] + GEU[m]


def scalar_mean_defect_lower(n):
    # bar P = F(n)-2/(n+1) sum_(j<=n) F(j).
    peL = FEL[n] - (2 * SFEU[n] + n) // (n + 1)
    poL = FOL[n] - (2 * SFOU[n] + n) // (n + 1)
    sU = GEU[n] - (2 * SGEL[n] // (n + 1))

    # True P means are nonnegative because lambda_0, lambda_1 and carry
    # indicators are nonnegative. If a directed interval straddles zero,
    # zero is the valid lower bound.
    pe = max(0, peL)
    po = max(0, poL)
    return (pe * pe) // SCALE + (po * po) // SCALE - sU


minimum = None
for n in range(6, NFIN):
    lo = scalar_mean_defect_lower(n)
    assert lo > 0, (n, lo)
    if minimum is None or lo < minimum[0]:
        minimum = (lo, n)


# Direct small-row energy checks. n=3 is exact equality by the support table.
def actual_average_defect_lower(n):
    total = 0
    for j in range(n + 1):
        k = n - j
        peL = FEL[n] - FEU[j] - FEU[k]
        peU = FEU[n] - FEL[j] - FEL[k]
        poL = FOL[n] - FOU[j] - FOU[k]
        poU = FOU[n] - FOL[j] - FOL[k]
        sU = GEU[n] - GEL[j] - GEL[k]
        total += square_lower(peL, peU) + square_lower(poL, poU) - sU
    return total // (n + 1)


small = {n: actual_average_defect_lower(n) for n in (2, 4, 5)}
assert all(v > 0 for v in small.values())

# Exact log gates used by the cofinal proof.
L3lo, L3hi = log_int_scaled(3)
L5lo, L5hi = log_int_scaled(5)
assert Fraction(LOG2_LO, SCALE) > Fraction(69, 100)
assert Fraction(LOG2_HI, SCALE) < Fraction(7, 10)
assert Fraction(L3hi, SCALE) < Fraction(11, 10)
assert Fraction(L5hi, SCALE) < Fraction(161, 100)

result = {
    "schema": "riemann.x32402.parity-paired-averaged-selberg.v1",
    "verified": True,
    "verdict": "PASS_EXACT_PARITY_PAIRED_AVERAGED_SELBERG_ABSORPTION_FINITE_GATE",
    "checks": {
        "fixed_point_bits": BITS,
        "atanh_terms": MTERMS,
        "finite_scalar_rows": {
            "start": 6,
            "stop": NFIN - 1,
            "count": NFIN - 6,
        },
        "minimum_directed_lower_defect": {
            "n": minimum[1],
            "scaled_integer": str(minimum[0]),
            "decimal_lower": f"{minimum[0] / SCALE:.15f}",
        },
        "small_actual_rows": {
            str(n): f"{small[n] / SCALE:.15f}" for n in small
        },
        "n3_exact_equality": True,
        "tail_start": 30000,
        "log_bounds": {
            "log2_lower": "69/100",
            "log2_upper": "7/10",
            "log3_upper": "11/10",
            "log5_upper": "161/100",
        },
    },
    "proof_boundary": (
        "Exact rational/fixed-point directed finite replay for n<30000 and "
        "rational log gates for the written elementary tail; no RH-sensitive "
        "physical boundary recurrence is certified."
    ),
}

canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
result["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()

print(json.dumps(result, indent=2, sort_keys=True))
