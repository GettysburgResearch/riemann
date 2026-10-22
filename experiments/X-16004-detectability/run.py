"""Driver for the detectability-law measurements.  Usage: python3 run.py <part>"""
import time, sys
import mpmath as mp
sys.path.insert(0, '/tmp/claude-0/-home-user-riemann/8aa2c694-669d-5c54-ab29-9ac46b683161/scratchpad/det')
from loewner import *

PART = sys.argv[1] if len(sys.argv) > 1 else "all"


def dps_for(N, mult=1):
    return int(mult * (40 + 6 * N))


# ---- pole profiles -------------------------------------------------------
_GAM_CACHE = {}
def zeta_mus(M, Delta="1.5"):
    if M not in _GAM_CACHE:
        _GAM_CACHE[M] = zeta_ordinates(M, dps=40)
    D = mp.mpf(Delta)
    return [g * D for g in _GAM_CACHE[M]]

def ladder_mus(M, h=None):
    """Uniform ladder with irrational spacing pi/2 = 1.5708..., so that no
    pole ever lands exactly on an integer node (h=1.5 does: 1.5*2=3)."""
    step = mp.pi / 2 if h is None else mp.mpf(h)
    return [step * k for k in range(1, M + 1)]


def row(N, mus, ws, star, dps, lo_exp=-90, label=""):
    """Full measurement for one configuration."""
    mp.mp.dps = dps
    t0 = time.time()
    Q0 = Q_of_delta(N, mus, ws, None, None)
    inr0 = inertia(Q0)
    lmin0 = lambda_min(Q0)
    lmax0 = lambda_max(Q0)
    dc, info = delta_critical(N, mus, ws, star, lo_exp=lo_exp, hi_exp=3, refine=32)
    # detection thresholds: observer resolving eigenvalues down to 10^-u * lam_max
    det = {}
    for u in (16, 30, 50):
        T = lmax0 * mp.mpf(10) ** (-u)
        d, _ = delta_critical(N, mus, ws, star, lo_exp=lo_exp, hi_exp=3,
                              refine=28, thresh=T)
        det[u] = d
    dt = time.time() - t0
    return dict(N=N, dim=2 * N + 1, dps=dps, mu_star=mus[star], inertia=inr0,
                lmin0=lmin0, lmax0=lmax0, dc=dc, det=det, secs=dt, label=label)


def _e(x):
    return "%.3e" % float(x) if x is not None else "   NEVER "


def fmt(r):
    return ("N=%2d dim=%2d dps=%3d mu*=%8.3f inertia=%-12s lmax=%.4e lmin0=%.6e "
            "kappa=%.2e  delta_c=%s  det16=%s det30=%s det50=%s  [%.1fs] %s"
            % (r["N"], r["dim"], r["dps"], float(r["mu_star"]), str(r["inertia"]),
               float(r["lmax0"]), float(r["lmin0"]), float(r["lmax0"] / r["lmin0"]),
               _e(r["dc"]), _e(r["det"][16]), _e(r["det"][30]), _e(r["det"][50]),
               r["secs"], r["label"]))


# =========================================================================
if PART in ("1", "all"):
    print("### PART 1: zeta profile, Delta=1.5, M=20 poles, a=1, star = lowest pole (mu=21.20)")
    MUS = zeta_mus(20); WS = [mp.mpf(1)] * 20
    for N in (4, 6, 8, 10, 12, 14):
        r = row(N, MUS, WS, 0, dps_for(N))
        print(fmt(r)); sys.stdout.flush()

if PART in ("1x", "all"):
    print()
    print("### PART 1x: dps-doubling self-consistency (same rows, 2x dps)")
    MUS = zeta_mus(20); WS = [mp.mpf(1)] * 20
    for N in (8, 14):
        r = row(N, MUS, WS, 0, dps_for(N, 2))
        print(fmt(r)); sys.stdout.flush()

if PART in ("2", "all"):
    print()
    print("### PART 2: pole-count convergence (does adding poles change the answer?)")
    for N in (8, 12):
        for M in (10, 20, 30, 40):
            MUS = zeta_mus(M); WS = [mp.mpf(1)] * M
            r = row(N, MUS, WS, 0, dps_for(N), label="M=%d" % M)
            print(fmt(r)); sys.stdout.flush()

if PART in ("3", "all"):
    print()
    print("### PART 3: dependence on the height mu_* of the perturbed pole (zeta profile, N=10)")
    MUS = zeta_mus(20); WS = [mp.mpf(1)] * 20
    for star in range(0, 10):
        r = row(10, MUS, WS, star, dps_for(10), label="star=%d" % star)
        print(fmt(r)); sys.stdout.flush()

if PART in ("4", "all"):
    print()
    print("### PART 4: synthetic ladder mu_k=k*pi/2 (poles straddle the node band |x|<=N)")
    print("    'NEVER' = no negative eigenvalue for any delta in [1e-90, 1e3]:")
    print("    the PSD background from the other poles is never overcome.")
    MUS = ladder_mus(20); WS = [mp.mpf(1)] * 20
    for N in (4, 6, 8, 10, 12):
        for star in (0, 4, 7, 19):     # mu = 1.571, 7.854, 12.566, 31.416
            r = row(N, MUS, WS, star, dps_for(N),
                    label="mu*=%.3f  mu*/N=%.2f" % (float(MUS[star]), float(MUS[star]) / N))
            print(fmt(r)); sys.stdout.flush()

if PART in ("5", "all"):
    print()
    print("### PART 5: weight dependence (zeta profile, N=8, star=0)")
    MUS = zeta_mus(20)
    print("  (a) scale ONLY the perturbed pole's weight a_*")
    for a in ("0.01", "0.1", "1", "10", "100"):
        WS = [mp.mpf(1)] * 20; WS[0] = mp.mpf(a)
        r = row(8, MUS, WS, 0, dps_for(8), label="a_*=%s" % a)
        print(fmt(r)); sys.stdout.flush()
    print("  (b) scale ALL weights (null test: Q -> cQ, delta_c must be invariant)")
    for a in ("0.01", "1", "100"):
        WS = [mp.mpf(a)] * 20
        r = row(8, MUS, WS, 0, dps_for(8), label="all a=%s" % a)
        print(fmt(r)); sys.stdout.flush()

if PART in ("6", "all"):
    print()
    print("### PART 6: signal strength  lambda_min(Q(delta))  vs delta")
    MUS = zeta_mus(20); WS = [mp.mpf(1)] * 20
    for N in (8, 12):
        dps = dps_for(N); mp.mp.dps = dps
        Q0 = Q_of_delta(N, MUS, WS, None, None)
        lmax0 = lambda_max(Q0); lmin0 = lambda_min(Q0)
        dc, _ = delta_critical(N, MUS, WS, 0, lo_exp=-90, hi_exp=3, refine=32)
        print("  N=%d dps=%d lam_max=%.4e lam_min(0)=%.4e delta_c=%.6e"
              % (N, dps, float(lmax0), float(lmin0), float(dc)))
        for ratio in ("0", "0.1", "0.5", "0.9", "0.99", "1.01", "1.1", "2", "10",
                      "100", "1e3", "1e6", "1e9"):
            d = mp.mpf(0) if ratio == "0" else dc * mp.mpf(ratio)
            Qd = Q_of_delta(N, MUS, WS, 0, d if d != 0 else None)
            lm = lambda_min(Qd)
            inr = inertia(Qd)
            print("     delta/delta_c=%-6s delta=%.4e  inertia=%-11s lam_min=%+.6e  lam_min/lam_max=%+.3e"
                  % (ratio, float(d), str(inr), float(lm), float(lm / lmax0)))
            sys.stdout.flush()
