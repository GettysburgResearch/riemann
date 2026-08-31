"""Read-only replay of the exact-head pass3 source-acquisition plan.

No fetch, ref update, checkout, push, or file write is performed.
The optional remote check observes advertisements; it does not fetch objects.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
SHA = re.compile(r"[0-9a-f]{40}\Z")
TOKENS = re.compile(rb"(?<![0-9a-f])[0-9a-f]{40}(?![0-9a-f])")
MAX_BLOB = 40_000_000


def fail(message):
    raise ValueError(message)


def git(*args, stdin=None):
    result = subprocess.run(
        ["git", "--no-replace-objects", *args],
        cwd=ROOT,
        input=stdin,
        capture_output=True,
        check=True,
    )
    return result.stdout


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def strict_pairs(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            fail("duplicate JSON key")
        out[key] = value
    return out


def load_plan():
    raw = (HERE / "sixhour_source_acquisition_review.json").read_bytes()
    plan = json.loads(raw, object_pairs_hook=strict_pairs)
    seal = plan.pop("payload_sha256")
    if hashlib.sha256(canonical(plan)).hexdigest() != seal:
        fail("plan payload seal mismatch")
    for path, expected in plan["artifacts_sha256_lf"].items():
        got = hashlib.sha256((ROOT / path).read_bytes().replace(b"\r\n", b"\n"))
        if got.hexdigest() != expected:
            fail("resident artifact mismatch: " + path)
    return plan


def object_types(names):
    names = sorted(set(names))
    if any(type(s) is not str or SHA.fullmatch(s) is None for s in names):
        fail("noncanonical commit candidate")
    data = git(
        "cat-file",
        "--batch-check=%(objectname) %(objecttype)",
        stdin=("\n".join(names) + "\n").encode(),
    )
    return dict(line.split(" ", 1) for line in data.decode().splitlines())


def ancestors(tips):
    if any(v != "commit" for v in object_types(tips).values()):
        fail("ancestry tip is not an actual commit")
    return set(
        git("rev-list", "--stdin", stdin=("\n".join(tips) + "\n").encode())
        .decode()
        .split()
    )


def frozen_blobs(queries):
    output = git("cat-file", "--batch", stdin=("\n".join(queries) + "\n").encode())
    cursor = 0
    for query in queries:
        end = output.index(b"\n", cursor)
        header = output[cursor:end].decode().split()
        if len(header) != 3 or header[1] != "blob":
            fail("missing/nonblob frozen scan input: " + query)
        size = int(header[2])
        if size < 0 or size > MAX_BLOB:
            fail("frozen scan blob cap")
        start = end + 1
        blob = output[start : start + size]
        if len(blob) != size or output[start + size : start + size + 1] != b"\n":
            fail("truncated Git batch")
        digest = hashlib.sha1(b"blob " + str(size).encode() + b"\0" + blob)
        if digest.hexdigest() != header[0]:
            fail("Git blob identity mismatch")
        cursor = start + size + 1
        yield query, blob
    if cursor != len(output):
        fail("surplus Git batch bytes")


def scan(plan):
    candidates = {plan["prospective_ancestry"]["QR_design"]}
    for report in plan["reports"].values():
        candidates.update(report["source_commits"])
        candidates.add(report["head"])
    file_counts = {}
    for programme in ("S", "G"):
        report = plan["reports"][programme]
        paths = git("diff", "--name-only", report["base"], report["head"])
        paths = [
            p
            for p in paths.decode().splitlines()
            if p.endswith((".md", ".py", ".json"))
        ]
        extras = (
            [
                "research/riemann-structures/CONTINUATION_SOURCE_REPLAY.md",
                "research/riemann-structures/RIEMANN_STRUCTURES_CONTINUATION_RESULTS.md",
            ]
            if programme == "S"
            else ["research/l-families/atlas/generalized/CONTINUATION_RESULTS.md"]
        )
        paths = sorted(set(paths + extras))
        file_counts[programme] = len(paths)
        for _, blob in frozen_blobs([report["head"] + ":" + p for p in paths]):
            candidates.update(s.decode() for s in TOKENS.findall(blob))
        messages = git("log", "--format=%B", report["base"] + ".." + report["head"])
        candidates.update(s.decode() for s in TOKENS.findall(messages))
    types = object_types(candidates)
    identities = {s for s in candidates if types[s] == "commit"}
    expected = plan["conservative_scan"]
    if file_counts != expected["file_counts"]:
        fail("frozen file-panel drift")
    if identities != set(expected["commit_witnesses"]):
        fail("literal commit-identity panel drift")
    if len(identities) != expected["commit_count"]:
        fail("commit count drift")
    return identities, file_counts


def replay(plan, replay_manifests=False):
    workflow = plan["workflow"]
    raw = git("show", workflow["commit"] + ":" + workflow["path"])
    if hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest() != workflow["sha256_lf"]:
        fail("frozen closure workflow hash")
    if replay_manifests:
        namespace = {
            "__name__": "frozen_read_only_closure",
            "__file__": str(ROOT / workflow["path"]),
        }
        # Exact Git source and LF hash verified immediately above; read-only workflow.
        exec(compile(raw, workflow["path"], "exec"), namespace)  # noqa: S102
        for name, report in plan["reports"].items():
            got = namespace["build"](
                report["head"], report["base"], report["programme"]
            )
            if canonical(got) != canonical(report):
                fail("full manifest replay differs: " + name)
    identities, file_counts = scan(plan)
    prospective = plan["prospective_ancestry"]
    current = ancestors([prospective["S"], prospective["G"]])
    retained = ancestors(list(plan["retained_archive_refs"].values()))
    planned = ancestors([prospective["QR_design"]])
    if prospective["QT"] not in planned:
        fail("QR design no longer retains the exact QT ancestor")
    uncovered = identities - current - retained - planned
    expected = plan["conservative_scan"]
    if uncovered != set(expected["uncovered"]):
        fail("uncovered identity set drift")
    coverage = {
        "current": len(identities & current),
        "archives_only": len(identities & (retained - current)),
        "planned_qr_only": len(identities & (planned - current - retained)),
        "uncovered": len(uncovered),
    }
    if coverage != expected["coverage_counts"]:
        fail("coverage counts drift")
    additions = plan["proposed_new_archive_refs"]
    new_ancestors = {}
    for ref, row in additions.items():
        if not ref.startswith("refs/heads/codex/review-sources-"):
            fail("unexpected proposed ref namespace")
        new_ancestors[row["commit"]] = ancestors([row["commit"]])
        covered = uncovered & new_ancestors[row["commit"]]
        if covered != set(row["covers_uncovered"]):
            fail("proposed archive coverage drift")
    if uncovered - set().union(*new_ancestors.values()):
        fail("proposed archives leave a gap")
    maxima = {
        s
        for s in uncovered
        if not any(s != t and s in ancestors([t]) for t in uncovered)
    }
    if maxima != set(expected["maximal_uncovered"]) or maxima != set(new_ancestors):
        fail("maximal uncovered states differ")
    return {
        "status": "PASS_PREPUBLICATION_LOCAL_PLAN",
        "frozen_files": file_counts,
        "commit_identities": len(identities),
        "coverage": coverage,
        "retained_archive_refs": len(plan["retained_archive_refs"]),
        "proposed_archive_refs": len(additions),
        "full_manifest_replay": replay_manifests,
        "remote_fetch_performed": False,
    }


def check_remote(plan):
    lines = git("ls-remote", plan["origin"]).decode().splitlines()
    refs = {ref: sha for sha, ref in (line.split() for line in lines)}
    for ref, expected in plan["retained_archive_refs"].items():
        if refs.get(ref) != expected:
            fail("retained archive missing or moved: " + ref)
    present = 0
    for ref, row in plan["proposed_new_archive_refs"].items():
        if ref in refs:
            if refs[ref] != row["commit"]:
                fail("proposed archive advertised at wrong identity: " + ref)
            present += 1
    return {
        "retained32_exact": True,
        "proposed8_currently_advertised_exact": present,
        "missing_proposed_is_planning_not_failure": True,
        "fresh_fetch_verified": False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--replay-manifests", action="store_true")
    parser.add_argument("--check-remote", action="store_true")
    parser.add_argument("--verify-descendant", action="append", nargs=2, default=[])
    args = parser.parse_args()
    plan = load_plan()
    result = replay(plan, args.replay_manifests)
    if args.check_remote:
        result["live_read_only_advertisement"] = check_remote(plan)
    for tip, required in args.verify_descendant:
        if required not in ancestors([tip]):
            fail("required exact commit is not an ancestor of supplied final tip")
    result["additional_exact_ancestry_checks"] = len(args.verify_descendant)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
