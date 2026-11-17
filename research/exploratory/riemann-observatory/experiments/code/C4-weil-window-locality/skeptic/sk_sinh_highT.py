"""SKEPTIC (C4): independent large-height check of C4-D3 with the single test function
g0(x) = e^{-iTx} sinh(delta x) 1_[-L,L] (the Theorem C4-B function), arithmetic side, additive model.

f = g0*g0~ = e^{-iTy} a(y),  a(y) = sinh(delta(2L-|y|))/(2 delta) - (2L-|y|) cosh(delta y)/2  (closed form)
W_true(g0) = pole + arch - sum_{log n < 2L} 2 Lambda(n) n^{-1/2} a(log n) cos(T log n)
  arch = (1/2pi) int |what(s)|^2 Phi(T+s) ds, Phi(r) = Re psi(1/4+ir/2) - log pi
       = s2*Phi(T) + (1/2pi) int |what(s)|^2 [Phi(T+s)-Phi(T)] ds  (second term evaluated for T <= 1e5: exact on
         |s|<=S1, averaged tail 2 sinh^2(dL)/s^2 beyond; dropped for T > 1e5, where it is o(1/T))
  pole = int 2cosh(y/2) cos(Ty) a(y) dy  (computed for T <= 1e5, dropped above: O(1/T^2))
W_mod(g0) = W_true(g0) - 2 s2^2 (+T pair; -T pair O(Ac^2/T^2) dropped for T > 1e5, included below).
Validation: at T = 1e4, 3e4 compare W_true(g0) with the zeros-side value from sk_thmB.json.
L_sinh = smallest L with W_mod(g0) < 0.  mpmath (phases at 90 digits) + numpy; non-rigorous.
"""
import os, sys, json, math, time
import numpy as np
import mpmath as mp

RES = "/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C4-weil-window-locality/skeptic"


def primes_upto(X):
    s = np.ones(X + 1, bool); s[:2] = False
    for p in range(2, int(X ** 0.5) + 1):
        if s[p]:
            s[p * p::p] = False
    return np.nonzero(s)[0]


class Height:
    def __init__(self, Tstr, Lmax):
        self.Tstr = Tstr
        self.T = mp.mpf(Tstr)
        X = int(math.exp(2 * Lmax)) + 2
        ps = primes_upto(X)
        with mp.workdps(90):
            T = mp.mpf(Tstr); tp = 2 * mp.pi
            base = [float(mp.fmod(T * mp.log(int(p)), tp)) for p in ps]
        ln, lam, ph = [], [], []
        for p, b in zip(ps, base):
            p = int(p); q = p; k = 1
            while q <= X:
                ln.append(math.log(q)); lam.append(math.log(p)); ph.append(math.fmod(k * b, 2 * math.pi))
                q *= p; k += 1
        self.ln = np.array(ln); self.amp = np.array(lam) / np.exp(self.ln / 2); self.cos = np.cos(np.array(ph))
        mp.mp.dps = 30
        self.Phi = float(mp.re(mp.digamma(mp.mpf(1) / 4 + 0.5j * self.T)) - mp.log(mp.pi))

    def a(self, y, d, L):
        u = 2 * L - np.abs(y)
        return np.sinh(d * u) / (2 * d) - u * np.cosh(d * y) / 2

    def arch(self, d, L, exact=False):
        s2 = math.sinh(2 * d * L) / (2 * d) - L
        if not exact:
            # correction (1/2pi) int |what|^2 [Phi(T+s)-Phi(T)]: leading 1/T term vanishes
            # (PV int log|1-u^2|/u^2 du = 0, checked numerically); remainder O(log T / T^2) dropped
            return s2 * self.Phi
        T = self.T
        w2 = lambda s: 4 * (d * mp.cosh(d * L) * mp.sin(s * L) - s * mp.sinh(d * L) * mp.cos(s * L)) ** 2 / (d * d + s * s) ** 2
        Ph = lambda r: mp.re(mp.digamma(mp.mpf(1) / 4 + 0.5j * r)) - mp.log(mp.pi)
        S1 = 300
        pts = list(np.arange(-S1, S1 + 1e-9, 1.0))
        core = mp.quad(lambda s: w2(s) * (Ph(T + s) - self.Phi), pts)
        c = 2 * mp.sinh(d * L) ** 2
        tail = mp.quad(lambda s: c / s ** 2 * (Ph(T + s) - self.Phi), [S1, 10 * S1, T / 2, T, 2 * T, mp.inf]) + \
            mp.quad(lambda s: c / s ** 2 * (Ph(T - s) - self.Phi), [S1, 10 * S1, T / 2, T, 2 * T, mp.inf])
        return s2 * self.Phi + float((core + tail) / (2 * mp.pi))

    def pole(self, d, L):
        T = float(self.T)
        if T > 1e5:
            return 0.0
        f = lambda y: 2 * mp.cosh(y / 2) * mp.cos(T * y) * (mp.sinh(d * (2 * L - y)) / (2 * d) - (2 * L - y) * mp.cosh(d * y) / 2)
        n = int(2 * L * T / math.pi) + 2
        return float(2 * mp.quad(f, list(np.linspace(0, 2 * L, n + 1))))

    def primes(self, d, L):
        m = self.ln < 2 * L
        return float(np.sum(2 * self.amp[m] * self.a(self.ln[m], d, L) * self.cos[m]))

    def W_true(self, d, L, exact=False):
        return self.pole(d, L) + self.arch(d, L, exact) - self.primes(d, L)

    def W_mod(self, d, L, exact=False):
        s2 = math.sinh(2 * d * L) / (2 * d) - L
        out = self.W_true(d, L, exact) - 2 * s2 ** 2
        if float(self.T) <= 1e5:   # -T pair (exact closed form)
            T = float(self.T)
            wh = lambda z: 2j * (d * mp.cosh(d * L) * mp.sin(z * L) - z * mp.sinh(d * L) * mp.cos(z * L)) / (d * d + z * z)
            out += float(2 * mp.re(wh(mp.mpc(-2 * T, -d)) * mp.conj(wh(mp.mpc(-2 * T, d)))))
        return out


def L_sinh(H, d, Llo, Lhi, step=0.02, nbis=12):
    prev = None
    for L in np.arange(Llo, Lhi + 1e-9, step):
        if H.W_mod(d, L) < 0:
            if prev is None:
                return None
            lo, hi = prev, L
            for _ in range(nbis):
                m = 0.5 * (lo + hi)
                if H.W_mod(d, m) < 0:
                    hi = m
                else:
                    lo = m
            return 0.5 * (lo + hi)
        prev = L
    return None


def L_flat(T, d):
    Psi = math.log(T / (2 * math.pi))
    f = lambda L: math.sinh(2 * d * L) / (2 * d) - L - Psi / 2
    lo, hi = 1e-6, 1.0
    while f(hi) < 0:
        hi *= 2
    for _ in range(100):
        m = 0.5 * (lo + hi)
        lo, hi = (m, hi) if f(m) < 0 else (lo, m)
    return 0.5 * (lo + hi)


def main():
    out = {"validation": [], "thresholds": []}
    t0 = time.time()
    zc = json.load(open(os.path.join(RES, "sk_thmB.json")))["zeros_check"]
    for T in (1.0e4, 3.0e4):
        H = Height(repr(T), 4.2)
        for r in zc:
            if (r["T"], r["delta"], r["L"]) in ((1.0e4, 0.1, 2.0), (1.0e4, 0.49, 3.0), (3.0e4, 0.3, 4.0)):
                wt = H.W_true(r["delta"], r["L"], exact=True)
                out["validation"].append({"T": T, "delta": r["delta"], "L": r["L"], "arith_W_true": wt, "zeros_P": r["P_zeros"],
                                          "diff": wt - r["P_zeros"]})
                print(json.dumps(out["validation"][-1]), flush=True)
    cases = [("1000000.7062205937", [0.49, 0.2]), ("100000000.86124954", [0.49, 0.2]), ("10000000000.170462", [0.49, 0.2]),
             ("1e12", [0.49, 0.4, 0.3]), ("1e15", [0.49, 0.4]), ("1e20", [0.49, 0.4, 0.3]), ("1e30", [0.49, 0.4]), ("1e50", [0.49, 0.4])]
    for Ts, ds in cases:
        T = float(Ts)
        Lmax = max(L_flat(T, d) for d in ds) + 1.0
        H = Height(Ts, Lmax)
        for d in ds:
            Lf = L_flat(T, d)
            Ls = L_sinh(H, d, max(0.5, Lf - 1.0), Lf + 1.0)
            rec = {"T": Ts, "delta": d, "L_flat": Lf, "L_N": 0.5 * math.log(T / (2 * math.pi)), "L_sinh_skeptic": Ls}
            out["thresholds"].append(rec)
            print(json.dumps(rec), flush=True)
    out["seconds"] = round(time.time() - t0, 1)
    json.dump(out, open(os.path.join(RES, "sk_sinh_highT.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
