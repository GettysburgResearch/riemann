"""Independent held-out replay; no author module is imported or executed."""

from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import math
import platform
import subprocess
import sys
from fractions import Fraction as Q
from pathlib import Path

import flint
from flint import acb, arb, ctx

ROOT = Path(__file__).resolve().parents[2]
SCIENCE = "64165b8c805d182dbc43f2e5855e64a86cf1aaf9"
DATA_PATH = "research/exploratory/xi_fixed_lambda_heldout_alignment.json"
DATA_HASH = "eb6464cc2eed61f8aecf2eff6e2f36a5ee5f850252237f0f95bd9b0e4e51b206"
HELPER_COMMIT = "26201b3a7de6293ea47621f06b45dd9837521a20"
HELPER_PATH = "research/exploratory/xi_fixed_lambda_joint_independent_review.py"
HELPER_BLOB = "35f8baf0486625490f3fb9afe998956f75fe5280"
PANELS = ((256, 384, 32, 36), (512, 384, 32, 36), (1024, 1152, 128, 52))


def need(value, reason):
    if not value:
        raise ValueError(reason)


def git(commit, path):
    return subprocess.check_output(["git", "show", f"{commit}:{path}"], cwd=ROOT)


def digest(raw):
    return hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest()


def blob(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


# These are independently authored helpers, not an executable science dependency.
helper_raw = git(HELPER_COMMIT, HELPER_PATH)
need(blob(helper_raw) == HELPER_BLOB, "frozen reviewer helper")
helper = {"__name__": "frozen_independent_reviewer", "__file__": __file__}
exec(compile(helper_raw, HELPER_PATH, "exec"), helper)  # noqa: S102 -- exact pinned reviewer blob
real = helper["real"]
fraction = helper["fraction"]
endpoint = helper["endpoint"]
pair = helper["pair"]
rbounds = helper["rbounds"]
cbounds = helper["cbounds"]
ball = helper["ball"]
canonical = helper["canonical"]
phase_lambda = helper["phase_lambda"]
xi_coeff = helper["xi_unit_s_coefficients"]
xi_scalar = helper["reflected_xi_scalar"]
fcoeff = helper["fcoeff"]
winding = helper["winding_quadrants"]


def interval(v):
    lo, hi = map(fraction, v)
    need(lo <= hi, "ordered interval")
    return arb(real((lo + hi) / 2), real((hi - lo) / 2))


def authenticate():
    raw = git(SCIENCE, DATA_PATH)
    need(digest(raw) == DATA_HASH == digest((ROOT / DATA_PATH).read_bytes()), "fixture")
    fixture = json.loads(raw)
    distribution = importlib.metadata.distribution("python-flint")
    native = {
        str(p): hashlib.sha256(
            Path(distribution.locate_file(p)).read_bytes()
        ).hexdigest()
        for p in distribution.files
        if str(p).endswith((".pyd", ".dll"))
    }
    runtime = {
        "python_flint": flint.__version__,
        "flint": flint.__FLINT_VERSION__,
        "python": platform.python_version(),
        "system": platform.system(),
        "machine": platform.machine(),
        "native_files": len(native),
        "native_files_sha256": digest(canonical(native)),
    }
    need(runtime == fixture["runtime"], "all 44 native runtime hashes and versions")
    payload = dict(fixture)
    expected = payload.pop("payload_sha256")
    need(digest(canonical(payload)) == expected, "canonical payload")
    for path, expected in fixture["artifacts"].items():
        need(digest(git(SCIENCE, path)) == expected, "frozen science artifact")
        need(digest((ROOT / path).read_bytes()) == expected, "current science artifact")
    pending = list(fixture["frozen_sources"])
    seen = set()
    while pending:
        source = pending.pop()
        key = (source["commit"], source["path"])
        if key in seen:
            continue
        seen.add(key)
        raw = git(*key)
        need(digest(raw) == source["sha256_lf"], "recursive source SHA256")
        need(blob(raw) == source["git_blob"], "recursive source Git blob")
        if key[1].endswith(".sources.json"):
            pending.extend(json.loads(raw).get("frozen_sources", []))
    need(len(fixture["roots"]) == 40, "complete forty roots")
    need(fixture["parameter_anchor"] == 64, "ONE lambda anchor")
    need([b["count"] for b in fixture["boxes"]] == [8, 9, 9], "source box coverage")
    return fixture, len(seen)


def boundary(original, bits, denominator, terms):
    ctx.prec = bits
    lam = phase_lambda(64)
    anchor = original["box_center"]
    corners = [
        (Q(anchor - 6), Q(0)),
        (Q(anchor + 6), Q(0)),
        (Q(anchor + 6), Q(1)),
        (Q(anchor - 6), Q(1)),
    ]
    path = []
    for a, b in zip(corners, corners[1:] + corners[:1]):
        steps = int((abs(b[0] - a[0]) + abs(b[1] - a[1])) * denominator)
        path.extend(
            (a[0] + Q(j, steps) * (b[0] - a[0]), a[1] + Q(j, steps) * (b[1] - a[1]))
            for j in range(steps)
        )
    need(len(path) == 26 * denominator == len(set(path)), "complete boundary")
    need(denominator == 2 * original["attempts"][-1]["mesh_denominator"], "refinement")
    vertices = []
    for x, y in path:
        value = fcoeff(acb(real(x), real(y)), lam, 1)[0]
        vertices.append((endpoint(value.real.mid()), endpoint(value.imag.mid())))
    stream = hashlib.sha256()
    for j, (p, q) in enumerate(zip(path, path[1:] + path[:1])):
        mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
        dx, dy = abs(p[0] - q[0]) / 2, abs(p[1] - q[1]) / 2
        h = dx + dy
        need(h == Q(1, 2 * denominator) and (dx == 0 or dy == 0), "arc coverage")
        center = acb(real(mx), real(my))
        coefficients = fcoeff(center, lam, terms)
        displacement = acb(arb(0, real(dx)), arb(0, real(dy)))
        enclosure = acb(0)
        for c in reversed(coefficients):
            enclosure = enclosure * displacement + c
        outer = acb(arb(center.real, real(Q(1, 4))), arb(center.imag, real(Q(1, 4))))
        sup = xi_scalar(outer).abs_upper()
        error = (
            sup * (120 * 8**5 + lam * 720 * 8**6) * real((8 * h) ** terms / (1 - 8 * h))
        ).upper()
        enclosure += acb(arb(0, error), arb(0, error))
        need(enclosure.is_finite(), f"finite arc {anchor}/{j}")
        bounds = cbounds(enclosure)
        separated = False
        for axis_index, axis in enumerate(("real", "imag")):
            lo, hi = map(fraction, bounds[axis])
            lo = min(
                lo, vertices[j][axis_index], vertices[(j + 1) % len(path)][axis_index]
            )
            hi = max(
                hi, vertices[j][axis_index], vertices[(j + 1) % len(path)][axis_index]
            )
            bounds[axis] = [pair(lo), pair(hi)]
            separated |= lo > 0 or hi < 0
        need(separated, f"zero-free homotopy arc {anchor}/{j}")
        need(
            enclosure.overlaps(ball(original["arcs"][j // 2]["image"])),
            "refined overlap",
        )
        stream.update(canonical(bounds))
    count = winding(vertices)
    need(count == original["count"], "independent quadrant winding")
    need(winding(list(reversed(vertices))) == -count, "orientation hostile control")
    return {
        "box_center": anchor,
        "bits": bits,
        "mesh_denominator": denominator,
        "terms": terms,
        "arcs": len(path),
        "count": count,
        "convex_hull_stream_sha256": stream.hexdigest(),
    }


def nodes_and_gram(fixture, bits):
    ctx.prec = bits
    lam = phase_lambda(64)
    # HA deliberately retains its source parameter through the frozen FC fixture.
    parent = json.loads(
        git(
            "0e3fc9b482f0f115a49a6209ccbfeffae640014a",
            "research/exploratory/xi_fixed_lambda_joint_box_compression.json",
        )
    )
    need(lam.overlaps(interval(parent["lambda_enclosure"])), "phase lambda overlap")
    nodes, values, records = [], [], []
    overlaps = 0
    for index, row in enumerate(fixture["roots"]):
        need(row["parameter_anchor"] == 64, "node parameter")
        x, y = map(fraction, row["center"])
        r = fraction(row["radius"])
        need(r == Q(1, 2**120), "root radius")
        center = acb(real(x), real(y))
        region = acb(arb(center.real, real(r)), arb(center.imag, real(r)))
        point = [v * math.factorial(j) for j, v in enumerate(xi_coeff(center, 9))]
        jets = [v * math.factorial(j) for j, v in enumerate(xi_coeff(region, 9))]
        for fresh, old in (
            (point, row["point_derivatives"]),
            (jets, row["rectangle_derivatives"]),
            (jets, row["reflected_rectangle_derivatives"]),
        ):
            need(len(old) == 9, "jet coverage")
            for a, b in zip(fresh, old):
                need(a.overlaps(ball(b)), "independent reflected jet")
                overlaps += 1
        residual = (point[5] - acb(0, 1) * lam * point[6]).abs_upper()
        derivative = (point[6] - acb(0, 1) * lam * point[7]).abs_lower()
        second = (jets[7] - acb(0, 1) * lam * jets[8]).abs_upper()
        need(
            (endpoint(residual) + endpoint(second) * r * r / 2) * 2**50
            < endpoint(derivative) * r,
            "fresh simple root Rouche",
        )
        r0, c0 = (
            jets[0] - acb(0, 1) * lam * jets[1],
            jets[0] + acb(0, 1) * lam * jets[1],
        )
        guards = [
            r0,
            c0,
            jets[5] + acb(0, 1) * lam * jets[6],
            jets[6],
            jets[0] * jets[6] - jets[1] * jets[5],
            jets[6] - acb(0, 1) * lam * jets[7],
        ]
        need(all(v.abs_lower() > 0 for v in guards), "fresh noncommon guards")
        value = r0 / c0
        need(value.overlaps(ball(row["raw_theta"])), "fresh raw value")
        need(abs(value).overlaps(interval(row["raw_modulus"])), "raw modulus")
        if index == 14:
            need(abs(value) < real(Q(54, 1000)), "heldout quarter-pattern refutation")
        w = row["box_center"]
        need(w - 6 < x - r < x + r < w + 6 and 0 < y - r < y + r < 1, "inside box")
        for previous in records:
            need(abs(x - fraction(previous["center"][0])) > 2 * r, "disjoint discs")
        records.append(row)
        nodes.append(region)
        values.append(value)
    gram, gram_abs = [], []
    for i, u in enumerate(nodes):
        grow, mrow = [], []
        for j, v in enumerate(nodes):
            g = (
                acb(1)
                if i == j
                else (
                    2
                    * (u.imag * v.imag).sqrt()
                    / (u.imag + v.imag + acb(0, 1) * (v.real - u.real))
                )
            )
            need(
                g.overlaps(ball(fixture["finite_data"]["normalized_gram"][i][j])),
                "Gram",
            )
            grow.append(g)
            mrow.append(abs(g))
        gram.append(grow)
        gram_abs.append(mrow)
    weights = [abs(v) ** 2 * b.imag / b.real for b, v in zip(nodes, values)]
    for fresh, old in zip(weights, fixture["finite_data"]["node_weighted_alignments"]):
        need(fresh.overlaps(interval(old)), "weighted node")
    prefixes = []
    prior_indices = set()
    for original, size in zip(fixture["finite_data"]["prefixes"], (14, 22, 31, 40)):
        ids = original["root_indices"]
        need(ids == list(range(size)), "complete nested prefix")
        ceiling = fraction(original["finite_bessel_strict_upper"])
        for i in ids:
            need(
                sum((gram_abs[i][j] for j in ids), arb(0)) < real(ceiling),
                "Bessel ceiling",
            )
        weight = sum((weights[i] for i in ids), arb(0))
        increment = sum((weights[i] for i in ids if i not in prior_indices), arb(0))
        need(
            weight > real(fraction(original["weighted_alignment_strict_lower"])),
            "weight floor",
        )
        need(
            increment > real(fraction(original["weighted_increment_strict_lower"])),
            "increment floor",
        )
        need(
            weight.overlaps(interval(original["weighted_alignment"])), "prefix overlap"
        )
        need(
            increment.overlaps(interval(original["weighted_increment"])),
            "increment overlap",
        )
        prefixes.append(
            {
                "dimension": size,
                "finite_bessel_ceiling": pair(ceiling),
                "weighted_alignment": rbounds(weight),
                "increment": rbounds(increment),
            }
        )
        prior_indices = set(ids)
    return {
        "bits": bits,
        "simple_noncommon_roots": 40,
        "jet_overlaps": overlaps,
        "full_gram_entries": 1600,
        "prefixes": prefixes,
        "first_heldout_raw_modulus": rbounds(abs(values[14])),
    }


def run(mode):
    fixture, source_count = authenticate()
    previous = ctx.prec, ctx.cap
    try:
        if mode == "boundary":
            rows = []
            for original, (anchor, bits, denominator, terms) in zip(
                fixture["boxes"], PANELS
            ):
                need(original["box_center"] == anchor, "fixed panel")
                rows.append(boundary(original, bits, denominator, terms))
                print(
                    f"independent complete box {anchor}: {rows[-1]['count']}",
                    file=sys.stderr,
                )
        else:
            rows = [nodes_and_gram(fixture, int(mode))]
        result = {
            "schema": "xi-heldout-independent-review-v1",
            "mode": mode,
            "science_commit": SCIENCE,
            "science_fixture_sha256_lf": DATA_HASH,
            "reviewer_helper_commit": HELPER_COMMIT,
            "reviewer_helper_git_blob": HELPER_BLOB,
            "recursive_source_files": source_count,
            "author_code_executed": False,
            "shared_special_function_library": True,
            "outcomes": rows,
            "script_sha256_lf": digest(Path(__file__).read_bytes()),
        }
        result["payload_sha256"] = digest(canonical(result))
        return result
    finally:
        ctx.prec, ctx.cap = previous


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("boundary", "384", "512"), required=True)
    print(json.dumps(run(parser.parse_args().mode), sort_keys=True, indent=2))
