import copy
import unittest

from assemble_certificate import assemble, canonical_sha

VECTOR = {
    "parameters": {"carrier": "37.5"},
    "dyadic_vector": {
        "scale_bits": 2,
        "real_numerators": [1, 2],
        "imag_numerators": [0, 1],
    },
}
ALPHA = {
    "carrier": {"numerator": 75, "denominator": 2},
    "alpha_dyadic_interval": {
        "lower_num": 10,
        "upper_num": 11,
        "scale_bits": 4,
    },
}
PLAN = {
    "cutoff_power10": 2,
    "cells": 2,
    "total_segments": 2,
    "shards": [
        {"segment_start": 0, "segment_end": 1, "include_higher_powers": True},
        {"segment_start": 1, "segment_end": 2, "include_higher_powers": False},
    ],
    "expected_counts": {
        "prime_count": 6,
        "higher_prime_power_count": 2,
        "total_terms": 8,
    },
}
VECTOR_CANONICAL = {
    "imag_numerators": [0, 1],
    "real_numerators": [1, 2],
    "scale_bits": 2,
}
VECTOR_SHA = canonical_sha(VECTOR_CANONICAL)
PARAMETERS = {
    "carrier": {"numerator": 75, "denominator": 2},
    "cells": 2,
    "cutoff_power10": 2,
    "total_segments": 2,
}
PARAMETER_SHA = canonical_sha(PARAMETERS)
NORMALIZATION_SHA = "65bacffb2e03518fa6ffb771f79d276b0018f7a22a1b17f3a7566d119024c8be"


def shard(start, end, higher, precision, lower, upper, prime_count, higher_count):
    return {
        "schema": "riemann.piecewise-carrier-directed-shard.v1",
        "segment_start": start,
        "segment_end": end,
        "include_higher_powers": higher,
        "prime_count": prime_count,
        "higher_prime_power_count": higher_count,
        "total_terms": prime_count + higher_count,
        "vector_sha256": VECTOR_SHA,
        "parameter_sha256": PARAMETER_SHA,
        "normalization_sha256": NORMALIZATION_SHA,
        "precision_bits": precision,
        "mpfr_version": "4.2.2",
        "prime_rayleigh_interval": {
            "lower": {"numerator": lower, "denominator": 100},
            "upper": {"numerator": upper, "denominator": 100},
        },
    }


SHARDS = [
    shard(0, 1, True, 192, 10, 20, 3, 2),
    shard(0, 1, True, 256, 12, 18, 3, 2),
    shard(1, 2, False, 192, -5, 5, 3, 0),
    shard(1, 2, False, 256, -4, 4, 3, 0),
]


class AssembleCertificateTests(unittest.TestCase):
    def test_assemble(self):
        result = assemble(VECTOR, ALPHA, SHARDS, PLAN)
        self.assertEqual(len(result["shards"]), 2)
        self.assertEqual(
            result["producer_evidence"]["global_counts"]["total_terms"], 8
        )
        self.assertEqual(
            result["shards"][0]["prime_rayleigh_interval"]["lower"]["numerator"],
            3,
        )

    def test_missing_precision_rejected(self):
        with self.assertRaises(ValueError):
            assemble(VECTOR, ALPHA, SHARDS[:-1], PLAN)

    def test_disjoint_precision_rejected(self):
        bad = copy.deepcopy(SHARDS)
        bad[1]["prime_rayleigh_interval"]["lower"]["numerator"] = 30
        bad[1]["prime_rayleigh_interval"]["upper"]["numerator"] = 31
        with self.assertRaises(ValueError):
            assemble(VECTOR, ALPHA, bad, PLAN)

    def test_normalization_mutation_rejected(self):
        bad = copy.deepcopy(SHARDS)
        bad[0]["normalization_sha256"] = "bad"
        with self.assertRaises(ValueError):
            assemble(VECTOR, ALPHA, bad, PLAN)

    def test_count_mismatch_rejected(self):
        bad = copy.deepcopy(SHARDS)
        bad[1]["prime_count"] = 4
        bad[1]["total_terms"] = 6
        with self.assertRaises(ValueError):
            assemble(VECTOR, ALPHA, bad, PLAN)


if __name__ == "__main__":
    unittest.main()
