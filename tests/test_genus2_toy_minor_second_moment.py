"""Focused exact tests for the genus-two toy-minor second moment."""

from __future__ import annotations

import json
import subprocess
import sys
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import genus2_toy_minor_second_moment as subject


class Genus2ToyMinorSecondMomentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()

    def test_exact_second_moment_and_variance(self) -> None:
        theorem = self.fixture["theorem"]
        self.assertEqual(
            theorem["mean_K_squared"],
            "E[K_D^2]=(3*q^7-8*q^6+6*q^5+8*q^4-9*q^3-19*q^2-4*q-1)/q^3",
        )
        self.assertEqual(theorem["mean_Z_squared_limit"], 3)
        self.assertEqual(theorem["variance_Z_limit"], 2)
        self.assertEqual(
            self.fixture["algebra_certificate"]["mean_K_low_to_high"],
            [[-3, 1], [-2, 1], [-1, 0], [0, -1], [1, 2], [2, -1]],
        )
        self.assertEqual(
            self.fixture["algebra_certificate"]["mean_K_squared_low_to_high"],
            [
                [-3, -1],
                [-2, -4],
                [-1, -19],
                [0, -9],
                [1, 8],
                [2, 6],
                [3, -8],
                [4, 3],
            ],
        )

    def test_held_out_histograms_match_without_becoming_inputs(self) -> None:
        controls = self.fixture["held_out_falsification_controls"]
        self.assertEqual(
            [(row["q"], row["sum_K_squared"]) for row in controls],
            [(3, 14_448), (5, 2_630_080), (7, 69_108_480)],
        )
        self.assertTrue(all(row["matches_all_q_formula"] for row in controls))
        resources = self.fixture["resource_contract"]
        self.assertTrue(resources["held_out_histograms_are_not_theorem_inputs"])
        self.assertEqual(resources["actual_histogram_atoms"], 89)

    def test_cantelli_endpoint_and_monotonicity_certificates(self) -> None:
        sign = self.fixture["sign_density"]
        self.assertEqual(sign["q3_value"], [1352, 8127])
        self.assertEqual(sign["limit"], [1, 3])
        shifted = self.fixture["algebra_certificate"][
            "shifted_positive_coefficients_low_to_high"
        ]
        for coefficients in shifted.values():
            self.assertTrue(all(value > 0 for value in coefficients))

    def test_cantelli_bound_is_strictly_increasing_on_controls(self) -> None:
        def bound(q: int) -> Fraction:
            p = q**5 - 2 * q**4 + q**3 - q - 1
            n = (
                3 * q**7
                - 8 * q**6
                + 6 * q**5
                + 8 * q**4
                - 9 * q**3
                - 19 * q**2
                - 4 * q
                - 1
            )
            return Fraction(p * p, q**3 * n)

        values = [bound(q) for q in (3, 5, 7, 9, 11, 25, 101)]
        self.assertEqual(values[0], Fraction(1352, 8127))
        self.assertEqual(values, sorted(set(values)))
        self.assertTrue(all(value < Fraction(1, 3) for value in values))

    def test_two_point_witness_matches_both_moments_and_support(self) -> None:
        for q in (3, 5, 7, 9, 25, 101):
            p = q**5 - 2 * q**4 + q**3 - q - 1
            n = (
                3 * q**7
                - 8 * q**6
                + 6 * q**5
                + 8 * q**4
                - 9 * q**3
                - 19 * q**2
                - 4 * q
                - 1
            )
            mean = Fraction(-p, q**5)
            second = Fraction(n, q**7)
            x = second / mean
            mass = mean * mean / second
            self.assertGreater(x, -20)
            self.assertLess(x, 0)
            self.assertGreater(mass, 0)
            self.assertLess(mass, 1)
            self.assertEqual(mass * x, mean)
            self.assertEqual(mass * x * x, second)

    def test_new_bound_strictly_dominates_old_range_bound(self) -> None:
        for q in range(3, 80):
            p = q**5 - 2 * q**4 + q**3 - q - 1
            n = (
                3 * q**7
                - 8 * q**6
                + 6 * q**5
                + 8 * q**4
                - 9 * q**3
                - 19 * q**2
                - 4 * q
                - 1
            )
            self.assertGreater(Fraction(p * p, q**3 * n), Fraction(p, 20 * q**5))

    def test_source_locks_scope_and_resource_caps(self) -> None:
        sources = self.fixture["source_manifest"]
        for name, path in {
            "second_reduction": subject.SECOND_REDUCTION_PATH,
            "M22": subject.M22_PATH,
            "B4": subject.B4_PATH,
            "q_scan": subject.Q_SCAN_PATH,
            "usp4_range": subject.USP4_RANGE_PATH,
        }.items():
            self.assertEqual(subject._lf_sha256(path), sources[name]["lf_sha256"])
            parsed = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(parsed["payload_sha256"], sources[name]["payload_sha256"])
        scope = self.fixture["scope"]
        self.assertEqual(scope["finite_fields_enumerated_by_theorem_replay"], 0)
        self.assertEqual(scope["sampled_values_used_as_theorem_input"], 0)
        resources = self.fixture["resource_contract"]
        self.assertLessEqual(
            resources["actual_laurent_updates"],
            resources["maximum_laurent_updates"],
        )
        self.assertLessEqual(
            resources["actual_translation_updates"],
            resources["maximum_translation_updates"],
        )
        self.assertLessEqual(
            resources["actual_histogram_atoms"],
            resources["maximum_histogram_atoms"],
        )
        self.assertEqual(resources["actual_laurent_updates"], 384)
        self.assertEqual(resources["actual_translation_updates"], 226)

        for name, path in {
            "packet_note": subject.NOTE_PATH,
            "packet_producer": Path(subject.__file__).resolve(),
            "packet_test": subject.TEST_PATH,
        }.items():
            self.assertEqual(subject._lf_sha256(path), sources[name]["lf_sha256"])
            self.assertNotIn("payload_sha256", sources[name])

    def test_fixture_hash_and_cli_replay(self) -> None:
        stored = json.loads(subject.OUTPUT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(stored, self.fixture)
        payload = dict(stored)
        claimed = payload.pop("payload_sha256")
        self.assertEqual(claimed, subject._canonical_sha256(payload))
        for optimization in ([], ["-O"]):
            process = subprocess.run(
                [sys.executable, *optimization, str(Path(subject.__file__)), "--check"],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
                timeout=10,
            )
            self.assertEqual(process.returncode, 0, process.stderr)
            self.assertIn("second-moment fixture matches", process.stdout)


if __name__ == "__main__":
    unittest.main()
