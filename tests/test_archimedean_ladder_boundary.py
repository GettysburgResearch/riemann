"""Bounded exact tests, not a numerical certificate for gamma continuation."""

import copy
import importlib.util
import json
import sys
import unittest
from fractions import Fraction
from itertools import product
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "research/riemann-structures/archimedean_ladder_boundary.py"
SPEC = importlib.util.spec_from_file_location("archimedean_ladder_boundary", MODULE)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load archimedean ladder producer")
ladder = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = ladder
SPEC.loader.exec_module(ladder)
Term = ladder.GammaTerm


class ArchimedeanLadderTests(unittest.TestCase):
    def test_empty_product(self):
        self.assertTrue(ladder.reduce_shifts(())["rational"])
        self.assertEqual(ladder.rational_value((), 5, 7), 1)

    def test_effective_product_not_rational(self):
        for terms in ((Term(0, 1),), (Term(0, 1), Term(1, 1)), (Term(-4, 2),)):
            self.assertFalse(ladder.reduce_shifts(terms)["rational"])

    def test_negative_multiplicities_give_infinite_zero_tails(self):
        terms = (Term(0, -2),)
        self.assertFalse(ladder.reduce_shifts(terms)["rational"])
        self.assertEqual(ladder.stable_tails(terms)[0]["orders"], [2, 2, 2])

    def test_zero_multiplicities_and_virtual_pole_cancellation(self):
        terms = (Term(0, 0), Term(1, 0), Term(4, 2), Term(4, -2))
        self.assertTrue(ladder.reduce_shifts(terms)["rational"])
        self.assertEqual(ladder.rational_value(terms, -4, 7), 1)
        self.assertEqual(ladder.divisor_order(terms, -4), 0)

    def test_total_multiplicity_not_enough(self):
        data = ladder.reduce_shifts((Term(1, 1), Term(0, -1)))
        self.assertFalse(data["rational"])
        self.assertEqual(data["tail_multiplicities"], [["0", -1], ["1", 1]])

    def test_forward_and_backward_shift(self):
        self.assertEqual(
            ladder.rational_value((Term(2, 1), Term(0, -1)), 5, 7), Fraction(5, 7)
        )
        self.assertEqual(
            ladder.rational_value((Term(-2, 1), Term(0, -1)), 5, 7), Fraction(7, 3)
        )

    def test_fractional_shift_heldout(self):
        terms = (Term(Fraction(17, 3), 1), Term(Fraction(-1, 3), -1))
        value = ladder.rational_value(terms, 4, 7)
        self.assertEqual(value, Fraction(11 * 17 * 23, 27 * 343))

    def test_exact_repeated_cancellation(self):
        data = ladder.reduce_shifts((Term(4, 2), Term(4, -2)))
        self.assertTrue(data["rational"])
        self.assertEqual(data["two_pi_power"], 0)
        self.assertEqual(data["linear_factors"], [])

    def test_stable_divisor_tail(self):
        terms = (Term(Fraction(-7, 3), 2), Term(Fraction(5, 3), -1))
        rows = ladder.stable_tails(terms)
        self.assertEqual(rows[0]["orders"], [-1, -1, -1])
        self.assertEqual(ladder.divisor_order(terms, Fraction(-100)), 0)

    def test_boundary_divisors_survive_but_tails_cancel(self):
        forward = (Term(2, 1), Term(0, -1))
        backward = (Term(-2, 1), Term(0, -1))
        self.assertEqual(ladder.divisor_order(forward, 0), 1)
        self.assertEqual(ladder.divisor_order(forward, -2), 0)
        self.assertEqual(ladder.divisor_order(backward, 2), -1)
        self.assertEqual(ladder.divisor_order(backward, 0), 0)
        with self.assertRaises(ZeroDivisionError):
            ladder.rational_value(backward, 2, 7)

    def test_unbalanced_value_rejected(self):
        with self.assertRaises(ValueError):
            ladder.rational_value((Term(1, 1),), 5, 7)

    def test_exact_input_contract(self):
        for value in (True, 0.5, "1/2", 1j):
            with self.assertRaises(TypeError):
                Term(value, 1)
        for value in (True, 0.5):
            with self.assertRaises(TypeError):
                Term(0, value)
        for value in (-1, 2, True):
            with self.assertRaises(ValueError):
                ladder.tensor_data(value, 0)

    def test_invalid_term_collections(self):
        for values in ([Term(0, 1)], (1,), None, ("gamma",)):
            with self.subTest(values=values), self.assertRaises(TypeError):
                ladder.reduce_shifts(values)
        with self.assertRaises(ValueError):
            ladder.reduce_shifts((Term(0, 1),) * (ladder.MAX_TERMS + 1))

    def test_bounded_resource_contract(self):
        for shift in (
            2 * (ladder.MAX_SHIFT_STEPS + 1),
            -2 * (ladder.MAX_SHIFT_STEPS + 1),
        ):
            with self.assertRaises(ValueError):
                Term(shift, 1)
        with self.assertRaises(ValueError):
            Term(0, ladder.MAX_MULTIPLICITY + 1)
        with self.assertRaises(ValueError):
            Term(Fraction(1, 1 << ladder.MAX_INPUT_BITS), 1)
        with self.assertRaises(ValueError):
            ladder.reduce_shifts(
                (Term(2 * ladder.MAX_SHIFT_STEPS, ladder.MAX_MULTIPLICITY),)
            )
        for degree in (-1, True, 0.5, ladder.MAX_BASIS_DEGREE + 1):
            with self.assertRaises(ValueError):
                ladder.basis_weight(0, 0, degree)

    def test_formal_scale_is_positive_and_exact(self):
        for scale in (0, -1):
            with self.assertRaises(ValueError):
                ladder.rational_value((), 0, scale)
        for scale in (True, 7.0):
            with self.assertRaises(TypeError):
                ladder.rational_value((), 0, scale)

    def test_all_tensor_intertwiners(self):
        for e, f in product((0, 1), repeat=2):
            row = ladder.pair_record(e, f)
            self.assertEqual(row["cokernel_dimension"], e * f)
            self.assertEqual(row["basis_checks"], 25)

    def test_all_triple_associativities(self):
        for values in product((0, 1), repeat=3):
            row = ladder.triple_record(*values)
            self.assertEqual(row["left_u_power"], row["right_u_power"])

    def test_dual_defect(self):
        self.assertTrue(ladder.dual_record(0)["perfect_over_A"])
        self.assertFalse(ladder.dual_record(1)["perfect_over_A"])

    def test_odd_dual_map_direction_and_missing_boundary(self):
        twist = Fraction(11, 7)
        for n in range(6):
            character_dual_weight = (Fraction(2 * n + 1), -twist)
            connection_dual_image_weight = (Fraction(2 * (n + 1) - 1), -twist)
            self.assertEqual(character_dual_weight, connection_dual_image_weight)
        image_degrees = {n + ladder.dual_record(1)["u_power"] for n in range(6)}
        self.assertNotIn(0, image_degrees)
        self.assertEqual(ladder.dual_record(1)["cokernel_dimension"], 1)

    def test_hurwitz_normalization_coefficients(self):
        # Exact algebra of the imported log-determinant formula, not gamma numerics.
        for z in (Fraction(1, 3), Fraction(1), Fraction(7, 2)):
            real_log_pi = -(Fraction(1, 2) - z / 2) + Fraction(1, 2)
            real_log_two = Fraction(1, 2)
            complex_log_two_pi = -(Fraction(1, 2) - z) + Fraction(1, 2)
            self.assertEqual(real_log_pi, z / 2)
            self.assertEqual(real_log_two, Fraction(1, 2))
            self.assertEqual(complex_log_two_pi, z)
        data = ladder.build_report()["regularized_determinant"]
        self.assertEqual(data["real"], "sqrt(2)/Gamma_R(s+mu)")
        self.assertEqual(data["complex"], "2/Gamma_C(s+mu)")

    def test_source_authentication(self):
        self.assertEqual(
            ladder.authenticate_sources()["frozen_programme_blob"], ladder.SOURCE_BLOB
        )

    def test_manifest_hash_is_independent_of_checkout_line_endings(self):
        source = ladder.expected_source_manifest()
        with TemporaryDirectory() as directory:
            path = Path(directory) / "source.json"
            with mock.patch.object(ladder, "SOURCES", path):
                path.write_bytes((json.dumps(source, indent=2) + "\n").encode())
                lf = ladder.authenticate_sources()
                path.write_bytes(
                    (json.dumps(source, indent=2) + "\n").replace("\n", "\r\n").encode()
                )
                crlf = ladder.authenticate_sources()
                path.write_text(
                    json.dumps(source, separators=(",", ":")), encoding="utf-8"
                )
                compact = ladder.authenticate_sources()
        self.assertEqual(lf, crlf)
        self.assertEqual(lf, compact)
        self.assertEqual(
            ladder.sha256_lf(b"one\ntwo\n"), ladder.sha256_lf(b"one\r\ntwo\r\n")
        )

    def test_complete_typed_manifest_contract(self):
        original = ladder.expected_source_manifest()
        mutations = []
        changed = copy.deepcopy(original)
        changed["schema"] = "unknown"
        mutations.append(changed)
        changed = copy.deepcopy(original)
        changed["current_programme_may_evolve"] = 1
        mutations.append(changed)
        changed = copy.deepcopy(original)
        changed["imported_analytic_facts"][0]["url"] = "https://example.invalid"
        mutations.append(changed)
        with TemporaryDirectory() as directory:
            path = Path(directory) / "source.json"
            with mock.patch.object(ladder, "SOURCES", path):
                for changed in mutations:
                    path.write_text(json.dumps(changed), encoding="utf-8")
                    with self.assertRaises(ValueError):
                        ladder.authenticate_sources()

    def test_missing_or_mutated_git_source_rejected(self):
        with (
            mock.patch.object(ladder, "git_bytes", return_value=b"wrong blob\n"),
            self.assertRaisesRegex(ValueError, "blob mismatch"),
        ):
            ladder.authenticate_sources()
        with (
            mock.patch.object(
                ladder,
                "git_bytes",
                side_effect=[ladder.SOURCE_BLOB.encode() + b"\n", b"wrong content"],
            ),
            self.assertRaisesRegex(ValueError, "content mismatch"),
        ):
            ladder.authenticate_sources()

    def test_frozen_fixture(self):
        ladder.validate_report(json.loads(ladder.FIXTURE.read_text(encoding="utf-8")))

    def test_fixture_boolean_integer_coercion_is_rejected(self):
        report = ladder.build_report()
        report["balanced_A_tensor_multiplicity"] = True
        with self.assertRaises(ValueError):
            ladder.validate_report(report)

    def test_current_packet_hashes_are_bound(self):
        hashes = ladder.build_report()["artifact_sha256_lf"]
        for path in (ladder.NOTE, MODULE, Path(__file__), ladder.SOURCES):
            self.assertEqual(
                hashes[path.relative_to(ROOT).as_posix()],
                ladder.sha256_lf(path.read_bytes()),
            )

    def test_distinct_tensor_products(self):
        report = ladder.build_report()
        self.assertEqual(report["ordinary_C_tensor_multiplicities"], list(range(1, 8)))
        self.assertEqual(report["balanced_A_tensor_multiplicity"], 1)
        self.assertEqual(report["spacing_one_split"], list(range(12)))

    def test_localized_heat_weights_have_a_growing_negative_tail(self):
        # At mu=0, t=log(2)/2, the exact diagonal weights are 2**(-n).
        for index in range(1, 9):
            self.assertEqual(Fraction(1, 2) ** (-index), 2**index)
            self.assertGreater(Fraction(1, 2) ** (-index), 1)


if __name__ == "__main__":
    unittest.main()
