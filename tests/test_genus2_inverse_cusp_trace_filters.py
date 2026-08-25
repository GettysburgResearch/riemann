"""Focused tests for exact inverse-designed genus-two cusp-trace filters."""

from __future__ import annotations

import json
import math
import subprocess
import sys
import unittest
from fractions import Fraction
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import genus2_inverse_cusp_trace_filters as subject


class InverseCuspTraceFilterAlgebraTests(unittest.TestCase):
    def test_exact_trace_coordinates(self) -> None:
        self.assertEqual(subject.trace_coordinates((1, 0, 0, 0)), (0, 1, -1))
        self.assertEqual(subject.trace_coordinates((0, 1, 0, 0)), (0, 0, -3))
        self.assertEqual(subject.trace_coordinates((0, 0, 1, 0)), (0, 0, -4))
        self.assertEqual(subject.trace_coordinates((0, 0, 0, 1)), (-1, -1, -6))
        self.assertEqual(subject.trace_coordinates((3, -7, 0, 3)), (-3, 0, 0))
        self.assertEqual(subject.trace_coordinates((4, 0, -7, 4)), (-4, 0, 0))

    def test_integral_lattice_parametrization_and_inverse(self) -> None:
        for m in range(-20, 21):
            for k in range(-20, 21):
                coefficients = subject.lattice_solution(m, k)
                self.assertEqual(subject.trace_coordinates(coefficients), (-m, 0, 0))
                self.assertEqual(subject.lattice_parameters(coefficients), (m, k))
        with self.assertRaises(ValueError):
            subject.lattice_parameters((1, 2, 3, 4))

    def test_no_two_scale_cusp_response_and_sparse_classification(self) -> None:
        for m in range(-30, 31):
            for k in range(-30, 31):
                coefficients = subject.lattice_solution(m, k)
                if subject.support_size(coefficients) <= 2:
                    self.assertEqual(m, 0)
                    self.assertEqual(coefficients, (0, -4 * k, 3 * k, 0))
        primitive_three_scale = set()
        for m in range(-30, 31):
            for k in range(-30, 31):
                coefficients = subject.lattice_solution(m, k)
                if (
                    m != 0
                    and subject.support_size(coefficients) == 3
                    and abs(math.gcd(*coefficients)) == 1
                ):
                    if coefficients[0] < 0:
                        coefficients = tuple(-value for value in coefficients)
                    primitive_three_scale.add(coefficients)
        self.assertEqual(
            primitive_three_scale,
            {(3, -7, 0, 3), (4, 0, -7, 4)},
        )

    def test_exact_haar_variances_and_sparse_comparison(self) -> None:
        f4 = tuple(Fraction(value) for value in (3, -7, 0, 3))
        f6 = tuple(Fraction(value) for value in (4, 0, -7, 4))
        for q in (3, 5, 7, 9, 101):
            self.assertEqual(
                subject.haar_variance(f4, q),
                9 * q**8 + 49 * q**4 + 9 * q**2,
            )
            self.assertEqual(
                subject.haar_variance(f6, q),
                16 * q**8 + 49 * q**6 + 16 * q**2,
            )
            f4_unit = subject.haar_variance(tuple(value / 3 for value in f4), q)
            f6_unit = subject.haar_variance(tuple(value / 4 for value in f6), q)
            self.assertEqual(
                f6_unit - f4_unit,
                Fraction(49 * q**4 * (9 * q**2 - 16), 144),
            )
            self.assertGreater(f6_unit, f4_unit)

    def test_rational_haar_optimum_and_completion_of_square(self) -> None:
        trial_values = (
            Fraction(-11),
            Fraction(-7, 3),
            Fraction(0),
            Fraction(13, 5),
        )
        for q in (3, 5, 7, 9):
            optimum = subject.optimal_unit_response_coefficients(q)
            self.assertEqual(optimum[0], 1)
            self.assertEqual(optimum[3], 1)
            self.assertEqual(3 * optimum[1] + 4 * optimum[2], -7)
            optimal_variance = subject.haar_variance(optimum, q)
            self.assertEqual(
                optimal_variance,
                subject.optimal_unit_response_variance(q),
            )
            delta = 9 * q**2 + 16
            for c4 in trial_values:
                c6 = Fraction(-7 - 3 * c4, 4)
                trial = (Fraction(1), c4, c6, Fraction(1))
                difference = subject.haar_variance(trial, q) - optimal_variance
                self.assertEqual(
                    difference,
                    Fraction(q**4 * delta, 16) * (c4 + Fraction(21 * q**2, delta)) ** 2,
                )
                self.assertGreaterEqual(difference, 0)

    def test_integral_unit_response_optimum(self) -> None:
        for q in (3, 5, 7, 9, 101):
            baseline = (Fraction(1), Fraction(-1), Fraction(-1), Fraction(1))
            baseline_variance = subject.haar_variance(baseline, q)
            self.assertEqual(
                baseline_variance,
                q**8 + q**6 + q**4 + q**2,
            )
            for k in range(-20, 21):
                coefficients = tuple(
                    Fraction(value) for value in subject.lattice_solution(1, k)
                )
                difference = subject.haar_variance(coefficients, q) - baseline_variance
                expected = q**4 * k * ((8 - 6 * q**2) + (16 + 9 * q**2) * k)
                self.assertEqual(difference, expected)
                self.assertEqual(difference == 0, k == 0)

    def test_four_root_and_isolated_hecke_recurrences(self) -> None:
        for p, a_p in ((3, 12), (5, -210), (7, 1016)):
            theta = subject.hecke_trace_tower(p, a_p, 12)
            cusp = tuple(-3 * value for value in theta)
            for exponent in range(2, len(theta)):
                self.assertEqual(
                    theta[exponent],
                    a_p * theta[exponent - 1] - p**7 * theta[exponent - 2],
                )
                self.assertEqual(
                    cusp[exponent],
                    a_p * cusp[exponent - 1] - p**7 * cusp[exponent - 2],
                )
            raw = tuple(-theta[r] - p**r - 6 for r in range(len(theta)))
            polynomial = subject.raw_trace_recurrence_polynomial(p, a_p)
            self.assertEqual(
                subject._recurrence_residual(raw, polynomial),
                (0,) * (len(raw) - 4),
            )
        theta_three = subject.hecke_trace_tower(3, 12, 2)
        self.assertEqual(theta_three, (2, 12, -4230))
        self.assertEqual(-theta_three[2] - 3**2 - 6, 4215)


class InverseCuspTraceFilterFixtureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()

    def test_locked_held_out_diagnostics(self) -> None:
        expected = {
            3: ((75, 0, 87), -216, [85916, 3], 3672, [-17, 1]),
            5: (
                (1300, 0, 1200),
                12600,
                [1672701534, 625],
                102500,
                [1025, 126],
            ),
            7: (
                (7434, 0, 6972),
                -128016,
                [4844515276200, 117649],
                2535456,
                [-7546, 381],
            ),
        }
        for row in self.fixture["held_out_F4_diagnostics"]:
            signs, total, variance, stratum_total, ratio = expected[row["q"]]
            self.assertEqual(
                (
                    row["sign_counts"]["negative"],
                    row["sign_counts"]["zero"],
                    row["sign_counts"]["positive"],
                ),
                signs,
            )
            self.assertEqual(row["observed_total_F4"], total)
            self.assertEqual(row["theorem_total_F4"], total)
            self.assertEqual(row["family_centered_variance_F4"], variance)
            self.assertEqual(
                row["zero_stratum"]["signed_total_F4"],
                stratum_total,
            )
            self.assertEqual(
                row["zero_stratum"]["ratio_to_full_signed_total"],
                ratio,
            )

    def test_source_locks_and_resource_caps(self) -> None:
        self.assertTrue(subject.source_locks_ready())
        manifest = self.fixture["source_manifest"]
        for name, lock in subject.SOURCE_LOCKS.items():
            self.assertEqual(
                subject._lf_sha256(lock["path"]),
                manifest[name]["sha256_lf_normalized"],
            )
            parsed = json.loads(lock["path"].read_text(encoding="utf-8"))
            payload = dict(parsed)
            claimed = payload.pop("payload_sha256")
            self.assertEqual(claimed, manifest[name]["payload_sha256"])
            self.assertEqual(claimed, subject._canonical_sha256(payload))
        resources = self.fixture["resource_contract"]
        self.assertEqual(resources["new_finite_fields_enumerated"], 0)
        self.assertEqual(resources["new_curves_enumerated"], 0)
        self.assertLessEqual(
            resources["actual_source_atoms"],
            resources["maximum_source_atoms"],
        )
        self.assertLessEqual(
            resources["actual_recurrence_updates"],
            resources["maximum_recurrence_updates"],
        )
        self.assertLessEqual(
            resources["actual_lattice_regression_points"],
            resources["maximum_lattice_regression_points"],
        )
        self.assertEqual(resources["actual_source_atoms"], 251)
        self.assertEqual(resources["actual_recurrence_updates"], 8 * 251 + 21)
        self.assertTrue(
            resources["held_out_source_parsed_only_after_theorem_certificates"]
        )

    def test_incomplete_source_locks_fail_closed(self) -> None:
        with mock.patch.dict(subject.SOURCE_LOCKS["sym8"], {"lf": ""}):
            self.assertFalse(subject.source_locks_ready())
            with self.assertRaisesRegex(RuntimeError, "source locks"):
                subject._load_sources(subject.THEOREM_SOURCE_NAMES)

    def test_incomplete_control_lock_does_not_gate_theorem_sources(self) -> None:
        with mock.patch.dict(subject.SOURCE_LOCKS["balanced"], {"lf": ""}):
            self.assertFalse(subject.source_locks_ready())
            theorem_sources = subject._load_sources(subject.THEOREM_SOURCE_NAMES)
            self.assertEqual(set(theorem_sources), set(subject.THEOREM_SOURCE_NAMES))
            with self.assertRaisesRegex(RuntimeError, "source locks"):
                subject._load_sources(subject.HELD_OUT_SOURCE_NAMES)

    def test_theorem_and_held_out_source_ordering(self) -> None:
        events: list[tuple[str, tuple[str, ...] | None]] = []
        original_load = subject._load_sources
        original_classification = subject._classification_certificate
        original_haar = subject._haar_certificate
        original_spectroscopy = subject._spectroscopy_certificate

        def observed_load(names: tuple[str, ...]) -> dict[str, dict[str, object]]:
            events.append(("load", names))
            return original_load(names)

        def observed_classification() -> dict[str, object]:
            result = original_classification()
            events.append(("classification_closed", None))
            return result

        def observed_haar() -> dict[str, object]:
            result = original_haar()
            events.append(("haar_closed", None))
            return result

        def observed_spectroscopy(
            controls: dict[int, int],
        ) -> dict[str, object]:
            result = original_spectroscopy(controls)
            events.append(("spectroscopy_closed", None))
            return result

        with (
            mock.patch.object(subject, "_load_sources", side_effect=observed_load),
            mock.patch.object(
                subject,
                "_classification_certificate",
                side_effect=observed_classification,
            ),
            mock.patch.object(
                subject,
                "_haar_certificate",
                side_effect=observed_haar,
            ),
            mock.patch.object(
                subject,
                "_spectroscopy_certificate",
                side_effect=observed_spectroscopy,
            ),
        ):
            subject.build_fixture()

        theorem_load = ("load", subject.THEOREM_SOURCE_NAMES)
        held_out_load = ("load", subject.HELD_OUT_SOURCE_NAMES)
        self.assertEqual(events.count(theorem_load), 1)
        self.assertEqual(events.count(held_out_load), 1)
        self.assertLess(
            events.index(theorem_load), events.index(("classification_closed", None))
        )
        self.assertLess(
            events.index(("classification_closed", None)),
            events.index(("haar_closed", None)),
        )
        self.assertLess(
            events.index(("haar_closed", None)),
            events.index(("spectroscopy_closed", None)),
        )
        self.assertLess(
            events.index(("spectroscopy_closed", None)), events.index(held_out_load)
        )

    def test_resource_caps_fail_before_over_budget_work(self) -> None:
        with (
            mock.patch.object(subject, "LATTICE_REGRESSION_RADIUS", 20),
            self.assertRaisesRegex(RuntimeError, "lattice-regression"),
        ):
            subject._classification_certificate()

        atom = {"a_D": 0, "b_D": 0, "member_count": 1}
        row = {
            "q": 3,
            "member_count": 1,
            "joint_a_D_b_D_law": {"atoms": [atom]},
        }
        with mock.patch.object(
            subject,
            "reciprocal_coefficients",
            side_effect=AssertionError("over-budget recurrence started"),
        ):
            with self.assertRaisesRegex(RuntimeError, "source-atom"):
                subject._held_out_panel(
                    row,
                    12,
                    [0],
                    [subject.MAX_SOURCE_ATOMS],
                )
            with self.assertRaisesRegex(RuntimeError, "recurrence-update"):
                subject._held_out_panel(
                    row,
                    12,
                    [subject.MAX_RECURRENCE_UPDATES - 7],
                    [0],
                )

        oversized = [
            {"joint_a_D_b_D_law": {"atoms": [atom] * (subject.MAX_SOURCE_ATOMS + 1)}}
        ]
        with self.assertRaisesRegex(RuntimeError, "source-atom"):
            subject._preflight_held_out_work(oversized, 0)
        with self.assertRaisesRegex(RuntimeError, "recurrence-update"):
            subject._preflight_held_out_work(
                [{"joint_a_D_b_D_law": {"atoms": [atom]}}],
                subject.MAX_RECURRENCE_UPDATES - 7,
            )

    def test_wall_cap_includes_payload_hashing(self) -> None:
        original_hash = subject._canonical_sha256
        state = {"payload_hashed": False}

        def observed_hash(value: object) -> str:
            result = original_hash(value)
            if isinstance(value, dict) and value.get("schema") == (
                "riemann.function_field.genus2_inverse_cusp_trace_filters.v1"
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

    def test_firewalls_remain_explicit(self) -> None:
        text = " ".join(self.fixture["firewalls"])
        self.assertIn("does not re-prove those source theorems", text)
        self.assertIn("not the finite arithmetic-family variance", text)
        self.assertIn("no memberwise sign claim", text)
        self.assertIn("No RH, GRH, novelty, motive", text)

    def test_fixture_hash_and_normal_optimized_cli_replay(self) -> None:
        stored = json.loads(subject.OUTPUT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(stored, self.fixture)
        payload = dict(stored)
        claimed = payload.pop("payload_sha256")
        self.assertEqual(claimed, subject._canonical_sha256(payload))
        for optimization in ([], ["-O"]):
            process = subprocess.run(
                [
                    sys.executable,
                    *optimization,
                    str(Path(subject.__file__)),
                    "--check",
                ],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
                timeout=10,
            )
            self.assertEqual(process.returncode, 0, process.stderr)
            self.assertIn(
                "inverse cusp-trace filter fixture matches",
                process.stdout,
            )


if __name__ == "__main__":
    unittest.main()
