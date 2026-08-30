"""Independent algebra controls and hostile contracts for circle-probe geometry."""

from __future__ import annotations

import importlib.util
import json
import unittest
from fractions import Fraction
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/l-families/atlas/generalized/circle_probe_geometry.py"
SPEC = importlib.util.spec_from_file_location("circle_geometry", PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load circle geometry producer")
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class TouchingTests(unittest.TestCase):
    def test_spectrum_by_independent_laurent_multiplication(self):
        for degree, weight in ((1, 3), (1, -3), (4, -10), (5, 15), (0, 0)):
            answer = {(weight - degree) // 2: Fraction(1)}
            for _ in range(degree):
                output = {}
                for label, value in answer.items():
                    output[label] = output.get(label, 0) + value
                    output[label + 1] = output.get(label + 1, 0) + value
                answer = output
            self.assertEqual(M.touching_spectrum(degree, weight), answer)

    def test_exotic_positive_and_negative_weights_at_i(self):
        # z=1+i; z^2/conj(z)=-1+i, and conjugation reverses weight.
        value = (Fraction(1), Fraction(1))
        self.assertEqual(M.monomial_map(value, 1, 3), (Fraction(-1), Fraction(1)))
        self.assertEqual(M.monomial_map(value, 1, -3), (Fraction(-1), Fraction(-1)))
        self.assertEqual(M.touching_spectrum(1, -3), {-2: 1, -1: 1})

    def test_zero_value_is_continuous_extension(self):
        for weight in (-9, -3, 1, 3, 11):
            self.assertEqual(M.monomial_map(M.C.ZERO, 1, weight), M.C.ZERO)
            self.assertEqual(
                M.laurent_value(M.touching_spectrum(1, weight), (-1, 0)), M.C.ZERO
            )
        self.assertEqual(M.monomial_map(M.C.ZERO, 0, 0), M.C.ONE)
        self.assertEqual(M.laurent_value(M.touching_spectrum(0, 0), (-1, 0)), M.C.ONE)

    def test_negative_power_contract(self):
        self.assertEqual(M.signed_power((1, 1), -1), (Fraction(1, 2), Fraction(-1, 2)))
        with self.assertRaisesRegex(ValueError, "division by zero"):
            M.signed_power((0, 0), -1)
        with self.assertRaises(TypeError):
            M.signed_power((1, 0), True)

    def test_degree_zero_and_parity_refusals(self):
        for degree, weight in ((0, 2), (0, -2), (1, 0), (2, 3)):
            with self.assertRaises(ValueError):
                M.touching_spectrum(degree, weight)
        for degree, weight in ((7, 7), (-1, 1), (2, 100000)):
            with self.assertRaises(ValueError):
                M.touching_spectrum(degree, weight)
        with self.assertRaises(TypeError):
            M.touching_spectrum(True, 1)

    def test_exact_multiplicativity_off_and_at_zero(self):
        a, b = (Fraction(2), Fraction(1)), (Fraction(-1), Fraction(3))
        for degree, weight in ((0, 0), (1, -3), (2, 8), (3, 1)):
            self.assertEqual(
                M.monomial_map(M.C.gmul(a, b), degree, weight),
                M.C.gmul(
                    M.monomial_map(a, degree, weight), M.monomial_map(b, degree, weight)
                ),
            )
            self.assertEqual(
                M.monomial_map(M.C.ZERO, degree, weight),
                M.C.gmul(
                    M.monomial_map(a, degree, weight),
                    M.monomial_map(M.C.ZERO, degree, weight),
                ),
            )


class HeldOutTests(unittest.TestCase):
    def test_inside_outside_polynomial_spectrum_independently(self):
        for center in (Fraction(0), Fraction(1, 2), Fraction(1), Fraction(2)):
            answer = {0: Fraction(1)}
            for shift in (1, 1, -1):
                output = {}
                for label, value in answer.items():
                    output[label] = output.get(label, 0) + center * value
                    output[label + shift] = output.get(label + shift, 0) + value
                answer = output
            answer = {label: value for label, value in answer.items() if value}
            self.assertEqual(M.polynomial_spectrum(center, 2, 1), answer)
            self.assertEqual(len(answer), 1 if center == 0 else 4)

    def test_same_exotic_formula_fails_on_both_sides(self):
        # Phi(1/2+i)=-11/10-i/5 and Phi(2+i)=2/5+11i/5.
        self.assertEqual(
            M.monomial_map((Fraction(1, 2), Fraction(1)), 1, 3),
            (Fraction(-11, 10), Fraction(-1, 5)),
        )
        self.assertEqual(
            M.monomial_map((Fraction(2), Fraction(1)), 1, 3),
            (Fraction(2, 5), Fraction(11, 5)),
        )
        for center in (Fraction(1, 2), Fraction(2)):
            row = M.moved_circle_control(center)
            self.assertNotEqual(row["actual"], row["incorrect_transplanted_c1_formula"])

    def test_hand_selected_theorem_chambers(self):
        centers = (0, Fraction(1, 2), 1, 2)
        # Explicit expected orders, independently chosen from the theorem statement.
        for parameters, orders in (
            ((0, 0, 0), (1, 1, 1, 1)),
            ((2, 0, 0), (1, 3, 3, 3)),
            ((1, 0, -3), (1, None, 2, None)),
            ((3, 0, 7), (1, None, 4, None)),
            ((Fraction(1, 2), 0, 0), (1, None, None, None)),
            ((2, 1, 0), (1, None, None, None)),
            ((2, 0, 1), (1, None, None, None)),
        ):
            self.assertEqual(
                tuple(
                    M.specialize_theorem(*parameters, center)["order"]
                    for center in centers
                ),
                orders,
            )

    def test_continuity_and_exact_parameter_refusals(self):
        for parameters in ((0, 0, 2), (0, 1, 0), (-1, 0, 0)):
            with self.assertRaisesRegex(ValueError, "continuous normalized"):
                M.specialize_theorem(*parameters, 1)
        with self.assertRaises(TypeError):
            M.specialize_theorem(1.0, 0, 1, 1)
        with self.assertRaises(TypeError):
            M.polynomial_spectrum(True, 1, 0)
        with self.assertRaises(ValueError):
            M.polynomial_spectrum(-1, 1, 0)
        with self.assertRaises(ValueError):
            M.polynomial_spectrum(Fraction(2**65), 1, 0)
        with self.assertRaisesRegex(ValueError, "unit-circle"):
            M.laurent_value({0: Fraction(1)}, (2, 0))


class ProvenanceTests(unittest.TestCase):
    def test_authentication_precedes_import(self):
        with (
            patch.object(M, "authenticate", side_effect=ValueError("untrusted source")),
            patch.object(M.importlib.util, "spec_from_file_location") as importer,
        ):
            with self.assertRaisesRegex(ValueError, "untrusted source"):
                M.load_precursor()
            importer.assert_not_called()

    def test_manifest_mutation_refused(self):
        with (
            patch.object(Path, "read_text", return_value="{}"),
            self.assertRaisesRegex(ValueError, "compiled contract"),
        ):
            M.authenticate()

    def test_current_source_mutation_refused(self):
        original = Path.read_bytes

        def changed(path):
            if path == ROOT / M.SOURCE_ROWS[0][0]:
                return b"mutated source"
            return original(path)

        with (
            patch.object(Path, "read_bytes", changed),
            self.assertRaisesRegex(ValueError, "current primitive"),
        ):
            M.authenticate()

    def test_full_replay_and_nonanalytic_scope(self):
        payload = M.produce()
        self.assertEqual(payload, json.loads(M.FIXTURE.read_text(encoding="utf-8")))
        self.assertEqual(len(payload["touching"]), 29)
        self.assertEqual(len(payload["polynomial_probes"]), 24)
        self.assertEqual(len(payload["theorem_specializations"]), 36)
        for row in payload["theorem_specializations"]:
            self.assertIn("not_finite_sample_certificate", row["evidence_kind"])
        self.assertIn("no natural-boundary theorem", payload["firewalls"])


if __name__ == "__main__":
    unittest.main()
