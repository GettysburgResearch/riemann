"""Exact cell-Carleson controls; the analytic Xi theorem is not machine verified."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from fractions import Fraction as Q
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
STEM = "xi_occupancy_carleson_capture"
BASE = "a7479e85fdc2a464cdc753021435cfef7a1f3910"
PREREG = "4f38c14b260fe939c3848884584b49ca3c3f7941"
NOTE = HERE / "XI_OCCUPANCY_CARLESON_CAPTURE.md"
MANIFEST = HERE / (STEM + ".sources.json")
FIXTURE = HERE / (STEM + ".json")
TEST = ROOT / "tests" / ("test_" + STEM + ".py")
BINDINGS = [
    {
        "commit": "a7479e85fdc2a464cdc753021435cfef7a1f3910",
        "path": "research/exploratory/XI_LAPLACE_LOW_PASS_LOWER_BOUND.md",
        "git_blob": "90e6bd89ca9a23c401d6d947c04a9d548f6b3030",
        "sha256_lf": "c56d29037b85c45398bcb34dc7fb8450ba0e4b0f32fa7293edcaf5d1d2ea4b64",
    },
    {
        "commit": "1904d20cdb76ecd26e0e63472625da930075303e",
        "path": "research/exploratory/XI_UNIFORM_COMPANION_COUNT_WIDTH.md",
        "git_blob": "a97d25f556a2bd085a4749d1e96d883a0646e666",
        "sha256_lf": "adaef750b277b755494d57e17a3e913e8f44f1614806d8274495ac88912fb0bc",
    },
    {
        "commit": "1904d20cdb76ecd26e0e63472625da930075303e",
        "path": "research/exploratory/XI_ACTUAL_KERNEL_LAPLACE_CONCENTRATION.md",
        "git_blob": "fa24f9c8e0a87709d1a297a4e72136c1135d066c",
        "sha256_lf": "f7f89abe2e54d0d8df72dc830162b2083bc4f05d402c3aa70eca464678e80246",
    },
    {
        "commit": "4f38c14b260fe939c3848884584b49ca3c3f7941",
        "path": "research/exploratory/XI_OCCUPANCY_CARLESON_CAPTURE.md",
        "git_blob": "c1c62d72ab77869ad2ebb43600ffdbf8f171edbb",
        "sha256_lf": "288b1165d1c58cd3eb8827464b9828b6023d598cbd0b3ff3f93d596cf0cdb080",
    },
]
MAX_N = 16
CONTRACT = {
    "arithmetic_class": "MIXED",
    "arithmetic_components": ["EXACT_RATIONAL", "CERTIFIED_INTEGER_COVERAGE"],
    "rounding": "none; exact canonical rational strings and integers",
    "source": "preregistered rational cell families; frozen literal-Xi analytic dependencies",
    "physical_metric": "unchanged boundary-dx Hardy norm; weights apply only to test vectors",
    "analytic": "local Jensen count, Carleson embedding and cofinal implication are written proofs",
    "imported": "classical half-plane Carleson embedding, Stirling, Euler-Maclaurin, Jensen",
    "scope": "finite exact controls; conditional infinite capture criterion",
    "open": "actual-Xi innerness, source-owned survival, divergent cofinal weighted alignment, decoder and RH",
    "no_xi_computation": True,
    "caps": {
        "nodes_per_cell": 16,
        "subset_oracle_nodes": 8,
        "interval_grid_rows": 600,
        "json_bytes": 1000000,
    },
}


def need(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode()


def lfhash(raw):
    return hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest()


def exact(value):
    need(type(value) in (int, Q), "exact rational input, not bool/float")
    result = Q(value)
    need(
        max(result.numerator.bit_length(), result.denominator.bit_length()) <= 256,
        "rational bit cap",
    )
    return result


def bounded_integer(value, low, high):
    need(type(value) is int and low <= value <= high, "integer index/cap")
    return value


def validate_tree(value):
    visits = 0

    def walk(obj, depth):
        nonlocal visits
        visits += 1
        need(visits <= 200000 and depth <= 16, "JSON tree cap")
        if type(obj) is dict:
            need(
                len(obj) <= 5000 and all(type(k) is str for k in obj),
                "JSON object cap/type",
            )
            for child in obj.values():
                walk(child, depth + 1)
        elif type(obj) is list:
            need(len(obj) <= 5000, "JSON array cap")
            for child in obj:
                walk(child, depth + 1)
        elif type(obj) is int:
            need(obj.bit_length() <= 4096, "JSON integer cap")
        elif type(obj) is str:
            need(
                len(obj) <= 4096 and all(ord(c) >= 32 or c in "\t\r\n" for c in obj),
                "JSON text cap",
            )
        else:
            need(type(obj) in (bool, type(None)), "JSON primitive")

    walk(value, 0)


def load_json(raw):
    need(type(raw) is bytes and len(raw) <= 1000000, "JSON byte cap")

    def pairs(items):
        result = {}
        for key, val in items:
            need(key not in result, "duplicate JSON key")
            result[key] = val
        return result

    def no_float(_):
        raise ValueError("JSON float or nonfinite number")

    result = json.loads(
        raw, object_pairs_hook=pairs, parse_float=no_float, parse_constant=no_float
    )
    validate_tree(result)
    return result


def manifest():
    return {
        "schema": STEM + "-sources-v1",
        "authoring_base": BASE,
        "preregistration": PREREG,
        "sources": BINDINGS,
        "contract": CONTRACT,
        "references": [
            {
                "url": "https://arxiv.org/pdf/1201.1021",
                "passage": "Theorem1.1, pp2-3",
                "role": "classical Carleson embedding",
            },
            {
                "url": "https://dlmf.nist.gov/5.11",
                "passage": "Stirling and digamma expansions",
                "role": "Gamma factor bounds",
            },
            {
                "url": "https://dlmf.nist.gov/25.2#iii",
                "passage": "Euler-Maclaurin representations",
                "role": "polynomial zeta growth on fixed strips",
            },
        ],
        "remote_reference_bytes": "not_authenticated_by_offline_checker",
    }


def authenticate():
    need(
        canonical(load_json(MANIFEST.read_bytes())) == canonical(manifest()),
        "source manifest",
    )
    for row in BINDINGS:
        raw = subprocess.check_output(
            ["git", "show", row["commit"] + ":" + row["path"]], cwd=ROOT
        )
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        need(
            blob == row["git_blob"] and lfhash(raw) == row["sha256_lf"],
            "frozen source identity",
        )
    # No historical theorem is executed or read from mutable current-parent paths.
    return len(BINDINGS)


def nodes(values):
    need(type(values) in (tuple, list) and 1 <= len(values) <= MAX_N, "node count/type")
    result = []
    for row in values:
        need(type(row) in (tuple, list) and len(row) == 2, "node shape")
        x, y = map(exact, row)
        need(0 <= x < 1 and 0 < y <= 1, "declared unit cell/height")
        result.append((x, y))
    return tuple(result)


def family(kind, n):
    n = bounded_integer(n, 1, MAX_N)
    need(type(kind) is str and kind in ("dispersed", "crowded"), "family name")
    if kind == "dispersed":
        return tuple(
            (Q(1, 4) + Q(j, 2 * (n + 1)), Q(1, 64 * n * n)) for j in range(1, n + 1)
        )
    return tuple(
        (Q(1, 4) + Q(j, 64 * n * n * (n + 1)), Q(1, 4)) for j in range(1, n + 1)
    )


def box_norm(values):
    pts = nodes(values)
    lengths = sorted(
        {y for x, y in pts} | {abs(x - u) for x, y in pts for u, v in pts if x != u}
    )
    anchors = sorted({x for x, y in pts})
    best = Q(0)
    witness = None
    checked = 0
    for length in lengths:
        for left in anchors:
            mass = sum(
                (y for x, y in pts if left <= x <= left + length and y <= length), Q(0)
            )
            checked += 1
            value = mass / length
            if value > best:
                best, witness = value, (left, length, mass)
    need(1 <= best <= len(pts), "Carleson elementary bounds")
    return best, witness, checked


def subset_norm(values):
    pts = nodes(values)
    need(len(pts) <= 8, "independent subset oracle cap")
    best = Q(0)
    for mask in range(1, 1 << len(pts)):
        chosen = [b for j, b in enumerate(pts) if mask & (1 << j)]
        radius = max(
            max(y for x, y in chosen),
            max(x for x, y in chosen) - min(x for x, y in chosen),
        )
        best = max(best, sum(y for x, y in chosen) / radius)
    return best


MIXED = (
    (Q(1, 8), Q(1, 8)),
    (Q(1, 4), Q(1, 4)),
    (Q(3, 8), Q(1, 16)),
    (Q(3, 4), Q(1, 2)),
)


def crowded_rayleigh(n):
    pts = nodes(family("crowded", n))
    total = Q(0)
    for x, y in pts:
        for u, v in pts:
            need(y == v == Q(1, 4), "equal-height Rayleigh control")
            total += (2 * y) ** 2 / ((2 * y) ** 2 + (x - u) ** 2)
    rayleigh = total / n
    need(rayleigh >= Q(16 * n, 17), "crowded unweighted norm growth")
    return rayleigh


def normalized_union():
    result = []
    for cell, kind, n in ((0, "dispersed", 3), (1, "crowded", 4), (2, "dispersed", 5)):
        pts = family(kind, n)
        cost = box_norm(pts)[0]
        result.extend((x + cell, y, Q(1) / cost) for x, y in pts)
    return tuple(result)


def box_mass(values, left, length):
    left, length = exact(left), exact(length)
    need(
        type(values) in (tuple, list) and length > 0 and len(values) <= 48,
        "finite box controls",
    )
    for row in values:
        need(type(row) in (tuple, list) and len(row) == 3, "weighted point shape")
        _x, y, weight = map(exact, row)
        need(0 < y <= 1 and 0 < weight <= 1, "weighted point range")
    return sum(
        (
            y * weight
            for x, y, weight in values
            if left <= x <= left + length and y <= length
        ),
        Q(0),
    )


def seal(value):
    need(type(value) is dict and "payload_sha256" not in value, "unsigned report")
    return {**value, "payload_sha256": hashlib.sha256(canonical(value)).hexdigest()}


def build_report():
    authenticate()
    panel = []
    for n in range(1, MAX_N + 1):
        for kind in ("dispersed", "crowded"):
            pts = family(kind, n)
            cost, witness, checked = box_norm(pts)
            need(
                cost == (1 if kind == "dispersed" else n),
                "preregistered family prediction",
            )
            if n <= 8:
                need(cost == subset_norm(pts), "independent exhaustive-subset identity")
            panel.append(
                {
                    "family": kind,
                    "N": n,
                    "nodes": [list(map(str, b)) for b in pts],
                    "carleson_cost": str(cost),
                    "witness_left_length_mass": list(map(str, witness)),
                    "candidate_boxes": checked,
                    "subset_oracle_complete": n <= 8,
                }
            )
    mixed_cost, mixed_witness, mixed_checks = box_norm(MIXED)
    need(mixed_cost == subset_norm(MIXED), "mixed-height independent identity")
    union = normalized_union()
    intervals = []
    for j in range(-8, 17):
        for m in range(1, 25):
            left, length = Q(j, 8), Q(m, 8)
            mass = box_mass(union, left, length)
            need(mass <= 3 * length, "global cell-normalized Carleson box bound")
            intervals.append(
                {
                    "left": str(left),
                    "length": str(length),
                    "mass": str(mass),
                    "bound": str(3 * length),
                }
            )
    rayleigh = [
        {
            "N": n,
            "unweighted_rayleigh": str(crowded_rayleigh(n)),
            "weighted_rayleigh": str(crowded_rayleigh(n) / n),
        }
        for n in range(1, 17)
    ]
    sparse = []
    for j in range(1, 33):
        total = sum((Q(k, 2**k) for k in range(1, j + 1)), Q(0))
        tail = Q(j + 2, 2**j)
        need(total + tail == 2, "complete dyadic tail identity")
        sparse.append(
            {
                "last_scale": j,
                "sum_j_over_2_power_j": str(total),
                "exact_remaining_tail": str(tail),
            }
        )
    need(
        (len(panel), len(intervals), len(rayleigh), len(sparse)) == (32, 600, 16, 32),
        "declared complete coverage",
    )
    return seal(
        {
            "schema": STEM + "-v1",
            "contract": CONTRACT,
            "sources": BINDINGS,
            "coverage": {
                "cell_families": 32,
                "independent_subset_controls": 17,
                "normalized_boxes": 600,
                "rayleigh": 16,
                "sparse_prefixes": 32,
            },
            "families": panel,
            "mixed": {
                "nodes": [list(map(str, b)) for b in MIXED],
                "carleson_cost": str(mixed_cost),
                "witness_left_length_mass": list(map(str, mixed_witness)),
                "candidate_boxes": mixed_checks,
            },
            "normalized_boxes": intervals,
            "rayleigh": rayleigh,
            "sparse_prefixes": sparse,
            "artifacts": {
                p.relative_to(ROOT).as_posix(): lfhash(p.read_bytes())
                for p in (NOTE, Path(__file__), MANIFEST, TEST)
            },
        }
    )


def check_report(value):
    validate_tree(value)
    need(type(value) is dict and "payload_sha256" in value, "report shape")
    unsigned = {k: v for k, v in value.items() if k != "payload_sha256"}
    need(
        value["payload_sha256"] == hashlib.sha256(canonical(unsigned)).hexdigest(),
        "payload seal",
    )
    need(
        canonical(value) == canonical(build_report()),
        "fresh exact primitive reconstruction",
    )
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--emit", action="store_true")
    modes.add_argument("--emit-sources", action="store_true")
    modes.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.emit_sources:
        value = manifest()
    elif args.check:
        check_report(load_json(FIXTURE.read_bytes()))
        print(
            "PASS exact Carleson crowding controls; cofinal actual-Xi alignment and innerness OPEN"
        )
        return
    else:
        value = build_report()
    print(json.dumps(value, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
