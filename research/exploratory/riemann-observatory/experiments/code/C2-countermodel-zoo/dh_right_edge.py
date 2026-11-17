#!/usr/bin/env python3
"""C2 zoo -- rigorous right edge for zeros of the Davenport-Heilbronn function f in sigma > 1.

Claim (THEOREM, proof in REPORT.md sect. DH-2): for sigma > 1,
    f(s) = 0  <=>  R(s) := L(s,chi)/L(s,chibar) = -(1+ik)/(1-ik) = exp(i(pi + 2 alpha)),  alpha = arctan k,
and R(s) = prod_{p = 2 mod 5} (1+i p^{-s})/(1-i p^{-s}) * prod_{p = 3 mod 5} (1-i p^{-s})/(1+i p^{-s}).
Each factor has |arg| <= 2 arctan(p^{-sigma}) (image of the disc |u|<=r under (1+u)/(1-u) is the disc with
centre (1+r^2)/(1-r^2), radius 2r/(1-r^2), whose max argument is arcsin(2r/(1+r^2)) = 2 arctan r).  Hence if
    S(sigma) := sum_{p = 2,3 mod 5} 2 arctan(p^{-sigma}) < pi - 2 alpha
then f has no zero on Re s = sigma (and S is decreasing, so none in Re s >= sigma).
This script brackets sigma_1 with S(sigma_1) = pi - 2 alpha rigorously:
  lower bound for S: partial sum over p <= P (Arb);
  upper bound for S: partial sum + 2 sum_{p > P} p^{-sigma} <= partial + 2 * 1.25506 sigma P^{1-sigma}/((sigma-1) log P)
  using pi(x) < 1.25506 x / log x for x > 1 (Rosser-Schoenfeld 1962, Thm 1 / (3.6)), via partial summation
  sum_{p>P} p^{-sigma} <= sigma int_P^inf pi(x) x^{-sigma-1} dx  (the boundary term -pi(P)P^{-sigma} is dropped, <= 0).
Usage: python3 dh_right_edge.py OUTDIR [P]
"""
import sys, os, json, time, hashlib
import numpy as np
import flint
from flint import arb

flint.ctx.prec = 96


def primes_upto(n):
    sieve = np.ones(n + 1, dtype=bool); sieve[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = False
    return np.nonzero(sieve)[0]


def S_bounds(sig, ps, P):
    s = arb(sig)
    tot = arb(0)
    for p in ps:
        tot += 2 * (arb(int(p)) ** (-s)).atan()
    tail = 2 * arb("1.25506") * s * arb(P) ** (1 - s) / ((s - 1) * arb(P).log())
    return tot, tot + tail


def main():
    outdir = sys.argv[1]
    P = int(sys.argv[2]) if len(sys.argv) > 2 else 2_000_000
    t0 = time.time()
    k = ((10 - 2 * arb(5).sqrt()).sqrt() - 2) / (arb(5).sqrt() - 1)
    target = arb.pi() - 2 * k.atan()
    allp = primes_upto(P)
    ps = [int(p) for p in allp if p % 5 in (2, 3)]
    # float pre-location of the root of S(sigma) = target
    psf = np.array(ps, dtype=float)
    Sf = lambda sg: float(np.sum(2 * np.arctan(psf ** (-sg))))
    lo, hi = 1.0001, 3.0
    for _ in range(60):
        mid = (lo + hi) / 2
        if Sf(mid) > float(target):
            lo = mid
        else:
            hi = mid
    approx = (lo + hi) / 2
    # rigorous bracket: find sig_a with S_lower(sig_a) > target (so S > target there)
    # and sig_b with S_upper(sig_b) < target (zero-free for Re s >= sig_b)
    res = dict(P=P, n_primes_2_3_mod5=len(ps), target_pi_minus_2alpha=target.str(20),
               float_root_partial_sum_only=approx)
    # NON-RIGOROUS estimate of the true root: add the PNT-heuristic tail sum_{p>P, p=2,3 mod 5} 2 p^{-sigma}
    # ~ int_P^inf x^{-sigma}/log x dx = E1((sigma-1) log P)
    import mpmath
    Sh = lambda sg: Sf(sg) + float(mpmath.e1((sg - 1) * mpmath.log(P)))
    lo2, hi2 = 1.0001, 3.0
    for _ in range(60):
        mid = (lo2 + hi2) / 2
        if Sh(mid) > float(target):
            lo2 = mid
        else:
            hi2 = mid
    res['heuristic_root_with_PNT_tail'] = (lo2 + hi2) / 2
    for d in [0.0005, 0.001, 0.002, 0.005, 0.01, 0.015, 0.02, 0.03, 0.05, 0.08]:
        b = approx + d
        lo_b, up_b = S_bounds(b, ps, P)
        if up_b < target:
            res['zero_free_for_sigma_ge'] = b
            res['S_upper_at_that_sigma'] = up_b.str(15)
            break
    for d in [0.0005, 0.001, 0.002, 0.005, 0.01]:
        a = approx - d
        lo_a, up_a = S_bounds(a, ps, P)
        if lo_a > target:
            res['S_exceeds_target_at_sigma'] = a
            res['S_lower_at_that_sigma'] = lo_a.str(15)
            break
    # how many primes are needed at sigma = 1 (heuristic for height of first zero in sigma > 1)
    cum = np.cumsum(2 * np.arctan(psf ** (-1.0)))
    K = int(np.searchsorted(cum, float(target))) + 1
    res['primes_needed_at_sigma_1'] = dict(K=K, largest_prime=ps[K - 1])
    for sg in [1.01, 1.05, 1.1]:
        c = np.cumsum(2 * np.arctan(psf ** (-sg)))
        KK = int(np.searchsorted(c, float(target))) + 1
        res[f'primes_needed_at_sigma_{sg}'] = dict(K=KK, largest_prime=ps[KK - 1] if KK <= len(ps) else None)
    res['runtime_s'] = round(time.time() - t0, 1)
    res['versions'] = dict(python_flint=flint.__version__, numpy=np.__version__)
    os.makedirs(outdir, exist_ok=True)
    fn = os.path.join(outdir, 'dh_right_edge.json')
    json.dump(res, open(fn, 'w'), indent=1)
    print(json.dumps(res, indent=1))
    print(hashlib.sha256(open(fn, 'rb').read()).hexdigest(), fn)


if __name__ == '__main__':
    main()
