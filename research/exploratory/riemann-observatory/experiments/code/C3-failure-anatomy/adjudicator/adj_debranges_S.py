#!/usr/bin/env python3
"""C3 adjudicator: the de Branges / Conrey-Li necessary zero condition rewritten through S(t).

Conrey-Li (IMRN 2000, Theorem 1 and Sec. 3.1): de Branges' positivity condition (3.1) on H(E),
E(z) = xi(1-iz), would force (Theorem 1, last clause, with rho = 1 - iw)
    P_n := -Re{ xi'(rho_n) xi(1+rho_n) } >= 0      at every zero rho_n = 1/2 + i g_n
(their value (3.2) is P_34 = -5.389...e-69 < 0),
with xi(s) = s(s-1) pi^{-s/2} Gamma(s/2) zeta(s) (no factor 1/2).

Identity used here (proof in FINAL.md, claim C3-ADJ-S):  if g_1 < ... < g_K are the first K
ordinates, all simple and on the line (true, and certified by acb.zeta_zeros / the TSV), then
    P_n >= 0   <=>   sin(pi*X_n) <= 0,      X_n := S(g_n) - delta_n - 3/4,
    S(g_n)   = n - 3/2 - theta(g_n)/pi      (S averaged at the jump),
    delta_n  = (a_n + c_n)/pi,  a_n = arg zeta(3/2+i g_n)  (principal; |a_n| <= log zeta(3/2) < 0.961),
    c_n      = [Im lgamma(3/4+i g/2) - Im lgamma(1/4+i g/2) - pi/4] + [arg(3/2+ig)+arg(1/2+ig) - pi].
So P_n < 0 (failure) iff X_n mod 2 lies in (0,1), i.e. iff S(g_n) - delta_n mod 2 lies in (3/4, 7/4).

The script evaluates X_n in Arb ball arithmetic (NUMERICAL-RIGOROUS given the certified ordinates),
and, for n <= KDIRECT, independently evaluates sign((-1)^{n+1} Im xi(3/2+i g_n)) with Gamma (not lgamma)
as an algebraic cross-check of the branch bookkeeping. It does NOT evaluate xi'(rho): the sign of
Z'(g_n) = (-1)^{n+1} follows from simplicity + correct indexing (Z(0) = zeta(1/2) < 0).

Usage: python3 adj_debranges_S.py K KDIRECT TSV1[,TSV2] out.json
"""
import sys, json, time, hashlib
import flint
from flint import arb, acb

K = int(sys.argv[1]); KDIRECT = int(sys.argv[2]); tsvs = sys.argv[3].split(','); out = sys.argv[4]
flint.ctx.prec = 128
PI = arb.pi(); LOGPI = PI.log()

def read_zeros(paths, K):
    zs = []
    for p in paths:
        for line in open(p):
            f = line.split()
            n = int(f[0])
            if n > K: return zs
            zs.append((n, arb(f[1], f[2]) if len(f) > 2 else arb(f[1])))
    return zs

def theta(t):
    return acb(arb(0.25), t / 2).lgamma().imag - t / 2 * LOGPI

def quantities(n, t):
    th = theta(t)
    a = acb(arb(1.5), t).zeta().arg()
    c1 = acb(arb(0.75), t / 2).lgamma().imag - acb(arb(0.25), t / 2).lgamma().imag - PI / 4
    c2 = (t / arb(1.5)).atan() + (t / arb(0.5)).atan() - PI
    S = arb(n) - arb(1.5) - th / PI
    delta = (a + c1 + c2) / PI
    X = S - delta - arb(0.75)
    s = (PI * X).sin()
    if s > 0: verdict = 'fail'
    elif s < 0: verdict = 'pass'
    else: verdict = 'undetermined'
    return verdict, S, a, c1 + c2, X

def direct_sign(n, t):
    s = acb(arb(1.5), t)
    xi = s * (s - 1) * acb(PI) ** (-s / 2) * (s / 2).gamma() * s.zeta()
    v = xi.imag * (1 if n % 2 == 1 else -1)
    if v > 0: return 'pass'
    if v < 0: return 'fail'
    return 'undetermined'

t0 = time.time()
zs = read_zeros(tsvs, K)
assert len(zs) == K and zs[-1][0] == K
fails = []; undet = []; mism = []; maxc = 0.0
Svals = []; Xfrac = []
for n, t in zs:
    v, S, a, c, X = quantities(n, t)
    if v == 'fail': fails.append(n)
    elif v == 'undetermined': undet.append(n)
    if n <= KDIRECT:
        d = direct_sign(n, t)
        if d != v: mism.append(n)
    if n >= 10: maxc = max(maxc, abs(float(c.mid())))
    Svals.append(float(S.mid())); Xfrac.append(float(X.mid()) % 2.0)

# blockwise statistics
import math
def block_stats(lo, hi):
    idx = range(lo - 1, hi)
    nf = sum(1 for i in idx if (i + 1) in fset)
    Ss = [Svals[i] for i in idx]
    m = sum(Ss) / len(Ss); var = sum((x - m) ** 2 for x in Ss) / len(Ss)
    return {"range": [lo, hi], "fail": nf, "rate": round(nf / len(Ss), 5),
            "mean_S": round(m, 5), "var_S": round(var, 5),
            "frac_S_lt_-0.25": round(sum(1 for x in Ss if x < -0.25) / len(Ss), 5)}
fset = set(fails)
blocks = []
B = 5000 if K >= 20000 else 500
for lo in range(1, K + 1, B):
    blocks.append(block_stats(lo, min(K, lo + B - 1)))
idx_str = ','.join(map(str, fails))
res = {
    "script": "adj_debranges_S.py", "K": K, "KDIRECT": KDIRECT, "prec_bits": 128,
    "versions": {"python": sys.version.split()[0], "python_flint": flint.__version__},
    "zero_source": tsvs,
    "num_fail": len(fails), "num_pass": K - len(fails) - len(undet), "undetermined": undet,
    "fail_count_n_le_2000": sum(1 for n in fails if n <= 2000),
    "fail_count_n_le_20000": sum(1 for n in fails if n <= 20000),
    "first_60_fail_indices": fails[:60],
    "direct_xi_crosscheck_mismatches_n_le_KDIRECT": mism,
    "max_abs_c_n_for_n_ge_10": maxc,
    "blocks": blocks,
    "fail_indices_sha256": hashlib.sha256(idx_str.encode()).hexdigest(),
    "fail_indices": fails if K <= 20000 else None,
    "runtime_s": round(time.time() - t0, 1),
}
json.dump(res, open(out, 'w'), indent=1)
print(json.dumps({k: v for k, v in res.items() if k not in ('fail_indices',)}, indent=1))
