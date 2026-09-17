#!/usr/bin/env python3
"""SPL26 bounded exact reconstruction; does NOT replay P7 or analytic zeta inputs."""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import hashlib
from itertools import product
import json
from math import factorial, isqrt
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
ALPHA = Q(19, 5000)
BETA = Q(1, 500)
SEPARATION = Q(2, 3)


def require(condition: bool, text: str) -> None:
    if not condition:
        raise ValueError(text)


def frac(x: Q | int) -> str:
    x = Q(x)
    return f"{x.numerator}/{x.denominator}"


def mul(a: list[Q], b: list[Q]) -> list[Q]:
    c = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


def at(a: list[Q], x: Q) -> Q:
    v = Q(0)
    for z in reversed(a):
        v = v*x+z
    return v


def alternating(terms: list[Q]) -> tuple[Q, Q]:
    require(len(terms) >= 2, "too few alternating terms")
    for a,b in zip(terms, terms[1:]):
        require(abs(b) < abs(a) and a*b < 0, "alternation invalid")
    s = sum(terms[:-1], Q(0))
    return min(s, s+terms[-1]), max(s, s+terms[-1])


def arctan_bounds(n: int, length: int = 90) -> tuple[Q,Q]:
    return alternating([Q((-1)**j, (2*j+1)*n**(2*j+1))
                        for j in range(length)])


def trig_constant_bounds(length: int = 50) -> tuple[tuple[Q,Q], tuple[Q,Q]]:
    c = alternating([Q((-1)**j, 2**j*factorial(2*j))
                     for j in range(length)])
    sinc = alternating([Q((-1)**j, 2**j*factorial(2*j+1))
                        for j in range(length)])
    require(sinc[0] > 0, "sinc lower bound")
    h = (Q(3,2)-c[1]/sinc[0], Q(3,2)-c[0]/sinc[1])
    return h, sinc


def sqrt_bounds(x: Q, bits: int = 240) -> tuple[Q,Q]:
    scale=1 << bits
    n=isqrt((x.numerator*scale*scale)//x.denominator)
    lo,hi=Q(n,scale),Q(n+1,scale)
    require(lo*lo<=x<=hi*hi, "sqrt enclosure")
    return lo,hi


def decimal_out(x: Q, places: int, upper: bool = False) -> str:
    n,d=x.numerator*10**places,x.denominator
    k=-((-n)//d) if upper else n//d
    sign='-' if k<0 else ''
    k=abs(k)
    return sign+str(k//10**places)+'.'+str(k%10**places).zfill(places)


def interval_text(x: tuple[Q,Q], places: int = 32) -> list[str]:
    return [decimal_out(x[0], places), decimal_out(x[1], places, True)]


def greedy(points: list[Q]) -> tuple[list[int], list[tuple[int,int]]]:
    require(points == sorted(points), "unsorted input")
    remain=[]; pairs=[]; i=0
    while i<len(points):
        if i+1<len(points) and points[i+1]-points[i]<SEPARATION:
            pairs.append((i,i+1)); i+=2
        else:
            remain.append(i); i+=1
    return remain,pairs


def psi(t: Q) -> Q:
    require(t>=0,"negative PSD eigenvalue")
    return (t-1)**2 if t<=2 else 2*t-3


def eye(n: int) -> list[list[Q]]:
    return [[Q(i==j) for j in range(n)] for i in range(n)]


def transpose(A):
    return [list(x) for x in zip(*A)]


def matmul(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),Q(0))
             for j in range(len(B[0]))] for i in range(len(A))]


def reconstruct() -> dict:
    # New majorant: regenerate its difference polynomial, do not import it.
    r=[Q(5,4)*x for x in mul([Q(1),-Q(20,27)],[Q(1),-Q(20,27)])]
    for i,x in enumerate([Q(1),-Q(1),Q(1,6)]):
        r[i]-=Q(12,11)*x
    require(r==[Q(7,44),-Q(226,297),Q(4042,8019)],"majorant expansion")
    der=[r[1],2*r[2]]
    require(der[1]>0 and at(der,Q(1,4))<0,"whole-interval derivative")
    margin=at(r,Q(1,4))
    require(margin==Q(23,64152)>0,"majorant endpoint")
    a5=arctan_bounds(5); a239=arctan_bounds(239)
    pi=(16*a5[0]-4*a239[1],16*a5[1]-4*a239[0])
    require(pi[0]>3 and pi[1]**2<10,"elementary pi bounds")
    h,sinc=trig_constant_bounds()
    require(sinc[0]>Q(11,12),"K0 lower bound")
    mass=Q(5,4)/SEPARATION
    require(mass==Q(15,8)<2,"Fourier majorant mass")
    # Triangle kernel is zero exactly at and beyond separation.
    triangle_checks=0
    for x in [Q(i,12) for i in range(-24,25)]:
        value=mass*max(Q(0),1-abs(x)/SEPARATION)
        overlap=max(Q(0),SEPARATION-abs(x))*Q(5,4)/SEPARATION**2
        require(value==overlap,"rectangle convolution")
        if abs(x)>=SEPARATION:
            require(value==0,"Fourier boundary support")
        triangle_checks+=1
    klower=1-Q(10)*SEPARATION**2/(6*Q(11,12))
    price=2*klower**2
    require(klower==Q(19,99),"close-pair lower value")
    require(price==Q(722,9801)>2*ALPHA,"pair payment")
    bonus=price-2*ALPHA
    # All finite window incidence coefficients, not a P7 source replay.
    incidence_checks=0
    for m in range(1,81):
        windows=[range(a,a+7) for a in range(max(0,m-6))]
        for i in range(m):
            for j in range(i+1,m):
                weight=Q(0)
                for W in windows:
                    if i in W and j in W:
                        weight+=Q(2,7-(j-i))
                require(0<=weight<=2,"seven-window pair multiplicity")
                incidence_checks+=1
        for i in range(m-1):
            count=sum(i in W and i+1 in W for W in windows)
            require(Q(count,3000)<=BETA,"seven-window gap charge")
            incidence_checks+=1
    # Complete finite enumeration of rational gap strings; repeated nodes included.
    matching_checks=0
    max_pairs=0
    alphabet=[Q(0),Q(1,3),Q(2,3),Q(1)]
    all_cases=[[]]
    for length in range(8):
        all_cases.extend(product(alphabet,repeat=length))
    for gaps in all_cases:
        points=[] if gaps==[] else [Q(0)]
        if not points and gaps != []:
            points=[Q(0)]
        for g in gaps:
            if not points: points=[Q(0)]
            points.append(points[-1]+g)
        # The empty tuple represents the singleton, [] the empty set.
        if isinstance(gaps,tuple) and not gaps: points=[Q(0)]
        remain,pairs=greedy(points)
        owned=remain+[j for pair in pairs for j in pair]
        require(sorted(owned)==list(range(len(points))),"matching coverage")
        require(len(set(owned))==len(owned),"matching duplication")
        for i,j in pairs:
            require(points[j]-points[i]<SEPARATION,"invalid pair")
        for i,j in zip(remain,remain[1:]):
            require(points[j]-points[i]>=SEPARATION,"survivor separation")
        D=points[-1]-points[0] if points else Q(0)
        DY=points[remain[-1]]-points[remain[0]] if remain else Q(0)
        require(DY<=D,"survivor span")
        lhs=ALPHA*(len(remain)-6)-BETA*DY+price*len(pairs)
        rhs=ALPHA*(len(points)-6)-BETA*D+bonus*len(pairs)
        require(lhs>=rhs,"global payment algebra")
        max_pairs=max(max_pairs,len(pairs)); matching_checks+=1
    # Independent exact synthetic matrices with known spectra.
    H=[[Q(1),Q(1),Q(1),Q(1)],
       [Q(1),-Q(1),Q(1),-Q(1)],
       [Q(1),Q(1),-Q(1),-Q(1)],
       [Q(1),-Q(1),-Q(1),Q(1)]]
    require(matmul(H,transpose(H))==[[4*x for x in row] for row in eye(4)],"Hadamard")
    roots=[[Q(1)]*4,[Q(2),Q(0),Q(0),Q(0)],
           [Q(3,2),Q(1,2),Q(1,2),Q(1,2)],
           [Q(1,2)]*4,[Q(0)]*4]
    qspecs=[[Q(x) for x in row] for row in
            [(0,0,0,0),(-2,0,0,0),(-3,-1,0,2),(2,2,-1,-1),(1,0,0,0),(-2,-2,-2,-2)]]
    matrix_checks=0; pinching_checks=0
    for root in roots:
        lamb=[x*x for x in root]
        require(sum(lamb)<=4,"column contract")
        V=[[root[i]*H[i][j]/2 for j in range(4)] for i in range(4)]
        P=matmul(V,transpose(V)); M=matmul(transpose(V),V)
        delta=sum((psi(x) for x in lamb),Q(0))
        for theta in [(Q(1),Q(0)),(Q(3,5),Q(4,5)),(Q(5,13),Q(12,13))]:
            cs,sn=theta; U=eye(4)
            U[0][0]=cs;U[0][1]=-sn;U[1][0]=sn;U[1][1]=cs
            require(matmul(U,transpose(U))==eye(4),"rational rotation")
            for qq in qspecs:
                Qmat=matmul([[U[i][j]*qq[j] for j in range(4)] for i in range(4)],transpose(U))
                A=[[P[i][j]+Qmat[i][j] for j in range(4)] for i in range(4)]
                norm=sum((x*x for row in A for x in row),Q(0))
                tr=sum((A[i][i] for i in range(4)),Q(0))
                b=sum(x>0 for x in qq)
                require(norm>=4*tr-12-4*b+delta,"synthetic rank stability")
                matrix_checks+=1
        for pairs in [[(0,1),(2,3)],[(0,2),(1,3)],[(0,3),(1,2)]]:
            block_delta=Q(0)
            for i,j in pairs:
                require(M[i][i]==M[j][j],"equal diagonal")
                a=M[i][i];b=M[i][j]
                block_delta+=psi(a+b)+psi(a-b)
            require(delta>=block_delta,"synthetic convex pinching")
            pinching_checks+=1
    # Endpoint-normalization, discarded grid tail, and multiplicity accounting.
    adapter_checks=0
    for L in range(8,81):
        require(Q(11,12)-Q(2,L)>=Q(2,3),"aL floor")
        require(Q(4)/(9*Q(2,3))*2*(Q(1,L**4)+Q(1,L**2))<=Q(4,L**2),"grid tail")
        adapter_checks+=1
    multiplicity_checks=0
    for s1,s2,p in product(range(7),repeat=3):
        for excess in range(3):
            N=s1+2*s2+2*p+excess
            D=s1+s2+2*p
            charge=3*s1+4*s2+4*p
            require(charge<=2*N+s1,"simple multiplicity charge")
            require(charge<=2*D+N,"distinct multiplicity charge")
            multiplicity_checks+=1
    new=((h[0]-BETA)/(1-ALPHA),(h[1]-BETA)/(1-ALPHA))
    old269=((1345000*h[0]-2680)/1340003,(1345000*h[1]-2680)/1340003)
    rad=sqrt_bounds(Q(726237,700000))
    c280=(2*rad[0]-1+Q(2603,700000),2*rad[1]-1+Q(2603,700000))
    old280=((h[0]-Q(279,140000))/(1-c280[0]/280),
            (h[1]-Q(279,140000))/(1-c280[1]/280))
    require(new[0]-old280[1]>Q(4867,100000000),"strict new lift")
    require(old280[0]>old269[1],"old comparison")
    require(new[0]>Q('0.673058325315610967410539842203'),"headline lower")
    require(new[1]<Q('0.673058325315610967410539842204'),"headline upper")
    distinct=((1+new[0])/2,(1+new[1])/2)
    return {
        'schema':'SPL26-bounded-v1',
        'status':{'new_mathematics':'proposed_complete_proof',
                  'rh_proved':False,'world_record_claimed':False,
                  'inherited_P7_replayed':False,'analytic_trace_input_reproved':False},
        'majorant':{'polynomial':[frac(x) for x in r],
                    'minimum':frac(margin),'derivative_at_right':frac(at(der,Q(1,4))),
                    'fourier_mass':frac(mass),'support_radius':frac(SEPARATION)},
        'pair':{'kernel_lower':frac(klower),'price':frac(price),'bonus':frac(bonus)},
        'global':{'count_coefficient':frac(ALPHA),'span_coefficient':frac(BETA),
                  'constant_loss':frac(6*ALPHA)},
        'coverage':{'triangle_convolution':triangle_checks,
                    'window_incidence':incidence_checks,
                    'matching_gap_strings':matching_checks,'maximum_pair_count':max_pairs,
                    'rank_stability_matrices':matrix_checks,'pinching_matrices':pinching_checks,
                    'adapter_constant_cases':adapter_checks,'multiplicity_cases':multiplicity_checks},
        'constants':{'H_MT':interval_text(h),'old269':interval_text(old269),
                     'old280':interval_text(old280),'new_simple':interval_text(new),
                     'new_distinct':interval_text(distinct),
                     'gain_vs_280':[decimal_out(new[0]-old280[1],32),
                                    decimal_out(new[1]-old280[0],32,True)]},
        'theorem_inputs':['P7 continuum inequality (imported)',
                          'Claude Theorem D trace and outside-zero tail (imported)',
                          'finite-dimensional spectral facts (proved/credited in manuscript)']
    }


def no_duplicate(pairs):
    obj={}
    for k,v in pairs:
        if k in obj: raise ValueError('duplicate JSON key')
        obj[k]=v
    return obj


def load_json(path: Path):
    return json.loads(path.read_text('utf-8'),object_pairs_hook=no_duplicate,
                      parse_float=lambda s: (_ for _ in ()).throw(ValueError('JSON floats forbidden')),
                      parse_constant=lambda s: (_ for _ in ()).throw(ValueError('nonfinite JSON forbidden')))


def same(a,b) -> bool:
    if type(a) is not type(b): return False
    if isinstance(a,dict): return a.keys()==b.keys() and all(same(a[k],b[k]) for k in a)
    if isinstance(a,list): return len(a)==len(b) and all(same(x,y) for x,y in zip(a,b))
    return a==b


def authenticate() -> None:
    manifest=ROOT/'SHA256SUMS'
    require(manifest.is_file() and not manifest.is_symlink(),'manifest missing/symlink')
    entries={}
    for line in manifest.read_text('utf-8').splitlines():
        digest,name=line.split('  ',1)
        require(len(digest)==64 and all(c in '0123456789abcdef' for c in digest),'hash syntax')
        require(name not in entries and '/' not in name and name not in ('.','..'),'manifest filename')
        entries[name]=digest
    actual={p.name for p in ROOT.iterdir() if p.name!='SHA256SUMS'}
    require(actual==set(entries),'package inventory differs')
    for name,digest in entries.items():
        p=ROOT/name
        require(p.is_file() and not p.is_symlink(),'nonregular package member')
        require(hashlib.sha256(p.read_bytes()).hexdigest()==digest,'package hash mismatch: '+name)


def main() -> int:
    ap=argparse.ArgumentParser(description=__doc__)
    group=ap.add_mutually_exclusive_group(required=True)
    group.add_argument('--check',type=Path)
    group.add_argument('--emit',type=Path)
    args=ap.parse_args()
    if args.check:
        authenticate()
        expected=load_json(args.check)
        actual=reconstruct()
        require(same(actual,expected),'mathematical reconstruction mismatch')
        print('PASS_SPL26_BOUNDED_ALGEBRA_NOT_P7_OR_ANALYTIC_REPLAY')
        print(hashlib.sha256(json.dumps(actual,sort_keys=True,separators=(',',':')).encode()).hexdigest())
    else:
        args.emit.write_text(json.dumps(reconstruct(),sort_keys=True,indent=2)+'\n','utf-8')
    return 0

if __name__=='__main__':
    try: sys.exit(main())
    except (ValueError, OSError, TypeError, KeyError, ZeroDivisionError) as exc:
        print('REFUSE: '+str(exc),file=sys.stderr)
        sys.exit(1)
