from __future__ import annotations

import importlib.util
import sys
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x23202_verify", ROOT / "verify.py")
assert SPEC is not None and SPEC.loader is not None
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


class CorrectedProposalTests(unittest.TestCase):
    def test_canonical_grid(self):
        total, counts = module.grid_check(Fraction(1, 5), 60)
        self.assertEqual(total, 715)
        self.assertEqual(sum(counts.values()), total)

    def test_old_delta_counterexample_is_rejected(self):
        with self.assertRaises(module.VerificationError):
            module.classify_triplet(
                Fraction(37, 100),
                Fraction(77, 200),
                Fraction(49, 200),
                Fraction(2, 5),
            )

    def test_complexity_cycle_is_rejected(self):
        with self.assertRaises(module.VerificationError):
            module.topological_order({1: [2], 2: [1]})

    def test_signed_recombination_is_not_rowwise_energy(self):
        _, direct, separate = module.recombine_signed(
            [
                [Fraction(3), Fraction(-2), Fraction(1)],
                [Fraction(-3), Fraction(2), Fraction(-1)],
                [Fraction(1), Fraction(1), Fraction(-1)],
            ]
        )
        self.assertEqual(direct, 3)
        self.assertEqual(separate, 31)
        self.assertLess(direct, separate)

    def test_missing_btp_field_is_rejected(self):
        with self.assertRaises(module.VerificationError):
            module.validate_btp_manifest({"signed_recombination": True})

    def test_wrong_orientation_is_rejected(self):
        manifest = {field: True for field in module.REQUIRED_BTP_FIELDS}
        manifest["normal_gram"] = "product-dilation"
        with self.assertRaises(module.VerificationError):
            module.validate_btp_manifest(manifest)

    def test_unsigned_manifest_is_rejected(self):
        manifest = {field: True for field in module.REQUIRED_BTP_FIELDS}
        manifest["normal_gram"] = "factor-ratio"
        manifest["signed_recombination"] = False
        with self.assertRaises(module.VerificationError):
            module.validate_btp_manifest(manifest)

    def test_complete_result(self):
        result = module.verify()
        self.assertEqual(
            result["classification"],
            "EXACT_SYNTHETIC_TERMINAL_EULER_BTP_AUDIT",
        )
        self.assertEqual(result["terminal_energy_decay_exponent"], [3, 5])
        self.assertEqual(
            result["exact_proof_object_sha256"],
            "172d510bc2b256e593c586f9fb9aab14d9b69edc024bc73ef845ec3c30c60726",
        )


if __name__ == "__main__":
    unittest.main()
