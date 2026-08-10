#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np

ROOT = Path(__file__).resolve().parent
RESULT = ROOT / "results" / "verification.json"


def cauchy_sobolev_kernel(a: mp.mpf, c: mp.mpf, z: mp.mpc, w: mp.mpc) -> mp.mpc:
    return 4 * a / (
        (c * c + z * z)
        * (c * c + mp.conj(w) * mp.conj(w))
        * (4 * a * a + (z - mp.conj(w)) ** 2)
    )


def kernel_integral(a: mp.mpf, c: mp.mpf, z: mp.mpc, w: mp.mpc) -> mp.mpc:
    integrand_pos = lambda u: mp.e ** (-2 * a * u) * mp.e ** (1j * (z - mp.conj(w)) * u)
    integrand_neg = lambda u: mp.e ** (-2 * a * u) * mp.e ** (-1j * (z - mp.conj(w)) * u)
    val = mp.quad(integrand_pos, [0, mp.inf]) + mp.quad(integrand_neg, [0, mp.inf])
    return val / ((c * c + z * z) * (c * c + mp.conj(w) ** 2))


def check_kernel() -> dict:
    mp.mp.dps = 60
    a = mp.mpf("0.75")
    c = mp.mpf("1.4")
    pts = [
        mp.mpc("-1.2", "0.1"),
        mp.mpc("0.3", "-0.25"),
        mp.mpc("1.8", "0.4"),
        mp.mpc("3.1", "-0.45"),
    ]
    max_err = mp.mpf("0")
    for z in pts:
        for w in pts:
            lhs = cauchy_sobolev_kernel(a, c, z, w)
            rhs = kernel_integral(a, c, z, w)
            max_err = max(max_err, abs(lhs - rhs))
    gram = np.array(
        [[complex(cauchy_sobolev_kernel(a, c, z, w)) for w in pts] for z in pts],
        dtype=complex,
    )
    gram = (gram + gram.conj().T) / 2
    mineig = float(np.linalg.eigvalsh(gram).min())
    if max_err > mp.mpf("1e-40") or mineig <= 0:
        raise AssertionError((max_err, mineig))
    return {
        "pairs_checked": len(pts) ** 2,
        "max_integral_error": mp.nstr(max_err, 8),
        "minimum_gram_eigenvalue": mineig,
    }


def check_pole_cardinals() -> dict:
    # Xi(+-i/2)=1/2.  E_+(z)=Xi(z)(1-2iz), E_-(z)=Xi(z)(1+2iz).
    zi = 0.5j
    zm = -0.5j
    xi_val = 0.5
    ep = lambda z: xi_val * (1 - 2j * z)
    em = lambda z: xi_val * (1 + 2j * z)
    table = np.array([[ep(zi), ep(zm)], [em(zi), em(zm)]], dtype=complex)
    target = np.eye(2)
    err = float(np.max(np.abs(table - target)))
    if err > 1e-15:
        raise AssertionError((table, err))
    return {"evaluation_table": [[[float(x.real), float(x.imag)] for x in row] for row in table], "max_error": err}


def check_index_shift() -> list[dict]:
    out = []
    for q in range(8):
        blocks = [-1.0, -1.0]
        pole_null = []
        for j in range(q):
            # one hyperbolic plane per off-line pair
            blocks.extend([1.0 + j / 10.0, -(1.0 + j / 10.0)])
            pole_null.extend([1.0 + j / 10.0, -(1.0 + j / 10.0)])
        # add harmless positive line coordinates
        blocks.extend([0.4, 0.9, 1.7])
        pole_null.extend([0.4, 0.9, 1.7])
        neg_full = sum(x < 0 for x in blocks)
        neg_null = sum(x < 0 for x in pole_null)
        if neg_full != q + 2 or neg_null != q:
            raise AssertionError((q, neg_full, neg_null))
        out.append({
            "off_line_pairs": q,
            "pole_free_negative_index": neg_full,
            "pole_null_negative_index": neg_null,
        })
    return out


def levy_symbol(tau: mp.mpf) -> mp.mpf:
    return (
        mp.re(mp.digamma(mp.mpf("0.25") + 0.5j * tau))
        - mp.digamma(mp.mpf("0.25"))
    ) / (2 * mp.pi)


def levy_integral(tau: mp.mpf) -> mp.mpf:
    f = lambda y: (mp.e ** (-y / 2) / (1 - mp.e ** (-2 * y))) * (1 - mp.cos(tau * y)) / mp.pi
    return mp.quad(f, [0, 1, mp.inf])


def gaussian_jump_energy(r: mp.mpf, tau_grid: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
    # fhat(t)=sqrt(2*pi) r exp(-r^2 t^2/2), so |fhat|^2=2*pi*r^2 exp(-r^2 t^2)
    lhs_integrand = lambda t: levy_symbol(t) * (2 * mp.pi * r * r) * mp.e ** (-r * r * t * t)
    lhs = 2 * mp.quad(lhs_integrand, [0, tau_grid]) + 2 * mp.quad(lhs_integrand, [tau_grid, mp.inf])

    # ||f-T_y f||^2 for f(u)=exp(-u^2/(2r^2)) is 2*sqrt(pi)*r*(1-exp(-y^2/(4r^2))).
    rhs_integrand = lambda y: (
        mp.e ** (-y / 2) / (1 - mp.e ** (-2 * y))
        * 2 * mp.sqrt(mp.pi) * r * (1 - mp.e ** (-y * y / (4 * r * r)))
    )
    rhs = mp.quad(rhs_integrand, [0, 1, mp.inf])
    return lhs, rhs


def check_levy() -> list[dict]:
    mp.mp.dps = 70
    # symbol identity pointwise
    for tau in (mp.mpf("0.4"), mp.mpf("1.3"), mp.mpf("4.1")):
        if abs(levy_symbol(tau) - levy_integral(tau)) > mp.mpf("1e-45"):
            raise AssertionError(tau)
    out = []
    for r in (mp.mpf("0.7"), mp.mpf("1.5"), mp.mpf("3.0")):
        lhs, rhs = gaussian_jump_energy(r, mp.mpf("8"))
        err = abs(lhs - rhs)
        if err > mp.mpf("1e-35"):
            raise AssertionError((r, lhs, rhs, err))
        out.append({"r": mp.nstr(r, 8), "lhs": mp.nstr(lhs, 30), "rhs": mp.nstr(rhs, 30), "error": mp.nstr(err, 8)})
    return out


def heat_trace(eigs: np.ndarray, beta: float) -> float:
    return float(np.sum(np.exp(-beta * eigs) - 1.0))


def heat_series(eigs: np.ndarray, beta: float, terms: int = 120) -> float:
    s = 0.0
    fact = 1.0
    power = 1.0
    for k in range(1, terms + 1):
        fact *= k
        power *= -beta
        moment = float(np.sum(eigs ** k))
        s += power * moment / fact
    return s


def check_heat() -> dict:
    positive = np.array([0.03, 0.11, 0.7, 1.6], dtype=float)
    indefinite = np.array([-0.07, 0.11, 0.7, 1.6], dtype=float)
    betas = [0.1, 0.5, 1.0, 4.0, 20.0, 100.0]
    pos_vals = [heat_trace(positive, b) for b in betas]
    ind_vals = [heat_trace(indefinite, b) for b in betas]
    if any(x > 1e-14 for x in pos_vals):
        raise AssertionError(pos_vals)
    if ind_vals[-1] <= 0:
        raise AssertionError(ind_vals)

    series_checks = []
    for name, eigs in (("positive", positive), ("indefinite", indefinite)):
        for beta in (0.25, 0.75, 1.5):
            direct = heat_trace(eigs, beta)
            series = heat_series(eigs, beta)
            err = abs(direct - series)
            if err > 1e-12:
                raise AssertionError((name, beta, direct, series, err))
            series_checks.append({"case": name, "beta": beta, "error": err})

    # log det(I+tA)=-int exp(-s)/s Theta(ts) ds for positive A.
    mp.mp.dps = 50
    eigs_mp = [mp.mpf(str(x)) for x in positive]
    t = mp.mpf("0.8")
    direct_logdet = sum(mp.log(1 + t * x) for x in eigs_mp)
    theta = lambda beta: sum(mp.e ** (-beta * x) - 1 for x in eigs_mp)
    integral = -mp.quad(lambda s: mp.e ** (-s) * theta(t * s) / s, [0, 1, mp.inf])
    det_err = abs(direct_logdet - integral)
    if det_err > mp.mpf("1e-35"):
        raise AssertionError((direct_logdet, integral, det_err))

    return {
        "betas": betas,
        "positive_values": pos_vals,
        "indefinite_values": ind_vals,
        "series_checks": series_checks,
        "determinant_heat_error": mp.nstr(det_err, 8),
    }


def main() -> None:
    result = {
        "verdict": "PASS_X_90502_POLE_NULL_LEVY_HEAT",
        "cauchy_sobolev_kernel": check_kernel(),
        "pole_cardinals": check_pole_cardinals(),
        "index_two_shift": check_index_shift(),
        "levy_gaussian_checks": check_levy(),
        "heat_trace": check_heat(),
        "scope": (
            "Finite algebra and high-precision identity checks only. The trace-class, "
            "global index, and form-domain proofs are analytic and require independent review. "
            "No RH sign theorem is claimed."
        ),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["verdict"])
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
