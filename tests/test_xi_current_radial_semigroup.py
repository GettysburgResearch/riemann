"""Independent exact controls and full source-replay attacks."""

import copy
import math
import sys
import unittest
from fractions import Fraction as Q
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "research/exploratory"))
import xi_current_radial_semigroup as M


class RadialCurrentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = M.build_report()

    def test_01_sources(self):
        self.assertEqual(M.authenticate(), 11)
        self.assertEqual(len(M.BINDINGS), 7)

    def test_02_fixture_primitive_replay(self):
        self.assertEqual(
            M.canonical(self.report), M.canonical(M.load_json(M.FIXTURE.read_bytes()))
        )

    def test_03_full_coverage(self):
        self.assertEqual(
            self.report["coverage"],
            {
                "moments": 13,
                "moment_compositions": 117,
                "adjacent_odd_orders": 31,
                "laplace_compositions": 36,
            },
        )
        self.assertEqual(
            [x["K"] for x in self.report["mlr_controls"]], list(range(1, 62, 2))
        )
        self.assertEqual(
            [x["moment_index"] for x in self.report["moments"]], list(range(13))
        )

    def test_04_first_three_moments(self):
        self.assertEqual(M.radial_multinomial(0), (1,))
        self.assertEqual(M.radial_multinomial(1), (Q(3, 2), 1))
        self.assertEqual(M.radial_multinomial(2), (Q(15, 4), 5, 1))
        self.assertEqual(M.radial_multinomial(3), (Q(105, 8), Q(105, 4), Q(21, 2), 1))

    def test_05_central_radial_chi_moments(self):
        value = Q(1)
        for m in range(13):
            if m:
                value *= Q(2 * m + 1, 2)
            self.assertEqual(M.radial_multinomial(m)[0], value)
            self.assertEqual(M.radial_multinomial(m)[-1], 1)

    def test_06_gaussian_variance_is_half(self):
        self.assertEqual(M.gaussian_even(1), Q(1, 2))
        self.assertEqual(M.gaussian_even(2), Q(3, 4))
        self.assertEqual(M.gaussian_even(3), Q(15, 8))

    def test_07_heldout_three_time_composition(self):
        # Different exact times from the declared producer panel.
        s, t, v = Q(2, 7), Q(3, 5), Q(11, 13)
        for m in range(13):
            first = M.compose_moment(m, t, v)
            result = [Q(0)] * (m + 1)
            for d, c in enumerate(first):
                for e, a in enumerate(M.radial_generator(d)):
                    result[e] += c * a * s ** (d - e)
            expected = [
                c * (s + t + v) ** (m - e) for e, c in enumerate(M.radial_generator(m))
            ]
            self.assertEqual(result, expected)

    def test_08_mlr_first_pair(self):
        self.assertEqual(M.mlr_control(1)["derivative_numerator"], ["1/3"])

    def test_09_independent_positive_mlr_evaluations(self):
        for k in range(1, 62, 2):
            for z in (Q(1, 7), Q(1), Q(9)):

                def polynomial(order, z=z):
                    coefficients = [
                        Q(math.comb(order, 2 * j + 1), order)
                        for j in range((order + 1) // 2)
                    ]
                    value = sum(c * z**j for j, c in enumerate(coefficients))
                    deriv = sum(
                        j * c * z ** (j - 1) for j, c in enumerate(coefficients) if j
                    )
                    return value, deriv

                a, ap = polynomial(k)
                b, bp = polynomial(k + 2)
                direct = bp * a - b * ap
                stored = sum(
                    Q(c) * z**j
                    for j, c in enumerate(M.mlr_control(k)["derivative_numerator"])
                )
                self.assertEqual(direct, stored)
                self.assertGreater(direct, 0)

    def test_10_rounding_and_semigroup_counterexample_geometry(self):
        for delta in (Q(1, 2), Q(1, 13), Q(7, 100)):
            for r in (Q(0), delta, Q(5, 4) * delta, Q(7) * delta):
                order = 1 + 2 * (r // delta)
                self.assertEqual(order % 2, 1)
                self.assertLessEqual(abs(delta * order - 2 * r), delta)
            ratio = Q(5, 4)
            self.assertTrue(1 < ratio and ratio * ratio < 2)
            # Time1 crosses K1->K3; time2 stays at K1.

    def test_11_laplace_zero_and_positive(self):
        for a in (Q(0), Q(2, 9), Q(5)):
            row = M.laplace_control(a, Q(3, 7), Q(8, 11))
            self.assertGreater(Q(row["combined_base"]), 0)
            self.assertEqual(
                Q(row["combined_rate"]), a / (1 + a * (Q(3, 7) + Q(8, 11)))
            )

    def test_12_domain_guards(self):
        for bad in (True, 1.0, "1", -1, 13):
            with self.assertRaises(ValueError):
                M.radial_generator(bad)
        for bad in (True, 0, 2, 64, "3"):
            with self.assertRaises(ValueError):
                M.current(bad)
        for bad in (True, 1.0, "1", 2**257):
            with self.assertRaises(ValueError):
                M.exact(bad)
        with self.assertRaises(ValueError):
            M.mlr_control(63)
        with self.assertRaises(ValueError):
            M.compose_moment(1, 0, 1)
        with self.assertRaises(ValueError):
            M.laplace_control(-1, 1, 1)

    def test_13_parser_guards(self):
        for raw in (b'{"a":1,"a":2}', b'{"a":1.0}', b"NaN", b"Infinity"):
            with self.assertRaises(ValueError):
                M.load_json(raw)
        with self.assertRaises(ValueError):
            M.validate_tree([[[[[[[[[[[[[[[[[0]]]]]]]]]]]]]]]]])
        with self.assertRaises(ValueError):
            M.validate_tree(2**1025)

    def test_14_fully_resealed_scope_and_data_attacks(self):
        mutations = [
            lambda x: x["contract"].update(semigroup="exact native physical semigroup"),
            lambda x: x["contract"].update(exclusions="RH established"),
            lambda x: x["coverage"].update(moment_compositions=116),
            lambda x: x["moments"][2]["x_d_t_m_minus_d_coefficients"].__setitem__(
                0, "15/2"
            ),
            lambda x: x["mlr_controls"].pop(),
            lambda x: x["laplace_controls"][2].update(combined_rate="1"),
        ]
        for change in mutations:
            value = copy.deepcopy(self.report)
            value.pop("payload_sha256")
            change(value)
            with self.assertRaises(ValueError):
                M.check_report(M.seal(value))

    def test_15_primitive_not_just_report_hash(self):
        with (
            mock.patch.object(M, "radial_multinomial", return_value=(Q(1),)),
            self.assertRaises(ValueError),
        ):
            M.check_report(self.report)

    def test_16_manifest_cannot_be_replaced_by_report(self):
        with (
            mock.patch.object(M, "manifest", return_value={}),
            self.assertRaises(ValueError),
        ):
            M.check_report(self.report)

    def test_17_artifacts_and_payload(self):
        raw = dict(self.report)
        seal = raw.pop("payload_sha256")
        self.assertEqual(seal, M.hashlib.sha256(M.canonical(raw)).hexdigest())
        for path, digest in raw["artifacts"].items():
            self.assertEqual(M.lfhash((ROOT / path).read_bytes()), digest)

    def test_18_explicit_boundary(self):
        self.assertEqual(self.report["contract"]["arithmetic_class"], "MIXED")
        self.assertIn("none", self.report["contract"]["rounding"])
        self.assertIn("not certified", self.report["contract"]["analytic_boundary"])
        self.assertIn("fixed finite", self.report["contract"]["semigroup"])
        self.assertIn("Gaussian", self.report["contract"]["universality"])

    def test_19_transitive_primitive_is_authenticated(self):
        original = M.subprocess.check_output

        def changed(command, **kwargs):
            if command[-1].startswith("3b6972320899a82c6caa3a98e2ada5ff703a605a:"):
                return b"changed transitive Xi source"
            return original(command, **kwargs)

        with (
            mock.patch.object(M.subprocess, "check_output", side_effect=changed),
            self.assertRaises(ValueError),
        ):
            M.authenticate()


if __name__ == "__main__":
    unittest.main()
