#!/usr/bin/env python3
"""Exact finite algebra for PROOF.md. This script does not prove RH.

Python >=3.10; standard library only. No prime sweep or special-function
numerics. Analytic convergence, all-degree estimates and the actual prime
cancellation remain mathematical proof obligations, not checker outputs.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from collections import Counter
from fractions import Fraction as Q
from math import comb, factorial
from pathlib import Path

G = tuple[Q, Q]

def g(x=0, y=0) -> G:
    return Q(x), Q(y)

def ga(a: G, b: G) -> G:
    return a[0]+b[0], a[1]+b[1]

def gs(a: G, b: G) -> G:
    return a[0]-b[0], a[1]-b[1]

def gm(a: G, b: G) -> G:
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]

def gd(a: G, b: G) -> G:
    norm = b[0]**2+b[1]**2
    if not norm:
        raise ValueError('zero denominator')
    return (a[0]*b[0]+a[1]*b[1])/norm, (a[1]*b[0]-a[0]*b[1])/norm

def gp(a: G, n: int) -> G:
    degree(n)
    out = g(1)
    for _ in range(n):
        out = gm(out, a)
    return out

def greal(a: G) -> Q:
    if a[1]:
        raise ValueError('unpaired complex value')
    return a[0]

def gsum(values) -> G:
    out = g()
    for a in values:
        out = ga(out, a)
    return out

def degree(n: int) -> None:
    if type(n) is not int or n < 0:
        raise ValueError('degree must be a nonnegative integer, not a Boolean')

def trim(p: list[Q]) -> list[Q]:
    while len(p)>1 and not p[-1]:
        p.pop()
    return p

def pa(a: list[Q], b: list[Q]) -> list[Q]:
    out = [Q(0)]*max(len(a),len(b))
    for j, v in enumerate(a): out[j] += v
    for j, v in enumerate(b): out[j] += v
    return trim(out)

def scale(a: list[Q], c: Q) -> list[Q]:
    return trim([c*x for x in a])

def pm(a: list[Q], b: list[Q]) -> list[Q]:
    out = [Q(0)]*(len(a)+len(b)-1)
    for j, u in enumerate(a):
        for k, v in enumerate(b): out[j+k] += u*v
    return trim(out)

def pe(a: list[Q], x: G) -> G:
    out = g()
    for c in reversed(a): out = ga(gm(out,x),g(c))
    return out

def compose_linear(a: list[Q], c0: Q, c1: Q) -> list[Q]:
    out = [Q(0)]
    for c in reversed(a): out = pa(pm(out,[c0,c1]),[c])
    return out

def derivative(a: list[Q]) -> list[Q]:
    return trim([j*a[j] for j in range(1,len(a))] or [Q(0)])

def chebyshev(n: int) -> list[list[Q]]:
    degree(n)
    out = [[Q(1)]]
    if n: out.append([Q(0),Q(1)])
    for j in range(1,n):
        out.append(pa(pm([Q(0),Q(2)],out[j]),scale(out[j-1],Q(-1))))
    return out

def cheb_expand(p: list[Q], basis: list[list[Q]]) -> list[Q]:
    n = len(p)-1
    residual = p[:]
    out = [Q(0)]*(n+1)
    for j in range(n,-1,-1):
        c = residual[j] if j<len(residual) else Q(0)
        out[j] = c/basis[j][-1]
        residual = pa(residual,scale(basis[j],-out[j]))
    if any(residual): raise RuntimeError('Chebyshev division residual')
    return out

def laguerre(n: int, alpha: int) -> list[list[Q]]:
    degree(n)
    if type(alpha) is not int or alpha not in (-1,0):
        raise ValueError('only alpha=-1,0 is implemented')
    out = [[Q(1)]]
    if n: out.append([Q(1+alpha),Q(-1)])
    for j in range(2,n+1):
        p = pa(pm([Q(2*j-1+alpha),Q(-1)],out[-1]),
               scale(out[-2],Q(-(j-1+alpha))))
        out.append(scale(p,Q(1,j)))
    return out

def lag_closed(n: int) -> list[Q]:
    degree(n)
    if n == 0: return [Q(1)]
    return [Q(0)]+[Q((-1)**j*comb(n-1,j-1),factorial(j)) for j in range(1,n+1)]

def exp_cayley(x: Q, n: int) -> list[Q]:
    """Taylor of exp(x*w/(1+w)) via the exponential differential equation."""
    degree(n)
    log_coeff = [Q(0)]+[x*(-1)**(j-1) for j in range(1,n+1)]
    out = [Q(1)]
    for k in range(1,n+1):
        out.append(sum((j*log_coeff[j]*out[k-j] for j in range(1,k+1)),Q(0))/k)
    return out

def rational_jet(num: list[G], den: list[G], n: int) -> list[G]:
    degree(n)
    out=[]
    for k in range(n+1):
        value=num[k] if k<len(num) else g()
        for j in range(1,min(k,len(den)-1)+1):
            value=gs(value,gm(den[j],out[k-j]))
        out.append(gd(value,den[0]))
    return out

def laplace_poly(p: list[Q], q: G) -> G:
    """Exact integral of exp(-q*y)*p(3*y), when Re(q)>0."""
    if q[0] <= 0: raise ValueError('positive real part required for Laplace input')
    return gsum(gd(g(c*3**j*factorial(j)),gp(q,j+1)) for j,c in enumerate(p))

def product_polynomial(params: list[G]) -> list[Q]:
    if not params or Counter(params)!=Counter((a,-b) for a,b in params):
        raise ValueError('nonempty multiplicity-matched conjugate spectrum required')
    out=[g(1)]
    for a in params:
        nxt=[g()]*(len(out)+1)
        for j,c in enumerate(out):
            nxt[j]=ga(nxt[j],c)
            nxt[j+1]=ga(nxt[j+1],gd(c,a))
        out=nxt
    return [greal(c) for c in out]

def formal_moments(p: list[Q], v: Q, n: int) -> list[Q]:
    """Independent Taylor division for v*h(v*(1+y))."""
    local=compose_linear(p,v,v)
    jets=rational_jet([g(c) for c in derivative(local)],[g(c) for c in local],n)
    return [(-1)**j*greal(c) for j,c in enumerate(jets)]

def functional(p: list[Q], moments: list[Q]) -> Q:
    if len(p)>len(moments): raise ValueError('insufficient moment data')
    return sum((c*moments[j] for j,c in enumerate(p)),Q(0))

class Checks:
    def __init__(self): self.groups=Counter()
    def require(self, group: str, condition: bool):
        self.groups[group]+=1
        if not condition: raise RuntimeError('FAILED: '+group)
    def refuses(self, fn):
        try: fn()
        except ValueError:
            self.require('input_refusals',True)
            return
        self.require('input_refusals',False)

PARENT_GIT_BLOBS={
    'GROWTH.md':'c19930a24cefb6d5543098b9958f47a1d71acd87',
    'README.md':'65fbdbb1407b7a169745daae7216cc0fd7cb8ae5',
    'verify_exact.py':'44bf0d6ac36d9bc6f5e4e7019ebc7b14eeb2deda',
    'result.json':'ff9146a57e2ce528efbdfb2bceecb221203cbbfa',
}

def run() -> dict:
    ck=Checks(); nmax=32
    lm=laguerre(nmax,-1); l0=laguerre(nmax,0); cb=chebyshev(nmax)
    for n in range(nmax+1):
        ck.require('Laguerre_closed_form', lm[n]==lag_closed(n))
        if n:
            ck.require('Laguerre_derivative',derivative(lm[n])==scale(l0[n-1],Q(-1)))
            ck.require('integration_by_parts_kernel',
                pa(scale(lm[n],Q(2)),scale(l0[n-1],Q(3)))==pa(scale(l0[n],Q(2)),l0[n-1]))
            ck.require('exact_polar_integral',laplace_poly(lm[n],g(1))==g((-1)**n*3*2**(n-1)))
    for x in (Q(1,2),Q(1),Q(3),Q(10),Q(100)):
        jets=exp_cayley(x,nmax)
        for n in range(nmax+1):
            ck.require('prime_atom_generating_identity',jets[n]==(-1)**n*greal(pe(lm[n],g(x))))
    # Rational coefficient tests; none of these input atoms is labelled an actual prime.
    for q in (g(1),g(2),g(Q(5,4),-1),g(Q(5,4),1)):
        r=gd(gs(g(3),q),q)
        jets=rational_jet([g(1),g(1)],[q,gs(q,g(3))],nmax)
        for n in range(1,nmax+1):
            integral=laplace_poly(lm[n],q)
            expected=gm(g((-1)**n*3),gd(gp(r,n-1),gp(q,2)))
            ck.require('Laplace_complex_atom',integral==expected)
            ck.require('rational_pole_vs_Laplace',jets[n]==gm(g((-1)**n),integral))
    for ell in range(1,26):
        jet=rational_jet([g(1),g(1)],[g(2*ell),g(2*ell-3)],nmax)
        for n in range(1,nmax+1):
            expected=Q(3,4*ell**2)*(-1+Q(3,2*ell))**(n-1)
            ck.require('archimedean_pole_coefficients',jet[n]==g(expected))
    for n in range(1,nmax+1):
        integral=sum((Q(comb(n-1,j))*(-Q(3,2))**j*Q(1,2**(j+1)*(j+1))
                      for j in range(n)),Q(0))
        ck.require('archimedean_integral',integral==Q(2,3*n)*(1-Q(1,4)**n))
        # Finite partial sum represents the actual remaining m>=1 gamma terms.
        arch=Q(-3,8)*sum((Q(3,4*ell**2)*(-1+Q(3,2*ell))**(n-1)
                          for ell in range(2,26)),Q(0))
        s=sum((Q(1,ell**2)*(1-Q(3,2*ell))**(n-1) for ell in range(2,26)),Q(0))
        ck.require('archimedean_sign_factor',arch==(-1)**n*Q(9,32)*s)
        if n>=2:
            xm=Q(3*(n+1),4)
            fm=xm**(-2)*(1-Q(3,2)/xm)**(n-1)
            ck.require('archimedean_maximum_bound',fm<=Q(16,9*(n+1)**2))
    fixtures=[
        [g(1),g(2),g(5)],
        [g(1),g(2,1),g(2,-1)],
        [g(1),g(2,1),g(2,-1),g(2,1),g(2,-1)],
    ]
    lamb=Q(8,9); v=Q(2); b=Q(9,4)
    transfer=[]
    for n in range(nmax+1):
        p=compose_linear(cb[n],lamb-1,lamb)
        coeff=cheb_expand(p,cb)
        reconstruction=[Q(0)]
        for j,c in enumerate(coeff): reconstruction=pa(reconstruction,scale(cb[j],c))
        ck.require('Chebyshev_affine_expansion',reconstruction==p)
        ck.require('Chebyshev_coefficient_bounds',abs(coeff[0])<=1 and all(abs(c)<=2 for c in coeff[1:]))
        parseval=coeff[0]**2+sum((c*c/2 for c in coeff[1:]),Q(0))
        ck.require('Chebyshev_Parseval_bound',parseval<=1)
        ck.require('Chebyshev_l1_bound',sum(map(abs,coeff))**2<=2*n+1)
        transfer.append(coeff)
    for params in fixtures:
        f=product_polynomial(params)
        shifted=compose_linear(f,Q(-1,4),Q(1))
        mo=formal_moments(f,v,nmax); mc=formal_moments(shifted,b,nmax)
        d=[functional(compose_linear(p,Q(-1),Q(2)),mc) for p in cb]
        for n in range(nmax+1):
            ck.require('source_shift_moments',mo[n]==lamb**(n+1)*mc[n])
            orig=functional(compose_linear(cb[n],Q(-1),Q(2)),mo)
            rhs=lamb*sum((a*d[j] for j,a in enumerate(transfer[n])),Q(0))
            ck.require('original_trace_return',orig==rhs)
        center_nodes=[gd(g(b),ga(g(v),a)) for a in params]
        for w in (g(Q(1,10)),g(Q(1,20),Q(1,30))):
            s=gd(gs(g(2),w),ga(g(1),w))
            u=gm(s,gs(s,g(1)))
            qlog=gm(gs(gm(g(2),s),g(1)),gd(pe(derivative(f),u),pe(f,u)))
            rhs=ga(g(d[0]/2),gm(g(Q(3,8)),qlog))
            terms=[]
            for k in center_nodes:
                x=gs(gm(g(2),k),g(1))
                terms.append(gd(gm(k,gs(g(1),gm(x,w))),ga(gs(g(1),gm(g(2),gm(x,w))),gp(w,2))))
            ck.require('centered_log_derivative_generating_identity',rhs==gsum(terms))
    rho=g(Q(3,4),1); q=gs(g(2),rho); r=gd(ga(g(1),rho),q)
    ck.require('positive_density_model_rate',r[0]**2+r[1]**2==Q(65,41))
    model=[str(Q(1,2)*laplace_poly(lm[n],q)[0]) for n in range(1,9)]
    ck.require('tail_log_constant',sum((Q(7,10)**j/Q(factorial(j)) for j in range(4)),Q(0))>2)
    ck.require('tail_exponent_constant',Q(8,3)-3*Q(7,10)>Q(1,2))
    for bad in (-1,True,1.0): ck.refuses(lambda bad=bad:laguerre(bad,-1))
    ck.refuses(lambda:laplace_poly([Q(1)],g(0)))
    ck.refuses(lambda:product_polynomial([g(2,1)]))
    ck.refuses(lambda:functional([Q(1),Q(1)],[Q(1)]))
    folder=Path(__file__).resolve().parent
    for name,wanted in PARENT_GIT_BLOBS.items():
        data=(folder.parent/name).read_bytes()
        blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
        ck.require('parent_frozen_blob',blob==wanted)
    lock=json.loads((folder/'SOURCE_LOCK.json').read_text())
    ck.require('parent_source_lock',lock['parent_commit']=='81e336a6d62d0963216ae05f809ec4df05447eb8'
               and lock['parent_git_blobs']==PARENT_GIT_BLOBS)
    hashes={name:hashlib.sha256((folder/name).read_bytes()).hexdigest()
            for name in ('README.md','PROOF.md','verify_arithmetic.py','SOURCE_LOCK.json')}
    return {
        'status':'PASS_FINITE_ALGEBRA_ONLY',
        'rh_inequality':'NOT_PROVED',
        'arithmetic':'EXACT_RATIONAL_AND_GAUSSIAN_RATIONAL',
        'maximum_degree':nmax,
        'checks':sum(ck.groups.values()),
        'check_groups':dict(sorted(ck.groups.items())),
        'continuous_countermodel':{'not_actual_primes':True,'rate_squared':'65/41','E_1_through_E_8':model},
        'source_sha256':hashes,
        'not_run':['actual-zeta derivative evaluation','prime sweep','zero census','Lean','independent proof review'],
    }

def encoded(value) -> str:
    return json.dumps(value,sort_keys=True,indent=2,ensure_ascii=True,allow_nan=False)+'\n'

def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    parser.add_argument('--check',type=Path)
    args=parser.parse_args()
    actual=run(); text=encoded(actual)
    if args.check:
        # Canonical serialized comparison does not accept True==1 or 1.0==1 aliases.
        expected=json.loads(args.check.read_text(encoding='utf-8'))
        if encoded(expected)!=text:
            raise SystemExit('REFUSED: saved result differs from exact recomputation')
    if args.output: args.output.write_text(text,encoding='utf-8')
    print(text,end='')

if __name__=='__main__':
    main()
