from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERIFY_PATH = ROOT / "verify.py"
CERT_PATH = ROOT / "certificates" / "synthetic.json"

spec = importlib.util.spec_from_file_location("verify_green_dipole", VERIFY_PATH)
verify = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(verify)


class GreenDipoleSkorokhodTests(unittest.TestCase):
    def cert(self):
        return json.loads(CERT_PATH.read_text(encoding="utf-8"))

    def test_valid_certificate(self):
        result = verify.verify_certificate(self.cert())
        self.assertEqual(result["verdict"], "PASS_EXACT_GREEN_DIPOLE_SKOROKHOD_INTERFACES")
        self.assertEqual(result["proof_sha256"], "5941277ae1d4435a1e57ab72c7cde8edadd0aed3fef5061b0618e07f898672ea")

    def test_boolean_endpoint_rejected(self):
        cert = self.cert()
        cert["X"] = True
        with self.assertRaises(verify.VerificationError):
            verify.verify_certificate(cert)

    def test_missing_seed_rejected(self):
        cert = self.cert()
        del cert["seed_b"]["7"]
        with self.assertRaises(verify.VerificationError):
            verify.verify_certificate(cert)

    def test_wrong_prime_power_manifest_rejected(self):
        cert = self.cert()
        cert["prime_powers"][-1] = 12
        with self.assertRaises(verify.VerificationError):
            verify.verify_certificate(cert)

    def test_target_mutation_rejected_by_expected_ledger(self):
        cert = self.cert()
        cert["target_w"]["11"] = "2/11"
        with self.assertRaises(verify.VerificationError):
            verify.verify_certificate(cert)

    def test_false_expected_contact_gap_rejected(self):
        cert = self.cert()
        cert["expected"]["prefix_contact_gap"]["2"] = "0"
        with self.assertRaises(verify.VerificationError):
            verify.verify_certificate(cert)

    def test_negative_seed_rejected(self):
        cert = self.cert()
        cert["seed_b"]["5"] = "-1"
        with self.assertRaises(verify.VerificationError):
            verify.verify_certificate(cert)

    def test_invalid_fraction_rejected(self):
        cert = self.cert()
        cert["target_w"]["7"] = "not-a-fraction"
        with self.assertRaises(verify.VerificationError):
            verify.verify_certificate(cert)

    def test_schema_rejected(self):
        cert = self.cert()
        cert["schema"] = "wrong"
        with self.assertRaises(verify.VerificationError):
            verify.verify_certificate(cert)


if __name__ == "__main__":
    unittest.main()
