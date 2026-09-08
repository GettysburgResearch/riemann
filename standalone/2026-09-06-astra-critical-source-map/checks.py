#!/usr/bin/env python3
"""Finite exact checks for CSM26. Not a machine proof of analytic theorems."""
from __future__ import annotations
import argparse, hashlib, json, math, sys
from fractions import Fraction as F
from pathlib import Path
import sympy as S
sys.dont_write_bytecode=True
import source_certificate as I

class Failure(ValueError): pass

def require(condition, message):
    if not condition: raise Failure(message)

def run():
    checks=[]
    def record(name,n):checks.append({'name':name,'fixtures':n,'passed':True})
    z,w,t,a,k,b,lam,A,n=S.symbols('z w t a k b lam A n')
    # Source-cell integration and right-continuous jump.
    require(S.diff(n*(1-t)+A,t)==-n,'cell derivative')
    N,T,LF=S.symbols('N T LF')
    before=(N-1)*(1-T)+LF
    after=N*(1-T)+LF+T
    require(S.expand(after-before)==1,'unit jump')
    require(S.cancel((w-1)/w*(1/(w-1)-z)-(1/w-z+z/w))==0,'Euler Laplace source')
    record('factorial_cells_and_Laplace_identity',3)
    v=A-n*t
    anti2=-S.exp(-lam*t)*(v*v/lam-2*n*v/lam**2+2*n*n/lam**3)
    anti1=-S.exp(-lam*t)*(v/lam-n/lam**2)
    require(S.simplify(S.diff(anti2,t)-S.exp(-lam*t)*v*v)==0,'norm primitive')
    require(S.simplify(S.diff(anti1,t)-S.exp(-lam*t)*v)==0,'Laplace primitive')
    record('exact_cell_antiderivatives',2)
    # The w^3 prefactor after extracting D from xi.
    require(S.cancel(w*(w-1)*(w*w/(w-1))-w**3)==0,'xi extraction')
    r=(z+S.Rational(1,2)-a)/(z+S.Rational(1,2)+a)
    require(S.cancel(r-(1-2*a/(z+S.Rational(1,2)+a)))==0,'output rational filter')
    record('actual_Xi_rational_prefactors',2)
    P=(z+a)**2*(z+2*a)**2*(z+4*a)**2
    Q=z*z+k*a*z+4*a*a
    quot,rem=S.div(z**3*P,Q,z)
    require(S.degree(quot,z)==7 and S.degree(rem,z)<=1,'desmoothing order')
    require(S.expand(quot*Q+rem-z**3*P)==0,'desmoothing identity')
    # q^3 P/Q times A Q/(q^2 P)(Z-c/q) plus cA = qAZ.
    C,Z,AA=S.symbols('C Z AA')
    require(S.cancel(z**3*P/Q*(AA*Q/(z*z*P)*(Z-C/z))+C*AA-z*AA*Z)==0,'center restoration')
    record('seventh_order_Jordan_desmoothing',3)
    require(F(2079,3304)<F(2,3),'short time margin')
    require(F(1,16)*F(64,63)==F(4,63),'exponent budget')
    require(F(1,1)/(1-F(4,63))==F(63,59),'exp geometric upper')
    require(F(33,56)*F(63,59)==F(2079,3304),'combined bound')
    record('uniform_short_time_constants',4)
    for j in range(13):
        f=1+sum(S.binomial(j,h)*(-2)**h/(z+1)**h for h in range(1,j+1))
        require(S.cancel(f-((z-1)/(z+1))**j)==0,'all-pass power')
    record('causal_allpass_power_expansions',13)
    # Positive causal synthetic pair, full spectral identity.
    dd=(z*z-2*z+5)/(z+1)**3
    nn=(z*z+2*z+5)/(z+1)**3
    require(S.cancel(dd*dd.subs(z,-z)-nn*nn.subs(z,-z))==0,'spectral identity')
    def exp_norm(poly):
        pp=S.Poly(S.expand(poly*poly),t)
        return sum(coef*S.factorial(power[0])/2**(power[0]+1) for power,coef in pp.terms())
    require(exp_norm((2*t-1)**2)==S.Rational(9,2),'input norm')
    require(exp_norm(1+2*t*t)==S.Rational(9,2),'output norm')
    require(dd.subs(z,1)==S.Rational(1,2) and nn.subs(z,1)==1,'source values')
    require(S.cancel((1-(nn/dd)**2)/(2*z)).subs(z,1)==-S.Rational(3,2),'critical negative diagonal')
    require(1-S.Rational(1,2)**2==S.Rational(3,4),'domain defect')
    record('positive_source_pair_full_spectrum_and_domain_defect',6)
    c=[F(9,2),F(-3),F(1)]
    prev=F(1);seq=[]
    for degree in range(13):
        G=S.Matrix([[S.Rational(c[abs(i-j)].numerator,c[abs(i-j)].denominator) if abs(i-j)<=2 else 0
                  for j in range(degree+1)] for i in range(degree+1)])
        det=G.det(method='domain-ge')
        require(det>0,'finite Gram PD')
        cofactor=1 if degree==0 else G[1:,1:].det(method='domain-ge')
        e=S.cancel(1-S.Rational(1,2)*cofactor/det)
        ef=F(int(S.numer(e)),int(S.denom(e)))
        require(F(3,4)<ef<=prev,'projection monotonicity/domain floor')
        seq.append(str(ef));prev=ef
    require(seq[:2]==['8/9','4/5'],'initial projection errors')
    record('synthetic_Toeplitz_projection_tower',27)
    require(F(1,2)<F(3,4)**2,'root radius bound')
    require((2*F(1,4)**2)**2/2==F(1,128),'coercivity lower bound')
    L=S.Matrix([[S.Rational(1,2),0],[1,S.Rational(1,2)]])
    require((S.eye(2)-L.T*L).det()==-S.Rational(7,16),'local/global control')
    record('coercivity_and_memory_counterexamples',3)
    require(S.cancel(w*w/(w-1)-(w+1+1/(w-1)))==0,'Mobius inverse prefactor')
    rr=1+1/((2-b)*(z+b-1))-(1-b)**2/((2-b)*(z+1))
    require(S.cancel(rr-(z+b)**2/((z+b-1)*(z+1)))==0,'outer inverse source')
    for m in range(1,257):
        require(sum(S.mobius(d) for d in S.divisors(m))==int(m==1),'Mobius convolution')
    record('literal_finite_Mobius_inverse',258)
    # Tail primitives by differentiation; all-real coverage is analytic.
    tail=S.exp(-2*b*t)*((1+t)**2/(2*b)+(1+t)/(2*b*b)+1/(4*b**3))
    require(S.simplify(S.diff(tail,t)+S.exp(-2*b*t)*(1+t)**2)==0,'source tail integral')
    record('infinite_source_tail_primitive',1)
    # Directed arithmetic tests compare to independent exact Fractions.
    count=0
    for p in range(-5,6):
        for q in range(1,5):
            x=I.Interval.rat(p,q);xx=F(p,q)
            require(F(x.lo,I.Q)<=xx<=F(x.hi,I.Q),'rational interval')
            for r0 in range(-2,3):
                y=I.Interval.rat(r0,3);yy=F(r0,3)
                for v0,exact in [(x+y,xx+yy),(x*y,xx*yy)]:
                    require(F(v0.lo,I.Q)<=exact<=F(v0.hi,I.Q),'directed operation');count+=1
    for m in range(1,65):
        for power in (3,6,7):
            x=I.inverse_quarter_power(m,power)
            require(x.lo**4*m**power<=I.Q**4<=x.hi**4*m**power,'root interval');count+=1
    record('directed_integer_arithmetic_against_exact_rationals',count+44)
    rejected=0
    for action in [lambda:I.Interval(2,1),lambda:I.log_int(0),lambda:I.inverse_quarter_power(0,3),
                   lambda:I.atanh_log_ratio(3,1),lambda:I.Interval.rat(1)/I.Interval(-1,1),
                   lambda:I.run(4097)]:
        try: action()
        except ValueError:rejected+=1
    require(rejected==6,'invalid inputs not rejected')
    record('source_input_refusals',6)
    return {'schema':'csm26.exact-bounded-controls.v1',
            'named_checks':len(checks),'fixtures':sum(x['fixtures'] for x in checks),
            'checks':checks,'synthetic_projection_errors':seq,
            'arithmetic':'MIXED','implementation':'EXACT_RATIONAL_SYMBOLIC_AND_DIRECTED_DYADIC',
            'RH_proved':False,'analytic_theorems_machine_checked':False,
            'actual_source_run':'separate source.normal.json; not a high-rank campaign'}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path);p.add_argument('--compare',type=Path)
    a=p.parse_args();out=json.dumps(run(),sort_keys=True,indent=2)+'\n'
    if a.compare and a.compare.read_text()!=out:raise Failure('retained exact result differs')
    if a.output:a.output.write_text(out)
    else:print(out,end='')
if __name__=='__main__':main()
