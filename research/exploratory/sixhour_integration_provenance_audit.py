"""Frozen S/G integration provenance audit; standard library only, no science replay."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STEM = "sixhour_integration_provenance_audit"
REPORT = Path(__file__).with_suffix(".json")
HEADS = {
    "S": {
        "head": "245943ccd1b381e2ca80625546a6851e85978057",
        "public_base": "1904d20cdb76ecd26e0e63472625da930075303e",
        "pr_base": "b870366141fe8d5f43d5b81f6e50a67d2a888070",
        "reviews": {
            "native": "a9e1587c90321e2f54e0a3c08a5ca74a15879f3b",
            "offaxis": "94c5c279283463eb472b8162b4c26db359b82f56",
            "box": "3adfd9cb4013052180fb973c55deed49bad4a809",
            "microscale": "3f00e46e79cf928f724a9170116cb69e14f7b02f",
            "globalsaddle": "6d122a1a5114d957ada9956ad4d10db4aad44316",
            "fixedlambda": "26201b3a7de6293ea47621f06b45dd9837521a20",
            "FCmetadata": "ffc2d0a5d8e24ab13565e51d0a0adfb36102de18",
            "lowpass": "5334c3776ce204a5982fac989a8b4f87dc645c35",
            "radial": "6fcbec7e579db751c1d0ebc60f92a70a15945617",
            "crowding": "bda894b84013d377b68c3602d4e8bb06e6f42e68",
            "heldout": "75bcae9036b82bc79b032df4bb26ddd5ed609130",
        },
    },
    "G": {
        "head": "3f5441b26d7f2e64247a4e4d52eb82eb7e27dbb1",
        "public_base": "7ee5e024e1d8c3dd187b40ea5d48f9c9ff46d95e",
        "pr_base": "10446e8ea9c55162c317810f63c1f7a379466459",
        "reviews": {
            "bridge": "acd91a621244872d49e0e4dfde76775879eadfc1",
            "chambers": "5bfbad61eb035168fdc4abb265ecb4c2f2d34d51",
            "ladder": "c29ae6f3d134e076fa41aef9ae39920478f16ac0",
            "heckeoriginal": "591d6ade9bcfe218e1519bbab91cce3d2c2ed305",
            "heckemetadata": "3575c8274a887bc5de29aa41749cac37f49b73cd",
            "FI": "0f29fd2d687c57402a14723dde2bc2b7e74fa317",
            "CF": "1148ed1fceedf3e103397ca426df98aeaafa5865",
            "SD": "a66879ab211052983f8849c8336b7500ecadffbf",
            "MP": "8b2bb44f3b82059b6e3721aba9b2cff2a70fd7d0",
        },
    },
}

EXPECTED = {
    "S": [11, 81, 32, 32, 37, 258, 113, 41],
    "G": [9, 59, 35, 35, 49, 266, 102, 34],
}
REMOTE_EVIDENCE = [
    {
        "pin": "cdad9e88097db4925c3bbbf731f7d1ae1a9e6c57",
        "advertised_head": "cdad9e88097db4925c3bbbf731f7d1ae1a9e6c57",
        "ref": "refs/heads/research/gpt56-pro/107100-xi-reverse-rolle-execution",
    },
    {
        "pin": "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc",
        "advertised_head": "59654c02d13545d6c8c0972315db2628e9efa1f6",
        "ref": "refs/heads/research/gpt56-pro/102700-half-divisor-defect-factorization",
    },
]
CAPS = {
    "blob_bytes": 16_000_000,
    "report_bytes": 2_000_000,
    "json_nodes": 100_000,
    "json_depth": 64,
    "tree_paths": 100_000,
    "manifest_versions": 500,
    "source_versions": 2_000,
    "edges": 5_000,
}
SHA = re.compile(r"[0-9a-f]{40}\Z")


def need(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return (
        json.dumps(
            value,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=True,
            allow_nan=False,
        ).encode("ascii")
        + b"\n"
    )


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def lf(raw):
    return raw.replace(b"\r\n", b"\n")


def decode(raw):
    need(type(raw) is bytes and len(raw) <= CAPS["report_bytes"], "JSON byte cap")

    def pairs(items):
        out = {}
        for key, value in items:
            need(key not in out, "duplicate JSON key")
            out[key] = value
        return out

    def bad(_):
        raise ValueError("noninteger JSON number")

    out = json.loads(raw, object_pairs_hook=pairs, parse_float=bad, parse_constant=bad)
    count = 0

    def visit(value, depth):
        nonlocal count
        count += 1
        need(count <= CAPS["json_nodes"] and depth <= CAPS["json_depth"], "JSON cap")
        need(type(value) in (dict, list, str, int, bool, type(None)), "JSON type")
        if type(value) is dict:
            for key, child in value.items():
                need(type(key) is str, "JSON key")
                visit(child, depth + 1)
        elif type(value) is list:
            for child in value:
                visit(child, depth + 1)

    visit(out, 0)
    return out


def source_rows(value, pointer=""):
    if type(value) is dict:
        if type(value.get("commit")) is str and type(value.get("path")) is str:
            yield pointer, value
        for key in sorted(value):
            escaped = key.replace("~", "~0").replace("/", "~1")
            yield from source_rows(value[key], pointer + "/" + escaped)
    elif type(value) is list:
        for index, child in enumerate(value):
            yield from source_rows(child, pointer + "/" + str(index))


class Git:
    def __init__(self, root):
        self.root = root
        self.trees = {}
        self.raw = {}

    def call(self, *args):
        run = subprocess.run(
            ["git", "--no-replace-objects", *args],
            cwd=self.root,
            check=False,
            capture_output=True,
        )
        need(run.returncode == 0, "Git command failed: " + repr(args))
        return run.stdout

    def ancestor(self, first, second):
        run = subprocess.run(
            [
                "git",
                "--no-replace-objects",
                "merge-base",
                "--is-ancestor",
                first,
                second,
            ],
            cwd=self.root,
            check=False,
            capture_output=True,
        )
        need(run.returncode in (0, 1), "Git ancestry failure")
        return run.returncode == 0

    def tree(self, commit):
        need(type(commit) is str and SHA.fullmatch(commit) is not None, "exact commit")
        if commit not in self.trees:
            rows = {}
            for line in self.call("ls-tree", "-r", commit).decode().splitlines():
                prefix, path = line.split("\t", 1)
                mode, kind, digest = prefix.split()
                need(
                    kind == "blob" and mode in ("100644", "100755", "120000"),
                    "tree type",
                )
                rows[path] = digest
            need(len(rows) <= CAPS["tree_paths"], "tree path cap")
            self.trees[commit] = rows
        return self.trees[commit]

    def read(self, commit, path):
        blob = self.tree(commit).get(path)
        need(blob is not None, "missing frozen path: " + commit + ":" + path)
        if blob not in self.raw:
            raw = self.call("show", commit + ":" + path)
            need(len(raw) <= CAPS["blob_bytes"], "Git source byte cap")
            actual = hashlib.sha1(
                b"blob " + str(len(raw)).encode() + b"\0" + raw
            ).hexdigest()
            need(actual == blob, "Git object byte identity")
            self.raw[blob] = raw
        return self.raw[blob]

    def changes(self, base, head):
        rows = []
        for line in (
            self.call("diff", "--no-renames", "--name-status", base, head)
            .decode()
            .splitlines()
        ):
            status, path = line.split("\t", 1)
            rows.append((status, path))
        return rows


def inventory(git, config):
    versions = {}
    for name, commit in sorted(config["reviews"].items()):
        need(git.ancestor(commit, config["head"]), "review not merged: " + name)
        for status, path in git.changes(config["public_base"], commit):
            need(status == "A", "review modifies public-baseline path: " + path)
            versions.setdefault(path, {})[name] = git.tree(commit)[path]
    actual = {
        path: status
        for status, path in git.changes(config["public_base"], config["head"])
    }
    need(set(actual) == set(versions), "combined path inventory mismatch")
    records = []
    for path in sorted(versions):
        blob = git.tree(config["head"])[path]
        need(
            actual[path] == "A" and blob in versions[path].values(),
            "unreviewed tree version",
        )
        records.append(
            {"path": path, "combined_blob": blob, "review_versions": versions[path]}
        )
    return records


def closure(git, head, roots):
    pending = [(head, path) for path in roots]
    seen, edges, sources, manifests = set(), [], {}, []
    while pending:
        key = min(pending)
        pending.remove(key)
        if key in seen:
            continue
        seen.add(key)
        need(len(seen) <= CAPS["manifest_versions"], "manifest cap")
        raw = git.read(*key)
        rows = []
        for pointer, row in source_rows(decode(raw)):
            target = row["commit"], row["path"]
            source = git.read(*target)
            blob = git.tree(target[0])[target[1]]
            digest = sha(lf(source))
            if "git_blob" in row:
                need(row["git_blob"] == blob, "source Git seal")
            if "sha256_lf" in row:
                need(row["sha256_lf"] == digest, "source LF seal")
            sources[target] = {
                "commit": target[0],
                "path": target[1],
                "git_blob": blob,
                "sha256_lf": digest,
            }
            edge = [key[0], key[1], pointer, target[0], target[1]]
            edges.append(edge)
            rows.append(edge)
            need(
                len(edges) <= CAPS["edges"] and len(sources) <= CAPS["source_versions"],
                "closure cap",
            )
            if target[1].endswith(".sources.json"):
                pending.append(target)
        manifests.append(
            {
                "commit": key[0],
                "path": key[1],
                "git_blob": git.tree(key[0])[key[1]],
                "sha256_lf": sha(lf(raw)),
                "outgoing_edges": len(rows),
                "outgoing_edges_sha256": sha(canonical(sorted(rows))),
            }
        )
    catalog = [sources[key] for key in sorted(sources)]
    commits = sorted({key[0] for key in sources})
    return {
        "root_manifests": roots,
        "manifest_versions": sorted(
            manifests, key=lambda row: (row["commit"], row["path"])
        ),
        "edges_count": len(edges),
        "edges_sha256": sha(canonical(sorted(edges))),
        "source_versions_count": len(sources),
        "source_catalog_sha256": sha(canonical(catalog)),
        "source_commits": commits,
        "source_commits_not_ancestors_of_combined_head": [
            c for c in commits if not git.ancestor(c, head)
        ],
        "missing_sources": [],
        "seal_mismatches": [],
    }


def imports(git, head, paths):
    local = {Path(path).stem for path in git.tree(head) if path.endswith(".py")}
    out = {}
    for path in sorted(paths):
        if not path.endswith(".py"):
            continue
        names = set()
        for node in ast.walk(ast.parse(git.read(head, path))):
            if isinstance(node, ast.Import):
                names.update(alias.name.split(".")[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                names.add(node.module.split(".")[0])
        extra = names - local - sys.stdlib_module_names - {"__future__", "tests"}
        need(extra <= {"flint", "sympy", "mpmath"}, "unclassified external import")
        if extra:
            out[path] = sorted(extra)
    return out


def literal_assignments(raw):
    out = {}
    for node in ast.parse(raw).body:
        if (
            isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
        ):
            try:
                out[node.targets[0].id] = ast.literal_eval(node.value)
            except (ValueError, TypeError):
                pass
    return out


def helper_caveat(git):
    head = HEADS["S"]["head"]
    path = "research/exploratory/xi_fixed_lambda_joint_independent_review.py"
    raw = git.read(head, path)
    values = literal_assignments(raw)
    expected = values["DATA_HASH"]
    old = sha(lf(git.read(values["SCIENCE"], values["DATA_PATH"])))
    current = sha(lf(git.read(head, values["DATA_PATH"])))
    need(expected == old and old != current, "historical FC fixture lock must differ")
    tree = ast.parse(raw)
    routine = next(
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == "source_fixture"
    )
    comparisons = [node for node in ast.walk(routine) if isinstance(node, ast.Compare)]
    need(
        any(
            isinstance(node.left, ast.Call)
            and isinstance(node.left.func, ast.Name)
            and node.left.func.id == "lfhash"
            and isinstance(node.left.args[0], ast.Call)
            and isinstance(node.left.args[0].func, ast.Attribute)
            and node.left.args[0].func.attr == "read_bytes"
            and len(node.comparators) == 1
            and isinstance(node.comparators[0], ast.Name)
            and node.comparators[0].id == "DATA_HASH"
            for node in comparisons
        ),
        "literal historical local-byte comparison",
    )
    return {
        "helper": path,
        "helper_blob": git.tree(head)[path],
        "historical_science": values["SCIENCE"],
        "fixture": values["DATA_PATH"],
        "expected_original_sha256_lf": expected,
        "combined_sha256_lf": current,
        "expected_combined_failure": "ValueError: current source fixture",
        "replay_at": HEADS["S"]["reviews"]["fixedlambda"],
        "science_producer_failure": False,
    }


def report(git):
    groups = {}
    for name, config in sorted(HEADS.items()):
        files = inventory(git, config)
        changed = [path for _, path in git.changes(config["pr_base"], config["head"])]
        tests = sorted(
            p for p in changed if p.startswith("tests/test_") and p.endswith(".py")
        )
        roots = sorted(p for p in changed if p.endswith(".sources.json"))
        source = closure(git, config["head"], roots)
        counts = [
            len(config["reviews"]),
            len(files),
            len(tests),
            len(roots),
            len(source["manifest_versions"]),
            source["edges_count"],
            source["source_versions_count"],
            len(source["source_commits"]),
        ]
        need(counts == EXPECTED[name], "fixed complete coverage counts: " + name)
        groups[name] = {
            **config,
            "inventory": files,
            "test_modules": tests,
            "external_imports": imports(git, config["head"], changed),
            "closure": source,
            "coverage_counts": counts,
        }
    for row in REMOTE_EVIDENCE:
        need(
            git.ancestor(row["pin"], row["advertised_head"]), "recorded remote ancestry"
        )
    out = {
        "schema": STEM + "-v1",
        "contract": {
            "scope": "workflow/provenance only; not a scientific theorem or full test-suite replay",
            "arithmetic_class": "CERTIFIED_INTEGER_COVERAGE",
            "rounding": "none",
            "source_access": "git --no-replace-objects show at exact commits; no release-worktree reads",
            "manifest_version": "ordered pair (commit,path), even if the Git blob is reused",
            "edge": "each recursive JSON dict with string commit/path, counted once per occurrence in each visited manifest version",
            "closure_recursion": "only source paths ending .sources.json are traversed; prose citations and executable imports are not inferred edges",
            "counts_order": [
                "review_heads",
                "added_paths",
                "test_modules",
                "root_manifests",
                "manifest_versions",
                "edges",
                "source_versions",
                "source_commits",
            ],
            "caps": CAPS,
        },
        "groups": groups,
        "historical_helper_caveat": helper_caveat(git),
        "remote_reachability_observation": {
            "observed_date": "2026-08-31",
            "method": "git ls-remote origin exact named heads, followed by local object ancestry",
            "live_ref_check_default": False,
            "scope": "historical observation only; offline replay authenticates object ancestry, not current advertisement",
            "rows": REMOTE_EVIDENCE,
        },
        "interpreter_plan": {
            "ball_modules": [
                "xi_companion_off_axis_ball_certificates",
                "xi_companion_box_count_compression",
                "xi_fixed_lambda_joint_box_compression",
                "xi_fixed_lambda_heldout_alignment",
                "xi_laplace_low_pass_lower_bound",
            ],
            "ball_runtime": "pinned native-xi-pass3-runtime Python with flint and mpmath; no sympy or numpy",
            "other_runtime": "system Python3.12 with sympy and mpmath; no flint",
            "do_not_install_into_pinned_runtime": True,
            "static_import_scan_not_runtime_installation_certificate": True,
        },
    }
    return {**out, "payload_sha256": sha(canonical(out))}


def verify_report(value, actual):
    need(type(value) is dict and "payload_sha256" in value, "report shape")
    unsigned = {key: item for key, item in value.items() if key != "payload_sha256"}
    need(value["payload_sha256"] == sha(canonical(unsigned)), "report payload seal")
    need(
        canonical(value) == canonical(actual), "fresh fixed-Git reconstruction mismatch"
    )


def self_test():
    bad_inputs = [
        b'{"x":1,"x":2}',
        b'{"x":NaN}',
        b'{"x":1.0}',
        b"[" * 70 + b"0" + b"]" * 70,
    ]
    for raw in bad_inputs:
        try:
            decode(raw)
        except (ValueError, RecursionError):
            continue
        raise ValueError("decoder accepted hostile input")
    sample = {
        "a": [{"commit": "a" * 40, "path": "x.sources.json"}],
        "b": {"commit": "a" * 40, "path": "x.sources.json"},
    }
    need(len(list(source_rows(sample))) == 2, "edge occurrence multiplicity")
    good = {"x": 1}
    sealed = {**good, "payload_sha256": sha(canonical(good))}
    verify_report(sealed, sealed)
    for mutant in (
        {"x": 2, "payload_sha256": sealed["payload_sha256"]},
        {"x": 2, "payload_sha256": sha(canonical({"x": 2}))},
        {"x": True, "payload_sha256": sha(canonical({"x": True}))},
    ):
        try:
            verify_report(mutant, sealed)
        except ValueError:
            continue
        raise ValueError("report accepted hostile input")
    print("PASS: 4 decoder controls, 3 report mutations, occurrence coverage")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--emit", action="store_true")
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--self-test", action="store_true")
    parser.add_argument(
        "--verify-remote",
        action="store_true",
        help="optional live read-only ls-remote; never fetches",
    )
    args = parser.parse_args()
    if args.self_test:
        need(not args.verify_remote, "self-test is offline")
        self_test()
        return
    git = Git(ROOT)
    if args.verify_remote:
        raw = git.call("ls-remote", "origin", *(row["ref"] for row in REMOTE_EVIDENCE))
        actual = {
            ref: commit
            for commit, ref in (line.split() for line in raw.decode().splitlines())
        }
        need(
            actual == {row["ref"]: row["advertised_head"] for row in REMOTE_EVIDENCE},
            "remote advertisements changed",
        )
    value = report(git)
    if args.emit:
        sys.stdout.buffer.write(canonical(value))
    else:
        need(REPORT.stat().st_size <= CAPS["report_bytes"], "report byte cap")
        verify_report(decode(REPORT.read_bytes()), value)
        print(
            "PASS: fixed S/G inventory, 67 test modules, 524 source edges; historical FC helper caveat retained"
        )


if __name__ == "__main__":
    main()
