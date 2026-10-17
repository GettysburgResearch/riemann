#!/usr/bin/env python3
"""Exact finite diagnostics for the affine-cancellation adapter.

Finite coefficient identities and tail budgets are checked. This program does
not prove Tao's analytic theorem, an asymptotic little-o, or RH. All rational
integer columns <= the stated caps are included; there is no ideal-field census.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
from math import gcd, isqrt, lcm
import hashlib
import json

Z = tuple[int, int]
ZERO: Z = (0, 0)
ONE: Z = (1, 0)
UNITS: tuple[Z, ...] = (ONE, (0, 1), (-1, 0), (0, -1))
COUNTS: dict[str, int] = {}
MUTATION = ''

def check(condition: bool, name: str) -> None:
    COUNTS[name] = COUNTS.get(name, 0) + 1
    if not condition:
        raise RuntimeError(f'FAILED: {name}')

def mul(a: Z, b: Z) -> Z:
    return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])

def scale(a: Z, k: int) -> Z:
    return (a[0]*k, a[1]*k)

def power(a: Z, j: int) -> Z:
    out = ONE
    while j:
        if j & 1:
            out = mul(out, a)
        a = mul(a, a)
        j //= 2
    return out

def norm2(a: Z) -> int:
    return a[0]*a[0]+a[1]*a[1]

def tables(n: int):
    spf = list(range(n+1))
    if n >= 1: spf[1] = 1
    for p in range(2, isqrt(n)+1):
        if spf[p] == p:
            for v in range(p*p, n+1, p):
                if spf[v] == v: spf[v] = p
    mu, phi, rad = [0]*(n+1), [0]*(n+1), [0]*(n+1)
    mu[1] = phi[1] = rad[1] = 1
    for v in range(2, n+1):
        p, r = spf[v], v//spf[v]
        if r % p == 0:
            mu[v], phi[v], rad[v] = 0, phi[r]*p, rad[r]
        else:
            mu[v], phi[v], rad[v] = -mu[r], phi[r]*(p-1), rad[r]*p
    return spf, mu, phi, rad

def char(n: int, twist: bool) -> int:
    if not twist: return 1
    if n % 2 == 0: return 0
    return 1 if n % 4 == 1 else -1

def zprime(p: int, profile: int) -> Z:
    return ONE if profile == 0 else UNITS[(p//2) % 4]

def zint(n: int, spf: list[int], profile: int) -> Z:
    z = ONE
    while n > 1:
        p = spf[n]
        z = mul(z, zprime(p, profile))
        n //= p
    return z

def direct(nmax: int, family: str, m: int, profile: int, mask: int, twist: bool, spf: list[int]):
    """Returns n*F(n), via local Euler coefficients; Gaussian integers exactly."""
    out = [ZERO]*(nmax+1)
    out[1] = ONE
    alpha = (m-2)//2
    for n in range(2, nmax+1):
        p, e, r = spf[n], 0, n
        while r % p == 0:
            r //= p
            e += 1
        masked = mask % p == 0
        if MUTATION == 'erase-mask': masked = False
        if masked or (twist and p == 2):
            local = ZERO
        else:
            chi, z = char(p, twist), zprime(p, profile)
            if family == 'native':
                local = (-chi*p, 0) if e == 1 else ZERO
            elif family == 'coupled':
                if e == 1:
                    local = (-chi*(p-1), 0)
                elif e == m:
                    weight = m+alpha+(1 if MUTATION == 'power-weight' else 0)
                    local = scale(z, -p**weight)
                else: local = ZERO
            elif family == 'two-channel':
                if e == 1: local = (-chi*p, 0)
                elif e == m: local = scale(z, -p**(m+alpha))
                elif e == m+1:
                    local = ZERO if MUTATION == 'delete-shared' else scale(z, chi*p**(m+1+alpha))
                else: local = ZERO
            elif family == 'geometric':
                if e >= 1 and (e-1) % m == 0:
                    j = (e-1)//m
                    local = scale(power(z, j), -chi*(p-1)*p**(j*(m+alpha)))
                else: local = ZERO
            else: raise ValueError(family)
        out[n] = mul(local, out[r])
    return out

def by_representation(nmax: int, family: str, m: int, profile: int, mask: int, twist: bool, tab):
    spf, mu, phi, rad = tab
    out = [ZERO]*(nmax+1)
    ds = [0]*(nmax+1)
    major = [0]*(nmax+1)
    alpha = (m-2)//2
    d = 1
    while d**m <= nmax:
        if family == 'native' and d > 1: break
        if gcd(d, mask) != 1 or (twist and d % 2 == 0):
            d += 1; continue
        if family in ('coupled', 'two-channel') and mu[d] == 0:
            d += 1; continue
        dm, zp = d**m, zint(d, spf, profile)
        for r in range(1, nmax//dm+1):
            if mu[r] == 0 or gcd(r, mask) != 1 or char(r, twist) == 0:
                continue
            if family == 'coupled' and gcd(d, r) != 1: continue
            if family == 'geometric' and r % rad[d] != 0: continue
            n = dm*r
            check(ds[n] == 0, 'unique-representation')
            ds[n] = d
            major[n] = d**(m-2)
            if family in ('coupled', 'geometric'):
                fac = mu[r]*char(r, twist)*phi[r]*d**(m+alpha)
            else:
                fac = mu[r]*char(r, twist)*n*d**alpha
            if family in ('coupled', 'two-channel'): fac *= mu[d]
            out[n] = scale(zp, fac)
        d += 1
    return out, ds, major

def solve_one(a: int, b: int, t: int):
    g = gcd(a, t)
    if b % g: return None
    q = t//g
    return ((-(b//g)*pow(a//g, -1, q)) % q, q) if q > 1 else (0, 1)

def solve_pair(a: int, b: int, c: int, d: int, t: int, u: int):
    x, y = solve_one(a,b,t), solve_one(c,d,u)
    if x is None or y is None: return None
    r, p = x
    s, q = y
    g = gcd(p,q)
    if (s-r) % g: return None
    mod = lcm(p,q)
    qg = q//g
    k = ((s-r)//g * pow(p//g,-1,qg)) % qg if qg > 1 else 0
    residue = (r+p*k) % mod
    return (residue if residue else mod, mod)

def crt_checks():
    fixtures = 0
    for a in (1,2,3):
      for c in (1,2,3):
       for b in (0,1,2):
        for d in (0,1,2):
         if a*d == c*b: continue
         for t in (1,4,8,9,25):
          for u in (1,4,8,9,25):
           sol = solve_pair(a,b,c,d,t,u)
           truth = [n for n in range(1,201) if (a*n+b)%t == 0 and (c*n+d)%u == 0]
           got = [] if sol is None else [n for n in range(1,201) if (n-sol[0])%sol[1] == 0]
           check(truth == got, 'full-crt-subsequence')
           if sol is None: continue
           n0, ell = sol
           A,B,C,D = a*ell//t,(a*n0+b)//t,c*ell//u,(c*n0+d)//u
           rhs = ell*(a*d-c*b)
           if MUTATION == 'determinant': rhs *= ell
           check(t*u*(A*D-C*B) == rhs and A*D != C*B, 'affine-determinant')
           for j in (0,1,2):
               n = n0+ell*j
               check(t*(A*j+B) == a*n+b and u*(C*j+D) == c*n+d,
                     'literal-cofactor-arguments')
           fixtures += 1
    return fixtures

def exact_filter_gram(nums: list[Z], nmax: int = 96, shifts: int = 4):
    def f(n): return Q(nums[n][0],n),Q(nums[n][1],n)
    def qm(a,b): return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
    def conj(a): return a[0],-a[1]
    gram = [[(Q(0),Q(0)) for _ in range(shifts)] for _ in range(shifts)]
    for i in range(shifts):
      for j in range(shifts):
       z = (Q(0),Q(0))
       for n in range(1,nmax+1):
        v = qm(f(n+i),conj(f(n+j)))
        z=(z[0]+v[0]/n,z[1]+v[1]/n)
       gram[i][j]=z
       if j<i: check(z==conj(gram[j][i]),'gram-hermitian')
    for weights in ((1,1,1,1),(1,-1,1,-1),(2,0,-1,3)):
      energy = Q(0)
      for n in range(1,nmax+1):
        a = sum(weights[j]*f(n+j)[0] for j in range(shifts))
        b = sum(weights[j]*f(n+j)[1] for j in range(shifts))
        energy += (a*a+b*b)/n
      pair = sum(Q(weights[i]*weights[j])*gram[i][j][0]
                 for i in range(shifts) for j in range(shifts))
      check(energy==pair and energy>=0,'complete-filter-gram')
    return {'nmax':nmax,'H':shifts,'off_diagonal_0_1_real':str(gram[0][1][0]),
            'diagonal_0_real':str(gram[0][0][0]),
            'purpose':'Finite identity only; not an asymptotic measurement.'}

def composed_correlation_checks(tab):
    spf, mu, phi, rad = tab
    def qm(x,y): return x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]
    def qc(x): return x[0],-x[1]
    def g(k, eps, excluded):
        if k<1 or gcd(k,excluded)!=1: return (Q(0),Q(0))
        return (Q(mu[k]*phi[k],k) if eps else Q(mu[k]), Q(0))
    def term(d,fam,m,profile):
        if gcd(d,3)!=1: return None
        if fam!='geometric' and mu[d]==0: return None
        z=zint(d,spf,profile); alpha=(m-2)//2
        if fam=='geometric':
            gamma=Q(mu[rad[d]]*phi[rad[d]]*d**alpha,rad[d])
            return (d**m*rad[d], (gamma*z[0],gamma*z[1]), 1, 3*d)
        gamma=Q(mu[d]*d**alpha)
        return (d**m,(gamma*z[0],gamma*z[1]),int(fam=='coupled'),3*d if fam=='coupled' else 3)
    for fam in ('coupled','two-channel','geometric'):
      for m in (2,4,6):
       for profile in (0,1):
        nums=direct(512,fam,m,profile,3,False,spf)
        alt,ds,_=by_representation(512,fam,m,profile,3,False,tab)
        check(nums==alt,'auxiliary-mask-three-coefficients')
        terms=[z for d in range(1,6) if (z:=term(d,fam,m,profile)) is not None]
        for a,b,c,d in ((1,0,1,6),(2,1,3,1),(1,1,2,0)):
          direct_sum=(Q(0),Q(0)); rhs=(Q(0),Q(0))
          for n in range(1,97):
            v,w=a*n+b,c*n+d
            if ds[v]>5 or ds[w]>5: continue
            z=qm((Q(nums[v][0],v),Q(nums[v][1],v)),qc((Q(nums[w][0],w),Q(nums[w][1],w))))
            direct_sum=(direct_sum[0]+z[0]/n,direct_sum[1]+z[1]/n)
          for t,gamma,e1,s1 in terms:
           for u,eta,e2,s2 in terms:
            sol=solve_pair(a,b,c,d,t,u)
            if sol is None: continue
            n0,ell=sol
            factor=qm(gamma,qc(eta))
            for n in range(n0,97,ell):
              z=qm(factor,qm(g((a*n+b)//t,e1,s1),qc(g((c*n+d)//u,e2,s2))))
              rhs=(rhs[0]+z[0]/n,rhs[1]+z[1]/n)
          check(direct_sum==rhs,'complete-truncated-affine-correlation')

def density_checks():
    for p in (2,3,5,7,11,13):
      v = Q(p-1,p)
      for m in (2,4,6,8):
       for z in UNITS+(ZERO,):
        zz=norm2(z)
        coupled=1+v*v/p+Q(zz,p*p)
        two=(1+Q(1,p))*(1+Q(zz,p*p))
        geo=1+v*v/(p*(1-Q(zz,p*p)))
        for fam,target in [('coupled',coupled),('two-channel',two)]:
          coeff={0:(Q(1),Q(0)),1:(-v if fam=='coupled' else Q(-1),Q(0))}
          coeff[m]=(Q(-z[0]*p**((m-2)//2)),Q(-z[1]*p**((m-2)//2)))
          if fam=='two-channel':
            coeff[m+1]=(Q(z[0]*p**((m-2)//2)),Q(z[1]*p**((m-2)//2)))
          actual=sum((a*a+b*b)/p**e for e,(a,b) in coeff.items())
          check(actual==target,'density-local-independent-degree')
        terms = 1+sum(v*v*Q(zz,p*p)**j/p for j in range(7))
        tail = v*v/p*Q(zz,p*p)**7/(1-Q(zz,p*p))
        check(terms+tail==geo,'geometric-density-full-tail')

def main():
    global MUTATION
    parser=argparse.ArgumentParser()
    parser.add_argument('--cap',type=int,default=131072)
    parser.add_argument('--mutation',choices=['erase-mask','power-weight','delete-shared','determinant'],default='')
    args=parser.parse_args()
    if args.cap<512: raise SystemExit('--cap must be at least 512 (auxiliary full-coefficient fixture)')
    MUTATION=args.mutation
    tab=tables(args.cap)
    cases=[]
    gram=None
    for family in ('native','coupled','two-channel','geometric'):
      for m in ((6,) if family=='native' else (2,4,6)):
       # All integers in each cap are included, not a selected prime semigroup.
       for profile in (0,1):
        twist=bool(profile)
        mask=6
        x=direct(args.cap,family,m,profile,mask,twist,tab[0])
        y,ds,major=by_representation(args.cap,family,m,profile,mask,twist,tab)
        pref=0
        tails={r:0 for r in (1,2,3,5,7,11)}
        digest=hashlib.sha256()
        for n in range(1,args.cap+1):
          check(x[n]==y[n],'complete-coefficient-comparison')
          check(norm2(x[n]) <= n*n*major[n],'coefficient-square-majorant')
          pref+=major[n]
          check(pref<=2*n,'full-square-prefix-budget')
          for r in tails:
            if ds[n]>r: tails[r]+=major[n]
            check(r*tails[r]<=n,'tail-prefix-budget')
          digest.update(f'{x[n][0]},{x[n][1]};'.encode())
        cases.append({'family':family,'m':m,'profile':profile,'xi':'mod4' if twist else 'principal',
          'cap':args.cap,'supported':sum(d>0 for d in ds),'digest':digest.hexdigest(),
          'square_majorant_sum':pref,'tail_majorant_sums':tails})
        if family=='coupled' and m==6 and profile==0:
          if args.cap>=5**6: check(x[5**6]==(-5**8,0),'actual-sixth-power-weight')
          if args.cap>=7**6: check(x[7**6]==(-7**8,0),'second-sixth-power-weight')
          gram=exact_filter_gram(direct(256,'coupled',6,0,3,False,tab[0]))
    composed_correlation_checks(tab)
    crt=crt_checks()
    density_checks()
    # Counterexample to deleting nonproportionality, with a complete mu^2 prefix.
    _,mu,_,_=tab
    check(sum(mu[n]**2 for n in range(1,101))==61,'proportional-negative-control')
    report={'status':'PASS_FINITE_ALGEBRA_AND_TAIL_BUDGETS','counts':COUNTS,'cases':cases,
       'compatible_crt_cases':crt,'finite_gram':gram,
       'scope':{'field':'Q','complete_integer_caps':True,'analytic_theorem_verified':False,
                'independent_review':False,'ordinary_elliott_rebuilt':False,'rh_proved':False}}
    print(json.dumps(report,sort_keys=True,indent=2))

if __name__=='__main__': main()
