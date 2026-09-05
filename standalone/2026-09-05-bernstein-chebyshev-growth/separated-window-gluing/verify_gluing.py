#!/usr/bin/env python3
"""Rational finite-source and integration-by-parts controls. Not an RH proof."""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from math import isqrt
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
PARENT = ROOT.parent / 'local-window-positivity'
LOCK = {
    'parent_commit': '2c3184545bafb4f5d873d2fa0ffc2c335a25d048',
    'parent_proof_blob': '8d7120ef2edc0ac033a4814eb61917652fc57ba8',
    'parent_checker_blob': 'be63ad510f482016cd5da5a727acb904cc7f1f1d',
}
COUNT = 0
EXPORT_DEN = 10**12
LW = None

def blob(data: bytes) -> str:
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()

def check(ok: bool, label: str) -> None:
    global COUNT
    if not ok:
        raise ValueError('CHECK_FAILED: ' + label)
    COUNT += 1

def no_duplicates(items):
    out = {}
    for k, v in items:
        if k in out:
            raise ValueError('DUPLICATE_JSON_KEY')
        out[k] = v
    return out

def read_json(path):
    return json.loads(Path(path).read_text(), object_pairs_hook=no_duplicates)

def strict_equal(a, b):
    if type(a) is not type(b):
        return False
    if isinstance(a, dict):
        return a.keys() == b.keys() and all(strict_equal(a[k], b[k]) for k in a)
    if isinstance(a, list):
        return len(a) == len(b) and all(strict_equal(x, y) for x, y in zip(a, b))
    return a == b

def load_parent():
    global LW
    if not strict_equal(read_json(ROOT/'SOURCE_LOCK.json'), LOCK):
        raise ValueError('SOURCE_LOCK_MISMATCH')
    for name, key in [('PROOF.md', 'parent_proof_blob'), ('verify_window.py', 'parent_checker_blob')]:
        if blob((PARENT/name).read_bytes()) != LOCK[key]:
            raise ValueError('PARENT_SOURCE_MISMATCH: ' + name)
    spec = importlib.util.spec_from_file_location('gluing_parent_intervals', PARENT/'verify_window.py')
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    LW = mod
    return mod.IV

def sqrt_iv(x):
    x = IV.cast(x)
    if x.lo < 0:
        raise ValueError('square root of negative interval')
    den = LW.DEN
    def lower(a):
        return F(isqrt((a*den*den).__floor__()), den)
    def upper(a):
        n = isqrt((a*den*den).__floor__())
        return F(n if F(n*n, den*den) >= a else n+1, den)
    return IV(lower(x.lo), upper(x.hi))

def exp_iv(x):
    x = IV.cast(x)
    return IV(LW.exp_rat(x.lo).lo, LW.exp_rat(x.hi).hi)

def sinh_iv(x):
    x = IV.cast(x)
    # Sinh is increasing, even on intervals crossing zero.
    lo = (LW.exp_rat(x.lo)-LW.exp_rat(-x.lo))/2
    hi = (LW.exp_rat(x.hi)-LW.exp_rat(-x.hi))/2
    return IV(lo.lo, hi.hi)

def cosh_positive(x):
    x = IV.cast(x)
    if x.lo < 0:
        raise ValueError('cosh_positive domain')
    lo = (LW.exp_rat(x.lo)+LW.exp_rat(-x.lo))/2
    hi = (LW.exp_rat(x.hi)+LW.exp_rat(-x.hi))/2
    return IV(lo.lo, hi.hi)

def export_upper(x):
    return str(F((F(x)*EXPORT_DEN).__ceil__(), EXPORT_DEN))

def abs_upper(x):
    return max(abs(x.lo), abs(x.hi))

def abs_lower(x):
    return F(0) if x.lo <= 0 <= x.hi else min(abs(x.lo), abs(x.hi))

def ldl(M):
    n = len(M)
    L = [[IV.cast(int(i == j)) for j in range(n)] for i in range(n)]
    ds = []
    for j in range(n):
        dj = M[j][j] - sum((L[j][k]*L[j][k]*ds[k] for k in range(j)), IV.cast(0))
        check(dj.lo > 0, 'strict source LDL pivot '+str(j))
        ds.append(dj)
        for i in range(j+1, n):
            L[i][j] = (M[i][j]-sum((L[i][k]*L[j][k]*ds[k] for k in range(j)), IV.cast(0)))/dj
    return ds

def actual_source():
    const = LW.source_constants()  # Independently reconstruct; no saved parent values are loaded.
    b = F(3, 2)
    ell = F(1, 1000)
    logs = {n: LW.log_rat(n) for n in range(1, 8)}
    # Literal von Mangoldt values through 6: log2,log3,log2,log5,0.
    q = {2: logs[2]/sqrt_iv(2), 3: logs[3]/sqrt_iv(3),
         4: logs[2]/2, 5: logs[5]/sqrt_iv(5)}
    check(LW.exp_rat(ell).hi < F(7, 6), 'all cross separations below log 7')
    check(logs[6].lo-logs[5].hi > ell, 'six intervals disjoint')
    check(0 < ell <= F(1,20), 'parent local curvature range')

    def W_Wp(x):
        x = IV.cast(x)
        if x.lo <= 0 or x.hi >= logs[7].lo:
            raise ValueError('source evaluation outside proved finite-prime interval')
        ep, em = exp_iv(b*x), exp_iv(-b*x)
        v = exp_iv(-x)
        lp, lm = LW.log_iv(1+v), LW.log_iv(1-v)
        sg = (em*(lp-lm)+ep*(lp+lm)+exp_iv(-x/2))/6
        dsg = (-em*(lp-lm)+ep*(lp+lm)+exp_iv(-x/2))/4
        w = exp_iv(x/2)/2+const['C_b']*em+sg-const['P2']/b*(ep+em)/2
        wp = exp_iv(x/2)/4-b*const['C_b']*em+dsg-const['P2']*(ep-em)/2
        for n, qn in q.items():
            y = x-logs[n]
            if y.hi <= 0:
                continue
            yp = IV(max(F(0), y.lo), y.hi)
            # The causal sinh is zero below the knot and continuous at it.
            w += qn/b*sinh_iv(b*yp)
            derivative = qn*cosh_positive(b*yp)
            # At a crossed knot both one-sided derivatives must be enclosed.
            wp += IV(F(0), derivative.hi) if y.lo <= 0 else derivative
        return w, wp

    w, wp = W_Wp(ell)
    p = -wp
    mass = w+ell*p/2
    check(w.lo > 0, 'full local endpoint positive')
    check(p.lo > F(11,5), 'local derivative p>11/5')
    r = 6
    mat = [[IV.cast(0) for _ in range(r)] for _ in range(r)]
    deriv = [[F(0) for _ in range(r)] for _ in range(r)]
    interaction = [[F(0) for _ in range(r)] for _ in range(r)]
    pairs = []
    for i in range(r):
        mat[i][i] = mass
        for j in range(i):
            ratio = F(i+1, j+1)
            d = LW.log_rat(ratio)
            xr = IV(d.lo-ell, d.hi+ell)
            v, vp = W_Wp(xr)
            reg = b*b*v-exp_iv(xr/2)+exp_iv(-F(5,2)*xr)/(1-exp_iv(-2*xr))
            knots = [n for n in q if logs[n].hi >= xr.lo and logs[n].lo <= xr.hi]
            # These cross cells meet exactly the corresponding integer prime-power knot.
            expected = [int(ratio)] if ratio.denominator == 1 and int(ratio) in q else []
            check(knots == expected, 'exact prime-knot coverage for '+str(ratio))
            jump = sum((q[n].hi for n in knots), F(0))
            deriv[i][j] = deriv[j][i] = abs_upper(vp)
            interaction[i][j] = interaction[j][i] = ell*abs_upper(reg)+jump
            cij = (W_Wp(d-ell)[0]+2*W_Wp(d)[0]+W_Wp(d+ell)[0])/4
            mat[i][j] = mat[j][i] = cij
            pairs.append({'ratio': str(ratio), 'cross_W': cij, 'Wprime_enclosure': vp,
                          'regular_Wsecond': reg, 'knots': knots, 'jump_bound': export_upper(jump)})
    shifted = [[mat[i][j]- (F(1,100) if i == j else 0) for j in range(r)] for i in range(r)]
    pivots = ldl(shifted)
    dr = list(map(sum, deriv))
    ir = list(map(sum, interaction))
    dmax, betamax = max(dr), max(ir)
    check(dmax < F(5,4), 'derivative coupling row bound')
    check(betamax < F(9,4), 'second derivative and prime cusp row bound')
    check(sum((abs_lower(mat[0][j]) for j in range(1,r)),F(0)) > F(7,100),
          'signed mass certificate is not absolute diagonal dominance')
    check(mass.hi < F(9,200), 'mass diagonal below 9/200')
    check(2*F(11,5)-F(9,4)==F(43,20), 'primitive diagonal margin')
    check(ell*F(5,4)**2 == F(1,640), 'squared mixed coupling bound')
    check(F(1,100)-F(1,640)==F(27,3200), 'final mass lower constant')
    check(F(43,20)-1==F(23,20), 'final primitive lower constant')
    return {'centers': ['log('+str(n)+')' for n in range(1,7)],
            'width':str(ell), 'P2': const['P2'], 'C_b': const['C_b'],
            'p':p, 'mass_diagonal':mass, 'shift':'1/100', 'shifted_LDL_pivots':pivots,
            'mass_matrix':mat, 'cross_pairs':pairs,
            'derivative_row_bounds':[export_upper(x) for x in dr],
            'second_derivative_row_bounds':[export_upper(x) for x in ir],
            'd_star_upper':export_upper(dmax), 'beta_star_upper':export_upper(betamax),
            'T_mass_lower':'81/6400', 'T_primitive_lower':'69/40'}

# Independent polynomial integration controls; these are NOT prime data.
def add(p, q):
    r=[F(0)]*max(len(p),len(q))
    for i,x in enumerate(p):r[i]+=x
    for i,x in enumerate(q):r[i]+=x
    return r

def mul(p,q):
    r=[F(0)]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q):r[i+j]+=x*y
    return r

def integ(p,ell):
    return sum((x*ell**(i+1)/F(i+1) for i,x in enumerate(p)),F(0))

def moment(p,ell,k):
    return integ([F(0)]*k+p,ell)

def primitive(p,ell):
    m=integ(p,ell)
    return [-m/2]+[x/F(i+1) for i,x in enumerate(p)]

def finite_controls():
    ps=[[F(1)],[F(1),F(-2)],[F(2),F(-3),F(4)],[F(-1,2),F(0),F(1),F(-2)]]
    for ell in (F(1),F(1,3),F(2,5)):
        d=2+ell
        for h in ps:
            for k in ps:
                M,N=integ(h,ell),integ(k,ell)
                G,H=primitive(h,ell),primitive(k,ell)
                m1,m2,n1,n2=moment(h,ell,1),moment(h,ell,2),moment(k,ell,1),moment(k,ell,2)
                for a,c,e,q in [(F(7),F(2),F(3),F(5)),(F(-3),F(1),F(-2),F(7)),(F(2),F(-1),F(1,2),F(0))]:
                    direct=a*M*N+c*(d*M*N+m1*N-M*n1)+e*(d*d*M*N+2*d*(m1*N-M*n1)+m2*N-2*m1*n1+M*n2)
                    hinge=sum((hk*kl*ell**(i+j+3)/((j+1)*(j+2)*(i+j+3)) for i,hk in enumerate(h) for j,kl in enumerate(k)),F(0))
                    direct+=q*hinge
                    C=a+c*d+e*(d*d+ell*ell/2)+q*ell/4
                    aij=[c+2*e*d+e*ell+q/2,-2*e]
                    aji=[-c-2*e*d+e*ell-q/2,-2*e]
                    byparts=M*N*C+M*integ(mul(aij,H),ell)+N*integ(mul(aji,G),ell)
                    byparts-=2*e*integ(G,ell)*integ(H,ell)+q*integ(mul(G,H),ell)
                    check(direct==byparts,'cross identity including signed prime-like derivative jump')
    for n in (2,3,5,7,11):
        x=IV.cast(n); y=sqrt_iv(x)
        check(y.lo*y.lo<=n<=y.hi*y.hi,'rational square-root enclosure')
    return {'polynomial_cross_identities':144,'square_root_controls':5}

def pack(x):
    if isinstance(x,IV):
        return {'lo':str(F((x.lo*EXPORT_DEN).__floor__(),EXPORT_DEN)),
                'hi':str(F((x.hi*EXPORT_DEN).__ceil__(),EXPORT_DEN))}
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {k:pack(v) for k,v in x.items()}
    if isinstance(x,list):return [pack(v) for v in x]
    return x

def produce():
    global COUNT, IV
    COUNT=0
    IV=load_parent()
    controls=finite_controls()
    src=actual_source()
    return {'status':'PROPOSED_COMPONENT_PROOFS_REVIEW_REQUIRED','RH_proved':False,
            'checks':COUNT,'arithmetic':'EXACT_RATIONAL_OUTWARD_INTERVAL',
            'internal_decimal_grid':40,'exported_interval_decimal_grid':12,
            'scope':'six separated intervals, all supported L2 functions; not arbitrary supports',
            'finite_controls':controls,'actual_source':pack(src),
            'source_lock':LOCK,
            'source_hashes':{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
                             for name in ('PROOF.md','SOURCE_LOCK.json','verify_gluing.py')}}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    g=parser.add_mutually_exclusive_group(required=True)
    g.add_argument('--write',type=Path);g.add_argument('--check',type=Path)
    args=parser.parse_args()
    result=produce()
    if args.check and not strict_equal(read_json(args.check),result):
        raise ValueError('RESULT_MISMATCH')
    text=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if args.write:args.write.write_text(text)
    print(text,end='')

if __name__=='__main__':
    try:main()
    except (ValueError,OSError,ArithmeticError) as e:
        print(str(e),file=sys.stderr);sys.exit(1)
