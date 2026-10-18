#!/usr/bin/env python3
"""Ordinary-Decimal collision continuation; this is not a root certificate.

Two selected b nodes are represented by u=(b1+b2)/2 and
d=(b1-b2)^2/4.  Negative d means a conjugate pair.  The full pair power
sum is polynomial in (u,d), so no branch or state is discarded.
"""
from decimal import Decimal as D, getcontext
from pathlib import Path
from math import comb
import argparse
import json

ROOT = Path(__file__).resolve().parent
from power_source import targets
from exact_polynomial import linear_solve


def pair_power(u, d, r):
    return 2 * sum((D(comb(r, 2*k)) * u**(r-2*k) * d**k
                    for k in range(r//2+1)), D(0))


def pair_jet(u, d, r):
    du = 2 * sum((D(comb(r, 2*k)*(r-2*k)) * u**(r-2*k-1) * d**k
                  for k in range((r-1)//2+1)), D(0))
    dd = 2 * sum((D(comb(r, 2*k)*k) * u**(r-2*k) * d**(k-1)
                  for k in range(1, r//2+1)), D(0))
    return du, dd


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--cloud', type=int, default=4)
    ap.add_argument('--band', default='0.33333333333333333333333333333333333333333333333333')
    args = ap.parse_args()
    getcontext().prec = 150
    L = args.cloud
    seed_file = ROOT / f'power_extension_22_64_cloud{L}_switch.json'
    seed = json.loads(seed_file.read_text())
    original = json.loads((ROOT.parent/'gaussian_parameters.json').read_text())
    record = next(q for q in original['models'] if q['degree']==22 and q['nodes']==64)
    b = list(map(D, record['centers']))
    for row in seed['rows']:
        for i, v in zip(row['active'], row['beta']):
            b[i] = D(v)
    last = seed['rows'][-1]
    active = last['active'][:]
    pair = min(((i, j) for i in active for j in active if i<j),
               key=lambda ij: abs(b[ij[0]]-b[ij[1]])/(b[ij[0]]+b[ij[1]]))
    others = [i for i in active if i not in pair]
    passive = [v for i, v in enumerate(b) if i not in active]
    goal = targets(24)
    m = 10
    pp = [sum((q**r for q in passive), D(0)) for r in range(2, m+3)]
    u = (b[pair[0]]+b[pair[1]])/2
    d = ((b[pair[0]]-b[pair[1]])/2)**2
    y = [b[i] for i in others]+[u,d]
    x = D(last['x'])
    source = json.loads((ROOT.parent/'theta26_source.json').read_text())
    variance = D(sum(source['variance']))/(D(2)**(source['bits']+1))
    band_limit = D(args.band)

    def values(y, x):
        return [pp[r-2]+sum((q**r for q in y[:-2]), D(0))+
                pair_power(y[-2],y[-1],r)+L*x**r for r in range(2,m+3)]

    def jacobian(y):
        return [[r*q**(r-1) for q in y[:-2]]+list(pair_jet(y[-2],y[-1],r))
                for r in range(2,m+2)]

    def physical_band(y):
        u,d=y[-2:]
        if d>=0:return D(0)
        p=u*u-d
        return ((p.sqrt()-u)/(2*p*variance)).sqrt()

    def legal(y,x,gate=True):
        u,d=y[-2:]
        return (min(y[:-2])>x>0 and u>x and u*u>d and
                (not gate or physical_band(y)<band_limit))

    def balance(y,x):
        y=y[:]
        for it in range(25):
            val=values(y,x)[:m]
            error=max(abs((u-v)/v) for u,v in zip(val,goal))
            if error<D('1e-120'):return y
            J=jacobian(y)
            correction=linear_solve(J,[goal[i]-val[i] for i in range(m)])
            scales=[max(abs(q),D('1e-4')) for q in y[:-1]]+[max(y[-2]**2,D('1e-10'))]
            norm=sum((v/s)**2 for v,s in zip(correction,scales))
            damping=D(1)
            while damping>D('1e-18'):
                trial=[q+damping*v for q,v in zip(y,correction)]
                if legal(trial,x):
                    vt=values(trial,x)[:m]
                    ct=linear_solve(J,[goal[i]-vt[i] for i in range(m)])
                    if sum((v/s)**2 for v,s in zip(ct,scales)) <= (1-damping/4)*norm:
                        break
                damping/=2
            else:return None
            y=trial
        return None

    y=balance(y,x)
    if y is None:raise ArithmeticError('initial balance failed')
    step=x/40
    rows=[]
    crossed=False
    for it in range(250):
        val=values(y,x);u,d=y[-2:]
        a=D('.5')-sum(passive)-sum(y[:-2])-2*u-L*x
        band=physical_band(y)
        residual=val[-1]-goal[-1]
        row={'x':str(x),'y':[str(q) for q in y],'next_residual':str(residual),
             'a':str(a),'physical_band':str(band),'pair_d':str(d),
             'absolute_square_budget':str(val[0]+4*max(D(0),-d)),
             'relative_preserved_power_error':str(max(abs((q-v)/v) for q,v in zip(val[:m],goal)))}
        rows.append(row)
        print('PAIR',L,'X',f'{x:.12f}','D',f'{d:.5E}','BAND',f'{band:.7f}',
              'RESIDUAL',f'{residual:.12E}',flush=True)
        if residual>=0:
            crossed=True
            break
        while step>D('1e-17'):
            tx=x+step
            trial=balance(y,tx)
            if trial is not None:
                x,y=tx,trial
                step*=D('1.2')
                break
            step/=2
        else:break
    result={'status':'ORDINARY_DECIMAL_PRODUCER_NOT_CERTIFICATE',
            'seed':seed_file.name,'cloud':L,'pair_indices':pair,'other_active_indices':others,
            'passive_nodes':[str(q) for q in passive], 'physical_band_limit':str(band_limit),
            'crossed_next_power_target':crossed,'rows':rows}
    suffix='third' if band_limit<D('.334') else str(band_limit).replace('.','p')
    (ROOT/f'conjugate_pair_cloud{L}_band{suffix}.json').write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':
    main()
