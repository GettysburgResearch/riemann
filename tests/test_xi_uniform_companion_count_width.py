"""Exact bounded controls only; these tests do not certify the analytic proof."""

from __future__ import annotations

import importlib.util
import json
import unittest
from copy import deepcopy
from fractions import Fraction
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "xi_count", ROOT / "research/exploratory/xi_uniform_companion_count_width.py"
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("missing producer")
m = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(m)


class XiCountTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = m.build_report()

    def test_01_complete_fixture(self):
        self.assertEqual(m.check_fixture(), self.report)

    def test_02_complete_counts(self):
        self.assertEqual(
            self.report["counts"],
            {
                "growth": 21,
                "geometry": 8,
                "anchors": 8,
                "phases": 14,
                "scales": 4,
                "widths": 9,
                "squared_width": 4,
                "cauchy": 3,
                "cosine": 3,
            },
        )
        self.assertEqual(len(self.report["source_bindings"]), 10)

    def test_03_native_anchor_signs(self):
        self.assertEqual(m.anchor_control(0, 1, 1)["base_phase"], [1, 0])
        self.assertEqual(m.anchor_control(0, 1, 1)["lambda_phase"], [1, 0])
        self.assertEqual(m.anchor_control(5, -1, -1)["base_phase"], [0, 1])
        self.assertEqual(m.anchor_control(5, -1, -1)["lambda_phase"], [0, 1])

    def test_04_wrong_anchor_negative_controls(self):
        for args in ((0, -1, 1), (0, 1, -1), (5, 1, -1), (5, -1, 1)):
            self.assertFalse(m.anchor_control(*args)["noncancelling"])

    def test_05_derivative_phase_direct_exponentials(self):
        for r in range(7):
            for side in (-1, 1):
                # i^r times the parity sign after pairing exp(-side*u).
                raw = (1, 0)
                for _ in range(r):
                    raw = (-raw[1], raw[0])
                if r % 2:
                    raw = (-side * raw[0], -side * raw[1])
                self.assertEqual(m.derivative_phase(r, side), raw)

    def test_06_gamma_parameters_and_prefactor(self):
        self.assertEqual(m.growth_control(1, 6)["gamma_parameter"], [13, 4])
        self.assertEqual(m.growth_control(1, 6)["coefficient_of_pi_squared"], 4320)
        self.assertEqual(m.growth_control(4, 0)["gamma_parameter"], [19, 4])

    def test_07_taylor_coefficient_witnesses(self):
        for r in range(7):
            row = m.growth_control(2, r)
            self.assertEqual(
                Fraction(*row["exp_series_coefficient"]) * row["factorial"], 1
            )

    def test_08_jensen_geometry_held_out(self):
        for radius in (Fraction(3, 2), 7, 1024):
            for side in (-1, 1):
                row = m.jensen_geometry(radius, side)
                self.assertEqual(Fraction(*row["outer_radius"]), 2 * (radius + 1))
                self.assertEqual(
                    Fraction(*row["origin_envelope_radius"]), 2 * radius + 3
                )
                self.assertEqual(
                    Fraction(*row["outer_gamma_parameter"]), radius + Fraction(17, 4)
                )

    def test_09_closed_radius_condition(self):
        for radius in (0, Fraction(1, 2), -1):
            with self.assertRaises(ValueError):
                m.jensen_geometry(radius, 1)

    def test_10_exact_fixed_scale(self):
        for omega in (1, Fraction(13, 7), 32767):
            row = m.scale_control(omega)
            self.assertEqual(Fraction(*row["lambda"]) * Fraction(*row["X"]), 2)

    def test_11_width_pi_cancellation_held_out(self):
        for k in (3, 7, 29):
            row = m.width_constant(k, Fraction(3, 2), 100, 5, Fraction(355, 113))
            self.assertEqual(row["before"], row["after"])
            self.assertEqual(Fraction(*row["after"]), Fraction(3 * k, 500))

    def test_12_squared_width_exact(self):
        row = m.squared_width_control(
            [(1, Fraction(1, 200)), (4, Fraction(1, 100))],
            Fraction(1, 1024),
            8,
            Fraction(1, 100),
        )
        self.assertEqual(row["rank_total"], 5)
        self.assertEqual(row["height_total"], [3, 200])
        self.assertEqual(
            Fraction(*row["coarse_normalized_square"]), Fraction(3, 163840)
        )
        self.assertGreater(Fraction(*row["gap"]), 0)

    def test_13_empty_zero_width(self):
        self.assertEqual(
            m.squared_width_control([], 0, 1, 1)["coarse_normalized_square"], [0, 1]
        )
        self.assertEqual(m.squared_width_control([(0, 0)], 1, 1, 1)["rank_total"], 0)
        self.assertEqual(m.squared_width_control([(1, 1)], 0, 1, 1)["gap"], [0, 1])

    def test_14_cauchy_equality_and_strictness(self):
        self.assertEqual(m.cauchy_control([1, 2], [3, 6])["gap"], [0, 1])
        self.assertEqual(m.cauchy_control([1, 0], [0, 1])["gap"], [1, 1])
        self.assertEqual(m.cauchy_control([], [])["gap"], [0, 1])

    def test_15_cosine_exact_upper_height(self):
        row = m.cosine_control(Fraction(1, 200))
        self.assertEqual(row["upper_q_squared"], [199, 201])
        self.assertEqual(row["height_upper_bound"], [200, 39999])
        self.assertLess(Fraction(*row["height_upper_bound"]), Fraction(1, 100))

    def test_16_cosine_independent_laurent_product(self):
        for lam in (Fraction(1, 201), Fraction(3, 5), Fraction(1, 7)):
            # Derive the two factors from exponentials, independent of the producer formula.
            cos = {-1: Fraction(1, 2), 1: Fraction(1, 2)}
            sin_over_i = {-1: Fraction(1, 2), 1: Fraction(-1, 2)}
            h0 = {j: cos[j] + lam * sin_over_i[j] for j in (-1, 1)}
            h5_over_i = {j: -sin_over_i[j] + lam * cos[j] for j in (-1, 1)}
            product = {}
            for a, x in h0.items():
                for b, y in h5_over_i.items():
                    product[a + b] = product.get(a + b, Fraction()) + x * y
            expected = [
                Fraction(*x)
                for x in m.cosine_control(lam)["D_over_i_laurent_minus2_0_2"]
            ]
            self.assertEqual([product[j] for j in (-2, 0, 2)], expected)
        row = m.cosine_control(Fraction(1, 201))
        self.assertEqual(row["upper_q_squared"], [100, 101])

    def test_17_scalar_type_firewall(self):
        for bad in (True, False, 1.0, "1", None, complex(1)):
            with self.assertRaises(ValueError):
                m.rational(bad)
            with self.assertRaises(ValueError):
                m.integer(bad, 0, 6)

    def test_18_rational_bits(self):
        for bad in (2**16, Fraction(1, 2**16), -(2**16)):
            with self.assertRaises(ValueError):
                m.rational(bad)
        self.assertEqual(m.rational(65535), 65535)
        with self.assertRaises(ValueError):
            m.rational(2**256, internal=True)

    def test_19_orders_signs_and_sides(self):
        for args in ((7, 1), (-1, 1), (2, 0), (2, 2), (True, 1)):
            with self.assertRaises(ValueError):
                m.derivative_phase(*args)
        for args in ((6, 1, 1), (0, 0, 1), (0, True, 1)):
            with self.assertRaises(ValueError):
                m.anchor_control(*args)

    def test_20_width_and_scale_domain(self):
        for k in (0, 2, 32, True):
            with self.assertRaises(ValueError):
                m.width_constant(k, 1, 100, 3, 3)
        for omega in (0, Fraction(1, 2), -1):
            with self.assertRaises(ValueError):
                m.scale_control(omega)
        for lam in (0, 1, -1):
            with self.assertRaises(ValueError):
                m.cosine_control(lam)

    def test_21_window_shape_and_count_caps(self):
        for bad in (
            None,
            {},
            [(1, 0)] * 9,
            [(1,)],
            [(1, 0, 0)],
            [(1025, 0)],
            [(True, 0)],
        ):
            with self.assertRaises(ValueError):
                m.squared_width_control(bad, 1, 1, 1)

    def test_22_shallow_and_normalizer_conditions(self):
        for windows in ([(0, 1)], [(1, -1)], [(1, 2)]):
            with self.assertRaises(ValueError):
                m.squared_width_control(windows, 1, 1, 1)
        for width, norm, eta in ((-1, 1, 1), (1, 0, 1), (1, 1, 0)):
            with self.assertRaises(ValueError):
                m.squared_width_control([], width, norm, eta)

    def test_23_vector_caps(self):
        for left, right in (([1], []), ([1] * 9, [1] * 9), (None, []), ([True], [1])):
            with self.assertRaises(ValueError):
                m.cauchy_control(left, right)

    def test_24_json_duplicates_nonfinite_and_float(self):
        for raw in (
            b'{"x":1,"x":2}',
            b'{"x":NaN}',
            b'{"x":Infinity}',
            b'{"x":1.0}',
            b"[] trailing",
        ):
            with self.assertRaises(ValueError):
                m.parse_json(raw)

    def test_25_json_size_depth_type_caps(self):
        for raw in (b" " * (m.MAX_JSON_BYTES + 1), b"[" * 20 + b"0" + b"]" * 20):
            with self.assertRaises(ValueError):
                m.parse_json(raw)
        for value in ({"x": 2**256}, {"x": "a" * 2049}, {"x": Fraction(1, 2)}):
            with self.assertRaises(ValueError):
                m.canonical(value)

    def test_26_manifest_metadata_tamper(self):
        manifest = json.loads(m.MANIFEST.read_text())
        manifest["sources"][0]["role"] = "unbound replacement"
        with self.assertRaises(ValueError):
            m.authenticate_sources(json.dumps(manifest).encode())

    def test_27_source_git_blob_tamper(self):
        with (
            patch.object(
                m.subprocess, "run", return_value=SimpleNamespace(stdout=b"wrong\n")
            ),
            self.assertRaisesRegex(ValueError, "Git blob"),
        ):
            m.authenticate_sources()

    def test_28_source_lf_hash_tamper(self):
        manifest = json.loads(m.MANIFEST.read_text())
        manifest["sources"][0]["sha256_lf"] = "0" * 64
        raw = json.dumps(manifest).encode()
        with (
            patch.object(m, "MANIFEST_SHA", m.digest(raw)),
            self.assertRaisesRegex(ValueError, "source LF hash"),
        ):
            m.authenticate_sources(raw)

    def test_29_complete_fixture_rejects_missing_extra_and_changed(self):
        mutations = []
        missing = deepcopy(self.report)
        del missing["geometry"]
        mutations.append(missing)
        extra = deepcopy(self.report)
        extra["unrequested"] = 1
        mutations.append(extra)
        changed = deepcopy(self.report)
        changed["counts"]["growth"] = True
        mutations.append(changed)
        changed_hash = deepcopy(self.report)
        changed_hash["artifacts_sha256_lf"][m.ARTIFACTS[0]] = "0" * 64
        mutations.append(changed_hash)
        with patch.object(m, "build_report", return_value=self.report):
            for obj in mutations:
                with self.assertRaises(ValueError):
                    m.check_fixture(json.dumps(obj).encode())

    def test_30_lf_and_bounded_file_semantics(self):
        self.assertEqual(m.lf_bytes(b"a\r\nb\r\n"), b"a\nb\n")
        with self.assertRaises(ValueError):
            m.lf_bytes(b"x" * (m.MAX_FILE_BYTES + 1))
        with self.assertRaises(ValueError):
            m.lf_bytes("not bytes")

    def test_31_no_kernel_coefficient_convention_relabel(self):
        roles = {row["role"] for row in self.report["source_bindings"]}
        self.assertIn("all_inner_finite_denominator_width_and_adjoint_source", roles)
        self.assertIn("accepted_band_CB18_CB20_only_not_historical_raw_values", roles)
        paths = {row["path"] for row in self.report["source_bindings"]}
        self.assertIn(
            "claims/lemmas/L-106610-riemann-siegel-gauge-factorization.md", paths
        )
        self.assertNotIn(
            "claims/lemmas/L-106610-fifth-residue-sign-transition-reverse-rolle.md",
            paths,
        )

    def test_32_all_result_checks_survive_optimization(self):
        with self.assertRaises(ValueError):
            m.require(False, "still checked")
        with patch.object(m, "build_report", return_value=self.report):
            raw = json.dumps(self.report).encode()
            self.assertEqual(m.check_fixture(raw), self.report)


if __name__ == "__main__":
    unittest.main()
