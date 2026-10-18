#!/usr/bin/env python3
"""Complete finite-model continuation after adding a ferromagnetic cross edge.

The source graph is a hidden hub tree.  The added edge creates a cycle.
All 2^305 configurations are retained exactly through conditional polynomial
moments and the identity dP_t/dP_0=(1+t sigma_u sigma_v)/(1+t E_0 sigma_u sigma_v).
"""
from decimal import Decimal as D,getcontext
from math import comb
from pathlib import Path
import argparse
import json
import sys
ROOT=Path(__file__).resolve().parent
SOURCE=ROOT.parent/'inherited'
import exact_polynomial as tree_core

def quotient(a,b):
    if hasattr(b,'d'):
        return type(b)(a.v/b.v,[(x*b.v-a.v*y)/(b.v*b.v) for x,y in zip(a.d,b.d)])
    return a/b

def exp_moments(kap):
    zero=kap[0]*0;one=zero+1;mu=[one]
    for n in range(1,len(kap)):
        mu.append(sum((comb(n-1,j-1)*kap[j]*mu[n-j]
                       for j in range(1,n+1)),zero))
    return mu

def convolve(a,b):
    zero=a[0]*0
    return [sum((comb(n,j)*a[j]*b[n-j] for j in range(n+1)),zero)
            for n in range(len(a))]

def evaluate(z,t,degree=22,left=3,right=8):
    zero=z[0]*0;one=zero+1;eta=one/10**10
    counts=(256,10)+(1,)*14;caps=[];total=[zero]*(degree+1);mixed=[]
    for i,count in enumerate(counts):
        A,B,p=z[3*i:3*i+3]
        mu=[one]+[(A**n if i==0 else p*A**n+(one-p)*B**n)
                         *(one if n%2==0 else eta) for n in range(1,degree+1)]
        cap=tree_core.cumulants(mu);caps.append(cap)
        total=[a+count*b for a,b in zip(total,cap)]
        if i in (left,right):
            mixed.append([(A**j if i==0 else p*A**j+(one-p)*B**j)
                          *(eta if j%2==0 else one) for j in range(degree+1)])
    base=exp_moments(total)
    excluded=exp_moments([a-b-c for a,b,c in zip(total,caps[left],caps[right])])
    joint=convolve(excluded,convolve(*mixed))
    denominator=one+t*eta*eta
    mu=[quotient(base[n]+t*joint[n],denominator) if n%2==0 else zero
        for n in range(degree+1)]
    kappa=tree_core.cumulants(mu);unit=tree_core.unit_cumulants(degree)
    return [kappa[n]/unit[n] for n in range(2,degree+1,2)],mu

def jet(z,t,active,degree=22,**kwargs):
    dim=len(active);zero=z[0]*0;one=zero+1
    extended=z+[t]
    dual=[tree_core.Dual(x,[one if i==j else zero for j in active])
          for i,x in enumerate(extended)]
    values,mu=evaluate(dual[:-1],dual[-1],degree,**kwargs)
    return [x.v for x in values],[list(x.d) for x in values]

def legal(z,t):
    return z[0]>0 and 0<=t<1 and all(z[i]>abs(z[i+1]) and D('.5')<z[i+2]<1
                                      for i in range(3,len(z),3))

def targets(source=SOURCE):
    src=json.loads((source.parent/'theta_source_replay.json').read_text())
    unit=tree_core.unit_cumulants(22)
    # This source replay uses 320 fractional bits.
    mu=[D(sum(pair))/D(2*(1<<320)) for pair in src['standardized_moments']]
    kap=tree_core.cumulants(mu)
    target=[kap[2*j]/unit[2*j] for j in range(1,11)]
    source22=json.loads((source.parent/'field22_dimer_exploration.json').read_text())
    target.append(D(source22['rows'][0]['target22_cumulant_ratio']))
    return target

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--left',type=int,default=3)
    parser.add_argument('--right',type=int,default=8)
    parser.add_argument('--full',action='store_true')
    parser.add_argument('--source',type=Path,default=SOURCE)
    args=parser.parse_args()
    global_source=args.source
    getcontext().prec=100;data=json.loads((global_source/'parameters20.json').read_text())
    z=[D(x) for x in data['centers']];active=data['active'];target=targets(global_source)
    points=['0','0.00001','0.0001','0.001','0.005','0.01','0.02','0.03','0.04','0.05','0.06','0.08','0.1']
    rows=[];status='COMPLETED'
    for text in points:
        t=D(text);success=False
        for iteration in range(25):
            value,jac=jet(z,t,active,left=args.left,right=args.right)
            olderr=max(abs((value[i]-target[i])/target[i]) for i in range(10))
            if olderr<D('1e-70'):success=True;break
            step=tree_core.linear_solve(jac[:10],[target[i]-value[i] for i in range(10)])
            damping=D(1)
            while damping>D('1e-16'):
                trial=z[:]
                for i,d in zip(active,step):trial[i]+=damping*d
                if legal(trial,t):
                    val,_=evaluate(trial,t,left=args.left,right=args.right)
                    error=max(abs((val[i]-target[i])/target[i]) for i in range(10))
                    if error<olderr:break
                damping/=2
            else:break
            z=trial
        value,_=evaluate(z,t,left=args.left,right=args.right)
        record={'tanh_added_coupling':str(t),'converged':success,'iterations':iteration,
                'max_relative_first20_residual':str(max(abs((value[i]-target[i])/target[i]) for i in range(10))),
                'order22_residual':str(value[10]-target[10]),'parameters':[str(x) for x in z],
                'legal_positive_model':legal(z,t)}
        rows.append(record);print(text,success,'R22',record['order22_residual'],
                                  'R20',record['max_relative_first20_residual'],flush=True)
        if not success:status='CHART_CONTINUATION_FAILED';break
    output={'status':'EMPIRICAL_'+status,'left_root_block':args.left,'right_root_block':args.right,
            'precision':100,'active':active,'rows':rows,
            'claim_limit':'No root or infeasibility conclusion from ordinary Decimal arithmetic.'}
    (ROOT/f'added_edge_{args.left}_{args.right}_exploration.json').write_text(json.dumps(output,indent=2)+'\n')

if __name__=='__main__':main()
