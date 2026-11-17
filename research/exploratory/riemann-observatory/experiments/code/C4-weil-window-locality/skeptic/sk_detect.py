"""SKEPTIC (C4): independent ZEROS-SIDE re-implementation of the detection thresholds (C4-D1, D2, D4).

Model (as stated in the report): W_mod = sum over true zeros (both signs) |h_g(gamma)|^2
   + sum_{z in {+-T0 +- i delta}} h_g(z) conj h_g(conj z)   [additive]
   minus the two neighbouring true zeros                        [collision].
Investigator: true-zero part from the ARITHMETIC side.  Here: from the first 100000 Arb ordinates
(both signs) + smooth tail  sqrt((2j+1)(2k+1))/L * int_G^inf [ (t-T0)^-2 + (t+T0)^-2 ] log(t/2pi)/(2pi) dt
(j = k mod 2), i.e. a completely different route.  Basis: e^{-i T0 x} phi_j(x), phi_j orthonormal Legendre,
j < N.  h_j(s) = i^j sqrt(2L(2j+1)) j_j(sL) (scipy, real s); complex s by Gauss-Legendre quadrature
(s = +-i delta) and by mpmath Bessel (mirror pair s = -2T0 +- i delta).
Detection: lambda_min < -tau (tau = 1e-8, as in the report).  Double precision, non-rigorous.
Usage: python3 sk_detect.py T0 delta1,delta2,.. model N|rule Llo Lhi step [nbis]
"""
import os, sys, json, math, time
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import numpy as np
import mpmath as mp
from scipy.special import spherical_jn
from numpy.polynomial.legendre import leggauss, legval

ZD = "/tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/data"
RES = "/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C4-weil-window-locality/skeptic"
GAM = np.concatenate([np.loadtxt(os.path.join(ZD, f), usecols=1) for f in ("zeros_1_50000.tsv", "zeros_50001_100000.tsv")])
GMAX = GAM[-1]
TAU = 1e-8


def h_real(s, L, N):
    s = np.asarray(s, float)
    out = np.empty((N, s.size), complex)
    for j in range(N):
        out[j] = (1j ** j) * math.sqrt(2 * L * (2 * j + 1)) * spherical_jn(j, s * L)
    return out


def h_imag(b, L, N, q=200):
    """h_j(i b) = int phi_j(x) e^{-b x} dx by Gauss-Legendre (smooth integrand)."""
    t, w = leggauss(q)
    x = L * t
    vals = np.empty(N)
    for j in range(N):
        c = np.zeros(j + 1); c[j] = 1
        phi = math.sqrt((2 * j + 1) / (2 * L)) * legval(t, c)
        vals[j] = np.sum(w * L * phi * np.exp(-b * x))
    return vals.astype(complex)


def h_mp(s, L, N):
    """h_j(s) for complex s via mpmath spherical Bessel j_n(w) = sqrt(pi/(2w)) J_{n+1/2}(w)."""
    mp.mp.dps = 30
    w = mp.mpc(s) * L
    out = np.empty(N, complex)
    for j in range(N):
        jn = mp.sqrt(mp.pi / (2 * w)) * mp.besselj(j + mp.mpf(1) / 2, w)
        out[j] = complex((1j ** j) * mp.sqrt(2 * L * (2 * j + 1)) * jn)
    return out


_TAILC = {}


def tail_coeff(T0):
    if T0 not in _TAILC:
        f = lambda t: (1 / (t - T0) ** 2 + 1 / (t + T0) ** 2) * mp.log(t / (2 * mp.pi)) / (2 * mp.pi)
        _TAILC[T0] = float(mp.quad(f, [GMAX, 2 * GMAX, mp.inf]))
    return _TAILC[T0]


def P_matrix(T0, L, N, remove=()):
    g = GAM
    s = np.concatenate([g - T0, -g - T0])
    E = h_real(s, L, N)
    P = E @ E.conj().T
    if remove:
        r = np.array(remove, float)
        Er = h_real(np.concatenate([r - T0, -r - T0]), L, N)
        P -= Er @ Er.conj().T
    jj = np.arange(N)
    par = ((jj[:, None] - jj[None, :]) % 2 == 0)
    P += par * np.sqrt(np.outer(2 * jj + 1, 2 * jj + 1)) / L * tail_coeff(T0)
    return P


def Q_matrix(T0, delta, L, N, mirror=True):
    hp = h_imag(delta, L, N)    # h(+i delta) = int phi e^{i(i delta) x} = int phi e^{-delta x}
    hm = h_imag(-delta, L, N)   # h(-i delta)
    Mq = np.outer(hp, hm.conj()) + np.outer(hm, hp.conj())   # z = T0 + i d and z = T0 - i d
    if mirror:
        a = h_mp(complex(-2 * T0, -delta), L, N)
        b = h_mp(complex(-2 * T0, delta), L, N)
        Mq += np.outer(a, b.conj()) + np.outer(b, a.conj())
    return Mq


def N_rule(L):
    return 48 if L <= 2.0 else (64 if L <= 3.5 else 96)


_PC = {}


def lam(T0, delta, L, N, model, nb):
    key = (T0, round(float(L), 10), N, model)
    if key not in _PC:
        if len(_PC) > 40:
            _PC.clear()
        _PC[key] = P_matrix(T0, L, N, remove=nb if model == "collision" else ())
    P = _PC[key]
    W = P + Q_matrix(T0, delta, L, N, mirror=(T0 < 2e4))
    W = 0.5 * (W + W.conj().T)
    return float(np.linalg.eigvalsh(W)[0]), float(np.linalg.eigvalsh(0.5 * (P + P.conj().T))[0])


def main():
    T0 = float(sys.argv[1]); deltas = [float(x) for x in sys.argv[2].split(",")]
    model = sys.argv[3]; Narg = sys.argv[4]
    Llo, Lhi, step = float(sys.argv[5]), float(sys.argv[6]), float(sys.argv[7])
    nbis = int(sys.argv[8]) if len(sys.argv) > 8 else 6
    k = int(np.searchsorted(GAM, T0)); nb = (GAM[k - 1], GAM[k])
    Nf = (lambda L: N_rule(L)) if Narg == "rule" else (lambda L, n=int(Narg): n)
    res = []
    t0 = time.time()
    for d in deltas:
        prev, found, hist = None, None, []
        for L in np.arange(Llo, Lhi + 1e-9, step):
            lm, l0 = lam(T0, d, L, Nf(L), model, nb)
            hist.append([round(float(L), 6), lm, l0])
            if lm < -TAU:
                found = (prev, float(L)); break
            prev = float(L)
        rec = {"T0": T0, "delta": d, "model": model, "N": Narg, "neighbors": [float(nb[0]), float(nb[1])],
               "L_N": 0.5 * math.log(T0 / (2 * math.pi)), "hist": hist}
        if found and found[0] is not None:
            lo, hi = found
            for _ in range(nbis):
                mid = 0.5 * (lo + hi)
                if lam(T0, d, mid, Nf(mid), model, nb)[0] < -TAU:
                    hi = mid
                else:
                    lo = mid
            rec["L_star"] = 0.5 * (lo + hi); rec["bracket"] = [lo, hi]
        else:
            rec["L_star"] = None; rec["bracket"] = found
        res.append(rec)
        print(json.dumps({k_: v for k_, v in rec.items() if k_ != "hist"}), flush=True)
    tag = f"T{T0:.0f}_{model}_N{Narg}_" + "_".join(str(x) for x in deltas)
    json.dump({"results": res, "seconds": round(time.time() - t0, 1), "numpy": np.__version__},
              open(os.path.join(RES, f"sk_detect_{tag}.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
