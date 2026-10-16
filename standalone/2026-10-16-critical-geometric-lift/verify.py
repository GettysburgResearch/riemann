#!/usr/bin/env python3
"""Exact finite diagnostics, not an analytic/RH certificate. Standard library only.

The physical fixtures use five named Eisenstein prime ideals, NOT all ideals
below the norm caps. Normal and -O executions use explicit checks (no assert).
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
from collections import Counter
import json

COUNTS: Counter[str] = Counter()
def check(ok: bool, group: str) -> None:
    COUNTS[group] += 1
    if not ok:
        raise ValueError(f'failed {group} predicate {COUNTS[group]}')

@dataclass(frozen=True)
class C:
    """a+b*omega, omega^2+omega+1=0."""
    a: F = F(0)
    b: F = F(0)
    def __post_init__(self):
        object.__setattr__(self, 'a', F(self.a))
        object.__setattr__(self, 'b', F(self.b))
    def __add__(self, other):
        o = other if isinstance(other, C) else C(other)
        return C(self.a+o.a, self.b+o.b)
    __radd__ = __add__
    def __neg__(self): return C(-self.a, -self.b)
    def __sub__(self, other): return self + (-other if isinstance(other, C) else -F(other))
    def __mul__(self, other):
        o = other if isinstance(other, C) else C(other)
        return C(self.a*o.a-self.b*o.b, self.a*o.b+self.b*o.a-self.b*o.b)
    __rmul__ = __mul__
    def __pow__(self, n: int):
        if n < 0: raise ValueError('nonnegative exponent required')
        r, x = C(1), self
        while n:
            if n & 1: r = r*x
            x, n = x*x, n//2
        return r
    def conj(self): return C(self.a-self.b, -self.b)
    def norm(self): return self.a*self.a-self.a*self.b+self.b*self.b

@dataclass(frozen=True)
class E:
    """a+sqrt(5)*b over Q(omega). Complex conjugation fixes sqrt(5)."""
    a: C = C()
    b: C = C()
    def __add__(self, o): return E(self.a+o.a, self.b+o.b)
    def __neg__(self): return E(-self.a, -self.b)
    def __sub__(self, o): return self + (-o)
    def __mul__(self, o): return E(self.a*o.a+5*(self.b*o.b), self.a*o.b+self.b*o.a)
    def scale(self, x): return E(self.a*x, self.b*x)
    def conj(self): return E(self.a.conj(), self.b.conj())
    def norm(self): return self*self.conj()
    def real(self): return (self+self.conj()).scale(F(1,2))
    def fourth(self):
        n = self.norm()
        return n*n
    def rational(self):
        check(self.b == C() and self.a.b == 0, 'rational_descent')
        return self.a.a

ATOMS = (E(C(F(1,2)), C(F(1,2))), E(C(F(1,2)), C(F(-1,2))))
PROBS = (E(C(F(1,2)), C(F(-1,10))), E(C(F(1,2)), C(F(1,10))))
ONE, ZERO = E(C(1)), E()
EPS = C(0,-1)  # -omega, a primitive sixth root
ROOTS = tuple(EPS**j for j in range(6))


def mul_series(a, b, n):
    out = [C() for _ in range(n+1)]
    for i in range(min(n, len(a)-1)+1):
        for j in range(min(n-i, len(b)-1)+1): out[i+j] = out[i+j]+a[i]*b[j]
    return out


def div_series(a, b, n):
    if b[0] != C(1): raise ValueError('unit constant required')
    out = [C() for _ in range(n+1)]
    for i in range(n+1):
        out[i] = a[i] if i < len(a) else C()
        for j in range(1, min(i,len(b)-1)+1): out[i] = out[i]-b[j]*out[i-j]
    return out


def local_checks():
    n = 30
    R = F(5,3)
    for q in (7,13,25,49):
        r, a = F(1,q), 1-F(1,q)
        nx = [C(1),C(-R)]
        ny = [C(1)]+[C()]*5+[C(-q*q)]
        denplus = mul_series(nx,ny,n)
        denminus = [C(1),C(-R*a)]+[C()]*4+[C(-q*q)]
        numer = [C(),C(R*r)]+[C()]*5+[C(R*q*q)]
        vp, vm = div_series(numer,denplus,n), div_series(numer,denminus,n)
        vp[0], vm[0] = C(1), C(1)
        for eta in ROOTS:
            for z in (C(1),C(-1),C(R),ROOTS[2]*R):
                src = [C(1)]+[C() for _ in range(n)]
                for j in range((n-1)//6+1): src[6*j+1] = -z*a*(eta**j)*(q**(2*j))
                native = [C(1),-z]
                forward = div_series(src,native,n)
                inverse = div_series(native,src,n)
                check(mul_series(forward,native,n)==src,'local_series')
                want = native+[C()]*(n+1-len(native))
                check(mul_series(inverse,src,n)==want,'local_series')
                for j in range(n+1):
                    check(vp[j].b==0 and vp[j].a>=0 and forward[j].norm()<=vp[j].a**2,'coefficient_majorants')
                    check(vm[j].b==0 and vm[j].a>=0 and inverse[j].norm()<=vm[j].a**2,'coefficient_majorants')
        if q in (25,49):
            sq = 5 if q == 25 else 7
            t = F(1,sq)
            limit = 1+F(35,3)*F(1,sq**3)
            for v in (vp,vm):
                check(sum(v[j].a*t**j for j in range(n+1))<=limit,'critical_mass')
    for q in range(7,102):
        for j in range(10):
            check(sum((1-F(1,q))*F(1,q)**i for i in range(j+1))==1-F(1,q)**(j+1),'geometric_mass')
    # Exact endpoint ratio and simultaneous-dilation exponent, rational inputs.
    for q in (7,13,25):
        for eta in ROOTS:
            h = [C(1)]+[-(eta**j)*F(q-1,q**j) for j in range(1,13)]
            check(mul_series(h,[C(1),-eta*F(1,q)],12)==[C(1),-eta]+[C()]*11,'homothety_euler_ratio')
    for xi,z,w in product((F(1,2),F(3,7),F(2),F(5,6)),repeat=3):
        check(-6*(F(1,2)-z)-6*(xi+z-1)==3-6*xi,'mellin_scaling')

# Five named prime ideals in Z[omega]. Split roots label distinct conjugates.
PRIMES = ((7,2),(7,4),(13,3),(19,7),(25,None))
QS = tuple(p[0] for p in PRIMES)
ROWS = tuple((a,b) for a in range(-5,6) for b in range(-5,6) if 0<a*a-a*b+b*b<=13)


def ringmul(x,y,p):
    a,b=x; c,d=y
    return ((a*c-b*d)%p,(a*d+b*c-b*d)%p)


def ringpow(x,n,p):
    r=(1,0)
    while n:
        if n&1: r=ringmul(r,x,p)
        x,n=ringmul(x,x,p),n//2
    return r


def symbol(row, prime):
    a,b=row; q,r=prime
    if r is not None:
        x=(a+b*r)%q
        if x==0: return C()
        v=pow(x,(q-1)//6,q)
        vals=[pow(-r%q,j,q) for j in range(6)]
    else:
        x=(a%5,b%5)
        if x==(0,0): return C()
        v=ringpow(x,4,5)
        vals=[ringpow((0,4),j,5) for j in range(6)]
    check(len(set(vals))==6 and v in vals,'field_setup')
    return ROOTS[vals.index(v)]


def columns(cap):
    """All 0 or 1 mod 6 exponent columns in ONLY the five-prime semigroup."""
    out=[]
    def rec(i,n,exps):
        if i==len(QS): out.append((n,tuple(exps))); return
        q=QS[i]
        rec(i+1,n,exps+[0])
        e=1
        while n*q**e<=cap:
            rec(i+1,n*q**e,exps+[e]); e+=6
    rec(0,1,[])
    return sorted(out)


def ccoeff(exps,etas):
    v=C(1)
    for q,e,eta in zip(QS,exps,etas):
        if e: v=v*(-F(q-1,q))*(eta**((e-1)//6))*q**(2*((e-1)//6))
    return v


def phase(exps,syms):
    v=C(1)
    for e,x in zip(exps,syms):
        if e: v=v*x**e
    return v


def polynomial(cols,syms,etas,lower,upper,excluded=None):
    pol={}
    for n,es in cols:
        if not lower<n<=upper or (excluded is not None and es[excluded]): continue
        mask=sum(1<<i for i,e in enumerate(es) if e)
        pol[mask]=pol.get(mask,C())+ccoeff(es,etas)*phase(es,syms)
    return {m:c for m,c in pol.items() if c!=C()}


def evaluate(pol,values):
    mon=[ONE]*32
    for m in range(1,32):
        bit=m&-m; i=bit.bit_length()-1
        mon[m]=mon[m^bit]*values[i]
    ans=ZERO
    for m,c in pol.items(): ans=ans+mon[m].scale(c)
    return ans


def assignments(indices):
    for bits in product((0,1),repeat=len(indices)):
        vals=[ONE]*5; pr=ONE
        for i,b in zip(indices,bits): vals[i]=ATOMS[b]; pr=pr*PROBS[b]
        yield vals,pr


def flow(pol,order):
    g=ZERO
    for vals,pr in assignments(order): g=g+pr*evaluate(pol,vals).fourth()
    inj=ZERO; comp=ZERO
    step_signs=[]
    for j,i in enumerate(order):
        iu=ZERO; dd=ZERO
        for vals,pr in assignments(order[j+1:]):
            vals[i]=ZERO; u=evaluate(pol,vals)
            vals[i]=ONE; v=evaluate(pol,vals)-u
            iu=iu+(pr*u.norm()*(u*v.conj()).real()).scale(4)
            dd=dd+pr*v.fourth()
        inj=inj+iu; comp=comp+dd
        f=(iu-dd).rational()
        step_signs.append(1 if f>0 else -1 if f<0 else 0)
    native=evaluate(pol,[ONE]*5).fourth().rational()
    gr,ir,dr=g.rational(),inj.rational(),comp.rational()
    check(native==gr+ir-dr,'lifted_flow')
    check(dr>=0,'lifted_flow')
    return gr,ir,dr,native,step_signs


def coercivity_checks():
    # Same inherited local theorem as #946; a separate same-author finite implementation here.
    pairs=(C(), C(1), C(-1), ROOTS[2], C(1,1))
    def power_e(v,n):
        out=ONE
        for _ in range(n): out=out*v
        return out
    for k in range(2,7):
        ck=F((2*k)*(2*k-1)*(2*k-2)*(2*k-3),24)*F(8,75)**(k-2)
        for u,v in product(pairs,repeat=2):
            eu,ev=E(u),E(v)
            expect=ZERO
            for z,pr in zip(ATOMS,PROBS):
                expect=expect+pr*power_e((eu+z*ev).norm(),k)
            endpoint=(u+v).norm()**k
            injection=2*k*u.norm()**(k-1)*(u*v.conj()).a- k*u.norm()**(k-1)*(u*v.conj()).b
            remainder=expect.rational()-endpoint+injection
            check(remainder>=ck*v.norm()**k,'inherited_all_order_coercivity')
            if k==2: check(remainder==v.norm()**2,'fourth_compensation_exact')


def physical_checks():
    check(len(ROWS)==54,'coverage')
    report=[]
    for cap in (128,10**6,10**8):
        cols=columns(cap)
        etas=tuple(ROOTS[(2*i+1)%6] for i in range(5))
        # Direct local exponent assembly versus radical/geometric formula.
        for n,es in cols:
            b=1; g=1; weight=F(1); eg=C(1); parity=1
            for q,e,eta in zip(QS,es,etas):
                if e:
                    j=(e-1)//6; b*=q; g*=q**j
                    parity*=-1; weight*=F(q-1,q); eg=eg*eta**j
            check(n==b*g**6,'radical_lift')
            check(ccoeff(es,etas)==eg*(parity*weight*g*g),'radical_lift')
        for row in ROWS:
            syms=tuple(symbol(row,p) for p in PRIMES)
            for _,es in cols:
                rad=tuple(int(e>0) for e in es)
                check(phase(es,syms)==phase(rad,syms),'literal_radical_masks')
            pol=polynomial(cols,syms,etas,F(cap,8),cap)
            # Exact cofactor at each prime, with all shorter column scales.
            for i,q in enumerate(QS):
                direct=sum((c for mask,c in pol.items() if mask&(1<<i)),C())
                rhs=C(); j=0
                while q**(6*j+1)<=cap:
                    scale=q**(6*j+1)
                    rest=polynomial(cols,syms,etas,F(cap,8*scale),F(cap,scale),excluded=i)
                    rs=sum(rest.values(),C())
                    rhs=rhs+rs*(-F(q-1,q))*etas[i]**j*q**(2*j)*syms[i]**(6*j+1)
                    j+=1
                check(direct==rhs,'physical_cofactor')
        # Seven declared actual rows for exact Mammen-flow tests.
        chosen=((1,0),(0,1),(1,1),(2,0),(3,1),(1,3),(4,1))
        totals=[F(0)]*4; signs=set()
        for row in chosen:
            check(row in ROWS,'coverage')
            syms=tuple(symbol(row,p) for p in PRIMES)
            pol=polynomial(cols,syms,etas,F(cap,8),cap)
            a=flow(pol,tuple(range(5)))
            b=flow(pol,tuple(reversed(range(5))))
            check(a[0]==b[0] and a[3]==b[3] and a[1]-a[2]==b[1]-b[2],'order_reunion')
            totals=[x+y for x,y in zip(totals,a[:4])]; signs.update(a[4])
        report.append({'cap':cap,'window':'cap/8 < Nn <= cap','semigroup_columns_under_cap':len(cols),
                       'rows_for_masks_and_cofactors':54,'rows_for_flow':len(chosen),
                       'G_I_D_M':[str(x) for x in totals],'restoration_signs':sorted(signs)})
    return report


def negative_controls():
    # These are direct false-substitution controls, not package mutation tests.
    q=7; eta=ROOTS[1]
    check(-F(q-1,q)*eta*q*q != C(),'negative_missing_lift')
    check(C(2)*(-F(q-1,q))*eta*q*q != C(2)**7*(-F(q-1,q))*eta*q*q,'negative_support_power')
    check(symbol((1,0),PRIMES[0])!=symbol((7**6,0),PRIMES[0]),'negative_row_mask_freezing')
    xi,z,w=F(3,4),F(1,6),F(2)
    right=3-6*xi
    check(-6*(xi+z-1)!=right,'negative_Z_only')
    check(right-6*(w-1)!=right,'negative_Y_dilation')
    check(-F(q-1,q)*eta != -eta,'negative_old_stripping_weight')
    # Scale envelopes cannot be replaced by a same-scale inequality.
    cap=2**20; cols=columns(cap); syms=tuple(symbol((1,0),p) for p in PRIMES)
    pol=polynomial(cols,syms,(C(1),)*5,F(cap,2),cap)
    native=sum((phase(es,syms)*((-1)**sum(e>0 for e in es)) for n,es in cols
                if F(cap,2)<n<=cap and all(e in (0,1) for e in es)),C())
    check(native==C() and sum(pol.values(),C())!=C(),'negative_fixed_scale_comparison')


def main():
    local_checks()
    coercivity_checks()
    cases=physical_checks()
    negative_controls()
    print(json.dumps({'status':'finite identities only; no RH or asymptotic certificate',
                      'arithmetic':'exact Fraction, Q(omega), Q(omega,sqrt(5))',
                      'prime_ideals':[{'norm':q,'omega_root':r} for q,r in PRIMES],
                      'scope':'Only this five-prime semigroup; not a full native ideal census.',
                      'cases':cases,'predicates_by_group':dict(sorted(COUNTS.items())),
                      'total_predicates':sum(COUNTS.values())},indent=2,sort_keys=True))

if __name__=='__main__': main()
