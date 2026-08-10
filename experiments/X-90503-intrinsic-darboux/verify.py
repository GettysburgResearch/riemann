#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp
import numpy as np

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "results" / "verification.json"
mp.mp.dps = 70


def base_kernel(a: mp.mpf, z: mp.mpc, w: mp.mpc) -> mp.mpc:
    return 4 * a / (4 * a * a + (z - mp.conj(w)) ** 2)


def darboux_multiplier(c: mp.mpf, z: mp.mpc) -> mp.mpc:
    return -(z * z + mp.mpf("0.25")) / (c * c + z * z) ** 2


def kernel(a: mp.mpf, c: mp.mpf, z: mp.mpc, w: mp.mpc) -> mp.mpc:
    return darboux_multiplier(c, z) * mp.conj(darboux_multiplier(c, w)) * base_kernel(a, z, w)


def green_solution(x: mp.mpf, f) -> mp.mpf:
    # Split at the cusp u=x and factor the two exponential tails.  This is
    # numerically stable even when the pole moments nearly cancel.
    left = mp.quad(lambda u: mp.e ** (u / 2) * f(u), [-mp.inf, x])
    right = mp.quad(lambda u: mp.e ** (-u / 2) * f(u), [x, mp.inf])
    return -mp.e ** (-x / 2) * left - mp.e ** (x / 2) * right


def main() -> None:
    a = mp.mpf("0.8")
    c = mp.mpf("1.7")
    zp, zm = mp.mpc(0, 0.5), mp.mpc(0, -0.5)
    pole_errors = [abs(kernel(a, c, z, zp)) for z in (mp.mpc(1.2, 0.1), mp.mpc(4.0, -0.2))]
    pole_errors += [abs(kernel(a, c, z, zm)) for z in (mp.mpc(1.2, 0.1), mp.mpc(4.0, -0.2))]

    nodes = [mp.mpc("1.1", "0.1"), mp.mpc("2.7", "-0.2"), mp.mpc("5.3", "0.35")]
    gram = np.array([[complex(kernel(a, c, z, w)) for w in nodes] for z in nodes])
    gram = (gram + gram.conj().T) / 2
    gram_eigs = np.linalg.eigvalsh(gram)

    # f=(d^2-1/4) exp(-u^2) is pole-null by construction; Green inversion must recover exp(-u^2).
    h = lambda u: mp.e ** (-u * u)
    f = lambda u: (4 * u * u - mp.mpf("2.25")) * mp.e ** (-u * u)
    xs = [mp.mpf(x) for x in (-3, -1, 0, 1, 3)]
    inversion_errors = [abs(green_solution(x, f) - h(x)) for x in xs]

    # Direct pole moments of f.
    moment_plus = mp.quad(lambda u: f(u) * mp.e ** (-u / 2), [-mp.inf, 0, mp.inf])
    moment_minus = mp.quad(lambda u: f(u) * mp.e ** (u / 2), [-mp.inf, 0, mp.inf])

    if max(pole_errors) > mp.mpf("1e-50"):
        raise AssertionError(pole_errors)
    if float(gram_eigs.min()) <= 0:
        raise AssertionError(gram_eigs)
    if max(inversion_errors) > mp.mpf("1e-45"):
        raise AssertionError(inversion_errors)
    if max(abs(moment_plus), abs(moment_minus)) > mp.mpf("1e-45"):
        raise AssertionError([moment_plus, moment_minus])

    result = {
        "verdict": "PASS_X_90503_INTRINSIC_DARBOUX",
        "pole_kernel_max": mp.nstr(max(pole_errors), 8),
        "minimum_gram_eigenvalue": float(gram_eigs.min()),
        "green_inversion_max_error": mp.nstr(max(inversion_errors), 8),
        "pole_moments": [mp.nstr(moment_plus, 8), mp.nstr(moment_minus, 8)],
        "scope": "Finite/high-precision identities only; no trace-class sign theorem or RH claim.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["verdict"])
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
