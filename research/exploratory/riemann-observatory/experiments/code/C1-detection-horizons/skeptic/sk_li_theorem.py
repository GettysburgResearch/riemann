#!/usr/bin/env python3
"""SKEPTIC check of C1-L1 / C1-L2 (Theorem L1: RH(T), T>=100 => lambda_n>0 for n<=T^2).
Independent of the investigator's code. Checks:
 (A) quadruple identity z_{1-conj rho} = 1/conj(z_rho) and Re-sum formula (mpmath, random rho);
 (B) Lemma A: a <= |beta-1/2|/(gamma^2-1), phi bounds, on a dense grid (beta, gamma);
 (C) Lemma B: 1-cosh(x)cos(y) >= 0.4496 y^2 - 0.5639 x^2 on [0,0.5001]x[0,1.1] (fine grid + interval-style margin);
 (D) Rosser-based tail bounds via Stieltjes integration with Rosser's error E(t)=0.137log t+0.443loglog t+1.588;
 (E) worst-case stress model: actual first 100000 zeros, every zero above T moved to beta=1-1e-12 (delta~1/2);
     lambda_n computed exactly for the finite zero set (zeros above gamma_100000 dropped: in Regime II they only add
     positive terms, so dropping them makes the test stricter for n << gamma_100000); first n with lambda_n<0.
Numerical class: NUMERICAL-NONRIGOROUS (float64/mpmath); (C),(D) are grid checks, not proofs.
"""
import math, time, json, sys
import numpy as np, mpmath as mp
from scipy import integrate
t0 = time.time()
out = {}
# (A)
mp.mp.dps = 40
rng = np.random.default_rng(1)
errA = 0
for _ in range(200):
    b = mp.mpf(rng.uniform(0.01, 0.99)); g = mp.mpf(rng.uniform(14, 1e6))
    rho = mp.mpc(b, g); z = 1 - 1/rho; zr = 1 - 1/(1 - mp.conj(rho))
    errA = max(errA, abs(zr - 1/mp.conj(z)))
    # quadruple sum of Re(1-z^n)
    n = int(rng.integers(1, 10**6))
    zs = [1 - 1/r for r in (rho, mp.conj(rho), 1 - rho, 1 - mp.conj(rho))]
    S = sum(mp.re(1 - zz**n) for zz in zs)
    a = -mp.log(abs(z)); ph = mp.arg(z)
    S2 = 4*(1 - mp.cosh(n*a)*mp.cos(n*ph))
    # a formula
    d = b - mp.mpf(1)/2
    a_formula = -mp.log(1 - 2*d/((mp.mpf(1)/2 + d)**2 + g**2))/2
    errA = max(errA, abs(S - S2)/max(1, abs(S)), abs(abs(a) - abs(a_formula)))
out["A_max_err"] = float(errA)
# (B)
worst_a, worst_phi_hi, worst_phi_lo = 0.0, 0.0, 0.0
for b in np.linspace(0.001, 0.999, 300):
    for g in np.concatenate([np.linspace(14, 30, 200), np.geomspace(30, 1e7, 200)]):
        rho = complex(b, g); z = 1 - 1/rho
        a = abs(math.log(abs(z))); ph = abs(math.atan2(z.imag, z.real))
        worst_a = max(worst_a, a/(abs(b - 0.5)/(g*g - 1)) if b != 0.5 else 0)
        worst_phi_hi = max(worst_phi_hi, ph*g)
        worst_phi_lo = min(worst_phi_lo, ph - (1/g)*(1 - 1/(3*g*g)))
out["B_max_a_ratio(<=1 required)"] = worst_a
out["B_max_phi*gamma (<=1.0013 claimed)"] = worst_phi_hi
out["B_min_phi_minus_lower (>=0 required)"] = worst_phi_lo
# (C)
xs = np.linspace(0, 0.5001, 2001); ys = np.linspace(0, 1.1, 2201)
X, Y = np.meshgrid(xs, ys)
marg = 1 - np.cosh(X)*np.cos(Y) - (0.4496*Y**2 - 0.5639*X**2)
out["C_min_margin_LemmaB"] = float(marg.min()); out["C_argmin"] = [float(X.flat[marg.argmin()]), float(Y.flat[marg.argmin()])]
xx = np.linspace(1e-6, 0.50006, 5000)
out["C_max_(cosh x-1)/x^2 on [0,0.50006]"] = float(((np.cosh(xx) - 1)/xx**2).max())
yy = np.linspace(1e-6, 1.1, 5000)
out["C_min_(1-cos y)/y^2 on [0,1.1]"] = float(((1 - np.cos(yy))/yy**2).min())
# (D) Rosser tail bounds
E = lambda t: 0.137*math.log(t) + 0.443*math.log(math.log(t)) + 1.588
def up4(T):
    main = (math.log(T/(2*math.pi)) + 1/3)/(6*math.pi*T**3)
    err = 4*integrate.quad(lambda t: (E(t) + E(T))*t**-5, T, np.inf)[0]
    return main + err, 2/(3*math.pi*T**3)*(math.log(T/(2*math.pi)) + 1/3)
def lo2(n):
    main = (math.log(n/(2*math.pi)) + 1)/(2*math.pi*n)
    err = 2*integrate.quad(lambda t: (E(t) + E(n))*t**-3, n, np.inf)[0]
    return main - err, math.log(n/(2*math.pi))/(10*math.pi*n)
worstD = []
for T in np.geomspace(100, 1e13, 400):
    u, claim = up4(T); l, claimL = lo2(T)
    worstD.append((T, u/claim, claimL/l))
out["D_max_ratio_rigorous_upper/claimed_upper (<=1 needed)"] = max(w[1] for w in worstD)
out["D_max_ratio_claimed_lower/rigorous_lower (<=1 needed)"] = max(w[2] for w in worstD)
# final positivity inequality 0.894*L2 > 0.282*(1+1/(T^2-1))^2 * U4 at n=T^2 (worst case n=T^2 for L2 decreasing)
def final(T):
    U = up4(T)[0]*(1/(1 - 1/T**2))**2
    L = lo2(T*T)[0]
    return 0.894*L - 0.282*U
out["D_min_final_margin_scaled(T^2*margin) over T in [100,1e13]"] = min(final(T)*T*T for T in np.geomspace(100, 1e13, 200))
# (E) worst-case stress model
g = []
for f in ["/tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/data/zeros_1_50000.tsv",
          "/tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/data/zeros_50001_100000.tsv"]:
    g += [float(l.split()[1]) for l in open(f)]
g = np.array(g)
def stress(T, nmax, beta=1 - 1e-12):
    on = g[g <= T]; off = g[g > T]
    z_on = (1 - 1/(0.5 + 1j*on))
    rho = beta + 1j*off; z = 1 - 1/rho; zp = 1/np.conj(z)       # zp = z_{1-conj rho}
    w_on = np.ones_like(z_on); w = np.ones_like(z); wp = np.ones_like(zp)
    first_neg = None; minval = None; lam_at = {}
    for n in range(1, nmax + 1):
        w_on *= z_on; w *= z; wp *= zp
        if n % 4096 == 0:   # renormalise drift
            w_on /= np.abs(w_on)
        lam = 2*np.sum(1 - w_on.real) + np.sum(2 - w.real - wp.real)
        if n in (int(T*T), int(T*T*math.log(T)), int(2*T*T*math.log(T))): lam_at[n] = float(lam)
        if minval is None or lam < minval[1]: minval = (n, float(lam))
        if lam < 0:
            first_neg = n; break
    return first_neg, minval, lam_at
rowsE = []
for T, nmax in [(100.0, 300000), (150.0, 600000)]:
    t1 = time.time()
    fn, mv, la = stress(T, nmax)
    rowsE.append({"T": T, "T^2": T*T, "first_negative_n (all zeros above T at beta=1-1e-12)": fn,
                  "min_lambda_seen(n,val)": mv, "lambda_at_T^2,T^2logT,2T^2logT": la, "T^2 log T": T*T*math.log(T), "sec": round(time.time() - t1, 1)})
    print(rowsE[-1], flush=True)
out["E_stress"] = rowsE
out["runtime_s"] = time.time() - t0
print(json.dumps(out, indent=1))
json.dump(out, open("/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C1-detection-horizons/skeptic/sk_li_theorem.json", "w"), indent=1)
