#!/usr/bin/env python3
"""AC26: bounded exact arithmetic and full-matrix certificate replay.

Standard library only. No repository module, zero data, or numerical eigensolver.
Native matrices are inverted by triangular elimination and separately reconstructed
from trial-factorized Mobius values. Integer Bareiss minors are independently
checked against rational LDL pivots. These are same-author implementation controls,
not independent mathematical peer review or an all-scale proof.
"""
from __future__ import annotations
import argparse
from copy import deepcopy
from fractions import Fraction as Q
from functools import lru_cache
import hashlib
import json
from math import gcd, isqrt, lcm
from pathlib import Path
import sys

BASE = 'f99d9e3908dde4865377c75d9ca051c1f545bf4f'
CUTS = (3, 5, 9, 17, 33, 65, 129)
SHELLS = (3, 9, 27, 81)

class Invalid(ValueError):
    pass

def need(ok, message):
    if not ok:
        raise Invalid(message)

def enc(x):
    if isinstance(x, Q):
        return [x.numerator, x.denominator]
    if isinstance(x, (tuple, list)):
        return [enc(y) for y in x]
    if isinstance(x, dict):
        return {k: enc(v) for k, v in x.items()}
    return x

def raw(x):
    return json.dumps(enc(x), sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode()

def digest(x):
    return hashlib.sha256(raw(x)).hexdigest()

def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]

def mul(A, B):
    columns = list(zip(*B))
    return [[sum(a*b for a, b in zip(row, col)) for col in columns] for row in A]

def gram(A):
    return mul(list(map(list, zip(*A))), A)

def frob(A):
    return sum(x*x for row in A for x in row)

@lru_cache(None)
def mu(n):
    """Independent trial factorization, not a Mobius sieve."""
    m, sign, p = n, 1, 2
    while p*p <= m:
        if m % p == 0:
            m //= p
            sign = -sign
            if m % p == 0:
                return 0
        p += 1
    return -sign if m > 1 else sign

@lru_cache(None)
def mobius_mean(n):
    return sum((Q(mu(d), d) for d in range(1, n+1, 2)), Q(0)) if n >= 1 else Q(0)

def energy(t):
    t = Q(t)
    if t <= 1:
        return Q(0)
    return sum((min(Q(2), t-n)*mobius_mean(n)**2
                for n in range(1, (t.numerator+t.denominator-1)//t.denominator, 2)
                if n < t), Q(0))

def matrices(X):
    need(X >= 3 and X % 2 == 1, 'odd exclusive endpoint')
    ns = list(range(1, X, 2)); N = len(ns)
    Z = [[int(n % d == 0) for d in ns] for n in ns]
    B = [[0]*N for _ in ns]
    for i, n in enumerate(ns):
        for j, d in enumerate(ns[:i+1]):
            if n % d == 0:
                B[i][j] += d
                if j:
                    B[i][j-1] -= d
    return ns, Z, B

def invert_lower(B):
    N = len(B); V = [[Q(0)]*N for _ in range(N)]
    for i in range(N):
        nz = [k for k in range(i) if B[i][k]]
        for j in range(i+1):
            V[i][j] = (int(i == j)-sum((B[i][k]*V[k][j] for k in nz if k >= j), Q(0)))/B[i][i]
    return V

def inverse_formula(ns):
    return [[mobius_mean(n//d)/d for d in ns] for n in ns]

def bareiss_minors(A):
    """Leading principal determinants by fraction-free symmetric elimination."""
    R = [list(row) for row in A]; out = []; previous = 1; N = len(R)
    for k in range(N):
        pivot = R[k][k]
        need(type(pivot) is int and pivot > 0, 'nonpositive integer principal minor')
        out.append(pivot)
        for i in range(k+1, N):
            for j in range(i, N):
                num = pivot*R[i][j]-R[i][k]*R[k][j]
                need(num % previous == 0, 'nonexact Bareiss division')
                R[i][j] = R[j][i] = num//previous
        previous = pivot
    return out

def ldl_minors(A):
    """Different rational congruence algorithm; all acceptance survives -O/-OO."""
    N = len(A); L = [[Q(0)]*N for _ in range(N)]; D = []; det = Q(1); out = []
    for i in range(N):
        L[i][i] = Q(1)
        d = Q(A[i][i])-sum((L[i][k]**2*D[k] for k in range(i)), Q(0))
        need(d > 0, 'nonpositive rational LDL pivot')
        D.append(d); det *= d
        need(det.denominator == 1, 'integer determinant expected')
        out.append(det.numerator)
        for j in range(i+1, N):
            L[j][i] = (A[j][i]-sum((L[j][k]*L[i][k]*D[k] for k in range(i)), Q(0)))/d
    return out

def certificate(A):
    a = bareiss_minors(A); b = ldl_minors(A)
    need(a == b, 'independent positive-definiteness constructions disagree')
    return {'dimension': len(A), 'positive_leading_minors': len(a),
            'integer_matrix_sha256': digest(A),
            'principal_minors_encoding': 'positive hexadecimal strings',
            'principal_minors_sha256': digest([format(v,'x') for v in a])}

def prime_product(ns):
    """Finite Euler zeta product via ascending row additions, including powers."""
    Z = eye(len(ns)); loc = {n:i for i,n in enumerate(ns)}; primes = []
    for p in ns[1:]:
        if all(p % k for k in range(2, isqrt(p)+1)):
            primes.append(p)
            for n in ns:
                if n % p == 0:
                    Z[loc[n]] = [a+b for a,b in zip(Z[loc[n]], Z[loc[n//p]])]
    return Z, primes

def round_box(v, D=10**9):
    a = v.numerator*D//v.denominator
    return [Q(a,D), Q(a+1,D)]

def model_mean(n):
    k = 0
    while 3**(k+1) <= n:
        k += 1
    return Q(2,3)**k

def model_kernel(n):
    if n == 1:
        return 1
    k = 0
    while n % 3 == 0:
        n //= 3; k += 1
    return 3**(k-1) if n == 1 else 0

def model_inverse(n):
    if n == 1:
        return 1
    k = 0
    while n % 3 == 0:
        n //= 3; k += 1
    return -(2**(k-1)) if n == 1 else 0

def payload():
    native = []; shell = []; model = []; count_inverse = count_factor = 0
    for X in CUTS:
        ns, Z, B = matrices(X); V = invert_lower(B); V2 = inverse_formula(ns)
        need(V == V2, 'triangular inverse differs from factored Mobius formula')
        need(mul(B,V) == eye(len(ns)) and mul(V,B) == eye(len(ns)), 'two-sided inverse')
        Z2, primes = prime_product(ns); need(Z == Z2, 'finite Euler factorization')
        count_factor += len(primes)
        count_inverse += len(ns)**2
        E = energy(X); HS = frob(V)
        need(E == 2*sum(row[0]**2 for row in V), 'native first-column energy')
        trace = sum((energy(Q(X,d))/d for d in ns), Q(0))
        H = sum((Q(1,d) for d in ns), Q(0))
        need(2*HS == trace and E <= trace <= H*E, 'exact trace/bounds')
        G = gram(B)
        G4 = [[4*G[i][j]-int(i == j) for j in range(len(ns))] for i in range(len(ns))]
        native.append({'X':X, 'N':len(ns), 'inverse_entries':len(ns)**2,
                       'energy': E, 'energy_box':round_box(E), 'twice_HS_squared':trace,
                       'harmonic':H, 'inverse_sha256':digest(V),
                       'B_sha256':digest(B), 'coercivity_gt_one_quarter':certificate(G4)})
    high_rows = 0
    for A in SHELLS:
        old, Z, B = matrices(A); ns, _, BB = matrices(3*A)
        V = invert_lower(B); VV = invert_lower(BB)
        need(VV == inverse_formula(ns), 'shell inverse formula')
        n = len(old); C = [row[:n] for row in BB[n:]]; D = [row[n:] for row in BB[n:]]
        J = [[Q(int(j<=i), A+2*j) for j in range(A)] for i in range(A)]
        need(mul(D,J) == eye(A), 'high block integration inverse')
        L = [[-x for x in row] for row in mul(J,C)]; K = [row[:n] for row in VV[n:]]
        need(mul(L,V) == K and [row[n:] for row in VV[n:]] == J, 'whole block inverse')
        jj = frob(J); need(jj <= Q(A+1,2*A) <= Q(2,3), 'uniform fresh-shell bound')
        # Native all-vector finite tests. No source-specific vector is substituted.
        scale = lcm(*range(1,3*A,2))
        Vi = [[int(v*scale) for v in row] for row in V]
        Ki = [[int(v*scale) for v in row] for row in K]
        need(all(Q(Vi[i][j],scale)==V[i][j] for i in range(n) for j in range(n)), 'V denominator')
        need(all(Q(Ki[i][j],scale)==K[i][j] for i in range(A) for j in range(n)), 'K denominator')
        vg, kg = gram(Vi), gram(Ki); tests=[]
        for den in (10,100):
            M = [[den*scale*scale*int(i == j)+vg[i][j]-den*kg[i][j]
                  for j in range(n)] for i in range(n)]
            tests.append({'eta':[1,den], 'C':1, 'certificate':certificate(M)})
        highs=[]
        for q in (2,4,8):
            indices=[j for j,d in enumerate(old) if q*d >= A]
            h=frob([[row[j] for j in indices] for row in K]) if indices else Q(0)
            need(h <= 2*q*q, 'high-forcing sector bound')
            highs.append({'q':q,'columns':len(indices),'HS_squared':h,'upper':2*q*q})
            high_rows += 1
        shell.append({'A':A,'old_dimension':n,'new_dimension':len(ns),'shell_dimension':A,
                      'J_HS_squared':jj,'J_upper':Q(A+1,2*A),'L_sha256':digest(L),
                      'K_sha256':digest(K),'finite_compactness':tests,'high_forcing':highs})
    primitive_model=0
    for n in range(1,730,2):
        total=sum(model_kernel(d)*model_inverse(n//d) for d in range(1,n+1,2) if n%d==0)
        need(total==int(n==1), 'synthetic divisor inverse')
        primitive_model += 1
    for r in range(1,8):
        A=3**r; ns=list(range(1,A,2)); vals=[model_mean(n) for n in ns]
        lhs=2*sum((v*v for v in vals),Q(0)); formula=6*((Q(4,3)**r)-1)
        need(lhs==formula,'exact synthetic energy')
        for n,v in zip(ns,vals):
            value=sum(model_kernel(n//d)*d*(model_mean(d)-(model_mean(d-2) if d>=3 else 0))
                      for d in range(1,n+1,2) if n%d==0 and model_kernel(n//d))
            need(value==int(n==1),'model first-column source equation')
        tail=Q(4,3)**r
        Cmin=tail-Q(1,10)*(lhs/2)
        need(Cmin==Q(7,10)*tail+Q(3,10) and Cmin>1,'model local obstruction')
        model.append({'r':r,'A':A,'source_dimension':len(ns),'energy':lhs,
                      'half_shell_energy':tail,'C_lower_eta_one_tenth':Cmin})
    return enc({'schema':'AC26/rational-v1','base':BASE,
        'status':'PROPOSED_COMPONENTS; UNIFORM_ARITHMETIC_COMPACTNESS_OPEN; RH_UNPROVED',
        'native':native,'shells':shell,'synthetic':model,
        'coverage':{'native_inverse_entries':count_inverse,'Euler_prime_factors':count_factor,
                    'native_cutoffs':len(native),'shells':len(shell),'shell_Loewner_tests':2*len(shell),
                    'high_forcing_checks':high_rows,'synthetic_divisor_checks':primitive_model,
                    'synthetic_source_equations':sum(row['source_dimension'] for row in model)},
        'limits':['finite matrices only','no all-scale bound on C_eta','synthetic model is not zeta',
                  'no numeric zero inputs','no independent mathematical review','no full-checkout validator run']})

def seal(p):
    return {'payload':p,'sha256':digest(p)}

def unique_pairs(pairs):
    d={}
    for k,v in pairs:
        need(k not in d,'duplicate JSON key'); d[k]=v
    return d

def reject_float(value):
    raise Invalid('floats and nonfinite constants are not accepted')

def read(path):
    need(not path.is_symlink(),'symlink report')
    return json.loads(path.read_text(),object_pairs_hook=unique_pairs,parse_float=reject_float,parse_constant=reject_float)

def accept(report,expected):
    need(type(report) is dict and set(report)=={'payload','sha256'},'report shape')
    need(report['sha256']==digest(report['payload']),'payload seal')
    need(raw(report['payload'])==raw(expected),'primitive replay differs; coverage or mathematics altered')

def self_test(expected):
    # Establish that a pristine report passes the exact same acceptance path.
    accept(seal(expected),expected)
    cases=[]
    def changed(f):
        p=deepcopy(expected); f(p); cases.append(seal(p))
    changed(lambda p:p.update(base='0'*40))
    changed(lambda p:p.update(status='RH_PROVED'))
    changed(lambda p:p['native'].pop())
    changed(lambda p:p['native'][0].update(energy=[0,1]))
    changed(lambda p:p['native'][-1]['coercivity_gt_one_quarter'].update(positive_leading_minors=0))
    changed(lambda p:p['shells'][0]['finite_compactness'][0].update(C=0))
    changed(lambda p:p['shells'][-1].update(A=243))
    changed(lambda p:p['shells'][0]['high_forcing'][0].update(upper=0))
    changed(lambda p:p['synthetic'][-1].update(C_lower_eta_one_tenth=[0,1]))
    changed(lambda p:p.update(limits=[]))
    for report in cases:
        try: accept(report,expected)
        except Invalid: continue
        raise Invalid('resealed corruption accepted')
    return len(cases)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--write',type=Path); ap.add_argument('--check',type=Path)
    ap.add_argument('--self-test',action='store_true'); args=ap.parse_args()
    need(not(args.write and args.check),'choose write or check')
    p=payload(); r=seal(p)
    if args.write:
        args.write.write_bytes(raw(r)+b'\n')
    if args.check:
        accept(read(args.check),p)
    count=self_test(p) if args.self_test else 0
    print(json.dumps({'result':'PASS','sha256':r['sha256'],'resealed_rejections':count,'coverage':p['coverage']},sort_keys=True))
    return 0

if __name__=='__main__':
    try: raise SystemExit(main())
    except (Invalid,OSError,ValueError,ZeroDivisionError) as exc:
        print('FAIL: '+str(exc),file=sys.stderr); raise SystemExit(1)
