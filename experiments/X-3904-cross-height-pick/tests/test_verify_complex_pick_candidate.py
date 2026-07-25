import copy
import unittest
from fractions import Fraction

from cross_height import Gaussian, fraction_json
from verify_certificate import CertificateError
from verify_complex_pick_candidate import verify_certificate


def rectangle(value: Gaussian):
    return {
        "real": {"lower": fraction_json(value.real), "upper": fraction_json(value.real)},
        "imag": {"lower": fraction_json(value.imag), "upper": fraction_json(value.imag)},
    }


def base_certificate(values, *, vector_real, vector_imag, scale_bits=0, t_values=(0, 0)):
    points = []
    for index, (x, t, value) in enumerate(
        zip((Fraction(1), Fraction(2)), t_values, values)
    ):
        points.append(
            {
                "id": f"p{index}",
                "x": fraction_json(x),
                "t": fraction_json(Fraction(t)),
                "f_via_xi": rectangle(value),
                "f_via_parts": rectangle(value),
                "zeta_abs_lower": {"mantissa": "1", "exponent": 0},
            }
        )
    channel = {
        "id": "candidate",
        "kind": "complex-pick-rayleigh",
        "points": ["p0", "p1"],
        "vector": {
            "scale_bits": scale_bits,
            "real_numerators": vector_real,
            "imag_numerators": vector_imag,
        },
        "source_nomination": {"frozen_before_replay": True},
    }
    return {
        "schema": "riemann.xi-passivity-value-balls.v1",
        "points": points,
        "channels": [channel],
        "declared_channel_ids": ["candidate"],
    }


class ComplexPickCandidateTests(unittest.TestCase):
    def test_synthetic_offline_pair_is_negative(self):
        d = Fraction(9, 4)
        values = [
            Gaussian(2 * x / (x * x - d))
            for x in (Fraction(1), Fraction(2))
        ]
        certificate = base_certificate(
            values,
            vector_real=[1, 0],
            vector_imag=[0, 0],
        )
        result = verify_certificate(certificate)
        self.assertEqual(result["channels"][0]["status"], "CERTIFIED_NEGATIVE")

    def test_finite_critical_line_model_is_nonnegative_cross_height(self):
        points = [Gaussian(Fraction(1), Fraction(-1, 2)), Gaussian(Fraction(2), Fraction(3, 4))]
        roots = [Gaussian(0, Fraction(-2)), Gaussian(0, Fraction(1, 3)), Gaussian(0, Fraction(5, 2))]
        values = [sum((1 / (point - root) for root in roots), Gaussian(0)) for point in points]
        certificate = base_certificate(
            values,
            vector_real=[1, -1],
            vector_imag=[1, 2],
            t_values=(Fraction(-1, 2), Fraction(3, 4)),
        )
        result = verify_certificate(certificate)
        self.assertEqual(result["channels"][0]["status"], "CERTIFIED_NONNEGATIVE")

    def test_zero_vector_rejected(self):
        certificate = base_certificate(
            [Gaussian(1), Gaussian(1)],
            vector_real=[0, 0],
            vector_imag=[0, 0],
        )
        with self.assertRaises(CertificateError):
            verify_certificate(certificate)

    def test_point_order_mutation_changes_identity(self):
        certificate = base_certificate(
            [Gaussian(1), Gaussian(2)],
            vector_real=[1, 2],
            vector_imag=[0, 0],
        )
        original = verify_certificate(certificate)["channels"][0]["interval"]
        mutated = copy.deepcopy(certificate)
        mutated["channels"][0]["points"].reverse()
        changed = verify_certificate(mutated)["channels"][0]["interval"]
        self.assertNotEqual(original, changed)

    def test_declared_manifest_is_closed(self):
        certificate = base_certificate(
            [Gaussian(1), Gaussian(2)],
            vector_real=[1, 2],
            vector_imag=[0, 0],
        )
        certificate["declared_channel_ids"] = []
        with self.assertRaises(CertificateError):
            verify_certificate(certificate)


if __name__ == "__main__":
    unittest.main()
