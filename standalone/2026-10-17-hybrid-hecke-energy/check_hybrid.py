#!/usr/bin/env python3
"""Finite diagnostics for the written hybrid theorem, NOT asymptotic certification.

Exact mode uses only the standard library. Numerical mode additionally uses
mpmath; its output is not directed/interval arithmetic. Field computations
below use a+b*omega, omega^2+omega+1=0, throughout (not the zeta_6 basis).
"""
from __future__ import annotations
import argparse
import itertools
import json
import math
from collections import Counter
from fractions import Fraction as Q

ONE = (1, 0)
ZERO = (0, 0)
UNITS = ((1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1))
MUTANT = ''
COUNTS: Counter[str] = Counter()


def require(ok: bool, category: str) -> None:
    COUNTS[category] += 1
    if not ok:
        raise RuntimeError('failed: ' + category)


def mul(a, b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]-a[1]*b[1]


def conj(a):
    return a[0]-a[1], -a[1]


def norm(a):
    return a[0]*a[0]-a[0]*a[1]+a[1]*a[1]


def power(a, e):
    out = ONE
    while e:
        if e & 1:
            out = mul(out, a)
        a = mul(a, a)
        e //= 2
    return out


def canon(a):
    return min(mul(a, e) for e in UNITS)


def ideals(cap: int):
    b = math.isqrt(2*cap)+1
    out = {canon((x,y)) for x in range(-b,b+1) for y in range(-b,b+1)
           if 0 < norm((x,y)) <= cap}
    if MUTANT == 'conjugates':
        out = set({norm(a):a for a in sorted(out)}.values())
    return sorted(out, key=lambda a:(norm(a),a))


def elements(cap: int):
    b = math.isqrt(2*cap)+1
    return [(x,y) for x in range(-b,b+1) for y in range(-b,b+1)
            if 0 < norm((x,y)) <= cap]


def divide(a, p):
    q = norm(p)
    z = mul(a, conj(p))
    if z[0] % q or z[1] % q:
        return None
    return z[0]//q, z[1]//q


def angular(a):
    q = norm(a)
    if MUTANT == 'units':
        z = power(a, 3)  # intentionally invalid unit convention
        return Q(z[0], q), Q(z[1], q)
    z = power(a, 6)
    return Q(z[0], q**3), Q(z[1], q**3)


def pmul(a, b):
    c = [Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j] += x*y
    return c


def ppow(a, k):
    c = [Q(1)]
    for _ in range(k):
        c = pmul(c, a)
    return c


def powerful_weight(q: int, m: int):
    if m % 2 == 0:
        return Q(q**(m//2-1 + int(MUTANT == 'power')))
    r = math.isqrt(q)
    if r*r != q:
        raise ValueError('odd-degree exact fixture requires square prime norm')
    return Q(r**(m-2))


def residue_power(a, e, p):
    out = ONE
    while e:
        if e & 1:
            out = tuple(v % p for v in mul(out,a))
        a = tuple(v % p for v in mul(a,a))
        e //= 2
    return out


def symbol(pi, u):
    q = norm(pi)
    p = math.isqrt(q)
    if p*p == q:
        v = (u[0] % p, u[1] % p)
        if v == ZERO:
            return None
        target = residue_power(v,(q-1)//6,p)
        return next(j for j in range(6) if residue_power((1,1),j,p)==target)
    p = q
    w = -pi[0]*pow(pi[1] % p,-1,p) % p
    v = (u[0]+u[1]*w) % p
    if not v:
        return None
    target = pow(v,(p-1)//6,p)
    return next(j for j in range(6) if pow((1+w)%p,j,p)==target)


def prime(q):
    return q>=2 and all(q%d for d in range(2,math.isqrt(q)+1))


def prime_ideals(cols):
    out=[]
    for a in cols:
        q=norm(a); r=math.isqrt(q)
        if prime(q) or (r*r==q and prime(r) and r%3==2):
            out.append(a)
    return out


def factor(a, primes):
    left=a; fs=[]
    for p in primes:
        if norm(p)>norm(left):
            break
        e=0
        while True:
            z=divide(left,p)
            if z is None:
                break
            left=z; e+=1
        if e:
            fs.append((p,e))
        if norm(left)==1:
            break
    if norm(left)!=1:
        raise RuntimeError('incomplete ideal factorization')
    return fs


def coeff(fs, m, native=False):
    out=Q(1)
    for p,e in fs:
        q=norm(p)
        if q in (3,4):
            return Q(0)
        if e==1:
            out *= -1 if native else -Q(q-1,q)
        elif not native and e==m:
            out *= -powerful_weight(q,m)
        else:
            return Q(0)
    return out


def exact_report():
    # A complete, independently counted norm census of ideals, not supported columns only.
    cols=ideals(512)
    bynorm=Counter(norm(a) for a in cols)
    expected=[0]*513
    for d in range(1,513):
        ch=0 if d%3==0 else (1 if d%3==1 else -1)
        for n in range(d,513,d):
            expected[n]+=ch
    for n in range(1,513):
        require(bynorm[n]==expected[n], 'complete_ideal_norm_counts')
    small=[a for a in cols if norm(a)<=128]
    for a in small:
        require(norm(angular(a))==1, 'angular_norm_one')
        for e in UNITS:
            require(angular(mul(a,e))==angular(a), 'unit_invariance')
    tiny=[a for a in cols if norm(a)<=32]
    for a,b in itertools.product(tiny,repeat=2):
        require(angular(mul(a,b))==mul(angular(a),angular(b)), 'angular_multiplicativity')
    for a,b in itertools.combinations(small,2):
        gap=min(norm((a[0]-z[0],a[1]-z[1])) for z in (mul(b,e) for e in UNITS))
        require(gap>=1, 'nonassociate_lattice_gap')
        if norm(a)==norm(b):
            require(angular(a)!=angular(b), 'equal_norm_separation')
    # All local coefficients, including the nonzero first-order correction.
    localcases=0
    for q in (7,13,25):
        for m in (2,3,4,6,7):
            if m%2 and q!=25:
                continue
            for k in (1,2,3,4):
                f=[Q(1),-Q(q-1,q)]+[Q(0)]*(m-1)
                f[m]=-powerful_weight(q,m)
                require(f[m]*f[m]/q**m==Q(1,q*q), 'critical_powerful_weight')
                pos=[abs(x) for x in f]
                de=ppow(pos,k)
                P=[x*x/q**e for e,x in enumerate(de)]
                require(sum(P[2:])<=Q(9**k,q*q), 'tensor_local_tail')
                V=[Q(math.comb(k*k,j)*(-1)**j,q**j) for j in range(k*k+1)]
                prod=pmul(P,V)
                require(prod[1]==k*k*(-Q(2,q*q)+Q(1,q**3)), 'linear_correction_retained')
                r=k*k; C=2*r+r*r+2**r*(1+r+9**k)
                require(sum(abs(x) for x in prod[1:])<=Q(C,q*q), 'uniform_local_mass')
                localcases+=1
    # Actual sextic nonunit masks on all 54 small physical rows.
    ps=[a for a in cols if norm(a)==7]+[a for a in cols if norm(a)==25]
    rows=elements(13)
    require(len(rows)==54 and len(ps)==3,'physical_fixture_size')
    for u in rows:
        for p in ps:
            j=symbol(p,u)
            require((j is None)==(divide(u,p) is not None),'literal_nonunit_zero')
            for e in (1,6):
                val=ZERO if j is None else power((1,1),(j*e)%6)
                require((val==ZERO)==(j is None),'power_keeps_mask')
                if j is not None and e==6:
                    require(val==ONE,'sixth_power_unit_value')
    # The first actual sixth-power ideal is represented, without calling it a full large census.
    for p in ps[:2]:
        a=power(p,6)
        require(norm(a)==7**6 and angular(a)==power(angular(p),6),'first_sixth_power')
    # Complete tensor regrouping in small ideal polynomials, with overlaps retained.
    allsmall=ideals(64); primes=prime_ideals(allsmall)
    for m in (2,4,6):
        supported=[(a,coeff(factor(a,primes),m)) for a in allsmall]
        supported=[(a,c) for a,c in supported if c]
        for k in (2,3):
            grouped={canon(ONE):Q(1)}
            for _ in range(k):
                nxt={}
                for a,x in grouped.items():
                    for b,y in supported:
                        ab=canon(mul(a,b));nxt[ab]=nxt.get(ab,Q(0))+x*y
                grouped=nxt
            direct={}
            for tup in itertools.product(supported,repeat=k):
                a=ONE;c=Q(1)
                for b,x in tup:a=mul(a,b);c*=x
                a=canon(a);direct[a]=direct.get(a,Q(0))+c
            require(grouped==direct,'complete_tensor_regrouping')
            require(all(norm(a)<=64**k for a in grouped),'tensor_support_length')
    # Finite class averaging is algebraic. This is a model of the gate, not a nonprincipal-field census.
    for h in (2,3,4,5):
        for a in range(h):
            for b in range(h):
                residues=Counter((j*(a-b))%h for j in range(h))
                if a==b:
                    require(residues=={0:h},'class_gate_diagonal')
                else:
                    d=math.gcd(a-b,h)
                    require(set(residues)==set(range(0,h,d)) and set(residues.values())=={d},
                            'class_gate_off_diagonal')
    return {'status':'PASS finite exact identities only','local_tensor_cases':localcases,
            'complete_ideal_cap':512,'complete_ideals':len(cols),'physical_rows':len(rows),
            'categories':dict(sorted(COUNTS.items())),
            'coverage_warning':'Large sixth-power ideals are local fixtures, not a full high-norm census. General class-group field geometry is proved, not numerically enumerated.'}


def numerical_report():
    import mpmath as mp
    mp.mp.dps=60
    embed=lambda a:mp.mpf(a[0].numerator)/a[0].denominator if isinstance(a[0],Q) else mp.mpf(a[0])
    def realq(x):return mp.mpf(x.numerator)/x.denominator if isinstance(x,Q) else mp.mpf(x)
    def emb(a):return realq(a[0])+realq(a[1])*mp.mpc(-mp.mpf('0.5'),mp.sqrt(3)/2)
    def directtheta(th,R):
        J=int(mp.ceil(20*R));zs=[mp.exp(-mp.mpf(j*j)/(2*R*R)) for j in range(-J,J+1)]
        return sum(z*mp.exp(1j*j*th) for j,z in zip(range(-J,J+1),zs))/sum(zs)
    def theta(th,R):
        if MUTANT=='periodic':return mp.exp(-R*R*th*th/2)
        th=mp.fmod(th+mp.pi,2*mp.pi)-mp.pi
        return (sum(mp.exp(-R*R*(th-2*mp.pi*j)**2/2) for j in range(-6,7)) /
                sum(mp.exp(-2*mp.pi**2*R*R*j*j) for j in range(-6,7)))
    def W(y,c):return y**(-c)*mp.exp(-mp.log(y)**2/4)/(2*mp.sqrt(mp.pi))
    def kernel(v,z,D,c):
        beta=2*c-(0 if MUTANT=='jacobian' else 1)
        return (mp.exp(beta**2/2)/(2*mp.sqrt(2*mp.pi*v*z))*mp.exp(-mp.log(v/z)**2/8)*
                mp.erfc(-(mp.log(D)-mp.log(v*z)/2-beta)/mp.sqrt(2))/2)
    maxheat=mp.mpf(0);heatcases=0
    for R in map(mp.mpf,(1,2,4)):
        for th in (mp.mpf(0),mp.mpf('0.1'),mp.pi,2*mp.pi,2*mp.pi-mp.mpf('0.2')):
            err=abs(theta(th,R)-directtheta(th,R));maxheat=max(maxheat,err);heatcases+=1
            require(err<mp.mpf('1e-45'),'periodic_fourier_numerical')
    maxkernel=mp.mpf(0)
    c=mp.mpf(5)/6
    for v,z,D in ((1,1,2),(7,7,8),(7,13,16),(25,49,32),(49,7,64),(1,117649,64)):
        vv,zz,DD=map(mp.mpf,(v,z,D))
        f=lambda x:W(vv/mp.exp(x),c)*W(zz/mp.exp(x),c)*mp.exp(-x)
        value=mp.quad(f,[-mp.inf,mp.log(DD)])
        err=abs(value-kernel(vv,zz,DD,c));maxkernel=max(maxkernel,err)
        require(err<mp.mpf('1e-45'),'critical_gaussian_integral')
    maxfourier=mp.mpf(0)
    for R in (mp.mpf(1),mp.mpf(2)):
        for x in (mp.log(2),mp.log(mp.mpf(13)/7)):
            v=mp.quad(lambda t:mp.exp(-t*t/(2*R*R))*mp.cos(t*x),[-mp.inf,mp.inf])/(mp.sqrt(2*mp.pi)*R)
            e=abs(v-mp.exp(-R*R*x*x/2));maxfourier=max(maxfourier,e)
            require(e<mp.mpf('1e-45'),'mellin_gaussian_fourier')
    # Complete finite polynomials: every supported ideal under the specified cap is retained.
    panels=[]
    for cap,m,native in ((32,2,False),(64,2,False),(64,6,False),(128,6,True)):
        acols=ideals(cap); primes=prime_ideals(acols)
        data=[(a,coeff(factor(a,primes),m,native)) for a in acols]
        data=[(a,v) for a,v in data if v]
        D=mp.mpf(cap)/2
        for R in (mp.sqrt(D),2*mp.sqrt(D)):
            diag=mp.mpf(0);full=mp.mpc(0);absolute=mp.mpf(0)
            for a,ca in data:
                n=mp.mpf(norm(a));diag+=realq(ca)**2*kernel(n,n,D,c)
                for b,cb in data:
                    j=mp.mpf(norm(b));th=6*mp.arg(emb(a)/emb(b))
                    F=mp.exp(-R*R*mp.log(n/j)**2/2)*theta(th,R)
                    term=realq(ca)*realq(cb)*kernel(n,j,D,c)*F
                    full+=term
                    if a!=b:absolute+=abs(term)
            require(abs(full.imag)<mp.mpf('1e-45') and full.real>=-mp.mpf('1e-45'),'finite_mean_nonnegative')
            require(abs(full.real-diag)<=absolute+mp.mpf('1e-45'),'finite_absolute_off_diagonal')
            panels.append({'cap':cap,'m':m,'native':native,'ideals':len(acols),
                           'nonzero_columns':len(data),'D':mp.nstr(D,16),'R':mp.nstr(R,16),
                           'diagonal':mp.nstr(diag,24),'full_finite_mean':mp.nstr(full.real,24),
                           'absolute_averaged_off_diagonal':mp.nstr(absolute,24)})
    return {'status':'PASS non-interval finite numerical diagnostics','digits':60,
            'heat_cases':heatcases,'gaussian_pair_cases':6,'radial_fourier_cases':4,
            'largest_heat_error':mp.nstr(maxheat,8),'largest_kernel_error':mp.nstr(maxkernel,8),
            'largest_radial_error':mp.nstr(maxfourier,8),'panels':panels,
            'coverage_warning':'Panels are complete FINITE ideal polynomials under their caps; none evaluates the infinite Gaussian source or certifies an asymptotic theorem.'}


def main():
    global MUTANT
    ap=argparse.ArgumentParser()
    ap.add_argument('--numerical',action='store_true')
    ap.add_argument('--mutant',default='',choices=('', 'conjugates','units','power','periodic','jacobian'))
    args=ap.parse_args();MUTANT=args.mutant
    out=numerical_report() if args.numerical else exact_report()
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__':main()
