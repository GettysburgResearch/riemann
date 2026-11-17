#!/usr/bin/env python3
"""C3 adjudicator: small independent checks of disputed or load-bearing items.

Sections (labels in FINAL.md):
 oliva_algebra   sympy: Oliva v1 (3)  <=>  (1-1/p) loglog N_{n+1} >= loglog N_n   (exact symbolic)
 oliva_H         Arb: H(L) = (1-1/p)log L - log(L - log p) is decreasing and H(p) > 0 (spot balls), and the
                 failure bound at p in [exp(727.25), exp(727.951332668)], E = theta(p)-p >= 1e152:
                 upper bound  y^2/(2(1-y)) - E(1+(1-1/p)log p)/(p+E)^2  < 0  (y = log p / p).
 cheng_graham    numpy longdouble, pairwise-free direct sum: |S| for the C3-CG1 example.
 dh              mpmath (non-rigorous): Davenport-Heilbronn coefficients from first principles,
                 functional-equation residual, |f| at the certified zero.
 zeta19          mpmath (non-rigorous): |zeta_19| at the certified zero and Re > 1.
 micheas         Arb: t_2 - 1/4 > t_1 from the certified TSV balls.
Usage: python3 adj_misc_checks.py TSV out.json
"""
import sys, json, time, math
t0 = time.time()
tsv = sys.argv[1]; out = sys.argv[2]
res = {}

# --- oliva_algebra
import sympy as sp
c, L1, L0, q = sp.symbols('c L1 L0 q', positive=True)   # c=e^-gamma, L1=loglogN_{n+1}, L0=loglogN_n, q=1/p
lhs = (1 - c / L1 - q) / (1 - c / L0); rhs = 1 - q
# (3): lhs >= rhs.  Multiply by (1 - c/L0) > 0  (true for large n since L0 -> oo):
diff = sp.simplify((lhs - rhs) * (1 - c / L0))
target = sp.simplify(c * ((1 - q) * L1 - L0) / (L0 * L1))
res["oliva_algebra"] = {"(lhs-rhs)*(1-c/L0)": str(diff), "c((1-q)L1-L0)/(L0 L1)": str(target),
                        "identical": bool(sp.simplify(diff - target) == 0),
                        "conclusion": "(3) <=> (1-1/p) L1 >= L0, i.e. (1-1/p) loglog N_{n+1} >= loglog N_n; c and A_n drop out"}

# --- oliva_H
import flint
from flint import arb
flint.ctx.prec = 256
def H(L, p): return (1 - 1 / p) * L.log() - (L - p.log()).log()
spots = {}
for p in [5, 7, 101, 17991383, 10**12, 139 * 10**15]:
    P = arb(p); y = P.log() / P
    hp = H(P, P)
    spots[str(p)] = {"H(p)": hp.str(8), "lower_bound_y^2/2": (y * y / 2).str(8), "H(p)>y^2/2": bool(hp > y * y / 2)}
res["oliva_H_spots"] = spots
# failure bound: worst case over log p in [727.25, 727.951332668] (p > x/2 by Bertrand), E >= 1e152, E <= 7.5e-7 p
lo, hi = arb(727.25), arb('727.951332668')
logp = arb.union(lo, hi)          # ball covering the whole range
P = logp.exp(); y = logp / P
E = arb(10) ** 152
# p^2 * [ y^2/(2(1-y)) - E(1+(1-1/p)log p)/(p+E)^2 ]  <=  logp^2/(2(1-y)) - E(1+(1-1/p)log p)/(1+7.5e-7)^2
scaled = logp * logp / (2 * (1 - y)) - E * (1 + (1 - 1 / P) * logp) / (1 + arb('7.5e-7')) ** 2
res["oliva_failure_bound"] = {"logp_ball": logp.str(12), "logp_lower": logp.lower().str(12), "logp_upper": logp.upper().str(12),
                              "p^2_times_upper_bound_for_H": scaled.str(8), "negative": bool(scaled < 0),
                              "note": "valid for E in [1e152, 7.5e-7 p] (Platt-Trudgian Cor. 2: theta(x) < (1+7.5e-7)x); "
                                      "H is decreasing in E, so larger E only helps"}

# --- cheng_graham
import numpy as np
th = np.longdouble('0.02'); w = np.longdouble('0.05')
def f(x):
    x = np.longdouble(x); z = (x - 1000) / w
    sp_ = np.where(z > 40, z, np.log1p(np.exp(np.minimum(z, 40))))
    return th * x + (1 - 2 * th) * w * sp_
n = np.arange(975, 1026, dtype=np.longdouble)
ph = 2 * np.pi * (f(n) % 1)
Sre = np.sum(np.cos(ph)); Sim = np.sum(np.sin(ph))
res["cheng_graham"] = {"|S|_longdouble": float(np.hypot(Sre, Sim)), "1/(pi theta)+1": float(1 / (np.pi * th) + 1),
                       "cot(pi theta/2)": float(1 / np.tan(np.pi * th / 2)), "num_terms": int(n.size)}

# --- dh and zeta19 (mpmath, non-rigorous)
import mpmath as mp
mp.mp.dps = 40
s5 = mp.sqrt(5)
kappa = (mp.sqrt(10 - 2 * s5) - 2) / (s5 - 1)
a = [1, kappa, -kappa, -1, 0]
def fdh(s): return sum(a[j] * mp.zeta(s, mp.mpf(j + 1) / 5) for j in range(5)) * mp.power(5, -s)
def Lam(s): return mp.power(5 / mp.pi, s / 2) * mp.gamma((s + 1) / 2) * fdh(s)
fe = []
for s in [mp.mpc('0.3', '7.1'), mp.mpc('0.81', '85.7'), mp.mpc('-1.2', '3.3')]:
    fe.append(float(abs(Lam(s) - Lam(1 - s)) / abs(Lam(s))))
z_dh = mp.mpc('0.808517182456637385553351961', '85.699348485377592171929267709')
res["dh"] = {"kappa": mp.nstr(kappa, 20), "fe_rel_residuals": fe, "|f(z_dh)|": mp.nstr(abs(fdh(z_dh)), 5),
             "|f'(z_dh)|": mp.nstr(abs(mp.diff(fdh, z_dh)), 8), "Re z - 1/2": mp.nstr(z_dh.real - 0.5, 12)}
z19 = mp.mpc('1.0010955115364762904215', '600884.2034277757127423323526')
F19 = sum(mp.power(k, -z19) for k in range(1, 20))
res["zeta19"] = {"|zeta_19(z)|": mp.nstr(abs(F19), 5), "Re z": mp.nstr(z19.real, 22)}

# --- micheas
rows = []
for line in open(tsv):
    fl = line.split()
    if int(fl[0]) <= 2: rows.append(arb(fl[1], fl[2]))
    else: break
gap = rows[1] - arb('0.25') - rows[0]
res["micheas"] = {"t1": rows[0].str(20), "t2": rows[1].str(20), "t2-1/4-t1": gap.str(10), "positive": bool(gap > 0)}

res["versions"] = {"python": sys.version.split()[0], "python_flint": flint.__version__, "mpmath": mp.__version__,
                   "numpy": np.__version__, "sympy": sp.__version__}
res["runtime_s"] = round(time.time() - t0, 1)
json.dump(res, open(out, 'w'), indent=1); print(json.dumps(res, indent=1))
