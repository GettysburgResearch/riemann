from __future__ import annotations

import importlib.util
import json
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
    / "ffps_sharp_rough_single_harmonic_normal_form.py"
)
FIXTURE = SCRIPT.with_suffix(".json")
SPEC = importlib.util.spec_from_file_location("sharp_rough_harmonic", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load sharp rough harmonic producer")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class SharpRoughSingleHarmonicNormalFormTest(unittest.TestCase):
    def test_frozen_source_contract(self) -> None:
        subject.check_source_contract()

    def test_mobius_beta_and_roughness(self) -> None:
        self.assertEqual(
            [subject.mobius(value) for value in range(1, 11)],
            [1, -1, -1, 0, -1, 1, -1, 0, 0, 1],
        )
        self.assertEqual(subject.beta(67), -2)
        self.assertTrue(subject.is_y_rough(17 * 19, 13))
        self.assertFalse(subject.is_y_rough(13 * 17, 13))
        self.assertTrue(subject.is_y_smooth(2**3 * 5 * 13, 13))
        self.assertFalse(subject.is_y_smooth(17, 13))

    def test_finite_rough_and_beta_scale_identities(self) -> None:
        panel = subject.scale_identity_panel(420, 13, subject.FREQUENCY)
        for error in panel["errors"].values():
            self.assertLess(float(error), subject.TOLERANCE)

    def test_two_sided_rough_phase_transport(self) -> None:
        panel = subject.phase_transport_panel(420, 13, subject.FREQUENCY)
        self.assertTrue(panel["two_sided_bound_verified"])
        self.assertLess(float(panel["abel_forward_max_error"]), subject.TOLERANCE)
        self.assertLess(float(panel["abel_reverse_max_error"]), subject.TOLERANCE)

    def test_normalized_unweighted_partial_summation(self) -> None:
        panel = subject.partial_summation_panel(420, 13)
        self.assertTrue(panel["verified"])
        self.assertIn("sqrt", panel["normalization"])

    def test_composed_normal_form_bounds(self) -> None:
        panel = subject.composed_normal_form_panel(420, 13, subject.FREQUENCY)
        self.assertTrue(panel["verified"])
        self.assertLessEqual(
            float(panel["lower_bound"]), float(panel["rough_twisted_max"])
        )
        self.assertLessEqual(
            float(panel["rough_twisted_max"]), float(panel["upper_bound"])
        )

    def test_canonical_fixture_and_theorem_scope(self) -> None:
        completed = subprocess.run(
            ["python", "-B", str(SCRIPT), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=10,
        )
        self.assertEqual(completed.stdout, "")
        fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
        theorem = fixture["theorem"]
        self.assertIn("freeze", theorem["cutoff_quantifier"])
        self.assertIn("fixed nonzero guarded harmonic", theorem["raw_equivalences"])
        self.assertIn("sqrt(N)", theorem["unweighted_equivalence"])

    def test_sharpness_and_no_go_fences(self) -> None:
        result = subject.run(check_sources=False)
        frontier = result["sharp_frontier"]
        self.assertIn("iff", frontier["coefficient_mass_iff"])
        self.assertIn("not a no-go", frontier["scope"])
        scope = result["scope_fences"]
        self.assertFalse(scope["endpoint_only_proved"])
        self.assertFalse(scope["dyadic_replacement_proved"])
        self.assertFalse(scope["moving_cutoff_inside_prefix_maximum"])
        self.assertFalse(scope["moving_frequency_inside_prefix_maximum"])
        self.assertFalse(scope["naive_unnormalized_moving_cutoff_mertens_equivalence"])
        self.assertFalse(scope["rough_estimate_proved"])
        self.assertFalse(scope["rh_or_grh_proved"])

    def test_guards_and_resource_caps(self) -> None:
        with self.assertRaises(ValueError):
            subject.mobius(0)
        with self.assertRaises(ValueError):
            subject.primes_through(0)
        result = subject.run(check_sources=False)
        self.assertEqual(result["resource_caps"]["integer_horizon"], 840)
        self.assertEqual(result["resource_caps"]["zeta_zeros"], 0)
        self.assertTrue(result["kernel_weight"]["nonzero_h_required"])


if __name__ == "__main__":
    unittest.main()
