import json
import sys
import unittest
from decimal import localcontext
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import generate


class GeneratedCertificateTests(unittest.TestCase):
    def test_generated_certificate(self):
        control = json.loads((HERE / "certificates" / "control.json").read_text())
        with localcontext() as ctx:
            ctx.prec = int(control["precision"])
            payload = generate.generate(64)
        self.assertEqual(payload["endpoint"], 64)
        self.assertEqual(payload["largest_slack_column"], 1)
        self.assertLess(abs(float(payload["native_deficit"])), 1e-50)
        self.assertFalse(payload["rh_established"])


if __name__ == "__main__":
    unittest.main()
