"""Actual global source support, interval roots, clipping and hostile controls."""

import copy
import importlib.util
import json
import unittest
from fractions import Fraction as F
from itertools import pairwise
from pathlib import Path
from unittest.mock import patch

PATH = (
    Path(__file__).resolve().parents[1]
    / "research/riemann-structures/native-six-hour/native_clipped_path_certificate.py"
)
SPEC = importlib.util.spec_from_file_location("native_global_clipped_optimum", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class NativeClippedOptimumTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scout = M.frozen("scout", True)
        cls.data = json.loads(M.frozen("data"))
        cls.heldout = json.loads(M.frozen("heldout"))
        cls.attempts = M.validate_discovery(cls.data)

    def test_exact_source_authentication_precedes_import(self):
        with (
            patch.object(
                M.subprocess, "check_output", side_effect=ValueError("source changed")
            ),
            patch("builtins.compile") as compiler,
        ):
            with self.assertRaisesRegex(ValueError, "source changed"):
                M.frozen("scout", True)
            compiler.assert_not_called()

    def test_all16_declared_starts_and_outcomes_retained(self):
        self.assertEqual(len(self.attempts), 16)
        self.assertEqual(
            [row["start"] for row in self.attempts],
            [list(map(str, x)) for x in self.scout.STARTS],
        )
        self.assertEqual(
            self.data["globally_certified_attempt_indices"], list(range(16))
        )
        self.assertTrue(all(len(row["steps"]) <= 32 for row in self.attempts))
        self.assertIs(self.data["floating_steps_are_seed_only"], True)

    def test_every_root_has_strict_whole_box_contraction(self):
        for attempt in self.attempts:
            row = attempt["rational_certificate"]
            self.assertLess(F(row["contraction_upper"]), 1)
            for box, image in zip(row["root_box"], row["Krawczyk_image"], strict=True):
                self.assertLess(F(box["lower"]), F(image["lower"]))
                self.assertLess(F(image["upper"]), F(box["upper"]))
                self.assertEqual(
                    F(box["upper"]) - F(box["lower"]), 2 * self.scout.RADIUS
                )

    def test_actual_minimizer_is_strictly_lower_clipped_only(self):
        for attempt in self.attempts:
            row = attempt["rational_certificate"]
            regime = row["clipping_regime"]
            self.assertIs(regime["lower_clipped"], True)
            self.assertIs(regime["upper_clipped"], False)
            self.assertGreater(F(regime["left_breakpoint"]["lower"]), F(22, 100))
            self.assertLess(F(regime["left_breakpoint"]["upper"]), F(23, 100))
            self.assertEqual(F(regime["right_breakpoint"]["lower"]), 1)

    def test_independent_lower_clipped_moments_keep_C_half(self):
        values = M.lower_clipped_moments(F(-1, 4), F(1))
        self.assertEqual(values, (F(9, 32), F(27, 128), F(9, 128), 0, 0, 0))
        self.assertEqual(2 * values[2], F(9, 64))
        for attempt in self.attempts:
            center = tuple(map(F, attempt["proposed_exact_binary_center"]))
            actual = attempt["rational_certificate"]["nearby_rational_actual_path"]
            self.assertEqual(
                tuple(map(F, actual["source_coordinates"])),
                M.lower_clipped_moments(*center),
            )

    def test_strict_full_support_margins_give_quantitative_coercivity(self):
        for attempt in self.attempts:
            row = attempt["rational_certificate"]
            self.assertGreater(F(row["original_source_c"]["lower"]), F(3, 2))
            cone = row["full_w_last_support_cone"]
            self.assertGreater(F(cone["f"]["lower"]), F(5, 2))
            self.assertGreater(F(cone["d_plus_e_half"]["lower"]), 2)
            self.assertGreater(F(cone["d_plus_e"]["lower"]), 2)

    def test_original_energy_improves_heldout_grid_without_using_it_as_proof(self):
        for attempt in self.attempts:
            energy = attempt["rational_certificate"]["root_energy"]
            self.assertGreater(F(energy["lower"]), F(15746, 100))
            self.assertLess(F(energy["upper"]), F(15748, 100))
            self.assertLess(
                F(energy["upper"]),
                F(self.heldout["panels"][0]["minimum_energy_interval"]["lower"]),
            )

    def test_every_nearby_actual_path_retains_all63_and45(self):
        for attempt in self.attempts:
            row = attempt["rational_certificate"]["nearby_rational_actual_path"]
            self.assertEqual(len(row["complete63_source"]), 63)
            self.assertEqual(len(row["complete45_ratio_image"]), 45)
            self.assertEqual(tuple(map(F, row["source_coordinates"][3:])), (0, 0, 0))

    def test_rational_path_is_monotone_and_last_activation_is_literal(self):
        for attempt in self.attempts:
            points = [
                tuple(map(F, x))
                for x in attempt["rational_certificate"]["nearby_rational_actual_path"][
                    "vertices"
                ]
            ]
            self.assertEqual(points[0], (0, 0, 0))
            self.assertEqual(points[-2:], [(1, 1, 0), (1, 1, 1)])
            for left, right in pairwise(points):
                self.assertTrue(all(a <= b for a, b in zip(left, right, strict=True)))

    def test_bad_rounding_domain_and_clipping_box_are_refused(self):
        with self.assertRaisesRegex(ValueError, "outward lattice"):
            self.scout.certificate(
                None, None, {"proposed_exact_binary_center": ["-1/3", "5/4"]}
            )
        with self.assertRaisesRegex(ValueError, "lower clipping boundary"):
            self.scout.interval_profile((self.scout.point(0), self.scout.point(1)))
        with self.assertRaises(ValueError):
            self.scout.interval_profile(
                (self.scout.point(F(-1, 4)), self.scout.point(-1))
            )

    def test_false_root_box_is_not_accepted_by_boolean_flags(self):
        changed = copy.deepcopy(self.data)
        row = changed["all16_declared_starts"][0]["rational_certificate"]
        row["Krawczyk_image"][0]["upper"] = row["root_box"][0]["upper"]
        with self.assertRaisesRegex(ValueError, "Krawczyk"):
            M.validate_discovery(changed)

    def test_false_full_support_cone_or_omitted_start_is_rejected(self):
        changed = copy.deepcopy(self.data)
        changed["all16_declared_starts"][0]["rational_certificate"][
            "full_w_last_support_cone"
        ]["f"]["lower"] = "-1"
        with self.assertRaisesRegex(ValueError, "full all-path source cone"):
            M.validate_discovery(changed)
        changed = copy.deepcopy(self.data)
        changed["all16_declared_starts"].pop()
        with self.assertRaises(ValueError):
            M.validate_discovery(changed)

    def test_scope_does_not_promote_to_full_gamma_or_all_horizons(self):
        self.assertIs(self.data["full_gamma_identified"], False)
        self.assertIs(self.data["all_height_path_theorem_claimed"], False)
        changed = copy.deepcopy(self.data)
        changed["full_gamma_identified"] = True
        with self.assertRaisesRegex(ValueError, "scope"):
            M.validate_discovery(changed)

    def test_exact_types_caps_and_artifact_hash(self):
        for wrong in (True, 0.5):
            with self.assertRaises(ValueError):
                M.lower_clipped_moments(wrong, 1)
            with self.assertRaises(ValueError):
                self.scout.point(wrong)
        with self.assertRaises(ValueError):
            M.lower_clipped_moments(F(-1, 4), 2)
        for wrong in (True, 1.0):
            with self.assertRaises(ValueError):
                M.strict_equal({"rank": 1}, {"rank": wrong})
        body = {
            key: value
            for key, value in self.data.items()
            if key != "proof_object_sha256"
        }
        self.assertEqual(
            M.sha256(M.canonical(body).encode()).hexdigest(),
            self.data["proof_object_sha256"],
        )


if __name__ == "__main__":
    unittest.main()
