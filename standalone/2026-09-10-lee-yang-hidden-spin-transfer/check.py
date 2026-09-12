#!/usr/bin/env python3
"""Exact bounded controls; not a proof of the infinite analytic theorems."""
from fractions import Fraction as F
from itertools import product
from math import comb, factorial
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
PARENT = 'c79c2f6c59640e5f5ef6e22b2ff745d3a8f5a0ff'
FILES = {'PROOF.md','README.md','SOURCES.json','VALIDATION.md',
         'check.py','result.json','SHA256SUMS'}

def need(ok, message):
    if not ok:
        raise ValueError(message)

def canonical(x):
    return json.dumps(x, sort_keys=True, separators=(',',':'))

def weight(spins, edges):
    out = F(1)
    for i,j,r in edges:
        need(r >= 1 and i < j, 'invalid pair weight')
        if spins[i] == spins[j]:
            out *= r
    return out

def partition(n, edges, field_bases, S):
    need(S % 2 == 0, 'exact field parameter parity')
    out = F(0)
    for z in product((-1,1), repeat=n):
        val = weight(z, edges)
        for a,r in enumerate(field_bases):
            val *= r ** (z[a]*(S//2))
        out += val
    return out

def levels(nv, nh, edges):
    out = {s:F(0) for s in range(-nv,nv+1,2)}
    for z in product((-1,1),repeat=nv+nh):
        out[sum(z[:nv])] += weight(z, edges)
    return out

def poly(coeff, x):
    return sum((v*x**(2*r) for r,v in enumerate(coeff)),F(0))

def entropy(d,x):
    return sum((x**(2*r)/F(2*r*(2*r-1)) for r in range(1,d+1)),F(0))

def laurent_derivative(p):
    q={}
    for k,v in p.items():
        if k:
            q[k-1]=q.get(k-1,F(0))+k*v
    return {k:v for k,v in q.items() if v}

def du(p, exponential=False):
    # D_u=(2t)^-1 D_t.  With exponential=True the expression is exp(2t)*p(t).
    q=laurent_derivative(p)
    if exponential:
        for k,v in p.items():
            q[k]=q.get(k,F(0))+2*v
    return {k-1:v/2 for k,v in q.items() if v}

def reconstruct():
    trace=[]
    hidden_cases=[(1,[],[F(1)]),(1,[],[F(2)]),
      (2,[(0,1,F(2))],[F(2),F(3)]),
      (3,[(0,1,F(3,2)),(1,2,F(2))],[F(1),F(2),F(3)]),
      (3,[(0,1,F(4,3)),(0,2,F(2)),(1,2,F(3,2))],[F(2),F(3),F(2)])]
    hidden_checks=0
    for nh,edges,bases in hidden_cases:
        Z=partition(nh,edges,bases,0)
        for s in (2,4,6,8):
            M=partition(nh,edges,bases,s)/Z
            M2=partition(nh,edges,bases,2*s)/Z
            need(M>=1 and M**4>=M2,'hidden pressure contrast')
            trace.append(['pressure',nh,s,str(M**4-M2)])
            hidden_checks+=1
    enumerated=0; factorizations=0
    for nv in (2,4,6):
      for nh,he,bases in hidden_cases:
        rv=F(3,2)
        edges=[(i,j,rv) for i in range(nv) for j in range(i+1,nv)]
        edges += [(nv+i,nv+j,r) for i,j,r in he]
        edges += [(i,nv+a,bases[a]) for i in range(nv) for a in range(nh)]
        got=levels(nv,nh,edges)
        enumerated+=2**(nv+nh)
        const=F(1)
        for r in bases: const*=r**(nv//2)
        for s,val in got.items():
            k=(nv+s)//2
            aligned=k*(k-1)//2+(nv-k)*(nv-k-1)//2
            expected=comb(nv,k)*rv**aligned*const*partition(nh,he,bases,s)
            need(val==expected,'full hidden partition factorization')
        trace.append(['factorization',nv,nh,[str(got[s]) for s in sorted(got)]])
        factorizations+=1
    target_checks=0
    for d in range(2,7):
      coeff=[F(2,3)]+[F((-1)**r*(r+1),r+2) for r in range(1,d)]+[F(1)]
      for L in (4,6,8,10,12):
        N=L**(2*d+1)
        H=lambda x:N*entropy(d,F(x,L))-poly(coeff,F(x))
        DP=poly(coeff,F(2))-4*poly(coeff,F(1))+3*poly(coeff,F(0))
        delta=H(2)-4*H(1)+3*H(0)
        exact=sum((F(2**(2*r)-4,2*r*(2*r-1))*L**(2*d+1-2*r)
                   for r in range(2,d+1)),F(0))-DP
        need(delta==exact,'entropy contrast identity')
        need(delta>=L**(2*d-3)-DP,'quartic lower bound')
        need(all((N+j*L**(2*d))%2==0 and j*L**(2*d)<=N
                 for j in (0,1,2)),'literal level parity/support')
        trace.append(['entropy',d,L,str(delta)])
        target_checks+=1
    # Complete exact connected pair witness: no hidden spins.
    edges=[(0,1,F(2)),(1,2,F(101,100)),(2,3,F(2))]
    got=levels(4,0,edges)
    R0=got[0]/6;R2=got[2]/4;R4=got[4]
    ratio=R4*R0**3/R2**4
    need((R0,R2,R4)==(F(601,300),F(201,100),F(101,25)),
         'connected witness level means')
    need(ratio==F(87701047604,44070501627) and ratio>F(199,100),
         'connected witness ratio')
    trace.append(['connected_witness',str(ratio)])
    # Exact derivative after x -> sqrt(u), without a symbolic engine.
    lead={0:F(1)}; drift={1:F(-9,2)}
    for _ in range(3):
        lead=du(lead,True);drift=du(drift)
    need(lead=={-3:F(1),-4:F(-3,2),-5:F(3,4)},'theta leading derivative')
    need(drift=={-5:F(-27,16)},'theta drift derivative')
    need((-6)**2-4*4*3==-12,'positive leading polynomial')
    # Coarse source constants and strictly separated polynomial degree test.
    need(F(8,3)**2>7 and 3**2==9,'exponential square brackets')
    need(4*21**2-6*21>2**10,'theta first-term lower factor')
    need(24*147**2<2**19,'theta upper factor')
    need(40-19-24==-3 and -144+147==3,'theta log-contrast accounting')
    need(sum((F(3,4)**k/F(factorial(k)) for k in range(4)),F(0))>2,
         'log2 upper comparison')
    need(F(3)-3*F(3,4)==F(3,4),'log-contrast lower constant')
    need(8*F(1,2)**4==F(1,2) and F(3,4)-F(1,2)==F(1,4),
         'degree-test margin')
    need(4*332==1328 and 1+4+3==8,'coefficient error budgets')
    # Bounded polynomial checks of the exact entropy remainder majorant.
    remainder_checks=0
    for r in range(4,17):
      for x in (F(0),F(1),F(2)):
        m=x/r; N=r**4
        part=N*sum((m**(2*k)/F(2*k*(2*k-1)) for k in range(3,13)),F(0))
        bound=N*m**6/(30*(1-m*m))
        need(0<=part<=bound,'critical quartic entropy remainder')
        need(N*m**4/12==x**4/12,'critical quartic coefficient')
        remainder_checks+=1
    # Exact product-factor inequality and its derivative signs.
    product_checks=0
    for k in range(1,25):
        t=F(k,17)
        need((1+t)**4-(1+4*t)==6*t*t+4*t**3+t**4,
             'single factor contrast')
        for u in (F(1,3),F(2),F(7)):
            g2=2+1/(u+t)**2;g3=-2/(u+t)**3
            need(g2>0 and g3<0,'squared-coordinate signs')
        product_checks+=1
    need(F(1,4)/3==F(1,12),'tightness Paley-Zygmund constant')
    return {'schema':1,'status':'PROPOSED_COMPONENT_PROOFS_NOT_RH',
      'source_head':PARENT,'rh_proved':False,'theta_pair_realization_proved':False,
      'all_pair_realizations_ruled_out':False,
      'groups':{'hidden_pressure_panels':hidden_checks,
        'complete_partition_factorizations':factorizations,
        'configuration_instances_in_factorizations':enumerated,
        'entropy_contrast_panels':target_checks,
        'complete_connected_witness_configurations':16,
        'quartic_remainder_panels':remainder_checks,
        'product_factor_panels':product_checks,
        'formal_theta_third_derivative_panels':1},
      'connected_ratio':str(ratio),
      'trace_sha256':hashlib.sha256(canonical(trace).encode()).hexdigest(),
      'actual_theta_integrals_computed':0,'analytic_theorems_machine_proved':False}

def strict_load(path):
    def pairs(items):
        out={}
        for k,v in items:
            need(k not in out,'duplicate JSON key');out[k]=v
        return out
    def invalid(s):
        raise ValueError('noninteger JSON number')
    return json.loads(Path(path).read_text(encoding='utf-8'),
        object_pairs_hook=pairs,parse_float=invalid,parse_constant=invalid)

def authenticate():
    need({p.name for p in ROOT.iterdir()}==FILES,'inventory differs')
    need(all((ROOT/n).is_file() and not (ROOT/n).is_symlink() for n in FILES),
         'nonregular file')
    entries={}
    for line in (ROOT/'SHA256SUMS').read_text().splitlines():
        h,n=line.split('  ',1)
        need(n in FILES-{'SHA256SUMS'} and n not in entries,'manifest path')
        need(len(h)==64 and all(c in '0123456789abcdef' for c in h),'hash encoding')
        entries[n]=h
    need(set(entries)==FILES-{'SHA256SUMS'},'manifest coverage')
    for n,h in entries.items():
        need(hashlib.sha256((ROOT/n).read_bytes()).hexdigest()==h,'hash: '+n)
    source=strict_load(ROOT/'SOURCES.json')
    need(source['source_head']==PARENT,'source drift')

def self_test():
    authenticate()
    outcomes=[]
    for case in ('pristine','false_realization','boolean_schema','duplicate_key',
                 'wrong_ratio','producer_ratio','changed_proof','extra_file'):
      with tempfile.TemporaryDirectory() as td:
        dst=Path(td)/'packet';shutil.copytree(ROOT,dst)
        out=dst/'result.json'
        if case in ('false_realization','boolean_schema','wrong_ratio'):
            data=json.loads(out.read_text())
            if case=='false_realization':data['theta_pair_realization_proved']=True
            elif case=='boolean_schema':data['schema']=True
            else:data['connected_ratio']='1'
            out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
        elif case=='duplicate_key':
            out.write_text(out.read_text().replace('{','{"schema":1,',1))
        elif case=='producer_ratio':
            f=dst/'check.py';old=f.read_text()
            new=old.replace('ratio=R4*R0**3/R2**4','ratio=R4*R0**2/R2**4',1)
            need(new!=old,'mutation missing');f.write_text(new)
        elif case=='changed_proof':
            (dst/'PROOF.md').write_text((dst/'PROOF.md').read_text()+'\nAlteration.\n')
        elif case=='extra_file':
            (dst/'extra.txt').write_text('not part of reviewed packet\n')
        if case not in ('pristine','changed_proof'):
            lines=[]
            for name in sorted(FILES-{'SHA256SUMS'}):
                lines.append(hashlib.sha256((dst/name).read_bytes()).hexdigest()+'  '+name)
            (dst/'SHA256SUMS').write_text('\n'.join(lines)+'\n')
        cmd=[sys.executable,'-I','-S','-B']
        if sys.flags.optimize:cmd.append('-O')
        cmd += [str(dst/'check.py'),'--check',str(out)]
        got=subprocess.run(cmd,text=True,capture_output=True,timeout=30)
        need((got.returncode==0)==(case=='pristine'),'wrong refusal: '+case)
        outcomes.append({'case':case,'accepted':got.returncode==0})
    print(json.dumps({'self_tests':outcomes},indent=2,sort_keys=True))

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    g=ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--emit',action='store_true')
    g.add_argument('--check',type=Path)
    g.add_argument('--self-test',action='store_true')
    args=ap.parse_args()
    if args.self_test:
        self_test();return
    expected=reconstruct()
    if args.check:
        authenticate()
        need(canonical(strict_load(args.check))==canonical(expected),'reconstruction differs')
    print(json.dumps(expected,indent=2,sort_keys=True))

if __name__=='__main__':
    try:main()
    except (ValueError,TypeError,KeyError,OSError,subprocess.TimeoutExpired) as exc:
        print('REJECT: '+str(exc),file=sys.stderr);sys.exit(1)
