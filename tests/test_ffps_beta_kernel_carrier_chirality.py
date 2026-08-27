from __future__ import annotations

import importlib.util
import json
import math
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_beta_kernel_carrier_chirality.py"
)
FIXTURE = SCRIPT.with_suffix(".json")
SPEC = importlib.util.spec_from_file_location("beta_kernel_chirality", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load beta-kernel chirality producer")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class FfpsBetaKernelCarrierChiralityTest(unittest.TestCase):
    def test_frozen_sources(self) -> None:
        subject.check_source_blobs()

    def test_atom_weight_is_even_in_tilt(self) -> None:
        for tilt in (-2.0, -0.25, 0.0, 0.25, 2.0):
            for frequency in (-10.0, -1.5, 0.0, 1.5, 10.0):
                self.assertTrue(
                    math.isclose(
                        subject.atom_fourier_weight(tilt, frequency),
                        subject.atom_fourier_weight(-tilt, frequency),
                        rel_tol=1e-13,
                        abs_tol=1e-15,
                    )
                )

    def test_ladder_weight_is_even_in_tilt(self) -> None:
        for order in range(1, subject.MAXIMUM_ORDER + 1):
            for tilt in (-1.0, -0.125, 0.0, 0.125, 1.0):
                for frequency in subject.FREQUENCY_SAMPLES:
                    left = subject.ladder_weight(tilt, order, float(frequency))
                    right = subject.ladder_weight(-tilt, order, float(frequency))
                    self.assertTrue(
                        math.isclose(left, right, rel_tol=1e-13, abs_tol=1e-15)
                    )

    def test_uniform_atom_has_the_expected_side_notches(self) -> None:
        self.assertEqual(subject.atom_fourier_weight(0.0, 0.0), 1.0)
        self.assertLess(subject.atom_fourier_weight(0.0, 2.0 * math.pi), 1e-30)
        self.assertGreater(subject.atom_fourier_weight(0.1, 2.0 * math.pi), 0.0)

    def test_direct_landau_phase_diagram(self) -> None:
        self.assertTrue(
            subject.direct_landau_zone(-0.01, 1).startswith("DIRECTLY SAFE")
        )
        self.assertTrue(subject.direct_landau_zone(0.0, 1).startswith("DIRECTLY SAFE"))
        self.assertTrue(
            subject.direct_landau_zone(0.1, 1).startswith("DIRECT CARRIER GAP")
        )
        self.assertTrue(subject.direct_landau_zone(0.25, 2).startswith("DIRECTLY SAFE"))
        self.assertTrue(subject.direct_landau_zone(1.0, 1).startswith("DIRECTLY SAFE"))

    def test_control_rows_and_scope(self) -> None:
        result = subject.run()
        rows = result["compressed_ladder"]["rows"]
        self.assertEqual(len(rows), subject.MAXIMUM_ORDER * len(subject.TILT_SAMPLES))
        self.assertTrue(all(row["mirror_weight_maximum_error"] == 0.0 for row in rows))
        self.assertEqual(
            result["proof_ledger"]["direct_one_sided_criterion_inside_carrier_gap"],
            "NOT CLAIMED",
        )
        self.assertEqual(result["proof_ledger"]["rh_or_grh"], "NOT PROVED")

    def test_fixture_is_canonical(self) -> None:
        completed = subprocess.run(
            ["python", "-B", str(SCRIPT), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=20,
        )
        self.assertEqual(completed.stdout, "")
        fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
        self.assertEqual(
            fixture["proof_ledger"]["finite_prefix_energy_isospectrality"],
            "PROVED EXACT",
        )
        self.assertEqual(fixture["resource_caps"]["zeta_zeros"], 0)

    def test_guards(self) -> None:
        for bad in (True, 0, -1, subject.MAXIMUM_ORDER + 1, 1.5):
            with self.assertRaises(ValueError):
                subject.validate_order(bad)
        with self.assertRaises(ValueError):
            subject.atom_fourier_weight(float("inf"), 1.0)
        with self.assertRaises(ValueError):
            subject.ladder_weight(0.5, 1, float("nan"))


if __name__ == "__main__":
    unittest.main()
