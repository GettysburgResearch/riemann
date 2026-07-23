from fractions import Fraction
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from matched_pole import (
    barycentric_weights,
    critical_line_pick_quadratic,
    matched_identities,
    matched_pole_vector,
    pick_quadratic_from_real_values,
    primitive_integer_scale,
    same_ordinate_pair_quadratic,
)


def offline_pair_real_value(x: Fraction, delta: Fraction, y: Fraction) -> Fraction:
    return sum(
        (x - beta) / ((x - beta) ** 2 + y * y)
        for beta in (delta, -delta)
    )


def critical_real_value(x: Fraction, offsets: list[Fraction]) -> Fraction:
    return sum(x / (x * x + y * y) for y in offsets)


class MatchedPoleTests(unittest.TestCase):
    def test_exact_annihilation_overlap_and_moments(self) -> None:
        nodes = [Fraction(v, 100000) for v in (1, 3, 10, 30, 100, 300, 1000)]
        d = Fraction(9, 1000)
        identities = matched_identities(nodes, d)
        self.assertEqual(identities["a_overlap"], 0)
        self.assertEqual(identities["b_overlap"], identities["expected_b_overlap"])
        self.assertTrue(all(value == 0 for value in identities["moments"]))
        self.assertEqual(
            primitive_integer_scale(identities["vector"]),
            (
                -16539879233914654832354524370000,
                23515038853801750873712859570000,
                -7840902633919673843989064577990,
                888890597261655236548071739110,
                -23408189640724901265510548343,
                261023362454990952789561603,
                -416950807523604621374380,
            ),
        )

    def test_pair_quadratic_is_exactly_negative(self) -> None:
        nodes = [Fraction(1), Fraction(2), Fraction(3)]
        d = Fraction(1, 4)
        vector = matched_pole_vector(nodes, d)
        product = Fraction(1)
        for x in nodes:
            product *= x * x - d
        self.assertEqual(
            same_ordinate_pair_quadratic(nodes, vector, d),
            -2 * d / (product * product),
        )

    def test_symmetry_closed_control_defeats_weaker_channels(self) -> None:
        nodes = [Fraction(1), Fraction(2), Fraction(3)]
        delta = Fraction(1, 2)
        d = delta * delta
        offsets = [Fraction(10), Fraction(-10), Fraction(190), Fraction(210)]
        values = []
        for x in nodes:
            same = 2 * x / (x * x - d)
            conjugate = offline_pair_real_value(x, delta, Fraction(200))
            background = 19 * critical_real_value(x, offsets)
            values.append(same + conjugate + background)
        self.assertTrue(all(value > 0 for value in values))

        # Every two-point A/B channel is positive.
        for i, j in ((0, 1), (0, 2), (1, 2)):
            x1, x2 = nodes[i], nodes[j]
            r1, r2 = values[i], values[j]
            denominator = x2 * x2 - x1 * x1
            a = (r1 / x1 - r2 / x2) / denominator
            b = (x2 * r2 - x1 * r1) / denominator
            self.assertGreater(a, 0)
            self.assertGreater(b, 0)

        standard = barycentric_weights(nodes)
        matched = matched_pole_vector(nodes, d)
        self.assertGreater(pick_quadratic_from_real_values(nodes, standard, values), 0)
        self.assertEqual(matched, (Fraction(-2, 21), Fraction(52, 105), Fraction(-2, 5)))
        self.assertLess(pick_quadratic_from_real_values(nodes, matched, values), 0)

        target = same_ordinate_pair_quadratic(nodes, matched, d)
        background = 19 * critical_line_pick_quadratic(nodes, matched, offsets)
        self.assertLess(target, 0)
        self.assertGreater(background, 0)

    def test_input_rejection(self) -> None:
        with self.assertRaises(ValueError):
            matched_pole_vector([Fraction(1)], Fraction(1, 4))
        with self.assertRaises(ValueError):
            matched_pole_vector([Fraction(1), Fraction(1)], Fraction(1, 4))
        with self.assertRaises(ZeroDivisionError):
            matched_pole_vector([Fraction(1), Fraction(2)], Fraction(1))
        with self.assertRaises(ValueError):
            matched_pole_vector([Fraction(1), Fraction(2)], Fraction(0))


if __name__ == "__main__":
    unittest.main()
