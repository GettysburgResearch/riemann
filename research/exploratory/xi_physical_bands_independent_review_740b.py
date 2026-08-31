"""Independent fixed-SHA physical-band review; no author arithmetic imports.

Fresh axis values use finite Dirichlet sums with analytic integral tails,
not the author's zeta-series derivative. Monotone corner bounds independently
validate every positive published norm floor. Parent roots remain inherited.
"""

import argparse
import copy
import hashlib
import importlib.util
import json
import math
import subprocess
import sys
from fractions import Fraction as Q
from itertools import pairwise
from pathlib import Path

from flint import acb, arb, ctx, fmpq

ROOT = Path(__file__).resolve().parents[2]
D = "research/exploratory/"
STEM = "xi_fixed_lambda_shrinking_physical_bands"
SCIENCE = "740b497e99e6e6fb274684cc53599302402f2718"
DESIGN = "f7cc9bea51c6ab0b969acdc6e279ed09f608acac"
FIXTURE_SHA = "994483f138682e2b740ddc84bd93197e6d11c57e609be5e6fdd51daf55fbf3b5"


def need(ok, reason):
    if not ok:
        raise ValueError(reason)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode()


def raw(commit, path):
    return subprocess.check_output(
        ["git", "--no-replace-objects", "show", commit + ":" + path], cwd=ROOT
    )


def lf(data):
    return data.replace(b"\r\n", b"\n")


def pair(value):
    need(type(value) is list and len(value) == 2, "rational pair shape")
    n, d = value
    need(
        type(n) is int and type(d) is int and d > 0 and math.gcd(n, d) == 1,
        "canonical exact rational",
    )
    return Q(n, d)


def ends(value):
    lo, hi = map(pair, value)
    need(lo <= hi, "interval order")
    return lo, hi


def ar(value):
    value = Q(value)
    return arb(fmpq(value.numerator, value.denominator))


def endpoint(value):
    q = value.fmpq()
    return Q(int(q.numerator), int(q.denominator))


def ball(value):
    lo, hi = ends(value)
    return arb(ar((lo + hi) / 2), ar((hi - lo) / 2))


def contains(recorded, fresh):
    lo, hi = ends(recorded)
    return lo <= endpoint(fresh.lower()) <= endpoint(fresh.upper()) <= hi


def fresh_axis(height, lam):
    sigma = ar(Q(1, 2) + height)
    z, d = arb(1), arb(0)
    for n in range(2, 65):
        logn = arb(n).log()
        term = (-sigma * logn).exp()
        z += term
        d += logn * term
    # Both x^-sigma and log(x)*x^-sigma decrease on [64,infinity).
    power = ((1 - sigma) * arb(64).log()).exp()
    ztail = power / (sigma - 1)
    dtail = power * (arb(64).log() / (sigma - 1) + 1 / (sigma - 1) ** 2)
    z += arb(ztail / 2, ztail / 2)
    derivative = -d - arb(dtail / 2, dtail / 2)
    ell = (
        1 / sigma
        + 1 / (sigma - 1)
        - arb.pi().log() / 2
        + acb(sigma / 2).digamma().real / 2
        + derivative / z
    )
    theta = (1 - lam * ell) / (1 + lam * ell)
    need(-1 < theta < 0, "negative finite axis")
    return ell, theta


def rectangle_abs_lower(value):
    coords = []
    for name in ("real", "imag"):
        lo, hi = ends(value[name])
        coords.append(Q(0) if lo <= 0 <= hi else min(abs(lo), abs(hi)))
    return ar(sum(q * q for q in coords)).sqrt()


def floor_below(q, digits):
    scaled = q * 10**digits
    n = scaled.numerator // scaled.denominator
    if n and scaled == n:
        n -= 1
    return Q(n, 10**digits)


def authenticate():
    data = raw(SCIENCE, D + STEM + ".json")
    need(sha(lf(data)) == FIXTURE_SHA, "frozen fixture LF identity")
    report = json.loads(data)
    unsigned = dict(report)
    payload = unsigned.pop("payload_sha256")
    need(sha(canonical(unsigned)) == payload, "payload identity")
    for path, expected in report["artifacts"].items():
        frozen = raw(SCIENCE, path)
        need(sha(lf(frozen)) == expected, "artifact seal")
        need(
            lf((ROOT / path).read_bytes()) == lf(frozen),
            "local frozen scientific artifact",
        )
    for row in report["sources"]:
        data = raw(row["commit"], row["path"])
        need(len(data) <= 24000000, "source cap")
        blob = hashlib.sha1(
            b"blob " + str(len(data)).encode() + b"\0" + data
        ).hexdigest()
        need(
            blob == row["git_blob"] and sha(lf(data)) == row["sha256_lf"],
            "source seals",
        )
    design = lf(raw(DESIGN, D + STEM.upper() + ".md")).decode()
    proof = lf(raw(SCIENCE, D + STEM.upper() + ".md")).decode()
    need(
        proof.split("## 1.", 1)[1].split("## 5.", 1)[0].strip()
        == design.split("## 1.", 1)[1].strip(),
        "unchanged preregistered sections",
    )
    return report


def independent(report):
    ctx.prec = 384
    lam = 2 / (acb(ar(Q(1, 4)), 32).digamma().real - arb.pi().log())
    need(contains(report["lambda_(64)"], lam), "fresh lambda containment")
    axes = {}
    axis_rows = []
    for row, height in zip(report["axis_calibrations"], (2**j for j in range(6, 17))):
        need(row["h"] == height, "full fixed axis grid")
        ell, theta = fresh_axis(height, lam)
        need(contains(row["log_derivative"], ell), "Dirichlet-tail ell containment")
        need(contains(row["theta_axis"], theta), "Dirichlet-tail theta containment")
        axes[height] = -theta
        axis_rows.append(
            {
                "h": height,
                "fresh_ell": [str(endpoint(ell.lower())), str(endpoint(ell.upper()))],
                "fresh_theta": [
                    str(endpoint(theta.lower())),
                    str(endpoint(theta.upper())),
                ],
            }
        )
    nodes = report["inherited_nodes"]
    need(len(nodes) == 40, "all inherited nodes")
    raw_abs = [rectangle_abs_lower(row["raw_theta"]) for row in nodes]
    summaries = []
    certified = zero = cells = 0
    for band, width in zip(report["bands"], (Q(1, 256), Q(1, 1024), Q(1, 4096))):
        need(pair(band["D"]) == width, "three fixed bands")
        best = []
        pos_here = 0
        for index, row in enumerate(band["all1320_grid_part"]):
            need(row["node_index"] == index, "complete node order")
            xs, ys = ends(nodes[index]["x_interval"]), ends(nodes[index]["y_interval"])
            vals = []
            need(len(row["witnesses"]) == 11, "all eleven witnesses")
            for v, h in zip(row["witnesses"], (2**j for j in range(6, 17))):
                need(v["h"] == h and pair(v["D"]) == width, "cell grid identity")
                # y < 1 < h: y/((h+y)^2+x^2) strictly increases in y;
                # all x are positive, and the same expression decreases in x.
                need(
                    0 < ys[0] <= ys[1] < 1 < h and xs[0] > 0,
                    "corner monotonicity domain",
                )
                laplace = (
                    2
                    * (arb(h) * ar(ys[0])).sqrt()
                    * axes[h]
                    / ((arb(h) + ar(ys[0])) ** 2 + ar(xs[1]) ** 2).sqrt()
                )
                tail = (-ar(h * width)).exp()
                den = (1 - (-ar(2 * h * width)).exp()).sqrt()
                q = pair(v["norm_lower"])
                need(
                    q >= 0 and type(v["positive"]) is bool and v["positive"] == (q > 0),
                    "cell positivity record",
                )
                need(v["tail_widened"] is False, "this panel has no sub2^-512 tails")
                if q > 0:
                    lower = raw_abs[index] * (laplace - tail) / den
                    need(
                        lower > 0 and q <= endpoint(lower.lower()),
                        "independent monotone-corner certified floor",
                    )
                    certified += 1
                    pos_here += 1
                else:
                    zero += 1
                vals.append(q)
                cells += 1
            best.append(max(vals))
        need(
            pos_here == band["positive_cells"] and 440 - pos_here == band["zero_cells"],
            "all positive and zero cells retained",
        )
        need(best == list(map(pair, band["best_node_lower"])), "independent maxima")
        for row, n, c in zip(
            band["prefixes"],
            (14, 22, 31, 40),
            (Q(1171, 500), Q(599, 250), Q(1207, 500), Q(121, 50)),
        ):
            need(
                row["prefix_nodes"] == n and pair(row["Gram_ceiling"]) == c,
                "literal inherited Gram denominator",
            )
            hs = sum((v * v for v in best[:n]), Q(0)) / c
            norm = max(best[:n])
            need(
                pair(row["squared_HS_lower"]) == hs and pair(row["norm_lower"]) == norm,
                "independent exact finite-frame aggregation",
            )
            need(
                pair(row["strict_squared_HS_floor"]) == floor_below(hs, 16)
                and pair(row["strict_norm_floor"]) == floor_below(norm, 12),
                "strict decimal floors",
            )
            summaries.append(
                {
                    "D": str(width),
                    "prefix": n,
                    "squared_HS_floor": str(floor_below(hs, 16)),
                    "norm_floor": str(floor_below(norm, 12)),
                }
            )
    need((cells, certified, zero) == (1320, 482, 838), "complete cell counts")
    order = sorted(range(40), key=lambda i: ends(nodes[i]["x_interval"])[0])
    geo = report["geometry"]
    need(order == geo["ordered_indices"], "geography order")
    for (i, j), row in zip(pairwise(order), geo["adjacent_gaps"]):
        gap = ends(nodes[j]["x_interval"])[0] - ends(nodes[i]["x_interval"])[1]
        height = ends(nodes[i]["y_interval"])[1] + ends(nodes[j]["y_interval"])[1]
        need(
            row["left"] == i
            and row["right"] == j
            and pair(row["gap_lower"]) == gap
            and pair(row["height_sum_upper"]) == height
            and gap >= height
            and row["certified"] is True,
            "independent complete gap",
        )
    range_checks = 0
    for a in range(40):
        for b in range(a + 1, 40):
            span = (
                ends(nodes[order[b]]["x_interval"])[0]
                - ends(nodes[order[a]]["x_interval"])[1]
            )
            mass = sum(
                (ends(nodes[order[k]]["y_interval"])[1] for k in range(a, b + 1)), Q(0)
            )
            need(span >= mass, "additional every consecutive range span/mass control")
            range_checks += 1
    occupied = set()
    for i, row in enumerate(geo["memberships"]):
        lo, hi = ends(nodes[i]["x_interval"])
        cell = lo.numerator // lo.denominator
        need(
            row == {"index": i, "lower_cell": cell, "resolved": True}
            and hi < cell + 1
            and cell not in occupied,
            "complete distinct unit membership",
        )
        occupied.add(cell)
    return {
        "precision_bits": 384,
        "axis_method": "63-term Dirichlet sums plus integral tails; digamma for gamma derivative",
        "axis_values": axis_rows,
        "positive_norm_floors_certified_independently": certified,
        "zero_cells_retained": zero,
        "grid_cells": cells,
        "prefix_summaries": summaries,
        "adjacent_gap_checks": 39,
        "additional_contiguous_range_checks": range_checks,
        "unit_memberships": 40,
        "root_census_reexecuted": False,
        "physical_inner_premise_proved": False,
    }


def hostile(report):
    sys.path.insert(0, str(ROOT / D))
    spec = importlib.util.spec_from_file_location(
        "reviewed_pb", ROOT / D / (STEM + ".py")
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    def drop_zero(r):
        for node in r["bands"][0]["all1320_grid_part"]:
            for i, v in enumerate(node["witnesses"]):
                if not v["positive"]:
                    node["witnesses"].pop(i)
                    return
        raise ValueError("no zero to remove")

    actions = [
        drop_zero,
        lambda r: r["contract"].__setitem__("cofinal_capture", True),
        lambda r: r["axis_calibrations"][-1].__setitem__("h", 32768),
        lambda r: r["inherited_prefixes"][-1].__setitem__("Gram_ceiling", [1, 1]),
        lambda r: r["geometry"]["memberships"][-1].__setitem__("resolved", False),
        lambda r: r["bands"][-1].__setitem__("all40_nodes_positive", 1),
    ]
    for change in actions:
        bad = copy.deepcopy(report)
        change(bad)
        bad.pop("payload_sha256")
        bad["payload_sha256"] = sha(canonical(bad))
        try:
            module.check_report(bad)
        except ValueError:
            continue
        raise ValueError("accepted independently resealed hostile report")
    return len(actions)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--hostile", action="store_true")
    ap.add_argument("--check-report")
    args = ap.parse_args()
    report = authenticate()
    result = {
        "science": SCIENCE,
        "fixture_sha256_lf": FIXTURE_SHA,
        "source_payload_sha256": report["payload_sha256"],
        "source_bindings": len(report["sources"]),
        "artifact_seals": len(report["artifacts"]),
        "review_kind": "hostile" if args.hostile else "independent_arithmetic",
    }
    if args.hostile:
        result["fresh_unmocked_resealed_attacks_rejected"] = hostile(report)
    else:
        result["independent"] = independent(report)
    result["payload_sha256"] = sha(canonical(result))
    if args.check_report:
        need(
            canonical(json.loads(Path(args.check_report).read_bytes()))
            == canonical(result),
            "type-exact review report",
        )
        print("PASS fixed-SHA independent PB review")
    else:
        print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
