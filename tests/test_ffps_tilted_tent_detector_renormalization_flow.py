from __future__ import annotations

import importlib.util
import json
import math
import subprocess
import unittest
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_tilted_tent_detector_renormalization_flow.py"
)
FIXTURE = SCRIPT.with_suffix(".json")
SPEC = importlib.util.spec_from_file_location("tilted_tent_flow", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load tilted-tent renormalization producer")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class FfpsTiltedTentDetectorRenormalizationFlowTest(unittest.TestCase):
    def test_frozen_sources(self) -> None:
        subject.check_source_blobs()

    def test_exact_mgf_and_first_four_cumulants(self) -> None:
        self.assertEqual(
            sp.simplify(subject.symbolic_mgf().subs(subject.T_SYMBOL, 0)), 1
        )
        actual = subject.symbolic_cumulants(4)
        expected = subject.expected_first_four_cumulants()
        self.assertTrue(
            all(sp.simplify(left - right) == 0 for left, right in zip(actual, expected))
        )

    def test_mean_and_variance_match_exact_formulas(self) -> None:
        mean, variance = subject.mean_and_variance()
        substitutions = {subject.E_SYMBOL: math.e}
        exact = subject.expected_first_four_cumulants()
        self.assertTrue(
            math.isclose(mean, float(exact[0].subs(substitutions)), rel_tol=1e-14)
        )
        self.assertTrue(
            math.isclose(
                variance,
                float(exact[1].subs(substitutions)),
                rel_tol=1e-14,
            )
        )
        self.assertGreater(variance, 0.0)

    def test_fourier_normalization_and_real_zero_control(self) -> None:
        self.assertEqual(subject.normalized_p_fourier(0.0), 1.0 + 0.0j)
        for frequency in subject.WEIGHT_FREQUENCIES:
            self.assertGreater(abs(subject.normalized_p_fourier(frequency)), 0.0)
            for order in subject.REPLAY_ORDERS:
                self.assertGreater(subject.diffusive_weight(order, frequency), 0.0)
        for order in subject.REPLAY_ORDERS:
            self.assertEqual(subject.diffusive_weight(order, 0.0), 0.0)

    def test_bounded_weight_flow_approaches_gaussian_control(self) -> None:
        rows = subject.weight_control_rows()
        self.assertEqual([row["order"] for row in rows], list(subject.REPLAY_ORDERS))
        self.assertLess(
            rows[-1]["maximum_sample_error"],
            rows[0]["maximum_sample_error"],
        )
        self.assertTrue(all(row["real_weight_zero_set"] == [0] for row in rows))

    def test_exact_gaussian_constants_and_scope(self) -> None:
        result = subject.run()
        constants = result["norm_and_jordan_asymptotics"]
        self.assertEqual(constants["derivative_gaussian_energy"], "1/(4*sqrt(pi))")
        self.assertEqual(constants["gaussian_density_energy"], "1/(2*sqrt(pi))")
        self.assertEqual(
            result["proof_ledger"]["growing_order_beta_theorem"],
            "NOT PROVED",
        )
        self.assertEqual(result["proof_ledger"]["rh_or_grh"], "NOT PROVED")
        self.assertEqual(result["resource_caps"]["zeta_zeros"], 0)
        self.assertEqual(result["resource_caps"]["primes"], 0)

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
        self.assertEqual(fixture["source_contract"]["commit"], "3658d4c31")
        self.assertEqual(
            fixture["proof_ledger"]["uniform_edgeworth_remainder"],
            "PROVED BY THE SELF-CONTAINED FOURIER-SPLITTING LEMMA IN THE MARKDOWN",
        )

    def test_guards(self) -> None:
        for bad in (True, 0, -1, subject.MAXIMUM_REPLAY_ORDER + 1, 1.5):
            with self.assertRaises(ValueError):
                subject.validate_order(bad)
        for bad in (True, 0, -1, 9, 1.5):
            with self.assertRaises(ValueError):
                subject.symbolic_cumulants(bad)
        with self.assertRaises(ValueError):
            subject.normalized_p_fourier(float("inf"))
        with self.assertRaises(ValueError):
            subject.diffusive_weight(1, float("nan"))
        with self.assertRaises(ValueError):
            subject.gaussian_derivative_weight(float("inf"))


if __name__ == "__main__":
    unittest.main()
