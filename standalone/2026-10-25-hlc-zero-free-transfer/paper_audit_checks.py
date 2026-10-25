"""Finite algebra checks for the 2610.20242 source audit; not a theorem proof."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import gcd, log
import json

results = {}
parity_cases = 0
for u in range(3, 64, 2):
    for v in range(3, 64, 2):
        if gcd(u, v) != 1:
            continue
        c = (-pow(v, -1, u)) % u
        d = (1 + v*c)//u
        up, vp = u, (u-v)//2
        cp, dp = -2*c, d-c
        assert up*dp-vp*cp == 1
        assert gcd(up, vp) == 1
        assert (Fraction(cp, up)+2*Fraction(c,u)).denominator == 1
        parity_cases += 1
results['parity_conjugacy_cases'] = parity_cases

projective = {}
for p in [3, 5, 7, 11]:
    cnt = Counter()
    for u,c,v,d in product(range(p), repeat=4):
        if (u*d-c*v)%p != 1:
            continue
        # Kernel of (u,-2c) represented by (2c,u).
        a,b = 2*c%p,u
        line = ('infinity',) if a == 0 else (b*pow(a,-1,p)%p,)
        cnt[line] += 1
    assert len(cnt) == p+1
    assert set(cnt.values()) == {p*(p-1)}
    projective[p] = {'lines':len(cnt), 'matrices_per_line':p*(p-1)}
results['projective_density'] = projective

root_moment = {}
for m in range(2, 41):
    units = [y for y in range(m) if gcd(y,m)==1]
    inv = {y:pow(y,-1,m) for y in units}
    counts = Counter(((a+b)%m,(inv[a]+inv[b])%m) for a,b in product(units,repeat=2))
    T = sum(v*v for v in counts.values())
    tau3 = sum(1 for a in range(1,m+1) if m%a==0 for b in range(1,m//a+1) if (m//a)%b==0)
    assert T <= 2*m*m*tau3
    root_moment[m] = T
results['appendix_A_fourth_moment_count_moduli'] = len(root_moment)

# Exact local identity in p.25, for A_p empty, R=1 and all projective configurations.
p = 5
q = [Fraction(1,4),Fraction(1,2),Fraction(1,4)]
eta = [1-qq for qq in q]
bp = 1-sum(eta)/(p+1)
local_cases = 0
for zz in product(range(p+1),repeat=3):
    lhs = Fraction(0)
    for ell in range(p+1):
        term = Fraction(1)
        for j in range(3):
            term *= (1-eta[j]) if ell == zz[j] else 1
        lhs += term/(p+1)
    rhs = bp
    for a in range(3):
        for c in range(a+1,3):
            if zz[a] != zz[c]:
                continue
            term = eta[a]*eta[c]/(p+1)
            for j in range(a+1,c):
                term *= (1-eta[j]) if zz[j] == zz[a] else 1
            rhs += term
    assert lhs == rhs
    local_cases += 1
results['local_damping_identity_cases'] = local_cases

N = 100000
mu = [1]*(N+1)
prime = [True]*(N+1)
prime[0] = prime[1] = False
for p in range(2,N+1):
    if prime[p]:
        for k in range(p,N+1,p):
            mu[k] *= -1
            if k>p:
                prime[k] = False
        for k in range(p*p,N+1,p*p):
            mu[k] = 0
s = 0.0
prime_power_count = 0
for p in range(2,N+1):
    if not prime[p]:
        continue
    power = p
    while power <= N:
        s += log(p)*mu[power]
        if power>p:
            assert mu[power] == 0
            prime_power_count += 1
        power *= p
theta = sum(log(p) for p in range(2,N+1) if prime[p])
assert abs(s+theta) < 1e-8
results['zero_shift'] = {'N':N, 'sum_Lambda_mu':s, 'minus_theta':-theta, 'checked_composite_prime_powers':prime_power_count}
print(json.dumps(results,indent=2))
