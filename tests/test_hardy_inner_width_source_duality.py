"""Exact hostile controls; analytic all-inner/HY theorem is not machine proved."""

import copy
import importlib.util
import json
import sys
import unittest
from fractions import Fraction as F
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "research/exploratory/hardy_inner_width_source_duality.py"
SPEC = importlib.util.spec_from_file_location("hardy_inner_width_under_test", SOURCE)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("test producer import unavailable")
m = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = m
SPEC.loader.exec_module(m)


class WidthDualityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = m.build_report()

    def test_fixture_complete_replay(self):
        m.validate_report(m.h.read_json(m.FIXTURE))

    def test_exact_orientation_falsifier(self):
        row = m.orientation_falsifier()
        self.assertEqual(row["wrong_deficit_determinant"], m.h.gaussian(F(-64, 14625)))
        self.assertEqual(row["wrong_charge"], m.h.gaussian(F(1943, 585)))
        self.assertEqual(row["correct_charge"], m.h.gaussian(F(235, 117)))
        self.assertGreater(row["wrong_charge"].r, 3)

    def test_confluent_HT4_phase_and_adjoint(self):
        row = m.duality_control(((1, 0), (1, 0)), ((2, 0),))
        self.assertEqual(
            row["HT4_G"], m.h.matrix(((F(1, 2), F(1, 4)), (F(1, 4), F(1, 4))))
        )
        self.assertEqual(
            row["HT4_A"], m.h.matrix(((F(-1, 3), F(-4, 9)), (0, F(-1, 3))))
        )
        self.assertEqual(row["physical_deficit"]["rank"], 1)

    def test_zero_charge_is_not_divided(self):
        row = m.duality_control(((1, 0),), ((1, 0),))
        self.assertEqual(row["correct_physical_charge"], m.Z)
        self.assertEqual(row["literal_and_reduced_band_surrogate"], m.Z)

    def test_constant_inner_charge_is_rank(self):
        row = m.duality_control(((1, 0), (F(3, 2), -2)), ())
        self.assertEqual(row["correct_physical_charge"], m.h.gaussian(2))
        self.assertEqual(row["physical_deficit"]["rank"], 0)

    def test_heldout_complex_confluent_source(self):
        row = m.duality_control(
            ((F(2, 3), 2), (F(2, 3), 2), (F(3, 4), -1)), ((F(4, 3), -2),)
        )
        self.assertLessEqual(row["correct_physical_charge"].r, 3)
        self.assertTrue(all(row["C_A_noncommutation_with_G"]))
        self.assertNotEqual(
            row["literal_and_reduced_band_surrogate"],
            row["incorrect_outer_metric_dropped"],
        )

    def test_fourfold_collision_MT(self):
        row = m.mt_control(((F(2, 3), -3),) * 4)
        self.assertEqual(row["unnormalized_squared_norms"], (F(3, 4),) * 4)
        self.assertEqual(row["rational_columns_checked"], 4)

    def test_MT_order_permutations(self):
        a = ((F(1, 2), -2), (1, 1), (F(1, 2), -2))
        self.assertEqual(m.mt_control(a)["dimension"], 3)
        self.assertEqual(m.mt_control(tuple(reversed(a)))["dimension"], 3)

    def test_unequal_heights_Cauchy_Schwarz(self):
        row = m.square_height_bound((F(1, 2), F(1, 3), F(1, 4)), F(1, 100))
        self.assertGreater(row["Cauchy_Schwarz_gap"], 0)

    def test_equal_heights_cap_equality(self):
        row = m.square_height_bound((F(2, 3),) * 4, 1)
        self.assertEqual(row["Cauchy_Schwarz_gap"], 0)

    def test_zero_measure_bound(self):
        row = m.square_height_bound((F(1), F(2)), 0)
        self.assertEqual(row["coarse_beta_squared_with_constant_4"], 0)

    def test_width_types_domain(self):
        for delta in (True, 0.1, -1, "1/2", complex(1, 0)):
            with self.subTest(delta=delta), self.assertRaises((TypeError, ValueError)):
                m.square_height_bound((F(1),), delta)

    def test_height_types_domain(self):
        for height in (True, 0.5, 0, -1, "1", complex(1, 0)):
            with (
                self.subTest(height=height),
                self.assertRaises((TypeError, ValueError)),
            ):
                m.mt_control(((height, 0),))

    def test_phase_types(self):
        for phase in (True, 1.0, "0", 1j):
            with self.subTest(phase=phase), self.assertRaises((TypeError, ValueError)):
                m.mt_control(((1, phase),))

    def test_bit_caps(self):
        for value in (2**m.h.INPUT_BITS, F(1, 2**m.h.INPUT_BITS)):
            with self.assertRaises(ValueError):
                m.mt_control(((value, 0),))
            with self.assertRaises(ValueError):
                m.rational_poly((value,))

    def test_degree_cap_before_expansion(self):
        with (
            mock.patch.object(
                m.h, "multiply_inner", side_effect=RuntimeError("allocated")
            ),
            self.assertRaises(ValueError),
        ):
            m.mt_control(((1, 0),) * 5)
        with (
            mock.patch.object(
                m, "derivative_gram", side_effect=RuntimeError("allocated")
            ),
            self.assertRaises(ValueError),
        ):
            m.duality_control(((1, 0),), ((2, 0),) * 3)

    def test_matrix_cap_before_helper_allocation(self):
        with mock.patch.object(m.h, "matrix", side_effect=RuntimeError("allocated")):
            with self.assertRaises(ValueError):
                m.determinant(((1,) * 5,) * 5)
            with self.assertRaises(ValueError):
                m.psd_control(((1,) * 5,) * 5)

    def test_polynomial_product_cap_before_helper(self):
        with (
            mock.patch.object(m.h, "pm", side_effect=RuntimeError("allocated")),
            self.assertRaises(ValueError),
        ):
            m.product((1,) * 6, (1,) * 6)

    def test_rational_jet_rejects_pole(self):
        with self.assertRaises(ValueError):
            m.rational_jet((1,), (-m.IU, 1), m.IU, 2)

    def test_negative_principal_minor_rejected(self):
        with self.assertRaises(ValueError):
            m.psd_control(((1, 2), (2, 1)))

    def test_nonnumeric_or_ragged_matrices(self):
        for matrix in (((1, 0), (1,)), ((True,),), "matrix"):
            with (
                self.subTest(matrix=matrix),
                self.assertRaises((TypeError, ValueError)),
            ):
                m.determinant(matrix)

    def test_manifest_missing_changed_extra_types(self):
        for mode in ("missing", "extra", "commit", "type"):
            manifest = copy.deepcopy(m.expected_manifest())
            if mode == "missing":
                manifest["sources"].pop()
            elif mode == "extra":
                manifest["invented"] = True
            elif mode == "commit":
                manifest["sources"][0]["commit"] = "0" * 40
            else:
                manifest["external_contracts"][0]["remote_bytes_authenticated"] = 0
            with self.subTest(mode=mode), self.assertRaises(ValueError):
                m.authenticate_sources(manifest)

    def test_git_blob_mismatch_rejected(self):
        with (
            mock.patch.object(m.subprocess, "check_output", return_value=b"wrong"),
            self.assertRaises(ValueError),
        ):
            m.authenticate_sources(m.expected_manifest())

    def test_resident_helper_mismatch_before_import(self):
        with (
            mock.patch.object(m, "lf_sha", return_value="wrong"),
            self.assertRaises(ValueError),
        ):
            m.load_helper()

    def test_report_extra_missing_wrong_type(self):
        for mode in ("extra", "missing", "type"):
            report = copy.deepcopy(self.report)
            if mode == "extra":
                report["invented"] = True
            elif mode == "missing":
                report["MT_controls"].pop()
            else:
                report["scope"]["numerical_Xi_samples"] = False
            with self.subTest(mode=mode), self.assertRaises(ValueError):
                m.validate_report(report)

    def test_changed_derived_control_rejected(self):
        report = copy.deepcopy(self.report)
        report["orientation_falsifier"]["wrong_charge"]["re"] = "3"
        with self.assertRaises(ValueError):
            m.validate_report(report)

    def test_duplicate_nonfinite_json_rejected(self):
        with (
            mock.patch.object(Path, "read_text", return_value='{"x":1,"x":2}'),
            self.assertRaises(ValueError),
        ):
            m.h.read_json(Path("unused"))
        for text in ('{"x":NaN}', '{"x":Infinity}'):
            with (
                mock.patch.object(Path, "read_text", return_value=text),
                self.assertRaises(ValueError),
            ):
                m.h.read_json(Path("unused"))

    def test_helper_intermediate_cap(self):
        with self.assertRaises(ValueError):
            m.Q(F(2**m.h.INTERMEDIATE_BITS), F(0))

    def test_coverage_and_firewalls(self):
        self.assertEqual(
            self.report["coverage"],
            {
                "MT_cases": 6,
                "MT_columns": 17,
                "dual_source_cases": 6,
                "bound_rows": 12,
                "unbounded_search": False,
            },
        )
        for name in (
            "height_sum_used_as_count",
            "total_charge_bound",
            "free_energy_or_descent_closure",
            "RH_or_percentage",
        ):
            self.assertFalse(self.report["scope"][name])
        self.assertEqual(len(self.report["artifact_sha256_lf"]), 4)

    def test_json_roundtrip_canonical(self):
        self.assertEqual(
            m.h.canonical(self.report),
            m.h.canonical(json.loads(json.dumps(self.report))),
        )


if __name__ == "__main__":
    unittest.main()
