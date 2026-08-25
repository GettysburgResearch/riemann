"""Focused tests for the native q-adic wavelet zero stratum."""

from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import native_qadic_wavelet_zero_stratum as subject


class NativeQadicWaveletZeroStratumTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()

    def test_symbolic_endpoint_three_certificate(self) -> None:
        certificate = subject.symbolic_certificate()
        self.assertEqual(certificate["r_1"], "-a")
        self.assertEqual(certificate["r_2"], "a^2-b")
        self.assertEqual(certificate["r_3"], "-a*(a^2-2*b+q)")
        self.assertEqual(
            certificate["W_3_Q_sqrt_q_coordinates"]["sqrt_q"],
            "-r_2+r_1=b-a^2-a",
        )
        self.assertEqual(
            certificate["reduced_rational_coordinate"],
            "a*((a+1)^2-q)",
        )

    def test_endpoint_three_equivalence_on_nonsquare_coefficient_grid(self) -> None:
        for q in (3, 5, 7, 11, 27):
            self.assertTrue(subject.is_nonsquare_integer(q))
            for a_coefficient in range(-8, 9):
                for b_coefficient in range(-12, 13):
                    reciprocal = subject.reciprocal_coefficients(
                        a_coefficient, b_coefficient, q, 3
                    )
                    wavelet_zero = subject.wavelet_coordinates(reciprocal, 3) == (
                        0,
                        0,
                    )
                    k_zero = (
                        q * a_coefficient * a_coefficient
                        - b_coefficient * b_coefficient
                        == 0
                    )
                    coefficient_zero = a_coefficient == 0 and b_coefficient == 0
                    self.assertEqual(wavelet_zero, coefficient_zero)
                    self.assertEqual(k_zero, coefficient_zero)

    def test_square_q_scope_is_necessary(self) -> None:
        self.assertFalse(subject.is_nonsquare_integer(9))
        reciprocal = subject.reciprocal_coefficients(2, 6, 9, 3)
        self.assertEqual(subject.wavelet_coordinates(reciprocal, 3), (0, 0))
        self.assertEqual(9 * 2**2 - 6**2, 0)
        self.assertNotEqual((2, 6), (0, 0))

    def test_zero_stratum_reciprocal_and_endpoint_pattern(self) -> None:
        q = 5
        reciprocal = subject.reciprocal_coefficients(0, 0, q, 24)
        for endpoint, value in enumerate(reciprocal):
            expected = (-q * q) ** (endpoint // 4) if endpoint % 4 == 0 else 0
            self.assertEqual(value, expected)
        for endpoint in range(25):
            self.assertEqual(
                subject.wavelet_coordinates(reciprocal, endpoint) == (0, 0),
                endpoint % 4 == 3,
            )

    def test_frozen_zero_counts_and_endpoint_seven_exclusion(self) -> None:
        panels = self.fixture["frozen_q_3_5_7_authentication"]
        self.assertEqual([panel["q"] for panel in panels], [3, 5, 7])
        expected = {3: 12, 5: 50, 7: 336}
        for panel in panels:
            count = expected[panel["q"]]
            self.assertEqual(panel["W_3_zero_count"], count)
            self.assertEqual(panel["K_D_zero_count"], count)
            self.assertEqual(panel["a_D_b_D_zero_count"], count)
            self.assertEqual(panel["W_7_zero_count"], count)
            self.assertEqual(panel["W_7_off_stratum_zero_count"], 0)

    def test_affine_orbit_tomography_and_stack_masses(self) -> None:
        panels = {
            panel["q"]: panel for panel in self.fixture["frozen_q_3_5_7_authentication"]
        }
        self.assertEqual(
            panels[3]["affine_zero_orbit_types"],
            [{"orbit_size": 6, "stabilizer_order": 1, "orbit_count": 2}],
        )
        self.assertEqual(
            panels[5]["affine_zero_orbit_types"],
            [
                {"orbit_size": 5, "stabilizer_order": 4, "orbit_count": 2},
                {"orbit_size": 20, "stabilizer_order": 1, "orbit_count": 2},
            ],
        )
        self.assertEqual(
            panels[7]["affine_zero_orbit_types"],
            [{"orbit_size": 42, "stabilizer_order": 1, "orbit_count": 8}],
        )
        self.assertEqual(
            {q: panel["marked_stack_mass"] for q, panel in panels.items()},
            {3: [2, 1], 5: [5, 2], 7: [8, 1]},
        )

    def test_source_locks_artifact_hashes_and_resource_caps(self) -> None:
        manifest = self.fixture["source_manifest"]
        for name, lock in subject.SOURCE_LOCKS.items():
            path = lock["path"]
            self.assertEqual(subject._lf_sha256(path), manifest[name]["lf_sha256"])
            if "payload_sha256" in lock:
                parsed = json.loads(path.read_text(encoding="utf-8"))
                payload = dict(parsed)
                claimed = payload.pop("payload_sha256")
                self.assertEqual(claimed, manifest[name]["payload_sha256"])
                self.assertEqual(claimed, subject._canonical_sha256(payload))
        artifacts = self.fixture["artifact_manifest"]
        self.assertEqual(
            artifacts["producer_lf_sha256"], subject._lf_sha256(Path(subject.__file__))
        )
        self.assertEqual(
            artifacts["note_lf_sha256"], subject._lf_sha256(subject.NOTE_PATH)
        )
        self.assertEqual(
            artifacts["test_lf_sha256"], subject._lf_sha256(subject.TEST_PATH)
        )
        resources = self.fixture["resource_contract"]
        self.assertEqual(resources["new_finite_fields_enumerated"], 0)
        self.assertEqual(resources["new_family_members_enumerated"], 0)
        self.assertEqual(resources["actual_source_atoms"], 251)
        self.assertEqual(resources["actual_recurrence_updates"], 1757)
        self.assertEqual(resources["actual_wavelet_coordinate_checks"], 502)
        for kind in (
            "source_atoms",
            "recurrence_updates",
            "wavelet_coordinate_checks",
            "symbolic_terms",
        ):
            self.assertLessEqual(
                resources[f"actual_{kind}"], resources[f"maximum_{kind}"]
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
            self.assertIn("zero-stratum fixture matches", process.stdout)


if __name__ == "__main__":
    unittest.main()
