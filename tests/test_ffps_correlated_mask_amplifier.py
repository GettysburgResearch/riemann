"""Focused exact tests for the FFPS correlated-mask amplifier packet."""

from __future__ import annotations

import ast
import hashlib
import importlib.util
import json
import sys
import tempfile
import time
import unittest
from fractions import Fraction
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_correlated_mask_amplifier.py"
)
OUTPUT_PATH = MODULE_PATH.with_suffix(".json")

SPEC = importlib.util.spec_from_file_location(
    "ffps_correlated_mask_amplifier", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load FFPS correlated-mask producer")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class FFPSCorrelatedMaskAmplifierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = MODULE.build_fixture()
        cls.disk = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))

    def test_fixture_is_canonical_and_payload_locked(self) -> None:
        self.assertEqual(self.fixture, self.disk)
        payload = dict(self.fixture)
        claimed = payload.pop("payload_sha256")
        self.assertEqual(claimed, MODULE._canonical_sha256(payload))
        self.assertEqual(
            self.fixture["status"],
            "EXACT_FORMAL_CORRELATED_RESTRICTED_GRAM_OPTIMIZATION",
        )

    def test_restricted_optimizer_is_sharp_and_unique(self) -> None:
        guard = MODULE.ResourceGuard()
        gram = MODULE.tensor_gram((2, 3), guard)
        support = (0, 2, 3, 4)
        result = MODULE.restricted_optimizer(gram, support, 6, guard)
        self.assertEqual(result["denominator_1_G_A_1"], [74, 1])
        self.assertEqual(result["dual_energy"], [18, 37])
        self.assertEqual(
            result["weights_N_G_A_1_over_E"],
            [[45, 37], [66, 37], [45, 37], [66, 37]],
        )

        restricted = MODULE.principal_submatrix(gram, support, guard)
        inverse = MODULE.invert_matrix(restricted, guard)
        optimum = tuple(Fraction(*value) for value in result["weights_N_G_A_1_over_E"])
        moved = list(optimum)
        moved[0] += Fraction(1, 7)
        moved[1] -= Fraction(1, 7)
        self.assertEqual(sum(moved), 6)
        self.assertGreater(
            MODULE.quadratic_form(inverse, moved, guard),
            Fraction(18, 37),
        )

    def test_two_prime_energy_and_balanced_fixed_size_frontier(self) -> None:
        for row_count, column_count in ((2, 3), (2, 4), (3, 3)):
            audit = MODULE.exhaustive_two_prime_audit(
                row_count, column_count, MODULE.ResourceGuard()
            )
            self.assertEqual(audit["subsets_checked"], 2 ** (row_count * column_count))
            for size in range(1, row_count * column_count + 1):
                support = MODULE.balanced_support(
                    row_count, column_count, size, MODULE.ResourceGuard()
                )
                self.assertEqual(
                    MODULE.two_prime_support_energy(row_count, column_count, support),
                    MODULE.two_prime_max_denominator(row_count, column_count, size),
                )

        self.assertEqual(MODULE.balanced_square_sum(5, 13), 35)
        self.assertEqual(MODULE.balanced_square_sum(3, 8), 22)

    def test_matching_gain_and_every_distinct_prime_pair(self) -> None:
        for row_count in range(2, 7):
            for column_count in range(2, 7):
                if row_count == column_count:
                    continue
                full = MODULE.two_prime_support_energy(
                    row_count,
                    column_count,
                    MODULE.full_grid_minus_matching(row_count, column_count, 0),
                )
                matched = MODULE.two_prime_support_energy(
                    row_count,
                    column_count,
                    MODULE.full_grid_minus_matching(row_count, column_count, 2),
                )
                self.assertEqual(
                    matched - full,
                    MODULE.matching_energy_gain(row_count, column_count, 2),
                )
                self.assertGreater(matched, full)

        example = self.fixture["exact_mathematics"]["five_seven_example"]
        self.assertEqual(example["full_denominator"], 72)
        self.assertEqual(example["restricted_denominator"], 74)
        self.assertEqual(example["restricted_leverage"], [18, 37])
        self.assertLess(Fraction(18, 37), Fraction(1, 2))

    def test_two_prime_asymptotic_controls_approach_two_thirds_three_fourths(
        self,
    ) -> None:
        controls = self.fixture["exact_mathematics"]["finite_controls"][
            "asymptotic_two_prime"
        ]
        previous_density_error = None
        previous_leverage_error = None
        for row in controls:
            density = Fraction(*row["best_density"][0])
            leverage = Fraction(*row["best_dual_energy"])
            density_error = abs(density - Fraction(2, 3))
            leverage_error = abs(leverage - Fraction(3, 4))
            if previous_density_error is not None:
                self.assertLessEqual(density_error, previous_density_error)
                self.assertLess(leverage_error, previous_leverage_error)
            previous_density_error = density_error
            previous_leverage_error = leverage_error

    def test_random_fixed_size_expectation_and_fractional_refusal(self) -> None:
        for dimensions in ((2, 3), (2, 2, 2)):
            audit = MODULE.exhaustive_expected_energy_audit(
                dimensions, MODULE.ResourceGuard()
            )
            for row in audit["rows"]:
                self.assertTrue(row["some_mask_at_least_expectation"])
                self.assertLessEqual(
                    row["minimum_energy"], Fraction(*row["expected_energy"])
                )
                self.assertGreaterEqual(
                    row["maximum_energy"], Fraction(*row["expected_energy"])
                )

        expected = MODULE.expected_fixed_size_energy((2, 3), 2)
        self.assertEqual(expected, Fraction(216, 5))
        refusal = self.fixture["exact_mathematics"]["arbitrary_d_expected_energy"][
            "fractional_refusal_example"
        ]
        self.assertFalse(refusal["exact_attainment"])
        self.assertTrue(refusal["individual_energies_are_integers"])

    def test_fixed_d_limit_constants(self) -> None:
        expected = {
            1: (Fraction(1), Fraction(1)),
            2: (Fraction(2, 3), Fraction(3, 4)),
            3: (Fraction(4, 7), Fraction(7, 16)),
            4: (Fraction(8, 15), Fraction(15, 64)),
            5: (Fraction(16, 31), Fraction(31, 256)),
        }
        for dimension_count, (density, leverage) in expected.items():
            self.assertEqual(MODULE.asymptotic_density(dimension_count), density)
            self.assertEqual(
                MODULE.asymptotic_leverage_bound(dimension_count), leverage
            )

    def test_legendre_pair_vectors_descend_and_balance(self) -> None:
        self.assertEqual(MODULE.legendre_pair_vector(5), (1, -1))
        self.assertEqual(MODULE.legendre_pair_vector(13), (1, -1, 1, 1, -1, -1))
        for prime in (5, 13, 17, 29):
            vector = MODULE.legendre_pair_vector(prime)
            self.assertEqual(sum(vector), 0)
            self.assertEqual(vector.count(1), len(vector) // 2)
            for representative, sign in enumerate(vector, start=1):
                opposite = prime - representative
                euler = pow(opposite, (prime - 1) // 2, prime)
                self.assertEqual(sign, 1 if euler == 1 else -1)
        with self.assertRaises(ValueError):
            MODULE.legendre_pair_vector(7)

    def test_checkerboard_is_constant_plus_top_mode_with_uniform_weights(self) -> None:
        guard = MODULE.ResourceGuard()
        control = MODULE.checkerboard_exact_audit((5, 13), guard)
        self.assertEqual(control["support_size"], 6)
        self.assertEqual(control["denominator"], [258, 1])
        self.assertEqual(control["sharp_restricted_leverage"], [24, 43])
        self.assertEqual(control["complete_tensor_leverage"], [4, 7])
        self.assertLess(Fraction(24, 43), Fraction(4, 7))
        self.assertTrue(
            all(
                weight == [2, 1]
                for weight in control["optimizer"]["weights_N_G_A_1_over_E"]
            )
        )
        retained = control["retained_canonical_pair_representatives"]
        vector_5 = MODULE.legendre_pair_vector(5)
        vector_13 = MODULE.legendre_pair_vector(13)
        for left, right in retained:
            self.assertEqual(vector_5[left - 1] * vector_13[right - 1], 1)

        three_prime = MODULE.checkerboard_closed_form((5, 13, 17))
        self.assertEqual(three_prime["sharp_restricted_leverage"], [192, 647])
        self.assertLess(Fraction(192, 647), Fraction(1, 2))

    def test_exact_half_prefix_formula_and_conductor_statements(self) -> None:
        for limit in (5, 13, 29, 43):
            primes = tuple(
                prime for prime in range(3, limit + 1) if MODULE._is_prime(prime)
            )
            row = MODULE.random_half_prefix_bound(primes)
            native = row["native_amplitude"]
            tensor_order = row["d"]
            b_value = Fraction(*row["b_B_over_N_squared"])
            expected = Fraction(*row["normalized_expected_denominator"])
            closed = (
                Fraction(2**tensor_order * native, 4 * (native - 1))
                + Fraction(native - 2, 4 * (native - 1)) * b_value
            )
            self.assertEqual(expected, closed)
            self.assertEqual(
                Fraction(*row["some_mask_leverage_upper_bound"]), 1 / expected
            )

        theorem = self.fixture["exact_mathematics"]["growing_prime_prefix_corollaries"]
        self.assertIn(
            "M^(-log 2/log log M", theorem["all_odd_primes_random_mask"]["leverage"]
        )
        self.assertIn(
            "PNT in the progression 1 mod 4",
            theorem["one_mod_four_explicit_checkerboard"]["imported_asymptotics"],
        )
        self.assertIn("subpolynomial", theorem["comparison"])

    def test_source_locks_and_live_gram_provenance(self) -> None:
        manifest = {row["id"]: row for row in self.fixture["source_manifest"]}
        self.assertEqual(set(manifest), set(MODULE.SOURCE_LOCKS))
        for name, lock in MODULE.SOURCE_LOCKS.items():
            path = lock["path"]
            self.assertIsInstance(path, Path)
            raw = path.read_bytes()
            self.assertEqual(MODULE._lf_sha256_bytes(raw), lock["lf_sha256"])
            self.assertEqual(MODULE._git_blob_sha1(raw), lock["git_blob"])
            self.assertEqual(manifest[name]["lf_sha256"], lock["lf_sha256"])
        signed = MODULE.SOURCE_LOCKS["signed_json"]
        self.assertEqual(
            signed["payload_sha256"],
            "a61fe11c49e38630762931971c573a87be1763974f9a7ee599ccf10f915c1e95",
        )
        relationship = self.fixture["source_relationship"]
        self.assertEqual(relationship["live_audited_head"], MODULE.LIVE_PR_751_HEAD)
        self.assertEqual(relationship["live_L_106024_blob"], MODULE.LIVE_L106024_BLOB)

    def test_sources_are_loaded_only_after_exact_mathematics(self) -> None:
        events: list[str] = []
        original_math = MODULE._build_exact_mathematics
        original_read = MODULE._read_locked_sources

        def observed_math(guard: object, deadline: object) -> object:
            result = original_math(guard, deadline)
            events.append("math_closed")
            return result

        def observed_read(guard: object, deadline: object) -> object:
            events.append("sources_opened")
            return original_read(guard, deadline)

        with (
            mock.patch.object(MODULE, "_build_exact_mathematics", observed_math),
            mock.patch.object(MODULE, "_read_locked_sources", observed_read),
        ):
            MODULE.build_fixture()
        self.assertEqual(events, ["math_closed", "sources_opened"])
        resources = self.fixture["resource_contract"]
        self.assertEqual(
            resources["operations_before_sources"], resources["actual_exact_operations"]
        )
        self.assertEqual(
            resources["subsets_before_sources"], resources["actual_enumerated_subsets"]
        )

    def test_caps_fail_closed_and_producer_has_no_assert_statement(self) -> None:
        guard = MODULE.ResourceGuard(exact_operations=MODULE.MAX_EXACT_OPERATIONS)
        with self.assertRaises(RuntimeError):
            guard.operation("over")
        guard = MODULE.ResourceGuard(enumerated_subsets=MODULE.MAX_ENUMERATED_SUBSETS)
        with self.assertRaises(RuntimeError):
            guard.subset()
        with self.assertRaises(RuntimeError):
            MODULE.Deadline(time.monotonic() - MODULE.MAX_WALL_SECONDS - 1).check(
                "late"
            )
        tree = ast.parse(MODULE_PATH.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(tree)))
        resources = self.fixture["resource_contract"]
        self.assertLessEqual(
            resources["actual_exact_operations"], resources["maximum_exact_operations"]
        )
        self.assertEqual(resources["actual_enumerated_subsets"], 1152)

    def test_fixture_reads_and_writes_are_byte_capped(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            oversized = Path(directory) / "oversized.json"
            oversized.write_bytes(b"x" * 129)
            with (
                mock.patch.object(MODULE, "OUTPUT_PATH", oversized),
                mock.patch.object(MODULE, "MAX_PACKET_FILE_BYTES", 128),
                mock.patch.object(MODULE, "build_fixture", return_value={"ok": 1}),
                self.assertRaisesRegex(RuntimeError, "existing fixture exceeds"),
            ):
                MODULE.main(["--check"])

            unwritten = Path(directory) / "unwritten.json"
            with (
                mock.patch.object(MODULE, "OUTPUT_PATH", unwritten),
                mock.patch.object(MODULE, "MAX_PACKET_FILE_BYTES", 8),
                mock.patch.object(
                    MODULE, "build_fixture", return_value={"too_long": "payload"}
                ),
                self.assertRaisesRegex(RuntimeError, "rendered fixture exceeds"),
            ):
                MODULE.main([])
            self.assertFalse(unwritten.exists())

    def test_firewalls_keep_fixed_tensor_separate_from_global_ffps(self) -> None:
        joined = " ".join(self.fixture["firewalls"])
        for token in ("varying owners", "WCADD", "WCKUM", "global FFPS", "RH"):
            self.assertIn(token, joined)
        checkerboard = self.fixture["exact_mathematics"]["global_legendre_checkerboard"]
        self.assertIn("fixed source-owned", self.fixture["firewalls"][1])
        self.assertIn("no signed cancellation", checkerboard["positive_optimizer"])
        self.assertIn(
            "lower-order tensor modes", checkerboard["contrast_with_product_masks"]
        )

    def test_packet_file_hashes_are_lf_normalized(self) -> None:
        manifest = self.fixture["packet_manifest"]
        for row in manifest.values():
            path = ROOT / row["path"]
            normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            self.assertEqual(hashlib.sha256(normalized).hexdigest(), row["lf_sha256"])


if __name__ == "__main__":
    unittest.main()
