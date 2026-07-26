from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("checker", HERE / "verify_one_node_pade.py")
checker = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(checker)


def rat(n: int, d: int = 1) -> dict[str, int]:
    return {"numerator": n, "denominator": d}


def iv(n: int, d: int = 1) -> dict[str, dict[str, int]]:
    return {"lower": rat(n, d), "upper": rat(n, d)}


def positive_certificate() -> dict:
    # Old measure delta_1 + delta_3, queried at w=1.
    return {
        "schema": checker.SCHEMA,
        "classification": "SYNTHETIC",
        "w": rat(1),
        "support_lower": rat(0),
        "old_moments": [iv(2), iv(4), iv(10)],
        "new_b0": iv(3, 4),
        "lower_witness": None,
        "upper_witness": None,
        "closure_delta": rat(1, 100),
    }


def verify_payload(payload: dict) -> dict:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "certificate.json"
        path.write_text(json.dumps(payload), encoding="utf-8")
        return checker.verify(path)


class OneNodePadeTests(unittest.TestCase):
    def test_positive_interval_closure(self) -> None:
        result = verify_payload(positive_certificate())
        self.assertEqual(result["verdict"], "CERTIFIED_POSITIVE_ONE_NODE_PADE_INTERVAL")

    def test_lower_square_witness(self) -> None:
        payload = positive_certificate()
        payload["new_b0"] = iv(0)
        payload["lower_witness"] = [rat(1), rat(-1)]
        result = verify_payload(payload)
        self.assertEqual(result["verdict"], "CERTIFIED_NEGATIVE_LOWER_SQUARE_WITNESS")

    def test_support_localizer_witness(self) -> None:
        payload = positive_certificate()
        payload["new_b0"] = iv(2)
        payload["upper_witness"] = [rat(1), rat(-1)]
        result = verify_payload(payload)
        self.assertEqual(
            result["verdict"], "CERTIFIED_NEGATIVE_SUPPORT_LOCALIZER_WITNESS"
        )

    def test_rejects_negative_support(self) -> None:
        payload = positive_certificate()
        payload["support_lower"] = rat(-1)
        with self.assertRaises(checker.CertificateError):
            verify_payload(payload)

    def test_rejects_even_old_moment_count(self) -> None:
        payload = positive_certificate()
        payload["old_moments"] = payload["old_moments"][:2]
        with self.assertRaises(checker.CertificateError):
            verify_payload(payload)

    def test_rejects_bad_witness_length(self) -> None:
        payload = positive_certificate()
        payload["lower_witness"] = [rat(1)]
        with self.assertRaises(checker.CertificateError):
            verify_payload(payload)

    def test_interval_uncertainty_can_remain_unresolved(self) -> None:
        payload = positive_certificate()
        payload["new_b0"] = {"lower": rat(0), "upper": rat(2)}
        payload["closure_delta"] = rat(1, 100)
        result = verify_payload(payload)
        self.assertEqual(result["verdict"], "UNRESOLVED_ONE_NODE_PADE_INTERVAL")


if __name__ == "__main__":
    unittest.main()
