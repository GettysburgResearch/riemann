"""True masked gauge inversion, exact source support, and prime-certificate guards."""

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
    / "ratio_masked_principal_gauge_inverse_barrier.py"
)
SPEC = importlib.util.spec_from_file_location("ratio_masked_inverse", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class RatioMaskedInverseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(M.CERTIFICATES.read_text(encoding="utf-8"))
        cls.r, cls.s, cls.big, cls.t = M.certificate_panel(cls.data)
        cls.panel = M.panel_matrices(cls.r, cls.s, cls.big, cls.t)

    def test_all_64_native_records_have_exactly_segre_ratio_support(self):
        horizon, cutoff, records, selected, _, _ = self.panel
        self.assertEqual(len(records), 64)
        self.assertEqual(len(selected), 20)
        for row in records:
            self.assertLessEqual(max(row["N"], row["M"]), horizon)
            self.assertLess(4 * row["g"], cutoff**2)
            self.assertEqual(
                Fraction(1, 8) < Fraction(row["ratio"]) < 8,
                row["ranks"][0] == row["ranks"][1],
            )

    def test_true_inverse_includes_the_source_gauge_activity(self):
        _, _, _, _, matrix, inverse = self.panel
        self.assertEqual(M.multiply(matrix, inverse), M.identity(20))
        self.assertEqual(M.multiply(inverse, matrix), M.identity(20))
        self.assertEqual(matrix[-1][0], Fraction(1, 16**6))
        self.assertEqual(inverse[-1][0], Fraction(-19, 16**6))
        self.assertLess(abs(inverse[-1][0]), 1)

    def test_principal_common_core_weight_pays_reciprocal_primes_exactly(self):
        _, _, _, selected, matrix, _ = self.panel
        start, end = selected[0], selected[-1]
        self.assertEqual(end["g"], self.t)
        self.assertEqual(start["g"], 1)
        self.assertEqual(Fraction(end["weight"]) / Fraction(start["weight"]), self.t**2)
        raw = M.A_TAU**6 / self.t
        self.assertEqual(raw * self.t, matrix[-1][0])

    def test_complete_boolean_allocations_include_empty_and_composite_groups(self):
        _, cutoff, _, selected, _, _ = self.panel
        for row in (selected[0], selected[-1]):
            for side in ("left", "right"):
                result = M.boolean_histories(tuple(row[side]), cutoff)
                self.assertEqual(len(result["histories"]), 2)
                self.assertEqual(abs(result["balanced"]), 2)
                self.assertEqual(result["complete_allocations"], 3 ** len(row[side]))

    def test_same_unchanged_width_eight_shell_has_only_identity_transition(self):
        _, _, _, selected, matrix, _ = self.panel
        start = selected[0]
        retained = [
            i
            for i, row in enumerate(selected)
            if start["N"] <= row["N"] < 8 * start["N"]
            and start["M"] <= row["M"] < 8 * start["M"]
        ]
        self.assertEqual(retained, [0])
        self.assertEqual(matrix[0][0], 1)

    def test_classical_mobius_values_and_independent_permutation_counts(self):
        mu = M.segre_mu(4)
        self.assertEqual(mu, [1, -1, 3, -19, 211])
        for m in range(1, 5):
            self.assertEqual(M.no_common_ascent_count(m), (-1) ** m * mu[m])

    def test_factorial_lower_bound_really_overcomes_all_gauge_activity(self):
        mu = M.segre_mu(64)
        lower = Fraction(M.factorial(64) ** 2, 2**63 * 16**128)
        self.assertGreater(lower, 1)
        self.assertGreaterEqual(Fraction(abs(mu[64]), 16**128), lower)

    def test_proth_certificates_are_verified_not_probable_prime_flags(self):
        for key in ("A", "B", "C", "D"):
            record = self.data["backgrounds"][key]
            self.assertEqual(M.proth_certificate(record), self.big[key])
            bad = dict(record)
            bad["prime"] += 2
            with self.assertRaises(ValueError):
                M.proth_certificate(bad)
            bad = dict(record)
            bad["witness"] = 1
            with self.assertRaises(ValueError):
                M.proth_certificate(bad)

    def test_resource_caps_and_bool_float_substitutions_fail_closed(self):
        for value in (True, 3.0, 65):
            with self.subTest(value=value), self.assertRaises(ValueError):
                M.segre_mu(value)
        with self.assertRaises(ValueError):
            M.no_common_ascent_count(5)
        with self.assertRaises(ValueError):
            M.identity(33)
        with self.assertRaises(ValueError):
            M.boolean_histories(tuple(range(2, 12)), 100)
        bad = json.loads(json.dumps(self.data))
        bad["m"] = True
        with self.assertRaises(ValueError):
            M.certificate_panel(bad)

    def test_source_authentication_and_strict_json_acceptance(self):
        first = type("Size", (), {"stdout": "3"})()
        second = type("Bytes", (), {"stdout": b"bad"})()
        with (
            patch.object(M.subprocess, "run", side_effect=[first, second]),
            self.assertRaisesRegex(ValueError, "Git blob"),
        ):
            M.source_bytes(next(iter(M.SOURCES)))
        self.assertNotEqual(M.canonical({"n": 1}), M.canonical({"n": True}))
        self.assertNotEqual(M.canonical({"n": 1}), M.canonical({"n": 1.0}))
        with self.assertRaises(ValueError):
            M.canonical({"n": float("nan")})


if __name__ == "__main__":
    unittest.main()
