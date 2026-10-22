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
        self.assertEqual(
            adapter_paths,
            {
                wrapper.Q_SCAN_SOURCE,
                wrapper.POLYNOMIAL_SOURCE,
                wrapper.AFFINE_ORBIT_SOURCE,
            },
        )
        input_paths = {binding["path"] for binding in self.evaluation["input_bindings"]}
        self.assertEqual(
            input_paths,
            {
                wrapper.Q_SCAN_FIXTURE,
                wrapper.AFFINE_ORBIT_FIXTURE,
                wrapper.MOMENT_IDENTITY_NOTE,
                wrapper.MOMENT_IDENTITY_CERTIFICATE,
                wrapper.SECOND_MOMENT_REDUCTION_FIXTURE,
                wrapper.SECOND_MOMENT_REDUCTION_SOURCE,
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
        affine_binding = next(
            binding
            for binding in self.evaluation["input_bindings"]
            if binding["path"] == wrapper.AFFINE_ORBIT_FIXTURE
        )
        self.assertEqual(
            self.result["affine_orbit_certificate"]["source_fixture"][
                "canonical_sha256"
            ],
            affine_binding["sha256"],
        )
        affine_fulfillment = next(
            fulfillment
            for fulfillment in self.evaluation["input_fulfillments"]
            if fulfillment["name"] == "affine_orbit_certificate"
        )
        self.assertEqual(affine_fulfillment["input_type"], "RAW_ARTIFACT")
        self.assertEqual(affine_fulfillment["coverage_class"], "FINITE_COMPLETE")
        self.assertEqual(
            affine_fulfillment["sources"],
            [wrapper.AFFINE_ORBIT_FIXTURE, wrapper.AFFINE_ORBIT_SOURCE],
        )
        note_binding = next(
            binding
            for binding in self.evaluation["input_bindings"]
            if binding["path"] == wrapper.MOMENT_IDENTITY_NOTE
        )
        self.assertEqual(note_binding["media_type"], "text/markdown")
        second_moment_bindings = {
            binding["path"]: binding
            for binding in self.evaluation["input_bindings"]
            if binding["path"]
            in {
                wrapper.SECOND_MOMENT_REDUCTION_FIXTURE,
                wrapper.SECOND_MOMENT_REDUCTION_SOURCE,
            }
        }
        self.assertEqual(
            second_moment_bindings[wrapper.SECOND_MOMENT_REDUCTION_FIXTURE][
                "hash_mode"
            ],
            "CANONICAL_JSON_UTF8_NFC",
        )
        self.assertEqual(
            second_moment_bindings[wrapper.SECOND_MOMENT_REDUCTION_SOURCE][
                "hash_mode"
            ],
            "RAW_BYTES",
        )
        self.assertTrue(
            all(
                binding["coverage_class"] == "PARTIAL"
                for binding in second_moment_bindings.values()
            )
        )
        self.assertEqual(
            self.result["second_moment_reduction"]["source_fixture"][
                "canonical_sha256"
            ],
            second_moment_bindings[wrapper.SECOND_MOMENT_REDUCTION_FIXTURE][
                "sha256"
            ],
        )
        second_moment_fulfillment = next(
            fulfillment
            for fulfillment in self.evaluation["input_fulfillments"]
            if fulfillment["name"] == "second_moment_reduction_roadmap"
        )
        self.assertEqual(second_moment_fulfillment["coverage_class"], "PARTIAL")
        self.assertEqual(
            second_moment_fulfillment["sources"],
            [
                wrapper.SECOND_MOMENT_REDUCTION_FIXTURE,
                wrapper.SECOND_MOMENT_REDUCTION_SOURCE,
            ],
        )
        self.assertEqual(self.evaluation["rigor_level"], "RIGOROUS_CERTIFIED")

    def test_compact_result_has_exact_finite_values_and_proof_backed_targets(self) -> None:
        by_q = {family["q"]: family for family in self.result["families"]}
        expected = {
            3: (162, 2112, 1584, 372, [-104, 243], {"negative": 102, "zero": 12, "positive": 48}),
            5: (2500, 116880, 84240, 10480, [-1994, 3125], {"negative": 1650, "zero": 50, "positive": 800}),
            7: (14406, 1503936, 1059744, 88452, [-12340, 16807], {"negative": 9702, "zero": 336, "positive": 4368}),
        }
        for q, (members, sum_a_fourth, sum_a_squared_b, sum_b, normalized_mean, signs) in expected.items():
            self.assertEqual(by_q[q]["member_count"], members)
            self.assertEqual(by_q[q]["moments"]["a_fourth"]["sum"], sum_a_fourth)
            self.assertEqual(by_q[q]["moments"]["a_squared_b"]["sum"], sum_a_squared_b)
            self.assertEqual(by_q[q]["moments"]["b"]["sum"], sum_b)
            self.assertEqual(by_q[q]["moments"]["normalized_K"]["mean"], normalized_mean)
            self.assertEqual(by_q[q]["sign_counts"], signs)
            self.assertTrue(all(by_q[q]["formula_matches_at_this_q"].values()))
        expected_character_means = {
            3: {"chi_(0,1)": [-19, 81], "chi_(2,0)": [2, 81], "chi_(0,2)": [-82, 243], "chi_(2,1)": [13, 243], "chi_(4,0)": [-1, 81]},
            5: {"chi_(0,1)": [-101, 625], "chi_(2,0)": [4, 625], "chi_(0,2)": [-626, 3125], "chi_(2,1)": [43, 3125], "chi_(4,0)": [-3, 3125]},
            7: {"chi_(0,1)": [-295, 2401], "chi_(2,0)": [6, 2401], "chi_(0,2)": [-2402, 16807], "chi_(2,1)": [89, 16807], "chi_(4,0)": [-3, 16807]},
        }
        for q, profile in expected_character_means.items():
            self.assertEqual(by_q[q]["low_weight_character_means"], profile)
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
            self.result["closed_formula_target"]["proof"]["symbolic_operations"], 2925
        )
        self.assertEqual(
            self.result["closed_formula_target"]["mean_a_fourth"],
            "3*q^2-7*q+5+12/q-14/q^2-11/q^3",
        )
        self.assertEqual(
            self.result["closed_formula_target"]["mean_b"],
            "q-1+(q^2-1)/q^3",
        )
        self.assertEqual(
            self.result["closed_formula_target"]["mean_a_squared_b"],
            "(q+1)*(q^2-2*q+3)*(2*q^2-2*q-1)/q^3",
        )
        profile = self.result["closed_formula_target"]["low_weight_character_profile"]
        self.assertEqual(profile["status"], "PROVED_FROM_EXACT_COEFFICIENT_MOMENTS")
        self.assertEqual(profile["mean_chi_(0,1)"], "-1/q+1/q^2-1/q^4")
        self.assertEqual(profile["mean_chi_(2,0)"], "1/q^3-1/q^4")
        self.assertEqual(profile["mean_chi_(0,2)"], "-1/q-1/q^5")
        self.assertEqual(profile["mean_chi_(2,1)"], "2/q^3-1/q^4-2/q^5")
        self.assertEqual(profile["mean_chi_(4,0)"], "-3/q^5")
        self.assertEqual(
            self.result["usp4_limit_target"]["status"], wrapper.MEAN_LIMIT_STATUS
        )
        self.assertFalse(self.result["usp4_limit_target"]["not_a_theorem"])
        corollary = self.result["negative_proportion_corollary"]
        self.assertEqual(corollary["status"], wrapper.SIGN_DENSITY_STATUS)
        self.assertEqual(corollary["range_lower_bound"], -20)
        self.assertEqual(corollary["liminf_lower_bound"], [1, 20])
        self.assertEqual(
            corollary["frozen_lower_bound_regressions"],
            {"3": [26, 1215], "5": [997, 31250], "7": [617, 16807]},
        )
        self.assertIsNone(self.evaluation["interpretation"]["theorem_claim_id"])

    def test_second_moment_reduction_is_exact_compact_partial_and_source_locked(
        self,
    ) -> None:
        reduction = self.result["second_moment_reduction"]
        self.assertEqual(reduction["status"], wrapper.SECOND_MOMENT_REDUCTION_STATUS)
        self.assertEqual(
            reduction["master_reduction"]["formula"],
            "sum_D K_D^2=q^2*A4(q)-2*q*M22(q)+B4(q)",
        )
        self.assertEqual(
            reduction["master_reduction"]["unresolved_block"],
            "B4(q)-2*q*M22(q)",
        )
        self.assertEqual(
            reduction["master_reduction"]["proven_A4"]["status"],
            "PROVED_BY_REWEIGHTING_THE_BOUND_QUARTIC_TABLE",
        )
        self.assertEqual(
            reduction["signature_inventory"],
            {
                "M22": {
                    "signature_count": 20,
                    "signature_count_derivation": "11+5+4=20",
                    "weighted_tuple_count_formula": "q^6",
                    "maximum_tuple_weight": 180,
                },
                "B4": {
                    "signature_count": 54,
                    "signature_count_derivation": "22+11+10+6+5=54",
                    "weighted_tuple_count_formula": "q^8",
                    "maximum_tuple_weight": 2520,
                },
                "total_signature_count": 74,
            },
        )
        primitive = reduction["primitive_character_reduction"]
        self.assertEqual(primitive["marked_family_count"], 6)
        self.assertEqual(
            primitive["new_marked_primitive_coefficients"],
            {
                "degree_4": ["p1(r)"],
                "degree_6": ["p1(r)", "p2(r)"],
                "degree_8": ["p1(r)", "p2(r)", "p3(r)"],
            },
        )
        character = reduction["character_reduction"]
        self.assertEqual(
            character["mixed_trace_middle"]["formula"],
            "(Tr U)^2*e_2(U)=2*chi_00+3*chi_01+3*chi_20+chi_02+chi_21",
        )
        self.assertEqual(
            character["mixed_trace_middle"]["dimension_checksum"], 96
        )
        self.assertEqual(
            character["single_virtual_character_obstruction"]["status"],
            "EXACT_REDUCTION_UNRESOLVED_FOR_GENERAL_Q",
        )
        refined = character["refined_honest_high_weight_obstruction"]
        self.assertEqual(refined["status"], "EXACT_REDUCTION_USING_PROVED_LOW_WEIGHT_MEANS")
        self.assertEqual(refined["formula"], "H=chi_04+chi_22+2*chi_03")
        self.assertEqual(refined["dimension_checksum"], 196)
        self.assertEqual(
            [row["highest_weight_a_b"] for row in refined["decomposition"]],
            [[0, 3], [2, 2], [0, 4]],
        )
        expected_checks = {
            3: (14_448, -4_560, [-16, 27], [536, 2187]),
            5: (2_630_080, -291_920, [-174, 625], [7_154, 78_125]),
            7: (69_108_480, -4_584_384, [-428, 2401], [37_652, 823_543]),
        }
        self.assertEqual(
            [row["q"] for row in reduction["finite_histogram_checks"]],
            [3, 5, 7],
        )
        for row in reduction["finite_histogram_checks"]:
            self.assertEqual(
                (
                    row["sum_K_squared"],
                    row["unresolved_B4_minus_2qM22"],
                    row["exact_low_weight_character_correction"],
                    row["normalized_honest_high_weight_packet"],
                ),
                expected_checks[row["q"]],
            )
        resource = reduction["resource_contract"]
        self.assertEqual(resource["actual_signatures"], 74)
        self.assertLessEqual(resource["exact_operations_used"], 50_000)
        self.assertEqual(resource["field_enumeration"], "FORBIDDEN_AND_NOT_IMPORTED")
        self.assertEqual(
            reduction["source_locks"]["q_scan"]["canonical_sha256"],
            self.result["source_fixture"]["canonical_sha256"],
        )
        required = {entry["name"]: entry for entry in self.detector["required_inputs"]}
        self.assertEqual(
            required["second_moment_reduction_roadmap"]["coverage_requirement"],
            "PARTIAL",
        )
        theorem = next(
            link
            for link in self.detector["theorem_links"]
            if link["semantic_id"].endswith("SECOND_MOMENT_REDUCTION")
        )
        self.assertEqual(theorem["status"], "OPEN")

    def test_affine_orbit_certificate_is_exact_compact_and_source_bound(self) -> None:
        certificate = self.result["affine_orbit_certificate"]
        self.assertEqual(certificate["status"], wrapper.AFFINE_ORBIT_STATUS)
        self.assertEqual(
            certificate["action"],
            {
                "definition": "D^{alpha,beta}(T)=alpha^(-5)*D(alpha*T+beta)",
                "convention": "right action",
                "a_D_law": "a_{D^{alpha,beta}}=chi_q(alpha)*a_D",
                "b_D_law": "b_{D^{alpha,beta}}=b_D",
                "K_D_law": "K_{D^{alpha,beta}}=K_D for K_D=q*a_D^2-b_D^2",
            },
        )
        self.assertEqual(certificate["total_member_action_pairs_checked"], 656024)
        self.assertTrue(certificate["q_scan_regressions_all_match"])
        expected = {
            3: {
                "members": 162,
                "group": 6,
                "edges": 972,
                "orbits": 29,
                "sizes": {"3": 4, "6": 25},
                "stabilizers": {"1": 25, "2": 4},
                "signs": {"negative": (102, 19), "zero": (12, 2), "positive": (48, 8)},
            },
            5: {
                "members": 2500,
                "group": 20,
                "edges": 50000,
                "orbits": 132,
                "sizes": {"1": 1, "4": 1, "5": 3, "10": 6, "20": 121},
                "stabilizers": {"1": 121, "2": 6, "4": 3, "5": 1, "20": 1},
                "signs": {"negative": (1650, 86), "zero": (50, 4), "positive": (800, 42)},
            },
            7: {
                "members": 14406,
                "group": 42,
                "edges": 605052,
                "orbits": 349,
                "sizes": {"21": 12, "42": 337},
                "stabilizers": {"1": 337, "2": 12},
                "signs": {"negative": (9702, 237), "zero": (336, 8), "positive": (4368, 104)},
            },
        }
        self.assertEqual([row["q"] for row in certificate["families"]], [3, 5, 7])
        for row in certificate["families"]:
            control = expected[row["q"]]
            self.assertEqual(row["member_count"], control["members"])
            self.assertEqual(row["group_order"], control["group"])
            self.assertEqual(row["member_action_pairs_checked"], control["edges"])
            self.assertEqual(row["orbit_count"], control["orbits"])
            self.assertEqual(row["orbit_size_histogram"], control["sizes"])
            self.assertEqual(row["stabilizer_order_histogram"], control["stabilizers"])
            self.assertEqual(
                {
                    sign: (values["member_count"], values["orbit_count"])
                    for sign, values in row["sign_summaries"].items()
                },
                control["signs"],
            )
        invariances = {entry["code"]: entry for entry in self.detector["invariances"]}
        self.assertEqual(invariances["AFFINE_TOY_MINOR_INVARIANCE"]["status"], "PROVED")
        self.assertIn("not an asymptotic", certificate["firewall"])

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

        false_density_claim = copy.deepcopy(self.result)
        false_density_claim["negative_proportion_corollary"]["liminf_lower_bound"] = [1, 2]
        hostile_cases.append(false_density_claim)

        reversed_affine_q = copy.deepcopy(self.result)
        reversed_affine_q["affine_orbit_certificate"]["families"].reverse()
        hostile_cases.append(reversed_affine_q)

        duplicate_affine_q = copy.deepcopy(self.result)
        duplicate_affine_q["affine_orbit_certificate"]["families"][1] = copy.deepcopy(
            duplicate_affine_q["affine_orbit_certificate"]["families"][0]
        )
        hostile_cases.append(duplicate_affine_q)

        false_orbit_histogram = copy.deepcopy(self.result)
        false_orbit_histogram["affine_orbit_certificate"]["families"][2][
            "orbit_size_histogram"
        ]["42"] -= 1
        hostile_cases.append(false_orbit_histogram)

        false_affine_law = copy.deepcopy(self.result)
        false_affine_law["affine_orbit_certificate"]["action"]["b_D_law"] = "b'=chi*b"
        hostile_cases.append(false_affine_law)

        false_second_moment_status = copy.deepcopy(self.result)
        false_second_moment_status["second_moment_reduction"]["status"] = (
            "PROVED_ALL_Q_SECOND_MOMENT_FORMULA"
        )
        hostile_cases.append(false_second_moment_status)

        missing_unresolved_block = copy.deepcopy(self.result)
        del missing_unresolved_block["second_moment_reduction"]["master_reduction"][
            "unresolved_block"
        ]
        hostile_cases.append(missing_unresolved_block)

        false_signature_count = copy.deepcopy(self.result)
        false_signature_count["second_moment_reduction"]["signature_inventory"][
            "M22"
        ]["signature_count"] = 19
        hostile_cases.append(false_signature_count)

        reversed_residual_q = copy.deepcopy(self.result)
        reversed_residual_q["second_moment_reduction"][
            "finite_histogram_checks"
        ].reverse()
        hostile_cases.append(reversed_residual_q)

        false_high_weight_upgrade = copy.deepcopy(self.result)
        false_high_weight_upgrade["second_moment_reduction"]["character_reduction"][
            "refined_honest_high_weight_obstruction"
        ]["status"] = "PROVED_ZERO_AVERAGE"
        hostile_cases.append(false_high_weight_upgrade)

        enabled_field_enumeration = copy.deepcopy(self.result)
        enabled_field_enumeration["second_moment_reduction"]["resource_contract"][
            "field_enumeration"
        ] = "ENABLED"
        hostile_cases.append(enabled_field_enumeration)

        wrong_reduction_source = copy.deepcopy(self.result)
        wrong_reduction_source["second_moment_reduction"]["source_fixture"][
            "path"
        ] = "unbound.json"
        hostile_cases.append(wrong_reduction_source)

        unexpected_reduction_field = copy.deepcopy(self.result)
        unexpected_reduction_field["second_moment_reduction"]["proved"] = True
        hostile_cases.append(unexpected_reduction_field)

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
