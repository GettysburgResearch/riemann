#!/usr/bin/env python3
"""Exact finite diagnostics only; does not certify the MRT input or asymptotics."""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as Q
import hashlib
import json

Z = (Q(0), Q(0)); ONE = (Q(1), Q(0))
COUNTS: Counter[str] = Counter()
MUTATION = ''

def need(ok: bool, label: str) -> None:
    COUNTS[label] += 1
    if not ok:
        raise ArithmeticError(label)

def add(z, w): return (z[0]+w[0], z[1]+w[1])
def mul(z, w): return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])
def cj(z): return (z[0], -z[1])
def sc(z, a): return (z[0]*a, z[1]*a)
def norm(z): return z[0]*z[0]+z[1]*z[1]
def ipow(k): return (ONE,(Q(0),Q(1)),(-Q(1),Q(0)),(Q(0),-Q(1)))[k%4]

def factors(n: int) -> dict[int,int]:
    out = {}; p=2
    while p*p<=n:
        while n%p==0:
            out[p]=out.get(p,0)+1; n//=p
        p+=1
    if n>1: out[n]=out.get(n,0)+1
    return out

def mob(n: int) -> int:
    f=factors(n)
    return 0 if any(e>1 for e in f.values()) else (-1)**len(f)

def rad(n: int) -> int:
    r=1
    for p in factors(n): r*=p
    return r

def v(n: int):
    z=Q(1)
    for p in factors(n): z*=Q(p-1,p)
    return z

def xi(n: int, twist: bool) -> int:
    return (0 if n%2==0 else (1 if n%4==1 else -1)) if twist else 1

def phase(n: int, profile: int):
    return ipow(sum((profile*(p%4+1)//2)*e for p,e in factors(n).items()))

def coprime(n: int, mask: int) -> bool:
    import math
    return math.gcd(n, mask)==1

def local(fam,p,e,m,profile,mask,twist):
    if e==0: return ONE
    if mask%p==0 and MUTATION!='mask': return Z
    a=xi(p,twist); zz=phase(p,profile)
    # Odd-degree fixtures use z_p=phase/sqrt(p), an allowed attenuated profile.
    power=(m-2)//2
    h=p**power
    if MUTATION=='power': h*=p
    if fam=='native': return (Q(-a),Q(0)) if e==1 else Z
    if fam=='coupled':
        if e==1: return (Q(-(p-1)*a,p),Q(0))
        return sc(zz,-h) if e==m else Z
    if fam=='two-channel':
        if e==1:return (Q(-a),Q(0))
        if e==m:return sc(zz,-h)
        if e==m+1:return sc(zz,h*a)
        return Z
    if fam=='geometric':
        if (e-1)%m:return Z
        j=(e-1)//m
        return sc(phase(p**j,profile), -Q(p-1,p)*a*h**j)
    raise ValueError(fam)

def direct(cap,fam,m,profile,mask,twist):
    out=[Z]*(cap+1);out[1]=ONE
    for n in range(2,cap+1):
        z=ONE
        for p,e in factors(n).items():z=mul(z,local(fam,p,e,m,profile,mask,twist))
        out[n]=z
    return out

def component_data(d,fam,m,profile,mask,twist):
    if not coprime(d,mask): return None
    if fam=='native': return (1,ONE,False,mask) if d==1 else None
    power=(m-2)//2
    if fam in ('coupled','two-channel'):
        if not mob(d):return None
        return (d**m, sc(phase(d,profile),mob(d)*d**power), fam=='coupled',
                mask*d if fam=='coupled' else mask)
    rr=rad(d)
    t=d**m*rr
    if MUTATION=='geometric':t=d**m
    gam=sc(phase(d,profile),mob(rr)*xi(rr,twist)*v(rr)*d**power)
    return (t,gam,True,mask*d)

def components(cap,fam,m,profile,mask,twist):
    out=[Z]*(cap+1); labels=[0]*(cap+1); occupancy=[0]*(cap+1)
    for d in range(1,cap+1):
        if fam!='native' and d**m>cap:break
        data=component_data(d,fam,m,profile,mask,twist)
        if data is None:continue
        t,gamma,atten,maskd=data
        for r in range(1,cap//t+1):
            if not coprime(r,maskd):continue
            a=Q(mob(r)*xi(r,twist))*(v(r) if atten else 1)
            if not a:continue
            n=t*r;out[n]=add(out[n],sc(gamma,a));labels[n]=d;occupancy[n]+=1
    need(max(occupancy)<=1,'unique_component_support')
    return out, labels

def coefficient_tests(cap):
    reports=[]
    for fam in ('native','coupled','two-channel','geometric'):
      for m in ((2,) if fam=='native' else (2,3,4,6,10)):
       for mask in (1,6):
        for profile in (0,1):
          twist=mask==6 and profile==1
          a=direct(cap,fam,m,profile,mask,twist)
          b,labels=components(cap,fam,m,profile,mask,twist)
          pref=Q(0); tails={r:Q(0) for r in (1,2,3,5)}
          for n in range(1,cap+1):
            need(a[n]==b[n],'complete_source_coefficient')
            if not coprime(n,mask):need(a[n]==Z,'literal_nonunit_zero')
            pref+=norm(a[n]);need(pref<=2*n,'square_prefix_guard')
            for r in tails:
              if labels[n]>r:tails[r]+=norm(a[n])
              need(r*tails[r]<=n,'power_tail_guard')
          digest=hashlib.sha256(repr(a).encode()).hexdigest()
          reports.append(dict(family=fam,m=m,mask=mask,profile=profile,twist=twist,
                              cap=cap,supported=sum(z!=Z for z in a),sha256=digest))
    # Exact normalized component weights include odd m without irrational arithmetic.
    for m in range(2,21):
      for d in range(1,17):
       for extra in (1,rad(d)):
        t=d**m*extra;g2=d**(m-2)
        need(Q(g2,t)<=Q(1,d*d),'component_critical_jacobian_weight')
        need(Q(g2,t*t)<=Q(1,d**4),'component_normalized_short_weight')
    return reports

def corr(f,g,h):
    z=Z
    for n in range(1,len(f)):
        if 0<n+h<len(g):z=add(z,mul(f[n],cj(g[n+h])))
    return z

def poly_add(p,k,z):p[k]=add(p.get(k,Z),z)

def direct_window_poly(f,g,L):
    p={};top=max(len(f),len(g))-1
    for j in range(1-L,top):
      for n in range(max(1,j+1),min(len(f),j+L+1)):
       for m in range(max(1,j+1),min(len(g),j+L+1)):
        right=g[m] if MUTATION=='conjugation' else cj(g[m])
        poly_add(p,n-m,mul(f[n],right))
    return {k:z for k,z in p.items() if z!=Z}

def overlap(L,h):
    return max(Q(0),Q(L)-(Q(h) if MUTATION=='overlap' else abs(Q(h))))

def gram_poly(f,g,L):
    return {-h:sc(corr(f,g,h),overlap(L,h)) for h in range(-len(f)+1,len(g))
            if overlap(L,h)>0 and corr(f,g,h)!=Z}

def ct_product(p,q):
    z=Z
    for k,a in p.items():z=add(z,mul(a,q.get(-k,Z)))
    return z

def mixed_tests():
    for N in (2,4,7):
      for seed in range(4):
        f=[Z]+[sc(ipow(n+seed),Q((n*3+seed)%5-2)) for n in range(1,N+1)]
        g=[Z]+[sc(ipow(2*n+seed+1),Q((n+2*seed)%7-3,2)) for n in range(1,2*N+1)]
        for L in (1,2,3,5,9):
          p=direct_window_poly(f,g,L);q=gram_poly(f,g,L)
          need(p==q,'mixed_Fourier_full_window_identity')
          spectral=sum((norm(z) for z in p.values()),Q(0))
          target=sum((overlap(L,h)**2*norm(corr(f,g,h))
                      for h in range(-N,2*N+1)),Q(0))
          need(spectral==target,'mixed_Parseval_identity')
          ef=direct_window_poly(f,f,L);eg=direct_window_poly(g,g,L)
          bound=ct_product(ef,eg)
          need(bound[1]==0 and spectral<=bound[0],'integrated_window_Cauchy')
          need(eg.get(0,Z)==(L*sum((norm(z) for z in g),Q(0)),Q(0)),
               'window_frequency_mass')

def energy_at_quarter(f,H,a):
    z=Z
    for n in range(1,len(f)):
      for m in range(1,len(f)):
        w=max(Q(0),H-abs(n-m))
        z=add(z,sc(mul(mul(f[n],cj(f[m])),ipow(a*(n-m))),w))
    need(z[1]==0 and z[0]>=0,'physical_window_energy_real_positive')
    return z[0]

def dilation_tests():
    base=[Z,ONE,(Q(0),Q(1)),(-Q(1),Q(0)),Z,ONE]
    gamma=(Q(2),Q(1))
    for t in (1,2,3,7):
      f=[Z]*((len(base)-1)*t+1)
      for r in range(1,len(base)):f[t*r]=mul(gamma,base[r])
      for H in (Q(3,2),Q(13,3),Q(7),Q(20)):
       for a in range(4):
        lhs=energy_at_quarter(f,H,a)
        jac=1 if MUTATION=='jacobian' else t
        rhs=norm(gamma)*jac*energy_at_quarter(base,H/t,(a*t)%4)
        need(lhs==rhs,'exact_dilation_Jacobian')
        need(lhs<=norm(gamma)*(H/t+1)*H*(len(base)-1),'microscopic_window_count_bound')

def partition(f,J):
    V=sum((norm(z) for z in f),Q(0));N=len(f)-1
    if not V:return [0,N],set()
    heavy={n for n in range(1,N+1) if norm(f[n])>V/J}
    endpoints=[0];mass=Q(0)
    for n in range(1,N+1):
        if n not in heavy:mass+=norm(f[n])
        if mass>=V/J:
            endpoints.append(n);mass=Q(0)
    if endpoints[-1]!=N:endpoints.append(N)
    need(len(endpoints)<=J+2,'partition_grid_count')
    need(len(heavy)<J,'partition_heavy_count')
    for l,r in zip(endpoints,endpoints[1:]):
        need(sum((norm(f[n]) for n in range(l+1,r+1) if n not in heavy),Q(0))<=2*V/J,
             'partition_light_mass')
    return endpoints,heavy

def maximal_case(f,g,H,J):
    V=sum((norm(z) for z in f),Q(0));W=sum((norm(z) for z in g),Q(0))
    endpoints,heavy=partition(f,J)
    maxima=Q(0);grid=Q(0)
    for h in range(1,H+1):
        c=Z;vals=[Q(0)]
        for n in range(1,len(f)):
            c=add(c,mul(f[n],cj(g[n+h])));vals.append(norm(c))
        maxima+=max(vals);grid+=sum(vals[j] for j in endpoints)
    hv=0 if MUTATION=='heavy' else 3*J*V*W
    rhs=3*grid+6*H*V*W/J+hv
    need(maxima<=rhs,'endpoint_maximal_heavy_light_bound')

def maximal_tests():
    # Two opposite heavy atoms cancel at the last endpoint, not at intermediate endpoints.
    maximal_case([Z,ONE,sc(ONE,-1)],[Z,ONE,ONE,ONE,ONE],1,1024)
    for N in (4,7,11):
      for seed in range(5):
        f=[Z]+[sc(ipow(n+seed),Q((n*5+seed)%9-4)) for n in range(1,N+1)]
        f[max(1,N//2)]=sc(ipow(seed),Q(100))
        g=[Z]+[sc(ipow(2*n+seed),Q((n*3+seed)%7-3,3)) for n in range(1,2*N+1)]
        for H in (1,2,min(5,N)):
         for J in (1,2,3,8,1024):maximal_case(f,g,H,J)
    maximal_case([Z]*5,[Z]*9,3,4)

def main():
    global MUTATION
    ap=argparse.ArgumentParser()
    ap.add_argument('--cap',type=int,default=729)
    ap.add_argument('--mutation',choices=['','mask','power','geometric','conjugation','overlap','jacobian','heavy'],default='')
    args=ap.parse_args()
    if args.cap<64:raise SystemExit('cap must be at least 64')
    MUTATION=args.mutation
    cases=coefficient_tests(args.cap)
    mixed_tests();dilation_tests();maximal_tests()
    need(Q(1,80)>Q(1,700),'strict_nonpretentious_exponent_budget')
    print(json.dumps({'status':'PASS_EXACT_FINITE_DIAGNOSTICS','source_case_count':len(cases),
       'source_cases_sha256':hashlib.sha256(json.dumps(cases,sort_keys=True).encode()).hexdigest(),
       'source_parameters':{'cap':args.cap,'families':['native','coupled','two-channel','geometric'],
           'native_degree':2,'completed_degrees':[2,3,4,6,10],'masks':[1,6],'profiles':[0,1]},
       'counts':dict(sorted(COUNTS.items())),
       'scope':{'arithmetic':'rational integers; Gaussian-rational coefficients',
                'odd_m_fixture':'powerful phase attenuated by p^(-1/2)',
                'full_native_asymptotic_verified':False,'MRT_reproved':False,
                'independent_review':False,'RH_proved':False}},indent=2,sort_keys=True))
if __name__=='__main__':main()
