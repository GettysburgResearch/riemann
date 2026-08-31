"""Preregistered26-point actual-Xi joint-polynomial transport panel."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import xi_joint_polynomial_point_transport as jp

qt, ha, oa = jp.qt, jp.ha, jp.oa
acb, arb = jp.acb, jp.arb
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
STEM = "xi_joint_polynomial_panel_transport"
NOTE = HERE / "XI_JOINT_POLYNOMIAL_PANEL_TRANSPORT.md"
MANIFEST = HERE / (STEM + ".sources.json")
FIXTURE = HERE / (STEM + ".json")
TEST = ROOT / "tests" / ("test_" + STEM + ".py")
BASE = "96543552b5bc5976d96c35123bfb82e609a27972"
PREREG = "0cc801421768e3e42ebf0f1c7960081707e52968"
BINDINGS = [
    {
        "commit": "96543552b5bc5976d96c35123bfb82e609a27972",
        "path": "research/exploratory/XI_JOINT_POLYNOMIAL_POINT_TRANSPORT.md",
        "git_blob": "a0409d4682177e805f96ca623db0c44d31d76bd4",
        "sha256_lf": "487411b452c5082ec086ec1a2edbc6571e83a179c9c80a90ca31d4b1a4e1d7b7",
    },
    {
        "commit": "96543552b5bc5976d96c35123bfb82e609a27972",
        "path": "research/exploratory/xi_joint_polynomial_point_transport.py",
        "git_blob": "1b12d3c95fee0c6cef2480453d52bc7a1b7f563e",
        "sha256_lf": "b09a81ec048ff42fbd4334692741204992ce59d2add020b99935eb2534cd4167",
    },
    {
        "commit": "96543552b5bc5976d96c35123bfb82e609a27972",
        "path": "research/exploratory/xi_joint_polynomial_point_transport.json",
        "git_blob": "67982e66d9c8cf097b917a9e44a3a41623c61d32",
        "sha256_lf": "aef1379325c101b31bdad40940066daa1fdae3a37496008a28fb22fe31cdc735",
    },
    {
        "commit": "96543552b5bc5976d96c35123bfb82e609a27972",
        "path": "research/exploratory/xi_joint_polynomial_point_transport.sources.json",
        "git_blob": "4bad9c73cc4301bcae3b754a0ce386d04c56bc8b",
        "sha256_lf": "eeb969218c44ae573476522be185de7c500e29c35c5329b82660968826a1a649",
    },
    {
        "commit": "96543552b5bc5976d96c35123bfb82e609a27972",
        "path": "tests/test_xi_joint_polynomial_point_transport.py",
        "git_blob": "0b7148472d5faf668e44815951a702440c132aaf",
        "sha256_lf": "e5799df7b3770e7fa1996c5e925537408b4ca5409fe90e61128ef131087e5979",
    },
    {
        "commit": "0cc801421768e3e42ebf0f1c7960081707e52968",
        "path": "research/exploratory/XI_JOINT_POLYNOMIAL_PANEL_TRANSPORT.md",
        "git_blob": "38764a517090590019ab0cb7de6f0f298e822f6f",
        "sha256_lf": "d5eff0088dd3961a7043d5ebb712e18f3d60a11c02814ddd161213042f261957",
    },
]
MAX_BYTES = 24_000_000
CONTRACT = {
    "selection": "fixed QT26; index19 known positive control,25 primary untried points",
    "panel": list(range(26)),
    "known_control": 19,
    "bits": 512,
    "signed_jet_terms": 40,
    "polynomial_terms": 32,
    "closed_arcs": 64,
    "ratio": [1, 2],
    "outer_radius": [7, 8],
    "primitive": "same literal Xi and calibrated lambda_(64); full unknown-t interval; algebraic f6(t)=0",
    "bounds": "same JP Horner joint-polynomial/Cauchy bound; inherited per-node QT512 complete256-cell cover",
    "evidence": "40 real coefficient intervals plus fullsignedjet hash;64 exact error/margin decisions plus complete uncompressed arc hash; fresh allprimitive replay",
    "failure": "all failedguards/unresolvedarcs/unmatchedrectangles retained;64not-evaluated slots after guardfailure",
    "arithmetic_class": "MIXED",
    "arithmetic_components": [
        "DIRECTED_BALL_ENCLOSURES",
        "EXACT_RATIONAL",
        "CERTIFIED_INTEGER_COVERAGE",
    ],
    "rounding": "unchanged pinned FLINT outward balls and exact rational endpoint comparisons",
    "domain": "unchanged HA 20<x<1100,-1<y<2; no parameter/radius/tier/degree/arc tuning",
    "source_quantifiers": "complete declared finite panel only; no innerness premise",
    "exclusions": "no independent zero census, cofinal transport, physical capture, RH or novelty",
    "caps": {
        "points": 26,
        "jet": 40,
        "arcs": 64,
        "json_bytes": MAX_BYTES,
        "source_bytes": MAX_BYTES,
        "nodes": 800000,
        "depth": 24,
        "container": 8000,
        "string": 4096,
        "integer_bits": 4096,
    },
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def validate_tree(v, depth=0, count=None):
    count = [0] if count is None else count
    count[0] += 1
    require(depth <= 24 and count[0] <= 800000, "JSON depth/node cap")
    if v is None or type(v) is bool:
        return
    if type(v) is int:
        require(v.bit_length() <= 4096, "integer cap")
        return
    if type(v) is str:
        require(v.isascii() and len(v) <= 4096, "string cap")
        return
    require(type(v) in (list, dict) and len(v) <= 8000, "container type/cap")
    if type(v) is dict:
        require(
            all(type(k) is str and k.isascii() and len(k) <= 4096 for k in v),
            "JSON keys",
        )
        values = v.values()
    else:
        values = v
    for child in values:
        validate_tree(child, depth + 1, count)


def canonical(v):
    validate_tree(v)
    raw = json.dumps(
        v, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode()
    require(len(raw) <= MAX_BYTES, "JSON byte cap")
    return raw


def decode(raw):
    require(type(raw) is bytes and len(raw) <= MAX_BYTES, "JSON input type/cap")

    def reject(_):
        raise ValueError("noninteger JSON primitive")

    value = json.loads(
        raw,
        object_pairs_hook=oa.pairs_unique,
        parse_float=reject,
        parse_constant=reject,
    )
    validate_tree(value)
    return value


def manifest():
    return {
        "schema": STEM + "-sources-v1",
        "authoring_base": BASE,
        "preregistration_commit": PREREG,
        "frozen_sources": BINDINGS,
        "runtime": oa.RUNTIME,
        "contract": CONTRACT,
        "documentation": jp.manifest()["documentation"],
    }


def authenticate():
    require(
        canonical(decode(MANIFEST.read_bytes())) == canonical(manifest()),
        "manifest mismatch",
    )
    jp.authenticate()
    for index, binding in enumerate(BINDINGS):
        raw = oa.read_source(binding)
        require(len(raw) <= MAX_BYTES, "source cap")
        sha1 = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        require(
            sha1 == binding["git_blob"]
            and oa.digest(jp.lf(raw)) == binding["sha256_lf"],
            "source mismatch",
        )
        if index < 5:
            require(
                oa.digest(jp.lf((ROOT / binding["path"]).read_bytes()))
                == binding["sha256_lf"],
                "local JP drift",
            )


def parents():
    source = qt.decode(oa.read_source(jp.BINDINGS[2]))
    parent = qt.parent_panel()
    require(len(source["records"]) == len(parent) == 26, "complete QT/HA26")
    return source["records"], parent


def point(index, row, parent):
    require(
        type(index) is int and 0 <= index < 26 and row["index"] == index,
        "fixed point index",
    )
    require(
        oa.digest(qt.canonical(parent)) == row["HA_record_sha256"], "HA source binding"
    )
    critical = row["critical"]
    require(
        critical["simple_real_critical"] is True
        and oa.unpair(critical["radius"]) == qt.EPS,
        "critical inheritance",
    )
    tier = next(v for v in row["jet_tiers"] if v["bits"] == 512)
    cover = tier["outer_scalar_bound"]["fixed_cover"]
    require(
        cover["status"] == "PASS"
        and cover["finite_cells"] == cover["cells_attempted"] == 256
        and cover["failed_cells"] == [],
        "full inherited cover",
    )
    result = {
        "index": index,
        "selection": "KNOWN_CONTROL" if index == 19 else "PRIMARY_UNTRIED",
        "QT_record_sha256": oa.digest(qt.canonical(row)),
        "HA_record_sha256": row["HA_record_sha256"],
        "critical": critical,
        "cover": cover,
        "HA_center": row["HA_center"],
        "HA_radius": row["HA_radius"],
        "transport_certified": False,
        "parent_matched": False,
        "matched_transport_certified": False,
        "status": "UNRESOLVED",
        "arcs": [
            {"index": j, "status": "NOT_EVALUATED_DUE_GUARD", "strict_pass": False}
            for j in range(64)
        ],
    }
    with ha.precision(512):
        try:
            center = oa.unpair(critical["center"])
            t = arb(oa.qarb(center), oa.qarb(qt.EPS))
            coeff = ha.xi_series(acb(t), 40)
            require(
                all(v.imag.contains(0) for v in coeff) and coeff[6].real.contains(0),
                "real critical jet",
            )
            result["T"] = oa.rbounds(t)
            result["real_coefficients_0_to39"] = [oa.rbounds(v.real) for v in coeff]
            result["full_signed_jet_sha256"] = oa.digest(
                jp.canonical([oa.cbounds(v) for v in coeff])
            )
            lam = ha.fixed_lambda()
            a, c = (
                (coeff[5] * math.factorial(5)).real,
                (coeff[7] * math.factorial(7)).real,
            )
            agreement = (
                oa.rbounds(t) == tier["T"]
                and oa.rbounds(a) == tier["a"]
                and oa.rbounds(c) == tier["c"]
                and oa.rbounds(lam) == tier["lambda"]
                and [oa.pair(oa.endpoint(v.abs_upper())) for v in coeff[8:]]
                == tier["coefficient_modulus_upper_8_to39"]
            )
            if not agreement:
                raise RuntimeError("fresh source jet disagrees with frozen QT metadata")
            result.update(
                a=oa.rbounds(a), c=oa.rbounds(c), lambda_calibrated=oa.rbounds(lam)
            )
            require(a * c < 0, "opposite critical signs")
            q = -a / (lam * c)
            result["q"] = oa.rbounds(q)
            require(q > 0 and 2 * q < lam, "quadratic discriminant")
            d = (lam * lam - 2 * lam * q).sqrt()
            y = 2 * lam * q / (lam + d)
            radius = oa.qarb(jp.RATIO) * y
            result.update(d=oa.rbounds(d), y=oa.rbounds(y), radius=oa.rbounds(radius))
            require(0 < radius < y and radius < 2 * d, "quadratic radius")
            margin = qt.scalar_lower(abs(c) * radius * (d - radius / 2))
            require(margin > 0, "positive margin")
            h = qt.scalar_upper(y + radius)
            result.update(h_upper=oa.pair(h), margin_lower=oa.pair(margin))
            tail = jp.joint_tail(oa.unpair(cover["upper"]), h, lam)
            result["tail_upper"] = oa.pair(tail)
            joint = jp.joint_coefficients(coeff, lam)
            complete, compact = [], []
            for j in range(64):
                item = {
                    "index": j,
                    "pi_interval": [oa.pair(jp.Q(j, 32)), oa.pair(jp.Q(j + 1, 32))],
                }
                try:
                    theta = jp.arc_angle(j)
                    z = acb(0, y) + radius * acb(theta.cos(), theta.sin())
                    polynomial = jp.horner(joint, z)
                    upper = oa.endpoint(polynomial.abs_upper())
                    error = upper + tail
                    item.update(
                        angle=oa.rbounds(theta),
                        w=oa.cbounds(z),
                        polynomial=oa.cbounds(polynomial),
                        polynomial_upper=oa.pair(upper),
                        tail_upper=oa.pair(tail),
                        error_upper=oa.pair(error),
                        margin_lower=oa.pair(margin),
                        error_over_margin=oa.pair(error / margin),
                        strict_pass=error < margin,
                        status="PASS" if error < margin else "UNRESOLVED",
                    )
                    compact.append(
                        {
                            "index": j,
                            "error_upper": oa.pair(error),
                            "strict_pass": error < margin,
                            "status": item["status"],
                        }
                    )
                except (ValueError, ZeroDivisionError, OverflowError) as exc:
                    item.update(strict_pass=False, status="UNRESOLVED", reason=str(exc))
                    compact.append(
                        {
                            "index": j,
                            "strict_pass": False,
                            "status": "UNRESOLVED",
                            "reason": str(exc),
                        }
                    )
                complete.append(item)
            result["arcs"] = compact
            result["full_arc_stream_sha256"] = oa.digest(jp.canonical(complete))
            distance = oa.endpoint(
                (qt.parent_rectangle(parent) - acb(t, y)).abs_upper()
            )
            rlower = qt.scalar_lower(radius)
            result.update(
                parent_displacement_upper=oa.pair(distance),
                radius_lower=oa.pair(rlower),
                parent_matched=distance < rlower,
                transport_certified=all(v["strict_pass"] for v in compact),
            )
            matched = result["parent_matched"] and result["transport_certified"]
            result.update(
                matched_transport_certified=matched,
                status="PASS" if matched else "UNRESOLVED",
            )
        except (ValueError, ZeroDivisionError, OverflowError) as exc:
            result["guard_failure"] = str(exc)
    return result


def summary(records):
    require(
        len(records) == 26 and [r["index"] for r in records] == list(range(26)),
        "complete ordered panel",
    )
    untried = [r for r in records if r["index"] != 19]
    return {
        "total_points": 26,
        "primary_untried_points": 25,
        "primary_matched_passes": sum(
            r["matched_transport_certified"] for r in untried
        ),
        "primary_unresolved": [
            r["index"] for r in untried if not r["matched_transport_certified"]
        ],
        "known_control_index": 19,
        "known_control_matched": records[19]["matched_transport_certified"],
        "total_matched_passes": sum(r["matched_transport_certified"] for r in records),
        "evaluated_arc_count": sum(
            v["status"] != "NOT_EVALUATED_DUE_GUARD" for r in records for v in r["arcs"]
        ),
        "passing_arc_count": sum(v["strict_pass"] for r in records for v in r["arcs"]),
        "guard_failures": [r["index"] for r in records if "guard_failure" in r],
    }


def build_report():
    authenticate()
    rows, parent = parents()
    records = [point(i, row, parent[i]) for i, row in enumerate(rows)]
    # The old known control is not counted as a heldout discovery.
    control = jp.decode(oa.read_source(BINDINGS[2]))["record"]
    require(
        records[19]["full_signed_jet_sha256"]
        == oa.digest(jp.canonical(control["fresh_signed_Xi_coefficients_0_to39"])),
        "known-control signed jet",
    )
    require(
        records[19]["full_arc_stream_sha256"]
        == oa.digest(jp.canonical(control["arcs"])),
        "known-control full64 stream",
    )
    value = {
        "schema": STEM + "-v1",
        "contract": CONTRACT,
        "frozen_sources": BINDINGS,
        "runtime": oa.RUNTIME,
        "records": records,
        "summary": summary(records),
        "inherited_exact_controls": jp.exact_controls(),
        "artifacts": {
            p.relative_to(ROOT).as_posix(): oa.digest(jp.lf(p.read_bytes()))
            for p in (NOTE, Path(__file__), MANIFEST, TEST)
        },
    }
    return {**value, "payload_sha256": oa.digest(canonical(value))}


def check_report(value):
    validate_tree(value)
    require(type(value) is dict and "payload_sha256" in value, "report shape")
    unsigned = {k: v for k, v in value.items() if k != "payload_sha256"}
    require(value["payload_sha256"] == oa.digest(canonical(unsigned)), "payload seal")
    require(
        canonical(value) == canonical(build_report()),
        "fresh full26 primitive reconstruction",
    )
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true")
    group.add_argument("--emit", action="store_true")
    group.add_argument("--emit-sources", action="store_true")
    args = parser.parse_args()
    if args.emit_sources:
        value = manifest()
    elif args.emit:
        value = build_report()
    else:
        check_report(decode(FIXTURE.read_bytes()))
        print("PASS fresh fixed26 joint-polynomial panel;25untried plus knowncontrol")
        print("fixture_sha256_lf=" + oa.digest(jp.lf(FIXTURE.read_bytes())))
        return
    print(json.dumps(value, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
