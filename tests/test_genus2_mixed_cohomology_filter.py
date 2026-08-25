"""Focused tests for the exact genus-two mixed-cohomology filter packet."""

from __future__ import annotations

import json
import subprocess
import sys
import unittest
from fractions import Fraction
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import genus2_mixed_cohomology_filter as subject


class MixedCohomologyFilterAlgebraTests(unittest.TestCase):
    def test_imported_trace_coordinates(self) -> None:
        expected = {
            4: (0, 0, 0, 0, 0, -3),
            6: (0, 0, 0, 0, 0, -4),
            8: (0, 0, -1, 0, -1, -6),
            10: (1, -1, -1, -1, -1, -7),
        }
        for index, weight in enumerate(subject.WEIGHTS):
            coefficients = tuple(1 if position == index else 0 for position in range(4))
            self.assertEqual(
                subject.trace_coordinates(coefficients),
                tuple(Fraction(value) for value in expected[weight]),
            )

    def test_complete_integral_lattice_and_inverse(self) -> None:
        for m in range(-20, 21):
            for k in range(-20, 21):
                coefficients = subject.lattice_solution(m, k)
                self.assertEqual(subject.lattice_parameters(coefficients), (m, k))
                self.assertEqual(
                    subject.trace_coordinates(coefficients),
                    tuple(Fraction(value) for value in (m, -m, 0, -m, 0, 0)),
                )
        with self.assertRaises(ValueError):
            subject.lattice_parameters((1, 2, 3, 4))
        with self.assertRaises(TypeError):
            subject.lattice_solution(1, Fraction(1, 2))  # type: ignore[arg-type]

    def test_sparse_filters_and_r2_exclusion(self) -> None:
        fixture = subject._classification_certificate(subject.ResourceGuard())
        sparse = fixture["primitive_three_scale_mixed_filters"]
        self.assertEqual(sparse["M4"]["coefficients"], [-1, 0, -3, 3])
        self.assertEqual(sparse["M6"]["coefficients"], [0, -1, -4, 4])
        self.assertEqual(
            fixture["only_primitive_support_at_most_two"]["coefficients"],
            [4, -3, 0, 0],
        )
        self.assertIn("forces c_2=0", fixture["r2_extension"])

    def test_integral_and_rational_haar_minima(self) -> None:
        baseline = tuple(Fraction(value) for value in (1, -1, -1, 1))
        for q in (3, 5, 7, 9, 101):
            baseline_variance = subject.haar_variance(baseline, q)
            self.assertEqual(baseline_variance, q**10 + q**8 + q**6 + q**4)
            for k in range(-20, 21):
                trial = tuple(Fraction(value) for value in subject.lattice_solution(1, k))
                difference = subject.haar_variance(trial, q) - baseline_variance
                expected = q**4 * k * (
                    (8 + 6 * q * q) + (16 + 9 * q * q) * k
                )
                self.assertEqual(difference, expected)
                self.assertEqual(difference == 0, k == 0)

            optimum = subject.optimal_unit_response_coefficients(q)
            denominator = 9 * q * q + 16
            self.assertEqual(
                optimum,
                (
                    Fraction(-3 * q * q, denominator),
                    Fraction(-4, denominator),
                    Fraction(-1),
                    Fraction(1),
                ),
            )
            self.assertEqual(
                subject.haar_variance(optimum, q),
                subject.optimal_unit_response_variance(q),
            )
            self.assertEqual(
                subject.optimal_unit_response_variance(q),
                Fraction(q**10 + q**8) + Fraction(q**6, denominator),
            )

    def test_sparse_haar_comparison(self) -> None:
        m4 = tuple(Fraction(value, 3) for value in (-1, 0, -3, 3))
        m6 = tuple(Fraction(value, 4) for value in (0, -1, -4, 4))
        for q in (3, 5, 7, 9, 101):
            difference = subject.haar_variance(m6, q) - subject.haar_variance(m4, q)
            self.assertEqual(difference, Fraction(q**4 * (9 * q * q - 16), 144))
            self.assertGreater(difference, 0)

    def test_six_root_recurrence_and_three_isolators(self) -> None:
        sources = subject._load_sources(subject.SOURCE_NAMES, subject.ResourceGuard())
        controls = subject._coefficient_controls(sources)
        for prime, (tau, g_value) in controls.items():
            guard = subject.ResourceGuard()
            delta = subject.power_sum_tower(tau, prime**11, 18, guard)
            level2_tower = subject.power_sum_tower(g_value, prime**9, 18, guard)
            shifted = tuple(prime**r * delta[r] for r in range(len(delta)))
            unshifted = tuple(-value for value in delta)
            level2 = tuple(-value for value in level2_tower)
            response = tuple(
                shifted[r] + unshifted[r] + level2[r] for r in range(len(delta))
            )

            p_shift = subject.quadratic_operator(prime * tau, prime**13)
            p_unshift = subject.quadratic_operator(tau, prime**11)
            p_level2 = subject.quadratic_operator(g_value, prime**9)
            annihilator = subject.polynomial_multiply(
                subject.polynomial_multiply(p_shift, p_unshift), p_level2
            )
            self.assertTrue(all(value == 0 for value in subject.recurrence_residual(response, annihilator)))

            cases = (
                (shifted, subject.polynomial_multiply(p_unshift, p_level2), p_shift),
                (unshifted, subject.polynomial_multiply(p_shift, p_level2), p_unshift),
                (level2, subject.polynomial_multiply(p_shift, p_unshift), p_level2),
            )
            for component, isolator, recurrence in cases:
                isolated = subject.apply_operator(response, isolator)
                self.assertEqual(isolated, subject.apply_operator(component, isolator))
                self.assertTrue(any(isolated))
                self.assertTrue(
                    all(value == 0 for value in subject.recurrence_residual(isolated, recurrence))
                )


class MixedCohomologyFilterFixtureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()
        cls.disk = json.loads(subject.OUTPUT_PATH.read_text(encoding="utf-8"))

    def test_fixture_is_canonical(self) -> None:
        self.assertEqual(self.fixture, self.disk)
        payload = dict(self.fixture)
        claimed = payload.pop("payload_sha256")
        self.assertEqual(claimed, subject._canonical_sha256(payload))

    def test_source_locks_and_full_commits(self) -> None:
        self.assertTrue(subject.source_locks_ready())
        manifest = {row["id"]: row for row in self.fixture["source_manifest"]}
        self.assertEqual(set(manifest), set(subject.SOURCE_NAMES))
        for name, lock in subject.SOURCE_LOCKS.items():
            self.assertEqual(len(manifest[name]["commit"]), 40)
            self.assertEqual(subject._lf_sha256(lock["path"]), lock["lf"])
            parsed = json.loads(lock["path"].read_text(encoding="utf-8"))
            payload = dict(parsed)
            claimed = payload.pop("payload_sha256")
            self.assertEqual(claimed, lock["payload"])
            self.assertEqual(claimed, subject._canonical_sha256(payload))

    def test_packet_manifest_is_current(self) -> None:
        roles = set()
        for row in self.fixture["packet_manifest"]:
            path = ROOT / row["path"]
            self.assertTrue(path.is_file())
            self.assertEqual(row["sha256_lf_normalized"], subject._lf_sha256(path))
            roles.add(row["role"])
        self.assertEqual(
            roles,
            {"exact producer", "proof note", "focused regression tests"},
        )

    def test_source_and_work_caps_fail_before_over_budget_work(self) -> None:
        with (
            mock.patch.object(subject, "MAX_SOURCE_BYTES", 0),
            mock.patch.object(
                Path,
                "read_bytes",
                side_effect=AssertionError("over-budget source read started"),
            ),
            self.assertRaisesRegex(RuntimeError, "source-byte"),
        ):
            subject._load_sources(subject.SOURCE_NAMES, subject.ResourceGuard())

        with (
            mock.patch.object(subject, "LATTICE_REGRESSION_RADIUS", 20),
            self.assertRaisesRegex(RuntimeError, "lattice-regression"),
        ):
            subject._classification_certificate(subject.ResourceGuard())

        with self.assertRaisesRegex(ValueError, "tower exponent"):
            subject.power_sum_tower(1, 3, subject.MAX_TOWER_EXPONENT + 1, subject.ResourceGuard())

    def test_incomplete_source_locks_fail_closed(self) -> None:
        with mock.patch.dict(subject.SOURCE_LOCKS["sym10"], {"lf": ""}):
            self.assertFalse(subject.source_locks_ready())
            with self.assertRaisesRegex(RuntimeError, "source locks"):
                subject._load_sources(subject.SOURCE_NAMES, subject.ResourceGuard())

    def test_output_cap_fails_before_output_read(self) -> None:
        with (
            mock.patch.object(subject, "MAX_OUTPUT_BYTES", 0),
            mock.patch.object(
                Path,
                "read_text",
                side_effect=AssertionError("over-budget output read started"),
            ),
            self.assertRaisesRegex(RuntimeError, "output-byte"),
        ):
            subject.check_fixture()

    def test_wall_cap_includes_final_payload_hash(self) -> None:
        original_hash = subject._canonical_sha256
        state = {"payload_hashed": False}

        def observed_hash(value: object) -> str:
            result = original_hash(value)
            if isinstance(value, dict) and value.get("schema") == (
                "riemann.function_field.genus2_mixed_cohomology_filter.v1"
            ):
                state["payload_hashed"] = True
            return result

        def observed_clock() -> float:
            return subject.MAX_WALL_SECONDS + 1 if state["payload_hashed"] else 0

        with (
            mock.patch.object(subject, "_canonical_sha256", side_effect=observed_hash),
            mock.patch.object(subject.time, "monotonic", side_effect=observed_clock),
            self.assertRaisesRegex(RuntimeError, "wall cap"),
        ):
            subject.build_fixture()

    def test_resource_contract_and_firewalls(self) -> None:
        resources = self.fixture["resource_contract"]
        for prefix in (
            "source_files",
            "source_bytes",
            "packet_bytes",
            "exact_operations",
            "lattice_regression_points",
            "recurrence_steps",
        ):
            self.assertLessEqual(resources[f"actual_{prefix}"], resources[f"maximum_{prefix}"])
        self.assertEqual(resources["actual_source_files"], 4)
        self.assertEqual(resources["actual_lattice_regression_points"], 625)
        self.assertEqual(self.fixture["scope"]["new_finite_fields_enumerated"], [])
        text = " ".join(self.fixture["firewalls"])
        self.assertIn("not a memberwise sign theorem", text)
        self.assertIn("same-prime", text)
        self.assertIn("No RH, GRH", text)

    def test_three_channel_isolators_are_recorded(self) -> None:
        spectroscopy = self.fixture["frobenius_interferometry_certificate"]
        self.assertIn("r>=1", spectroscopy["same_prime_response"])
        self.assertIn("C_0=-2", spectroscopy["formal_initialization"])
        self.assertEqual(
            spectroscopy["exact_channel_isolators"],
            {
                "shifted_Delta": "P_unshift(E)*P_10_2(E)",
                "unshifted_Delta": "P_shift(E)*P_10_2(E)",
                "level_2_weight_10": "P_shift(E)*P_unshift(E)",
            },
        )
        self.assertTrue(
            all(row["all_recurrence_residuals_zero"] for row in spectroscopy["prime_controls"])
        )
        premise = self.fixture["external_mathematical_premises"][0]
        self.assertIn("Deligne purity", premise["premise"])
        self.assertIn("do not require purity", premise["role"])

    def test_normal_and_optimized_cli_replay(self) -> None:
        for optimization in ([], ["-O"]):
            process = subprocess.run(
                [sys.executable, *optimization, str(subject.SCRIPT_PATH), "--check"],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
                timeout=10,
            )
            self.assertEqual(process.returncode, 0, process.stderr)
            self.assertIn("mixed-cohomology filter fixture matches", process.stdout)


if __name__ == "__main__":
    unittest.main()
