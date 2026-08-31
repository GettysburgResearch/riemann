"""One selected-point joint-polynomial actual-Xi transport certificate."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction as Q
from pathlib import Path

import xi_quadratic_critical_transport as qt
from flint import acb, arb, ctx

ha, oa = qt.ha, qt.oa
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
STEM = "xi_joint_polynomial_point_transport"
NOTE = HERE / "XI_JOINT_POLYNOMIAL_POINT_TRANSPORT.md"
MANIFEST = HERE / (STEM + ".sources.json")
FIXTURE = HERE / (STEM + ".json")
TEST = ROOT / "tests" / ("test_" + STEM + ".py")
BASE = "530732c5fd7f50364381f8af50e97ce809b674c5"
PREREG = "689a93971cdd741a2b154f9506672667aa1a32dc"
CORRECTION = "f8003a2569ba8cd9c62516d6f72aa8dfca9ce7b4"
NODE, BITS, TERMS, ARCS = 19, 512, 32, 64
RATIO, OUTER = Q(1, 2), Q(7, 8)
MAX_BYTES, MAX_SOURCE_BYTES = 2_000_000, 24_000_000
BINDINGS = [
    {
        "commit": "530732c5fd7f50364381f8af50e97ce809b674c5",
        "path": "research/exploratory/XI_QUADRATIC_CRITICAL_TRANSPORT.md",
        "git_blob": "cb634e9ac1e5ddbdffad01286a0b37ca958ac92b",
        "sha256_lf": "b9e7cf4911688d81c44ec9d871104e063c7bf46f574d86b479c6d912559d7269",
    },
    {
        "commit": "530732c5fd7f50364381f8af50e97ce809b674c5",
        "path": "research/exploratory/xi_quadratic_critical_transport.py",
        "git_blob": "a5e48dea3a25e1ff7419b2f6e2cfeef3de230185",
        "sha256_lf": "28033a330ade30e0079f6e24cd0f4b07e9de9ba70438f92c88fe5c0f7fe8c373",
    },
    {
        "commit": "530732c5fd7f50364381f8af50e97ce809b674c5",
        "path": "research/exploratory/xi_quadratic_critical_transport.json",
        "git_blob": "322281110f34af24575be29aed32acfd25657959",
        "sha256_lf": "45e9d81f5cfe22662ad9e07b9a994796b3c3b18743ae74c8cbd3ce095f3a4cce",
    },
    {
        "commit": "530732c5fd7f50364381f8af50e97ce809b674c5",
        "path": "research/exploratory/xi_quadratic_critical_transport.sources.json",
        "git_blob": "58bd03b1d15ce4d2eb91addb4c209a0f43fab80c",
        "sha256_lf": "66aa6f3d483bc638eed43315592c3cc5f3f8ef2baa9d9518e2fa0de3e685d757",
    },
    {
        "commit": "530732c5fd7f50364381f8af50e97ce809b674c5",
        "path": "tests/test_xi_quadratic_critical_transport.py",
        "git_blob": "cde20699d7b3894bf40db419b2d90a3d93459751",
        "sha256_lf": "d5493e8c31d53d66fdb00f35dfa1198b173513e23b2bfd3bdcb2d39d80423749",
    },
    {
        "commit": "689a93971cdd741a2b154f9506672667aa1a32dc",
        "path": "research/exploratory/XI_JOINT_POLYNOMIAL_POINT_TRANSPORT.md",
        "git_blob": "7dede48e26e34e79c123ab6741f11644273b8f3d",
        "sha256_lf": "2cd0cad4228f573be998641d090264b6a9cdddef2870832e523b685c9920aa28",
    },
    {
        "commit": "f8003a2569ba8cd9c62516d6f72aa8dfca9ce7b4",
        "path": "research/exploratory/XI_JOINT_POLYNOMIAL_POINT_TRANSPORT.md",
        "git_blob": "40e1b5ed858ec838667f2dd68764a89a0d781535",
        "sha256_lf": "b4df49fb751288edbb833753a76724be42619f77501c67f40f5e3f0ed3d85908",
    },
    {
        "commit": "a99a357b96abf535af79a20d5e1948aed6bd3da7",
        "path": "research/exploratory/XI_QUADRATIC_CRITICAL_TRANSPORT_AUDIT_530732C5.md",
        "git_blob": "61ff29d0365a1b856ec9fa873082569db930f8e8",
        "sha256_lf": "faac44110eb02985dd647151df7716836d1e98229447b488aa7fd9e3f47d1082",
    },
]
CONTRACT = {
    "primitive": "literal unrescaled Xi(1/2+iz), g=f5, fixed calibrated lambda_(64)",
    "selection": "post-QT/post-joint-M3 selected known node19; not a blind heldout point",
    "panel": {
        "node_index": NODE,
        "bits": BITS,
        "ratio": [1, 2],
        "terms": TERMS,
        "arcs": ARCS,
    },
    "jet": "fresh signed40-term actual-Xi jet over FULL inherited real-critical interval",
    "source_equation": "f6(t)=0 canceled algebraically; real symmetry permits projection to real coefficient enclosures",
    "cover": "inherit authenticated QT512-bit complete256-cell cover at R7/8; no fresh outer native calls",
    "contour": "64 equal CLOSED arcs, outward sin/cos and complex Horner; retain every failure",
    "tail": "joint f5/f6 Cauchy tails from n32; no separate-M3 triangle estimate",
    "matching": "FULL inherited HA rectangle inside disc for every t/y/r allowed by their enclosures",
    "arithmetic_class": "MIXED",
    "arithmetic_components": [
        "DIRECTED_BALL_ENCLOSURES",
        "EXACT_RATIONAL",
        "CERTIFIED_INTEGER_COVERAGE",
    ],
    "rounding": "pinned FLINT outward balls; exact rational lower/upper endpoints; strict rational comparisons",
    "domain": "unchanged HA 20<Re z<1100,-1<Im z<2; local requested series cap40",
    "source_quantifiers": "one selected local actual-source companion root; QT critical/cover certificates inherited",
    "no_innerness_premise": True,
    "exclusions": "no new zero census, new point, parameter tuning, cofinal theorem, physical capture, RH, novelty or priority",
    "caps": {
        "jet": 40,
        "arcs": 64,
        "terms": 32,
        "json_bytes": MAX_BYTES,
        "source_bytes": MAX_SOURCE_BYTES,
        "nodes": 60000,
        "depth": 24,
        "container": 4096,
        "string": 4096,
        "integer_bits": 4096,
    },
    "trust": "same pinned FLINT special functions; not a second implementation or formal verification",
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def validate_tree(value, depth=0, visits=None):
    visits = [0] if visits is None else visits
    visits[0] += 1
    require(depth <= 24 and visits[0] <= 60000, "JSON depth/node cap")
    if value is None or type(value) is bool:
        return
    if type(value) is int:
        require(value.bit_length() <= 4096, "JSON integer cap")
        return
    if type(value) is str:
        require(value.isascii() and len(value) <= 4096, "JSON string type/cap")
        return
    require(
        type(value) in (list, dict) and len(value) <= 4096, "JSON container type/cap"
    )
    if type(value) is dict:
        require(
            all(type(k) is str and k.isascii() and len(k) <= 4096 for k in value),
            "JSON keys",
        )
        children = value.values()
    else:
        children = value
    for child in children:
        validate_tree(child, depth + 1, visits)


def canonical(value):
    validate_tree(value)
    raw = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode()
    require(len(raw) <= MAX_BYTES, "canonical byte cap")
    return raw


def decode(raw):
    require(type(raw) is bytes and len(raw) <= MAX_BYTES, "input byte type/cap")

    def reject(_):
        raise ValueError("noninteger numeric primitive")

    value = json.loads(
        raw,
        object_pairs_hook=oa.pairs_unique,
        parse_float=reject,
        parse_constant=reject,
    )
    validate_tree(value)
    return value


def lf(raw):
    require(type(raw) is bytes and len(raw) <= MAX_SOURCE_BYTES, "source byte cap")
    return ha.lf(raw)


def manifest():
    return {
        "schema": STEM + "-sources-v1",
        "authoring_base": BASE,
        "preregistration": PREREG,
        "preregistration_correction": CORRECTION,
        "frozen_sources": BINDINGS,
        "runtime": oa.RUNTIME,
        "contract": CONTRACT,
        "documentation": ha.manifest()["documentation"],
    }


def authenticate():
    require(
        canonical(decode(MANIFEST.read_bytes())) == canonical(manifest()),
        "manifest mismatch",
    )
    qt.authenticate()
    for index, binding in enumerate(BINDINGS):
        raw = oa.read_source(binding)
        require(len(raw) <= MAX_SOURCE_BYTES, "frozen source cap")
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        require(
            blob == binding["git_blob"] and oa.digest(lf(raw)) == binding["sha256_lf"],
            "frozen source mismatch",
        )
        if index < 5:
            require(
                oa.digest(lf((ROOT / binding["path"]).read_bytes()))
                == binding["sha256_lf"],
                "local QT source drift",
            )


def inherit():
    source = qt.decode(oa.read_source(BINDINGS[2]))
    require(len(source["records"]) == 26, "QT26 panel")
    row = source["records"][NODE]
    require(type(row["index"]) is int and row["index"] == NODE, "selected fixed node")
    critical = row["critical"]
    require(
        critical["simple_real_critical"] is True, "inherited simple real critical point"
    )
    require(oa.unpair(critical["radius"]) == qt.EPS, "inherited critical radius")
    tier = next(item for item in row["jet_tiers"] if item["bits"] == BITS)
    cover = tier["outer_scalar_bound"]["fixed_cover"]
    require(
        cover["status"] == "PASS"
        and cover["finite_cells"] == 256
        and cover["cells_attempted"] == 256
        and cover["failed_cells"] == [],
        "complete inherited cover",
    )
    parent = qt.parent_panel()[NODE]
    require(
        oa.digest(qt.canonical(parent)) == row["HA_record_sha256"],
        "exact HA root binding",
    )
    return row, tier, cover, parent


def joint_coefficients(coeff, lam):
    require(type(coeff) is list and len(coeff) == 40, "fresh40 coefficients")
    require(
        type(lam) is arb and lam > 0 and ctx.prec == BITS,
        "fixed coefficient precision/lambda",
    )
    require(
        all(type(v) is acb and v.is_finite() and v.imag.contains(0) for v in coeff),
        "real source coefficients",
    )
    out = [acb(0), acb(0), -acb(0, 1) * lam * coeff[8].real * math.factorial(8) / 2]
    for n in range(3, TERMS):
        out.append(
            acb(coeff[n + 5].real * (math.factorial(n + 5) // math.factorial(n)))
            - acb(0, 1)
            * lam
            * coeff[n + 6].real
            * (math.factorial(n + 6) // math.factorial(n))
        )
    return out


def joint_tail(m, h, lam):
    require(
        type(m) is Q and type(h) is Q and m >= 0 and 0 <= h < OUTER,
        "joint Cauchy radius/bound",
    )
    require(
        type(lam) is arb and lam > 0 and ctx.prec == BITS, "joint tail precision/lambda"
    )
    outer = oa.qarb(OUTER)
    x = oa.qarb(h) / outer
    first = math.factorial(5) * math.comb(TERMS + 5, 5) / (outer**5 * (1 - x) ** 6)
    second = (
        lam * math.factorial(6) * math.comb(TERMS + 6, 6) / (outer**6 * (1 - x) ** 7)
    )
    return qt.scalar_upper(oa.qarb(m) * x**TERMS * (first + second))


def arc_angle(index):
    require(
        type(index) is int and 0 <= index < ARCS and ctx.prec == BITS,
        "fixed64 arc index/precision",
    )
    return arb.pi() * arb(oa.qarb(Q(2 * index + 1, ARCS)), oa.qarb(Q(1, ARCS)))


def horner(coeff, z):
    require(
        type(coeff) is list and len(coeff) == TERMS and type(z) is acb, "Horner32 input"
    )
    value = acb(0)
    for item in reversed(coeff):
        value = value * z + item
    return value


def selected_point():
    row, tier, cover, parent = inherit()
    center = oa.unpair(row["critical"]["center"])
    eps = oa.unpair(row["critical"]["radius"])
    with ha.precision(BITS):
        t = arb(oa.qarb(center), oa.qarb(eps))
        coeff = ha.xi_series(acb(t), 40)
        require(all(v.imag.contains(0) for v in coeff), "Schwarz-real jet")
        require(coeff[6].real.contains(0), "f6 critical interval consistency")
        lam = ha.fixed_lambda()
        a, c = (coeff[5] * math.factorial(5)).real, (coeff[7] * math.factorial(7)).real
        require(a * c < 0, "opposite critical signs")
        q = -a / (lam * c)
        require(q > 0 and 2 * q < lam, "quadratic discriminant")
        d = (lam * lam - 2 * lam * q).sqrt()
        y = 2 * lam * q / (lam + d)
        radius = oa.qarb(RATIO) * y
        require(0 < radius < y and radius < 2 * d, "positive upper-half-plane disc")
        require(
            oa.rbounds(t) == tier["T"]
            and oa.rbounds(a) == tier["a"]
            and oa.rbounds(c) == tier["c"]
            and oa.rbounds(lam) == tier["lambda"],
            "fresh inherited-jet agreement",
        )
        moduli = [oa.pair(oa.endpoint(v.abs_upper())) for v in coeff[8:]]
        require(
            moduli == tier["coefficient_modulus_upper_8_to39"],
            "fresh signed jet/modulus agreement",
        )
        model_margin = qt.scalar_lower(abs(c) * radius * (d - radius / 2))
        require(model_margin > 0, "positive model margin")
        h = qt.scalar_upper(y + radius)
        tail = joint_tail(oa.unpair(cover["upper"]), h, lam)
        joint = joint_coefficients(coeff, lam)
        arcs = []
        for index in range(ARCS):
            item = {
                "index": index,
                "pi_interval": [
                    oa.pair(Q(2 * index, ARCS)),
                    oa.pair(Q(2 * index + 2, ARCS)),
                ],
            }
            try:
                angle = arc_angle(index)
                z = acb(0, y) + radius * acb(angle.cos(), angle.sin())
                polynomial = horner(joint, z)
                polynomial_upper = oa.endpoint(polynomial.abs_upper())
                error = polynomial_upper + tail
                passes = error < model_margin
                item.update(
                    angle=oa.rbounds(angle),
                    w=oa.cbounds(z),
                    polynomial=oa.cbounds(polynomial),
                    polynomial_upper=oa.pair(polynomial_upper),
                    tail_upper=oa.pair(tail),
                    error_upper=oa.pair(error),
                    margin_lower=oa.pair(model_margin),
                    error_over_margin=oa.pair(error / model_margin),
                    strict_pass=passes,
                    status="PASS" if passes else "UNRESOLVED",
                )
            except (ValueError, ZeroDivisionError, OverflowError) as exc:
                item.update(status="UNRESOLVED", strict_pass=False, reason=str(exc))
            arcs.append(item)
        displacement = oa.endpoint(
            (qt.parent_rectangle(parent) - acb(t, y)).abs_upper()
        )
        radius_lower = qt.scalar_lower(radius)
        matched = displacement < radius_lower
        transport = all(item["strict_pass"] for item in arcs)
        return {
            "node_index": NODE,
            "bits": BITS,
            "box_center": row["box_center"],
            "QT_record_sha256": oa.digest(qt.canonical(row)),
            "HA_record_sha256": row["HA_record_sha256"],
            "inherited_critical": row["critical"],
            "inherited_cover": cover,
            "inherited_HA_center": row["HA_center"],
            "inherited_HA_radius": row["HA_radius"],
            "T": oa.rbounds(t),
            "fresh_signed_Xi_coefficients_0_to39": [oa.cbounds(v) for v in coeff],
            "fresh_joint_coefficients_0_to31": [oa.cbounds(v) for v in joint],
            "lambda": oa.rbounds(lam),
            "a": oa.rbounds(a),
            "c": oa.rbounds(c),
            "q": oa.rbounds(q),
            "d": oa.rbounds(d),
            "y": oa.rbounds(y),
            "radius": oa.rbounds(radius),
            "h_upper": oa.pair(h),
            "outer_radius": oa.pair(OUTER),
            "tail_upper": oa.pair(tail),
            "margin_lower": oa.pair(model_margin),
            "arcs": arcs,
            "parent_displacement_upper": oa.pair(displacement),
            "radius_lower": oa.pair(radius_lower),
            "parent_matched": matched,
            "transport_certified": transport,
            "matched_transport_certified": transport and matched,
            "status": "PASS" if transport and matched else "UNRESOLVED",
        }


def exact_controls():
    # Two independently organized rational-complex polynomial evaluations.
    def add(x, y):
        return x[0] + y[0], x[1] + y[1]

    def mul(x, y):
        return x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0]

    def power(z, n):
        v = Q(1), Q(0)
        for _ in range(n):
            v = mul(v, z)
        return v

    count = 0
    for family, lam in ((1, Q(2, 3)), (2, Q(7, 5))):
        v = [Q(((-1) ** j) * (family + j), (j + 1) ** 2) for j in range(37)]
        v[6] = Q(0)
        a, c = v[5] * math.factorial(5), v[7] * math.factorial(7)
        for z in (
            (Q(0), Q(0)),
            (Q(1, 7), Q(2, 9)),
            (Q(-2, 5), Q(1, 11)),
            (Q(3, 8), Q(-1, 6)),
        ):
            full = Q(0), Q(0)
            for j in range(5, 37):
                full = add(
                    full,
                    mul(
                        (v[j] * math.factorial(j) / math.factorial(j - 5), Q(0)),
                        power(z, j - 5),
                    ),
                )
            for j in range(6, 37):
                full = add(
                    full,
                    mul(
                        (Q(0), -lam * v[j] * math.factorial(j) / math.factorial(j - 6)),
                        power(z, j - 6),
                    ),
                )
            model = add(
                (a, Q(0)),
                add(mul((c / 2, Q(0)), power(z, 2)), mul((Q(0), -lam * c), z)),
            )
            direct = full[0] - model[0], full[1] - model[1]
            remainder = Q(0), Q(0)
            for n in reversed(range(2, TERMS)):
                real = (
                    Q(0)
                    if n == 2
                    else v[n + 5] * math.factorial(n + 5) / math.factorial(n)
                )
                imag = (
                    -lam
                    * (v[n + 6] if n + 6 < len(v) else Q(0))
                    * math.factorial(n + 6)
                    / math.factorial(n)
                )
                remainder = add(mul(remainder, z), (real, imag))
            remainder = mul(remainder, power(z, 2))
            require(
                direct == remainder, "independent exact polynomial remainder identity"
            )
            count += 1
    inequalities = 0
    for order in (5, 6):
        for j in range(65):
            require(
                math.comb(TERMS + j + order, order)
                <= math.comb(TERMS + order, order) * math.comb(j + order, order),
                "binomial tail control",
            )
            inequalities += 1
    return {
        "exact_polynomial_evaluation_equalities": count,
        "binomial_inequalities": inequalities,
        "scope": "finite controls of the proved algebra; not replacement for the analytic infinite-tail proof",
    }


def build_report():
    authenticate()
    record = selected_point()
    value = {
        "schema": STEM + "-v1",
        "contract": CONTRACT,
        "frozen_sources": BINDINGS,
        "runtime": oa.RUNTIME,
        "record": record,
        "exact_controls": exact_controls(),
        "summary": {
            "attempted_arcs": len(record["arcs"]),
            "passing_arcs": sum(item["strict_pass"] for item in record["arcs"]),
            "failed_arcs": [
                item["index"] for item in record["arcs"] if not item["strict_pass"]
            ],
            "transport_certified": record["transport_certified"],
            "parent_matched": record["parent_matched"],
            "matched_transport_certified": record["matched_transport_certified"],
            "status": record["status"],
        },
        "artifacts": {
            p.relative_to(ROOT).as_posix(): oa.digest(lf(p.read_bytes()))
            for p in (NOTE, Path(__file__), MANIFEST, TEST)
        },
    }
    return {**value, "payload_sha256": oa.digest(canonical(value))}


def check_report(value):
    validate_tree(value)
    require(type(value) is dict and "payload_sha256" in value, "report shape")
    unsigned = {k: v for k, v in value.items() if k != "payload_sha256"}
    require(
        type(value["payload_sha256"]) is str
        and value["payload_sha256"] == oa.digest(canonical(unsigned)),
        "payload seal",
    )
    require(
        canonical(value) == canonical(build_report()), "fresh primitive reconstruction"
    )
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--emit", action="store_true")
    mode.add_argument("--emit-sources", action="store_true")
    args = parser.parse_args()
    if args.emit_sources:
        value = manifest()
    elif args.emit:
        value = build_report()
    else:
        check_report(decode(FIXTURE.read_bytes()))
        print(
            "PASS fresh fixed node19 full64-arc joint-polynomial transport and HA matching"
        )
        print("fixture_sha256_lf=" + oa.digest(lf(FIXTURE.read_bytes())))
        return
    print(json.dumps(value, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
