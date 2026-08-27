from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_basewave_primcar_identity.py"
)
SPEC = importlib.util.spec_from_file_location("basewave_primcar_identity", MODULE_PATH)
assert SPEC and SPEC.loader
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class BasewavePrimcarIdentityTest(unittest.TestCase):
    def test_frozen_sources_and_repaired_scope(self) -> None:
        subject.check_source_blobs()
        subject.check_scope_markers()

    def test_u_one_predicates_match_in_all_channels(self) -> None:
        for alpha in subject.ALPHAS:
            for d in subject.SIEVE_VALUES:
                if not subject.is_squarefree_67_free(d):
                    continue
                for heights in subject.replay_height_family(alpha, 8):
                    for left in range(1, 9):
                        for right in range(1, 9):
                            with self.subTest(
                                alpha=alpha,
                                d=d,
                                heights=tuple(sorted(heights)),
                                left=left,
                                right=right,
                            ):
                                self.assertEqual(
                                    subject.original_predicate(
                                        alpha, d, heights, left, right
                                    ),
                                    subject.generalized_u_one_predicate(
                                        alpha, d, heights, left, right
                                    ),
                                )

    def test_u_one_generalized_and_wavelet_terms_match_original(self) -> None:
        for alpha in subject.ALPHAS:
            for d in (1, 2, 3, 6):
                for heights in subject.replay_height_family(alpha, 8):
                    original = subject.original_terms(alpha, d, heights, 8)
                    self.assertEqual(
                        original,
                        subject.generalized_u_one_terms(alpha, d, heights, 8),
                    )
                    self.assertEqual(
                        original,
                        subject.basewave_u_one_terms(alpha, d, heights, 8),
                    )

    def test_finite_energy_certificate(self) -> None:
        certificate = subject.finite_identity_certificate(8)
        self.assertTrue(certificate["termwise_identity"])
        self.assertEqual(certificate["alphas"], [0, 1, 2])
        self.assertEqual(certificate["aux_u_one_weight"], "1")
        self.assertGreater(certificate["predicate_checks"], 0)
        self.assertGreater(certificate["panel_checks"], 0)
        for row in certificate["rows"]:
            self.assertEqual(row["basewave_probe_energy"], row["primcar_probe_energy"])

    def test_hierarchy_and_firewalls(self) -> None:
        report = subject.run(check_sources=False)
        hierarchy = report["conditional_hierarchy"]
        self.assertEqual(
            hierarchy["wave_route"],
            "WAVEPRIMCAR -> BASEWAVE (=PRIMCAR) -> PRIMLS -> RH",
        )
        self.assertFalse(hierarchy["eta_below_one_half_needed_for_direct_wave_route"])
        scope = report["scope"]
        self.assertFalse(scope["basewave_estimate_proved"])
        self.assertFalse(scope["primcar_estimate_proved"])
        self.assertFalse(scope["rh_proved"])
        self.assertFalse(scope["colorprimcar_d_one_alone_suffices"])

    def test_guards(self) -> None:
        with self.assertRaises(ValueError):
            subject.mobius(0)
        with self.assertRaises(ValueError):
            subject.primitive_height(3, 1, 1)
        with self.assertRaises(ValueError):
            subject.divisors(0)
        with self.assertRaises(ValueError):
            subject.finite_identity_certificate(0)


if __name__ == "__main__":
    unittest.main()
