# s6_ray_uniformity_check.py -- (1) case (c,lambda)=1 with cusps +/- ; (2) Lemma 6.3 uniformity:
# kappa_0, the cusp index sigma, delta'_0 = delta' mod D_0 and r^{-1} mod D_0 depend on the active
# primes only through r mod M^2 (M = lambda^12 L^4).  We replace r = p (N p = 7 or 13) or r = p7*p13 by a
# LARGE prime r' = r mod M^2 (norm ~ 10^50) and recompute everything with exact integer arithmetic
# (cubic symbols via the Euclid/reciprocity algorithm cubic_jacobi, self-tested in s6_cubic_selftest.py).
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s6_ray_multiplier_check import *

L = mul(power(LAM, 5), (-8, 0))
p7 = primes_over(7)[0]; p13 = primes_over(13)[0]
print("--- case (c,lambda)=1 with nonzero cusp (v_lambda(h0)=3) ---")
for name, h0 in {'lam^3': power(LAM, 3), 'lam^3(2+3w)': mul(power(LAM, 3), (2, 3)), 'lam^3(-1+3w)': mul(power(LAM, 3), (-1, 3)),
                 'lam^3*w': mul(power(LAM, 3), OM)}.items():
    for primes, js in [([p7], [1]), ([p13], [4]), ([p7, p13], [1, 0])]:
        out = run(L, h0, primes, js)
        print("h0 %-13s N=%s j=%s: case %d cusp %s kappa0=w^%d CRT err %.1e sum err %.1e"
              % (name, [norm(p) for p in primes], js, out['case'], out['sigma'], out['kappa0'], out['err_crt'], out['err_sum']))

print("--- Lemma 6.3: dependence on r only through r mod M^2 ---")
M = mul(power(LAM, 12), power(L, 4)); M2 = mul(M, M)
rnd = random.Random(7)
def big_prime_congruent(r, tries=4000):
    for _ in range(tries):
        t = (rnd.randint(1, 50), rnd.randint(-50, 50))
        x = add(r, mul(M2, t))
        if sympy.isprime(norm(x)):
            return make_primary(x)
    raise RuntimeError
def data(h0, primes, hps):
    d = build(L, h0, primes, hps)
    D0 = mul(power(LAM, 3), d['c0'])
    k0 = (d['kappa'] - cub(d['a'], d['r'])) % 3
    rinv = inv_mod(d['r'], D0) if norm(D0) > 1 else ONE
    return (d['case'], d['sigma'], k0, canon_mod(d['dp'], D0), canon_mod(rinv, D0), d['c0'])
tot = 0; bad = 0
for h0 in [(1, 1), mul(LAM, (2, 0)), mul(power(LAM, 2), (2, 0)), mul(power(LAM, 2), (-2, 3)), power(LAM, 3),
           mul(power(LAM, 3), (2, 3)), mul(power(LAM, 5), (-2, 1)), (0, 0)]:
    for rp in ([p7], [p13], [p7, p13]):
        r = ONE
        for p in rp: r = mul(r, p)
        ref = set()
        for hps in itertools.islice(itertools.product(*[[x for x in residues(p) if not is_zero(x)] for p in rp]), 0, 6):
            ref.add(data(h0, rp, list(hps)))
        assert len(ref) == 1
        ref = ref.pop()
        for _ in range(3):
            rr = big_prime_congruent(r)
            # r' must equal r mod M^2 exactly (primary normalisation keeps the residue since r is primary)
            assert divides(M2, sub(rr, r))
            for _ in range(3):
                h = (rnd.randint(1, 10**30), rnd.randint(1, 10**30))
                if divides(rr, h): continue
                got = data(h0, [rr], [h])
                tot += 1
                if got != ref:
                    bad += 1; print("MISMATCH", h0, rp, got, ref)
        print("h0=%s r=%s: case %d cusp %s kappa0=w^%d  [checked against 3 large primes r' = r mod M^2, N(r') ~ 1e%d]"
              % (h0, [norm(p) for p in rp], ref[0], ref[1], ref[2], len(str(norm(rr))) - 1))
print("uniformity checks:", tot, "mismatches:", bad)
