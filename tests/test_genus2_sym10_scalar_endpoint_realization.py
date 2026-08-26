from __future__ import annotations

import copy
import importlib.util
import json
import math
import sys
import tempfile
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
    / "genus2_sym10_scalar_endpoint_realization.py"
)
OUTPUT_PATH = MODULE_PATH.with_suffix(".json")

SPEC = importlib.util.spec_from_file_location(
    "genus2_sym10_scalar_endpoint_realization", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load scalar-endpoint producer")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class Genus2Sym10ScalarEndpointRealizationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = MODULE.build_fixture()
        cls.disk = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))
        cls.exact = cls.fixture["exact_certificate"]

    def test_fixture_is_canonical(self) -> None:
        self.assertEqual(self.fixture, self.disk)
        claimed = self.fixture["payload_sha256"]
        payload = dict(self.fixture)
        payload.pop("payload_sha256")
        self.assertEqual(claimed, MODULE._canonical_sha256(payload))

    def test_seed_quintic_is_squarefree(self) -> None:
        guard = MODULE.ResourceGuard()
        polynomial = (1, 0, 0, 0, 0, 1)
        derivative = MODULE._derivative_mod(polynomial, 3, guard)
        self.assertEqual(derivative, (0, 0, 0, 0, 2))
        self.assertEqual(MODULE._gcd_mod(polynomial, derivative, 3, guard), (1,))
        certificate = self.exact["seed"]["squarefree_quintic"]
        self.assertEqual(certificate["monic_gcd_with_derivative_mod_3"], [1])

    def test_point_counts_use_power_map_bijections(self) -> None:
        rows = self.exact["seed"]["point_counts_without_field_sweep"]["rows"]
        self.assertEqual(
            [
                (
                    row["field_order"],
                    math.gcd(5, row["multiplicative_group_order"]),
                    row["quadratic_character_sum"],
                    row["projective_point_count"],
                )
                for row in rows
            ],
            [(3, 1, 0, 4), (9, 1, 0, 10)],
        )
        counts = self.exact["seed"]["point_counts_without_field_sweep"]
        self.assertEqual((counts["N_1"], counts["N_2"]), (4, 10))

    def test_newton_reconstruction_is_exact(self) -> None:
        n1, n2 = 4, 10
        s1 = 3 + 1 - n1
        s2 = 3**2 + 1 - n2
        e2 = Fraction(s1**2 - s2, 2)
        self.assertEqual((s1, s2, e2), (0, 0, 0))
        newton = self.exact["seed"]["newton_reconstruction"]
        self.assertEqual(
            newton["local_factor_coefficients_increasing_T"], [1, 0, 0, 0, 9]
        )
        self.assertEqual(
            newton["frobenius_characteristic_polynomial_coefficients_increasing_X"],
            [9, 0, 0, 0, 1],
        )

    def test_all_k_base_change_sign_and_sym10_value(self) -> None:
        for k in (1, 2, 7):
            q = 3 ** (4 * k)
            frobenius_scalar = (-9) ** k
            self.assertEqual(frobenius_scalar**2, q)
            self.assertEqual(frobenius_scalar**10, q**5)
            self.assertEqual(frobenius_scalar // 3 ** (2 * k), (-1) ** k)
            self.assertEqual(math.comb(13, 3) * frobenius_scalar**10, 286 * q**5)
        base_change = self.exact["base_change"]
        self.assertEqual(base_change["normalized_frobenius"], "U=(-1)^k*I_4")
        self.assertEqual(base_change["sym10"]["dimension"], 286)
        smallest = base_change["smallest_tower_specialization_not_a_field_sweep"]
        self.assertEqual(
            (smallest["U"], smallest["a"], smallest["point_count"]),
            ("-I_4", 36, 118),
        )
        self.assertEqual(
            (
                smallest["quadratic_twist"]["U"],
                smallest["quadratic_twist"]["a"],
                smallest["quadratic_twist"]["point_count"],
            ),
            ("I_4", -36, 46),
        )

    def test_affine_stabilizer_and_square_subgroup(self) -> None:
        orbit = self.exact["affine_orbits_and_moments"]
        self.assertEqual(
            orbit["characteristic_three_expansion"][
                "binomial_coefficients_mod_3_in_increasing_T_power"
            ],
            [1, 2, 1, 1, 2, 1],
        )
        self.assertEqual(orbit["stabilizer"]["order"], 5)
        for k in (1, 2, 5):
            q = 81**k
            self.assertEqual((q - 1) % 10, 0)
            generator_exponent = (q - 1) // 5
            self.assertEqual(generator_exponent % 2, 0)
            self.assertEqual(math.gcd(5, q - 1), 5)
        twist = orbit["nonsquare_twist_sign_derivation"]
        self.assertIn("r^q=-r", twist["setup"])
        self.assertIn("U maps to -U", twist["conclusion"])

    def test_orbit_sizes_densities_and_moment_contribution(self) -> None:
        for k in (1, 2, 3):
            q = 81**k
            family = q**4 * (q - 1)
            each = q * (q - 1) // 10
            combined = q * (q - 1) // 5
            self.assertEqual(Fraction(each, family), Fraction(1, 10 * q**3))
            self.assertEqual(Fraction(combined, family), Fraction(1, 5 * q**3))
            for m in (1, 2, 5):
                self.assertEqual(
                    Fraction(combined * 286**m, family),
                    Fraction(286**m, 5 * q**3),
                )
        smallest = self.exact["affine_orbits_and_moments"][
            "smallest_tower_specialization_not_a_field_sweep"
        ]
        self.assertEqual(smallest["members_each_endpoint_sign"], 648)
        self.assertEqual(smallest["members_both_endpoint_signs"], 1296)

    def test_log_order_bounds_are_exact(self) -> None:
        for k in (1, 4, 20):
            q = 81**k
            target = q**3
            m_q = 0
            power = 1
            while power * 286 <= target:
                power *= 286
                m_q += 1
            contribution = Fraction(power, 5 * target)
            self.assertGreaterEqual(contribution, Fraction(1, 5 * 286))
            self.assertLessEqual(contribution, Fraction(1, 5))

    def test_locked_sources_are_compatibility_only_and_load_late(self) -> None:
        events: list[str] = []
        original_derive = MODULE._derive_exact_certificate
        original_load = MODULE._load_sources

        def observed_derive(guard: object) -> object:
            result = original_derive(guard)
            events.append("exact_closed")
            return result

        def observed_load(guard: object) -> object:
            events.append("sources_loaded")
            return original_load(guard)

        with (
            mock.patch.object(
                MODULE, "_derive_exact_certificate", side_effect=observed_derive
            ),
            mock.patch.object(MODULE, "_load_sources", side_effect=observed_load),
        ):
            MODULE.build_fixture()
        self.assertLess(events.index("exact_closed"), events.index("sources_loaded"))
        self.assertTrue(
            self.fixture["source_order_firewall"][
                "locked_sources_applied_only_as_compatibility_checks"
            ]
        )

    def test_source_compatibility_rejects_twist_sign_drift(self) -> None:
        sources = MODULE._load_sources(MODULE.ResourceGuard())
        drifted = copy.deepcopy(sources)
        drifted["marked_stack_adapter"]["odd_central_weight"]["exact_result"] = (
            "sign unavailable"
        )
        with self.assertRaisesRegex(ArithmeticError, "twist sign drifted"):
            MODULE._validate_source_compatibility(drifted, MODULE.ResourceGuard())

    def test_caps_and_hashes_fail_closed(self) -> None:
        cases = (
            ("MAX_SOURCE_RECORDS", 0, "source-record cap"),
            ("MAX_EXACT_OPERATIONS", 0, "exact-operation cap"),
        )
        for attribute, limit, message in cases:
            with (
                self.subTest(attribute=attribute),
                mock.patch.object(MODULE, attribute, limit),
                self.assertRaisesRegex(RuntimeError, message),
            ):
                MODULE.build_fixture()

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "oversize.json"
            path.write_bytes(b"x" * 32)
            lock = {
                "path": path,
                "schema": "unused",
                "lf_sha256": "unused",
                "payload_sha256": "unused",
                "audited_commit": "unused",
            }
            with (
                mock.patch.object(MODULE, "MAX_SOURCE_BYTES", 8),
                mock.patch.object(MODULE, "SOURCE_LOCKS", {"oversize": lock}),
                self.assertRaisesRegex(RuntimeError, "before full read"),
            ):
                MODULE._load_sources(MODULE.ResourceGuard())

        locks = {name: dict(lock) for name, lock in MODULE.SOURCE_LOCKS.items()}
        locks["marked_stack_adapter"]["lf_sha256"] = "0" * 64
        with (
            mock.patch.object(MODULE, "SOURCE_LOCKS", locks),
            self.assertRaisesRegex(RuntimeError, "LF-normalized source hash mismatch"),
        ):
            MODULE.build_fixture()

    def test_wall_cap_is_checked_after_payload_hash(self) -> None:
        events: list[str] = []
        original_hash = MODULE._canonical_sha256

        def observed_hash(value: object) -> str:
            if (
                isinstance(value, dict)
                and value.get("schema") == self.fixture["schema"]
            ):
                events.append("payload_hashed")
            return original_hash(value)

        with (
            mock.patch.object(MODULE, "_canonical_sha256", side_effect=observed_hash),
            mock.patch.object(MODULE.time, "perf_counter", side_effect=[0.0, 3.0]),
            self.assertRaisesRegex(RuntimeError, "wall cap"),
        ):
            MODULE.build_fixture()
        self.assertEqual(events, ["payload_hashed"])

    def test_scope_contains_no_literature_dependency_or_enumeration(self) -> None:
        scope = self.fixture["scope"]
        self.assertFalse(scope["external_literature_used_by_producer"])
        self.assertEqual(scope["finite_fields_enumerated"], 0)
        self.assertEqual(scope["field_elements_enumerated"], 0)
        self.assertEqual(scope["curves_enumerated"], 0)
        self.assertNotIn("Howe", json.dumps(self.fixture, sort_keys=True))


if __name__ == "__main__":
    unittest.main()
