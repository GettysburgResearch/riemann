#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from decimal import Decimal, Context, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
from typing import Any

HERE=Path(__file__).resolve().parent
SCHEMA='riemann.x97200.rjte-completion-port.control.v1'
RESULT='riemann.x97200.rjte-completion-port.result.v1'
DYADIC=[Fraction(1),Fraction(-5,2),Fraction(2),Fraction(-1,2)]


def primes_upto(N:int)->list[int]:
    isp=bytearray(b'\x01')*(N+1)
    if N>=0: isp[0]=0
    if N>=1: isp[1]=0
    for p in range(2,isqrt(N)+1):
        if isp[p]: isp[p*p:N+1:p]=b'\x00'*(((N-p*p)//p)+1)
    return [i for i in range(2,N+1) if isp[i]]


def mobius(N:int)->list[int]:
    mu=[1]*(N+1);mu[0]=0
    for p in primes_upto(N):
        for k in range(p,N+1,p):mu[k]*=-1
        pp=p*p
        for k in range(pp,N+1,pp):mu[k]=0
    return mu


def finite_b(n:int,P:set[int])->Fraction:
    e=0;m=n
    while m%2==0:
        e+=1;m//=2
    if e>3:return Fraction(0)
    parity=0
    for p in P:
        if m%p==0:
            m//=p;parity+=1
            if m%p==0:return Fraction(0)
    if m!=1:return Fraction(0)
    return DYADIC[e]*((-1)**parity)


def finite_g(n:int,P:set[int])->Fraction:
    e=0;m=n
    while m%2==0:
        e+=1;m//=2
    for p in P:
        while m%p==0:m//=p
    if m!=1:return Fraction(0)
    return Fraction(2*e,1)+Fraction(1,2**e)


def divisors(n:int)->list[int]:return [d for d in range(1,n+1) if n%d==0]

# fixed dyadic rational intervals, represented by integer endpoints / 2^bits

def invsqrt_interval(n:int,bits:int)->tuple[int,int]:
    S=1<<bits; A=n*S*S; lo=isqrt(A); hi=lo if lo*lo==A else lo+1
    return S*S//hi,(S*S+lo-1)//lo

def iadd(a,b):return a[0]+b[0],a[1]+b[1]
def isub(a,b):return a[0]-b[1],a[1]-b[0]
def iqmul(q:Fraction,a:tuple[int,int])->tuple[int,int]:
    num,den=q.numerator,q.denominator
    if num>=0:return (num*a[0]//den,(num*a[1]+den-1)//den)
    m=-num;return (-(m*a[1]+den-1)//den,-(m*a[0]//den))
def imul(a,b,bits:int)->tuple[int,int]:
    S=1<<bits;v=[a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1]]
    return min(v)//S,(max(v)+S-1)//S
def istr(a,bits:int)->list[str]:
    S=1<<bits
    return [str(Fraction(a[0],S)),str(Fraction(a[1],S))]

# directed Decimal intervals for log/sqrt certificate
class DecI:
    def __init__(self,prec:int):
        self.lo=Context(prec=prec,rounding=ROUND_FLOOR)
        self.hi=Context(prec=prec,rounding=ROUND_CEILING)
    def add(self,a,b):return self.lo.add(a[0],b[0]),self.hi.add(a[1],b[1])
    def scale(self,q:int,a):
        qd=Decimal(q)
        return ((self.lo.multiply(qd,a[0]),self.hi.multiply(qd,a[1])) if q>=0
                else (self.lo.multiply(qd,a[1]),self.hi.multiply(qd,a[0])))
    def sqrt(self,n:int):
        x=Decimal(n);return self.lo.sqrt(x),self.hi.sqrt(x)
    def lnrat(self,a:int,b:int=1):
        xlo=self.lo.divide(Decimal(a),Decimal(b));xhi=self.hi.divide(Decimal(a),Decimal(b))
        return self.lo.ln(xlo),self.hi.ln(xhi)
    def divpos(self,a,b):return self.lo.divide(a[0],b[1]),self.hi.divide(a[1],b[0])
    def h(self,X:int,n:int):
        if n>=X:return Decimal(0),Decimal(0)
        l=self.lnrat(4) if X>=4*n else self.lnrat(X,n)
        return self.divpos(l,self.sqrt(n))
    def psi(self,X:int,d:int):
        z=(Decimal(0),Decimal(0))
        z=self.add(z,self.scale(6,self.h(X,d)))
        z=self.add(z,self.scale(-9,self.h(X,2*d)))
        z=self.add(z,self.scale(3,self.h(X,4*d)))
        return z


def validate(data:dict[str,Any])->dict[str,Any]:
    if data.get('schema')!=SCHEMA:raise ValueError('schema')
    expected={
      'pr570':'992404909d6c2940ae8ae849633fe5530ed79db0',
      'pr564':'c74fe9bd7fd284718f4dcef8328af07e553d9d90',
      'pr557':'d11b08938c4db6a6192e96c564a7818cffc77100',
      'pr561':'db9bdc63c855c6ddf664b763d748f8155a6a2c67'}
    if data.get('frozen')!=expected:raise ValueError('freeze mismatch')
    if data.get('expected_mutations')!=12:raise ValueError('mutation contract')
    if any(v is not False for v in data['firewalls'].values()):raise ValueError('firewall promoted')

    # Exact finite Euler system: positive reciprocal, Julia channels, inverse, martingale algebra.
    ov=data['finite_overshoot'];P=set(map(int,ov['odd_primes']));N=int(ov['endpoint']);bits=int(ov['bits'])
    if P!={3,5,7,11,13} or N!=26:raise ValueError('overshoot fixture')
    for n in range(1,N+1):
        b=finite_b(n,P);g=finite_g(n,P)
        if abs(b)>g:raise ValueError(('Julia channel',n,b,g))
        conv=sum((finite_b(d,P)*finite_g(n//d,P) for d in divisors(n)),Fraction(0))
        if conv!=(1 if n==1 else 0):raise ValueError(('inverse',n,conv))
    I=(0,0);m0=(0,0);m2=(0,0)
    terms=[]
    for n in range(1,N+1):
        b=finite_b(n,P);g=finite_g(n,P)
        if b:
            t=iqmul(b,invsqrt_interval(n,bits));I=iadd(I,t);terms.append([n,str(b),*istr(t,bits)])
        if g:
            m0=iadd(m0,iqmul(g,invsqrt_interval(n,bits)))
            m2=iadd(m2,iqmul(b*b/g,invsqrt_interval(n,bits)))
    S=1<<bits
    if I[0]<=S:raise ValueError('finite overshoot disappeared')
    # Unit-normalized Schur matrix [[1,B],[B,1]] has negative determinant.
    B2=imul(I,I,bits);det=(S-B2[1],S-B2[0])
    if det[1]>=0:raise ValueError('Schur separator disappeared')
    # The genuine moment matrix is PSD atomwise; check determinant interval nonnegative.
    momdet=isub(imul(m0,m2,bits),B2)
    if momdet[0]<0:raise ValueError('moment PSD failed')

    # Reconstruct TFPE/ACBI data and refute the trace-only shortcut exactly.
    tc=data['trace_counterexample'];X=int(tc['endpoint']);Dctx=DecI(int(tc['decimal_precision']))
    mu=mobius(X);T=(Decimal(0),Decimal(0));D=(Decimal(0),Decimal(0))
    for d in range(1,X+1,2):
        if mu[d]:
            p=Dctx.psi(X,d);T=Dctx.add(T,p);D=Dctx.add(D,Dctx.scale(mu[d],p))
    bulk=(Decimal(0),Decimal(0));q=1
    while q<=X:
        bulk=Dctx.add(bulk,Dctx.h(X,q));q*=2
    sixbulk=Dctx.scale(6,bulk);A=Dctx.add(sixbulk,Dctx.scale(-1,D))
    if not T[0]>sixbulk[1]:raise ValueError('trace counterexample disappeared')
    if not A[0]>0:raise ValueError('counterexample accidentally refuted TFPE')

    # Exact directed future-prime completion diagnostic.
    cd=data['completion_diagnostic'];K=int(cd['endpoint']);kbits=int(cd['bits'])
    if cd.get('prime_order')!='descending':raise ValueError('completion order')
    scale=1<<kbits
    term=[(0,0)]*(K+1);term[1]=(scale,scale)
    term[2]=iqmul(Fraction(-5,2),invsqrt_interval(2,kbits))
    term[4]=iqmul(Fraction(2),invsqrt_interval(4,kbits))
    term[8]=iqmul(Fraction(-1,2),invsqrt_interval(8,kbits))
    B=[];cur=(0,0)
    for x in term:cur=iadd(cur,x);B.append(cur)
    min_slack=None;min_witness=None
    for p in reversed([q for q in primes_upto(K) if q>=3]):
        r=invsqrt_interval(p,kbits);new=[]
        for x in range(K+1):new.append(isub(B[x],imul(r,B[x//p],kbits)))
        for x in range(2,K+1):
            slack=scale-new[x][1]
            if slack<0:raise ValueError(('descending completion failed',p,x,istr(new[x],kbits)))
            if min_slack is None or slack<min_slack:min_slack=slack;min_witness=(p,x,new[x])
        B=new

    out={
      'schema':RESULT,
      'verdict':'PASS_T97200_RJTE_STATE_AUDIT_AND_COMPLETION_PORT',
      'frozen':expected,
      'finite_euler_overshoot':{
        'odd_primes':sorted(P),'endpoint':N,'boundary_interval':istr(I,bits),
        'excess_lower':str(Fraction(I[0]-S,S)),'terms':terms,
        'unit_schur_determinant_interval':istr(det,bits),
        'moment_matrix_determinant_interval':istr(momdet,bits),
        'interpretation':'positive compiler + PSD Julia + bounded martingale + finite energy do not imply unit-normalized RJTE'},
      'tfpe_acbi_reconstruction':{
        'identity':'A_P(X)=integral_[X/4,X] 6(1-B_P(y)) dy/y = 6 bulk - parity defect',
        'bellman':'A_(Pp)(X)=A_P(X)-p^(-1/2)A_P(X/p)',
        'trace_lower':str(T[0]),'six_bulk_upper':str(sixbulk[1]),
        'trace_shortcut_refuted':True,'parity_defect_interval':[str(D[0]),str(D[1])],
        'actual_tfpe_margin_interval':[str(A[0]),str(A[1])],
        'tfpe_refuted':False},
      'future_prime_completion':{
        'endpoint':K,'prime_order':'descending','directed_bits':kbits,
        'minimum_slack_lower':str(Fraction(min_slack,scale)),
        'minimum_witness':{'prime':min_witness[0],'endpoint':min_witness[1],
                           'boundary_interval':istr(min_witness[2],kbits)},
        'classification':'EXACT_FINITE_DIAGNOSTIC_NOT_ALL_SCALE'},
      'corrected_analytic_scope':{
        'all_scale_RJTE':'equivalent to complete monotonicity of A(s)/s',
        'eventual_RJTE':'equivalent only after subtracting the compact initial Laplace term'},
      'open_producers':['RJTE','TFPE/ACBI','future-complete Bellman inequality'],
      'rh_established':False,
      'proof_boundary':'Exact finite separation, exact TFPE/ACBI reconstruction, directed trace no-go, exact quotient-profile recurrence and finite diagnostic. Does not prove an all-scale producer or RH.'}
    canonical=json.dumps(out,sort_keys=True,separators=(',',':')).encode()
    out['proof_object_sha256']=hashlib.sha256(canonical).hexdigest()
    return out


def main()->int:
    ap=argparse.ArgumentParser();ap.add_argument('certificate',nargs='?',type=Path,default=HERE/'certificates/control.json');ap.add_argument('--output',type=Path)
    a=ap.parse_args();out=validate(json.loads(a.certificate.read_text()));txt=json.dumps(out,indent=2,sort_keys=True)+'\n'
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(txt)
    print(out['verdict']);print(out['proof_object_sha256']);return 0
if __name__=='__main__':raise SystemExit(main())
