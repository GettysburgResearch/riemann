from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest


VERIFY = Path(__file__).resolve().parents[1] / "verify.py"
SPEC = importlib.util.spec_from_file_location("x104640_verify", VERIFY)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class TestT104640(unittest.TestCase):
    def test_exact_replay(self) -> None:
        payload = MODULE.run()
        self.assertEqual(
            payload["classification"],
            "PASS_T104640_SOURCE_INNER_FACTOR_FIREWALL",
        )
        self.assertEqual(payload["finite_checks"], 19)
        self.assertTrue(payload["bezout_identity_verified"])
        self.assertTrue(payload["grade_zero_is_exact_model_projection"])
        self.assertFalse(payload["universal_source_to_inner_promotion_proved"])
        self.assertFalse(payload["selfkrylov104636_proved"])
        self.assertFalse(payload["more_than_ninety_percent_established"])
        self.assertFalse(payload["rh_established"])


if __name__ == "__main__":
    unittest.main()
