"""Independent QR review: no author-code imports; shared pinned FLINT backend."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
from fractions import Fraction as Q
from pathlib import Path

from flint import acb, acb_series, arb, ctx

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
SCIENCE = "21936f22246a12ab0b4e8bd706154b861b56b585"
PARENT = "530732c5fd7f50364381f8af50e97ce809b674c5"
STEM = "xi_all_radius_transport_obstruction"
FIXTURE_SHA = "806c4c0554af651c0fdd6a97a92bbb2f4cff5c16b86d8a2eef56c0372bc517d2"
OUT = HERE / "xi_all_radius_independent_audit_21936f22.json"
PATHS = [
    "research/exploratory/" + STEM.upper() + ".md",
    "research/exploratory/" + STEM + ".py",
    "research/exploratory/" + STEM + ".json",
    "research/exploratory/" + STEM + ".sources.json",
    "tests/test_" + STEM + ".py",
]


def need(ok, message):
    if not ok:
        raise ValueError(message)


def canon(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def lf(data):
    return data.replace(b"\r\n", b"\n")


def git(commit, path):
    raw = subprocess.check_output(
        ["git", "--no-replace-objects", "show", commit + ":" + path], cwd=ROOT
    )
    need(len(raw) <= 24000000, "bounded source")
    return raw


def pair(value):
    need(type(value) is list and len(value) == 2, "pair")
    n, d = value
    need(type(n) is int and type(d) is int and d > 0, "strict rational")
    need(max(abs(n).bit_length(), d.bit_length()) <= 4096, "rational cap")
    q = Q(n, d)
    need([q.numerator, q.denominator] == value, "reduced rational")
    return q


def interval(value):
    need(type(value) is list and len(value) == 2, "interval")
    a, b = map(pair, value)
    need(a <= b, "ordered interval")
    return a, b


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def neg(a):
    return -a[1], -a[0]


def mul(a, b):
    v = [x * y for x in a for y in b]
    return min(v), max(v)


def scale(a, q):
    return mul(a, (q, q))


def div(a, b):
    need(b[0] * b[1] > 0, "division avoids zero")
    return mul(a, (1 / b[1], 1 / b[0]))


def absolute(a):
    return (Q(0) if a[0] <= 0 <= a[1] else min(map(abs, a)), max(map(abs, a)))


def sqrt_interval(a):
    need(a[0] > 0, "positive discriminant")
    scale = 1 << 384
    lo = math.isqrt(a[0].numerator * scale**2 // a[0].denominator)
    hi = math.isqrt(a[1].numerator * scale**2 // a[1].denominator)
    hi += Q(hi, scale) ** 2 < a[1]
    return Q(lo, scale), Q(hi, scale)


def comparison(a, c, third, lam):
    # Eliminate q and rationalized y: d^2=lambda^2+2a/c;
    # B=3d^2/[(lambda^2-d^2)(4lambda-d)].
    need(mul(a, c)[1] < 0 and lam[0] > 0, "opposite source signs")
    L2 = mul(lam, lam)
    dd = add(L2, scale(div(a, c), Q(2)))
    d = sqrt_interval(dd)
    y = add(lam, neg(d))
    need(y[0] > 0, "positive source y")
    denominator = mul(add(L2, neg(dd)), add(scale(lam, Q(4)), neg(d)))
    need(denominator[0] > 0, "positive alternative denominator")
    B = div(scale(dd, Q(3)), denominator)
    coarse = div(d, scale(mul(lam, y), Q(2)))
    m = div(absolute(third), absolute(c))
    return m[0] >= B[1], m[0] >= coarse[1]


def end(value):
    need(value.is_finite() and value.is_exact(), "finite exact endpoint")
    x = value.fmpq()
    return Q(int(x.numerator), int(x.denominator))


def bounds(value):
    return end(value.lower()), end(value.upper())


def ball(q):
    return arb(q.numerator) / arb(q.denominator)


def reflected_xi(z):
    # Direct source formula xi_R(1-(1/2+iz)), not HA/QT/QR code.
    old = ctx.cap
    ctx.cap = 9
    try:
        w = acb_series([acb(arb(1) / 2) - acb(0, 1) * z, acb(0, -1)])
        v = w * (w - 1) / 2 * (-w * arb.pi().log() / 2).exp()
        v = v * (w / 2).gamma() * w.zeta()
        return [v[j] * math.factorial(j) for j in range(9)]
    finally:
        ctx.cap = old


def provenance():
    for path in PATHS:
        need(
            lf((ROOT / path).read_bytes()) == lf(git(SCIENCE, path)),
            "science unchanged",
        )
    raw = lf((HERE / (STEM + ".json")).read_bytes())
    need(sha(raw) == FIXTURE_SHA, "frozen fixture")
    report = json.loads(raw)
    unsigned = {k: v for k, v in report.items() if k != "payload_sha256"}
    need(sha(canon(unsigned)) == report["payload_sha256"], "payload")
    for path, digest in report["artifacts"].items():
        need(sha(lf((ROOT / path).read_bytes())) == digest, "artifact")
    manifest = json.loads((HERE / (STEM + ".sources.json")).read_bytes())
    pending = list(manifest["frozen_sources"])
    seen = {}
    while pending:
        row = pending.pop()
        key = row["commit"] + ":" + row["path"]
        if key in seen:
            need(seen[key] == row["sha256_lf"], "consistent closure")
            continue
        raw = git(row["commit"], row["path"])
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        need(blob == row["git_blob"] and sha(lf(raw)) == row["sha256_lf"], "source pin")
        seen[key] = row["sha256_lf"]
        if row["path"].endswith(".sources.json"):
            doc = json.loads(raw)
            pending.extend(doc.get("frozen_sources", doc.get("sources", [])))
    parent = json.loads(
        git(PARENT, "research/exploratory/xi_quadratic_critical_transport.json")
    )
    unsigned = {k: v for k, v in parent.items() if k != "payload_sha256"}
    need(
        sha(canon(unsigned)) == report["parent_payload_sha256"], "inherited QT payload"
    )
    return report, parent, seen


def algebra():
    # Additional nonsource rational geometries and extreme ratios.
    count = 0
    for d in [Q(1, 1000), Q(1, 3), Q(5), Q(1000)]:
        for y in [Q(1, 999), Q(2, 7), Q(11), Q(999)]:
            L = d + y
            rstar = d * y / L
            need(0 < rstar < min(y, 2 * d), "interior maximizer")
            B = 3 * d * d / (y * (L + d) * (3 * L + y))
            need(B == 3 * d * d / ((L * L - d * d) * (4 * L - d)), "alternative B")
            for ratio in [Q(1, 10000), Q(1, 31), Q(1, 2), Q(30, 31), Q(9999, 10000)]:
                r = ratio * min(y, 2 * d)
                F = r * (d - r / 2) / (y + r) ** 2
                # Exact positive square is a second proof of the maximum.
                gap = d * d / (2 * y * (L + d)) - F
                need(
                    gap == (L * r - d * y) ** 2 / (2 * y * (L + d) * (y + r) ** 2),
                    "square gap",
                )
                need(6 * F / (3 * L + y + r) < B < d / (2 * L * y), "strict ceilings")
                count += 1
    return count


def build():
    report, parent, closure = provenance()
    need(len(report["records"]) == len(parent["records"]) == 26, "complete panel")
    need(
        report["contract"]["joint_remainder_criterion_ruled_out"] is False,
        "target firewall",
    )
    need(report["contract"]["threshold_is_exact_supremum"] is False, "ceiling firewall")
    result = []
    old = ctx.prec
    ctx.prec = 1024
    try:
        lam = 1 / ((acb(arb(1) / 4, arb(32)).digamma().real - arb.pi().log()) / 2)
        L = bounds(lam)
        for i, (row, p) in enumerate(zip(report["records"], parent["records"])):
            critical = p["critical"]
            need(
                row["index"] == i
                and row["center"] == critical["center"]
                and row["radius"] == critical["radius"],
                "same critical interval",
            )
            need(sha(canon(critical)) == row["parent_critical_sha256"], "critical seal")
            need(critical["simple_real_critical"] is True, "inherited critical theorem")
            native = comparison(
                *(interval(row["jets"][key]) for key in ("f5", "f7", "f8")),
                interval(report["lambda_(64)"]),
            )
            center, epsilon = pair(row["center"]), pair(row["radius"])
            need(epsilon == Q(1, 2**120), "fixed full radius")
            values = reflected_xi(acb(arb(ball(center), ball(epsilon))))
            need(
                all(v.is_finite() and v.imag.contains(0) for v in values),
                "real finite reflected jets",
            )
            need(values[6].real.contains(0), "inherited critical consistency")
            fresh = comparison(*(bounds(values[j].real) for j in (5, 7, 8)), L)
            for j in (5, 6, 7, 8):
                a, b = bounds(values[j].real), interval(row["jets"]["f" + str(j)])
                need(
                    max(a[0], b[0]) <= min(a[1], b[1]),
                    "independent reflected jet overlap",
                )
            expected = row["sharp_obstruction"], row["coarse_obstruction"]
            need(native == fresh == expected, "independent all-radius decisions")
            need(
                (row["status"] == "ALL_RADII_CRITERION_IMPOSSIBLE") == fresh[0],
                "status",
            )
            result.append({"index": i, "sharp": fresh[0], "coarse": fresh[1]})
    finally:
        ctx.prec = old
    need(
        sum(r["sharp"] for r in result) == 18
        and sum(r["coarse"] for r in result) == 15,
        "full outcomes",
    )
    out = {
        "source": SCIENCE,
        "source_fixture_sha256_lf": FIXTURE_SHA,
        "source_payload_sha256": report["payload_sha256"],
        "source_pins": len(closure),
        "source_closure_sha256": sha(canon(closure)),
        "fresh_reflected_full_interval_jets": 26,
        "coefficients_per_node": 9,
        "precision_bits": 1024,
        "comparison": "d^2=lambda^2+2a/c; B=3d^2/[(lambda^2-d^2)(4lambda-d)]; 384-bit integer sqrt",
        "same_flint_backend_not_second_special_function_implementation": True,
        "critical_existence_inherited_not_reproved_here": True,
        "additional_extreme_rational_radius_checks": algebra(),
        "records": result,
    }
    out["payload_sha256"] = sha(canon(out))
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    report = build()
    if args.check:
        need(
            canon(report) == canon(json.loads(OUT.read_bytes())), "independent fixture"
        )
        print(
            "PASS QR21936f22:38 pins;26 reflected full-interval jets;18 sharp/15 coarse;80 extra exact radii"
        )
    else:
        print(json.dumps(report, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
