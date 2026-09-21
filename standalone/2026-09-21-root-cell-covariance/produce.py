"""Full native sieve reconnaissance and rigorous endpoint-only energy bounds.
The gain certificate uses coarse endpoints and a proved worst-case loss,
not the measured within-cell error. Standard library, deterministic.
"""
from array import array
from fractions import Fraction
from hashlib import sha256
from math import isqrt
from pathlib import Path
import argparse
from core import *

STAGES=[3,7,15,31,63,127,255,511,1023,2047]
RESOLUTIONS=[1,2,4]

def sieve(n):
    prime=bytearray(b'\1')*(n+1);prime[0:2]=b'\0\0'
    for p in range(2,isqrt(n)+1):
        if prime[p]:prime[p*p:n+1:p]=b'\0'*((n-p*p)//p+1)
    mu=array('b',[1])*(n+1);mu[0]=0
    for p in range(2,n+1):
        if prime[p]:
            for k in range(p,n+1,p):mu[k]=-mu[k]
            for k in range(p*p,n+1,p*p):mu[k]=0
    return mu

class Tables:
    def __init__(self,mu, checkpoints, wanted=None):
        n=len(mu)-1;self.mu=mu
        if wanted is None:wanted=set(range(n+2))
        self.M={0:0};self.mlo={0:0};self.merr={0:0};self.hlo={0:0};self.herr={0:0}
        self.states={0:{'E':integer(0),'F':integer(0),'u':integer(0),'A':integer(0)}}
        ml=me=Elo=Ee=Flo=Fhi=M=hl=he=0
        for k in range(1,n+2):
            hl+=S//k;he+=int(S%k!=0)
            if k in wanted:self.hlo[k]=hl;self.herr[k]=he
            if k>n:continue
            M+=mu[k]
            if k in wanted:self.M[k]=M
            ml+=mu[k]*S//k;me+=int(mu[k]!=0 and S%k!=0)
            if k in wanted:self.mlo[k]=ml;self.merr[k]=me
            ep=M*M*S//(k*(k+1));Elo+=ep
            Ee+=int(M*M*S%(k*(k+1))!=0)
            ff=square((ml,ml+me));Flo+=ff[0];Fhi+=ff[1]
            if k in checkpoints:
                E=(Elo,Elo+Ee);F=(Flo,Fhi);u=sub((ml,ml+me),rat(M,k+1))
                A=add(E,scale(square(u),2*(k+1)))
                need(overlap(F,add(E,scale(square(u),k+1))),'innovation identity')
                self.states[k]={'E':E,'F':F,'u':u,'A':A}
    def m(self,k):return self.mlo[k],self.mlo[k]+self.merr[k]
    def H(self,k):return self.hlo[k],self.hlo[k]+self.herr[k]
    def endpoint(self,k):return {'M':int(self.M[k]),'m':list(self.m(k)),'H':list(self.H(k))}

def m_sum(s,t,at):
    # at(k) = (ordinary cumulative, reciprocal cumulative enclosure).
    Mt,mt=at(t);Mp,mp=at(s-1)
    return sub(sub(scale(mt,t+1),scale(mp,s)),integer(Mt-Mp))

def physical_mean(s,t,at):
    Mt,mt=at(t);Mp,mp=at(s-1)
    return add(sub(mt,mp),sub(rat(Mp,s),rat(Mt,t+1)))

def h_moments(n,H):
    return (sub(scale(H,n+1),integer(n)),
            add(sub(scale(square(H),n+1),scale(H,2*n+1)),integer(2*n)))

def losses(s,t,H):
    ell=t-s+1;W=rat(ell,s*(t+1))
    dh=sub(H(t+1),H(s))
    U_E=nonnegative(sub(sub(integer(ell),dh),divide(square(dh),W)))
    a,b=h_moments(t,H(t));c,d=h_moments(s-1,H(s-1))
    U_F=nonnegative(sub(sub(b,d),divint(square(sub(a,c)),ell)))
    return W,U_E,U_F

def clipped(Y,mu):
    c={k:Fraction(mu[k]) for k in range(1,Y+1) if mu[k]}
    r=sum((a/k for k,a in c.items()),Fraction());n=Y
    while r:
        n+=1;a=-min(Fraction(3),n*abs(r))*(1 if r>0 else -1)
        c[n]=a;r+=a/n
    need(n<=Y+(Y+1)//2,'completion support')
    total=rec=Fraction(0);ordinary=[Fraction(0)];recips=[Fraction(0)]
    for k in range(1,n+1):
        total+=c.get(k,Fraction(0));rec+=c.get(k,Fraction(0))/k
        ordinary.append(total);recips.append(rec)
    need(rec==0,'completed reciprocal moment')
    def at(k):
        return ordinary[min(k,n)],rat(recips[min(k,n)].numerator,recips[min(k,n)].denominator)
    # m_sum accepts integral cumulative; use separate exact Fraction formula below.
    return c,n,ordinary,recips

def c_m_sum(s,t,C):
    c,L,A,m=C
    val=(t+1)*m[min(t,L)]-s*m[min(s-1,L)]-(A[min(t,L)]-A[min(s-1,L)])
    return rat(val.numerator,val.denominator)

def stage(Y,T):
    b=Y+1;B=b*b-1;X=b*b;state=T.states
    at=lambda k:(int(T.M[k]),T.m(k))
    Eann=sub(state[B]['E'],state[Y]['E'])
    Fann=sub(state[B]['F'],state[Y]['F'])
    C=clipped(Y,T.mu);L=C[1]
    Qenergy=Fann
    for k in range(b,L):
        mc=rat(C[3][k].numerator,C[3][k].denominator)
        Qenergy=add(Qenergy,sub(scale(square(mc),4),scale(mul(mc,T.m(k)),4)))
    panels=[];endpoints=set()
    for resolution in RESOLUTIONS:
        coarseE=coarseF=coarseQ=UE=UF=UQ=integer(0);count=0
        for s,t in cells(b,B,resolution):
            endpoints.update([s-1,s,t,t+1]);count+=1
            W,ue,uf=losses(s,t,T.H)
            u=physical_mean(s,t,at);ms=m_sum(s,t,at);qs=sub(scale(c_m_sum(s,t,C),2),ms)
            coarseE=add(coarseE,divide(square(u),W))
            coarseF=add(coarseF,divint(square(ms),t-s+1))
            coarseQ=add(coarseQ,divint(square(qs),t-s+1))
            UE=add(UE,ue);UF=add(UF,uf);UQ=add(UQ,scale(uf,49 if s<=L else 1))
        remE=sub(Eann,coarseE);remF=sub(Fann,coarseF);remQ=sub(Qenergy,coarseQ)
        for rem,bound in [(remE,UE),(remF,UF),(remQ,UQ)]:
            need(rem[1]>=0 and rem[0]<=bound[1],'coarse variance/loss inequality')
        upper=add(add(state[Y]['E'],coarseE),add(UE,scale(square(state[B]['u']),2*X)))
        gain=(S+upper[1])**2*S<=4*(S+state[Y]['A'][0])**3
        panels.append({'resolution':resolution,'cells':count,'coarse_E':coarseE,'coarse_F':coarseF,'coarse_Q':coarseQ,
                       'remainder_E':remE,'remainder_F':remF,'remainder_Q':remQ,
                       'worst_E':UE,'worst_F':UF,'worst_Q':UQ,'completed_A_upper':upper,'certified_gain':gain})
    # Harmonics at B+1 needed; M,m do not. Avoid inventing an endpoint beyond the range.
    ep={str(k):T.endpoint(k) for k in sorted(endpoints) if k<=B}
    return {'Y':Y,'B':B,'completion_support':L,'input':state[Y],'output':state[B],
            'annular_E':Eann,'annular_F':Fann,'Q_energy':Qenergy,'panels':panels,'endpoints':ep,
            'H_after':list(T.H(B+1))}

def build(stages=STAGES):
    n=(max(stages)+1)**2-1
    checks=set(stages)|{(Y+1)**2-1 for Y in stages}
    mu=sieve(n);wanted=set(range((3*max(stages)+1)//2+2))|checks
    for Y in stages:
        for q in RESOLUTIONS:
            for a,b in cells(Y+1,(Y+1)**2-1,q):wanted.update([a-1,a,b,b+1])
    T=Tables(mu,checks,wanted)
    result={'schema':'RSC26-v1','bits':BITS,'stages':[stage(Y,T) for Y in stages],
            'max_endpoint':n,'coefficient_digest':sha256(bytes(x+1 for x in mu[1:])).hexdigest(),
            'status':'FINITE_CERTIFICATES_ONLY; uniform coarse-energy bound open'}
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',default='reports/native.json');p.add_argument('--small',action='store_true');a=p.parse_args()
    r=build(STAGES[:5] if a.small else STAGES);path=Path(a.write);path.parent.mkdir(parents=True,exist_ok=True);path.write_text(canonical(r)+'\n')
    for st in r['stages']:
        p=st['panels'][0]
        print(st['Y'],'cells',p['cells'],'A',show(st['output']['A']),'coarse upper',show(p['completed_A_upper']),
              'loss',show(p['worst_E']),'actual loss',show(p['remainder_E']),'gain',p['certified_gain'])
    print('SHA256',sha256(canonical(r).encode()).hexdigest())
