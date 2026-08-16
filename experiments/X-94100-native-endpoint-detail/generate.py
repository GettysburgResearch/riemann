#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from decimal import localcontext
from pathlib import Path

import verify as V

HERE = Path(__file__).resolve().parent
CONTROL = HERE / "certificates" / "control.json"


def generate(X: int) -> dict:
    residual = {q: V.omega(X, q) for q in range(2, X + 1)}
    stages: list[dict] = []
    lambdas = {}

    for T in range(X, 2, -1):
        values = {q: V.detail(T, q) for q in range(2, T)}
        lam, q_min = min((residual[q] / value, q) for q, value in values.items())
        lambdas[T] = lam
        stages.append({"T": T, "lambda": str(lam), "minimizer": q_min})
        for q, value in values.items():
            residual[q] -= lam * value
            if abs(residual[q]) < V.D("1e-55"):
                residual[q] = V.D(0)
            if residual[q] < 0:
                raise V.ContractError(("negative residual", X, T, q, residual[q]))

    row = {
        n: sum((lambdas[T] * V.endpoint_row(T, n) for T in range(max(3, n + 1), X + 1)), V.D(0))
        for n in range(2, X)
    }
    ordinary = {
        q: sum((lambdas[T] * V.gamma(T, q) for T in range(max(3, q + 1), X + 1)), V.D(0))
        for q in range(2, X + 1)
    }
    detail = {
        q: ordinary[q] - V.D(2) * ordinary.get(4 * q, V.D(0))
        for q in range(2, X + 1)
    }
    direct_detail = {
        q: sum((lambdas[T] * V.detail(T, q) for T in range(max(3, q + 1), X + 1)), V.D(0))
        for q in range(2, X + 1)
    }
    if any(abs(detail[q] - direct_detail[q]) > V.D("1e-50") for q in detail):
        raise V.ContractError("q/4q common-row assembly failed")
    if any(value < 0 for value in row.values()):
        raise V.ContractError("negative generated row")
    if any(detail[q] > V.omega(X, q) + V.D("1e-50") for q in detail):
        raise V.ContractError("detail overdraw")
    if any(ordinary[q] > V.w_native(X, q) + V.D("1e-50") for q in ordinary):
        raise V.ContractError("ordinary overdraw")

    score = sum((V.y4(q) * detail[q] for q in detail), V.D(0))
    benchmark = sum((V.y4(q) * V.omega(X, q) for q in detail), V.D(0))
    deficit = benchmark - score
    slack = {q: V.omega(X, q) - detail[q] for q in detail}
    dual_deficit = sum((V.y4(q) * slack[q] for q in slack), V.D(0))
    if abs(deficit - dual_deficit) > V.D("1e-50"):
        raise V.ContractError("native dual mismatch")

    payload = {
        "schema": "riemann.t94100.native-endpoint-detail-certificate.v1",
        "endpoint": X,
        "precision_digits": 70,
        "source_dictionary": "positive parabolic endpoint atoms a_T=d_T-d_(T-1)",
        "target": "native radix-four detail vector Omega_X",
        "coefficient_contract": "one lambda_T in source owner, row, q, 4q, detail, score, Y4 and endpoint deficit",
        "owners": [str(T) for T in range(3, X + 1)],
        "stages": stages,
        "row": {str(k): str(v) for k, v in row.items()},
        "ordinary": {str(k): str(v) for k, v in ordinary.items()},
        "detail": {str(k): str(v) for k, v in detail.items()},
        "native_target": {str(q): str(V.omega(X, q)) for q in range(2, X + 1)},
        "slack": {str(k): str(v) for k, v in slack.items()},
        "y4": {str(q): str(V.y4(q)) for q in range(2, X + 1)},
        "score": str(score),
        "native_benchmark": str(benchmark),
        "native_deficit": str(deficit),
        "largest_slack_column": max((q for q, value in slack.items() if value > V.D("1e-45")), default=1),
        "rh_established": False,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--endpoint", type=int, default=256)
    parser.add_argument("--output", type=Path, default=HERE / "results" / "certificate-X256.json")
    args = parser.parse_args()
    control = json.loads(CONTROL.read_text())
    with localcontext() as ctx:
        ctx.prec = int(control["precision"])
        payload = generate(args.endpoint)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print("PASS_GENERATED_NATIVE_ENDPOINT_DETAIL_CERTIFICATE")
    print(payload["proof_object_sha256"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
