"""Metadata-only exact-successor audit; no new Xi theorem or numeric claim."""

from __future__ import annotations

import argparse
import ast
import copy
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[2]
OLD = "0e3fc9b482f0f115a49a6209ccbfeffae640014a"
NEW = "71dc38e7619409a27dd4d1973dec985b0e655a30"
STEM = "xi_fixed_lambda_joint_box_compression"
DIR = "research/exploratory/"
FILES = [
    DIR + "XI_FIXED_LAMBDA_JOINT_BOX_COMPRESSION.md",
    DIR + STEM + ".py",
    DIR + STEM + ".json",
    DIR + STEM + ".sources.json",
    "tests/test_" + STEM + ".py",
]
KEYS = {"arithmetic_class", "arithmetic_components", "rounding", "source_quantifiers"}
EXPECTED = {
    "arithmetic_class": "MIXED",
    "arithmetic_components": [
        "DIRECTED_BALL_ENCLOSURES",
        "EXACT_RATIONAL",
        "CERTIFIED_INTEGER_COVERAGE",
    ],
    "rounding": "FLINT real/complex balls round outward; exact rational endpoint acceptance and integer winding; scouts and approximate eigenvectors are not certificates",
    "source_quantifiers": "finite actual-Xi certificates are unconditional relative to the pinned runtime; global Hardy lower bounds require component innerness; no band or cofinal conclusion",
}
OUTPUT = Path(__file__).with_suffix(".json")


def need(ok, message):
    if not ok:
        raise ValueError(message)


def lf(raw):
    return raw.replace(b"\r\n", b"\n")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canon(value):
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode()


def read(commit, path):
    raw = subprocess.check_output(["git", "show", commit + ":" + path], cwd=ROOT)
    need(len(raw) <= 12000000, "source byte cap")
    return raw


def strip_contract(value):
    value = copy.deepcopy(value)
    actual = {key: value["contract"].pop(key) for key in KEYS}
    need(actual == EXPECTED, "exact new metadata values")
    return value


def strip_ast(raw):
    tree = ast.parse(raw)
    matches = [
        node
        for node in tree.body
        if isinstance(node, ast.Assign)
        and any(isinstance(t, ast.Name) and t.id == "CONTRACT" for t in node.targets)
    ]
    need(
        len(matches) == 1 and isinstance(matches[0].value, ast.Dict),
        "single literal CONTRACT",
    )
    d = matches[0].value
    pairs = list(zip(d.keys, d.values))
    extra = {
        ast.literal_eval(k): ast.literal_eval(v)
        for k, v in pairs
        if ast.literal_eval(k) in KEYS
    }
    need(extra == EXPECTED, "exact added AST metadata")
    keep = [(k, v) for k, v in pairs if ast.literal_eval(k) not in KEYS]
    d.keys = [k for k, v in keep]
    d.values = [v for k, v in keep]
    return ast.dump(tree, include_attributes=False)


def build():
    old = {p: read(OLD, p) for p in FILES}
    new = {p: read(NEW, p) for p in FILES}
    for p in FILES:
        need(
            lf((ROOT / p).read_bytes()) == lf(new[p]), "frozen successor current bytes"
        )
    need(old[FILES[4]] == new[FILES[4]], "test source byte identity")
    need(
        strip_ast(new[FILES[1]])
        == ast.dump(ast.parse(old[FILES[1]]), include_attributes=False),
        "all producer AST except explicit metadata unchanged",
    )
    old_note = lf(old[FILES[0]]).decode()
    new_note = lf(new[FILES[0]]).decode()
    a = new_note.index(
        "Metadata-only clarification following the frozen scientific identity"
    )
    b = new_note.index("The adjacent producer, fixture, manifest and tests", a)
    need(new_note[:a] + new_note[b:] == old_note, "entire original proof text retained")
    olds = json.loads(old[FILES[3]])
    news = json.loads(new[FILES[3]])
    need(strip_contract(news) == olds, "manifest exact whitelist")
    oldr = json.loads(old[FILES[2]])
    newr = json.loads(new[FILES[2]])
    normalized = strip_contract(newr)
    normalized["artifacts"] = oldr["artifacts"]
    normalized["payload_sha256"] = oldr["payload_sha256"]
    need(normalized == oldr, "all remaining scientific fields EXACT")
    need(newr["contract"] == news["contract"], "fixture manifest contract identity")
    hashes = {}
    for label, files, report in (("old", old, oldr), ("new", new, newr)):
        unsigned = {k: v for k, v in report.items() if k != "payload_sha256"}
        need(sha(canon(unsigned)) == report["payload_sha256"], "payload seal")
        need(
            set(report["artifacts"]) == set(FILES) - {FILES[2]},
            "four artifact coverage",
        )
        for p, digest in report["artifacts"].items():
            need(sha(lf(files[p])) == digest, "artifact seal")
        hashes[label] = {p: sha(lf(raw)) for p, raw in files.items()}
    need(
        news["frozen_sources"] == newr["frozen_sources"] == olds["frozen_sources"],
        "source pins unchanged",
    )
    for row in news["frozen_sources"]:
        raw = read(row["commit"], row["path"])
        need(sha(lf(raw)) == row["sha256_lf"], "frozen LF source")
        need(
            hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
            == row["git_blob"],
            "frozen Git blob",
        )
    science = {
        k: v
        for k, v in newr.items()
        if k not in ("contract", "artifacts", "payload_sha256")
    }
    science_sha = sha(canon(science))
    need(
        science_sha
        == "18b2bd7d928ae50fd6ebaf9dc751424b71cd756931ae04dd17f717d83150e7df",
        "advertised science hash",
    )
    schema = json.loads((ROOT / "canonical/provenance.schema.json").read_bytes())
    need(
        "MIXED" in schema["properties"]["arithmetic"]["properties"]["class"]["enum"],
        "resident class enum",
    )
    sys.path.insert(0, str(ROOT / "research/exploratory"))
    import xi_fixed_lambda_joint_box_compression as source

    source.authenticate()
    need(source.CONTRACT == newr["contract"], "runtime contract")
    attacks = 0
    for key in sorted(KEYS):
        forged = copy.deepcopy(newr)
        forged["contract"][key] = "forged"
        forged.pop("payload_sha256")
        forged["payload_sha256"] = sha(canon(forged))
        with mock.patch.object(source, "build_report", return_value=newr):
            try:
                source.check_report(forged)
            except ValueError:
                attacks += 1
            else:
                raise ValueError("resealed metadata accepted")
    return {
        "schema": "fixed-lambda-metadata-review-v1",
        "old": OLD,
        "new": NEW,
        "verdict": "PASS metadata-only; prior scientific verdict not widened",
        "allowed_contract_additions": sorted(KEYS),
        "unchanged_science_sha256": science_sha,
        "source_bindings": len(news["frozen_sources"]),
        "unchanged_test_sha256_lf": hashes["new"][FILES[4]],
        "source_file_sha256_lf": hashes,
        "full_producer_AST_except_added_contract": "identical",
        "entire_original_proof": "identical after deleting metadata paragraph",
        "resealed_metadata_rejections": attacks,
        "runtime": news["runtime"],
        "arithmetic_class": "MIXED",
        "rounding": "none in semantic comparison",
        "review_limit": "metadata/identity/assurance successor, not an independent new special-function implementation",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--emit", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.emit:
        print(json.dumps(result, sort_keys=True, indent=2))
    else:
        need(json.loads(OUTPUT.read_bytes()) == result, "review fixture")
        print(
            "PASS exact metadata-only successor, six source pins, runtime, four hostile metadata checks"
        )


if __name__ == "__main__":
    main()
