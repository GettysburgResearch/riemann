#!/usr/bin/env python3
"""Exact finite checks of local identities and exponent budgets, not analytic certification."""
from __future__ import annotations
from collections import defaultdict
from fractions import Fraction as Q
from itertools import product
import json
import sys

# Mutation runner alters these actual model switches in isolated copies.
KEEP_NONUNIT_ZERO = True
KEEP_J5_BOUNDARY = True
KEEP_VALUATION_SUPPORT = True
KEEP_RAMIFIED_UNIT_PHASE = True
USE_SHIFTED_B = True
USE_SHIFTED_MOLLIFIER = True
KEEP_DUAL_CONDUCTOR = True
COUNT_POWER = Q(1, 4)
CHECKS = 0


def need(test: bool, label: str) -> None:
    global CHECKS
    CHECKS += 1
    if not test:
        raise ValueError(label)


# Z[zeta_6,zeta_(p^n)] in the basis (1,omega), omega^2+omega+1=0.
SIX = [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1)]

def pa(x, y): return (x[0]+y[0], x[1]+y[1])
def pn(x): return (-x[0], -x[1])
def pm(x, y):
    return (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0]-x[1]*y[1])

def canonical(raw, p, level):
    if level == 0:
        out = (0, 0)
        for val in raw.values(): out = pa(out, val)
        return {} if out == (0, 0) else {0: out}
    mod, step = p**level, p**(level-1)
    d = {}
    for key, val in raw.items():
        key %= mod
        d[key] = pa(d.get(key, (0, 0)), val)
    bases = {key % step for key in d}
    out = {}
    for b in bases:
        last = d.get(b+(p-1)*step, (0, 0))
        for j in range(p-1):
            key = b+j*step
            v = pa(d.get(key, (0, 0)), pn(last))
            if v != (0, 0): out[key] = v
    return out

def const(c, p, level):
    return canonical({0: (c, 0)}, p, level)

def scal(poly, c):
    return {k: (c*v[0], c*v[1]) for k, v in poly.items() if c*v[0] or c*v[1]}

def poly_mul(a, b, p, level):
    raw = {}
    for i, u in a.items():
        for j, v in b.items(): raw[i+j] = pa(raw.get(i+j, (0, 0)), pm(u, v))
    return canonical(raw, p, level)

def embed(a, p, level):
    if level < 1: raise ValueError('cannot embed Gauss sum into absent modulus')
    return canonical({k*p**(level-1): v for k, v in a.items()}, p, level)


class UnramifiedRing:
    """Degree 1 at p=13,37; degree 2 unramified Z_5[sqrt(2)]."""
    def __init__(self, p: int, degree: int):
        self.p, self.degree = p, degree
        self.q = p**degree
        self.one = (1,) if degree == 1 else (1, 0)
        self.zero = (0,) if degree == 1 else (0, 0)
        self.logs = {}
        for g in product(range(p), repeat=degree):
            if g == self.zero: continue
            orbit, val = [], self.one
            for _ in range(self.q-1):
                orbit.append(val)
                val = self.mul(val, g, p)
            if val == self.one and len(set(orbit)) == self.q-1:
                self.logs = {v: j for j, v in enumerate(orbit)}
                self.generator = g
                break
        if not self.logs: raise ValueError('no finite-field generator')
        self.taus = [self.tau(j) for j in range(6)]

    def mul(self, x, y, mod):
        if self.degree == 1: return ((x[0]*y[0]) % mod,)
        return ((x[0]*y[0]+2*x[1]*y[1]) % mod,
                (x[0]*y[1]+x[1]*y[0]) % mod)

    def trace(self, x): return x[0]*self.degree

    def units(self, level):
        if level == 0: return [self.zero]
        return [x for x in product(range(self.p**level), repeat=self.degree)
                if any(v % self.p for v in x)]

    def phase(self, x, power):
        r = tuple(v % self.p for v in x)
        if r == self.zero:
            if not KEEP_NONUNIT_ZERO and power % 6 == 0: return (1, 0)
            return (0, 0)
        return SIX[(power*self.logs[r]) % 6]

    def tau(self, power):
        raw = {}
        for x in product(range(self.p), repeat=self.degree):
            v = self.phase(x, power)
            idx = self.trace(x) % self.p
            raw[idx] = pa(raw.get(idx, (0, 0)), v)
        return canonical(raw, self.p, 1)

    def direct_C(self, t, k, J):
        level = t+k
        if level == 0: return const(1, self.p, 0)
        mod = self.p**level
        raw = {}
        ds, vs = self.units(k), self.units(t)
        for d in ds:
            b = tuple(((self.p**J if i == 0 else 0)-self.p**t*d[i]) % mod
                      for i in range(self.degree))
            if any(v % (self.p**k) for v in b): continue
            dc = (1, 0) if k == 0 else self.phase(d, k)
            for v in vs:
                vc = (1, 0) if t == 0 else self.phase(v, t)
                idx = self.trace(self.mul(b, v, mod)) % mod
                raw[idx] = pa(raw.get(idx, (0, 0)), pm(dc, vc))
        return canonical(raw, self.p, level)

    def predicted_C(self, t, k, J):
        n, q = t+k, self.q
        if t == 0: return const(int(k == 0 or J == 0), self.p, n)
        if k >= 2: return {}
        if k == 0:
            if J < t-1: return {}
            if J == t-1: val = self.taus[t % 6]
            elif t % 6 == 0: val = const(q-1, self.p, 1)
            else: val = {}
        else:
            if J < t: return {}
            if J == t: val = poly_mul(self.taus[1], self.taus[(t-1) % 6], self.p, 1)
            elif (t-1) % 6 == 0: val = scal(self.taus[1], q-1)
            else: val = {}
        return embed(scal(val, q**(t-1)), self.p, n)


def scalar_C(t, k, J, q, tau):
    if t == 0: return Q(int(k == 0 or J == 0))
    if k >= 2: return Q(0)
    if k == 0:
        if J < t-1 and KEEP_VALUATION_SUPPORT: return Q(0)
        if J <= t-1: return q**(t-1)*tau[t % 6]
        return Q(q**(t-1)*(q-1)) if t % 6 == 0 else Q(0)
    if J < t and KEEP_VALUATION_SUPPORT: return Q(0)
    if J <= t: return q**(t-1)*tau[1]*tau[(t-1) % 6]
    return q**(t-1)*tau[1]*(q-1) if (t-1) % 6 == 0 else Q(0)


def series_checks():
    count = 0
    for q in [13, 25, 37]:
        tau = [Q(-1), Q(2), Q(3), Q(5), Q(7), Q(q, 2)]
        for variant in [1, 2]:
            a, b, r = Q(variant, q*q), Q(1, q**4), Q(variant+1, q)
            d, e0 = -a*tau[1], q**6*b*b
            for j in range(6):
                f = []
                for m in range(13):
                    J = j+6*m
                    val = Q(1)+(r/(1-r) if j == 0 and m == 0 else 0)
                    for eps in [0, 1]:
                        for ell in range((J+1)//3+1):
                            t = eps+3*ell
                            if t == 0: continue
                            for k in [0, 1]:
                                val += a**eps*b**ell*r**k*scalar_C(t,k,J,q,tau)
                    f.append(val)
                if j == 0:
                    for m, actual in enumerate(f):
                        pred = Q(1)+(r/(1-r) if m == 0 else 0)
                        pred += (1-Q(1,q))*sum((e0**n for n in range(1,m+1)),Q(0))
                        if m: pred += r*e0**m
                        pred -= d*e0**m+d*(q-1)*r*sum((e0**n for n in range(m)),Q(0))
                        need(actual == pred, 'unramified exact-series coefficient')
                        count += 1
                    continue
                rr = r if KEEP_RAMIFIED_UNIT_PHASE else Q(0)
                base = 1-(q-1)*d*rr
                if j == 1: poly = [1+d*rr, -e0/q-q*d*rr]
                elif j == 2:
                    c = q*q*b*tau[3]; poly = [base+c,-e0/q-c]
                elif j == 3:
                    c = q*q*b*tau[1]*tau[2]*rr+q**3*a*b*tau[4]
                    poly = [base+c,-e0/q-c]
                elif j == 4:
                    c = q**3*a*b*tau[1]*tau[3]*rr; poly = [base+c,-e0/q-c]
                else:
                    c = q**5*b*b if KEEP_J5_BOUNDARY else Q(0)
                    poly = [base-c,-e0/q+c]
                for m, actual in enumerate(f):
                    lhs = actual-(1+e0)*(f[m-1] if m else 0)+e0*(f[m-2] if m>=2 else 0)
                    need(lhs == (poly[m] if m<2 else 0), 'ramified rational numerator j='+str(j))
                    count += 1
    return count


def density_checks():
    lam, sig, a, b = Q(6,11), Q(3,4), Q(65,92), Q(211,184)
    need(Q(1,2)<lam<sig<1 and 0<a<b,'detector parameter domain')
    kap = max(Q(1),Q(13,6)-2*lam)
    ml = lam if USE_SHIFTED_MOLLIFIER else Q(1,2)
    moll = [Q(1),1+(1-2*ml)*a,(2-2*ml)*a,
            Q(5,6)+(Q(4,3)-2*ml)*a,Q(1,3)+(Q(11,6)-2*ml)*a]
    first = ((lam if USE_SHIFTED_B else Q(1,2))-sig)*b+kap/4+max(moll)/2
    g = first/(1-COUNT_POWER)
    need(kap==Q(71,66),'off-central fourth moment')
    need(max(moll)==Q(1525,1518),'same-line mollifier mass')
    need(first==Q(395,736),'shifted detection first exponent')
    need(g==Q(395,552),'unknown-count elimination')
    endpoints=[(2-2*sig)*b,1+(1-2*sig)*a]
    endpoints += [Q(1,3)+(Q(11,6)-2*sig)*v for v in [a,b]]
    endpoints += [Q(5,6)+(Q(4,3)-2*sig)*v for v in [a,b]]
    for t in endpoints: need(t<=g,'complete second detector endpoint')
    need(Q(43,60)-g==Q(1,920),'strict gain over #966')
    need(Q(8,11)-g==Q(71,6072),'strict gain over displayed DF exponent')
    # Actual conductor Q0=U^theta is retained in the dual prefactor.
    conductor_cases=0
    for line in [Q(1,2),lam,Q(7,12)]:
        bound=max(Q(1),Q(13,6)-2*line)
        for theta in [Q(i,20) for i in range(21)]:
            for c,d0 in [(Q(0),Q(1)),(Q(1),Q(0)),(Q(1,3),Q(5,6)),(Q(5,6),Q(1,3))]:
                dual=(theta*(2-4*line) if KEEP_DUAL_CONDUCTOR else Q(0))+d0+theta*(c+2*line-1)
                correct=d0+theta*(c+1-2*line)
                need(dual==correct,'actual dual conductor cancellation')
                need(dual<=bound,'off-central conductor dyad bound')
                conductor_cases+=1
    return {'lambda':str(lam),'sigma':str(sig),'A_exponent':str(a),'B_exponent':str(b),
            'kappa4':str(kap),'mollifier_monomials':[str(t) for t in moll],
            'first_exponent':str(first),'density_exponent':str(g),
            'other_exponents':[str(t) for t in endpoints],'gain_over_966':'1/920',
            'conductor_monomials':conductor_cases}


def domain_checks():
    def margins(x,y,z): return [x,y,z,6*z+y-1,x+6*z-1,x+y-1,x+y+6*z-2,6*x+6*z-5]
    for xyz in [(Q(3,5),Q(1,2),Q(2,5)),(Q(1,2),Q(3,4),Q(1,2))]:
        for v in margins(*xyz): need(v>0,'new domain strict margin')
    x,y,z=Q(3,5),Q(1,2),Q(2,5)
    need(3*x<2 and 3*x+y<Q(5,2),'strict removal of old walls')
    n=0
    for p in [Q(1),Q(3,2),Q(2),Q(4),Q(10)]:
        for r in range(1,20):
            delta=Q(r,60)/p # strictly below 1/(3p)
            for j,c in [(2,3),(3,4),(4,3),(5,6)]:
                need(p*c*delta-j < -1,'summable weighted local correction')
                n+=1
    for x in [Q(1,4),Q(1,3),Q(2,5),Q(49,100)]:
        need(Q(3,2)-3*x>0,'true subcritical local growth')
        need((Q(3,2)-3*x)/2==Q(3,4)-Q(3,2)*x,'full-norm versus prime-norm growth')
    return {'new_interior_point':['3/5','1/2','2/5'],
            'critical_face_point':['1/2','3/4','1/2'],
            'weighted_moment_exponents':n,'second_correction_moment_threshold':'1/3'}


def run():
    finite=[]
    for p,deg,maxlevel in [(13,1,4),(37,1,2),(5,2,3)]:
        ring=UnramifiedRing(p,deg)
        need(ring.taus[0]==const(-1,p,1),'nonunit mask in zeroth Gauss character')
        
        for r in range(1,6):
            need(poly_mul(ring.taus[r],ring.taus[6-r],p,1)==const(ring.q,p,1),'Gauss norm/product at every nontrivial power')
        minus=tuple((-v)%p for v in ring.one)
        need(ring.phase(minus,1)==(1,0),'chi(-1)=1 gate')
        cases=0
        for t in range(maxlevel+1):
            for k in range(maxlevel+1-t):
                for J in range(max(2,t+2)):
                    need(ring.direct_C(t,k,J)==ring.predicted_C(t,k,J),
                         f'direct complete residue sum Q={ring.q},t={t},k={k},J={J}')
                    cases+=1
        finite.append({'residue_norm':ring.q,'characteristic':p,'unramified_degree':deg,
                       'max_t_plus_k':maxlevel,'complete_residue_sum_cases':cases,
                       'primitive_generator':list(ring.generator)})
    series=series_checks()
    density=density_checks()
    domain=domain_checks()
    return {'status':'PASS: exact finite algebra; not an analytic or independent proof certificate',
            'predicates':CHECKS,'finite_local_rings':finite,'formal_series_coefficients':series,
            'formal_series_scope':'rational formal Gauss-symbol fixtures, coefficients through v^12; not actual L-values',
            'density':density,'correction_domain':domain}

if __name__=='__main__':
    try:
        print(json.dumps(run(),indent=2,sort_keys=True))
    except (ValueError,TypeError,KeyError,ZeroDivisionError) as exc:
        print('FAIL: '+str(exc),file=sys.stderr)
        sys.exit(1)
