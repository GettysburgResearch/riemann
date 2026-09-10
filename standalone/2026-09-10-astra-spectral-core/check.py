#!/usr/bin/env python3
"""Exact bounded checks for SC26; not an RH or infinite-theorem verifier.

Only Python's standard library is used. Synthetic spectra are labeled as such.
The perturbed-Gaussian moment bounds cover the complete defining integrals.
"""
from __future__ import annotations
import argparse
from dataclasses import dataclass
from fractions import Fraction as F
import json
from math import comb, factorial
from pathlib import Path
import subprocess
import sys
import tempfile


def need(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


@dataclass(frozen=True)
class C:
    x: F = F(0)
    y: F = F(0)

    def __add__(self, b):
        b = to_c(b)
        return C(self.x + b.x, self.y + b.y)
    __radd__ = __add__

    def __neg__(self):
        return C(-self.x, -self.y)

    def __sub__(self, b):
        return self + -to_c(b)

    def __rsub__(self, b):
        return to_c(b) + -self

    def __mul__(self, b):
        b = to_c(b)
        return C(self.x*b.x-self.y*b.y, self.x*b.y+self.y*b.x)
    __rmul__ = __mul__

    def __truediv__(self, b):
        b = to_c(b)
        d = b.x*b.x + b.y*b.y
        need(d != 0, 'zero Gaussian-rational denominator')
        return self*b.conj()*C(1/d)

    def __pow__(self, n):
        need(type(n) is int and n >= 0, 'nonnegative integer exponent required')
        a, b = C(F(1)), self
        while n:
            if n & 1:
                a = a*b
            b, n = b*b, n//2
        return a

    def conj(self):
        return C(self.x, -self.y)

    def upper_abs(self):
        return abs(self.x)+abs(self.y)


def to_c(a):
    return a if isinstance(a, C) else C(F(a))


def mul(a, b):
    out = [C() for _ in range(len(a)+len(b)-1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] = out[i+j]+x*y
    return out


def evaluate(p, z):
    v = C()
    for c in reversed(p):
        v = v*z+c
    return v


def lagrange(nodes, k):
    p = [C(F(1))]
    for j, z in enumerate(nodes):
        if j != k:
            p = [c/(nodes[k]-z) for c in mul(p, [-z, C(F(1))])]
    return p


def matmul(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def angle_checks():
    rows = []
    for d in (2, 3, 5, 11, 101, 1001):
        t = F(1, d)
        r, s = (1-t*t)/(1+t*t), 2*t/(1+t*t)
        u, v = [F(1), F(0)], [r, s]
        # (V V^T)^(-1), with V=[u v].
        g = [[F(1), -r/s], [-r/s, (1+r*r)/(s*s)]]
        dot = lambda a, b: sum(a[i]*b[i] for i in range(2))
        apply = lambda a: [dot(row, a) for row in g]
        need(dot(u, apply(v)) == 0, 'metric orthogonality')
        for sign in (-1, 1):
            q = [u[i]+sign*v[i] for i in range(2)]
            need(apply(q) == [x/(1+sign*r) for x in q], 'sharp eigenpair')
        kappa = (1+r)/(1-r)
        need(kappa == d*d, 'sharp angle condition number')
        rows.append({'denominator': d, 'correlation': str(r), 'condition': str(kappa)})
    return rows


def spectral_checks():
    rows = []
    r, r0 = F(1, 8), F(1, 16)
    for aa, bb in ((F(1,2),F(1,3)), (F(2,5),F(1,5)), (F(1,3),F(1,4))):
        alpha = C(aa, bb)
        nodes = [alpha, alpha.conj(), C(F(1,4)), C(F(-1,5))]
        ell = [lagrange(nodes, j) for j in range(2)]
        for j in range(2):
            for k in range(4):
                need(evaluate(ell[j], nodes[k]) == to_c(int(j == k)), 'Lagrange cardinality')
        bound_c = sum(c.upper_abs()*r**k for p in ell for k, c in enumerate(p))
        norm2 = aa*aa+bb*bb
        need(norm2 > r*r, 'separated outer spectral node')
        for m in range(5):
            a = C(F(0), F(1))/(alpha**(m+1))
            p = [C()]*m + [a*x+a.conj()*y for x,y in zip(ell[0],ell[1])]
            need(all(c.y == 0 for c in p), 'real polynomial coefficients')
            need(evaluate(p, alpha)*alpha == C(F(0), F(1)), 'target interpolation')
            need(evaluate(p, alpha.conj())*alpha.conj() == C(F(0), F(-1)), 'conjugate interpolation')
            need(all(evaluate(p,z) == C() for z in nodes[2:]), 'other outer nodes retained')
            square = mul(p,p)
            # EXACT complete tail lambda_k=r0/2^k, k>=1, not a truncated sum.
            tail = sum(c.x*r0**(j+2)/F(2**(j+2)-1) for j,c in enumerate(square))
            bound = bound_c**2/norm2*(r*r/norm2)**m*r0*r0/3
            need(F(0) <= tail <= bound, 'entire synthetic spectral tail')
            total = F(-2)+tail
            # Independently reconstruct from the complete power-sum sequence.
            direct = C()
            for i, x in enumerate(p):
                for j, y in enumerate(p):
                    power = i+j+2
                    sn = sum((z**power for z in nodes), C())+r0**power/F(2**power-1)
                    direct = direct + x*y*sn
            need(direct == C(total), 'signed Hankel versus spectral evaluation')
            need(bound < 2 and total < 0, 'complete negative witness')
            rows.append({'alpha': [str(aa),str(bb)], 'm': m,
                         'full_tail': str(tail), 'tail_bound': str(bound), 'total': str(total)})
    return rows


def cumulant_checks():
    count = 0
    for weights in ((1,1,1),(1,2,3),(2,3,1),(5,1,2),(1,7,2),(3,4,5)):
        mass = sum(weights)
        moments = [F(1)]+[F(sum(w*x**n for w,x in zip(weights,(1,2,3))), mass)
                             if n%2 == 0 else F(0) for n in range(1,17)]
        kappas = [F(0)]*17
        for n in range(1,17):
            kappas[n] = moments[n]-sum(F(comb(n-1,j-1))*kappas[j]*moments[n-j]
                                      for j in range(1,n))
        q = [C()]+[C((-1)**m*moments[2*m]/factorial(2*m)) for m in range(1,9)]
        log = [C()]*9
        power = [C(F(1))]
        for j in range(1,9):
            power = mul(power,q)[:9]
            for k,c in enumerate(power):
                log[k] = log[k]+c*F((-1)**(j+1),j)
        for m in range(1,9):
            trace = F((-1)**(m+1),2*factorial(2*m-1))*kappas[2*m]
            need(log[m] == C(-trace/m), 'cumulant/determinant trace sign')
            count += 1
    # A real Jordan block: algebraic multiplicity survives every trace.
    for lam in (F(1,3), F(-2,5)):
        a = [[lam,F(1)],[F(0),lam]]
        power = [[F(1),F(0)],[F(0),F(1)]]
        for n in range(1,9):
            power = matmul(power,a)
            need(power[0][0]+power[1][1] == 2*lam**n, 'Jordan multiplicity')
            count += 1
    return count


def model_check():
    eps = F(1,1024)
    def gaussian(j):
        value = F(1)
        for k in range(1,j+1):
            value *= F(2*k-1,2)
        need(value == F(factorial(2*j),4**j*factorial(j)), 'Gaussian moment reconstruction')
        return value
    raw = [gaussian(j)+gaussian(j+2)/16 for j in range(5)]
    lower = [raw[j]-eps*raw[j+2] for j in range(3)]
    need(all(x > 0 for x in lower), 'positive moment denominators')
    kappa_lower = lower[2]/raw[0]-3*(raw[1]/lower[0])**2
    need(kappa_lower > F(3,64), 'full perturbed-density fourth cumulant')
    kappa0 = raw[2]/raw[0]-3*(raw[1]/raw[0])**2
    need(kappa0 == F(294,4489), 'unperturbed fourth cumulant')
    need(F(3,67)**2-4*F(1,268) == F(-58,4489), 'unperturbed transform discriminant')
    return {'epsilon': str(eps), 'raw_gaussian_moments': [str(x) for x in raw],
            'fourth_cumulant_lower': str(kappa_lower),
            'strict_fourth_cumulant_floor': '3/64',
            'strict_trace_square_upper': '-1/256'}


def reconstruct():
    return {'packet': 'SC26', 'rh_proved': False, 'all_theta_hankels_proved': False,
            'scope': 'bounded exact algebra; complete changed-density moment bounds; synthetic spectral tails',
            'angles': angle_checks(), 'synthetic_spectral_witnesses': spectral_checks(),
            'formal_cumulant_and_jordan_identities': cumulant_checks(),
            'changed_density_certificate': model_check()}


def canonical(data):
    return json.dumps(data,sort_keys=True,indent=2,ensure_ascii=True)+'\n'


def pairs(items):
    out = {}
    for k,v in items:
        need(k not in out, 'duplicate JSON key')
        out[k] = v
    return out


def bad_number(_):
    raise ValueError('nonintegral or nonfinite JSON number')


def load(text):
    return json.loads(text,object_pairs_hook=pairs,parse_float=bad_number,parse_constant=bad_number)


def self_test(expected):
    valid = canonical(expected)
    changed = json.loads(valid)
    changed['rh_proved'] = True
    cases = [canonical(changed), valid.replace('"denominator": 2','"denominator": true',1),
             valid.replace('"denominator": 2','"denominator": 2.0',1),
             valid.replace('"packet": "SC26",','"packet": "SC26", "packet": "SC26",',1),
             valid.replace('"strict_trace_square_upper": "-1/256"','"strict_trace_square_upper": "1/256"',1)]
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp)/'receipt.json'
        cmd = [sys.executable]+(['-O'] if sys.flags.optimize else [])+['-I','-S','-B',str(Path(__file__).resolve()),'--check',str(path)]
        for i,text in enumerate([valid]+cases):
            if i:
                need(text != valid, 'mutation must change actual bytes')
            path.write_text(text,encoding='utf-8')
            run = subprocess.run(cmd,capture_output=True,text=True,timeout=30)
            need((run.returncode == 0) == (i == 0), 'CLI acceptance/refusal mismatch')
    return len(cases)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--emit',type=Path)
    mode.add_argument('--check',type=Path)
    parser.add_argument('--self-test',action='store_true')
    args = parser.parse_args()
    expected = reconstruct()
    if args.emit:
        args.emit.write_text(canonical(expected),encoding='utf-8')
    else:
        actual = load(args.check.read_text(encoding='utf-8'))
        need(canonical(actual) == canonical(expected), 'receipt differs from full reconstruction')
    refused = self_test(expected) if args.self_test else 0
    print(json.dumps({'status':'PASS_BOUNDED_SC26','refusals':refused,
                      'angles':len(expected['angles']),
                      'synthetic_witnesses':len(expected['synthetic_spectral_witnesses']),
                      'formal_trace_identities':expected['formal_cumulant_and_jordan_identities'],
                      'rh_proved':False},sort_keys=True))


if __name__ == '__main__':
    try:
        main()
    except (ValueError,OSError,TypeError,KeyError,subprocess.TimeoutExpired) as error:
        print('REFUSE: '+str(error),file=sys.stderr)
        sys.exit(1)
