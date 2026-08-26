from __future__ import annotations

import copy
import importlib.util
import json
import math
import sys
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
    / "genus2_scalar_endpoint_symmetric_power_phase_diagram.py"
)
OUTPUT_PATH = MODULE_PATH.with_suffix(".json")

SPEC = importlib.util.spec_from_file_location(
    "genus2_scalar_endpoint_symmetric_power_phase_diagram", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load scalar-endpoint phase producer")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class Genus2ScalarEndpointSymmetricPowerPhaseDiagramTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = MODULE.build_fixture()
        cls.disk = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))
        cls.theorem = cls.fixture["all_rank_theorem"]
        cls.controls = cls.theorem["exact_controls"]

    def test_fixture_and_payload_are_canonical(self) -> None:
        self.assertEqual(self.fixture, self.disk)
        payload = dict(self.fixture)
        claimed = payload.pop("payload_sha256")
        self.assertEqual(claimed, MODULE._canonical_sha256(payload))
        self.assertEqual(
            self.fixture["schema"],
            "riemann.function_field."
            "genus2_scalar_endpoint_symmetric_power_phase_diagram.v1",
        )

    def test_source_is_locked_to_the_requested_commit(self) -> None:
        manifest = self.fixture["source_manifest"]
        self.assertEqual(len(manifest), 1)
        source = manifest[0]
        self.assertEqual(source["commit"], "77c6a1b31d6d2b475df0d87e187f32d9a09479e5")
        self.assertEqual(source["git_blob"], "ce5f1baba8c33e9243ac18e381fbd4824e7a5baa")
        self.assertEqual(
            source["payload_sha256"],
            "bc2d9dcea68befbda0281ebc702b26dca805cb41676862e0c50be35ff66cf49a",
        )
        raw = MODULE.SOURCE_PATH.read_bytes()
        self.assertEqual(MODULE._git_blob_sha1(raw), source["git_blob"])
        self.assertEqual(MODULE._lf_sha256_bytes(raw), source["lf_sha256"])

    def test_dimension_formula_for_every_control_rank(self) -> None:
        expected = {0: 1, 1: 4, 2: 10, 3: 20, 4: 35, 5: 56, 10: 286, 20: 1771}
        rows = self.controls["dimension_rows"]
        self.assertEqual({row["rank"]: row["dimension"] for row in rows}, expected)
        for rank in range(101):
            self.assertEqual(
                MODULE.symmetric_power_dimension(rank), math.comb(rank + 3, 3)
            )

    def test_scalar_character_values_have_exact_rank_parity(self) -> None:
        for k in (1, 2, 7):
            sign = (-1) ** k
            for rank in range(13):
                dimension = math.comb(rank + 3, 3)
                self.assertEqual(
                    MODULE.scalar_character(rank, sign), sign**rank * dimension
                )
                self.assertEqual(
                    MODULE.scalar_character(rank, -sign), (-sign) ** rank * dimension
                )

    def test_two_orbit_absolute_and_signed_subtotals(self) -> None:
        for k in (1, 2, 4):
            q = 3 ** (4 * k)
            sign = (-1) ** k
            for rank in range(8):
                dimension = math.comb(rank + 3, 3)
                for moment in range(1, 7):
                    result = MODULE.constructed_moment_contributions(
                        rank, moment, q, sign
                    )
                    absolute = Fraction(dimension**moment, 5 * q**3)
                    signed = Fraction(0) if rank * moment % 2 else absolute
                    self.assertEqual(result["absolute"], absolute)
                    self.assertEqual(result["signed"], signed)
                    self.assertEqual(result["absolute"], result["expected_absolute"])
                    self.assertEqual(result["signed"], result["expected_signed"])

    def test_orbit_counting_reproduces_the_subtotal(self) -> None:
        for k in (1, 2, 3):
            q = 3 ** (4 * k)
            family = q**4 * (q - 1)
            each_orbit = q * (q - 1) // 10
            self.assertEqual(Fraction(each_orbit, family), Fraction(1, 10 * q**3))
            for rank, moment in ((1, 1), (1, 2), (2, 3), (10, 5)):
                dimension = math.comb(rank + 3, 3)
                absolute_sum = 2 * each_orbit * dimension**moment
                self.assertEqual(
                    Fraction(absolute_sum, family),
                    Fraction(dimension**moment, 5 * q**3),
                )

    def test_compact_bound_gives_the_recorded_mth_root_squeeze(self) -> None:
        moment = self.theorem["moment_theorem"]
        self.assertEqual(
            moment["full_absolute_moment_squeeze"],
            "d_r^m/(5*q^3)<=A_(r,m)(q)<=d_r^m",
        )
        self.assertEqual(
            moment["fixed_q_r_limit"],
            "lim_(m->infinity) A_(r,m)(q)^(1/m)=d_r",
        )

        # Exact epsilon control: if T*(a-1)^m <= a^m, then
        # T^(-1/m) >= 1-1/a.  Such an m exists for every a>=2.
        target = 5 * 81**3
        for denominator in (2, 3, 10):
            exponent = 1
            while target * (denominator - 1) ** exponent > denominator**exponent:
                exponent += 1
            self.assertLessEqual(
                target * (denominator - 1) ** exponent, denominator**exponent
            )

    def test_fixed_rank_crossovers_use_exact_integer_logs(self) -> None:
        for row in self.controls["fixed_rank_crossovers"]:
            dimension = row["dimension"]
            target = row["target_5q3"]
            floor_m = row["largest_m_with_constructed_subtotal_at_most_one"]
            next_m = row["first_m_with_constructed_subtotal_above_one"]
            self.assertEqual(next_m, floor_m + 1)
            self.assertLessEqual(dimension**floor_m, target)
            self.assertLess(target, dimension**next_m)
            below = Fraction(*row["subtotal_at_floor_m"])
            above = Fraction(*row["subtotal_at_next_m"])
            self.assertGreater(below, Fraction(1, dimension))
            self.assertLessEqual(below, 1)
            self.assertGreater(above, 1)
            self.assertLessEqual(above, dimension)

    def test_fixed_moment_crossovers_and_cubic_windows_are_exact(self) -> None:
        for row in self.controls["fixed_moment_crossovers"]:
            moment = row["moment"]
            target = row["target_5q3"]
            rank = row["largest_rank_with_constructed_subtotal_at_most_one"]
            next_rank = row["first_rank_with_constructed_subtotal_above_one"]
            self.assertEqual(next_rank, rank + 1)
            self.assertLessEqual(math.comb(rank + 3, 3) ** moment, target)
            self.assertLess(target, math.comb(next_rank + 3, 3) ** moment)

            x_floor = row["floor_of_asymptotic_scale_X"]
            scaled = 6**moment * target
            self.assertLessEqual(x_floor ** (3 * moment), scaled)
            self.assertLess(scaled, (x_floor + 1) ** (3 * moment))
            lower, upper = row["exact_rank_window"]
            self.assertLessEqual(lower, rank)
            self.assertLessEqual(rank, upper)
            self.assertLessEqual(upper - lower, 2)

    def test_sym10_is_an_exact_specialization(self) -> None:
        sym10 = self.controls["sym10_specialization"]
        self.assertEqual(sym10["dimension"], 286)
        for k in (1, 2):
            q = 3 ** (4 * k)
            for moment in (1, 2, 5):
                result = MODULE.constructed_moment_contributions(
                    10, moment, q, (-1) ** k
                )
                expected = Fraction(286**moment, 5 * q**3)
                self.assertEqual(result["absolute"], expected)
                self.assertEqual(result["signed"], expected)

    def test_rank_zero_has_no_moment_order_crossover(self) -> None:
        for k in (1, 2):
            q = 3 ** (4 * k)
            for moment in (1, 10, 100):
                result = MODULE.constructed_moment_contributions(
                    0, moment, q, (-1) ** k
                )
                self.assertEqual(result["absolute"], Fraction(1, 5 * q**3))
                self.assertEqual(result["signed"], Fraction(1, 5 * q**3))

    def test_all_rank_algebra_closes_before_source_read(self) -> None:
        events: list[str] = []
        original_derive = MODULE._derive_all_rank_theorem
        original_read = MODULE._read_locked_source

        def observed_derive(guard: object) -> object:
            result = original_derive(guard)
            events.append("all_rank_closed")
            return result

        def observed_read(guard: object, deadline: object) -> object:
            events.append("source_read")
            return original_read(guard, deadline)

        with (
            mock.patch.object(
                MODULE, "_derive_all_rank_theorem", side_effect=observed_derive
            ),
            mock.patch.object(MODULE, "_read_locked_source", side_effect=observed_read),
        ):
            fixture = MODULE.build_fixture()
        self.assertEqual(events, ["all_rank_closed", "source_read"])
        self.assertTrue(
            fixture["source_order_firewall"][
                "all_rank_representation_and_phase_algebra_closed_before_source_read"
            ]
        )

    def test_source_semantics_reject_geometric_drift(self) -> None:
        source, _ = MODULE._read_locked_source(
            MODULE.ResourceGuard(), MODULE.Deadline()
        )
        drifted = copy.deepcopy(source)
        drifted["exact_certificate"]["affine_orbits_and_moments"]["family_and_density"][
            "constructed_density_each_endpoint_sign"
        ] = "unknown"
        with self.assertRaisesRegex(RuntimeError, "source density drifted"):
            MODULE._validate_source_semantics(drifted)

    def test_caps_and_hashes_fail_closed(self) -> None:
        with (
            mock.patch.object(MODULE, "MAX_EXACT_OPERATIONS", 0),
            self.assertRaisesRegex(RuntimeError, "exact-operation cap"),
        ):
            MODULE.build_fixture()
        with (
            mock.patch.object(MODULE, "MAX_SOURCE_BYTES", 1),
            self.assertRaisesRegex(RuntimeError, "source-byte cap"),
        ):
            MODULE.build_fixture()
        with (
            mock.patch.object(MODULE, "MAX_OUTPUT_BYTES", 1),
            self.assertRaisesRegex(RuntimeError, "output-byte cap"),
        ):
            MODULE.build_fixture()

        drifted_lock = dict(MODULE.SOURCE_LOCK)
        drifted_lock["git_blob"] = "0" * 40
        with (
            mock.patch.object(MODULE, "SOURCE_LOCK", drifted_lock),
            self.assertRaisesRegex(RuntimeError, "source git-blob mismatch"),
        ):
            MODULE.build_fixture()

    def test_deadline_and_argument_validation_fail_closed(self) -> None:
        with (
            mock.patch.object(MODULE.time, "monotonic", return_value=3.0),
            self.assertRaisesRegex(RuntimeError, "wall-time cap"),
        ):
            MODULE.Deadline(started=0.0).check("test")

        invalid_dimensions = (-1, True, 1.5)
        for value in invalid_dimensions:
            with self.subTest(value=value), self.assertRaises(ValueError):
                MODULE.symmetric_power_dimension(value)
        with self.assertRaises(ValueError):
            MODULE.scalar_character(2, 0)
        with self.assertRaises(ValueError):
            MODULE.constructed_moment_contributions(2, 0, 81, -1)

    def test_claim_boundaries_remain_strict(self) -> None:
        boundaries = " ".join(self.fixture["claim_boundaries"])
        for phrase in (
            "constructed orbits",
            "not an asymptotic",
            "not a classification",
            "full signed moment remains unrestricted",
            "not a q-asymptotic",
            "No motive",
        ):
            self.assertIn(phrase, boundaries)
        scope = self.fixture["scope"]
        self.assertEqual(scope["finite_fields_enumerated"], 0)
        self.assertEqual(scope["curves_enumerated"], 0)
        self.assertEqual(scope["representations_enumerated"], 0)


if __name__ == "__main__":
    unittest.main()
