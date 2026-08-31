"""Exact frozen JX inventory and independent rational checks; no author imports."""

import hashlib
import json
import math
from fractions import Fraction as Q
from pathlib import Path

import xi_joint_polynomial_panel_independent_review as independent

ROOT = Path(__file__).resolve().parents[2]
SCI = "2a27043c73cded47c2804ba50b9b1001145a0a82"
STEM = "research/exploratory/xi_joint_polynomial_panel_transport"
EXPECTED = "9e60f5d7dca44eca9323ec32500bc9b5dd10c8a83aae2fdcec07f0669428e94a"
PAYLOAD = "a6fc98cd4cfe8c9b526dd8b0e738ce84d6e2edd0cf45c8951f925743736a736a"


def need(ok, reason):
    if not ok:
        raise ValueError(reason)


def canon(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def load(raw):
    need(type(raw) is bytes and len(raw) <= 24_000_000, "JSON byte cap")

    def unique(items):
        out = {}
        for key, value in items:
            need(key not in out, "duplicate key")
            out[key] = value
        return out

    def reject(_):
        raise ValueError("noninteger JSON primitive")

    return json.loads(
        raw, object_pairs_hook=unique, parse_float=reject, parse_constant=reject
    )


def sealed(data):
    unsigned = {k: v for k, v in data.items() if k != "payload_sha256"}
    need(sha(canon(unsigned)) == data["payload_sha256"], "payload")


def q(pair):
    need(type(pair) is list and len(pair) == 2, "pair")
    a, b = pair
    need(type(a) is int and type(b) is int and b > 0, "strict pair")
    need(max(abs(a).bit_length(), b.bit_length()) <= 8192, "integer cap")
    out = Q(a, b)
    need([out.numerator, out.denominator] == pair, "canonical fraction")
    return out


def bounds(value):
    lo, hi = map(q, value)
    need(lo <= hi, "ordered bounds")
    return lo, hi


def maximum_difference(a, b):
    return max(abs(a[0] - b[1]), abs(a[1] - b[0]))


def main():
    paths = [
        "research/exploratory/XI_JOINT_POLYNOMIAL_PANEL_TRANSPORT.md",
        STEM + ".py",
        STEM + ".json",
        STEM + ".sources.json",
        "tests/test_xi_joint_polynomial_panel_transport.py",
    ]
    raw = {}
    for path in paths:
        value = independent.source(SCI, path)
        need(
            value.replace(b"\r\n", b"\n")
            == (ROOT / path).read_bytes().replace(b"\r\n", b"\n"),
            "frozen local science",
        )
        need(not any(b < 32 and b not in (9, 10, 13) for b in value), "control byte")
        raw[path] = value
    need(sha(raw[paths[2]].replace(b"\r\n", b"\n")) == EXPECTED, "fixture identity")
    data, manifest = load(raw[paths[2]]), load(raw[paths[3]])
    sealed(data)
    need(data["payload_sha256"] == PAYLOAD, "literal payload")
    need(len(data["artifacts"]) == 4, "four artifact seals")
    for path, expected in data["artifacts"].items():
        need(
            path in raw and sha(raw[path].replace(b"\r\n", b"\n")) == expected,
            "artifact seal",
        )
    for key in ("contract", "runtime", "frozen_sources"):
        need(canon(data[key]) == canon(manifest[key]), "manifest/fixture binding")
    queue, catalog = list(manifest["frozen_sources"]), {}
    while queue:
        pin = queue.pop(0)
        key = pin["commit"] + ":" + pin["path"]
        if key in catalog:
            need(catalog[key] == (pin["git_blob"], pin["sha256_lf"]), "conflicting pin")
            continue
        need(len(catalog) < 100, "source closure cap")
        value = independent.source(pin["commit"], pin["path"])
        blob = hashlib.sha1(
            b"blob " + str(len(value)).encode() + b"\0" + value
        ).hexdigest()
        need(
            blob == pin["git_blob"]
            and sha(value.replace(b"\r\n", b"\n")) == pin["sha256_lf"],
            "source pin",
        )
        catalog[key] = (blob, pin["sha256_lf"])
        if pin["path"].endswith(".sources.json"):
            queue.extend(load(value)["frozen_sources"])
    parent_raw = independent.source(independent.QT, independent.QT_PATH)
    need(sha(parent_raw.replace(b"\r\n", b"\n")) == independent.QT_SHA, "QT fixture")
    parent = load(parent_raw)
    sealed(parent)
    calc = load(independent.OUT.read_bytes())
    sealed(calc)
    need(
        calc["source_evidence"]["runtime"] == manifest["runtime"],
        "pinned runtime lineage",
    )
    need(len(data["records"]) == len(calc["records"]) == 26, "all26")
    passed, tail_checks, containment_checks = [], 0, 0
    for index, row in enumerate(data["records"]):
        need(
            type(row["index"]) is int and row["index"] == index, "ordered source index"
        )
        need(
            row["selection"] == ("KNOWN_CONTROL" if index == 19 else "PRIMARY_UNTRIED"),
            "selection",
        )
        source = parent["records"][index]
        tier = next(v for v in source["jet_tiers"] if v["bits"] == 512)
        need(row["QT_record_sha256"] == sha(canon(source)), "QT record")
        need(
            row["critical"] == source["critical"]
            and row["cover"] == tier["outer_scalar_bound"]["fixed_cover"],
            "critical/full-cover inheritance",
        )
        need(
            row["HA_center"] == source["HA_center"]
            and row["HA_radius"] == source["HA_radius"],
            "whole HA rectangle",
        )
        need(
            row["T"] == tier["T"]
            and row["a"] == tier["a"]
            and row["c"] == tier["c"]
            and row["lambda_calibrated"] == tier["lambda"],
            "literal jet metadata",
        )
        need(
            "guard_failure" not in row and len(row["arcs"]) == 64,
            "all guards/all slots",
        )
        for value in row["real_coefficients_0_to39"]:
            bounds(value)
        need(len(row["real_coefficients_0_to39"]) == 40, "complete real jet")
        radius = Q(7, 8)
        h = q(row["h_upper"])
        need(0 <= h < radius, "fixed outer radius")
        x = h / radius
        exact_tail = (
            q(row["cover"]["upper"])
            * x**32
            * (
                math.factorial(5) * math.comb(37, 5) / (radius**5 * (1 - x) ** 6)
                + bounds(row["lambda_calibrated"])[1]
                * math.factorial(6)
                * math.comb(38, 6)
                / (radius**6 * (1 - x) ** 7)
            )
        )
        need(q(row["tail_upper"]) >= exact_tail, "entire Cauchy tail rational audit")
        tail_checks += 1
        margin = q(row["margin_lower"])
        need(margin > 0, "positive margin")
        for j, arc in enumerate(row["arcs"]):
            need(type(arc["index"]) is int and arc["index"] == j, "all64 ordered")
            error = q(arc["error_upper"])
            need(error >= q(row["tail_upper"]), "nonnegative polynomial upper")
            need(
                type(arc["strict_pass"]) is bool
                and arc["strict_pass"] == (error < margin),
                "exact arc comparison",
            )
            need(
                arc["status"] == ("PASS" if error < margin else "UNRESOLVED"),
                "arc status",
            )
        all_arcs = all(a["strict_pass"] for a in row["arcs"])
        need(row["transport_certified"] is all_arcs, "whole-circle rule")
        hr = q(row["HA_radius"])
        cx, cy = map(q, row["HA_center"])
        dx = maximum_difference((cx - hr, cx + hr), bounds(row["T"]))
        dy = maximum_difference((cy - hr, cy + hr), bounds(row["y"]))
        distance = q(row["parent_displacement_upper"])
        need(distance**2 >= dx**2 + dy**2, "whole rectangle displacement upper")
        matched = distance < q(row["radius_lower"])
        need(row["parent_matched"] is matched, "strict matching")
        need(
            row["matched_transport_certified"] is (all_arcs and matched),
            "matched transport",
        )
        containment_checks += 1
        if all_arcs and matched:
            passed.append(index)
        own = calc["records"][index]
        need(
            own["critical_recertified"] is True
            and own["fresh_cover_cells"] == 256
            and own["fresh_reflected_coefficients"] == 40,
            "independent fresh primitive coverage",
        )
        need(
            own["matched_transport"] == (all_arcs and matched),
            "independent matched set agrees",
        )
    control = load(
        independent.source(
            independent.SCIENCE,
            "research/exploratory/xi_joint_polynomial_point_transport.json",
        )
    )["record"]
    known = data["records"][19]
    need(
        known["full_signed_jet_sha256"]
        == sha(canon(control["fresh_signed_Xi_coefficients_0_to39"])),
        "known full signed jet",
    )
    need(
        known["full_arc_stream_sha256"] == sha(canon(control["arcs"])),
        "known full arc stream",
    )
    need(passed == [17, 18, 19, 20, 21, 23, 24, 25], "complete protected matched set")
    need(
        sum(a["strict_pass"] for row in data["records"] for a in row["arcs"]) == 650,
        "all650 author arcs",
    )
    print(
        json.dumps(
            {
                "science": SCI,
                "direct_bindings": len(manifest["frozen_sources"]),
                "transitive_versions": len(catalog),
                "source_catalog_sha256": sha(canon(catalog)),
                "artifacts": 4,
                "exact_arc_comparisons": 1664,
                "rational_tail_checks": tail_checks,
                "whole_rectangle_checks": containment_checks,
                "matched_indices": passed,
                "independent_matched_indices": calc["matched_indices"],
                "independent_arc_passes": sum(r["passes"] for r in calc["records"]),
                "fixture_sha256_lf": EXPECTED,
                "payload_sha256": PAYLOAD,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
