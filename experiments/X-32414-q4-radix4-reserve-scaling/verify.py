from fractions import Fraction
import hashlib
import json

M = 80
NMAX = 40


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def mul(a, b):
    vals = [a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1]]
    return min(vals), max(vals)


def scale(c, a):
    if c >= 0:
        return c * a[0], c * a[1]
    return c * a[1], c * a[0]


def log2_interval():
    # log 2 = 2 atanh(1/3), with a positive geometric tail.
    x = Fraction(1, 3)
    s = Fraction(0)
    xp = x
    for r in range(M):
        s += Fraction(2, 2 * r + 1) * xp
        xp *= x * x
    rem = Fraction(2, 2 * M + 1) * xp / (1 - x * x)
    return s, s + rem


LOG2 = log2_interval()


def log_ratio_interval(num, den):
    # 1 <= num/den < 2.
    x = Fraction(num - den, num + den)
    s = Fraction(0)
    xp = x
    for r in range(M):
        s += Fraction(2, 2 * r + 1) * xp
        xp *= x * x
    rem = Fraction(2, 2 * M + 1) * xp / (1 - x * x)
    return s, s + rem


def log_int(n):
    if n == 1:
        return Fraction(0), Fraction(0)
    k = n.bit_length() - 1
    den = 1 << k
    return add(scale(k, LOG2), log_ratio_interval(n, den))


def factorint(n):
    out = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def prime_power_base(n):
    f = factorint(n)
    if len(f) == 1:
        return next(iter(f))
    return None


def power4_exponent(n):
    if n < 4:
        return None
    r = 0
    while n % 4 == 0:
        n //= 4
        r += 1
    return r if n == 1 else None


LOG = [(Fraction(0), Fraction(0))] * (NMAX + 1)
for n in range(1, NMAX + 1):
    LOG[n] = log_int(n)

LAMBDA4 = [(Fraction(0), Fraction(0)) for _ in range(NMAX + 1)]
for n in range(2, NMAX + 1):
    p = prime_power_base(n)
    val = (Fraction(0), Fraction(0)) if p is None else LOG[p]
    r = power4_exponent(n)
    if r is not None:
        # (4^r-1) log 4 = 2(4^r-1) log 2.
        val = add(val, scale(2 * (4**r - 1), LOG2))
    LAMBDA4[n] = val

C4 = [(Fraction(0), Fraction(0)) for _ in range(NMAX + 1)]
for n in range(2, NMAX + 1):
    C4[n] = mul(LAMBDA4[n], LOG[n])
for a in range(2, NMAX + 1):
    if LAMBDA4[a][1] == 0:
        continue
    for b in range(2, NMAX // a + 1):
        if LAMBDA4[b][1] == 0:
            continue
        C4[a * b] = add(C4[a * b], mul(LAMBDA4[a], LAMBDA4[b]))


def carry(n, j, q):
    return n // q - j // q - (n - j) // q


def s4_interval(n, j):
    ans = Fraction(0), Fraction(0)
    for q in range(2, n + 1):
        if carry(n, j, q):
            ans = add(ans, C4[q])
    return ans


ROWS = []
for k in range(1, 6):
    for j in range(1, k + 1):
        n = j + k
        if n >= 4 and 4 * j >= n:
            ROWS.append((n, j))
ROWS = sorted(set(ROWS))

rows = []
for n, j in ROWS:
    lo, hi = s4_interval(n, j)
    slo, shi = s4_interval(4 * n, 4 * j)
    margin_lo = 16 * lo - shi
    assert margin_lo > 0, (n, j, margin_lo)
    # This integer is only a compact orientation field.  The proof uses
    # margin_lo itself above, which is an exact Fraction.
    milli = (1000 * margin_lo.numerator) // margin_lo.denominator
    rows.append({"n": n, "j": j, "margin_floor_milli": int(milli)})

core = {
    "classification": "PASS_EXACT_Q4_RADIX4_SECOND_MOMENT_SMALL_ROWS",
    "atanh_terms": M,
    "rows": rows,
}
digest = hashlib.sha256(
    json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
).hexdigest()
result = dict(core)
result["sha256"] = digest
print(json.dumps(result, indent=2, sort_keys=True))
