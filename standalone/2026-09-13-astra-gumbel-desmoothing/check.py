"""HBR30: full anchor reconstruction and exact bounded algebra controls.

--write is unauthenticated producer mode; --check is accepting reconstruction.
--self-test executes a pristine copied CLI and eight actual refusal processes.
All mathematical acceptance uses integers/Fractions and authenticated dyadic balls.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
from math import factorial
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
NAMES = {'PROOF.md', 'README.md', 'SOURCES.json', 'VALIDATION.md',
         'ball_core.py', 'anchor.py', 'check.py', 'result.json', 'SHA256.json'}
BALL_BLOB = '2d5dd98a78d0afe279cde2610819165f4b3bef1c'
T = 2**40
P = 2**14


def fail(message: str):
    raise ValueError(message)


def pairs_unique(pairs):
    d = {}
    for k, v in pairs:
        if k in d:
            fail('duplicate JSON key')
        d[k] = v
    return d


def forbidden_number(value):
    fail('floating/nonfinite JSON is outside the contract')


def load(path: Path):
    return json.loads(path.read_text(encoding='utf-8'),
                      object_pairs_hook=pairs_unique,
                      parse_float=forbidden_number, parse_constant=forbidden_number)


def canonical(value) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(',', ':'),
                      ensure_ascii=True).encode('ascii')


def authenticate(root: Path = ROOT):
    got = {p.name for p in root.iterdir()}
    if got != NAMES:
        fail('exact packet inventory differs')
    for name in NAMES:
        p = root / name
        if p.is_symlink() or not p.is_file():
            fail('nonregular or symlink member: '+name)
    manifest = load(root/'SHA256.json')
    if set(manifest) != NAMES-{'SHA256.json'}:
        fail('manifest inventory differs')
    for name, value in manifest.items():
        digest = hashlib.sha256((root/name).read_bytes()).hexdigest()
        if type(value) is not str or value != digest:
            fail('manifest mismatch: '+name)
    data = (root/'ball_core.py').read_bytes()
    blob = hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    if blob != BALL_BLOB:
        fail('inherited primitive blob mismatch')


class C:
    """Small exact Gaussian-rational type, independent of dyadic ball arithmetic."""
    __slots__ = ('r', 'i')
    def __init__(self, r=0, i=0):
        self.r, self.i = F(r), F(i)
    @staticmethod
    def coerce(v):
        return v if isinstance(v, C) else C(v)
    def __add__(self, v):
        v = C.coerce(v)
        return C(self.r+v.r, self.i+v.i)
    __radd__ = __add__
    def __neg__(self):
        return C(-self.r, -self.i)
    def __sub__(self, v):
        return self+-C.coerce(v)
    def __rsub__(self, v):
        return C.coerce(v)+-self
    def __mul__(self, v):
        v = C.coerce(v)
        return C(self.r*v.r-self.i*v.i, self.r*v.i+self.i*v.r)
    __rmul__ = __mul__
    def inv(self):
        d = self.r*self.r+self.i*self.i
        if d == 0:
            fail('Gaussian rational division by zero')
        return C(self.r/d, -self.i/d)
    def __truediv__(self, v):
        return self*C.coerce(v).inv()
    def __rtruediv__(self, v):
        return C.coerce(v)*self.inv()
    def __pow__(self, n):
        if type(n) is not int:
            fail('integer powers required')
        if n < 0:
            return self.inv()**(-n)
        out, base = C(1), self
        while n:
            if n & 1:
                out = out*base
            base = base*base
            n //= 2
        return out
    def conj(self):
        return C(self.r, -self.i)
    def __eq__(self, v):
        v = C.coerce(v)
        return self.r == v.r and self.i == v.i


def mul(a, b, degree=None):
    n = len(a)+len(b)-2 if degree is None else degree
    out = [F(0)]*(n+1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i+j <= n:
                out[i+j] += x*y
    return out


def exp_series(g, n):
    if g[0] != 0:
        fail('formal exponential must have zero constant')
    a = [F(1)]
    for j in range(1, n+1):
        a.append(sum((k*g[k]*a[j-k] for k in range(1, j+1)), F(0))/j)
    return a


def eval_poly(p, x):
    v = C(0) if isinstance(x, C) else F(0)
    for a in reversed(p):
        v = v*x+a
    return v


def frac(v):
    v = F(v)
    return [str(v.numerator), str(v.denominator)]


def algebra():
    from anchor import derivative_polynomials, CELLS, DEGREE, THETA_TERMS
    counts = Counter()
    def require(group, condition):
        if not condition:
            fail('independent algebra failed: '+group)
        counts[group] += 1
    require('parameter_budget', T < 3000175332800)
    require('parameter_budget', P == 16384 and T == 1099511627776)
    require('parameter_budget', T >= max(30, 16*P, 64*P*P))
    require('parameter_budget', T//(32*P) == 2**21)
    exponent = 3+80*P-2**21
    require('parameter_budget', exponent == -786429 and exponent < -1)
    require('coverage', (CELLS, DEGREE, THETA_TERMS) == (128, 24, 4))
    require('coverage', F(1, CELLS)/F(1, 16) == F(1, 8))
    last = F(0)
    for j in range(CELLS):
        c, h = F(2*j+1, CELLS), F(1, CELLS)
        require('coverage', c-h == last)
        last = c+h
    require('coverage', last == 2)
    require('tail_constants', sum((F(3)**j/factorial(j) for j in range(9)), F(0)) > 16)
    require('tail_constants', sum((F(4)**j/factorial(j) for j in range(13)), F(0)) > 50)
    require('tail_constants', F(34, 2**90)/(1-F(1, 2**42)) < F(1, 2**84))
    require('tail_constants', 2*(150**2+2*150+2) < 2**16)
    require('tail_constants', 8*F(1, 2**134) < F(1, 2**128))
    # Independent formal compositions reconstruct the literal differentiated source.
    rows = derivative_polynomials(DEGREE)
    for q in (F(1), F(2), F(7, 2)):
        g = [F(0)] + [(F(1, 2) if k == 1 else 0)-q*F(2)**k/factorial(k)
                       for k in range(1, DEGREE+1)]
        e = exp_series(g, DEGREE)
        pref = [(4*q*q*F(4)**k-6*q*F(2)**k)/factorial(k)
                for k in range(DEGREE+1)]
        composed = mul(e, pref, DEGREE)
        for k in range(DEGREE+1):
            require('source_derivatives', composed[k] == eval_poly(rows[k], q)/factorial(k))
    # Polynomial differentiation independently reconstructs the tail antiderivative.
    for p in (1, 2, 3, 4, 8, 16):
        for b in (F(1, 3), F(2), F(7, 2)):
            factor = [F(0)]*(2*p+1)
            factor[0], factor[2*p] = 2/b, F(2)
            derivative = [F(0)]*(4*p)
            for j in range(1, len(factor)):
                derivative[j-1] += j*factor[j]
            for j, coef in enumerate(factor):
                derivative[j+2*p-1] -= 2*p*b*coef
            wanted = [F(0)]*(4*p)
            wanted[-1] = -4*p*b
            require('tail_antiderivative', derivative == wanted)
            for A in (F(3), F(7,2), F(17)):
                require('tail_antiderivative_values', eval_poly(derivative,A) == -4*p*b*A**(4*p-1))
        for a in (C(2), C(5), C(100, 1), C(100, -1)):
            for k in range(7):
                lhs = factorial(k)*a**(p-1)/(a**p)**(k+1)
                rhs = factorial(k)*a**(-p*k-1)
                require('gamma_moment_algebra', lhs == rhs)
    # Factor-level characteristic identities and the complete centered variances.
    for p1, p2 in ((1, 1), (1, 2), (2, 7), (3, 16), (1, 16384), (8192, 16384)):
        r = F(p1, p2)
        for k in (1, 2, 5, 11):
            for t in (F(0), F(1, 3), F(2), F(-7, 2)):
                lhs = r+(1-r)/(C(1)+C(0, t/F(p1*k)))
                rhs = (C(1)+C(0, t/F(p2*k)))/(C(1)+C(0, t/F(p1*k)))
                require('gamma_product_factor', lhs == rhs)
            variance = (2*(1-r)-(1-r)**2)/F(p1*k)**2
            require('noise_variance', variance == (F(1,p1*p1)-F(1,p2*p2))/F(k*k))
        for K in (1, 2, 7, 32):
            # Finite comparisons plus the exact telescoping majorant of the full tail.
            finite = sum((F(1, k*k) for k in range(K+1, 2*K+1)), F(0))
            telescope = sum((F(1,k*(k-1)) for k in range(K+1, 2*K+1)), F(0))
            require('variance_tail', finite <= telescope == F(1,K)-F(1,2*K))
    # Positive rescaling is a congruence, with the extra scalar in the shifted tower.
    for d in range(1, 6):
        for i in range(d+1):
            for j in range(d+1):
                require('centered_congruence', F(3,2)**(i+j+1) == F(3,2)*F(3,2)**i*F(3,2)**j)
    # Synthetic three-node divisor: no actual zeta-zero claim.
    z0, zp, zm = C(F(29,2)), C(T+1,F(1,4)), C(T+1,F(-1,4))
    nodes = [z**-2 for z in (z0,zp,zm)]
    l0, lp, lm = nodes
    target = C(0,1)/(lp*(lp-l0))
    u = target.i/lp.i
    v = target.r-u*lp.r
    poly = [-l0.r*v, v-l0.r*u, u]
    require('synthetic_witness', eval_poly(poly,l0) == 0)
    require('synthetic_witness', lp*eval_poly(poly,lp) == C(0,1))
    require('synthetic_witness', lm*eval_poly(poly,lm) == C(0,-1))
    q = {k:sum((a**k for a in nodes),C()) for k in range(2,7)}
    form = sum((poly[i]*poly[j]*q[i+j+2] for i in range(3) for j in range(3)),C())
    require('synthetic_witness', form == -2)
    direct = sum(((a*eval_poly(poly,a))**2 for a in nodes),C())
    require('synthetic_witness', form == direct)
    witness_cost = sum((abs(poly[i]*poly[j])*(i+j+1)**2*abs(q[i+j+2].r)
                        for i in range(3) for j in range(3)), F(0))
    require('synthetic_witness', witness_cost > 0)
    return {'counts':dict(sorted(counts.items())),
            'total_controls':sum(counts.values()),
            'tail_exponent_bound':exponent,
            'synthetic':{'is_zeta':False,'polynomial_coefficients':list(map(frac,poly)),
                         'unweighted_quadratic_form':frac(form.r),
                         'centered_witness_cost':frac(witness_cost)}}


def reconstruct():
    sys.path.insert(0, str(ROOT))
    finite = algebra()
    from anchor import reconstruct as native, validate_anchor
    anchor = native()
    validate_anchor(anchor)
    return {'schema':'HBR30-v1','status':'PROPOSED_COMPONENTS_RH_OPEN',
            'rh_proved':False,'p_interval':[1,P], 'imported_zero_height':T,
            'mathematical_scope':'all_times_all_hankel_sizes_bounded_real_p',
            'finite':finite,'native_anchor':anchor}


def verify(path: Path):
    authenticate()
    data = load(path)
    expected = reconstruct()
    if canonical(data) != canonical(expected):
        fail('complete reconstruction mismatch')
    digest = hashlib.sha256(canonical(expected)).hexdigest()
    print('PASS HBR30 full native anchor and',expected['finite']['total_controls'],
          'bounded controls; semantic SHA256',digest)
    return expected


def reseal(root):
    m = {name:hashlib.sha256((root/name).read_bytes()).hexdigest()
         for name in sorted(NAMES-{'SHA256.json'})}
    (root/'SHA256.json').write_text(json.dumps(m,indent=2,sort_keys=True)+'\n',encoding='utf-8')


def selftest():
    flags = ['-I','-S','-B']+(['-O'] if sys.flags.optimize else [])
    cases = ['false_rh','larger_p','wrong_anchor','boolean_alias',
             'duplicate_json','resealed_theta_mutation','unsealed_proof','extra_member']
    with tempfile.TemporaryDirectory(prefix='hbr30-test-') as td:
        base=Path(td)
        for case in ['pristine']+cases:
            target=base/case
            shutil.copytree(ROOT,target)
            if case in ('false_rh','larger_p','wrong_anchor','boolean_alias'):
                data=load(target/'result.json')
                if case=='false_rh':data['rh_proved']=True
                elif case=='larger_p':data['p_interval']=[1,32768]
                elif case=='boolean_alias':data['p_interval'][0]=True
                else:data['native_anchor']['values']['15']['lo_numerator']='1'
                (target/'result.json').write_bytes(canonical(data)+b'\n')
                reseal(target)
            elif case=='duplicate_json':
                text=(target/'result.json').read_text()
                (target/'result.json').write_text('{"rh_proved":true,'+text.lstrip()[1:])
                reseal(target)
            elif case=='resealed_theta_mutation':
                p=target/'anchor.py'
                text=p.read_text()
                old='F(-6), F(4)'
                if text.count(old)!=1:fail('theta mutation is not unique')
                p.write_text(text.replace(old,'F(-5), F(4)'))
                reseal(target)
            elif case=='unsealed_proof':
                with (target/'PROOF.md').open('a') as f:f.write('\nChanged unsealed proof.\n')
            elif case=='extra_member':
                (target/'unexpected.txt').write_text('extra')
            proc=subprocess.run([sys.executable,*flags,str(target/'check.py'),'--check',
                                 str(target/'result.json')],capture_output=True,text=True,timeout=180)
            if (proc.returncode==0)!=(case=='pristine'):
                fail('CLI self-test wrong exit for '+case+': '+proc.stdout+proc.stderr)
            print(('ACCEPT ' if case=='pristine' else 'REFUSE ')+case)
    print('PASS one pristine copied CLI and eight actual altered-copy CLI refusals')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--check',type=Path)
    group.add_argument('--write',type=Path)
    parser.add_argument('--self-test',action='store_true')
    args=parser.parse_args()
    if args.write:
        if args.self_test:fail('producer is not a self-test acceptance')
        report=reconstruct()
        args.write.write_text(json.dumps(report,sort_keys=True,indent=2)+'\n',encoding='utf-8')
        print('PRODUCER ONLY: wrote',args.write)
    else:
        verify(args.check)
        if args.self_test:selftest()

if __name__=='__main__':
    try:main()
    except (ValueError,ArithmeticError,OSError,KeyError,TypeError) as exc:
        print('REJECT:',str(exc),file=sys.stderr)
        sys.exit(1)
