"""CRIT23 Level-2 audit, part 2, step S9 (counting bookkeeping) and the bookkeeping half of S10 (Knausgard).

(a) sympy: every algebraic identity used to turn the spectral inequalities into counts:
    AF Section 6 (i)/(ii); Lamzouri Thm 1.1 constants C0, C1, C2 and the t = 2+sqrt2 balancing of (2.7);
    KN Thm 3.2 (mu, nu, r_h, r_k identities), Thm 5.1, Thm 6.2(a) identity 3-C-b+xs = 1+s, Thm 6.2(b)/(c) inequalities,
    the Chandru closed form at t = 2+sqrt(2-2x1), and the reduction of 6.2(b) at (0,0,0), c=2, t=2+sqrt2 to LZ C2.
(b) exact rational arithmetic (fractions) for all KN final constants and every numerical hypothesis of
    Thms 2.6, 3.2, 5.1/Prop 5.2, 6.2 as stated in KN (independent re-typing from the LaTeX source).
(c) randomised tests on the ACTUAL operator A = sum_z nu_z F_z <F_{zbar}, .> (nonzero spectrum = that of
    diag(nu) P Gram, Gram_{w,u} = K(u - conj w)), with KN's first-window kernel K and the MT kernel, for random
    conjugation-invariant configurations with on-line multiplicities 1..4 and off-line pairs of multiplicity 1..2:
      KN (eq:key) for c in {2, 3, 67/20}; KN (eq:key2); KN Lemma 6.1 (two levels, t >= c);
      the final count inequalities N0s >= 2N - trA^2, Nd >= (3N - trA^2)/2, Ns+N0 >= 3N - trA^2.
    Synthetic points are NOT zeta zeros: these test finite algebraic statements asserted for all configurations.

Run: python3 -I s9_counting.py"""
from fractions import Fraction as Fr
import numpy as np
import sympy as sp

rng = np.random.default_rng(2026_11_17_2)


def part_a():
    ok = []
    s1, s2, p, N, trG, HS, trP1 = sp.symbols('s1 s2 p N trG HS trP1')
    # AF (ii): 2(s1+s2+p) - (4trG - HS - N) = [3s1+4s2+4p-(4trG-HS)] + [N-(s1+2s2+2p)]
    ok.append(sp.simplify(2 * (s1 + s2 + p) - (4 * trG - HS - N) - ((3 * s1 + 4 * s2 + 4 * p - (4 * trG - HS)) + (N - (s1 + 2 * s2 + 2 * p)))) == 0)
    # AF (i): 2trP1 + 4(trG-trP1) - 4(s2+p) - HS = 4trG - HS - 2(trP1 + 2(s2+p))
    ok.append(sp.simplify(2 * trP1 + 4 * (trG - trP1) - 4 * (s2 + p) - HS - (4 * trG - HS - 2 * (trP1 + 2 * (s2 + p)))) == 0)
    # LZ constants
    CMT = sp.Rational(1, 2) + sp.cot(1 / sp.sqrt(2)) / sp.sqrt(2)
    C0 = sp.Rational(3, 2) - sp.cot(1 / sp.sqrt(2)) / sp.sqrt(2)
    ok.append(sp.simplify(C0 - (2 - CMT)) == 0)
    ok.append(sp.simplify((C0 + 1) / 2 - (sp.Rational(3, 2) - CMT / 2)) == 0)
    ok.append(sp.simplify((1 + 2 * sp.sqrt(2) + 2 * C0) / (3 + 2 * sp.sqrt(2)) - (5 + 2 * sp.sqrt(2) - 2 * CMT) / (3 + 2 * sp.sqrt(2))) == 0)
    # LZ (2.7) balancing: t^2-4t+2=0, b2=t^2/4, b3=t^2/4-1, b1=2-A+b3, check b1+b2=2t-A and final ratio
    A, t = sp.symbols('A t')
    tt = 2 + sp.sqrt(2)
    b2 = tt ** 2 / 4; b3 = tt ** 2 / 4 - 1; b1 = 2 - A + b3
    ok.append(sp.simplify(tt ** 2 - 4 * tt + 2) == 0)
    ok.append(sp.simplify(b1 + b2 - (2 * tt - A)) == 0)
    ok.append(sp.simplify(b2 - (sp.Rational(3, 2) + sp.sqrt(2))) == 0 and sp.simplify(b3 - (sp.Rational(1, 2) + sp.sqrt(2))) == 0)
    ok.append(sp.simplify(b1 / b2 - (5 + 2 * sp.sqrt(2) - 2 * A) / (3 + 2 * sp.sqrt(2))) == 0)
    # KN Thm 3.2
    c, x1, x2, b, C, x = sp.symbols('c x1 x2 b C x')
    mu = 2 - 2 * x1 + x2; nu = 2 * c - 3 + x1 - x2
    rh = 6 * c - 7 - c ** 2 + x1 - 2 * x2; rk = 4 * c - 2 - c ** 2 - 2 * x1
    ok.append(sp.expand(nu + mu - (2 * c - 1 - x1)) == 0)
    ok.append(sp.expand(2 * nu + mu - (4 * c - 4 - x2)) == 0)
    ok.append(sp.expand(3 * nu + mu - c ** 2 - rh) == 0)
    ok.append(sp.expand(2 * nu + 2 * mu - c ** 2 - rk) == 0)
    ok.append(sp.expand((2 * c - nu) - (3 - x1 + x2)) == 0)
    # KN eq:key from Lemma 2.1: 2cN - 2c(n1+2n2) + trphi - c^2 p, rewritten with trD^2 = n1 + 4 n2
    n1, n2, hk, trphi = sp.symbols('n1 n2 hk trphi')
    lhs = 2 * c * N - 2 * c * (n1 + 2 * n2) + trphi - c ** 2 * hk
    rhs = 2 * c * N - (2 * c - 1) * n1 - (4 * c - 4) * n2 - c ** 2 * hk + (trphi - (n1 + 4 * n2))
    ok.append(sp.expand(lhs - rhs) == 0)
    # KN Thm 6.2(a)
    s = (2 - C - b) / (1 - x)
    ok.append(sp.simplify(3 - C - b + x * s - (1 + s)) == 0)
    # KN Thm 6.2(b): 2t - t^2/3 - (4t - t^2)/2 = t^2/6 >= 0; e0 = 2t - t^2/4, 4t - t^2/2 = 2 e0
    e0 = 2 * t - t ** 2 / 4
    ok.append(sp.expand(2 * t - t ** 2 / 3 - (4 * t - t ** 2) / 2 - t ** 2 / 6) == 0)
    ok.append(sp.expand(4 * t - t ** 2 / 2 - 2 * e0) == 0)
    # Chandru closed form at t = 2 + sqrt(2-2x1)
    sq = sp.sqrt(2 - 2 * x1); tc = 2 + sq; e0c = 2 * tc - tc ** 2 / 4
    ok.append(sp.simplify((e0c - C - b) / (e0c - 1 - x1) - (1 - 2 * (C + b - 1 - x1) / (3 - x1 + 2 * sq))) == 0)
    ok.append(sp.simplify((4 * tc - tc ** 2) - (2 + 2 * x1)) == 0)
    # 6.2(b) at (0,0,0), t = 2+sqrt2 reduces to LZ C2
    e0l = 2 * tt - tt ** 2 / 4
    ok.append(sp.simplify((e0l - C) / (e0l - 1) - (5 + 2 * sp.sqrt(2) - 2 * C) / (3 + 2 * sp.sqrt(2))) == 0)
    # KN Cor 1.2: N >= Ns + 2(Nd - Ns)  =>  Ns >= 2Nd - N
    print(f"(a) sympy identities: {sum(ok)}/{len(ok)} hold")
    return all(ok)


def part_b():
    print("(b) KN constants and hypotheses in exact rational arithmetic")
    c = Fr(67, 20); th = Fr(17, 20)
    x1, x2, alpha, Om = Fr(54350, 10 ** 6), Fr(69433, 10 ** 6), Fr(6219, 10 ** 6), Fr(15882, 10 ** 6)
    b = 6 * alpha
    beta1 = Fr(8824337, 134217728)
    C0 = Fr(266541, 200000)
    mu = 2 - 2 * x1 + x2; nu = 2 * c - 3 + x1 - x2; rh = 6 * c - 7 - c * c + x1 - 2 * x2; rk = 4 * c - 2 - c * c - 2 * x1
    q = (3 - C0 + x2 - x1 - b) / mu
    print(f"   Thm 1.1: b = 6 alpha = {b} (= 0.037314: {b == Fr(37314, 10**6)}); mu={float(mu)}, nu={float(nu)}, r_h={float(rh)}, r_k={float(rk)}"
          f" -> all >= 0: {mu > 0 and nu >= 0 and rh >= 0 and rk >= 0}")
    print(f"            q = {q} = {float(q):.11f}; equals 1645064/1960733: {q == Fr(1645064, 1960733)}; Cor 1.2 2q-1 = {2*q-1} = {float(2*q-1):.8f}")
    sb = float(beta1) ** 0.5
    print(f"   Thm 2.6 hyps (window 1): beta={float(beta1):.8f}, 2+2sqrt(beta)={2+2*sb:.5f} < c={float(c)}: {2+2*sb < float(c)};"
          f" 2beta>=2x1: {2*beta1 >= 2*x1}; 4beta>=x1+x2: {4*beta1 >= x1+x2}; 8beta>=2x2: {8*beta1 >= 2*x2}")
    print(f"            r_k >= 0 iff c <= 2+sqrt(2-2x1) = {2+float(2-2*x1)**0.5:.5f}  (c = {float(c)})")
    # Theorem 1.3
    x, al2 = Fr(8722, 10 ** 6), Fr(627, 10 ** 6); b2 = 7 * al2; C0p = Fr(6639737, 5000000); beta2 = Fr(13707941, 2 ** 28)
    s0 = (2 - C0p - b2) / (1 - x)
    print(f"   Thm 1.3: b = 7 alpha = {b2} (= 0.004389: {b2 == Fr(4389, 10**6)}); s0 = {s0} = {float(s0):.8f}; equals 1669159/2478195: {s0 == Fr(1669159, 2478195)};"
          f" beta={float(beta2):.6f} >= x: {beta2 >= x}")
    # Theorem 1.4
    print(f"   Thm 1.4a: (1+s0)/2 = {(1+s0)/2} = {float((1+s0)/2):.8f}; equals 2073677/2478195: {(1+s0)/2 == Fr(2073677, 2478195)}")
    t = Fr(27, 8); e0 = 2 * t - t * t / 4
    v = (e0 - C0 - b) / (e0 - 1 - x1)
    print(f"   Thm 1.4b: t={t} >= c: {t >= c}; 4t-t^2 = {float(4*t-t*t)} >= 2+2x1 = {float(2+2*x1)}: {4*t-t*t >= 2+2*x1};"
          f" e0 = {e0}; 2-2x1+x2>=0: {mu >= 0}; value = {v} = {float(v):.8f}; equals 3376433/3797325: {v == Fr(3376433, 3797325)}")
    # Theorem 1.5
    x3, al3 = Fr(54525, 10 ** 6), Fr(6212, 10 ** 6); b3 = 6 * al3; C0pp = Fr(6662319, 5000000); beta3 = Fr(4483379, 2 ** 26)
    v3 = (e0 - C0pp - b3) / (e0 - 1 - x3)
    print(f"   Thm 1.5: b = 6 alpha = {b3} (= 0.037272: {b3 == Fr(37272, 10**6)}); 4t-t^2 >= 2+2x = {float(2+2*x3)}: {4*t-t*t >= 2+2*x3};"
          f" beta={float(beta3):.6f} >= x: {beta3 >= x3}; value = {v3} = {float(v3):.8f}; equals 50652159/56956375: {v3 == Fr(50652159, 56956375)}")
    print(f"   x <= 7/128 at t=27/8 (KN Remark): 7/128 = {7/128:.6f}, x3 = {float(x3)}: {x3 <= Fr(7, 128)}")


def sinc(z):
    z = np.asarray(z, dtype=complex)
    out = np.ones_like(z)
    nz = np.abs(z) > 1e-14
    out[nz] = np.sin(np.pi * z[nz]) / (np.pi * z[nz])
    return out


A1 = np.array([193305, -23105, 29166, 13952, -21009, 41052]) / 1e6


def K_kn1(z):
    out = sinc(z)
    for j, a in enumerate(A1, start=1):
        out = out + a / 2 * (sinc(z - j) + sinc(z + j))
    return out


S2 = np.sqrt(2.0)


def K_mt(z):
    z = np.asarray(z, dtype=complex); w = 2 * np.pi * z
    cst = 1 / (S2 * np.sin(1 / S2))

    def I(k):
        k = np.where(np.abs(k) < 1e-12, 1e-12, k)
        return 2 * np.sin(k / 2) / k
    return cst * 0.5 * (I(S2 + w) + I(S2 - w))


def phi_c(lam, c):
    return np.where(lam <= c, lam ** 2, 2 * c * lam - c * c)


def config(rng, spread):
    pts, nu, kind = [], [], []
    n1, n2, nh, k = rng.integers(0, 7), rng.integers(0, 4), rng.integers(0, 3), rng.integers(0, 4)
    for _ in range(n1):
        pts.append(complex(rng.uniform(0, spread))); nu.append(1); kind.append('s')
    for _ in range(n2):
        pts.append(complex(rng.uniform(0, spread))); nu.append(2); kind.append('d')
    for _ in range(nh):
        pts.append(complex(rng.uniform(0, spread))); nu.append(int(rng.integers(3, 5))); kind.append('h')
    for _ in range(k):
        xx = rng.uniform(0, spread); yy = rng.uniform(1e-3, 0.8); m = int(rng.integers(1, 3))
        pts += [complex(xx, yy), complex(xx, -yy)]; nu += [m, m]; kind += ['o', 'o']
    return np.array(pts), np.array(nu), np.array(kind)


def spectrum_A(pts, nu, K):
    n = len(pts)
    conjidx = np.array([int(np.argmin(np.abs(pts - np.conj(z)))) for z in pts])
    Pm = np.zeros((n, n)); Pm[np.arange(n), conjidx] = 1
    Gram = K(pts[None, :] - np.conj(pts)[:, None])          # Gram[w,u] = K(u - conj w)
    M = np.diag(nu) @ Pm @ Gram
    ev = np.linalg.eigvals(M)
    return ev


def part_c():
    print("(c) randomised tests on the actual operator (synthetic configurations)")
    worst = {}
    maxim = 0.0
    trials = 0
    for Kname, K in (("KN-window-1", K_kn1), ("MT", K_mt)):
        for it in range(3000):
            pts, nu, kind = config(rng, rng.choice([0.6, 1.5, 3.0, 6.0]))
            if len(pts) == 0:
                continue
            trials += 1
            ev = spectrum_A(pts, nu, K)
            maxim = max(maxim, np.max(np.abs(ev.imag)) / max(1, np.max(np.abs(ev))))
            ev = ev.real
            N = nu.sum()
            trA2 = np.sum(ev ** 2)
            D = pts[:, None] - pts[None, :]
            trA2_direct = np.real(np.sum(nu[:, None] * nu[None, :] * K(D) ** 2))
            worst["trA2 identity"] = max(worst.get("trA2 identity", 0), abs(trA2 - trA2_direct) / max(1, abs(trA2)))
            on12 = (kind == 's') | (kind == 'd')
            y = pts[on12].real; d = nu[on12].astype(float)
            U = np.real(K(y[:, None] - y[None, :])) if len(y) else np.zeros((0, 0))
            G = np.sqrt(d)[:, None] * U * np.sqrt(d)[None, :] if len(y) else U
            eG = np.linalg.eigvalsh(G) if len(y) else np.zeros(0)
            n1 = int(np.sum(kind == 's')); n2 = int(np.sum(kind == 'd')); h = int(np.sum(kind == 'h')); kk = int(np.sum(kind == 'o')) // 2
            for c in (2.0, 3.0, 3.35):
                rhs = 2 * c * N - (2 * c - 1) * n1 - (4 * c - 4) * n2 - c * c * (h + kk) + (np.sum(phi_c(eG, c)) - np.sum(d ** 2))
                key = f"KN eq:key c={c}"
                worst[key] = min(worst.get(key, np.inf), trA2 - rhs)
                for tlev in (c, c + 0.4, 3.375):
                    if tlev < c:
                        continue
                    # Lemma 6.1 with P = on-line mult 1,2 part (trP = n1 + 2 n2), p = h + kk
                    rhs2 = np.sum(phi_c(eG, c)) + 2 * tlev * (N - (n1 + 2 * n2)) - tlev ** 2 * (h + kk)
                    key2 = "KN Lemma 6.1 (two levels)"
                    worst[key2] = min(worst.get(key2, np.inf), trA2 - rhs2)
            # eq:key2 (c=2, P = simple on-line only)
            ys = pts[kind == 's'].real
            Us = np.real(K(ys[:, None] - ys[None, :])) if len(ys) else np.zeros((0, 0))
            eU = np.linalg.eigvalsh(Us) if len(ys) else np.zeros(0)
            n = len(ys); pcount = int(np.sum(kind == 'd') + np.sum(kind == 'h') + kk)
            worst["KN eq:key2 first"] = min(worst.get("KN eq:key2 first", np.inf), trA2 - (4 * (N - n) - 4 * pcount + np.sum(phi_c(eU, 2.0))))
            worst["KN eq:key2 second"] = min(worst.get("KN eq:key2 second", np.inf), trA2 - (2 * (N - n) + np.sum(phi_c(eU, 2.0))))
            # final counts (no interaction)
            Nd = len(pts)
            Ns = int(np.sum(nu == 1)); N0 = int(np.sum(nu[np.abs(pts.imag) < 1e-15]))
            worst["N0s >= 2N - trA2"] = min(worst.get("N0s >= 2N - trA2", np.inf), n - (2 * N - trA2))
            worst["Nd >= (3N - trA2)/2"] = min(worst.get("Nd >= (3N - trA2)/2", np.inf), Nd - (3 * N - trA2) / 2)
            worst["Ns+N0 >= 3N - trA2"] = min(worst.get("Ns+N0 >= 3N - trA2", np.inf), Ns + N0 - (3 * N - trA2))
    print(f"   {trials} configurations; max |Im eig|/scale of diag(nu) P Gram = {maxim:.2e} (A is Hermitian)")
    for kname, v in worst.items():
        print(f"   {kname:28s}: {'max rel. diff' if 'identity' in kname else 'min slack'} = {v:.3e}")


if __name__ == "__main__":
    part_a()
    part_b()
    part_c()
