"""Explicit AND manifest-inherited local source closure; workflow evidence only.

Supports legacy generalized-L top-level commit defaults and the archimedean
single-file lock. Unknown implicit bindings fail closed. Never fetches, writes
scientific data, or substitutes branch tips for exact identities.
"""

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SHA = re.compile(r"[0-9a-f]{40}\Z")
MAX_BLOB = 40_000_000
HASH_KEYS = ("sha256_lf", "file_sha256_lf_normalized")
CACHE = {}
COMMIT_CACHE = set()


def need(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def git(*args):
    return subprocess.check_output(["git", "--no-replace-objects", *args], cwd=ROOT)


def validate_commit(commit):
    need(type(commit) is str and SHA.fullmatch(commit), "exact source commit")
    if commit not in COMMIT_CACHE:
        need(git("cat-file", "-t", commit).strip() == b"commit", "Git commit type")
        COMMIT_CACHE.add(commit)


def source(commit, path):
    validate_commit(commit)
    need(
        type(path) is str
        and path
        and not any(ord(char) < 32 or ord(char) == 127 for char in path)
        and "\\" not in path
        and ":" not in path
        and all(part not in ("", ".", "..") for part in path.split("/")),
        "canonical relative source path",
    )
    key = commit, path
    if key not in CACHE:
        obj = git("rev-parse", commit + ":" + path).decode().strip()
        size = int(git("cat-file", "-s", obj))
        need(size <= MAX_BLOB, "source byte cap")
        data = git("show", commit + ":" + path)
        need(len(data) == size, "source size")
        blob = hashlib.sha1(b"blob " + str(size).encode() + b"\0" + data).hexdigest()
        need(blob == obj, "Git source blob identity")
        CACHE[key] = data, blob, digest(data.replace(b"\r\n", b"\n"))
    return CACHE[key]


def strict_json(data):
    def pairs(items):
        out = {}
        for key, value in items:
            need(key not in out, "duplicate JSON key")
            out[key] = value
        return out

    def reject(_):
        raise ValueError("noninteger JSON primitive")

    return json.loads(
        data, object_pairs_hook=pairs, parse_float=reject, parse_constant=reject
    )


def bindings(document):
    schema = document.get("schema", "")
    defaults = [
        (key, document[key])
        for key in ("imported_parent_state_commit", "source_commit", "base_commit")
        if key in document
    ]
    legacy = (
        schema.startswith("riemann.atlas.generalized.")
        or schema == "graded-parent-global-boundary-sources-v1"
    )

    def walk(value, pointer=""):
        if type(value) is dict:
            sealed = "git_blob" in value or any(key in value for key in HASH_KEYS)
            if "path" in value and ("commit" in value or sealed):
                if "commit" in value:
                    yield pointer, value, "explicit_commit"
                else:
                    need(
                        legacy and defaults,
                        "unknown implicit binding: " + schema + pointer,
                    )
                    key, commit = defaults[0]
                    yield pointer, dict(value, commit=commit), "inherited_" + key
            for key in sorted(value):
                escaped = key.replace("~", "~0").replace("/", "~1")
                yield from walk(value[key], pointer + "/" + escaped)
        elif type(value) is list:
            for index, child in enumerate(value):
                yield from walk(child, pointer + "/" + str(index))

    yield from walk(document)
    if "frozen_programme_path" in document:
        need(
            schema == "archimedean-ladder-source-lock-v1",
            "unknown special source schema",
        )
        yield (
            "/frozen_programme_path",
            {
                "commit": document["source_commit"],
                "path": document["frozen_programme_path"],
                "git_blob": document["frozen_programme_blob"],
                "sha256_lf": document["frozen_programme_sha256_lf"],
            },
            "archimedean_single_file_lock",
        )


def build(head, base, programme):
    validate_commit(head)
    validate_commit(base)
    need(programme in ("S", "G"), "programme identity")
    roots = sorted(
        path
        for path in git("diff", "--no-renames", "--name-only", base, head)
        .decode()
        .splitlines()
        if path.endswith(".sources.json")
    )
    pending = [(head, path) for path in roots]
    seen = set()
    manifests = []
    edges = []
    catalog = {}
    implicit = []
    while pending:
        key = min(pending)
        pending.remove(key)
        if key in seen:
            continue
        seen.add(key)
        need(len(seen) <= 1000, "manifest cap")
        data, blob, content_hash = source(*key)
        doc = strict_json(data)
        need(type(doc) is dict, "source manifest object")
        rows = list(bindings(doc))
        manifests.append(
            {
                "commit": key[0],
                "path": key[1],
                "git_blob": blob,
                "sha256_lf": content_hash,
                "outgoing_edges": len(rows),
            }
        )
        for pointer, row, method in rows:
            target = row["commit"], row["path"]
            _, target_blob, target_hash = source(*target)
            if "git_blob" in row:
                need(row["git_blob"] == target_blob, "declared Git blob mismatch")
            for hash_key in HASH_KEYS:
                if hash_key in row:
                    need(row[hash_key] == target_hash, "declared LF SHA mismatch")
            edge = [key[0], key[1], pointer, target[0], target[1], method]
            edges.append(edge)
            need(len(edges) <= 10000, "edge cap")
            catalog[target] = {
                "commit": target[0],
                "path": target[1],
                "git_blob": target_blob,
                "sha256_lf": target_hash,
            }
            if method != "explicit_commit":
                implicit.append(edge)
            if target[1].endswith(".sources.json"):
                pending.append(target)
    source_catalog = [catalog[key] for key in sorted(catalog)]
    commits = sorted({key[0] for key in catalog})
    payload = {
        "schema": "sixhour-complete-local-manifest-closure-v1",
        "programme": programme,
        "head": head,
        "base": base,
        "counts": {
            "roots": len(roots),
            "manifest_versions": len(manifests),
            "edges": len(edges),
            "source_versions": len(catalog),
            "source_commits": len(commits),
            "implicit_edges": len(implicit),
        },
        "root_paths": roots,
        "source_commits": commits,
        "manifest_catalog": sorted(manifests, key=lambda r: (r["commit"], r["path"])),
        "edges_sha256": digest(canonical(sorted(edges))),
        "source_catalog_sha256": digest(canonical(source_catalog)),
        "implicit_resolutions": sorted(implicit),
        "all_local_objects_present": True,
        "all_declared_seals_match": True,
        "contract": {
            "scope": "Local manifest-binding closure, including explicit legacy defaults; not all prose or executable dependencies.",
            "inherited_precedence": [
                "imported_parent_state_commit",
                "source_commit",
                "base_commit",
            ],
            "implicit_schema_scope": [
                "riemann.atlas.generalized.*",
                "graded-parent-global-boundary-sources-v1",
            ],
            "special_schema": "archimedean-ladder-source-lock-v1",
            "blob_limit_bytes": MAX_BLOB,
            "remote_acquisition_verified": False,
            "external_papers_authenticated": False,
        },
    }
    return dict(payload, payload_sha256=digest(canonical(payload)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--head", required=True)
    parser.add_argument("--base", required=True)
    parser.add_argument("--programme", required=True, choices=["S", "G"])
    parser.add_argument("--check-report")
    args = parser.parse_args()
    report = build(args.head, args.base, args.programme)
    if args.check_report:
        recorded = strict_json(Path(args.check_report).read_bytes())
        need(
            canonical(recorded) == canonical(report),
            "fresh complete closure report mismatch",
        )
        print(
            json.dumps({"status": "PASS", "counts": report["counts"]}, sort_keys=True)
        )
    else:
        print(json.dumps(report, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
