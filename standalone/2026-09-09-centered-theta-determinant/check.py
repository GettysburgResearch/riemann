#!/usr/bin/env python3
"""Bounded exact controls for the centered-theta determinant paper.
No theta value, infinite determinant, operator domain, or RH claim is computed.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
FILES = {'PROOF.md', 'README.md', 'REVIEW.md', 'SOURCES.json',
         'VALIDATION.md', 'check.py', 'result.json', 'SHA256SUMS'}
PARENT = '2787339f8f1feb619f1679afb96cb9995e440958'


def require(ok, message):
    if not ok:
        raise ValueError(message)


def matrix(n, m=None):
    return [[F(0) for _ in range(n if m is None else m)] for _ in range(n)]


def eye(n):
    a = matrix(n)
    for i in range(n):
        a[i][i] = F(1)
    return a


def mul(a, b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def tr(a):
    return sum((a[i][i] for i in range(len(a))), F(0))


def det(a):
    a = [row[:] for row in a]
    answer = F(1)
    for i in range(len(a)):
        p = next((j for j in range(i, len(a)) if a[j][i]), None)
        if p is None:
            return F(0)
        if p != i:
            a[i], a[p] = a[p], a[i]
            answer = -answer
        pivot = a[i][i]
        answer *= pivot
        for j in range(i+1, len(a)):
            q = a[j][i]/pivot
            for k in range(i+1, len(a)):
                a[j][k] -= q*a[i][k]
    return answer


def verify_math():
    groups = {}
    # Formal finite Volterra analogues: J is strictly lower triangular.
    count = 0
    for n in range(1, 8):
        j = matrix(n)
        for k in range(n-1):
            j[k+1][k] = F(k+2, k+3)
        e = [[F(k+1, n+1)] for k in range(n)]
        ell = [[F((-1)**k*(k+2), n+2) for k in range(n)]]
        outer = mul(e, ell)
        k = [[j[a][b]-outer[a][b] for b in range(n)] for a in range(n)]
        for u in [F(-2), F(0), F(1, 3), F(2)]:
            r, power = [row[:] for row in e], [row[:] for row in e]
            for v in range(1, n):
                power = mul(j, power)
                for a in range(n):
                    r[a][0] += u**v*power[a][0]
            q = eye(n)
            for a in range(n):
                for b in range(n):
                    q[a][b] -= u*k[a][b]
            require(det(q) == 1+u*mul(ell, r)[0][0], 'Volterra determinant sign')
            require(tr(k) == -mul(ell, e)[0][0], 'centering exponential')
            # The exponent remaining in the det_2 product is -u ell(e).
            require(-u*mul(ell,r)[0][0]+u*u*mul(ell,mul(j,r))[0][0]
                    == -u*mul(ell,e)[0][0], 'det_2 multiplication correction')
            count += 1
    groups['finite_volterra_rank_one_cases'] = count

    # Parity blocks: ordinary determinant, without squaring the answer.
    count = 0
    for ne, no in [(1,1),(2,1),(2,2),(3,2),(3,3)]:
        a = [[F(i+2*j+1, 5) for j in range(no)] for i in range(ne)]
        b = [[F((-1)**(i+j)*(2*i+j+1), 7) for j in range(ne)] for i in range(no)]
        ba = mul(b,a)
        ab = mul(a,b)
        for u in [F(-1),F(1,2),F(3,2)]:
            big = eye(ne+no)
            for i in range(ne):
                for j in range(no):
                    big[i][ne+j] = -u*a[i][j]
                    big[ne+j][i] = -u*b[j][i]
            small = eye(no)
            for i in range(no):
                for j in range(no):
                    small[i][j] -= u*u*ba[i][j]
            require(det(big) == det(small), 'parity determinant')
            require(tr(ab)==tr(ba), 'parity trace')
            count += 1
    groups['parity_block_cases'] = count

    # Actual integrals for THREE explicitly declared compact polynomial laws.
    # These are controls of the general identity, not theta computations.
    count = 0
    for c in [F(0),F(1),F(2)]:
        z = 2+2*c/3
        def moment(n):
            return F(0) if n%2 else (F(2,n+1)+c*F(2,n+3))/z
        def integrate_poly(p):
            return sum((v*moment(i) for i,v in enumerate(p)),F(0))
        def anti(p):
            out=[F(0)]+[p[i]/(i+1) for i in range(len(p))]
            out[0] = -integrate_poly(out)
            return out
        for n in range(9):
            p=[F(0)]*n+[F(1)]
            kp=anti(p)
            require(integrate_poly(kp)==0,'weighted centering')
            require([(i+1)*kp[i+1] for i in range(len(p))]==p,'derivative inverse')
            # Coefficient of u^n in (exp(ut)-M(u))/u.
            require(kp[0]==-moment(n+1)/(n+1),'moment generating normalization')
            count += 1
    groups['compact_law_polynomial_cases'] = count

    # Independent full integrals for piecewise-constant positive densities.
    # I=integral FQ/w; J=integral_(s<t) F(s)Q(t). Exact polynomial cells.
    count = 0
    for masses in [[F(1)], [F(1,3),F(2,3)],
                   [F(1,4),F(1,2),F(1,4)], [F(1,8),F(3,8),F(1,2)]]:
        require(sum(masses)==1,'probability normalization')
        fleft=F(0); int_f=F(0); cross=F(0); hs=F(0)
        mu=F(0); second=F(0)
        for i,m in enumerate(masses):
            # On [i,i+1], F(i+s)=fleft+m*s and integral_-infty^(i+s)F
            # equals int_f+fleft*s+m*s^2/2.
            qleft=1-fleft
            cross += int_f*qleft + (fleft*qleft-int_f*m)/2 \
                + (m*qleft/2-fleft*m)/3 - m*m/8
            hs += (fleft*qleft + m*(qleft-fleft)/2 - m*m/3)/m
            int_f += fleft+m/2
            fleft += m
            mu += m*F(2*i+1,2)
            second += m*F(3*i*i+3*i+1,3)
        var=second-mu*mu
        require(2*cross==var,'complete trace K^2 normalization')
        require(hs>=var,'Hilbert Schmidt versus bilinear trace')
        require(hs>0 and var>0,'nondegenerate compact law')
        count += 1
    groups['complete_piecewise_law_trace_cases'] = count

    # Exact finite adjoint-chain controls; not an infinite-theta numerical proof.
    count = 0
    for n in range(2,10):
        a=matrix(n)
        for i in range(n-1):
            a[i][i+1]=F(-1)
        q=[[F(int(i==0))] for i in range(n)]
        require(all(x[0]==0 for x in mul(a,q)), 'adjoint root')
        for j in range(1,n):
            q=[[F(int(i==j))] for i in range(n)]
            aq=mul(a,q)
            require(aq[j-1][0]==-1 and sum(x[0]*x[0] for x in aq)==1,
                    'adjoint chain sign')
            count+=1
    groups['finite_adjoint_chain_relations'] = count
    return {'schema':1,'rh_proved':False,'infinite_proofs_machine_verified':False,
            'actual_theta_spectrum_computed':False,'groups':groups,
            'total_bounded_cases':sum(groups.values())}


def unique_pairs(pairs):
    out={}
    for k,v in pairs:
        require(k not in out,'duplicate JSON key')
        out[k]=v
    return out


def load(path):
    return json.loads(path.read_text(),object_pairs_hook=unique_pairs,
                      parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))


def typed_equal(a,b):
    if type(a) is not type(b):
        return False
    if isinstance(a,dict):
        return a.keys()==b.keys() and all(typed_equal(a[k],b[k]) for k in a)
    if isinstance(a,list):
        return len(a)==len(b) and all(typed_equal(x,y) for x,y in zip(a,b))
    return a==b


def authenticate():
    require({p.name for p in ROOT.iterdir()}==FILES,'file inventory')
    for p in ROOT.iterdir():
        require(p.is_file() and not p.is_symlink(),'regular files required')
    lines=(ROOT/'SHA256SUMS').read_text().splitlines()
    names=[]
    for line in lines:
        digest,name=line.split('  ')
        require('/' not in name and name in FILES and name!='SHA256SUMS','manifest path')
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,'hash '+name)
        names.append(name)
    require(len(names)==7 and len(set(names))==7 and set(names)==FILES-{'SHA256SUMS'},'manifest coverage')
    require(load(ROOT/'SOURCES.json')['parent_commit']==PARENT,'source parent')


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--emit',action='store_true',help='producer mode; no manifest authentication')
    ap.add_argument('--check',type=Path)
    args=ap.parse_args()
    require(args.emit != (args.check is not None),'choose --emit or --check')
    result=verify_math()
    if args.check is not None:
        authenticate()
        require(typed_equal(load(args.check),result),'result mismatch')
    print(json.dumps(result,sort_keys=True,indent=2))


if __name__=='__main__':
    try:
        main()
    except (ValueError,KeyError,TypeError,OSError,json.JSONDecodeError) as e:
        print('REJECT: '+str(e),file=sys.stderr)
        sys.exit(1)
