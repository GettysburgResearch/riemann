"""Strict finite source/frequency tests; analytic conclusions have a written proof."""

import copy
import importlib.util
import json
import sys
import unittest
from fractions import Fraction as F
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
PATH = (
    ROOT
    / "research/l-families/atlas/generalized/rankin_selberg_quotient_global_parent.py"
)
SPEC = importlib.util.spec_from_file_location("rankin_quotient_tested", PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("producer import unavailable")
m = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = m
SPEC.loader.exec_module(m)


class RankinQuotientTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = m.build_report()
        cls.source = m.qsource()

    def test_complete_fixture(self):
        m.validate_report(m.read_json(m.FIXTURE))

    def test_source_q_coefficients(self):
        a, b, c = self.source
        self.assertEqual((a[6], b[6], c[6]), (-882400608, 143820, -982499328))
        self.assertEqual((a[3], b[3], c[3]), (162252, -48, 195660))

    def test_source_prefix_independent_orders(self):
        for order in (6, 8, 12, 18):
            small = m.qsource(order)
            self.assertEqual(small, tuple(row[: order + 1] for row in self.source))

    def test_Hecke_matrix_and_polynomial(self):
        row = m.hecke_control(self.source[0], self.source[1], m.Budget())
        self.assertEqual(row["T2"], ((696, 1), (20736000, 384)))
        self.assertEqual(row["defect_coefficients"], (-995328000, 14976, 48))
        self.assertEqual(row["coefficient_checks"], 24)

    def test_first_fractional_frequency(self):
        row = m.frequency_control(F(9, 2))
        self.assertEqual(row["first_noninteger_frequency"], F(9, 2))
        self.assertEqual(row["bare_F"][F(9, 2)], -88203653222400)

    def test_zeta_does_not_cancel(self):
        row = m.frequency_control(6)
        self.assertEqual(row["L_Q_zeta_times_F"][F(9, 2)], row["bare_F"][F(9, 2)])
        self.assertEqual(row["L_Q_zeta_times_F"][F(4)] - row["bare_F"][F(4)], 2**46)

    def test_degree_one_coefficient_is_absent(self):
        row = m.frequency_control(6)
        self.assertNotIn(F(2), row["bare_F"])
        self.assertEqual(row["bare_F"][F(1)], 1)

    def test_convolution_prefix_consistency(self):
        large = m.frequency_control(12)
        for cutoff in (F(9, 2), F(11, 2), F(27, 4), F(10)):
            small = m.frequency_control(cutoff)
            for key in ("bare_F", "L_Q_zeta_times_F"):
                self.assertEqual(
                    small[key], {f: v for f, v in large[key].items() if f <= cutoff}
                )

    def test_second_fractional_word(self):
        row = m.frequency_control(F(27, 4))
        self.assertEqual(row["bare_F"][F(27, 4)], 203221217024409600)

    def test_geometric_depth_exact(self):
        self.assertEqual([m.depth_bound(c) for c in (F(9, 2), 6, 10, 12)], [0, 0, 1, 2])
        for cutoff in (F(9, 2), 6, 10, 12):
            self.assertGreater(F(9, 2) * F(3, 2) ** (m.depth_bound(cutoff) + 1), cutoff)

    def test_Gram_shear_and_scale(self):
        first = m.gram_control((1, 2, 3), 0, 1, self.source, m.Budget())
        held = m.gram_control((1, 2, 3), F(-11, 3), F(7, 5), self.source, m.Budget())
        self.assertEqual(first["quotient"], held["quotient"])
        self.assertGreater(first["quotient"], 0)

    def test_two_frequency_quotient(self):
        row = m.gram_control((F(2, 3), F(7, 5)), -696, -2, self.source, m.Budget())
        self.assertEqual(row["quotient"], F(2, 3))

    def test_pole_residue_sign_control(self):
        row = m.gram_control((1, 1, 1, 1), 2, 3, self.source, m.Budget())
        r1, r0 = row["formal_endpoint_residues"]
        self.assertEqual(r1, -r0)
        self.assertGreater(r1, 0)

    def test_three_direction_obstruction(self):
        self.assertEqual(self.report["first_three_direction_minors"], [1, -48, -195660])

    def test_q_order_types_caps(self):
        for value in (True, 6.0, "6", 5, 25, -1):
            with self.subTest(value=value), self.assertRaises(ValueError):
                m.qsource(value)

    def test_cutoff_types_caps(self):
        for value in (True, 4.5, "6", 4, 13, -1):
            with self.subTest(value=value), self.assertRaises(ValueError):
                m.frequency_control(value)

    def test_q_cap_before_allocation(self):
        with (
            mock.patch.object(m, "qmul", side_effect=RuntimeError("allocated")),
            self.assertRaises(ValueError),
        ):
            m.qsource(25)

    def test_cutoff_cap_before_source(self):
        with (
            mock.patch.object(m, "qsource", side_effect=RuntimeError("allocated")),
            self.assertRaises(ValueError),
        ):
            m.frequency_control(13)

    def test_work_cap_before_convolution(self):
        work = m.Budget(1)
        with self.assertRaises(ValueError):
            m.series_mul({F(1): 1, F(2): 2}, {F(1): 1, F(2): 2}, 4, work)
        self.assertEqual(work.used, 0)

    def test_rational_bit_cap(self):
        for value in (2**m.INPUT_BITS, F(1, 2**m.INPUT_BITS)):
            with self.assertRaises(ValueError):
                m.exact(value)
        with self.assertRaises(ValueError):
            m.exact(2**m.INTERNAL_BITS, internal=True)

    def test_bool_not_rational(self):
        with self.assertRaises(ValueError):
            m.exact(True)
        with self.assertRaises(ValueError):
            m.exact(1, internal=1)

    def test_series_types_support(self):
        for value in ([], "series", {F(1, 2): 1}, {1: True}):
            with self.subTest(value=value), self.assertRaises(ValueError):
                m.series(value)
        with self.assertRaises(ValueError):
            m.series({F(n): 1 for n in range(1, m.MAX_TERMS + 2)})

    def test_polynomial_shapes_types(self):
        for value in ("poly", [True], [F(1)], [0] * 26):
            with self.subTest(value=value), self.assertRaises(ValueError):
                m.polynomial(value)

    def test_Gram_degeneracy_rejected(self):
        for weights, shear, scale in (((1,), 0, 1), ((1, 0), 0, 1), ((1, 1), 0, 0)):
            with self.assertRaises(ValueError):
                m.gram_control(weights, shear, scale, self.source, m.Budget())

    def test_short_or_mismatched_source_rejected(self):
        for source in (self.source[:2], tuple(row[:12] for row in self.source)):
            with self.assertRaises(ValueError):
                m.frequency_control(6, source)
        bad = [list(row) for row in self.source]
        bad[2][3] += 1
        with self.assertRaises(ValueError):
            m.frequency_control(6, bad)

    def test_manifest_missing_extra_type(self):
        for kind in ("missing", "extra", "type", "primitive"):
            manifest = copy.deepcopy(m.expected_manifest())
            if kind == "missing":
                manifest["context_sources"] = []
            elif kind == "extra":
                manifest["extra"] = True
            elif kind == "type":
                manifest["external_contracts"][0]["remote_bytes_authenticated"] = 0
            else:
                manifest["primitive_definitions"]["f1"] = "Delta"
            with self.subTest(kind=kind), self.assertRaises(ValueError):
                m.authenticate_sources(manifest)

    def test_source_blob_drift(self):
        with (
            mock.patch.object(m.subprocess, "check_output", return_value=b"wrong"),
            self.assertRaises(ValueError),
        ):
            m.authenticate_sources(m.expected_manifest())

    def test_fixture_missing_extra_type_coefficient(self):
        for kind in ("missing", "extra", "type", "coefficient"):
            value = copy.deepcopy(self.report)
            if kind == "missing":
                value["frequency_controls"].pop()
            elif kind == "extra":
                value["extra"] = "invented"
            elif kind == "type":
                value["scope"]["new_automorphic_representation"] = 0
            else:
                value["frequency_controls"][0]["bare_F"]["9/2"] = "0"
            with self.subTest(kind=kind), self.assertRaises(ValueError):
                m.validate_report(value)

    def test_JSON_duplicates_nonfinite(self):
        for raw in ('{"a":1,"a":2}', '{"a":NaN}', '{"a":Infinity}'):
            with (
                mock.patch.object(Path, "read_text", return_value=raw),
                self.assertRaises(ValueError),
            ):
                m.read_json(Path("unused"))

    def test_scope_and_work(self):
        scope = self.report["scope"]
        self.assertFalse(scope["analytic_proof_machine_verified"])
        self.assertFalse(scope["generalized_prime_systems_excluded"])
        self.assertFalse(scope["RH_GRH_or_novelty_claim"])
        self.assertLessEqual(self.report["coverage"]["work_units"], m.MAX_WORK)
        self.assertEqual(json.loads(m.canonical(self.report)), self.report)


if __name__ == "__main__":
    unittest.main()
