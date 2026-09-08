#!/usr/bin/env python3
"""Independent pass-three bounded checks. No repository producer is imported.

This is not a proof of the unbounded analytic assertions or a package replay.
All accepting arithmetic is Fraction/integer arithmetic. Interval endpoints
are rounded outwards to a fixed dyadic grid after every operation.
"""
from __future__ import annotations
from fractions import Fraction as F
from dataclasses import dataclass
from itertools import combinations
from math import isqrt
import json

BITS=180
DEN=1<<BITS
counts={}
def check(group, cond):
    counts[group]=counts.get(group,0)+1
    if not cond: raise ValueError('failed independent check: '+group)

def down(x): return F((x.numerator*DEN)//x.denominator,DEN)
def up(x): return F(-((-x.numerator*DEN)//x.denominator),DEN)
@dataclass(frozen=True)
class I:
    lo:F
    hi:F
    @staticmethod
    def point(x):
        q=F(x);return I(down(q),up(q))
    def __add__(self,o):
        o=iv(o);return I(down(self.lo+o.lo),up(self.hi+o.hi))
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,o): return self+-iv(o)
    def __rsub__(self,o):return iv(o)+-self
    def __mul__(self,o):
        o=iv(o);v=[a*b for a in (self.lo,self.hi) for b in (o.lo,o.hi)]
        return I(down(min(v)),up(max(v)))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=iv(o)
        if o.lo<=0<=o.hi:raise ValueError('zero interval divisor')
        return self*I(down(1/o.hi),up(1/o.lo))
    def __rtruediv__(self,o):return iv(o)/self
    def square(self):
        a=0 if self.lo<=0<=self.hi else min(self.lo*self.lo,self.hi*self.hi)
        return I(down(a),up(max(self.lo*self.lo,self.hi*self.hi)))
def iv(x):return x if isinstance(x,I) else I.point(x)

def log_unit(q):
    q=F(q);z=(q-1)/(q+1)
    if not 0<=z<=F(1,3):raise ValueError('log reduction')
    s=F(0);power=z
    for k in range(100):s+=2*power/(2*k+1);power*=z*z
    rem=2*power/(201*(1-z*z))
    return I(down(s),up(s+rem))
LOG2=log_unit(F(2))
def lograt(q):
    q=F(q)
    if q<=0:raise ValueError('nonpositive log')
    k=0
    while q>=2:q/=2;k+=1
    while q<1:q*=2;k-=1
    return log_unit(q)+k*LOG2

def sqrt_interval(q):
    q=F(q)
    if q<0:raise ValueError('sqrt negative')
    scaled=q.numerator*DEN*DEN//q.denominator
    n=isqrt(scaled)
    return I(F(n,DEN),F(n if F(n*n,DEN*DEN)==q else n+1,DEN))

def decimals(x,places=16):
    n=10**places
    def fmt(k):return ('-' if k<0 else '')+str(abs(k)//n)+'.'+str(abs(k)%n).zfill(places)
    return [fmt(x.lo.numerator*n//x.lo.denominator),fmt(-((-x.hi.numerator*n)//x.hi.denominator))]

def mobius(n):
    q=n;p=2;sign=1
    while p*p<=q:
        if q%p==0:
            q//=p;sign=-sign
            if q%p==0:return 0
        p+=1
    return -sign if q>1 else sign

def prime_base(n):
    for p in range(2,isqrt(n)+1):
        if n%p==0:
            q=n
            while q%p==0:q//=p
            return p if q==1 else None
    return n if n>=2 else None

def ant_constant():
    # Integrate the independently derived floor-profile on EVERY unit cell.
    T=4096;h=[I.point(0)]
    for k in range(1,T+1):h.append(h[-1]+F(1,k*k))
    total=I.point(0);d=[1,-5,8,-4]
    for r in range(1,T):
        a=I.point(0);b=F(0)
        for j in range(4):
            U=r//(1<<j);L=r//(1<<(j+1))
            a+=d[j]*(h[U]-h[L])/F(2*(4**j))
            b+=d[j]*(2*L-F(U,2))
        term=a.square()*F(3*r*r+3*r+1,3)+2*a*b+F(b*b,r*(r+1))
        # Rounding can give a tiny negative lower bound on a near-zero cell.
        total+=I(max(F(0),term.lo),term.hi)
        check('ANT full rational profile cells',term.hi>=0)
    total=I(total.lo,total.hi+F(10000,3*T**3))
    check('ANT printed continuum constant',total.lo>F('1.704219450036') and total.hi<F('1.704219498544'))
    # Validate the cell formula against a separate exact integral of H at points.
    def H(t):
        # floor(t/v)=sum_{k<=t} 1_{v<=t/k}, integrate v on [1,2].
        return sum((min(F(2),t/k)**2-1)/2 for k in range(1,t.numerator//t.denominator+1))
    for r in range(1,65):
        t=F(2*r+1,2)
        actual=sum(d[j]*H(t/(1<<j)) for j in range(4))
        a=F(0);b=F(0)
        for j in range(4):
            U=r//(1<<j);L=r//(1<<(j+1))
            a+=F(d[j],2*4**j)*sum(F(1,k*k) for k in range(L+1,U+1))
            b+=d[j]*(2*L-F(U,2))
        check('ANT independent layer-cake profile',actual==a*t*t+b)
    return {'interval':decimals(total),'unit_cells':T-1,'tail_bound':str(F(10000,3*T**3))}

def capacities():
    primes=[2,3,5,7,11,13];logs={p:lograt(p) for p in primes};ans={}
    advertised={'sf':('1.18532285971072','1.18532285971074','1.91594153472685','1.91594153472687'),
                'geo':('1.82250119177775','1.82250119177777','2.37221708831717','2.37221708831720')}
    for kind in ('sf','geo'):
        terms=[]
        for mask in range(1,1<<len(primes)):
            b=F(1);lam=I.point(0)
            for j,p in enumerate(primes):
                if mask>>j&1:
                    b*=F(1,p if kind=='sf' else p-1)
                    lam+=logs[p]*F(p+1,p) if kind=='sf' else logs[p]*F(p,p-1)
            terms.append((b,lam))
            check('capacity positive visible mode',b>0 and lam.lo>0)
        K=sum((b/lam for b,lam in terms),I.point(0))
        klo,khi,alo,ahi=map(F,advertised[kind]);check('capacity printed contrast',K.lo>klo and K.hi<khi)
        def residual(c):return sum((b/(c*lam-1) for b,lam in terms),I.point(-1))
        # Direct outward sign checks at the advertised endpoints suffice;
        # no floating eigenvalue or floating root finder is an accepting input.
        rl,rh=residual(alo),residual(ahi)
        check('capacity secular endpoint signs',rl.lo>0 and rh.hi<0)
        ans[kind]={'contrast':decimals(K),'anchored_bracket':[str(alo),str(ahi)],'visible_modes':len(terms),
                   'left_residual':decimals(rl,22),'right_residual':decimals(rh,22)}
    # Reconstruct actual squarefree graph at rational rates, independently
    # checking unnormalised orthogonal eigenvectors (avoids irrational sqrt).
    ps=[2,3,5];rates={2:F(3,2),3:F(7,3),5:F(11,5)}
    vertices=[1]
    for p in ps:vertices += [p*n for n in list(vertices)]
    vertices.sort();Z=sum(F(1,n) for n in vertices)
    vec=[]
    for mask in range(8):
        f={n:F(1) for n in vertices};lam=F(0)
        for j,p in enumerate(ps):
            if mask>>j&1:
                lam+=rates[p]*F(p+1,p)
                for n in vertices:f[n]*=1 if n%p==0 else -F(1,p)
        for n in vertices:
            L=sum((rates[p]*(f[n]-f[n//p]) if n%p==0 else rates[p]/p*(f[n]-f[n*p])) for p in ps)
            check('capacity graph eigenvectors',L==lam*f[n])
        for g in vec:check('capacity graph orthogonality',sum(f[n]*g[n]/n for n in vertices)==0)
        vec.append(f)
    return ans

def ant_native_jets():
    for Y in range(2,65):
        # q_Y has coefficients d_j n/Y at 2^j n; derivative at 1 cancels
        # separately for log n and log 2, i.e. without numeric logarithms.
        d=[1,-5,8,-4];q={}
        for j in range(4):
            for n in range(Y,2*Y):q[(1<<j)*n]=F(d[j]*n,Y)
        check('ANT balanced jet',sum(v/n for n,v in q.items())==0)
        check('ANT centered jet',sum(q.values())==0)
        check('ANT derivative jet log2',sum(F(j*d[j],1<<j) for j in range(4))==0)
        S=sum(v*v/n for n,v in q.items())
        check('ANT exact coefficient norm',S==F(3*Y-1,2*Y)*F(63,2))
        # On [3Y/2,2Y), integrate an explicit lower constant.
        x=F(3*Y,2);val=sum(v*(x//n) for n,v in q.items())
        check('ANT full-prefix obstruction interval',val>=F(Y,2))
    return {'integer_horizons':63,'all_three_zero_jet_constraints':True}

def coherent_source():
    mu=[0]+[mobius(n) for n in range(1,129)];M=[0]
    for n in range(1,129):M.append(M[-1]+mu[n])
    last=F(0);pair=F(0)
    for N in range(1,129):
        pair+=F(mu[N]**2+2*mu[N]*M[N-1],N)
        cell=sum(F(M[k]**2,k*(k+1)) for k in range(1,N))+F(M[N]**2,N)
        check('CCS entire future norm',pair==cell)
        check('CCS signed work increment',cell-last==F(mu[N]**2+2*mu[N]*M[N-1],N));last=cell
        # Separate symbolic log-prime coefficients in two independent expansions.
        direct={};formula={}
        for q in range(2,N+1):
            p=prime_base(q)
            if p is None:continue
            for j in range(1,N//q+1):
                direct[p]=direct.get(p,F(0))+mu[q*j]**2+F(mu[j]**2-2*mu[q*j]*mu[j],q)
                formula[p]=formula.get(p,F(0))+mu[q*j]**2+F(mu[j]**2,q)
                if q==p and j%p:formula[p]+=F(2*mu[j]**2,p)
        check('CCS full prime-power graph identity',direct==formula)
    return {'horizons':128,'last_full_norm':str(last),'filters':'exponential; NOT cubic MWR filter'}

def annular_budgets():
    logs={p:lograt(p) for p in [2,3,5,7,11,13]}
    weights={2:F(35,128),3:F(18343,124416),5:F(3971,38400),7:F(1251,25088),11:F(2765,185856),13:F(633,86528)}
    printed=sum((c*logs[p] for p,c in weights.items()),I.point(-F(45,64)))
    def w(u):
        if not F(1,4)<u<4:return F(0)
        return u/3-F(1,192)/u**2 if u<=1 else F(1,3)/u**2-u/192
    direct=I.point(-F(45,64))
    for n in range(2,17):
        p=prime_base(n)
        if p:direct+=logs[p]*w(F(n,4))/2
    check('CR actual signed negative scalar',direct.lo>-F(17,500) and direct.hi<-F(33,1000))
    check('CR source versus printed overlap',max(direct.lo,printed.lo)<=min(direct.hi,printed.hi))
    check('CR weaker native sign survives',direct.lo+F(1,4)>0)
    # Exact rational continuum budgets, conditional on the separately
    # reviewed C0 and complete height-tail enclosures in the paper.
    R0=F(37,25*10**12);budgets=[]
    for split,upper,margin in [(4,5*10**10,F(1,10)),(16,10**11,F(1,200))]:
        for a,b in [(2,split),(split,upper)]:
            lower=F(1,4)-F(237,5000)-F(205,128*a**5)-F(85,64)*R0*(b+2+F(1,b))
            check('HT exact continuum endpoint budgets',lower>margin)
            budgets.append({'a':a,'b':b,'lower':str(lower),'required':str(margin)})
    return {'signed_m2':decimals(direct),'continuum_budgets':budgets}

def work_storage():
    Q=[[F(x,2048) for x in row] for row in [[385,-639,324,-54],[-639,3518,-2882,660],[324,-2882,2536,-600],[-54,660,-600,144]]]
    A=[[F(-1 if i==j else 1 if i==j+1 else 0) for j in range(4)] for i in range(4)]
    C=[F(1),-F(5,2),F(7,4),-F(3,8)]
    for i in range(4):
        for j in range(4):check('MWR exact Lyapunov storage',sum(A[k][i]*Q[k][j]+Q[i][k]*A[k][j] for k in range(4))==-C[i]*C[j])
    L=[[F(int(i==j)) for j in range(4)] for i in range(4)];ds=[]
    for i in range(4):
        d=Q[i][i]-sum(L[i][k]**2*ds[k] for k in range(i));ds.append(d)
        check('MWR positive storage pivots',d>0)
        for j in range(i+1,4):L[j][i]=(Q[j][i]-sum(L[j][k]*L[i][k]*ds[k] for k in range(i)))/d
    # R(log r)=r^-1 polynomial(log r)/2048; sqrt only in impulse normalisation.
    def corr(r):
        v=lograt(r);return (385-639*v+162*v.square()-9*v.square()*v)/(2048*F(r))
    W=-sqrt_interval(2)*corr(2)-2/sqrt_interval(3)*corr(3)+2/sqrt_interval(6)*corr(F(3,2))
    check('MWR actual N3 counterexample',W.lo>F(1,20))
    return {'pivots':[str(d) for d in ds],'W3':decimals(W)}

def pi_interval():
    def atan_inverse(q):
        x=F(1,q);t=x;total=F(0)
        for k in range(120):
            total+=(-1 if k%2 else 1)*t/(2*k+1);t*=x*x
        # Even number of terms: partial sum is below the true value.
        return I(down(total),up(total+t/241))
    return 16*atan_inverse(5)-4*atan_inverse(239)

def height_primitives():
    pi=pi_interval()
    lp=I(lograt(pi.lo).lo,lograt(pi.hi).hi)
    n=1024;hn=sum((F(1,k) for k in range(1,n+1)),F(0))
    gam=I((iv(hn)-lograt(n)-F(1,2*n)).lo,
          (iv(hn)-lograt(n)-F(1,2*n+1)).hi)
    c0=F(47,64)-F(21,64)*(gam+lp)+F(115,96)*LOG2-F(641,1728)*lograt(3)-F(65,192)*lograt(5)
    check('HT primitive C0 bound',c0.lo>F(1,25) and c0.hi<F(237,5000))
    H=3*10**12
    logarg=iv(H)/(2*pi)
    logh=I(lograt(logarg.lo).lo,lograt(logarg.hi).hi)
    tail=(logh+1)/(2*pi*H)+(40*lograt(H+2)+10)/(H*H)
    check('HT complete analytic tail constant',tail.hi<F(37,25*10**12))
    check('HT gamma strict primitive order',gam.lo<gam.hi and 0<gam.lo<gam.hi<1)
    return {'C0':decimals(c0,14),'height_tail_bound':decimals(tail,25),
            'height':H,'external_height_theorem':'Platt-Trudgian arXiv:2004.09765v1; imported, not replayed',
            'zero_count_remainder':'paper argument reviewed, not numerically proving the infinite estimate'}

def divisor_family_controls():
    def phi(n):return sum(__import__('math').gcd(j,n)==1 for j in range(1,n+1))
    def j2(n):return sum(mobius(d)*(n//d)**2 for d in range(1,n+1) if n%d==0)
    def fracpart(n,k):return F(n%k,k)
    # Vasyunin finite-support duals against the literal step dictionary.
    for q in range(2,33):
        f={}
        for d in range(1,q+1):
            if q%d:continue
            a=mobius(q//d)
            if d>1:f[d-1]=f.get(d-1,0)+a*d*(d-1)
            f[d]=f.get(d,0)-a*d*(d+1)
        for k in range(2,33):
            pairing=sum(F(v,n*(n+1))*fracpart(n,k) for n,v in f.items())
            check('DO exact biorthogonal controls',pairing==int(k==q))
        check('DO exact target dual pairing',sum(F(v,n*(n+1)) for n,v in f.items())==-mobius(q))
    result={}
    for M in (3,4,8,16,32):
        odd=list(range(1,M+1,2));js={d:j2(d) for d in odd}
        SS=sum(F(mobius(d)**2,js[d]) for d in odd)
        AA=sum(F(mobius(d)*phi(d),js[d]) for d in odd)
        DD=sum(F(phi(d)**2,js[d]) for d in odd);KK=SS*DD-AA*AA
        check('BL positive constraint determinant',KK>0)
        v={k:k*k*sum(F(mobius(d//k)*mobius(d),js[d]) for d in odd if d%k==0) for k in odd}
        w={k:k*k*sum(F(mobius(d//k)*phi(d),js[d]) for d in odd if d%k==0) for k in odd}
        lam={k:(DD*v[k]-AA*w[k])/KK for k in odd}
        check('BL exact first constraint',lam[1]==1)
        check('BL exact balance',sum(lam[k]/k for k in odd)==0)
        for k in odd:
            check('BG Jordan incidence factorization',all(sum(js[d] for d in odd if k%d==0 and l%d==0)==__import__('math').gcd(k,l)**2 for l in odd))
            rv=sum(F(__import__('math').gcd(k,l)**2,k*k*l*l)*lam[l] for l in odd)
            check('BL rational KKT normal equation',rv==(DD*int(k==1)-AA/F(k))/KK)
        if M==16:check('BL nonsquarefree coordinate',lam[9]==-F(20880,57769))
        result[str(M)]={str(k):str(a) for k,a in lam.items()}
    return {'dual_q_and_k_range':[2,32],'balanced_rational_sources':result}

def terminal_hyperbola_controls():
    mu={k:mobius(k) for k in range(1,4914)}
    def mo(x):return sum(mu[k] for k in range(1,int(x)+1,2))
    def mho(x):return sum((F(mu[k],k) for k in range(1,int(x)+1,2)),F(0))
    def Q(x):return mo(x)-F(x)*mho(x)
    def W(x):return sum((F(x,k)-1 for k in range(1,int(x)+1,2)),F(0))
    rows=[]
    for Y in (3,5,9,17):
        lam={k:F(mu[k])-(Y*mho(Y) if k==Y else 0) for k in range(1,Y+1,2)}
        check('TE terminal normalization',lam[1]==1 and sum(a/k for k,a in lam.items())==0)
        for n in range(1,129):
            literal=sum(a*(n//k-n//(2*k)) for k,a in lam.items())
            continuation=1+(n//Y-n//(2*Y))*Q(Y)-sum(mo(F(n,j)) for j in range(1,n//Y+1,2))
            check('TE full arithmetic continuation',literal==continuation)
            if n<Y:check('TE exact native horizon',literal==1)
        quad=sum(a*b*W(F(Y*Y,k*l)) for k,a in lam.items() for l,b in lam.items())
        check('BH exact balanced quadratic',Q(Y*Y)==2*Q(Y)+quad)
        check('BH zero weighted endpoint',1-F(Y*Y,Y*Y)==0)
        rows.append({'Y':Y,'B':str(quad),'Q_Y2':str(Q(Y*Y))})
    for L in range(1,9):
        Y=200*L+1
        for kind,(lo,hi) in enumerate(((110,130),(150,180))):
            c={lo*L+2*r+1:F(lo*L+2*r+1,Y) for r in range(L)}
            c.update({hi*L+2*r+1:-F(hi*L+2*r+1,Y) for r in range(L)})
            check('BH hostile source exact balance',sum(a/k for k,a in c.items())==0)
            quad=sum(a*b*W(F(Y*Y,k*l)) for k,a in c.items() for l,b in c.items())
            expected=F(L*L,3)-F(12721*L**4,Y**2) if kind==0 else -F(900*L**4,Y**2)
            check('BH both signed quadratic countermodels',quad==expected and ((quad>0) if kind==0 else (quad<0)))
    return {'terminal_rows':rows,'countermodel_L_range':[1,8],
            'unbounded_countermodels':'polynomial proof reviewed separately from these finite checks'}

def main():
    ans={'schema':'riemann.review.pass3.independent-bounded-checks.v1',
         'ANT_constant':ant_constant(),'capacities':capacities(),
         'ANT_jets':ant_native_jets(),'coherent_source':coherent_source(),
         'annular':annular_budgets(),'work_storage':work_storage(),
         'height_primitives':height_primitives(),'divisor_family':divisor_family_controls(),
         'terminal_hyperbola':terminal_hyperbola_controls()}
    ans.update(marker='PASS_INDEPENDENT_BOUNDED_PASS3_CHECKS',groups=counts,assertions=sum(counts.values()),
               author_packages_replayed=False,full_checkout=False,unbounded_analysis_machine_proved=False,
               lean_build=False,rh_proved=False)
    print(json.dumps(ans,sort_keys=True,indent=2))
if __name__=='__main__':main()
