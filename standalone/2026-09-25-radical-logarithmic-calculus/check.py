#!/usr/bin/env python3
"""RLC35 primitive replay. Standard library only; acceptance never uses floats."""
from __future__ import annotations
import argparse
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import json
from math import factorial
from pathlib import Path
import sys

COUNTS: Counter[str] = Counter()

def require(ok: bool, label: str) -> None:
    if not ok:
        raise ValueError(label)
    COUNTS[label] += 1

def eq(a, b, label: str) -> None:
    require(a == b, label)


def sieve(n: int):
    mu = [1]*(n+1); mu[0] = 0
    factors = [{} for _ in range(n+1)]
    for p in range(2, n+1):
        if factors[p]:
            continue
        for j in range(p, n+1, p):
            q, e = j, 0
            while q % p == 0:
                q //= p; e += 1
            factors[j][p] = e
            mu[j] = 0 if e > 1 else -mu[j]
    return mu, factors


def conv(a, b, n: int):
    out = [0]*(n+1)
    for d in range(1, min(n, len(a)-1)+1):
        if not a[d]:
            continue
        for j in range(1, min(n//d, len(b)-1)+1):
            if b[j]:
                out[d*j] += a[d]*b[j]
    return out


def energy(c, n: int) -> F:
    total = F(0); s = F(0)
    for j in range(1, n+1):
        s += c[j] if j < len(c) else 0
        total += s*s/F(j*(j+1))
    return total


def fjson(x: F):
    x = F(x)
    return {"num": x.numerator, "den": x.denominator}

# Multivariate polynomials in formal prime logarithms; variable 0 denotes u.
Poly = dict[tuple[int, ...], F]

def const(x=0) -> Poly:
    return {(): F(x)} if x else {}

def add(*args: Poly) -> Poly:
    out: Poly = {}
    for p in args:
        for m, c in p.items():
            out[m] = out.get(m, F(0))+c
    return {m:c for m,c in out.items() if c}

def scale(p: Poly, c) -> Poly:
    return {m:v*F(c) for m,v in p.items() if v*c}

def mul(p: Poly, q: Poly) -> Poly:
    out: Poly = {}
    for a,x in p.items():
        for b,y in q.items():
            m = tuple(sorted(a+b))
            out[m] = out.get(m,F(0))+x*y
    return {m:c for m,c in out.items() if c}

def power(p: Poly, k: int) -> Poly:
    out = const(1)
    for _ in range(k):
        out = mul(out,p)
    return out

def logpoly(n: int, factors) -> Poly:
    return {(p,):F(e) for p,e in factors[n].items()}

def pconv(a: list[Poly], b: list[Poly], n: int) -> list[Poly]:
    out = [{} for _ in range(n+1)]
    for d in range(1,min(n,len(a)-1)+1):
        if not a[d]: continue
        for j in range(1,min(n//d,len(b)-1)+1):
            if b[j]: out[d*j] = add(out[d*j],mul(a[d],b[j]))
    return out

def at_u(p: Poly, t: Poly) -> Poly:
    out = {}
    for m,c in p.items():
        r = m.count(0)
        rest = tuple(x for x in m if x)
        out = add(out,mul({rest:c},power(t,r)))
    return out

def integral_exp(p: Poly, j: int, factors) -> Poly:
    """Exact integral e^-u p(u) from log j to log(j+1)."""
    primitive = {}
    for m,c in p.items():
        r = m.count(0); rest = tuple(x for x in m if x)
        for v in range(r+1):
            term = tuple([0]*v)+rest
            primitive[term] = primitive.get(term,F(0))+c*F(factorial(r),factorial(v))
    return add(scale(at_u(primitive,logpoly(j,factors)),F(1,j)),
               scale(at_u(primitive,logpoly(j+1,factors)),F(-1,j+1)))

def phash(p: Poly) -> str:
    rows = [[list(m), c.numerator,c.denominator] for m,c in sorted(p.items())]
    return hashlib.sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()

BITS = 112
SCALE = 1 << BITS

def ceildiv(a: int, b: int) -> int:
    return -((-a)//b)

@lru_cache(None)
def ln_interval(n: int) -> tuple[int,int]:
    if n == 1: return 0,0
    def atanh_bound(x: F):
        t = (x-1)/(x+1); t2=t*t
        total=F(0); z=t
        for k in range(64):
            total += 2*z/F(2*k+1); z *= t2
        return total, total+2*z/F(129)/(1-t2)
    k = n.bit_length()-1
    a,b=atanh_bound(F(2)); c,d=atanh_bound(F(n,1<<k))
    lo,hi=k*a+c,k*b+d
    return lo.numerator*SCALE//lo.denominator,ceildiv(hi.numerator*SCALE,hi.denominator)


def imul(a,b):
    vals = [x*y for x in a for y in b]
    return min(vals)//SCALE, ceildiv(max(vals),SCALE)

def peval(p: Poly):
    lo=hi=0
    for m,c in p.items():
        v=(SCALE,SCALE)
        for t in m:
            if not t: raise ValueError('unevaluated u')
            v=imul(v,ln_interval(t))
        vals=[x*c.numerator for x in v]
        lo += min(vals)//c.denominator
        hi += ceildiv(max(vals),c.denominator)
    return lo,hi

def interval_json(p: Poly):
    a,b=peval(p); shift=1<<(BITS-40)
    a,b=a//shift,ceildiv(b,shift)
    return {"lower_num":a,"upper_num":b,"den":1<<40,
            "display":[a/(1<<40),b/(1<<40)]}

@dataclass(frozen=True)
class G:
    """Exact Gaussian rational for the phase-sensitive controls."""
    re: F = F(0)
    im: F = F(0)
    @staticmethod
    def coerce(z):
        return z if isinstance(z,G) else G(F(z))
    def __add__(self,z):
        z=G.coerce(z); return G(self.re+z.re,self.im+z.im)
    __radd__=__add__
    def __neg__(self): return G(-self.re,-self.im)
    def __sub__(self,z): return self+-G.coerce(z)
    def __rsub__(self,z): return G.coerce(z)+-self
    def __mul__(self,z):
        z=G.coerce(z)
        return G(self.re*z.re-self.im*z.im,self.re*z.im+self.im*z.re)
    __rmul__=__mul__
    def __bool__(self): return bool(self.re or self.im)
    def __eq__(self,z):
        try: z=G.coerce(z)
        except (ValueError,TypeError): return False
        return self.re==z.re and self.im==z.im
    def conj(self): return G(self.re,-self.im)
    def as_json(self): return {"re":fjson(self.re),"im":fjson(self.im)}


def adjoint_kernel(a, phi, n: int):
    return [0]+[sum((a[d]*phi[d*m] for d in range(1,n//m+1)),0)
                for m in range(1,n+1)]


def kernel(n: int, x: int) -> F:
    # g(t)=(1-t)^4 on (0,1); Phi(n)=sum_j g(j*x/n)/n.
    return sum((F(n-j*x,n)**4 for j in range(1,(n-1)//x+1)),F(0))/n


def polynomial_panels(mu, factors):
    panels=[]; U={(0,):F(1)}
    for n,k in [(7,1),(7,2),(7,3),(15,1),(15,2),(15,3),(31,1),(31,2),(63,1)]:
        prefix={}; m=0; iprefix={}
        norm={}; moment={}; ynorm={}; ymoment={}
        for j in range(1,n+1):
            m += mu[j]
            prefix=add(prefix,scale(power(logpoly(j,factors),k),mu[j]))
            norm=add(norm,scale(mul(prefix,prefix),F(1,j*(j+1))))
            moment=add(moment,scale(integral_exp(power(U,2*k),j,factors),m*m))
            offset=add(iprefix,scale(power(logpoly(j,factors),k),F(-m,k)))
            ycell=add(scale(power(U,k),F(m,k)),offset)
            eq(add(scale(power(U,k),m),scale(ycell,-k)),prefix,
               'weighted_source_Abel_cell')
            ysquare=mul(ycell,ycell)
            ynorm=add(ynorm,integral_exp(ysquare,j,factors))
            ymoment=add(ymoment,integral_exp(mul(U,ysquare),j,factors))
            iprefix=at_u(ycell,logpoly(j+1,factors))
        boundary=scale(mul(logpoly(n+1,factors),mul(iprefix,iprefix)),F(k,n+1))
        positivebulk=scale(ymoment,k)
        rhs=add(moment,scale(ynorm,k*(k+1)))
        lhs=add(norm,positivebulk,boundary)
        eq(lhs,rhs,'all_order_quadratic_identity')
        for label,p in [('norm',norm),('positive_bulk',positivebulk),('boundary',boundary)]:
            require(peval(p)[0]>=0,'positive_term_interval')
        panels.append({'N':n,'order':k,'norm':interval_json(norm),
                       'moment':interval_json(moment),'positive_bulk':interval_json(positivebulk),
                       'boundary':interval_json(boundary),
                       'rhs_sha256':phash(rhs),'identity_residual_terms':len(add(lhs,scale(rhs,-1)))})
    return panels


def defect_panel(y: int, kind: str, mu, factors):
    b=(y+1)**2+3
    c=[F(0)]*(b+1)
    for n in range(1,y+1): c[n]=F(mu[n])
    c[y+1]=-(y+1)*sum((F(mu[n],n) for n in range(1,y+1)),F(0))
    eq(sum((c[n]/n for n in range(1,b+1)),F(0)),0,'completion_balance')
    if kind=='damping':
        chi=[F(0)]+[F(1,n) for n in range(1,b+1)]
    else:
        roots=[G(F(1)),G(F(0),F(1)),G(F(-1)),G(F(0),F(-1))]
        chi=[G()]+[roots[sum(factors[n].values())%4] for n in range(1,b+1)]
    muc=[0]+[mu[n]*chi[n] for n in range(1,b+1)]
    ones=[0]+[1]*b
    a=conv(ones,muc,b); nu=conv(ones,c,b)
    cc=[0]+[c[n]*chi[n] for n in range(1,b+1)]
    ac=conv(a,c,b)
    residual=[0]+[ac[n]-cc[n] for n in range(1,b+1)]
    delta=[0]+[nu[n]-nu[n]*chi[n] for n in range(1,b+1)]
    independent=conv(muc,delta,b)
    for n in range(1,b+1):
        eq(residual[n],independent[n],'primitive_modulation_defect')
        if n<=y: eq(residual[n],0,'defect_native_prefix_vanishes')
    z=conv(c,c,b); aa=conv(a,a,b)
    left=conv(aa,z,b); linear=conv(cc,residual,b); square=conv(residual,residual,b)
    for n in range(1,b+1):
        eq(left[n],z[n]*chi[n]+2*linear[n]+square[n],'tensor_defect_identity')
        if n<(y+1)**2: eq(square[n],0,'square_defect_strict_support')
    eq(square[(y+1)**2],residual[y+1]*residual[y+1],'square_defect_endpoint')
    x=8 if y==2 else max(1,(y+1)**2//2)
    phi=[0]+[kernel(n,x) for n in range(1,b+1)]
    adj=adjoint_kernel(a,adjoint_kernel(a,phi,b),b)
    lhs=sum((z[n]*(adj[n]-chi[n]*phi[n]) for n in range(1,b+1)),0)
    rhs=sum(((2*linear[n]+square[n])*phi[n] for n in range(1,b+1)),0)
    eq(lhs,rhs,'bilinear_Hankel_adapter')
    if kind=='gaussian':
        aconj=[v.conj() if isinstance(v,G) else v for v in a]
        wrong=adjoint_kernel(aconj,adjoint_kernel(aconj,phi,b),b)
        wronglhs=sum((z[n]*(wrong[n]-chi[n]*phi[n]) for n in range(1,b+1)),0)
        require(wronglhs!=rhs,'Hermitian_replacement_rejected')
    if y==2 and kind=='damping':
        eq(residual[3],F(-1,3),'explicit_first_defect')
        eq(square[9],F(1,9),'explicit_square_endpoint')
        eq(phi[9],F(1,9**5),'product_kernel_beyond_observation')
        eq(square[9]*phi[9],F(1,9**6),'masked_quadratic_residual')
    return {'Y':y,'B':b,'character':kind,
            'first_defect_at_Yplus1':residual[y+1].as_json() if isinstance(residual[y+1],G) else fjson(residual[y+1]),
            'pairing':lhs.as_json() if isinstance(lhs,G) else fjson(lhs)}


def build():
    COUNTS.clear()
    mu,factors=sieve(511)
    # Independent triangular Dirichlet inversion, not the sieve's prime signs.
    inv=[0]*512; inv[1]=1
    sums=[0]*512
    for n in range(1,512):
        if n>1: inv[n]=-sums[n]
        eq(mu[n],inv[n],'Mobius_primitive_authentication')
        for m in range(2*n,512,n): sums[m]+=inv[n]
    bad=mu.copy(); bad[6] += 1
    require(conv(bad,[0]+[1]*511,511)[6]!=0,'corrupt_Mobius_rejected')
    # Classification with an unrelated deterministic radical-invariant kernel.
    rad=[1]*512
    for n in range(1,512):
        for p in factors[n]: rad[n]*=p
    ar=[0]+[F((rad[n]*17)%29-14,1+rad[n]%7) for n in range(1,512)]
    br=conv(ar,mu,511)
    for n in range(1,512):
        if not mu[n]: eq(br[n],0,'radical_classification_nonsquarefree')
    eq(conv(br,[0]+[1]*511,511),ar,'radical_classification_reconstruction')
    identity=[0]+list(range(1,512))
    require(conv(identity,mu,511)[4]!=0,'nonradical_kernel_rejected')

    # Exact formal logarithmic derivative algebra through order four.
    nmax=127; ones=[{}]+[const(1) for _ in range(nmax)]
    pmu=[const(x) for x in mu[:nmax+1]]
    logs=[{}]+[logpoly(n,factors) for n in range(1,nmax+1)]
    lam=[{} for _ in range(nmax+1)]
    for n in range(2,nmax+1):
        if len(factors[n])==1:
            p=next(iter(factors[n])); lam[n]={(p,):F(1)}
    ak=[]
    for k in range(5):
        source=[{}]+[scale(power(logs[n],k),mu[n]) for n in range(1,nmax+1)]
        a=pconv(ones,source,nmax); ak.append(a)
        restored=pconv(a,pmu,nmax)
        for n in range(1,nmax+1):
            eq(restored[n],source[n],'complete_logarithmic_divisor_identity')
            eq(a[n],a[rad[n]],'log_kernel_radical_invariance')
            if len(factors[n])>k: eq(a[n],{},'prime_cube_degree_support')
        if k:
            prev=ak[k-1]; convolution=pconv(lam,prev,nmax)
            for n in range(1,nmax+1):
                eq(a[n],add(mul(logs[n],prev[n]),scale(convolution[n],-1)),
                   'logarithmic_kernel_recurrence')
    for n in range(2,nmax+1):
        ps=list(factors[n])
        expected=scale(power({(ps[0],):F(1)},2),-1) if len(ps)==1 else (
            {(min(ps),max(ps)):F(2)} if len(ps)==2 else {})
        eq(ak[2][n],expected,'two_prime_complete_kernel')

    covariance=[]
    for n in [15,31,63]:
        m=[0]*(n+1)
        for j in range(1,n+1): m[j]=m[j-1]+mu[j]
        gram={}
        for d in range(1,n+1):
            for e in range(d,n+1):
                v=sum((F(m[j//d]*m[j//e],j*(j+1)) for j in range(max(d,e),n+1)),F(0))
                gram[d,e]=v
        for sigma in [1,2]:
            source=[F(0)]+[F(mu[j],j**sigma) for j in range(1,n+1)]
            a=conv([0]+[1]*n,source,n)
            for j in range(1,n+1):
                prod=F(1)
                for p in factors[j]: prod*=1-F(1,p**sigma)
                eq(a[j],prod,'damped_Euler_product')
            eq(conv(a,mu,n),source,'damped_native_source_identity')
            expanded=F(0)
            for (d,e),v in gram.items():
                expanded+=(1 if d==e else 2)*a[d]*a[e]*v
            direct=energy(source,n)
            eq(expanded,direct,'complete_composite_covariance_energy')
            require(direct<=(1+2*sigma)**2*energy(mu,n),'bounded_profile_energy_panel')
            # Off-grid rational x: authenticate the actual Abel identity.
            for j in range(1,n+1):
                x=F(2*j+1,2)
                integral=F(0)
                for h in range(1,j+1):
                    right=x if h==j else F(h+1)
                    integral+=m[h]*(F(1,h**sigma)-right**(-sigma))
                expected=F(m[j])*x**(-sigma)+integral
                eq(expected,sum(source[1:j+1],F(0)),'off_grid_Abel_identity')
            covariance.append({'N':n,'damping':sigma,'full_pairs':n*n,
                               'energy':fjson(direct)})
    eq(conv([0,F(1),F(1,2)],[0,F(1),F(1,2)],2)[2],F(1),
       'native_only_operator_control')
    require(F(1)!=F(3,4),'false_operator_group_law_rejected')
    # Phase multiplier maximum at tau=3/4, kappa=2; all rational frequencies.
    tau=F(3,4)
    for h in range(-80,81):
        xi=F(h,8)
        ratio=(F(1,4)+(xi-tau)**2)/(F(1,4)+xi**2)
        require(F(1,4)<=ratio<=4,'phase_multiplier_rational_panel')
    eq((F(1,4)+(F(-1,4)-tau)**2)/(F(1,4)+F(-1,4)**2),F(4),
       'sharp_phase_constant')

    polynomials=polynomial_panels(mu,factors)
    defects=[defect_panel(y,'damping',mu,factors) for y in [2,3,5,7,15]]
    defects.append(defect_panel(5,'gaussian',mu,factors))
    repair=[]
    for n in [2,7,31,127]:
        s=F(0); J=F(0)
        c=[F(0)]*(n+2); c[1]=F(1); c[2]=F(-1); c[n+1]-=F(n+1,2)
        for j in range(1,n+1):
            s+=c[j]/j; J+=s*s
        eq(J,1+F(n-1,4),'terminal_balance_cost')
        eq(s+c[n+1]/(n+1),0,'terminal_balance_restored')
        eq(energy(c,n),F(1,2),'cumulative_metric_stays_bounded')
        repair.append({'N':n,'J':fjson(J),'E_prefix':fjson(energy(c,n))})
    root=Path(__file__).resolve().parent
    return {'packet':'RLC35','version':1,'arithmetic':'integer/Fraction/formal prime logs/Gaussian rationals',
            'source_sha256':{name:hashlib.sha256((root/name).read_bytes()).hexdigest()
                             for name in ['check.py','PROOF.md']},
            'finite_predicates':sum(COUNTS.values()),'counts':dict(sorted(COUNTS.items())),
            'native_authentication_through':511,'log_kernel_orders':[0,1,2,3,4],
            'log_kernel_cutoff':127,'covariance_panels':covariance,
            'quadratic_polynomial_panels':polynomials,'defect_panels':defects,
            'terminal_repair_panels':repair,
            'not_claimed':['independent mathematical review','formal proof','full Newton covariance bound',
                           'native asymptotic energy improvement','RH']}


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    parser.add_argument('--check',type=Path)
    args=parser.parse_args()
    try:
        report=build()
        if args.check:
            expected=json.loads(args.check.read_text(encoding='utf-8'))
            if report!=expected: raise ValueError('receipt does not match primitive replay')
        text=json.dumps(report,indent=2,sort_keys=True)+'\n'
        if args.output: args.output.write_text(text,encoding='utf-8')
        else: print(text,end='')
    except (ValueError,OSError,TypeError) as exc:
        print('REJECT: '+str(exc),file=sys.stderr)
        return 1
    return 0

if __name__=='__main__':
    raise SystemExit(main())
