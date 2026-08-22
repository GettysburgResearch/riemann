#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


def digest(payload):
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


SQRT2 = math.sqrt(2.0)
QCOEFF = [
    1.0,
    -2.0 * (1.0 + SQRT2),
    3.0 + 4.0 * SQRT2,
    -4.0 - 2.0 * SQRT2,
    2.0,
]


def phi0(y):
    if y < 1.0:
        return 0.0
    return 8.0 * math.sqrt(y) - 8.0 - 4.0 * math.log(y)


def dphi0(y):
    if y < 1.0:
        return 0.0
    return 4.0 * math.sqrt(y) - 4.0


def phistar(y):
    return sum(QCOEFF[j] * phi0(y / (2.0**j)) for j in range(5))


def cv(y):
    return sum(QCOEFF[j] * dphi0(y / (2.0**j)) for j in range(5))


def xd(y):
    return 0.5 * (cv(y) + 1.5 * phistar(y))


def mphi(s):
    q = 1.0 - SQRT2 * 2.0 ** (-s)
    r = 1.0 - 2.0 ** (-s)
    return 2.0 * q * q * r * r / (s * s * (s - 0.5))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    multiplier_checks = 0
    for s in [0.13 + 0.17j, 0.27 + 0.41j, 0.39 + 1.2j, 0.61 + 0.3j]:
        mp = mphi(s)
        mcv = s * mp
        mxd = 0.5 * (s + 1.5) * mp
        assert abs((-2.0 / 3.0) * mcv + (4.0 / 3.0) * mxd - mp) < 1e-11
        multiplier_checks += 1

    kernel_checks = 0
    for k in range(1, 4000):
        y = 0.5 * math.exp(k * math.log(64.0 / 0.5) / 4000.0)
        h = phistar(y)
        c = cv(y)
        x = xd(y)
        assert abs((-2.0 / 3.0) * c + (4.0 / 3.0) * x - h) < 1e-10
        if y < 1.0 or y > 16.0:
            assert abs(h) < 1e-9
            assert abs(c) < 1e-9
        kernel_checks += 1

    zero_safety_checks = 0
    for a in [0.05, 0.13, 0.25, 0.37, 0.49]:
        for b in [0.0, 0.3, 1.7, 4.2]:
            s = a + 1j * b
            q = 1 - SQRT2 * 2 ** (-s)
            r = 1 - 2 ** (-s)
            assert abs(q) > 1e-6
            assert abs(r) > 1e-6
            zero_safety_checks += 1

    labels = [(2, -(2 ** -0.5)), (67, -(67 ** -0.5)), (67, -(67 ** -0.5))]
    us = [-0.2 + i * (9.0 / 30000.0) for i in range(30001)]
    du = us[1] - us[0]
    fvals, cvals, xvals = [], [], []
    for u in us:
        fv = phistar(math.exp(u))
        cvv = cv(math.exp(u))
        xvv = xd(math.exp(u))
        for p, a in labels:
            y = math.exp(u) / p
            fv += a * phistar(y)
            cvv += a * cv(y)
            xvv += a * xd(y)
        fvals.append(fv)
        cvals.append(cvv)
        xvals.append(xvv)

    def integ(vals):
        return du * (0.5 * vals[0] + sum(vals[1:-1]) + 0.5 * vals[-1])

    A = integ([v * v for v in cvals])
    H = integ([v * v for v in fvals])
    B = integ([v * v for v in xvals])
    cross = integ([cvals[i] * xvals[i] for i in range(len(us))])
    assert abs(cross - 0.5 * A) < 2e-5
    assert abs(B - (0.25 * A + 9.0 * H / 16.0)) < 2e-5
    det = A * B - cross * cross
    assert abs(det - 9.0 * A * H / 16.0) < 5e-5

    kappa = 0.25 + 225.0 * math.log(2.0) ** 2 / (16.0 * math.pi**2)
    assert kappa < 0.935

    lam = math.log(10**6)
    residuals = []
    for y in [1.1, 2.0, 4.0, 8.0]:
        h = 1e-5
        f0 = phistar(y)
        fp = phistar(y * math.exp(h))
        fm = phistar(y * math.exp(-h))
        second = (fp - 2 * f0 + fm) / (h * h)
        residuals.append(second - lam * lam * f0)
    assert min(residuals) < 0 and max(residuals) > 0

    payload = {
        "schema": "riemann.t102500.common-mother-stress-tensor.v1",
        "multiplier_checks": multiplier_checks,
        "kernel_checks": kernel_checks,
        "zero_safety_checks": zero_safety_checks,
        "channel_gram_error": abs(det - 9.0 * A * H / 16.0),
        "one_octave_kappa": kappa,
        "naive_euclidean_residual_has_both_signs": True,
        "ar_scale102500_proved": False,
        "ar_occ102500_proved": False,
        "rh_established": False,
        "verdict": "PASS_T102500_COMMON_MOTHER_STRESS_TENSOR",
    }
    payload["proof_object_sha256"] = digest(payload)
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    else:
        print(text, end="")
    print(payload["verdict"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
