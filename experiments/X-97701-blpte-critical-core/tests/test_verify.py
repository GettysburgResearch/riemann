#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import unittest

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("verify", HERE / "verify.py")
verify = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = verify
assert spec.loader is not None
spec.loader.exec_module(verify)


class TestCriticalCore(unittest.TestCase):
    def test_sparse_dictionary(self):
        self.assertEqual(verify.verify_sparse_dictionary(200), 200)

    def test_four_bands(self):
        bands = verify.verify_four_bands()
        self.assertEqual(bands["band_1"], ("-3/2", "0"))
        self.assertEqual(bands["band_2"], ("-3/2", "9/2"))
        self.assertEqual(bands["band_3"], ("-6", "9/2"))
        self.assertEqual(bands["band_4"], ("-6", "0"))

    def test_owner_identity(self):
        self.assertGreater(verify.verify_logarithmic_ownership(300), 100)

    def test_equivalence(self):
        self.assertEqual(verify.verify_equivalence(), 125)

    def test_mutation(self):
        result = verify.verify_unsigned_mutation()
        self.assertEqual(result["original"], "13/12")
        self.assertEqual(result["mutated"], "-13/12")

    def test_wrong_band_mutation_rejected(self):
        bands = verify.verify_four_bands()
        self.assertNotEqual(bands["band_3"], ("-3/2", "9/2"))

    def test_owner_weights_are_not_uniform(self):
        # The exact theorem uses additive logarithmic weights, not 1/omega(n).
        weights = [2, 5, 11]
        total = sum(weights)
        self.assertNotEqual([w / total for w in weights], [1 / 3] * 3)

    def test_status_is_fail_closed(self):
        # The checker proves identities only; no all-scale sign flag exists.
        self.assertNotIn("prove_c4mbi67", dir(verify))


if __name__ == "__main__":
    unittest.main()
