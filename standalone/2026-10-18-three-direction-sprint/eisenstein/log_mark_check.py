"""Exact finite checks for the new cumulative logarithmic-mark deduction.

Prime logarithms are represented by independent formal coordinates.  The
Gauss/CRT check uses genuine Eisenstein primary primes and exact cyclotomic
polynomials.  None of these finite checks proves the imported mean estimate.
"""
from fractions import Fraction as F
from pathlib import Path
from math import gcd, isqrt
import hashlib
import json
import sys

private = Path(__file__).with_name('_packages')
if private.is_dir():
    sys.path.insert(0, str(private))
from flint import fmpz_poly


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def mul(a, b):
    x, y = a
    u, v = b
    return x*u-y*v, x*v+y*u-y*v


def scale(a, t):
    return a[0]*t, a[1]*t


def inverse(a):
    x, y = a
    n = x*x-x*y+y*y
    require(n != 0, 'Zero denominator.')
    return (x-y)/n, -y/n


def div(a, b):
    return mul(a, inverse(b))


ONE = F(1), F(0)
ZETA = F(0), F(1)
UNITS = [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1)]


def prime_factors(n):
    out = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def formal_log_checks():
    count = 0
    mutation = False
    for c in range(1, 193):
        fs = prime_factors(c)
        if any(e != 1 for e in fs.values()):
            continue
        for k in range(1, 257):
            fk = prime_factors(k)
            common = fs.keys() & fk.keys()
            left = {p: 1 for p in fs.keys() | fk.keys()}
            right = dict(fs)
            for p in fk:
                right[p] = right.get(p, 0) + 1
            for p in common:
                right[p] -= 1
            require(left == right, 'Formal radical-log decomposition failed.')
            if common:
                mutation = True
                require(any(fs.get(p, 0)+int(p in fk) != left[p]
                            for p in common), 'Missing shared-prime term undetected.')
            for p in common:
                require(c % p == 0 and k % p == 0, 'Extraction support failed.')
                cp, h = c//p, k//p
                require(cp % p != 0, 'Squarefree c extraction left a p factor.')
                require(c*k**3 == cp*p**4*h**3, 'Exact p^4 scale failed.')
                count += 1
    require(mutation, 'No shared-prime mutation control was tested.')
    return count


def data(a):
    x, y = a
    p = x*x-x*y+y*y
    t = -x*pow(y, -1, p) % p
    z = (1+t) % p
    require(pow(z, 6, p) == 1 and pow(z, 3, p) != 1,
            'Wrong embedded sixth root.')
    images = {pow(z, j, p): UNITS[j] for j in range(6)}

    def chi(n):
        n %= p
        return (0, 0) if n == 0 else images[pow(n, (p-1)//6, p)]
    return p, t, chi


def arrays_product(a, b):
    m = len(a)
    out = [(0, 0)]*m
    for i, x in enumerate(a):
        if x == (0, 0):
            continue
        for j, y in enumerate(b):
            if y != (0, 0):
                at = (i+j) % m
                out[at] = add(out[at], mul(x, y))
    return out


def gauss_crt_checks():
    primaries = [(-2, -3), (1, -3), (-2, 3)]
    count = 0
    for i, a in enumerate(primaries):
        for b in primaries[i+1:]:
            p, tp, cp = data(a)
            q, tq, cq = data(b)
            m = p*q
            ab = mul(a, b)
            ga = [(0, 0)]*m
            gb = [(0, 0)]*m
            gab = [(0, 0)]*m
            for x in range(p):
                at = -a[1]*x*q % m
                ga[at] = add(ga[at], mul(cp(x), cp(x)))
            for x in range(q):
                at = -b[1]*x*p % m
                gb[at] = add(gb[at], mul(cq(x), cq(x)))
            for x in range(m):
                at = -ab[1]*x % m
                ch = mul(cp(x), cq(x))
                gab[at] = add(gab[at], mul(ch, ch))
            phase_p = mul(cp(b[0]+b[1]*tp), cp(b[0]+b[1]*tp))
            phase_q = mul(cq(a[0]+a[1]*tq), cq(a[0]+a[1]*tq))
            phase = mul(phase_p, phase_q)
            fourth = mul(phase_q, phase_q)
            require(phase == fourth, 'Fourth-power CRT phase failed.')
            rhs = [mul(phase, x) for x in arrays_product(ga, gb)]
            xp = fmpz_poly([0]*p + [1])-1
            xq = fmpz_poly([0]*q + [1])-1
            xm = fmpz_poly([0]*m + [1])-1
            cyclo, remainder = divmod(xm*fmpz_poly([-1, 1]), xp*xq)
            require(not remainder, 'Cyclotomic polynomial division failed.')
            for coord in range(2):
                diff = fmpz_poly([x[coord]-y[coord]
                                  for x, y in zip(gab, rhs, strict=True)])
                require(not divmod(diff, cyclo)[1], 'Actual Gauss CRT identity failed.')
            for row in range(0, 2*m+1):
                # The complete row identity chi_p^4 chi_h^3 chi_c' is tested
                # independently, including collisions at p and q.
                chp = cp(row)
                chq = cq(row)
                left = mul(mul(chp, chp), mul(chp, chp))
                right = mul(chp, mul(chp, mul(chp, chp)))
                require(left == right, 'Shared-prime row phase failed.')
                if row % p == 0:
                    require(left == (0, 0), 'Nonunit zero was lost.')
                if row % q == 0:
                    require(chq == (0, 0), 'Label puncture zero was lost.')
            count += 1
    return count


def local_principal_checks():
    count = 0
    for q in [7, 13, 19, 31]:
        for d in [F(1, 11), F(1, 5), F(2, 7)]:
            for r0 in [F(1, 37), F(1, 8), F(-1, 9)]:
                for phase in [ONE, ZETA, mul(ZETA, ZETA)]:
                    r = scale(phase, r0)
                    dr = d, F(0)
                    a = add(ONE, add(scale(dr, -(1-F(1, q))), scale(r, -F(1, q))))
                    ps = div(scale(add(r, scale(dr, -1)), 1+F(1, q)),
                             add(ONE, scale(r, -1)))
                    pp = div(scale(a, 1+F(1, q)),
                             scale(add(ONE, scale(r, -1)), 1-F(1, q)))
                    b = add(scale(div(ps, pp), 1/d), (-F(1, q), F(0)))
                    br = div(scale(add(scale(r, 1/d),
                                       add(scale(dr, -(1-F(1, q))),
                                           scale(r, -F(1, q)))), 1-F(1, q)), a)
                    require(add(b, ONE) == br, 'Exact principal B+1 formula failed.')
                    count += 1
    return count


def exponent_checks():
    count = 0
    # Exact rational grid: no feasible point below sqrt(5/6).
    for bn in range(84, 97):
        b = F(bn, 100)
        for xi in range(1, 100):
            x = F(xi, 100)
            for yi in range(1, 100):
                y = F(yi, 100)
                low = b >= F(5, 6)+max(x, y)/2-x/3
                high = b*y >= F(5, 6)*(1-x)
                if low and high:
                    require(b*b >= F(5, 6), 'Consumer floor violated.')
                count += 1
    return count


def main():
    out = {
        'status': 'PASS',
        'formal_shared_prime_extractions': formal_log_checks(),
        'actual_Eisenstein_composite_Gauss_CRT_cases': gauss_crt_checks(),
        'exact_local_principal_identities': local_principal_checks(),
        'exact_rational_consumer_grid_cases': exponent_checks(),
        'scope': 'Finite algebra/masks/phase/consumer checks; no analytic mean theorem verified.',
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'external_source_sha256': '414d196862672b5aefbfa671b4b2e60f60ad9dde12dc3042d038a1bfb1d08d39',
    }
    target = Path(__file__).with_name('LOG_MARK_CHECKS.json')
    target.write_text(json.dumps(out, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
