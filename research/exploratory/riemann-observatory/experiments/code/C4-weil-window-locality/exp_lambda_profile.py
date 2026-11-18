"""Experiment P: window profile lambda_min(L) of the Weil form (arithmetic side, high precision).

For each L, assemble the N x N arithmetic-side matrix in the orthonormal Legendre basis on
[-L, L] with python-flint (Arb) at `prec` bits (hp_core.HPWeil), split by parity (the form
commutes with x -> -x), and compute the smallest eigenvalue of each parity block by inverse
iteration on the midpoint matrix followed by a ball-arithmetic Rayleigh quotient.

What is (and is not) certified: the Rayleigh quotient is evaluated in ball arithmetic on the
assembled matrix, but the archimedean integral uses an S-node Gauss rule whose truncation error
is not enclosed; we therefore label all values NUMERICAL-NONRIGOROUS (high precision), with
convergence in S and N reported. Each value is (up to that quadrature error) a variational
upper bound for the true window infimum.

Usage: python3 exp_lambda_profile.py [tag]
"""
import sys, os, time, json, math, hashlib, platform
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import flint
from flint import arb, arb_mat, ctx
from hp_core import HPWeil

RES = "/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C4-weil-window-locality"

PLAN = [  # (L, [N values], prec bits)
    (0.1, [8, 12, 16], 200), (0.2, [8, 12, 16], 200), (0.3, [12, 16, 24], 200),
    (0.34657359027997264, [12, 16, 24], 200), (0.4, [16, 24, 32], 250), (0.40541, [16, 24, 32], 250),
    (0.5, [24, 32, 40], 300), (0.6, [24, 32, 48], 300), (0.7, [32, 48, 64], 300),
    (0.8, [40, 56, 72], 350), (0.9, [56, 72, 88], 400), (1.0, [72, 88, 104], 450),
    (1.1, [88, 108, 128], 500), (1.2, [108, 132, 156], 560),
]


def block(W, idx):
    n = len(idx)
    B = arb_mat(n, n)
    for a, j in enumerate(idx):
        for b, k in enumerate(idx):
            B[a, b] = W[j, k]
    return B


def lam_min_block(B, iters=60):
    n = B.nrows()
    Bm = B.mid()
    x = arb_mat(n, 1)
    for j in range(n):
        x[j, 0] = arb(1) / (j + 1)
    for _ in range(iters):
        y = Bm.solve(x, algorithm="approx")
        nrm = sum((y[j, 0] ** 2 for j in range(n)), arb(0)).sqrt()
        x = y * (1 / nrm)
    Bx = B * x
    num = sum((x[j, 0] * Bx[j, 0] for j in range(n)), arb(0))
    den = sum((x[j, 0] ** 2 for j in range(n)), arb(0))
    return num / den, x


def main(tag="main"):
    out = []
    t_all = time.time()
    for L, Ns, prec in PLAN:
        for N in Ns:
            S = max(200, 2 * N + 120)
            t0 = time.time()
            ctx.prec = prec
            H = HPWeil(L, N, prec=prec)
            W = H.matrix(S=S)
            ev = list(range(0, N, 2)); od = list(range(1, N, 2))
            le, xe = lam_min_block(block(W, ev))
            lo, xo = lam_min_block(block(W, od))
            rec = {"L": L, "N": N, "S": S, "prec_bits": prec,
                   "lam_even": le.str(12, radius=False), "lam_even_rad": float(le.rad()),
                   "lam_odd": lo.str(12, radius=False), "lam_odd_rad": float(lo.rad()),
                   "seconds": round(time.time() - t0, 1)}
            out.append(rec)
            print(json.dumps(rec), flush=True)
    meta = {"experiment": "lambda_min(L) profile, arithmetic side, Legendre basis, Arb assembly",
            "python": platform.python_version(), "python-flint": flint.__version__,
            "runtime_s": round(time.time() - t_all, 1), "plan": PLAN}
    path = os.path.join(RES, f"lambda_profile_{tag}.json")
    with open(path, "w") as f:
        json.dump({"meta": meta, "rows": out}, f, indent=1)
    print("wrote", path, hashlib.sha256(open(path, "rb").read()).hexdigest())


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "main")
