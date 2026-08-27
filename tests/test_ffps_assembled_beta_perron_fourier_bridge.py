from __future__ import annotations

import importlib.util
import json
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_assembled_beta_perron_fourier_bridge.py"
)
SPEC = importlib.util.spec_from_file_location("assembled_beta_perron", MODULE_PATH)
assert SPEC and SPEC.loader
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class AssembledBetaPerronFourierBridgeTest(unittest.TestCase):
    def test_source_blobs(self) -> None:
        subject.check_source_blobs()

    def test_exceptional_source_coefficients(self) -> None:
        prime = subject.REPLAY_EXCEPTIONAL_PRIME
        residue = 7
        self.assertEqual(
            [subject.beta((prime**exponent) * residue, prime) for exponent in range(4)],
            [
                coefficient * subject.mobius(residue)
                for coefficient in (*subject.EXCEPTIONAL_COEFFICIENTS, 0)
            ],
        )

    def test_exact_primitive_reindex(self) -> None:
        direct, direct_pairs = subject.direct_prefix_energy()
        assembled, assembled_pairs, checks = subject.assembled_prefix_energy()
        self.assertEqual(direct_pairs, assembled_pairs)
        self.assertEqual(direct, assembled)
        self.assertEqual(checks, len(direct_pairs))
        panel = subject.finite_reindex_panel()
        self.assertEqual(panel["ordered_source_pairs"], 2209)
        self.assertEqual(panel["radical_basis_dimension"], 522)

    def test_displayed_collapsed_wavelet_replay(self) -> None:
        direct, _ = subject.direct_prefix_energy()
        collapsed, primitive_products, orientations = (
            subject.collapsed_wavelet_prefix_energy()
        )
        self.assertEqual(collapsed, direct)
        self.assertEqual(primitive_products, 430)
        self.assertEqual(orientations, 1271)
        panel = subject.finite_reindex_panel()
        self.assertEqual(panel["collapsed_wavelet_sha256"], panel["radical_sum_sha256"])

    def test_local_euler_factorizations(self) -> None:
        panel = subject.local_factor_panel()
        self.assertEqual(panel["generic_factorization"], "1+xy-x-y=(1-x)(1-y)")
        self.assertEqual(panel["exceptional_coefficients"], [1, -2, 1])
        self.assertEqual(panel["pair_factorization"], "(1-x)^2(1-y)^2")

    def test_notch_and_max_tilt_firewall(self) -> None:
        panel = subject.notch_tilt_panel()
        for row in panel["rows"]:
            self.assertTrue(row["tilt_refills_zero_mode"])
            self.assertEqual(row["zero_moments"], 2 * row["difference_order"])
        first = subject.repeated_difference(subject.TOY_BOUNDARY_KERNEL, 1)
        correlation = subject.autocorrelation(first)
        self.assertEqual(subject.correlation_moment(correlation, 0), Fraction(0))
        self.assertEqual(subject.correlation_moment(correlation, 1), Fraction(0))

    def test_canonical_json_and_scope(self) -> None:
        result = subject.run(check_sources=False)
        fixture = json.loads(
            MODULE_PATH.with_suffix(".json").read_text(encoding="utf-8")
        )
        self.assertEqual(result, fixture)
        self.assertTrue(result["assembled_identity"]["rh_equivalent"])
        self.assertFalse(result["assembled_identity"]["estimate_proved"])
        self.assertFalse(result["open_gate"]["rh_proved"])
        self.assertEqual(result["resource_caps"]["zeta_zeros"], 0)

    def test_guards(self) -> None:
        with self.assertRaises(ValueError):
            subject.beta(0)
        with self.assertRaises(ValueError):
            subject.ratio_kernel(0, 1)
        with self.assertRaises(ValueError):
            subject.repeated_difference((Fraction(1),), -1)
        with self.assertRaises(ValueError):
            subject.autocorrelation(())
        with self.assertRaises(ValueError):
            subject.harmonic_common_factor(-1, 1, 5)


if __name__ == "__main__":
    unittest.main()
