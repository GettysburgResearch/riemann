#!/usr/bin/env python3
"""Exact bounded controls for JGC26, not a proof of its analytic theorems.

Uses only integer/rational SymPy algebra. No zeta, gamma, floating-point,
prime census beyond the declared finite controls, or upstream producer.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any
import sympy as S

SCHEMA = 'riemann.astra.sharp-jordan-green.v1'
class CheckError(ValueError):
    pass

def require(ok: Any, message: str) -> None:
    if not bool(ok):
        raise CheckError(message)

def equal(a: Any, b: Any, message: str) -> None:
    require(S.expand(S.cancel(S.expand(a-b))) == 0, message)

def bernstein(poly: Any, x: Any, lo: Any, hi: Any) -> list[Any]:
    """Exact interval positivity certificate, not grid sampling."""
    v = S.Symbol('v')
    p = S.Poly(S.expand(poly.subs(x, lo+(hi-lo)*v)), v)
    n = p.degree()
    if n == S.S.NegativeInfinity:
        return [S.Rational(0)]
    a = [p.nth(j) for j in range(n+1)]
    return [sum(a[j]*S.Rational(math.comb(k,j),math.comb(n,j))
                for j in range(k+1)) for k in range(n+1)]

def positive_rational(expr: Any, x: Any, lo: Any, hi: Any, name: str) -> int:
    num, den = S.fraction(S.cancel(expr))
    bn, bd = bernstein(num,x,lo,hi), bernstein(den,x,lo,hi)
    if all(t<0 for t in bd):
        bn,bd=[-t for t in bn],[-t for t in bd]
    require(all(t>=0 for t in bn), name+': numerator Bernstein coefficient')
    require(all(t>0 for t in bd), name+': denominator Bernstein coefficient')
    return len(bn)+len(bd)

def fs(n: int, s: int) -> Any:
    return S.prod(1-S.Rational(1,p**s) for p in S.factorint(n))

def run() -> dict[str, Any]:
    rows: list[dict[str,Any]] = []
    def add(name: str, fixtures: int, detail: str='') -> None:
        require(fixtures>0, name+': empty control')
        require(all(x['name']!=name for x in rows), 'duplicate control')
        rows.append({'name':name,'fixtures':fixtures,'detail':detail})
    s,y,r,q,c,k=S.symbols('s y r q c k',real=True)
    p=y-y**2/4+y**3/18-y**4/96
    j=y**2/2-y**3/12+y**4/72-y**5/480
    equal(S.diff(j,y),p,'integrated polynomial')
    equal(S.diff(p,y),1-y/2+y**2/6-y**3/24,'Ein polynomial')
    equal(p.subs(y,2),S.Rational(23,18),'p(2)')
    equal(j.subs(y,2),S.Rational(67,45),'j(2)')
    add('Ein_envelope_exact_coefficients',4)
    equal(S.diff(p,y,2),-S.Rational(5,18)-(y-S.Rational(4,3))**2/8,'e concavity')
    equal(S.diff(p,y)+S.diff(p,y,2),S.Rational(1,2)-y*(y*y-y+4)/24,'L concavity')
    equal(y*y-y+4,(y-S.Rational(1,2))**2+S.Rational(15,4),'positive quadratic')
    add('uniform_concavity_identities',3)
    L=2*(1-s-r*y+p)+2*((1-s)*y-r*y*y/2+j)-2*r
    equal(S.diff(L,y,2),2*(S.diff(p,y,2)+S.diff(p,y)-r),'L second derivative')
    equal(S.diff(L,r),-y*y-2*y-2,'L r monotonicity')
    b=S.cancel(L.subs(r,2/(s+2)))
    equal(S.diff(b,s),-2*(1+y)+2*(y*y+2*y+2)/(s+2)**2,'s monotonicity formula')
    equal(10*(1+y)-3*(y*y+2*y+2),(2-y)*(3*y+2),'monotonicity interval certificate')
    add('comparison_monotonicity',4)
    U=2-2*r+2*(1-r)*y-r*y*y
    equal(U.subs({y:0,r:2/(s+2)}),2*s/(s+2),'unit endpoint 0')
    equal(U.subs(y,s).subs(r,2/(s+2)),2*s/(s+2),'unit endpoint s')
    f=positive_rational(2/(s+2)-S.Rational(4,5),s,0,S.Rational(1,2),'initial margin')
    add('small_scale_unit_interval',f+2)
    N=1440-2160*s-1160*s*s-30*s**3-s**4-3*s**5
    equal(b.subs(y,s),s*N/(720*(s+2)),'small endpoint polynomial')
    equal(N.subs(s,S.Rational(1,2)),S.Rational(2115,32),'N endpoint')
    f=positive_rational(-S.diff(N,s),s,0,S.Rational(1,2),'N monotonicity')
    equal(S.Rational(2115,32)/1800,S.Rational(47,1280),'small margin')
    add('small_scale_middle_left',f+3)
    equal(b.subs(y,2),-(90*s*s+7*s-46)/(15*(s+2)),'right endpoint formula')
    f=positive_rational(b.subs(y,2)-S.Rational(8,15),s,0,S.Rational(1,2),'small right margin')
    require(S.Rational(8,15)>S.Rational(47,2560),'right margin comparison')
    add('small_scale_middle_right',f+2)
    T=S.Rational(157,45)-2*s-6/(s+2)
    f=positive_rational(T-S.Rational(4,45),s,0,S.Rational(1,2),'small tail')
    require(S.Rational(8,45)>S.Rational(47,2560),'tail margin comparison')
    add('small_scale_infinite_tail',f+1)
    equal(U.subs({r:S.Rational(4,5),y:0}),S.Rational(2,5),'middle unit start')
    equal(U.subs({r:S.Rational(4,5),y:S.Rational(19,20)}),S.Rational(29,500),'middle unit end')
    require(S.Rational(29,500)>S.Rational(1,256),'middle first margin')
    add('middle_scale_unit_interval',3)
    left=b.subs({s:S.Rational(2,3),y:S.Rational(19,20)})
    equal(left,S.Rational(1068867,256000000),'middle left value')
    require(left>S.Rational(1,256),'middle left margin')
    equal(b.subs({s:S.Rational(2,3),y:2}),S.Rational(1,30),'middle right value')
    require(S.Rational(1,30)>S.Rational(1,256),'middle right margin')
    add('middle_scale_concave_interval',4)
    Tmid=S.Rational(1,5)+2*T
    f=positive_rational(Tmid-S.Rational(1,90),s,S.Rational(1,2),S.Rational(2,3),'middle tail')
    require(S.Rational(1,90)>S.Rational(1,256),'middle tail margin')
    add('middle_scale_infinite_tail',f+1)
    d=S.Rational(3,25)
    barrier=2*d+(1-d*d)/r-2*r
    equal(U.subs(y,(1-d)/r),barrier,'large join')
    equal(barrier.subs(r,S.Rational(3,4)),S.Rational(203,3750),'large margin')
    # Clear the positive factor r before the closed interval r=0 is included.
    f=positive_rational(S.cancel(r*(barrier-S.Rational(203,3750))),r,0,S.Rational(3,4),'large barrier')
    require(S.Rational(1,2)>S.Rational(203,3750),'large initial margin')
    add('large_scale_unit_flat_barrier',f+3)
    require(S.Rational(1,3)*S.Rational(3,10)==S.Rational(1,10),'middle source floor')
    require(S.Rational(2,5)*S.Rational(3,10)==d,'large source floor')
    tail=2*S.Rational(1,27)/3/(1-S.Rational(1,9))
    equal(S.Rational(2,3)+tail,S.Rational(25,36),'log2 upper')
    require(S.Rational(25,36)<S.Rational(7,10),'delta bound')
    add('source_floors_and_log2',4)
    e2=1-s-4/(s+2)+S.Rational(23,18)
    f=positive_rational(e2-S.Rational(8,45),s,0,S.Rational(1,2),'small e floor')
    require(S.Rational(275,14)>S.Rational(34,9)**2>3**2,'original kappa comparisons')
    equal((S.Rational(34,9)-2)/20,S.Rational(4,45),'original margin comparison')
    add('original_density_uniform_margin',f+2)
    # Necessity test uses only the rigorous lower bound r>1/(1+s).
    require(S.Rational(3,2)/2<1/(1+S.Rational(1,10)),'sharp threshold counterparameter')
    add('subthreshold_parameter_refused',1,'kappa=3/2, s=1/10 has negative density at zero')
    rhs=S.Symbol('Z')-c/q+k*s/2*(S.Symbol('Z')/q-c/q**2)+s*s*(S.Symbol('Z')/q**2-c/q**3)
    lhs=(q*q+k*s*q/2+s*s)/q**2*(S.Symbol('Z')-c/q)
    equal(lhs,rhs,'full contact formula')
    add('Laplace_contact_and_all_channels',1)
    R=(q+1)/((q+s)*(q+s+1))
    equal(R*(q+s+1)/(q+1),1/(q+s),'gamma regrouping')
    equal(R,(1-s)/(q+s)+s/(q+s+1),'separate rational residues')
    require(S.Rational(1,4)**2*(-1+2*S.Rational(1,4))==-S.Rational(1,32),'negative isolated factor')
    equal(R.subs(s,2)*2/(q+1),2/((q+2)*(q+3)),'s=2 completed factor normalized by pi')
    add('all_scale_gamma_regrouping',4)
    primes=list(S.primerange(2,129))
    fixtures=0
    for n in range(2,129):
        a={p:sum(n//(p**k) for k in range(1,n.bit_length()+1)) for p in primes if p<=n}
        v={p:sum(S.factorint(m).get(p,0) for m in range(1,n+1)) for p in primes if p<=n}
        require(a==v,'factorial valuation identity')
        fixtures+=1
    add('factorial_prime_power_valuations',fixtures,'all N=2,...,128; exact coefficients of every log p')
    fixtures=0
    for ss in (1,2,3):
        for n in range(1,129):
            v=sum(S.mobius(d)*S.Rational(1,d**ss) for d in S.divisors(n))
            equal(v,fs(n,ss),'Jordan divisor identity')
            fixtures+=1
    add('literal_Jordan_coefficients',fixtures,'n=1,...,128 and integer s=1,2,3')
    fixtures=0
    for prime in (2,3,5,7):
        for ss in (1,2,3):
            for power in range(1,9):
                require(1-S.Rational(1,prime**ss)>=(1-S.Rational(1,prime**(ss*power)))/power,'prime-power minorant')
                fixtures+=1
    add('prime_power_subsource',fixtures)
    fixtures=0
    for ss in (1,2,3):
        for n in range(1,25):
            prod=S.prod(1-S.Rational(1,p**(1+ss)) for p in primes if p<=n)
            a=sum(fs(k,ss)*S.Rational(n+1-k,k) for k in range(1,n+1))
            b0=prod*sum(S.Rational(n+1-k,k) for k in range(1,n+1))
            require(a>=b0,'finite decreasing-test FKG')
            fixtures+=1
    add('finite_weighted_association_controls',fixtures,'h(k)=N+1-k; not the proof of general association')
    P=(s+1)*(s+2)*(s+3)
    equal(P/(s+4),s*s+2*s+3-6/(s+4),'mean remainder quotient')
    f=positive_rational(S.Rational(24,5)-P/(s+4),s,0,1,'mean derivative remainder')
    equal(S.Rational(1,12)+S.Rational(1,75),S.Rational(29,300),'mean upper defect')
    equal(S.Rational(1,9)-S.Rational(29,300),S.Rational(13,900),'mean strict reserve')
    equal(S.Rational(13,900)/2,S.Rational(13,1800),'mean final margin')
    add('real_axis_remainder_and_margin',f+4)
    v=S.Symbol('v')
    B4=v*v*(1-v)**2-S.Rational(1,30)
    equal(B4.subs(v,S.Rational(1,2)),S.Rational(7,240),'Bernoulli maximum')
    require(S.Rational(7,240)<S.Rational(1,30),'Bernoulli absolute bound')
    equal(S.diff(B4,v),2*v*(1-v)*(1-2*v),'Bernoulli monotonicity')
    add('periodic_B4_bound',3)
    t=S.Symbol('t')
    equal(t-t/(2-t),t*(1-t)/(2-t),'prime2 reserve identity')
    f=positive_rational(t/(2-t)-S.Rational(1,3),t,S.Rational(1,2),1,'prime2 ratio')
    add('one_prime_real_axis_reserve',f+1)
    b2=S.Rational(1,3);A=S.Rational(1,2)
    src=(1-A*A)/(4*b2*b2);hyp=(1-b2*b2)/(4*b2*b2);crit=(1-(A/b2)**2)/4
    equal(src,crit+hyp,'model port identity')
    require(src==S.Rational(27,16) and hyp==2 and crit==-S.Rational(5,16),'signed port values')
    # Full-rank source positivity is illustrated in its inherited congruence.
    z=[S.Rational(2),S.Rational(3),S.Rational(4)]
    gram=S.Matrix([[(1-A*A)/(x+w)/(((x-1)/(x+1))*((w-1)/(w+1))) for w in z] for x in z])
    for n in range(1,4):require(gram[:n,:n].det()>0,'synthetic source PD')
    add('positive_source_does_not_exhaust',5,'synthetic Schur quotient, not Xi')
    result={'schema':SCHEMA,'status':'PASS_EXACT_BOUNDED_JGC26_CONTROLS',
            'arithmetic':'EXACT_INTEGER_RATIONAL_AND_SYMBOLIC',
            'check_count':len(rows),'fixture_count':sum(x['fixtures'] for x in rows),
            'checks':rows,'RH_proved':False,'analytic_proofs_machine_checked':False,
            'zeta_gamma_evaluations':0,'upstream_producer_imports':0}
    return result

def load_strict(path: Path) -> Any:
    def pairs(xs: list[tuple[str, Any]]) -> dict[str, Any]:
        out={}
        for key,value in xs:
            if key in out:raise CheckError('duplicate JSON key: '+key)
            out[key]=value
        return out
    return json.loads(path.read_text(encoding='utf-8'),object_pairs_hook=pairs,
                      parse_constant=lambda _: (_ for _ in ()).throw(CheckError('nonfinite JSON')))

def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    parser.add_argument('--compare',type=Path)
    args=parser.parse_args()
    try:
        result=run()
        text=json.dumps(result,indent=2,sort_keys=True)+'\n'
        if args.compare:
            other=load_strict(args.compare)
            # Canonical serialization also distinguishes booleans from integers.
            require(json.dumps(other,sort_keys=True,separators=(',',':'))==
                    json.dumps(result,sort_keys=True,separators=(',',':')),'result mismatch')
        if args.output:args.output.write_text(text,encoding='utf-8')
        else:print(text,end='')
        return 0
    except (CheckError,OSError,json.JSONDecodeError) as exc:
        print(json.dumps({'status':'REJECTED','reason':str(exc)},sort_keys=True))
        return 2
if __name__=='__main__':
    raise SystemExit(main())
