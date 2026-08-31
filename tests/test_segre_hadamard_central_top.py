"""Central source and exact non-membership tests, with separate final obligations."""

import copy
import importlib.util
import unittest
from pathlib import Path
from unittest.mock import patch

PATH = (
    Path(__file__).resolve().parents[1]
    / "research/l-families/atlas/generalized/segre-hadamard-source/central_top_resolution.py"
)
SPEC = importlib.util.spec_from_file_location("central_top_tests", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class CentralAuthentication(unittest.TestCase):
    def test_pending_pin_fails_before_source_access(self):
        with (
            patch.object(M, "HELPER_FREEZE", "PENDING"),
            patch.object(M.subprocess, "check_output") as git,
        ):
            with self.assertRaises(ValueError):
                M.authenticate()
            git.assert_not_called()

    def test_all_direct_auth_before_helper_execution(self):
        with (
            patch.object(M, "authenticate", side_effect=ValueError("source")),
            patch("builtins.compile") as execute,
        ):
            with self.assertRaises(ValueError):
                M.source()
            execute.assert_not_called()

    def test_strict_json_and_complete_typed_comparison(self):
        for raw in (b'{"a":1.0}', b'{"a":NaN}', b'{"a":1,"a":2}'):
            with self.assertRaises(ValueError):
                M.read_json(raw)
        for value in (True, 1.0):
            with self.assertRaises(ValueError):
                M.equal({"rank": value}, {"rank": 1})

    def test_bound_proof_is_part_of_direct_inputs(self):
        self.assertIn("CENTRAL_TOP_CLASS_GLOBAL_EXACTNESS.md", M.PROOF_PINS)
        self.assertEqual(
            {name for _, name, _ in M.THEOREM_PINS},
            {
                "MATHEMATICS.md",
                "TERNARY_CUBE_TOR_CHARACTERS.md",
                "tor_characters.verification.json",
            },
        )


class CentralSourceAndAlgebra(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prefix, cls.context = M.source()
        cls.evaluation, cls.indices = M.central_matrix(cls.context)
        cls.old, cls.old_records = M.old_central_columns(
            cls.context, cls.evaluation, cls.indices
        )

    def test_all_original_central_columns_and_addresses(self):
        self.assertEqual(len(self.indices), 592)
        self.assertEqual(len(set(self.indices)), 592)
        self.assertEqual(len(self.evaluation["target_basis"]), 86515)
        self.assertTrue(all(tuple(w) == M.WEIGHT for w in self.evaluation["weights"]))
        c = self.context
        full = c.streamed.lazy_evaluation(
            c.helper, c.maps["D1_columns"], c.maps["D2_columns"], 7
        )
        for local, original in enumerate(self.indices):
            self.assertEqual(
                self.evaluation["domain_basis"][local], full["domain_basis"][original]
            )
            self.assertEqual(
                self.evaluation["columns"][local], full["columns"][original]
            )

    def test_complete_old_list_by_independent_lazy_module_route(self):
        c = self.context
        full = c.streamed.lazy_evaluation(
            c.helper, c.maps["D2_columns"], c.maps["D3_columns"], 7
        )
        selected = [
            i for i, weight in enumerate(full["weights"]) if tuple(weight) == M.WEIGHT
        ]
        self.assertEqual(len(selected), len(self.old_records))
        for original, record in zip(selected, self.old_records, strict=True):
            generator, multiplier = full["domain_basis"][original]
            self.assertEqual(
                (record["D3_generator"], tuple(record["multiplier"])),
                (generator, multiplier),
            )
            self.assertEqual(
                record["original_F2_coordinates"],
                c.upstream.sparse(full["columns"][original]),
            )

    def test_every_old_column_is_a_full_original_row_kernel_vector(self):
        for vector in self.old:
            self.assertFalse(
                self.context.helper.image_of_relation(
                    self.evaluation["columns"], vector
                )
            )

    def test_missing_lower_generator_is_rejected(self):
        maps = self.context.maps
        with (
            patch.object(
                self.context, "maps", {**maps, "D3_columns": maps["D3_columns"][:-1]}
            ),
            self.assertRaises(ValueError),
        ):
            M.old_central_columns(self.context, self.evaluation, self.indices)

    def test_exact_quotient_does_not_assume_old_columns_independent(self):
        vector, record = M.outside_old_span(
            self.context, [{0: 1}, {0: 2}], [{0: 1}, {1: 1}]
        )
        self.assertEqual(vector, {1: 1})
        self.assertEqual(record["complete_old_columns"], 2)
        self.assertEqual(record["exact_old_rank"], 1)
        self.assertEqual(record["exact_augmented_rank"], 2)

    def test_no_new_class_or_two_new_classes_is_not_accepted(self):
        for relations in ([{0: 1}], [{0: 1}, {1: 1}, {2: 1}]):
            with self.assertRaises(ValueError):
                M.outside_old_span(self.context, [{0: 1}], relations)

    def test_modular_rank_drop_cannot_fake_nonmembership(self):
        # The two old columns span Q^2 but become dependent modulo 65521.
        with self.assertRaises(ValueError):
            M.outside_old_span(
                self.context, [{0: 1}, {0: 1, 1: 65521}], [{0: 1}, {1: 1}]
            )

    def test_inherited_prefix_and_unchanged_caps(self):
        self.assertIs(self.context.inherited["lower_stage_elimination_replayed"], False)
        self.assertIs(self.context.inherited["coordinate_acquisition_replayed"], False)
        self.assertEqual(self.context.streamed.MAX_COLUMNS, 640)
        self.assertEqual(self.context.streamed.MAX_ROWS, 4096)


class CentralCertifiedTop(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record = M.read_json(M.FIXTURE.read_bytes())
        cls.prefix, cls.context = M.source()

    def test_full_final_replay(self):
        M.equal(M.build(), self.record)

    def test_one_measured_central_quotient_and_global_deduction(self):
        certificate = self.record["central_certificate"]
        quotient = certificate["quotient"]
        self.assertEqual(
            quotient["exact_augmented_rank"] - quotient["exact_old_rank"], 1
        )
        self.assertEqual(
            quotient["central_kernel_dimension_measured"],
            len(certificate["complete_central_kernel"]),
        )
        self.assertIs(quotient["global_775_column_rank_measured"], False)
        self.assertEqual(
            self.record["deductions_after_top_class"][
                "global_degree7_kernel_dimension"
            ],
            776,
        )
        self.assertIs(
            self.record["deductions_after_top_class"][
                "these_global_dimensions_are_measurements"
            ],
            False,
        )

    def test_top_polynomial_composes_to_zero_directly(self):
        top = self.record["central_certificate"]["actual_top_polynomial_column"]
        self.assertEqual(top["degree"], 7)
        self.assertEqual(top["weight"], [7, 7, 7])
        self.prefix.compose(self.record["result"]["D2_columns"], [top])

    def test_changed_top_polynomial_is_refused(self):
        top = copy.deepcopy(
            self.record["central_certificate"]["actual_top_polynomial_column"]
        )
        top["terms"][0]["coefficient"] += 2
        with self.assertRaises(ValueError):
            self.prefix.compose(self.record["result"]["D2_columns"], [top])

    def test_every_full_original_row_certificate_retained(self):
        proof = self.record["central_certificate"]["full_row_certificate"]
        self.assertEqual(proof["status"], "FULL_KERNEL_CERTIFIED")
        last = proof["attempts"][-1]["certificate"]
        self.assertIs(last["every_full_original_row_checked"], True)
        self.assertEqual(last["full_composition_failures"], [])
        self.assertIs(last["full_and_restricted_kernels_equal"], True)

    def test_old_contracts_are_not_reported_executed(self):
        contract = self.record["contract"]
        for key in (
            "global_775_column_elimination_executed",
            "global_776_vector_kernel_census_executed",
            "old52_contract_completed",
            "old42_contract_completed",
            "old26_contract_completed",
            "full_composed_contract_completed",
        ):
            self.assertIs(contract[key], False)

    def test_lower_source_maps_and_complete29_columns(self):
        maps = self.record["result"]
        self.assertEqual(len(maps["D3_columns"]), 29)
        M.equal(maps["D3_columns"][:28], self.context.maps["D3_columns"])
        self.assertIs(
            self.record["final_polynomial_checks"]["D2D3"]["all_compositions_zero"],
            True,
        )

    def test_body_or_numeric_status_counterfeit_cannot_match(self):
        changed = dict(self.record)
        changed["contract"] = {**changed["contract"], "old52_contract_completed": 0}
        with self.assertRaises(ValueError):
            M.equal(changed, self.record)
        self.assertNotEqual(
            M.digest({k: v for k, v in changed.items() if k != "proof_object_sha256"}),
            changed["proof_object_sha256"],
        )


if __name__ == "__main__":
    unittest.main()
