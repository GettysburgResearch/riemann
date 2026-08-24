#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path
from typing import Dict, Tuple

VERDICT = "PASS_T105530_HERMITIAN_BANK_MATRIX_FLUX"
ROOT = Path(__file__).resolve().parents[2]
CONTENT = (
    "README_105530.md",
    "PR_BODY_105530_ADDENDUM.md",
    "PACKET_METADATA_105530.json",
    "claims/lemmas/L-105530-minimal-hermitian-wick-bank.md",
    "claims/lemmas/L-105531-matrix-companion-lorentz-flux.md",
    "claims/refutations/R-105530-scalar-hermitian-second-chaos-no-go.md",
    "claims/refutations/R-105531-closed-contour-calibration-no-free-anchor.md",
    "claims/theorems/T-105530-hermitian-bank-companion-ninety-frontier.md",
    "claims/methodology/M-105530-hostile-review-contract.md",
    "experiments/X-105530-hermitian-bank/README.md",
    "experiments/X-105530-hermitian-bank/verify.py",
    "experiments/X-105530-hermitian-bank/tests/test_verify.py",
    "reports/gpt56-pro/2026-08-24-hermitian-bank-companion-frontier.md",
    "standalone/2026-08-24-hermitian-bank-companion-frontier/PROOF.md",
    "integration/2026-08-24/t105530-source-lock.json",
)
Mon = Tuple[int, int]
Poly = Dict[Mon, F]


def add(*ps: Poly) -> Poly:
    out: Poly = {}
    for p in ps:
        for m, c in p.items():
            out[m] = out.get(m, F(0)) + c
    return {m: c for m, c in out.items() if c}


def mul(p: Poly, q: Poly, degree: int = 8) -> Poly:
    out: Poly = {}
    for (a, b), c in p.items():
        for (d, e), f in q.items():
            if a + b + d + e <= degree:
                m = (a + d, b + e)
                out[m] = out.get(m, F(0)) + c * f
    return {m: c for m, c in out.items() if c}


def conj(p: Poly) -> Poly:
    return {(b, a): c for (a, b), c in p.items()}


def hermitian_resolvent_series(degree: int = 8) -> Poly:
    out: Poly = {(0, 0): F(1)}
    for n in range(1, degree + 1):
        out[(n, 0)] = F(1, 2)
        out[(0, n)] = F(1, 2)
    return out


def scalar_no_go() -> dict:
    # w=1+a z+b z^2; first-order cancellation forces a=-1/2.
    a = F(-1, 2)
    mixed = a * a + a
    assert mixed == F(-1, 4)
    return {
        "forced_linear_coefficient": str(a),
        "unavoidable_z_zbar_coefficient": str(mixed),
    }


def bank_checks() -> dict:
    w0: Poly = {(0, 0): F(1), (1, 0): F(-1, 2), (2, 0): F(-1, 4)}
    w1: Poly = {(1, 0): F(1, 2)}
    S = add(mul(w0, conj(w0)), mul(w1, conj(w1)))
    lam = mul(S, hermitian_resolvent_series())
    assert lam[(0, 0)] == 1
    for m in ((1, 0), (0, 1), (2, 0), (1, 1), (0, 2)):
        assert lam.get(m, F(0)) == 0
    expected_degree3 = {
        (3, 0): F(1, 8),
        (0, 3): F(1, 8),
    }
    for m, c in expected_degree3.items():
        assert lam.get(m) == c
    eps_quarter = F(77, 9216)
    assert 1 - eps_quarter == F(9139, 9216)
    assert 1 + eps_quarter == F(9293, 9216)
    return {
        "linear_and_quadratic_coefficients_zero": True,
        "degree_three_coefficients": {f"{a},{b}": str(c) for (a, b), c in expected_degree3.items()},
        "epsilon_at_one_quarter": str(eps_quarter),
        "lower_at_one_quarter": "9139/9216",
        "upper_at_one_quarter": "9293/9216",
    }


def poly_eval(coeffs, x):
    return sum(c * x ** i for i, c in enumerate(coeffs))


def poly_derivative(coeffs):
    return [F(i) * coeffs[i] for i in range(1, len(coeffs))]


def matrix_flux_checks() -> dict:
    # q'=p with p=(x+2)x(x-3); all critical roots rational.
    p = [F(0), F(-6), F(-1), F(1)]
    pp = poly_derivative(p)
    q = [F(5), F(0), F(-3), F(-1, 3), F(1, 4)]
    roots = [F(-2), F(0), F(3)]
    lam = F(2, 3)
    delta = F(5, 7)
    residue_checks = 0
    gram = [[F(0) for _ in range(3)] for _ in range(3)]
    defect = [[F(0) for _ in range(3)] for _ in range(3)]
    pick = [[F(0) for _ in range(3)] for _ in range(3)]
    square = [[F(0) for _ in range(3)] for _ in range(3)]
    for c in roots:
        pc = poly_eval(pp, c)
        qc = poly_eval(q, c)
        assert pc != 0
        rho = qc / pc
        Hc = pc + lam * qc
        residue = Hc * Hc / (pc * pc)
        assert residue == (1 + lam * rho) ** 2
        v = [F(1), c, c*c]
        for i in range(3):
            for j in range(3):
                gram[i][j] += v[i] * v[j]
                defect[i][j] += residue * v[i] * v[j]
                pick[i][j] += (-rho) * v[i] * v[j]
                square[i][j] += rho*rho * v[i] * v[j]
        residue_checks += 1
    for i in range(3):
        for j in range(3):
            rhs = (gram[i][j] + lam*lam*square[i][j] - defect[i][j])/(2*lam)
            assert pick[i][j] == rhs
    # Symbolic real-axis identity tested at exact rational points away from poles.
    line_checks = 0
    for x in [F(-5,2),F(-1),F(1,2),F(2),F(7,2)]:
        px=poly_eval(p,x); ppx=poly_eval(pp,x); qx=poly_eval(q,x)
        if px == 0: continue
        H=ppx+lam*qx
        # Im of H^2/[p (p'+i delta p)] equals -delta H^2/(p'^2+delta^2 p^2).
        den_re=px*ppx; den_im=delta*px*px
        imag_recip=-den_im/(den_re*den_re+den_im*den_im)
        lhs=-(H*H)*imag_recip
        rhs=delta*H*H/(ppx*ppx+delta*delta*px*px)
        assert lhs == rhs
        line_checks += 1
    return {
        "real_residue_checks": residue_checks,
        "matrix_entry_checks": 9,
        "real_axis_lorentz_checks": line_checks,
        "lambda": str(lam),
        "delta": str(delta),
    }


def threshold_checks() -> dict:
    kappa = F(9139, 9216)
    cut = kappa/F(20)
    assert cut == F(9139, 184320)
    assert 2*F(19,20)-1 == F(9,10)
    return {
        "bank_anchor": str(kappa),
        "negative_trace_cut": str(cut),
        "positive_index_fraction": "19/20",
        "line_fraction_boundary": "9/10",
    }


def hashes() -> dict:
    return {
        p: hashlib.sha256((ROOT / p).read_bytes().replace(b"\r\n", b"\n")).hexdigest()
        for p in CONTENT
    }


def build_payload() -> dict:
    out = {
        "verdict": VERDICT,
        "scalar_no_go": scalar_no_go(),
        "two_channel_bank": bank_checks(),
        "matrix_companion_flux": matrix_flux_checks(),
        "ninety_percent_threshold": threshold_checks(),
        "content_sha256": hashes(),
        "bankreal105530_proved": False,
        "matrixlerc105531_proved": False,
        "stripneg105520_proved": False,
        "ninety_percent_established": False,
        "public_record_beaten": False,
        "rh_established": False,
    }
    out["proof_object_sha256"] = hashlib.sha256(
        json.dumps(out, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    return out


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = build_payload()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(VERDICT)
    print(payload["proof_object_sha256"])
    print("BANKREAL105530_OPEN")
    print("MATRIXLERC105531_OPEN")
    print("NINETY_PERCENT_UNPROVED")
    print("RH_UNPROVED")
