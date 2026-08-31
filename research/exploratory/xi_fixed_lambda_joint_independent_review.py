"""Non-author replay: reflected log-Gamma, half-sized arcs, and unit-s jets.

No author module is imported. The same FLINT library remains a trusted
special-function implementation; this is not an independent library.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
from fractions import Fraction as Q
from pathlib import Path

from flint import acb, acb_mat, acb_series, arb, ctx, fmpq

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SCIENCE = "0e3fc9b482f0f115a49a6209ccbfeffae640014a"
DATA_PATH = "research/exploratory/xi_fixed_lambda_joint_box_compression.json"
DATA_HASH = "504071292138882ad5192fc62f765edc5615c3140542c7f597651679ba682cdb"


def need(value, reason):
    if not value:
        raise ValueError(reason)


def canonical(value):
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode()


def lfhash(raw):
    return hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest()


def fraction(pair):
    need(type(pair) is list and len(pair) == 2, "rational pair")
    n, d = pair
    need(type(n) is int and type(d) is int and d > 0, "rational types")
    result = Q(n, d)
    need([result.numerator, result.denominator] == pair, "canonical rational")
    return result


def real(q):
    q = Q(q)
    return arb(fmpq(q.numerator, q.denominator))


def endpoint(v):
    need(v.is_exact() and v.is_finite(), "exact finite endpoint")
    q = v.fmpq()
    return Q(int(q.numerator), int(q.denominator))


def pair(q):
    q = Q(q)
    return [q.numerator, q.denominator]


def rbounds(v):
    return [pair(endpoint(v.lower())), pair(endpoint(v.upper()))]


def cbounds(v):
    return {"real": rbounds(v.real), "imag": rbounds(v.imag)}


def ball(row):
    parts = []
    for axis in ("real", "imag"):
        lo, hi = map(fraction, row[axis])
        parts.append(arb(real((lo + hi) / 2), real((hi - lo) / 2)))
    return acb(*parts)


def source_fixture():
    raw = subprocess.check_output(["git", "show", f"{SCIENCE}:{DATA_PATH}"], cwd=ROOT)
    need(lfhash(raw) == DATA_HASH, "exact source fixture")
    need(lfhash((ROOT / DATA_PATH).read_bytes()) == DATA_HASH, "current source fixture")
    data = json.loads(raw)
    for path, digest in data["artifacts"].items():
        frozen = subprocess.check_output(["git", "show", f"{SCIENCE}:{path}"], cwd=ROOT)
        need(
            lfhash(frozen) == digest == lfhash((ROOT / path).read_bytes()),
            "artifact identity",
        )
    return data


def phase_lambda(anchor):
    previous = ctx.cap
    ctx.cap = 2
    try:
        t = acb_series([anchor, 1])
        zplus = acb(real(Q(1, 4))) + acb(0, 1) * t / 2
        zminus = acb(real(Q(1, 4))) - acb(0, 1) * t / 2
        phase = (zplus.lgamma() - zminus.lgamma()) / acb(0, 2) - t * arb.pi().log() / 2
        need(phase[1].imag.contains(0) and phase[1].real > 0, "phase derivative")
        return 1 / phase[1].real
    finally:
        ctx.cap = previous


def xi_unit_s_coefficients(z, cap):
    previous = ctx.cap
    ctx.cap = cap
    try:
        # Independent variable is s, not z; i**j performs the chain rule after
        # a reflected functional-equation evaluation and log-Gamma exponential.
        s0 = acb(real(Q(1, 2))) + acb(0, 1) * z
        s = 1 - acb_series([s0, 1])
        result = (
            s
            * (s - 1)
            / 2
            * ((s / 2).lgamma() - s * arb.pi().log() / 2).exp()
            * s.zeta()
        )
        values = [result[j] * acb(0, 1) ** j for j in range(cap)]
        need(all(v.is_finite() for v in values), "finite independent series")
        return values
    finally:
        ctx.cap = previous


def reflected_xi_scalar(z):
    s = 1 - (acb(real(Q(1, 2))) + acb(0, 1) * z)
    return (
        s * (s - 1) / 2 * ((s / 2).lgamma() - s * arb.pi().log() / 2).exp() * s.zeta()
    )


def fcoeff(z, lam, terms):
    v = xi_unit_s_coefficients(z, terms + 6)
    return [
        v[j + 5] * (math.factorial(j + 5) // math.factorial(j))
        - acb(0, 1) * lam * v[j + 6] * (math.factorial(j + 6) // math.factorial(j))
        for j in range(terms)
    ]


def winding_quadrants(points):
    def quadrant(p):
        x, y = p
        need(x != 0 or y != 0, "polygon vertex at zero")
        if x > 0 and y >= 0:
            return 0
        if x <= 0 and y > 0:
            return 1
        if x < 0 and y <= 0:
            return 2
        return 3

    total = 0
    for a, b in zip(points, points[1:] + points[:1]):
        change = quadrant(b) - quadrant(a)
        if change == 3:
            change = -1
        elif change == -3:
            change = 1
        elif abs(change) == 2:
            cross = a[0] * b[1] - a[1] * b[0]
            need(cross != 0, "opposite-quadrant edge through zero")
            change = 2 if cross > 0 else -2
        total += change
    need(total % 4 == 0, "closed polygon quarter-turn count")
    return total // 4


def independent_boundary(anchor, lam, original):
    # Build four oriented edges by interpolation, using 1/32 rather than1/16.
    corners = [
        (Q(anchor - 6), Q(0)),
        (Q(anchor + 6), Q(0)),
        (Q(anchor + 6), Q(1)),
        (Q(anchor - 6), Q(1)),
    ]
    path = []
    for a, b in zip(corners, corners[1:] + corners[:1]):
        steps = int((abs(b[0] - a[0]) + abs(b[1] - a[1])) * 32)
        path.extend(
            (a[0] + Q(j, steps) * (b[0] - a[0]), a[1] + Q(j, steps) * (b[1] - a[1]))
            for j in range(steps)
        )
    need(len(path) == 832 and len(set(path)) == 832, "refined complete coverage")
    vertices = []
    for x, y in path:
        value = fcoeff(acb(real(x), real(y)), lam, 1)[0]
        vertices.append((endpoint(value.real.mid()), endpoint(value.imag.mid())))
    digest = hashlib.sha256()
    for j, (p, q) in enumerate(zip(path, path[1:] + path[:1])):
        mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
        dx, dy = abs(p[0] - q[0]) / 2, abs(p[1] - q[1]) / 2
        h = dx + dy
        need(h == Q(1, 64) and (dx == 0 or dy == 0), "complete half-size arc")
        center = acb(real(mx), real(my))
        coefficients = fcoeff(center, lam, 24)
        displacement = acb(arb(0, real(dx)), arb(0, real(dy)))
        enclosure = acb(0)
        for c in reversed(coefficients):
            enclosure = enclosure * displacement + c
        outer = acb(arb(center.real, real(Q(1, 4))), arb(center.imag, real(Q(1, 4))))
        m = reflected_xi_scalar(outer).abs_upper()
        error = (
            m * (120 * 8**5 + lam * 720 * 8**6) * real(Q(1, 8) ** 24 / Q(7, 8))
        ).upper()
        enclosure += acb(arb(0, error), arb(0, error))
        need(enclosure.is_finite(), "finite independent arc")
        bounds = cbounds(enclosure)
        separation = False
        for axis_index, axis in enumerate(("real", "imag")):
            lo, hi = map(fraction, bounds[axis])
            lo = min(
                lo, vertices[j][axis_index], vertices[(j + 1) % len(path)][axis_index]
            )
            hi = max(
                hi, vertices[j][axis_index], vertices[(j + 1) % len(path)][axis_index]
            )
            bounds[axis] = [pair(lo), pair(hi)]
            separation |= lo > 0 or hi < 0
        need(separation, "independent arc/polygon homotopy excludes zero")
        need(
            enclosure.overlaps(ball(original["arcs"][j // 2]["image"])),
            "coarse/refined arc overlap",
        )
        digest.update(canonical(bounds))
    count = winding_quadrants(vertices)
    need(count == original["count"], "independent quadrant winding")
    need(winding_quadrants(list(reversed(vertices))) == -count, "orientation reversal")
    return {
        "anchor": anchor,
        "complete_arcs": len(path),
        "taylor_terms": 24,
        "half_arc_length": [1, 64],
        "count": count,
        "arc_hulls_sha256": digest.hexdigest(),
    }


def independent_compression(comp, lam):
    nodes, values = [], []
    derivative_overlaps = 0
    for row in comp["roots"]:
        x, y = map(fraction, row["center"])
        r = fraction(row["radius"])
        center = acb(real(x), real(y))
        region = acb(arb(center.real, real(r)), arb(center.imag, real(r)))
        point = [
            v * math.factorial(j)
            for j, v in enumerate(xi_unit_s_coefficients(center, 9))
        ]
        jet = [
            v * math.factorial(j)
            for j, v in enumerate(xi_unit_s_coefficients(region, 9))
        ]
        for current, recorded in (
            (point, row["point_derivatives"]),
            (jet, row["rectangle_derivatives"]),
        ):
            for a, b in zip(current, recorded):
                need(a.overlaps(ball(b)), "independent root derivative")
                derivative_overlaps += 1
        residual = (point[5] - acb(0, 1) * lam * point[6]).abs_upper()
        derivative = (point[6] - acb(0, 1) * lam * point[7]).abs_lower()
        second = (jet[7] - acb(0, 1) * lam * jet[8]).abs_upper()
        need(
            (endpoint(residual) + endpoint(second) * r * r / 2) * 2**50
            < endpoint(derivative) * r,
            "fresh independent root Rouche",
        )
        r0, c0 = jet[0] - acb(0, 1) * lam * jet[1], jet[0] + acb(0, 1) * lam * jet[1]
        nonzeros = [
            r0,
            c0,
            jet[5] + acb(0, 1) * lam * jet[6],
            jet[6],
            jet[0] * jet[6] - jet[1] * jet[5],
            jet[6] - acb(0, 1) * lam * jet[7],
        ]
        need(
            all(v.abs_lower() > 0 for v in nonzeros),
            "fresh independent noncommon guards",
        )
        value = r0 / c0
        lo, hi = map(fraction, row["raw_corridor"])
        need(
            abs(value) > real(lo) and abs(value) < real(hi),
            "fresh independent raw modulus",
        )
        nodes.append(region)
        values.append(value)
    n = len(nodes)
    g = acb_mat(
        [
            [
                1
                / (
                    nodes[i].imag
                    + nodes[j].imag
                    + acb(0, 1) * (nodes[j].real - nodes[i].real)
                )
                for j in range(n)
            ]
            for i in range(n)
        ]
    )
    h = acb_mat(
        [
            [values[i] * g[i, j] * values[j].conjugate() for j in range(n)]
            for i in range(n)
        ]
    )
    # LU solve of G X=H, not the author's matrix inverse or Gauss-Jordan routine.
    trace = g.solve(h, algorithm="lu").trace()
    ray = acb_mat([[acb(*p)] for p in comp["ray_gaussian_integer_coefficients"]])
    adj = ray.transpose().conjugate()
    quotient = ((adj * h * ray)[0, 0] / (adj * g * ray)[0, 0]).real
    tf = fraction(comp["conditional_reduced_global_trace_strict_lower"])
    nf = fraction(comp["conditional_reduced_global_norm_strict_lower"])
    need(trace.imag.contains(0) and trace.real > real(tf), "independent LU trace floor")
    need(quotient > real(nf * nf), "independent Rayleigh floor")
    need(trace.overlaps(ball(comp["raw_trace"])), "independent trace overlap")
    return {
        "label": comp["label"],
        "root_count": n,
        "derivative_overlaps": derivative_overlaps,
        "fresh_simple_noncommon_roots": n,
        "raw_trace": cbounds(trace),
        "rayleigh_squared": rbounds(quotient),
        "strict_trace_floor": pair(tf),
        "strict_norm_floor": pair(nf),
    }


def run(bits):
    need(type(bits) is int and bits in (320, 448), "independent precision panel")
    fixture = source_fixture()
    previous = ctx.prec, ctx.cap
    ctx.prec = bits
    try:
        need(fixture["parameter_anchor"] == 64, "ONE source parameter")
        lam = phase_lambda(64)
        lo, hi = map(fraction, fixture["lambda_enclosure"])
        need(
            lam.overlaps(arb(real((lo + hi) / 2), real((hi - lo) / 2))),
            "lambda overlap",
        )
        boxes, compressions = [], []
        for box in fixture["boxes"]:
            need(box["parameter_anchor"] == 64, "fixed boundary lambda")
            boxes.append(independent_boundary(box["box_center"], lam, box))
        need([b["count"] for b in boxes] == [3, 5, 6], "complete fixed-source counts")
        groups = {
            "box32": list(range(3)),
            "box64": list(range(3, 8)),
            "box128": list(range(8, 14)),
            "prefix32_64": list(range(8)),
            "joint": list(range(14)),
        }
        need(len(fixture["roots"]) == 14, "complete fourteen nodes")
        for row in fixture["roots"]:
            need(row["parameter_anchor"] == 64, "fixed root lambda")
        for comp in fixture["compressions"]:
            need(
                comp["root_indices"] == groups[comp["label"]],
                "exact nested source spaces",
            )
            expanded = dict(comp)
            expanded["roots"] = [fixture["roots"][i] for i in comp["root_indices"]]
            compressions.append(independent_compression(expanded, lam))
        need(
            [c["root_count"] for c in compressions] == [3, 5, 6, 8, 14],
            "matrix coverage",
        )
        traces = {c["label"]: ball(c["raw_trace"]) for c in compressions}
        increments = []
        for row in fixture["orthogonal_input_increments"]:
            value = traces[row["to"]] - traces[row["from"]]
            floor = fraction(row["conditional_reduced_increment_trace_strict_lower"])
            need(
                value.imag.contains(0) and value.real > real(floor),
                "independent increment floor",
            )
            need(value.overlaps(ball(row["raw_increment_trace"])), "increment overlap")
            increments.append(
                {
                    "from": row["from"],
                    "to": row["to"],
                    "raw_increment": cbounds(value),
                    "strict_floor": pair(floor),
                }
            )
        coupling = traces["joint"] - sum(
            (traces[k] for k in ("box32", "box64", "box128")), acb(0)
        )
        need(
            coupling.imag.contains(0) and coupling.real > real(Q(1, 100)),
            "nonadditive joint trace",
        )
        need(
            coupling.overlaps(ball(fixture["joint_minus_sum_individual_raw_traces"])),
            "coupling overlap",
        )
        report = {
            "schema": "xi-fixed-lambda-joint-independent-review-v1",
            "science_commit": SCIENCE,
            "science_fixture_sha256_lf": DATA_HASH,
            "precision_bits": bits,
            "author_code_imported": False,
            "independent_special_function_library": False,
            "different_variable_reflected_loggamma_evaluation": True,
            "parameter_anchor": 64,
            "lambda_enclosure": rbounds(lam),
            "complete_boundary_replay": boxes,
            "root_and_metric_replay": compressions,
            "independent_orthogonal_input_increments": increments,
            "independent_joint_minus_sum": cbounds(coupling),
            "review_script_sha256_lf": lfhash(Path(__file__).read_bytes()),
        }
        report["payload_sha256"] = hashlib.sha256(canonical(report)).hexdigest()
        return report
    finally:
        ctx.prec, ctx.cap = previous


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bits", type=int, choices=(320, 448), default=320)
    print(json.dumps(run(parser.parse_args().bits), sort_keys=True, indent=2))
