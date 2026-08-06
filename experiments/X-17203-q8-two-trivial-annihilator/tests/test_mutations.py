from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path


EXPERIMENT_DIR = Path(__file__).resolve().parents[1]
VERIFY_PATH = EXPERIMENT_DIR / "verify.py"
CERTIFICATE_PATH = EXPERIMENT_DIR / "certificate.json"


def load_verifier():
    spec = importlib.util.spec_from_file_location("x17203_verify_tests", VERIFY_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class MutationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.verifier = load_verifier()
        cls.certificate = json.loads(CERTIFICATE_PATH.read_text(encoding="utf-8"))

    def assert_rejected(self, mutate) -> None:
        cert = copy.deepcopy(self.certificate)
        mutate(cert)
        with self.assertRaises(AssertionError):
            self.verifier.verify_certificate(cert, EXPERIMENT_DIR)

    def test_reference_certificate_passes(self) -> None:
        result = self.verifier.verify_certificate(self.certificate, EXPERIMENT_DIR)
        self.assertEqual(result["classification"], "EXACT_RATIONAL_CHECK_PASSED")

    def test_changed_trivial_ordinate_is_rejected(self) -> None:
        self.assert_rejected(
            lambda cert: cert["annihilators"][1].__setitem__("lambda", "11/2")
        )

    def test_understated_line_factor_is_rejected(self) -> None:
        self.assert_rejected(
            lambda cert: cert["directed_constants"].__setitem__(
                "critical_line_factor_upper", "1"
            )
        )

    def test_understated_support_is_rejected(self) -> None:
        self.assert_rejected(
            lambda cert: cert["directed_constants"].__setitem__(
                "support_endpoint_upper", "10"
            )
        )

    def test_understated_trivial_tail_is_rejected(self) -> None:
        self.assert_rejected(
            lambda cert: cert["directed_constants"].__setitem__(
                "trivial_tail_target", "1/100000000000000000000"
            )
        )

    def test_understated_raw_moat_is_rejected(self) -> None:
        self.assert_rejected(
            lambda cert: cert["directed_constants"].__setitem__(
                "raw_tail_moat", "1/200000000000000000"
            )
        )


if __name__ == "__main__":
    unittest.main()

