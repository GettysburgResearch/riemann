#!/usr/bin/env python3
"""Exact finite controls for CFC26; not an infinite-theorem verifier.

The ICR26 receipt is an authenticated imported input. This program does not
regenerate its theta integrals. A separate parent-backend replay is recorded.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
from itertools import product
from math import comb, factorial, isqrt
from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parent
Q = F(1, 5)
PINNED = {
    'ICR_PARAMETERS.json': '5f2377e538069e5e5d6f4df01e15a91880e21f1bfd73dd83818a226974a71c0b',
    'ICR_RECEIPT.json': '531b80259640396ce9f54144b69dbfb8daf90ecf944ca9cecc1e0809d0500160',
}

def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)

def pairs(items):
    out = {}
    for key, value in items:
        need(key not in out, 'duplicate JSON key: '+key)
        out[key] = value
    return out

def bad_number(value):
    raise ValueError('floating/nonfinite JSON number: '+value)

def read_json(path: Path):
    return json.loads(path.read_text(), object_pairs_hook=pairs,
                      parse_float=bad_number, parse_constant=bad_number)

def canon(value) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(',',':')).encode()+b'\n'

def rat(x: F):
    return [x.numerator, x.denominator]

def inverse(a):
    n=len(a)
    a=[list(row)+[F(i==j) for j in range(n)] for i,row in enumerate(a)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if a[i][j]),None)
        need(pivot is not None,'singular rational matrix')
        a[j],a[pivot]=a[pivot],a[j]
        v=a[j][j];a[j]=[x/v for x in a[j]]
        for i in range(n):
            if i!=j:
                v=a[i][j];a[i]=[x-v*y for x,y in zip(a[i],a[j])]
    return [row[n:] for row in a]

def cumulants(moments):
    out=[F(0)]*len(moments)
    for n in range(1,len(moments)):
        out[n]=moments[n]-sum(comb(n-1,j-1)*out[j]*moments[n-j]
                              for j in range(1,n))
    return out

def law(n, edges):
    for i,j,q in edges:
        need(0<=i<j<n and F(0)<=q<F(1),'invalid/nonferromagnetic edge')
    entries=[]
    for bits in product((-1,1),repeat=n):
        mass=F(1)
        for i,j,q in edges:
            mass*=1+q*bits[i]*bits[j]
        entries.append((bits,mass))
    z=sum(mass for _,mass in entries)
    return [(bits,mass/z) for bits,mass in entries]

def path_moments(core_law, core_weights, core_deriv, weights, deriv, order):
    k=len(core_weights)
    a={sign:[F(0)]*(order+1) for sign in (-1,1)}
    da={sign:[F(0)]*(order+1) for sign in (-1,1)}
    for bits,prob in core_law:
        y=sum(w*s for w,s in zip(core_weights,bits))
        dy=sum(w*s for w,s in zip(core_deriv,bits))
        sign=bits[-1]
        for j in range(order+1):
            a[sign][j]+=prob*y**j
            if j: da[sign][j]+=prob*j*y**(j-1)*dy
    for w,dw in zip(weights,deriv):
        b={sign:[F(0)]*(order+1) for sign in (-1,1)}
        db={sign:[F(0)]*(order+1) for sign in (-1,1)}
        for old in (-1,1):
            for new in (-1,1):
                p=(1+Q*old*new)/2
                for n in range(order+1):
                    for j in range(n+1):
                        power=n-j; coeff=p*comb(n,j)
                        b[new][n]+=coeff*a[old][j]*(w*new)**power
                        db[new][n]+=coeff*da[old][j]*(w*new)**power
                        if power:
                            db[new][n]+=coeff*a[old][j]*power*(w*new)**(power-1)*dw*new
        a,da=b,db
    return [a[-1][n]+a[1][n] for n in range(order+1)], [da[-1][n]+da[1][n] for n in range(order+1)]

def graph_controls():
    records=[]; identities=0; configurations=0
    for k,core_edges in [(1,[]),(2,[(0,1,F(1,3))]),
                         (3,[(0,1,F(1,7)),(1,2,F(1,4)),(0,2,F(1,6))])]:
        for cloud in (1,2,3):
            tail=2
            cw=[F(i+1,3*i+7) for i in range(k)]
            ws=[F(1,10)]*cloud+[F(1,2*(12+j)) for j in range(tail)]
            cds=[F(int(i==0)) for i in range(k)]
            ds=[-F(1,cloud)]*cloud+[F(0)]*tail
            core=law(k,core_edges)
            n=k+len(ws)
            edges=core_edges+[(k-1+j,k+j,Q) for j in range(len(ws))]
            full=law(n,edges);configurations+=len(full)
            marg={bits:F(0) for bits,_ in core}
            cond={bits:[F(0)]*7 for bits,_ in core}
            raw=[F(0)]*11;draw=[F(0)]*11
            eb2=F(0); cross=F(0)
            for bits,p in full:
                cb=bits[:k];bs=bits[k:]
                marg[cb]+=p
                y=sum(a*s for a,s in zip(cw,cb));b=sum(a*s for a,s in zip(ws,bs))
                dy=sum(a*s for a,s in zip(cds,cb));db=sum(a*s for a,s in zip(ds,bs))
                for j in range(7):cond[cb][j]+=p*b**j
                for j in range(11):
                    raw[j]+=p*(y+b)**j
                    if j:draw[j]+=p*j*(y+b)**(j-1)*(dy+db)
                eb2+=p*b*b;cross+=p*y*b
            mean=sum((Q**(j+1)*w for j,w in enumerate(ws)),F(0))
            vcov=sum(ws[i]*ws[j]*Q**abs(i-j) for i in range(len(ws)) for j in range(len(ws)))
            for bits,p in core:
                need(marg[bits]==p,'attached path changed core marginal');identities+=1
                need(cond[bits][1]/p==bits[-1]*mean,'conditional mean / bridge error');identities+=1
                for j in (2,4,6):
                    uncond=sum(vals[j] for vals in cond.values())
                    need(cond[bits][j]/p==uncond,'conditional even moment');identities+=1
            need(eb2==vcov,'full covariance including all cross terms');identities+=1
            need(eb2<=F(3,2)*sum(w*w for w in ws),'variance row-sum bound');identities+=1
            need(mean<=max(ws)/4,'complete prefix-boundary mean');identities+=1
            eys=sum(p*sum(a*s for a,s in zip(cw,bits))*bits[-1] for bits,p in core)
            need(cross==mean*eys and cross>0,'missing positive core-tail cross term');identities+=1
            pm,pd=path_moments(core,cw,cds,ws,ds,10)
            need(pm==raw and pd==draw,'independent transfer/derivative enumeration mismatch');identities+=22
            need(sum(cds)+sum(ds)==0,'calibration head sum derivative');identities+=1
            for j in (2,4,6):
                bj=sum(vals[j] for vals in cond.values())
                bound=F(factorial(j),2**(j//2)*factorial(j//2))*vcov**(j//2)
                need(bj<=bound,'finite Lee-Yang moment consequence');identities+=1
            records.append({'core_spins':k,'cloud':cloud,'finite_tail':tail,
                            'variance_append':rat(vcov),'conditional_mean':rat(mean),
                            'cross_core_tail':rat(cross),'moment6':rat(raw[6]),
                            'moment6_derivative':rat(draw[6])})
    try:
        law(2,[(0,1,-F(1,5))])
    except ValueError:
        identities+=1
    else:
        raise ValueError('negative edge accepted')
    return {'panels':records,'identities':identities,'enumerated_configurations':configurations}

def sqrt_bounds(x, bits=100):
    need(x>=0,'negative radical')
    scale=1<<bits
    a=isqrt(x.numerator*scale*scale//x.denominator)
    lo,hi=F(a,scale),F(a+1,scale)
    need(lo*lo<=x<=hi*hi,'invalid sqrt enclosure')
    return lo,hi

def perron_controls():
    panels=[]
    for fields in ([1],[2],[4,3,2,1],[9,9,9,3,2],[16,8,4,2,1],
                   [F(5,4)]*8,[3,3,F(3,2),F(4,3),F(7,6),1]):
        fields=list(map(F,fields))
        need(all(a>=b>=1 for a,b in zip(fields,fields[1:])),'field monotonicity')
        row=[F(1,2),F(1,2)]; lo=hi=F(1)
        for e in fields:
            # Direct Markov transfer, not a product-of-eigenvalues substitution.
            row=[((1+Q)*row[0]+(1-Q)*row[1])*e/2,
                 ((1-Q)*row[0]+(1+Q)*row[1])/e/2]
            tr=(1+Q)*(e+1/e)/2
            a,b=sqrt_bounds(tr*tr-4*Q)
            lo*= (tr+a)/2;hi*=(tr+b)/2
        mg=sum(row)
        need(mg*6>=hi and mg<=6*lo,'uniform Perron product comparison')
        panels.append({'fields':[rat(e) for e in fields],'mgf':rat(mg),
                       'product_eigenvalue_interval':[rat(lo),rat(hi)]})
    return panels

def imported_core_controls():
    for name,wanted in PINNED.items():
        need(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==wanted,
             'imported primitive changed: '+name)
    pars=read_json(ROOT/'ICR_PARAMETERS.json');data=read_json(ROOT/'ICR_RECEIPT.json')
    need(data['status']=='proposed-component-not-RH' and data['rh_proved'] is False,'imported status')
    need(data['matched_even_orders']==[2,4,6,8,10,12,14],'imported exact scope')
    bits=data['bits'];need(type(bits) is int and bits==320,'imported scale')
    sc=1<<bits
    need(F(data['variance'][0],sc)>F(1,25) and F(data['variance'][1],sc)<F(1,20),'variance bound')
    c=list(map(F,pars['centers']));rad=F(pars['radius'])
    need(len(c)==7 and rad==F(1,10**14),'source box')
    need(all(F(1,2000)<x-rad<x+rad<1 for x in c),'source positive box')
    sign=cumulants([F(int(j%2==0)) for j in range(17)])
    dimmom=[F(1)]+[F(0) if j%2 else F(3,5) for j in range(1,17)]
    dim=cumulants(dimmom)
    ratio=[dim[2*j]/sign[2*j] for j in range(1,9)]
    nu=[256,10,1,1,1,1]
    J=[[r*nu[j]*c[j]**(r-1) for j in range(6)]
        +[r*ratio[r-1]*c[6]**(r-1)] for r in range(1,8)]
    inv=inverse(J)
    for i in range(7):
        for j in range(7):
            need(sum(inv[i][k]*J[k][j] for k in range(7))==int(i==j),'source rational inverse')
    rn=max(sum(map(abs,row)) for row in inv)
    need(rn<75000000,'source inverse row norm')
    need(F(data['beta_dyadic_upper'],sc)<F(6,10**22),'source beta')
    need(F(data['jacobian_row_sum_dyadic_upper'],sc)<F(101,10**9),'source Jacobian row sum')
    return {'imported_not_new_theta_integration':True,'inverse_identities':49,
            'row_norm':rat(rn),'variance_interval':[rat(F(x,sc)) for x in data['variance']],
            'sign_cumulants':[rat(sign[2*j]) for j in range(1,9)]}

def explicit_threshold_controls():
    # All comparisons are integers/Fractions, not decimal floating checks.
    N=10**1000; rootN=10**500
    need(rootN*rootN==N,'threshold square')
    need(F(1,2)<1000-304 and 1500+7<2000,'cloud positivity/mass ceiling')
    need(F(3,2)*(F(2000**2,N)+F(1,4*(N-1)))<F(7*10**6,N),'complete tail variance ceiling')
    need(64*7*10**6<30000**2 and 96*10000**2<100000**2,'Lp tail ceilings')
    need(F(542,N)<F(1,3) and F(3,2)*542<1000,'Gibbs density coefficient')
    raw0=16*30000*601**15+1000*300**16
    raw1=16*15*10000*30000*601**14+16*100000*301**15+1000*16*10000*300**15
    need(raw0<10**60 and raw1<10**60,'raw moment C1 integer bounds')
    cpoly=factorial(16)*2**15
    need(cpoly<10**18 and 301**16<10**40,'cumulant coefficient/degree bounds')
    need(16*cpoly*10**40*10**60<10**120,'cumulant telescope')
    need((16+16**2*10**6)*cpoly*10**40*10**60<10**130,'cumulant derivative telescope')
    need(25**8<2*10**11 and 10**130*25**8<10**150,'variance normalization budget')
    eta=F(10**150,rootN)
    need(eta==F(1,10**350),'perturbation exponent')
    beta=F(6,10**22)+10**8*eta
    lip=F(101,10**9)+7*10**8*eta
    rad=F(1,10**14)
    need(lip<1 and beta+lip*rad<rad,'full nonlinear contraction budget')
    need(1903757312<2*10**9 and 2*10**9*eta<F(1,100),'moment sixteen guard')
    need(F(7,8)/F(1,2)==F(7,4),'logarithmic growth coefficient')
    # Formal exact coefficient accounting: constants stand for already-defined
    # convergent quantities, not fresh numerical evaluations of them.
    for B0,Btheta,H,S,d,core in [(F(2,3),-F(7,5),F(9,2),F(1,100),-F(12,7),F(3,4)),
                                (F(1,4),-F(5,3),F(8),F(1,20),-F(5,3),F(1,2))]:
        cloud=Btheta-B0+H/2-d*S-core
        need(B0-H/2+d*S+core+cloud==Btheta,'linear coefficient / cloud accounting')
    return {'N_definition':'10^1000','square_root_N_definition':'10^500',
            'equation_C1_perturbation_bound':rat(eta),
            'preconditioned_beta_bound':rat(beta),'preconditioned_row_sum_bound':rat(lip),
            'box_radius':rat(rad),'invariance_margin':rat(rad-beta-lip*rad),
            'new_root_numerically_evaluated':False,'checks':18}

def reconstruct():
    need(Q==F(1,5),'primitive correlation drift')
    return {'schema':'CFC26.result.v1','status':'proposed-components-not-RH',
            'rh_proved':False,'all_order_reachability_proved':False,
            'theta_application_matched_even_orders':[2,4,6,8,10,12,14],
            'theta_application_is_theta':False,'theorem_directions':'completion and stability, not all-order reachability',
            'core_source':imported_core_controls(),'finite_graph':graph_controls(),
            'perron_finite_panels':perron_controls(),'explicit_analytic_threshold':explicit_threshold_controls()}

def authenticate():
    manifest=ROOT/'SHA256SUMS'
    need(manifest.is_file() and not manifest.is_symlink(),'missing regular manifest')
    listed={}
    for line in manifest.read_text().splitlines():
        digest,name=line.split('  ',1)
        need('/' not in name and name not in listed and name not in ('.','..'),'manifest path')
        p=ROOT/name
        need(p.is_file() and not p.is_symlink(),'missing/nonregular payload '+name)
        need(hashlib.sha256(p.read_bytes()).hexdigest()==digest,'payload hash '+name)
        listed[name]=digest
    need(set(p.name for p in ROOT.iterdir())==set(listed)|{'SHA256SUMS'},'exact package inventory')
    need({'PROOF.md','check.py','ICR_PARAMETERS.json','ICR_RECEIPT.json','result.json'}<=set(listed),'mandatory payload')

def main():
    parser=argparse.ArgumentParser()
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--emit',action='store_true')
    group.add_argument('--check',type=Path)
    args=parser.parse_args()
    if args.check:
        authenticate(); old=read_json(args.check)
    new=reconstruct()
    if args.check:
        need(canon(old)==canon(new),'reconstructed mathematical result mismatch')
    sys.stdout.buffer.write(canon(new))

if __name__=='__main__':
    try: main()
    except (ValueError,OSError,KeyError,TypeError) as exc:
        print('REJECT: '+str(exc),file=sys.stderr)
        sys.exit(1)
