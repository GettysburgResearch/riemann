#!/usr/bin/env python3
"""Bounded exact controls, not a machine proof of the analytic theorems."""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = '94ed8cd0395350b465165b424cc5c6366223d4ae'
PARENTS = {
    '../euler-tail-stability/PROOF.md': ('24ebe2ccf09d26e773a0071c6b335bcaff2b4b3d', '223109ec431d245d62df71d989796bd65e2ca9bbc5671b2d93180d637ea6c2ce'),
    '../annular-scalar-route/PROOF.md': ('0f1b21227d064e61f4f532d9025c78106baa688e', 'c68840c91308d4a93b85d38e34edc5c5ba9a335b2b25d0b4546a9e86979ffd04'),
}
NAMES = {'README.md','PROOF.md','SOURCES.json','ATTEMPT.md','VALIDATION.md',
         'verify.py','test_rejections.py','result.json','SHA256SUMS'}
BITS=112
SCALE=1 << BITS

def require(ok: bool, msg: str) -> None:
    if not ok:
        raise ValueError(msg)

def strict_json(text: str):
    def pairs(items):
        out={}
        for k,v in items:
            require(k not in out, 'duplicate JSON key')
            out[k]=v
        return out
    return json.loads(text, object_pairs_hook=pairs,
                      parse_constant=lambda _: (_ for _ in ()).throw(ValueError('nonfinite JSON')))

def canonical(obj) -> str:
    return json.dumps(obj, sort_keys=True, indent=2, ensure_ascii=False)+'\n'

def git_blob(data: bytes) -> str:
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

def authenticate(check_result: bool=True) -> None:
    require({p.name for p in HERE.iterdir()} == NAMES, 'file inventory')
    require(all(p.is_file() and not p.is_symlink() for p in HERE.iterdir()), 'nonregular file')
    entries={}
    for line in (HERE/'SHA256SUMS').read_text().splitlines():
        digest,name=line.split('  ',1)
        require(name not in entries and name in NAMES-{'SHA256SUMS'}, 'manifest entry')
        entries[name]=digest
    require(set(entries)==NAMES-{'SHA256SUMS'}, 'manifest coverage')
    for name,digest in entries.items():
        if name=='result.json' and not check_result:
            continue
        require(hashlib.sha256((HERE/name).read_bytes()).hexdigest()==digest, 'hash: '+name)
    sources=strict_json((HERE/'SOURCES.json').read_text())
    require(sources['publication_parent']==BASE, 'wrong source parent')
    require(sources['rh_proved'] is False and sources['new_native_sign_bound'] is False,
            'source scope')
    for path,(blob,sha256) in PARENTS.items():
        p=HERE/path
        require(p.is_file() and not p.is_symlink(), 'missing parent')
        data=p.read_bytes()
        require(git_blob(data)==blob and hashlib.sha256(data).hexdigest()==sha256,
                'parent bytes')

# Laurent-polynomial arithmetic over Q: all integrals used here avoid log powers.
def clean(p): return {e:F(c) for e,c in p.items() if c}
def add(p,q):
    r=dict(p)
    for e,c in q.items(): r[e]=r.get(e,F(0))+c
    return clean(r)
def scale(p,c): return clean({e:v*c for e,v in p.items()})
def mul(p,q):
    r={}
    for e,c in p.items():
        for f,d in q.items(): r[e+f]=r.get(e+f,F(0))+c*d
    return clean(r)
def deriv(p): return clean({e-1:e*c for e,c in p.items()})
def val(p,x): return sum((c*x**e for e,c in p.items()),F(0))
def integral(p,a,b):
    require(-1 not in p,'unexpected logarithmic primitive')
    return sum((c*(b**(e+1)-a**(e+1))/F(e+1) for e,c in p.items()),F(0))

def w(u):
    u=F(u)
    if F(1,4)<u<=1: return u/3-1/(192*u*u)
    if 1<u<4: return 1/(3*u*u)-u/192
    return F(0)

def atom_polys(n):
    return {3:F(1,3*n*n),-3:-F(n,192)}, {-3:F(n,3),3:-F(1,192*n*n)}

def atom_value(n,m): return w(F(n)/m**2)/m

def green(a,b,m,t):
    if not a<=t<=b: return F(0)
    return (min(m,t)-a)*(b-max(m,t))/(b-a)

def green_integral_atom(r,a,b,m):
    n=r*r
    lo,hi=atom_polys(n)
    knots=[F(r,2),F(r),F(2*r)]
    cuts=sorted({a,b,m}|{t for t in knots if a<t<b})
    answer=F(0)
    for x,y in zip(cuts,cuts[1:]):
        mid=(x+y)/2
        p=lo if knots[0]<mid<knots[1] else hi if knots[1]<mid<knots[2] else {}
        kp={1:(b-m)/(b-a),0:-a*(b-m)/(b-a)} if mid<m else {0:b*(m-a)/(b-a),1:-(m-a)/(b-a)}
        answer+=integral(mul(deriv(deriv(p)),kp),x,y)
    jumps=[F(1,2*n),-F(65,32*n),F(1,8*n)]
    answer+=sum((green(a,b,m,t)*j for t,j in zip(knots,jumps) if a<t<b),F(0))
    return answer

@lru_cache(None)
def factor(n):
    require(type(n) is int and n>=1, 'factor input')
    out={};p=2
    while p*p<=n:
        while n%p==0:
            out[p]=out.get(p,0)+1;n//=p
        p+=1
    if n>1:out[n]=out.get(n,0)+1
    return out

def mobius(n):
    f=factor(n)
    return 0 if any(e>1 for e in f.values()) else (-1)**len(f)

def primebase(n):
    f=factor(n)
    return next(iter(f)) if len(f)==1 else None

def vector_add(dst,src,c=F(1)):
    for p,v in src.items():
        dst[p]=dst.get(p,F(0))+c*v
        if dst[p]==0:del dst[p]
    return dst

def lattice(x, prime):
    result={}
    for n in range(2,(4*x).numerator//(4*x).denominator+1):
        weight=w(F(n)/x)
        if not weight:continue
        if prime:
            p=primebase(n)
            if p:vector_add(result,{p:F(1)},weight)
        else:vector_add(result,factor(n),weight)
    return result

def power4(x):
    require((2*x).denominator==1, 'half integer power')
    return F(2)**int(2*x)

def mellin_moment(s):
    def integ(e,lo,hi):
        # lo and hi are powers 4^lo,4^hi
        return (power4(F(hi)*e)-power4(F(lo)*e))/e
    return (integ(s+1,-1,0)/3-integ(s-2,-1,0)/192
           +integ(s-2,0,1)/3-integ(s+1,0,1)/192)

# Independent elementary logarithm enclosures; ordinary floating point is unused.
@lru_cache(None)
def log_bounds(n: int):
    require(n>=1,'log domain')
    def basic(r):
        t=(r-1)/(r+1); require(0<=t<=F(1,3),'log range')
        k=40
        lower=2*sum((t**(2*j+1)/F(2*j+1) for j in range(k)),F(0))
        upper=lower+2*t**(2*k+1)/(F(2*k+1)*(1-t*t))
        return lower,upper
    k=n.bit_length()-1
    l2,u2=basic(F(2));lr,ur=basic(F(n,1<<k))
    lo=k*l2+lr;hi=k*u2+ur
    return (lo.numerator*SCALE//lo.denominator,
            -((-hi.numerator*SCALE)//hi.denominator))

def round_ratio(lo,hi,c):
    if c<0:lo,hi=hi,lo
    a=F(lo)*c;b=F(hi)*c
    return a.numerator//a.denominator, -((-b.numerator)//b.denominator)

def actual_D(m):
    m=F(m);lo=hi=0
    for n in range(2,int(4*m*m)+1):
        p=primebase(n)
        if p:
            c=w(F(n)/(m*m))/m
            l,u=round_ratio(*log_bounds(p),c);lo+=l;hi+=u
    c=-F(45,128)*m+F(1,4)
    a=F(SCALE)*c
    lo+=a.numerator//a.denominator;hi+=-((-a.numerator)//a.denominator)
    return lo,hi

def reconstruct():
    counts={}; digest=hashlib.sha256()
    def checked(group,ok,fixture):
        require(ok, 'mathematical control: '+group)
        counts[group]=counts.get(group,0)+1
        digest.update((group+':'+str(fixture)+'\n').encode())
    for r in range(1,13):
        n=r*r;lo,hi=atom_polys(n)
        l0,c0,u0=F(r,2),F(r),F(2*r)
        checked('atom-jumps', val(lo,l0)==val(hi,u0)==0 and val(lo,c0)==val(hi,c0)
          and val(deriv(lo),l0)==F(1,2*n)
          and val(deriv(hi),c0)-val(deriv(lo),c0)==-F(65,32*n)
          and -val(deriv(hi),u0)==F(1,8*n),r)
        checked('atom-regular-curvature',deriv(deriv(lo))=={1:F(2,n*n),-5:-F(n,16)}
                and deriv(deriv(hi))=={-5:F(4*n),1:-F(1,32*n*n)},r)
        for a,b in [(F(2),F(4)),(F(3),F(6)),(F(4),F(8)),(F(5),F(10))]:
            for t in [F(1,4),F(1,2),F(3,4)]:
                m=a+(b-a)*t
                direct=atom_value(n,m)-(1-t)*atom_value(n,a)-t*atom_value(n,b)
                integ=green_integral_atom(r,a,b,m)
                checked('green-identity',direct==-integ,(r,a,b,t))
    checked('curvature-budget',F(24)+F(255,32)<32 and F(85,32)<3, '32-and-3')
    checked('grid-budget',8*F(49,9)+F(3,4)*F(7,81)<45,'fourth-power')
    checked('negative-run-budget',F(1,4)+F(15,256)<F(1,2),'run')
    for k in range(3,65):
        a=F(k*k);b=F((k+1)**2);h=b-a
        checked('grid-geometry',b<=2*a and 8*h*h/a+3*h/(4*a*a)<45,k)
    for s in [F(-3,2),F(-1,2),F(0),F(1,2),F(1),F(3,2),F(5,2),F(3)]:
        z=s-F(1,2)
        rhs=(F(65,64)-(power4(z)+power4(-z))/8)/(F(9,4)-z*z)
        checked('mellin-normalization',mellin_moment(s)==rhs,s)
    for n in range(1,257):
        ds=[d for d in range(1,n+1) if n%d==0];v={}
        for d in ds:
            p=primebase(d)
            if p:vector_add(v,{p:1})
        checked('native-divisor',v==factor(n) and sum(mobius(d) for d in ds)==(n==1),n)
    for x in [F(1,4),F(1,2),F(3,4),F(1),F(3,2),F(2),F(4),F(9),F(16),F(25)]:
        lhs={};inverse={}
        for d in range(1,int(2*x)+1):
            vector_add(lhs,lattice(x/d,True))
            vector_add(inverse,lattice(x/d,False),F(mobius(d)))
        checked('native-renewal',lhs==lattice(x,False) and inverse==lattice(x,True),x)
    actual=[]
    for m in [2,3,4,9,16,25]:
        lo,hi=actual_D(F(m))
        checked('bounded-native-scalar',0<lo<=hi,(m,lo,hi))
        # Retain exact outward dyadic endpoints. These are finite tests only.
        actual.append({'m':m,'lower_numerator':lo,'upper_numerator':hi,'denominator_power':BITS})
    for a,b in [(3,6),(4,8),(9,16)]:
        a=F(a);b=F(b);la,ua=actual_D(a);lb,ub=actual_D(b)
        for theta in [F(1,4),F(1,2),F(3,4)]:
            x=a+theta*(b-a);lx,ux=actual_D(x)
            qlo=F(lx)-(1-theta)*ua-theta*ub
            qhi=F(ux)-(1-theta)*la-theta*lb
            _,lu=log_bounds(int(4*b*b))
            budget=F(lu)*(8*(b-a)**2/a+3*(b-a)/(4*a*a))
            checked('bounded-native-interpolation',max(abs(qlo),abs(qhi))<budget,(a,b,theta))
    return {'schema':'riemann.prime-curvature.v1','parent':BASE,
            'rh_proved':False,'failure_count_upper_bound_proved':False,
            'new_native_positive_range':False,'independent_review':False,
            'counts':counts,'total_bounded_fixtures':sum(counts.values()),
            'fixture_digest':digest.hexdigest(),'native_scalar_samples':actual,
            'primitive_scope':{'factorization_through':2500,'log_series_terms':40,
                'dyadic_bits':BITS,'sample_m_max':25},
            'proof_scope':'Paper theorems; bounded checks do not prove infinite passages.'}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--check',type=Path);ap.add_argument('--write',type=Path)
    ns=ap.parse_args()
    authenticate(check_result=not bool(ns.write))
    result=reconstruct();text=canonical(result)
    if ns.check:
        got=strict_json(ns.check.read_text())
        require(canonical(got)==text,'result reconstruction mismatch')
    if ns.write:ns.write.write_text(text)
    print(text,end='')

if __name__=='__main__':
    try:main()
    except (ValueError,KeyError,FileNotFoundError,json.JSONDecodeError) as exc:
        raise SystemExit('REJECT: '+str(exc))
