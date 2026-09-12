#!/usr/bin/env python3
"""Exact finite-exponential controls. No native xi energy is evaluated."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import argparse
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parent
PARENT = '346f630299252183aec2d8c41a0f3b4027bb9d19'
FILES = {'PROOF.md', 'README.md', 'REVIEW.md', 'SOURCES.json',
         'VALIDATION.md', 'check.py', 'result.json', 'SHA256SUMS'}


def need(test, message):
    if not test:
        raise ValueError(message)


class Q:
    """Gaussian rational; no floating arithmetic or implicit complex casts."""
    __slots__ = ('r', 'i')
    def __init__(self, r=0, i=0):
        if isinstance(r, Q):
            need(i == 0, 'invalid Gaussian copy')
            self.r, self.i = r.r, r.i
        else:
            need(not isinstance(r, float) and not isinstance(i, float), 'float')
            self.r, self.i = F(r), F(i)
    def __add__(self, other):
        b = Q(other)
        return Q(self.r + b.r, self.i + b.i)
    __radd__ = __add__
    def __neg__(self):
        return Q(-self.r, -self.i)
    def __sub__(self, other):
        return self + (-Q(other))
    def __rsub__(self, other):
        return Q(other) - self
    def __mul__(self, other):
        b = Q(other)
        return Q(self.r*b.r - self.i*b.i, self.r*b.i + self.i*b.r)
    __rmul__ = __mul__
    def conj(self):
        return Q(self.r, -self.i)
    def abs2(self):
        return self.r*self.r + self.i*self.i
    def __truediv__(self, other):
        b = Q(other)
        need(b.abs2() > 0, 'zero divisor')
        c = self * b.conj()
        return Q(c.r/b.abs2(), c.i/b.abs2())
    def __rtruediv__(self, other):
        return Q(other)/self
    def __pow__(self, n):
        need(type(n) is int, 'noninteger power')
        if n < 0:
            return (Q(1)/self)**(-n)
        out, x = Q(1), self
        while n:
            if n & 1:
                out = out*x
            n //= 2
            if n:
                x = x*x
        return out
    def __eq__(self, other):
        b = Q(other)
        return self.r == b.r and self.i == b.i


def real(q):
    q = Q(q)
    need(q.i == 0, 'imaginary part remains in a real quantity')
    return q.r


def energy_pair(rates, n):
    """The b_jk w_jk^n formula (all ordered pairs, full time integral)."""
    total = Q(0)
    for a, ma in rates:
        for b, mb in rates:
            den = a + b.conj()
            base = 4*a*b.conj()/den**2
            total += ma*mb/den**2 * base**n
    return real(total)


def gamma_integral(k, rate):
    need(rate.r > 0 and type(k) is int and k >= 0, 'gamma domain')
    return factorial(k)/rate**(k+1)


def derivative_integrals(rates, n):
    """Differentiate each exponential recursively, then integrate products.

    I: physical weighted derivative norm. J: log-time derivative norm.
    Returns exact infinite-interval integrals for finite exponential laws.
    """
    coeff = [(a, Q(m)) for a, m in rates]
    for _ in range(n):
        coeff = [(a, -a*c) for a, c in coeff]
    I, J = Q(0), Q(0)
    for a, ca in coeff:
        for b, cb in coeff:
            q = a + b.conj()
            z = ca*cb.conj()
            I += z*gamma_integral(2*n+1, q)
            # Product of two explicit degree-one log-time derivative factors.
            poly = [Q((n+1)**2), -(n+1)*q, a*b.conj()]
            for k, ck in enumerate(poly):
                J += z*ck*gamma_integral(2*n+1+k, q)
    return real(I), real(J)


def reconstruct():
    groups, record = {}, []
    # Physical strip algebra, no zeta ordinates are supplied.
    native_shaped = []
    for gamma in [F(1,3), F(1,2), F(1), F(2), F(5), F(10)]:
        for delta in [F(-2,5), F(-1,3), F(0), F(1,4), F(2,5)]:
            z = Q(gamma, -delta)
            a = 1+z*z
            x, y = a.r, a.i
            rhs = (gamma*gamma-(1-delta*delta))**2 + 4*gamma*gamma*(1-4*delta*delta)
            need(x > F(3,4) and x*x-3*y*y == rhs > 0, 'strip identity')
            need(3*a.abs2() < 4*x*x, 'angle bound')
            native_shaped.append(a)
    groups['strip_identity_panels'] = len(native_shaped)
    pair_count = 0
    for a in native_shaped:
        for b in native_shaped:
            den = a+b.conj()
            w = 4*a*b.conj()/den**2
            bound = (a.abs2()/(a.r*a.r))*(b.abs2()/(b.r*b.r))
            need(w.abs2() <= bound, 'complete-pair angular bound')
            if a != b:
                need(w.abs2() < bound, 'distinct-rate strictness')
            else:
                need(w == a.abs2()/(a.r*a.r), 'diagonal frequency')
            pair_count += 1
    groups['pair_geometry_panels'] = pair_count

    examples = [
        [(Q(1),2), (Q(3),3)],
        [(Q(1),2), (Q(2,1),1), (Q(2,-1),1)],
        [(Q(3),1), (Q(4,F(1,2)),2), (Q(4,F(-1,2)),2)],
        [(Q(1,F(1,4)),3), (Q(1,F(-1,4)),3)],
    ]
    count = 0
    for index, rates in enumerate(examples):
        S = sum((F(m)/a.r for a,m in rates), F(0))
        R2 = max(a.abs2()/a.r**2 for a,m in rates)
        for n in range(13):
            E = energy_pair(rates,n)
            I, J = derivative_integrals(rates,n)
            I_next, _ = derivative_integrals(rates,n+1)
            need(E > 0 and J >= 0, 'positive integral')
            need(E == F(4**n, factorial(2*n+1))*I, 'two energy reconstructions')
            need(I_next == (n+1)**2*I + J, 'H1 identity')
            V = J/I
            ratio = ((n+1)**2+V)/((n+1)*(F(n)+F(3,2)))
            need(ratio == energy_pair(rates,n+1)/E, 'normalized ratio')
            need((ratio <= 1) == (V <= F(n+1,2)), 'descent threshold')
            need(E <= R2**n*S*S/4, 'whole-energy upper bound')
            record.append([index,n,str(E),str(V)])
            count += 1
    groups['full_integral_and_variational_panels'] = count

    real_model = examples[0]
    complex_model = examples[1]
    d, r = Q(F(4,50),F(3,50)), Q(F(22,25),F(4,25))
    need(d.abs2()==F(1,100) and r.abs2()==F(4,5), 'synthetic magnitudes')
    need((r-1).abs2()==F(1,25), 'synthetic increment modulus')
    for n in range(65):
        E_real = F(5,4)+F(3,4)*F(3,4)**n
        need(energy_pair(real_model,n)==E_real, 'real closed form')
        need(energy_pair(real_model,n+1)<E_real, 'real descent')
        E_bad = F(53,50)+F(1,8)*F(5,4)**n+8*(d*r**n).r
        need(energy_pair(complex_model,n)==E_bad, 'complex closed form')
        if n>=5:
            bound = F(1,32)*F(5,4)**n-F(4,25)*F(9,10)**n
            need(bound>0, 'positive growth budget')
            need(energy_pair(complex_model,n+1)-E_bad>=bound,'complete oscillatory remainder')
    need(energy_pair(complex_model,0)==F(73,40),'initial synthetic value')
    # One exact base inequality and increasing ratio justify every n>=5 in the paper.
    base = F(1,32)*F(5,4)**5-F(4,25)*F(9,10)**5
    need(base>0 and F(5,4)/F(9,10)>1,'all-n geometric argument')
    groups['real_and_complex_closed_forms'] = 65

    # Splitting multiplicities is harmless only if every cross term is retained.
    split = [(a,1) for a,m in complex_model for _ in range(m)]
    for n in range(17):
        need(energy_pair(split,n)==energy_pair(complex_model,n),'multiplicity grouping')
    groups['multiplicity_panels'] = 17

    # Exact complete finite remainder tests, not a native zero-tail verification.
    tail_count = 0
    for extra_x in range(5,10):
        full = complex_model+[(Q(extra_x,F(1,3)),2),(Q(extra_x,F(-1,3)),2)]
        SP = sum((F(m)/a.r for a,m in complex_model),F(0))
        T = F(4,extra_x)
        R2 = max(a.abs2()/a.r**2 for a,m in full)
        for n in range(9):
            need(abs(energy_pair(full,n)-energy_pair(complex_model,n))
                 <= R2**n*(2*SP*T+T*T)/4, 'section remainder')
            tail_count += 1
    groups['finite_section_error_panels'] = tail_count
    digest = hashlib.sha256(json.dumps(record,separators=(',',':')).encode()).hexdigest()
    return {'schema':1, 'status':'PROPOSED_COMPONENT_PROOF_NOT_RH',
            'parent_commit':PARENT, 'groups':groups,
            'mathematical_record_sha256':digest,
            'synthetic_E0':str(F(73,40)),
            'synthetic_growth_base_n5':str(base),
            'native_energies_computed':0,
            'cofinal_native_descent_proved':False,
            'rh_proved':False,
            'analytic_theorems_machine_proved':False}


def strict_json(path):
    def pairs(items):
        out = {}
        for key,value in items:
            need(key not in out,'duplicate JSON key')
            out[key] = value
        return out
    def no_float(s):
        raise ValueError('noninteger numeric JSON token')
    return json.loads(Path(path).read_text(encoding='utf-8'),object_pairs_hook=pairs,
                      parse_float=no_float,parse_constant=no_float)


def canonical(obj):
    return json.dumps(obj,sort_keys=True,separators=(',',':'),ensure_ascii=True)


def authenticate():
    need({p.name for p in ROOT.iterdir()}==FILES, 'packet inventory')
    need(all((ROOT/name).is_file() and not (ROOT/name).is_symlink()
             for name in FILES),'nonregular entry')
    rows = {}
    for line in (ROOT/'SHA256SUMS').read_text(encoding='ascii').splitlines():
        digest,name = line.split('  ',1)
        need(name not in rows and name in FILES-{'SHA256SUMS'},'manifest name')
        rows[name] = digest
    need(set(rows)==FILES-{'SHA256SUMS'},'manifest coverage')
    for name,digest in rows.items():
        need(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,
             'checksum '+name)
    need(strict_json(ROOT/'SOURCES.json')['parent_commit']==PARENT,'source identity')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    g = parser.add_mutually_exclusive_group(required=True)
    g.add_argument('--emit',action='store_true',help='producer; inventory not authenticated')
    g.add_argument('--check',type=Path,help='reconstruct, authenticate and compare')
    args = parser.parse_args()
    expected = reconstruct()
    if args.check:
        authenticate()
        need(canonical(strict_json(args.check))==canonical(expected),'reconstruction mismatch')
    print(json.dumps(expected,sort_keys=True,indent=2))


if __name__=='__main__':
    try:
        main()
    except (ValueError, OSError, KeyError, TypeError, ZeroDivisionError) as exc:
        print('REJECT: '+str(exc),file=sys.stderr)
        sys.exit(1)
