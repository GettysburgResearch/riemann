from __future__ import annotations

import importlib.util
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
    / "ffps_primitive_pair_harmonic_incidence_carleson.py"
)
SPEC = importlib.util.spec_from_file_location("primitive_pair_incidence", MODULE_PATH)
assert SPEC and SPEC.loader
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class PrimitivePairHarmonicIncidenceCarlesonTest(unittest.TestCase):
    def test_source_blobs(self) -> None:
        subject.check_source_blobs()

    def test_layer_partition_recovers_the_shell(self) -> None:
        alpha, gamma = subject.REPLAY_CHANNEL
        height = subject.REPLAY_HEIGHT
        strata = subject.block_strata(
            alpha, gamma, tuple(range(height + 1, 2 * height + 1))
        )
        for sieve in (1, 2, 3, 5, 6):
            with self.subTest(sieve=sieve):
                self.assertEqual(
                    subject.panel_from_strata(strata, sieve),
                    subject.SOURCE.panel_form(alpha, gamma, sieve, height, 2 * height),
                )

    def test_finite_linear_and_quadratic_incidence_gram(self) -> None:
        alpha, gamma = subject.REPLAY_CHANNEL
        height = subject.REPLAY_HEIGHT
        strata = subject.block_strata(
            alpha, gamma, tuple(range(height + 1, 2 * height + 1))
        )
        self.assertEqual(
            subject.direct_linear_energy(strata, subject.REPLAY_LIMIT),
            subject.gram_linear_energy(strata, subject.REPLAY_LIMIT),
        )

    def test_every_prefix_has_a_short_dyadic_decomposition(self) -> None:
        for length in range(1, 18):
            family = set(subject.aligned_dyadic_intervals(length))
            for prefix in range(length + 1):
                blocks = subject.prefix_dyadic_decomposition(prefix, length)
                self.assertTrue(all(block in family for block in blocks))
                self.assertEqual(sum(stop - start for start, stop in blocks), prefix)
                self.assertLessEqual(len(blocks), max(1, length.bit_length()))

    def test_dyadic_certificate(self) -> None:
        certificate = subject.dyadic_certificate(0, 0, subject.REPLAY_HEIGHT)
        self.assertEqual(certificate["height_count"], subject.REPLAY_HEIGHT)
        self.assertEqual(certificate["family_size"], 7)
        self.assertEqual(certificate["max_blocks_in_prefix"], 2)

    def test_harmonic_cube_mean_is_rho_tilted(self) -> None:
        alpha, gamma = subject.REPLAY_CHANNEL
        height = subject.REPLAY_HEIGHT
        strata = subject.block_strata(
            alpha, gamma, tuple(range(height + 1, 2 * height + 1))
        )
        modulus = subject.primorial_through(2 * height)
        certificate = subject.harmonic_cube_certificate(strata, modulus)
        self.assertTrue(certificate["rho_tilt_match"])
        self.assertTrue(certificate["squarefree_harmonic_coefficient_match"])
        self.assertTrue(certificate["mode_energy_match"])
        self.assertEqual(certificate["incidence_classes"], 16)
        self.assertEqual(len(certificate["mode_digests"]), 16)

    def test_rho_and_local_euler_correction(self) -> None:
        self.assertEqual(subject.rho(1), 1)
        self.assertEqual(subject.rho(30), Fraction(5, 12))
        rows = subject.local_euler_certificate()
        self.assertEqual(rows[0]["rho"], "2/3")
        self.assertEqual(rows[-1]["correction_linear"], "1/8")

    def test_canonical_run_and_scope(self) -> None:
        result = subject.run(check_sources=False)
        gate = result["conditional_gate"]
        self.assertEqual(gate["name"], "PRIMCAR")
        self.assertTrue(gate["implies_primls"])
        self.assertTrue(gate["conditional_implication_to_rh_proved"])
        self.assertFalse(gate["estimate_proved"])
        self.assertFalse(gate["rh_proved"])
        self.assertFalse(result["scope"]["primls_proved"])
        self.assertFalse(result["scope"]["rh_or_grh_proved"])
        self.assertEqual(result["resource_caps"]["zeta_zeros"], 0)

    def test_guards(self) -> None:
        with self.assertRaises(ValueError):
            subject.layer_strata(1, 1, 4)
        with self.assertRaises(ValueError):
            subject.layer_strata(0, 0, 0)
        with self.assertRaises(ValueError):
            subject.panel_from_strata({}, 4)
        with self.assertRaises(ValueError):
            subject.prefix_dyadic_decomposition(3, 2)
        with self.assertRaises(ValueError):
            subject.rho(0)


if __name__ == "__main__":
    unittest.main()
