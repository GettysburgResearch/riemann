from fractions import Fraction
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from barycentric import (
    amplification_l1,
    barycentric_weights,
    online_product_value,
    online_real_f,
    online_two_channel_values,
    primitive_integer_scale,
    quadratic_from_real_f,
    symmetric_offline_pair_product_value,
    symmetric_offline_pair_real_f,
    symmetric_offline_pair_two_channels,
)


class BarycentricIdentityTests(unittest.TestCase):
    def test_online_product_identity(self) -> None:
        nodes = [Fraction(1, 10), Fraction(1, 4), Fraction(2, 3)]
        offsets = [Fraction(0), Fraction(2, 5), Fraction(-7, 3)]
        weights = barycentric_weights(nodes)
        direct = quadratic_from_real_f(nodes, weights, online_real_f(nodes, offsets))
        expected = online_product_value(nodes, offsets)
        self.assertEqual(direct, expected)
        self.assertGreater(direct, 0)

    def test_offline_pair_product_and_bracket_sign(self) -> None:
        nodes = [Fraction(1, 10), Fraction(1, 2)]
        delta = Fraction(1, 4)
        weights = barycentric_weights(nodes)
        direct = quadratic_from_real_f(
            nodes, weights, symmetric_offline_pair_real_f(nodes, delta)
        )
        expected = symmetric_offline_pair_product_value(nodes, delta)
        self.assertEqual(direct, expected)
        self.assertLess(direct, 0)

    def test_two_channel_online_positivity(self) -> None:
        a_value, b_value = online_two_channel_values(
            Fraction(1, 10),
            Fraction(1, 2),
            [Fraction(0), Fraction(2, 5), Fraction(-7, 3)],
        )
        self.assertGreaterEqual(a_value, 0)
        self.assertGreaterEqual(b_value, 0)

    def test_two_channel_bracket_sign_and_ratio(self) -> None:
        delta = Fraction(1, 4)
        a_value, b_value = symmetric_offline_pair_two_channels(
            Fraction(1, 10), Fraction(1, 2), delta
        )
        self.assertLess(a_value, 0)
        self.assertGreater(b_value, 0)
        self.assertEqual(b_value / a_value, -(delta * delta))

    def test_two_channel_right_side_sign_and_ratio(self) -> None:
        delta = Fraction(1, 4)
        a_value, b_value = symmetric_offline_pair_two_channels(
            Fraction(1, 3), Fraction(1, 2), delta
        )
        self.assertGreater(a_value, 0)
        self.assertLess(b_value, 0)
        self.assertEqual(b_value / a_value, -(delta * delta))

    def test_even_number_below_delta_is_positive(self) -> None:
        nodes = [Fraction(1, 10), Fraction(1, 5), Fraction(1, 2)]
        delta = Fraction(1, 4)
        self.assertGreater(symmetric_offline_pair_product_value(nodes, delta), 0)

    def test_primitive_integer_vector(self) -> None:
        nodes = [
            Fraction(value, 100000)
            for value in (1, 3, 10, 30, 100, 300, 1000, 3000)
        ]
        vector = primitive_integer_scale(barycentric_weights(nodes))
        self.assertEqual(
            vector,
            (
                -18278001000000000,
                26004329000000000,
                -8692207821270000,
                992352095670000,
                -26793506583090,
                321933623010,
                -702116883,
                676963,
            ),
        )
        integer_nodes = (1, 3, 10, 30, 100, 300, 1000, 3000)
        for power in range(7):
            self.assertEqual(
                sum(vector[i] * integer_nodes[i] ** power for i in range(8)), 0
            )
        self.assertEqual(
            sum(vector[i] * integer_nodes[i] ** 7 for i in range(8)),
            846150346569085279722000000000,
        )

    def test_amplification_is_positive(self) -> None:
        nodes = [Fraction(1, 10), Fraction(1, 4), Fraction(2, 3)]
        vector = primitive_integer_scale(barycentric_weights(nodes))
        self.assertGreater(amplification_l1(nodes, vector), 0)

    def test_input_rejection(self) -> None:
        with self.assertRaises(ValueError):
            barycentric_weights([Fraction(1, 2), Fraction(1, 2)])
        with self.assertRaises(ValueError):
            barycentric_weights([Fraction(0), Fraction(1, 2)])
        with self.assertRaises(ValueError):
            symmetric_offline_pair_two_channels(
                Fraction(1, 2), Fraction(1, 3), Fraction(1, 4)
            )


if __name__ == "__main__":
    unittest.main()
