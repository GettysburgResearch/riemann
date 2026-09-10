#!/usr/bin/env python3
"""Exact finite arithmetic for THA26. This is NOT an RH proof or zero producer.

Only standard-library integer/Fraction operations enter the mathematical checks.
Imported ordinate intervals are authenticated, not independently regenerated.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import comb, factorial, prod
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
INPUT_SHA256 = 'cadf56ddcaf85c0c42138c707cae7141c6270eb1c20c3b1abfc8709508e6e825'


def need(condition, message):
    if not condition:
        raise ValueError(message)


def unique_pairs(items):
    out = {}
    for k, v in items:
        need(k not in out, 'duplicate JSON key: ' + k)
        out[k] = v
    return out


def forbidden_number(x):
    raise ValueError('floating/nonfinite JSON number: ' + x)


def load_json(raw):
    return json.loads(raw, object_pairs_hook=unique_pairs,
                      parse_float=forbidden_number, parse_constant=forbidden_number)


def equal_typed(a, b):
    if type(a) is not type(b):
        return False
    if type(a) is dict:
        return a.keys() == b.keys() and all(equal_typed(a[k], b[k]) for k in a)
    if type(a) is list:
        return len(a) == len(b) and all(equal_typed(x, y) for x, y in zip(a, b))
    return a == b


def regular_bytes(path):
    p = Path(path)
    for item in [p] + list(p.parents):
        need(not item.is_symlink(), 'symlink input')
    need(p.is_file(), 'missing regular input')
    return p.read_bytes()


def pair(x):
    x = Q(x)
    return [x.numerator, x.denominator]


def enclosure(x, places=30):
    unit = 10 ** places
    n = x.numerator * unit // x.denominator
    lo, hi = Q(n, unit), Q(n + 1, unit)
    need(lo <= x <= hi, 'outward rational enclosure')
    return [pair(lo), pair(hi)]


def log_near(x, terms=64):
    """For 1<=x<=2: log x=2 atanh((x-1)/(x+1)), positive remainder."""
    x = Q(x)
    need(1 <= x <= 2, 'range-reduced logarithm domain')
    y = (x - 1) / (x + 1)
    low = 2 * sum((y ** (2*j+1) / (2*j+1) for j in range(terms)), Q(0))
    error = 2*y**(2*terms+1)/((2*terms+1)*(1-y*y))
    return low, low + error


def log_bound(x):
    x = Q(x)
    need(x >= 1, 'positive logarithm domain')
    k = 0
    while x >= 2:
        x /= 2
        k += 1
    lo, hi = log_near(x)
    l2, u2 = log_near(Q(2))
    return lo + k*l2, hi + k*u2


def atan_bound(x, terms=40):
    x = Q(x)
    need(0 < x < 1 and terms > 0, 'arctangent domain')
    s = sum(((-1)**j * x**(2*j+1)/(2*j+1) for j in range(terms)), Q(0))
    t = s + (-1)**terms*x**(2*terms+1)/(2*terms+1)
    return min(s, t), max(s, t)


def interpolation_budget(intervals, radius, mass, shift):
    """Uniform exact upper bound from all selected interpolation factors."""
    need(type(shift) is int and shift >= 1, 'integer positive shift')
    need(radius > 0 and mass >= 0 and len(intervals) > 0, 'tail data')
    L = []
    for j, (lo, hi) in enumerate(intervals):
        need(0 < radius < lo <= hi, 'node/tail separation')
        factors = []
        for k, (lk, uk) in enumerate(intervals):
            if j == k:
                continue
            sep = lo - uk if j < k else lk - hi
            need(sep > 0, 'overlapping/unordered head intervals')
            factors.append((uk + radius) / sep)
        L.append(prod(factors, start=Q(1)))
    budget = mass*radius**(shift-1)*sum((a*a/intervals[j][0]**shift for j, a in enumerate(L)), Q(0))
    return budget, L


def determinant(a):
    a = [list(map(Q, row)) for row in a]
    n = len(a)
    need(all(len(row) == n for row in a), 'square matrix')
    ans = Q(1)
    for k in range(n):
        i = next((i for i in range(k, n) if a[i][k]), None)
        if i is None:
            return Q(0)
        if i != k:
            a[k], a[i] = a[i], a[k]
            ans = -ans
        pivot = a[k][k]
        ans *= pivot
        for i in range(k+1, n):
            c = a[i][k] / pivot
            for j in range(k+1, n):
                a[i][j] -= c*a[k][j]
    return ans


def comparator_moments(b, R, top):
    c = (R*R+1)/(R+1)**2
    # Moments of uniform[-1,1] plus an independent three-point variable.
    a = [Q(1, k+1) if k % 2 == 0 else Q(0) for k in range(top+1)]
    v = [Q(1)] + [(1-c)*b**k if k % 2 == 0 else Q(0) for k in range(1, top+1)]
    mus = [sum((comb(k,j)*a[k-j]*v[j] for j in range(k+1)), Q(0)) for k in range(top+1)]
    # Separate direct integration of each of the three shifted uniform densities.
    weights = [(Q(0), c), (b, (1-c)/2), (-b, (1-c)/2)]
    direct = [sum((weight*((shift+1)**(k+1)-(shift-1)**(k+1))/(2*(k+1))
                   for shift, weight in weights), Q(0)) for k in range(top+1)]
    need(mus == direct and mus[0] == 1, 'independent density moments')
    return mus


def trace_by_cumulants(mu, count):
    cumul = [Q(0)] * len(mu)
    for n in range(1, len(mu)):
        cumul[n] = mu[n] - sum((comb(n-1,k-1)*cumul[k]*mu[n-k] for k in range(1,n)), Q(0))
    return [Q(0)] + [(-1)**(m+1)*cumul[2*m]/(2*factorial(2*m-1)) for m in range(1,count+1)]


def trace_by_log_derivative(mu, count):
    coeff = [(-1)**k*mu[2*k]/factorial(2*k) for k in range(count+1)]
    sums = [Q(0)]
    for m in range(1,count+1):
        sums.append(-m*coeff[m] - sum((sums[k]*coeff[m-k] for k in range(1,m)), Q(0)))
    return sums


# Gaussian rationals, not floating complex arithmetic.
def ca(a,b): return (a[0]+b[0], a[1]+b[1])
def cm(a,b): return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])
def cp(a,n):
    out = (Q(1),Q(0))
    for _ in range(n): out = cm(out,a)
    return out

def poly(c,z):
    out = (Q(0),Q(0))
    for a in reversed(c): out = ca(cm(out,z),(Q(a),Q(0)))
    return out


def synthetic_domination():
    count = 0
    for d in (1,2,3):
        xs = [Q(1,j*j) for j in range(1,d+1)]
        ints = [(x,x) for x in xs]
        r, B = Q(1,100), Q(1,50)
        lam = (r/2,r/3)
        for n in range(1,5):
            eps, _ = interpolation_budget(ints,r,B,n)
            for c in ([1]*d, list(range(1,d+1)), [(-1)**j for j in range(d)]):
                head = sum((x**n*poly(c,(x,Q(0)))[0]**2 for x in xs),Q(0))
                pv = poly(c,lam)
                tail = 2*cm(cp(lam,n),cm(pv,pv))[0]
                need(abs(tail) <= eps*head, 'complete conjugate-pair domination')
                need(head+tail >= (1-eps)*head, 'lower form inequality')
                count += 1
    return count


def reconstruct(input_path=None):
    raw = regular_bytes(input_path or ROOT/'INPUTS.json')
    need(sha256(raw).hexdigest() == INPUT_SHA256, 'imported input bytes changed')
    data = load_json(raw)
    H = data['height']
    need(type(H) is int and H == 3*10**12, 'height type/value')
    intervals = data['positive_ordinate_intervals']
    need(len(intervals) == 25 and all(type(x) is int for row in intervals for x in row), 'ordinate primitive format')
    den = data['ordinate_denominator']
    nodes = [(Q(den,b)**2,Q(den,a)**2) for a,b in intervals]

    al, au = atan_bound(Q(1,5)); bl, bu = atan_bound(Q(1,239))
    pi_lo, pi_hi = 16*al-4*bu,16*au-4*bl
    need(Q(3) < pi_lo < pi_hi < Q(22,7), 'Machin pi enclosure')
    lratio, _ = log_bound(Q(200,101))
    need(lratio > Q(2,3), 'Jensen radius budget')
    _, lH = log_bound(H)
    need(lH < 29, 'complete height-tail log bound')
    # Elementary budgets in the written Jensen proof.
    need(Q(76,7)>10 and Q(55,14)<4 and Q(2,81)>Q(1,100), 'theta mass lower bound')
    need(Q(5,2)**8>1200 and 3**4<100, 'elementary exponential comparisons')
    need(Q(100)+Q(27,4)<Q(4,3)*100, 'all-T Jensen monotone inequality at100')

    radius, mass = Q(1,H*H),Q(60,H)
    eps25, factors = interpolation_budget(nodes,radius,mass,2)
    need(eps25 < Q(1,5_000_000), 'all-shift25 threshold')
    eps9, _ = interpolation_budget(nodes[:9],radius,mass,1)
    need(eps9 < Q(1,3), 'all-shift9 threshold')
    eps10, _ = interpolation_budget(nodes[:10],radius,mass,1)
    need(eps10 > 1, 'inconclusive next rank is recorded, not called a negative form')
    heat_loss = 16*mass
    need(heat_loss < Q(1,10**9), 'positive Gaussian sum: full tail reserve')
    need(H*H-Q(1,4)-225 >= Q(H*H,2), 'off-line phase payment geometry')
    need(determinant([[Q(1),Q(1,2)],[Q(1,2),Q(1,6)]]) == -Q(1,12), 'inverse factorial is not a PSD multiplier')
    scalar_loss = 225*mass
    need(scalar_loss < Q(1,10**8), 'all positive scalar traces')
    need(Q(225,H*H)<1, 'all-exponent scalar monotonicity')
    # Ratios prove all shifts symbolically in the paper; these are additional finite controls.
    for n in (3,4,7):
        en, _ = interpolation_budget(nodes,radius,mass,n)
        need(en <= eps25, 'shift monotonicity control')

    tiny = Q(1,10**16)
    Rtheta = 1+tiny/10
    mass_theta = mass+tiny*tiny/4
    epstheta, _ = interpolation_budget(nodes,radius,mass_theta,2)
    need(tiny*H < 3 and Rtheta>1, 'added zeros beyond imported height')
    need(epstheta < Q(1,5_000_000), 'actual-theta perturbation keeps25-rank margin')
    need(225*mass_theta<Q(1,10**8), 'perturbed scalar all-order margin')

    count = 16
    mus = comparator_moments(Q(1,2),Q(6,5),2*count)
    sm = trace_by_cumulants(mus,count)
    need(sm == trace_by_log_derivative(mus,count), 'two exact trace reconstructions')
    need(all(x>0 for x in sm[1:]), 'finite scalar sign controls')
    mat = [[sm[2+i+j] for j in range(4)] for i in range(4)]
    det = determinant(mat)
    expected_det = Q(-19170822476692170759725788896551,
                    18160328599274715237536977953314688937542592738885632000000000)
    need(det == expected_det and det<0, 'explicit full-rank counterexample')
    small = Q(1,10**8)
    eps_model,_ = interpolation_budget([(Q(1,j*j),Q(1,j*j)) for j in range(1,26)],
                                     small*small,4*small*small,2)
    need(eps_model<Q(1,10**10), 'compact comparator hides from25 ranks at every shift')
    need(Q(3,8)<1 and 2*(Q(1,2))**2*(1-Q(1,4))==Q(3,8), 'analytic comparator all-order margin')
    ncontrol=synthetic_domination()

    return {
      'packet':'THA26', 'schema':1, 'rh_proved':False,
      'input_sha256':INPUT_SHA256,
      'external_zeros_recomputed':False,
      'bounds':{
       'pi':[pair(pi_lo),pair(pi_hi)],
       'theta_normalization_lower':pair(Q(1,100)),
       'zero_count_scope':'N(T) <= T log T for every real T >= 100; analytic Jensen proof, not a zero-count execution',
       'height':H, 'tail_radius':pair(radius),'tail_absolute_mass_upper':pair(mass),
       'scalar_relative_loss_upper':pair(scalar_loss),
       'gaussian_sum_relative_loss_upper':pair(heat_loss),
       'inverse_factorial_2_by_2_determinant':pair(-Q(1,12)),
       'bernstein_scope':'log(xi(1/2+sqrt(t))/xi(1/2)) is Bernstein for t>=0; paper proof from positive complete Gaussian zero sum, not numerical extrapolation',
       'hankel_d25_shift2_epsilon':enclosure(eps25),
       'hankel_d9_shift1_epsilon':enclosure(eps9),
       'hankel_d10_shift1_majorant_inconclusive':enclosure(eps10),
       'all_integer_shifts_scope':'d<=25 and n>=2; additionally d<=9 and n>=1, by the written monotonicity proof',
       'lagrange_products_used':len(factors),
      },
      'actual_theta_perturbation':{
       'shift_b':pair(tiny),'R':pair(Rtheta),
       'added_nonreal_height_lower':'pi/b > imported H',
       'added_imaginary_distance_upper':pair(Q(1,10)),
       'total_tail_absolute_mass_upper':pair(mass_theta),
       'gaussian_sum_relative_loss_upper':pair(16*mass_theta),
       'hankel_d25_shift2_epsilon':enclosure(epstheta),
       'is_original_theta_source':False,
      },
      'compact_control':{
       'b':pair(Q(1,2)), 'R':pair(Q(6,5)), 'central_probability':pair(Q(61,121)),
       'trace_values':[pair(s) for s in sm[1:]],
       'hankel_d4_shift2_determinant':pair(det),
       'hankel_d4_shift2_determinant_outward':enclosure(det,50),
       'all_scalar_positive_factor_lower':pair(Q(5,8)),
       'separate_small_b':pair(small),
       'separate_small_b_d25_all_shift_epsilon':enclosure(eps_model),
       'gaussian_rational_domination_panels':ncontrol,
       'moments_checked_by_two_methods':len(mus),
       'traces_checked_by_two_methods':count,
      },
      'not_claimed':['unweighted all-rank Hankel positivity for xi','numerical actual xi moments','new zero census',
        'fresh parent code execution','independent mathematical acceptance','Lean proof','remote publication'],
    }


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--inputs',type=Path,default=ROOT/'INPUTS.json')
    ap.add_argument('--expect',type=Path)
    ap.add_argument('--emit',type=Path)
    args=ap.parse_args()
    result=reconstruct(args.inputs)
    text=json.dumps(result,sort_keys=True,indent=2)+'\n'
    if args.expect is not None:
        expected=load_json(regular_bytes(args.expect))
        need(equal_typed(result,expected),'fresh exact reconstruction differs from typed receipt')
    if args.emit is not None:
        need(args.emit.resolve() not in {args.inputs.resolve(),Path(__file__).resolve()},'refuse source overwrite')
        args.emit.write_text(text,encoding='utf-8')
    print(text,end='')

if __name__=='__main__':
    try: main()
    except (ValueError,OSError,json.JSONDecodeError) as exc:
        print('FAIL_THA26: '+str(exc),file=sys.stderr)
        raise SystemExit(1)
