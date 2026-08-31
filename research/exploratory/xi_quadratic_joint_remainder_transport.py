"""Exact inherited-data replay of the post-QT joint Taylor remainder panel."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import subprocess
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
STEM = "xi_quadratic_joint_remainder_transport"
NOTE = HERE / "XI_QUADRATIC_JOINT_REMAINDER_TRANSPORT.md"
MANIFEST = HERE / (STEM + ".sources.json")
FIXTURE = HERE / (STEM + ".json")
TEST = ROOT / "tests" / ("test_" + STEM + ".py")
BASE = "530732c5fd7f50364381f8af50e97ce809b674c5"
DESIGN = "99a7eb0310ca86392ef28b91b7c6d1fe81f35e61"
QT_STEM = "research/exploratory/xi_quadratic_critical_transport"
EPS = Q(1, 2**120)
SQRT_BITS = 512
RATIOS = (Q(1, 16), Q(1, 8), Q(1, 4), Q(1, 2), Q(3, 4))
TIERS = (256, 512, 1024)
MAX_BYTES, MAX_BITS, MAX_NODES = 24_000_000, 12_288, 600_000
BINDINGS = [
    {
        "commit": BASE,
        "path": "research/exploratory/XI_QUADRATIC_CRITICAL_TRANSPORT.md",
        "git_blob": "cb634e9ac1e5ddbdffad01286a0b37ca958ac92b",
        "sha256_lf": "b9e7cf4911688d81c44ec9d871104e063c7bf46f574d86b479c6d912559d7269",
    },
    {
        "commit": BASE,
        "path": QT_STEM + ".py",
        "git_blob": "a5e48dea3a25e1ff7419b2f6e2cfeef3de230185",
        "sha256_lf": "28033a330ade30e0079f6e24cd0f4b07e9de9ba70438f92c88fe5c0f7fe8c373",
    },
    {
        "commit": BASE,
        "path": QT_STEM + ".json",
        "git_blob": "322281110f34af24575be29aed32acfd25657959",
        "sha256_lf": "45e9d81f5cfe22662ad9e07b9a994796b3c3b18743ae74c8cbd3ce095f3a4cce",
    },
    {
        "commit": BASE,
        "path": QT_STEM + ".sources.json",
        "git_blob": "58bd03b1d15ce4d2eb91addb4c209a0f43fab80c",
        "sha256_lf": "66aa6f3d483bc638eed43315592c3cc5f3f8ef2baa9d9518e2fa0de3e685d757",
    },
    {
        "commit": BASE,
        "path": "tests/test_xi_quadratic_critical_transport.py",
        "git_blob": "cde20699d7b3894bf40db419b2d90a3d93459751",
        "sha256_lf": "d5493e8c31d53d66fdb00f35dfa1198b173513e23b2bfd3bdcb2d39d80423749",
    },
    {
        "commit": DESIGN,
        "path": "research/exploratory/XI_QUADRATIC_JOINT_REMAINDER_TRANSPORT.md",
        "git_blob": "0b13e70ffef6610f9ae2a2dc484ac17ebb3294f3",
        "sha256_lf": "7f2c0270404fce9b627154c68464d5f96f58823f7644228e17fd1a1b8a92e1c9",
    },
]
CONTRACT = {
    "arithmetic_class": "MIXED",
    "arithmetic_components": ["EXACT_RATIONAL", "CERTIFIED_INTEGER_COVERAGE"],
    "rounding": "exact rational operations; fixed512-bit dyadic square-root endpoints outward",
    "primitive": "actual f(z)=xi_R(1/2+iz), g=f5, inherited fixed positive lambda_(64)",
    "inheritance": "authenticated QT critical/jet/M3/root certificates; no parent special-function or runtime-binary replay",
    "panel": "all26 nodes times5 ratios times3 tiers, all390 outcomes retained",
    "source_domain": "unchanged QT disc and wrapper; no new M3, gauge, radius ratio or source window",
    "criterion": "M3*(y+r)^2*(lambda/2-(y-r)/6)<abs(c)*r*(d-r/2)",
    "matching": "separate entire HA rectangle squared-displacement upper < lower-radius squared",
    "nonpass": "inherited bounds did not certify; NOT impossibility for every valid M3",
    "exclusions": "no QR-old-criterion retraction, RH, innerness, novelty or physical capture",
    "caps": {
        "bytes": MAX_BYTES,
        "integer_bits": MAX_BITS,
        "json_nodes": MAX_NODES,
        "json_depth": 28,
        "container": 30000,
        "source_versions": 100,
        "cells": 390,
        "sqrt_bits": SQRT_BITS,
    },
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def integer(n, lo, hi):
    require(type(n) is int and lo <= n <= hi, "strict integer/cap")
    return n


def rational(n):
    require(type(n) in (int, Q), "strict rational")
    value = Q(n)
    require(
        max(abs(value.numerator).bit_length(), value.denominator.bit_length())
        <= MAX_BITS,
        "rational bit cap",
    )
    return value


def pair(n):
    n = rational(n)
    return [n.numerator, n.denominator]


def unpair(value):
    require(type(value) is list and len(value) == 2, "rational pair shape")
    a, b = value
    require(type(a) is int and type(b) is int and b > 0, "rational pair types")
    out = rational(Q(a, b))
    require(pair(out) == value, "canonical rational pair")
    return out


def interval(value):
    require(type(value) is list and len(value) == 2, "interval shape")
    lo, hi = map(unpair, value)
    require(lo <= hi, "ordered interval")
    return lo, hi


def packed(value):
    return [pair(n) for n in value]


def point(n):
    n = rational(n)
    return n, n


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def sub(a, b):
    return a[0] - b[1], a[1] - b[0]


def mul(a, b):
    values = [x * y for x in a for y in b]
    return min(values), max(values)


def div(a, b):
    require(not b[0] <= 0 <= b[1], "division interval contains zero")
    return mul(a, tuple(sorted((1 / b[0], 1 / b[1]))))


def scale(a, n):
    return mul(a, point(n))


def absolute(a):
    return (Q(0) if a[0] <= 0 <= a[1] else min(map(abs, a)), max(map(abs, a)))


def meet(*values):
    result = max(v[0] for v in values), min(v[1] for v in values)
    require(result[0] <= result[1], "disjoint valid source enclosures")
    return result


def square_root(value):
    lo, hi = value
    require(0 <= lo <= hi, "square-root domain")
    grid = 1 << SQRT_BITS
    lower = math.isqrt((lo.numerator * grid * grid) // lo.denominator)
    upper = math.isqrt((hi.numerator * grid * grid) // hi.denominator)
    if upper * upper * hi.denominator != hi.numerator * grid * grid:
        upper += 1
    return Q(lower, grid), Q(upper, grid)


def validate_tree(value, depth=0, visits=None):
    visits = [0] if visits is None else visits
    visits[0] += 1
    require(depth <= 28 and visits[0] <= MAX_NODES, "JSON depth/node cap")
    if value is None or type(value) is bool:
        return
    if type(value) is int:
        require(value.bit_length() <= MAX_BITS, "JSON integer bit cap")
        return
    if type(value) is str:
        require(value.isascii() and len(value) <= 4096, "JSON string cap/ASCII")
        return
    require(
        type(value) in (dict, list) and len(value) <= 30000, "JSON container type/cap"
    )
    if type(value) is dict:
        require(
            all(type(k) is str and k.isascii() and len(k) <= 4096 for k in value),
            "JSON key type/cap",
        )
        children = value.values()
    else:
        children = value
    for child in children:
        validate_tree(child, depth + 1, visits)


def canonical(value):
    validate_tree(value)
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    require(len(raw) <= MAX_BYTES, "JSON byte cap")
    return raw


def decode(raw):
    require(type(raw) is bytes and len(raw) <= MAX_BYTES, "JSON byte type/cap")

    def unique(items):
        out = {}
        for key, value in items:
            require(key not in out, "duplicate JSON key")
            out[key] = value
        return out

    def reject(_):
        raise ValueError("noninteger JSON number")

    value = json.loads(
        raw, object_pairs_hook=unique, parse_float=reject, parse_constant=reject
    )
    validate_tree(value)
    return value


def lf(raw):
    require(type(raw) is bytes and len(raw) <= MAX_BYTES, "source byte type/cap")
    text = raw.decode("utf-8")
    require(
        all(ord(c) >= 32 or c in "\t\r\n" for c in text)
        and not any(127 <= ord(c) <= 159 for c in text),
        "source control byte",
    )
    return raw.replace(b"\r\n", b"\n")


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


@lru_cache(maxsize=100)
def commit_object(commit):
    require(
        type(commit) is str and re.fullmatch("[0-9a-f]{40}", commit), "source commit"
    )
    kind = subprocess.check_output(
        ["git", "--no-replace-objects", "cat-file", "-t", commit], cwd=ROOT
    ).strip()
    require(kind == b"commit", "source must be a commit object")


def read_source(binding):
    require(type(binding) is dict, "source binding type")
    require(
        all(k in binding for k in ("commit", "path", "git_blob", "sha256_lf")),
        "source binding fields",
    )
    commit, path = binding["commit"], binding["path"]
    require(
        type(commit) is str and re.fullmatch("[0-9a-f]{40}", commit), "source commit"
    )
    require(
        type(path) is str
        and path
        and ":" not in path
        and "\\" not in path
        and all(ord(c) >= 32 and not 127 <= ord(c) <= 159 for c in path)
        and all(x not in ("", ".", "..") for x in path.split("/")),
        "source path",
    )
    require(
        type(binding["git_blob"]) is str
        and re.fullmatch("[0-9a-f]{40}", binding["git_blob"])
        and type(binding["sha256_lf"]) is str
        and re.fullmatch("[0-9a-f]{64}", binding["sha256_lf"]),
        "source digest types",
    )
    commit_object(commit)
    raw = subprocess.check_output(
        ["git", "--no-replace-objects", "show", commit + ":" + path], cwd=ROOT
    )
    require(len(raw) <= MAX_BYTES, "source byte cap")
    blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    require(
        blob == binding["git_blob"] and digest(lf(raw)) == binding["sha256_lf"],
        "frozen source seal mismatch",
    )
    return raw


def manifest():
    return {
        "schema": STEM + "-sources-v1",
        "authoring_base": BASE,
        "post_QT_design": DESIGN,
        "contract": CONTRACT,
        "frozen_sources": BINDINGS,
    }


def authenticate():
    require(
        canonical(decode(MANIFEST.read_bytes())) == canonical(manifest()),
        "manifest mismatch",
    )
    pending, catalog, documents = list(BINDINGS), {}, {}
    while pending:
        pin = pending.pop()
        key = pin["commit"], pin["path"]
        if key in catalog:
            require(
                catalog[key]["git_blob"] == pin["git_blob"]
                and catalog[key]["sha256_lf"] == pin["sha256_lf"],
                "conflicting source pins",
            )
            continue
        require(len(catalog) < 100, "source closure cap")
        raw = read_source(pin)
        catalog[key] = {k: pin[k] for k in ("commit", "path", "git_blob", "sha256_lf")}
        if pin["path"].endswith(".sources.json"):
            document = decode(raw)
            documents[key] = document
            require(
                type(document.get("frozen_sources")) is list,
                "inherited manifest sources",
            )
            pending.extend(document["frozen_sources"])
    parent = decode(read_source(BINDINGS[2]))
    unsigned = {k: v for k, v in parent.items() if k != "payload_sha256"}
    require(parent["payload_sha256"] == digest(canonical(unsigned)), "QT payload seal")
    qt_manifest = documents[(BASE, QT_STEM + ".sources.json")]
    require(
        canonical(parent["contract"]) == canonical(qt_manifest["contract"]),
        "QT contract binding",
    )
    require(
        canonical(parent["frozen_sources"]) == canonical(qt_manifest["frozen_sources"]),
        "QT source binding",
    )
    require(
        canonical(parent["runtime"]) == canonical(qt_manifest["runtime"]),
        "QT runtime provenance",
    )
    require(
        digest(canonical(parent["environmental_attempt_history"]))
        == qt_manifest["broad_history_sha256"],
        "QT historical ledger pin",
    )
    expected_artifacts = {
        p["path"]: p["sha256_lf"]
        for p in BINDINGS[:5]
        if p["path"] != QT_STEM + ".json"
    }
    require(
        canonical(parent["artifacts"]) == canonical(expected_artifacts),
        "QT four artifact seals",
    )
    return parent, [catalog[k] for k in sorted(catalog)]


def geometry(lam, a, c, ratio, source_q, source_d, source_y, source_r):
    require(type(ratio) is Q and ratio in RATIOS, "fixed ratio")
    require(lam[0] > 0 and mul(a, c)[1] < 0, "positive lambda/opposite signs")
    q = meet(div(scale(a, -1), mul(lam, c)), source_q)
    require(q[0] > 0 and 2 * q[1] < lam[0], "positive q/discriminant")
    disc = meet(
        sub(mul(lam, lam), scale(mul(lam, q), 2)),
        add(mul(lam, lam), scale(div(a, c), 2)),
    )
    require(disc[0] > 0, "positive discriminant")
    d = meet(square_root(disc), source_d)
    # Keep the dyadic source/difference enclosure.  The stable quotient is an
    # independent consistency intersection, not a new rounding operation.
    y = meet(sub(lam, d), source_y)
    meet(y, div(scale(mul(lam, q), 2), add(lam, d)))
    r = meet(scale(y, ratio), source_r)
    require(
        y[0] > 0 and y[1] < lam[0] and 0 < r[0] and r[1] < y[0] and r[1] < 2 * d[0],
        "quadratic disc geometry",
    )
    return q, d, y, r


def model_bounds(lam, d, y, r, c, m3):
    m3 = rational(m3)
    require(m3 >= 0, "nonnegative M3")
    h = add(y, r)
    joint_factor = sub(scale(lam, Q(1, 2)), scale(sub(y, r), Q(1, 6)))
    old_factor = add(scale(lam, Q(1, 2)), scale(h, Q(1, 6)))
    require(joint_factor[0] > 0, "positive joint factor")
    common = scale(mul(h, h), m3)
    joint_error, old_error = mul(common, joint_factor), mul(common, old_factor)
    margin = mul(mul(absolute(c), r), sub(d, scale(r, Q(1, 2))))
    require(margin[0] > 0, "positive model margin")
    return joint_factor, joint_error, old_error, margin


def containment(t, y, r, center, radius):
    x, eta = map(unpair, center)
    radius = unpair(radius)
    require(radius > 0, "positive parent radius")
    dx = sub((x - radius, x + radius), t)
    dy = sub((eta - radius, eta + radius), y)
    displacement2 = max(abs(x) for x in dx) ** 2 + max(abs(x) for x in dy) ** 2
    return displacement2, r[0] ** 2, displacement2 < r[0] ** 2


def source_record(node):
    require(node["critical"]["simple_real_critical"] is True, "inherited real critical")
    critical = node["critical"]
    center, eps = unpair(critical["center"]), unpair(critical["radius"])
    require(eps == EPS, "fixed critical radius")
    valid = False
    for attempt in critical["attempts"]:
        if "left" in attempt:
            residual, low, upper = [
                unpair(attempt[k])
                for k in ("residual", "derivative_lower", "second_upper")
            ]
            require(residual >= 0 and low > 0 and upper >= 0, "critical bound signs")
            require(
                unpair(attempt["left"]) == residual + upper * eps * eps / 2
                and unpair(attempt["right"]) == low * eps,
                "critical exact inequality",
            )
            valid |= (
                attempt["status"] == "PASS"
                and residual + upper * eps * eps / 2 < low * eps
            )
    require(valid, "critical Rouche certificate")
    return center - eps, center + eps


def cell(node, group, attempt, tier, t):
    ratio = unpair(group["ratio"])
    require(
        type(attempt["bits"]) is int
        and attempt["bits"] in TIERS
        and attempt["bits"] == tier["bits"],
        "same source tier",
    )
    require(attempt["ratio"] == group["ratio"], "same source ratio")
    lam, a, c = [interval(tier[k]) for k in ("lambda", "a", "c")]
    require(
        interval(tier["T"])[0] <= t[0] and interval(tier["T"])[1] >= t[1],
        "whole critical interval",
    )
    q, d, y, r = geometry(
        lam,
        a,
        c,
        ratio,
        interval(tier["q"]),
        interval(attempt["d"]),
        interval(attempt["y"]),
        interval(attempt["radius"]),
    )
    third = attempt["third_derivative"]
    require(third["status"] == "PASS", "inherited M3 available")
    m3, radius = unpair(third["upper"]), unpair(third["radius_upper"])
    # Intersections retain the original enclosures; never enlarge the inherited M3 region.
    require(add(y, r)[1] <= radius, "inherited M3 region covers new interval disc")
    factor, error, old_error, margin = model_bounds(lam, d, y, r, c, m3)
    matched_data = containment(t, y, r, node["HA_center"], node["HA_radius"])
    passed = error[1] < margin[0]
    old = {
        k: attempt[k]
        for k in ("status", "reason", "transport_certified", "parent_matched")
    }
    require(
        old["transport_certified"] is False and old["status"] == "FAILED",
        "unchanged old failures",
    )
    result = {
        "node": node["index"],
        "box_center": node["box_center"],
        "ratio": pair(ratio),
        "bits": attempt["bits"],
        "old_outcome": old,
        "old_attempt_sha256": digest(canonical(attempt)),
        "old_tier_sha256": digest(canonical(tier)),
        "source_M3_upper": pair(m3),
        "source_region_radius": pair(radius),
        "lambda": packed(lam),
        "q": packed(q),
        "d": packed(d),
        "y": packed(y),
        "r": packed(r),
        "joint_factor": packed(factor),
        "joint_error": packed(error),
        "old_error_reconstructed": packed(old_error),
        "model_margin": packed(margin),
        "full_parent_displacement_squared_upper": pair(matched_data[0]),
        "radius_squared_lower": pair(matched_data[1]),
        "full_parent_rectangle_contained": matched_data[2],
        "transport_certified": passed,
        "matched_parent_root": passed and matched_data[2],
        "status": "MATCHED_PARENT"
        if passed and matched_data[2]
        else "TRANSPORT_ONLY"
        if passed
        else "NOT_CERTIFIED_INHERITED_BOUND",
    }
    canonical(result)
    return result


def exact_control():
    lam, d, y, r, c, m3 = Q(1), Q(1, 2), Q(1, 2), Q(1, 4), Q(-1), Q(1, 3)
    _, error, old, margin = model_bounds(*map(point, (lam, d, y, r, c)), m3)
    require(
        error[1] == Q(11, 128) and old[0] == Q(15, 128) and margin[0] == Q(12, 128),
        "strict joint control",
    )
    return {
        "g": "3/8-w^2/2+w^3/18",
        "lambda": pair(lam),
        "M3": pair(m3),
        "old_threshold": [4, 15],
        "joint_threshold": [4, 11],
        "old_error": packed(old),
        "joint_error": packed(error),
        "margin": packed(margin),
    }


def build_report():
    parent, closure = authenticate()
    records = parent["records"]
    require(
        type(records) is list
        and len(records) == 26
        and [n["index"] for n in records] == list(range(26)),
        "complete node coverage",
    )
    output = []
    for node in records:
        integer(node["index"], 0, 25)
        t = source_record(node)
        require(
            [unpair(g["ratio"]) for g in node["quadratic"]] == list(RATIOS),
            "five fixed ratios",
        )
        require(
            [j["bits"] for j in node["jet_tiers"]] == list(TIERS),
            "three fixed jet tiers",
        )
        for group in node["quadratic"]:
            require(
                [a["bits"] for a in group["attempts"]] == list(TIERS),
                "all three old attempts",
            )
            for attempt, tier in zip(group["attempts"], node["jet_tiers"]):
                output.append(cell(node, group, attempt, tier, t))
    require(len(output) == 390, "all390 cells")
    best = min(
        output,
        key=lambda row: (
            interval(row["joint_error"])[1] / interval(row["model_margin"])[0]
        ),
    )
    best_ratio = interval(best["joint_error"])[1] / interval(best["model_margin"])[0]
    best_floor = (best_ratio * 1_000_000).__floor__()
    summary = {
        "cells": 390,
        "nodes": 26,
        "node_ratio_cases": 130,
        "old_noncertified_cells": 390,
        "joint_certified_cells": sum(x["transport_certified"] for x in output),
        "joint_matched_cells": sum(x["matched_parent_root"] for x in output),
        "joint_noncertified_cells": sum(not x["transport_certified"] for x in output),
        "least_sufficient_check_ratio": {
            "node": best["node"],
            "ratio": best["ratio"],
            "bits": best["bits"],
            "scale": 1_000_000,
            "floor": best_floor,
            "strict_upper_integer": best_floor + 1,
            "meaning": "floor <= 1000000*error_upper/margin_lower < strict_upper_integer; not actual error",
        },
        "by_ratio": [
            {
                "ratio": pair(r),
                "cells": 78,
                "certified": sum(
                    x["transport_certified"] for x in output if x["ratio"] == pair(r)
                ),
                "matched": sum(
                    x["matched_parent_root"] for x in output if x["ratio"] == pair(r)
                ),
            }
            for r in RATIOS
        ],
    }
    report = {
        "schema": STEM + "-v1",
        "contract": CONTRACT,
        "frozen_sources": BINDINGS,
        "authenticated_source_closure": closure,
        "inherited_QT_payload_sha256": parent["payload_sha256"],
        "inherited_runtime_not_replayed": parent["runtime"],
        "exact_control": exact_control(),
        "records": output,
        "summary": summary,
        "artifacts": {
            p.relative_to(ROOT).as_posix(): digest(lf(p.read_bytes()))
            for p in (NOTE, Path(__file__), MANIFEST, TEST)
        },
    }
    return {**report, "payload_sha256": digest(canonical(report))}


def check_report(report):
    validate_tree(report)
    require(type(report) is dict and "payload_sha256" in report, "report shape")
    unsigned = {k: v for k, v in report.items() if k != "payload_sha256"}
    require(report["payload_sha256"] == digest(canonical(unsigned)), "payload seal")
    require(
        canonical(report) == canonical(build_report()),
        "fresh inherited-data reconstruction",
    )
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--emit", action="store_true")
    modes.add_argument("--emit-sources", action="store_true")
    modes.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.check:
        check_report(decode(FIXTURE.read_bytes()))
        print(
            "PASS exact390-cell inherited joint-remainder replay; no parent special-function replay"
        )
        return
    result = manifest() if args.emit_sources else build_report()
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
