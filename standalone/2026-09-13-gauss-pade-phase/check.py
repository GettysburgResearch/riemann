#!/usr/bin/env python3
"""Exact BOUNDED algebra checks for GPP26. Not a machine proof of RH or of limits.

Only Python standard-library integers/Fractions enter acceptance. Diagnostic
mpmath outputs are neither imported nor compared here. --emit produces a
receipt; --check reconstructs it and enforces a strict typed comparison.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import factorial
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def trim(a):
    a=list(a)
    while len(a)>1 and not a[-1]: a.pop()
    return a or [F(0)]


def add(a,b):
    return trim([(a[i] if i<len(a) else F(0))+(b[i] if i<len(b) else F(0))
                 for i in range(max(len(a),len(b)))])


def scale(a,c): return trim([x*c for x in a])
def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return trim(c)


def shift(a,j): return [F(0)]*j+list(a)
def diff(a): return trim([i*a[i] for i in range(1,len(a))])
def at(a,x):
    v=F(0)
    for c in reversed(a): v=v*x+c
    return v


def pade(n):
    return [F(factorial(2*n-j)*factorial(n)*2**j,
              factorial(2*n)*factorial(n-j)*factorial(j)) for j in range(n+1)]


def continuants(m):
    p0,p1=[F(1)],[F(1),F(2,5)]
    q0,q1=[F(0)],[F(1)]
    if m==0: return p0,q0
    for j in range(1,m):
        b=F(12,(4*j+1)*(4*j+5))
        lam=F(36,(4*j-1)*(4*j+1)**2*(4*j+3))
        p0,p1=p1,add(mul([F(1),b],p1),scale(shift(p0,2),-lam))
        q0,q1=q1,add(mul([F(1),b],q1),scale(shift(q0,2),-lam))
    return p1,q1


def source_g(degree):
    # g=S'/S, S=sinh(sqrt(6t))/sqrt(6t); independent of Jacobi/Padé.
    s=[F(6**j,factorial(2*j+1)) for j in range(degree+2)]
    g=[]
    for j in range(degree+1):
        g.append((j+1)*s[j+1]-sum((s[k]*g[j-k] for k in range(1,j+1)),F(0)))
    return g


def p1(r): return -F(r*(4*r*r-7),6)
def p2(r): return F(r*(r-1)*(2*r-1)*(40*r**3+24*r*r-124*r-123),360)
def n1(r): return -F(r*(r+1)*(2*r+1),3)
def n2(r): return F(r*(r+1)*(2*r+1)*(40*r**3+24*r*r-16*r-123),360)


def edge_product(m,r):
    if r>m: return F(0)
    a=F(m*(2*m+3),2);v=F(1)
    for j in range(r):
        v*=1-F(j*(2*j+3),2)/a
        v*=1-F((2*j-1)*(j+1),2)/a
    return v


# Laurent polynomials in u and polynomials in S=sinh(u), C=cosh(u),
# reduced exactly by C^2=1+S^2. No symbolic/transcendental package.
def reduce_ring(p):
    out={}
    for (u,s,c),a in p.items():
        stack=[(u,s,c,a)]
        while stack:
            i,j,k,v=stack.pop()
            if k>=2:
                stack.append((i,j,k-2,v));stack.append((i,j+2,k-2,v))
            elif v:
                key=(i,j,k);out[key]=out.get(key,F(0))+v
    return {k:v for k,v in out.items() if v}


def ra(*ps):
    out={}
    for p in ps:
        for k,v in p.items(): out[k]=out.get(k,F(0))+v
    return reduce_ring(out)


def rs(p,c): return reduce_ring({k:v*c for k,v in p.items()})
def rm(p,q):
    out={}
    for i,a in p.items():
        for j,b in q.items():
            k=tuple(x+y for x,y in zip(i,j));out[k]=out.get(k,F(0))+a*b
    return reduce_ring(out)


def mon(u,s=0,c=0,v=F(1)): return {(u,s,c):F(v)}
def rd(p):
    out={}
    def put(k,v): out[k]=out.get(k,F(0))+v
    for (u,s,c),v in p.items():
        if u: put((u-1,s,c),u*v)
        if s: put((u,s-1,c+1),s*v)
        if c: put((u,s+1,c-1),c*v)
    return reduce_ring(out)


def euler(p): return rs(rm(mon(1),rd(p)),F(1,2))
def apply_poly(coeff,p):
    out={};v=p
    for a in coeff:
        out=ra(out,rs(v,a));v=euler(v)
    return out


def interpolation_coeff(fn,degree):
    # Exact Lagrange reconstruction of the explicitly given degree bound.
    out=[F(0)]
    for i in range(degree+1):
        p=[F(1)];den=F(1)
        for j in range(degree+1):
            if j!=i: p=mul(p,[F(-j),F(1)]);den*=i-j
        out=add(out,scale(p,fn(i)/den))
    for i in range(degree+1,degree+12):
        require(at(out,F(i))==fn(i),'polynomial reconstruction')
    return out


def ring_controls():
    d0,n0=mon(0,c=1),mon(-1,s=1)
    d1=ra(mon(3,s=1,v=F(-1,12)),mon(2,c=1,v=F(-1,4)),mon(1,s=1,v=F(1,2)))
    nn1=ra(mon(2,c=1,v=F(-1,12)),mon(1,s=1,v=F(-1,4)))
    d2=ra(mon(6,c=1,v=F(1,288)),mon(5,s=1,v=F(11,240)),
          mon(4,c=1,v=F(11,96)),mon(3,s=1,v=F(-1,12)))
    nn2=ra(mon(5,s=1,v=F(1,288)),mon(4,c=1,v=F(11,240)),
           mon(3,s=1,v=F(5,32)),mon(2,c=1,v=F(1,24)),mon(1,s=1,v=F(-1,4)))
    for fn,deg,base,want in [(p1,3,d0,d1),(p2,6,d0,d2),(n1,3,n0,nn1),(n2,6,n0,nn2)]:
        require(apply_poly(interpolation_coeff(fn,deg),base)==want,'Euler sum identity')
    quotient=rs(rm(mon(2),ra(rm(nn2,rm(d0,d0)),rs(rm(nn1,rm(d1,d0)),-1),
                                    rm(n0,ra(rm(d1,d1),rs(rm(d2,d0),-1))))),F(3,2))
    stated=rs(rm(mon(3),ra(mon(4,s=1,v=-5),mon(3,c=1,v=18),mon(2,s=1,v=60),
                                      mon(1,c=1,v=30),mon(0,s=1,v=-180))),F(1,480))
    require(quotient==stated,'complete hyperbolic quotient identity')
    return 5


def compute():
    counts={'pade_orders':0,'pade_exponential_coefficients':0,'phase_coefficient_tests':0,
            'source_matching_coefficients':0,'source_pade_links':0,'edge_remainder_tests':0,
            'edge_elementary_coefficients':0,'bulk_rational_panels':0,'mellin_correction_panels':0}
    g=source_g(48)
    for n in range(1,50):
        p=pade(n);pn=[(-1)**j*v for j,v in enumerate(p)]
        # Padé exponential matching through degree 2n.
        exp=[F(2**j,factorial(j)) for j in range(2*n+1)]
        prod=mul(exp,pn)
        for j in range(2*n+1):
            require((p[j] if j<len(p) else 0)==prod[j],'Pade exponential match')
            counts['pade_exponential_coefficients']+=1
        ode=add(shift(diff(diff(p)),1),add(scale(mul([F(n),F(1)],diff(p)),-2),scale(p,2*n)))
        require(ode==[0],'Pade ODE')
        U=mul(p,pn)
        W=add(mul(diff(p),pn),mul(p,[(-1)**j*v for j,v in enumerate(diff(p))]))
        rhs=scale(U,2);rhs[-1]-=2*(-1)**n*p[-1]**2
        require(trim(W)==trim(rhs),'Wronskian phase formula')
        c=F(1)
        for j in range(n+1):
            if j: c*=F(2*(n-j+1),j*(2*n-2*j+1)*(2*n-j+1))
            require((-1)**j*U[2*j]==c and c>0,'positive phase modulus coefficient')
            counts['phase_coefficient_tests']+=1
        require(c==p[-1]**2,'phase highest coefficient')
        counts['pade_orders']+=1
    for m in range(1,25):
        p,q=continuants(m);n=2*m+1
        pp=[F(0)]*(2*m+1);qq=[F(0)]*(2*m-1)
        for j,c in enumerate(p): pp[2*j]=c/F(6**j)
        for j,c in enumerate(q): qq[2*j]=c/F(6**j)
        link=add(mul([F(1),F(1)],pp),scale(shift(qq,2),F(1,3)))
        require(link==pade(n),'source/Pade exact link')
        counts['source_pade_links']+=1
        pg=mul(p,g)
        for j in range(2*m):
            require(pg[j]==(q[j] if j<len(q) else 0),'native sinh series quadrature matching')
            counts['source_matching_coefficients']+=1
        # Complete square residual, clearing all denominators.
        expr=add(scale(shift(add(mul(diff(q),p),scale(mul(q,diff(p)),-1)),1),2),
                 add(scale(mul(q,p),3),add(scale(shift(mul(q,q),1),2),scale(mul(p,p),-3))))
        want=[F(0)]*(2*m)+[-3*p[-1]**2]
        require(expr==want,'square residual')
    for r in range(1,101):
        factors=[]
        for j in range(r): factors.extend([F(j*(2*j+3),2),F((2*j-1)*(j+1),2)])
        S=sum(factors,F(0));E2=sum((factors[i]*factors[j] for i in range(len(factors)) for j in range(i)),F(0))
        require(-S==p1(r) and E2==p2(r),'edge elementary polynomial coefficient')
        d=F(r*(2*r+3),2)
        require(n1(r)==p1(r)-d and n2(r)==p2(r)-d*p1(r),'numerator correction coefficient')
        counts['edge_elementary_coefficients']+=4
    for m in range(1,41):
        a=F(m*(2*m+3),2)
        for r in range(1,3*m+2):
            v=edge_product(m,r);w=v*(1-F(r*(2*r+3),2)/a)
            require(abs(v-1-p1(r)/a-p2(r)/a**2)<=4*F(r**9)/a**3,'denominator complete coefficient bound')
            require(abs(w-1-n1(r)/a-n2(r)/a**2)<=16*F(r**9)/a**3,'numerator complete coefficient bound')
            counts['edge_remainder_tests']+=2
    bulk=[]
    for n in range(3,100,2):
        an=pade(n)[-1];R=F(n,2);exact=an**2*R**(2*n);simple=F(3,4)**(2*n)
        require(exact<simple<1,'bulk exponential slope bound')
        delta=an**2*R**(2*n+1)/(2*n+1)
        j=0
        while F(j+1)*F(22,7)+delta<=R:j+=1
        # Pi upper bound used only to select valid bulk crossings.
        counts['bulk_rational_panels']+=1
        if n in (17,33,65,99):
            bulk.append({'n':n,'m':(n-1)//2,'guaranteed_crossings':j,
                         'phase_error_upper':str(delta),'slope_defect_upper':str(exact)})
    counts['hyperbolic_ring_identities']=ring_controls()
    # Gamma recurrence / dyadic factors in K2/C. No eta value is an input.
    for s in [F(1,5),F(1,2),F(1),F(7,4),F(3),F(11,2)]:
        q=(s+1)/2
        rise=lambda r: __import__('functools').reduce(lambda a,j:a*(s+j),range(r),F(1))
        require((5*q-8)*rise(5)/11520==(5*s-11)*rise(5)/23040,'eta(s+4) coefficient')
        require(-(60*q+90)*rise(3)/2880==-rise(3)*(s+4)/96,'eta(s+2) coefficient')
        require(180*q*4*s/2880==s*(s+1)/8,'eta(s) coefficient')
        counts['mellin_correction_panels']+=3
    for m in range(1,41):
        a=F(m*(2*m+3),2)
        require(1-8*a-16*a*a<0 and 2*a-F(1,2)>=F(9,2),'correcting denominator strip')
    return {'id':'GPP26','status':'PROPOSED_COMPONENTS_NOT_RH_PROOF',
            'arithmetic':'Python integers and fractions; bounded exact algebra only',
            'counts':counts,'bulk_examples':bulk,
            'analytic_limits_machine_proved':False,'native_zero_certificates':0,
            'native_zero_scouts_certified':False,'remote_publication_by_this_session':False}


def canonical(obj): return json.dumps(obj,sort_keys=True,separators=(',',':'),ensure_ascii=True)
def strict_json(path):
    def pairs(items):
        d={}
        for k,v in items:
            if k in d: raise ValueError('duplicate JSON key: '+k)
            d[k]=v
        return d
    return json.loads(Path(path).read_text(encoding='utf-8'),object_pairs_hook=pairs,
                      parse_float=lambda s: (_ for _ in ()).throw(ValueError('JSON floats not allowed')))


def authenticate():
    manifest=strict_json(ROOT/'MANIFEST.json')
    require(set(manifest)=={'algorithm','files'} and manifest['algorithm']=='sha256','manifest contract')
    expected=manifest['files']
    actual={p.name for p in ROOT.iterdir() if p.is_file()}
    require(actual==set(expected)|{'MANIFEST.json'},'packet inventory')
    for name,digest in expected.items():
        path=ROOT/name
        require(not path.is_symlink(),'symlink payload')
        require(hashlib.sha256(path.read_bytes()).hexdigest()==digest,'payload hash: '+name)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    group=ap.add_mutually_exclusive_group(required=True)
    group.add_argument('--emit',type=Path);group.add_argument('--check',type=Path)
    args=ap.parse_args()
    if args.check:authenticate()
    result=compute()
    if args.emit:
        args.emit.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
        print('PRODUCED_BOUNDED_RECEIPT')
    else:
        require(canonical(strict_json(args.check))==canonical(result),'reconstructed receipt differs')
        print('PASS_BOUNDED_EXACT_GPP26',hashlib.sha256(canonical(result).encode()).hexdigest())
        print(json.dumps(result['counts'],sort_keys=True))


if __name__=='__main__':
    try: main()
    except (ArithmeticError,ValueError,OSError,KeyError,TypeError) as exc:
        print('REFUSED:',exc,file=sys.stderr);sys.exit(1)
