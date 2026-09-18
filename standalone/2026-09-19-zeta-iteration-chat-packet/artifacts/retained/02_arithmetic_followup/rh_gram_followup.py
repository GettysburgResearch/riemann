#!/usr/bin/env python3
"""Fast Vasyunin Gram evaluator and finite BSY-bound certificate.

G_mn=sum_{k>=1} {k/m}{k/n}/[k(k+1)], v_n=log(n)/n.
The analytically proved bound is D<=log((c^T G c)/(c^T v)^2)/2.
No RH assumption is made. Floating-point output is exploratory.
Certificates enclose fixed rational witnesses using mpmath.iv and exact integers,
and enclose the exact optimum using the proved bound G >= I/(6*N**3).

Put W(a,b)=sum_{r=1}^{b-1} ((a*r)%b)/b*cot(pi*r/b).
For g=gcd(m,n), a=m/g,b=n/g,
R_mn=((m-n)*log(n/m)-pi*g*(W(a,b)+W(b,a)))/(2*m*n).
G_mn=R_mn-R_m1/n-R_1n/m.
This follows by cancelling C=(log(2*pi)-gamma)/2 in Vasyunin's formula.
Reference: Darses--Hillion, arXiv:2004.10086 p.2.
Construction is O(N^3), memory O(N^2); no O(log N) claim per entry.

Dependencies: numpy, scipy, numba, threadpoolctl, mpmath.
Usage: python rh_gram_followup.py --max-n 2048 --cert-n 512 --out-dir results
"""
from __future__ import annotations
import argparse,json,math,time
from functools import lru_cache
from pathlib import Path
import numpy as np
import mpmath as mp
from numba import njit
from scipy.linalg import cho_factor,cho_solve
from threadpoolctl import threadpool_limits

@njit(cache=True)
def w_table(N):
    W=np.zeros((N+1,N+1))
    for b in range(2,N+1):
        half=(b-1)//2
        cot=np.empty(half)
        for r in range(1,half+1):cot[r-1]=1/math.tan(math.pi*r/b)
        for a in range(1,b//2+1):
            d=math.gcd(a,b)
            if d>1:value=d*W[b//d,a//d]
            else:
                value=0.;corr=0.
                for r in range(1,half+1):
                    term=(2*((a*r)%b)-b)*cot[r-1]/b
                    y=term-corr;t=value+y;corr=(t-value)-y;value=t
            W[b,a]=value;W[b,b-a]=-value
    return W

@njit(cache=True)
def r_float(m,n,W):
    d=math.gcd(m,n);a=m//d;b=n//d
    x=0. if b==1 else W[b,a%b]
    y=0. if a==1 else W[a,b%a]
    return ((m-n)*math.log(n/m)-math.pi*d*(x+y))/(2*m*n)

@njit(cache=True)
def gram(N,W):
    G=np.empty((N-1,N-1));edge=np.zeros(N+1)
    for n in range(2,N+1):edge[n]=r_float(1,n,W)
    for m in range(2,N+1):
        for n in range(m,N+1):
            g=r_float(m,n,W)-edge[m]/n-edge[n]/m
            G[m-2,n-2]=g;G[n-2,m-2]=g
    return G

def direct(m,n):
    from scipy.special import digamma
    p=math.lcm(m,n);r=np.arange(1,p+1,dtype=np.int64)
    return float(np.dot((r%m)/m*(r%n)/n,(digamma((r+1)/p)-digamma(r/p))/p))

def floor_binary(t):
    sign,man,exp,bc=t;man=int(man)
    if exp>=0:return (-1 if sign else 1)*(man<<exp)
    q,r=divmod(man,1<<(-exp))
    return -q-bool(r) if sign else q

def ceil_binary(t):
    sign,man,exp,bc=t
    return -floor_binary((1-sign,man,exp,bc)) if man else 0

class Certificate:
    def __init__(self,bits=100,dps=50):
        self.bits=bits;self.scale=1<<bits;mp.iv.dps=dps;self.calls=0
    @lru_cache(maxsize=None)
    def cots(self,n):
        out=[]
        for r in range(1,(n-1)//2+1):
            x=mp.iv.pi*r/n;y=mp.iv.cos(x)/mp.iv.sin(x)*self.scale
            out.append((floor_binary(y._mpi_[0]),ceil_binary(y._mpi_[1])))
            self.calls+=1
        return tuple(out)
    @lru_cache(maxsize=None)
    def wnum(self,a,b):
        if not a or b==1:return (0,0)
        if a>b//2:
            lo,hi=self.wnum(b-a,b);return (-hi,-lo)
        if math.gcd(a,b)!=1:raise ValueError('Expected coprime arguments')
        lo=0;hi=0
        for r,(cl,ch) in enumerate(self.cots(b),start=1):
            q=2*((a*r)%b)-b
            if q>=0:lo+=q*cl;hi+=q*ch
            else:lo+=q*ch;hi+=q*cl
        return lo,hi
    def w(self,a,b):
        if b==1:return mp.iv.mpf(0)
        lo,hi=self.wnum(a%b,b)
        return mp.iv.mpf([lo,hi])/(b*self.scale)
    def r(self,m,n):
        d=math.gcd(m,n);a=m//d;b=n//d
        return ((m-n)*mp.iv.log(mp.iv.mpf(n)/m)-mp.iv.pi*d*(self.w(a,b)+self.w(b,a)))/(2*m*n)
    def run(self,z,den):
        N=len(z)+1;c=[mp.iv.mpf(k)/den for k in z]
        edge=[mp.iv.mpf(0)]*(N+1)
        for n in range(2,N+1):edge[n]=self.r(1,n)
        Q=mp.iv.mpf(0)
        gc=[mp.iv.mpf(0) for _ in range(N-1)]
        for m in range(2,N+1):
            for n in range(m,N+1):
                g=self.r(m,n)-edge[m]/n-edge[n]/m
                Q+=(1 if m==n else 2)*c[m-2]*c[n-2]*g
                gc[m-2]+=g*c[n-2]
                if n!=m:gc[n-2]+=g*c[m-2]
        v=sum((c[n-2]*mp.iv.log(n)/n for n in range(2,N+1)),mp.iv.mpf(0))
        if not(Q.a>0 and v.a>0):raise ArithmeticError('Positivity not certified')
        U=mp.iv.log(Q/(v*v))/2
        grad2=sum(((mp.iv.log(n)/n-gc[n-2])**2 for n in range(2,N+1)),mp.iv.mpf(0))
        F=1-2*v+Q
        correction=6*N**3*grad2
        exact_E=mp.iv.mpf([(F-correction).a,F.b])
        safe=f'{math.ceil(float(U.b)*1e8)/1e8:.8f}'
        assert U.b<mp.iv.mpf(safe).a
        return dict(N=N,coefficient_denominator=den,coefficient_numerators=z,
          energy_interval=str(Q),evaluation_interval=str(v),witness_error_interval=str(1-2*v+Q),
          D_upper_bound_interval=str(U),proved_D_less_than=safe,
          exact_optimal_E_interval=str(exact_E),gradient_squared_interval=str(grad2),
          optimality_correction_upper=str(correction.b),eigenvalue_lower_bound=f'1/{6*N**3}',
          cot_fixed_point_bits=self.bits,interval_decimal_digits=mp.iv.dps,cotangent_calls=self.calls,
          status='Finite rational-witness bound plus certified optimum enclosure via G >= I/(6*N^3); not RH')

def run(N,certN,out):
    if N<2 or certN<0 or certN>N:raise ValueError('Invalid sizes')
    out.mkdir(parents=True,exist_ok=True);t=time.monotonic()
    W=w_table(N);G=gram(N,W);seconds=time.monotonic()-t
    tests=[];rng=np.random.default_rng(713)
    pairs=[(2,2),(2,3),(3,3),(5,17),(7,14),(20,20)]+[tuple(map(int,rng.integers(2,min(N,100)+1,size=2))) for _ in range(15)]
    for m,n in pairs:
        if max(m,n)>N:continue
        err=abs(G[m-2,n-2]-direct(m,n))
        tests.append(dict(m=m,n=n,abs_error=err))
        if err>2e-13:raise ArithmeticError(f'Failed independent check: {(m,n,err)}')
    sizes=sorted(set([n for n in [20,40,80,128,200,256,512,1024,2048,4096] if n<=N]+[N]+([certN] if certN else [])))
    rows=[];solutions={}
    with threadpool_limits(limits=2):
        for n in sizes:
            ix=np.arange(2,n+1);v=np.log(ix)/ix
            c=cho_solve(cho_factor(G[:n-1,:n-1],lower=True),v);E=1-float(v@c)
            if E<=0:raise ArithmeticError('Invalid float distance')
            row=dict(N=n,E_approx=E,E_logN_approx=E*math.log(n),U_approx=-.5*math.log1p(-E),l1_coeff_approx=float(np.abs(c).sum()),max_abs_coeff_approx=float(np.abs(c).max()),certified=False)
            rows.append(row);solutions[n]=c;print(json.dumps(row),flush=True)
    schur=[]
    with threadpool_limits(limits=2):
        for n in [n for n in sizes if 2*n in solutions]:
            A=G[:n-1,:n-1];B=G[:n-1,n-1:2*n-1];C=G[n-1:2*n-1,n-1:2*n-1]
            S=C-B.T@cho_solve(cho_factor(A,lower=True),B)
            ix=np.arange(n+1,2*n+1);r=np.log(ix)/ix-B.T@solutions[n]
            gain=float(r@cho_solve(cho_factor(S,lower=True),r))
            e=next(x['E_approx'] for x in rows if x['N']==n);e2=next(x['E_approx'] for x in rows if x['N']==2*n)
            schur.append(dict(N=n,gain=gain,error_difference=e-e2,relative_difference=abs(gain-(e-e2))/gain,scale_ratio=(1+math.log(n))*gain/e**2))
    result=dict(algorithm='Paired Vasyunin sums: O(N^3) construction, O(N^2) memory',construction_seconds=seconds,benchmark_constant=float(2+mp.euler-mp.log(4*mp.pi)),table=rows,cross_checks=tests,schur_checks=schur)
    (out/'exploration.json').write_text(json.dumps(result,indent=2)+'\n')
    if certN:
        den=10**12;z=[int(round(float(x)*den)) for x in solutions[certN]]
        start=time.monotonic();cert=Certificate().run(z,den);cert['seconds']=time.monotonic()-start
        (out/f'certificate_N{certN}.json').write_text(json.dumps(cert,indent=2)+'\n')
        print('CERTIFIED',cert['proved_D_less_than'],cert['seconds'],flush=True)
    print('TOTAL',time.monotonic()-t,flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--max-n',type=int,default=1024);p.add_argument('--cert-n',type=int,default=256);p.add_argument('--out-dir',type=Path,default=Path('results'))
    a=p.parse_args();run(a.max_n,a.cert_n,a.out_dir)
