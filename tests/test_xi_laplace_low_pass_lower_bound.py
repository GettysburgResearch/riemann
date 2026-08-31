"""Independent elementary band controls and primitive Xi replay contracts."""

import copy
import sys
import unittest
from fractions import Fraction as Q
from pathlib import Path
from unittest import mock

from flint import acb, arb

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "research/exploratory"))
import xi_laplace_low_pass_lower_bound as M

OA = M.oa


class XiLaplaceBandTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = M.build_report()

    def test_01_sources_and_runtime(self):
        M.authenticate()
        self.assertEqual(len(M.BINDINGS), 6)

    def test_02_complete_preregistered_grid(self):
        self.assertEqual(M.WIDTHS, (Q(1, 4), Q(1, 16), Q(1, 64), Q(1, 256)))
        self.assertEqual(M.HEIGHTS, tuple(2**j for j in range(6, 17)))
        count = 0
        for op in self.report["operators"]:
            self.assertEqual(len(op["calibrations"]), 11)
            for band in op["bands"]:
                self.assertEqual(len(band["all_node_height_bounds"]), len(op["roots"]))
                for node in band["all_node_height_bounds"]:
                    self.assertEqual([v["h"] for v in node], list(M.HEIGHTS))
                    count += len(node)
        self.assertEqual(count, 616)

    def test_03_fresh_source_rebuild(self):
        self.assertEqual(
            M.bc.canonical(self.report),
            M.bc.canonical(M.bc.load_json(M.FIXTURE.read_bytes())),
        )

    def test_04_axis_direct_product_all_calibrations(self):
        with OA.precision():
            for anchor in (32, 64, 128):
                lam = OA.frozen_lambda(anchor)
                for h in M.HEIGHTS:
                    value, ell = M.axis_value(h, lam, direct=True)
                    self.assertTrue(value.is_finite())
                    self.assertTrue(ell > 0)
                    self.assertTrue(abs(value) < 1)

    def test_05_all_final_cells_positive(self):
        for op in self.report["operators"]:
            for band in op["bands"]:
                self.assertTrue(band["all_nodes_positive"])
                self.assertGreater(
                    OA.unpair(band["strict_global_input_band_norm_floor"]), 0
                )
                self.assertGreater(
                    OA.unpair(band["strict_global_input_band_squared_HS_floor"]), 0
                )

    def test_06_trace_metric_reconstruction(self):
        for op in self.report["operators"]:
            c = OA.unpair(op["normalized_gram_upper"])
            self.assertEqual(c, max(map(OA.unpair, op["normalized_gram_row_bounds"])))
            for band in op["bands"]:
                best = [
                    max(OA.unpair(v["norm_lower"]) for v in node)
                    for node in band["all_node_height_bounds"]
                ]
                self.assertEqual(
                    best, list(map(OA.unpair, band["best_node_norm_lower"]))
                )
                self.assertLess(
                    OA.unpair(band["strict_global_input_band_squared_HS_floor"]),
                    sum(x * x for x in best) / c,
                )
                self.assertLess(
                    OA.unpair(band["strict_global_input_band_norm_floor"]), max(best)
                )

    def test_07_failed_grid_values_are_retained(self):
        zeros = 0
        for op in self.report["operators"]:
            for band in op["bands"]:
                for node in band["all_node_height_bounds"]:
                    zeros += sum(OA.unpair(v["norm_lower"]) == 0 for v in node)
        self.assertGreater(zeros, 0)

    def test_08_exact_blaschke_band_integral(self):
        # U(z)=(z-i)/(z+i), b=2i. Ue_b has time signal
        # 2(3e^-2t-2e^-t); the physical projection adds U(b)=1/3.
        with OA.precision():
            node = acb(0, 2)
            raw = acb(OA.qarb(Q(1, 3)))
            for width in (Q(1, 8), Q(1, 4), Q(1, 2), Q(1)):
                w = OA.qarb(width)
                true_squared = (
                    9 * (1 - (-4 * w).exp())
                    - 16 * (1 - (-3 * w).exp())
                    + 8 * (1 - (-2 * w).exp())
                ) / 9
                self.assertTrue(true_squared > 0)
                for h in (2, 4, 8, 16):
                    axis = OA.qarb(Q(h - 1, h + 1))
                    floor = OA.unpair(
                        M.lower_bound(node, raw, h, width, axis)["norm_lower"]
                    )
                    self.assertTrue(OA.qarb(floor * floor) < true_squared)

    def test_09_delay_obstruction_not_overruled(self):
        with OA.precision():
            tau = arb(1)
            node = acb(0, 2)
            raw = acb((-2 * tau).exp())
            for h in (2, 4, 8, 16):
                for width in (Q(1, 8), Q(1, 2)):
                    row = M.lower_bound(node, raw, h, width, (-tau * h).exp())
                    self.assertEqual(OA.unpair(row["norm_lower"]), 0)

    def test_10_zero_physical_scalar_stays_zero(self):
        with OA.precision():
            row = M.lower_bound(acb(0, 2), acb(0), 16, Q(1, 2), arb(1))
            self.assertEqual(OA.unpair(row["norm_lower"]), 0)

    def test_11_calibration_prefactor_contractive(self):
        for x in (-7, 0, 11):
            for y in (Q(1, 3), Q(2), Q(9)):
                for h in (Q(1, 7), Q(3), Q(20)):
                    self.assertLessEqual(4 * h * y, (h + y) ** 2 + x * x)

    def test_12_cofinal_positive_part_inequality(self):
        for a in (Q(0), Q(1, 7), Q(1), Q(3)):
            for e in (Q(0), Q(1, 5), Q(1), Q(4)):
                self.assertGreaterEqual(max(Q(0), a - e) ** 2, a * a / 2 - e * e)

    def test_13_normalized_two_kernel_gram(self):
        with OA.precision():
            bound, rows = M.gram_bound([acb(0, 1), acb(3, 1)])
            expected = 1 + 2 / arb(13).sqrt()
            self.assertGreaterEqual(OA.qarb(bound), expected.lower())
            self.assertLess(OA.qarb(bound) - expected.lower(), OA.qarb(Q(1, 2**200)))
            self.assertEqual(rows[0], rows[1])

    def test_14_strict_rational_floor(self):
        self.assertEqual(M.strict_decimal_floor(Q(123, 1000), 3), Q(122, 1000))
        self.assertEqual(M.strict_decimal_floor(Q(1231, 10000), 3), Q(123, 1000))
        self.assertEqual(M.strict_decimal_floor(Q(0), 6), 0)
        for bad in (True, 1.0, "1"):
            with self.assertRaises(ValueError):
                M.strict_decimal_floor(bad, 6)

    def test_15_domain_and_type_guards(self):
        with OA.precision():
            lam = OA.frozen_lambda(64)
            for h in (True, 0, 63, 65, 65537):
                with self.assertRaises(ValueError):
                    M.axis_value(h, lam)
            for width in (True, 0, -1, 2, 0.25):
                with self.assertRaises(ValueError):
                    M.lower_bound(acb(0, 1), acb(1), 64, width, arb(1))
            with self.assertRaises(ValueError):
                M.lower_bound(acb(0, -1), acb(1), 64, Q(1, 4), arb(1))
            with self.assertRaises(ValueError):
                M.gram_bound([])

    def test_16_full_fresh_resealed_attacks(self):
        for field, value in (
            ("inner_premise", "unconditional"),
            ("output", "outer weighted physical norm"),
            ("exclusions", "cofinal proved"),
        ):
            mutant = copy.deepcopy(self.report)
            mutant.pop("payload_sha256")
            mutant["contract"][field] = value
            with self.assertRaises(ValueError):
                M.check_report(M.bc.seal(mutant))
        mutant = copy.deepcopy(self.report)
        mutant.pop("payload_sha256")
        mutant["operators"][0]["bands"][0]["all_node_height_bounds"][0].pop()
        with self.assertRaises(ValueError):
            M.check_report(M.bc.seal(mutant))

    def test_17_source_replay_cannot_be_replaced_by_hash_consistency(self):
        with (
            mock.patch.object(M, "axis_value", return_value=(arb(1), arb(1))),
            self.assertRaises(ValueError),
        ):
            M.check_report(self.report)

    def test_18_parser_rejects_duplicate_or_rounded_inputs(self):
        for raw in (b'{"a":1,"a":2}', b'{"a":1.0}', b"NaN"):
            with self.assertRaises(ValueError):
                M.bc.load_json(raw)

    def test_19_explicit_arithmetic_and_scope(self):
        self.assertEqual(self.report["contract"]["arithmetic_class"], "MIXED")
        self.assertIn("no float acceptance", self.report["contract"]["rounding"])
        self.assertIn(
            "not finite-grid certificates",
            self.report["contract"]["analytic_quantifiers"],
        )

    def test_20_exact_artifact_and_payload(self):
        unsigned = dict(self.report)
        seal = unsigned.pop("payload_sha256")
        self.assertEqual(seal, OA.digest(M.bc.canonical(unsigned)))
        for path, sha in unsigned["artifacts"].items():
            self.assertEqual(M.digest((ROOT / path).read_bytes()), sha)

    def test_21_tiny_tail_widening_is_outward_not_zero(self):
        with OA.precision():
            row = M.lower_bound(acb(0, 1), acb(1), 65536, Q(1, 4), arb(1))
            lo, hi = map(OA.unpair, row["tail"])
            target = Q(1, 2**512)
            self.assertLessEqual(lo, 0)
            self.assertGreaterEqual(hi, target)
            self.assertGreaterEqual(lo, -target / 2**20)
            self.assertLessEqual(hi, target * (1 + Q(1, 2**20)))
            self.assertTrue((-arb(16384)).exp() < OA.qarb(hi))


if __name__ == "__main__":
    unittest.main()
