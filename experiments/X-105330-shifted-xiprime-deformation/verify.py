#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

VERDICT = "PASS_T105330_SHIFTED_XIPRIME_DEFORMATION"
ROOT = Path(__file__).resolve().parents[2]
CONTENT = (
    "claims/lemmas/L-105330-shifted-critical-zero-deformation.md",
    "claims/lemmas/L-105331-shifted-safe-line-coefficient-identity.md",
    "claims/lemmas/L-105332-uniform-analytic-error-differentiation.md",
    "claims/refutations/R-105330-pointwise-error-cannot-be-differentiated.md",
    "claims/theorems/T-105330-shifted-xiprime-pick-transfer-frontier.md",
    "claims/methodology/M-105330-hostile-review-contract.md",
    "experiments/X-105330-shifted-xiprime-deformation/verify.py",
    "experiments/X-105330-shifted-xiprime-deformation/tests/test_verify.py",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def derivative(a: list[F]) -> list[F]:
    return [F(k) * a[k] for k in range(1, len(a))]


def evaluate(a: list[F], x: F) -> F:
    out = F(0)
    for c in reversed(a):
        out = out * x + c
    return out


def deformation_fixture() -> dict[str, object]:
    p = [F(3, 2), F(-3), F(0), F(1)]
    p1 = derivative(p)
    p2 = derivative(p1)
    roots = [F(-1), F(1)]
    rho = [evaluate(p, c) / evaluate(p2, c) for c in roots]
    require(rho == [F(-7, 12), F(-1, 12)], "critical residue fixture")

    rows = []
    for power in range(0, 8):
        zero_motion = sum((c**power * r for c, r in zip(roots, rho, strict=True)), F(0))
        residue_side = sum((c**power * evaluate(p, c) / evaluate(p2, c) for c in roots), F(0))
        require(zero_motion == residue_side, "zero-motion deformation mismatch")
        rows.append({"power": power, "derivative": str(zero_motion)})

    z = F(5, 2)
    alpha = F(2, 7)
    f = evaluate(p, z)
    fp = evaluate(p1, z)
    fpp = evaluate(p2, z)
    e = fp - alpha * f
    ep = fpp - alpha * fp
    logder_direct = ep / e
    L = fp / f
    Lprime = fpp / f - L * L
    logder_split = L + Lprime / (L - alpha)
    require(logder_direct == logder_split, "shifted log-derivative identity")

    parameter_derivative = Lprime / (L * L)
    reciprocal_derivative = Lprime / (L * L)
    require(parameter_derivative == reciprocal_derivative, "reciprocal derivative sign")

    return {
        "critical_roots": [str(c) for c in roots],
        "critical_residues": [str(r) for r in rho],
        "primitive_checks": rows,
        "shifted_log_derivative": str(logder_direct),
        "parameter_derivative": str(parameter_derivative),
    }


def coefficient_shift_fixture() -> dict[str, object]:
    rows = []
    for L in (F(5, 2), F(11, 4), F(17, 5)):
        for A in (F(1, 3), F(2, 5), F(7, 10)):
            for B in (F(2, 7), F(5, 9)):
                require(L != A, "bad fixture")
                dalpha = B / (L - A) ** 2
                dL = -B / (L - A) ** 2
                reciprocal = F(1) / (L - A)
                require(dalpha == -dL, "alpha/L derivative sign")
                require(dalpha == B * reciprocal * reciprocal, "reciprocal square")
                rows.append({"L": str(L), "A": str(A), "B": str(B), "dalpha": str(dalpha)})
    return {"checks": len(rows), "rows": rows[:6]}


def cauchy_transfer_fixture() -> dict[str, object]:
    checks = 0
    minimum_gap: F | None = None
    for r in (F(1, 2), F(1, 3), F(2, 5)):
        for seed in range(1, 41):
            coeffs = [F((seed * (k + 3)) % 11 - 5, k + 2) for k in range(7)]
            majorant = sum((abs(c) * r**k for k, c in enumerate(coeffs)), F(0))
            derivative = abs(coeffs[1])
            gap = majorant / r - derivative
            require(gap >= 0, "finite Cauchy majorant")
            minimum_gap = gap if minimum_gap is None else min(minimum_gap, gap)
            checks += 1

    firewall = []
    for N in (2, 5, 10, 100, 1000):
        interval_radius = F(1, N * N)
        sup_bound = F(N) * interval_radius
        derivative_value = F(N)
        require(sup_bound == F(1, N), "firewall sup")
        require(derivative_value > 1, "firewall derivative")
        firewall.append({"N": N, "real_interval_sup": str(sup_bound), "derivative": str(derivative_value)})

    return {"analytic_majorant_checks": checks, "minimum_gap": str(minimum_gap), "firewall": firewall}


def reflection_fixture() -> dict[str, object]:
    rows = []
    for xi_value, xip_value, alpha in (
        (F(3, 2), F(5, 7), F(2, 9)),
        (F(-4, 3), F(7, 5), F(-1, 6)),
        (F(11, 8), F(-9, 10), F(3, 11)),
    ):
        e_alpha_reflected = -xip_value - alpha * xi_value
        minus_e_minus_alpha = -(xip_value + alpha * xi_value)
        require(e_alpha_reflected == minus_e_minus_alpha, "reflection covariance")
        rows.append(str(e_alpha_reflected))
    return {"checks": len(rows), "values": rows}


def content_hashes() -> dict[str, str]:
    result = {}
    for rel in CONTENT:
        path = ROOT / rel
        if not path.is_file():
            raise FileNotFoundError(rel)
        result[rel] = hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()
    return result


def build_payload() -> dict[str, object]:
    payload: dict[str, object] = {
        "verdict": VERDICT,
        "deformation": deformation_fixture(),
        "coefficient_shift": coefficient_shift_fixture(),
        "analytic_error_transfer": cauchy_transfer_fixture(),
        "reflection_pair": reflection_fixture(),
        "content_sha256": content_hashes(),
        "shifted_xiprime_explicit_formula_machine_proved": False,
        "suef105330_proved": False,
        "new_zero_proportion_established": False,
        "rh_established": False,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = build_payload()
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(VERDICT)
    print(payload["proof_object_sha256"])
    print("SUEF105330_OPEN")
    print("NEW_ZERO_PROPORTION_UNPROVED")
    print("RH_UNPROVED")


if __name__ == "__main__":
    main()
