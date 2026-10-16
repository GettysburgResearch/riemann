#!/usr/bin/env python3
"""Exact, standard-library checks. Not a theta build or asymptotic certificate.

Local Gauss tests cover complete small residue rings and declared higher-power
samples. The row tests use finite sparse Eisenstein fixtures and named prime
semigroups, NOT all native ideals or all rows below their large norm caps.
"""
from __future__ import annotations
from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
from math import isqrt
import json

COUNTS = Counter()
NEGATIVE = []
def check(ok: bool, name: str) -> None:
    COUNTS[name] += 1
    if not ok:
        raise RuntimeError(f'{name}: predicate {COUNTS[name]} failed')
def reject(ok: bool, name: str) -> None:
    check(not ok, 'negative_controls')
    NEGATIVE.append(name)

@dataclass(frozen=True)
class C:
    a: F = F(0)
    b: F = F(0)
    def __post_init__(self):
        object.__setattr__(self, 'a', F(self.a))
        object.__setattr__(self, 'b', F(self.b))
    def __add__(self, y):
        y = y if isinstance(y,C) else C(y)
        return C(self.a+y.a,self.b+y.b)
    __radd__=__add__
    def __neg__(self): return C(-self.a,-self.b)
    def __sub__(self,y): return self+(-y if isinstance(y,C) else -F(y))
    def __mul__(self,y):
        y=y if isinstance(y,C) else C(y)
        return C(self.a*y.a-self.b*y.b,self.a*y.b+self.b*y.a-self.b*y.b)
    __rmul__=__mul__
    def __pow__(self,n:int):
        if n<0: raise ValueError('nonnegative power required')
        x=self; r=C(1)
        while n:
            if n&1:r=r*x
            n//=2;x=x*x
        return r
    def conj(self):return C(self.a-self.b,-self.b)
    def norm(self):return self.a*self.a-self.a*self.b+self.b*self.b
ZERO,ONE=C(),C(1)
ROOTS=tuple(C(1,1)**j for j in range(6))

# O=Z[omega] and prime generators. Two distinct norm-7 prime ideals remain.
def mul(x,y):
    a,b=x;c,d=y
    return (a*c-b*d,a*d+b*c-b*d)
def norm(x):return x[0]*x[0]-x[0]*x[1]+x[1]*x[1]
def powe(x,n):
    r=(1,0)
    while n:
        if n&1:r=mul(r,x)
        x=mul(x,x);n//=2
    return r
def divexact(x,y):
    a,b=mul(x,(y[0]-y[1],-y[1]));q=norm(y)
    return (a//q,b//q) if a%q==0 and b%q==0 else None
def vp(x,pi):
    if x==(0,0):raise ValueError('zero is not a row')
    e=0
    while True:
        y=divexact(x,pi)
        if y is None:return e,x
        e+=1;x=y

PIS=((2,-1),(3,1),(5,0),(4,1))
QS=tuple(norm(pi) for pi in PIS)
RS=(2,4,None,9)

def modmul(x,y,p):return tuple(t%p for t in mul(x,y))
def modpow(x,n,p):
    r=(1,0)
    while n:
        if n&1:r=modmul(r,x,p)
        x=modmul(x,x,p);n//=2
    return r

def chi_index(row,i):
    q,r=QS[i],RS[i]
    if r is not None:
        x=(row[0]+r*row[1])%q
        if x==0:return None
        v=pow(x,(q-1)//6,q)
        return [pow(1+r,j,q) for j in range(6)].index(v)
    x=tuple(t%5 for t in row)
    if x==(0,0):return None
    v=modpow(x,4,5)
    return [((int(z.a)%5),(int(z.b)%5)) for z in ROOTS].index(v)

def gauss_shape(row,exponents):
    """Actual CRT Gauss row up to one nonzero scalar depending only on s.
    The scalar cancels from every homogeneous identity tested below.
    """
    out=ONE
    for i,e in enumerate(exponents):
        if not e:continue
        v,_=vp(row,PIS[i])
        if v<e-1:return ZERO
        if e%6:
            if v!=e-1:return ZERO
            t=divexact(row,powe(PIS[i],e-1))
            ci=chi_index(t,i)
            if ci is None:raise RuntimeError('unit shell was not a unit')
            out=out*ROOTS[(-e*ci)%6]
        else:
            out=out*(-1 if v==e-1 else QS[i]-1)
    return out

# Exact cyclotomic reduction in Q(omega)[Y]/Phi_(p^e)(Y), p != 3.
def reduce_poly(poly,p,e):
    n=p**e;block=p**(e-1);cut=(p-1)*block
    a={i%n:z for i,z in poly.items() if z!=ZERO}
    for i in list(a):
        if i>=cut:
            z=a.pop(i);r=i-cut
            for k in range(p-1):
                j=r+k*block;a[j]=a.get(j,ZERO)-z
    return tuple(sorted((i,z) for i,z in a.items() if z!=ZERO))
def add_term(a,i,z):
    a[i]=a.get(i,ZERO)+z

def primitive_root(p):
    for g in range(2,p):
        vals=[pow(g,j,p) for j in range(p-1)]
        if len(set(vals))==p-1:return g
    raise RuntimeError('prime without primitive root')

def gauss_split(p,e,m):
    n=p**e;g=primitive_root(p)
    ind={pow(g,j,p):j%6 for j in range(p-1)}
    coeff={}
    for x in range(n):
        if x%p:add_term(coeff,(m*x)%n,ROOTS[(e*ind[x%p])%6])
    return reduce_poly(coeff,p,e)
def gauss_split_fiber(p,e,m):
    n=p**e;b=p**(e-1)
    if m%b:return ()
    g=primitive_root(p);ind={pow(g,j,p):j%6 for j in range(p-1)}
    coeff={};t=(m//b)%p
    for r in range(1,p):add_term(coeff,(t*r%p)*b,ROOTS[(e*ind[r])%6]*b)
    return reduce_poly(coeff,p,e)

def gauss_inert(e,m):
    mod=5**e;coeff={}
    for x in product(range(mod),repeat=2):
        ci=chi_index(x,2)
        if ci is None:continue
        a,b=modmul(m,x,mod)
        add_term(coeff,(2*a-b)%mod,ROOTS[(e*ci)%6])
    return reduce_poly(coeff,5,e)
def gauss_inert_fiber(e,m):
    b=5**(e-1);coeff={}
    if m[0]%b or m[1]%b:return ()
    t=(m[0]//b,m[1]//b)
    for x in product(range(5),repeat=2):
        ci=chi_index(x,2)
        if ci is None:continue
        a,c=modmul(t,x,5)
        add_term(coeff,((2*a-c)%5)*b,ROOTS[(e*ci)%6]*(25**(e-1)))
    return reduce_poly(coeff,5,e)

def cyclo_norm(poly,p,e):
    n=p**e;a={}
    for i,x in poly:
        for j,y in poly:add_term(a,(i-j)%n,x*y.conj())
    return reduce_poly(a,p,e)

def local_gauss_checks():
    coverage=[]
    for p,e in ((7,1),(7,2),(7,3),(13,1),(13,2)):
        for m in range(p**e):
            g=gauss_split(p,e,m)
            check(g==gauss_split_fiber(p,e,m),'split_complete_gauss')
            check(bool(g)==(m%(p**(e-1))==0 and m%(p**e)!=0),'active_support')
        coverage.append({'prime':p,'exponent':e,'all_residues':p**e})
    p,e=7,6
    ms=(0,1,p**4,p**5,2*p**5,p**6)
    for m in ms:
        g=gauss_split(p,e,m)
        check(g==gauss_split_fiber(p,e,m),'neutral_gauss_samples')
        expected=(p**(e-1)*(p-1) if m%(p**e)==0 else -p**(e-1)) if m%(p**(e-1))==0 else 0
        check(g==(() if expected==0 else ((0,C(expected)),)),'neutral_ramanujan')
    coverage.append({'prime':7,'exponent':6,'sample_rows':list(ms)})
    for e in (1,2):
        mod=5**e
        for m in product(range(mod),repeat=2):
            g=gauss_inert(e,m)
            check(g==gauss_inert_fiber(e,m),'inert_complete_gauss')
            b=5**(e-1)
            check(bool(g)==(m[0]%b==0 and m[1]%b==0 and m!=(0,0)),'active_support')
        coverage.append({'residue_characteristic':5,'residue_norm':25,'exponent':e,'all_residues':mod*mod})
    for p in (7,13):
        for e in (1,2,3,4,5):
            # Finite-field primitive character chi^e, rather than a p^e modulus.
            coeff={};g=primitive_root(p)
            for j in range(p-1):add_term(coeff,pow(g,j,p),ROOTS[(e*j)%6])
            tau=reduce_poly(coeff,p,1)
            check(cyclo_norm(tau,p,1)==((0,C(p)),),'finite_field_gauss_norm')
    reject(gauss_split(7,6,7**5)==(), 'neutral_gauss_is_not_supported_only_on_units')
    reject(gauss_split(7,6,0)==((0,C(7**6)),), 'zero_extended_principal_is_not_constant_one')
    return coverage

@dataclass(frozen=True)
class Ideal:
    exps: tuple[int,...]
    gen: tuple[int,int]
    q: int
    h: C

def ideal(exps,phase=1):
    g=(1,0);q=1;h=ONE
    for i,j in enumerate(exps):
        g=mul(g,powe(PIS[i],j));q*=QS[i]**j
        if j:h=h*ROOTS[(phase*(i+1)*j)%6]*F(-(QS[i]-1),QS[i]**j)
    return Ideal(tuple(exps),g,q,h)

def boxes(indices,cap=1,phase=1):
    out=[]
    for ee in product(range(cap+1),repeat=len(indices)):
        es=[0]*len(PIS)
        for i,e in zip(indices,ee):es[i]=e
        out.append(ideal(es,phase))
    return out

SEEDS=tuple((a,b) for a in range(-5,6) for b in range(-5,6) if 0<norm((a,b))<=13)

def fixture_rows(es):
    # Every one of the 54 seed rows, at explicit denominator-shell translates.
    base=(1,0)
    neutral=[]
    for i,e in enumerate(es):
        if e:base=mul(base,powe(PIS[i],e-1))
        if e and e%6==0:neutral.append(i)
    rows=set()
    for choices in product((0,1,7),repeat=len(neutral)):
        fac=base
        for i,j in zip(neutral,choices):fac=mul(fac,powe(PIS[i],j))
        for x in SEEDS:rows.add(mul(fac,x))
    return tuple(sorted(rows))

def Bvalue(row,Z):
    a,b=row
    return C((a+2*b)%11-5,(2*a-b)%7-3)*F(Z,1+Z)

def bare(es,rows,Z):return {x:gauss_shape(x,es)*Bvalue(x,Z) for x in rows}

def dress(source,ds,Z):
    """source(Z) is a finite row dictionary. Direct push-forward of every row."""
    out=defaultdict(lambda:ZERO)
    for d in ds:
        for x,v in source(Z/F(d.q**6)).items():
            m=mul(powe(d.gen,6),x)
            out[m]=out[m]+d.h*(d.q**3)*v
    return {x:v for x,v in out.items() if v!=ZERO}

def energy(a,T,Z,p,critical=True):
    # Hard-ball norm test; finite fixture, not the manuscript's smooth weight.
    v=sum((z.norm()**(p//2) for x,z in a.items() if norm(x)<=T),F(0))
    return v/(T*(Z**(p//2) if critical else 1))

def weighted_sum(a,T):
    return sum((z*F(1+norm(x),1+T) for x,z in a.items() if norm(x)<=T),ZERO)

def closed_cost(es,p):
    KA=F(1);LN=F(1)
    for i,e in enumerate(es):
        if not e:continue
        q=QS[i]
        if e%6:KA*=1+F((q-1)**p,q**(p+6)-1)
        else:
            if p==2:r=F(1,q**4)
            elif p==4:r=F(1,q*q*isqrt(q)) # upper bound for q^(-5/2)
            else:raise ValueError('fixture uses p=2 or 4')
            LN*=1+F(q-1)*r/(1-r)
    return KA*LN**p

def row_checks():
    report=[]
    cases=((1,1,0,0),(2,0,1,0),(0,0,1,1),(6,0,0,0),(1,6,0,0))
    phase=1
    for es in cases:
        active=[i for i,e in enumerate(es) if e%6]
        neutral=[i for i,e in enumerate(es) if e and e%6==0]
        shared=active+neutral
        coprime=[i for i in range(len(PIS)) if i not in shared][:1]
        aa=boxes(active,1,phase);nn=boxes(neutral,1,phase);bb=boxes(coprime,1,phase)
        ds=boxes(shared+coprime,1,phase)
        rows=fixture_rows(es)
        source=lambda Z:bare(es,rows,Z)
        U=lambda Z:dress(source,bb,Z)
        A=lambda Z:dress(U,aa,Z)
        Z=F(37)
        full=dress(source,ds,Z)
        split=dress(A,nn,Z)
        check(full==split,'full_coprime_shared_factorization')
        T=max(norm(x) for x in full)
        # Includes a restrictive ball, so row-domain changes are tested too.
        for T0 in (F(T),F(max(1,T//5))):
            left=weighted_sum(full,T0)
            direct=ZERO
            for d in ds:
                direct=direct+d.h*d.q**3*sum((v*F(1+norm(x)*d.q**6,1+T0)
                    for x,v in source(Z/F(d.q**6)).items() if norm(x)*d.q**6<=T0),ZERO)
            check(left==direct,'finite_probe_reindexing')
            for p in (2,4):
                lhs=energy(A(Z),T0,Z,p)
                rhs=sum((d.h.norm()**(p//2)*F(1,d.q**6)*
                    energy(U(Z/F(d.q**6)),T0/F(d.q**6),Z/F(d.q**6),p) for d in aa),F(0))
                check(lhs==rhs,'exact_active_shell_energy')
                # All scales needed by the finite rectangular operator are included.
                shared_ds=boxes(shared,1,phase)
                maxref=max(energy(U(Z/F(d.q**6)),T0/F(d.q**6),Z/F(d.q**6),p) for d in shared_ds)
                check(energy(full,T0,Z,p)<=closed_cost(es,p)*maxref,'complete_shared_energy_budget')
            # The unnormalized L2 formula is separate, with a different coefficient.
            rhs0=sum((d.h.norm()*energy(U(Z/F(d.q**6)),T0/F(d.q**6),Z/F(d.q**6),2,False) for d in aa),F(0))
            check(energy(A(Z),T0,Z,2,False)==rhs0,'unnormalized_active_energy')
        report.append({'denominator_prime_exponents':list(es),'seed_rows':len(rows),
            'dilation_ideals':len(ds),'nonzero_output_rows':len(full),
            'row_norm_cap':T,'moments':[2,4]})
    # Direct local support checks on genuine split/conjugate/inert arithmetic.
    for es in cases:
        for row in fixture_rows(es):
            z=gauss_shape(row,es)
            if z!=ZERO:
                for i,e in enumerate(es):
                    if e%6:check(vp(row,PIS[i])[0]==e-1,'physical_active_support')
    # Equal norm does not mean equal ideal: two sixth-power row images differ.
    d0=ideal((1,0,0,0));d1=ideal((0,1,0,0))
    check(d0.q==d1.q,'conjugate_norm_control')
    reject(powe(d0.gen,6)==powe(d1.gen,6),'aliasing_conjugate_ideals_by_norm')
    # Neutral overlap is real, not just an absent proof of disjointness.
    es=(6,0,0,0);row=powe(PIS[0],12)
    reject(gauss_shape(row,es)==ZERO or gauss_shape(divexact(row,powe(PIS[0],6)),es)==ZERO,
           'neutral_shared_terms_are_not_disjoint')
    # A small one-prime fixture records visible failures of tempting substitutions.
    es=(1,0,0,0);rs=((1,0),(1,1));ds=boxes([0],1)
    src=lambda Z:bare(es,rs,Z)
    right=dress(src,ds,F(37));T=max(norm(x) for x in right)
    wrong=defaultdict(lambda:ZERO)
    frozen=defaultdict(lambda:ZERO)
    wrongrow=defaultdict(lambda:ZERO)
    for d in ds:
        for x,v in src(F(37,d.q**6)).items():
            m=mul(powe(d.gen,6),x)
            wrong[m]=wrong[m]+d.h*v
            frozen[m]=frozen[m]+d.h*d.q**3*src(F(37)).get(x,ZERO)
            wrongrow[m]=wrongrow[m]+d.h*d.q**3*gauss_shape(m,es)*Bvalue(m,F(37,d.q**6))
    clean=lambda a:{x:v for x,v in a.items() if v!=ZERO}
    reject(clean(wrong)==right,'omitting_critical_D_cubed_prefactor')
    reject(clean(frozen)==right,'freezing_theta_column_scale')
    reject(clean(wrongrow)==right,'replacing_divided_row_by_undivided_row')
    return report

def coefficient_checks():
    for q in (7,13,25,49):
        for p in (2,4,6,12):
            mass=F(1)
            for j in range(1,13):
                mass+=F((q-1)**p,q**((p+6)*j))
                target=1+F((q-1)**p,q**(p+6)-1)*(1-F(1,q**((p+6)*j)))
                check(mass==target,'critical_active_geometric_mass')
            check(1+F((q-1)**p,q**(p+6)-1)<=1+F(2,q**6),'uniform_active_majorant')
        for phase in range(6):
            eta=ROOTS[phase]
            h=[ONE]+[-eta**j*F(q-1,q**j) for j in range(1,10)]
            for j in range(1,10):
                coeff=h[j]-eta*F(1,q)*h[j-1]
                check(coeff==(-eta if j==1 else ZERO),'signed_local_multiplier')
            for j in range(10):
                sumsq=sum((v.norm() for v in h[:j+1]),F(0))
                check(sumsq==1+F((q-1)**2,q*q-1)*(1-F(1,q**(2*j))),'unnormalized_squared_mass')
        for lam in (F(0),F(1,3),F(2,3),F(1)):
            exp=int(2+6*lam)
            check(exp>0 and 1+F((q-1)**2,q**exp-1)<=F(2*q,q+1),'nonadverse_ray_budget')
    # At lambda=-1/3, every nonconstant squared-mass term has the same size.
    q=7;terms=[F((q-1)**2,q**(2*j))*q**(2*j) for j in range(1,6)]
    check(terms==[F((q-1)**2)]*5,'ray_endpoint_terms')
    reject(terms[-1]==0,'infinite_endpoint_mass_converges')


def sharpness_checks():
    # Actual inert generator 5, norm 25; all amplitudes remain rational.
    q=25
    for p in (2,4):
        for J in range(6):
            T=Z=F(5**(12*J));out={};mass=F(0)
            for j in range(J+1):
                h=ONE if j==0 else -ROOTS[j%6]*F(q-1,q**j)
                amplitude=h*q**(3*j)*5**((6+12//p)*(J-j))
                out[powe(PIS[2],6*j)]=amplitude
                mass+=h.norm()**(p//2)*F(1,q**(6*j))
            check(energy(out,T,Z,p)==mass,'critical_operator_sharpness')
            check(mass>=1,'identity_channel_survives')
    reject(mass<=F(1,T),'universal_power_saving_from_shared_operator')

def main():
    if any(norm(pi)!=q for pi,q in zip(PIS,QS)):raise RuntimeError('prime norm mismatch')
    check(len(SEEDS)==54,'fixture_setup')
    gauss=local_gauss_checks()
    rows=row_checks()
    coefficient_checks()
    sharpness_checks()
    output={'status':'PASS: finite algebra and finite-support fixtures only',
            'arithmetic':'exact integers, fractions and cyclotomic polynomial reduction',
            'predicates':sum(COUNTS.values()),'groups':dict(sorted(COUNTS.items())),
            'negative_controls':NEGATIVE,'gauss_coverage':gauss,'row_fixtures':rows,
            'not_claimed':['native ideal census','infinite theta or Gaussian evaluation',
                           'asymptotic proof','independent mathematical review','Lean build']}
    print(json.dumps(output,indent=2,sort_keys=True))
if __name__=='__main__':main()
