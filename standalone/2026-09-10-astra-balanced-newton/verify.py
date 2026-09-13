#!/usr/bin/env python3
"""Independent BNR26 reconstruction: trial factors, divisor fibers, work energy.

Imports neither producer nor repository code. No all-scale conclusion is checked.
"""
from __future__ import annotations
import argparse
import copy
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import gcd, isqrt
from pathlib import Path
from tempfile import TemporaryDirectory

PRECISION=128
UNIT=2**PRECISION
MAXIMUM=65535


def check(ok: bool, why: str) -> None:
    if not ok: raise ValueError(why)


def encode(x: object) -> bytes:
    return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode()


def stamp(x: object) -> str:
    return sha256(encode(x)).hexdigest()


def pair(x: Q) -> list[int]: return [x.numerator,x.denominator]


def mu_single(n: int) -> int:
    sign=1; p=2
    while p*p<=n:
        if n%p==0:
            n//=p; sign=-sign
            if n%p==0: return 0
        p+=1
    return -sign if n>1 else sign


def divisor_table(N: int) -> list[list[int]]:
    ds=[[] for _ in range(N+1)]
    for d in range(1,N+1):
        for n in range(d,N+1,d): ds[n].append(d)
    return ds


def cumulative(prefix: list[int]) -> list[int]:
    ans=[0]; total=0
    for a in prefix[1:]:
        total+=a; ans.append(total)
    return ans


def completion(prefix: list[int]) -> dict[int,Q]:
    b=len(prefix); M=cumulative(prefix)
    u=sum((Q(M[k],k*(k+1)) for k in range(1,b)),Q())
    late=-2*b*u
    c={n:Q(a) for n,a in enumerate(prefix) if n and a}
    c[b]=late-M[-1]; c[2*b]=-late
    c={n:a for n,a in c.items() if a}
    check(sum(c.values(),Q())==0,'zero terminal cumulative')
    check(sum((a/n for n,a in c.items()),Q())==0,'zero at one')
    return c


def work_energy(c: dict[int,Q]) -> Q:
    prior=Q(); total=Q()
    for n,a in sorted(c.items()):
        total+=(2*a*prior+a*a)/n
        prior+=a
    return total


def triple_state(prefix: list[int]) -> tuple[Q,Q,Q]:
    b=len(prefix); M=sum(prefix[1:])
    old={n:Q(a) for n,a in enumerate(prefix) if n and a}
    E=work_energy(old)-Q(M*M,b)
    u=sum((Q(a,n) for n,a in enumerate(prefix) if n),Q())-Q(M,b)
    return E,u,E+2*b*u*u


def inverse_lift(c: dict[int,Q],N: int,ds: list[list[int]]) -> list[Q]:
    den=1
    for a in c.values(): den=den*a.denominator//gcd(den,a.denominator)
    cs={n:int(a*den) for n,a in c.items()}
    cc=[0]*(N+1)
    for d in range(1,N+1):
        cc[d]=sum(cs.get(r,0)*cs.get(d//r,0) for r in ds[d])
    out=[Q()]
    for n in range(1,N+1):
        # Difference of the complete floor-pair cumulative at n and n-1.
        numerator=2*den*cs.get(n,0)-sum(cc[d] for d in ds[n])
        out.append(Q(numerator,den*den))
    return out


def saw_pair(c: dict[int,Q],k: int) -> tuple[Q,Q,Q]:
    a=b=boundary=Q()
    for r,cr in c.items():
        for s,cs in c.items():
            x=Q(k,r*s); frac=x-x.numerator//x.denominator
            a+=cr*cs*(frac-Q(1,2))
            b+=cr*cs*(Q() if x.denominator==1 else frac-Q(1,2))
            if x.denominator==1: boundary+=cr*cs
    return a,b,boundary


def panels(mu: list[int],ds: list[list[int]]) -> dict:
    pp=[];kk=[];bb=[];ss=[]
    for Y in range(1,25):
        b=Y+1; B=b*b-1
        prefix=mu[:b]; c=completion(prefix); E,u,A=triple_state(prefix)
        check(work_energy(c)==A,'optimum energy')
        p={b:Q(b*(1-b)),b+1:Q(b*(b+1)),2*b:Q(-2*b)}
        for t in (Q(-2,3),Q(1),Q(5,2)):
            perturb={n:t*a for n,a in p.items()}
            a={n:c.get(n,Q())+perturb.get(n,Q()) for n in c.keys()|perturb.keys()}
            check(work_energy(a)==A+work_energy(perturb),'orthogonality')
            pp.append([Y,pair(t),pair(A),pair(work_energy(perturb))])
        predicted=inverse_lift(c,B+1,ds)
        check(predicted[1:B+1]==mu[1:B+1],'all native coefficient fibers')
        eb=-sum((c.get(d,Q()) for d in ds[b]),Q())
        check(Q(mu[B+1])-predicted[B+1]==eb*eb,'first omitted coefficient')
        bb.append([Y,pair(eb),pair(predicted[B+1]),mu[B+1]])
        curve=cumulative(predicted)
        I=sum((curve[k]**2/Q(k*(k+1)) for k in range(b,B+1)),Q())
        ell=sum((curve[k]/Q(k*(k+1)) for k in range(b,B+1)),Q())
        EB,uB,AB=triple_state(mu[:B+1])
        check(EB==E+I and uB==u+ell and AB==E+I+2*(B+1)*(u+ell)**2,'joint transition')
        ss.append([Y,B,pair(I),pair(ell),pair(AB)])
        if Y<=10:
            for k in range(b,B+1):
                collar=2*sum((a for n,a in c.items() if n<=k),Q())
                psi,psi0,d=saw_pair(c,k)
                check(curve[k]==collar+psi and psi==psi0-d/2,'physical kernel / boundary')
                kk.append([Y,k,pair(curve[k]),pair(collar),pair(d)])
    return {'projection_cases':len(pp),'kernel_cases':len(kk),'boundary_cases':len(bb),'joint_map_cases':len(ss),
            'projection_sha256':stamp(pp),'kernel_sha256':stamp(kk),'boundary_rows':bb,'joint_map_sha256':stamp(ss)}


def ladder(mu: list[int],ds: list[list[int]]) -> list[dict]:
    source=[0,1]; rows=[]
    for Y in (1,3,15,255):
        B=(Y+1)**2-1
        check(len(source)==Y+1,'coefficient recursion source')
        pred=inverse_lift(completion(source),B,ds)
        check(all(a.denominator==1 for a in pred),'integral predicted prefix')
        ints=[int(a) for a in pred]
        check(ints==mu[:B+1],'trial factorization authentication')
        rows.append({'Y':Y,'B':B,'coefficients_checked':B,'source_sha256':stamp(source[1:]),'predicted_sha256':stamp(ints[1:])})
        source=ints
    return rows


def enclosures(mu: list[int]) -> dict:
    ys=list(range(1,65))+[127,255]
    cuts=sorted(set(ys+[(y+1)**2-1 for y in ys]))
    curve=cumulative(mu); rows={}; se=su=0
    for k in range(1,MAXIMUM+1):
        # Fixed 128-bit cell contract; division is toward negative infinity.
        numerator=curve[k]*UNIT
        su+=numerator//(k*(k+1))
        se+=(numerator*curve[k])//(k*(k+1))
        if k in cuts:
            el,eu=Q(se,UNIT),Q(se+k,UNIT)
            ul,uu=Q(su,UNIT),Q(su+k,UNIT)
            mn=Q() if ul<=0<=uu else min(abs(ul),abs(uu))**2
            mx=max(abs(ul),abs(uu))**2
            rows[k]={'Y':k,'M':curve[k],'E':[pair(el),pair(eu)],'u':[pair(ul),pair(uu)],
                     'A':[pair(el+2*(k+1)*mn),pair(eu+2*(k+1)*mx)]}
    trials=[]
    for y in ys:
        B=(y+1)**2-1; low=Q(*rows[y]['A'][0]); high=Q(*rows[B]['A'][1])
        margin=4*(1+low)**3-(1+high)**2
        check(margin>0,'finite source-specific pilot')
        trials.append([y,B,pair(margin)])
    return {'rounding_bits':PRECISION,'all_prefix_entries':MAXIMUM,'enclosed_cutoffs':len(cuts),
            'all_rows_sha256':stamp([rows[k] for k in cuts]),
            'candidate':'1+A_B <= 2(1+A_Y)^(3/2)','candidate_cases':len(trials),'candidate_sha256':stamp(trials),
            'ladder_rows':[rows[k] for k in (1,3,15,255,65535)]}


def tails(mu: list[int]) -> list[dict]:
    rows=[]
    for Y in (1,2,3,7):
        c=completion(mu[:Y+1]); X=4096; units=0
        # Entire finite sum reconstructed by floor endpoints, not convolution.
        for k in range(1,X):
            cumulative_value=2*sum((a for n,a in c.items() if n<=k),Q())
            cumulative_value-=sum((a*b*(k//(r*s)) for r,a in c.items() for s,b in c.items()),Q())
            term=cumulative_value**2/Q(k*(k+1))
            units+=(term.numerator*UNIT)//term.denominator
        norm1=sum((abs(a) for a in c.values()),Q())
        tail=norm1**4/(4*X)
        rows.append({'Y':Y,'first_unintegrated_cell':X,'lower':pair(Q(units,UNIT)),
                     'upper':pair(Q(units+X-1,UNIT)+tail),'whole_tail_bound':pair(tail)})
    return rows


def fake() -> list[dict]:
    ans=[]
    for b in (16,32,64,128):
        c=completion([0,1]+[0]*(b-2))
        check(c=={1:Q(1),b:Q(1-2*b),2*b:Q(2*b-2)},'fake source')
        J=work_energy(c); check(J==2*b-3+Q(1,b) and J<=2*b,'fake input')
        total=0
        for k in range(b*b//2,b*b):
            v=-sum((a*d*(k//(r*s)) for r,a in c.items() for s,d in c.items()),Q())
            check(v>=Q(k,2),'fake pointwise barrier')
            term=v*v/Q(k*(k+1)); total+=(UNIT*term.numerator)//term.denominator
        lo,hi=Q(total,UNIT),Q(total+b*b//2,UNIT)
        check(lo>=Q(b*b,16) and lo>=J*J/64,'fake energy barrier')
        ans.append({'b':b,'input_J':pair(J),'annular_energy':[pair(lo),pair(hi)],'lower':pair(Q(b*b,16)),'native_mobius':False})
    return ans


def reconstruct() -> dict:
    mu=[0]+[mu_single(n) for n in range(1,MAXIMUM+1)]
    ds=divisor_table(MAXIMUM)
    body={'schema':'BNR26-v1','scope':{'rh_proved':False,'unbounded_gain_proved':False,
          'finite_native_prefix_reconstruction':True,'raw_future_tail':'analytic bound, not omitted or fully enumerated',
          'generic_control_is_mobius':False},'base':'f99d9e3908dde4865377c75d9ca051c1f545bf4f',
          'panels':panels(mu,ds),'recursive_ladder':ladder(mu,ds),'prefix_energy':enclosures(mu),
          'raw_tails':tails(mu),'generic_obstruction':fake()}
    return {'body':body,'sha256':stamp(body)}


def load(path: Path) -> object:
    def object_hook(pairs):
        result={}
        for key,value in pairs:
            check(key not in result,'duplicate JSON key')
            result[key]=value
        return result
    def forbidden(s):raise ValueError('nonfinite JSON token')
    return json.loads(path.read_text(),object_pairs_hook=object_hook,parse_constant=forbidden)


def accept(actual: object, expected: dict) -> None:
    check(type(actual) is dict and set(actual)=={'body','sha256'},'report shape')
    check(actual['sha256']==stamp(actual['body']),'report seal')
    check(encode(actual)==encode(expected),'typed primitive reconstruction mismatch')


def self_test(expected: dict) -> int:
    mutations=[lambda b:b['scope'].update(rh_proved=True),
      lambda b:b['scope'].update(unbounded_gain_proved=0),
      lambda b:b['prefix_energy'].update(candidate_cases=66.0),
      lambda b:b['recursive_ladder'][0].update(B=4),
      lambda b:b['panels'].update(kernel_cases=1),
      lambda b:b['panels']['boundary_rows'][0][2].__setitem__(0,0),
      lambda b:b['prefix_energy'].update(all_prefix_entries=65534),
      lambda b:b['raw_tails'][0].update(whole_tail_bound=[0,1]),
      lambda b:b['generic_obstruction'][0].update(native_mobius=True),
      lambda b:b['generic_obstruction'].pop(),
      lambda b:b['prefix_energy']['ladder_rows'][-1]['A'][1].__setitem__(0,1),
      lambda b:b['recursive_ladder'][-1].update(predicted_sha256='0'*64)]
    count=0
    with TemporaryDirectory() as d:
        for i,mutate in enumerate(mutations):
            bad=copy.deepcopy(expected); mutate(bad['body'])
            check(encode(bad)!=encode(expected),'no-op mutation')
            bad['sha256']=stamp(bad['body']); path=Path(d)/f'mutation-{i}.json'
            path.write_bytes(encode(bad))
            try:accept(load(path),expected)
            except ValueError:count+=1
            else:raise ValueError('resealed corruption accepted')
        duplicate=Path(d)/'duplicate.json'; duplicate.write_text('{"a":1,"a":2}')
        try:load(duplicate)
        except ValueError:pass
        else:raise ValueError('duplicate key accepted')
    return count


def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('report',type=Path)
    ap.add_argument('--output',type=Path);ap.add_argument('--self-test',action='store_true')
    args=ap.parse_args(); expected=reconstruct(); accept(load(args.report),expected)
    if args.output:args.output.write_bytes(encode(expected)+b'\n')
    print('BNR INDEPENDENT IMPLEMENTATION PASS',expected['sha256'])
    if args.self_test:print('RESEALED CORRUPTIONS REJECTED',self_test(expected),'AND DUPLICATE-KEY REFUSAL')

if __name__=='__main__':main()
