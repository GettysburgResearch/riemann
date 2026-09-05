#!/usr/bin/env python3
"""Exact finite identities and rational source bounds; not a proof of RH."""
from __future__ import annotations
import argparse
from dataclasses import dataclass
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parent
DEN = 10**40
COUNT = 0
B = F(3, 2)
LOCK = {
    'publication_parent': 'dc4bb9dbb49876732eb656339e79ee4ec43b157f',
    'mathematical_parent': '39c13367f4b3956631ea1e00fac6c3005fc32057',
    'parent_path': '../cross-route-hardy-laguerre/BRIDGE.md',
    'parent_git_blob': '81d7d5db7a25f5875a08c10235fdb514d67cc744',
}

def check(ok: bool, label: str) -> None:
    global COUNT
    if not ok:
        raise ValueError('CHECK_FAILED: ' + label)
    COUNT += 1

@dataclass(frozen=True)
class IV:
    lo: F
    hi: F
    def __post_init__(self):
        if self.lo > self.hi:
            raise ValueError('reversed interval')
    @staticmethod
    def cast(x):
        return x if isinstance(x, IV) else IV(F(x), F(x))
    @staticmethod
    def bound(lo, hi):
        lo, hi = F(lo), F(hi)
        return IV(F((lo*DEN).__floor__(), DEN), F((hi*DEN).__ceil__(), DEN))
    def __add__(self, x):
        x = IV.cast(x)
        return IV.bound(self.lo+x.lo, self.hi+x.hi)
    __radd__ = __add__
    def __neg__(self): return IV(-self.hi, -self.lo)
    def __sub__(self, x): return self + -IV.cast(x)
    def __rsub__(self, x): return IV.cast(x) + -self
    def __mul__(self, x):
        x = IV.cast(x)
        p = [self.lo*x.lo, self.lo*x.hi, self.hi*x.lo, self.hi*x.hi]
        return IV.bound(min(p), max(p))
    __rmul__ = __mul__
    def __truediv__(self, x):
        x = IV.cast(x)
        if x.lo <= 0 <= x.hi:
            raise ValueError('interval division by possible zero')
        return self * IV.bound(1/x.hi, 1/x.lo)
    def __rtruediv__(self, x): return IV.cast(x)/self
    def __pow__(self, n):
        if type(n) is not int: raise ValueError('integer exponent required')
        if n < 0: return (1/self)**(-n)
        r = IV.cast(1)
        for _ in range(n): r = r*self
        return r

def exp_rat(x, terms=60):
    x = F(x)
    if x < 0: return 1/exp_rat(-x, terms)
    k = 0
    while x > 1: x /= 2; k += 1
    t = F(1); s = t
    for j in range(1, terms+1): t *= x/j; s += t
    err = t*x/(terms+1)/(1-x/F(terms+2))
    ans = IV.bound(s, s+err)
    for _ in range(k): ans = ans*ans
    return ans

def log_rat(x, terms=60):
    x = F(x)
    if x <= 0: raise ValueError('log domain')
    k = 0
    while x > 2: x /= 2; k += 1
    while x < 1: x *= 2; k -= 1
    def base(t):
        y = (t-1)/(t+1)
        s = 2*sum((y**(2*j+1)/F(2*j+1) for j in range(terms)), F(0))
        err = 2*y**(2*terms+1)/(F(2*terms+1)*(1-y*y))
        return IV.bound(s, s+err)
    return base(x) + k*base(F(2))

def log_iv(x):
    x = IV.cast(x)
    return IV(log_rat(x.lo).lo, log_rat(x.hi).hi)

def atan_inv(k, terms=50):
    s = sum((F((-1)**j, (2*j+1)*k**(2*j+1)) for j in range(terms)), F(0))
    t = F((-1)**terms, (2*terms+1)*k**(2*terms+1))
    return IV.bound(min(s, s+t), max(s, s+t))

def bernoulli(n):
    a = [F(0)]*(n+1); out = []
    for m in range(n+1):
        a[m] = F(1, m+1)
        for j in range(m, 0, -1): a[j-1] = j*(a[j-1]-a[j])
        out.append(a[0])
    return out

def source_constants():
    N, m = 32, 6
    bs = bernoulli(2*m)
    check(bs[2] == F(1, 6) and bs[12] == F(-691, 2730), 'Bernoulli anchors')
    logs = [IV.cast(0)] + [log_rat(n) for n in range(1, N+1)]
    ln = logs[N]
    z = IV.cast(sum((F(1,n*n) for n in range(1,N)),F(0))) + F(1,N)+F(1,2*N*N)
    zp = -sum((logs[n]/(n*n) for n in range(1,N)),IV.cast(0))-(ln+1)/N-ln/(2*N*N)
    for k in range(1,m+1):
        c = bs[2*k]/N**(2*k+1)
        z += c
        zp += c*(sum((F(1,j) for j in range(2,2*k+1)),F(0))-ln)
    prod = F(1)
    for j in range(2*m): prod *= F(9,4)+j
    r0 = abs(bs[2*m])*prod/(factorial(2*m)*(2*m)*N**(2*m))
    z += IV(-r0,r0); zp += IV(-4*r0,4*r0)
    p2 = -zp/z
    ge = IV.cast(sum((F(1,n) for n in range(1,N)),F(0)))-ln+F(1,2*N)
    for k in range(1,m+1): ge += bs[2*k]/(2*k*N**(2*k))
    er = abs(bs[2*m])/(2*m*N**(2*m))
    ge += IV(-er,er)
    pi = 16*atan_inv(5)-4*atan_inv(239)
    cb = (1-ge-log_iv(2*pi))/3
    check(F(569,1000)<p2.lo and p2.hi<F(571,1000), 'actual P2 rough enclosure')
    check(-F(1,2)<cb.lo and cb.hi<0, 'actual Cb range')
    return {'P2':p2,'gamma_E':ge,'pi':pi,'C_b':cb,'EM_r0':IV.cast(r0)}

def kernel_values(x, const):
    x = F(x)
    ep, em = exp_rat(B*x), exp_rat(-B*x)
    ec, enc = exp_rat(x/2), exp_rat(-x/2)
    u = exp_rat(-x)
    lp, lm = log_iv(1+u), log_iv(1-u)
    sg = (em*(lp-lm)+ep*(lp+lm)+enc)/6
    dsg = (-em*(lp-lm)+ep*(lp+lm)+enc)/4
    p2, cb = const['P2'], const['C_b']
    w = ec/2+cb*em+sg-p2/B*(ep+em)/2
    wp = ec/4-B*cb*em+dsg-p2*(ep-em)/2
    return w,wp,sg,dsg

def arithmetic_certificate():
    c = source_constants(); L = F(1,20)
    w,wp,sg,dsg = kernel_values(L,c)
    check(w.lo>F(1,250), 'W(1/20)>1/250')
    check(w.hi<F(1,200), 'W(1/20)<1/200')
    check(wp.hi<-F(1,3), 'Wprime(1/20)<-1/3')
    co = (exp_rat(F(3,40))+exp_rat(-F(3,40)))/2
    check(co.hi<F(101,100), 'cosh curvature bound')
    check(F(35,4)-F(9,8)-F(9,10)*F(101,100)>6, 'uniform curvature lower bound')
    check(F(1,250)+F(1,3)*L/2==F(37,3000), 'primitive coercivity constant')
    check(L+F(1,200)*3<F(1,10), 'positive extension support upper bound')
    # A strict arithmetic separation: the actual kernel is negative at 1/10.
    # This refutes only a global nonnegative-convex continuation of W, not PSD.
    w10,_,_,_ = kernel_values(F(1,10),c)
    check(w10.hi<-F(1,200), 'W(1/10)<-1/200')
    c.update({'W_L':w,'Wprime_L':wp,'gamma_series_L':sg,'gamma_series_derivative_L':dsg,'W_1_10':w10})
    return c

def finite_identities():
    # Exact rank-two tail: t_i=4 log r_i, with rational r_i>=1;
    # log-prime weights are replaced by declared rational fixture weights only.
    nodes = [F(1),F(5,4),F(3,2),F(2)]
    for k in (5,7,11):
        n = k*k
        for i in nodes:
            for j in nodes:
                ratio = i/j
                # n>max exp(|t_i-t_j|); n^(+-3/2) and damping are rational here.
                direct = -F(1,2*k)*(i*j)**(-3)*F(1,k**3)*(ratio**6+ratio**(-6))
                outer = -F(1,2*n*n)*(i**3*j**(-9)+i**(-9)*j**3)
                check(direct==outer,'literal remote-atom / rank-two identity')
    for R in (F(5,4),F(3,2),F(2),F(3)):
        A=(R**6-1)/B; D=(1-R**(-18))/(3*B); C=(1-R**(-6))/B
        check(A*D>C*C,'strict two-channel independence')
        for tau in (F(1,7),F(2,5)):
            mat=[[-tau*C/2,-tau*D/2],[-tau*A/2,-tau*C/2]]
            tr=mat[0][0]+mat[1][1]
            det=mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]
            check(tr==-tau*C,'tail trace')
            check(det==tau*tau*(C*C-A*D)/4<0,'one positive and one negative eigenvalue')
            check(tr*tr-4*det==tau*tau*A*D,'exact squared trace norm')
    for j in range(1,41):
        cc=2*j+F(1,2)
        check(1/(cc*cc-B*B)==F(1,3*(2*j-1))-F(1,6*(j+1)), 'gamma closed-form coefficient')
        check(cc*cc/(cc*cc-B*B)<=F(25,16), 'integrable curvature bound')
    # The triangle Gram is reconstructed as an exact interval-overlap norm.
    nodes2=[F(0),F(1,9),F(1,3),F(2,3),F(1)]
    weights=[F(2),F(-3),F(1,2),F(4),F(-1)]
    for scale in (F(1,7),F(1,3),F(1),F(7,5)):
        for n in range(1,6):
            ts=nodes2[:n]; cs=weights[:n]
            gram=sum((cs[i]*cs[j]*max(F(0),scale-abs(ts[i]-ts[j])) for i in range(n) for j in range(n)),F(0))
            cuts=sorted(set(ts+[t+scale for t in ts])); norm=F(0)
            for left,right in zip(cuts,cuts[1:]):
                mid=(left+right)/2
                val=sum((v for t,v in zip(ts,cs) if t<=mid<t+scale),F(0))
                norm+=(right-left)*val*val
            check(gram==norm>=0,'triangle integral Gram factorization')
    for n in range(1,6):
        ts=nodes2[:n]; cs=weights[:n]; mass=sum(cs,F(0)); primitive=F(0)
        cuts=sorted(set([F(0),F(1)]+ts))
        for left,right in zip(cuts,cuts[1:]):
            mid=(left+right)/2
            val=sum((v for t,v in zip(ts,cs) if t<=mid),F(0))-mass/2
            primitive+=(right-left)*val*val
        direct=sum((cs[i]*cs[j]*(1-abs(ts[i]-ts[j])) for i in range(n) for j in range(n)),F(0))
        check(direct==mass*mass/2+2*primitive,'primitive norm identity')

def git_blob(data):
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

def no_duplicates(pairs):
    out={}
    for k,v in pairs:
        if k in out: raise ValueError('DUPLICATE_JSON_KEY')
        out[k]=v
    return out

def read_json(path):
    return json.loads(path.read_text(),object_pairs_hook=no_duplicates)

def equal_exact(a,b):
    if type(a) is not type(b): return False
    if isinstance(a,dict): return a.keys()==b.keys() and all(equal_exact(a[k],b[k]) for k in a)
    if isinstance(a,list): return len(a)==len(b) and all(equal_exact(x,y) for x,y in zip(a,b))
    return a==b

def build():
    global COUNT
    COUNT=0
    lock=read_json(ROOT/'SOURCE_LOCK.json')
    check(equal_exact(lock,LOCK),'literal parent lock')
    parent=(ROOT/LOCK['parent_path']).resolve()
    check(git_blob(parent.read_bytes())==LOCK['parent_git_blob'],'parent proof blob')
    finite_identities()
    c=arithmetic_certificate()
    def pack(v): return {'lo':str(v.lo),'hi':str(v.hi)}
    return {
        'status':'FINITE_IDENTITIES_AND_SOURCE_INTERVALS_ONLY',
        'RH_proved':False,
        'checks':COUNT,
        'scope_L':'1/20',
        'constants':{k:pack(v) for k,v in c.items()},
        'source_lock':lock,
        'sha256':{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in ['PROOF.md','SOURCES.md','verify_window.py','SOURCE_LOCK.json']},
    }

def main():
    p=argparse.ArgumentParser(description=__doc__)
    group=p.add_mutually_exclusive_group();group.add_argument('--write',type=Path);group.add_argument('--check',type=Path)
    args=p.parse_args(); out=build()
    if args.check and not equal_exact(read_json(args.check),out): raise ValueError('RESULT_MISMATCH')
    text=json.dumps(out,sort_keys=True,indent=2)+'\n'
    if args.write:args.write.write_text(text)
    sys.stdout.write(text)

if __name__=='__main__':
    try: main()
    except (ValueError, OSError, ZeroDivisionError) as exc:
        print(str(exc),file=sys.stderr);sys.exit(1)
