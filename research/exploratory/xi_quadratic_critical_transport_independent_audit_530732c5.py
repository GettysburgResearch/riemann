"""Independent QT audit: no author producer imports; same pinned FLINT library."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path

from flint import acb, acb_series, arb, ctx

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
SCIENCE = "530732c5fd7f50364381f8af50e97ce809b674c5"
STEM = "xi_quadratic_critical_transport"
FIXTURE_SHA = "45e9d81f5cfe22662ad9e07b9a994796b3c3b18743ae74c8cbd3ce095f3a4cce"
HISTORY_SHA = "20e3b2d04d62b9b26119c77613a68fc9f4d76eba4be09bdee28d4f4bd7d8cd2e"
EPS, OUTER = Q(1, 2**120), Q(7, 8)
RATIOS = (Q(1, 16), Q(1, 8), Q(1, 4), Q(1, 2), Q(3, 4))
OUT = HERE / "xi_quadratic_critical_transport_independent_audit_530732c5.json"
PATHS = [
    "research/exploratory/XI_QUADRATIC_CRITICAL_TRANSPORT.md",
    "research/exploratory/" + STEM + ".py",
    "research/exploratory/" + STEM + ".json",
    "research/exploratory/" + STEM + ".sources.json",
    "tests/test_" + STEM + ".py",
]


def need(ok, message):
    if not ok:
        raise ValueError(message)


def canon(value):
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def lf(raw):
    return raw.replace(b"\r\n", b"\n")


def git(commit, path):
    raw = subprocess.check_output(["git", "show", commit + ":" + path], cwd=ROOT)
    need(len(raw) < 24000000, "bounded source")
    return raw


def qp(pair):
    need(type(pair) is list and len(pair) == 2, "pair")
    a, b = pair
    need(type(a) is int and type(b) is int and b > 0, "strict pair")
    need(max(abs(a).bit_length(), b.bit_length()) <= 4096, "pair cap")
    q = Q(a, b)
    need([q.numerator, q.denominator] == pair, "reduced pair")
    return q


def pair(q):
    return [q.numerator, q.denominator]


def ball(q):
    return arb(q.numerator) / arb(q.denominator)


def end(value):
    need(value.is_exact() and value.is_finite(), "exact finite endpoint")
    q = value.fmpq()
    return Q(int(q.numerator), int(q.denominator))


def bounds(value):
    return end(value.lower()), end(value.upper())


def iv(data):
    return tuple(qp(v) for v in data)


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
    need(b[0] * b[1] > 0, "inverse interval avoids zero")
    return mul(a, (1 / b[1], 1 / b[0]))


def sqrt_iv(a):
    need(a[0] > 0, "positive sqrt")
    n = 2**320
    lo = math.isqrt(a[0].numerator * n * n // a[0].denominator)
    hi = math.isqrt(a[1].numerator * n * n // a[1].denominator)
    if Q(hi, n) ** 2 < a[1]:
        hi += 1
    return Q(lo, n), Q(hi, n)


def abs_iv(a):
    return (0 if a[0] <= 0 <= a[1] else min(abs(x) for x in a)), max(abs(x) for x in a)


def point_test(a, c, lam, lower):
    q = neg(div(a, mul(lam, c)))
    need(q[0] > 0 and 2 * q[1] < lam[0], "source discriminant")
    d = sqrt_iv(add(mul(lam, lam), neg(scale(mul(lam, q), Q(2)))))
    # Independent formula, not author's cancellation-stable rationalization.
    y = add(lam, neg(d))
    need(y[0] > 0, "positive y")
    result = []
    for ratio in RATIOS:
        r = scale(y, ratio)
        need(r[1] < y[0] and r[1] < 2 * d[0], "uniform radius geometry")
        h = add(y, r)
        lhs = scale(mul(mul(h, h), add(scale(h, Q(1, 6)), scale(lam, Q(1, 2)))), lower)
        rhs = mul(mul(abs_iv(c), r), add(d, neg(scale(r, Q(1, 2)))))
        result.append(lhs[0] >= rhs[1])
    return result


def xi(z, reflected=False, cap=9):
    # Native completed function; no imported HA/QT helper.
    old = ctx.cap
    ctx.cap = cap
    try:
        s = acb_series([acb(arb(1) / 2) + acb(0, 1) * z, acb(0, 1)])
        if reflected:
            s = 1 - s
        value = (s * (s - 1) / 2) * (-s * arb.pi().log() / 2).exp()
        value = value * (s / 2).gamma() * s.zeta()
        return [value[j] * math.factorial(j) for j in range(cap)]
    finally:
        ctx.cap = old


def xi_scalar(z):
    s = acb(arb(1) / 2) + acb(0, 1) * z
    return (
        s * (s - 1) / 2 * (-s / 2 * arb.pi().log()).exp() * (s / 2).gamma() * s.zeta()
    )


def provenance():
    for path in PATHS:
        need(
            lf((ROOT / path).read_bytes()) == lf(git(SCIENCE, path)),
            "science source unchanged",
        )
    raw = lf((HERE / (STEM + ".json")).read_bytes())
    need(sha(raw) == FIXTURE_SHA, "exact frozen fixture")
    data = json.loads(raw)
    unsigned = {k: v for k, v in data.items() if k != "payload_sha256"}
    need(sha(canon(unsigned)) == data["payload_sha256"], "payload")
    for path, digest in data["artifacts"].items():
        need(sha(lf((ROOT / path).read_bytes())) == digest, "artifact")
    manifest = json.loads((HERE / (STEM + ".sources.json")).read_bytes())
    pending = list(manifest["frozen_sources"])
    seen = {}
    while pending:
        row = pending.pop()
        key = row["commit"] + ":" + row["path"]
        if key in seen:
            need(seen[key] == row["sha256_lf"], "consistent repeated binding")
            continue
        raw = git(row["commit"], row["path"])
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        need(
            blob == row["git_blob"] and sha(lf(raw)) == row["sha256_lf"],
            "transitive source",
        )
        seen[key] = row["sha256_lf"]
        if row["path"].endswith(".sources.json"):
            source = json.loads(raw)
            pending.extend(source.get("frozen_sources", source.get("sources", [])))
    history = data["environmental_attempt_history"]
    need(sha(canon(history)) == HISTORY_SHA, "history pin")
    need(len(history["entries"]) == 546, "546 tasks")
    for e in history["entries"]:
        need(sha(canon(e["task"])) == e["task_id"], "task identity")
        need(
            e["outcome"]["status"] == "PASS" or "upper" not in e["outcome"],
            "no historical failed bound",
        )
    return data, seen


def finite(data):
    counts = [0] * 5
    tails, attempts = 0, 0
    allcenters = []
    needed_tasks = set()
    timeouts = []
    rows = data["records"]
    for row, diagnostic in zip(rows, data["postresult_necessary_bound"]["records"]):
        need(row["index"] == len(allcenters), "ordered26")
        center = qp(row["critical"]["center"])
        allcenters.append(center)
        need(qp(row["critical"]["radius"]) == EPS, "tiny radius")
        cert = row["critical"]["attempts"][-1]
        need(
            qp(cert["residual"]) + qp(cert["second_upper"]) * EPS**2 / 2
            < qp(cert["derivative_lower"]) * EPS,
            "literal critical Rouche",
        )
        tier = row["jet_tiers"][-1]
        flags = point_test(
            iv(tier["a"]),
            iv(tier["c"]),
            iv(tier["lambda"]),
            qp(diagnostic["point_f8_lower"]),
        )
        need(
            flags == [x["criterion_impossible"] for x in diagnostic["ratios"]],
            "independent130 point signs",
        )
        counts = [a + int(b) for a, b in zip(counts, flags)]
        for tier in row["jet_tiers"]:
            bits = tier["bits"]
            task = {
                "route": "outer_direct",
                "center": pair(center),
                "radius": pair(OUTER),
                "bits": bits,
            }
            needed_tasks.add(sha(canon(task)))
            source = tier["outer_scalar_bound"]
            need(
                source["fixed_cover"]["cells_attempted"]
                == source["fixed_cover"]["finite_cells"]
                == 256,
                "full cover",
            )
            m = qp(source["upper"])
            coeff = [qp(v) for v in tier["coefficient_modulus_upper_8_to39"]]
            for branch in row["quadratic"] + [row["linear"]]:
                attempt = next(a for a in branch["attempts"] if a["bits"] == bits)
                third = attempt["third_derivative"]
                h = qp(third["radius_upper"])
                task = {
                    "route": "third_direct",
                    "center": pair(center),
                    "radius": pair(h),
                    "bits": bits,
                }
                needed_tasks.add(sha(canon(task)))
                need(
                    third["status"] == "PASS" and not attempt["transport_certified"],
                    "valid bound/no certificate",
                )
                tc = third["taylor_cauchy"]
                need(h < OUTER and tc["status"] == "PASS", "same-radius Cauchy")
                x = h / OUTER
                exact = (
                    m
                    * math.factorial(8)
                    * math.comb(40, 8)
                    * x**32
                    / (OUTER**8 * (1 - x) ** 9)
                )
                need(qp(tc["tail"]) >= exact, "outward infinite-tail majorant")
                poly = sum(
                    coeff[n] * Q(math.factorial(n + 8), math.factorial(n)) * h**n
                    for n in range(32)
                )
                need(qp(tc["polynomial"]) >= poly, "outward finite polynomial")
                need(qp(tc["upper"]) == qp(tc["tail"]) + qp(tc["polynomial"]), "sum")
                tails += 1
                if "ratio" in attempt:
                    attempts += 1
                    need(
                        qp(attempt["error_upper"]) >= qp(attempt["margin_lower"]),
                        "quadratic failed strict guard",
                    )
        # Full exact16x16 coverage geometry, independent endpoints.
        xr = [
            center - OUTER - EPS + Q(i, 16) * (2 * OUTER + 2 * EPS) for i in range(17)
        ]
        yr = [-OUTER + Q(j, 16) * (2 * OUTER) for j in range(17)]
        need(
            xr[0] == center - OUTER - EPS and xr[-1] == center + OUTER + EPS,
            "uncertain center cover",
        )
        need(
            sum(
                (xr[i + 1] - xr[i]) * (yr[j + 1] - yr[j])
                for i in range(16)
                for j in range(16)
            )
            == 4 * OUTER * (OUTER + EPS),
            "exact cover area",
        )
    hist = data["environmental_attempt_history"]["entries"]
    need(needed_tasks == {e["task_id"] for e in hist}, "every546 exact task")
    for e in hist:
        if e["outcome"]["status"] == "TIMEOUT_UNRESOLVED":
            t = e["task"]
            index = allcenters.index(qp(t["center"]))
            timeouts.append([index, t["bits"], t["route"]])
    need(
        sorted(timeouts)
        == [[i, b, "outer_direct"] for i in range(22, 26) for b in (256, 512, 1024)],
        "timeout geography",
    )
    need(
        all(
            abs(a - b) > 2 * EPS
            for i, a in enumerate(allcenters)
            for b in allcenters[i + 1 :]
        ),
        "distinct critical intervals",
    )
    need(
        counts == [26, 26, 26, 21, 19] and attempts == 390 and tails == 468,
        "finite counts",
    )
    # Product proof of binomial inequality is uniform; extra exact finite controls.
    binomial = 0
    for n in (0, 1, 7, 32, 97):
        for j in range(101):
            need(
                math.comb(n + j + 8, 8) <= math.comb(n + 8, 8) * math.comb(j + 8, 8),
                "binomial control",
            )
            binomial += 1
    return {
        "point_impossible_by_ratio": counts,
        "exact_tail_and_polynomial_checks": tails,
        "quadratic_attempts": attempts,
        "complete_cover_geometries": 78,
        "exact_task_identities": len(needed_tasks),
        "history_counts": dict(Counter(e["outcome"]["status"] for e in hist)),
        "timeout_geography": sorted(timeouts),
        "extra_binomial_controls": binomial,
    }


def fresh_native(data):
    oldprec = ctx.prec
    ctx.prec = 1024
    result, counts = [], [0] * 5
    try:
        lam = 1 / ((acb(arb(1) / 4, 32).digamma().real - arb.pi().log()) / 2)
        for row in data["records"]:
            center = qp(row["critical"]["center"])
            t = arb(ball(center), ball(EPS))
            point = xi(acb(ball(center)), reflected=True)
            square = xi(acb(t, arb(0, ball(EPS))), reflected=True)
            need(
                end(point[6].abs_upper()) + end(square[8].abs_upper()) * EPS**2 / 2
                < end(point[7].abs_lower()) * EPS,
                "fresh reflected critical Rouche",
            )
            native = xi(acb(t), reflected=True)
            need(native[6].real.contains(0), "same unknown critical interval")
            need(all(v.imag.contains(0) for v in native), "Schwarz jets")
            m = end(native[8].abs_lower())
            flags = point_test(
                bounds(native[5].real), bounds(native[7].real), bounds(lam), m
            )
            need(
                flags
                == [
                    x["criterion_impossible"]
                    for x in data["postresult_necessary_bound"]["records"][
                        row["index"]
                    ]["ratios"]
                ],
                "fresh reflected point signs",
            )
            counts = [a + int(b) for a, b in zip(counts, flags)]
            result.append(
                {
                    "index": row["index"],
                    "reflected_critical_pass": True,
                    "point_impossible": flags,
                }
            )
        # Extra complete native covers fixed before this independent calculation.
        extra = []
        ctx.prec = 512
        for index in (0, 12, 25):
            center = qp(data["records"][index]["critical"]["center"])
            maximum = Q(0)
            stream = []
            for i in range(16):
                xl = center - OUTER - EPS + Q(i, 16) * (2 * OUTER + 2 * EPS)
                xu = center - OUTER - EPS + Q(i + 1, 16) * (2 * OUTER + 2 * EPS)
                for j in range(16):
                    yl = -OUTER + Q(j, 16) * (2 * OUTER)
                    yu = -OUTER + Q(j + 1, 16) * (2 * OUTER)
                    z = acb(
                        arb(ball((xl + xu) / 2), ball((xu - xl) / 2)),
                        arb(ball((yl + yu) / 2), ball((yu - yl) / 2)),
                    )
                    upper = end(xi_scalar(z).abs_upper())
                    maximum = max(maximum, upper)
                    stream.append(pair(upper))
            published = next(
                t for t in data["records"][index]["jet_tiers"] if t["bits"] == 512
            )["outer_scalar_bound"]["fixed_cover"]
            need(maximum == qp(published["upper"]), "independent heldout cover maximum")
            extra.append(
                {
                    "index": index,
                    "bits": 512,
                    "cells": 256,
                    "upper": pair(maximum),
                    "bound_stream_sha256": sha(canon(stream)),
                }
            )
        return {
            "independent_reflected_Rouche": 26,
            "independent_reflected_point_counts": counts,
            "records": result,
            "additional_complete_native_covers": extra,
        }
    finally:
        ctx.prec = oldprec


def build():
    data, sources = provenance()
    result = {
        "science": SCIENCE,
        "fixture_sha256_lf": FIXTURE_SHA,
        "transitive_bindings": len(sources),
        "source_closure_sha256": sha(canon(sources)),
        "finite": finite(data),
        "native": fresh_native(data),
        "scope": "Independent algebra/primitive formula, SAME pinned FLINT implementation; no new nodes,radii,or cofinal claim.",
    }
    result["payload_sha256"] = sha(canon(result))
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.check:
        need(
            canon(result) == canon(json.loads(OUT.read_bytes())),
            "independent audit fixture",
        )
        print(
            "PASS independent QT530732c5:26 reflected critical certificates,130 point cases,468 exact Taylor bounds,768 extra native cells"
        )
    else:
        print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
