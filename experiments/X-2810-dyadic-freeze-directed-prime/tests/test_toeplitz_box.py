import unittest
from fractions import Fraction
from exact_vector import SCHEMA as VECTOR_SCHEMA, canonical_sha256
from verify_toeplitz_box import contract


def rational(value):
    return {"numerator": value, "denominator": 1}


def box(lower, upper):
    return {"lower": rational(lower), "upper": rational(upper)}


class ToeplitzBoxTests(unittest.TestCase):
    def vector(self):
        vector = {
            "real_numerators": [2, -1, 3],
            "imag_numerators": [1, 4, -2],
            "scale_bits": 3,
        }
        return {
            "schema": VECTOR_SCHEMA,
            "cells": 3,
            "vector": vector,
            "vector_sha256": canonical_sha256(vector),
        }

    def test_point_boxes_match_exact_contraction(self):
        # Exact lag coefficients z=[2, 3+5i, -1+2i].
        data = {
            "schema": "riemann.toeplitz-coefficient-box.v1",
            "cells": 3,
            "lags": [
                {
                    "lag": 0,
                    "real_interval": box(2, 2),
                    "imag_interval": box(0, 0),
                },
                {
                    "lag": 1,
                    "real_interval": box(3, 3),
                    "imag_interval": box(5, 5),
                },
                {
                    "lag": 2,
                    "real_interval": box(-1, -1),
                    "imag_interval": box(2, 2),
                },
            ],
        }
        output = contract(data, self.vector())
        result = output["prime_rayleigh_interval"]
        self.assertEqual(result["lower"], result["upper"])
        self.assertEqual(
            Fraction(
                result["lower"]["numerator"],
                result["lower"]["denominator"],
            ),
            Fraction(29, 32),
        )

    def test_negative_interval_scaling_orders_endpoints(self):
        data = {
            "schema": "riemann.toeplitz-coefficient-box.v1",
            "cells": 3,
            "lags": [
                {
                    "lag": 0,
                    "real_interval": box(0, 0),
                    "imag_interval": box(0, 0),
                },
                {
                    "lag": 1,
                    "real_interval": box(1, 2),
                    "imag_interval": box(-3, -2),
                },
                {
                    "lag": 2,
                    "real_interval": box(0, 0),
                    "imag_interval": box(0, 0),
                },
            ],
        }
        output = contract(data, self.vector())
        result = output["prime_rayleigh_interval"]
        lower = Fraction(result["lower"]["numerator"], result["lower"]["denominator"])
        upper = Fraction(result["upper"]["numerator"], result["upper"]["denominator"])
        self.assertLessEqual(lower, upper)


if __name__ == "__main__":
    unittest.main()
