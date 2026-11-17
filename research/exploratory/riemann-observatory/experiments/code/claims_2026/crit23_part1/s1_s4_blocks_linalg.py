"""CRIT23 Level-2 audit, part 1: steps S1 (encoding, conjugation symmetry), S3 (block/inertia structure) and
S4 (rank-trace inequality) of Alpoge-Furman arXiv:2608.13637v2, checked on the ACTUAL AF matrix G~ built from
synthetic conjugation-invariant zero configurations, plus a spectral comparison with Lamzouri's (arXiv:2609.02882v2)
kernel matrix, plus an optimisation-based adversarial search against AF Lemma 3.2 and checks of every
intermediate inequality in its proof.

Non-rigorous floating point. Synthetic configurations are NOT zeta zeros; they test finite algebraic statements
(Prop 4.1, Lemma 3.1, Lemma 3.2, the Section 6 chain) that AF assert for every conjugation-invariant configuration.
Run:  python3 -I s1_s4_blocks_linalg.py   (from this directory; deterministic seeds)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from scipy.optimize import minimize
from af_testfn import TestFunction, HatTable, grid

rng = np.random.default_rng(2026_11_17)
TOL = 1e-9


def config(rng, n1, n2, npairs, lo, hi, depth_max, min_sep=None, cluster=False):
    """zeros as (beta, gamma, m); on-line simple (n1), on-line multiple (n2), off-line pairs (npairs, both members)."""
    Z = []
    def draw():
        return rng.uniform(lo, hi)
    used = []
    def sep_ok(g):
        return min_sep is None or all(abs(g - u) >= min_sep for u in used)
    k = 0
    while k < n1:
        g = draw() if not cluster else rng.uniform(lo, lo + 1.5)
        if sep_ok(g):
            Z.append((0.5, g, 1)); used.append(g); k += 1
    k = 0
    while k < n2:
        g = draw()
        if sep_ok(g):
            Z.append((0.5, g, int(rng.integers(2, 4)))); used.append(g); k += 1
    k = 0
    while k < npairs:
        g = draw() if not cluster else rng.uniform(lo, lo + 1.5)
        if sep_ok(g):
            y = rng.uniform(1e-3, depth_max)               # |beta - 1/2| = y < 1/2
            m = int(rng.integers(1, 4))
            Z.append((0.5 + y, g, m)); Z.append((0.5 - y, g, m)); used.append(g); k += 1
    return Z


def gamma_rho(beta, gam):
    # AF Section 1.2: gamma_rho = (rho - 1/2)/i with rho = beta + i gamma
    return ((beta - 0.5) + 1j * gam) / 1j


def analyse(tf, alphas, Z, label, out):
    L, a = tf.L, tf.a
    aL2 = a * L * L
    d = len(alphas)
    g = np.array([gamma_rho(b, t) for (b, t, m) in Z])
    mult = np.array([m for (_, _, m) in Z])
    # v_rho = (phihat(gamma_rho - alpha_k))_k ; one FFT table per distinct imaginary part (validated in __main__)
    V = np.empty((len(Z), len(alphas)), dtype=complex)
    tabs = {}
    for j, gj in enumerate(g):
        y = float(np.round(gj.imag, 15))
        if y not in tabs:
            tabs[y] = HatTable(tf.L, tf.window, y)
        V[j] = tabs[y](gj.real - alphas)
    # ---- S1: functional-equation pairing v_{1-conj(rho)} = conj(v_rho), real <=> beta = 1/2
    s1_err = 0.0
    for j, (b, t, m) in enumerate(Z):
        if b != 0.5:
            partner = [i for i, (b2, t2, m2) in enumerate(Z) if t2 == t and abs(b2 - (1 - b)) < 1e-15][0]
            s1_err = max(s1_err, np.max(np.abs(V[partner] - np.conj(V[j]))))
            assert mult[partner] == m
        else:
            s1_err = max(s1_err, np.max(np.abs(V[j].imag)))
    G = (V.T * mult) @ V / aL2                           # sum_rho m v v^T / (aL^2)   (bilinear, NOT v v^*)
    imagG = np.max(np.abs(G.imag)); G = G.real
    asym = np.max(np.abs(G - G.T))
    on = np.array([b == 0.5 for (b, _, _) in Z])
    on1 = on & (mult == 1)
    P = (V[on].T * mult[on]) @ V[on] / aL2; P = P.real
    P1 = (V[on1].T) @ V[on1] / aL2; P1 = P1.real
    Q = G - P
    Qp = G - P1
    s1 = int(on1.sum()); s2 = int((on & (mult >= 2)).sum()); p = int((~on).sum() // 2)
    N = int(mult.sum())
    eP = np.linalg.eigvalsh(P); eP1 = np.linalg.eigvalsh(P1)
    eQ = np.linalg.eigvalsh(Q); eQp = np.linalg.eigvalsh(Qp); eG = np.linalg.eigvalsh(G)
    scale = max(1.0, np.max(np.abs(eG)))
    thr = 1e-8 * scale
    rankP = int((eP > thr).sum()); rankP1 = int((eP1 > thr).sum())
    npQ = int((eQ > thr).sum()); npQp = int((eQp > thr).sum())
    trG = np.trace(G); hs = np.sum(G * G); trP1 = np.trace(P1)
    # pair-block structure (S3): trace 2m*(1 - truncation), signature (1,1)
    pair_info = []
    for j, (b, t, m) in enumerate(Z):
        if b > 0.5:
            A = V[j].real; B = V[j].imag
            blk = 2 * m * (np.outer(A, A) - np.outer(B, B)) / aL2
            ev = np.linalg.eigvalsh(blk)
            pair_info.append((b - 0.5, m, np.trace(blk) / (2 * m), A @ B / aL2,
                              (A @ A - B @ B) / aL2, ev[-1], ev[0], int((ev > 1e-10).sum()), int((ev < -1e-10).sum())))
    # Lemma 3.2 with (P1, Q'), r = s1 (>= rank P1), b = s2 + p (>= n+(Q'))
    lem32_slack = s1 - (2 * trP1 + 4 * np.trace(Qp) - 4 * (s2 + p) - hs)
    chain_i = s1 - (4 * trG - 2 * N - hs)                     # AF (1.2) with finite-configuration N
    chain_ii = 2 * (s1 + s2 + p) - (4 * trG - hs - N)          # AF Section 6 (ii)
    # Lamzouri kernel matrix on the same configuration: K(z - s) with z = i(rho - 1/2)L/2pi; equals
    # L * (phi^2)^(gamma_rho - gamma_rho') / (a L^2) for eta^2(u) := L phi(Lu)^2 / ||phi||^2 (exact, full lattice)
    do_lz = len(Z) <= 60
    if do_lz:
        sm = np.sqrt(mult)
        M = sm[:, None] * sm[None, :] * (L * tf.hat_phi2(g[:, None] - g[None, :])) / aL2
        eM = np.linalg.eigvals(M)
        eM_sorted = np.sort(eM.real)[::-1]
        eG_top = np.sort(eG)[::-1][:len(Z)]
        spec_diff = np.max(np.abs(eM_sorted - eG_top))
        trM = np.trace(M).real; hsM = np.sum(M * M).real
    else:
        spec_diff = 0.0
    out.append(f"[{label}] window={tf.window} L={L} d={d} distinct={len(Z)} N={N} s1={s1} s2={s2} p={p}")
    out.append(f"   S1: max|v_(1-conj rho) - conj v_rho| (or |Im v| on-line) = {s1_err:.2e};  max|Im G~| = {imagG:.2e}; max|G~-G~^T| = {asym:.2e}")
    out.append(f"   S3: min eig P = {eP.min():.2e} (>= -tol), rank P = {rankP} vs #on distinct = {int(on.sum())}; "
               f"n+(Q) = {npQ} <= p = {p}; n+(Q') = {npQp} <= s2+p = {s2+p}; tr P1 = {trP1:.6f} <= s1 = {s1}")
    for (y, m, trn, ab, diff, emax, emin, npos, nneg) in pair_info[:4]:
        out.append(f"      pair depth |beta-1/2|={y:.3f} m={m}: trace/(2m)={trn:.8f}, <a,b>/aL2={ab:.1e}, (|a|^2-|b|^2)/aL2={diff:.8f}, "
                   f"eig range [{emin:.3f}, {emax:.3f}], signature ({npos},{nneg})")
    out.append(f"   S5(trace, interior): tr G~ = {trG:.8f} vs N = {N};  ||G~||_HS^2 = {hs:.6f}")
    out.append(f"   S4: Lemma 3.2 slack (P1,Q') = {lem32_slack:.6f} (>=0);  chain (i) slack s1-(4trG-2N-HS) = {chain_i:.6f};  "
               f"chain (ii) slack = {chain_ii:.6f}")
    if do_lz:
        out.append(f"   LZ cross-check: tr K-matrix = {trM:.8f}, sum K^2 = {hsM:.6f}; max |eig(G~) - eig(K-matrix)| = {spec_diff:.2e}; "
                   f"max|Im eig(K)| = {np.max(np.abs(eM.imag)):.1e}")
    ok = (s1_err < 1e-12 and imagG < 1e-10 and eP.min() > -1e-9 * scale and rankP <= int(on.sum()) and npQ <= p
          and npQp <= s2 + p and trP1 <= s1 + 1e-9 and lem32_slack > -1e-8 and chain_i > -1e-6 and chain_ii > -1e-6)
    return ok, spec_diff, lem32_slack


def part_configs(out):
    out.append("=" * 100)
    out.append("PART A. Actual AF matrices G~ (eq. 2.10) from synthetic conjugation-invariant configurations")
    out.append("=" * 100)
    allok = True; worst_spec = 0.0; worst_slack = np.inf
    L = 6.0; d = 200; alphas = grid(0.0, L, d)        # grid covers [0, 208]; points placed in [70, 140]
    for window in ("flat", "MT"):
        tf = TestFunction(L, window, zmax=80.0)
        cases = [
            ("separated, shallow pairs", dict(n1=22, n2=4, npairs=6, lo=70, hi=140, depth_max=0.05, min_sep=1.2)),
            ("separated, deep pairs", dict(n1=18, n2=3, npairs=8, lo=70, hi=140, depth_max=0.49, min_sep=1.2)),
            ("dense random", dict(n1=30, n2=4, npairs=10, lo=70, hi=140, depth_max=0.49)),
            ("tight cluster (spacing << 1/L)", dict(n1=6, n2=0, npairs=3, lo=100, hi=101.5, depth_max=0.3, cluster=True)),
        ]
        for (lab, kw) in cases:
            Z = config(rng, **kw)
            ok, sd, sl = analyse(tf, alphas, Z, lab, out)
            allok &= ok
            if "cluster" not in lab:
                worst_spec = max(worst_spec, sd)
            worst_slack = min(worst_slack, sl)
        # random sweep
        nrand = 60
        for it in range(nrand):
            kw = dict(n1=int(rng.integers(0, 40)), n2=int(rng.integers(0, 5)), npairs=int(rng.integers(0, 15)),
                      lo=70, hi=float(rng.uniform(72, 140)), depth_max=float(rng.uniform(0.01, 0.49)))
            if kw["n1"] + kw["n2"] + kw["npairs"] == 0:
                continue
            Z = config(rng, **kw)
            tmp = []
            ok, sd, sl = analyse(tf, alphas, Z, "rand", tmp)
            allok &= ok
            worst_slack = min(worst_slack, sl)
        out.append(f"   [{window}] random sweep of {nrand} configurations: all assertions hold = {allok}")
    out.append(f"PART A summary: all S1/S3/S4 assertions hold = {allok}; min Lemma 3.2 slack = {worst_slack:.4f}; "
               f"max spectral mismatch AF G~ vs LZ K-matrix (non-cluster) = {worst_spec:.2e}")
    return allok


# ---------------------------------------------------------------------------------------------------------------
def lemma31_random(out, trials=3000):
    worst = 0
    for _ in range(trials):
        m = int(rng.integers(1, 7)); dd = int(rng.integers(1, 8))
        H = rng.normal(size=(m, m)) + 1j * rng.normal(size=(m, m)); H = (H + H.conj().T) / 2
        A = rng.normal(size=(m, dd)) + 1j * rng.normal(size=(m, dd))
        if rng.uniform() < 0.3:
            A[:, 0] = A[:, 1 % dd]        # rank-deficient maps too
        npH = int((np.linalg.eigvalsh(H) > 1e-10).sum())
        npB = int((np.linalg.eigvalsh(A.conj().T @ H @ A) > 1e-9).sum())
        worst = max(worst, npB - npH)
    out.append(f"Lemma 3.1 (n+(A* Q0 A) <= n+(Q0)), {trials} random complex instances: max violation = {worst} (must be <= 0)")
    return worst <= 0


def lemma32_proof_steps(out, trials=20000):
    """Check every displayed inequality inside AF's proof of Lemma 3.2 on random Hermitian instances."""
    worst = dict(vN=np.inf, step1=np.inf, step2=np.inf, step3=np.inf, final=np.inf)
    for _ in range(trials):
        d = int(rng.integers(1, 9)); r = int(rng.integers(0, d + 1)); b = int(rng.integers(0, d + 1))
        X = (rng.normal(size=(d, r)) + 1j * rng.normal(size=(d, r))) * rng.uniform(0.1, 2.5)
        P = X @ X.conj().T
        U, _ = np.linalg.qr(rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d)))
        ev = -np.abs(rng.normal(size=d)) * rng.uniform(0, 3)
        k = min(b, d); pos = rng.choice(d, size=k, replace=False)
        ev[pos] = np.abs(rng.normal(size=k)) * rng.uniform(0, 5)
        Q = U @ np.diag(ev) @ U.conj().T
        w, Uq = np.linalg.eigh(Q)
        Qp = (Uq * np.maximum(w, 0)) @ Uq.conj().T; Qm = (Uq * np.maximum(-w, 0)) @ Uq.conj().T
        p_ = np.sort(np.linalg.eigvalsh(P))[::-1]; n_ = np.sort(np.maximum(-w, 0))[::-1]
        q_ = w[w > 0]
        hs = lambda A: np.real(np.trace(A @ A.conj().T))
        trPQm = np.real(np.trace(P @ Qm))
        worst["vN"] = min(worst["vN"], np.dot(p_, n_) - trPQm)                         # von Neumann
        lhs1 = hs(P) - 2 * trPQm + hs(Qm)
        mid = np.sum((p_ - n_) ** 2)
        worst["step1"] = min(worst["step1"], lhs1 - mid)
        rhs2 = np.sum(2 * (p_[:r] - n_[:r]) - 1) + np.sum(n_[r:] ** 2)
        worst["step2"] = min(worst["step2"], mid - rhs2)
        worst["step3"] = min(worst["step3"], rhs2 - (2 * np.real(np.trace(P)) - r - 4 * np.real(np.trace(Qm))))
        worst["final"] = min(worst["final"], r - (2 * np.real(np.trace(P)) + 4 * np.real(np.trace(Q)) - 4 * b - hs(P + Q)))
        assert len(q_) <= b
    out.append("Lemma 3.2 proof steps on %d random Hermitian instances (min of LHS-RHS, all must be >= 0 up to rounding):" % trials)
    for k_, v in worst.items():
        out.append(f"   {k_:6s}: {v:.3e}")
    return all(v > -1e-9 for v in worst.values())


def lemma32_adversarial(out, starts=400):
    """Minimise the slack r - (2trP + 4trQ - 4b - ||P+Q||^2) over real P = X X^T (rank <= r) and
    Q = Y Y^T - Z Z^T (n+(Q) <= b), with L-BFGS from random starts."""
    best = np.inf; best_case = None
    for s in range(starts):
        d = int(rng.integers(2, 7)); r = int(rng.integers(0, d + 1)); b = int(rng.integers(0, d + 1)); c = int(rng.integers(1, d + 1))
        nX, nY, nZ = d * r, d * b, d * c
        def unpack(x):
            X = x[:nX].reshape(d, r); Y = x[nX:nX + nY].reshape(d, b); Zm = x[nX + nY:].reshape(d, c)
            return X, Y, Zm
        def f(x):
            X, Y, Zm = unpack(x)
            P = X @ X.T; Q = Y @ Y.T - Zm @ Zm.T; S = P + Q
            val = r - (2 * np.trace(P) + 4 * np.trace(Q) - 4 * b - np.sum(S * S))
            # gradient
            gS = 2 * S                                  # d||S||^2/dS
            gP = -2 * np.eye(d) + gS                    # d(-2trP + ||S||^2)/dP  (val = r - 2trP - 4trQ + 4b + ||S||^2)
            gQ = -4 * np.eye(d) + gS
            gX = 2 * gP @ X; gY = 2 * gQ @ Y; gZ = -2 * gQ @ Zm
            return val, np.concatenate([gX.ravel(), gY.ravel(), gZ.ravel()])
        x0 = rng.normal(size=nX + nY + nZ) * rng.uniform(0.2, 2.0)
        res = minimize(f, x0, jac=True, method="L-BFGS-B", options=dict(maxiter=3000, gtol=1e-12, ftol=1e-15))
        if res.fun < best:
            best = res.fun; best_case = (d, r, b, c)
    out.append(f"Lemma 3.2 adversarial L-BFGS search, {starts} starts (d<=6): min slack found = {best:.3e} at (d,r,b,#neg)={best_case} "
               f"(0 is attained by the stated equality case; negative beyond rounding would refute the lemma)")
    return best > -1e-8


def equality_case_exact(out):
    import sympy as sp
    d = 7; r = 2; b = 3
    P = sp.diag(1, 1, 0, 0, 0, 0, 0); Q = sp.diag(0, 0, 2, 2, 2, 0, 0)
    S = P + Q
    rhs = 2 * P.trace() + 4 * Q.trace() - 4 * b - (S * S).trace()
    out.append(f"Lemma 3.2 equality case P=Pi1 (rank {r}), Q=2 Pi2 (rank {b}), exact sympy: r - RHS = {sp.nsimplify(r - rhs)}")
    # AF Section 7.2(b) extremal configuration, per unit N: 2/3 simple orthogonal on-line (eig 1), 1/6 doubles (eig 2)
    s1 = sp.Rational(2, 3); s2 = sp.Rational(1, 6)
    tr = s1 * 1 + s2 * 2; hs = s1 * 1 + s2 * 4
    out.append(f"AF 7.2(b) extremal (per N): tr = {tr}, HS^2 = {hs}, s1 = {s1}, distinct = {s1 + s2}; "
               f"certificate (i) 4tr-2-HS = {4*tr - 2 - hs}, (ii) (4tr-HS-1)/2 = {(4*tr - hs - 1)/2}")
    return (r - rhs) == 0


def validate_tables(out):
    tf = TestFunction(6.0, "MT", zmax=200.0)
    worst = 0.0
    for y in (0.0, 0.2, -0.37, 0.49):
        tab = HatTable(6.0, "MT", y)
        xs = np.linspace(-190, 190, 397) + 0.0137
        worst = max(worst, np.max(np.abs(tab(xs) - tf.hat(xs + 1j * y))))
    out.append(f"HatTable (FFT+spline) vs direct quadrature, |x|<=190, y in {{0,.2,-.37,.49}}: max abs error = {worst:.1e}")


if __name__ == "__main__":
    out = []
    validate_tables(out)
    okA = part_configs(out)
    out.append("=" * 100)
    out.append("PART B. Linear algebra lemmas in isolation")
    out.append("=" * 100)
    okB1 = lemma31_random(out)
    okB2 = lemma32_proof_steps(out)
    okB3 = lemma32_adversarial(out)
    okB4 = equality_case_exact(out)
    out.append(f"OVERALL: PART A ok={okA}; Lemma 3.1 ok={okB1}; Lemma 3.2 steps ok={okB2}; adversarial ok={okB3}; equality exact={okB4}")
    print("\n".join(out))
