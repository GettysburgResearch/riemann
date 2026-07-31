from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x17202_verify", ROOT / "verify.py")
assert SPEC is not None and SPEC.loader is not None
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


class CertificateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.certificate = json.loads((ROOT / "certificate.json").read_text(encoding="utf-8"))

    def test_retained_certificate(self) -> None:
        result = VERIFY.verify_rational(copy.deepcopy(self.certificate))
        self.assertEqual(result["classification"], "EXACT_RATIONAL_CHECK_PASSED")

    def test_rejects_count_gap(self) -> None:
        mutated = copy.deepcopy(self.certificate)
        mutated["filter"]["notches"][4]["count_hi"] = 6
        with self.assertRaises(AssertionError):
            VERIFY.verify_rational(mutated)

    def test_rejects_reversed_pi_interval(self) -> None:
        mutated = copy.deepcopy(self.certificate)
        constants = mutated["directed_constants"]
        constants["pi_lo"], constants["pi_hi"] = constants["pi_hi"], constants["pi_lo"]
        with self.assertRaises(AssertionError):
            VERIFY.verify_rational(mutated)

    def test_rejects_understated_line_moat(self) -> None:
        mutated = copy.deepcopy(self.certificate)
        mutated["directed_constants"]["nontrivial_zero_moat"] = "3/1000000000000000000"
        with self.assertRaises(AssertionError):
            VERIFY.verify_rational(mutated)


if __name__ == "__main__":
    unittest.main()
