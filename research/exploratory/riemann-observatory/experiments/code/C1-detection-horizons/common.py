"""Shared helpers for campaign C1-detection-horizons (Riemann Observatory).
Zero data: Arb-certified ordinates of the first 100000 zeta zeros (columns n, midpoint, radius),
produced by experiments/code/zeros_arb.py (python-flint acb.zeta_zeros)."""
import os, sys, json, time, hashlib, platform
import numpy as np

SCR = "/tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/data"
ZERO_FILES = [os.path.join(SCR, "zeros_1_50000.tsv"), os.path.join(SCR, "zeros_50001_100000.tsv")]
RESULTS = "/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C1-detection-horizons"
EULER_GAMMA = 0.57721566490153286061
T0_PLATT_TRUDGIAN = 3.0001753328e12   # Platt-Trudgian 2021, Thm 1: RH true up to height 3 000 175 332 800

def load_zeros(as_str=False):
    """Return float64 array of the first 100000 ordinates (midpoints) and max radius."""
    g, rad, strs = [], 0.0, []
    for f in ZERO_FILES:
        with open(f) as fh:
            for line in fh:
                n, m, r = line.split()
                g.append(float(m)); rad = max(rad, float(r)); strs.append(m)
    g = np.array(g)
    assert len(g) == 100000 and np.all(np.diff(g) > 0)
    return (g, rad, strs) if as_str else (g, rad)

def N_smooth(t):
    """Riemann-von Mangoldt main term N(t) ~ (t/2pi) log(t/2pi e) + 7/8."""
    t = np.asarray(t, dtype=float)
    return t / (2 * np.pi) * np.log(t / (2 * np.pi * np.e)) + 7.0 / 8.0

def dens(t):
    return np.log(np.asarray(t, dtype=float) / (2 * np.pi)) / (2 * np.pi)

def env():
    import mpmath, scipy
    v = {"python": platform.python_version(), "numpy": np.__version__, "mpmath": mpmath.__version__, "scipy": scipy.__version__}
    try:
        import flint; v["python-flint"] = flint.__version__
    except Exception:
        pass
    return v

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()

def save_json(name, obj):
    os.makedirs(RESULTS, exist_ok=True)
    p = os.path.join(RESULTS, name)
    with open(p, "w") as f:
        json.dump(obj, f, indent=1, default=float)
    return p
