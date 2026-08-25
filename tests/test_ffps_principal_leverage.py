"""Focused exact tests for the corrected FFPS leverage packet."""

from __future__ import annotations

import hashlib
import itertools
import json
import sys
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import ffps_principal_leverage as subject  # noqa: E402


class FFPSPrincipalLeverageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()

    def test_phase_gram_and_sharp_constant_extremizer(self) -> None:
        for prime in (3, 5, 7, 11):
            dimension = (prime - 1) // 2
            gram = subject.phase_gram(prime)
            self.assertEqual(len(gram), dimension)
            self.assertTrue(
                all(
                    gram[row][column] == (prime - 1 if row == column else -1)
                    for row in range(dimension)
                    for column in range(dimension)
                )
            )
            vector = subject.constant_extremizer(prime)
            observation = sum(vector, Fraction(0))
            ratio = observation**2 / subject.phase_energy(prime, vector)
            self.assertEqual(ratio, Fraction(prime - 1, prime + 1))

            # Sum-zero modes are invisible to the principal observation and
            # have Gram eigenvalue p.
            if dimension > 1:
                mode = (1, -1) + (0,) * (dimension - 2)
                self.assertEqual(sum(mode), 0)
                self.assertEqual(
                    subject.phase_energy(prime, mode),
                    prime * sum(value * value for value in mode),
                )

    def test_tensor_and_positive_block_assembly_are_different(self) -> None:
        self.assertEqual(subject.tensor_leverage_squared((3, 5)), Fraction(1, 3))
        self.assertEqual(
            subject.positive_block_leverage_squared((3, 5), (1, 1)),
            Fraction(7, 6),
        )
        for prime in (3, 5, 7, 11):
            count = 3
            self.assertEqual(
                subject.positive_block_leverage_squared(
                    (prime,) * count, (1,) * count
                ),
                count * Fraction(prime - 1, prime + 1),
            )

    def test_collision_lines_match_direct_equations(self) -> None:
        aggregate = 0
        for prime in (3, 5, 7, 11):
            for owner, other_owner in ((1, 1), (1, 2)):
                for sign in (-1, 1):
                    row = subject.verify_collision_lines(
                        owner, other_owner, sign, prime
                    )
                    aggregate += row["atoms_checked"]
                    self.assertIn(row["line_count"], (0, 2))
                    self.assertEqual(
                        row["collision_pair_count"],
                        row["line_count"] * (prime - 1),
                    )
        self.assertLess(aggregate, subject.MAX_CONTROL_ATOMS)

    def test_same_owner_class_two_or_four_line_law(self) -> None:
        for prime in (3, 5, 7, 11, 13):
            plus = subject.collision_slopes(1, 1, 1, prime)
            minus = subject.collision_slopes(1, 1, -1, prime)
            self.assertEqual(len(plus), 2)
            self.assertEqual(len(minus), 2 if prime % 4 == 1 else 0)
            self.assertEqual(len(plus) + len(minus), 4 if prime % 4 == 1 else 2)

    def test_owner_only_and_physical_aliases_are_distinct(self) -> None:
        self.assertEqual(subject.physical_squareclass(1, 1, 7), 1)
        self.assertEqual(subject.physical_squareclass(1, 2, 7), 4)
        self.assertNotIn(1, (4, -4 % 7))
        self.assertEqual(subject.physical_squareclass(1, 2, 7), 4)
        self.assertEqual(subject.physical_squareclass(2, 3, 7), 4)

    def test_quadratic_character_and_roots(self) -> None:
        for prime in (3, 5, 7, 11):
            for value in range(1, prime):
                roots = subject.square_roots(value, prime)
                self.assertEqual(bool(roots), subject.quadratic_character(value, prime) == 1)
                self.assertTrue(all(root * root % prime == value for root in roots))

    def test_fixture_and_provenance(self) -> None:
        locked = json.loads(subject.OUTPUT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(locked, self.fixture)
        self.assertEqual(
            locked["source_frontier"]["commit"], subject.SOURCE_COMMIT_751
        )
        self.assertEqual(
            locked["source_frontier"]["git_blob_ids"], subject.SOURCE_BLOBS_751
        )
        hashes = locked["provenance"]
        for label, path in (
            ("producer_sha256_lf", Path(subject.__file__)),
            ("note_sha256_lf", subject.NOTE_PATH),
            ("test_sha256_lf", Path(__file__)),
        ):
            normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            self.assertEqual(hashes[label], hashlib.sha256(normalized).hexdigest())

    def test_fail_closed_domains(self) -> None:
        for value in (-3, -1, 0, 1, 2, 9, 15):
            with self.assertRaises(ValueError):
                subject.phase_gram(value)
        with self.assertRaises(ValueError):
            subject.positive_block_leverage_squared((3,), (1, 1))
        with self.assertRaises(ValueError):
            subject.collision_slopes(1, 1, 0, 7)
        with self.assertRaises(ValueError):
            subject.square_roots(1, 131)
        with self.assertRaises(ValueError):
            subject.verify_collision_lines(1, 1, 1, 127)


if __name__ == "__main__":
    unittest.main()
