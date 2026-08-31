"""Source-bound low-pass lower bounds from actual-Xi Laplace calibration."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from fractions import Fraction as Q
from pathlib import Path

import xi_companion_box_count_compression as bc
from flint import acb, acb_series, arb, ctx

oa = bc.oa
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
STEM = "xi_laplace_low_pass_lower_bound"
BASE = "7fbcd592042a5cc98c17d0db2fac62f8171267f2"
PREREG = "2df9e543c07eba1f17d18043afc7dda110304b03"
NOTE = HERE / "XI_LAPLACE_LOW_PASS_LOWER_BOUND.md"
FIXTURE = HERE / (STEM + ".json")
MANIFEST = HERE / (STEM + ".sources.json")
TEST = ROOT / "tests" / ("test_" + STEM + ".py")
WIDTHS = tuple(Q(1, 2**j) for j in (2, 4, 6, 8))
HEIGHTS = tuple(2**j for j in range(6, 17))
BINDINGS = (
    (
        "BCproof",
        BASE,
        "research/exploratory/XI_COMPANION_BOX_COUNT_COMPRESSION.md",
        "2860d9c9bb90f4423f17f0d272229e78a30ae62b",
        "22d11bf3dccb72fa25633deeee063164611dbaa977c5e66fca84f4350ae79c65",
    ),
    (
        "BCproducer",
        BASE,
        "research/exploratory/xi_companion_box_count_compression.py",
        "698211f63f2268f421faa1ed76d4dd8749a4b311",
        "cea67ec0b5335ecef7a6df8d453859a249b73d1b716b8c87565709d27ec95e58",
    ),
    (
        "BCfixture",
        BASE,
        "research/exploratory/xi_companion_box_count_compression.json",
        "346a452e1c3136f19139debe1620577ef41e6b43",
        "9148321153c7319518dc9475adee61f2ba5b646663f1cb35b762f31f280834e4",
    ),
    (
        "BCmanifest",
        BASE,
        "research/exploratory/xi_companion_box_count_compression.sources.json",
        "fcbfb819e09f97f9f4e9af60141ffe198238bf1c",
        "b916af0286ddd686e700b56032a2f10f9b0bc08212bed6ca60bb99270b85299f",
    ),
    (
        "BCtests",
        BASE,
        "tests/test_xi_companion_box_count_compression.py",
        "ea093cc50fb8b9de415ce4e71bc370ffe456d8ed",
        "e9b40aaa100f1f8ae74ad2d90978b8e7621303ac750a847cbfc8ec045a2e05b5",
    ),
    (
        "positive_full_theta_kernel",
        "3b6972320899a82c6caa3a98e2ada5ff703a605a",
        "research/exploratory/XI_ACTUAL_KERNEL_LAPLACE_CONCENTRATION.md",
        "fa24f9c8e0a87709d1a297a4e72136c1135d066c",
        "f7f89abe2e54d0d8df72dc830162b2083bc4f05d402c3aa70eca464678e80246",
    ),
)
CONTRACT = {
    "primitive": "actual Xi, fixed lambda per anchor, fourteen surviving BC nodes rebuilt locally",
    "arithmetic_class": "MIXED",
    "arithmetic_components": [
        "DIRECTED_BALL_ENCLOSURES",
        "EXACT_RATIONAL",
        "CERTIFIED_INTEGER_COVERAGE",
    ],
    "rounding": "pinned FLINT outward balls; tails below 2^-512 widened to an outward ball enclosing [0,2^-512]; exact dyadic endpoints and rational final floors; no float acceptance",
    "output": "Fourier low-pass [0,D], boundary-dx Hardy norm, physical P_U not multiplication alone",
    "inner_premise": "Theta0 and Theta5 inner, separately for each fixed lambda32/64/128",
    "common_factor": "two scalar modulus comparisons at b and ih; no band Loewner implication",
    "finite_coverage": "all14nodes x4widths x11calibrationheights; no omitted failed grid values",
    "primitive_replay": "local root certificates and raw values rerun; BC complete boundary census not needed or rerun here",
    "analytic_quantifiers": "all-D positivity and conditional cofinal criterion are written proofs, not finite-grid certificates",
    "exclusions": "no actual Xi Bessel/alignment divergence proof, outer metric, cofinal capture, RH, or parameter selection",
}


def digest(raw):
    return hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest()


def manifest():
    return {
        "schema": STEM + "-sources-v1",
        "authoring_base": BASE,
        "preregistration": PREREG,
        "contract": CONTRACT,
        "runtime": oa.RUNTIME,
        "sources": [
            dict(zip(("role", "commit", "path", "git_blob", "sha256_lf"), r))
            for r in BINDINGS
        ],
    }


def authenticate():
    oa.require(
        bc.canonical(bc.load_json(MANIFEST.read_bytes())) == bc.canonical(manifest()),
        "manifest source/scope identity",
    )
    bc.authenticate()
    for role, commit, path, blob, sha in BINDINGS:
        raw = subprocess.check_output(["git", "show", f"{commit}:{path}"], cwd=ROOT)
        actual = hashlib.sha1(
            b"blob " + str(len(raw)).encode() + b"\0" + raw
        ).hexdigest()
        oa.require(actual == blob and digest(raw) == sha, "direct source identity")
        if role.startswith("BC"):
            oa.require(
                digest((ROOT / path).read_bytes()) == sha, "executed local BC identity"
            )


def axis_value(height, lam, direct=False):
    oa.integer(height, 64, 65536)
    oa.require(
        height in HEIGHTS and type(lam) is arb and lam > 0, "axis calibration domain"
    )
    oa.require(type(direct) is bool and 192 <= ctx.prec <= 512, "axis route/precision")
    previous = ctx.cap
    ctx.cap = 2
    try:
        s = oa.qarb(Q(1, 2) + height)
        series = acb_series([acb(s), 1])
        zeta = series.zeta()
        oa.require(zeta[0].real > 0 and zeta[0].imag.contains(0), "positive zeta axis")
        ell = (
            1 / s
            + 1 / (s - 1)
            - arb.pi().log() / 2
            + acb(s / 2).digamma().real / 2
            + (zeta[1] / zeta[0]).real
        )
        oa.require(
            ell > 0 and 1 + lam * ell > 0, "positive large-axis logarithmic derivative"
        )
        value = (1 - lam * ell) / (1 + lam * ell)
        if direct:
            full = (
                series
                * (series - 1)
                / 2
                * (-series * arb.pi().log() / 2).exp()
                * (series / 2).gamma()
                * zeta
            )
            ratio = (full[0] - lam * full[1]) / (full[0] + lam * full[1])
            oa.require(
                ratio.is_finite()
                and ratio.imag.contains(0)
                and ratio.real.overlaps(value),
                "direct reflected Xi calibration",
            )
        return value, ell
    finally:
        ctx.cap = previous


def lower_bound(node, raw_value, height, width, axis_modulus):
    oa.require(
        type(node) is acb and node.is_finite() and node.imag > 0,
        "upper half-plane node",
    )
    oa.require(type(raw_value) is acb and raw_value.is_finite(), "raw numerator value")
    oa.integer(height, 1, 65536)
    width = oa.rational(width)
    oa.require(
        0 < width <= 1 and type(axis_modulus) is arb and axis_modulus >= 0,
        "positive width/axis modulus",
    )
    h = arb(height)
    w = oa.qarb(width)
    laplace = (
        2
        * (h * node.imag).sqrt()
        * axis_modulus
        / ((h + node.imag) ** 2 + node.real**2).sqrt()
    )
    tail = (-h * w).exp()
    # Widen before calculation rather than materializing huge rational
    # denominators for an irrelevant extremely small exponential.
    if tail < oa.qarb(Q(1, 2**512)):
        tail = arb(oa.qarb(Q(1, 2**513)), oa.qarb(Q(1, 2**513)))
    bracket = laplace - tail
    denominator = (1 - (-2 * h * w).exp()).sqrt()
    oa.require(denominator > 0 and laplace.is_finite(), "finite calibration bound")
    if bracket > 0:
        value = abs(raw_value) * bracket / denominator
        floor = oa.endpoint(value.lower())
        oa.require(floor >= 0, "nonnegative node floor")
    else:
        floor = Q(0)
    return {
        "h": height,
        "D": oa.pair(width),
        "laplace_term": oa.rbounds(laplace),
        "tail": oa.rbounds(tail),
        "bracket": oa.rbounds(bracket),
        "norm_lower": oa.pair(floor),
    }


def gram_bound(nodes):
    oa.require(
        type(nodes) is list and 1 <= len(nodes) <= 6, "finite normalized Gram size"
    )
    rows = []
    for i, a in enumerate(nodes):
        total = arb(1)
        for j, b in enumerate(nodes):
            if i != j:
                total += (
                    2
                    * (a.imag * b.imag).sqrt()
                    / ((a.imag + b.imag) ** 2 + (b.real - a.real) ** 2).sqrt()
                )
        rows.append(oa.endpoint(total.upper()))
    return max(rows), rows


def strict_decimal_floor(value, digits):
    value = oa.rational(value)
    oa.integer(digits, 1, 12)
    oa.require(value >= 0, "nonnegative floor input")
    scaled = value * 10**digits
    n = scaled.numerator // scaled.denominator
    if n and Q(n) == scaled:
        n -= 1
    floor = Q(n, 10**digits)
    oa.require(floor == 0 or 0 < floor < value, "strict reported rational floor")
    return floor


def build_report():
    authenticate()
    operators = []
    with oa.precision():
        for anchor in (32, 64, 128):
            lam = oa.frozen_lambda(anchor)
            records = [bc.root_record(r) for r in bc.DISKS if r[0] == anchor]
            rows, nodes, values = map(list, zip(*records))
            calibrations = []
            for h in HEIGHTS:
                theta, ell = axis_value(h, lam, direct=h in (64, 256, 1024))
                calibrations.append(
                    {
                        "h": h,
                        "theta_axis": oa.rbounds(theta),
                        "log_derivative": oa.rbounds(ell),
                    }
                )
            axis = [abs(axis_value(h, lam)[0]) for h in HEIGHTS]
            c, row_bounds = gram_bound(nodes)
            bands = []
            for width in WIDTHS:
                grid = []
                best = []
                for node, value in zip(nodes, values):
                    entries = [
                        lower_bound(node, value, h, width, v)
                        for h, v in zip(HEIGHTS, axis)
                    ]
                    grid.append(entries)
                    best.append(max(oa.unpair(r["norm_lower"]) for r in entries))
                trace = sum(x * x for x in best) / c
                norm = max(best)
                bands.append(
                    {
                        "D": oa.pair(width),
                        "all_node_height_bounds": grid,
                        "best_node_norm_lower": [oa.pair(x) for x in best],
                        "strict_global_input_band_norm_floor": oa.pair(
                            strict_decimal_floor(norm, 6)
                        ),
                        "strict_global_input_band_squared_HS_floor": oa.pair(
                            strict_decimal_floor(trace, 10)
                        ),
                        "all_nodes_positive": all(x > 0 for x in best),
                    }
                )
            operators.append(
                {
                    "anchor": anchor,
                    "lambda": oa.rbounds(lam),
                    "roots": rows,
                    "calibrations": calibrations,
                    "normalized_gram_row_bounds": [oa.pair(v) for v in row_bounds],
                    "normalized_gram_upper": oa.pair(c),
                    "bands": bands,
                }
            )
    return bc.seal(
        {
            "schema": STEM + "-v1",
            "contract": CONTRACT,
            "runtime": oa.RUNTIME,
            "preregistration": PREREG,
            "sources": manifest()["sources"],
            "coverage": {
                "operators": 3,
                "nodes": 14,
                "widths": 4,
                "calibration_heights": 11,
                "node_grid_cells": 616,
                "axis_values": 33,
            },
            "operators": operators,
            "artifacts": {
                p.relative_to(ROOT).as_posix(): digest(p.read_bytes())
                for p in (NOTE, Path(__file__), TEST, MANIFEST)
            },
        }
    )


def check_report(report):
    bc.validate_tree(report)
    oa.require(type(report) is dict and "payload_sha256" in report, "report shape")
    unsigned = {k: v for k, v in report.items() if k != "payload_sha256"}
    oa.require(
        report["payload_sha256"] == oa.digest(bc.canonical(unsigned)), "report seal"
    )
    oa.require(
        bc.canonical(report) == bc.canonical(build_report()),
        "fresh actual-Xi low-pass reconstruction",
    )
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--emit", action="store_true")
    modes.add_argument("--emit-sources", action="store_true")
    modes.add_argument("--check", action="store_true")
    modes.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    if args.emit_sources:
        result = manifest()
    elif args.check:
        check_report(bc.load_json(FIXTURE.read_bytes()))
        print(
            "PASS: complete actual-Xi low-pass grid; operator interpretation conditional; cofinal/RH OPEN"
        )
        return
    else:
        result = build_report()
        if args.summary:
            result = [
                {
                    "anchor": op["anchor"],
                    "D": str(oa.unpair(b["D"])),
                    "norm_floor": str(
                        oa.unpair(b["strict_global_input_band_norm_floor"])
                    ),
                    "squared_HS_floor": str(
                        oa.unpair(b["strict_global_input_band_squared_HS_floor"])
                    ),
                    "all_nodes_positive": b["all_nodes_positive"],
                }
                for op in result["operators"]
                for b in op["bands"]
            ]
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
