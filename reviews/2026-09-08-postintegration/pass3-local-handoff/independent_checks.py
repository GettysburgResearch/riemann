#!/usr/bin/env python3
"""Reviewer-written exact/directed controls; no author modules or network.

These certify explicitly bounded calculations, not the infinite paper arguments.
Every numerical accepting comparison uses rational outward endpoints.
"""
from __future__ import annotations
from fractions import Fraction as F
from dataclasses import dataclass
from itertools import combinations
from math import factorial, gcd, isqrt
from pathlib import Path
import argparse, json
BITS=160
DEN=1<<BITS
COUNTS={}
def need(ok:bool, message:str)->None:
    if not ok: raise ValueError(message)
def check(group:str,ok:bool,message:str)->None:
    need(ok,message);COUNTS[group]=COUNTS.get(group,0)+1
def rat(x):
    need(type(x) in (int,F),'exact rational required')
    return F(x)
def down(x):
    x=rat(x);return F((x.numerator*DEN)//x.denominator,DEN)
def up(x):return -down(-rat(x))
@dataclass(frozen=True)
class I:
    lo:F
    hi:F
    def __post_init__(self):
        need(type(self.lo) is F and type(self.hi) is F and self.lo<=self.hi,'bad interval')
    @staticmethod
    def make(x,y=None):
        x=rat(x);y=x if y is None else rat(y)
        return I(down(x),up(y))
    def __add__(self,o):
        o=as_i(o);return I(down(self.lo+o.lo),up(self.hi+o.hi))
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,o):return self+-as_i(o)
    def __rsub__(self,o):return as_i(o)+-self
    def __mul__(self,o):
        o=as_i(o);v=[a*b for a in (self.lo,self.hi) for b in (o.lo,o.hi)]
        return I(down(min(v)),up(max(v)))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=as_i(o);need(not o.lo<=0<=o.hi,'zero denominator interval')
        return self*I(down(1/o.hi),up(1/o.lo))
    def __rtruediv__(self,o):return as_i(o)/self
    def sq(self):
        low=F(0) if self.lo<=0<=self.hi else min(self.lo*self.lo,self.hi*self.hi)
        return I(down(low),up(max(self.lo*self.lo,self.hi*self.hi)))
    def pow(self,n):
        need(type(n) is int and n>=0,'nonnegative integer exponent required')
        r=I.make(1);a=self
        while n:
            if n&1:r=r*a
            a=a*a;n//=2
        return r
    def sqrt(self):
        need(self.lo>=0,'negative square root')
        a=isqrt((self.lo.numerator*DEN*DEN)//self.lo.denominator)
        b=isqrt((self.hi.numerator*DEN*DEN)//self.hi.denominator)
        return I(F(a,DEN),F(b if F(b*b,DEN*DEN)==self.hi else b+1,DEN))
def as_i(x):return x if type(x) is I else I.make(x)
def log_frac(x:F,terms=180):
    x=rat(x);need(x>0,'positive logarithm argument required')
    k=0
    while x>=2:x/=2;k+=1
    while x<1:x*=2;k-=1
    def series(z):
        z=I.make(z);q=z*z;p=z;s=I.make(0)
        for j in range(terms):s=s+p*F(2,2*j+1);p=p*q
        rem=(p*F(2,2*terms+1)/(1-q)).hi
        return I(s.lo,up(s.hi+rem))
    base=series((x-1)/(x+1))
    return base+k*series(F(1,3)) if k else base
def log_i(x:I):
    need(x.lo>0,'positive logarithm interval required')
    return I(log_frac(x.lo).lo,log_frac(x.hi).hi)
def pi_interval():
    def atan(q,n):
        x=F(1,q);s=sum(((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(n)),F(0))
        e=x**(2*n+1)/F(2*n+1)
        return I.make(s-e,s+e)
    return 16*atan(5,120)-4*atan(239,40)
def enclosure(x:I,digits=20):
    scale=10**digits
    def floor_s(q):
        n=q.numerator*scale//q.denominator
        return ('-' if n<0 else '')+str(abs(n)//scale)+'.'+str(abs(n)%scale).zfill(digits)
    def ceil_s(q):
        n=-((-q.numerator*scale)//q.denominator)
        return ('-' if n<0 else '')+str(abs(n)//scale)+'.'+str(abs(n)%scale).zfill(digits)
    return {'lower':str(x.lo),'upper':str(x.hi),'decimal_outward':[floor_s(x.lo),ceil_s(x.hi)]}
def inside(group,x,lo,hi):
    check(group,F(lo)<x.lo and x.hi<F(hi),'advertised interval not established: '+str((lo,hi,enclosure(x))))

def arithmetic_controls():
    g='interval_contracts'
    for a,b in [(F(-7,3),F(2,5)),(F(1,7),F(9,11)),(F(0),F(3)),(F(-2),F(-1,3))]:
        x=I.make(a);y=I.make(b)
        for z,exact in [(x+y,a+b),(x*y,a*b),(x-y,a-b),(x/y,a/b)]:
            check(g,z.lo<=exact<=z.hi,'outward arithmetic')
    for value in (True,0.5,'1'):
        try:I.make(value)
        except ValueError:check(g,True,'rejected nonexact input')
        else:raise ValueError('nonexact input accepted')
    try:I.make(1)/I.make(-1,1)
    except ValueError:check(g,True,'zero enclosure rejected')
    else:raise ValueError('zero enclosure accepted')
    for n in range(1,30):
        x=I.make(F(n,7)).sqrt()
        check(g,x.lo*x.lo<=F(n,7)<=x.hi*x.hi,'outward sqrt')
    for n in range(1,25):
        a=log_frac(F(n));b=log_frac(F(2*n))-log_frac(F(2))
        check(g,max(a.lo,b.lo)<=min(a.hi,b.hi),'log doubling control')


def capacity():
    ps=[2,3,5,7,11,13];logs={p:log_frac(F(p)) for p in ps};out={}
    targets={
      'squarefree':('1.18532285971072','1.18532285971074','1.91594153472685','1.91594153472687'),
      'geometric':('1.82250119177775','1.82250119177777','2.37221708831717','2.37221708831720')}
    for kind,(gl,gu,cl,cu) in targets.items():
        modes=[];G=I.make(0)
        for mask in range(1,1<<len(ps)):
            weight=F(1);lam=I.make(0)
            for i,p in enumerate(ps):
                if mask>>i&1:
                    weight*=F(1,p if kind=='squarefree' else p-1)
                    lam+=logs[p]*(F(p+1,p) if kind=='squarefree' else F(p,p-1))
            modes.append((weight,lam));G+=weight/lam
        check('capacity',len(modes)==63,'complete nonempty-subset cover')
        inside('capacity',G,gl,gu)
        residuals=[]
        for c,lower_side in [(F(cl),True),(F(cu),False)]:
            s=I.make(0)
            for b,lam in modes:s+=b/(c*lam-1)
            check('capacity',s.lo>1 if lower_side else s.hi<1,'secular root bracket')
            residuals.append(enclosure(s-1))
        out[kind]={'G':enclosure(G),'C_certified_open_bracket':[cl,cu],
                   'secular_residuals':residuals,'complete_visible_modes':len(modes)}
    # Exact rational-rate product eigenvectors and root Green/Poisson equations.
    for ps in ([2],[2,3],[2,3,5],[2,5,7]):
        rates={p:F(p+2,p+1) for p in ps};states=list(range(1<<len(ps)))
        value={m:__import__('functools').reduce(lambda x,p:x*p,(p for i,p in enumerate(ps) if m>>i&1),1) for m in states}
        Z=sum((F(1,value[m]) for m in states),F(0));mu={m:F(1,value[m])/Z for m in states}
        def op(f):
            return {m:sum((rates[p]*(1 if m>>i&1 else F(1,p))*(f[m]-f[m^(1<<i)]) for i,p in enumerate(ps)),F(0)) for m in states}
        green={m:F(0) for m in states};K=F(0)
        for subset in states[1:]:
            denom=value[subset];lam=sum((rates[p]*F(p+1,p) for i,p in enumerate(ps) if subset>>i&1),F(0))
            eigen={m:__import__('functools').reduce(lambda a,x:a*x,(-p if m>>i&1 else 1 for i,p in enumerate(ps) if subset>>i&1),1) for m in states}
            got=op(eigen)
            check('product_spectrum',all(got[m]==lam*eigen[m] for m in states),'product eigenvector')
            check('product_spectrum',sum(mu[m]*eigen[m] for m in states)==0,'mean-zero eigenvector')
            check('product_spectrum',sum(mu[m]*eigen[m]**2 for m in states)==denom,'root normalization')
            for m in states:green[m]+=eigen[m]/(denom*lam)
            K+=1/(denom*lam)
        Lg=op(green)
        check('product_spectrum',all(Lg[m]==(1/mu[0]-1 if m==0 else -1) for m in states),'root Green equation')
        check('product_spectrum',sum(mu[m]*green[m] for m in states)==0,'centered Green vector')
        check('product_spectrum',sum(mu[m]*green[m]*Lg[m] for m in states)==K,'capacity energy identity')
        life={m:K-green[m] for m in states};Ll=op(life)
        check('product_spectrum',life[0]==0 and all(Ll[m]==1 for m in states if m),'killed Poisson equation')
        check('product_spectrum',sum(mu[m]*life[m] for m in states)==K,'exact stationary mean lifetime')
    return out


def ant_profile(T=4096):
    harmonic=[I.make(0)]
    for n in range(1,T):harmonic.append(harmonic[-1]+F(1,n*n))
    total=I.make(0);d=[1,-5,8,-4]
    for r in range(1,T):
        A=I.make(0);B=F(0)
        for j,dj in enumerate(d):
            U=r//(1<<j);L=r//(1<<(j+1))
            A+=(harmonic[U]-harmonic[L])*F(dj,2*4**j)
            B+=dj*(2*L-F(U,2))
        cell=A.sq()*F(3*r*r+3*r+1,3)+A*(2*B)+F(B*B,r*(r+1))
        check('profile_cells',cell.hi>=0,'negative square-cell upper bound')
        total+=cell
    tail=F(10000,3*T**3);complete=I(total.lo,up(total.hi+tail))
    inside('profile_certificate',complete,'1.704219450036','1.704219498544')
    check('profile_certificate',sum(d)==0 and sum(F(d[j],2**j) for j in range(4))==0,'two profile cancellations')
    check('profile_certificate',sum(abs(d[j])*2**j for j in range(4))==75,'profile remainder sum')
    return {'cutoff':T,'cells':T-1,'finite_integral':enclosure(total),
            'complete_integral':enclosure(complete),'complete_tail_upper':str(tail),
            'norm_ratio_limit_factor':'4*C_star/189; not the optimal uniform comparison constant'}


def mobius_values(N):
    def one(n):
        sign=1;p=2
        while p*p<=n:
            if n%p==0:
                n//=p;sign=-sign
                if n%p==0:return 0
            p+=1
        return -sign if n>1 else sign
    return [0]+[one(n) for n in range(1,N+1)]
def factor(n):
    d={};p=2
    while p*p<=n:
        while n%p==0:d[p]=d.get(p,0)+1;n//=p
        p+=1
    if n>1:d[n]=d.get(n,0)+1
    return d

def native_and_jets():
    Nmax=128;mu=mobius_values(Nmax);M=[0]
    for n in range(1,Nmax+1):M.append(M[-1]+mu[n])
    previous=F(0)
    for N in range(1,Nmax+1):
        J=sum((F(M[k]**2,k*(k+1)) for k in range(1,N)),F(0))+F(M[N]**2,N)
        check('native_source',J-previous==F(2*mu[N]*M[N-1]+mu[N]**2,N),'complete work increment')
        check('native_source',sum(mu[d] for d in range(1,N+1) if N%d==0)==int(N==1),'Mobius divisor inversion')
        H=sum((F(1,k) for k in range(1,N+1)),F(0))
        check('native_source',0<=J/H<=sum(mu[k]**2 for k in range(1,N+1)),'coherent/complement norm')
        if N<=32 or N in (64,96,128):
            pair=sum((F(mu[m]*mu[n],max(m,n)) for m in range(1,N+1) for n in range(1,N+1)),F(0))
            check('native_source',pair==J,'complete pair norm includes stopped future')
            direct={};formula={}
            for n in range(1,N+1):
                for p,v in factor(n).items():
                    formula[p]=formula.get(p,F(0))+mu[n]**2*v
                for p in range(2,N+1):
                    if factor(p)!={p:1}:continue
                    q=p
                    while q*n<=N:
                        direct[p]=direct.get(p,F(0))+mu[q*n]**2+F(mu[n]**2-2*mu[q*n]*mu[n],q)
                        formula[p]=formula.get(p,F(0))+F(mu[n]**2,q)
                        q*=p
                    if p*n<=N and n%p:
                        formula[p]=formula.get(p,F(0))+F(2*mu[n]**2,p)
            check('native_source',direct=={p:a for p,a in formula.items() if a or p in direct},'all prime-power edge identity')
        previous=J
    # Tail variations with every normalization retained; ordinary indices, not squarefree-only.
    for Y in range(2,33):
        c={}
        for n in range(Y,2*Y):
            for j,dj in enumerate([1,-5,8,-4]):c[n*2**j]=F(dj*n,Y)
        check('tail_variations',sum(c.values())==0,'zero jet at 0')
        check('tail_variations',sum(a/F(n) for n,a in c.items())==0,'balance at 1')
        # Derivative cancellation: collect log(integer) as exact prime-log coefficients.
        derivative={}
        for n,a in c.items():
            for p,k in factor(n).items():derivative[p]=derivative.get(p,F(0))-a*k/n
        check('tail_variations',all(x==0 for x in derivative.values()),'derivative jet at 1')
        S=sum((a*a/n for n,a in c.items()),F(0))
        check('tail_variations',S==F(63*(3*Y-1),4*Y) and S<F(189,4),'complete coefficient norm')
        for x in (F(3*Y,2),F(7*Y,4),F(2*Y)-F(1,100)):
            A=sum((a*(x//n) for n,a in c.items()),F(0))
            check('tail_variations',A>=F(Y,2),'physical lower interval')
    return {'max_native_integer':Nmax,'pair_and_graph_panels':35,'tail_variations':31,
            'J_128':str(previous),'all_higher_prime_powers_retained':True}


def polynomial_matrix_controls():
    # Polynomial operations in ascending order, all exact.
    def mul(a,b):
        r=[F(0)]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):r[i+j]+=x*y
        return r
    def inner_exp(a,b,rate):return sum((v*factorial(i)/F(rate**(i+1)) for i,v in enumerate(mul(a,b))),F(0))
    phi=[F(1),F(-5,2),F(7,8),F(-1,16)]
    target=[F(0),F(1),F(-3,2),F(3,8)]
    check('finite_algebra',inner_exp(phi,phi,2)==F(385,2048),'pole-neutral input norm')
    check('finite_algebra',inner_exp(target,target,2)==F(29,512),'pole-neutral target norm')
    # State Lyapunov identity and positive definite Q by exact LDL.
    Q=[[F(v,2048) for v in row] for row in [[385,-639,324,-54],[-639,3518,-2882,660],[324,-2882,2536,-600],[-54,660,-600,144]]]
    A=[[F(-1 if i==j else 1 if i==j+1 else 0) for j in range(4)] for i in range(4)]
    C=[F(1),F(-5,2),F(7,4),F(-3,8)]
    for i in range(4):
        for j in range(4):check('finite_algebra',sum(A[k][i]*Q[k][j]+Q[i][k]*A[k][j] for k in range(4))==-C[i]*C[j],'exact Lyapunov identity')
    piv=[];L=[[F(int(i==j)) for j in range(4)] for i in range(4)]
    for i in range(4):
        d=Q[i][i]-sum(L[i][k]**2*piv[k] for k in range(i));need(d>0,'Q not positive');piv.append(d)
        for j in range(i+1,4):L[j][i]=(Q[j][i]-sum(L[j][k]*L[i][k]*piv[k] for k in range(i)))/d
    check('finite_algebra',piv==[F(385,2048),F(946109,788480),F(6400405,484407808),F(6561,3277007360)],'four advertised pivots')
    # Rank-one signed residue formula, including its unbalanced principal parts.
    # Formal polynomials store powers -3..2 in dictionaries.
    def pmul(a,b):
        d={}
        for i,x in a.items():
            for j,y in b.items():d[i+j]=d.get(i+j,F(0))+x*y
        return d
    for a,b,c,g,e,H0,H1,H2 in [(F(a),F(b),F(c),F(2,3),F(-1,7),F(3,5),F(-2),F(7,4)) for a,b,c in [(0,1,0),(1,-2,3),(2,3,-1),(-1,0,2)]]:
        zeta={-1:F(1),0:g,1:e};dzeta={-2:F(-1),0:e};p={0:a,1:b,2:c/2}
        lp=pmul(pmul(zeta,dzeta),pmul(p,p));linear=pmul(dzeta,p)
        for k,v in linear.items():lp[k]=lp.get(k,F(0))-2*v
        residue=H0*lp.get(-1,0)+H1*lp.get(-2,0)+H2/2*lp.get(-3,0)
        expected=-a*a*H2/2+(2*a-2*a*b-g*a*a)*H1+(2*b-b*b-a*c-2*g*a*b)*H0
        check('finite_algebra',residue==expected,'three-jet residue')
    for r in (1,2):
        for delta in (F(1,1000),F(1,100),F(1,3),F(1)):
            steps=(F(r,1)/delta).__ceil__();u=max(F(0),1-steps*delta/r)
            check('finite_algebra',u==0 and max(F(0),1-(steps-1)*delta/r)>0,'sparse-sign finite logical bootstrap')
    return {'lyapunov_pivots':[str(x) for x in piv]}


def scalar_certificates():
    logs={n:log_frac(F(n)) for n in (2,3,4,5,7,11,13,4096)};pi=pi_interval()
    harmonic=sum((F(1,n) for n in range(1,4097)),F(0))
    gamma=I(harmonic-logs[4096].hi-F(1,8192),harmonic-logs[4096].lo-F(1,8194))
    C0=F(47,64)-F(21,64)*(gamma+log_i(pi))+F(115,96)*logs[2]-F(641,1728)*logs[3]-F(65,192)*logs[5]
    inside('scalar_certificates',C0,0,F(237,5000))
    H=3*10**12
    RH=(log_i(H/(2*pi))+1)/(2*pi*H)+(40*log_frac(F(H+2))+10)/H**2
    check('scalar_certificates',RH.hi<F(37,25*10**12),'full zero-count tail bound')
    r=F(37,25*10**12)
    def margin(lo,hi):return F(1,4)-F(237,5000)-F(205,128*lo**5)-F(85,64)*r*(hi+2+F(1,hi))
    for lo,hi,target in [(2,4,F(1,10)),(4,5*10**10,F(1,10)),(2,16,F(1,200)),(16,10**11,F(1,200))]:
        check('scalar_certificates',margin(lo,hi)>target,'complete HT range endpoint budget')
    # Native m=2 signed integral, all prime powers (formal coefficients checked separately below).
    raw=F(35,128)*logs[2]+F(18343,124416)*logs[3]+F(3971,38400)*logs[5]+F(1251,25088)*logs[7]+F(2765,185856)*logs[11]+F(633,86528)*logs[13]-F(45,64)
    inside('scalar_certificates',raw,F(-17,500),F(-33,1000))
    def w(x):
        return x/3-1/(192*x*x) if F(1,4)<x<=1 else 1/(3*x*x)-x/192 if 1<x<4 else F(0)
    coeff={}
    for n in range(2,17):
        f=factor(n)
        if len(f)==1:
            p=next(iter(f));coeff[p]=coeff.get(p,F(0))+w(F(n,4))/2
    wanted={2:F(35,128),3:F(18343,124416),5:F(3971,38400),7:F(1251,25088),11:F(2765,185856),13:F(633,86528)}
    check('scalar_certificates',coeff==wanted,'actual m=2 full prime-power source')
    p2=(4-pi)/2*(1/logs[2]-1)
    inside('scalar_certificates',p2,F(189,1000),F(191,1000))
    # A distinct complete Y=4 period certificate, including every future period.
    t=(1-logs[2]/2-logs[3]/3)/logs[2]
    coeffs={1:I.make(1),2:I.make(-1),3:I.make(-1),4:4*t-2,8:-8*t+F(8,3)}
    p4=I.make(0);period=24;K=2048
    for residue in range(1,period+1):
        value=1-sum((a*(residue//n) for n,a in coeffs.items()),I.make(0))
        omega=I.make(0)
        for k in range(K):
            q=residue+k*period
            omega+=F(1,q*(q+1))
        omega=I(omega.lo,up(omega.hi+F(1,period*(residue+period*(K-1)))))
        p4+=value.sq()*omega
    inside('scalar_certificates',p4,F(57,1000),F(59,1000))
    # Actual three-impulse work; exp(-log(n/m)) is m/n exactly.
    def R_ratio(n,m):
        v=log_frac(F(n,m));return F(m,n)*(385-639*v+162*v.sq()-9*v.pow(3))/2048
    work3=-I.make(2).sqrt()*R_ratio(2,1)-2/I.make(3).sqrt()*R_ratio(3,1)+2/I.make(6).sqrt()*R_ratio(3,2)
    check('scalar_certificates',work3.lo>F(1,20),'actual work at N=3 is positive')
    return {'C0':enclosure(C0),'zero_count_tail_at_3e12':enclosure(RH),
            'signed_I_at_m2':enclosure(raw),'two_jet_p2_error':enclosure(p2),'two_jet_p4_error':enclosure(p4),
            'actual_work_N3':enclosure(work3),'gamma_interval':enclosure(gamma)}


def main():
    p=argparse.ArgumentParser();p.add_argument('--group',choices=['all','capacity','profile','native','algebra','scalars'],default='all');p.add_argument('--output',type=Path)
    args=p.parse_args();arithmetic_controls();result={}
    for label,fun in [('capacity',capacity),('profile',ant_profile),('native',native_and_jets),('algebra',polynomial_matrix_controls),('scalars',scalar_certificates)]:
        if args.group in ('all',label):result[label]=fun()
    report={'marker':'PASS_REVIEWER_EXACT_COMPONENT_CONTROLS','groups':result,'checks':COUNTS,
      'checks_total':sum(COUNTS.values()),'arithmetic_bits':BITS,'author_module_imported':False,
      'whole_package_replay':False,'infinite_arguments_machine_proved':False,
      'full_repository_checkout':False,'rh_proved':False}
    data=json.dumps(report,indent=2,sort_keys=True)+'\n'
    if args.output:args.output.write_text(data,encoding='utf-8')
    print(data)
if __name__=='__main__':main()
