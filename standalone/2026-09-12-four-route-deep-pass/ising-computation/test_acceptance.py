"""Strict finite proof-gate controls; no extra theta integration required."""
from fractions import Fraction as Q
import unittest
import certify_dimer as c


class Tests(unittest.TestCase):
    def test_exact_self_map_boundary_rejected(self):
        with self.assertRaisesRegex(ArithmeticError, 'self-map'):
            c.check_contraction(c.SCALE, 0, Q(1))
        # One dyadic unit below the boundary is a strict success.
        c.check_contraction(c.SCALE - 1, 0, Q(1))

    def test_unit_contraction_rejected(self):
        with self.assertRaisesRegex(ArithmeticError, 'contraction'):
            c.check_contraction(0, c.SCALE, Q(1))

    def test_invalid_radius_and_bound_types_rejected(self):
        for radius in (Q(0), Q(-1), 1.0):
            with self.assertRaises(ArithmeticError):
                c.check_contraction(0, 0, radius)
        with self.assertRaises(ArithmeticError):
            c.check_contraction(False, 0, Q(1))

    def test_parameter_boundaries_rejected(self):
        valid = [c.I.q(Q(1,10)) for _ in range(5)]
        c.check_parameter_box(valid)
        for index, endpoint in ((0, Q(0)), (1, Q(-1,10)), (4, Q(1))):
            box = list(valid)
            box[index] = c.I.q(endpoint)
            with self.assertRaisesRegex(ArithmeticError, 'ferromagnetic'):
                c.check_parameter_box(box)


if __name__ == '__main__':
    unittest.main()
