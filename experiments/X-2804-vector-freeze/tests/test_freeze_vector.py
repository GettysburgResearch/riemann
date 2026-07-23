import unittest
import numpy as np

from freeze_vector import (
    VECTOR_SCHEMA,
    canonicalize_phase,
    freeze,
    hermitian_toeplitz,
    round_nearest_even_binary64,
)


def shard(start, end, real, imag, *, powers=False):
    return {
        "schema": "riemann.carrier-piecewise-shard.v1",
        "parameters": {
            "cutoff": 100,
            "carrier": "37.5",
            "cells": len(real),
            "segment_size": 50,
            "total_segments": 2,
        },
        "segment_range": {"start": start, "end": end},
        "include_higher_prime_powers": powers,
        "prime_count": 3,
        "higher_prime_power_count": 2 if powers else 0,
        "total_prime_power_terms": 3 + (2 if powers else 0),
        "coefficients": {"real": real, "imag": imag},
    }


class FreezeVectorTests(unittest.TestCase):
    def test_round_nearest_even(self):
        self.assertEqual(round_nearest_even_binary64(0.5, 0), 0)
        self.assertEqual(round_nearest_even_binary64(1.5, 0), 2)
        self.assertEqual(round_nearest_even_binary64(-1.5, 0), -2)

    def test_phase_pivot_is_real_positive(self):
        v = np.asarray([1j, -2 + 2j, 0.5], dtype=np.complex128)
        rotated, pivot = canonicalize_phase(v)
        self.assertEqual(pivot, 1)
        self.assertGreater(rotated[pivot].real, 0)
        self.assertEqual(rotated[pivot].imag, 0)

    def test_complete_export(self):
        a = shard(0, 1, [1.0, 0.2, -0.1], [0.0, 0.3, 0.1], powers=True)
        b = shard(1, 2, [0.5, -0.1, 0.05], [0.0, 0.2, -0.02])
        out = freeze([a, b], 80)
        self.assertEqual(out["schema"], VECTOR_SCHEMA)
        self.assertEqual(out["coverage"]["total_prime_power_terms"], 8)
        self.assertEqual(len(out["dyadic_vector"]["real_numerators"]), 3)
        self.assertLess(out["discovery_diagnostics"]["eigenpair_residual_inf_norm"], 1e-12)

    def test_partition_invariance(self):
        a = shard(0, 1, [1.0, 0.2], [0.0, 0.3], powers=True)
        b = shard(1, 2, [0.5, -0.1], [0.0, 0.2])
        left = freeze([a, b], 72)
        right = freeze([b, a], 72)
        self.assertEqual(left["canonical_sha256"], right["canonical_sha256"])

    def test_gap_rejected(self):
        a = shard(0, 1, [1.0, 0.2], [0.0, 0.3], powers=True)
        b = shard(0, 2, [0.5, -0.1], [0.0, 0.2])
        with self.assertRaises(ValueError):
            freeze([a, b], 72)

    def test_higher_power_uniqueness(self):
        a = shard(0, 1, [1.0, 0.2], [0.0, 0.3], powers=True)
        b = shard(1, 2, [0.5, -0.1], [0.0, 0.2], powers=True)
        with self.assertRaises(ValueError):
            freeze([a, b], 72)

    def test_toeplitz_is_hermitian(self):
        matrix = hermitian_toeplitz(np.asarray([1 + 0j, 2 + 3j, -1 + 0.5j]))
        self.assertTrue(np.allclose(matrix, matrix.conj().T))


if __name__ == "__main__":
    unittest.main()
