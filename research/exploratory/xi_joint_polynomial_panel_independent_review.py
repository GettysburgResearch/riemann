"""Independent all26 reflected-Xi/direct-power replay, adapted from root JP review."""

import argparse
import hashlib
import importlib.metadata
import json
import math
import platform
import re
import subprocess
from fractions import Fraction as Q
from pathlib import Path, PurePosixPath

import flint
from flint import acb, acb_series, arb, ctx

ROOT = Path(__file__).resolve().parents[2]
QT = "530732c5fd7f50364381f8af50e97ce809b674c5"
QT_PATH = "research/exploratory/xi_quadratic_critical_transport.json"
QT_SHA = "45e9d81f5cfe22662ad9e07b9a994796b3c3b18743ae74c8cbd3ce095f3a4cce"
INDICES, N, ARCS, PREC = tuple(range(26)), 32, 64, 1024
EPS, R = Q(1, 2**120), Q(7, 8)
OUT = Path(__file__).with_suffix(".json")
SCIENCE = "96543552b5bc5976d96c35123bfb82e609a27972"
STEM = "xi_joint_polynomial_point_transport"
FIXTURE_SHA = "aef1379325c101b31bdad40940066daa1fdae3a37496008a28fb22fe31cdc735"


def need(ok, reason):
    if not ok:
        raise ValueError(reason)


def canon(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def source(commit, path):
    need(
        type(commit) is str and re.fullmatch(r"[0-9a-f]{40}", commit), "commit identity"
    )
    need(
        type(path) is str and "\\" not in path and ":" not in path, "POSIX source path"
    )
    parsed = PurePosixPath(path)
    need(
        not parsed.is_absolute()
        and parsed.as_posix() == path
        and ".." not in parsed.parts,
        "canonical source path",
    )
    kind = subprocess.check_output(
        ["git", "--no-replace-objects", "cat-file", "-t", commit], cwd=ROOT
    ).strip()
    need(kind == b"commit", "actual commit object")
    raw = subprocess.check_output(
        ["git", "--no-replace-objects", "show", commit + ":" + path], cwd=ROOT
    )
    need(len(raw) <= 24_000_000, "source byte cap")
    return raw


def provenance():
    paths = [
        "research/exploratory/XI_JOINT_POLYNOMIAL_POINT_TRANSPORT.md",
        "research/exploratory/" + STEM + ".py",
        "research/exploratory/" + STEM + ".json",
        "research/exploratory/" + STEM + ".sources.json",
        "tests/test_" + STEM + ".py",
    ]
    lf = lambda raw: raw.replace(b"\r\n", b"\n")
    raw = {}
    for path in paths:
        raw[path] = source(SCIENCE, path)
        need(
            lf(raw[path]) == lf((ROOT / path).read_bytes()), "frozen science unchanged"
        )
    fixture = json.loads(raw[paths[2]])
    need(sha(lf(raw[paths[2]])) == FIXTURE_SHA, "frozen JP fixture")
    unsigned = {k: v for k, v in fixture.items() if k != "payload_sha256"}
    need(sha(canon(unsigned)) == fixture["payload_sha256"], "JP payload")
    for path, digest in fixture["artifacts"].items():
        need(path in raw and sha(lf(raw[path])) == digest, "JP artifact seal")
    manifest = json.loads(raw[paths[3]])
    queue, seen = list(manifest["frozen_sources"]), {}
    while queue:
        row = queue.pop(0)
        key = row["commit"] + ":" + row["path"]
        if key in seen:
            need(seen[key] == row["sha256_lf"], "consistent source binding")
            continue
        value = source(row["commit"], row["path"])
        blob = hashlib.sha1(
            b"blob " + str(len(value)).encode() + b"\0" + value
        ).hexdigest()
        need(
            blob == row["git_blob"] and sha(lf(value)) == row["sha256_lf"],
            "transitive source seal",
        )
        seen[key] = row["sha256_lf"]
        if row["path"].endswith(".sources.json"):
            parent_manifest = json.loads(value)
            queue += parent_manifest.get(
                "frozen_sources", parent_manifest.get("sources", [])
            )
    distribution = importlib.metadata.distribution("python-flint")
    native = {}
    for path in distribution.files:
        if str(path).endswith((".pyd", ".dll")):
            location = Path(distribution.locate_file(path))
            need(
                location.is_file() and location.stat().st_size <= 100_000_000,
                "native library size",
            )
            native[str(path)] = sha(location.read_bytes())
    runtime = {
        "python_flint": flint.__version__,
        "flint": flint.__FLINT_VERSION__,
        "python": platform.python_version(),
        "system": platform.system(),
        "machine": platform.machine(),
        "native_files": len(native),
        "native_files_sha256": sha(canon(native)),
    }
    need(runtime == manifest["runtime"], "independent pinned runtime")
    record = fixture["record"]
    need(len(record["arcs"]) == 64, "all author arcs")
    for j, arc in enumerate(record["arcs"]):
        need(
            arc["index"] == j
            and arc["pi_interval"] == [pair(Q(j, 32)), pair(Q(j + 1, 32))],
            "author exact coverage",
        )
        error, margin = qp(arc["error_upper"]), qp(arc["margin_lower"])
        need(
            error == qp(arc["polynomial_upper"]) + qp(arc["tail_upper"]),
            "author exact error sum",
        )
        need(error < margin and arc["strict_pass"] is True, "author strict comparison")
        need(qp(arc["error_over_margin"]) == error / margin, "author exact ratio")
    return {
        "science": SCIENCE,
        "fixture_sha256_lf": FIXTURE_SHA,
        "payload_sha256": fixture["payload_sha256"],
        "transitive_sources": len(seen),
        "source_catalog_sha256": sha(canon(seen)),
        "runtime": runtime,
        "author_arc_exact_checks": 64,
    }


def qp(p):
    need(type(p) is list and len(p) == 2, "rational pair")
    a, b = p
    need(type(a) is int and type(b) is int and b > 0, "strict rational")
    need(max(abs(a).bit_length(), b.bit_length()) <= 8192, "rational cap")
    v = Q(a, b)
    need([v.numerator, v.denominator] == p, "reduced rational")
    return v


def ball(q):
    return arb(q.numerator) / arb(q.denominator)


def end(a):
    need(a.is_exact() and a.is_finite(), "finite exact endpoint")
    q = a.fmpq()
    return Q(int(q.numerator), int(q.denominator))


def pair(q):
    return [q.numerator, q.denominator]


def report_bounds(a):
    # Explicit outward rounding for a compact review fixture, not computation.
    scale = 2**64
    lo, hi = end(a.lower()), end(a.upper())
    low = lo.numerator * scale // lo.denominator
    high = -((-hi.numerator * scale) // hi.denominator)
    return [pair(Q(low, scale)), pair(Q(high, scale))]


def interval(lo, hi):
    need(lo <= hi, "ordered interval")
    return arb(ball((lo + hi) / 2), ball((hi - lo) / 2))


def reflected_jet(z, count):
    old = ctx.cap
    ctx.cap = count
    try:
        # The reflected s=1/2-i*z formula differs from the producer formula.
        s = acb_series([acb(arb(1) / 2) - acb(0, 1) * z, acb(0, -1)])
        value = s * (s - 1) / 2
        value *= (-s * arb.pi().log() / 2).exp() * (s / 2).gamma() * s.zeta()
        result = [value[j] * math.factorial(j) for j in range(count)]
        need(all(v.is_finite() for v in result), "finite reflected jet")
        return result
    finally:
        ctx.cap = old


def reflected_scalar(z):
    s = acb(arb(1) / 2) - acb(0, 1) * z
    value = s * (s - 1) / 2
    value *= (-s * arb.pi().log() / 2).exp() * (s / 2).gamma() * s.zeta()
    need(value.is_finite(), "finite reflected cell")
    return value


def parent():
    raw = subprocess.check_output(
        ["git", "--no-replace-objects", "show", QT + ":" + QT_PATH], cwd=ROOT
    ).replace(b"\r\n", b"\n")
    need(len(raw) < 8_000_000 and sha(raw) == QT_SHA, "exact QT parent")
    data = json.loads(raw)
    payload = {k: v for k, v in data.items() if k != "payload_sha256"}
    need(sha(canon(payload)) == data["payload_sha256"], "QT payload")
    need(len(data["records"]) == 26, "complete parent panel")
    rows = data["records"]
    need([row["index"] for row in rows] == list(INDICES), "complete ordered panel")
    for row in rows:
        need(type(row["index"]) is int, "strict point index")
        need(row["critical"]["simple_real_critical"] is True, "critical source")
        need(qp(row["critical"]["radius"]) == EPS, "critical radius")
    return rows


def compute(row):
    oldprec = ctx.prec
    ctx.prec = PREC
    try:
        center = qp(row["critical"]["center"])
        need(
            center - R - EPS > 20 and center + R + EPS < 1100 and -R > -1 and R < 2,
            "unchanged literal source rectangle",
        )
        t = interval(center - EPS, center + EPS)
        point = reflected_jet(acb(ball(center)), 9)
        square = reflected_jet(acb(t, interval(-EPS, EPS)), 9)
        critical_error = (
            end(point[6].abs_upper()) + end(square[8].abs_upper()) * EPS**2 / 2
        )
        critical_margin = end(point[7].abs_lower()) * EPS
        need(critical_error < critical_margin, "independent simple real critical point")
        derivatives = reflected_jet(acb(t), 40)
        need(all(v.imag.contains(0) for v in derivatives), "real full-interval jets")
        need(derivatives[6].real.contains(0), "unknown exact critical point")
        derivatives = [v.real for v in derivatives]
        a, c = derivatives[5], derivatives[7]
        lam = 2 / (acb(arb(1) / 4, 32).digamma().real - arb.pi().log())
        q = -a / (lam * c)
        need(q > 0 and 2 * q < lam, "quadratic discriminant")
        d = (lam**2 - 2 * lam * q).sqrt()
        y = lam - d  # Not the producer's rationalized y.
        radius = y / 2
        h = end((y + radius).upper())
        need(radius > 0 and radius < y and radius < 2 * d and h < R, "disc geometry")
        margin = end((abs(c) * radius * (d - radius / 2)).lower())
        need(margin > 0, "strict model margin")

        # Entire new 16x16 scalar cover at1024bits, including center uncertainty.
        cells, maximum = [], Q(0)
        for i in range(16):
            xl = center - R - EPS + Q(i, 16) * (2 * R + 2 * EPS)
            xu = center - R - EPS + Q(i + 1, 16) * (2 * R + 2 * EPS)
            for j in range(16):
                yl, yu = -R + Q(j, 16) * 2 * R, -R + Q(j + 1, 16) * 2 * R
                upper = end(
                    reflected_scalar(
                        acb(interval(xl, xu), interval(yl, yu))
                    ).abs_upper()
                )
                maximum = max(maximum, upper)
                cells.append(pair(upper))
        x = h / R
        tail = (
            maximum
            * x**N
            * (
                math.factorial(5) * math.comb(N + 5, 5) / (R**5 * (1 - x) ** 6)
                + end(lam.upper())
                * math.factorial(6)
                * math.comb(N + 6, 6)
                / (R**6 * (1 - x) ** 7)
            )
        )
        coefficients = [acb(0), acb(0), acb(0, -lam * derivatives[8] / 2)]
        coefficients += [
            acb(derivatives[n + 5], -lam * derivatives[n + 6]) / math.factorial(n)
            for n in range(3, N)
        ]
        records = []
        for j in range(ARCS):
            theta = arb.pi() * interval(Q(2 * j, ARCS), Q(2 * (j + 1), ARCS))
            w = acb(radius * theta.cos(), y + radius * theta.sin())
            # Direct, ascending powers and summation, not complex Horner evaluation.
            power, total = acb(1), acb(0)
            for n in range(N):
                total += coefficients[n] * power
                power *= w
            error = end(total.abs_upper()) + tail
            records.append(
                {
                    "index": j,
                    "pass": error < margin,
                    "ratio": report_bounds(ball(error / margin)),
                }
            )

        raw_center = row["HA_center"]
        need(type(raw_center) is list and len(raw_center) == 2, "HA complex center")
        xr, yi = map(qp, raw_center)
        hr = qp(row["HA_radius"])
        offset = acb(interval(xr - hr, xr + hr) - t, interval(yi - hr, yi + hr) - y)
        displacement = end(offset.abs_upper())
        radius_lower = end(radius.lower())
        matched = displacement < radius_lower
        need(len(records) == ARCS and len(cells) == 256, "complete geometry")
        result = {
            "schema": "xi-joint-polynomial-independent-reflected-review-v1",
            "parent": QT,
            "parent_fixture_sha256_lf": QT_SHA,
            "point_index": row["index"],
            "precision": PREC,
            "terms": N,
            "critical_recertified": True,
            "critical_error_margin_ratio": report_bounds(
                ball(critical_error / critical_margin)
            ),
            "fresh_reflected_coefficients": len(derivatives),
            "fresh_cover_cells": len(cells),
            "fresh_cover_stream_sha256": sha(canon(cells)),
            "fresh_cover_maximum": pair(maximum),
            "y": report_bounds(y),
            "radius": report_bounds(radius),
            "tail_margin_ratio": report_bounds(ball(tail / margin)),
            "records": records,
            "passes": sum(r["pass"] for r in records),
            "full_parent_rectangle_matched": matched,
            "parent_displacement_radius_ratio": report_bounds(
                ball(displacement / radius_lower)
            ),
            "scope": "Independent reflected formula, full fresh cover and direct-power remainder; same FLINT special-function implementation; fixed panel point.",
        }
        result["payload_sha256"] = sha(canon(result))
        return result
    finally:
        ctx.prec = oldprec


PREREG = "0cc801421768e3e42ebf0f1c7960081707e52968"
LINEAGE = "f77477c061e0e9e5ce340ee810254ddd50fad32f"
PREPARATION_PINS = [
    {
        "commit": PREREG,
        "path": "research/exploratory/XI_JOINT_POLYNOMIAL_PANEL_TRANSPORT.md",
        "git_blob": "38764a517090590019ab0cb7de6f0f298e822f6f",
        "sha256_lf": "d5eff0088dd3961a7043d5ebb712e18f3d60a11c02814ddd161213042f261957",
    },
    {
        "commit": LINEAGE,
        "path": "research/exploratory/XI_JOINT_POLYNOMIAL_INDEPENDENT_REVIEW_96543552.md",
        "git_blob": "f306b92a2d62c0507f0ab315cd7a68b6007a600c",
        "sha256_lf": "cbee150228cbfd0c610baff505ab7dfd701f360fb623440b6de3656a71c0f571",
    },
    {
        "commit": LINEAGE,
        "path": "research/exploratory/xi_joint_polynomial_independent_review.py",
        "git_blob": "0c0b45293e69a9d25b94d06dfc1ccdd9e89b0e90",
        "sha256_lf": "77bd6409282113b193aead5cab9b308e40aceb0e4dc2a6c5dc4ae5ca5d8fdd0a",
    },
]


def build():
    source_evidence = provenance()
    for pin in PREPARATION_PINS:
        raw = source(pin["commit"], pin["path"])
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        need(
            blob == pin["git_blob"]
            and sha(raw.replace(b"\r\n", b"\n")) == pin["sha256_lf"],
            "preparation design/method pin",
        )
    rows = parent()
    records = []
    for row in rows:
        try:
            record = compute(row)
            record["transport_certified"] = record["passes"] == ARCS
            record["matched_transport"] = (
                record["transport_certified"]
                and record["full_parent_rectangle_matched"]
            )
            record["status"] = (
                "MATCHED" if record["matched_transport"] else "UNRESOLVED"
            )
        except ValueError as exc:
            record = {
                "point_index": row["index"],
                "status": "UNRESOLVED_GUARD",
                "reason": str(exc),
                "transport_certified": False,
                "matched_transport": False,
                "records": [
                    {"index": j, "pass": None, "status": "NOT_EVALUATED_DUE_GUARD"}
                    for j in range(ARCS)
                ],
            }
        record.pop("payload_sha256", None)
        record["payload_sha256"] = sha(canon(record))
        records.append(record)
        print(
            "independent point",
            row["index"],
            record["status"],
            record.get("passes", 0),
            file=__import__("sys").stderr,
            flush=True,
        )
    matches = [r["point_index"] for r in records if r["matched_transport"]]
    result = {
        "schema": "xi-joint-polynomial-panel-independent-reflected-review-v1",
        "source_evidence": source_evidence,
        "preparation_pins": PREPARATION_PINS,
        "extension_design": PREREG,
        "method_lineage_review": LINEAGE,
        "precision": PREC,
        "terms": N,
        "arcs_per_point": ARCS,
        "ratio": [1, 2],
        "outer_radius": pair(R),
        "critical_radius": pair(EPS),
        "independent_fresh_cover": "all256 cells per point at1024bits; original rectangle",
        "rounding": "directed FLINT acceptance; exact rational comparisons; display ratios outward to2^-64",
        "selection": "known point19 control; all25 others fixed before extension arithmetic; disclosed author8-success result is not blinded",
        "independent_calculation_inputs": "accepted JP/QT and frozen design only; no extension values or helper code",
        "matched_indices": matches,
        "known_control_matched": 19 in matches,
        "other25_matched": len([i for i in matches if i != 19]),
        "records": records,
        "scope": "finite no-author-import computation; same FLINT and disclosed root-review method lineage; no cofinal/RH/capture conclusion",
    }
    result["payload_sha256"] = sha(canon(result))
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.check:
        need(
            canon(result) == canon(json.loads(OUT.read_bytes())),
            "independent panel replay",
        )
        print("PASS independent all26 reflected-Xi/direct-power replay")
    elif args.summary:
        print(
            json.dumps(
                {k: v for k, v in result.items() if k != "records"}, sort_keys=True
            )
        )
    else:
        print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
