"""Independent algebra countercontrols and the new single-witness contract."""

import gc
import importlib.util
import math
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = ROOT / "research/l-families/atlas/generalized/segre-hadamard-source"
SPEC = importlib.util.spec_from_file_location(
    "single_top_witness_tested", DIRECTORY / "single_top_witness.py"
)
W = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(W)


def example(denominator=2, extra_row=False):
    columns = [{0: 1}, {1: denominator}, {0: -1}, {1: -1}]
    if extra_row:
        columns[3][2] = 1
    return columns, [{0: 1, 2: 1}]


class SingleWitnessAuthentication(unittest.TestCase):
    def test_pending_pin_refuses_before_git(self):
        with (
            patch.object(W, "FREEZE", "PENDING"),
            patch.object(
                W.subprocess,
                "check_output",
                side_effect=AssertionError("source touched"),
            ),
            self.assertRaisesRegex(ValueError, "pins"),
        ):
            W.authenticate()

    def test_authentication_precedes_compilation(self):
        with (
            patch.object(W, "authenticate", side_effect=ValueError("blocked source")),
            patch("builtins.compile", side_effect=AssertionError("compiled too early")),
            self.assertRaisesRegex(ValueError, "blocked source"),
        ):
            W.source()

    def test_strict_json_and_typed_equality(self):
        for raw in (b'{"a":1.0}', b'{"a":NaN}', b'{"a":1,"a":2}'):
            with self.assertRaises(ValueError):
                W.read_json(raw)
        for altered in (True, 1.0):
            with self.assertRaises(ValueError):
                W.equal({"a": 1}, {"a": altered})
        with self.assertRaises(ValueError):
            W.checked(True)

    def test_body_and_owned_bindings(self):
        value = {"value": 1}
        value["proof_object_sha256"] = W.digest(value)
        W.body_check(value)
        value["value"] = True
        with self.assertRaises(ValueError):
            W.body_check(value)
        bindings = W.owned_bindings()
        self.assertEqual(len(bindings), 4)
        self.assertTrue(all(len(x) == 64 for x in bindings.values()))


class SingleWitnessAlgebra(unittest.TestCase):
    def test_fixed_primes_and_caps(self):
        for prime in W.MODULI:
            self.assertTrue(all(prime % d for d in range(2, math.isqrt(prime) + 1)))
        columns, old = example()
        for modulus in (True, 65519, 65521.0):
            with self.assertRaises(ValueError):
                W.dixon_attempt(columns, old, modulus)
        with self.assertRaises(ValueError):
            W.dixon_attempt(columns, old, W.MODULI[0], 17)
        with self.assertRaises(W.CapacityError):
            W.lu_factor([[1 << 4096]], W.MODULI[0])

    def test_lu_row_permutation_and_direct_residual(self):
        matrix = [[0, 2, -3], [5, 1, 4], [1, -2, 7]]
        expected = [17, 23, 31]
        rhs = [sum(a * b for a, b in zip(row, expected, strict=True)) for row in matrix]
        for prime in W.MODULI:
            factor = W.lu_factor(matrix, prime)
            solution = W.lu_solve(factor, rhs)
            self.assertEqual(solution, expected)
            self.assertNotEqual(factor["permutation"], [0, 1, 2])
            self.assertTrue(
                all(
                    (sum(a * b for a, b in zip(row, solution, strict=True)) - target)
                    % prime
                    == 0
                    for row, target in zip(matrix, rhs, strict=True)
                )
            )
        self.assertIsNone(W.lu_factor([[1, 2], [2, 4]], W.MODULI[0]))

    def test_signed_rational_reconstruction(self):
        modulus = W.MODULI[0] ** 2
        for numerator, denominator in ((0, 1), (1, 257), (-17, 113), (251, 2)):
            residue = numerator * pow(denominator, -1, modulus) % modulus
            self.assertEqual(
                W.rational_reconstruct(residue, modulus), (numerator, denominator)
            )
        self.assertNotEqual(
            W.rational_reconstruct(pow(257, -1, W.MODULI[0]), W.MODULI[0]), (1, 257)
        )

    def test_multilift_actual_integer_witness(self):
        columns, old = example(257)
        vector, record = W.dixon_attempt(columns, old, W.MODULI[0])
        self.assertEqual(vector, {1: 1, 3: 257})
        self.assertEqual(record["status"], "PASS_SINGLE_WITNESS")
        self.assertEqual(len(record["lifts"]), 2)
        self.assertNotEqual(record["lifts"][0]["status"], "EXACT_WITNESS_ACCEPTED")
        self.assertEqual(record["lifts"][-1]["full_original_residual"], [])

    def test_unselected_original_row_falsifies_candidate(self):
        columns, old = example(257, extra_row=True)
        vector, record = W.dixon_attempt(columns, old, W.MODULI[0], 2)
        self.assertIsNone(vector)
        self.assertEqual(record["status"], "UNKNOWN_LIFT_BUDGET_EXHAUSTED")
        self.assertNotIn(2, record["subsystem"]["selected_original_rows"])
        self.assertEqual(record["lifts"][-1]["full_original_residual"], [[2, 257]])

    def test_modular_old_rank_drop_is_not_rational_dependence(self):
        columns, old = example()
        old = [{i: x * W.MODULI[0] for i, x in old[0].items()}]
        vector, first = W.dixon_attempt(columns, old, W.MODULI[0])
        self.assertIsNone(vector)
        self.assertEqual(first["status"], "UNKNOWN_OLD_MINOR_RANK_DROP")
        vector, second = W.dixon_attempt(columns, old, W.MODULI[1])
        self.assertIsNotNone(vector)
        self.assertEqual(second["status"], "PASS_SINGLE_WITNESS")

    def test_complete_minor_rejects_modular_rank_counterfeit(self):
        old = [{0: 1}, {0: 1, 1: W.MODULI[0]}]
        with self.assertRaisesRegex(ValueError, "nonsingular"):
            W.minor_certificate(old, [0, 1], W.MODULI[0])
        certificate = W.minor_certificate(old, [0, 1], W.MODULI[1])
        self.assertEqual(certificate["determinant_mod_prime"], W.MODULI[0])
        for gauge in ([0, 0], [0, True], [0, 1.0]):
            with self.assertRaises(ValueError):
                W.minor_certificate(old, gauge, W.MODULI[1])

    def test_exact_gauge_proves_nonmembership_not_just_residual(self):
        columns, old = example(2)
        self.assertEqual(W.full_residual(columns, old[0]), {})
        with self.assertRaisesRegex(ValueError, "gauge"):
            W.verify_witness(columns, old, [0], W.MODULI[0], old[0])
        certificate = W.verify_witness(columns, old, [0], W.MODULI[0], {1: 1, 3: 2})
        self.assertFalse(certificate["central_kernel_dimension_measured"])

    def test_zero_nonprimitive_and_changed_top_refused(self):
        columns, old = example(2)
        for vector in ({}, {1: 2, 3: 4}, {1: 1, 3: 3}, {1: True, 3: 2}):
            with self.assertRaises(ValueError):
                W.verify_witness(columns, old, [0], W.MODULI[0], vector)

    def test_subsystem_rank_drop_and_ordered_fallback(self):
        columns = [{0: 1}, {}, {0: -1}, {}]
        old = [{0: 1, 2: 1}]
        vector, attempts = W.search(columns, old)
        self.assertIsNone(vector)
        self.assertEqual([a["modulus"] for a in attempts], list(W.MODULI))
        self.assertTrue(
            all(a["status"] == "UNKNOWN_SUBSYSTEM_RANK_DROP" for a in attempts)
        )


class SingleWitnessSource(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.central, cls.prefix, cls.context = W.source()
        cls.evaluation, cls.original = cls.central.central_matrix(cls.context)
        cls.old, cls.old_records = cls.central.old_central_columns(
            cls.context, cls.evaluation, cls.original
        )

    @classmethod
    def tearDownClass(cls):
        for name in (
            "central",
            "prefix",
            "context",
            "evaluation",
            "original",
            "old",
            "old_records",
        ):
            delattr(cls, name)
        gc.collect()

    def test_fresh_source_and_complete_old_count(self):
        self.assertEqual(len(self.evaluation["columns"]), 592)
        self.assertEqual(len(self.evaluation["target_basis"]), 86515)
        self.assertEqual(len(self.old), 49)
        self.assertEqual(len(set(self.original)), 592)
        self.assertTrue(
            all(weight == (7, 7, 7) for weight in self.evaluation["weights"])
        )

    def test_all_old_polynomial_rows_and_labels(self):
        self.assertTrue(
            all(not W.full_residual(self.evaluation["columns"], v) for v in self.old)
        )
        expected = []
        helper = self.context.helper
        for i, column in enumerate(self.context.maps["D3_columns"]):
            for exponent in helper.compositions(7 - column["degree"], 10):
                if helper.add(helper.polynomial_weight(exponent), column["weight"]) == (
                    7,
                    7,
                    7,
                ):
                    expected.append((i, list(exponent)))
        self.assertEqual(
            [(r["D3_generator"], r["multiplier"]) for r in self.old_records], expected
        )

    def test_old_coordinate_minor_and_actual_543_gauge(self):
        for prime in W.MODULI:
            selection = W.select_rows(self.old, prime, 49)
            gauge = selection["selected_original_rows"]
            restricted = self.context.streamed.restricted_columns(self.old, gauge)
            independent = self.context.streamed.modular_rank640(restricted, prime)
            self.assertEqual(independent["rank"], selection["selected_rank"])
            if selection["selected_rank"] == 49:
                certificate = W.minor_certificate(self.old, gauge, prime)
                self.assertNotEqual(certificate["determinant_mod_prime"], 0)
                self.assertEqual(len([i for i in range(592) if i not in gauge]), 543)

    def test_accepted_lower_maps_preserved_without_grade7_claim(self):
        self.assertEqual(len(self.context.maps["D3_columns"]), 28)
        for key in (
            "F0_generators",
            "D1_columns",
            "D2_columns",
            "D3_columns",
            "stages",
        ):
            self.assertEqual(
                self.prefix.digest(self.context.maps[key]),
                self.context.inherited["lower_map_hashes"][key],
            )
        self.assertEqual(self.central.HELPER_FREEZE, W.PROOF_FREEZE)


class SingleWitnessCertified(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture = W.read_json(W.FIXTURE.read_bytes())
        W.body_check(cls.fixture)
        cls.fresh = W.build()
        W.need(
            cls.fresh["status"] == "PASS_SINGLE_WITNESS",
            "final tests require a certified witness",
        )

    @classmethod
    def tearDownClass(cls):
        del cls.fixture
        del cls.fresh
        gc.collect()

    def test_complete_fresh_replay(self):
        W.equal(self.fixture, self.fresh)

    def test_exact_witness_and_original_columns(self):
        data = self.fresh["original_central_data"]
        columns = [dict(c) for c in data["all_original_columns"]]
        old = [dict(c["central_coordinates"]) for c in data["complete_old_columns"]]
        accepted = self.fresh["attempts"][-1]
        vector = dict(self.fresh["selected_top_vector"])
        certificate = W.verify_witness(
            columns,
            old,
            accepted["old_minor"]["gauge_coordinates"],
            accepted["modulus"],
            vector,
        )
        W.equal(certificate, accepted["acceptance"])

    def test_actual_top_map_and_complete_resolution(self):
        top = self.fresh["actual_top_polynomial_column"]
        self.assertEqual(top["degree"], 7)
        self.assertEqual(tuple(top["weight"]), (7, 7, 7))
        self.assertEqual(len(self.fresh["result"]["D3_columns"]), 29)
        self.assertTrue(self.fresh["complete_minimal_resolution"])
        self.assertTrue(self.fresh["result"]["all_old_and_new_compositions_zero"])

    def test_nonmeasured_global_deductions(self):
        result = self.fresh["deductions_after_top_class"]
        self.assertEqual(result["global_degree7_old_dimension"], 775)
        self.assertEqual(result["global_degree7_kernel_dimension"], 776)
        self.assertFalse(result["these_global_dimensions_are_measurements"])

    def test_old_contracts_stay_uncompleted(self):
        contract = self.fresh["contract"]
        for key in (
            "full_central_kernel_computed",
            "central_kernel_dimension_measured",
            "modular_rank_promoted_to_rational_nullity",
            "old20_contract_completed",
            "old52_contract_completed",
            "old42_contract_completed",
            "old26_contract_completed",
            "full_composed_contract_completed",
            "lower_stage_elimination_replayed",
            "coordinate_acquisition_replayed",
            "marked_lifts_claimed_GL3_equivariant",
        ):
            self.assertIs(contract[key], False)

    def test_failed_attempts_and_lift_bounds_retained(self):
        attempts = self.fresh["attempts"]
        self.assertEqual(
            [a["modulus"] for a in attempts], list(W.MODULI[: len(attempts)])
        )
        self.assertEqual(attempts[-1]["status"], "PASS_SINGLE_WITNESS")
        for attempt in attempts:
            self.assertLessEqual(len(attempt["lifts"]), 16)
            self.assertEqual(
                [r["lift"] for r in attempt["lifts"]],
                list(range(1, len(attempt["lifts"]) + 1)),
            )
        self.assertEqual(attempts[-1]["lifts"][-1]["status"], "EXACT_WITNESS_ACCEPTED")

    def test_preserved_lower_maps_and_complete_owned_binding(self):
        for key in ("F0_generators", "D1_columns", "D2_columns", "stages"):
            self.assertEqual(
                W.digest(self.fresh["result"][key]),
                self.fresh["inherited_proofs"]["lower_map_hashes"][key],
            )
        self.assertEqual(
            W.digest(self.fresh["result"]["D3_columns"][:28]),
            self.fresh["inherited_proofs"]["lower_map_hashes"]["D3_columns"],
        )
        W.equal(self.fresh["owned_sha256_lf"], W.owned_bindings())

    def test_typed_body_and_source_forgeries_refused(self):
        altered = dict(self.fixture)
        altered["complete_minimal_resolution"] = 1
        with self.assertRaises(ValueError):
            W.body_check(altered)
        altered["proof_object_sha256"] = W.digest(
            {k: v for k, v in altered.items() if k != "proof_object_sha256"}
        )
        with self.assertRaises(ValueError):
            W.equal(altered, self.fresh)


if __name__ == "__main__":
    unittest.main()
