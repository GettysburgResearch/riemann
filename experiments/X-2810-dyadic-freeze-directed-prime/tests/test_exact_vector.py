import unittest
from fractions import Fraction
from exact_vector import (
    SCHEMA,
    autocorrelation_numerators,
    canonical_sha256,
    parse_vector,
    target_rounding_bound,
)


class ExactVectorTests(unittest.TestCase):
    def test_autocorrelation(self):
        real = [1, 2]
        imag = [3, -4]
        auto_real, auto_imag = autocorrelation_numerators(real, imag)
        self.assertEqual(auto_real[0], 30)
        self.assertEqual(auto_imag[0], 0)
        self.assertEqual(auto_real[1], -10)
        self.assertEqual(auto_imag[1], -10)

    def test_rounding_bound_target(self):
        bound = target_rounding_bound(
            cells=1024, bits=80, operator_norm_upper=6_957_023
        )
        self.assertLess(bound, Fraction(1, 10**15))

    def test_digest(self):
        vector = {
            "imag_numerators": [0],
            "real_numerators": [1],
            "scale_bits": 3,
        }
        data = {
            "schema": SCHEMA,
            "cells": 1,
            "vector": vector,
            "vector_sha256": canonical_sha256(vector),
        }
        self.assertEqual(parse_vector(data)[0], 1)


if __name__ == "__main__":
    unittest.main()
