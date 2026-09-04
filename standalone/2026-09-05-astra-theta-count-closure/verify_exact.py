#!/usr/bin/env python3
"""Exact finite controls for the Astra theta-count packet.

Uses only Python's standard library and Fraction. No zeta evaluation, zero
census, theta integration, or extrapolation. The analytic proofs are in the
Markdown files; this program checks the specified finite algebra only.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
import json
from math import comb, factorial
from pathlib import Path


def poly_add(a, b):
    c = [Q(0)] * max(len(a), len(b))
    for i, x in enumerate(a):
        c[i] += x
    for i, x in enumerate(b):
        c[i] += x
    return c


def poly_mul(a, b):
    c = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


def shifted(a, x):
    c = [Q(0)] * len(a)
    for n, v in enumerate(a):
        for k in range(n+1):
            c[k] += v * comb(n, k) * x**(n-k)
    return c


def dcal(p):
    out = [Q(0)] * (len(p)+1)
    for i, c in enumerate(p):
        out[i] += (2*i+Q(1, 2))*c
        out[i+1] -= 2*c
    return out


def trace_from_pgf(p, nmax):
    f = shifted(p, Q(1))
    if f[0] != 1:
        raise ValueError("PGF must have P(1)=1")
    f += [Q(0)] * max(0, nmax+1-len(f))
    # Divide F'(y) by F(y), independently of roots or cumulants.
    h = []
    for n in range(nmax):
        h.append((n+1)*f[n+1] - sum(
            (f[j]*h[n-j] for j in range(1, n+1)), Q(0)))
    return [(-1)**n*h[n] for n in range(nmax)]


def pgf_of_probs(probs):
    p = [Q(1)]
    for x in probs:
        if not 0 <= x <= 1:
            raise ValueError("Not a Bernoulli probability")
        p = poly_mul(p, [1-x, x])
    return p


def mixed_pgf(weights, states):
    if len(weights) != len(states) or sum(weights) != 1 or any(w < 0 for w in weights):
        raise ValueError("Invalid probability weights")
    ans = [Q(0)]
    for w, ps in zip(weights, states):
        ans = poly_add(ans, [w*x for x in pgf_of_probs(ps)])
    return ans


def partitions(n):
    if n == 0:
        yield ()
        return
    for old in partitions(n-1):
        yield old + ((n-1,),)
        for i in range(len(old)):
            yield old[:i] + (old[i]+(n-1,),) + old[i+1:]


def compositions(n, r):
    if r == 1:
        yield (n,)
    else:
        for first in range(1, n-r+2):
            for rest in compositions(n-first, r-1):
                yield (first,) + rest


def cumulant_traces(weights, states, nmax):
    qs = [[sum((p**m for p in ps), Q(0)) for m in range(1, nmax+1)] for ps in states]

    @lru_cache(None)
    def moment(ms):
        return sum((w * prodq(qs[s][m-1] for m in ms)
                    for s, w in enumerate(weights)), Q(0))

    @lru_cache(None)
    def cumulant(ms):
        ans = Q(0)
        for blocks in partitions(len(ms)):
            ans += factorial(len(blocks)-1) * (-1)**(len(blocks)-1) * prodq(
                moment(tuple(sorted(ms[i] for i in block))) for block in blocks)
        return ans

    out = []
    for n in range(1, nmax+1):
        val = Q(0)
        for r in range(1, n+1):
            for ms in compositions(n, r):
                val += Q((-1)**(r-1)*n, factorial(r)) * cumulant(tuple(sorted(ms))) / prodq(ms)
        out.append(val)
    return out


def prodq(xs):
    ans = Q(1)
    for x in xs:
        ans *= x
    return ans


def hausdorff(ps, a, b):
    return sum(((-1)**j*comb(b, j)*ps[a+j] for j in range(b+1)), Q(0))


def run():
    counts = Counter()

    def check(group, name, ok):
        if not ok:
            raise ArithmeticError(f"{group}: {name}")
        counts[group] += 1

    p0 = [Q(0), Q(-6), Q(4)]
    p2 = dcal(dcal(p0))
    p4 = dcal(dcal(p2))
    check("source_polynomial", "P2", p2 == [0, Q(-75,2), 165, -112, 16])
    check("source_polynomial", "P4", p4 == [0, Q(-1875,8), Q(15465,4), -8512, 5176, -1056, 64])
    good2 = shifted(poly_add(p2, [20*x for x in p0]), Q(3))
    check("source_polynomial", "P2 plus 20P0", good2 == [Q(9,2), Q(33,2), 101, 80, 16])
    check("source_polynomial", "nonnegative shifted P2", all(c >= 0 for c in good2))
    check("source_polynomial", "shift3 P4", shifted(p4, Q(3)) ==
          [Q(108585,8), Q(142233,8), Q(-2391,4), -6880, -2024, 96, 64])
    shift20 = shifted(p4, Q(20))
    check("source_polynomial", "shift20 P4", shift20 ==
          [Q(2956811625,2), Q(4316576125,8), Q(324142185,4), 6421568, 283576, 6624, 64])
    check("source_polynomial", "positive shift20", all(c > 0 for c in shift20))
    neg_bound = 2024*17**4 + 6880*17**3 + Q(2391,4)*17**2
    check("source_polynomial", "negative polynomial budget", neg_bound == Q(812082775,4))
    check("source_polynomial", "C4 budget", neg_bound < 18*20_000_000)
    R, d = Q(1000), Q(1,4)
    alpha = 2*(R*R-d*d)/(R*R+d*d)**2
    beta = 1/(R*R+d*d)**2
    q = [Q(1), Q(0), -alpha, Q(0), beta]
    factors = poly_mul([R*R+d*d, -2*R, 1], [R*R+d*d, 2*R, 1])
    check("source_polynomial", "quartet factorization", [x/(R*R+d*d)**2 for x in factors] == q)
    margin = 1-20*alpha-20_000_000*beta
    check("source_polynomial", "global positivity margin", margin > Q(9999,10000))

    check("heat_budget", "first real invariant parameter", 15**2+Q(1,4) < 226)
    check("heat_budget", "exponential exponent", 100-Q(226,100) > 97)
    check("heat_budget", "prefactor", 10100 < 2**14)
    check("heat_budget", "uniform bit bound", Q(2**14, 2**97) == Q(1,2**83))
    check("heat_budget", "gamma tail exponent", Q(15*22,2*7) < 24 and 3**24 < 2**39)
    check("heat_budget", "counterfeit count slack", Q(4,10)+Q(2,100**2) < 1)
    for t in (Q(1,100), Q(1,10), Q(1), Q(2)):
        f = [1/t, Q(0), Q(1)]
        # derivative f(B)e^(-t B^2), divided by the exponential.
        der = [Q(0), Q(2)]
        residual = poly_add(der, poly_mul([Q(0), -2*t], f))
        check("heat_budget", f"Gaussian primitive {t}", residual == [0, 0, 0, -2*t])

    families = [
        ([Q(1,3),Q(2,3)], [[Q(1,5),Q(2,5),Q(3,7)],[Q(1,2),Q(3,4),Q(5,6)]]),
        ([Q(1,4),Q(1,2),Q(1,4)], [[Q(0)]*4, [Q(1,7),Q(2,9),Q(3,11),Q(4,13)],
                                  [Q(2,7),Q(4,9),Q(6,11),Q(8,13)]]),
        ([Q(1)], [[Q(1,2),Q(1,3),Q(1,5),Q(1,7)]])]
    for k, (weights, states) in enumerate(families):
        direct = trace_from_pgf(mixed_pgf(weights, states), 7)
        connected = cumulant_traces(weights, states, 7)
        for n, (x,y) in enumerate(zip(direct, connected), 1):
            check("connected_cumulants", f"family{k} order{n}", x == y)

    weights = [Q(1,2),Q(1,2)]
    ys = [Q(0), Q(2)]
    v, b = Q(1), Q(5,4)
    for i in range(6):
        ci, cj = Q((2*i+1)**2), Q((2*i+3)**2)
        ps = [v*y/(ci+b*y) for y in ys]
        qs = [v*y/(cj+b*y) for y in ys]
        ep = sum(w*p for w,p in zip(weights, ps))
        eq = sum(w*p for w,p in zip(weights, qs))
        epq = sum(w*p*qj for w,p,qj in zip(weights, ps,qs))
        cov = epq-ep*eq
        sym = sum((weights[k]*weights[l]*(ps[k]-ps[l])*(qs[k]-qs[l])/2
                   for k,l in product(range(2),repeat=2)),Q(0))
        check("marked_covariance", f"strict covariance {i}", cov == sym and cov > 0)
        pp = mixed_pgf(weights, list(zip(ps,qs)))
        disc = pp[1]**2-4*pp[0]*pp[2]
        check("marked_covariance", f"discriminant identity {i}", disc == (ep-eq)**2-4*cov)
        if i >= 2:
            check("marked_covariance", f"complex pair {i}", disc < 0)
    check("marked_covariance", "Hermitian DPP control", Q(3,16)-Q(1,2)**2 == -Q(1,16))

    # Finite high-mode control of the same variance inequality (not a native tail run).
    cs = [Q((2*j+1)**2) for j in range(100,116)]
    ss, rr = sum((1/c for c in cs),Q(0)), sum((1/c**2 for c in cs),Q(0))
    mu = [sum((v*y/(c+b*y) for c in cs),Q(0)) for y in ys]
    eq2 = sum((w*sum(((v*y/(c+b*y))**2 for c in cs),Q(0)) for w,y in zip(weights,ys)),Q(0))
    em = sum(w*m for w,m in zip(weights,mu))
    excess = sum(w*m*m for w,m in zip(weights,mu))-em*em-eq2
    lower = v*v*(ss*ss-2*rr-2*b*ss*rr*4)  # V=1, M2=2, M3=4.
    check("high_mode_tail", "finite variance bound", excess >= lower > 0)
    for L in (Q(1),Q(3,2),Q(5),Q(100)):
        check("high_mode_tail", f"ratio bound {L}", 1/(3*L)+1/L**2 <= 4/(3*L))

    fake_pgf = [Q(1,4),Q(9,20),Q(1,4),Q(1,20)]
    fake = trace_from_pgf(fake_pgf, 24)
    w = [Q(2),Q(3,5)]
    for n in range(2,25):
        w.append(Q(3,5)*w[-1]-Q(1,10)*w[-2])
    for n in range(1,25):
        check("bernstein_counterexample", f"power recurrence {n}", fake[n-1] == Q(1,2)**n+w[n])
    bad = hausdorff(fake,0,14)
    check("bernstein_counterexample", "negative mixed difference", bad == Q(-433316717939,10**15))
    check("bernstein_counterexample", "b0 sample only", all(x > 0 for x in fake))

    kappas = [Q(1,2), Q(1,3), Q(1,7)]
    real_ps = [sum((k**n for k in kappas),Q(0)) for n in range(1,18)]
    for a in range(6):
        for bb in range(8):
            target = sum((k**(a+1)*(1-k)**bb for k in kappas),Q(0))
            check("hausdorff", f"real spectral {a},{bb}", hausdorff(real_ps,a,bb) == target >= 0)
    for a in range(7):
        for bb in range(9):
            left = [Q((-1)**j*comb(bb,j), factorial(a+j)) for j in range(bb+1)]
            right = [Q(factorial(bb),factorial(a+bb))*Q((-1)**j*comb(a+bb,bb-j),factorial(j))
                     for j in range(bb+1)]
            check("laguerre", f"coefficient identity {a},{bb}", left == right)

    for m in (2,5,10,100):
        pol = pgf_of_probs([Q(1,m)]*m)
        shifted_pol = shifted(pol,Q(1))
        for n in range(min(m,5)+1):
            check("exterior_limit", f"Poisson escape {m},{n}", shifted_pol[n] == Q(comb(m,n),m**n))

    for weights, states in [([Q(-1),Q(2)],[[Q(1,2)],[Q(1,3)]]),
                             ([Q(1,2)],[[Q(1,2)]]),
                             ([Q(1)],[[Q(3,2)]])]:
        try:
            mixed_pgf(weights,states)
        except ValueError:
            check("refusal", "invalid probability", True)
        else:
            raise ArithmeticError("Invalid probability fixture accepted")
    return {"status":"PASS_ASTRA_THETA_COUNT_EXACT", "arithmetic":"EXACT_RATIONAL",
            "checks_by_group":dict(sorted(counts.items())), "checks_total":sum(counts.values()),
            "quartet_source_margin":str(margin), "fake_H_0_14":str(bad),
            "analytic_theorems_machine_proved":False, "native_theta_sweep":False,
            "complete_zero_census":False, "rh_proved":False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check",type=Path,help="Recompute and compare a complete retained JSON result")
    args = parser.parse_args()
    result = run()
    if args.check is not None:
        old = json.loads(args.check.read_text(encoding="utf-8"))
        if json.dumps(old, sort_keys=True, separators=(",", ":")) != json.dumps(
                result, sort_keys=True, separators=(",", ":")):
            raise ArithmeticError("Retained result differs from fresh exact computation")
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__ == "__main__":
    main()
