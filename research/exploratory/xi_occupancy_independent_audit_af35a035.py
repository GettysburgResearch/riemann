"""Independent exact arithmetic and hostile review of frozen OC af35a035.

Arithmetic does not import the author implementation. Author code is loaded
only after reconstruction, to test rejection of resealed or primitive attacks.
No analytic theorem or Xi value is certified by this finite review script.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import itertools
import json
import subprocess
from fractions import Fraction as Q
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[2]
SCIENCE = "af35a035a921a8e3164bda3dce95290afc456645"
BASE = "a7479e85fdc2a464cdc753021435cfef7a1f3910"
STEM = "xi_occupancy_carleson_capture"
DIR = "research/exploratory/"
FILES = (
    DIR + "XI_OCCUPANCY_CARLESON_CAPTURE.md",
    DIR + STEM + ".py",
    DIR + STEM + ".json",
    DIR + STEM + ".sources.json",
    "tests/test_" + STEM + ".py",
)
OUT = Path(__file__).with_suffix(".json")


def require(test, text):
    if not test:
        raise ValueError(text)


def canonical(value):
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode()


def lf(raw):
    return raw.replace(b"\r\n", b"\n")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def git_bytes(commit, path):
    return subprocess.check_output(["git", "show", commit + ":" + path], cwd=ROOT)


def subset_cost(points):
    require(1 <= len(points) <= 8, "independent subset coverage cap")
    scores = []
    for count in range(1, len(points) + 1):
        for chosen in itertools.combinations(points, count):
            width = max(
                max(p[1] for p in chosen),
                max(p[0] for p in chosen) - min(p[0] for p in chosen),
            )
            scores.append(sum((p[1] for p in chosen), Q(0)) / width)
    return max(scores)


def oracle_points(kind, n):
    if kind == "dispersed":
        gap, height = Q(1, 2 * n + 2), Q(1, 64 * n * n)
    else:
        gap, height = Q(1, 64 * n * n * (n + 1)), Q(1, 4)
    return tuple((Q(1, 4) + j * gap, height) for j in range(1, n + 1))


def rows_reconstruction(report):
    require(
        report["coverage"]
        == {
            "cell_families": 32,
            "independent_subset_controls": 17,
            "normalized_boxes": 600,
            "rayleigh": 16,
            "sparse_prefixes": 32,
        },
        "exact coverage",
    )
    complete_families = []
    for n in range(1, 17):
        for kind in ("dispersed", "crowded"):
            pts = oracle_points(kind, n)
            height = pts[0][1]
            if kind == "dispersed":
                # Every subset of l>=2 points has diameter >=(l-1)*gap;
                # its score <=2*height/gap<1, whereas singleton score=1.
                if n > 1:
                    require(
                        2 * height < pts[1][0] - pts[0][0], "all-subset spacing proof"
                    )
                cost, width, mass = Q(1), height, height
            else:
                require(pts[-1][0] - pts[0][0] < height, "crowding proof")
                cost, width, mass = Q(n), height, n * height
            if n <= 8:
                require(subset_cost(pts) == cost, "independent subset family")
            widths = {height}
            for a, b in itertools.combinations(pts, 2):
                widths.add(b[0] - a[0])
            complete_families.append(
                {
                    "family": kind,
                    "N": n,
                    "nodes": [list(map(str, b)) for b in pts],
                    "carleson_cost": str(cost),
                    "witness_left_length_mass": list(
                        map(str, (pts[0][0], width, mass))
                    ),
                    "candidate_boxes": len(widths) * n,
                    "subset_oracle_complete": n <= 8,
                }
            )
    require(report["families"] == complete_families, "every family field")
    mixed = (
        (Q(1, 8), Q(1, 8)),
        (Q(1, 4), Q(1, 4)),
        (Q(3, 8), Q(1, 16)),
        (Q(3, 4), Q(1, 2)),
    )
    require(subset_cost(mixed) == Q(7, 4), "mixed independent cost")
    require(
        report["mixed"]
        == {
            "nodes": [list(map(str, b)) for b in mixed],
            "carleson_cost": "7/4",
            "witness_left_length_mass": ["1/8", "1/4", "7/16"],
            "candidate_boxes": 24,
        },
        "mixed complete row",
    )
    union = []
    for cell, kind, n in ((0, "dispersed", 3), (1, "crowded", 4), (2, "dispersed", 5)):
        for x, y in oracle_points(kind, n):
            union.append((x + cell, y, Q(1, n) if kind == "crowded" else Q(1)))
    boxes = []
    for j, m in itertools.product(range(-8, 17), range(1, 25)):
        left, width = Q(j, 8), Q(m, 8)
        mass = sum(
            (y * wt for x, y, wt in union if left <= x <= left + width and y <= width),
            Q(0),
        )
        require(mass <= 3 * width, "independent weighted global box")
        boxes.append(
            {
                "left": str(left),
                "length": str(width),
                "mass": str(mass),
                "bound": str(3 * width),
            }
        )
    require(report["normalized_boxes"] == boxes, "all 600 rows")
    rayleigh = []
    for n in range(1, 17):
        gap = Q(1, 64 * n * n * (n + 1))
        # Difference multiplicities, not the author's double node loop.
        total = Q(n) + sum(
            (2 * Q(n - d) / (1 + 4 * (d * gap) ** 2) for d in range(1, n)), Q(0)
        )
        value = total / n
        require(value >= Q(16 * n, 17), "Gram Rayleigh bound")
        rayleigh.append(
            {
                "N": n,
                "unweighted_rayleigh": str(value),
                "weighted_rayleigh": str(value / n),
            }
        )
    require(report["rayleigh"] == rayleigh, "all Rayleigh fields")
    sparse = []
    for j in range(1, 33):
        tail = Q(j + 2, 2**j)
        sparse.append(
            {
                "last_scale": j,
                "sum_j_over_2_power_j": str(2 - tail),
                "exact_remaining_tail": str(tail),
            }
        )
    require(report["sparse_prefixes"] == sparse, "all sparse fields")
    return sha(canonical([complete_families, report["mixed"], boxes, rayleigh, sparse]))


def load_author():
    spec = importlib.util.spec_from_file_location("reviewed_oc", ROOT / FILES[1])
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def additional_controls(author):
    grid = tuple(itertools.product((Q(0), Q(1, 8), Q(7, 8)), (Q(1, 64), Q(1, 8), Q(1))))
    count = 0
    for n in range(1, 6):
        for pts in itertools.combinations(grid, n):
            require(author.box_norm(pts)[0] == subset_cost(pts), "held-out edge grid")
            count += 1
    repeated = (
        ((Q(0), Q(1)),) * 5,
        ((Q(0), Q(1, 4)), (Q(0), Q(1, 4)), (Q(1, 4), Q(1, 4))),
        ((Q(0), Q(1, 64)), (Q(63, 64), Q(1))),
    )
    for pts in repeated:
        require(
            author.box_norm(pts)[0] == subset_cost(pts), "held-out repeated endpoints"
        )
        count += 1
    return count


def rejection_controls(author, report):
    count = 0

    def reject(call):
        nonlocal count
        try:
            call()
        except (ValueError, TypeError, RecursionError):
            count += 1
            return
        raise ValueError("hostile input accepted")

    mutations = [
        lambda r: r.__setitem__("schema", "wrong"),
        lambda r: r.__setitem__("extra", "unpaid"),
        lambda r: r["families"].pop(),
        lambda r: r["families"][0].__setitem__("N", True),
        lambda r: r["families"][1].__setitem__("carleson_cost", "1/1"),
        lambda r: r["coverage"].__setitem__("normalized_boxes", 599),
        lambda r: r["normalized_boxes"].reverse(),
        lambda r: r["contract"].__setitem__("scope", "unconditional Xi capture"),
        lambda r: r["contract"].__setitem__("no_xi_computation", False),
        lambda r: r["contract"].__setitem__(
            "physical_metric", "weighted physical norm"
        ),
        lambda r: r["contract"].__setitem__("arithmetic_class", "DIRECTED_BALL"),
        lambda r: r["rayleigh"][0].__setitem__("weighted_rayleigh", "0"),
    ]
    for index in range(4):
        mutations.append(
            lambda r, j=index: r["sources"][j].__setitem__("commit", "0" * 40)
        )
    for path in report["artifacts"]:
        mutations.append(lambda r, p=path: r["artifacts"].__setitem__(p, "0" * 64))
    for change in mutations:
        value = copy.deepcopy(report)
        value.pop("payload_sha256")
        change(value)
        forged = author.seal(value)
        reject(lambda v=forged: author.check_report(v))
    original = author.subprocess.check_output
    for row in report["sources"]:

        def corrupted(args, *, cwd, selected=row):
            raw = original(args, cwd=cwd)
            if args[2] == selected["commit"] + ":" + selected["path"]:
                return raw + b"\n"
            return raw

        with mock.patch.object(
            author.subprocess, "check_output", side_effect=corrupted
        ):
            reject(author.authenticate)
    original_read = Path.read_bytes
    for relpath in report["artifacts"]:
        target = ROOT / relpath

        def bad_read(path, *, chosen=target):
            raw = original_read(path)
            return raw + b" " if path == chosen else raw

        with mock.patch.object(Path, "read_bytes", bad_read):
            reject(lambda: author.check_report(report))
    for raw in (
        b'{"x":1,"x":2}',
        b'{"x":1e0}',
        b'{"x":NaN}',
        b'{"x":-Infinity}',
        b"[" * 18 + b"0" + b"]" * 18,
        b" " * 1000001,
    ):
        reject(lambda r=raw: author.load_json(r))
    for bad in (False, 1.0, "1", None, -1, 0, 17, 2**4096):
        reject(lambda n=bad: author.family("crowded", n))
    for bad in (True, Q(1, 2**257), Q(2**257), "1/2", 0.5):
        reject(lambda n=bad: author.exact(n))
    reject(lambda: author.nodes([(Q(0), Q(1))] * 17))
    reject(lambda: author.subset_norm(author.family("dispersed", 9)))
    return count


def build():
    source_hashes = {}
    for path in FILES:
        raw = git_bytes(SCIENCE, path)
        require(lf((ROOT / path).read_bytes()) == lf(raw), "current science drift")
        source_hashes[path] = sha(lf(raw))
    report = json.loads(git_bytes(SCIENCE, FILES[2]))
    manifest = json.loads(git_bytes(SCIENCE, FILES[3]))
    require(manifest["sources"] == report["sources"], "source list equality")
    require(manifest["contract"] == report["contract"], "contract equality")
    require(report["schema"] == STEM + "-v1", "report schema")
    unsigned = {k: v for k, v in report.items() if k != "payload_sha256"}
    require(
        sha(canonical(unsigned)) == report["payload_sha256"], "independent payload seal"
    )
    require(set(report["artifacts"]) == set(FILES) - {FILES[2]}, "four artifacts")
    for path, digest in report["artifacts"].items():
        require(source_hashes[path] == digest, "independent artifact seal")
    require(len(manifest["sources"]) == 4, "four source bindings")
    for row in manifest["sources"]:
        raw = git_bytes(row["commit"], row["path"])
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        require(
            blob == row["git_blob"] and sha(lf(raw)) == row["sha256_lf"],
            "frozen source seal",
        )
    arithmetic_sha = rows_reconstruction(report)
    author = load_author()
    extra = additional_controls(author)
    attacks = rejection_controls(author, report)
    return {
        "schema": "independent-oc-review-af35a035-v1",
        "science": SCIENCE,
        "authoring_base": BASE,
        "science_sha256_lf": source_hashes,
        "source_bindings_checked": 4,
        "own_artifacts_checked": 4,
        "independent_arithmetic_sha256": arithmetic_sha,
        "reconstructed_rows": {
            "families": 32,
            "mixed": 1,
            "boxes": 600,
            "rayleigh": 16,
            "sparse": 32,
        },
        "additional_subset_endpoint_cases": extra,
        "hostile_rejections": attacks,
        "arithmetic_class": "MIXED",
        "components": ["EXACT_RATIONAL", "CERTIFIED_INTEGER_COVERAGE"],
        "rounding": "none",
        "analytic_or_Xi_evaluation_machine_certified": False,
        "scope": "exact frozen finite arithmetic/source audit; analytic verdict is in the separate review note",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    actions = parser.add_mutually_exclusive_group(required=True)
    actions.add_argument("--emit", action="store_true")
    actions.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.emit:
        print(json.dumps(result, sort_keys=True, indent=2))
    else:
        require(json.loads(OUT.read_bytes()) == result, "independent review fixture")
        print(
            "PASS independent OC arithmetic, source seals, endpoints and hostile controls"
        )


if __name__ == "__main__":
    main()
