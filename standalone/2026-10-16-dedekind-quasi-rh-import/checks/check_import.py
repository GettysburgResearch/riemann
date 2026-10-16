#!/usr/bin/env python3
"""Exact source transport, Euler algebra, dilation, and exponent diagnostics.

No network, floating arithmetic, Lean execution, or asymptotic inference.
Run with normal Python and python -O; all rejection gates remain active.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
PIN = '09afbb4ce6570c1615d58509dc197fc9f0956b7d'

def require(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)

def git_blob(data: bytes) -> str:
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()

@dataclass(frozen=True)
class QI:
    """Gaussian rationals, for exact finite complex-algebra diagnostics."""
    re: F = F(0)
    im: F = F(0)

    @staticmethod
    def lift(x: QI | F | int) -> QI:
        return x if isinstance(x, QI) else QI(F(x))

    def __add__(self, other: QI | F | int) -> QI:
        o = self.lift(other)
        return QI(self.re + o.re, self.im + o.im)
    __radd__ = __add__

    def __neg__(self) -> QI:
        return QI(-self.re, -self.im)

    def __sub__(self, other: QI | F | int) -> QI:
        return self + -self.lift(other)

    def __rsub__(self, other: QI | F | int) -> QI:
        return self.lift(other) + -self

    def __mul__(self, other: QI | F | int) -> QI:
        o = self.lift(other)
        return QI(self.re*o.re-self.im*o.im, self.re*o.im+self.im*o.re)
    __rmul__ = __mul__

    def norm2(self) -> F:
        return self.re*self.re+self.im*self.im

    def __truediv__(self, other: QI | F | int) -> QI:
        o = self.lift(other)
        n = o.norm2()
        if n == 0:
            raise ZeroDivisionError('Gaussian-rational denominator is zero')
        return self*QI(o.re/n, -o.im/n)

    def __rtruediv__(self, other: QI | F | int) -> QI:
        return self.lift(other)/self

ONE = QI(F(1))
ZERO = QI()

def correction(r: F, a: QI, b: QI) -> QI:
    return (1-r*r)*(1-(1-r)*a-r*b)/((1-b)*(1-a))

def normalized(r: F, a: QI, b: QI) -> QI:
    return (1-r*r)*(1+r*(a-b)/(1-a))

def source_checks() -> list[dict]:
    lock = json.loads((ROOT/'UPSTREAM_LOCK.json').read_text())
    require(lock['commit'] == PIN, 'Unrecognized upstream revision')
    rows = []
    require(len(lock['files']) == 13, 'Incomplete selected-source snapshot')
    for item in lock['files']:
        p = ROOT/item['path']
        data = p.read_bytes()
        require(git_blob(data) == item['git_blob'], f'Git identity mismatch: {p}')
        require(hashlib.sha256(data).hexdigest() == item['sha256'], f'SHA256 mismatch: {p}')
        require(len(data) == item['bytes'], f'Length mismatch: {p}')
        rows.append({'path': item['path'], 'git_blob': item['git_blob']})
    challenge = (ROOT/'upstream/Challenge/DedekindZetaChallenge.lean').read_text()
    solution = (ROOT/'upstream/Solution/DedekindZetaSolution.lean').read_text()
    require(len(re.findall(r'\bby sorry\b', challenge)) == 2,
            'Challenge placeholders must be disclosed, not hidden')
    require(re.search(r'\bsorry\b', solution) is None, 'Solution entrypoint has a placeholder')
    for token in ['NumberField.dedekindZeta K s', '31 / 32 < s.re',
                  's ≠ 1', '¬ χ.IsPrincipal → Differentiable ℂ f', 'HasSum']:
        require(token in challenge and token in solution, f'Missing declared interface: {token}')
    config = json.loads((ROOT/'upstream/comparator.json').read_text())
    require(config['permitted_axioms'] == ['propext','Quot.sound','Classical.choice'],
            'Comparator declaration differs from the documented one')
    return rows

def local_checks() -> dict:
    units = [ONE, -ONE, QI(F(0),F(1)), QI(F(0),F(-1))]
    disk = [ZERO] + [r*u for r in [F(1,8),F(1,2),F(7,8)] for u in units]
    n = 0
    for q in [2,7,13,25]:
        r = F(1,q)
        for a in disk:
            for b in disk:
                require(a.norm2()<1 and b.norm2()<1, 'Fixture outside local disk')
                c, cnew = correction(r,a,b), normalized(r,a,b)
                require((1-b)*c == cnew, 'Euler denominator extraction failed')
                require(cnew-1 == -r*r+(1-r*r)*r*(a-b)/(1-a), 'Majorant identity failed')
                require(cnew != ZERO, 'Unexpected local zero inside the permitted disk')
                require(((1-r)*a+r*b).norm2()<1, 'Convex numerator estimate failed')
                n += 1
    r,a,b = F(1,7), QI(F(1,2)), QI(F(1,3))
    require(normalized(r,a,b) != correction(r,a,b), 'Dropping the extraction factor went undetected')
    require(normalized(r,a,b) != (1-r*r)*(1+(a-b)/(1-a)),
            'Missing norm factor q^-1 went undetected')
    # An actual zero when the unit-disk condition on B is violated.
    require(normalized(r,ZERO,QI(1/r)) == ZERO,
            'The necessity of the local domain was not exposed')
    return {'exact_local_configurations': n, 'negative_controls': 3,
            'scope': 'Gaussian-rational local algebra, not a native row census'}

def dilation_checks() -> dict:
    # Distinct formal prime labels may share a norm. Do not deduplicate them.
    primes = [(7, ONE), (7, QI(F(0),F(1))), (25, -ONE)]
    atoms = [(1,QI(F(2))), (7,QI(F(-3),F(1))), (49,ONE)]
    masks = range(1 << len(primes))
    tests = 0
    for s in [1,2,3]:
        base = sum((a*F(1,n**s) for n,a in atoms), ZERO)
        euler = ONE
        for q,b in primes:
            euler *= 1-b*F(q**3,q**(6*s))
        direct = ZERO
        for mask in masks:
            norm, coeff, parity = 1, ONE, 0
            for j,(q,b) in enumerate(primes):
                if (mask >> j) & 1:
                    norm *= q; coeff *= b; parity += 1
            coeff *= (-1)**parity*norm**3
            for n,a in atoms:
                direct += coeff*a*F(1,(n*norm**6)**s)
        require(direct == euler*base, 'Finite signed Mellin/dilation identity failed')
        tests += 1
    q,s=7,1
    true_factor=1-F(q**3,q**(6*s))
    require(true_factor != 1-F(1,q**(6*s)), 'Missing d^3 weight was not detected')
    require(true_factor != 1-F(q**3,q**(5*s)), 'Wrong dilation power was not detected')
    require(F(1,7)*true_factor != F(1,7), 'False added gcd restriction was not detected')
    return {'finite_three_prime_mellin_tests': tests, 'negative_controls':3,
            'equal_norm_prime_labels_retained':True}

def budget_checks() -> dict:
    scales = (ROOT/'upstream/DedekindZetaZeroFree/Moments/Probes/Poisson/Scales.lean').read_text()
    growth = (ROOT/'upstream/DedekindZetaZeroFree/Nonvanishing/Mellin/Quantitative/Growth.lean').read_text()
    def ratio(name: str) -> F:
        m=re.search(r'def '+name+r'\s*: ℝ := (\d+) / (\d+)',scales)
        if not m: raise RuntimeError('Missing source scale '+name)
        return F(int(m[1]),int(m[2]))
    x,y,m,r = [ratio(t) for t in ['xExponent','yExponent','supportExponent','reflectedExponent']]
    require('717 / 2000' in growth and '61 / 100' in growth, 'Unrecognized growth-source budget')
    err,shift=F(717,2000),F(61,100)
    require(x+y==m, 'Support exponent mismatch')
    require((2*m-1-y)/2==r, 'Cauchy exponent mismatch')
    beta=shift+max(r,err); floor=shift+err
    require(beta==F(31,32), 'Published exponent mismatch')
    require(floor==F(1937,2000) and beta-floor==F(1,4000), 'Error-floor calculation mismatch')
    for gain in [F(0),F(1,8000),F(1,4000),F(1,1000),F(1)]:
        require(beta-(shift+max(r-gain,err))<=F(1,4000), 'Fixed-error budget incorrectly crossed')
    require((3+1)/F(6)==F(2,3) and (2+1)/F(6)==F(1,2), 'Euler convergence thresholds mismatch')
    for k in range(1,17):
        require(1+2*beta*(k-1)-k==F(15,16)*(k-1), 'High-moment excess calculation mismatch')
    return {k:str(v) for k,v in {'x':x,'y':y,'row_exponent':m,'row_second_moment':2*m-1,
            'reflected':r,'comparison_error':err,'normalization':shift,'published_boundary':beta,
            'fixed_comparison_floor':floor,'maximum_reflected_only_gain':beta-floor,
            'required_f_growth_at_fixed_normalization':F(1,2)-shift,
            'original_product_absolute_threshold':F(2,3),
            'normalized_product_absolute_threshold':F(1,2),
            'signed_dilation_absolute_cost_threshold':F(2,3)}.items()}

def main() -> None:
    result = {'status':'PASS', 'scope':'Finite diagnostics and source identities only',
              'upstream_files':source_checks(), 'local_algebra':local_checks(),
              'signed_dilation':dilation_checks(), 'rational_budget':budget_checks(),
              'lean_build_run':False, 'independent_mathematical_review':False,
              'manuscript_bytes_retrieved':False}
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
