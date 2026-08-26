from __future__ import annotations

import hashlib
import json
import sys
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_DIR = ROOT / "research" / "l-families" / "atlas" / "function_field"
if str(MODULE_DIR) not in sys.path:
    sys.path.insert(0, str(MODULE_DIR))

import native_qadic_wavelet_square_tower_bifurcation as packet


def canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def reciprocal(a: int, b: int, q: int, endpoint: int = 3) -> list[int]:
    values = [1]
    for degree in range(1, endpoint + 1):
        value = -a * values[degree - 1]
        if degree >= 2:
            value -= b * values[degree - 2]
        if degree >= 3:
            value -= q * a * values[degree - 3]
        if degree >= 4:
            value -= q * q * values[degree - 4]
        values.append(value)
    return values


def square_wavelet(a: int, b: int, s: int) -> int:
    values = reciprocal(a, b, s * s)
    return values[3] - (1 + s) * values[2] + s * values[1]


def evaluate_ascending(coefficients: list[int], value: int) -> int:
    return sum(
        coefficient * value**degree for degree, coefficient in enumerate(coefficients)
    )


class SquareTowerBifurcationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = packet.build_fixture()

    def test_payload_and_checked_in_fixture(self) -> None:
        claimed = self.fixture["payload_sha256"]
        payload = dict(self.fixture)
        payload.pop("payload_sha256")
        self.assertEqual(claimed, canonical_sha256(payload))
        checked_in = json.loads(packet.OUTPUT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(checked_in, self.fixture)

    def test_graph_identity_on_independent_rational_samples(self) -> None:
        for s in (3, 5, 9, 11):
            for a in (-3 * s, -s, 0, s - 1, s + 2):
                denominator = 2 * a + s + 1
                if denominator == 0:
                    continue
                b = Fraction(a * (a * a + (s + 1) * a + s * (s + 1)), denominator)
                # Clear the denominator in the literal W expression.
                numerator = (
                    -(a**3)
                    - a * a * s
                    - a * a
                    + 2 * a * b
                    - a * s * s
                    - a * s
                    + b * s
                    + b
                )
                self.assertEqual(numerator, 0)

    def test_vertical_value_is_nonzero(self) -> None:
        for s in (3, 5, 7, 9):
            a = Fraction(-(s + 1), 2)
            for b in (-100, 0, 73):
                value = (
                    -(a**3)
                    - a * a * s
                    - a * a
                    + 2 * a * b
                    - a * s * s
                    - a * s
                    + b * s
                    + b
                )
                self.assertEqual(value, Fraction((s + 1) ** 2 * (3 * s - 1), 8))
                self.assertGreater(value, 0)

    def test_four_exact_K_intersections(self) -> None:
        for s in (3, 5, 7, 11):
            points = (
                (0, 0),
                (s - 1, s * (s - 1)),
                (-2 * s, 2 * s * s),
                (-s - 1, s * (s + 1)),
            )
            self.assertEqual(len(set(points)), 4)
            for a, b in points:
                self.assertEqual(square_wavelet(a, b, s), 0)
                self.assertEqual(s * s * a * a - b * b, 0)

            # On each K-line, the displayed factorizations exhaust all roots.
            plus_roots = {0, s - 1}
            minus_roots = {0, -2 * s, -s - 1}
            for a in range(-2 * s - 2, s + 3):
                if square_wavelet(a, s * a, s) == 0:
                    self.assertIn(a, plus_roots)
                if square_wavelet(a, -s * a, s) == 0:
                    self.assertIn(a, minus_roots)

    def test_compact_endpoint_certificates(self) -> None:
        compact = self.fixture["compact_admissibility"]
        self.assertIn("necessary and sufficient", compact["sufficiency_certificate"])
        rows = compact["rows"]
        self.assertEqual(len(rows), 4)
        expected_numerators = (
            {
                "discriminant": [0, 0, 8],
                "quadratic_at_minus_2": [0, 0, 2],
                "quadratic_at_plus_2": [0, 0, 2],
                "four_plus_x_plus_y": [0, 4],
                "four_minus_x_plus_y": [0, 4],
            },
            {
                "discriminant": [1, 2, 5],
                "quadratic_at_minus_2": [0, 1, 1],
                "quadratic_at_plus_2": [0, -3, 5],
                "four_plus_x_plus_y": [1, 3],
                "four_minus_x_plus_y": [-1, 5],
            },
            {
                "discriminant": [0, 0, 4],
                "quadratic_at_minus_2": [0, 0, 8],
                "quadratic_at_plus_2": [0],
                "four_plus_x_plus_y": [0, 6],
                "four_minus_x_plus_y": [0, 2],
            },
            {
                "discriminant": [1, -2, 5],
                "quadratic_at_minus_2": [0, 3, 5],
                "quadratic_at_plus_2": [0, -1, 1],
                "four_plus_x_plus_y": [1, 5],
                "four_minus_x_plus_y": [-1, 3],
            },
        )
        self.assertEqual(
            tuple(row["nonnegative_numerators_ascending"] for row in rows),
            expected_numerators,
        )
        for s in (3, 5, 13):
            points = (
                (0, 0),
                (s - 1, s * (s - 1)),
                (-2 * s, 2 * s * s),
                (-s - 1, s * (s + 1)),
            )
            for row, (a, b) in zip(rows, points, strict=True):
                root_sum = Fraction(-a, s)
                root_product = Fraction(b, s * s) - 2
                discriminant = root_sum * root_sum - 4 * root_product
                at_minus_two = 4 + 2 * root_sum + root_product
                at_plus_two = 4 - 2 * root_sum + root_product
                certificates = row["nonnegative_numerators_ascending"]
                self.assertEqual(
                    Fraction(
                        evaluate_ascending(certificates["discriminant"], s), s * s
                    ),
                    discriminant,
                )
                self.assertEqual(
                    Fraction(
                        evaluate_ascending(certificates["quadratic_at_minus_2"], s),
                        s * s,
                    ),
                    at_minus_two,
                )
                self.assertEqual(
                    Fraction(
                        evaluate_ascending(certificates["quadratic_at_plus_2"], s),
                        s * s,
                    ),
                    at_plus_two,
                )
                self.assertEqual(
                    Fraction(
                        evaluate_ascending(certificates["four_plus_x_plus_y"], s),
                        s,
                    ),
                    4 + root_sum,
                )
                self.assertEqual(
                    Fraction(
                        evaluate_ascending(certificates["four_minus_x_plus_y"], s),
                        s,
                    ),
                    4 - root_sum,
                )
                self.assertGreaterEqual(discriminant, 0)
                self.assertGreaterEqual(at_minus_two, 0)
                self.assertGreaterEqual(at_plus_two, 0)
                self.assertLessEqual(abs(root_sum), 4)

    def test_tower_parity_and_claim_firewall(self) -> None:
        tower = self.fixture["tower_bifurcation"]
        self.assertIn("irrational", tower["odd_extension_degree"])
        self.assertIn("rational zero curve", tower["even_extension_degree"])
        firewall = " ".join(self.fixture["firewall"])
        self.assertIn("not a family count", firewall)
        self.assertIn("not asserted to be Jacobians", firewall)
        self.assertIn("No novelty", firewall)

    def test_upstream_locks_and_resource_cap(self) -> None:
        self.assertEqual(
            self.fixture["upstream_payload_locks"], packet.EXPECTED_UPSTREAM_PAYLOADS
        )
        resources = self.fixture["resource_accounting"]
        self.assertLessEqual(
            resources["sparse_polynomial_operations"],
            resources["operation_cap_inclusive"],
        )
        self.assertEqual(resources["finite_fields"], 0)
        self.assertEqual(resources["curves"], 0)
        self.assertEqual(resources["family_members"], 0)


if __name__ == "__main__":
    unittest.main()
