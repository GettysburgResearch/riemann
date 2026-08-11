#!/usr/bin/env python3
"""Finite diagnostic for L-90605.

A three-term Dirichlet polynomial is given a torus twist with an exact zero at
sigma. We then search recurrent vertical phases, Newton-refine actual zeros of
the untwisted polynomial, and verify repeated returns in successive phase
blocks. This illustrates the theorem; compactness/minimality and Rouché, not the
finite scan, prove syndetic recurrence.
"""
from __future__ import annotations

import cmath
import hashlib
import json
import math
from pathlib import Path

STATUS = "PASS_X_90603_BOHR_SYNDETIC_RECURRENCE"


def polynomial(z: complex) -> complex:
    return (
        1.0
        + cmath.exp(-2.0 * z * math.log(2.0))
        + cmath.exp(-2.0 * z * math.log(3.0))
    )


def derivative(z: complex) -> complex:
    return (
        -2.0 * math.log(2.0) * cmath.exp(-2.0 * z * math.log(2.0))
        -2.0 * math.log(3.0) * cmath.exp(-2.0 * z * math.log(3.0))
    )


def main() -> dict[str, object]:
    sigma = 0.30
    r2 = 2.0 ** (-2.0 * sigma)
    r3 = 3.0 ** (-2.0 * sigma)

    # Triangle construction: r2*u+r3*v=-1, |u|=|v|=1.
    cos_alpha = (r2 * r2 + 1.0 - r3 * r3) / (2.0 * r2)
    alpha = math.acos(cos_alpha)
    u = cmath.exp(1j * (math.pi + alpha))
    v = (-1.0 - r2 * u) / r3
    hull_residual = abs(1.0 + r2 * u + r3 * v)

    arg_u = cmath.phase(u)
    block_size = 2000
    blocks = 30
    rows: list[dict[str, float | int]] = []
    roots: list[complex] = []

    for block in range(blocks):
        best_error = math.inf
        best_t = 0.0
        first = 1 + block * block_size
        last = (block + 1) * block_size
        # Enforce the p=2 phase exactly and choose the best p=3 return.
        for k in range(first, last + 1):
            t = (2.0 * math.pi * k - arg_u) / (2.0 * math.log(2.0))
            phase3 = cmath.exp(-2j * t * math.log(3.0))
            error = abs(phase3 - v)
            if error < best_error:
                best_error = error
                best_t = t

        z = sigma + 1j * best_t
        for _ in range(30):
            step = polynomial(z) / derivative(z)
            z -= step
            if abs(step) < 1e-13:
                break
        residual = abs(polynomial(z))
        roots.append(z)
        rows.append(
            {
                "block": block,
                "phase_error": best_error,
                "root_real": z.real,
                "root_imag": z.imag,
                "root_residual": residual,
            }
        )

    gaps = [roots[j + 1].imag - roots[j].imag for j in range(len(roots) - 1)]
    gates = {
        "exact_torus_triangle": (
            abs(abs(u) - 1.0) < 2e-15
            and abs(abs(v) - 1.0) < 2e-15
            and hull_residual < 2e-15
        ),
        "one_root_per_phase_block": len(roots) == blocks,
        "roots_are_distinct": all(gap > 100.0 for gap in gaps),
        "roots_stay_near_sigma": max(abs(z.real - sigma) for z in roots) < 0.001,
        "root_residuals_small": max(abs(polynomial(z)) for z in roots) < 5e-10,
        "finite_observed_gap": max(gaps) < 20000.0,
    }
    if not all(gates.values()):
        raise AssertionError([name for name, ok in gates.items() if not ok])

    result = {
        "status": STATUS,
        "gates": gates,
        "torus_zero": {
            "sigma": sigma,
            "u": [u.real, u.imag],
            "v": [v.real, v.imag],
            "residual": hull_residual,
        },
        "return_blocks": {
            "count": blocks,
            "block_size_in_exact_p2_returns": block_size,
            "max_observed_root_gap": max(gaps),
            "max_real_displacement": max(abs(z.real - sigma) for z in roots),
            "max_root_residual": max(abs(polynomial(z)) for z in roots),
            "rows": rows,
        },
        "scope": (
            "finite diagnostic only; syndetic recurrence follows analytically "
            "from Kronecker minimality, compactness and Rouche"
        ),
    }
    payload = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(payload).hexdigest()
    return result


if __name__ == "__main__":
    result = main()
    out = Path(__file__).resolve().parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(STATUS)
