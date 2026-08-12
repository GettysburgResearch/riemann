#!/usr/bin/env python3
"""Finite replay for annular Clark entropy and quantitative Green moats."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import mpmath as mp

mp.mp.dps = 70


def bmod2(eta: mp.mpf, x: mp.mpf, y: mp.mpf) -> mp.mpf:
    return ((eta - x) ** 2 + y**2) / ((eta + x) ** 2 + y**2)


def charge(eta: mp.mpf, x: mp.mpf, y: mp.mpf) -> mp.mpf:
    return -mp.log(bmod2(eta, x, y))


def entropy_integral(q: mp.mpf) -> mp.mpf:
    return mp.quad(lambda t: q / (1 + t * q), [0, 1])


def green_laplace(eta: mp.mpf, x: mp.mpf, y: mp.mpf) -> mp.mpf:
    f = lambda t: 4 * mp.e ** (-eta * t) * mp.sinh(x * t) * mp.cos(y * t) / t
    return mp.quad(f, [0, 1, mp.inf])


def build():
    eta = mp.mpf("1")
    zeros = [
        (mp.mpf("0.08"), mp.mpf("0.37"), 1),
        (mp.mpf("0.14"), mp.mpf("0.82"), 2),
        (mp.mpf("0.23"), mp.mpf("1.31"), 1),
    ]

    product_mod2 = mp.mpf("1")
    sum_charge = mp.mpf("0")
    min_moat_slack = mp.inf
    laplace_error = mp.mpf("0")
    zero_records = []
    for x, y, mult in zeros:
        xmod = bmod2(eta, x, y)
        g = charge(eta, x, y)
        moat = 4 * eta * x / ((eta + x) ** 2 + y**2)
        min_moat_slack = min(min_moat_slack, g - moat)
        gl = green_laplace(eta, x, y)
        laplace_error = max(laplace_error, abs(g - gl))
        product_mod2 *= xmod**mult
        sum_charge += mult * g
        zero_records.append({
            "x": float(x),
            "y": float(y),
            "multiplicity": mult,
            "charge": float(g),
            "moat": float(moat),
            "moat_slack": float(g - moat),
        })

    log_product = -mp.log(product_mod2)
    H = (1 / product_mod2 - 1) / (2 * eta)
    entropy = entropy_integral(2 * eta * H)

    annuli = [
        [(mp.mpf("0.05"), mp.mpf("0.2"), 1)],
        [(mp.mpf("0.10"), mp.mpf("0.6"), 1), (mp.mpf("0.12"), mp.mpf("1.0"), 1)],
        [(mp.mpf("0.18"), mp.mpf("1.4"), 2)],
    ]
    B2 = mp.mpf("1")
    Lambda = mp.mpf("0")
    Hprev = mp.mpf("0")
    max_additive_error = mp.mpf("0")
    max_weighted_error = mp.mpf("0")
    annular_records = []
    for packet in annuli:
        C2 = mp.mpf("1")
        La = mp.mpf("0")
        for x, y, mult in packet:
            z = bmod2(eta, x, y)
            C2 *= z**mult
            La += mult * charge(eta, x, y)
        H_ann = (1 / C2 - 1) / (2 * eta)
        Hnew = Hprev + (1 / B2) * H_ann
        B2 *= C2
        Lambda_new = Lambda + La
        direct_H = (1 / B2 - 1) / (2 * eta)
        direct_L = -mp.log(B2)
        max_weighted_error = max(max_weighted_error, abs(Hnew - direct_H))
        max_additive_error = max(max_additive_error, abs(Lambda_new - direct_L))
        Hprev, Lambda = Hnew, Lambda_new
        annular_records.append({"log_increment": float(La), "hyperbolic_increment": float(H_ann)})

    x0 = mp.mpf("0.1")
    Y = mp.mpf("2")
    strip_moat = 4 * eta * x0 / ((eta + mp.mpf("0.5")) ** 2 + Y**2)

    gates = {
        "product_log_additivity": abs(log_product - sum_charge) < mp.mpf("1e-60"),
        "entropy_resolvent": abs(log_product - entropy) < mp.mpf("1e-60"),
        "green_laplace": laplace_error < mp.mpf("1e-55"),
        "moat": min_moat_slack > 0,
        "dyadic_additive": max_additive_error < mp.mpf("1e-60"),
        "dyadic_weighted": max_weighted_error < mp.mpf("1e-60"),
        "positive_strip_moat": strip_moat > 0,
    }
    gates = {k: bool(v) for k, v in gates.items()}
    assert all(gates.values())

    return {
        "status": "PASS_ANNULAR_CLARK_ENTROPY",
        "gates": gates,
        "eta": float(eta),
        "zero_records": zero_records,
        "total_log_mass": float(log_product),
        "total_hyperbolic_mass": float(H),
        "entropy_resolvent_error": float(abs(log_product - entropy)),
        "green_laplace_error": float(laplace_error),
        "minimum_moat_slack": float(min_moat_slack),
        "dyadic_additive_error": float(max_additive_error),
        "dyadic_weighted_error": float(max_weighted_error),
        "annular_records": annular_records,
        "depth_strip_moat_x0_0p1_Y_2": float(strip_moat),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    payload = json.dumps(build(), sort_keys=True, separators=(",", ":")) + "\n"
    if args.json:
        args.json.write_text(payload)
    else:
        print(payload, end="")


if __name__ == "__main__":
    main()
