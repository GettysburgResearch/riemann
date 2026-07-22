from __future__ import annotations

import math
from pathlib import Path
import sys
import unittest

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from merge import hermitian_toeplitz, merge_shards
from stream import compute_shard, simple_primes


class PiecewiseCarrierTests(unittest.TestCase):
    def parameters(self, **changes):
        values = dict(
            cutoff=1000,
            carrier_text="3012.125",
            cells=16,
            segment_size=200,
            start_segment=0,
            end_segment=5,
            include_higher_powers=True,
        )
        values.update(changes)
        return values

    def test_simple_primes(self):
        self.assertEqual(simple_primes(20).tolist(), [2, 3, 5, 7, 11, 13, 17, 19])

    def test_partition_invariance(self):
        full = compute_shard(**self.parameters())
        left = compute_shard(**self.parameters(end_segment=2, include_higher_powers=False))
        right = compute_shard(**self.parameters(start_segment=2))
        merged = merge_shards([left, right])
        direct = merge_shards([full])
        self.assertEqual(merged["prime_count"], direct["prime_count"])
        self.assertEqual(merged["higher_prime_power_count"], direct["higher_prime_power_count"])
        self.assertAlmostEqual(merged["leading_margin"], direct["leading_margin"], places=12)

    def test_gap_is_rejected(self):
        left = compute_shard(**self.parameters(end_segment=2, include_higher_powers=False))
        right = compute_shard(**self.parameters(start_segment=3))
        with self.assertRaisesRegex(ValueError, "gap or overlap"):
            merge_shards([left, right])

    def test_higher_powers_must_appear_once(self):
        left = compute_shard(**self.parameters(end_segment=2, include_higher_powers=False))
        right = compute_shard(**self.parameters(start_segment=2, include_higher_powers=False))
        with self.assertRaisesRegex(ValueError, "exactly one"):
            merge_shards([left, right])

    def test_toeplitz_is_hermitian(self):
        coefficients = np.array([3 + 4j, 2 - 5j, -1 + 7j], dtype=np.complex128)
        matrix = hermitian_toeplitz(coefficients)
        self.assertTrue(np.allclose(matrix, matrix.conj().T))
        self.assertEqual(matrix[0, 0], 3)
        self.assertEqual(matrix[0, 1], 1 - 2.5j)

    def test_one_cell_matches_triangular_prime_sum(self):
        shard = compute_shard(**self.parameters(cells=1))
        merged = merge_shards([shard])
        cutoff = self.parameters()["cutoff"]
        carrier = float(self.parameters()["carrier_text"])
        primes = simple_primes(cutoff)
        terms = []
        for raw in primes:
            p = int(raw)
            q = p
            while q <= cutoff:
                terms.append((q, p))
                if q > cutoff // p:
                    break
                q *= p
        expected = 0.0
        log_c = math.log(cutoff)
        for q, p in terms:
            expected += (
                math.log(p)
                / (math.pi * math.sqrt(q))
                * (1.0 - math.log(q) / log_c)
                * math.cos(carrier * math.log(q))
            )
        recovered = merged["archimedean_leading_scalar"] - merged["leading_margin"]
        self.assertAlmostEqual(recovered, expected, places=10)


if __name__ == "__main__":
    unittest.main()
