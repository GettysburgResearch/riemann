from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("x15408verify", ROOT / "verify.py")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
assert spec.loader is not None
spec.loader.exec_module(module)

CERT = json.loads((ROOT / "certificates" / "synthetic.json").read_text())


class HardyPoleGramTests(unittest.TestCase):
    def test_committed_certificate(self):
        out = module.verify(copy.deepcopy(CERT))
        self.assertEqual(out["status"], "EXACT_FINITE_HARDY_POLE_GRAM")
        self.assertEqual(
            out["unstable_packet"]["energy"],
            {"numerator": "1562625", "denominator": "5002"},
        )

    def test_false_unstable_energy_rejected(self):
        bad = copy.deepcopy(CERT)
        bad["unstable_packet"]["claimed"]["energy"]["numerator"] = "1562626"
        with self.assertRaises(module.CertificateError):
            module.verify(bad)

    def test_line_through_pole_rejected(self):
        bad = copy.deepcopy(CERT)
        bad["unstable_packet"]["sigma"] = {"numerator": "1", "denominator": "4"}
        with self.assertRaises(module.CertificateError):
            module.verify(bad)

    def test_duplicate_pole_rejected(self):
        bad = copy.deepcopy(CERT)
        bad["unstable_packet"]["poles"][1] = copy.deepcopy(
            bad["unstable_packet"]["poles"][0]
        )
        with self.assertRaises(module.CertificateError):
            module.verify(bad)

    def test_zero_residue_rejected(self):
        bad = copy.deepcopy(CERT)
        bad["stable_packet"]["residues"][0] = {
            "real": {"numerator": "0", "denominator": "1"},
            "imag": {"numerator": "0", "denominator": "1"},
        }
        with self.assertRaises(module.CertificateError):
            module.verify(bad)

    def test_nonpositive_sigma_rejected(self):
        bad = copy.deepcopy(CERT)
        bad["boundary_packet"]["sigma"] = {"numerator": "0", "denominator": "1"}
        with self.assertRaises(module.CertificateError):
            module.verify(bad)

    def test_boolean_integer_rejected(self):
        bad = copy.deepcopy(CERT)
        bad["stable_packet"]["sigma"]["numerator"] = True
        with self.assertRaises(module.CertificateError):
            module.verify(bad)

    def test_false_weighted_energy_rejected(self):
        bad = copy.deepcopy(CERT)
        bad["boundary_packet"]["claimed"]["sigma_times_energy"]["numerator"] = "22"
        with self.assertRaises(module.CertificateError):
            module.verify(bad)

    def test_packet_gram_is_hermitian(self):
        out = module.verify(copy.deepcopy(CERT))
        gram = out["unstable_packet"]["cauchy_gram"]
        self.assertEqual(gram[0][1]["real"], gram[1][0]["real"])
        self.assertEqual(
            int(gram[0][1]["imag"]["numerator"]),
            -int(gram[1][0]["imag"]["numerator"]),
        )


if __name__ == "__main__":
    unittest.main()
