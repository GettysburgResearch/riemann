"""Independent metadata-only replay of native acquisition successor 6c5c99a0."""

from __future__ import annotations

import ast
import copy
import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OLD = "a9e1587c90321e2f54e0a3c08a5ca74a15879f3b"
SCIENCE = "ac7fa9af27c3fbcb3314f3ed58c8eed35b318052"
NEW = "6c5c99a0d2f2d2ecca5087da0fd171998b444d2b"
STEM = "research/exploratory/native_tuple_source_acquisition"
PRODUCER = STEM + ".py"
MANIFEST = STEM + ".sources.json"
FIXTURE = STEM + ".json"
TEST = "tests/test_native_tuple_source_acquisition.py"
NOTE = "research/exploratory/NATIVE_TUPLE_SOURCE_ACQUISITION.md"
FILES = [NOTE, PRODUCER, FIXTURE, MANIFEST, TEST]
EXPECTED = {
    "arithmetic_class": "MIXED",
    "components": ["EXACT_RATIONAL", "CERTIFIED_INTEGER_COVERAGE"],
    "rounding": "none",
}


def require(condition, label):
    if not condition:
        raise ValueError(label)


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def read(commit, path):
    return git("show", commit + ":" + path)


def lf(raw):
    return raw.replace(b"\r\n", b"\n")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("ascii")


def normalize_contract(value):
    result = copy.deepcopy(value)
    for key, expected in EXPECTED.items():
        require(canonical(result["contract"].pop(key)) == canonical(expected), key)
    return result


def producer_ast(raw, strip=False):
    tree = ast.parse(raw)
    if strip:
        contracts = [
            node
            for node in tree.body
            if isinstance(node, ast.Assign)
            and any(
                isinstance(t, ast.Name) and t.id == "CONTRACT" for t in node.targets
            )
        ]
        require(len(contracts) == 1, "one CONTRACT assignment")
        node = contracts[0].value
        require(isinstance(node, ast.Dict), "literal contract")
        removed, kept = {}, []
        for key, value in zip(node.keys, node.values):
            name = ast.literal_eval(key)
            if name in EXPECTED:
                require(name not in removed, "unique added metadata")
                removed[name] = ast.literal_eval(value)
            else:
                kept.append((key, value))
        require(canonical(removed) == canonical(EXPECTED), "exact three additions")
        node.keys = [k for k, _ in kept]
        node.values = [v for _, v in kept]
    return ast.dump(tree, include_attributes=False)


def tests_ast(raw, strip=False):
    tree = ast.parse(raw)
    classes = [n for n in tree.body if isinstance(n, ast.ClassDef)]
    require(len(classes) == 1, "one test class")
    methods = [
        n
        for n in classes[0].body
        if isinstance(n, ast.FunctionDef) and n.name.startswith("test_")
    ]
    count = len(methods)
    if strip:
        added = [n for n in methods if n.name == "test_release_arithmetic_taxonomy"]
        require(len(added) == 1, "one added taxonomy test")
        classes[0].body.remove(added[0])
    return ast.dump(tree, include_attributes=False), count


def authenticate(commit):
    report = json.loads(read(commit, FIXTURE))
    manifest = json.loads(read(commit, MANIFEST))
    require(
        canonical(report["contract"]) == canonical(manifest["contract"]), "contract"
    )
    require(
        canonical(report["frozen_sources"]) == canonical(manifest["frozen_sources"]),
        "source lists",
    )
    require(
        set(report["artifacts"]) == {NOTE, PRODUCER, MANIFEST, TEST}, "four artifacts"
    )
    for path, expected in report["artifacts"].items():
        require(sha(lf(read(commit, path))) == expected, "artifact " + path)
    unsealed = {k: v for k, v in report.items() if k != "payload_sha256"}
    require(sha(canonical(unsealed)) == report["payload_sha256"], "payload seal")
    for pin in manifest["frozen_sources"]:
        raw = read(pin["commit"], pin["path"])
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        require(blob == pin["git_blob"], "Git blob " + pin["id"])
        require(sha(lf(raw)) == pin["sha256_lf"], "LF SHA " + pin["id"])
    return report, manifest


def metadata_attacks(module, report):
    mutations = []
    for key in EXPECTED:
        for remove in (True, False):
            item = copy.deepcopy(report)
            if remove:
                del item["contract"][key]
            else:
                item["contract"][key] = "incorrect"
            mutations.append(item)
    extra = [
        ("arithmetic_class", None),
        ("arithmetic_class", "mixed"),
        ("components", list(reversed(EXPECTED["components"]))),
        ("components", ["EXACT_RATIONAL", "EXACT_RATIONAL"]),
        ("components", "EXACT_RATIONAL,CERTIFIED_INTEGER_COVERAGE"),
        ("rounding", False),
    ]
    for key, value in extra:
        item = copy.deepcopy(report)
        item["contract"][key] = value
        mutations.append(item)
    for index, item in enumerate(mutations):
        item.pop("payload_sha256")
        item["payload_sha256"] = sha(canonical(item))
        try:
            module.check_report(item)
        except ValueError as error:
            require(str(error) == "fresh reconstruction", "unexpected rejection")
        else:
            raise ValueError("accepted resealed mutation " + str(index))
    return len(mutations)


def main():
    require(git("rev-parse", NEW + "^").decode().strip() == OLD, "exact parent")
    changed = git("diff", "--name-only", OLD, NEW).decode().splitlines()
    require(set(changed) == {PRODUCER, FIXTURE, MANIFEST, TEST}, "four-file delta")
    for path in FILES:
        require(read(SCIENCE, path) == read(OLD, path), "original science " + path)
        require(lf((ROOT / path).read_bytes()) == lf(read(NEW, path)), "local " + path)
    require(read(OLD, NOTE) == read(NEW, NOTE), "proof bytes")
    require(
        producer_ast(read(OLD, PRODUCER)) == producer_ast(read(NEW, PRODUCER), True),
        "whole producer AST",
    )
    old_ast, old_count = tests_ast(read(OLD, TEST))
    new_ast, new_count = tests_ast(read(NEW, TEST), True)
    require(old_ast == new_ast and (old_count, new_count) == (32, 33), "whole test AST")
    old_report, old_manifest = authenticate(OLD)
    new_report, new_manifest = authenticate(NEW)
    require(
        canonical(old_manifest) == canonical(normalize_contract(new_manifest)),
        "whole manifest except three metadata keys",
    )
    stripped = normalize_contract(new_report)
    for obj in (stripped, old_report):
        obj.pop("artifacts")
        obj.pop("payload_sha256")
    require(canonical(stripped) == canonical(old_report), "whole scientific payload")
    require(len(new_manifest["frozen_sources"]) == 11, "eleven source pins")
    for path in FILES:
        chars = lf(read(NEW, path)).decode("utf-8")
        require(
            all(ord(c) in (9, 10) or ord(c) >= 32 for c in chars)
            and not any(127 <= ord(c) <= 159 for c in chars),
            "source control chars",
        )
    spec = importlib.util.spec_from_file_location(
        "native_taxonomy_review", ROOT / PRODUCER
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    fixture = module.load_json(read(NEW, FIXTURE))
    attacks = metadata_attacks(module, fixture)
    mode = ["-O"] if sys.flags.optimize else []
    command = [sys.executable, "-B", *mode, str(ROOT / PRODUCER)]
    checked = subprocess.check_output(command + ["--check"], cwd=ROOT)
    require(checked.startswith(b"PASS native source acquisition"), "producer check")
    for flag, path in (("--emit", FIXTURE), ("--emit-sources", MANIFEST)):
        emitted = subprocess.check_output(command + [flag], cwd=ROOT)
        require(lf(emitted) == lf(read(NEW, path)), "LF-exact " + flag)
    print(
        json.dumps(
            {
                "verdict": "PASS metadata-only successor; no new scientific acceptance",
                "science": SCIENCE,
                "parent": OLD,
                "successor": NEW,
                "changed_files": sorted(changed),
                "original_science_files_unchanged_at_parent": 5,
                "source_pins_authenticated_and_unchanged": 11,
                "artifact_seals_per_snapshot": 4,
                "payload_seals": 2,
                "producer_AST_equal_after_exact_three_key_removal": True,
                "scientific_payload_type_exact_equal": True,
                "manifest_equal_after_exact_three_key_removal": True,
                "tests_before_after": [old_count, new_count],
                "fresh_resealed_metadata_mutations_rejected": attacks,
                "producer_check": True,
                "LF_exact_emits": 2,
                "successor_fixture_LF_sha256": sha(lf(read(NEW, FIXTURE))),
                "successor_payload_sha256": fixture["payload_sha256"],
                "contract_additions": EXPECTED,
            },
            sort_keys=True,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
