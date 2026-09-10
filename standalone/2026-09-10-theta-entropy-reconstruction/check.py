#!/usr/bin/env python3
"""Exact finite controls and one whole-integral counterlaw enclosure, not RH."""
from fractions import Fraction as F
from math import comb, prod
from pathlib import Path
import argparse
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parent
FILES = {'PROOF.md', 'README.md', 'REVIEW.md', 'SOURCES.json', 'VALIDATION.md',
         'check.py', 'test_check.py', 'result.json', 'SHA256SUMS'}
PARENT = '8f1f457b0b92e76a0a75bd3d8a8921c205fa75b0'


def need(ok, message):
    if not ok:
        raise ValueError(message)


def entropy_coeff(r):
    return F(1, 2*r*(2*r-1))


def fwht(values):
    a = list(values)
    width = 1
    while width < len(a):
        for start in range(0, len(a), 2*width):
            for j in range(start, start+width):
                u, v = a[j], a[j+width]
                a[j], a[j+width] = u+v, u-v
        width *= 2
    return a


def parity_counts(n, power):
    # Count ordered index tuples by their parity masks, independently of spins.
    a = [0]*(1 << n)
    a[0] = 1
    for _ in range(power):
        b = [0]*len(a)
        for mask, count in enumerate(a):
            for i in range(n):
                b[mask ^ (1 << i)] += count
        a = b
    return a


def gaussian_moment(n):
    need(n >= 0 and n % 2 == 0, 'even Gaussian moment required')
    return prod(range(1, n, 2))


def counterlaw():
    epsilon = F(1, 10**6)
    A = {}
    for n in (0, 2, 4, 6):
        lower = F(gaussian_moment(n))-epsilon*gaussian_moment(n+6)
        upper = lower+epsilon**2*gaussian_moment(n+12)/2
        need(0 < lower <= upper, 'normalization guard')
        A[n] = (lower, upper)
    moments = {n:(a/A[0][1], b/A[0][0]) for n,(a,b) in A.items()}
    lower = moments[6][0]-15*moments[4][1]*moments[2][1]+30*moments[2][0]**3
    upper = moments[6][1]-15*moments[4][0]*moments[2][0]+30*moments[2][1]**3
    need(F(-740,10**6) < lower <= upper < F(-696,10**6) < F(-1,2000),
         'sixth cumulant counterlaw sign')
    return {
        'epsilon':str(epsilon),
        'unnormalized_integral_bounds':{str(n):[str(a),str(b)] for n,(a,b) in A.items()},
        'sixth_cumulant_bounds':[str(lower),str(upper)],
        'safe_sixth_cumulant_interval':['-37/50000','-87/125000'],
        'scope':'density proportional to exp(-x^2/2-10^-6*x^6), NOT theta'}


def reconstruct():
    groups = {}
    ncases = 0
    for d in range(1, 9):
        for r in range(1,d+1):
            need(entropy_coeff(r)*2*r*(2*r-1) == 1, 'entropy second derivative')
        for m in (F(-3,4), F(-1,2), F(0), F(1,3), F(3,4)):
            finite_tail = sum((entropy_coeff(r)*m**(2*r) for r in range(d+1,d+10)), F(0))
            bound = m**(2*d+2)*entropy_coeff(d+1)/(1-m*m)
            need(0 <= finite_tail <= bound, 'geometric entropy tail control')
            ncases += 1
    groups['entropy_polynomial_panels'] = ncases

    potentials = [
        [F(0),F(1)],
        [F(9),F(-5),F(1)],
        [F(0),F(1,2),F(0),F(1,10**6)],
        [F(1),F(3),F(3),F(2),F(1)]]
    construction = []
    for coeff in potentials:
        d = len(coeff)-1
        bound = max([F(1)]+[v/entropy_coeff(r) for r,v in enumerate(coeff) if r and v>0])
        L = bound.numerator//bound.denominator+1
        N = L**(2*d+1)
        b = [F(0)]+[N*entropy_coeff(r)-coeff[r]*L**(2*r) for r in range(1,d+1)]
        need(all(v>0 for v in b[1:]), 'positive many-body coefficients')
        need(F(N,L**(2*d)) == L, 'magnetization normalization')
        for m in (F(0),F(1,3),F(-2,5),F(1)):
            lhs = N*sum((entropy_coeff(r)*m**(2*r) for r in range(1,d+1)),F(0))
            lhs -= sum((v*(L*m)**(2*r) for r,v in enumerate(coeff)),F(0))
            rhs = -coeff[0]+sum((b[r]*m**(2*r) for r in range(1,d+1)),F(0))
            need(lhs == rhs, 'exact exponent identity')
        construction.append({'P_even_coefficients':list(map(str,coeff)), 'L':L, 'N':N})
    groups['rational_potential_constructions'] = len(construction)

    walsh_digest = hashlib.sha256()
    mask_cases = 0
    panels = 0
    for n in range(2,9):
        for r in range(1,5):
            spin_values = [(n-2*mask.bit_count())**(2*r) for mask in range(1<<n)]
            transformed = fwht(spin_values)
            tuples = parity_counts(n,2*r)
            for mask in range(1<<n):
                need(transformed[mask] == (1<<n)*tuples[mask], 'Walsh/tuple mismatch')
                need(tuples[mask]>=0 and (mask.bit_count()%2==0 or tuples[mask]==0),
                     'interaction parity or positivity')
            walsh_digest.update(json.dumps([n,r,tuples],separators=(',',':')).encode())
            mask_cases += 1<<n
            panels += 1
    groups['complete_spin_Walsh_panels'] = panels
    groups['checked_Walsh_coefficients'] = mask_cases

    convex_cases = 0
    for d in range(1,5):
        H = lambda x:sum((F(x)**(2*r)/(r+1) for r in range(1,d+1)),F(0))
        for s in range(-16,17):
            need(H(s+2)+H(s-2)-2*H(s)>=0, 'conditional pair attraction')
            convex_cases += 1
    groups['conditional_attraction_controls'] = convex_cases

    fourspin = []
    for r in (F(1,2),F(3,4),F(7,8),F(999,1000)):
        a = [F(0)]*5
        for state in range(16):
            minus = state.bit_count()
            a[minus] += r if minus%2 else 1
        need(a == [1,4*r,6,4*r,1], 'complete four-spin polynomial')
        # Reconstruct the reciprocal reduction independently at rational nodes.
        for u in (F(1,3),F(2,3),F(2),F(5)):
            lhs = sum((a[k]*u**k for k in range(5)),F(0))/u**2
            y = u+1/u
            need(lhs == y*y+4*r*y+4, 'reciprocal polynomial reduction')
        discriminant = 16*(r*r-1)
        need(discriminant < 0, 'four-spin roots are off the unit circle')
        fourspin.append({'r':str(r),'coefficients':list(map(str,a)),
                         'reduced_discriminant':str(discriminant)})
    groups['complete_four_spin_laws'] = len(fourspin)
    q = F(101,100)
    a = [F(0)]*5
    for state in range(16):
        minus = state.bit_count()
        S = 4-2*minus
        a[minus] += q**(S**4//16)
        spins = [1 if not state & (1<<i) else -1 for i in range(4)]
        pairs = sum(spins[i]*spins[j] for i in range(4) for j in range(i+1,4))
        need(S**4 == 40+32*pairs+24*prod(spins), 'connected quartic expansion')
    need(a == [q**16,4*q,F(6),4*q,q**16], 'connected four-spin polynomial')
    need(q**30-3*q**14+2 < 0, 'connected attractive non-LY discriminant')
    groups['connected_attractive_four_spin_law'] = 1

    bernstein = 0
    for n in range(2,17):
        for t in (F(0),F(1,7),F(1,2),F(6,7),F(1)):
            prob = [comb(n,k)*t**k*(1-t)**(n-k) for k in range(n+1)]
            need(sum(prob)==1, 'Bernstein mass')
            mean = sum((F(k,n)*p for k,p in enumerate(prob)),F(0))
            variance = sum(((F(k,n)-t)**2*p for k,p in enumerate(prob)),F(0))
            need(mean==t and variance==t*(1-t)/n, 'Bernstein moment/variance')
            bernstein += 1
    groups['Bernstein_binomial_variances'] = bernstein

    # Test the normalization comparison without approximating exponentials.
    ratio_panels = 0
    for c in (F(101,100),F(11,10),F(2)):
        q = list(map(F,[1,3,7,3,1]))
        factors = [1/c,c,F(1),c,1/c]
        Q = [x*f for x,f in zip(q,factors)]
        Z,ZQ = sum(q),sum(Q)
        for x,y in zip(q,Q):
            ratio = y*Z/(x*ZQ)
            need(1/c**2 <= ratio <= c**2, 'partition normalizing cost')
        ratio_panels += 1
    groups['restricted_partition_normalization_panels'] = ratio_panels
    need(1+F(3,4)+F(3,4)**2/2+F(3,4)**3/6 > 2, 'source geometric tail')
    need(F(8,3)**6 > 256, 'source envelope offset')
    need(8*6**3+30*4**2+15*2 == 2238, 'source derivative budget')
    need(2238 < 63*36, 'q derivative budget')
    need(1-15+30==16 and 720//3==240, 'sixth cumulant normalization')
    groups['source_and_cumulant_constants'] = 5
    groups['complete_counterlaw_integral_certificate'] = 1
    return {
        'schema':1,
        'status':'PROPOSED_MANY_SPIN_RECONSTRUCTION_NOT_PAIR_OR_RH',
        'parent_commit':PARENT,
        'rh_proved':False,
        'pair_realization_proved':False,
        'analytic_theorems_machine_proved':False,
        'actual_theta_moments_newly_computed':0,
        'bounded_groups':groups,
        'potential_constructions':construction,
        'Walsh_sha256':walsh_digest.hexdigest(),
        'four_spin_countermodels':fourspin,
        'continuous_countermodel':counterlaw()}


def strict_json(path):
    def pairs(items):
        out = {}
        for key,value in items:
            need(key not in out, 'duplicate JSON key')
            out[key] = value
        return out
    def nofloat(value):
        raise ValueError('non-integer JSON numeric literal')
    return json.loads(Path(path).read_text(),object_pairs_hook=pairs,
                      parse_float=nofloat,parse_constant=nofloat)


def canonical(obj):
    return json.dumps(obj,sort_keys=True,separators=(',',':'))


def authenticate():
    need({p.name for p in ROOT.iterdir()} == FILES, 'packet inventory')
    need(all((ROOT/n).is_file() and not (ROOT/n).is_symlink() for n in FILES),
         'nonregular packet entry')
    entries = {}
    for line in (ROOT/'SHA256SUMS').read_text().splitlines():
        digest,name = line.split('  ',1)
        need(name not in entries and name in FILES-{'SHA256SUMS'}, 'manifest path')
        need(len(digest)==64, 'manifest hash format')
        entries[name]=digest
    need(set(entries)==FILES-{'SHA256SUMS'}, 'manifest completeness')
    for name,digest in entries.items():
        need(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest, 'hash: '+name)
    need(strict_json(ROOT/'SOURCES.json')['parent_commit']==PARENT, 'parent source drift')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--emit',action='store_true',help='produce only; no authentication')
    mode.add_argument('--check',type=Path)
    args = parser.parse_args()
    result = reconstruct()
    if args.check:
        authenticate()
        need(canonical(strict_json(args.check))==canonical(result), 'result reconstruction differs')
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, KeyError, TypeError, ZeroDivisionError) as error:
        print('REJECT: '+str(error),file=sys.stderr)
        sys.exit(1)
