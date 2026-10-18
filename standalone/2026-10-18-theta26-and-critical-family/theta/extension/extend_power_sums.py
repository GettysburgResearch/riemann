#!/usr/bin/env python3
"""Ordinary-Decimal continuation adding a cloud of equal new real-root factors.

The exact monotonicity theorem is in POWER_SUM_EXTENSION.md.  This program is a
producer only; its final centers need a separate directed certificate.
"""
from decimal import Decimal as D,getcontext
from pathlib import Path
from math import factorial
import argparse
import json
import numpy as np
from scipy.linalg import qr
ROOT=Path(__file__).resolve().parent
from power_source import targets
from exact_polynomial import linear_solve

def power(b,m):return [sum((x**r for x in b),D(0)) for r in range(2,m+2)]

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--degree',type=int,default=22)
    parser.add_argument('--nodes',type=int,default=64);parser.add_argument('--cloud',type=int,default=1)
    parser.add_argument('--switch-anchors',action='store_true')
    parser.add_argument('--max-switches',type=int,default=30)
    parser.add_argument('--parameters',type=Path,default=ROOT.parent/'gaussian_parameters.json')
    parser.add_argument('--output',type=Path)
    args=parser.parse_args();getcontext().prec=150
    if args.cloud<1 or args.max_switches<0:raise ValueError('positive integer cloud and nonnegative switch limit required')
    data=json.loads(args.parameters.read_text())
    record=next(row for row in data['models'] if row['degree']==args.degree and row['nodes']==args.nodes)
    b=[D(s) for s in record.get('centers',record.get('b'))];m=args.degree//2-1;goal=targets(args.degree+2);L=args.cloud
    matrix=np.array([[float(r*x**r/goal[r-2]) for x in b] for r in range(2,m+2)])
    _,_,pivot=qr(matrix,pivoting=True,mode='economic');active=sorted(map(int,pivot[:m]),key=lambda i:b[i])
    passive=[x for i,x in enumerate(b) if i not in active]
    beta=[b[i] for i in active];oldbeta=beta[:];x=D(0)
    passive_powers=power(passive,m+1)
    oldnext=sum((v**(m+2) for v in b),D(0));delta=goal[m]-oldnext
    rows=[];best=None

    def balance(start,x):
        beta=start[:]
        for iteration in range(20):
            value=[passive_powers[r-2]+sum((q**r for q in beta),D(0))+L*x**r
                   for r in range(2,m+2)]
            err=max(abs((a-c)/c) for a,c in zip(value,goal))
            if err<D('1e-120'):return beta
            J=[[r*q**(r-1) for q in beta] for r in range(2,m+2)]
            step=linear_solve(J,[goal[i]-value[i] for i in range(m)])
            norm=sum((s*s for s in step),D(0));damping=D(1)
            while damping>D('1e-18'):
                trial=[a+damping*s for a,s in zip(beta,step)]
                if x<min(trial) and all(trial[i]<trial[i+1] for i in range(m-1)):
                    val=[passive_powers[r-2]+sum((q**r for q in trial),D(0))+L*x**r
                         for r in range(2,m+2)]
                    correction=linear_solve(J,[goal[i]-val[i] for i in range(m)])
                    if sum((s*s for s in correction),D(0))<=(1-damping/4)*norm:break
                damping/=2
            else:return None
            beta=trial
        return None

    beta=balance(beta,x)
    if beta is None:raise ArithmeticError('starting moment balance failed')
    step=min(beta)/20
    print('POWER_EXTENSION',args.degree,args.nodes,L,'DELTA',delta,flush=True)
    sign=D((-1)**m);crossed=False
    switches=0
    for it in range(30+args.max_switches*30):
        nextpower=passive_powers[m]+sum((q**(m+2) for q in beta),D(0))+L*x**(m+2)
        residual=nextpower-goal[m];a=D('.5')-sum(passive)-sum(beta)-L*x
        row={'x':str(x),'a':str(a),'next_residual':str(residual),'beta':[str(q) for q in beta],
             'active':active[:]}
        rows.append(row);print('X',f'{x:.9f}','NEXT_RESIDUAL',f'{residual:.12E}','A',f'{a:.9f}',flush=True)
        if sign*residual>=0:crossed=True;break
        previous=(x,beta[:],residual)
        while step>D('1e-12'):
            trialx=x+step
            # Canonical-factor normality only uses the fixed second power sum.
            # A negative Gaussian coefficient is therefore permitted.
            trial=balance(beta,trialx)
            if trial is not None:
                x,beta=trialx,trial;step*=D('1.15');break
            step/=2
        else:
            if not args.switch_anchors or switches>=args.max_switches:break
            for index,new in zip(active,beta):b[index]=new
            eligible=[i for i,q in enumerate(b) if q>x*D('1.25')]
            if len(eligible)<m:break
            matrix=np.array([[float(r*b[i]**r/goal[r-2]) for i in eligible]
                             for r in range(2,m+2)])
            _,_,pivot=qr(matrix,pivoting=True,mode='economic')
            newactive=sorted((eligible[int(p)] for p in pivot[:m]),key=lambda i:b[i])
            if newactive==active:break
            active=newactive;passive=[q for i,q in enumerate(b) if i not in active]
            passive_powers=power(passive,m+1);beta=[b[i] for i in active]
            beta=balance(beta,x)
            if beta is None:raise ArithmeticError('anchor-switch balance failed')
            step=(min(beta)-x)/20;switches+=1
            print('ANCHOR_SWITCH',switches,active,flush=True)
    if crossed:
        # Safeguarded square Newton refinement of all m+1 matched powers.
        # Raw square steps can diverge near a chart collision.
        y=beta+[x]
        upper_node_limit=2*max(y)
        for iteration in range(100):
            vals=[passive_powers[r-2]+sum((q**r for q in y[:-1]),D(0))+L*y[-1]**r
                  for r in range(2,m+3)]
            err=max(abs((u-v)/v) for u,v in zip(vals,goal))
            if err<D('1e-125'):break
            J=[[r*q**(r-1) for q in y[:-1]]+[L*r*y[-1]**(r-1)] for r in range(2,m+3)]
            step=linear_solve(J,[v-u for u,v in zip(vals,goal)])
            norm=sum((v/u)**2 for u,v in zip(y,step))
            damping=D(1)
            while damping>D('1e-40'):
                trial=[u+damping*v for u,v in zip(y,step)]
                if 0<min(trial) and max(trial)<upper_node_limit and trial[-1]<min(trial[:-1]):
                    vt=[passive_powers[r-2]+sum((q**r for q in trial[:-1]),D(0))+L*trial[-1]**r
                        for r in range(2,m+3)]
                    ct=linear_solve(J,[v-u for u,v in zip(vt,goal)])
                    if sum((v/u)**2 for u,v in zip(y,ct))<=(1-damping/4)*norm:break
                damping/=2
            else:raise ArithmeticError('safeguarded endpoint refinement failed; no endpoint certificate produced')
            y=trial
        else:raise ArithmeticError('endpoint refinement iteration limit; no endpoint certificate produced')
        beta,x=y[:-1],y[-1]
        for index,new in zip(active,beta):b[index]=new
        b.extend([x]*L)
        reserve=D('.5')-sum(b)
        final={'b':[str(q) for q in b],'a':str(reserve),'active_old_indices':active,
               'shared_new_node':str(x),'new_node_multiplicity':L,'relative_power_error':str(err),
               'all_nodes_positive':min(b)>0,'reserve_positive':reserve>0,
               'new_node_below_selected_anchors':0<x<min(beta)}
        print('EXTENSION_REFINED',len(b),args.degree+2,'ERROR',err,flush=True)
    else:final=None
    result={'status':'EMPIRICAL_EXTENSION_PRODUCER_NOT_CERTIFICATE','input_degree':args.degree,
            'input_nodes':args.nodes,'cloud':L,'active':active,'target_next_delta':str(delta),
            'direction_sign':int(sign),'crossed':crossed,'rows':rows,'final':final}
    result['anchor_switches']=switches
    result['maximum_anchor_switches']=args.max_switches
    suffix='_switch' if args.switch_anchors else ''
    output=args.output or ROOT/f'power_extension_{args.degree}_{args.nodes}_cloud{L}{suffix}.json'
    output.write_text(json.dumps(result,indent=2)+'\n')

if __name__=='__main__':main()
