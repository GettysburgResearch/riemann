#!/usr/bin/env python3
"""CAP36 exact finite replay; standard library only, no float acceptance."""
from __future__ import annotations
import argparse
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys

COUNT: Counter[str] = Counter()
TERMS: Counter[str] = Counter()


def require(ok: bool, label: str) -> None:
    if not ok:
        raise ValueError(label)
    COUNT[label] += 1


def eq(a, b, label: str) -> None:
    require(a == b, label)


@dataclass(frozen=True)
class G:
    re: F = F(0)
    im: F = F(0)

    @staticmethod
    def cast(x):
        return x if isinstance(x, G) else G(F(x))

    def __add__(self, x):
        x = G.cast(x)
        return G(self.re + x.re, self.im + x.im)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.re, -self.im)

    def __sub__(self, x):
        return self + (-G.cast(x))

    def __rsub__(self, x):
        return G.cast(x) + (-self)

    def __mul__(self, x):
        x = G.cast(x)
        return G(self.re*x.re - self.im*x.im,
                 self.re*x.im + self.im*x.re)

    __rmul__ = __mul__

    def __truediv__(self, x):
        x = F(x)
        return G(self.re/x, self.im/x)

    def __pow__(self, n: int):
        if n < 0:
            raise ValueError('negative Gaussian power')
        out = G(F(1))
        for _ in range(n):
            out = out*self
        return out

    def conj(self):
        return G(self.re, -self.im)

    def norm2(self):
        return self.re*self.re + self.im*self.im

    def __bool__(self):
        return bool(self.re or self.im)


ZERO = G()
ONE = G(F(1))
UNITS = (ONE, G(F(0), F(1)), -ONE, G(F(0), F(-1)))


def sieve(n: int):
    mu = [1]*(n+1)
    mu[0] = 0
    factors = [{} for _ in range(n+1)]
    for p in range(2, n+1):
        if factors[p]:
            continue
        for k in range(p, n+1, p):
            q, power = k, 0
            while q % p == 0:
                q //= p
                power += 1
            factors[k][p] = power
            mu[k] = 0 if power > 1 else -mu[k]
    return mu, factors


def inverse_one(n: int):
    """Triangular inverse, independently of prime factorization."""
    accum = [0]*(n+1)
    ans = [0]*(n+1)
    for k in range(1, n+1):
        ans[k] = 1 if k == 1 else -accum[k]
        for j in range(2*k, n+1, k):
            accum[j] += ans[k]
    return ans


def conv(a, b, n: int):
    out = [ZERO]*(n+1)
    for d in range(1, min(n, len(a)-1)+1):
        if not a[d]:
            continue
        for j in range(1, min(n//d, len(b)-1)+1):
            if b[j]:
                out[d*j] = out[d*j] + a[d]*b[j]
    return out


def twist(c, chi):
    return [ZERO] + [G.cast(c[n])*chi[n] for n in range(1, len(c))]


def balance(c):
    c = [G.cast(x) for x in c]
    residual = sum((c[n]/n for n in range(1, len(c))), ZERO)
    c[1] = c[1] - residual
    return c


def reciprocal_energy(c):
    s, value = ZERO, F(0)
    for n in range(1, len(c)):
        s = s + G.cast(c[n])/n
        if n < len(c)-1:
            value += s.norm2()
    return value, s


def cap(mu, y: int):
    c = [F(0)] + [F(mu[n]) for n in range(1, y+1)]
    m = sum((F(mu[n], n) for n in range(1, y+1)), F(0))
    residual = abs(m)
    sign = 1 if m >= 0 else -1
    while residual:
        n = len(c)
        take = min(F(3), n*residual)
        c.append(-sign*take)
        residual -= take/n
        if len(c)-1 > 2*y:
            raise ValueError('cap exceeded proven support')
    return c, m


def char_data(n: int, factors, mode: str):
    chi = [ZERO]*(n+1)
    chi[1] = ONE
    for k in range(2, n+1):
        if mode == 'damp':
            chi[k] = G(F(1, k))
        else:
            z = ONE
            for p, power in factors[k].items():
                z = z * (UNITS[p % 4]**power)
            chi[k] = z
    return chi


def divisor_kernel(mu, chi, n: int):
    return conv([ZERO]+[ONE]*n, [ZERO]+[mu[k]*chi[k] for k in range(1, n+1)], n)


def phi_control(n: int, x: int, h: int = 1):
    """Structural rational bump; NOT the centered harmonic kernel."""
    return sum(((1-F(j*x, 2*h*n))**4
                for j in range(1, (2*h*n-1)//x+1)), F(0))/n


def pair(c, d, phi):
    total = ZERO
    for r in range(1, len(c)):
        for s in range(1, len(d)):
            TERMS['bilinear_source_pairs'] += 1
            total = total + c[r]*d[s]*phi[r*s]
    return total


def four_factor_pair(c, a, phi):
    l = len(c)-1
    total = ZERO
    for r in range(1, l+1):
        for s in range(1, l+1):
            kernel = ZERO
            for d in range(1, l//r+1):
                for e in range(1, l//s+1):
                    TERMS['compressed_kernel_terms'] += 1
                    kernel = kernel + a[d]*a[e]*phi[r*s*d*e]
            total = total + c[r]*c[s]*kernel
    return total


def rat(x):
    x = F(x)
    return {'num': x.numerator, 'den': x.denominator}


def gaussian(x):
    x = G.cast(x)
    return {'re': rat(x.re), 'im': rat(x.im)}


def enclosure(x, bits: int = 40):
    x = F(x)
    s = 1 << bits
    return {'lower': x.numerator*s//x.denominator,
            'upper': -((-x.numerator*s)//x.denominator), 'bits': bits}


def generate():
    COUNT.clear()
    TERMS.clear()
    nmax = 8192
    mu, factors = sieve(nmax)
    other = inverse_one(nmax)
    for n in range(1, nmax+1):
        eq(mu[n], other[n], 'independent Mobius authentication')
    changed = list(mu)
    changed[30] += 1
    rejected = False
    try:
        for n in range(1, nmax+1):
            if changed[n] != other[n]:
                raise ValueError('primitive disagrees with independent inverse')
    except ValueError as exc:
        rejected = str(exc) == 'primitive disagrees with independent inverse'
    require(rejected, 'corrupted primitive rejected')
    fvals = [F(0)]*4096
    mvals = [F(0)]*4096
    s, ef = F(0), F(0)
    for n in range(1, 4096):
        s += F(mu[n], n)
        ef += s*s
        mvals[n], fvals[n] = s, ef
    ys = list(range(2, 257)) + [511, 1023, 2047, 4095]
    displayed = {2, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095}
    cap_rows = []
    for y in ys:
        c, my = cap(mu, y)
        l, fy, a = len(c)-1, fvals[y], abs(my)
        width = l-y
        jc, residual = reciprocal_energy(c)
        eq(residual, ZERO, 'cap reciprocal balance')
        eq(my, mvals[y], 'cap primitive agrees with independent prefix')
        for n in range(1, y+1):
            eq(c[n], mu[n], 'native cap prefix preserved')
        require(all(abs(z) <= 3 for z in c[1:]), 'cap coefficient ceiling')
        require(y <= l <= 2*y and l < 2*(y+1), 'first gap support')
        require(F(width) <= y*a/2+1, 'completion width bound')
        require(jc <= 2*fy, 'entire completion energy bound')
        require(y*a**3 <= 9*fy, 'native cubic point bound')
        require(F(width**3, y*y) <= 6*fy, 'cubic width budget')
        d0 = F(32*width**4, y**3)
        require(d0 <= 192*F(width, y)*fy, 'anchored defect envelope budget')
        # Generic amplitude-envelope controls, not invented arithmetic phases.
        for mode in (0, 1):
            r = [ZERO]*(l+1)
            for j in range(1, width+1):
                r[y+j] = F(4*j, y)*UNITS[(j % 4) if mode else 0]
            jr, sr = reciprocal_energy(balance(r))
            eq(sr, ZERO, 'envelope repair is balanced')
            require(jr <= d0, 'full repaired envelope energy including early cells')
        if y in displayed:
            cap_rows.append({'Y': y, 'L': l, 'width': width,
                'm_Y': enclosure(my), 'F_Y': enclosure(fy),
                'J_c': enclosure(jc), 'rho': rat(F(width, y)),
                'D_per_tau_squared': enclosure(d0),
                'D_per_tau_squared_over_F': enclosure(d0/fy)})

    algebra_rows = []
    nonhermitian = False
    for y in [2, 3, 7, 15, 31, 63]:
        raw, _ = cap(mu, y)
        c = [G.cast(z) for z in raw]
        l = len(c)-1
        for mode in ['damp', 'gaussian']:
            chi = char_data(l, factors, mode)
            ac = divisor_kernel(mu, chi, l)
            for n in range(1, l+1):
                prod = ONE
                for p in factors[n]:
                    prod = prod*(1-chi[p])
                eq(ac[n], prod, 'divisor sum equals prime product')
            q = conv(ac, c, l)
            ct = twist(c, chi)
            r = [q[n]-ct[n] for n in range(l+1)]
            for n in range(1, l+1):
                expected = (1-chi[n])*(c[n]-mu[n])
                eq(r[n], expected, 'all compressed defect coefficients')
                if n <= y:
                    eq(r[n], ZERO, 'defect gap is preserved')
            if mode == 'gaussian':
                psi = [z.conj() for z in chi]
            else:
                psi = [ZERO]+[G(F(n)) for n in range(1, l+1)]
            back = balance(twist(balance(twist(c, chi)), psi))
            eq(back, c, 'balanced multiplier inverse algebra')
            combined = [chi[n]*chi[n] for n in range(l+1)]
            eq(balance(twist(balance(twist(c, chi)), chi)),
               balance(twist(c, combined)), 'balanced multiplier composition')
            # Complete, independently grouped rational product-kernel panels.
            if y <= 31:
                x = max(2*l, (l*l+3)//4)
                phi = [F(0)]+[phi_control(n, x) for n in range(1, l*l+1)]
                require(all(phi[n] == 0 for n in range(1, l+1)),
                        'microscopic low-coordinate invisibility')
                uqq, utt = pair(q, q, phi), pair(ct, ct, phi)
                cross, rr = pair(ct, r, phi), pair(r, r, phi)
                eq(uqq-utt, 2*cross+rr, 'complete tensor difference')
                p, d = balance(ct), balance(r)
                eq(utt, pair(p, p, phi), 'phase repair leaves observable unchanged')
                eq(cross, pair(p, d, phi), 'cross repair leaves observable unchanged')
                eq(rr, pair(d, d, phi), 'quadratic repair leaves observable unchanged')
                eq(uqq, four_factor_pair(c, ac, phi),
                   'factorwise compressed kernel direct replay')
                product = conv(q, q, l*l)
                eq(uqq, sum((product[n]*phi[n] for n in range(1, l*l+1)), ZERO),
                   'product collisions all retained')
                wrong = pair([z.conj() for z in ct], r, phi)
                if wrong != cross:
                    nonhermitian = True
                algebra_rows.append({'Y': y, 'L': l, 'mode': mode,
                    'control_X': x, 'U_twisted': gaussian(utt),
                    'U_compressed': gaussian(uqq), 'difference': gaussian(uqq-utt)})
    require(nonhermitian, 'Hermitian replacement genuinely rejected')

    # Exact anticausal Abel formula for phi(t)=1/t at off-grid rational t.
    for y in [3, 7, 15, 31]:
        raw, _ = cap(mu, y)
        c = [G.cast(z) for z in raw]
        l = len(c)-1
        chi = [ZERO]+[G(F(1, n)) for n in range(1, l+1)]
        out = balance(twist(c, chi))
        jc, _ = reciprocal_energy(c)
        jo, so = reciprocal_energy(out)
        require(jo <= 9*jc, 'anticausal damping operator bound')
        eq(so, ZERO, 'damped repair balance')
        prefixes, s = [ZERO]*l, ZERO
        for j in range(1, l):
            s = s+c[j]/j
            prefixes[j] = s
        for k in range(1, l):
            t = F(3*k+1, 3)
            image = prefixes[k]/t
            for j in range(k, l):
                start, end = max(t, F(j)), F(j+1)
                image = image+prefixes[j]*(1/end-1/start)
            direct = -sum((c[n]/(n*n) for n in range(k+1, l+1)), ZERO)
            eq(image, direct, 'off-grid anticausal Abel identity')

    # Exact phase multiplier normalization; analytic proof covers every real xi.
    tau = F(3, 4)
    for j in range(-128, 129):
        xi = F(j, 16)
        ratio = (F(1, 4)+(xi-tau)**2)/(F(1, 4)+xi**2)
        require(F(1, 4) <= ratio <= 4, 'phase multiplier two-sided normalization')
    xi = F(-1, 4)
    eq((F(1, 4)+(xi-tau)**2)/(F(1, 4)+xi**2), F(4),
       'exact multiplier maximum at declared phase')

    raw, _ = cap(mu, 2)
    c = [G.cast(z) for z in raw]
    chi = char_data(9, factors, 'damp')
    ac = divisor_kernel(mu, chi, 9)
    fullq = conv(ac, c, 9)
    shortq = fullq[:4]
    leakage = conv(fullq, fullq, 9)[9]-conv(shortq, shortq, 9)[9]
    eq(fullq[3], G(F(-5, 6)), 'uncompressed leakage q3')
    eq(fullq[9], G(F(-1, 3)), 'uncompressed leakage q9')
    eq(leakage, G(F(-2, 3)), 'factor compression leakage is nonzero')
    phi9 = F(1, 9**5)  # g(t)=(1-t)^4, support 1, X=8.
    eq(leakage*phi9, G(F(-2, 3*9**5)), 'nonzero masked leakage pairing')
    extended = c+[ZERO]*3
    q6 = conv(ac, extended, 6)
    r6 = q6[6]-extended[6]*chi[6]
    leading = (1-chi[6])*(extended[6]-mu[6])
    eq(r6-leading, G(F(-1, 4)), 'first-gap endpoint cannot be included')
    require(phi9 != 0, 'low-coordinate invisibility fails outside its range')

    return {'packet': 'CAP36', 'arithmetic': 'integer/Fraction/Gaussian rational',
        'mobius_limit': nmax,
        'mobius_sha256': hashlib.sha256(bytes(v+1 for v in mu[1:])).hexdigest(),
        'cap_cutoffs': {'all_integers': [2, 256], 'additional': [511, 1023, 2047, 4095]},
        'predicates': dict(sorted(COUNT.items())),
        'predicate_total': sum(COUNT.values()),
        'arithmetic_coverage_terms_not_predicates': dict(sorted(TERMS.items())),
        'cap_panels': cap_rows, 'rational_product_kernel_panels': algebra_rows,
        'negative_controls': {'uncompressed_coefficient_leakage': gaussian(leakage),
            'uncompressed_masked_leakage': gaussian(leakage*phi9),
            'first_gap_endpoint_extra_term': gaussian(r6-leading)},
        'not_numerically_tested': ['actual real anchored phases',
            'the centered harmonic microscopic kernel', 'unbounded analytic quantifiers'],
        'scope': 'Written analytic proofs plus declared exact finite structural replays; not independent review or an RH proof.'}


def strict_object(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise ValueError('duplicate JSON key')
        out[key] = value
    return out


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output', type=Path)
    p.add_argument('--check', type=Path)
    args = p.parse_args()
    result = generate()
    text = json.dumps(result, sort_keys=True, indent=2)+'\n'
    if args.check is not None:
        expected = json.loads(args.check.read_text(encoding='utf-8'),
                              object_pairs_hook=strict_object)
        canonical = json.dumps(expected, sort_keys=True, indent=2)+'\n'
        if text != canonical:
            raise ValueError('receipt does not match primitive replay')
    if args.output is not None:
        args.output.write_text(text, encoding='utf-8')
    else:
        print(text, end='')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print('REJECT: '+str(exc), file=sys.stderr)
        sys.exit(1)
