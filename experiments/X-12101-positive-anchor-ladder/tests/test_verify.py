from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "positive_anchor_verify", ROOT / "verify.py"
)
assert SPEC is not None and SPEC.loader is not None
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


def load(name: str) -> dict:
    return json.loads(
        (ROOT / "certificates" / name).read_text(encoding="utf-8")
    )


class PositiveAnchorLadderTests(unittest.TestCase):
    def test_positive_control(self) -> None:
        result = verify.verify(load("synthetic-positive.json"))
        self.assertEqual(
            result["status"],
            "CERTIFIED_POSITIVE_FULL_HALF_LINE_CONE",
        )
        self.assertEqual(
            result["verification_sha256"],
            "0423469c646627ca5d9c5c2d21bf67638c3e7f36cf8f350b5b92d0aedd2cb196",
        )

    def test_negative_control(self) -> None:
        result = verify.verify(load("synthetic-negative.json"))
        self.assertEqual(
            result["status"],
            "CERTIFIED_NEGATIVE_HALF_LINE_RESPONSE",
        )
        self.assertEqual(
            result["negative_checks"], ["negative-h0-square"]
        )

    def test_anchor_order_is_canonical(self) -> None:
        data = load("synthetic-positive.json")
        data["anchors"].reverse()
        data["anchor_scalars"].reverse()
        with self.assertRaises(verify.CertificateError):
            verify.verify(data)

    def test_duplicate_anchor_is_rejected(self) -> None:
        data = load("synthetic-positive.json")
        data["anchors"][1] = copy.deepcopy(data["anchors"][0])
        with self.assertRaises(verify.CertificateError):
            verify.verify(data)

    def test_claimed_quadratic_mutation_is_rejected(self) -> None:
        data = load("synthetic-negative.json")
        data["checks"][0]["claimed_value"]["numerator"] = "-1"
        with self.assertRaises(verify.CertificateError):
            verify.verify(data)

    def test_declared_check_manifest_is_closed(self) -> None:
        data = load("synthetic-positive.json")
        data["declared_check_ids"].append("decorative")
        with self.assertRaises(verify.CertificateError):
            verify.verify(data)

    def test_zero_vector_is_rejected(self) -> None:
        data = load("synthetic-negative.json")
        data["checks"][0]["vector"] = [
            {"numerator": "0", "denominator": "1"}
            for _ in range(4)
        ]
        with self.assertRaises(verify.CertificateError):
            verify.verify(data)

    def test_boolean_degree_is_rejected(self) -> None:
        data = load("synthetic-positive.json")
        data["old_degree"] = True
        with self.assertRaises(verify.CertificateError):
            verify.verify(data)


if __name__ == "__main__":
    unittest.main()
