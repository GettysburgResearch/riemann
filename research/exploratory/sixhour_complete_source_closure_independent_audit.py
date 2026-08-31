"""Independent Git-batch/BFS reference for the complete local manifest closure."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import subprocess
from collections import deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AUDITED = "6b679973888841e56703ccf40ffe88e0574c1f01"
PREDECESSOR = "0c7c1192aa683daf6cc473fd168a7cf6cc7e3bb7"
PATH = "research/exploratory/sixhour_complete_source_closure.py"
REGRESSIONS = [
    (
        "old_G",
        "7ee5e024e1d8c3dd187b40ea5d48f9c9ff46d95e",
        "10446e8ea9c55162c317810f63c1f7a379466459",
        "G",
        [27, 43, 246, 104, 27, 75],
    ),
    (
        "combined_S",
        "245943ccd1b381e2ca80625546a6851e85978057",
        "b870366141fe8d5f43d5b81f6e50a67d2a888070",
        "S",
        [32, 37, 259, 113, 41, 1],
    ),
    (
        "combined_G",
        "3f5441b26d7f2e64247a4e4d52eb82eb7e27dbb1",
        "10446e8ea9c55162c317810f63c1f7a379466459",
        "G",
        [35, 55, 341, 147, 43, 75],
    ),
]
COUNT_KEYS = [
    "roots",
    "manifest_versions",
    "edges",
    "source_versions",
    "source_commits",
    "implicit_edges",
]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def git(*args, input_data=None):
    return subprocess.check_output(
        ["git", "--no-replace-objects", *args], cwd=ROOT, input=input_data
    )


def load_audited():
    frozen = git("show", AUDITED + ":" + PATH)
    require(
        (ROOT / PATH).read_bytes().replace(b"\r\n", b"\n") == frozen,
        "audited local script changed",
    )
    spec = importlib.util.spec_from_file_location("closure_audited", ROOT / PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ReferenceReader:
    """Read batches with cat-file, not the audited source()/git-show route."""

    def __init__(self):
        self.cache = {}
        self.commits = set()

    def fill(self, pairs):
        missing = sorted(set(pairs) - self.cache.keys())
        commit_ids = sorted({c for c, _ in missing} - self.commits)
        if commit_ids:
            output = (
                git(
                    "cat-file",
                    "--batch-check=%(objectname) %(objecttype)",
                    input_data=("\n".join(commit_ids) + "\n").encode(),
                )
                .decode()
                .splitlines()
            )
            require(
                output == [c + " commit" for c in commit_ids], "reference commit types"
            )
            self.commits.update(commit_ids)
        if not missing:
            return
        raw = git(
            "cat-file",
            "--batch",
            input_data=("".join(c + ":" + p + "\n" for c, p in missing)).encode(),
        )
        offset = 0
        for pair in missing:
            end = raw.index(b"\n", offset)
            name, kind, size = raw[offset:end].split()
            require(kind == b"blob", "reference object must be blob")
            length = int(size)
            require(0 <= length <= 40_000_000, "reference source size cap")
            start = end + 1
            data = raw[start : start + length]
            offset = start + length + 1
            require(raw[offset - 1 : offset] == b"\n", "batch delimiter")
            calculated = hashlib.sha1(
                b"blob " + str(length).encode() + b"\0" + data
            ).hexdigest()
            require(calculated.encode() == name, "independent Git blob identity")
            self.cache[pair] = (data, calculated, digest(data.replace(b"\r\n", b"\n")))
        require(offset == len(raw), "batch exhausted")

    def get(self, pair):
        self.fill([pair])
        return self.cache[pair]


def strict_load(data):
    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, "reference duplicate key")
            result[key] = value
        return result

    def reject(_):
        raise ValueError("reference noninteger JSON")

    result = json.loads(
        data, object_pairs_hook=pairs, parse_float=reject, parse_constant=reject
    )
    require(type(result) is dict, "reference manifest object")
    return result


def reference_rows(document):
    """Independent iterative traversal, with explicit source precedence."""
    schema = document.get("schema", "")
    require(type(schema) is str, "reference schema string")
    default = None
    for key in ["base_commit", "source_commit", "imported_parent_state_commit"]:
        if key in document:
            default = (key, document[key])
    stack = deque([("", document)])
    result = []
    while stack:
        pointer, value = stack.popleft()
        if isinstance(value, list):
            stack.extend((pointer + "/" + str(i), x) for i, x in enumerate(value))
        elif isinstance(value, dict):
            bound = "path" in value and any(
                name in value
                for name in (
                    "commit",
                    "git_blob",
                    "sha256_lf",
                    "file_sha256_lf_normalized",
                )
            )
            if bound:
                row = copy.deepcopy(value)
                if "commit" in row:
                    method = "explicit_commit"
                else:
                    require(
                        (
                            schema.startswith("riemann.atlas.generalized.")
                            or schema == "graded-parent-global-boundary-sources-v1"
                        )
                        and default is not None,
                        "reference unknown inherited binding",
                    )
                    name, row["commit"] = default
                    method = "inherited_" + name
                result.append((pointer, row, method))
            for name, child in value.items():
                segment = name.replace("~", "~0").replace("/", "~1")
                stack.append((pointer + "/" + segment, child))
    if "frozen_programme_path" in document:
        require(
            schema == "archimedean-ladder-source-lock-v1", "reference special schema"
        )
        result.append(
            (
                "/frozen_programme_path",
                {
                    "path": document["frozen_programme_path"],
                    "commit": document["source_commit"],
                    "git_blob": document["frozen_programme_blob"],
                    "sha256_lf": document["frozen_programme_sha256_lf"],
                },
                "archimedean_single_file_lock",
            )
        )
    return result


def reference_build(reader, head, base):
    roots = sorted(
        p.decode()
        for p in git("diff", "--no-renames", "--name-only", "-z", base, head).split(
            b"\0"
        )
        if p.endswith(b".sources.json")
    )
    pending = deque((head, path) for path in roots)
    manifests, targets, edges = {}, {}, []
    while pending:
        reader.fill(pending)
        key = pending.popleft()
        if key in manifests:
            continue
        data, blob, content_hash = reader.get(key)
        rows = reference_rows(strict_load(data))
        manifests[key] = {
            "commit": key[0],
            "path": key[1],
            "git_blob": blob,
            "sha256_lf": content_hash,
            "outgoing_edges": len(rows),
        }
        reader.fill((row["commit"], row["path"]) for _, row, _ in rows)
        for pointer, row, method in rows:
            target = (row["commit"], row["path"])
            _, target_blob, target_hash = reader.get(target)
            if "git_blob" in row:
                require(row["git_blob"] == target_blob, "reference declared blob")
            for name in ["sha256_lf", "file_sha256_lf_normalized"]:
                if name in row:
                    require(row[name] == target_hash, "reference declared LF SHA")
            edges.append([key[0], key[1], pointer, *target, method])
            targets[target] = {
                "commit": target[0],
                "path": target[1],
                "git_blob": target_blob,
                "sha256_lf": target_hash,
            }
            if target[1].endswith(".sources.json"):
                pending.append(target)
    commits = sorted({c for c, _ in targets})
    implicit = sorted(e for e in edges if e[-1] != "explicit_commit")
    return {
        "counts": dict(
            zip(
                COUNT_KEYS,
                [
                    len(roots),
                    len(manifests),
                    len(edges),
                    len(targets),
                    len(commits),
                    len(implicit),
                ],
            )
        ),
        "root_paths": roots,
        "source_commits": commits,
        "manifest_catalog": [manifests[k] for k in sorted(manifests)],
        "edges_sha256": digest(canonical(sorted(edges))),
        "source_catalog_sha256": digest(
            canonical([targets[k] for k in sorted(targets)])
        ),
        "implicit_resolutions": implicit,
    }


def main():
    audited, reader, reports = load_audited(), ReferenceReader(), []
    for name, head, base, programme, expected in REGRESSIONS:
        ref = reference_build(reader, head, base)
        require(
            [ref["counts"][k] for k in COUNT_KEYS] == expected,
            "reference counts " + name,
        )
        actual = audited.build(head, base, programme)
        for key, value in ref.items():
            require(
                canonical(actual[key]) == canonical(value),
                "independent " + name + "/" + key,
            )
        unsigned = {k: v for k, v in actual.items() if k != "payload_sha256"}
        require(
            actual["payload_sha256"] == digest(canonical(unsigned)), "report payload"
        )
        reports.append(
            {
                "regression": name,
                "head": head,
                "base": base,
                "counts": ref["counts"],
                "edges_sha256": ref["edges_sha256"],
                "source_catalog_sha256": ref["source_catalog_sha256"],
                "closure_payload_sha256": actual["payload_sha256"],
            }
        )
        print(json.dumps(reports[-1], sort_keys=True), flush=True)
    print(
        json.dumps(
            {
                "status": "PASS",
                "audited_source": AUDITED,
                "independent_algorithms": "Git batch + FIFO breadth-first traversal",
                "regressions": len(reports),
                "scope": "local manifest bindings only",
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
