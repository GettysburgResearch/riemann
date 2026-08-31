"""Independent JR audit: standard library only, no author producer imports."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
SCIENCE = "a29373d16abcf646cc0f86bd7d3f215e98ed15b0"
BASE = "530732c5fd7f50364381f8af50e97ce809b674c5"
STEM = "xi_quadratic_joint_remainder_transport"
FIXTURE_SHA = "b94616081a5f3ed187cd5aeb17fe36e03c09e97b6f1460c798531035678e8c3a"
OUT = HERE / "xi_joint_remainder_independent_audit_a29373d1.json"
EPS = Q(1, 2**120)
RATIOS = (Q(1, 16), Q(1, 8), Q(1, 4), Q(1, 2), Q(3, 4))
TIERS = (256, 512, 1024)


def need(ok, why):
    if not ok:
        raise ValueError(why)


def canon(v):
    return json.dumps(v, sort_keys=True, separators=(",", ":")).encode()


def sha(v):
    return hashlib.sha256(v).hexdigest()


def lf(v):
    return v.replace(b"\r\n", b"\n")


def git(commit, path):
    raw = subprocess.check_output(
        ["git", "--no-replace-objects", "show", commit + ":" + path], cwd=ROOT
    )
    need(len(raw) <= 24000000, "bounded source")
    return raw


def pair(v):
    need(type(v) is list and len(v) == 2, "rational shape")
    n, d = v
    need(type(n) is int and type(d) is int and d > 0, "rational types")
    need(max(abs(n).bit_length(), d.bit_length()) <= 12288, "rational cap")
    q = Q(n, d)
    need([q.numerator, q.denominator] == v, "canonical rational")
    return q


def iv(v):
    a, b = map(pair, v)
    need(a <= b, "ordered interval")
    return a, b


def plus(a, b):
    return a[0] + b[0], a[1] + b[1]


def minus(a, b):
    return a[0] - b[1], a[1] - b[0]


def times(a, b):
    values = [x * y for x in a for y in b]
    return min(values), max(values)


def factor(a, b):
    return times(a, (b, b))


def divide(a, b):
    need(b[0] * b[1] > 0, "zero-free denominator")
    return times(a, tuple(sorted([1 / b[0], 1 / b[1]])))


def intersect(*values):
    lo, hi = max(x[0] for x in values), min(x[1] for x in values)
    need(lo <= hi, "nonempty source intersection")
    return lo, hi


def root(a):
    need(a[0] > 0, "positive discriminant")
    n = 2**512
    lo = math.isqrt(a[0].numerator * n * n // a[0].denominator)
    hi = math.isqrt(a[1].numerator * n * n // a[1].denominator)
    if Q(hi, n) ** 2 < a[1]:
        hi += 1
    return Q(lo, n), Q(hi, n)


def absolute(a):
    need(a[0] * a[1] > 0, "sign-separated c")
    return tuple(sorted(map(abs, a)))


def source():
    paths = ["research/exploratory/" + STEM.upper() + ".md"]
    paths += [
        "research/exploratory/" + STEM + s for s in (".py", ".json", ".sources.json")
    ]
    paths += ["tests/test_" + STEM + ".py"]
    for path in paths:
        need(
            lf((ROOT / path).read_bytes()) == lf(git(SCIENCE, path)),
            "science unchanged",
        )
    raw = lf((HERE / (STEM + ".json")).read_bytes())
    need(sha(raw) == FIXTURE_SHA, "fixture identity")
    report = json.loads(raw)
    unsigned = {k: v for k, v in report.items() if k != "payload_sha256"}
    need(sha(canon(unsigned)) == report["payload_sha256"], "payload seal")
    for path, digest in report["artifacts"].items():
        need(sha(lf((ROOT / path).read_bytes())) == digest, "artifact seal")
    pending = list(report["frozen_sources"])
    seen = {}
    while pending:
        binding = pending.pop()
        key = binding["commit"] + ":" + binding["path"]
        if key in seen:
            need(seen[key] == binding["sha256_lf"], "consistent source pin")
            continue
        raw = git(binding["commit"], binding["path"])
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        need(
            blob == binding["git_blob"] and sha(lf(raw)) == binding["sha256_lf"],
            "source pin",
        )
        seen[key] = binding["sha256_lf"]
        if binding["path"].endswith(".sources.json"):
            doc = json.loads(raw)
            pending.extend(doc.get("frozen_sources", doc.get("sources", [])))
    parent = json.loads(
        git(BASE, "research/exploratory/xi_quadratic_critical_transport.json")
    )
    need(
        report["inherited_QT_payload_sha256"] == parent["payload_sha256"],
        "QT inheritance",
    )
    return report, parent, seen


def independent_cell(record, node, group, attempt, tier):
    critical = node["critical"]
    t = pair(critical["center"]) - EPS, pair(critical["center"]) + EPS
    need(
        pair(critical["radius"]) == EPS and critical["simple_real_critical"] is True,
        "inherited real root",
    )
    lo, hi = iv(tier["T"])
    need(lo <= t[0] <= t[1] <= hi, "full critical interval")
    ratio = pair(group["ratio"])
    need(
        (record["node"], pair(record["ratio"]), record["bits"])
        == (node["index"], ratio, tier["bits"]),
        "cell identity",
    )
    need(record["old_attempt_sha256"] == sha(canon(attempt)), "attempt binding")
    need(record["old_tier_sha256"] == sha(canon(tier)), "tier binding")
    L, a, c = (iv(tier[x]) for x in ("lambda", "a", "c"))
    need(L[0] > 0 and times(a, c)[1] < 0, "source sign conditions")
    q = intersect(divide(factor(a, -1), times(L, c)), iv(tier["q"]))
    need(q[0] > 0 and 2 * q[1] < L[0], "source q guard")
    disc = intersect(
        minus(times(L, L), factor(times(L, q), 2)),
        plus(times(L, L), factor(divide(a, c), 2)),
    )
    d = intersect(root(disc), iv(attempt["d"]))
    y = intersect(minus(L, d), iv(attempt["y"]))
    intersect(y, divide(factor(times(L, q), 2), plus(L, d)))
    r = intersect(factor(y, ratio), iv(attempt["radius"]))
    need(0 < r[0] <= r[1] < y[0] <= y[1] < L[0] and r[1] < 2 * d[0], "disc guard")
    for key, value in [("lambda", L), ("q", q), ("d", d), ("y", y), ("r", r)]:
        need(iv(record[key]) == value, "exact geometry " + key)
    third = attempt["third_derivative"]
    need(third["status"] == "PASS", "inherited M3")
    m, region = pair(third["upper"]), pair(third["radius_upper"])
    need(m >= 0 and y[1] + r[1] <= region, "original M3 domain retained")
    need(
        pair(record["source_M3_upper"]) == m
        and pair(record["source_region_radius"]) == region,
        "M3 binding",
    )
    f = L[0] / 2 - y[1] / 6 + r[0] / 6, L[1] / 2 - y[0] / 6 + r[1] / 6
    of = L[0] / 2 + (y[0] + r[0]) / 6, L[1] / 2 + (y[1] + r[1]) / 6
    need(f[0] > 0, "positive factor")
    error = tuple(m * (y[j] + r[j]) ** 2 * f[j] for j in (0, 1))
    old = tuple(m * (y[j] + r[j]) ** 2 * of[j] for j in (0, 1))
    absc = absolute(c)
    margin = absc[0] * r[0] * (d[0] - r[1] / 2), absc[1] * r[1] * (d[1] - r[0] / 2)
    for key, value in [
        ("joint_factor", f),
        ("joint_error", error),
        ("old_error_reconstructed", old),
        ("model_margin", margin),
    ]:
        need(iv(record[key]) == value, "independent endpoint formula " + key)
    need(
        error[1] >= margin[0] > 0 and record["transport_certified"] is False,
        "noncertification only",
    )
    x, eta = map(pair, node["HA_center"])
    eps = pair(node["HA_radius"])
    dx = max(abs(x - eps - t[1]), abs(x + eps - t[0]))
    dy = max(abs(eta - eps - y[1]), abs(eta + eps - y[0]))
    distance = dx * dx + dy * dy
    need(
        pair(record["full_parent_displacement_squared_upper"]) == distance
        and pair(record["radius_squared_lower"]) == r[0] ** 2,
        "entire rectangle",
    )
    contained = distance < r[0] ** 2
    need(record["full_parent_rectangle_contained"] is contained, "rectangle flag")
    need(
        record["matched_parent_root"] is False
        and record["status"] == "NOT_CERTIFIED_INHERITED_BOUND",
        "no matched inheritance",
    )
    need(
        record["old_outcome"]
        == {
            key: attempt[key]
            for key in ("status", "reason", "transport_certified", "parent_matched")
        },
        "old outcome unchanged",
    )
    return error[1] / margin[0], contained


def integral_controls():
    count = 0
    for n in range(3, 33):
        # Beta integrals prove both coefficients of the monomial identity.
        first = Q(math.factorial(2) * math.factorial(n - 3), math.factorial(n))
        second = Q(math.factorial(1) * math.factorial(n - 3), math.factorial(n - 1))
        coefficient = n * (n - 1) * (n - 2)
        need(
            coefficient * first / 2 == 1 and coefficient * second == n,
            "joint monomial identity",
        )
        count += 1
    directions = [
        (Q(0), Q(1)),
        (Q(0), Q(-1)),
        (Q(8, 17), Q(15, 17)),
        (Q(-20, 29), Q(21, 29)),
    ]
    cases = 0
    for y in [Q(1, 100), Q(1, 2), Q(99, 100)]:
        for ratio in RATIOS:
            r = y * ratio
            for tau in [Q(0), Q(1, 13), Q(1, 2), Q(12, 13), Q(1)]:
                for u, v in directions:
                    lhs = (tau * r * u / 2) ** 2 + (tau * (y + r * v) / 2 - 1) ** 2
                    rhs = (1 - tau * (y - r) / 2) ** 2
                    need(lhs <= rhs, "disc factor")
                    cases += 1
    need(Q(1, 3) * Q(3, 4) ** 2 * Q(11, 24) == Q(11, 128), "joint cubic")
    need(Q(11, 128) < Q(12, 128) < Q(15, 128), "strict cubic gain")
    return count, cases


def build():
    report, parent, seen = source()
    need(
        len(report["records"]) == 390 and len(parent["records"]) == 26, "complete panel"
    )
    quotients, contained = [], 0
    for node in parent["records"]:
        certificates = node["critical"]["attempts"]
        need(
            any(
                p.get("status") == "PASS"
                and pair(p["residual"]) + pair(p["second_upper"]) * EPS**2 / 2
                < pair(p["derivative_lower"]) * EPS
                for p in certificates
                if "left" in p
            ),
            "inherited critical inequality",
        )
        need(
            [pair(g["ratio"]) for g in node["quadratic"]] == list(RATIOS),
            "complete ratios",
        )
        need(
            [tier["bits"] for tier in node["jet_tiers"]] == list(TIERS),
            "complete tiers",
        )
        for group in node["quadratic"]:
            for attempt, tier in zip(group["attempts"], node["jet_tiers"]):
                row = report["records"][len(quotients)]
                value, flag = independent_cell(row, node, group, attempt, tier)
                quotients.append(value)
                contained += flag
    best = min(range(390), key=quotients.__getitem__)
    row = report["records"][best]
    need(
        (row["node"], pair(row["ratio"]), row["bits"]) == (19, Q(1, 2), 256),
        "least sufficient-check ratio",
    )
    need(1637350 <= quotients[best] * 1000000 < 1637351, "exact integer bracket")
    monomials, discs = integral_controls()
    result = {
        "source": SCIENCE,
        "fixture_sha256_lf": FIXTURE_SHA,
        "source_payload": report["payload_sha256"],
        "source_closure_count": len(seen),
        "source_closure_sha256": sha(canon(seen)),
        "inherited_critical_inequalities": 26,
        "cells_independently_reconstructed": 390,
        "joint_certified": 0,
        "full_rectangle_containment_flags_true": contained,
        "least_bound_cell": [19, "1/2", 256],
        "scaled_bound_ratio_integer_bracket": [1637350, 1637351],
        "additional_monomial_coefficient_controls": monomials,
        "additional_rational_disc_controls": discs,
        "no_new_Xi_or_M3_evaluations": True,
        "noncertification_not_criterion_impossibility": True,
    }
    result["payload_sha256"] = sha(canon(result))
    return result


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    result = build()
    if args.check:
        need(
            canon(result) == canon(json.loads(OUT.read_bytes())), "independent fixture"
        )
        print(
            "PASS independent JRa29373d1:390 exact cells/domains/rectangles;38 source pins;30 monomial and300 disc controls"
        )
    else:
        print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
