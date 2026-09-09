#!/usr/bin/env python3
"""Bounded exact checks for TRG26. No finite test certifies the asymptotic theorem."""
import argparse
import hashlib
import json
from fractions import Fraction as F
from math import isqrt
from pathlib import Path

BITS = 160
DEN = 1 << BITS
HERE = Path(__file__).resolve().parent


def require(ok, message):
    if not ok:
        raise ValueError(message)


def primes(n):
    a = [True] * (n + 1)
    a[:2] = [False, False]
    for p in range(2, isqrt(n) + 1):
        if a[p]:
            for k in range(p * p, n + 1, p):
                a[k] = False
    return [p for p in range(2, n + 1) if a[p]]


def trial_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def box(pp):
    s = [1]
    for p in pp:
        s += [n * p for n in s[:]]
    return sorted(s)


def mass(s):
    return sum((F(1, n) for n in s), F(0))


def modes(pp, rates):
    out = [(1, F(0))]
    for p in pp:
        ap = F(p + 1, p) * rates[p]
        out += [(n * p, x + ap) for n, x in out[:]]
    return out[1:]


def matrix(s, pp, rates):
    ix = {n: i for i, n in enumerate(s)}
    a = [[F(0) for _ in s] for _ in s]
    edges = 0
    for n in s:
        for p in pp:
            if n % p == 0 and n // p in ix:
                i, j = ix[n], ix[n // p]
                w = rates[p]
                a[i][i] += w
                a[i][j] -= w
                a[j][j] += w / p
                a[j][i] -= w / p
                edges += 1
    return a, edges


def shifted(a, z):
    return [[x - (z if i == j else 0) for j, x in enumerate(row)]
            for i, row in enumerate(a)]


def det(a):
    a = [r[:] for r in a]
    value = F(1)
    for j in range(len(a)):
        k = next((k for k in range(j, len(a)) if a[k][j]), None)
        if k is None:
            return F(0)
        if k != j:
            a[k], a[j] = a[j], a[k]
            value = -value
        d = a[j][j]
        value *= d
        for i in range(j + 1, len(a)):
            r = a[i][j] / d
            for k in range(j + 1, len(a)):
                a[i][k] -= r * a[j][k]
    return value


def solve(a, b):
    a = [row[:] + [F(v)] for row, v in zip(a, b)]
    n = len(a)
    for j in range(n):
        k = next((k for k in range(j, n) if a[k][j]), None)
        require(k is not None, 'singular exact solve')
        a[k], a[j] = a[j], a[k]
        d = a[j][j]
        a[j] = [v / d for v in a[j]]
        for i in range(n):
            if i != j:
                r = a[i][j]
                a[i] = [v - r * w for v, w in zip(a[i], a[j])]
    return [r[-1] for r in a]


def mul(a, v):
    return [sum((x * y for x, y in zip(row, v)), F(0)) for row in a]


def dot(s, a, b):
    return sum((x * y / n for n, x, y in zip(s, a, b)), F(0))


def phi(za, zb, ma, mb, z):
    ka = sum((F(1, n) / (a - z) for n, a in ma), F(0))
    kb = sum((F(1, n) / (a - z) for n, a in mb), F(0))
    return za + zb - 1 - z * ((za - 1) * kb + (zb - 1) * ka) - z*z*ka*kb


class I:
    """Outward dyadic intervals; all arithmetic is integer/Fraction arithmetic."""
    def __init__(self, lo, hi=None):
        self.lo, self.hi = lo, lo if hi is None else hi
        require(self.lo <= self.hi, 'reversed interval')

    @staticmethod
    def point(x):
        x = F(x) * DEN
        return I(x.numerator // x.denominator,
                 -((-x.numerator) // x.denominator))

    def __add__(self, other):
        if not isinstance(other, I): other = I.point(other)
        return I(self.lo + other.lo, self.hi + other.hi)
    __radd__ = __add__

    def __neg__(self): return I(-self.hi, -self.lo)
    def __sub__(self, other): return self + (-other if isinstance(other, I) else -F(other))
    def __rsub__(self, other): return I.point(other) - self

    def __mul__(self, other):
        if not isinstance(other, I): other = I.point(other)
        t = [a*b for a in (self.lo, self.hi) for b in (other.lo, other.hi)]
        return I(min(t) // DEN, -((-max(t)) // DEN))
    __rmul__ = __mul__

    def reciprocal(self):
        require(not self.lo <= 0 <= self.hi, 'interval division through zero')
        a, b = F(DEN*DEN, self.hi), F(DEN*DEN, self.lo)
        return I(a.numerator // a.denominator, -((-b.numerator) // b.denominator))

    def __truediv__(self, other):
        if not isinstance(other, I): other = I.point(other)
        return self * other.reciprocal()

    def pair(self): return [str(self.lo), str(self.hi)]


def atanh_log(x, terms=100):
    """log x for 1<=x<=2: positive series plus its complete geometric remainder."""
    x = F(x)
    require(1 <= x <= 2, 'log reduction range')
    z = (x - 1) / (x + 1)
    value = sum((2*z**(2*j+1)/F(2*j+1) for j in range(terms)), F(0))
    remainder = 2*z**(2*terms+1)/(F(2*terms+1)*(1-z*z))
    a, b = I.point(value), I.point(value+remainder)
    return I(a.lo, b.hi)


def log_integer(n):
    k = n.bit_length() - 1
    return k * atanh_log(F(2)) + atanh_log(F(n, 1 << k))


def actual_certificate(P, lower, upper):
    pp = primes(P)
    zp = F(1)
    for p in pp: zp *= F(p+1,p)
    A, za = [], F(1)
    for p in pp:
        candidate = za * F(p+1,p)
        if candidate**3 <= zp:
            A.append(p); za = candidate
        else: break
    require(A, 'empty first reservoir')
    B = [p for p in pp if p not in A]
    zb = zp/za
    rates = {p: log_integer(p) for p in pp}
    def imodes(ps):
        out = [(1,I.point(0))]
        for p in ps:
            ap=F(p+1,p)*rates[p]
            out += [(n*p,a+ap) for n,a in out[:]]
        return out[1:]
    ma,mb=imodes(A),imodes(B)
    def iphi(z):
        z=I.point(z)
        ka=sum((I.point(F(1,n))/(a-z) for n,a in ma),I.point(0))
        kb=sum((I.point(F(1,n))/(a-z) for n,a in mb),I.point(0))
        return za+zb-1-z*((za-1)*kb+(zb-1)*ka)-z*z*ka*kb
    pl,ph=iphi(F(lower)),iphi(F(upper))
    require(pl.lo>0 and ph.hi<0,'gap bracket not strict')
    require(I.point(F(upper)).hi < (F(3,2)*rates[2]).lo, 'not below box gap')
    s=sorted(set(box(A))|set(box(B)))
    for n in s:
        for p in pp:
            if n % p == 0: require(n//p in s, 'divisor closure')
    edges=sum(1 for n in s for p in pp if n%p==0 and n//p in s)
    expected=len(A)*2**(len(A)-1)+len(B)*2**(len(B)-1)
    require(edges==expected,'missing cross edge or wrong population')
    return {'P':P,'A':A,'B':B,'vertices':len(s),'edges':edges,
            'visible_nonconstant_modes':len(ma)+len(mb),
            'Z_A':str(za),'Z_B':str(zb),'gap_interval':[lower,upper],
            'secular_at_lower_dyadic':pl.pair(),'secular_at_upper_dyadic':ph.pair()}


def calculate():
    groups={}
    pp=primes(257)
    require(pp==[n for n in range(2,258) if trial_prime(n)],'prime reconstruction')
    groups['sieve_vs_trial_integers']=256
    panels=[([2],[3]),([2],[3,5]),([2,3],[5]),([2,3],[5,7]),
            ([2,5],[3,7]),([2,3,5],[7]),([2],[3,5,7])]
    identities=0; vertices=0; edge_count=0; spectrum_cases=0; green_cases=0
    for A,B in panels:
        ps=sorted(A+B);rates={p:F((i%3)+2,2) for i,p in enumerate(ps)}
        sa,sb=box(A),box(B);s=sorted(set(sa)|set(sb))
        la,ea=matrix(sa,ps,rates);lb,eb=matrix(sb,ps,rates);ls,es=matrix(s,ps,rates)
        require(es==ea+eb,'unexpected inter-reservoir edge')
        za,zb=mass(sa),mass(sb);ma,mb=modes(A,rates),modes(B,rates)
        vertices+=len(s);edge_count+=es
        for z in [F(-2),F(-1),F(1,19)]:
            da,db,ds=det(shifted(la,z)),det(shifted(lb,z)),det(shifted(ls,z))
            expected=-phi(za,zb,ma,mb,z)*da*db/(za*zb*z)
            require(ds==expected,'root mass / determinant factor mismatch')
            identities+=1
        for si,li,mi,zi in [(sa,la,ma,za),(sb,lb,mb,zb)]:
            pi=sorted({p for p in ps if p in si})
            for nD,aD in mi:
                factors=[p for p in pi if nD%p==0]
                u=[]
                for n in si:
                    value=F(1)
                    for p in factors: value *= F(1) if n%p==0 else F(-1,p)
                    u.append(value)
                require(mul(li,u)==[aD*v for v in u],'product eigenvector')
                require(dot(si,[F(1)]*len(si),u)==0,'not centered')
                spectrum_cases+=1
            a=[[li[i][j]+F(1,si[j])/zi for j in range(len(si))] for i in range(len(si))]
            h=solve(a,[zi-1]+[F(-1)]*(len(si)-1))
            G=sum((F(1,n)/x for n,x in mi),F(0))
            H=sum((F(1,n)/(x*x) for n,x in mi),F(0))
            require(h[0]==G,'root Green normalization')
            require(dot(si,h,h)/zi==H,'second moment')
            require(dot(si,h,mul(li,h))/zi==G,'Green energy')
            green_cases+=1
        # Complete rooted trial in Section 6, including global recentering.
        a=[[la[i][j]+F(1,sa[j])/za for j in range(len(sa))] for i in range(len(sa))]
        h=solve(a,[za-1]+[F(-1)]*(len(sa)-1));G=h[0]
        H=dot(sa,h,h)/za; fa={n:1-v/G for n,v in zip(sa,h)}
        f=[fa.get(n,F(0)) for n in s];zs=mass(s);alpha=za/zs
        mean=dot(s,[F(1)]*len(s),f)/zs
        var=dot(s,f,f)/zs-mean*mean;energy=dot(s,f,mul(ls,f))/zs
        require(energy==alpha/G,'trial energy')
        require(var==alpha*(1-alpha)+alpha*H/(G*G),'trial variance')
    groups.update(formal_graph_panels=len(panels),vertex_instances=vertices,
                  edge_instances=edge_count,determinant_identities=identities,
                  product_eigenvectors=spectrum_cases,root_green_identities=green_cases,
                  complete_trial_variances=len(panels))
    # A genuine simultaneous zero of both local root resolvents.
    rates={2:F(1),3:F(1)};s=[1,2,3];l,_=matrix(s,[2,3],rates)
    require(mul(l,[F(0),F(2),F(-3)])==[F(0),F(2),F(-3)],'coincident pole eigenvector')
    require(phi(F(3,2),F(4,3),modes([2],rates),modes([3],rates),F(1))==0,
            'coincident root lost')
    groups['coincident_root_cases']=1
    certs=[actual_certificate(17,'0.73956963541318','0.73956963541319'),
           actual_certificate(31,'0.72552568064883','0.72552568064885')]
    return {'schema':'TRG26-bounded-v1','rh_proved':False,'asymptotic_machine_verified':False,
            'dyadic_bits':BITS,'log_series_terms':100,'groups':groups,'actual_gap_certificates':certs}


def no_duplicates(pairs):
    out={}
    for k,v in pairs:
        require(k not in out,'duplicate JSON key')
        out[k]=v
    return out


def canonical(o):
    return json.dumps(o,sort_keys=True,separators=(',',':'),ensure_ascii=True)


def read_json(p):
    def bad(x): raise ValueError('noninteger JSON number')
    return json.loads(p.read_text(),object_pairs_hook=no_duplicates,
                      parse_float=bad,parse_constant=bad)


def authenticate():
    p=HERE/'SHA256SUMS'
    require(p.is_file() and not p.is_symlink(),'missing manifest')
    rows={}
    for line in p.read_text().splitlines():
        sha,name=line.split('  ',1)
        require(name not in rows and '/' not in name and name not in ('.','..'),'manifest path')
        require(len(sha)==64,'manifest digest')
        rows[name]=sha
    expected={'PROOF.md','ATTEMPT.md','README.md','CLAIMS.json','SOURCES.json',
              'VALIDATION.md','verify.py','test_rejections.py','result.json'}
    require(set(rows)==expected,'wrong manifest inventory')
    require({x.name for x in HERE.iterdir()}==set(rows)|{'SHA256SUMS'},'inventory mismatch')
    for name,sha in rows.items():
        f=HERE/name
        require(f.is_file() and not f.is_symlink(),'not regular file')
        require(hashlib.sha256(f.read_bytes()).hexdigest()==sha,'changed source: '+name)


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--emit',action='store_true',help='Unauthenticated producer mode')
    p.add_argument('--check',type=Path)
    args=p.parse_args()
    require(args.emit != bool(args.check),'choose emit XOR check')
    if not args.emit: authenticate()
    result=calculate()
    if args.check:
        require(canonical(read_json(args.check))==canonical(result),'result reconstruction mismatch')
    print(json.dumps(result,sort_keys=True,indent=2))


if __name__=='__main__': main()
