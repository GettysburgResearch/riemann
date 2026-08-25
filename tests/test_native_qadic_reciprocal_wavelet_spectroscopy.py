"""Focused tests for native q-adic reciprocal-wavelet spectroscopy."""

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

import native_qadic_reciprocal_wavelet_spectroscopy as subject


class NativeQadicReciprocalWaveletSpectroscopyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()

    def test_reciprocal_recurrence_inverts_the_quartic(self) -> None:
        for q, a_coefficient, b_coefficient in (
            (3, -3, 5),
            (5, 2, -1),
            (7, 0, 14),
        ):
            reciprocal = subject.reciprocal_coefficients(
                a_coefficient, b_coefficient, q, 12
            )
            polynomial = (1, a_coefficient, b_coefficient, q * a_coefficient, q**2)
            for degree in range(13):
                convolution = sum(
                    polynomial[index] * reciprocal[degree - index]
                    for index in range(min(4, degree) + 1)
                )
                self.assertEqual(convolution, 1 if degree == 0 else 0)

    def test_wavelet_coordinates_equal_direct_partial_sum_filter(self) -> None:
        reciprocal = subject.reciprocal_coefficients(-2, 6, 3, 10)
        partial = []
        running = 0
        for value in reciprocal:
            running += value
            partial.append(running)
        for endpoint in range(2, 11):
            rational, radical = subject.wavelet_coordinates(reciprocal, endpoint)
            self.assertEqual(
                rational,
                partial[endpoint] - 2 * partial[endpoint - 1] + partial[endpoint - 2],
            )
            shifted = (
                partial[endpoint - 1]
                - 2 * partial[endpoint - 2]
                + (partial[endpoint - 3] if endpoint >= 3 else 0)
            )
            self.assertEqual(radical, -shifted)

    def test_quadratic_sign_is_exact(self) -> None:
        self.assertEqual(subject.quadratic_sign(1, 1, 5), 1)
        self.assertEqual(subject.quadratic_sign(-1, -1, 5), -1)
        self.assertEqual(subject.quadratic_sign(3, -1, 5), 1)
        self.assertEqual(subject.quadratic_sign(2, -1, 5), -1)
        self.assertEqual(subject.quadratic_sign(2, -1, 4), 0)
        self.assertEqual(subject.quadratic_sign(0, 0, 7), 0)

    def test_exact_symmetric_power_trace_panels(self) -> None:
        panels = self.fixture["exact_finite_panels"]
        traces = {
            str(panel["q"]): panel["marked_symmetric_power_trace_values"]
            for panel in panels
        }
        self.assertEqual(
            traces,
            {
                "3": {
                    "T_(2,0)": 2,
                    "T_(4,0)": -3,
                    "T_(6,0)": -4,
                    "T_(8,0)": -21,
                },
                "5": {
                    "T_(2,0)": 4,
                    "T_(4,0)": -3,
                    "T_(6,0)": -4,
                    "T_(8,0)": 199,
                },
                "7": {
                    "T_(2,0)": 6,
                    "T_(4,0)": -3,
                    "T_(6,0)": -4,
                    "T_(8,0)": -1029,
                },
            },
        )

    def test_twist_parity_and_adjacent_pair_mean_law(self) -> None:
        definition = self.fixture["definition"]
        theorem = self.fixture["normalization_theorem"]
        self.assertEqual(
            definition["negative_endpoint_convention"],
            "M_D(N)=r_D(N)=0 for N<0",
        )
        self.assertIn("irreducible Sp4", theorem["symmetric_power_irreducibility"])
        self.assertIn("full AGL(1,F_q)", theorem["twist_pairing"])
        self.assertIn("nonsquare multiplier", theorem["twist_pairing"])
        for panel in self.fixture["exact_finite_panels"]:
            reciprocal_means = {
                int(endpoint): Fraction(*pair)
                for endpoint, pair in panel["reciprocal_means_0_through_8"].items()
            }
            self.assertTrue(
                all(reciprocal_means[endpoint] == 0 for endpoint in (1, 3, 5, 7))
            )
            for row in panel["wavelet_rows"]:
                endpoint = row["endpoint"]
                coordinates = row["mean_Q_sqrt_q_coordinates"]
                rational = Fraction(*coordinates["rational"])
                radical = Fraction(*coordinates["sqrt_q"])
                if endpoint % 2 == 0:
                    self.assertEqual(rational, reciprocal_means[endpoint])
                    self.assertEqual(radical, reciprocal_means[endpoint - 2])
                else:
                    self.assertEqual(rational, -reciprocal_means[endpoint - 1])
                    self.assertEqual(radical, -reciprocal_means[endpoint - 1])

    def test_every_locked_endpoint_has_both_memberwise_signs(self) -> None:
        for panel in self.fixture["exact_finite_panels"]:
            for row in panel["wavelet_rows"]:
                counts = row["sign_counts"]
                self.assertGreater(counts["negative"], 0)
                self.assertGreater(counts["positive"], 0)
                self.assertEqual(
                    counts["negative"] + counts["zero"] + counts["positive"],
                    panel["members"],
                )
                self.assertTrue(row["memberwise_sign_is_mixed"])

    def test_source_locks_and_resource_contract(self) -> None:
        manifest = self.fixture["source_manifest"]
        for name, lock in subject.SOURCE_LOCKS.items():
            path = lock["path"]
            self.assertEqual(subject._lf_sha256(path), manifest[name]["lf_sha256"])
            parsed = json.loads(path.read_text(encoding="utf-8"))
            if lock["payload"] is not None:
                self.assertEqual(
                    parsed["payload_sha256"], manifest[name]["payload_sha256"]
                )
        resources = self.fixture["resource_contract"]
        self.assertEqual(resources["new_finite_fields_enumerated"], 0)
        self.assertEqual(resources["new_curves_enumerated"], 0)
        self.assertLessEqual(
            resources["actual_source_atoms"], resources["maximum_source_atoms"]
        )
        self.assertLessEqual(
            resources["actual_atom_endpoint_evaluations"],
            resources["maximum_atom_endpoint_evaluations"],
        )
        self.assertLessEqual(
            resources["actual_recurrence_updates"],
            resources["maximum_recurrence_updates"],
        )

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
            self.assertIn("native q-adic wavelet fixture matches", process.stdout)


if __name__ == "__main__":
    unittest.main()
