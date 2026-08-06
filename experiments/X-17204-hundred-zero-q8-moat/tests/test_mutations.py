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
    spec = importlib.util.spec_from_file_location("x17204_verify_tests", VERIFY_PATH)
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
            self.verifier.verify_rational(cert, EXPERIMENT_DIR)

    def test_reference_certificate_passes(self) -> None:
        result = self.verifier.verify_rational(self.certificate, EXPERIMENT_DIR)
        self.assertEqual(result["classification"], "EXACT_RATIONAL_PRECHECK_PASSED")

    def test_changed_base_hash_is_rejected(self) -> None:
        self.assert_rejected(
            lambda cert: cert["base_dependencies"].__setitem__(
                "ten_notch_certificate_sha256", "0" * 64
            )
        )

    def test_changed_inherited_verifier_hash_is_rejected(self) -> None:
        self.assert_rejected(
            lambda cert: cert["base_dependencies"].__setitem__(
                "q8_verifier_sha256", "0" * 64
            )
        )

    def test_changed_cutoff_is_rejected(self) -> None:
        self.assert_rejected(
            lambda cert: cert["zero_census"].__setitem__("count_cutoff", "236")
        )

    def test_changed_bracket_radius_is_rejected(self) -> None:
        self.assert_rejected(
            lambda cert: cert["zero_census"].__setitem__("bracket_radius", "1e-6")
        )

    def test_understated_line_target_is_rejected(self) -> None:
        self.assert_rejected(
            lambda cert: cert["directed_constants"].__setitem__(
                "nontrivial_line_target", "3/100000000000000000000000000"
            )
        )

    def test_changed_tail_power_is_rejected(self) -> None:
        self.assert_rejected(
            lambda cert: cert["directed_constants"].__setitem__("tail_power", 30)
        )

    def test_understated_raw_moat_is_rejected(self) -> None:
        self.assert_rejected(
            lambda cert: cert["directed_constants"].__setitem__(
                "raw_tail_moat", "3/100000000000000000000000000"
            )
        )


if __name__ == "__main__":
    unittest.main()
