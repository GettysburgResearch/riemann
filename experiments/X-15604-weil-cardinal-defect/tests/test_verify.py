import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x15604", ROOT / "verify.py")
V = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = V
SPEC.loader.exec_module(V)


def certificate():
    return {
        "schema": "riemann.x15604-weil-cardinal-defect.v1",
        "classification": "SYNTHETIC_ZERO_CONFIGURATION",
        "radical_dimension": 2,
        "zeros": [
            {"id": "g1", "conjugate": "g1", "multiplicity": 1, "deflated": True},
            {"id": "g2", "conjugate": "g2", "multiplicity": 2, "deflated": True},
            {"id": "rho", "conjugate": "rhobar", "multiplicity": 1, "deflated": False},
            {"id": "rhobar", "conjugate": "rho", "multiplicity": 1, "deflated": False},
        ],
        "expected": {
            "inertia": {"positive": 3, "negative": 1, "zero": 2},
            "residual_inertia": {"positive": 1, "negative": 1, "zero": 4},
            "off_line_negative_pair": ["rho", "rhobar"],
            "off_line_negative_quadratic": {"numerator": -2, "denominator": 1},
        },
        "schur_control": {
            "ideal_min": {"numerator": -1, "denominator": 1},
            "block_error": {"numerator": 1, "denominator": 100},
            "cross_squared": {"numerator": 1, "denominator": 400},
            "complement_floor": {"numerator": 1, "denominator": 2},
            "claimed_floor": {"numerator": -203, "denominator": 200},
        },
    }


class CardinalDefectTests(unittest.TestCase):
    def test_exact_control(self):
        result = V.verify(certificate())
        self.assertEqual(result["inertia"], {"positive": 3, "negative": 1, "zero": 2})
        self.assertEqual(result["negative_witness"]["quadratic"], {"numerator": -2, "denominator": 1})
        self.assertEqual(result["schur_control"]["floor"], {"numerator": -203, "denominator": 200})

    def test_line_only_deflation_is_radical(self):
        data = certificate()
        data["zeros"] = data["zeros"][:2]
        data["expected"] = {
            "inertia": {"positive": 2, "negative": 0, "zero": 2},
            "residual_inertia": {"positive": 0, "negative": 0, "zero": 4},
        }
        data["schur_control"]["ideal_min"] = {"numerator": 0, "denominator": 1}
        data["schur_control"]["claimed_floor"] = {"numerator": -3, "denominator": 200}
        result = V.verify(data)
        self.assertEqual(result["residual_inertia"], {"positive": 0, "negative": 0, "zero": 4})
        self.assertEqual(result["schur_control"]["floor"], {"numerator": -3, "denominator": 200})

    def test_bad_conjugation_rejected(self):
        data = certificate()
        data["zeros"][2]["conjugate"] = "g1"
        with self.assertRaises(V.VerificationError):
            V.verify(data)

    def test_multiplicity_mismatch_rejected(self):
        data = certificate()
        data["zeros"][3]["multiplicity"] = 2
        with self.assertRaises(V.VerificationError):
            V.verify(data)

    def test_off_line_deflation_rejected(self):
        data = certificate()
        data["zeros"][2]["deflated"] = True
        with self.assertRaises(V.VerificationError):
            V.verify(data)

    def test_false_inertia_rejected(self):
        data = certificate()
        data["expected"]["inertia"]["negative"] = 0
        with self.assertRaises(V.VerificationError):
            V.verify(data)

    def test_false_negative_witness_rejected(self):
        data = certificate()
        data["expected"]["off_line_negative_quadratic"] = {"numerator": -1, "denominator": 1}
        with self.assertRaises(V.VerificationError):
            V.verify(data)

    def test_nonpositive_complement_rejected(self):
        data = certificate()
        data["schur_control"]["complement_floor"] = {"numerator": 0, "denominator": 1}
        with self.assertRaises(V.VerificationError):
            V.verify(data)

    def test_false_schur_floor_rejected(self):
        data = certificate()
        data["schur_control"]["claimed_floor"] = {"numerator": -1, "denominator": 1}
        with self.assertRaises(V.VerificationError):
            V.verify(data)

    def test_boolean_integer_rejected(self):
        data = certificate()
        data["radical_dimension"] = True
        with self.assertRaises(V.VerificationError):
            V.verify(data)


if __name__ == "__main__":
    unittest.main()
