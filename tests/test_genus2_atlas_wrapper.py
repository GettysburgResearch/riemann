"""Focused identity, replay, and firewall checks for the genus-two atlas wrapper."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ATLAS_ROOT = ROOT / "research" / "l-families" / "atlas"
CORE = ATLAS_ROOT / "core"
sys.path.insert(0, str(CORE))

from atlas_core import read_json, sha256_hex  # noqa: E402
from validate_atlas import SchemaStore, validate_instance  # noqa: E402
import wrap_genus2_pilot  # noqa: E402


class GenusTwoAtlasWrapperTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.spec, cls.detector, cls.evaluation, cls.fixture = wrap_genus2_pilot.run(ATLAS_ROOT)

    def test_records_are_draft_content_addressed_and_programme_bound(self) -> None:
        for record, kind in (
            (self.spec, "LFUNC"),
            (self.detector, "DETECTOR"),
            (self.evaluation, "EVAL"),
        ):
            self.assertEqual(record["record_state"], "DRAFT")
            self.assertEqual(record["identity_sha256"], sha256_hex(record["identity_kernel"]))
            self.assertTrue(record["semantic_id"].startswith(f"ATLAS.{kind}."))
            self.assertTrue(record["semantic_id"].endswith(record["identity_sha256"][:32]))
            self.assertEqual([ref["number"] for ref in record["programme_refs"]], [737, 741])

    def test_evaluation_binds_spec_sources_fixture_and_schema(self) -> None:
        spec_binding = self.evaluation["lfunction_spec_bindings"][0]
        self.assertEqual(spec_binding["semantic_id"], self.spec["semantic_id"])
        self.assertEqual(spec_binding["record_sha256"], sha256_hex(self.spec))
        self.assertEqual(self.spec["base_field"]["label"], "F_3(T)")
        self.assertEqual(self.spec["conductor"]["norm_decimal"], "243")
        self.assertEqual(self.spec["classification"]["automorphic_class"], "GL1")
        self.assertIn("degree 4", self.spec["completed_normalization"]["conductor_factor"])
        adapter_paths = {binding["path"] for binding in self.evaluation["adapter_bindings"]}
        self.assertEqual(
            adapter_paths,
            {wrap_genus2_pilot.GENUS2_PILOT, wrap_genus2_pilot.POLYNOMIAL_PILOT},
        )
        self.assertEqual(
            self.evaluation["input_bindings"][0]["path"], wrap_genus2_pilot.GENUS2_FIXTURE
        )
        artifact = self.evaluation["result"]["artifact"]
        self.assertEqual(artifact["path"], wrap_genus2_pilot.GENUS2_FIXTURE)
        self.assertEqual(artifact["schema_path"], wrap_genus2_pilot.RAW_RESULT_SCHEMA)
        self.assertEqual(artifact["sha256"], sha256_hex(self.fixture))

    def test_raw_fixture_validates_against_bound_schema(self) -> None:
        schema_path = ROOT / wrap_genus2_pilot.RAW_RESULT_SCHEMA
        errors = validate_instance(
            self.fixture,
            read_json(schema_path),
            schema_path,
            SchemaStore(),
        )
        self.assertEqual(errors, [])

    def test_exact_finite_result_and_target_only_boundary_are_preserved(self) -> None:
        self.assertEqual(self.fixture["family"]["member_count"], 162)
        self.assertTrue(all(self.fixture["exact_checks"].values()))
        self.assertEqual(
            (
                self.fixture["family_statistics"]["negative_member_count"],
                self.fixture["family_statistics"]["zero_member_count"],
                self.fixture["family_statistics"]["positive_member_count"],
            ),
            (102, 12, 48),
        )
        self.assertEqual(
            self.fixture["asymptotic_target"]["status"],
            "CONJECTURAL_TARGET_NOT_A_THEOREM",
        )
        self.assertIsNone(self.evaluation["interpretation"]["theorem_claim_id"])
        self.assertEqual(self.evaluation["rigor_level"], "RIGOROUS_CERTIFIED")
        self.assertEqual(self.spec["zero_data"]["rigor_level"], "RIGOROUS_CERTIFIED")

    def test_toy_minor_is_not_conflated_with_analytic_detectors(self) -> None:
        boundary_text = " ".join(
            [
                self.detector["scope_boundary"],
                self.detector["notes"],
                *(mode["description"] for mode in self.detector["failure_modes"]),
                *(firewall["statement"] for firewall in self.evaluation["firewalls"]),
            ]
        ).lower()
        for forbidden_conflation in ("pick/loewner", "xd", "hcnc"):
            self.assertIn(forbidden_conflation, boundary_text)
        self.assertIn("toy", boundary_text)
        self.assertIn("not", boundary_text)

    def test_written_records_equal_dynamic_builder_output(self) -> None:
        spec_path = ATLAS_ROOT / "specs" / f"{self.spec['semantic_id']}.json"
        detector_path = ATLAS_ROOT / "detectors" / f"{self.detector['semantic_id']}.json"
        evaluation_path = ATLAS_ROOT / "evaluations" / f"{self.evaluation['semantic_id']}.json"
        self.assertEqual(read_json(spec_path), self.spec)
        self.assertEqual(read_json(detector_path), self.detector)
        self.assertEqual(read_json(evaluation_path), self.evaluation)


if __name__ == "__main__":
    unittest.main()
