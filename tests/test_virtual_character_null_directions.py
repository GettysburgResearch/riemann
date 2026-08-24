"""Exact replay tests for the bounded USp(4) virtual-null search."""

from __future__ import annotations

import hashlib
import itertools
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import virtual_character_null_directions as subject  # noqa: E402


class VirtualCharacterNullDirectionsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()

    def test_coefficient_square_null_lattice(self) -> None:
        lattice = self.fixture["coefficient_square_lattice"]
        self.assertEqual(lattice["haar_means"], [1, 2, 1])
        self.assertEqual(lattice["integer_basis"], [[2, -1, 0], [-1, 0, 1]])
        for t in range(-3, 4):
            for s in range(-3, 4):
                a, b, c = 2 * t - s, -t, s
                self.assertEqual(a + 2 * b + c, 0)
        for a, b, c in itertools.product(range(-2, 3), repeat=3):
            if a + 2 * b + c == 0:
                t, s = -b, c
                self.assertEqual((a, b, c), (2 * t - s, -t, s))

    def test_character_and_torus_identities(self) -> None:
        guard = subject.SearchGuard()
        character_guard = subject.base.ResourceGuard()
        engine = subject.base.CnCharacterEngine(2, character_guard)
        one = subject._character(engine, (0, 0))
        chi_01 = subject._character(engine, (0, 1))
        chi_20 = subject._character(engine, (2, 0))
        chi_02 = subject._character(engine, (0, 2))
        e1 = subject.base.elementary_character(2, 1)
        e2 = subject.base.elementary_character(2, 2)
        e3 = subject.base.elementary_character(2, 3)
        self.assertEqual(e1, e3)
        e1_square = subject.multiply(e1, e1, guard)
        e2_square = subject.multiply(e2, e2, guard)
        self.assertEqual(
            e1_square,
            subject.add_linear(((one, 1), (chi_01, 1), (chi_20, 1)), guard),
        )
        self.assertEqual(
            e2_square,
            subject.add_linear(
                ((one, 2), (chi_01, 2), (chi_20, 1), (chi_02, 1)), guard
            ),
        )
        b_character = subject.add_linear(((chi_20, 1), (chi_02, -1)), guard)
        u = {(2, 0): 1, (-2, 0): 1}
        v = {(0, 2): 1, (0, -2): 1}
        self.assertEqual(b_character, subject.scale(subject.multiply(u, v, guard), -1))

    def test_frozen_panels_have_only_certified_survivors(self) -> None:
        square, central, weight_four = self.fixture["search_panels"]
        self.assertEqual(subject._survivor_vectors(square), {(0, 0, 1, -1)})
        self.assertEqual(
            subject._survivor_vectors(weight_four), {(0, 0, 1, -1, 0, 0)}
        )
        expected_central = {
            (0, 0, 0, 0, *odd)
            for odd in itertools.product((-1, 0, 1), repeat=3)
            if subject._primitive_sign_normalized(odd)
        }
        expected_central.add((0, 0, 1, -1, 0, 0, 0))
        self.assertEqual(subject._survivor_vectors(central), expected_central)
        self.assertEqual(len(expected_central), 14)
        self.assertEqual([panel["survivor_count"] for panel in self.fixture["search_panels"]], [1, 14, 1])

    def test_central_odd_involution_on_laurent_support(self) -> None:
        character_guard = subject.base.ResourceGuard()
        engine = subject.base.CnCharacterEngine(2, character_guard)
        for highest in ((1, 0), (1, 1), (3, 0)):
            character = subject._character(engine, highest)
            transformed = {
                exponent: ((-1) ** sum(exponent)) * coefficient
                for exponent, coefficient in character.items()
            }
            self.assertEqual(transformed, subject.scale(character, -1))

    def test_b_residue_and_closed_moments(self) -> None:
        certificate = self.fixture["exact_symmetry_certificates"]["B_residue"]
        self.assertTrue(
            all(
                row["coefficient"] == 0
                for row in certificate[
                    "weyl_density_coefficients_on_possible_residue_support"
                ]
            )
        )
        self.assertEqual(
            certificate["frozen_moments_1_through_10"],
            [0, 2, 0, 12, 0, 100, 0, 980, 0, 10584],
        )
        b_support = {(2, 2), (2, -2), (-2, 2), (-2, -2)}
        self.assertTrue(all((a % 4, b % 4) == (2, 2) for a, b in b_support))

    def test_residue_null_module_generators(self) -> None:
        guard = subject.SearchGuard()
        u = {(2, 0): 1, (-2, 0): 1}
        v = {(0, 2): 1, (0, -2): 1}
        u2 = subject.multiply(u, u, guard)
        v2 = subject.multiply(v, v, guard)
        sigma = subject.add_linear(((u2, 1), (v2, 1)), guard)
        product = subject.multiply(u2, v2, guard)
        self.assertTrue(all(a % 4 == b % 4 == 0 for a, b in sigma))
        self.assertTrue(all(a % 4 == b % 4 == 0 for a, b in product))
        b_polynomial = subject.scale(subject.multiply(u, v, guard), -1)
        for multiplier in ({(0, 0): 1}, sigma, product):
            module_element = subject.multiply(b_polynomial, multiplier, guard)
            self.assertTrue(
                all((a % 4, b % 4) == (2, 2) for a, b in module_element)
            )

    def test_independent_weyl_density_reconstruction(self) -> None:
        density = {(0, 0): 1}
        for root in ((2, 0), (0, 2), (1, 1), (1, -1)):
            next_density: dict[tuple[int, int], int] = {}
            factor = {(0, 0): 2, root: -1, (-root[0], -root[1]): -1}
            for (a, b), coefficient in density.items():
                for (c, d), factor_coefficient in factor.items():
                    exponent = (a + c, b + d)
                    next_density[exponent] = (
                        next_density.get(exponent, 0)
                        + coefficient * factor_coefficient
                    )
            density = {key: value for key, value in next_density.items() if value}
        self.assertEqual(density[(0, 0)], 8)
        actual = subject.base.weyl_density(2, subject.base.ResourceGuard())
        self.assertEqual(actual, density)
        self.assertFalse(
            any(
                coefficient
                for (a, b), coefficient in actual.items()
                if a % 4 == 2 and b % 4 == 2
            )
        )

    def test_checked_in_fixture_and_hash_locks(self) -> None:
        expected = json.loads(
            (FUNCTION_FIELD / "virtual_character_null_directions.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(self.fixture, expected)
        producer = self.fixture["producer"]

        def independent_lf_sha256(path: Path) -> str:
            normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(
                b"\r", b"\n"
            )
            return hashlib.sha256(normalized).hexdigest()

        self.assertEqual(
            producer["source_sha256_lf_normalized"],
            independent_lf_sha256(Path(subject.__file__)),
        )
        self.assertEqual(
            producer["note_sha256_lf_normalized"],
            independent_lf_sha256(subject.NOTE_PATH),
        )
        self.assertEqual(
            producer["checker_sha256_lf_normalized"],
            independent_lf_sha256(subject.CHECKER_PATH),
        )
        self.assertEqual(
            producer["character_dependency_sha256_lf_normalized"],
            independent_lf_sha256(subject.BASE_PATH),
        )

    def test_resource_contract_and_fail_closed_cap(self) -> None:
        contract = self.fixture["resource_contract"]
        self.assertTrue(
            all(
                contract["observed_counts"][name] < cap
                for name, cap in contract["hard_caps"].items()
            )
        )
        guard = subject.SearchGuard()
        guard.limits["candidate_vectors"] = 0
        with self.assertRaisesRegex(RuntimeError, "resource cap exceeded"):
            guard.charge("candidate_vectors")


if __name__ == "__main__":
    unittest.main()
