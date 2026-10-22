from __future__ import annotations

import copy
import hashlib
import math
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CORE = REPO_ROOT / "research" / "l-families" / "atlas" / "core"
sys.path.insert(0, str(CORE))

from atlas_core import ATLAS_ROOT, canonical_bytes, read_json, semantic_identity, sha256_hex, write_json  # noqa: E402
from validate_atlas import (  # noqa: E402
    AtlasValidationError,
    SchemaStore,
    safe_repo_path,
    validate_atlas,
    validate_canonical_provenance,
    validate_identity,
    validate_input_fulfillments,
    validate_instance,
    validate_output_contract,
    validate_parameter_values,
    validate_run_implementation,
)


class CanonicalJsonTests(unittest.TestCase):
    def test_nfc_identity_is_stable(self) -> None:
        self.assertEqual(canonical_bytes({"x": "e\u0301"}), canonical_bytes({"x": "\u00e9"}))

    def test_nan_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            canonical_bytes({"bad": math.nan})

    def test_duplicate_keys_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"x": 1, "x": 2}', encoding="utf-8")
            with self.assertRaises(ValueError):
                read_json(path)

    def test_semantic_id_binds_identity_kernel(self) -> None:
        kernel = {"version": 1, "slug": "TEST", "value": 7}
        semantic_id, digest = semantic_identity("DETECTOR", "TEST", kernel)
        self.assertTrue(semantic_id.endswith(f".H{digest[:32]}"))
        self.assertEqual(digest, sha256_hex(kernel))


class ContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.spec_path = next((ATLAS_ROOT / "specs").glob("ATLAS.LFUNC.ZETA.*.json"))
        cls.detector_path = next((ATLAS_ROOT / "detectors").glob("ATLAS.DETECTOR.LOCAL_EULER.*.json"))
        cls.spec = read_json(cls.spec_path)
        cls.detector = read_json(cls.detector_path)
        cls.evaluation_path = next((ATLAS_ROOT / "evaluations").glob("ATLAS.EVAL.ZETA.RIEMANN.LOCAL_EULER.*.json"))
        cls.evaluation = read_json(cls.evaluation_path)

    def test_full_atlas_validates(self) -> None:
        counts = validate_atlas(ATLAS_ROOT)
        self.assertEqual(counts["specs"], 10)
        self.assertEqual(counts["detectors"], 11)
        self.assertEqual(counts["evaluations"], 15)

    def test_unexpected_schema_property_fails(self) -> None:
        mutated = copy.deepcopy(self.spec)
        mutated["silent_normalization_change"] = True
        schema_path = ATLAS_ROOT / "schema" / "l-function-spec.schema.json"
        store = SchemaStore()
        errors = validate_instance(mutated, store.load(schema_path), schema_path, store)
        self.assertTrue(any("unexpected property" in error for error in errors))

    def test_identity_mutation_fails(self) -> None:
        mutated = copy.deepcopy(self.spec)
        mutated["identity_kernel"]["construction"] += " mutated"
        errors = validate_identity(mutated)
        self.assertTrue(any("identity_sha256 mismatch" in error for error in errors))

    def test_released_without_sidecar_fails(self) -> None:
        mutated = copy.deepcopy(self.spec)
        mutated["record_state"] = "RELEASED"
        errors = validate_identity(mutated)
        self.assertTrue(any("lacks canonical provenance" in error for error in errors))

    def test_unknown_configuration_key_fails(self) -> None:
        errors = validate_parameter_values(
            self.detector,
            {"prime_bound": 43, "moments": [2, 4], "bad_prime_policy": "DECLARED_OMIT", "drift": 1},
        )
        self.assertTrue(any("unknown detector parameters" in error for error in errors))

    def test_odd_moment_fails(self) -> None:
        errors = validate_parameter_values(
            self.detector,
            {"prime_bound": 43, "moments": [2, 3], "bad_prime_policy": "DECLARED_OMIT"},
        )
        self.assertTrue(any("declared multiples" in error for error in errors))

    def test_duplicate_parameter_declaration_fails(self) -> None:
        mutated = copy.deepcopy(self.detector)
        mutated["parameters"].append(copy.deepcopy(mutated["parameters"][0]))
        errors = validate_parameter_values(mutated, self.evaluation["configuration"]["values"])
        self.assertTrue(any("duplicate detector parameter" in error for error in errors))

    def test_multi_enum_domain_fails_closed(self) -> None:
        detector = {
            "parameters": [{"name": "choice", "value_type": "ENUM", "required": True, "domain": "A|B"}],
        }
        self.assertEqual(validate_parameter_values(detector, {"choice": "A"}), [])
        self.assertTrue(validate_parameter_values(detector, {"choice": "C"}))

    def test_required_input_fulfillment_is_bound(self) -> None:
        mutated = copy.deepcopy(self.evaluation)
        mutated["input_fulfillments"] = mutated["input_fulfillments"][1:]
        errors = validate_input_fulfillments(self.detector, mutated)
        self.assertTrue(any("missing required input" in error for error in errors))
        mutated = copy.deepcopy(self.evaluation)
        mutated["input_fulfillments"][0]["sources"] = ["research/unbound.json"]
        errors = validate_input_fulfillments(self.detector, mutated)
        self.assertTrue(any("unbound sources" in error for error in errors))

    def test_output_contract_rejects_representation_drift(self) -> None:
        mutated = copy.deepcopy(self.evaluation)
        mutated["result"]["representation"] = "MATRIX"
        errors = validate_output_contract(self.detector, mutated)
        self.assertTrue(any("representation violates" in error for error in errors))

    def test_path_escape_fails(self) -> None:
        with self.assertRaises(AtlasValidationError):
            safe_repo_path(REPO_ROOT, "../outside.json")


class ProvenanceTests(unittest.TestCase):
    def make_fixture(self, directory: str) -> tuple[Path, dict, Path, dict]:
        repo_root = Path(directory)
        schema_target = repo_root / "canonical" / "provenance.schema.json"
        write_json(schema_target, read_json(REPO_ROOT / "canonical" / "provenance.schema.json"))
        record = copy.deepcopy(read_json(next((ATLAS_ROOT / "specs").glob("ATLAS.LFUNC.ZETA.*.json"))))
        record["record_state"] = "RELEASED"
        record_relative = f"research/l-families/atlas/specs/{record['semantic_id']}.json"
        record_path = repo_root / record_relative
        write_json(record_path, record)
        sidecar_relative = f"research/l-families/atlas/provenance/{record['semantic_id']}.json"
        sidecar_path = repo_root / sidecar_relative
        sidecar = {
            "schema_version": "riemann.provenance.v1",
            "object_id": record["semantic_id"],
            "title": "Atlas release provenance test",
            "object_kind": "artifact",
            "scope": {"class": "finite", "statement": "test fixture", "boundary": "test only"},
            "status": {"review_state": "unreviewed", "lifecycle": "canonical_candidate"},
            "source": {
                "repository": "gfreund123/riemann",
                "pr": 1,
                "commit": "0" * 40,
                "paths": [record_relative],
            },
            "review": {
                "verdict": "NOT REVIEWED",
                "reviewer": "test",
                "report_path": "tests/test_atlas_core.py",
                "frozen_commit": "0" * 40,
            },
            "dependencies": [],
            "integration": {
                "state": "metadata_only",
                "timestamp": "2026-08-24T00:00:00Z",
                "integration_commit": "PENDING",
            },
        }
        write_json(sidecar_path, sidecar)
        record["canonical_provenance_ref"] = {
            "schema_id": "https://github.com/gfreund123/riemann/canonical/provenance.schema.json",
            "record_path": sidecar_relative,
            "object_id": record["semantic_id"],
            "record_sha256": sha256_hex(sidecar),
        }
        return repo_root, record, record_path, sidecar

    def test_valid_sidecar_passes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            repo_root, record, record_path, _ = self.make_fixture(directory)
            self.assertEqual(validate_canonical_provenance(record, record_path, repo_root, SchemaStore()), [])

    def test_missing_or_wrong_hash_sidecar_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            repo_root, record, record_path, _ = self.make_fixture(directory)
            record["canonical_provenance_ref"]["record_path"] = "research/l-families/atlas/provenance/missing.json"
            errors = validate_canonical_provenance(record, record_path, repo_root, SchemaStore())
            self.assertTrue(any("missing canonical provenance" in error for error in errors))
        with tempfile.TemporaryDirectory() as directory:
            repo_root, record, record_path, _ = self.make_fixture(directory)
            record["canonical_provenance_ref"]["record_sha256"] = "f" * 64
            errors = validate_canonical_provenance(record, record_path, repo_root, SchemaStore())
            self.assertTrue(any("canonical hash mismatch" in error for error in errors))

    def test_object_ids_and_backlink_are_checked(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            repo_root, record, record_path, sidecar = self.make_fixture(directory)
            record["canonical_provenance_ref"]["object_id"] = "ATLAS.LFUNC.OTHER.H" + "0" * 32
            sidecar["object_id"] = "ATLAS.LFUNC.OTHER.H" + "0" * 32
            sidecar["source"]["paths"] = ["research/l-families/atlas/specs/other.json"]
            sidecar_path = repo_root / record["canonical_provenance_ref"]["record_path"]
            write_json(sidecar_path, sidecar)
            record["canonical_provenance_ref"]["record_sha256"] = sha256_hex(sidecar)
            errors = validate_canonical_provenance(record, record_path, repo_root, SchemaStore())
            self.assertTrue(any("reference object_id mismatch" in error for error in errors))
            self.assertTrue(any("sidecar object_id mismatch" in error for error in errors))
            self.assertTrue(any("source.paths omits" in error for error in errors))

    def test_malformed_and_duplicate_sidecars_fail(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            repo_root, record, record_path, sidecar = self.make_fixture(directory)
            sidecar["unexpected"] = True
            sidecar_path = repo_root / record["canonical_provenance_ref"]["record_path"]
            write_json(sidecar_path, sidecar)
            record["canonical_provenance_ref"]["record_sha256"] = sha256_hex(sidecar)
            errors = validate_canonical_provenance(record, record_path, repo_root, SchemaStore())
            self.assertTrue(any("unexpected property" in error for error in errors))
            sidecar_path.write_text('{"object_id":"x","object_id":"y"}', encoding="utf-8")
            errors = validate_canonical_provenance(record, record_path, repo_root, SchemaStore())
            self.assertTrue(any("invalid canonical provenance" in error for error in errors))


class ImplementationBindingTests(unittest.TestCase):
    def test_actual_source_hash_passes_and_lie_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            repo_root = Path(directory)
            implementation = repo_root / "impl.py"
            implementation.write_text("print('exact')\n", encoding="utf-8")
            digest = hashlib.sha256(implementation.read_bytes()).hexdigest()
            record = {
                "semantic_id": "ATLAS.EVAL.TEST.H" + "0" * 32,
                "identity_kernel": {"implementation_sha256": digest},
                "run": {"implementation_path": "impl.py", "implementation_sha256": digest},
            }
            self.assertEqual(validate_run_implementation(record, repo_root), [])
            record["run"]["implementation_sha256"] = "f" * 64
            errors = validate_run_implementation(record, repo_root)
            self.assertTrue(any("identity implementation hash drift" in error for error in errors))
            self.assertTrue(any("run implementation hash mismatch" in error for error in errors))

    def test_unsafe_implementation_path_fails(self) -> None:
        record = {
            "semantic_id": "ATLAS.EVAL.TEST.H" + "0" * 32,
            "identity_kernel": {"implementation_sha256": "0" * 64},
            "run": {"implementation_path": "../impl.py", "implementation_sha256": "0" * 64},
        }
        errors = validate_run_implementation(record, REPO_ROOT)
        self.assertTrue(any("unsafe repository-relative path" in error for error in errors))

    def test_implementation_hash_changes_semantic_identity(self) -> None:
        kernel = {"version": 1, "slug": "TEST", "implementation_sha256": "0" * 64}
        first, _ = semantic_identity("EVAL", "TEST", kernel)
        kernel["implementation_sha256"] = "1" * 64
        second, _ = semantic_identity("EVAL", "TEST", kernel)
        self.assertNotEqual(first, second)


class SchemaSubsetTests(unittest.TestCase):
    def test_max_items_is_enforced(self) -> None:
        schema_path = ATLAS_ROOT / "schema" / "common.schema.json"
        errors = validate_instance([1, 2], {"type": "array", "maxItems": 1}, schema_path, SchemaStore())
        self.assertTrue(any("too many items" in error for error in errors))

    def test_prefix_items_are_heterogeneous_and_items_apply_only_after_prefix(self) -> None:
        schema_path = ATLAS_ROOT / "schema" / "common.schema.json"
        schema = {
            "type": "array",
            "prefixItems": [{"type": "integer"}, {"type": "string"}],
            "items": {"type": "boolean"},
        }
        self.assertEqual(
            validate_instance([7, "seven", True], schema, schema_path, SchemaStore()),
            [],
        )
        self.assertTrue(
            validate_instance([7, 7, True], schema, schema_path, SchemaStore())
        )
        self.assertTrue(
            validate_instance([7, "seven", 7], schema, schema_path, SchemaStore())
        )

    def test_false_items_rejects_values_after_prefix(self) -> None:
        schema_path = ATLAS_ROOT / "schema" / "common.schema.json"
        schema = {
            "type": "array",
            "prefixItems": [{"type": "integer"}],
            "items": False,
        }
        self.assertEqual(validate_instance([7], schema, schema_path, SchemaStore()), [])
        self.assertTrue(validate_instance([7, 8], schema, schema_path, SchemaStore()))

    def test_rfc3339_datetime_profile(self) -> None:
        schema_path = ATLAS_ROOT / "schema" / "common.schema.json"
        schema = {"type": "string", "format": "date-time"}
        invalid = (
            "2026-08-24T12:00:00",
            "2026-W34-1T12:00:00+00:00",
            "2026-08-24 12:00:00+00:00",
            "2026-08-24T12:00+00:00",
            "2026-08-24T12:00:00+0000",
            "2026-08-24T12:00:00,5Z",
            "2026-08-24T12:00:00+00:60",
            "2026-08-24T12:00:00+12:99",
            "2026-02-29T12:00:00Z",
            "2026-08-24T24:00:00Z",
        )
        for value in invalid:
            with self.subTest(value=value):
                self.assertTrue(validate_instance(value, schema, schema_path, SchemaStore()))
        valid = (
            "2026-08-24T12:00:00Z",
            "2026-08-24T12:00:00.125+03:00",
            "2026-08-24t12:00:00z",
            "1990-12-31T23:59:60Z",
            "0000-02-29T12:00:00Z",
        )
        for value in valid:
            with self.subTest(value=value):
                self.assertEqual(validate_instance(value, schema, schema_path, SchemaStore()), [])

    def test_input_type_vocabulary_is_shared_and_strict(self) -> None:
        common_path = ATLAS_ROOT / "schema" / "common.schema.json"
        input_schema = SchemaStore().load(common_path)["$defs"]["inputType"]
        self.assertEqual(
            validate_instance("RAW_ARTIFACT", input_schema, common_path, SchemaStore()),
            [],
        )
        self.assertTrue(
            validate_instance("BOGUS_INPUT", input_schema, common_path, SchemaStore())
        )
        for filename, path in (
            ("detector-contract.schema.json", ("properties", "required_inputs", "items", "properties", "input_type")),
            ("evaluation-record.schema.json", ("properties", "input_fulfillments", "items", "properties", "input_type")),
        ):
            schema = SchemaStore().load(ATLAS_ROOT / "schema" / filename)
            node = schema
            for key in path:
                node = node[key]
            self.assertEqual(node, {"$ref": "common.schema.json#/$defs/inputType"})


if __name__ == "__main__":
    unittest.main()
