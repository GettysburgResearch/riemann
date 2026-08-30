"""Exact coefficient, kernel, prime-certificate and normalization firewalls."""

import importlib.util
import json
import unittest
from fractions import Fraction
from pathlib import Path
from unittest.mock import patch

PATH = (
    Path(__file__).resolve().parents[1]
    / "research"
    / "riemann-structures"
    / "subcritical_observed_boolean_block.py"
)
SPEC = importlib.util.spec_from_file_location("subcritical_boolean", PATH)
S = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(S)


class SubcriticalObservedBooleanTests(unittest.TestCase):
    def test_primitive_kernel_norm_and_endpoint_variation(self):
        record = S.kernel_record()
        self.assertEqual(record["norm_log2_coefficient"], ["384", "128"])
        self.assertEqual(record["norm_constant"], ["-288", "0"])
        self.assertEqual(record["total_variation"], ["0", "32"])
        self.assertEqual(record["translation_penalty"], "512")
        self.assertEqual(Fraction(record["strict_gram_lower"]), Fraction(544, 15))

    def test_quadratic_signs_do_not_use_float_approximations(self):
        self.assertEqual(S.sign(S.q2(-7, 5)), 1)
        self.assertEqual(S.sign(S.q2(7, -5)), -1)
        self.assertEqual(S.sign(S.q2(-3, 2)), -1)
        self.assertEqual(S.sign(S.q2()), 0)
        self.assertEqual(S.mul(S.q2(0, 1), S.q2(0, 1)), S.q2(2))

    def test_all_twenty_four_large_and_small_prime_certificates(self):
        count = 0
        for panel in S.PANELS.values():
            for certificate in panel.values():
                self.assertEqual(S.verify_prime(certificate)["prime"], certificate[0])
                count += 1
        self.assertEqual(count, 24)

    def test_prime_certificate_failures_are_not_probable_prime_acceptance(self):
        for certificate in (
            (9, 0, 0),
            (True, 0, 0),
            (25, 3, 2),
            (17, 4, 1),
            (2**65 + 1, 32, 3),
        ):
            with self.subTest(certificate=certificate), self.assertRaises(ValueError):
                S.verify_prime(certificate)

    def test_frozen_a_u_sign_convention_and_cutoff(self):
        self.assertEqual(S.a_u((11,), 5), -1)
        self.assertEqual(S.a_u((2, 3), 5), 1)
        self.assertEqual(S.a_u((11,), 11), 0)
        self.assertEqual(S.a_u((), 5), 0)

    def test_complete_boolean_history_count_not_selected_signs(self):
        histories = S.histories((11, 2, 3), 5)
        self.assertEqual(len(histories), 2)
        self.assertEqual([row["coefficient"] for row in histories], [-1, -1])
        self.assertEqual(
            {tuple(map(tuple, row["groups"])) for row in histories},
            {((11,), (2, 3), ()), ((2, 3), (11,), ())},
        )
        self.assertEqual(S.histories((11, 2, 3), 7), [])

    def test_all_three_exact_physical_window_panels(self):
        for j, panel in S.PANELS.items():
            record = S.panel_record(j, panel)
            self.assertLess(record["Y"], min(record["N"], record["M"]))
            self.assertLess(
                max(record["N"], record["M"]), Fraction(11, 10) * record["Y"]
            )
            self.assertEqual(record["equal_pair_share"], "1/10")
            self.assertEqual(record["bilateral_literal_histories"], 4)

    def test_original_bilateral_and_literal_wick_diagonal_are_distinct(self):
        record = S.panel_record(52, S.PANELS[52])
        aggregate = Fraction(record["aggregate_coefficient_square"])
        diagonal = Fraction(record["literal_bilateral_diagonal"])
        self.assertEqual(aggregate, 4 * diagonal)
        self.assertEqual(aggregate, Fraction(1, 625 * record["N"] * record["M"]))
        self.assertNotEqual(
            Fraction(record["source_dual_coefficient_square"]), aggregate
        )

    def test_strict_native_windows_reject_a_valid_but_wrong_prime(self):
        panel = dict(S.PANELS[52])
        panel["ell"] = panel["rho"]
        with self.assertRaisesRegex(ValueError, "strict source window"):
            S.panel_record(52, panel)
        with self.assertRaises(ValueError):
            S.panel_record(True, S.PANELS[52])

    def test_canonical_fixture_comparison_preserves_numeric_types(self):
        for alternate in (True, 1.0):
            self.assertNotEqual(S.canonical({"n": 1}), S.canonical({"n": alternate}))
        with self.assertRaises(ValueError):
            S.canonical({"n": float("nan")})

    def test_source_manifest_does_not_authenticate_its_own_claimed_hash(self):
        manifest = {
            "schema": "riemann.subcritical_boolean.sources.v1",
            "sources": [
                {"commit": commit, "path": path, "git_blob": blob}
                for (commit, path), blob in S.SOURCES.items()
            ],
        }
        manifest["sources"][0]["git_blob"] = "0" * 40
        with (
            patch.object(
                Path, "read_bytes", return_value=json.dumps(manifest).encode()
            ),
            self.assertRaisesRegex(ValueError, "manifest blob mismatch"),
        ):
            S.authenticate_sources()


if __name__ == "__main__":
    unittest.main()
