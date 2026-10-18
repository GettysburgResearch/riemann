#!/usr/bin/env python3
"""Reduce the unmatched22 coordinate while exactly rebalancing first20.

This producer uses a projected Newton predictor and a full-coordinate
first20 corrector. All arithmetic here is ordinary high-precision Decimal.
"""
from pathlib import Path
from decimal import Decimal as D,getcontext
import argparse,json
import search_full as s
import continue_cycle as c
e=c.e


def main():
    p=argparse.ArgumentParser();p.add_argument('--seed',type=Path,default=s.ROOT/'best_cycle22_seed.json')
    p.add_argument('--iterations',type=int,default=100)
    args=p.parse_args();getcontext().prec=120
    seed=json.loads(args.seed.read_text());z=list(map(D,seed['parameters']));t=D(seed['t'])
    target=s.get_target(26);rows=[];ok=False
    for k in range(args.iterations):
        value,jac=e.jet(z,t,s.FREE)
        residual=value[10]-target[10]
        if abs(residual)<D('1e-80'):
            ok=True;break
        step=s.direction(z,jac,[y-x for x,y in zip(value,target)],s.FREE,'full')
        damping=D(1)
        while damping>D('1e-9'):
            trial=z[:]
            for i,d in zip(s.FREE,step):trial[i]+=damping*d
            if s.legal(trial):
                corrected,balanced,n,error=c.balanced(trial,t,target,3,8,iterations=25)
                if balanced:
                    trialvalue,_=e.evaluate(corrected,t,degree=26)
                    newres=trialvalue[10]-target[10]
                    if abs(newres)<abs(residual):break
            damping/=2
        else:
            print('MANIFOLD_DESCENT_STALLED',k,flush=True);break
        z=corrected
        row={'iteration':k,'damping':str(damping),'r22':str(newres),
             'r24':str(trialvalue[11]-target[11]),'r26':str(trialvalue[12]-target[12]),
             'first20_relative_residual':str(error),'parameters':[str(x)for x in z]}
        rows.append(row)
        out={'status':'EMPIRICAL_MANIFOLD_OPTIMIZATION_NOT_CERTIFICATE','t':str(t),'rows':rows}
        (s.ROOT/'cycle_manifold22.json').write_text(json.dumps(out,indent=2)+'\n')
        print('MANIFOLD22',k,'R22',newres,'DAMPING',damping,flush=True)
    value,_=e.evaluate(z,t,degree=26)
    center={'status':'EMPIRICAL_ROOT_PRODUCER_NOT_CERTIFICATE','settled':ok,
            'left':3,'right':8,'t':str(t),'parameters':[str(x)for x in z],
            'residuals':[str(x-y)for x,y in zip(value,target)]}
    (s.ROOT/'cycle22_manifold_center.json').write_text(json.dumps(center,indent=2)+'\n')
    print('MANIFOLD22_END',ok,'R22',value[10]-target[10],flush=True)


if __name__=='__main__':main()
