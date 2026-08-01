from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from verify import verify  # noqa: E402

CERT = ROOT / "certificates" / "synthetic.json"


class TestVerifier(unittest.TestCase):
    def test_control(self):
        result = verify(CERT)
        self.assertEqual(result["verdict"], "PASS_EXACT_L15632_DIRECT_SHORT_LMI")

    def mutate(self, fn):
        data = json.loads(CERT.read_text())
        fn(data)
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "x.json"
            path.write_text(json.dumps(data))
            with self.assertRaises(ValueError):
                verify(path)

    def test_bad_profile_psd(self):
        self.mutate(lambda d: d["profile"]["es"].update(numerator="2"))

    def test_bad_soft_gate(self):
        self.mutate(
            lambda d: d["profile"]["ss"].update(numerator="1", denominator="1")
        )

    def test_bad_remainder_lmi(self):
        self.mutate(
            lambda d: d["remainder"]["es"].update(numerator="1", denominator="1")
        )

    def test_bad_epsilon(self):
        self.mutate(
            lambda d: d["relative_error"].update(numerator="1", denominator="2")
        )

    def test_bad_ambient(self):
        self.mutate(lambda d: d["profile"]["ee"].update(numerator="0"))


if __name__ == "__main__":
    unittest.main()
