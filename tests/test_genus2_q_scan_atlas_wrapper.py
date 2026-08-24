"""Focused atlas registration tests for the exact q=3,5,7 genus-two scan."""

from __future__ import annotations

import copy
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ATLAS_ROOT = ROOT / "research" / "l-families" / "atlas"
CORE = ATLAS_ROOT / "core"
sys.path.insert(0, str(CORE))

from atlas_core import read_json, sha256_hex  # noqa: E402
from validate_atlas import SchemaStore, validate_instance  # noqa: E402
import wrap_genus2_q_scan as wrapper  # noqa: E402


class GenusTwoQScanAtlasTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.specs, cls.new_specs, cls.detector, cls.evaluation, cls.result = wrapper.run(
            ATLAS_ROOT
        )
        cls.specs_by_q = {
            spec["base_field"]["constant_field_order"]: spec for spec in cls.specs
        }

    def test_three_true_family_specs_are_bound_and_f3_is_reused(self) -> None:
        self.assertEqual(set(self.specs_by_q), {3, 5, 7})
        self.assertEqual(len(self.new_specs), 2)
        self.assertEqual(
            {spec["base_field"]["constant_field_order"] for spec in self.new_specs},
            {5, 7},
        )
        f3_matches = [
            path
            for path in (ATLAS_ROOT / "specs").glob("ATLAS.LFUNC.*.json")
            if read_json(path)["identity_kernel"]["slug"] == wrapper.EXISTING_F3_SPEC_SLUG
        ]
        self.assertEqual(len(f3_matches), 1)
        for q, spec in self.specs_by_q.items():
            self.assertEqual(spec["base_field"]["label"], f"F_{q}(T)")
            self.assertEqual(spec["conductor"]["norm_decimal"], str(q**5))
            self.assertEqual(spec["classification"]["automorphic_class"], "GL1")

    def test_records_are_draft_content_addressed_and_programme_bound(self) -> None:
        records = [*self.new_specs, self.detector, self.evaluation]
        for record in records:
            self.assertEqual(record["record_state"], "DRAFT")
            self.assertEqual(record["identity_sha256"], sha256_hex(record["identity_kernel"]))
            self.assertTrue(record["semantic_id"].endswith(record["identity_sha256"][:32]))
            self.assertEqual([ref["number"] for ref in record["programme_refs"]], [737, 741])

    def test_evaluation_binds_all_specs_and_source_locked_replay(self) -> None:
        bound_ids = {
            binding["semantic_id"] for binding in self.evaluation["lfunction_spec_bindings"]
        }
        self.assertEqual(bound_ids, {spec["semantic_id"] for spec in self.specs})
        adapter_paths = {binding["path"] for binding in self.evaluation["adapter_bindings"]}
        self.assertEqual(adapter_paths, {wrapper.Q_SCAN_SOURCE, wrapper.POLYNOMIAL_SOURCE})
        input_paths = {binding["path"] for binding in self.evaluation["input_bindings"]}
        self.assertEqual(
            input_paths,
            {
                wrapper.Q_SCAN_FIXTURE,
                wrapper.MOMENT_IDENTITY_NOTE,
                wrapper.MOMENT_IDENTITY_CERTIFICATE,
            },
        )
        q_scan_binding = next(
            binding
            for binding in self.evaluation["input_bindings"]
            if binding["path"] == wrapper.Q_SCAN_FIXTURE
        )
        self.assertEqual(
            self.result["source_fixture"]["canonical_sha256"],
            q_scan_binding["sha256"],
        )
        note_binding = next(
            binding
            for binding in self.evaluation["input_bindings"]
            if binding["path"] == wrapper.MOMENT_IDENTITY_NOTE
        )
        self.assertEqual(note_binding["media_type"], "text/markdown")
        self.assertEqual(self.evaluation["rigor_level"], "RIGOROUS_CERTIFIED")

    def test_compact_result_has_exact_finite_values_and_proof_backed_targets(self) -> None:
        by_q = {family["q"]: family for family in self.result["families"]}
        expected = {
            3: (162, [-104, 243], {"negative": 102, "zero": 12, "positive": 48}),
            5: (2500, [-1994, 3125], {"negative": 1650, "zero": 50, "positive": 800}),
            7: (14406, [-12340, 16807], {"negative": 9702, "zero": 336, "positive": 4368}),
        }
        for q, (members, normalized_mean, signs) in expected.items():
            self.assertEqual(by_q[q]["member_count"], members)
            self.assertEqual(by_q[q]["moments"]["normalized_K"]["mean"], normalized_mean)
            self.assertEqual(by_q[q]["sign_counts"], signs)
            self.assertTrue(all(by_q[q]["formula_matches_at_this_q"].values()))
        self.assertEqual(self.result["finite_result_status"], "RIGOROUS_CERTIFIED")
        self.assertEqual(
            self.result["resource_controls"]["candidate_cap_scope"],
            "PER_FIELD_Q_SCAN",
        )
        self.assertEqual(self.result["closed_formula_target"]["status"], wrapper.FORMULA_STATUS)
        self.assertFalse(self.result["closed_formula_target"]["not_a_theorem"])
        self.assertEqual(
            self.result["closed_formula_target"]["scope"], "every odd prime power q"
        )
        self.assertEqual(
            self.result["closed_formula_target"]["proof"]["symbolic_operations"], 1761
        )
        self.assertEqual(
            self.result["usp4_limit_target"]["status"], wrapper.MEAN_LIMIT_STATUS
        )
        self.assertFalse(self.result["usp4_limit_target"]["not_a_theorem"])
        self.assertIsNone(self.evaluation["interpretation"]["theorem_claim_id"])

    def test_raw_result_schema_and_firewalls_hold(self) -> None:
        schema_path = ROOT / wrapper.RAW_RESULT_SCHEMA
        errors = validate_instance(
            self.result,
            read_json(schema_path),
            schema_path,
            SchemaStore(),
        )
        self.assertEqual(errors, [])
        text = " ".join(
            [
                *self.result["firewalls"],
                *(item["statement"] for item in self.evaluation["firewalls"]),
                self.detector["scope_boundary"],
            ]
        ).lower()
        self.assertRegex(text, r"not (?:a theorem|theorems)")
        self.assertIn("higher moment", text.replace("higher-moment", "higher moment"))
        self.assertIn("separately bound", text)
        for name in ("pick/loewner", "xd", "hcnc", "20,000", "each field", "8-second"):
            self.assertIn(name, text)

    def test_raw_schema_rejects_q_order_duplicates_and_bad_denominator(self) -> None:
        schema_path = ROOT / wrapper.RAW_RESULT_SCHEMA
        schema = read_json(schema_path)
        hostile_cases = []

        wrong_q_values = copy.deepcopy(self.result)
        wrong_q_values["resource_controls"]["q_values"] = [3, 7, 5]
        hostile_cases.append(wrong_q_values)

        duplicate_family_q = copy.deepcopy(self.result)
        duplicate_family_q["families"][1]["q"] = 3
        hostile_cases.append(duplicate_family_q)

        zero_denominator = copy.deepcopy(self.result)
        zero_denominator["families"][0]["moments"]["normalized_K"]["mean"][1] = 0
        hostile_cases.append(zero_denominator)

        for hostile in hostile_cases:
            with self.subTest(hostile=hostile):
                self.assertTrue(
                    validate_instance(hostile, schema, schema_path, SchemaStore())
                )

    def test_stale_scan_detects_orphan_result_without_evaluation(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "results").mkdir()
            orphan = (
                root
                / "results"
                / f"ATLAS.EVAL.{wrapper.EVALUATION_SLUG}.H{'0' * 32}.json"
            )
            orphan.write_text("{}\n", encoding="utf-8")
            stale = wrapper._stale_paths(
                root, self.new_specs, self.detector, self.evaluation
            )
            self.assertEqual(stale, [orphan])

    def test_written_artifacts_equal_dynamic_builder_output(self) -> None:
        for spec in self.new_specs:
            path = ATLAS_ROOT / "specs" / f"{spec['semantic_id']}.json"
            self.assertEqual(read_json(path), spec)
        detector_path = ATLAS_ROOT / "detectors" / f"{self.detector['semantic_id']}.json"
        evaluation_path = ATLAS_ROOT / "evaluations" / f"{self.evaluation['semantic_id']}.json"
        result_path = ROOT / self.evaluation["result"]["artifact"]["path"]
        self.assertEqual(read_json(detector_path), self.detector)
        self.assertEqual(read_json(evaluation_path), self.evaluation)
        self.assertEqual(read_json(result_path), self.result)


if __name__ == "__main__":
    unittest.main()
