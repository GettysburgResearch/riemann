"""Hostile rational checks; no Xi source-Pick or zero-count assertion."""

import copy
import importlib.util
import json
import unittest
from fractions import Fraction
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "research/exploratory/xi_near_adapted_scale_firewall.py"
SPEC = importlib.util.spec_from_file_location("xi_scale_firewall", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load Xi scale producer")
scale = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(scale)


class XiScaleFirewallTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = scale.build_report()

    def test_both_coefficient_certificates(self):
        for order in range(1, 16, 2):
            p, q = scale.polynomials(order)
            for j, (left, right) in enumerate(zip(p, q)):
                self.assertEqual(
                    order * left - right,
                    Fraction(2 * j * (order + 1), 2 * j + 1) * left,
                )
                self.assertEqual(
                    order * right - left,
                    Fraction((order + 1) * (order - 1 - 2 * j), 2 * j + 1) * left,
                )
                self.assertGreaterEqual(order * left - right, 0)
                self.assertGreaterEqual(order * right - left, 0)

    def test_ratio_bounds_and_evenness(self):
        for order in range(1, 16, 2):
            for x in (0, Fraction(1, 3), 1, 2, 10):
                value = scale.ratio_r(order, x)
                self.assertLessEqual(Fraction(1, order), value)
                self.assertLessEqual(value, order)
                self.assertEqual(value, scale.ratio_r(order, -x))
        self.assertEqual(scale.ratio_r(1, 19), 1)

    def test_fifth_gaussian_polynomials(self):
        self.assertEqual(
            scale.gaussian_polynomials(5),
            {
                "U": (1, 10, 15),
                "V": (0, 5, 30, 15),
                "W": (0, 1, 30, 75),
                "Z": (0, 0, 15, 150, 105),
            },
        )

    def test_fifth_exact_formulas(self):
        for nu in (Fraction(1, 16), Fraction(1, 256), Fraction(1, 4096), Fraction(4)):
            data = scale.gaussian_data(5, nu)
            self.assertEqual(
                data["g"],
                (1 + 10 * nu + 15 * nu**2) / (10 * nu + 60 * nu**2 + 30 * nu**3),
            )
            self.assertEqual(
                data["p"], (1 + 30 * nu + 75 * nu**2) / (10 + 60 * nu + 30 * nu**2)
            )

    def test_first_order_exact_control(self):
        nu, xi = Fraction(3, 7), Fraction(11, 5)
        data = scale.gaussian_data(1, nu, xi)
        self.assertEqual(data["g"], 1 / (2 * nu))
        self.assertEqual(data["p"], Fraction(1, 2))
        self.assertEqual(data["m2"], 3 * xi**2 * nu)

    def test_mismatch_identity_and_difference(self):
        data = scale.gaussian_data(5, Fraction(1, 256))
        g, p = data["g"], data["p"]
        for eta in (
            Fraction(1, 2),
            Fraction(9, 10),
            Fraction(1),
            Fraction(11, 10),
            Fraction(2),
        ):
            value = scale.phase(g, p, eta)
            self.assertEqual(value, eta * p + (1 - eta**2) * g / eta)
            self.assertEqual(abs(value - p), abs(eta - 1) * (g * (1 + 1 / eta) - p))

    def test_exact_window_endpoints(self):
        window = scale.phase_window(2, 1, 1)
        self.assertEqual(window["discriminant"], 9)
        self.assertEqual(window["width"], 1)
        self.assertEqual(window["endpoint_product"], 2)
        self.assertEqual(scale.phase(2, 1, 1), 1)
        self.assertEqual(scale.phase(2, 1, 2), -1)
        self.assertGreater(scale.phase(2, 1, Fraction(9, 10)), 1)
        self.assertLess(scale.phase(2, 1, Fraction(21, 10)), -1)

    def test_zero_bound_is_singleton_window(self):
        window = scale.phase_window(2, 1, 0)
        self.assertEqual(window["width"], 0)
        self.assertEqual(window["zero_scale_squared"], 2)

    def test_variance_gain_and_window_bounds(self):
        for order in (1, 3, 5, 9, 15):
            data = scale.gaussian_data(order, Fraction(1, 4096))
            g, p, xi, m2 = (data[key] for key in ("g", "p", "xi", "m2"))
            self.assertGreaterEqual(g, xi**2 / (2 * order * m2))
            actual = scale.phase_window(g, p, 1)
            bound = scale.variance_window_bound(order, xi, m2, 1)
            self.assertLessEqual(actual["width"], bound["width_upper"])
            self.assertLessEqual(
                actual["relative_envelope_about_one"], bound["relative_envelope_upper"]
            )

    def test_no_sign_transition_if_gain_not_larger(self):
        data = scale.gaussian_data(1, 4)
        self.assertLess(data["g"], data["p"])
        for eta in (Fraction(1, 10), Fraction(1), Fraction(10)):
            self.assertGreater(scale.phase(data["g"], data["p"], eta), 0)
        with self.assertRaises(ValueError):
            scale.phase_window(data["g"], data["p"], 1)

    def test_fixed_scale_residue_first_order(self):
        for nu in (Fraction(1, 16), Fraction(1, 4096)):
            data = scale.gaussian_data(1, nu)
            for eta in (Fraction(9, 10), Fraction(11, 10)):
                residue = (1 - eta**2) / (2 * eta)
                self.assertEqual(
                    nu * scale.phase(data["g"], data["p"], eta), residue + eta * nu / 2
                )

    def test_vanishing_fifth_scale_error_can_reverse_sign(self):
        for nu in (Fraction(1, 256), Fraction(1, 4096)):
            data = scale.gaussian_data(5, nu)
            self.assertGreater(data["p"], 0)
            self.assertLess(scale.phase(data["g"], data["p"], 1 + nu), 0)

    def test_boundary_layer_limits(self):
        for order in range(1, 16, 2):
            for slope in (Fraction(-1), Fraction(0), Fraction(1, 2), Fraction(1)):
                row = scale.boundary_layer_limit(order, slope)
                self.assertEqual(row["rho_limit"], (1 - 2 * slope) / (2 * order))
        self.assertEqual(scale.boundary_layer_limit(5, 0)["rho_limit"], Fraction(1, 10))
        self.assertEqual(scale.boundary_layer_limit(5, Fraction(1, 2))["rho_limit"], 0)

    def test_hardy_band_rational_bounds(self):
        for denominator in (16, 256, 4096):
            self.assertEqual(
                scale.hardy_band_bound(Fraction(1, denominator)),
                Fraction(2, denominator - 1),
            )
        self.assertEqual(scale.hardy_band_bound(Fraction(1, 2)), 1)

    def test_invalid_order_and_exact_types(self):
        for order in (0, 2, 17, True, 3.0):
            with self.assertRaises(ValueError):
                scale.polynomials(order)
        for value in (True, 0.5, "1/2", 1j):
            with self.assertRaises(TypeError):
                scale.gaussian_data(5, value)

    def test_zero_negative_and_degenerate_inputs(self):
        for nu in (0, -1):
            with self.assertRaises(ValueError):
                scale.gaussian_data(5, nu)
        with self.assertRaises(ValueError):
            scale.gaussian_data(5, 1, 0)
        for eta in (0, -1):
            with self.assertRaises(ValueError):
                scale.phase(2, 1, eta)
        with self.assertRaises(ValueError):
            scale.phase_window(2, 1, -1)
        with self.assertRaises(ValueError):
            scale.variance_window_bound(5, 1, 1, 1)
        for epsilon in (0, -1, 1, 2):
            with self.assertRaises(ValueError):
                scale.hardy_band_bound(epsilon)

    def test_resource_caps(self):
        with self.assertRaises(ValueError):
            scale.gaussian_data(5, Fraction(1, 1 << scale.MAX_SOURCE_BITS))
        with self.assertRaises(ValueError):
            scale.phase(1 << scale.MAX_SCALAR_BITS, 1, 1)

    def test_frozen_fixture(self):
        scale.validate_report(json.loads(scale.FIXTURE.read_text(encoding="utf-8")))

    def test_scope_is_not_pick_congruence_or_zero_count(self):
        scope = self.report["scope"]
        for key in (
            "source_Pick_congruence_proved",
            "physical_outer_normalization_transferred",
            "confluent_or_collective_Hardy_localization_proved",
            "free_energy_or_zero_count_bound_proved",
            "ninety_percent_density_one_or_RH_proved",
            "novelty_claim",
        ):
            self.assertIs(scope[key], False)
        self.assertFalse(
            self.report["source_authentication"][
                "Xi_concentration_independently_reproved"
            ]
        )

    def test_typed_fixture_mutations_rejected(self):
        changed = copy.deepcopy(self.report)
        changed["scope"]["source_Pick_congruence_proved"] = 0
        with self.assertRaises(ValueError):
            scale.validate_report(changed)
        changed = copy.deepcopy(self.report)
        changed["gaussian_controls"][0]["p"] = "0"
        with self.assertRaises(ValueError):
            scale.validate_report(changed)

    def test_source_contract_and_line_endings(self):
        expected = scale.expected_manifest()
        with TemporaryDirectory() as directory:
            path = Path(directory) / "sources.json"
            with mock.patch.object(scale, "MANIFEST", path):
                path.write_bytes((json.dumps(expected, indent=2) + "\n").encode())
                lf = scale.authenticate_sources()
                path.write_bytes(
                    (json.dumps(expected, indent=2) + "\n")
                    .replace("\n", "\r\n")
                    .encode()
                )
                self.assertEqual(lf, scale.authenticate_sources())
                expected["concentration_status"] = "proved here"
                path.write_text(json.dumps(expected), encoding="utf-8")
                with self.assertRaises(ValueError):
                    scale.authenticate_sources()

    def test_packet_hashes(self):
        hashes = self.report["artifact_sha256_lf"]
        for path in (scale.NOTE, SCRIPT, Path(__file__), scale.MANIFEST):
            self.assertEqual(
                hashes[path.relative_to(ROOT).as_posix()],
                scale.sha256_lf(path.read_bytes()),
            )

    def test_frozen_source_identity_tampering(self):
        with (
            mock.patch.object(
                scale.subprocess,
                "check_output",
                side_effect=[b"wrong blob\n", b"wrong content"],
            ),
            self.assertRaises(ValueError),
        ):
            scale.authenticate_sources()
        with (
            mock.patch.object(
                scale.subprocess,
                "check_output",
                side_effect=[
                    scale.SOURCE_ROWS[0][2].encode() + b"\n",
                    b"wrong content",
                ],
            ),
            self.assertRaises(ValueError),
        ):
            scale.authenticate_sources()


if __name__ == "__main__":
    unittest.main()
