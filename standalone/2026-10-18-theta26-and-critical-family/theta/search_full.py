#!/usr/bin/env python3
"""Exploratory high-precision moment matching with all dimer coordinates.

The ordinary Decimal search is a producer, never an existence certificate.
It broadens the old ten-coordinate chart to up to forty-six free coordinates.
"""
from pathlib import Path
from decimal import Decimal as D, getcontext
from math import comb
import argparse
import hashlib
import json
import sys
import numpy as np
from scipy.linalg import qr

ROOT = Path(__file__).resolve().parent
SCRATCH = ROOT.parents[1]
from source26 import DEFAULT_SOURCE
SOURCE = DEFAULT_SOURCE
if not SOURCE.exists():
    # Local research staging; installed repository replays use the sibling
    # pinned standalone packet by default.
    SOURCE = SCRATCH / 'riemann_new/strip/inherited'
sys.path.insert(0, str(SOURCE))
from tree_core import Dual, cumulants, unit_cumulants, linear_solve

COUNTS = (256, 10) + (1,)*14
FREE = tuple(i for i in range(48) if i not in (1, 2))


def model(z, degree=22, eta=None):
    zero = z[0]*0
    one = zero+1
    if eta is None:
        eta = one/10**10
    total = [zero for _ in range(degree+1)]
    for i, count in enumerate(COUNTS):
        A, B, p = z[3*i:3*i+3]
        mu = [one]+[(A**n if i == 0 else p*A**n+(one-p)*B**n)
                     * (one if n % 2 == 0 else eta)
                     for n in range(1, degree+1)]
        kap = cumulants(mu)
        total = [x+count*y for x, y in zip(total, kap)]
    conditional = [one]
    for n in range(1, degree+1):
        conditional.append(sum((comb(n-1,j-1)*total[j]*conditional[n-j]
                                for j in range(1,n+1)), zero))
    mu = [v if n % 2 == 0 else zero for n, v in enumerate(conditional)]
    kap = cumulants(mu)
    unit = unit_cumulants(degree)
    return [kap[n]/unit[n] for n in range(2, degree+1, 2)], mu


def jet(z, active=FREE, degree=22):
    dual = [Dual(x, [D(i == j) for j in active]) for i, x in enumerate(z)]
    value, _ = model(dual, degree)
    return [x.v for x in value], [list(x.d) for x in value]


def legal(z):
    return z[0] > 0 and all(z[i] > abs(z[i+1]) and D('.5') < z[i+2] < 1
                           for i in range(3,len(z),3))


def margins(z):
    out = [z[0]] + [D(0)]*47
    for i in range(3,len(z),3):
        A, B, p = z[i:i+3]
        out[i] = (A-abs(B))/2
        out[i+1] = (A-abs(B))/2
        out[i+2] = min(p-D('.5'), 1-p)/2
    return out


def get_target(degree):
    path = ROOT/'theta26_source.json'
    if path.exists():
        record = json.loads(path.read_text())
        scale = D(2)**record['bits']
        return [D(lo+hi)/(2*scale) for lo,hi in record['standardized_cumulant_ratios'][:degree//2]]
    if degree > 22:
        raise ValueError('source26 must complete before a higher-order search')
    old = json.loads((SCRATCH/'riemann_new/strip/theta_source_replay.json').read_text())
    scale = D(2)**old['bits']
    target = [D(lo+hi)/(2*scale) for lo,hi in old['standardized_cumulant_ratios']]
    ext = json.loads((SCRATCH/'riemann_new/strip/field22_dimer_exploration.json').read_text())
    target.append(D(ext['rows'][0]['target22_cumulant_ratio']))
    return target[:degree//2]


def norm(value, target):
    return max(abs((x-y)/y) for x,y in zip(value,target))


def direction(z, jac, residual, active, mode):
    if mode == 'chart':
        return linear_solve(jac, residual)
    scale = [margins(z)[i] for i in active]
    rows = [[x*s for x,s in zip(row,scale)] for row in jac]
    gram = [[sum(x*y for x,y in zip(a,b)) for b in rows] for a in rows]
    lagrange = linear_solve(gram, residual)
    return [s*sum(row[j]*u for row,u in zip(rows,lagrange)) for j,s in enumerate(scale)]


def solve(z, target, active, mode='chart', iterations=50, verbose=True, merit='natural'):
    degree = 2*len(target)
    z = list(z)
    history = []
    for iteration in range(iterations):
        value, jac = jet(z, active, degree)
        old_norm = norm(value,target)
        step = direction(z,jac,[y-x for x,y in zip(value,target)],active,mode)
        scale = [margins(z)[i] for i in active]
        old_natural = max(abs(v/s) for v,s in zip(step,scale))
        damping = D(1)
        while damping > D('1e-15'):
            trial = list(z)
            for i, delta in zip(active,step):
                trial[i] += damping*delta
            if legal(trial):
                trial_value,_ = model(trial,degree)
                new_norm = norm(trial_value,target)
                if merit == 'natural':
                    correction = direction(z,jac,[y-x for x,y in zip(trial_value,target)],active,mode)
                    new_merit = max(abs(v/s) for v,s in zip(correction,scale))
                    accept = new_merit < old_natural
                elif merit == 'domain':
                    accept = True
                else:
                    accept = new_norm < old_norm
                if accept or new_norm < D('1e-75'):
                    break
            damping /= 2
        else:
            return z,False,history,'positive-domain descent line search failed'
        z = trial
        item = {'iteration':iteration, 'residual':str(new_norm), 'damping':str(damping),
                'maximum_step':str(max(abs(damping*v) for v in step))}
        history.append(item)
        if verbose:
            print('NEWTON', iteration, 'RESIDUAL', new_norm, 'DAMPING', damping, flush=True)
        if new_norm < D('1e-75'):
            return z,True,history,'settled'
    return z,False,history,'iteration budget reached'


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--degree',type=int,choices=[22,24,26],default=22)
    p.add_argument('--mode',choices=['charts','full'],default='full')
    p.add_argument('--iterations',type=int,default=40)
    p.add_argument('--merit',choices=['natural','raw','domain'],default='natural')
    p.add_argument('--initial',type=Path)
    p.add_argument('--output',type=Path)
    args = p.parse_args()
    getcontext().prec = 110
    if args.initial:
        data = json.loads(args.initial.read_text())
        z = [D(v) for v in data['parameters']]
    else:
        data = json.loads((SOURCE/'parameters20.json').read_text())
        z = [D(v) for v in data['centers']]
    target = get_target(args.degree)
    records = []
    if args.mode == 'full':
        choices = [('full',FREE)]
    else:
        value,jac = jet(z,FREE,args.degree)
        jacf = np.array([[float(x/t) for x in row] for row,t in zip(jac,target)])
        margin = np.array([float(margins(z)[i]) for i in FREE])
        choices = []
        for power in (0., .5, 1., 1.5):
            matrix = jacf * margin**power
            _,r,piv = qr(matrix,pivoting=True,mode='economic')
            active = tuple(FREE[i] for i in piv[:len(target)])
            if active not in [x[1] for x in choices]:
                choices.append(('chart',active))
            print('QR_CHART',power,active,'CONDITION',np.linalg.cond(matrix[:,piv[:len(target)]]),flush=True)
    for mode,active in choices:
        print('CHART_START',mode,active,flush=True)
        answer,ok,history,reason = solve(z,target,active,mode,args.iterations,merit=args.merit)
        value,_ = model(answer,args.degree)
        record = {'mode':mode,'merit':args.merit,'active':list(active),'settled':ok,'reason':reason,
                  'history':history,'parameters':[str(v) for v in answer],
                  'target':[str(v) for v in target],
                  'residuals':[str(x-y) for x,y in zip(value,target)],
                  'legal':legal(answer)}
        records.append(record)
        output = args.output or ROOT/f'full_search{args.degree}_{args.mode}.json'
        output.write_text(json.dumps({'status':'EMPIRICAL_PRODUCER_NOT_CERTIFICATE',
                                     'degree':args.degree,'precision':110,'records':records},indent=2)+'\n')
        if ok:
            center = ROOT/f'center{args.degree}.json'
            center.write_text(json.dumps(record,indent=2)+'\n')
            print('EMPIRICAL_HIGHER_ORDER_ROOT',args.degree,'CENTER',center,flush=True)
            break


if __name__ == '__main__':
    main()
