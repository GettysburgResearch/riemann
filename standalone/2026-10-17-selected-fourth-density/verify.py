#!/usr/bin/env python3
"""Exact bookkeeping and finite algebra, NOT verification of analytic inputs."""
from __future__ import annotations
from fractions import Fraction as Q
from pathlib import Path
import json
import itertools
import sys

HERE = Path(__file__).resolve().parent
E = Q(1, 10**7)
A, H, THETA, Z0, DELTA = Q(9,20), Q(11,20), Q(9,40), Q(2,5), Q(1,200)
MOMENT4 = Q(7,6)
ELIMINATION = Q(4,3)
CLAIM_B = Q(41,60)
PREDICATES = 0

def need(ok: bool, msg: str) -> None:
    global PREDICATES
    PREDICATES += 1
    if not ok:
        raise ValueError(msg)

def p(x=0, y=0, z=0): return (Q(x), Q(y), Q(z))
def add(x,y): return tuple(a+b for a,b in zip(x,y))
def neg(x): return tuple(-a for a in x)
def sub(x,y): return add(x,neg(y))
def scale(x,c): return tuple(Q(c)*a for a in x)
def mul(x,y):
    need(x[2]*y[1]+x[1]*y[2]==0 and x[2]*y[2]==0, 'polynomial degree overflow')
    return (x[0]*y[0],x[0]*y[1]+x[1]*y[0],x[0]*y[2]+x[1]*y[1]+x[2]*y[0])
def value(x,t): return x[0]+x[1]*t+x[2]*t*t

def bernstein(x, strict=False):
    b=(x[0], x[0]+x[1]*E/2, value(x,E))
    need(all(t>=0 for t in b),'negative whole-interval Bernstein coefficient')
    if strict:
        need(any(t>0 for t in b) and b[2]>0,'not strictly positive on 0<e<=E')
    return [str(t) for t in b]

def domain(x,y,z):
    forms=[x,y,z,sub(add(scale(z,6),y),p(1)),sub(add(x,scale(z,6)),p(1)),
           sub(add(x,y),p(1)),sub(add(add(x,y),scale(z,6)),p(2)),
           sub(add(scale(x,6),scale(z,6)),p(5)),sub(x,p(Q(1,2))),
           sub(scale(x,3),p(2)),sub(add(scale(x,3),y),p(Q(5,2)))]
    for f in forms: bernstein(f,True)

def norm_exponents(s,a,b,fourth):
    r=[]
    for c,d in [(Q(1),Q(0)),(Q(0),Q(1)),(Q(1,3),Q(5,6)),(Q(5,6),Q(1,3))]:
        if fourth:
            r.append(ELIMINATION*((Q(1,2)-s)*b+MOMENT4/4+(c*a+d)/2))
        else:
            r.append((Q(1,2)-s)*b+Q(1,2)+(c*a+d)/2)
    r += [(2-2*s)*b,1+(1-2*s)*a]
    r += [Q(1,3)+(Q(11,6)-2*s)*v for v in (a,b)]
    r += [Q(5,6)+(Q(4,3)-2*s)*v for v in (a,b)]
    return r

def density4(s):
    d=36*s*s-75*s+31
    return (-(48*s-29)/(2*d), -(33*s-19)/d, (468*s*s-741*s+271)/(6*d))

def cost(x,y,z):
    return add(add(p(A/2-1),x),add(scale(z,H),scale(sub(y,p(1)),A)))

def arithmetic_checks():
    # Exact Q(omega), omega^2+omega+1=0; named two-prime semigroup only.
    def times(x,y):
        a,b=x;c,d=y
        return (a*c-b*d,a*d+b*c-b*d)
    def power(x,n):
        out=(1,0)
        for _ in range(n): out=times(out,x)
        return out
    roots=[(1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1)]
    atoms=[(0,0)]+roots
    for z in roots: need(power(z,6)==(1,0),'sixth root')
    monomials=0
    for r1,r2 in itertools.product(atoms,repeat=2):
        for e1,e2 in itertools.product(range(14),repeat=2):
            c=(e1%6,e2%6);d=(e1//6,e2//6)
            orig=times(power(r1,e1),power(r2,e2))
            mask=all(v==0 or r!=(0,0) for v,r in zip(d,(r1,r2)))
            rhs=times(power(r1,c[0]),power(r2,c[1])) if mask else (0,0)
            need(orig==rhs,'full sixth-power column and nonunit mask')
            monomials+=1
    # Shared support must remain: p^7 has c=p,d=p, not a coprime pair.
    need(7%6==1 and 7//6==1,'shared prime split')
    need(power(roots[1],7)==roots[1],'shared prime character retained')
    need(power((0,0),6)==(0,0),'neutral nonunit zero retained')
    # Exact Holder finite tests: (sum u*v)^4 <= R sum u^4 (sum v^2)^2.
    holder=0
    for n in range(1,7):
        for j in range(25):
            u=[(j+3*i*i)%7 for i in range(n)]
            v=[(2*j+i*i+i)%9 for i in range(n)]
            need(sum(x*y for x,y in zip(u,v))**4 <= n*sum(x**4 for x in u)*sum(y*y for y in v)**2,'Holder 4,2,4')
            holder+=1
    elim=0
    for t,a,b in itertools.product(range(8),range(10),range(10)):
        r=t**4
        if r<=a*t+b:
            need(r<=2*b or r**3<=16*a**4,'self-selected elimination')
            elim+=1
    return {'abstract_prime_profiles':49,'monomials':monomials,'holder_arrays':holder,'elimination_cases':elim}

def run():
    need(MOMENT4==Q(7,6),'unpaid fourth-moment exponent')
    need(ELIMINATION==Q(4,3),'wrong self-selected Holder elimination')
    need(A*2<Q(1),'not a short-support application')
    need(CLAIM_B==1-A/2-H/6,'wrong principal Mellin normalization')
    need(CLAIM_B+THETA==Q(109,120),'wrong final boundary')
    need(Q(91,100)-Q(109,120)==Q(1,600),'comparison')
    # Moment source is the four terms of DF at U=V, not an assumed diagonal sieve.
    need(max(Q(1),Q(1),Q(5,6)+Q(1,3),Q(1,3)+Q(5,6))==MOMENT4,'fourth moment scale')
    ds=Q(3,4); da=Q(7,10); db=Q(23,20)
    dterms=norm_exponents(ds,da,db,True)
    need(max(dterms)==Q(43,60),'three-quarter density')
    need(Q(8,11)-Q(43,60)==Q(7,660),'density improvement')
    need((Q(1,2)-ds)*db+MOMENT4/4+Q(16,15)/2==Q(43,80),'pre-elimination exponent')
    data=json.loads((HERE/'strata.json').read_text())
    need(len(data)==17,'missing row class')
    previous=None; rows=[]
    for j,r in enumerate(data):
        s,nu=Q(r['s']),Q(r['nu'])
        need(Q(1,2)<s<=1 and 0<=nu<=1,'stratum range')
        need(previous is None or previous<s,'threshold order')
        if j:
            need(Q(r['previous'])==previous,'wrong lower-count upper-contour linkage')
            a,b=Q(r['da']),Q(r['db'])
            need(0<=a<=b,'detector length order')
            four=r['density']=='fourth'
            terms=norm_exponents(previous,a,b,four)
            need(max(terms)<=nu,'unproved exceptional-count exponent')
            if four: need((a,b,nu)==density4(previous),'fourth density parameter identity')
        else:
            need(nu==1 and r['mode']=='second','missing full good class')
            terms=[]
        count=p(nu,0 if j==0 else 1)
        x=p(s,1)
        y=p(Q(1,2)) if r['mode']!='convex' else p(1-s,1)
        z=p(Z0)
        domain(p(1,1),p(1,1),z)
        domain(x,p(1,1),z)
        domain(x,y,z)
        if r['mode']=='second': v=sub(scale(add(count,p(1)),Q(1,2)),z)
        elif r['mode']=='fourth': v=sub(add(scale(count,Q(3,4)),p(MOMENT4/4)),z)
        elif r['mode']=='convex': v=sub(add(count,scale(sub(p(1),y),Q(1,2))),z)
        else: raise ValueError('unknown method')
        bernstein(v,True)
        growth=add(cost(x,y,z),mul(p(H,1),v))
        cert=bernstein(sub(p(THETA,2),growth))
        if j and j<16: need(THETA-growth[0]>Q(1,10000),'lost middle-class fixed margin')
        rows.append({'j':j,'growth':[str(vv) for vv in growth],'density_terms':[str(t) for t in terms],'margin_bernstein':cert})
        if j<16:
            radii=[p(1,-Q(1,4)),p(2-s,-1),p(2-s,-Q(1,2)),p(2-s,-Q(1,4))]
            for lo,hi in zip(radii,radii[1:]): bernstein(sub(hi,lo),True)
        previous=s
    # Nested exceptional sets: exactly one class for every possible highest threshold crossed.
    for rank in range(-1,16):
        memberships=[rank>=j for j in range(16)]
        classes=[not memberships[0]]+[memberships[j-1] and not memberships[j] for j in range(1,16)]+[memberships[15]]
        need(sum(classes)==1 and classes[rank+1],'disjoint exhaustive zero strata')
    corners=[(p(1,1),p(1,1),p(Q(1,6),1)),(p(1,1),p(Q(1,2)),p(Q(1,6),1)),(p(1,1),p(1),p(0,1))]
    for corner in corners: domain(*corner)
    pw=cost(*corners[1]); pz=cost(*corners[2])
    need(pw==p(Q(11,120),Q(31,20)) and pz==p(THETA,Q(31,20)),'principal remainder')
    small=add(cost(p(1,1),p(Q(1,2)),p(Z0)),p(DELTA*(1-Z0)))
    need(small==p(Q(223,1000),1),'incorrect small-frequency threshold')
    for q in (pw,pz,small): bernstein(sub(p(THETA,2),q))
    # Exact large-range identity after substituting L=10/e+2: e(h-L cancellation) retained.
    large=p(A/2+3+3*A+H-10,-1)
    need(large==p(-Q(39,8),-1),'large-frequency initial-line norm')
    finite=arithmetic_checks()
    return {'status':'PASS; finite algebra only, no analytic certification','predicates_including_guards':PREDICATES,'three_quarters':{'terms':[str(t) for t in dterms],'g':'43/60','old_g':'8/11','gain':'7/660'},'e_max':str(E),'strata':rows,'principal_w':[str(t) for t in pw],'principal_z':[str(t) for t in pz],'small':[str(t) for t in small],'large':[str(t) for t in large],'boundary':'109/120','finite_scope':finite}

if __name__=='__main__':
    try: print(json.dumps(run(),indent=2,sort_keys=True))
    except (ValueError,KeyError,TypeError,ZeroDivisionError,json.JSONDecodeError) as exc:
        print(f'FAIL: {exc}',file=sys.stderr);sys.exit(1)
