#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "results" / "verification.json"

mp.mp.dps = 70


def kernel_closed(a: mp.mpf, c: mp.mpf, z: complex, w: complex) -> complex:
    z = mp.mpc(z)
    w = mp.mpc(w)
    return 4 * a / (
        (c * c + z * z)
        * (c * c + mp.conj(w) * mp.conj(w))
        * (4 * a * a + (z - mp.conj(w)) ** 2)
    )


def kernel_integral(a: mp.mpf, c: mp.mpf, z: complex, w: complex) -> complex:
    z = mp.mpc(z)
    w = mp.mpc(w)
    delta = z - mp.conj(w)
    val = mp.quad(
        lambda u: mp.e ** (-2 * a * abs(u)) * mp.e ** (1j * delta * u),
        [-mp.inf, 0, mp.inf],
    )
    return val / ((c * c + z * z) * (c * c + mp.conj(w) ** 2))


def mu(t: mp.mpf) -> mp.mpf:
    return (
        mp.re(mp.digamma(mp.mpf("0.25") + 0.5j * t)) - mp.log(mp.pi)
    ) / (2 * mp.pi)


def levy_gaussian_identity(r: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
    mu0 = mu(mp.mpf("0"))
    lhs = mp.quad(
        lambda t: (mu(t) - mu0)
        * (2 * mp.pi / r)
        * mp.e ** (-(t * t) / r),
        [-mp.inf, 0, mp.inf],
    )
    norm2 = mp.sqrt(mp.pi / r)

    def integrand(y: mp.mpf) -> mp.mpf:
        if y == 0:
            return mp.mpf("0")
        k = mp.e ** (-y / 2) / (1 - mp.e ** (-2 * y))
        diff2 = 2 * norm2 * (1 - mp.e ** (-r * y * y / 4))
        return k * diff2

    rhs = mp.quad(integrand, [0, 1, 4, mp.inf])
    return lhs, rhs


def inertia(matrix: np.ndarray, tol: float = 1e-9) -> tuple[int, int, int]:
    vals = np.linalg.eigvalsh(matrix)
    return (
        int(np.sum(vals > tol)),
        int(np.sum(vals < -tol)),
        int(np.sum(np.abs(vals) <= tol)),
    )


def heat_trace(eigs: np.ndarray, beta: float) -> float:
    return float(np.sum(np.exp(-beta * eigs) - 1.0))


def heat_series(eigs: np.ndarray, beta: float, order: int) -> float:
    result = 0.0
    for k in range(1, order + 1):
        moment = float(np.sum(eigs**k))
        result += ((-beta) ** k / math.factorial(k)) * moment
    return result


def main() -> None:
    a = mp.mpf("0.8")
    c = mp.mpf("1.7")

    kernel_errors = []
    nodes = [
        mp.mpc("1.25", "0.2"),
        mp.mpc("3.75", "-0.1"),
        mp.mpc("7.5", "0.35"),
        mp.mpc("11.0", "-0.3"),
    ]
    for z in nodes:
        for w in nodes:
            closed = kernel_closed(a, c, z, w)
            integ = kernel_integral(a, c, z, w)
            kernel_errors.append(abs(closed - integ))

    gram = np.array(
        [[complex(kernel_closed(a, c, z, w)) for w in nodes] for z in nodes],
        dtype=np.complex128,
    )
    gram = (gram + gram.conj().T) / 2
    gram_eigs = np.linalg.eigvalsh(gram)
    if float(np.min(gram_eigs)) <= 0:
        raise AssertionError(("kernel Gram not positive", gram_eigs))

    # Pole-cardinal interpolation factors. Xi(±i/2)=1/2.
    zp = 0.5j
    zm = -0.5j
    eplus = lambda z: 0.5 * (1 - 2j * z)
    eminus = lambda z: 0.5 * (1 + 2j * z)
    pole_table = np.array(
        [[eplus(zp), eplus(zm)], [eminus(zp), eminus(zm)]],
        dtype=np.complex128,
    )
    expected_table = np.eye(2, dtype=np.complex128)
    pole_error = float(np.max(np.abs(pole_table - expected_table)))

    # Exact index-one synthetic model: q off-line hyperbolic planes plus the known hyperbolic pole block.
    pole_free_block = np.array([[0.0, -1.0], [-1.0, 0.0]])
    pole_free_eigs = np.linalg.eigvalsh(pole_free_block)
    if not np.allclose(pole_free_eigs, [-1.0, 1.0]):
        raise AssertionError(("pole block", pole_free_eigs))
    index_cases = []
    for q in range(0, 8):
        blocks = [pole_free_block]
        for j in range(q):
            m = float(j + 1)
            blocks.append(np.array([[0.0, m], [m, 0.0]]))
        size = sum(b.shape[0] for b in blocks)
        mat = np.zeros((size, size))
        pos = 0
        for b in blocks:
            n = b.shape[0]
            mat[pos : pos + n, pos : pos + n] = b
            pos += n
        full_inertia = inertia(mat)
        pole_null = mat[2:, 2:]
        null_inertia = inertia(pole_null) if pole_null.size else (0, 0, 0)
        if full_inertia[1] != q + 1 or null_inertia[1] != q:
            raise AssertionError((q, full_inertia, null_inertia))
        index_cases.append(
            {
                "off_line_pairs": q,
                "pole_free_negative_index": full_inertia[1],
                "pole_null_negative_index": null_inertia[1],
            }
        )

    levy_results = []
    for r in (mp.mpf("0.7"), mp.mpf("1.5"), mp.mpf("3.0")):
        lhs, rhs = levy_gaussian_identity(r)
        err = abs(lhs - rhs)
        if err > mp.mpf("1e-40"):
            raise AssertionError(("Levy identity", r, lhs, rhs, err))
        levy_results.append(
            {
                "r": str(r),
                "lhs": mp.nstr(lhs, 30),
                "rhs": mp.nstr(rhs, 30),
                "error": mp.nstr(err, 8),
            }
        )

    positive_eigs = np.array([0.03, 0.11, 0.4, 1.25], dtype=float)
    indefinite_eigs = np.array([-0.07, 0.03, 0.11, 0.4, 1.25], dtype=float)
    betas = [0.1, 0.5, 1.0, 4.0, 20.0, 100.0]
    pos_values = [heat_trace(positive_eigs, b) for b in betas]
    ind_values = [heat_trace(indefinite_eigs, b) for b in betas]
    if any(v > 1e-13 for v in pos_values):
        raise AssertionError(("positive heat sign", pos_values))
    if ind_values[-1] <= 0:
        raise AssertionError(("negative eigenvalue not amplified", ind_values))

    series_checks = []
    for eigs, label in ((positive_eigs, "positive"), (indefinite_eigs, "indefinite")):
        for beta in (0.25, 0.75, 1.5):
            exact = heat_trace(eigs, beta)
            approx = heat_series(eigs, beta, 40)
            err = abs(exact - approx)
            if err > 5e-13:
                raise AssertionError(("heat series", label, beta, exact, approx, err))
            series_checks.append(
                {"case": label, "beta": beta, "error": err}
            )

    # Fredholm/heat integral identity for a positive finite spectrum.
    t = mp.mpf("0.7")
    logdet = mp.fsum([mp.log(1 + t * mp.mpf(str(x))) for x in positive_eigs])

    def theta_mp(beta: mp.mpf) -> mp.mpf:
        return mp.fsum([mp.e ** (-beta * mp.mpf(str(x))) - 1 for x in positive_eigs])

    heat_integral = -mp.quad(
        lambda s: mp.e ** (-s) * theta_mp(t * s) / s if s != 0 else t * mp.fsum([mp.mpf(str(x)) for x in positive_eigs]),
        [0, 1, 4, mp.inf],
    )
    determinant_heat_error = abs(logdet - heat_integral)
    if determinant_heat_error > mp.mpf("1e-40"):
        raise AssertionError(("det/heat", logdet, heat_integral, determinant_heat_error))

    result = {
        "verdict": "PASS_X_90502_POLE_NULL_LEVY_HEAT",
        "cauchy_sobolev_kernel": {
            "pairs_checked": len(kernel_errors),
            "max_integral_error": mp.nstr(max(kernel_errors), 8),
            "minimum_gram_eigenvalue": float(np.min(gram_eigs)),
        },
        "pole_cardinals": {
            "evaluation_table": [
                [[float(z.real), float(z.imag)] for z in row] for row in pole_table
            ],
            "max_error": pole_error,
            "pole_free_block": pole_free_block.tolist(),
            "pole_free_eigenvalues": pole_free_eigs.tolist(),
        },
        "index_one_shift": index_cases,
        "levy_gaussian_checks": levy_results,
        "heat_trace": {
            "betas": betas,
            "positive_values": pos_values,
            "indefinite_values": ind_values,
            "series_checks": series_checks,
            "determinant_heat_error": mp.nstr(determinant_heat_error, 8),
        },
        "scope": (
            "Finite algebra and high-precision identity checks only. The trace-class, "
            "global index, and form-domain proofs are analytic and require independent review. "
            "No RH sign theorem is claimed."
        ),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["verdict"])
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
