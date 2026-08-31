"""Independent workflow controls for closure successor 6b679973; no new mathematics."""

import copy
import hashlib
import importlib.util
import json
import subprocess
import types
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/exploratory/sixhour_complete_source_closure.py"
SPEC = importlib.util.spec_from_file_location("closure_review", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)
HEAD = "6b679973888841e56703ccf40ffe88e0574c1f01"
BASE = "0c7c1192aa683daf6cc473fd168a7cf6cc7e3bb7"
A, B, C = "a" * 40, "b" * 40, "c" * 40
SHA256 = "d" * 64
LEGACY = "riemann.atlas.generalized.review"


def row(**updates):
    return {"path": "p.md", "sha256_lf": SHA256, **updates}


def doc(**updates):
    return {
        "schema": LEGACY,
        "base_commit": A,
        "source_commit": B,
        "imported_parent_state_commit": C,
        "sources": [row()],
        **updates,
    }


class TestBindings(unittest.TestCase):
    def test_explicit_wins(self):
        got = list(M.bindings(doc(sources=[row(commit=A)])))
        self.assertEqual(got, [("/sources/0", row(commit=A), "explicit_commit")])

    def test_all_default_precedence_combinations(self):
        keys = ["imported_parent_state_commit", "source_commit", "base_commit"]
        for mask in range(1, 8):
            payload = {"schema": LEGACY, "sources": [row()]}
            for i, key in enumerate(keys):
                if mask & (1 << i):
                    payload[key] = [A, B, C][i]
            selected = next(key for key in keys if key in payload)
            with self.subTest(mask=mask):
                result = next(M.bindings(payload))
                self.assertEqual(result[1]["commit"], payload[selected])
                self.assertEqual(result[2], "inherited_" + selected)

    def test_no_nested_default_inference(self):
        payload = doc(sources=[{"base_commit": B, "child": row()}])
        got = list(M.bindings(payload))
        self.assertEqual(got[0][1]["commit"], C)

    def test_both_legacy_schemas(self):
        for schema in (LEGACY, "graded-parent-global-boundary-sources-v1"):
            with self.subTest(schema=schema):
                self.assertEqual(next(M.bindings(doc(schema=schema)))[1]["commit"], C)

    def test_unknown_implicit_schema_or_missing_default(self):
        for payload in (
            doc(schema="other-sources-v1"),
            {"schema": LEGACY, "sources": [row()]},
        ):
            with self.assertRaisesRegex(ValueError, "unknown implicit binding"):
                list(M.bindings(payload))

    def test_explicit_rows_need_no_legacy_schema(self):
        self.assertEqual(
            list(M.bindings({"sources": [{"commit": A, "path": "p"}]})),
            [("/sources/0", {"commit": A, "path": "p"}, "explicit_commit")],
        )

    def test_all_three_seal_names(self):
        for key, value in (
            ("git_blob", A),
            ("sha256_lf", SHA256),
            ("file_sha256_lf_normalized", SHA256),
        ):
            payload = {
                "schema": LEGACY,
                "base_commit": A,
                "sources": [{"path": "p", key: value}],
            }
            self.assertEqual(next(M.bindings(payload))[1]["commit"], A)

    def test_plain_paths_not_claimed_as_bindings(self):
        self.assertEqual(list(M.bindings({"path": "prose.md"})), [])

    def test_json_pointer_escaping_and_nested_order(self):
        payload = {"z": [row(commit=B)], "a~/": {"inner": row(commit=A)}}
        self.assertEqual([x[0] for x in M.bindings(payload)], ["/a~0~1/inner", "/z/0"])

    def test_archimedean_lock(self):
        payload = {
            "schema": "archimedean-ladder-source-lock-v1",
            "source_commit": A,
            "frozen_programme_path": "p.md",
            "frozen_programme_blob": B,
            "frozen_programme_sha256_lf": SHA256,
        }
        self.assertEqual(
            list(M.bindings(payload)),
            [
                (
                    "/frozen_programme_path",
                    {"commit": A, "path": "p.md", "git_blob": B, "sha256_lf": SHA256},
                    "archimedean_single_file_lock",
                )
            ],
        )
        payload["schema"] = "wrong"
        with self.assertRaisesRegex(ValueError, "unknown special source schema"):
            list(M.bindings(payload))

    def test_special_lock_missing_field_fails(self):
        with self.assertRaises(KeyError):
            list(
                M.bindings(
                    {
                        "schema": "archimedean-ladder-source-lock-v1",
                        "frozen_programme_path": "p",
                    }
                )
            )

    def test_duplicate_json_top_and_nested(self):
        for raw in (b'{"x":1,"x":2}', b'{"a":{"x":1,"x":2}}'):
            with self.assertRaisesRegex(ValueError, "duplicate JSON key"):
                M.strict_json(raw)

    def test_json_float_nonfinite_rejection(self):
        for value in ("1.0", "1e0", "NaN", "Infinity", "-Infinity"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                M.strict_json(('{"x":' + value + "}").encode())

    def test_json_integer_bool_distinction_preserved(self):
        one = M.strict_json(b'{"x":1}')
        boolean = M.strict_json(b'{"x":true}')
        self.assertNotEqual(M.canonical(one), M.canonical(boolean))

    def test_malformed_json_utf8(self):
        for raw in (b'{"x":}', b"\xff"):
            with self.assertRaises((ValueError, UnicodeDecodeError)):
                M.strict_json(raw)


class TestSources(unittest.TestCase):
    def setUp(self):
        M.CACHE.clear()
        M.COMMIT_CACHE.clear()

    def test_original_tree_sha_witness_and_repair(self):
        raw = subprocess.check_output(
            [
                "git",
                "show",
                BASE + ":" + str(PATH.relative_to(ROOT)).replace("\\", "/"),
            ],
            cwd=ROOT,
        )
        old = types.ModuleType("old_closure")
        old.__file__ = str(PATH)
        # Execute only the exact frozen predecessor, to retain the original witness.
        exec(compile(raw, str(PATH), "exec"), old.__dict__)  # noqa: S102
        tree = M.git("rev-parse", BASE + "^{tree}").decode().strip()
        before = old.source(tree, "README.md")
        self.assertEqual(before[0], old.source(BASE, "README.md")[0])
        with self.assertRaisesRegex(ValueError, "Git commit type"):
            M.source(tree, "README.md")
        with self.assertRaisesRegex(ValueError, "Git commit type"):
            M.build(tree, BASE, "S")
        with self.assertRaisesRegex(ValueError, "Git commit type"):
            M.build(HEAD, tree, "S")

    def test_commit_syntax_and_types(self):
        for value in (None, True, 0, [], "", "a" * 39, "A" * 40, "HEAD", A + "\n"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                M.validate_commit(value)

    def test_noncommit_blob_rejected(self):
        blob = M.git("rev-parse", HEAD + ":README.md").decode().strip()
        with self.assertRaisesRegex(ValueError, "Git commit type"):
            M.validate_commit(blob)

    def test_canonical_path_rejections(self):
        cases = [
            None,
            True,
            [],
            "",
            "./README.md",
            "../README.md",
            "/README.md",
            "a//b",
            "a/./b",
            "a/../b",
            "a/",
            "a\\b",
            "a:b",
            "a\0b",
            "a\nb",
            "a\tb",
            "a\rb",
            "a\x7fb",
        ]
        for value in cases:
            with (
                self.subTest(value=value),
                self.assertRaisesRegex(ValueError, "canonical relative source path"),
            ):
                M.source(HEAD, value)

    def test_current_source_blob_and_lf(self):
        data, blob, sha = M.source(HEAD, "README.md")
        expected = M.git("cat-file", "blob", HEAD + ":README.md")
        self.assertEqual(data, expected)
        self.assertEqual(
            blob,
            hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest(),
        )
        self.assertEqual(sha, hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest())
        with mock.patch.object(M, "git", side_effect=RuntimeError("cache miss")):
            self.assertEqual(M.source(HEAD, "README.md"), (data, blob, sha))

    def test_missing_path_fails_closed(self):
        original = subprocess.check_output

        def quiet(*args, **kwargs):
            return original(*args, **kwargs, stderr=subprocess.PIPE)

        with (
            mock.patch.object(subprocess, "check_output", side_effect=quiet),
            self.assertRaises(subprocess.CalledProcessError),
        ):
            M.source(HEAD, "__missing_closure_review_path__.md")

    def fake_git(self, data, *, object_id=None, size=None):
        blob = hashlib.sha1(
            b"blob " + str(len(data)).encode() + b"\0" + data
        ).hexdigest()

        def fake(*args):
            if args[:2] == ("cat-file", "-t"):
                return b"commit\n"
            if args[0] == "rev-parse":
                return ((object_id or blob) + "\n").encode()
            if args[:2] == ("cat-file", "-s"):
                return str(len(data) if size is None else size).encode()
            if args[0] == "show":
                return data
            raise AssertionError(args)

        return fake

    def test_synthetic_crlf_normalization(self):
        with mock.patch.object(M, "git", self.fake_git(b"x\r\ny\n")):
            self.assertEqual(M.source(A, "p")[2], hashlib.sha256(b"x\ny\n").hexdigest())

    def test_source_size_cap_and_size_mismatch(self):
        for size, text in ((M.MAX_BLOB + 1, "source byte cap"), (3, "source size")):
            M.CACHE.clear()
            with (
                mock.patch.object(M, "git", self.fake_git(b"x", size=size)),
                self.assertRaisesRegex(ValueError, text),
            ):
                M.source(A, "p")

    def test_computed_git_blob_mismatch(self):
        with (
            mock.patch.object(M, "git", self.fake_git(b"x", object_id=B)),
            self.assertRaisesRegex(ValueError, "Git source blob identity"),
        ):
            M.source(A, "p")

    def test_commit_cache_checked_once(self):
        with mock.patch.object(M, "git", return_value=b"commit\n") as call:
            M.validate_commit(A)
            M.validate_commit(A)
            call.assert_called_once_with("cat-file", "-t", A)

    def test_git_disables_replace_objects(self):
        with mock.patch.object(subprocess, "check_output", return_value=b"x") as call:
            M.git("cat-file", "-t", A)
            self.assertEqual(
                call.call_args.args[0][:2], ["git", "--no-replace-objects"]
            )

    def test_programme_identity(self):
        for value in (None, True, 1, [], "X", "s"):
            with (
                self.subTest(value=value),
                self.assertRaisesRegex(ValueError, "programme identity"),
            ):
                M.build(HEAD, BASE, value)


class TestGraph(unittest.TestCase):
    def run_graph(self, documents, roots):
        def source(commit, path):
            data = documents[(commit, path)]
            if not isinstance(data, bytes):
                data = json.dumps(data, sort_keys=True).encode()
            blob = hashlib.sha1(
                b"blob " + str(len(data)).encode() + b"\0" + data
            ).hexdigest()
            return data, blob, hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()

        def git(*args):
            if args[:2] == ("cat-file", "-t"):
                return b"commit\n"
            if args[0] == "diff":
                return ("\n".join(roots) + "\n").encode()
            raise AssertionError(args)

        with (
            mock.patch.object(M, "source", side_effect=source),
            mock.patch.object(M, "git", side_effect=git),
        ):
            return M.build(A, B, "G")

    def test_cycle_repeat_edges_and_version_identity(self):
        docs = {
            (A, "a.sources.json"): {
                "refs": [
                    {"commit": B, "path": "b.sources.json"},
                    {"commit": B, "path": "b.sources.json"},
                    {"commit": A, "path": "p.md"},
                    {"commit": B, "path": "p.md"},
                ]
            },
            (B, "b.sources.json"): {"ref": {"commit": A, "path": "a.sources.json"}},
            (A, "p.md"): b"same",
            (B, "p.md"): b"same",
        }
        result = self.run_graph(docs, ["a.sources.json", "irrelevant.py"])
        self.assertEqual(
            result["counts"],
            {
                "roots": 1,
                "manifest_versions": 2,
                "edges": 5,
                "source_versions": 4,
                "source_commits": 2,
                "implicit_edges": 0,
            },
        )
        payload = {k: v for k, v in result.items() if k != "payload_sha256"}
        self.assertEqual(
            result["payload_sha256"], hashlib.sha256(M.canonical(payload)).hexdigest()
        )

    def test_each_declared_seal_rejected(self):
        for key in ("git_blob", "sha256_lf", "file_sha256_lf_normalized"):
            for bad in (False, 0, None, "", "e" * (40 if key == "git_blob" else 64)):
                docs = {
                    (A, "a.sources.json"): {
                        "ref": {"commit": B, "path": "p", key: bad}
                    },
                    (B, "p"): b"x",
                }
                with (
                    self.subTest(key=key, bad=bad),
                    self.assertRaisesRegex(ValueError, "declared"),
                ):
                    self.run_graph(docs, ["a.sources.json"])

    def test_both_lf_aliases_must_match(self):
        digest = hashlib.sha256(b"x").hexdigest()
        docs = {
            (A, "a.sources.json"): {
                "ref": {
                    "commit": B,
                    "path": "p",
                    "sha256_lf": digest,
                    "file_sha256_lf_normalized": "e" * 64,
                }
            },
            (B, "p"): b"x",
        }
        with self.assertRaisesRegex(ValueError, "declared LF SHA"):
            self.run_graph(docs, ["a.sources.json"])

    def test_nonobject_manifest_rejected(self):
        for raw in (b"[]", b"null", b"true", b"1", b'"schema"'):
            with (
                self.subTest(raw=raw),
                self.assertRaisesRegex(ValueError, "source manifest object"),
            ):
                self.run_graph({(A, "a.sources.json"): raw}, ["a.sources.json"])

    def test_unknown_implicit_cannot_be_silently_dropped(self):
        with self.assertRaisesRegex(ValueError, "unknown implicit binding"):
            self.run_graph(
                {(A, "a.sources.json"): {"refs": [row()]}}, ["a.sources.json"]
            )

    def test_manifest_cap(self):
        docs = {
            (A, f"{i}.sources.json"): {
                "ref": {"commit": A, "path": f"{i + 1}.sources.json"}
            }
            for i in range(1002)
        }
        with self.assertRaisesRegex(ValueError, "manifest cap"):
            self.run_graph(docs, ["0.sources.json"])

    def test_edge_cap(self):
        docs = {
            (A, "a.sources.json"): {"refs": [{"commit": B, "path": "p"}] * 10001},
            (B, "p"): b"x",
        }
        with self.assertRaisesRegex(ValueError, "edge cap"):
            self.run_graph(docs, ["a.sources.json"])

    def test_resealed_report_tampering_and_bool_collision(self):
        expected = {"count": 1, "all_local_objects_present": True}
        expected["payload_sha256"] = hashlib.sha256(M.canonical(expected)).hexdigest()
        for key, replacement in (
            ("count", True),
            ("count", 2),
            ("all_local_objects_present", 1),
        ):
            bad = copy.deepcopy(expected)
            bad[key] = replacement
            bad.pop("payload_sha256")
            bad["payload_sha256"] = hashlib.sha256(M.canonical(bad)).hexdigest()
            args = types.SimpleNamespace(
                head=A, base=B, programme="G", check_report="unused.json"
            )
            with (
                mock.patch.object(
                    M.argparse.ArgumentParser, "parse_args", return_value=args
                ),
                mock.patch.object(M, "build", return_value=expected),
                mock.patch.object(
                    Path, "read_bytes", return_value=json.dumps(bad).encode()
                ),
                self.assertRaisesRegex(
                    ValueError, "fresh complete closure report mismatch"
                ),
            ):
                M.main()


if __name__ == "__main__":
    unittest.main()
