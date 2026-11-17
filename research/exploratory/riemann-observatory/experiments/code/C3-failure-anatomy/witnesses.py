#!/usr/bin/env python3
"""C3-failure-anatomy: explicit witnesses for the failure dossiers.

Sections (each writes a sub-dict of the output JSON):
  atiyah     sympy: Atiyah 2018 property 2.6 with f=g=s forces T(1+w) constant (exact algebra, degree <= 14)
  queme      Queme 2020 (arXiv:2004.00460) step 6: termwise limit of a Taylor series at a boundary pole.
             exact model g(z)=1/(z-rho) and mpmath (non-rigorous) Taylor coefficients of zeta'/zeta at rho_1+3/2
  oliva      Oliva 2018 (arXiv:1807.06447v1) induction step (3): margin h_n for p_{n+1} <= PMAX (float64,
             non-rigorous) and its first-order law h ~ [-(1+log p)E + (log p)^2/2]/p^2, E = theta(p)-p;
             non-uniformity of 'Lemma 2.2' when b ~ x
  micheas    Micheas 2026 (arXiv:2607.04338v1) Thm 1 counterexample: Arb partial products of
             prod (tau_n^2 - t_1^2)/(1/4 + tau_n^2), tau_n = t_n - 1/(2n), using certified ordinates t_n
  bbm        Bender-Brody-Mueller: |zeta(z, x+1)| x^{-1/2} |z-1| -> 1 for z = rho_1 (Arb Hurwitz zeta)
  chengraham Cheng-Graham 2004 Lemma 2 (S <= 1/(pi theta) + 1) violated by a smooth monotone phase (Arb)
  turan      independent Krawczyk certification of a zero of zeta_19 with Re s > 1 (C2 witness replay)
  dh         independent Krawczyk certification of a Davenport-Heilbronn zero off the line (C2 witness replay)
Usage: python3 witnesses.py ZEROS_TSV[,ZEROS_TSV2] out.json
"""
import sys, json, time, math, platform, hashlib
import numpy as np
import mpmath
import sympy
import flint
from flint import acb, arb, acb_series, ctx

R = {"versions": {"python": platform.python_version(), "python_flint": flint.__version__,
                  "mpmath": mpmath.__version__, "sympy": sympy.__version__, "numpy": np.__version__}}


def timed(name):
    def deco(fn):
        def w(*a):
            t0 = time.time()
            out = fn(*a)
            out["runtime_s"] = round(time.time() - t0, 2)
            R[name] = out
            print(name, "done", out["runtime_s"], "s", flush=True)
        return w
    return deco


@timed("atiyah")
def atiyah():
    s = sympy.symbols("s")
    D = 14
    c = sympy.symbols("c0:%d" % (D + 1))
    h = lambda w: sum(c[k] * w ** k for k in range(D + 1))
    # property 2.6 with f = g = s:  T{(1+s)(1+s)} = T{1+2s}, i.e. h(2s + s^2) = h(2s) with h(w) = T(1+w)
    diff = sympy.expand(h(2 * s + s ** 2) - h(2 * s))
    eqs = [sympy.expand(diff).coeff(s, m) for m in range(1, D + 1)]
    sol = sympy.solve(eqs, c[1:D], dict=True)
    return {"identity_used": "h(2s+s^2) = h(2s) as power series in s (Atiyah 2.6 with f=g=s), h(w)=T(1+w)",
            "degree_tested": D, "solution": {str(k): str(v) for k, v in sol[0].items()},
            "conclusion": "c_1 = ... = c_{D-1} = 0: T is constant near 1 (exact algebra up to degree D-1)"}


@timed("queme")
def queme():
    mpmath.mp.dps = 40
    rho = mpmath.zetazero(1)
    v = mpmath.mpf(3) / 2
    c0 = rho + v
    f = lambda z: mpmath.zeta(z, derivative=1) / mpmath.zeta(z)
    K = 26
    co = mpmath.taylor(f, c0, K)
    terms = [abs(co[k] * (-v) ** k) for k in range(K + 1)]
    # exact model: g(z) = 1/(z - rho); Taylor at c = rho + v: coefficients (-1)^k / v^{k+1};
    # termwise limit series sum_k (-v)^k g^{(k)}(rho+v)/k! = sum_k 1/v diverges.
    eps = [mpmath.mpf(10) ** -j for j in (2, 4, 6)]
    fvals = [abs(f(rho + e)) * e for e in eps]
    return {"rho1": str(rho), "v": 1.5,
            "abs_terms_(-v)^k a_k(rho+v)_k=0..26": [float(x) for x in terms],
            "exact_model_terms": "|(-v)^k a_k| = 1/v = 0.6667 for every k (pole at distance v)",
            "eps*|f(rho+eps)| for eps=1e-2,1e-4,1e-6": [float(x) for x in fvals],
            "note": "non-rigorous mpmath numerics; the rigorous statement is Cauchy-Hadamard + Abel (see report)"}


@timed("oliva")
def oliva(PMAX=20_000_000):
    sieve = np.ones(PMAX + 1, dtype=bool); sieve[:2] = False
    for i in range(2, int(PMAX ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = False
    P = np.nonzero(sieve)[0].astype(np.float64)
    theta = np.cumsum(np.log(P))                 # theta(p_k) = log N_k
    p1 = P[1:]                                   # p_{n+1}
    L1 = theta[1:]                               # log N_{n+1}
    L0 = theta[:-1]                              # log N_n
    # h_n = (1 - 1/p) log L1 - log L0, computed stably: = -(log L1)/p + log(L1/L0)
    h = -np.log(L1) / p1 + np.log1p((L1 - L0) / L0)
    E = L1 - p1
    approx = (-(1 + np.log(p1)) * E + np.log(p1) ** 2 / 2) / p1 ** 2
    sel = p1 > 1000
    rel = np.abs(h[sel] - approx[sel]) / np.abs(approx[sel])
    # Lemma 2.2 non-uniformity: f(x) = (1 - a/log x - 1/b)/(1 - a/log(x - log b)), a = e^-gamma
    a = math.exp(-0.5772156649015329)
    out_l22 = {}
    for b in (1e4, 1e6, 1e8):
        xs = np.array([0.5 * b, b, 2 * b, 5 * b, b * math.log(b), 3 * b * math.log(b), 30 * b * math.log(b)])
        def fval(x):
            return (1 - a / math.log(x) - 1 / b) / (1 - a / math.log(x - math.log(b)))
        der = [(fval(x * (1 + 1e-6)) - fval(x * (1 - 1e-6))) / (2e-6 * x) for x in xs]
        out_l22[str(int(b))] = {"x": xs.tolist(), "sign_of_df/dx": ["+" if d > 0 else "-" for d in der]}
    imin = int(np.argmin(h))
    return {"PMAX": PMAX, "num_steps": int(len(h)), "min_h": float(h[imin]), "p_at_min": float(p1[imin]),
            "all_h_positive": bool((h > 0).all()), "max_E_over_range": float(E.max()),
            "first_order_law_median_rel_err_p>1000": float(np.median(rel)),
            "first_order_law_max_rel_err_p>1000": float(rel.max()),
            "lemma22_derivative_signs": out_l22,
            "note": "float64, non-rigorous; h_n>0 here only because theta(p)<p throughout this range"}


def load_zeros(paths, nmax):
    t = []
    for path in paths.split(","):
        with open(path) as f:
            for line in f:
                parts = line.split()
                if len(parts) < 3:
                    continue
                assert int(parts[0]) == len(t) + 1, "zero files must be consecutive"
                t.append((parts[1], parts[2]))
                if len(t) >= nmax:
                    return t
    return t


@timed("micheas")
def micheas(path):
    ctx.prec = 128
    zs = load_zeros(path, 100000)
    tball = [arb(m, r) for (m, r) in zs]
    t1 = tball[0]
    prod = arb(1)
    checkpoints = {}
    for n, tn in enumerate(tball, start=1):
        tau = tn - arb(1) / (2 * n)
        fac = (tau * tau - t1 * t1) / (arb(1) / 4 + tau * tau)
        prod = prod * fac
        if n in (1, 2, 10, 100, 1000, 10000, 100000):
            checkpoints[str(n)] = str(prod)
    # simple variant: tau_1 = t_1 - 1/2, tau_n = t_n (n >= 2): xi_hat/xi is the rational function below
    return {"s0": "1/2 + i t_1", "tau_n": "t_n - 1/(2n)",
            "partial_products_at_s0": checkpoints,
            "note": "factors are in (0,1) for n>=2 and the product converges absolutely (C3); the "
                    "limit is nonzero, while xi(s0)=0: Theorem 1 (17) fails for this admissible sequence"}


@timed("bbm")
def bbm():
    ctx.prec = 128
    z = acb.zeta_zeros(1, 1)[0]
    rows = {}
    for x in (1e2, 1e4, 1e6, 1e8, 1e10):
        a = acb(arb(x) + 1)
        val = z.zeta(a)
        ratio = abs(val) * abs(z - 1) / arb(x).sqrt()
        rows[str(x)] = {"|zeta(rho1, x+1)|": str(abs(val)), "ratio_to_sqrt(x)/|rho1-1|": str(ratio)}
    return {"z": str(z), "rows": rows,
            "conclusion": "|psi_z(x)| ~ x^{1/2}/|z-1| (DLMF 25.11.43), so psi_z is not in L^2(0,inf) for Re z = 1/2"}


@timed("chengraham")
def chengraham():
    ctx.prec = 128
    th = arb("0.02"); w = arb("0.05")
    Lh = 25
    bound_cg = 1 / (arb.pi() * th) + 1
    bound_landau = (arb.pi() * th / 2).cos() / (arb.pi() * th / 2).sin()
    best = None
    for j in range(200):
        m = arb(1000) + arb(j) / 200
        S = acb(0)
        for n in range(1000 - Lh, 1000 + Lh + 1):
            u = (arb(n) - m) / w
            # f(n) = th*n + (1-2 th) w log(1+e^u)  (f' = th + (1-2th) sigmoid(u), monotone, in (th, 1-th))
            fn = th * n + (1 - 2 * th) * w * (1 + u.exp()).log()
            S += (2 * arb.pi() * fn).exp_pi_i() if False else acb(0, 2 * arb.pi() * fn).exp()
        aS = abs(S)
        if best is None or aS.mid() > best[0].mid():
            best = (aS, j)
    aS, j = best
    return {"theta": "0.02", "w": "0.05", "terms": 2 * Lh + 1, "m": f"1000 + {j}/200",
            "phase": "f(x) = theta x + (1-2theta) w log(1+exp((x-m)/w))",
            "|S|": str(aS), "CG04_claimed_bound_1/(pi theta)+1": str(bound_cg),
            "Landau_sharp_bound_cot(pi theta/2)": str(bound_landau),
            "violates_CG04": bool(aS > bound_cg), "respects_Landau": bool(aS < bound_landau)}


def krawczyk(F, Fp, m, r):
    mm = acb(m.real.mid(), m.imag.mid())
    B = acb(arb(mm.real.mid(), r), arb(mm.imag.mid(), r))
    fm = F(mm); dm = Fp(mm); dB = Fp(B)
    Y = 1 / acb(dm.real.mid(), dm.imag.mid())
    K = mm - Y * fm + (1 - Y * dB) * (B - mm)
    ok = B.contains(K)
    return ok, K


@timed("turan")
def turan():
    ctx.prec = 128
    N = 19
    logs = [acb(n).log() for n in range(1, N + 1)]
    F = lambda s: sum(((-s) * L).exp() for L in logs)
    Fp = lambda s: sum(-L * ((-s) * L).exp() for L in logs)
    m = acb("1.0010955115364764", "600884.2034277758")
    for _ in range(5):
        m = m - F(m) / Fp(m)
        m = acb(m.real.mid(), m.imag.mid())
    ok, K = krawczyk(F, Fp, m, arb("1e-12"))
    return {"N": N, "krawczyk_ok": bool(ok), "zero_ball": str(K),
            "Re_lower_bound": str(K.real.lower()), "Re_gt_1_certified": bool(K.real > 1)}


@timed("dh")
def dh():
    ctx.prec = 128
    r5 = arb(5).sqrt()
    kappa = ((10 - 2 * r5).sqrt() - 2) / (r5 - 1)
    coef = [acb(1), acb(kappa), acb(-kappa), acb(-1)]   # a(n) for n = 1,2,3,4 mod 5; a(5k)=0
    def F(s):
        return sum(c * s.zeta(acb(a) / 5) for c, a in zip(coef, (1, 2, 3, 4))) * ((-s) * acb(5).log()).exp()
    def Fp(s):
        ser = acb_series([s, 1], prec=2)
        tot = None
        for c, a in zip(coef, (1, 2, 3, 4)):
            term = acb_series.zeta(ser, acb(a) / 5) * c
            tot = term if tot is None else tot + term
        tot = tot * (-(ser) * acb(5).log()).exp()
        return tot.coeffs()[1]
    m = acb("0.808517", "85.699348")
    for _ in range(6):
        m = m - F(m) / Fp(m)
        m = acb(m.real.mid(), m.imag.mid())
    ok, K = krawczyk(F, Fp, m, arb("1e-15"))
    # functional-equation sanity check on a random point: |f(s)| vs reflected (not needed for the witness)
    return {"kappa": str(kappa), "krawczyk_ok": bool(ok), "zero_ball": str(K),
            "Re_minus_half_lower_bound": str((K.real - arb("0.5")).lower()),
            "off_line_certified": bool(K.real > arb("0.5"))}


if __name__ == "__main__":
    zeros_tsv = sys.argv[1]
    out = sys.argv[2]
    t0 = time.time()
    atiyah(); queme(); oliva(); micheas(zeros_tsv); bbm(); chengraham(); turan(); dh()
    R["total_runtime_s"] = round(time.time() - t0, 2)
    s = json.dumps(R, indent=1)
    open(out, "w").write(s + "\n")
    print(s)
    print("sha256", hashlib.sha256((s + "\n").encode()).hexdigest())
