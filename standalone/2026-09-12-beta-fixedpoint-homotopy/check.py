#!/usr/bin/env python3
"""BFC26: bounded exact identities, not machine proof of the analytic theorems.

Python standard library only. No root finder, zeta evaluation, or quadrature.
Run: python -I -S -B check.py --check result.json
--emit is a producer operation, not acceptance.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from math import comb, factorial
from pathlib import Path
import re
import sys

FILES = {
    'README.md', 'PROOF.md', 'REVIEW.md', 'SOURCES.json', 'VALIDATION.md',
    'check.py', 'test_check.py', 'result.json', 'SHA256SUMS',
}
PARAMETERS = tuple(map(F, ('0', '1/10', '1/4', '1/2', '3/4', '9/10', '1')))
ORDER = 14


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def rising(x: F, n: int) -> F:
    out = F(1)
    for j in range(n):
        out *= x + j
    return out


def beta_moment(j: int) -> F:
    return rising(F(5, 2), j) / rising(F(5), j)


def uniform_moment(j: int) -> F:
    return F(1) if j == 0 else (1 - F(1, 2**(2*j-1))) / (2*j-1)


def scale_moment(theta: F, j: int) -> F:
    require(F(0) <= theta <= F(1), 'parameter outside source interval')
    return (1-theta)*beta_moment(j) + theta*uniform_moment(j)


def fixed_moments(theta: F, order: int) -> tuple[list[F], list[F]]:
    """Triangular fixed-point moments and their exact theta derivatives."""
    require(order >= 1, 'order must be positive')
    m, dm = [F(1), F(1)], [F(0), F(0)]
    for j in range(2, order+1):
        a = scale_moment(theta, j)
        da = uniform_moment(j)-beta_moment(j)
        denom = 1-2*a
        require(denom > 0, 'moment recurrence denominator')
        b = sum((F(comb(j, i))*m[i]*m[j-i] for i in range(1, j)), F(0))
        db = sum((F(comb(j, i))*(dm[i]*m[j-i]+m[i]*dm[j-i])
                  for i in range(1, j)), F(0))
        m.append(a*b/denom)
        dm.append(da*b/(denom*denom)+a*db/denom)
    return m, dm


def sum_moments(m: list[F], j: int) -> F:
    return sum((F(comb(j, i))*m[i]*m[j-i] for i in range(j+1)), F(0))


def peano_moment(j: int) -> F:
    return (uniform_moment(j+3)-beta_moment(j+3))/((j+1)*(j+2)*(j+3))


def response_moments(theta: F, m: list[F], order: int) -> list[F]:
    """Independently reconstruct the positive-measure renewal moments."""
    out = []
    for j in range(order+1):
        a = scale_moment(theta, j+3)
        born = sum_moments(m, j+3)*peano_moment(j)
        lower = sum((F(comb(j, i))*m[i]*out[j-i] for i in range(1, j+1)), F(0))
        out.append((born+2*a*lower)/(1-2*a))
    return out


def brownian_moments(order: int) -> list[F]:
    """Independently invert sinh(sqrt(6t))/sqrt(6t), as exact series."""
    s = [F(6**j, factorial(2*j+1)) for j in range(order+1)]
    inv = [F(1)]
    for j in range(1, order+1):
        inv.append(-sum((s[i]*inv[j-i] for i in range(1, j+1)), F(0)))
    return [(-1)**j * factorial(j) * inv[j] for j in range(order+1)]


def third(theta: F) -> F:
    return F(21, 5)*(30+theta)/(50-theta)


def chi(theta: F) -> F:
    return F(56)/(50-theta)**2


def distance(a: F, b: F) -> F:
    return F(56)*(b-a)/((50-a)*(50-b))


def collision_speed(c: F, a: F, q: F) -> F:
    require(q != 0, 'degenerate collision denominator')
    return 16*c*a/q


def qstr(x: F) -> str:
    return str(x.numerator) + '/' + str(x.denominator)


def digest_obj(x: object) -> str:
    text = json.dumps(x, sort_keys=True, separators=(',', ':'), ensure_ascii=True)
    return hashlib.sha256(text.encode()).hexdigest()


def reconstruct() -> dict:
    panels = []
    identities = 0
    for j in range(15):
        require(beta_moment(j) > 0 and uniform_moment(j) > 0, 'scale positivity')
        if j <= 2:
            require(beta_moment(j) == uniform_moment(j), 'scale low moments')
        if j >= 3:
            require(uniform_moment(j) > beta_moment(j), 'finite higher scale moment')
        identities += 1
    require(beta_moment(3) == F(3,16), 'beta third')
    require(uniform_moment(3) == F(31,160), 'uniform third')
    require(peano_moment(0) == F(1,960), 'Peano mass')
    for theta in PARAMETERS:
        m, dm = fixed_moments(theta, ORDER)
        response = response_moments(theta, m, ORDER-3)
        require(m[2] == F(7,5), 'fixed variance')
        require(m[3] == third(theta), 'third moment formula')
        require(dm[3] == 6*chi(theta), 'metric speed')
        require(response[0] == chi(theta), 'response mass')
        for j in range(ORDER-2):
            expected = dm[j+3]/((j+1)*(j+2)*(j+3))
            require(response[j] == expected, 'independent response identity')
            require(response[j] > 0, 'finite response positivity')
            identities += 1
        r = 2*scale_moment(theta,3)
        born = sum_moments(m,3)/960
        require(born == F(7,10)/(50-theta), 'source mass')
        require(born/(1-r) == chi(theta), 'resolvent mass')
        require(1/(1-r) == F(80)/(50-theta), 'inverse norm formula')
        for J in (0,1,2,4,8,16,32):
            partial = sum((born*r**j for j in range(J+1)), F(0))
            require(chi(theta)-partial == chi(theta)*r**(J+1), 'whole geometric tail')
            identities += 1
        panels.append({
            'theta':qstr(theta), 'moments':[qstr(x) for x in m],
            'moment_derivatives':[qstr(x) for x in dm],
            'response_measure_moments':[qstr(x) for x in response],
            'resolvent_inverse_norm':qstr(1/(1-r)),
        })
        identities += 7
    g,_ = fixed_moments(F(0), ORDER)
    b,_ = fixed_moments(F(1), ORDER)
    independently_b = brownian_moments(ORDER)
    for j in range(ORDER+1):
        require(g[j] == rising(F(5,2),j)/F(5,2)**j, 'gamma endpoint')
        require(b[j] == independently_b[j], 'Brownian endpoint sinh inversion')
        identities += 2
    metric_panels=[]
    for i,a in enumerate(PARAMETERS):
        for b in PARAMETERS[i:]:
            require(distance(a,b) == (third(b)-third(a))/6, 'distance formula')
            mid=(a+b)/2
            require(distance(a,b) == distance(a,mid)+distance(mid,b), 'metric additivity')
            metric_panels.append([qstr(a),qstr(b),qstr(distance(a,b))])
            identities += 2
    require(distance(F(0),F(1)) == F(4,175), 'endpoint length')
    fold_panels=[]
    for c in (F(1),chi(F(0)),chi(F(1))):
        for a in (F(-2),F(-1,3),F(1,5),F(3)):
            for q in (F(-4),F(-1,2),F(2),F(7,3)):
                # Independent convention: F_theta=4*c*a and F_zz=-q/2.
                direct=-2*(4*c*a)/(-q/2)
                got=collision_speed(c,a,q)
                require(got == direct, 'collision factor/sign')
                require((got>0) == (a*q>0), 'fold birth/death sign')
                fold_panels.append([qstr(c),qstr(a),qstr(q),qstr(got)])
                identities += 1
    # These are arithmetic verifications of constants in written proofs, not
    # sample-value substitutes for the continuum Jensen or Peano argument.
    beta_53 = F(2)/rising(F(5,2),3)
    require(beta_53 == F(16,315), 'Peano envelope beta integral')
    require(F(1024,945*3) < 1, 'Peano envelope constant')
    require(F(24,5)*F(2,9) == F(16,15), 'uniform source-response tail')
    require(F(640)*F(29,8)/8 == 290, 'response first-branch bound')
    require(F(16,3)*F(25,3)**2 == F(10000,27) < 400, 'response continuing bound')
    phase = F(1,25)+(F(4,25)-F(8,625))/2-F(1,10)-F(1,300)
    require(phase == F(77,7500) > 0, 'whole-height gamma phase lower')
    for delta in (F(i,40) for i in range(-20,21)):
        h=delta**2*(F(1,4)-delta**2)
        require(F(1,64)-h == (delta**2-F(1,8))**2, 'exact zero-weight maximum')
        identities += 1
    require(F(20,64) == F(5,16), 'whole spectral tail factor')
    require(F(80,49) < 2, 'uniform inverse below two')
    identities += 8
    data={
        'schema':'BFC26-exact-v1',
        'status':{
            'rh_proved':False, 'zero_production_sign_proved':False,
            'analytic_proofs_machine_verified':False,
            'new_native_zero_evaluation':False,
            'bounded_arithmetic_reconstructed':True,
        },
        'scope':{'parameter_panels':len(PARAMETERS), 'moment_order':ORDER,
                 'response_order':ORDER-3, 'fold_panels':len(fold_panels),
                 'bounded_identity_checks':identities},
        'constants':{'w2_squared_contraction':'7/12','max_response_contraction':'31/80',
                     'max_inverse_norm':'80/49','endpoint_d3':'4/175',
                     'peano_mass':'1/960','response_inverse_moment_ceiling':'400/1',
                     'weighted_zero_tail_prefactor':'5/16',
                     'weighted_zero_tail_exponent':'pi/2',
                     'gamma_phase_lower':qstr(phase)},
        'fixed_point_panels':panels,
        'metric_panels':metric_panels,
        'synthetic_fold_panels':fold_panels,
    }
    data['semantic_sha256']=digest_obj(data)
    return data


def no_duplicates(pairs):
    out={}
    for key,value in pairs:
        if key in out:
            raise ValueError('duplicate JSON key: '+key)
        out[key]=value
    return out


def load_strict(path: Path):
    def bad(x):
        raise ValueError('nonfinite JSON number: '+x)
    return json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=no_duplicates,
                      parse_constant=bad)


def same_typed(a, b, at='root'):
    require(type(a) is type(b), 'JSON type mismatch at '+at)
    if isinstance(a,dict):
        require(a.keys() == b.keys(), 'JSON keys mismatch at '+at)
        for k in a:
            same_typed(a[k],b[k],at+'.'+k)
    elif isinstance(a,list):
        require(len(a)==len(b), 'JSON length mismatch at '+at)
        for i,(x,y) in enumerate(zip(a,b)):
            same_typed(x,y,at+'.'+str(i))
    else:
        require(a==b,'reconstruction mismatch at '+at)


def authenticate(root: Path):
    require(not root.is_symlink(), 'symlink root not allowed')
    found=set()
    for p in root.iterdir():
        require(not p.is_symlink(), 'symlink member not allowed')
        require(p.is_file(), 'unexpected non-file member')
        found.add(p.name)
    require(found == FILES, 'packet inventory mismatch')
    seen={}
    for line in (root/'SHA256SUMS').read_text(encoding='ascii').splitlines():
        match=re.fullmatch(r'([0-9a-f]{64})  ([A-Za-z0-9_.]+)',line)
        require(match is not None, 'malformed manifest line')
        hexdigest,name=match.groups()
        require(name not in seen, 'duplicate manifest path')
        seen[name]=hexdigest
    require(set(seen)==FILES-{'SHA256SUMS'},'manifest coverage mismatch')
    for name,wanted in seen.items():
        got=hashlib.sha256((root/name).read_bytes()).hexdigest()
        require(got==wanted,'content drift: '+name)


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--check',type=Path)
    group.add_argument('--emit',type=Path)
    args=parser.parse_args(argv)
    root=Path(__file__).resolve().parent
    if args.emit:
        require(args.emit.resolve() != Path(__file__).resolve(), 'unsafe output')
        result=reconstruct()
        args.emit.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
        print('PRODUCED_BFC26; this is not acceptance')
        return 0
    authenticate(root)
    result=reconstruct()
    given=load_strict(args.check)
    same_typed(given,result)
    print('PASS_BFC26_BOUNDED '+result['semantic_sha256'])
    print(json.dumps(result['scope'],sort_keys=True))
    print('RH and the source-specific complex production sign remain unproved.')
    return 0


if __name__=='__main__':
    try:
        raise SystemExit(main())
    except (ValueError, OSError, KeyError, TypeError, ZeroDivisionError) as exc:
        print('REFUSE_BFC26: '+str(exc),file=sys.stderr)
        raise SystemExit(2)
