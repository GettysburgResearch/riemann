"""Exact certificates for ALL_ORDER_BARRIER.md; finite scope is in the report."""
from fractions import Fraction as F
from pathlib import Path
from math import gcd, isqrt
import argparse
import hashlib
import json


class CheckFailure(ValueError):
    pass


class Checks:
    def __init__(self):
        self.count = 0

    def require(self, truth, label):
        self.count += 1
        if not truth:
            raise CheckFailure(label)


def plus(*forms):
    return tuple(sum(v, F(0)) for v in zip(*forms))


def scale(a, v):
    return tuple(a*x for x in v)


def kap(r, s):
    return max(F(1), r*(1-s), F(5, 6)+r*(F(2, 3)-s),
               F(1, 3)+r*(F(11, 12)-s))


def tcrit(s):
    if s <= F(7, 12):
        return 2-3*s
    if s <= F(3, 4):
        return F(11, 16)-F(3, 4)*s
    return (1-s)/2


# Exact Z[zeta_12] arithmetic, reduced by X^4-X^2+1.
ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
ROOT = (0, 1, 0, 0)


def zadd(a, b):
    return tuple(x+y for x, y in zip(a, b))


def zscale(k, a):
    return tuple(k*x for x in a)


def zmul(a, b):
    out = [0]*7
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    for j in range(6, 3, -1):
        out[j-2] += out[j]
        out[j-4] -= out[j]
        out[j] = 0
    return tuple(out[:4])


def zpow(a, n):
    out = ONE
    while n:
        if n & 1:
            out = zmul(out, a)
        a = zmul(a, a)
        n >>= 1
    return out


def fixed_character(n, prime, generator, multiplier):
    if n % prime == 0:
        return ZERO
    for j in range(prime-1):
        if pow(generator, j, prime) == n % prime:
            return zpow(ROOT, (multiplier*j) % 12)
    raise CheckFailure('Bad primitive generator in finite character fixture')


def chi(n):
    return fixed_character(n, 7, 3, 2)


def psi(n):
    return fixed_character(n, 5, 2, 3)


def character(n):
    return zmul(chi(n), psi(n))


def factor(n):
    out = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0)+1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0)+1
    return out


def remove_sixth(n):
    c = d = 1
    for p, j in factor(n).items():
        c *= p**(j % 6)
        d *= p**(j // 6)
    return c, d


def mobius(n):
    fs = factor(n)
    if any(j >= 2 for j in fs.values()):
        return 0
    return (-1)**len(fs)


def divisors(n):
    out = []
    for d in range(1, isqrt(n)+1):
        if n % d == 0:
            out.append(d)
            if d*d != n:
                out.append(n//d)
    return sorted(out)


def cA(n, A):
    return sum(mobius(d) for d in divisors(n) if d <= A)


def run(mutation):
    ck = Checks()
    # Forms below use the order (e,t,y,constant), and mean form >= 0.
    left = [
        (F(1), F(-1), F(1), F(-1, 2)),
        (F(1), F(-5, 6), F(1, 2), F(-1, 3)),
        (F(1), F(-1, 3), F(1, 2), F(-11, 24)),
    ]
    w = (24, 34, 8)
    if mutation == 'wrong_plane_weight':
        w = (24, 33, 8)
    cert1 = plus(*(scale(F(k), v) for k, v in zip(w, left)))
    ck.require(cert1 == (66, -55, 45, -27), 'positive supporting-plane certificate')
    cert2 = plus(*(scale(F(k), v) for k, v in zip((9, 14, 4), left)))
    ck.require(cert2 == (27, -22, 18, -11), 'positive 9/10 escape certificate')
    ck.require(all(k >= 0 for k in (*w, 9, 14, 4)), 'certificate weights nonnegative')
    # The right-half residuals use y>=1/2,t>=0, without a finite grid.
    rem1 = plus((66, -55, 45, -27), scale(F(-66), left[1]))
    ck.require(rem1 == (0, 0, 12, -5), 'right-strip first residual')
    ck.require(F(12, 2)-5 == 1, 'right-strip first minimum')
    rem2 = plus((27, -22, 18, -11), scale(F(-27), left[1]))
    ck.require(rem2 == (0, F(1, 2), F(9, 2), -2), 'right-strip second residual')
    ck.require(F(9, 4)-2 == F(1, 4), 'right-strip second minimum')

    # The r>=4 simplification is an affine half-line certificate.
    ck.require(F(5, 6)-F(4, 3) == F(-1, 2), 'third term below main at r=4')
    ck.require(F(-1, 3) < 0, 'third difference decreases with r')
    ck.require(F(1, 3)-F(4, 12) == 0, 'fourth term ties main at r=4')
    ck.require(F(-1, 12) < 0, 'fourth difference decreases with r')

    points = [(1, F(1, 2)), (2, F(7, 12)), (3, F(25, 36)), (4, F(3, 4))]
    for r, s in points:
        ck.require(kap(r, s) == 1, f'mean-U moment point r={r}')
        ck.require(tcrit(s) == F(1, 2*r), f'interpolation vertex/segment r={r}')
    # Exact general r formula for sigma=1-1/r at r>=4 follows algebraically.
    ck.require(plus((F(1), F(-1, 2)), (F(-1), F(1, 2))) == (0, 0),
               'higher mean-U segment identity sigma=1-2t')
    central_expected = {1: F(1), 2: F(7, 6), 3: F(19, 12), 4: F(2)}
    for r, expected in central_expected.items():
        ck.require(kap(r, F(1, 2)) == expected, f'prior central exponent r={r}')
    # Main and ACTUAL-Q dual endpoint exponents, symbolic in sigma.
    for r in range(1, 5):
        # Coefficients (constant,sigma) in Q0 exponents.
        dual_prefactor = (F(r), F(-2*r))
        v_weight = (F(-r, 2), F(r))
        ck.require(plus(dual_prefactor, v_weight) == (F(r, 2), F(-r)),
                   f'actual dual endpoint prefactor r={r}')
    fe = F(1, 2)-F(5, 12)
    if mutation == 'wrong_fe_sign':
        fe = -fe
    ck.require(kap(2, F(7, 12))+4*fe == F(4, 3), 'fourth reflected conductor exponent')
    ck.require(kap(4, F(3, 4))+8*(F(1, 2)-F(1, 4)) == 3,
               'eighth reflected conductor exponent')

    sigma = F(2, 3)
    cross = (F(5, 6), F(4, 3)-2*sigma)
    if mutation == 'drop_type_ii_cross':
        cross = (F(0), F(0))
    ck.require(cross == (F(5, 6), F(0)), 'retained native Type-II constant')
    # All four native Type-II norm exponents at sigma=2/3.
    norm_terms = [(0, 2-2*sigma), (1, 1-2*sigma),
                  (F(1, 3), F(11, 6)-2*sigma),
                  (F(5, 6), F(4, 3)-2*sigma)]
    ck.require(norm_terms == [(0, F(2, 3)), (1, F(-1, 3)),
                             (F(1, 3), F(1, 2)), (F(5, 6), 0)],
               'complete Type-II exponent table')

    nu = F(5, 6)
    a0 = F(15, 37)
    y = F(5, 12)
    t = F(1, 4)
    e = F(1, 3)
    if mutation == 'dense_subset_lindelof':
        e = t
    m = nu*(1-t)+e
    ck.require(m == F(23, 24), 'actual dense selected fourth-mean exponent')
    ck.require(66*m+45*y == 82, 'selected supporting-plane equality')
    ck.require(a0*y+(1-a0)*m == F(82, 111), 'balanced weighted equality')
    theta = a0/2
    if mutation == 'omit_diagonal_term':
        theta = (3*a0-1)/2
    ck.require(theta == F(15, 74), 'complete two-term physical norm')
    b = F(5, 6)-a0/3
    if mutation == 'old_mellin_shift':
        b = F(37, 54)
    ck.require(b+theta == F(100, 111), 'actual scale-dependent principal shift')
    ck.require(F(2, 3)-1-a0+a0*y+(1-a0)*m == 0, 'single-class exact floor')
    # Asymmetric derivative coefficients in (constant,m,y).
    derivative = plus((F(1, 2), F(-1), 0), (F(-1), 0, F(2, 3)))
    ck.require(derivative == (F(-1, 2), -1, F(2, 3)), 'fixed-boundary asymmetric derivative')
    ck.require(-F(1, 2)-nu+F(2, 3) == -F(2, 3), 'asymmetric derivative uniform negativity')
    ck.require(F(11, 12) > F(100, 111), 'long-support bound cannot evade floor')
    ck.require(F(5, 6)-F(22, 27) == F(1, 54), 'necessary density saving')
    ck.require(F(23, 24)-F(17, 18) == F(1, 72), 'necessary selected numerator saving')
    nu2 = F(22, 27)
    m2 = nu2*(1-t)+e
    ck.require(m2 == F(17, 18), '9/10 density threshold selected exponent')
    ck.require(9*m2+6*y == 11, '9/10 supporting-plane equality')

    # Exact character fixtures. These are not the full CT ideal family.
    ck.require(zpow(ROOT, 12) == ONE and zpow(ROOT, 6) == zscale(-1, ONE),
               'cyclotomic ring convention')
    phase_cases = 0
    for base in (2, 3, 7):
        for power in range(20):
            n = base**power
            c, d = remove_sixth(n)
            ck.require(c*d**6 == n, 'literal sixth-power decomposition')
            rhs = zmul(psi(c), zmul(zpow(psi(d), 6), chi(c)))
            mask = gcd(7, d) == 1
            if mutation == 'erase_power_mask':
                mask = True
            if mutation == 'add_coprimality' and gcd(c, d) != 1:
                mask = False
            if mutation == 'erase_fixed_twist':
                rhs = zmul(psi(c), chi(c))
            rhs = rhs if mask else ZERO
            ck.require(character(n) == rhs, f'full phase/mask identity base={base}, power={power}')
            phase_cases += 1
    ck.require(gcd(*remove_sixth(2**7)) > 1, 'required shared-prime column exists')
    ck.require(zpow(psi(2), 6) != ONE, 'fixed twist sixth power is not silently one')
    ck.require(character(7**6) == ZERO, 'native nonunit zero retained at a pure sixth power')

    # Exact integer-ideal fixture for the source convolution before analytic weights.
    convolution_cases = 0
    prefix_cases = 0
    for A in (3, 7, 12):
        coeffs = {}
        expanded = {}
        for n in range(1, 121):
            if n % 5 == 0:
                continue  # fixed S omission for psi
            coeffs[n] = zscale(cA(n, A), character(n))
            expanded[n] = ZERO
            for d in divisors(n):
                if d <= A:
                    expanded[n] = zadd(expanded[n], zscale(mobius(d), zmul(character(d), character(n//d))))
            ck.require(coeffs[n] == expanded[n], f'actual Mobius convolution A={A}, n={n}')
            ck.require(n == 1 or n > A or cA(n, A) == 0, 'annihilated original initial coefficients')
            convolution_cases += 1
        for V in (A, 2*A, 4*A):
            for H in range(V, min(2*V, 120)+1):
                native = {n: c for n, c in coeffs.items() if V < n <= H and n > A}
                product = {n: c for n, c in expanded.items() if V < n <= H and n > A}
                ck.require(native == product, 'literal Type-II prefix cap')
                prefix_cases += 1

    here = Path(__file__).resolve()
    proof = here.with_name('ALL_ORDER_BARRIER.md')
    return {
        'status': 'PASS', 'explicit_checks': ck.count,
        'scope': 'Exact affine certificates and stated finite coefficient fixtures; no L-value or theta computation',
        'all_order_argument': 'Written AFE proof plus nonnegative affine certificates, not a finite order census',
        'first_certificate_weights': [24, 34, 8],
        'second_certificate_weights': [9, 14, 4],
        'method_floor': '100/111', 'arithmetic_lower_bound_claimed': False,
        'necessary_density_saving': '1/54', 'necessary_numerator_saving': '1/72',
        'phase_cases': phase_cases, 'convolution_cases': convolution_cases,
        'prefix_cases': prefix_cases,
        'proof_sha256': hashlib.sha256(proof.read_bytes()).hexdigest(),
        'checker_sha256': hashlib.sha256(here.read_bytes()).hexdigest(),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mutation', choices=['wrong_plane_weight', 'wrong_fe_sign',
                        'drop_type_ii_cross', 'dense_subset_lindelof', 'omit_diagonal_term',
                        'old_mellin_shift', 'erase_power_mask', 'add_coprimality',
                        'erase_fixed_twist'])
    args = parser.parse_args()
    print(json.dumps(run(args.mutation), indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
