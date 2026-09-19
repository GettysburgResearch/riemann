from fractions import Fraction as F
from math import isqrt, log
import numpy as np

def sieve(n):
    mu=[1]*(n+1); mu[0]=0; primes=[]; comp=[False]*(n+1)
    for i in range(2,n+1):
        if not comp[i]: primes.append(i);mu[i]=-1
        for p in primes:
            if i*p>n: break
            comp[i*p]=True
            if i%p==0: mu[i*p]=0;break
            mu[i*p]=-mu[i]
    return mu,primes

def complete(a):
    y=len(a)-1; m=sum((F(a[n],n) for n in range(1,y+1)),F(0))
    c={n:F(a[n]) for n in range(1,y+1) if a[n]}
    r=abs(m); s=1 if m>0 else -1
    n=y
    while r:
        n+=1; h=min(F(3),n*r);c[n]=-s*h; r-=h/n
    return c

def coalesce(c):
    z={}
    for r,u in c.items():
        for s,v in c.items(): z[r*s]=z.get(r*s,F(0))+u*v
    return {d:v for d,v in z.items() if v}

def core(d,bank):
    a=1;p=2
    while p*p<=d:
        e=0
        while d%p==0:d//=p;e^=1
        if e and p not in bank:a*=p
        p+=1
    if d>1 and d not in bank:a*=d
    return a

def panel(y,bank,kind='native'):
    B=(y+1)**2-1;mu,pr=sieve(max(B,2*y))
    a=mu[:y+1] if kind=='native' else [0]+[1]+[0]*(y-1)
    c=complete(a);z=coalesce(c)
    k=np.arange(y+1,B+1);H=np.r_[0.,np.cumsum(1/np.arange(1,B+1))]
    groups={};diag=0.;Q=np.zeros(len(k))
    for d,val in z.items():
        term=float(val)*(H[k//d]-H[k]+log(d))/d
        a=core(d,bank)
        if a not in groups:groups[a]=np.zeros(len(k))
        groups[a]+=term;diag+=term@term;Q+=term
    D=sum(v@v for v in groups.values());N=Q@Q
    mc=np.zeros(B+1)
    for n,v in c.items():mc[n:]+=float(v)/n
    q=2*mc[y+1:]-Q
    direct=np.cumsum(np.array(mu[1:],float)/np.arange(1,len(mu)))
    Fy=mc[1:y+1]@mc[1:y+1]
    I=direct[y:B]@direct[y:B]
    return {'Y':y,'B':B,'kind':kind,'bank':sorted(bank),'L':max(c),'products':len(z),'groups':len(groups),'source_input_energy':float(Fy),'native_reference_annulus':float(I), 'actual_output_annulus':float(q@q),'norm_Q':float(N),'diagonal':float(diag),'within_class_off_diagonal':float(D-diag),'rough_cross':float(N-D),'sum_class_energies':float(D),'collar_norm':float(mc[y+1:]@mc[y+1:]),'q_native_maxerror':float(np.max(np.abs(q-direct[y:B]))) if kind=='native' else None}
if __name__=='__main__':
    import json
    out=[]
    for y in [5,15,31,63,95,127]:
        for bank in [set(),{2,3},{2,3,5,7}]:
            q=panel(y,bank);out.append(q);print(q,flush=True)
    for y in [15,31,63]:
        q=panel(y,{2,3},'fake');out.append(q);print(q,flush=True)
    open(__import__('pathlib').Path(__file__).with_name('scout.json'),'w').write(json.dumps(out,indent=2)+'\n')
