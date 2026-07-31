import importlib.util
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("verify", ROOT / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def base():
    return json.loads((ROOT / "certificates" / "symmetric-finite-control.json").read_text())


class DeterminantMomentGateTests(unittest.TestCase):
    def test_control_passes(self):
        out = VERIFY.verify(base())
        self.assertEqual(out["status"], "CERTIFIED_FINITE_DET2_MOMENT_GATE")

    def test_wrong_trace_rejected(self):
        data = base()
        data["trace_moments"]["4"] = 0
        with self.assertRaises(ValueError):
            VERIFY.verify(data)

    def test_wrong_log_coefficient_rejected(self):
        data = base()
        data["formal_log_coefficients"]["6"] = 0
        with self.assertRaises(ValueError):
            VERIFY.verify(data)

    def test_broken_symmetry_rejected(self):
        data = base()
        data["eigenvalues"][-1] = {"numerator": -1, "denominator": 4}
        eigs = [VERIFY.rat(x) for x in data["eigenvalues"]]
        for m in range(2, data["max_order"] + 1):
            value = sum(x ** m for x in eigs)
            data["trace_moments"][str(m)] = VERIFY.dump_rat(value)
            data["formal_log_coefficients"][str(m)] = VERIFY.dump_rat(
                VERIFY.Fraction((-1) ** (m - 1), m) * value
            )
        with self.assertRaises(ValueError):
            VERIFY.verify(data)

    def test_boolean_rejected(self):
        data = base()
        data["eigenvalues"][0] = True
        with self.assertRaises(ValueError):
            VERIFY.verify(data)

    def test_missing_order_rejected(self):
        data = base()
        del data["trace_moments"]["7"]
        with self.assertRaises(ValueError):
            VERIFY.verify(data)

    def test_false_hankel_request_rejected(self):
        data = base()
        data["hankel_size"] = 4
        with self.assertRaises(ValueError):
            VERIFY.verify(data)


if __name__ == "__main__":
    unittest.main()
