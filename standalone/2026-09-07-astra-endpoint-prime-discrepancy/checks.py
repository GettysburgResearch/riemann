#!/usr/bin/env python3
"""Bounded exact algebra controls only; not an analytic RH proof."""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import argparse
import json
import sys


def add(a, b):
    out = [F(0)] * max(len(a), len(b))
    for i, x in enumerate(a): out[i] += x
    for i, x in enumerate(b): out[i] += x
    return out


def scale(a, c): return [F(c) * x for x in a]


def mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): out[i+j] += x*y
    return out


def power(a, n):
    out = [F(1)]
    for _ in range(n): out = mul(out, a)
    return out


def derivative(a): return [i*a[i] for i in range(1,len(a))] or [F(0)]


def value(a, x):
    out = F(0)
    for c in reversed(a): out = out*x+c
    return out


def integral(a, lo, hi):
    return sum((c*(hi**(i+1)-lo**(i+1))/F(i+1) for i,c in enumerate(a)), F(0))


def strict_load(path):
    def pairs(items):
        out = {}
        for k,v in items:
            if k in out: raise ValueError('duplicate JSON key')
            out[k] = v
        return out
    return json.loads(Path(path).read_text(), object_pairs_hook=pairs,
                      parse_float=lambda _: (_ for _ in ()).throw(ValueError('float forbidden')),
                      parse_constant=lambda _: (_ for _ in ()).throw(ValueError('constant forbidden')))


def run():
    groups = []
    count = 0
    def need(ok, reason):
        nonlocal count
        count += 1
        if not ok: raise ValueError(reason)
    def finish(name, start): groups.append({'name':name, 'cases':count-start})
    # Integrate each entire polynomial piece; these are exact coefficients,
    # not a grid used as a stand-in for an interval theorem.
    start=count
    t=[F(0),F(1)]
    lower_cut=add(scale(power([F(-1),F(3)],2),3),scale(power([F(-1),F(3)],3),-2))
    lower=scale(mul(t,lower_cut),-2)
    lower2=derivative(derivative(lower))
    lower_norm=integral(power(add(lower,scale(lower2,-1)),2),F(1,3),F(2,3))
    upper_cut=add(add([F(1)],scale(power([F(-1),F(1)],2),-3)),scale(power([F(-1),F(1)],3),2))
    a=scale(mul(t,upper_cut),-2); a2=derivative(derivative(a))
    ua=integral(mul(a,a),F(1),F(2))
    ub=integral(scale(mul(a,a2),-2),F(1),F(2))
    uc=integral(mul(a2,a2),F(1),F(2))
    need(lower_norm==F(463994,1215),'lower multiplier norm')
    need((ua,ub,uc)==(F(722,315),F(768,35),F(624,5)),'upper multiplier coefficients')
    need(lower_norm-F(32,81)==F(463514,1215),'middle interval endpoint')
    total_at_one=ua+F(4,3)+ub+lower_norm-F(32,81)+uc
    need(total_at_one==F(904696,1701),'complete multiplier norm')
    need(total_at_one<F(576),'uniform 24 squared bound')
    finish('full_multiplier_polynomial_integrations',start)
    start=count
    need(value(lower,F(1,3))==0 and value(derivative(lower),F(1,3))==0,'lower start C1')
    need(value(lower,F(2,3))==F(-4,3) and value(derivative(lower),F(2,3))==-2,'lower end C1')
    need(value(a,F(1))==-2 and value(derivative(a),F(1))==-2,'upper start C1')
    need(value(a,F(2))==0 and value(derivative(a),F(2))==0,'upper end C1')
    for lam in (F(1),F(3,2),F(2),F(7,3),F(4),F(10),F(64)):
        exact=lower_norm+F(4,3)*(lam**3-F(8,27))+ua*lam**3+ub*lam+uc/lam
        formula=F(1142,315)*lam**3+F(768,35)*lam+F(463514,1215)+F(624,5)/lam
        need(exact==formula and exact<576*lam**3,'parameter reconstruction')
    need(F(3)<F(7,4)**2,'sqrt3 rational upper bound')
    need(F(7,16)*29<13 and F(7,16)*2<1,'stable remainder cost')
    finish('joins_and_bound_constants',start)
    start=count
    # Kernel factorization for arbitrary rational signed atoms at log n.
    # This verifies the actual Cauchy kernel, not independent prime phases.
    def quadratic(nodes, weights):
        return sum((weights[i]*weights[j]*(F(min(m,n),max(m,n))+F(1,m*n))/2
                    for i,m in enumerate(nodes) for j,n in enumerate(nodes)),F(0))
    def tail_square(nodes, weights):
        z=sum((c/F(n) for n,c in zip(nodes,weights)),F(0))
        out=z*z; left=F(1)
        for i,right in enumerate(nodes):
            tail=sum((c/F(n) for n,c in zip(nodes[i:],weights[i:])),F(0))
            out+=(F(right)**2-left**2)*tail**2/2
            left=F(right)
        return out
    cases=[([2],[F(1)]),([2,3,5],[F(1),F(-2),F(3,7)]),
           ([2,4,8,16],[F(-1),F(2),F(-3),F(4)]),
           ([11,12,13],[F(1),F(-2),F(1)])]
    for k in range(1,13):
        cases.append((list(range(2,k+2)),[F((-1)**j*(j+1),j+2) for j in range(k)]))
    for nodes,weights in cases:
        need(quadratic(nodes,weights)==tail_square(nodes,weights)>0,'signed tail factorization')
    need(quadratic([2],[F(0)])==tail_square([2],[F(0)])==0,'zero signed measure')
    need(quadratic([2],[F(1)])/2==F(5,16),'actual X=2 amplitude square')
    # Explicit cross term is nonzero. A diagonal-only replacement must fail.
    full=quadratic([2,3],[F(1),F(1)])
    diag=quadratic([2],[F(1)])+quadratic([3],[F(1)])
    need(full-diag==F(5,6),'ordered cross-term contribution')
    finish('complete_signed_physical_gram',start)
    start=count
    def lag(n): return [F((-1)**k*comb(n,k),factorial(k)) for k in range(n+1)]
    for i in range(8):
        for j in range(8):
            p=mul(lag(i),lag(j))
            norm=sum((c*factorial(k) for k,c in enumerate(p)),F(0))
            need(norm==int(i==j),'Laguerre normalization')
    for m in range(1,9):
        p=lag(m-1)
        need(p[-1]*((-1)**(m-1))*factorial(m-1)==1,'top jet sign')
    finish('multiplicity_jet_normalizations',start)
    start=count
    for beta in (F(3,5),F(2,3),F(3,4),F(4,5),F(9,10)):
        v=(1/(2*beta-1)-2/(beta+F(1,2))+F(1,2))/(F(3,2)-beta)**2
        need(v==2/(4*beta**2-1)>0,'continuous control asymptotic coefficient')
    need(2/(4*F(3,4)**2-1)==F(8,5),'beta three-quarter coefficient')
    finish('synthetic_continuous_control',start)
    return {'status':'PASS_BOUNDED_EXACT_CONTROLS','rh_proved':False,
            'arithmetic_class':'EXACT_RATIONAL','groups':groups,'total_cases':count,
            'multiplier_square_at_one':str(total_at_one),
            'q_at_two':str(F(5,16)),
            'scope':'Finite algebra only. No actual all-cutoff entropy, prime-error norm, or analytic theorem is computed.'}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--expect',type=Path)
    args=parser.parse_args()
    result=run()
    if args.expect is not None:
        expected=strict_load(args.expect)
        if json.dumps(expected,sort_keys=True)!=json.dumps(result,sort_keys=True):
            raise ValueError('retained result differs from exact reconstruction')
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__':
    try: main()
    except Exception as exc:
        print('REJECT: '+str(exc),file=sys.stderr)
        sys.exit(1)
