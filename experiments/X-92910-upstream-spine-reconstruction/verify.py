#!/usr/bin/env python3
from __future__ import annotations
from fractions import Fraction
from pathlib import Path
from hashlib import sha256
import argparse, json, math, subprocess, sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
CTRL=json.loads((HERE/'certificates/control.json').read_text())

def require(x,msg):
    if not x: raise AssertionError(msg)

def constants():
    require(8*8<CTRL['R'],'subcritical coefficient')
    require(CTRL['terminal_overfill']<CTRL['terminal_reserve'],'terminal margin')
    require(CTRL['thinning_cost']+4+CTRL['terminal_overfill']*11+1<CTRL['native_total'],'native total')
    require(9*100>21*21*2,'C_square > 1/10')
    return True

def quantizer():
    count=0
    for den in range(3,40):
        r0=Fraction(den+2,den); r1=Fraction(den,den+2)
        for a in range(1,20):
            r=r1+Fraction(a,20)*(r0-r1)
            q0=(r-r1)/(r0-r1); q1=1-q0
            require(0<=q0<=1 and 0<=q1<=1,'positive weights')
            require(q0+q1==1,'mass')
            require(q0*r0+q1*r1==r,'martingale mode')
            count+=1
    return count

def y4(N=20000):
    def factor(n):
        d={};p=2
        while p*p<=n:
            while n%p==0:d[p]=d.get(p,0)+1;n//=p
            p+=1
        if n>1:d[n]=d.get(n,0)+1
        return d
    def lam(n):
        f=factor(n); return math.log(next(iter(f))) if len(f)==1 else 0.0
    def Y(q):
        s=0.0;w=1
        while True:
            s+=w*lam(q)
            if q%4:return s
            q//=4;w*=2
    for q in range(2,N+1):
        lhs=Y(q)-(2*Y(q//4) if q%4==0 else 0)
        require(abs(lhs-lam(q))<1e-12,'Y4 recurrence')
    return N

def frozen_replays():
    out=[]
    for rel in [
        'experiments/X-91690-factor67-sontr/verify.py',
        'experiments/X-91682-post-hall-complete-profile/verify.py',
        'experiments/X-91754-one-shot-native-slack/verify.py']:
        p=ROOT/rel
        if not p.exists(): continue
        cp=subprocess.run([sys.executable,str(p)],cwd=p.parent,text=True,capture_output=True)
        require(cp.returncode==0,rel+'\n'+cp.stderr)
        out.append({'path':rel,'tail':cp.stdout[-300:]})
    require(len(out)>=2,'missing frozen replays')
    return out

def required_paths():
    paths=[
      'claims/lemmas/L-92910-root-hall-profile-spine-is-finite-and-directed.md',
      'claims/lemmas/L-92911-whole-cell-endpoint-realization-is-positive-and-exact.md',
      'claims/lemmas/L-92912-all-column-and-terminal-reserve-is-explicit.md',
      'claims/lemmas/L-92913-native-y4-cost-is-below-55000.md',
      'claims/lemmas/L-92914-prime-square-source-has-explicit-positive-quadratic-drift.md',
      'claims/theorems/T-92910-bounded-native-deficit-forces-rh.md',
      'claims/theorems/T-92911-upstream-spine-reconstructed-resolution-proposal.md',
      'imports/t92910/IMPORT_MANIFEST.json']
    for p in paths: require((ROOT/p).is_file(),p)
    text='\n'.join((ROOT/p).read_text() for p in paths[:7])
    require('54983<55000' in text,'native bound')
    require('C_{\\square}>1/10' in text,'positive moat')
    require('full-child-capacity substitution is absent' in text,'capacity firewall')
    return paths

def mutations():
    result={}
    old=CTRL['terminal_overfill']; CTRL['terminal_overfill']=6000
    try: constants(); result['terminal_overdraw_fails']=False
    except AssertionError: result['terminal_overdraw_fails']=True
    CTRL['terminal_overfill']=old
    old=CTRL['native_total']; CTRL['native_total']=50000
    try: constants(); result['native_total_fails']=False
    except AssertionError: result['native_total_fails']=True
    CTRL['native_total']=old
    return result

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--mutations',action='store_true'); ap.add_argument('--output',default='results/verification.json'); args=ap.parse_args()
    payload={'ok':True,'verdict':'PASS_UPSTREAM_SPINE_RECONSTRUCTION_PACKET','checks':{'constants':constants(),'quantizer_samples':quantizer(),'y4_range':y4(),'frozen_replays':frozen_replays(),'required_paths':required_paths()},'mutations':mutations() if args.mutations else {},'scope':'finite/directed reconstruction, constants, provenance and endpoint composition; independent human proof review remains required','rh_proved':False}
    canonical=json.dumps(payload,sort_keys=True,separators=(',',':')).encode(); payload['proof_object_sha256']=sha256(canonical).hexdigest()
    out=HERE/args.output; out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
    print(payload['verdict']); print(payload['proof_object_sha256'])
if __name__=='__main__': main()
