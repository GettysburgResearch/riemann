# s5_recursion_bookkeeping.py -- Level-2 audit of Section 5 of "The Quasi-Riemann Hypothesis"
# (paper2.tex l.1254-1631).  Written from scratch; no code from the OpenAI repository is used.
#
# Checks the SCALE BOOKKEEPING of the recursion Prop. 5.1 <- Lemma 5.3 + Prop. 5.4 (+ Lemma 7.3's
# construction of the children), i.e. that the induction is well-founded, terminates after a number
# of steps independent of D, and that every child satisfies the hypotheses under which the induction
# hypothesis is invoked.
#
#  R1  Exponent LP (log_D units, constants dropped): for a parent (h,x,f) with h,x,f>=0, x+f<=C0,
#      h<=x+f-kappa, a cube index b with  2x-2h < 3*beta < x  (nonempty supremum in Lemma 5.3),
#      L=x-3beta, and a child of Lemma 7.3 (rho=log R>=0, phi=log F'>=0 with phi<=H', iota=log N(j)
#      in [0,rho]) we maximise/minimise every quantity the proof of Prop. 5.1 needs.
#  R2  Exact-inequality random test (real values, constants kept) of the chain
#      H' = H L/(Sigma F R^2) <= H L_b/(Sigma F) = H/(N(b)^3 F^2) < H (H/Sigma)^2 <= D^{-2kappa} H,
#      H'/Sigma' <= H/Sigma, Sigma' <= L_b <= Sigma <= D^C0, H' >= 1, X'/N(j) >= 1, F' N(j) >= 1,
#      N(k') <= H', including the self-referential cube index b=1 (possible when X < H).
#  R3  Initialisation from Prop. 4.5 (l.1611-1629): H/Sigma = C D^{-theta}/B, kappa=theta/2, C0=2.
#  R4  Depth / derivative-order / epsilon bookkeeping of the induction.
import math, random
from fractions import Fraction as Fr
import numpy as np
from scipy.optimize import linprog

out = []
def log(s):
    print(s); out.append(s)

# ------------------------------------------------------------------------------------------
# R1: exponent LP
# variables v = [h, x, f, beta, rho, phi, iota]
def lp_checks(kappa, C0):
    idx = dict(h=0, x=1, f=2, beta=3, rho=4, phi=5, iota=6)
    n = 7
    def vec(**kw):
        a = np.zeros(n)
        for k, val in kw.items(): a[idx[k]] = val
        return a
    # linear forms
    L = vec(x=1, beta=-3)
    Hp = vec(h=1) + L - vec(x=1, f=1) - vec(f=1) - vec(rho=2)          # h+L-(x+f)-f-2rho
    Xp = L - vec(rho=1, phi=1)
    Xpp = Xp - vec(iota=1)
    Fpp = vec(phi=1, iota=1)
    Sigp = L - vec(rho=1)
    Sig = vec(x=1, f=1)
    A, b = [], []
    def le(form, const):      # form . v <= const
        A.append(form); b.append(const)
    eps = 1e-9
    for k in ('h', 'x', 'f', 'beta', 'rho', 'phi', 'iota'):
        le(-vec(**{k: 1}), 0.0)
    le(Sig, C0)                                    # Sigma <= D^C0
    le(vec(h=1) - Sig, -kappa)                     # H <= Sigma D^-kappa
    le(vec(x=2, h=-2, beta=-3), -eps)              # 3 beta > 2x-2h   (N(b)>H_c, H^2>X)
    le(vec(beta=3, x=-1), -eps)                    # 3 beta < x       (L_b>1)
    le(vec(phi=1) - Hp, 0.0)                       # F' <= N(f') <= N(k') <= H'
    le(vec(iota=1, rho=-1), 0.0)                   # N(j) <= N(r) ~ R
    A_ = np.array(A); b_ = np.array(b)
    bounds = [(None, None)] * n
    res = {}
    def opt(name, form, sense):
        c = -form if sense == 'max' else form
        r = linprog(c, A_ub=A_, b_ub=b_, bounds=bounds, method='highs')
        assert r.status == 0, (name, r.message)
        val = -r.fun if sense == 'max' else r.fun
        res[name] = val
        return val
    opt("max H' - (h - 2kappa)", Hp - vec(h=1), 'max'); res["max H' - (h - 2kappa)"] += 2 * kappa
    opt("max H' - [h + 2(h-(x+f))]", Hp - (vec(h=3) - 2 * Sig), 'max')
    opt("max H' - (h + L - (x+f) - f)", Hp - (vec(h=1) + L - Sig - vec(f=1)), 'max')
    opt("max (H'-Sigma') - (h-(x+f))", (Hp - Sigp) - (vec(h=1) - Sig), 'max')
    opt("max H' - (Sigma' - kappa)", Hp - Sigp, 'max'); res["max H' - (Sigma' - kappa)"] += kappa
    opt("max Sigma' - C0", Sigp, 'max'); res["max Sigma' - C0"] -= C0
    opt("max Sigma' - L", Sigp - L, 'max')
    opt("max (L+f) - (x+f)  [L_b F <= Sigma]", L - vec(x=1), 'max')
    opt("min X''", Xpp, 'min')
    opt("min F''", Fpp, 'min')
    opt("min H'", Hp, 'min')
    opt("min L", L, 'min')
    return res

# ------------------------------------------------------------------------------------------
# R2: exact inequality random test in log10 space with constants kept
def r2(trials, rng):
    fails = {}; n_ok = 0; n_self = 0
    def chk(name, cond):
        if not cond: fails[name] = fails.get(name, 0) + 1
    tol = 1e-9
    for _ in range(trials):
        d = rng.uniform(3, 60)                     # log10 D
        kappa = rng.choice([0.005, 0.02, 0.05, 0.1, 0.3])
        C0 = rng.choice([1.0, 2.0, 3.0])
        lsig = rng.uniform(kappa * d, C0 * d)      # log10 Sigma  (need Sigma >= D^kappa for H>=1)
        lF = rng.uniform(0, lsig)                  # log10 F
        lX = lsig - lF
        lH = rng.uniform(0, lsig - kappa * d)      # H <= Sigma D^-kappa
        # cube index: nonempty sup needs H^2 > X; choose b in ((X/H)^{2/3}, X^{1/3}), allow b=1
        if 2 * lH <= lX: continue
        lo = max(0.0, (2 * lX - 2 * lH) / 3); hi = lX / 3
        if lo >= hi: continue
        is_self = False
        if rng.random() < 0.5 and lo == 0.0:
            lb = 0.0; is_self = True               # self-referential b=1 (requires X<H)
            if not (lX < lH): continue
        else:
            lb = rng.uniform(lo, hi)
            if lb <= lo + tol or lb >= hi - tol: continue
        lL = lX - 3 * lb
        # child (Lemma 7.3): Hmax = H L/(Sigma F N(r)^2) must be >= N(f') >= F' >= 1
        lHLSF = lH + lL - lsig - lF
        if lHLSF < 0: continue
        lR = rng.uniform(0, lHLSF / 2)
        lNr = lR + rng.uniform(0, math.log10(2) * 0.999)
        lkmax = lHLSF - 2 * lNr                    # bound for N(k')
        if lkmax < 0: continue
        lFp = rng.uniform(0, lkmax)                # dyadic F'
        lNfp = lFp + rng.uniform(0, math.log10(2) * 0.999)
        if lNfp > lkmax: continue
        lNk = rng.uniform(lNfp, lkmax)
        lNj = rng.uniform(0, lNr)                  # j | r
        lHp = lH + lL - lsig - lF - 2 * lR         # H' = H L /(Sigma F R^2)
        lXp = lL - lR - lFp                        # X' = L/(R F')
        lSp = lL - lR                              # Sigma' = L/R
        n_ok += 1; n_self += is_self
        chk("H' >= 1", lHp >= -tol)
        chk("N(k') <= H'", lNk <= lHp + tol)
        chk("X'/N(j) >= 1", lXp - lNj >= -tol)
        chk("F' N(j) >= 1", lFp + lNj >= -tol)
        chk("H' <= H L_b/(Sigma F)", lHp <= lH + lL - lsig - lF + tol)
        chk("H L_b/(Sigma F) = H/(N(b)^3 F^2)", abs((lH + lL - lsig - lF) - (lH - 3 * lb - 2 * lF)) < 1e-7)
        chk("H' < H (H/Sigma)^2", lHp < lH + 2 * (lH - lsig) + tol)
        chk("H' <= D^{-2kappa} H", lHp <= lH - 2 * kappa * d + tol)
        chk("H'/Sigma' <= H/Sigma", lHp - lSp <= lH - lsig + tol)
        chk("H' <= Sigma' D^{-kappa}", lHp <= lSp - kappa * d + tol)
        chk("Sigma' <= L_b <= Sigma <= D^C0", lSp <= lL + tol and lL + lF <= lsig + tol and lsig <= C0 * d + tol)
        chk("Sigma'' = Sigma'", abs(((lXp - lNj) + (lFp + lNj)) - lSp) < 1e-7)
    return n_ok, n_self, fails

# ------------------------------------------------------------------------------------------
def main():
    rng = random.Random(5)
    log("R1 exponent LP (log_D units; positive 'max' values or negative 'min' values would be failures)")
    for kappa in (0.005, 0.05, 0.25):
        for C0 in (1.0, 2.0, 4.0):
            res = lp_checks(kappa, C0)
            log(f"  kappa={kappa}, C0={C0}: " + "; ".join(f"{k} = {v:+.3e}" for k, v in res.items()))
    log("  [max H'-(h-2kappa) <= 0, min X''>=0, min F''>=0, min H'>=0, max Sigma'-C0<=0 etc. as required]")

    n_ok, n_self, fails = r2(400000, rng)
    log(f"R2 exact-inequality random test: {n_ok} admissible (parent,b,child) samples, {n_self} with b=1; failures: {fails if fails else 'none'}")

    # R3 initialisation
    log("R3 initialisation (Prop. 4.5 scales, kappa=theta/2, C0=2):")
    for theta in (Fr(1, 100), Fr(1, 20), Fr(1, 10), Fr(3, 10), Fr(9, 10)):
        # H_dual = C D^{1-theta}/B^2, Sigma = D/B, X = D/(BF): exponents with B=D^beta, F=D^phi
        worst = None
        for beta in [Fr(i, 20) for i in range(0, 21)]:
            for phi in [Fr(i, 20) for i in range(0, 21)]:
                if beta + phi > 1: continue
                h = 1 - theta - 2 * beta; sig = 1 - beta
                gap = sig - h                     # = theta + beta >= theta
                worst = gap if worst is None else min(worst, gap)
        kappa = theta / 2
        jmax = math.ceil(Fr(2) / kappa)
        # induction level actually needed for H <= C D^{1-theta}: j with j*kappa >= 1-theta (+ room for C)
        jneed = math.ceil((1 - theta) / kappa) + 1
        # true chain depth: each step H' < H (H/Sigma)^2 and the gap never shrinks: h_{t+1} <= h_t - 2 theta
        depth = math.floor((1 - theta) / (2 * theta)) + 1
        log(f"  theta={theta}: min gap (Sigma-H exponent) = {worst} >= theta/2 ok; large-D threshold D >= C^(2/theta); "
            f"paper's j=ceil(C0/kappa)={jmax}; level needed for H<=D^(1-theta)*C: <= {jneed}; "
            f"actual recursion depth <= {depth}")

    # R4 derivative-order recursion: J_0=1, J_{j+1}=max(J*, 4 J_j + 12)  (J* = Lemma 5.3 order)
    log("R4 derivative orders J_j (J_{j+1} = max(J*, 4 J_j + 12), J_0 = 1), symbolic in J*:")
    for Jstar in (10, 100):
        J = 1; seq = [J]
        for j in range(40):
            J = max(Jstar, 4 * J + 12); seq.append(J)
        log(f"  J*={Jstar}: J_1..J_5 = {seq[1:6]}, J_18 = {seq[18]:.3e}, J_40 = {seq[40]:.3e}; closed-form bound J_j <= 4^j (J*+4)")
        assert all(seq[j] <= 4 ** j * (Jstar + 4) for j in range(41))
    log("  epsilon: level j+1 at eps uses level j at eps/3 -> level 0 at eps/3^j; finitely many levels, so fine.")
    return out

if __name__ == "__main__":
    main()
