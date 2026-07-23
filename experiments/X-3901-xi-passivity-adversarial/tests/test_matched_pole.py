from fractions import Fraction
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from matched_pole import (
    contracted_real_f_coefficients,
    finite_online_model_quadratic,
    matched_pole_vector,
    model_overlaps,
    moment,
    pair_polynomial_data,
    pair_quadratic_from_polynomials,
    symmetric_pair_quadratic,
)


class MatchedPoleTests(unittest.TestCase):
    def test_canonical_identities_through_six_nodes(self) -> None:
        d = Fraction(7, 100)
        for count in range(2, 7):
            nodes = [Fraction(index + 1, 10) for index in range(count)]
            vector = matched_pole_vector(nodes, d)
            for power in range(max(0, count - 2)):
                self.assertEqual(moment(nodes, vector, power), 0)
            alpha, beta = model_overlaps(nodes, vector, d)
            self.assertEqual(alpha, 0)
            self.assertEqual(beta, -1)
            self.assertEqual(
                symmetric_pair_quadratic(nodes, vector, d),
                -2 * d,
            )

    def test_multiplicity_and_polynomial_reconstruction(self) -> None:
        nodes = [
            Fraction(1, 10),
            Fraction(1, 4),
            Fraction(2, 3),
            Fraction(5, 4),
        ]
        model_d = Fraction(7, 100)
        actual_d = Fraction(9, 100)
        vector = matched_pole_vector(nodes, model_d)
        direct = symmetric_pair_quadratic(
            nodes,
            vector,
            actual_d,
            multiplicity=3,
        )
        polynomial = pair_quadratic_from_polynomials(
            nodes,
            vector,
            actual_d,
            multiplicity=3,
        )
        self.assertEqual(direct, polynomial)
        u_value, v_value, denominator = pair_polynomial_data(
            nodes,
            vector,
            model_d,
        )
        self.assertEqual(u_value, 0)
        self.assertEqual(v_value, -denominator)

    def test_model_cell_has_open_negative_neighborhood(self) -> None:
        nodes = [
            Fraction(1, 10),
            Fraction(1, 4),
            Fraction(2, 3),
            Fraction(5, 4),
        ]
        d = Fraction(7, 100)
        vector = matched_pole_vector(nodes, d)
        for perturbation in (
            Fraction(-1, 10000),
            Fraction(0),
            Fraction(1, 10000),
        ):
            self.assertLess(
                symmetric_pair_quadratic(nodes, vector, d + perturbation),
                0,
            )

    def test_critical_line_controls_are_nonnegative(self) -> None:
        nodes = [
            Fraction(1, 10),
            Fraction(1, 4),
            Fraction(2, 3),
            Fraction(5, 4),
        ]
        vector = matched_pole_vector(nodes, Fraction(7, 100))
        offsets = [
            Fraction(0),
            Fraction(1, 3),
            Fraction(-7, 5),
            Fraction(11, 2),
        ]
        self.assertGreater(
            finite_online_model_quadratic(nodes, vector, offsets),
            0,
        )

    def test_exact_control_vector_and_contraction(self) -> None:
        nodes = [
            Fraction(1, 10),
            Fraction(1, 4),
            Fraction(2, 3),
            Fraction(5, 4),
        ]
        vector = matched_pole_vector(nodes, Fraction(7, 100))
        self.assertEqual(
            vector,
            (
                Fraction(432, 1955),
                Fraction(-1347, 50000),
                Fraction(-579303, 1487500),
                Fraction(314619, 1610000),
            ),
        )
        self.assertEqual(
            contracted_real_f_coefficients(nodes, vector),
            (
                Fraction(462288, 1573775),
                Fraction(-73353579, 4812500000),
                Fraction(-2316036594213, 43278812500000),
                Fraction(1872297669, 231437500000),
            ),
        )
        self.assertEqual(
            symmetric_pair_quadratic(
                nodes,
                vector,
                Fraction(7, 100),
                multiplicity=3,
            ),
            Fraction(-21, 50),
        )

    def test_input_rejection(self) -> None:
        with self.assertRaises(ValueError):
            matched_pole_vector([Fraction(1, 2)], Fraction(1, 10))
        with self.assertRaises(ValueError):
            matched_pole_vector(
                [Fraction(1, 2), Fraction(1, 2)],
                Fraction(1, 10),
            )
        with self.assertRaises(ValueError):
            matched_pole_vector(
                [Fraction(1, 2), Fraction(2, 3)],
                Fraction(0),
            )
        with self.assertRaises(ZeroDivisionError):
            matched_pole_vector(
                [Fraction(1, 2), Fraction(2, 3)],
                Fraction(1, 4),
            )


if __name__ == "__main__":
    unittest.main()
