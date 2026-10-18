"""Independent exact generating-product and Jacobian check for the T20 tree.

The alternative path multiplies truncated exponential generating polynomials,
uses their formal logarithm and reciprocal, and differentiates the product
directly. It does not use the author's cumulant or automatic-differentiation
implementation to construct the expected values. This validates the finite
map and all 100 Jacobian entries at the rational center, not a root or an
infinite theta tail.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import argparse
import hashlib
import json
import sys

DEGREE = 20
ZERO = [F(0)] * (DEGREE + 1)
ONE = [F(1)] + [F(0)] * DEGREE

def multiply(a, b):
    return [sum((a[j] * b[k-j] for j in range(k+1)), F(0))
            for k in range(DEGREE+1)]

def power(a, n):
    out = ONE[:]
    while n:
        if n % 2:
            out = multiply(out, a)
        n //= 2
        if n:
            a = multiply(a, a)
    return out

def reciprocal(a):
    if a[0] != 1:
        raise ValueError('unit constant required')
    out = [F(1)]
    for k in range(1, DEGREE+1):
        out.append(-sum((a[j]*out[k-j] for j in range(1,k+1)), F(0)))
    return out

def logarithm(a):
    if a[0] != 1:
        raise ValueError('unit constant required')
    t = a[:]
    t[0] = F(0)
    pp = ONE[:]
    out = ZERO[:]
    for j in range(1, DEGREE+1):
        pp = multiply(pp, t)
        factor = F((-1)**(j+1), j)
        out = [x+factor*y for x,y in zip(out,pp)]
    return out

def main(directory, mutation=None):
    sys.path.insert(0, str(directory))
    from connected_blocks import jet
    data = json.loads((directory/'parameters20.json').read_text())
    z = [F(v) for v in data['centers']]
    counts = [256,10] + [1]*14
    active = [6,0,15,21,3,27,9,12,4,42]
    if data['counts'] != counts or data['active'] != active:
        raise ValueError('independently specified complete graph')
    eta = F(1,10**10)
    if mutation == 'erase_hub':
        eta = F(0)
    bases = []
    factors = []
    for i,count in enumerate(counts):
        A,B,p = z[3*i:3*i+3]
        base = [F(1)]
        for n in range(1,DEGREE+1):
            moment = A**n if i == 0 else p*A**n+(1-p)*B**n
            base.append(moment*(eta if n%2 else 1)/factorial(n))
        bases.append(base)
        factors.append(power(base,count))
    prefix = [ONE[:]]
    for factor in factors:
        prefix.append(multiply(prefix[-1],factor))
    suffix = [None]*(len(factors)+1)
    suffix[-1] = ONE[:]
    for i in range(len(factors)-1,-1,-1):
        suffix[i] = multiply(factors[i],suffix[i+1])
    distribution = [v if n%2 == 0 else F(0) for n,v in enumerate(prefix[-1])]
    log_distribution = logarithm(distribution)
    unit_log = logarithm([F(int(n%2 == 0),factorial(n)) for n in range(DEGREE+1)])
    values = [log_distribution[n]/unit_log[n] for n in range(2,DEGREE+1,2)]
    inv = reciprocal(distribution)
    columns = []
    for coordinate in active:
        i,k = divmod(coordinate,3)
        A,B,p = z[3*i:3*i+3]
        derivative = [F(0)]
        for n in range(1,DEGREE+1):
            if k == 0:
                d = n*A**(n-1)*(1 if i == 0 else p)
            elif k == 1:
                d = n*B**(n-1)*(1-p)
            else:
                d = A**n-B**n
            derivative.append(d*(eta if n%2 else 1)/factorial(n))
        db = multiply(power(bases[i],counts[i]-1),derivative)
        dp = multiply(multiply(prefix[i],db),suffix[i+1])
        dp = [counts[i]*v if n%2 == 0 else F(0) for n,v in enumerate(dp)]
        dlog = multiply(dp,inv)
        columns.append([dlog[n]/unit_log[n] for n in range(2,DEGREE+1,2)])
    if mutation == 'permute_derivative':
        columns[0],columns[1] = columns[1],columns[0]
    actual_values,actual_jacobian,actual_raw = jet(z,active)
    raw = [v*factorial(n) for n,v in enumerate(distribution)]
    if raw != actual_raw or values != actual_values:
        raise ValueError('independent full graph moment map')
    if any(columns[j][i] != actual_jacobian[i][j] for i in range(10) for j in range(10)):
        raise ValueError('independent complete Jacobian')
    if mutation is not None:
        raise ValueError('mutation unexpectedly accepted')
    return {'status':'PASS','arithmetic':'exact Fraction',
            'vertices':305,'raw_orders':list(range(21)),
            'cumulant_orders':list(range(2,21,2)),
            'jacobian_entries_compared':100,'active_coordinates':active,
            'method':'direct generating product, formal logarithm, product derivative and formal reciprocal',
            'scope':'finite rational-center map and Jacobian; no root or source-tail assertion',
            'input_hashes':{name:hashlib.sha256((directory/name).read_bytes()).hexdigest()
                            for name in ['parameters20.json','connected_blocks.py','tree_core.py']}}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--theta-dir',type=Path,default=Path(__file__).resolve().parent.parent/'theta')
    parser.add_argument('--mutation',choices=['erase_hub','permute_derivative'])
    args = parser.parse_args()
    print(json.dumps(main(args.theta_dir.resolve(),args.mutation),sort_keys=True,indent=2))
