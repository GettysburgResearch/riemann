from __future__ import annotations

import importlib.util
import json
import math
import subprocess
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_compact_kernel_carrier_zero_flip.py"
)
FIXTURE = SCRIPT.with_suffix(".json")
SPEC = importlib.util.spec_from_file_location("compact_kernel_zero_flip", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load compact-kernel zero-flip producer")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class FfpsCompactKernelCarrierZeroFlipTest(unittest.TestCase):
    def test_frozen_sources(self) -> None:
        subject.check_source_blobs()

    def test_toy_mean_and_carrier_root_are_exact(self) -> None:
        self.assertEqual(sum(subject.TOY_WEIGHTS, Fraction(0)), 0)
        self.assertEqual(
            subject.toy_root_polynomial(subject.TOY_EXPONENTIAL_ROOT),
            0,
        )

    def test_single_flip_has_unit_fourier_modulus(self) -> None:
        for real, imaginary in subject.COMPLEX_ZERO_SAMPLES:
            zero = complex(float(real), float(imaginary))
            for frequency in subject.FREQUENCY_SAMPLES:
                multiplier = subject.zero_flip_multiplier(
                    zero, complex(0.0, float(frequency))
                )
                self.assertTrue(math.isclose(abs(multiplier), 1.0, rel_tol=1e-13))

    def test_conjugate_pair_flip_has_real_coefficients_and_unit_modulus(self) -> None:
        zero = complex(0.25, 1.5)
        for frequency in subject.FREQUENCY_SAMPLES:
            multiplier = subject.conjugate_pair_multiplier(
                zero, complex(0.0, float(frequency))
            )
            self.assertTrue(math.isclose(abs(multiplier), 1.0, rel_tol=1e-13))
        spectral_point = complex(0.7, 0.0)
        multiplier = subject.conjugate_pair_multiplier(zero, spectral_point)
        self.assertAlmostEqual(multiplier.imag, 0.0, places=13)

    def test_toy_energy_weight_is_unchanged(self) -> None:
        for frequency in subject.FREQUENCY_SAMPLES:
            spectral_point = complex(0.0, float(frequency))
            original = subject.toy_transform(spectral_point)
            flipped = subject.toy_flipped_transform(spectral_point)
            self.assertTrue(
                math.isclose(abs(original), abs(flipped), rel_tol=1e-13, abs_tol=1e-15)
            )

    def test_control_rows_and_scope(self) -> None:
        result = subject.run()
        rows = result["toy_certificate"]["rows"]
        self.assertEqual(len(rows), len(subject.FREQUENCY_SAMPLES))
        self.assertTrue(all(row["toy_weight_error"] < 1e-12 for row in rows))
        self.assertEqual(
            result["proof_ledger"]["arbitrary_infinite_zero_flip"],
            "NOT PROVED",
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
            fixture["proof_ledger"]["finite_carrier_defect_repair"],
            "PROVED EXACT",
        )
        self.assertEqual(fixture["resource_caps"]["zeta_zeros"], 0)

    def test_guards(self) -> None:
        with self.assertRaises(ValueError):
            subject.zero_flip_multiplier(1.0j, 1.0)
        with self.assertRaises(ValueError):
            subject.zero_flip_multiplier(1.0, 1.0)
        with self.assertRaises(ValueError):
            subject.conjugate_pair_multiplier(1.0, 1.0j)
        with self.assertRaises(ValueError):
            subject.toy_transform(complex(float("nan"), 0.0))
        with self.assertRaises(TypeError):
            subject.toy_root_polynomial(0.75)


if __name__ == "__main__":
    unittest.main()
