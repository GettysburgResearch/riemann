# s5_energy_sanity.py -- EXPLORATION ONLY (not probative): small-scale values of the dual mean square
#   E(H,X,1;1,W) = (1/X) sum_{0<N(k)<=H} | sum*_{(n,6)=1} a(n) chi_n(k) W(N(n)/X) |^2
# (paper2.tex (eq:energy) l.938-966 with F=1, f=1, xi=1, S={2,lambda}) for the coefficients
#   a(n) = conj(alpha(n)) gamma_2(n)   (the paper's a_xi),
#   a(n) = gamma_2(n)                  (no angle; Patterson-type coefficients),
#   a(n) = mu(n)                       (the original Moebius coefficients),
# in the regime H < X that Proposition 5.1 covers (H <= Sigma D^{-kappa}, Sigma = X).
# Prop. 5.1 asserts E << D^eps * X there.  Finite computations cannot confirm or refute an
# asymptotic statement with unspecified constants; this only checks that nothing grossly
# inconsistent (e.g. E/X growing like a power of X) is visible at these sizes.
# Written from scratch; imports our own s5_cube_inversion_checks.py by absolute path.
import importlib.util, math, cmath, sys, time
import numpy as np
HERE = "/home/user/riemann/research/exploratory/riemann-observatory/experiments/code/quasi_rh/"
spec = importlib.util.spec_from_file_location("s5ci", HERE + "s5_cube_inversion_checks.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

def main():
    Xmax = 4000
    primes = m.prime_list(Xmax)
    g2 = {i: m.gamma2_direct(primes, [i], P.pi) for i, P in enumerate(primes)}
    def gamma2(idx):
        val = 1 + 0j; acc_idx = []; acc = (1, 0)
        for i in idx:
            P = primes[i]
            val *= g2[i] * m.chi_val(primes, acc_idx, P.pi, 2) * m.chi_val(primes, [i], acc, 2)
            acc_idx = acc_idx + [i]; acc = m.mul(acc, P.pi)
        return val
    W = m.bump(0.5, 1.0)
    ns_all = m.squarefree_ideals(primes, Xmax)
    print("X, H, #rows, #cols, E/X for [conj(alpha) gamma_2, gamma_2, mu]; diagonal/X = #rows * sum_n W(N n/X)^2 / X^2 (value if the rows were exactly orthogonal)")
    for X in (500, 1000, 2000, 4000):
        cols = [(g, idx) for g, idx in ns_all if 0.5 * X < m.norm(g) <= X]
        for Hfrac in (0.125, 0.5):
            H = Hfrac * X
            rows = [(a, b) for a in range(-int(2 * math.sqrt(H)) - 2, int(2 * math.sqrt(H)) + 3)
                    for b in range(-int(2 * math.sqrt(H)) - 2, int(2 * math.sqrt(H)) + 3)
                    if 0 < a * a - a * b + b * b <= H]
            used = sorted({i for g, idx in cols for i in idx})
            # sextic symbols chi_p(k) for every used prime and every row, as exponents (-1 = zero)
            symtab = {}
            for i in used:
                P = primes[i]
                symtab[i] = np.array([(-1 if (s := P.sym(k)) is None else s) for k in rows])
            M = np.ones((len(rows), len(cols)), dtype=complex)
            for c, (g, idx) in enumerate(cols):
                e = np.zeros(len(rows), dtype=int); z = np.zeros(len(rows), dtype=bool)
                for i in idx:
                    s = symtab[i]; z |= (s < 0); e += np.where(s < 0, 0, s)
                M[:, c] = np.where(z, 0, m.Z6 ** (e % 6))
            Wn = W(np.array([m.norm(g) / X for g, idx in cols], float))
            res = []
            for kind in ("ag", "g", "mu"):
                a = np.array([(np.conj(m.alpha(g)) * gamma2(idx)) if kind == "ag" else
                              (gamma2(idx) if kind == "g" else (-1) ** len(idx)) for g, idx in cols])
                S = M @ (a * Wn)
                res.append(np.sum(np.abs(S) ** 2) / X / X)          # E/X = (1/X^2) sum_k |S_k|^2
            diag = len(rows) * np.sum(Wn ** 2) / X
            print(f"X={X:5d} H={H:7.1f} rows={len(rows):5d} cols={len(cols):4d}  E/X = "
                  f"{res[0]:.4f}, {res[1]:.4f}, {res[2]:.4f}   diagonal/X = {diag / X:.4f}"); sys.stdout.flush()

if __name__ == "__main__":
    t = time.time(); main(); print(f"elapsed {time.time()-t:.1f}s")
