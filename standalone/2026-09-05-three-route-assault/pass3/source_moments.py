"""Source-only rational interval moments at s=2; no zero data or float arithmetic.
Run from the published pass3 directory, adjacent to pass2. Proof: R1_MOMENTS.md.
"""
from fractions import Fraction as F
from math import factorial, comb
from pathlib import Path
import hashlib, importlib.util, json, sys

PARENT_SHA256 = '128df4f27cc62683a58ef74c1f374910db13b507208e00535df3e1c9a9b3c6e5'
parent = Path(__file__).resolve().parent.parent / 'pass2' / 'source_certificate.py'
if not parent.is_file():
    raise RuntimeError('missing source-locked pass2/source_certificate.py')
if hashlib.sha256(parent.read_bytes()).hexdigest() != PARENT_SHA256:
    raise RuntimeError('parent interval implementation changed')
spec = importlib.util.spec_from_file_location('locked_pass2_interval', parent)
mod = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = mod
spec.loader.exec_module(mod)
Ball, log_rational, log_ball, atan_small = mod.Ball, mod.log_rational, mod.log_ball, mod.atan_small
ORDER, N, EM = 6, 256, 12

def bernoulli(n):
    b = [F(1)]
    for m in range(1, n + 1):
        b.append(-sum((F(comb(m+1,k))*b[k] for k in range(m)), F(0))/F(m+1))
    return b

BERN = bernoulli(2*EM)

def add(a,b):
    return [a[j]+b[j] for j in range(ORDER+1)]

def scale(a,c):
    # Do not round a tiny EM prefactor before its large rising polynomial.
    if isinstance(c,(int,F)) and not isinstance(c,bool):
        c=F(c)
        return [Ball(min(v.lo*c,v.hi*c),max(v.lo*c,v.hi*c)) for v in a]
    if not isinstance(c,Ball): raise TypeError('exact scalar required')
    return [v*c for v in a]

def mul(a,b):
    return [sum((a[k]*b[j-k] for k in range(j+1)),Ball(0)) for j in range(ORDER+1)]

def unit(x=1):
    return [Ball(x)] + [Ball(0)]*ORDER

def rising_poly(s,degree):
    out=unit()
    for k in range(degree):
        f=unit(s+k); f[1]=Ball(1); out=mul(out,f)
    return out

def zeta_series(s):
    if type(s) is not int or s<2: raise ValueError('integer s>=2 required')
    ell=log_rational(F(N))
    expn=[(-ell)**j/factorial(j) for j in range(ORDER+1)]
    out=[Ball(0)]*(ORDER+1)
    for n in range(1,N):
        ln=log_rational(F(n))
        out=add(out,[(-ln)**j/F(factorial(j)*n**s) for j in range(ORDER+1)])
    inv=[Ball(F((-1)**j,(s-1)**(j+1))) for j in range(ORDER+1)]
    out=add(out,scale(mul(expn,inv),F(1,N**(s-1))))
    out=add(out,scale(expn,F(1,2*N**s)))
    for k in range(1,EM+1):
        out=add(out,scale(mul(rising_poly(s,2*k-1),expn),
                   BERN[2*k]/F(factorial(2*k)*N**(s+2*k-1))))
    # |h|<=1/4; N**(1/4)=4. Cauchy bounds every Taylor remainder.
    r=F(1,4); rising=F(1)
    for j in range(2*EM): rising*=s+r+j
    remainder=(abs(BERN[2*EM])*rising*4 /
        (F(factorial(2*EM))*(s-r+2*EM-1)*N**(s+2*EM-1)))
    return [a.widen(remainder*4**j) for j,a in enumerate(out)],remainder

def log_series(a):
    out=[Ball(0)]*(ORDER+1)
    for n in range(1,ORDER+1):
        out[n]=(n*a[n]-sum((k*out[k]*a[n-k] for k in range(1,n)),Ball(0)))/(n*a[0])
    return out

def det(a):
    if len(a)==1: return a[0][0]
    return sum(((-1)**j*a[0][j]*det([r[:j]+r[j+1:] for r in a[1:]])
                for j in range(len(a))),Ball(0))

def source_moments():
    z2,remainder=zeta_series(2); L=log_series(z2)
    ell=log_rational(F(N))
    gamma=Ball(sum((F(1,n) for n in range(1,N)),F(0)))-ell+F(1,2*N)
    for k in range(1,EM+1): gamma+=BERN[2*k]/F(2*k*N**(2*k))
    gamma=gamma.widen(abs(BERN[2*EM])/F(2*EM*N**(2*EM)))
    pi=16*atan_small(F(1,5))-4*atan_small(F(1,239))
    for j in range(1,ORDER+1):
        L[j]+=F((-1)**(j+1),j)*(1+F(1,2**j))
    L[1]-=(gamma+log_ball(pi))/2
    for j in range(2,ORDER+1):
        zj,_=zeta_series(j)
        L[j]+=zj[0]*F((-1)**j,j*2**j)
    # u=3h+h^2, the shift from invariant coordinate 2 to s=2+h.
    h=[Ball(0)]*(ORDER+1);h[1]=Ball(F(1,3))
    for j in range(2,ORDER+1):
        h[j]=-sum((h[k]*h[j-k] for k in range(1,j)),Ball(0))/3
    out=[Ball(0)]*(ORDER+1);power=unit()
    for j in range(1,ORDER+1):
        power=mul(power,h);out=add(out,scale(power,L[j]))
    p=[(-1)**(j-1)*j*out[j] for j in range(1,ORDER+1)]
    return p,remainder

def certify():
    p,rem=source_moments();checks={}; intervals={f'p{j+1}':v.decimal() for j,v in enumerate(p)}
    for shift in (0,1):
        H=[[p[i+j+shift]*200**(i+j+shift) for j in range(3)] for i in range(3)]
        for size in (1,2,3):
            d=det([r[:size] for r in H[:size]])
            label=f'shift_{shift}_leading_minor_{size}'
            checks[label]=d.lo>0;intervals[label]=d.decimal()
    if not all(checks.values()): raise ArithmeticError('actual-source Hankel certificate failed')
    return {'status':'PASS_SOURCE_S2_SIX_MOMENTS', 'arithmetic':'RATIONAL_INTERVAL_ANALYTIC_REMAINDERS',
            'center_invariant':2,'center_s':2,'order':ORDER,'N':N,'EM_order':EM,
            'parent_sha256':PARENT_SHA256,'checks':checks,'intervals':intervals,
            'zeta_complex_remainder_bound':str(rem),'RH_proved':False,
            'all_order_Hankel_positivity_proved':False}

if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args()
    result=certify();text=json.dumps(result,sort_keys=True,indent=2)+'\n'
    path=Path(__file__).with_name('MOMENTS.json')
    if args.write:path.write_text(text)
    elif not path.is_file() or path.read_text()!=text:raise SystemExit('stored source result mismatch')
    print(result['status']); print(len(result['checks']),'strict signs reconstructed')
