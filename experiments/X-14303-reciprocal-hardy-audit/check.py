import numpy as np
import mpmath as mp

rng = np.random.default_rng(20260729)
max_ratio = 0.0
max_constraint_ratio = 0.0

for trial in range(5000):
    n = int(rng.integers(2, 10))
    k = int(rng.integers(1, n))
    x = rng.normal(size=(n, n))
    w = x.T @ x + (0.2 + rng.random()) * np.eye(n)
    q, _ = np.linalg.qr(rng.normal(size=(n, k)))
    z = rng.normal(size=n)

    m = q.T @ w @ q
    r = q.T @ z
    lhs = r @ np.linalg.solve(m, r)
    rhs = z @ np.linalg.solve(w, z)
    if lhs > rhs + 1e-9 * (1 + rhs):
        raise RuntimeError(("base compression inequality failed", trial, lhs, rhs))
    max_ratio = max(max_ratio, lhs / rhs if rhs else 0.0)

    y = rng.normal(size=n)
    p = y - q @ (q.T @ y)
    if np.linalg.norm(p) < 1e-8:
        continue
    p /= np.linalg.norm(p)
    winv_z = np.linalg.solve(w, z)
    winv_p = np.linalg.solve(w, p)
    corrected = rhs - abs(winv_z @ p) ** 2 / (winv_p @ p)
    if lhs > corrected + 2e-8 * (1 + abs(corrected)):
        raise RuntimeError(("constraint-corrected inequality failed", trial, lhs, corrected))
    max_constraint_ratio = max(
        max_constraint_ratio,
        lhs / corrected if corrected > 1e-15 else 0.0,
    )

print("random compression tests PASS", max_ratio, max_constraint_ratio)

mp.mp.dps = 80
worst_direct = mp.mpf("0")
worst_tail_ratio = mp.mpf("0")

for support in [mp.mpf("0.7"), mp.mpf("2.3"), mp.mpf("7.0")]:
    for tau in [mp.mpf("0.03"), mp.mpf("0.17"), mp.mpf("0.49")]:
        for d in range(-8, 9):
            omega = mp.pi * d / support
            direct = mp.quad(
                lambda t: (2 * mp.cosh(2 * tau * t))
                * mp.exp(1j * omega * t)
                / (2 * support),
                [-support, support],
            )
            formula = (
                (-1) ** d
                * 4
                * tau
                * support
                * mp.sinh(2 * tau * support)
                / (4 * tau**2 * support**2 + mp.pi**2 * d**2)
            )
            error = abs(direct - formula)
            worst_direct = max(worst_direct, error)
            if error > mp.mpf("1e-60"):
                raise RuntimeError(("direct Hardy formula failed", support, tau, d, error))

            reciprocal = mp.quad(
                lambda t: mp.exp(1j * omega * t)
                / (2 * mp.cosh(2 * tau * t))
                / (2 * support),
                [-support, support],
            )
            full_line = (
                mp.pi
                / (8 * tau * support)
                * mp.sech(mp.pi**2 * d / (4 * tau * support))
            )
            tail_bound = mp.exp(-2 * tau * support) / (2 * tau * support)
            error = abs(reciprocal - full_line)
            worst_tail_ratio = max(worst_tail_ratio, error / tail_bound)
            if error > tail_bound * (1 + mp.mpf("1e-50")):
                raise RuntimeError(("reciprocal tail failed", support, tau, d, error, tail_bound))

print(
    "Fourier formula tests PASS",
    mp.nstr(worst_direct, 8),
    mp.nstr(worst_tail_ratio, 12),
)

for support in [0.4, 1.0, 3.0, 10.0]:
    for tau in [0.01, 0.1, 0.49]:
        for half_width in [1, 3, 8, 20]:
            indices = np.arange(-half_width, half_width + 1)
            gram = np.empty((len(indices), len(indices)))
            for i, row_index in enumerate(indices):
                for j, column_index in enumerate(indices):
                    d = int(column_index - row_index)
                    gram[i, j] = float(
                        (-1) ** d
                        * 4
                        * tau
                        * support
                        * mp.sinh(2 * tau * support)
                        / (4 * tau**2 * support**2 + mp.pi**2 * d**2)
                    )
            minimum = np.linalg.eigvalsh(gram)[0]
            if minimum < 2 - 1e-10:
                raise RuntimeError(("Hardy Gram floor failed", support, tau, half_width, minimum))

print("finite Gram floor tests PASS")
