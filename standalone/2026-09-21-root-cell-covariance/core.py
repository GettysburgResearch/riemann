"""Integer-directed arithmetic and integer-square observation grids."""
from math import isqrt
import json
from pathlib import Path

BITS=128
S=1<<BITS

def need(ok, message):
    if not ok: raise ValueError(message)

def add(a,b): return (a[0]+b[0], a[1]+b[1])
def neg(a): return (-a[1],-a[0])
def sub(a,b): return add(a,neg(b))
def integer(n): return (n*S,n*S)
def rat(n,d=1):
    need(d>0,'positive denominator')
    return (n*S//d, -((-n*S)//d))
def mul(a,b):
    v=[x*y for x in a for y in b]
    return (min(v)//S, -((-max(v))//S))
def scale(a,n): return (a[0]*n,a[1]*n) if n>=0 else (a[1]*n,a[0]*n)
def divint(a,n):
    need(n>0,'positive divisor')
    return (a[0]//n,-((-a[1])//n))
def square(a):
    vals=[a[0]**2,a[1]**2]
    lo=0 if a[0]<=0<=a[1] else min(vals)
    return (lo//S,-((-max(vals))//S))
def divide(a,b):
    need(b[0]>0,'positive interval divisor')
    vs=[(x*S)//y for x in a for y in b]
    ws=[-((-x*S)//y) for x in a for y in b]
    return min(vs),max(ws)
def nonnegative(a):
    need(a[1]>=0,'negative enclosure of nonnegative quantity')
    return max(0,a[0]),a[1]
def overlap(a,b): return max(a[0],b[0])<=min(a[1],b[1])
def contains(a,b): return a[0]<=b[0]<=b[1]<=a[1]
def show(a): return (a[0]+a[1])/(2*S) # descriptive only

def cells(start, stop, resolution=1):
    """Partition inclusive integers by floor(q*sqrt(k)); no float endpoints."""
    need(type(start) is int and type(stop) is int and 1<=start<=stop,'grid range')
    need(type(resolution) is int and resolution>=1,'grid resolution')
    q2=resolution**2
    s=start
    while s<=stop:
        j=isqrt(q2*s)
        t=min(stop,((j+1)**2-1)//q2)
        need(t>=s,'grid progress')
        yield s,t
        s=t+1

def canonical(obj): return json.dumps(obj,sort_keys=True,separators=(',',':'),ensure_ascii=True)
def strict_read(path):
    def pairs(xs):
        out={}
        for k,v in xs:
            need(k not in out,'duplicate key');out[k]=v
        return out
    def bad(x): raise ValueError('nonfinite JSON')
    return json.loads(Path(path).read_text(),object_pairs_hook=pairs,parse_constant=bad)

def typed_equal(a,b):
    need(type(a) is type(b),'numeric type or structural alias')
    if isinstance(a,dict):
        need(a.keys()==b.keys(),'keys')
        for k in a: typed_equal(a[k],b[k])
    elif isinstance(a,list):
        need(len(a)==len(b),'length')
        for x,y in zip(a,b):typed_equal(x,y)
    else: need(a==b,'changed value')
