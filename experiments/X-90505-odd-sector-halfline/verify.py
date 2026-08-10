#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp
import numpy as np

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "results" / "verification.json"
mp.mp.dps = 70


def inertia(a: np.ndarray, tol: float = 1e-10) -> tuple[int, int, int]:
    e = np.linalg.eigvalsh((a + a.conj().T) / 2)
    return int(np.sum(e > tol)), int(np.sum(e < -tol)), int(np.sum(np.abs(e) <= tol))


def h(x: mp.mpf) -> mp.mpc:
    return mp.e ** (-mp.mpf("0.3") * x * x) * (1 + mp.mpf("0.2") * 1j * mp.sin(mp.mpf("1.7") * x))


def F(u: mp.mpf) -> mp.mpc:
    if u > 0:
        return h(u)
    if u < 0:
        return -h(-u)
    return mp.mpc(0)


def main() -> None:
    # One known even pole-negative line, and one even plus one odd negative line per quartet.
    index_cases = []
    for p in range(9):
        odd = -np.eye(p)
        even = -np.eye(p + 1)
        if inertia(odd)[1] != p or inertia(even)[1] != p + 1:
            raise AssertionError(p)
        index_cases.append({"quartets": p, "odd_negative_index": p, "even_negative_index": p + 1})

    errors = []
    for y in (mp.mpf("0.2"), mp.mpf("0.7"), mp.mpf("1.5"), mp.mpf("3.0")):
        corr_direct = mp.quad(lambda u: F(u) * mp.conj(F(u - y)), [-mp.inf, 0, y, mp.inf])
        energy_direct = mp.quad(lambda u: abs(F(u) - F(u - y)) ** 2, [-mp.inf, 0, y, mp.inf])

        A = mp.quad(lambda x: h(x + y) * mp.conj(h(x)), [0, mp.inf])
        B = mp.quad(lambda x: h(x) * mp.conj(h(y - x)), [0, y])
        corr_half = 2 * mp.re(A) - B

        diff = mp.quad(lambda x: abs(h(x + y) - h(x)) ** 2, [0, mp.inf])
        boundary = mp.quad(lambda x: abs(h(x) + h(y - x)) ** 2, [0, y])
        energy_half = 2 * diff + boundary

        err_corr = abs(corr_direct - corr_half)
        err_energy = abs(energy_direct - energy_half)
        errors.append({
            "y": str(y),
            "correlation_error": mp.nstr(err_corr, 8),
            "energy_error": mp.nstr(err_energy, 8),
        })
        if err_corr > mp.mpf("1e-50") or err_energy > mp.mpf("1e-50"):
            raise AssertionError((y, corr_direct, corr_half, energy_direct, energy_half))

    result = {
        "verdict": "PASS_X_90505_ODD_SECTOR_HALFLINE",
        "index_cases": index_cases,
        "halfline_identity_checks": errors,
        "scope": "Finite parity algebra and high-precision half-line identities only; no all-prime sign theorem or RH claim.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["verdict"])
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
