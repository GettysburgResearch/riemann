from fractions import Fraction
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from verify_fixed_vector_certificate import (  # noqa: E402
    CertificateError,
    SCHEMA,
    canonical_sha256,
    parameter_fingerprint,
    verify,
)


def rat(x: int, y: int = 1):
    return {"numerator": x, "denominator": y}


def iv(lo: int, hi: int | None = None, den: int = 1):
    if hi is None:
        hi = lo
    return {"lower": rat(lo, den), "upper": rat(hi, den)}


def base(prime_value=0):
    vector = {
        "scale_bits": 0,
        "real_numerators": [1],
        "imag_numerators": [0],
    }
    vector_digest = canonical_sha256(
        {
            "imag_numerators": [0],
            "real_numerators": [1],
            "scale_bits": 0,
        }
    )
    carrier_value = Fraction(94184072727073, 20)
    parameter_digest = parameter_fingerprint(
        cutoff_power10=11,
        cells=1,
        carrier=carrier_value,
        total_segments=2,
    )
    return {
        "schema": SCHEMA,
        "cutoff_power10": 11,
        "cells": 1,
        "carrier": rat(carrier_value.numerator, carrier_value.denominator),
        "total_segments": 2,
        "vector": vector,
        "vector_sha256": vector_digest,
        "parameter_sha256": parameter_digest,
        "alpha_interval": iv(1),
        "shards": [
            {
                "segment_start": 0,
                "segment_end": 1,
                "include_higher_powers": True,
                "prime_count": 1,
                "higher_prime_power_count": 1,
                "total_terms": 2,
                "vector_sha256": vector_digest,
                "parameter_sha256": parameter_digest,
                "prime_rayleigh_interval": iv(prime_value, den=2),
            },
            {
                "segment_start": 1,
                "segment_end": 2,
                "include_higher_powers": False,
                "prime_count": 1,
                "higher_prime_power_count": 0,
                "total_terms": 1,
                "vector_sha256": vector_digest,
                "parameter_sha256": parameter_digest,
                "prime_rayleigh_interval": iv(prime_value, den=2),
            },
        ],
    }


class FixedVectorCertificateTests(unittest.TestCase):
    def test_strict_positive_is_accepted(self):
        result = verify(base(prime_value=0))
        self.assertTrue(result["certified_positive"])
        self.assertFalse(result["certified_negative"])

    def test_strict_negative_is_accepted(self):
        result = verify(base(prime_value=2))
        self.assertTrue(result["certified_negative"])
        self.assertFalse(result["certified_positive"])

    def test_zero_is_unresolved_after_correction(self):
        result = verify(base(prime_value=1))
        self.assertEqual(result["verdict"], "UNRESOLVED")

    def test_segment_gap_is_rejected(self):
        data = base()
        data["shards"][1]["segment_start"] = 2
        with self.assertRaises(CertificateError):
            verify(data)

    def test_segment_overlap_is_rejected(self):
        data = base()
        data["shards"][1]["segment_start"] = 0
        with self.assertRaises(CertificateError):
            verify(data)

    def test_duplicate_higher_stream_is_rejected(self):
        data = base()
        data["shards"][1]["include_higher_powers"] = True
        with self.assertRaises(CertificateError):
            verify(data)

    def test_missing_higher_stream_is_rejected(self):
        data = base()
        data["shards"][0]["include_higher_powers"] = False
        data["shards"][0]["higher_prime_power_count"] = 0
        data["shards"][0]["total_terms"] = 1
        with self.assertRaises(CertificateError):
            verify(data)

    def test_vector_digest_mismatch_is_rejected(self):
        data = base()
        data["shards"][0]["vector_sha256"] = "0" * 64
        with self.assertRaises(CertificateError):
            verify(data)

    def test_parameter_digest_mismatch_is_rejected(self):
        data = base()
        data["parameter_sha256"] = "0" * 64
        with self.assertRaises(CertificateError):
            verify(data)

    def test_term_count_mismatch_is_rejected(self):
        data = base()
        data["shards"][0]["total_terms"] = 99
        with self.assertRaises(CertificateError):
            verify(data)

    def test_zero_vector_is_rejected(self):
        data = base()
        data["vector"]["real_numerators"] = [0]
        with self.assertRaises(CertificateError):
            verify(data)

    def test_boolean_count_is_rejected(self):
        data = base()
        data["shards"][0]["prime_count"] = True
        with self.assertRaises(CertificateError):
            verify(data)


if __name__ == "__main__":
    unittest.main()
