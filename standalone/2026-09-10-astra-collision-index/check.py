#!/usr/bin/env python3
"""Exact polynomial-heat boundary certificates. NO actual theta evaluation or RH proof."""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import hashlib
import json
from math import comb, factorial
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
VERSION = 'HCI26-1'


def need(p, message):
    if not p:
        raise ValueError(message)


def pairs(items):
    out = {}
    for k, v in items:
        need(k not in out, 'duplicate JSON key')
        out[k] = v
    return out


def no_float(x):
    raise ValueError('floating/nonfinite JSON number forbidden')


def load(data):
    need(len(data) < 2_000_000, 'receipt too large')
    return json.loads(data, object_pairs_hook=pairs, parse_float=no_float,
                      parse_constant=no_float)


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode()


def typed_equal(a, b):
    if type(a) is not type(b):
        return False
    if isinstance(a, dict):
        return a.keys() == b.keys() and all(typed_equal(a[k], b[k]) for k in a)
    if isinstance(a, list):
        return len(a) == len(b) and all(typed_equal(x, y) for x, y in zip(a, b))
    return a == b


def encode(q):
    q = Q(q)
    return [q.numerator, q.denominator]


def decode(q):
    need(type(q) is list and len(q) == 2 and all(type(a) is int for a in q), 'rational type')
    need(q[1] > 0, 'rational denominator')
    a = Q(q[0], q[1])
    need(encode(a) == q, 'noncanonical rational')
    return a


def clean(p):
    return {k: Q(v) for k, v in p.items() if v}


def p_add(a, b):
    c = dict(a)
    for k, v in b.items():
        c[k] = c.get(k, Q(0)) + v
    return clean(c)


def p_scale(p, c):
    return clean({k: c*v for k, v in p.items()})


def partial(p, dim):
    ans = {}
    for key, val in p.items():
        if key[dim]:
            k = list(key)
            k[dim] -= 1
            ans[tuple(k)] = val * key[dim]
    return clean(ans)


def heat(m):
    need(type(m) is int and m >= 0, 'invalid heat degree')
    return {(j, m-2*j): Q((-1)**j*factorial(m), factorial(j)*factorial(m-2*j))
            for j in range(m//2+1)}


def shift(p, a, b):
    ans = {}
    for (i, j), c in p.items():
        for k in range(i+1):
            for l in range(j+1):
                key = (k, l)
                ans[key] = ans.get(key, Q(0)) + c*comb(i,k)*comb(j,l)*(-a)**(i-k)*(-b)**(j-l)
    return clean(ans)


def is_backward_heat(p):
    return not p_add(partial(p,0), partial(partial(p,1),1))


def u_clean(p):
    p = list(p)
    while len(p)>1 and p[-1] == 0:
        p.pop()
    return p or [Q(0)]


def u_add(a,b):
    n=max(len(a),len(b))
    return u_clean([(a[k] if k<len(a) else 0)+(b[k] if k<len(b) else 0) for k in range(n)])


def u_mul(a,b,limit=None):
    n=len(a)+len(b)-1
    if limit is not None:
        n=min(n,limit+1)
    c=[Q(0)]*n
    for i,x in enumerate(a):
        for j,y in enumerate(b[:max(0,n-i)]):
            c[i+j]+=x*y
    return u_clean(c)


def u_diff(p):
    return u_clean([k*p[k] for k in range(1,len(p))])


def u_eval(p, x):
    v=Q(0)
    for c in reversed(p):
        v=v*x+c
    return v


def u_affine(p,a,b):
    out=[Q(0)]*len(p)
    for n,c in enumerate(p):
        for k in range(n+1):
            out[k]+=c*comb(n,k)*a**(n-k)*b**k
    return u_clean(out)


def on_edge(p, start, end):
    t0,x0=start
    dt,dx=end[0]-t0,end[1]-x0
    ans=[Q(0)]
    for (i,j),c in p.items():
        a=[Q(comb(i,k))*t0**(i-k)*dt**k for k in range(i+1)]
        b=[Q(comb(j,k))*x0**(j-k)*dx**k for k in range(j+1)]
        ans=u_add(ans,[c*v for v in u_mul(a,b)])
    return ans


def vertices(rect):
    a,b,c,d=map(Q,rect)
    need(a<b and c<d,'invalid rectangle')
    return [(a,c),(b,c),(b,d),(a,d)]


def curves(p,rect):
    vv=vertices(rect)
    px=partial(p,1)
    return [(on_edge(p,vv[k],vv[(k+1)%4]),on_edge(px,vv[k],vv[(k+1)%4])) for k in range(4)]


def dot(a,b):
    return a[0]*b[0]+a[1]*b[1]


def dist2(a,b):
    d=(b[0]-a[0],b[1]-a[1])
    dd=dot(d,d)
    if not dd:
        return dot(a,a)
    lam=max(Q(0),min(Q(1),-dot(a,d)/dd))
    c=(a[0]+lam*d[0],a[1]+lam*d[1])
    return dot(c,c)


def segment(curve,l,r):
    need(Q(0)<=l<r<=Q(1),'segment interval')
    local=[u_affine(p,l,r-l) for p in curve]
    a=tuple(p[0] for p in local)
    b=tuple(u_eval(p,Q(1)) for p in local)
    curvature=sum(abs(v) for p in local for v in u_diff(u_diff(p)))
    error=curvature/8
    return a,b,error,dist2(a,b)


def adaptive(curve,l=Q(0),r=Q(1),depth=0):
    a,b,e,d=segment(curve,l,r)
    need(a!=(0,0) and b!=(0,0),'boundary jet is zero')
    if d>e*e:
        return [(l,r)]
    need(depth<24,'inconclusive: boundary tube depth limit')
    m=(l+r)/2
    return adaptive(curve,l,m,depth+1)+adaptive(curve,m,r,depth+1)


def poly_winding(points):
    need(len(points)>=3,'insufficient polygon')
    out=0
    for a,b in zip(points,points[1:]+points[:1]):
        need(dist2(a,b)>0,'polygon passes through origin')
        cross=a[0]*b[1]-a[1]*b[0]
        if a[1]<=0<b[1] and cross>0:
            out+=1
        if b[1]<=0<a[1] and cross<0:
            out-=1
    return out


def produce_cover(p,rect):
    return [[{'lo':encode(l),'hi':encode(r)} for l,r in adaptive(c)] for c in curves(p,rect)]


def verify_cover(p,rect,cover):
    need(type(cover) is list and len(cover)==4,'four complete sides required')
    pts=[]
    witness=[]
    minimum=None
    cs=curves(p,rect)
    for side in range(4):
        cells=cover[side]
        need(type(cells) is list and bool(cells),'empty side')
        last=Q(0)
        for cell in cells:
            need(type(cell) is dict and set(cell)=={'lo','hi'},'cell schema')
            l,r=decode(cell['lo']),decode(cell['hi'])
            need(l==last and l<r<=1,'gap, overlap or reversed coverage')
            a,b,e,d=segment(cs[side],l,r)
            need(d>e*e,'unpaid continuum interpolation error')
            margin=d-e*e
            minimum=margin if minimum is None else min(minimum,margin)
            pts.append(a)
            witness.append([side,encode(l),encode(r),[encode(v) for v in a],
                            [encode(v) for v in b],encode(e),encode(d)])
            last=r
        need(last==1,'incomplete terminal side')
    # Each endpoint is fixed by the same corner values; all four sides are paid.
    return {'degree':poly_winding(pts),'segments':len(pts),
            'minimum_squared_margin':encode(minimum),
            'complete_witness_sha256':hashlib.sha256(canonical(witness)).hexdigest()}


def models():
    rows=[]
    for m in range(2,13):
        rows.append((f'Hermite-{m}',heat(m),(-1,1,-m-1,m+1),-(m//2),True))
    for m in (2,3,4,7):
        a,b=Q(1,3),Q(2)
        rows.append((f'translated-{m}',shift(heat(m),a,b),
                     (a-Q(1,4),a+Q(1,4),b-m,b+m),-(m//2),True))
    rows.append(('two-time-collisions',p_add(shift(heat(4),Q(3),Q(0)),{(0,0):Q(-12)}),
                 (1,5,-8,8),-2,True))
    pair=p_add(p_add(heat(4),p_scale(heat(2),Q(-2))),{(0,0):Q(1)})
    pair=shift(pair,Q(1,3),Q(0))
    rows.append(('even-off-axis-pair',pair,(Q(1,12),Q(7,12),-3,3),-2,True))
    rows.append(('positive-half-pair',pair,(Q(1,12),Q(7,12),Q(1,10),3),-1,True))
    rows.append(('negative-half-pair',pair,(Q(1,12),Q(7,12),-3,Q(-1,10)),-1,True))
    rows.append(('zero-time-double-excluded',heat(2),(Q(1,16),1,-3,3),0,True))
    rows.append(('simple-root-crosses-boundary',{(0,1):Q(1)},(-1,1,-1,1),0,True))
    rows.append(('forward-heat-sign-control',{(0,2):Q(1),(1,0):Q(2)},(-1,1,-3,3),1,False))
    return rows


def theta_step(p):
    # Exponents are (u,q,t); multiplication by 1+2tu-4q.
    ans=p_add(partial(p,0),{})
    for (a,b,c),v in p.items():
        for key,coef in [((a,b,c),1+4*b),((a+1,b,c+1),2),((a,b+1,c),-4)]:
            ans[key]=ans.get(key,Q(0))+coef*v
    return clean(ans)


def multi_eval(p,u,q,t):
    return sum(v*u**a*q**b*t**c for (a,b,c),v in p.items())


def series_exp(a,n):
    need(a[0]==0,'formal exponential must have zero constant')
    b=[Q(1)]
    for j in range(1,n+1):
        b.append(sum(k*(a[k] if k<len(a) else 0)*b[j-k] for k in range(1,j+1))/j)
    return b


def theta_checks():
    polynomials=[{(0,2,0):Q(2),(0,1,0):Q(-3)}]
    for k in range(6):
        polynomials.append(theta_step(polynomials[-1]))
    fixed=clean({(a,b):v for (a,b,c),v in polynomials[1].items() if c==0})
    need(fixed=={(0,3):Q(-8),(0,2):Q(30),(0,1):Q(-15)},'first theta derivative')
    count=1
    for u in (Q(0),Q(1,3)):
        for q in (Q(3),Q(7),Q(13)):
            for t in (Q(0),Q(1,2)):
                qe=[q*Q(4**j,factorial(j)) for j in range(7)]
                p0=u_add([2*v for v in u_mul(qe,qe,6)],[-3*v for v in qe])
                a=[Q(0)]+[-qe[j] for j in range(1,7)]
                a[1]+=1+2*t*u
                a[2]+=t
                expanded=u_mul(series_exp(a,6),p0,6)
                for k in range(7):
                    need(multi_eval(polynomials[k],u,q,t)==factorial(k)*expanded[k],
                         'independent formal theta jet mismatch')
                    count+=1
    return {'formal_jet_checks':count,'max_derivative_order':6,
            'actual_theta_values_evaluated':False}


def reconstruct():
    rows=[]
    for name,p,rect,w,backward in models():
        need(is_backward_heat(p)==backward,'heat PDE status mismatch')
        cover=produce_cover(p,rect)
        result=verify_cover(p,rect,cover)
        need(result['degree']==w,'wrong collision degree')
        rows.append({'model':name,'backward_heat':backward,'rectangle':[encode(Q(v)) for v in rect],**result})
    need(rows[16]['degree']==rows[17]['degree']+rows[18]['degree'],'half-box additivity')
    # Elementary exact timing of the positive Gaussian-mixture collision.
    t=Q(1,5); d=1-4*t
    need(d==Q(1,5) and t/d==1 and 1/d**2==25,'mixture collision parameters')
    recurrence=0
    for m in range(1,17):
        need(partial(heat(m),1)==p_scale(heat(m-1),Q(m)),'Hermite derivative')
        need(is_backward_heat(heat(m)),'Hermite backward PDE')
        recurrence+=2
    return {'schema':VERSION,'status':'PROPOSED_COMPONENT_RESEARCH','rh_proved':False,
            'actual_theta_boundary_certified':False,'new_newman_upper_bound':False,
            'models':rows,'total_certified_segments':sum(r['segments'] for r in rows),
            'hermite_identities':recurrence,'theta_recurrence':theta_checks(),
            'gaussian_mixture_t':[1,5],'multiplicity_theorem_machine_proved':False}


def authenticate():
    manifest=ROOT/'SHA256SUMS'
    need(manifest.is_file() and not manifest.is_symlink(),'missing manifest')
    expected={}
    for line in manifest.read_text().splitlines():
        digest,name=line.split('  ',1)
        need(len(digest)==64 and name not in expected,'invalid/duplicate manifest')
        need('/' not in name and '\\' not in name and name not in {'.','..','SHA256SUMS'},'unsafe manifest')
        expected[name]=digest
    need(bool(expected),'empty manifest')
    names=set()
    for f in ROOT.iterdir():
        need(f.is_file() and not f.is_symlink(),'nonregular/extra package member')
        names.add(f.name)
    need(names==set(expected)|{'SHA256SUMS'},'package inventory mismatch')
    for name,digest in expected.items():
        need(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,'package bytes changed: '+name)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    g=p.add_mutually_exclusive_group(required=True)
    g.add_argument('--write',type=Path,help='unauthenticated producer mode')
    g.add_argument('--check',type=Path,help='authenticate package and fully reconstruct receipt')
    args=p.parse_args()
    if args.check:
        authenticate()
        need(not args.check.is_symlink(),'receipt symlink')
        expected=load(args.check.read_bytes())
        actual=reconstruct()
        need(typed_equal(expected,actual),'receipt does not match full reconstruction')
        print(json.dumps({'marker':'PASS_EXACT_HEAT_MODEL_BOUNDARIES',
                          'models':len(actual['models']),
                          'segments':actual['total_certified_segments'],
                          'receipt_sha256':hashlib.sha256(canonical(actual)).hexdigest(),
                          'actual_theta_boundary_certified':False,'rh_proved':False},sort_keys=True))
    else:
        actual=reconstruct()
        args.write.write_text(json.dumps(actual,sort_keys=True,indent=2)+'\n')
        print('PRODUCER_ONLY '+hashlib.sha256(canonical(actual)).hexdigest())

if __name__=='__main__':
    try:
        main()
    except (ValueError,OSError,KeyError,TypeError) as exc:
        print('FAIL: '+str(exc),file=sys.stderr)
        sys.exit(1)
