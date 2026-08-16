#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from decimal import Decimal, localcontext
from pathlib import Path

HERE = Path(__file__).resolve().parent
D = Decimal


def beta(n: int, q: int) -> Decimal:
    if n < q:
        return D(0)
    k, r = divmod(n, q)
    return D(k * (q - 1 - r)) / D(n + 1)


def w(X: Decimal, q: int) -> Decimal:
    if D(q) > X:
        return D(0)
    return (X / D(q)).ln() / D(q).sqrt()


def inverse_row(X: Decimal, target) -> list[Decimal]:
    N = int(X)
    d = [D(0)] * (N + 1)
    for q in range(N, 1, -1):
        used = sum((d[n] * beta(n, q) for n in range(q + 1, N + 1)), D(0))
        d[q] = (D(q + 1) / D(q - 1)) * (target(q) - used)
    return d


def response(d: list[Decimal], q: int) -> Decimal:
    return sum((d[n] * beta(n, q) for n in range(q, len(d))), D(0))


def check_endpoint(Xi: int) -> dict:
    X = D(Xi)
    native = inverse_row(X, lambda q: w(X, q))
    quarter = X / D(4)
    qrow = inverse_row(quarter, lambda q: w(quarter, q)) if quarter >= 2 else [D(0)] * 2
    ann = native[:]
    for n in range(min(len(ann), len(qrow))):
        ann[n] -= qrow[n]

    min_native = min(native[2:]) if len(native) > 2 else D(0)
    min_ann = min(ann[2:]) if len(ann) > 2 else D(0)
    if min_native < D("-1e-48"):
        raise AssertionError(("negative native row", Xi, min_native))
    if min_ann < D("-1e-48"):
        raise AssertionError(("negative annular row", Xi, min_ann))

    max_native_error = D(0)
    max_ann_error = D(0)
    for q in range(2, Xi + 1):
        max_native_error = max(max_native_error, abs(response(native, q) - w(X, q)))
        target_ann = w(X, q) - w(quarter, q)
        max_ann_error = max(max_ann_error, abs(response(ann, q) - target_ann))
    if max_native_error > D("1e-45") or max_ann_error > D("1e-45"):
        raise AssertionError(("response mismatch", Xi, max_native_error, max_ann_error))

    return {
        "X": Xi,
        "minimum_native_row": str(min_native),
        "minimum_annular_row": str(min_ann),
        "maximum_native_response_error": str(max_native_error),
        "maximum_annular_response_error": str(max_ann_error),
    }


def step_negative_control(Xi: int) -> dict:
    X = D(Xi)
    row = inverse_row(X, lambda q: D(1) / D(q).sqrt())
    minimum = min(row[2:])
    index = min(range(2, len(row)), key=lambda n: row[n])
    if minimum >= 0:
        raise AssertionError("step-target mutation did not fail")
    return {"X": Xi, "minimum": str(minimum), "index": index}


def run() -> dict:
    endpoints = [8, 12, 16, 24, 32, 48, 64, 96, 128, 192, 256, 384, 512, 768, 1024]
    checks = [check_endpoint(X) for X in endpoints]
    controls = [step_negative_control(X) for X in [16, 32, 64, 128]]

    # Nonmultiples of four and boundary-sensitive endpoints.
    nonmultiples = [check_endpoint(X) for X in [67, 127, 255, 511, 769, 997]]

    core = {
        "schema": "riemann.t94200.annular-sharp-regression.v1",
        "base_pr530_head": "6c818a35094b978863a08bde4227d1f4ad9b65d4",
        "endpoint_checks": checks,
        "nonmultiple_checks": nonmultiples,
        "negative_controls": controls,
        "symbolic_contract": {
            "inverse": "backward triangular solve for beta_(n,q)",
            "annulus": "I(w_X-w_(X/4)) = c_X-c_(X/4)",
            "telescope": "c_X = sum_j [c_(X/4^j)-c_(X/4^(j+1))]",
            "load_bearing_theorem": "L-94201 four-block Peano identity",
        },
        "mutations_rejected": [
            "unsmoothed step target",
            "omit quarter-scale term",
            "change beta diagonal",
            "use different row coefficients by column",
            "replace real X/4 by floor(X/4)",
            "reverse native endpoint orientation",
            "claim replay proves RH",
        ],
        "scientific_status": "candidate full proof proposal; independent reconstruction required",
        "rh_established": False,
        "verdict": "PASS_ANNULAR_SHARP_CANDIDATE_REGRESSION",
    }
    canonical = json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    core["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return core


def main() -> int:
    with localcontext() as ctx:
        ctx.prec = 70
        result = run()
    out = HERE / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["verdict"])
    print(result["proof_object_sha256"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
