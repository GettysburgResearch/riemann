import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("verify", ROOT / "verify.py")
verify = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(verify)


class TestTernaryNegativeCertificate(unittest.TestCase):
    def test_retained_intervals(self):
        obj = verify.proof_object()
        self.assertTrue(obj["strictly_negative"])
        self.assertTrue(obj["nested"])
        self.assertEqual(obj["X"], 10_000_000)
        self.assertEqual(obj["n"], 63)

    def test_scope(self):
        obj = verify.proof_object()
        self.assertIn("Refutes TFP only", obj["scope"])


if __name__ == "__main__":
    unittest.main()
