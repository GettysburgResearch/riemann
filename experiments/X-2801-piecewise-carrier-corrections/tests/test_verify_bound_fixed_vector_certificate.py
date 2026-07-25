import copy
import unittest

from verify_bound_fixed_vector_certificate import (
    NORMALIZATION_SHA256,
    CertificateError,
    verify,
)
from test_verify_fixed_vector_certificate import base


class BoundFixedVectorTests(unittest.TestCase):
    def test_canonical_normalization_is_accepted(self):
        data = base(prime_value=2)
        data["normalization_sha256"] = NORMALIZATION_SHA256
        result = verify(data)
        self.assertEqual(result["normalization_sha256"], NORMALIZATION_SHA256)
        self.assertTrue(result["certified_negative"])

    def test_missing_normalization_is_rejected(self):
        with self.assertRaises(CertificateError):
            verify(base(prime_value=2))

    def test_mutated_normalization_is_rejected(self):
        data = base(prime_value=2)
        data["normalization_sha256"] = "0" * 64
        with self.assertRaises(CertificateError):
            verify(data)


if __name__ == "__main__":
    unittest.main()
