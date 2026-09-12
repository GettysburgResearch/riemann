#!/usr/bin/env python3
"""BLS26 bounded exact algebra checks. Does NOT prove RH or certify a zero.

No numerical special-function evaluator or floating arithmetic enters acceptance.
The written infinite-dimensional/analytic proofs need independent review.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import comb, factorial
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
K = F(5, 2)


def demand(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def rise(x: F | int, n: int) -> F:
    a = F(1)
    for j in range(n):
        a *= x + j
    return a


def choose(x: F, n: int) -> F:
    a = F(1)
    for j in range(n):
        a *= (x-j)/F(j+1)
    return a


def wm(j: int) -> F:
    return F(1) if j == 0 else (1-F(1, 2**(2*j-1)))/F(2*j-1)


def bm(j: int) -> F:
    return rise(K, j)/rise(5, j)


def am(theta: F, j: int) -> F:
    return (1-theta)*bm(j)+theta*wm(j)


def normalized_moments(theta: F, n: int) -> tuple[list[F], list[F]]:
    e = [F(1), F(1)]
    for j in range(2,n+1):
        a = am(theta,j)
        e.append(a*sum((e[i]*e[j-i] for i in range(1,j)), F(0))/(1-2*a))
    s = [sum((e[i]*e[j-i] for i in range(j+1)),F(0)) for j in range(n+1)]
    return e[:n+1],s


def raw_moments(theta: F, n: int) -> tuple[list[F], list[F]]:
    # A distinct raw binomial recurrence, not a call to normalized_moments.
    m = [F(1),F(1)]
    for j in range(2,n+1):
        a = am(theta,j)
        m.append(a*sum((comb(j,i)*m[i]*m[j-i] for i in range(1,j)),F(0))/(1-2*a))
    s = [sum((comb(j,i)*m[i]*m[j-i] for i in range(j+1)),F(0)) for j in range(n+1)]
    return m[:n+1],s


def moment_b(s: list[F]) -> list[F]:
    return [sum(((-K)**r*comb(j+4,j-r)*s[r] for r in range(j+1)),F(0))
            for j in range(len(s))]


def w_entry(i: int,j: int) -> F:
    total=F(0)
    for h in range(i-j+1):
        d=i-j-h
        mixing=sum(((-1)**v*comb(d,v)*wm(j+v) for v in range(d+1)),F(0))
        total += (-1)**h*choose(K,h)*rise(5+j,d)/factorial(d)*mixing
    return total


def direct_laguerre(theta: F,n: int, W: list[list[F]]) -> tuple[list[F],list[F]]:
    alpha=[F(1),F(0)]
    beta=[F(1),F(0)]
    for i in range(2,n+1):
        inner=sum((alpha[j]*alpha[i-j] for j in range(1,i)),F(0))
        forcing=sum((W[i][j]*beta[j] for j in range(i)),F(0))
        a=am(theta,i)
        alpha.append((a*inner+theta*forcing)/(1-2*a))
        beta.append(2*alpha[i]+inner)
    return alpha,beta


def lag_poly(n: int) -> list[F]:
    return [F((-1)**r*comb(n+4,n-r),factorial(r)) for r in range(n+1)]


def lag_recurrence(n: int) -> list[F]:
    if n==0:return [F(1)]
    prev=[F(1)];cur=[F(5),F(-1)]
    for j in range(1,n):
        nxt=[F(0)]*(j+2)
        for r,v in enumerate(cur):
            nxt[r]+=(2*j+5)*v/F(j+1)
            nxt[r+1]-=v/F(j+1)
        for r,v in enumerate(prev):nxt[r]-=(j+4)*v/F(j+1)
        prev,cur=cur,nxt
    return cur


def enc(x: F) -> list[int]:return [x.numerator,x.denominator]


def build() -> dict:
    n=18
    W=[[w_entry(i,j) for j in range(i+1)] for i in range(n+1)]
    thetas=[F(0),F(1,10),F(1,4),F(1,2),F(3,4),F(9,10),F(1)]
    source_rows=[]
    count_moment=0; count_direct=0; count_beta=0
    for th in thetas:
        e,s=normalized_moments(th,n);m,raw=raw_moments(th,n)
        b=moment_b(s);alpha,bb=direct_laguerre(th,n,W)
        for j in range(n+1):
            demand(e[j]*factorial(j)==m[j],'raw X moment mismatch')
            demand(s[j]*factorial(j)==raw[j],'raw pair moment mismatch')
            count_moment+=2
            demand(b[j]==bb[j],'direct orthogonal-coordinate mismatch')
            count_direct+=1
        demand(b[:3]==[F(1),F(0),F(0)],'mean/variance normalization')
        demand(b[3]==-35*th/(50-th),'native b3 identity')
        source_rows.append({'theta':enc(th),'b_through_18':[enc(x) for x in b]})
    # Beta matrix is diagonal. The independently expanded kernel uses bm instead of wm.
    for i in range(13):
        for j in range(i+1):
            v=F(0)
            for h in range(i-j+1):
                d=i-j-h
                mix=sum(((-1)**q*comb(d,q)*bm(j+q) for q in range(d+1)),F(0))
                v+=(-1)**h*choose(K,h)*rise(5+j,d)/factorial(d)*mix
            demand(v==(bm(i) if i==j else 0),'beta operator is not diagonal')
            count_beta+=1
    demand(W[3][0]==F(-7,32),'signed forcing term')
    for j in range(n+1):demand(W[j][j]==wm(j),'scale diagonal')
    _,s0=normalized_moments(F(0),n)
    for j in range(n+1):
        demand(s0[j]*factorial(j)==rise(5,j)/K**j,'gamma endpoint pair moments')
    # Endpoint sinh reciprocal generates Laplace coefficients without fixed-point recurrence.
    sinh=[F(6**j,factorial(2*j+1)) for j in range(n+1)]
    lap=[F(1)]
    for j in range(1,n+1):lap.append(-sum((sinh[i]*lap[j-i] for i in range(1,j+1)),F(0)))
    e1,_=normalized_moments(F(1),n)
    demand([(-1)**j*lap[j] for j in range(n+1)]==e1,'Brownian endpoint series')
    # Direct polynomial orthogonality and Mellin polynomial tests.
    orth=0;mell=0
    polys=[lag_poly(j) for j in range(11)]
    for j in range(11):demand(polys[j]==lag_recurrence(j),'Laguerre recurrence normalization')
    for i in range(11):
        for j in range(11):
            val=sum((u*v*rise(5,r+t) for r,u in enumerate(polys[i]) for t,v in enumerate(polys[j])),F(0))
            demand(val==(F(comb(i+4,4)) if i==j else 0),'orthogonality')
            orth+=1
    for j in range(11):
        for q in range(11):
            lhs=sum((v*rise(5,q+r) for r,v in enumerate(polys[j])),F(0))
            rhs=rise(5,q)*rise(-q,j)/factorial(j)
            demand(lhs==rhs,'finite Mellin identity')
            mell+=1
    # Exact Gaussian-rational ratio/telescoping panels for the complete tail theorem.
    tail=0
    for a in [F(-1,4),F(0),F(1,4),F(1,2),F(3,4)]:
        for imag in [F(0),F(1,2),F(2),F(7)]:
            mag=a*a+imag*imag
            J=max(1,(mag+2*a).__ceil__())
            nu=5+2*a
            for j in range(J,J+8):
                ratio=((j-a)**2+imag**2)/F((j+1)*(j+5))
                major=1-nu/F(j+5)
                demand(F(0)<=ratio<=major<F(1),'complete-tail ratio')
                demand((j+4)/F(nu-1)-major*(j+5)/F(nu-1)==1,'telescoping majorant')
                tail+=1
    constants={
        'sin3_lower': F(7,50)-F(7,50)**3/6,
        'sin_sqrt6_lower':F(27,40)-F(27,40)**3/6,
        'weighted_inverse_1_upper':F(3)*F(5,8)+16,
        'weighted_inverse_3half_upper':F(5)*F(5,8)+576,
        'square_norm_upper':F(114000*18),
        'pole_coefficient_over_pi5':F(2)*F(128,3)*F(2,63)**2,
        'gamma_residue_over_pi_minus5':F(6)**5*K**5/12,
    }
    demand(constants['sin3_lower']>F(1,8),'sin3 guard')
    demand(constants['sin_sqrt6_lower']>F(49,80),'sin sqrt6 guard')
    demand(constants['weighted_inverse_1_upper']<18,'weighted inverse1')
    demand(constants['weighted_inverse_3half_upper']<580,'weighted inverse3/2')
    demand(32*580<19000,'density exponential constant')
    demand(K**5>96 and K**5<100,'gamma normalization bounds')
    demand(constants['square_norm_upper']<1500**2,'L2 constant')
    demand(constants['pole_coefficient_over_pi5']==F(1024,11907),'pole coefficient')
    demand(constants['gamma_residue_over_pi_minus5']==F(15)**5/12,'gamma endpoint residue')
    demand(400*F(3,128)*F(22,7)<30,'small-x pair envelope')
    return {
        'packet':'BLS26',
        'status':{'rh_proved':False,'native_collision_sign_proved':False,
                  'new_native_zero_certificate':False,'finite_exact_algebra_only':True},
        'coverage':{'raw_normalized_moment_comparisons':count_moment,
                    'independent_coordinate_comparisons':count_direct,
                    'beta_diagonal_panels':count_beta,'orthogonality_panels':orth,
                    'finite_mellin_panels':mell,'tail_ratio_panels':tail},
        'source_rows':source_rows,
        'constants':{k:enc(v) for k,v in constants.items()},
        'w30':enc(W[3][0]),
        'full_analytic_proofs_machine_verified':False,
    }


def strict_load(path: Path):
    def pairs(items):
        d={}
        for k,v in items:
            if k in d:raise ValueError('duplicate JSON key')
            d[k]=v
        return d
    return json.loads(path.read_text(encoding='utf8'),object_pairs_hook=pairs,
                      parse_constant=lambda x: (_ for _ in ()).throw(ValueError('nonfinite JSON')))


def canonical(o) -> str:
    return json.dumps(o,sort_keys=True,separators=(',',':'),ensure_ascii=False)


def authenticate() -> None:
    mf=ROOT/'SHA256SUMS'
    seen=set()
    for line in mf.read_text(encoding='ascii').splitlines():
        digest,name=line.split('  ',1)
        demand(name not in seen and '/' not in name and '\\' not in name,'manifest path')
        seen.add(name);p=ROOT/name
        demand(p.is_file() and not p.is_symlink(),'file kind')
        demand(hashlib.sha256(p.read_bytes()).hexdigest()==digest,'hash mismatch: '+name)
    names={p.name for p in ROOT.iterdir() if p.name!='SHA256SUMS'}
    demand(names==seen,'complete inventory mismatch')


def main() -> int:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--check',type=Path)
    ap.add_argument('--emit',type=Path)
    ap.add_argument('--no-auth',action='store_true',help='development only; output is not an authenticated acceptance')
    args=ap.parse_args()
    if not args.no_auth:authenticate()
    result=build()
    if args.emit:
        args.emit.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf8')
    if args.check:
        supplied=strict_load(args.check)
        demand(canonical(supplied)==canonical(result),'mathematical/type result mismatch')
    digest=hashlib.sha256(canonical(result).encode()).hexdigest()
    print(json.dumps({'result':'PASS_BOUNDED_EXACT_ALGEBRA', 'authenticated':not args.no_auth,
                      'sha256':digest,'coverage':result['coverage'],'rh_proved':False},sort_keys=True))
    return 0


if __name__=='__main__':
    try:raise SystemExit(main())
    except (ValueError,OSError,KeyError,TypeError) as exc:
        print('REJECT: '+str(exc),file=sys.stderr)
        raise SystemExit(1)
