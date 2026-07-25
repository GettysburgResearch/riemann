from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
SPEC = importlib.util.spec_from_file_location(
    "verify_log_localizer", ROOT / "verify_log_localizer.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

CERT = ROOT / "certificates" / "synthetic-odd-log-localizer.json"


class LogLocalizerTests(unittest.TestCase):
    def load(self):
        return json.loads(CERT.read_text(encoding="utf-8"))

    def test_order_three_control_is_negative(self):
        result = MODULE.verify(self.load())
        self.assertEqual(result["verdict"], "SYNTHETIC_NEGATIVE_CONTROL")
        row = result["rows"][0]
        self.assertEqual(row["primitive_integer_coefficients"], [-143, 312, -297, 128])
        self.assertEqual(row["coefficient_sum"], 0)
        self.assertEqual(row["status"], "CERTIFIED_NEGATIVE")

    def test_coefficients_annihilate_cubic_background_below_order(self):
        nodes = [Fraction(1, 16), Fraction(1, 4), Fraction(9, 16), Fraction(49, 64)]
        coefficients = MODULE.primitive_oriented_coefficients(nodes)
        for power in range(3):
            self.assertEqual(sum(c * u**power for c, u in zip(coefficients, nodes)), 0)

    def test_common_positive_scale_preserves_negative_sign(self):
        data = self.load()
        for point in data["points"]:
            for endpoint in ("lower", "upper"):
                point["xi_rectangle"]["real"][endpoint]["numerator"] *= 2
        result = MODULE.verify(data)
        self.assertEqual(result["rows"][0]["status"], "CERTIFIED_NEGATIVE")

    def test_even_order_local_factor_has_rh_orientation(self):
        data = self.load()
        data["log_rows"] = [{"id": "even-two", "points": ["q0", "q1", "q2"]}]
        result = MODULE.verify(data)
        self.assertEqual(result["rows"][0]["order"], 2)
        self.assertEqual(result["rows"][0]["status"], "CERTIFIED_NONNEGATIVE")

    def test_reversed_nodes_rejected(self):
        data = self.load()
        data["log_rows"][0]["points"] = ["q0", "q2", "q1", "q3"]
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_boolean_coordinate_rejected(self):
        data = self.load()
        data["points"][0]["x"]["numerator"] = True
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)


if __name__ == "__main__":
    unittest.main()
