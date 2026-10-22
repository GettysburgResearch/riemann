"""Focused tests for the exact USp(4) toy-minor character packet."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import usp4_toy_minor_character_decomposition as packet  # noqa: E402


class C2CharacterEngineTests(unittest.TestCase):
    def setUp(self) -> None:
        self.guard = packet.ResourceGuard()
        self.engine = packet.C2CharacterEngine(self.guard)

    def test_small_character_dimensions_and_highest_weights(self) -> None:
        expected = {
            (0, 0): 1,
            (1, 0): 4,
            (1, 1): 5,
            (2, 0): 10,
            (2, 1): 16,
            (2, 2): 14,
        }
        for highest, dimension in expected.items():
            character = self.engine.character(highest)
            a, b = highest[0] - highest[1], highest[1]
            self.assertEqual(packet.evaluate_at_identity(character), dimension)
            self.assertEqual(packet.weyl_dimension(a, b), dimension)
            self.assertEqual(character[highest], 1)

    def test_defining_statistic_identity_is_independent_and_exact(self) -> None:
        G = self.engine.character((0, 0))
        G = packet.add_scaled(G, self.engine.character((1, 1)), 1, self.guard)
        G = packet.add_scaled(G, self.engine.character((2, 2)), 1, self.guard)
        defining = packet.statistic_from_defining_characters(self.guard)
        self.assertEqual(defining, packet.scale(G, -1))
        self.assertEqual(packet.evaluate_at_identity(defining), -20)

    def test_kostant_partition_and_weight_multiplicity_controls(self) -> None:
        self.assertEqual(self.engine.kostant_partition((0, 0)), 1)
        self.assertEqual(self.engine.kostant_partition((1, -1)), 1)
        self.assertEqual(self.engine.kostant_partition((0, 2)), 1)
        self.assertEqual(self.engine.kostant_partition((-1, 1)), 0)
        self.assertEqual(self.engine.weight_multiplicity((2, 2), (0, 0)), 2)
        with self.assertRaisesRegex(ValueError, "highest weight"):
            self.engine.character((13, 0))
        with self.assertRaisesRegex(ValueError, "nonnegative"):
            packet.weyl_dimension(-1, 0)

    def test_resource_caps_are_enforced(self) -> None:
        guard = packet.ResourceGuard(
            limits={
                "character_weight_candidates": 1,
                "kostant_weyl_summands": 1,
                "laurent_pair_products": 1,
                "residual_term_updates": 1,
            }
        )
        with self.assertRaisesRegex(RuntimeError, "resource cap exceeded"):
            guard.charge("laurent_pair_products", 2)
        with self.assertRaisesRegex(ValueError, "nonnegative"):
            guard.charge("residual_term_updates", -1)


class PacketTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = packet.build_fixture()

    def test_all_six_decompositions_have_exact_sign_and_dimension(self) -> None:
        expected_irreducible_counts = [3, 9, 16, 25, 36, 49]
        expected_trivial_G = [1, 3, 11, 56, 374, 3117]
        self.assertEqual(
            [row["irreducible_count"] for row in self.fixture["powers"]],
            expected_irreducible_counts,
        )
        for row, trivial in zip(self.fixture["powers"], expected_trivial_G):
            power = row["power"]
            sign = -1 if power % 2 else 1
            self.assertEqual(row["global_sign_from_F_equals_minus_G"], sign)
            self.assertEqual(row["tensor_dimension"], 20**power)
            self.assertEqual(row["dimension_sum_from_decomposition"], 20**power)
            self.assertEqual(row["trivial_tensor_multiplicity_in_G_power"], trivial)
            self.assertEqual(row["trivial_coefficient_in_F_power"], sign * trivial)
            self.assertEqual(
                row["independent_weyl_constant_term_haar_moment"], sign * trivial
            )
            self.assertTrue(row["reconstruction_exact"])
            for entry in row["decomposition"]:
                self.assertGreater(entry["tensor_multiplicity_in_G_power"], 0)
                self.assertEqual(
                    entry["coefficient_in_F_power"],
                    sign * entry["tensor_multiplicity_in_G_power"],
                )
                weight = entry["highest_weight"]
                a = weight["omega1_coefficient"]
                b = weight["omega2_coefficient"]
                self.assertEqual(weight["notation"], f"{a}*omega1+{b}*omega2")
                self.assertEqual(weight["e_basis_coordinates"], [a + b, b])
                self.assertEqual(entry["dimension"], packet.weyl_dimension(a, b))

    def test_character_identity_records_the_all_power_sign_theorem(self) -> None:
        corollary = self.fixture["all_power_corollary"]
        self.assertTrue(corollary["integrality"])
        self.assertIn("every integer m>=0", corollary["statement"])
        self.assertEqual(
            corollary["strict_sign_rule"],
            "(-1)^m*Haar(F^m)>0 for every m>=0",
        )
        self.assertIn("trivial summand", corollary["proof"])
        self.assertIn("no finite-family convergence", corollary["scope"])

    def test_first_two_tensor_decompositions_are_frozen_explicitly(self) -> None:
        def as_map(row: dict) -> dict[tuple[int, int], int]:
            return {
                (
                    entry["highest_weight"]["omega1_coefficient"],
                    entry["highest_weight"]["omega2_coefficient"],
                ): entry["tensor_multiplicity_in_G_power"]
                for entry in row["decomposition"]
            }

        self.assertEqual(
            as_map(self.fixture["powers"][0]),
            {(0, 0): 1, (0, 1): 1, (0, 2): 1},
        )
        self.assertEqual(
            as_map(self.fixture["powers"][1]),
            {
                (0, 0): 3,
                (0, 2): 4,
                (0, 4): 1,
                (2, 0): 2,
                (2, 1): 2,
                (2, 2): 1,
                (4, 0): 1,
                (0, 1): 4,
                (0, 3): 2,
            },
        )

    def test_exact_reconstruction_is_reproducible_independently(self) -> None:
        guard = packet.ResourceGuard()
        engine = packet.C2CharacterEngine(guard)
        G = engine.character((0, 0))
        G = packet.add_scaled(G, engine.character((1, 1)), 1, guard)
        G = packet.add_scaled(G, engine.character((2, 2)), 1, guard)
        current = {(0, 0): 1}
        for frozen in self.fixture["powers"]:
            current = packet.multiply(current, G, guard)
            decomposition = packet.decompose_character(current, engine)
            self.assertEqual(packet.reconstruct_character(decomposition, engine), current)
            frozen_map = {
                tuple(entry["highest_weight"]["e_basis_coordinates"]): entry[
                    "tensor_multiplicity_in_G_power"
                ]
                for entry in frozen["decomposition"]
            }
            self.assertEqual(decomposition, frozen_map)

    def test_independent_weyl_constant_terms_match_signed_trivial_parts(self) -> None:
        guard = packet.ResourceGuard()
        engine = packet.C2CharacterEngine(guard)
        G = engine.character((0, 0))
        G = packet.add_scaled(G, engine.character((1, 1)), 1, guard)
        G = packet.add_scaled(G, engine.character((2, 2)), 1, guard)
        density = packet.weyl_density(guard)
        current = {(0, 0): 1}
        observed = []
        for power in range(1, 7):
            current = packet.multiply(current, G, guard)
            observed.append(
                packet.haar_constant_term(
                    packet.scale(current, -1 if power % 2 else 1), density, guard
                )
            )
        self.assertEqual(observed, list(packet.FROZEN_HAAR_MOMENTS))

    def test_fixture_verification_and_resource_firewalls(self) -> None:
        verification = self.fixture["verification"]
        for key, value in verification.items():
            if key.startswith("all_"):
                self.assertTrue(value, key)
        contract = self.fixture["resource_contract"]
        for category, observed in contract["observed_operations"].items():
            self.assertLessEqual(observed, contract["operation_caps"][category])
        self.assertFalse(contract["random_sampling"])
        self.assertFalse(contract["numerical_integration"])
        self.assertFalse(contract["external_cas"])
        self.assertIn(
            "finite genus-two family moment convergence",
            self.fixture["scope_firewall"]["this_does_not_prove"],
        )

    def test_producer_source_is_content_locked(self) -> None:
        source = Path(packet.__file__).read_text(encoding="utf-8").replace("\r\n", "\n")
        self.assertEqual(
            self.fixture["producer"]["source_sha256_lf_normalized"],
            __import__("hashlib").sha256(source.encode("utf-8")).hexdigest(),
        )

    def test_checked_in_fixture_is_exact_generator_output(self) -> None:
        stored = json.loads(
            (FUNCTION_FIELD / "usp4_toy_minor_character_decomposition.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(stored, self.fixture)


if __name__ == "__main__":
    unittest.main()
