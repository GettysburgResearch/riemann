from __future__ import annotations

import importlib.util
import json
import math
import unittest
from fractions import Fraction
from itertools import pairwise
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_chebyshev_max_cusp_compensation.py"
)
NOTE = SCRIPT.with_name("FFPS_CHEBYSHEV_MAX_CUSP_COMPENSATION.md")
SPEC = importlib.util.spec_from_file_location("chebyshev_cusp", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load Chebyshev max-cusp producer")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class ChebyshevMaxCuspCompensationTest(unittest.TestCase):
    def test_source_contract(self) -> None:
        subject.check_source_blobs()

    def test_first_primitive_energy_ratios(self) -> None:
        self.assertAlmostEqual(subject.primitive_energy_ratio(1), 1 / 12)
        self.assertAlmostEqual(subject.primitive_energy_ratio(2), 1 / 48)
        self.assertAlmostEqual(subject.primitive_l1_ratio(1), 1 / 4)
        self.assertAlmostEqual(subject.primitive_l1_ratio(2), 1 / 8)

    def test_independent_cell_integral(self) -> None:
        for order in range(1, 9):
            self.assertAlmostEqual(
                subject.primitive_energy_ratio(order),
                subject.primitive_energy_ratio_by_cells(order),
                places=13,
            )
            self.assertAlmostEqual(
                subject.primitive_energy_ratio(order),
                subject.primitive_energy_ratio_cosine(order),
                places=13,
            )

    def test_order_constants(self) -> None:
        self.assertEqual(subject.order_constant(1), Fraction(100, 3))
        self.assertEqual(subject.order_constant(2), Fraction(3136, 45))

    def test_compensation_first_values(self) -> None:
        self.assertAlmostEqual(subject.compensation_product(1), 25 / 9)
        self.assertAlmostEqual(subject.compensation_product(2), Fraction(196, 135))

    def test_refill_asymptotic(self) -> None:
        for order in (100, 1000):
            scaled = (
                subject.primitive_energy_ratio(order)
                * 72
                * (order + 1) ** 2
                / math.pi**2
            )
            self.assertAlmostEqual(scaled, 1, delta=0.001)

    def test_compensation_limit(self) -> None:
        ratio = subject.compensation_product(1000) / subject.refill_limit()
        self.assertAlmostEqual(ratio, 1, delta=0.005)

    def test_strict_product_descent(self) -> None:
        products = [subject.compensation_product(order) for order in range(1, 50)]
        self.assertTrue(all(left > right for left, right in pairwise(products)))
        for order in range(1, 100):
            self.assertLess(subject.compensation_ratio_upper_bound(order), 1)
            self.assertGreater(subject.compensation_ratio_gap_numerator(order), 0)
        ledger = subject.run()["proof_ledger"]
        self.assertEqual(
            ledger["compensation_product_strictly_decreases_for_all_orders"],
            "PROVED",
        )

    def test_uniform_relative_remainder_constant(self) -> None:
        sharp = float(subject.sharp_relative_remainder_constant())
        self.assertEqual(subject.sharp_relative_remainder_constant(), Fraction(3, 16))
        self.assertAlmostEqual(subject.relative_remainder_coefficient(1), sharp)
        self.assertAlmostEqual(subject.relative_remainder_coefficient(2), sharp)
        for order in range(1, 1000):
            self.assertLessEqual(subject.relative_remainder_coefficient(order), sharp)
        coefficients = [
            subject.relative_remainder_coefficient(order) for order in range(2, 1000)
        ]
        self.assertTrue(all(left > right for left, right in pairwise(coefficients)))
        self.assertAlmostEqual(
            subject.relative_remainder_coefficient(1000),
            9 * math.pi**2 / 512,
            delta=0.001,
        )

    def test_global_tilted_jump_and_cell_formulas(self) -> None:
        for order in range(1, 9):
            coefficient = subject.primitive_energy_ratio(order)
            for z in (0.25, 1.0, 4.0):
                by_jumps = subject.tilted_zero_mode_by_jumps(order, z)
                by_cells = subject.tilted_zero_mode_by_cells(order, z)
                self.assertAlmostEqual(by_jumps, by_cells, places=11)
                self.assertGreater(by_jumps, 0)
                self.assertLess(by_jumps, z * coefficient)

    def test_stieltjes_ratio_strictly_decreases(self) -> None:
        for order in range(1, 9):
            values = [
                subject.normalized_stieltjes_ratio(order, z)
                for z in (0.0625, 0.125, 0.25, 0.5, 1, 2, 4)
            ]
            self.assertTrue(all(left > right for left, right in pairwise(values)))
            self.assertAlmostEqual(
                values[0],
                subject.primitive_energy_ratio(order),
                delta=0.02 * subject.primitive_energy_ratio(order),
            )

    def test_complex_zero_free_half_disk(self) -> None:
        for order in range(1, 9):
            coefficient = subject.primitive_energy_ratio(order)
            for z in (complex(0.5, 1), complex(0, 4), complex(2, 3)):
                value = subject.tilted_zero_mode_by_jumps_complex(order, z)
                bound = Fraction(3, 16) * abs(z) ** 2 * coefficient
                self.assertLessEqual(abs(value - z * coefficient), bound + 1e-12)
                self.assertNotEqual(value, 0)

    def test_large_tilt_endpoint(self) -> None:
        for order in range(1, 5):
            scaled = 800 * subject.tilted_zero_mode_by_cells(order, 800)
            self.assertAlmostEqual(scaled, 4, delta=0.12)
            delta = math.sin(math.pi / (2 * (order + 1))) ** 2
            for z in (8, 100):
                exact = subject.tilted_zero_mode_by_jumps(order, z)
                approximation = 4 / z - (16 * order + 8) / z**2
                bound = (
                    (16 * order**2 + 16 * order + 8) * math.exp(-z * delta / 2) / z**2
                )
                self.assertLessEqual(abs(exact - approximation), bound + 1e-13)

    def test_causal_primitive_norms_and_terminal_sensitivity(self) -> None:
        for order in range(1, 9):
            self.assertAlmostEqual(
                subject.primitive_norm_ratio(order, 1),
                subject.primitive_energy_ratio(order),
                places=13,
            )
            self.assertAlmostEqual(
                subject.primitive_mass_ratio(order, order),
                1 / (math.factorial(order) * 4**order),
                places=13,
            )

    def test_global_alternating_primitive_bounds(self) -> None:
        for order in range(1, 9):
            exact = subject.normalized_stieltjes_ratio(order, 2)
            for depth in range(1, min(order, 4) + 1):
                signed_error = (-1) ** depth * (
                    exact - subject.stieltjes_partial_sum(order, 2, depth)
                )
                self.assertGreater(signed_error, 0)

    def test_exact_second_primitive_formula(self) -> None:
        for order in range(2, 9):
            self.assertAlmostEqual(
                subject.second_primitive_energy_ratio(order),
                subject.second_primitive_energy_ratio_closed(order),
                places=13,
            )
            self.assertAlmostEqual(
                subject.primitive_norm_ratio(order, 2),
                subject.second_primitive_norm_ratio_closed(order),
                places=13,
            )
            self.assertLess(
                subject.second_primitive_energy_ratio_closed(order) * (order + 1) ** 2,
                1,
            )

    def test_second_primitive_sharp_asymptotic(self) -> None:
        scaled = subject.second_primitive_energy_ratio_closed(100) * 101**2
        self.assertAlmostEqual(scaled, math.pi**2 / 50, delta=0.0002)

    def test_linear_scale_profile(self) -> None:
        for c in (0.5, 1.0, 2.0, 5.0):
            profile = subject.linear_scale_profile(c)
            self.assertGreater(profile, 0)
            self.assertLess(profile, 1)
        self.assertEqual(subject.linear_scale_profile(0), 1)
        self.assertAlmostEqual(
            subject.linear_scale_profile(0.5),
            0.9878257496,
            places=9,
        )
        self.assertAlmostEqual(
            subject.linear_scale_profile(1e-7),
            1 - math.pi**2 * 1e-14 / 200,
            places=13,
        )
        complex_c = complex(1, 0.5)
        complex_profile = subject.linear_scale_profile_complex(complex_c)
        self.assertGreater(complex_profile.real, 0)
        self.assertAlmostEqual(
            subject.linear_scale_replay_complex(127, complex_c),
            complex_profile,
            delta=3e-5,
        )

    def test_linear_scale_finite_replay(self) -> None:
        for c in (1.0, 2.0):
            self.assertAlmostEqual(
                subject.linear_scale_replay(127, c),
                subject.linear_scale_profile(c),
                delta=6e-5,
            )

    def test_cost_charged_local_chart(self) -> None:
        order = 4
        width = 100.0
        log_x = 5.0
        z = 1e-5
        exact = subject.cost_charged_refill(order, width, log_x, z)
        main = (
            float(subject.order_constant(order))
            * subject.primitive_energy_ratio(order)
            * (1 + log_x / width) ** (2 * order + 2)
        )
        self.assertAlmostEqual(exact / main, 1, delta=0.001)
        self.assertGreater(exact, subject.refill_limit())

    def test_canonical_fixture_matches_payload(self) -> None:
        fixture = json.loads(subject.OUTPUT.read_text(encoding="utf-8"))
        self.assertEqual(fixture, subject.run())

    def test_note_control_bytes_and_math_delimiters(self) -> None:
        text = NOTE.read_text(encoding="utf-8")
        self.assertFalse(
            any(ord(character) < 32 and character not in "\n\r" for character in text)
        )
        self.assertEqual(text.count(r"\("), text.count(r"\)"))
        self.assertEqual(text.count(r"\["), text.count(r"\]"))
        self.assertEqual(text.count("~~~"), 2)

    def test_firewalls(self) -> None:
        ledger = subject.run()["proof_ledger"]
        self.assertEqual(ledger["exact_linear_max_cusp_refill"], "PROVED")
        self.assertEqual(ledger["moving_order_Perron_estimate"], "NOT PROVED")
        self.assertEqual(ledger["RH_or_GRH"], "NOT PROVED")

    def test_resource_caps(self) -> None:
        caps = subject.run()["resource_caps"]
        self.assertEqual(caps["maximum_cell_replay_order"], 8)
        self.assertEqual(caps["beta_terms"], 0)
        self.assertEqual(caps["quadratures"], 1)
        self.assertEqual(caps["profile_simpson_panels"], 4096)

    def test_validation(self) -> None:
        with self.assertRaises(ValueError):
            subject.primitive_energy_ratio(0)
        with self.assertRaises(ValueError):
            subject.cell_boundaries(-1)
        with self.assertRaises(ValueError):
            subject.order_constant(0)
        with self.assertRaises(ValueError):
            subject.tilted_zero_mode_by_jumps(1, 0)
        with self.assertRaises(ValueError):
            subject.tilted_zero_mode_by_cells(1, -1)
        with self.assertRaises(ValueError):
            subject.tilted_zero_mode_by_jumps_complex(1, complex(-1, 1))
        with self.assertRaises(ValueError):
            subject.safe_factor(1, 0, 1)
        with self.assertRaises(ValueError):
            subject.primitive_cell_polynomials(2, 0)
        with self.assertRaises(ValueError):
            subject.stieltjes_partial_sum(2, 1, 3)
        with self.assertRaises(ValueError):
            subject.second_primitive_energy_ratio_closed(1)
        with self.assertRaises(ValueError):
            subject.linear_scale_profile(-1)
        with self.assertRaises(ValueError):
            subject.linear_scale_profile(1, panels=3)
        with self.assertRaises(ValueError):
            subject.linear_scale_replay(2, 0)
        with self.assertRaises(ValueError):
            subject.linear_scale_profile_complex(complex(0, 1))
        with self.assertRaises(ValueError):
            subject.linear_scale_replay_complex(2, complex(-1, 1))


if __name__ == "__main__":
    unittest.main()
