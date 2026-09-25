#!/usr/bin/env python3
"""ADP37 primitive replay. Standard library; exact/outward acceptance only."""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import json
from math import factorial, gcd
from pathlib import Path
import sys

COUNTS = Counter()
COVERAGE = Counter()
BITS = 100
SCALE = 1 << BITS


def require(ok, label):
    if not ok:
        raise ValueError(label)
    COUNTS[label] += 1


def rat(q):
    q = F(q)
    return {'numerator': q.numerator, 'denominator': q.denominator}


def floor_q(q):
    q = F(q)
    return q.numerator // q.denominator


def down(q):
    return F(floor_q(F(q)*SCALE), SCALE)


def up(q):
    return -down(-F(q))


@dataclass(frozen=True)
class I:
    lo: F
    hi: F

    @staticmethod
    def point(q):
        q = F(q)
        return I(down(q), up(q))

    @staticmethod
    def cast(q):
        return q if isinstance(q, I) else I.point(q)

    def __add__(self, other):
        other = I.cast(other)
        return I(down(self.lo+other.lo), up(self.hi+other.hi))

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-I.cast(other))

    def __rsub__(self, other):
        return I.cast(other) - self

    def __mul__(self, other):
        other = I.cast(other)
        products = [a*b for a in (self.lo, self.hi)
                    for b in (other.lo, other.hi)]
        return I(down(min(products)), up(max(products)))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = I.cast(other)
        if other.lo <= 0 <= other.hi:
            raise ValueError('interval division through zero')
        rec = I(down(1/other.hi), up(1/other.lo))
        return self*rec

    def square(self):
        lower = 0 if self.lo <= 0 <= self.hi else min(self.lo**2, self.hi**2)
        return I(down(lower), up(max(self.lo**2, self.hi**2)))

    def contains_zero(self):
        return self.lo <= 0 <= self.hi

    def record(self):
        return {'lo': rat(self.lo), 'hi': rat(self.hi)}


def atan_small(q, terms=48):
    q = F(q)
    total = sum(((-1)**j*q**(2*j+1)/F(2*j+1)
                 for j in range(terms)), F(0))
    nxt = (-1)**terms*q**(2*terms+1)/F(2*terms+1)
    return I(down(min(total, total+nxt)), up(max(total, total+nxt)))


PI = 16*atan_small(F(1, 5))-4*atan_small(F(1, 239))


@lru_cache(maxsize=None)
def log_unit(q):
    q = F(q)
    if q == 1:
        return I.point(0)
    if not 1 <= q <= 2:
        raise ValueError('log reduction outside [1,2]')
    t = I.point((q-1)/(q+1))
    t2 = t.square()
    power, total = t, I.point(0)
    for j in range(64):
        total = total + power/F(2*j+1)
        power = power*t2
    tail = F(2)*F(1, 3)**129/(129*(1-F(1, 9)))
    total = 2*total
    return I(total.lo, up(total.hi+tail))


LOG2 = log_unit(F(2))


@lru_cache(maxsize=None)
def log_point(q):
    q = F(q)
    if q <= 0:
        raise ValueError('log of nonpositive input')
    exponent = 0
    while q < 1:
        q *= 2
        exponent -= 1
    while q >= 2:
        q /= 2
        exponent += 1
    return log_unit(q) + exponent*LOG2


def log_i(x):
    if x.lo <= 0:
        raise ValueError('nonpositive logarithm interval')
    return I(log_point(x.lo).lo, log_point(x.hi).hi)


def trig_turns(turns, sine=False):
    """sin/cos(2*pi*turns), reducing a certified interval modulo one."""
    turns = I.cast(turns)
    shift = floor_q((turns.lo+turns.hi)/2 + F(1, 2))
    x = 2*PI*(turns-shift)
    if max(abs(x.lo), abs(x.hi)) > 4:
        raise ValueError('trig interval too broad')
    z = x.square()
    term = x if sine else I.point(1)
    val = term
    for j in range(1, 41):
        denom = (2*j)*(2*j+1) if sine else (2*j-1)*(2*j)
        term = -term*z/denom
        val = val+term
    order = 83 if sine else 82
    rem = F(4)**order/factorial(order)
    return I(down(val.lo-rem), up(val.hi+rem))


@lru_cache(maxsize=None)
def cos_rational(q):
    return trig_turns(F(q))


@dataclass(frozen=True)
class G:
    re: F = F(0)
    im: F = F(0)

    @staticmethod
    def cast(x):
        return x if isinstance(x, G) else G(F(x))

    def __add__(self, x):
        x = G.cast(x)
        return G(self.re+x.re, self.im+x.im)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.re, -self.im)

    def __sub__(self, x):
        return self + (-G.cast(x))

    def __mul__(self, x):
        x = G.cast(x)
        return G(self.re*x.re-self.im*x.im, self.re*x.im+self.im*x.re)

    __rmul__ = __mul__

    def __truediv__(self, q):
        return G(self.re/F(q), self.im/F(q))

    def conj(self):
        return G(self.re, -self.im)

    def norm2(self):
        return self.re**2+self.im**2

    def __pow__(self, k):
        if k < 0:
            if self.norm2() != 1:
                raise ValueError('negative power requires unit norm')
            return self.conj()**(-k)
        answer, base = G(F(1)), self
        while k:
            if k & 1:
                answer = answer*base
            base = base*base
            k //= 2
        return answer


@lru_cache(maxsize=None)
def harmonic(n):
    return sum((F(1, k) for k in range(1, n+1)), F(0))


def mu_sieve(n):
    mu = [1]*(n+1)
    mu[0] = 0
    composite = [False]*(n+1)
    for p in range(2, n+1):
        if composite[p]:
            continue
        for j in range(p, n+1, p):
            composite[j] = True
            mu[j] *= -1
        for j in range(p*p, n+1, p*p):
            mu[j] = 0
    return mu


def triangular_inverse(n):
    accum, inverse = [0]*(n+1), [0]*(n+1)
    for j in range(1, n+1):
        inverse[j] = 1 if j == 1 else -accum[j]
        for k in range(2*j, n+1, j):
            accum[k] += inverse[j]
    return inverse


def convolution(a, b):
    result = defaultdict(lambda: F(0))
    for n, x in a.items():
        for m, y in b.items():
            COVERAGE['ordered_source_products'] += 1
            result[n*m] += x*y
    return {n: x for n, x in result.items() if x != 0}


def cap(mu, y):
    source = {n: F(mu[n]) for n in range(1, y+1) if mu[n]}
    residual = sum((source.get(n, F(0))/n for n in range(1, y+1)), F(0))
    initial, n = residual, y
    while residual:
        n += 1
        signed = 1 if residual > 0 else -1
        value = -signed*min(F(3), n*abs(residual))
        source[n] = value
        residual += value/n
        if n > 2*y:
            raise ValueError('cap beyond permitted support')
    return source, n, initial


def totients(n):
    phi = list(range(n+1))
    for p in range(2, n+1):
        if phi[p] == p:
            for j in range(p, n+1, p):
                phi[j] -= phi[j]//p
    return phi


def class_key(n, y):
    while n % y == 0:
        n //= y
    return n


def aliases_direct(n, m, y):
    n, m = max(n, m), min(n, m)
    while m < n:
        m *= y
    return m == n


def phi_structural(n, x, h=1):
    """Rational bump only: NOT the centered harmonic observable."""
    return sum(((1-F(j*x, 2*h*n))**4
                for j in range(1, (2*h*n-1)//x+1)), F(0))/n


def exact_panels(mu, quick):
    phi = totients(64)
    max_rectangle = 6 if quick else 16
    for a in range(1, max_rectangle+1):
        for b in range(1, max_rectangle+1):
            counts = Counter(i*j for i in range(1, a+1) for j in range(1, b+1))
            actual = sum(v*v for v in counts.values())
            expected = a*b+2*sum(phi[r]*(a//r)*(b//r)
                                  for r in range(2, min(a, b)+1))
            require(actual == expected, 'complete rectangular product collision identity')
            require(actual <= a*b*(2*harmonic(min(a, b))-1), 'collision harmonic upper bound')
            COVERAGE['rectangular_product_pairs'] += a*b
    for y in range(2, 9 if quick else 17):
        for n in range(1, 33 if quick else 129):
            for m in range(1, n+1):
                require((class_key(n, y) == class_key(m, y)) == aliases_direct(n, m, y),
                        'exact anchored alias classification')
    require(class_key(2, 4) != class_key(4, 4), 'perfect-power anchor not replaced by its base')
    alias_data = {3: F(1), 12: F(-1)}
    grouped = defaultdict(lambda: F(0))
    for n, b in alias_data.items():
        grouped[class_key(n, 4)] += b
    require(sum(b*b for b in grouped.values()) == 0 and sum(b*b for b in alias_data.values()) == 2,
            'ungrouped alias diagonal genuinely wrong')
    require(convolution({2:F(1), 3:F(1)}, {2:F(1), 3:F(1)})[6]**2 == 4,
            'product collisions squared after summation')

    coefficients = [G(F(1), F(1, 2)), G(F(-2), F(1, 3)), G(F(3, 2), F(-1))]
    phases = [G(F(1)), G(F(3, 5), F(4, 5)), G(F(5, 13), F(12, 13))]
    for k in (1, 2, 3, 5, 9):
        weights = {j:F(k-abs(j), k*k) for j in range(1-k, k)}
        require(sum(weights.values()) == 1, 'Fejer weights normalized')
        direct = sum((w*sum((b*p**j for b, p in zip(coefficients, phases)), G()).norm2()
                      for j, w in weights.items()), F(0))
        gram = G()
        wrong = G()
        for a, ba in enumerate(coefficients):
            for b, bb in enumerate(coefficients):
                phase = phases[a]*phases[b].conj()
                fk = (sum((phase**j for j in range(k)), G())/k).norm2()
                gram += ba*bb.conj()*fk
                wrong += ba*bb*fk
                COVERAGE['exact_Fejer_Gram_entries'] += 1
        require(gram.im == 0 and gram.re == direct, 'exact Gaussian direct versus Fejer Gram')
        require(wrong != gram, 'wrong non-Hermitian observation energy rejected')

    panels = []
    for y in ((3, 7, 15) if quick else (3, 7, 15, 31, 63, 127, 255)):
        c, length, residual = cap(mu, y)
        require(sum((v/n for n,v in c.items()), F(0)) == 0, 'literal cap reciprocal balance')
        require(length <= 2*y and max(map(abs, c.values())) <= 3, 'literal cap length and coefficient bounds')
        z = convolution(c, c)
        gamma = sum((a*a for a in z.values()), F(0))
        phi_large = totients(length)
        collisions = length*length+2*sum(phi_large[r]*(length//r)**2 for r in range(2,length+1))
        require(gamma <= 81*collisions, 'native cap convolution collision budget')
        x = length*length
        b = {n: a*phi_structural(n, x) for n,a in z.items() if 2*n>x}
        product_pair = sum((a*bb*phi_structural(r*s,x) for r,a in c.items() for s,bb in c.items()),F(0))
        require(product_pair == sum(b.values()), 'complete rational product-kernel reconstruction')
        diag = sum((v*v for v in b.values()),F(0))
        principal = sum(b.values())**2
        require(principal <= len(b)*diag, 'finite product coherence Cauchy bound')
        panels.append({'Y':y,'L':length,'product_energy':rat(gamma),
                       'collision_count':collisions,'structural_diagonal':rat(diag),
                       'structural_principal':rat(principal)})
    return panels


def sign_rectangle_checks():
    epsilon = F(1,4096)
    ci_lower = F(49,1936)-F(1,216)
    require(ci_lower > F(1,50), 'cosine integral signed lower bound constant')
    eta_quarter = 1-10*F(1,4)**3+15*F(1,4)**4-6*F(1,4)**5
    require(eta_quarter == F(459,512) and eta_quarter>F(1,2), 'actual mask positive rectangle')
    require((1-epsilon)**(-2)<F(5,4), 'single numerator harmonic rectangle')
    require(epsilon+2*epsilon/(1-epsilon) <= 4*epsilon, 'rectangle logarithmic width bound')
    z_upper = -F(1,25)+8*epsilon+F(200,8192**2)
    require(z_upper < -F(1,32), 'actual harmonic rectangle strictly negative')
    require(epsilon**5/F(4096) == F(1,2**72), 'principal lower-bound normalization')
    require(2+(4*F(22,7))**2+F(2,3)*(2*F(22,7))**2/8 < 200,
            'uniform finite harmonic to cosine-integral error constant')
    for length in (8192,8193,10000,16384,100000):
        first = floor_q((1-epsilon)*length)+1
        size = length-first+1
        require(size >= epsilon*length, 'coherent source block cardinality')
        require(F(size, first)<=1, 'coherent balanced source coefficient cap')
        require(length*length//2>=length, 'early repair invisible for actual harmonic mask')
    return {'epsilon':rat(epsilon),'ci_lower':rat(ci_lower),
            'z_rectangle_upper':rat(z_upper),'principal_energy_coefficient':rat(F(1,2**72)),
            'scope':'rational constants supporting the written all-scale harmonic proof; not a giant finite simulation'}


def actual_harmonic_panel(mu, y):
    c, length, _ = cap(mu,y)
    z = convolution(c,c)
    x = length*length
    m = 2*x-1
    nodes = sorted(n for n,a in z.items() if 2*n>x and a)
    values = {}
    envelope = harmonic(16)/x
    for n in nodes:
        # X=L^2: only j=1 is inside the exact smooth mask.
        t = F(x,n)
        v = t-1
        eta = 1-10*v**3+15*v**4-6*v**5
        require(1 <= t < 2 and 0<=eta<=1, 'actual harmonic single-numerator support')
        cosines = [cos_rational(F(j,n)) for j in range(n)]
        sine = trig_turns(F(1,2*n),True)
        zk = 2*sum((cosines[j%n]/j for j in range(1,x+1)),I.point(0))+2*log_i(2*sine)
        seq=[]
        for k in range(x,m+1):
            phi = eta*zk/n
            require(max(abs(phi.lo),abs(phi.hi)) <= envelope,
                    'actual centered harmonic complete-tail envelope')
            seq.append(z[n]*phi)
            zk = zk+2*cosines[(k+1)%n]/(k+1)
            COVERAGE['actual_harmonic_observation_cells'] += 1
        values[n]=seq
    d = sum((v.square() for n in nodes for v in values[n]),I.point(0))
    u0 = [sum((values[n][j] for n in nodes),I.point(0)) for j in range(x)]
    principal = sum((v.square() for v in u0),I.point(0))
    require(d.lo>0, 'actual native phase diagonal positive')
    gamma=sum((a*a for a in z.values()),F(0))
    crude=gamma*harmonic(16)**2/x
    require(d.hi<=crude, 'actual diagonal independently bounded by complete product energy')
    require(y*x >=4*length*length, 'actual anchored alias-separation hypothesis')
    logy=log_point(F(y))
    k_large=floor_q(2*x*logy.hi)+1
    eps=(F(x)*logy.hi/k_large)**2
    require(eps<=F(1,4), 'finite large phase window selected outward')

    def gram_average(k):
        total=d
        for a,n in enumerate(nodes):
            for mm in nodes[:a]:
                theta=log_point(F(n,mm))/logy
                sn=trig_turns(k*theta/2,True).square()
                sd=trig_turns(theta/2,True).square()
                fk=sn/(k*k*sd)
                # Both cuts are mathematical consequences of the exact Fejer identity.
                fk=I(max(F(0),fk.lo),min(F(1),fk.hi))
                if fk.lo>fk.hi:
                    raise ValueError('inconsistent Fejer interval')
                cross=sum((aa*bb for aa,bb in zip(values[n],values[mm])),I.point(0))
                total=total+2*fk*cross
                COVERAGE['actual_anchored_Fejer_pairs'] += 1
        return total

    avg=gram_average(k_large)
    require(avg.lo >= (1-eps)*d.lo and avg.hi <= (1+eps)*d.hi,
            'actual finite anchored Fejer mean inside theorem envelope')
    # A small direct phase enumeration independently checks the Gram normalization.
    small_k=3
    direct=I.point(0)
    for j in range(1-small_k,small_k):
        phase={n:(trig_turns(j*log_point(F(n))/logy),
                  trig_turns(j*log_point(F(n))/logy,True)) for n in nodes}
        energy=I.point(0)
        for obs in range(x):
            re=sum((values[n][obs]*phase[n][0] for n in nodes),I.point(0))
            im=sum((values[n][obs]*phase[n][1] for n in nodes),I.point(0))
            energy=energy+re.square()+im.square()
        direct=direct+F(small_k-abs(j),small_k*small_k)*energy
    small_gram=gram_average(small_k)
    difference=direct-small_gram
    require(difference.contains_zero() and difference.hi-difference.lo<F(1,10**20),
            'actual direct and Gram enclosures consistent at high precision')
    ratio=principal/d
    return {'Y':y,'L':length,'H':1,'X':x,'M':m,'active_products':nodes,
            'phase_K':k_large,'diagonal':d.record(),'principal_energy':principal.record(),
            'principal_to_diagonal':ratio.record(),'finite_Fejer_mean':avg.record(),
            'finite_mean_relative_error_upper':rat(eps),'small_direct_mean':direct.record(),
            'small_Gram_mean':small_gram.record(),
            'scope':'actual centered harmonic kernel, full declared observation block, actual logarithmic anchor phases'}


def authenticate(candidate, reference):
    if len(candidate) != len(reference) or any(a != b for a,b in zip(candidate,reference)):
        raise ValueError('primitive Mobius disagrees with independent inverse')


def campaign(quick=False):
    COUNTS.clear(); COVERAGE.clear()
    maximum=64 if quick else 1024
    mu=mu_sieve(maximum)
    independent=triangular_inverse(maximum)
    authenticate(mu, independent)
    for n in range(1,maximum+1):
        require(mu[n]==independent[n], 'primitive Mobius authenticated independently')
    corrupted=mu[:]
    corrupted[6]+=1
    caught = False
    try:
        authenticate(corrupted, independent)
    except ValueError:
        caught = True
    require(caught, 'corrupted primitive Mobius rejected')
    exact=exact_panels(mu,quick)
    sign=sign_rectangle_checks()
    actual=[] if quick else [actual_harmonic_panel(mu,y) for y in (5,7)]
    require(PI.lo>3 and PI.hi<F(22,7), 'certified Machin pi interval')
    require(LOG2.lo>F(1,2) and LOG2.hi<1, 'certified logarithm base interval')
    for q in (F(1),F(2),F(3,2),F(7,8),F(19)):
        residual=log_point(q)+log_point(1/q)
        require(residual.contains_zero(), 'directed logarithm reciprocal consistency')
    encoded=json.dumps(mu,separators=(',',':')).encode()
    return {'packet':'ADP37','mode':'quick-controls' if quick else 'full',
            'arithmetic':'integer/Fraction, Gaussian rationals, outward 100-bit dyadic intervals',
            'primitive_limit':maximum,'primitive_sha256':hashlib.sha256(encoded).hexdigest(),
            'predicate_count':sum(COUNTS.values()),'predicates':dict(sorted(COUNTS.items())),
            'arithmetic_coverage':dict(sorted(COVERAGE.items())),
            'exact_source_panels':exact,'actual_harmonic_panels':actual,
            'universal_counterexample_constants':sign,
            'boundaries':['not independent mathematical review','not a proof assistant',
                          'no native principal-phase upper bound','no full covariance or RH proof',
                          'finite enclosures do not replace the written all-scale proofs']}


def reject_constant(value):
    raise ValueError('nonfinite JSON constant')


def unique_object(pairs):
    result={}
    for k,v in pairs:
        if k in result:
            raise ValueError('duplicate JSON key')
        result[k]=v
    return result


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path)
    parser.add_argument('--check',type=Path)
    parser.add_argument('--quick',action='store_true')
    args=parser.parse_args()
    try:
        report=campaign(args.quick)
        if args.check:
            saved=json.loads(args.check.read_text(),object_pairs_hook=unique_object,
                             parse_constant=reject_constant)
            if saved!=report:
                raise ValueError('receipt does not match primitive replay')
        text=json.dumps(report,indent=2,sort_keys=True)+'\n'
        if args.output:
            args.output.write_text(text)
        print('PASS',report['mode'],report['predicate_count'],'predicates')
    except (ValueError,OSError,TypeError,KeyError,ZeroDivisionError) as exc:
        print('REJECT:',exc,file=sys.stderr)
        return 1
    return 0


if __name__=='__main__':
    raise SystemExit(main())
