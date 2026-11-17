#!/usr/bin/env python3
"""C3 adjudicator: failure rate of the de Branges/Conrey-Li zero condition at larger heights.

For each start index n0 in a list, take the k consecutive zeros n0..n0+k-1 (from the certified TSV
when n0+k-1 <= 100000, otherwise from flint.acb.zeta_zeros(n0, k), which certifies the index), and
decide the sign of P_n = -Re{xi'(rho_n) xi(1+rho_n)} via the exact reformulation of adj_debranges_S.py:
    failure  <=>  sin(pi*X_n) > 0,   X_n = S(g_n) - delta_n - 3/4.
Arb balls (128 bits): the per-zero verdicts are NUMERICAL-RIGOROUS. The block failure RATE is a finite
statistic; the comparison with a Gaussian model for S is HEURISTIC (no theorem is claimed).

Gaussian comparisons (HEURISTIC): (a) with m, V the empirical mean/variance of S(g_n) in the block,
    rate_a = mean_n P( (G - delta_n) mod 2 in (3/4, 7/4) ),  G ~ N(m, V) independent of delta_n;
(b) with mY, VY the empirical mean/variance of Y_n = S(g_n) - delta_n,
    rate_b = P( G mod 2 in (3/4, 7/4) ),  G ~ N(mY, VY).
(a) ignores the correlation between S(g_n) and arg zeta(3/2+i g_n); (b) keeps it.

Usage: python3 adj_debranges_highblocks.py k n0,n0,... TSV1,TSV2 out.json
"""
import sys, json, time, math
import flint
from flint import arb, acb

k = int(sys.argv[1]); starts = [int(x) for x in sys.argv[2].split(',')]
tsvs = sys.argv[3].split(','); out = sys.argv[4]
flint.ctx.prec = 128
PI = arb.pi(); LOGPI = PI.log()

def tsv_block(n0, k):
    zs = []
    for p in tsvs:
        for line in open(p):
            f = line.split(); n = int(f[0])
            if n0 <= n < n0 + k: zs.append((n, arb(f[1], f[2])))
    return zs

def verdict(n, t):
    th = acb(arb(0.25), t / 2).lgamma().imag - t / 2 * LOGPI
    a = acb(arb(1.5), t).zeta().arg()
    c = (acb(arb(0.75), t / 2).lgamma().imag - acb(arb(0.25), t / 2).lgamma().imag - PI / 4
         + (t / arb(1.5)).atan() + (t / arb(0.5)).atan() - PI)
    S = arb(n) - arb(1.5) - th / PI
    delta = (a + c) / PI
    X = S - delta - arb(0.75)
    s = (PI * X).sin()
    v = 'fail' if s > 0 else ('pass' if s < 0 else 'undetermined')
    return v, float(S.mid()), float(delta.mid()), float(t.mid()), float(t.rad())

def Phi(x): return 0.5 * math.erfc(-x / math.sqrt(2))

def wrapped_fail_prob(mu, sd):
    # P( Y mod 2 in (3/4, 7/4) ), Y ~ N(mu, sd^2)
    p = 0.0
    for j in range(-60, 61):
        lo = 0.75 + 2 * j; hi = 1.75 + 2 * j
        p += Phi((hi - mu) / sd) - Phi((lo - mu) / sd)
    return p

res = {"script": "adj_debranges_highblocks.py", "k": k, "prec_bits": 128,
       "versions": {"python": sys.version.split()[0], "python_flint": flint.__version__}, "blocks": []}
for n0 in starts:
    t0 = time.time()
    if n0 + k - 1 <= 100000:
        zs = tsv_block(n0, k); src = 'TSV (acb.zeta_zeros, precomputed)'
    else:
        zl = flint.acb.zeta_zeros(n0, k); src = 'flint.acb.zeta_zeros(n0,k)'
        zs = [(n0 + i, z.imag) for i, z in enumerate(zl)]
    tz = time.time() - t0
    rows = [verdict(n, t) for n, t in zs]
    nf = sum(1 for r in rows if r[0] == 'fail'); nu = sum(1 for r in rows if r[0] == 'undetermined')
    Ss = [r[1] for r in rows]; m = sum(Ss) / len(Ss); V = sum((x - m) ** 2 for x in Ss) / len(Ss)
    model = sum(wrapped_fail_prob(m - r[2], math.sqrt(V)) for r in rows) / len(rows)
    Ys = [r[1] - r[2] for r in rows]; mY = sum(Ys) / len(Ys); VY = sum((y - mY) ** 2 for y in Ys) / len(Ys)
    ds = [r[2] for r in rows]; md = sum(ds) / len(ds); Vd = sum((d - md) ** 2 for d in ds) / len(ds)
    cov = sum((r[1] - m) * (r[2] - md) for r in rows) / len(rows)
    modelY = wrapped_fail_prob(mY, math.sqrt(VY))
    blk = {"n0": n0, "k": len(rows), "zero_source": src, "t_first": rows[0][3], "t_last": rows[-1][3],
           "max_ordinate_radius": max(r[4] for r in rows),
           "fail": nf, "undetermined": nu, "rate": round(nf / len(rows), 4),
           "binomial_se": round(math.sqrt(max(nf, 1) * (len(rows) - nf) / len(rows) ** 3), 4),
           "mean_S": round(m, 4), "var_S": round(V, 4),
           "selberg_var_(1/2pi^2)loglogT": round(math.log(math.log(rows[-1][3])) / (2 * math.pi ** 2), 4),
           "gaussian_S_model_rate_(S~N(m,V)_indep_of_delta)": round(model, 4),
           "mean_Y=S-delta": round(mY, 4), "var_Y": round(VY, 4), "corr(S,delta)": round(cov / math.sqrt(V * Vd), 4),
           "gaussian_Y_model_rate_(Y~N(mY,VY))": round(modelY, 4),
           "runtime_zeros_s": round(tz, 1), "runtime_total_s": round(time.time() - t0, 1)}
    res["blocks"].append(blk); print(json.dumps(blk), flush=True)
    json.dump(res, open(out, 'w'), indent=1)
