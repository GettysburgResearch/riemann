import copy
import unittest
from fractions import Fraction

from cross_height import Gaussian, fraction_json, matched_pole_vector
from verify_certificate import CertificateError
from verify_cross_height_certificate import verify_certificate


def rectangle(value):
    return {
        "real": {"lower": fraction_json(value.real), "upper": fraction_json(value.real)},
        "imag": {"lower": fraction_json(value.imag), "upper": fraction_json(value.imag)},
    }


def make_certificate(off_line=True):
    center = Fraction(37)
    nodes = [
        Gaussian(Fraction(1, 16), Fraction(0)),
        Gaussian(Fraction(1, 8), Fraction(-1, 32)),
        Gaussian(Fraction(1, 4), Fraction(1, 16)),
    ]
    model_d = Fraction(9, 1024)
    vector = matched_pole_vector(nodes, model_d)
    if off_line:
        values = [2 * node / (node * node - model_d) for node in nodes]
    else:
        roots = [Gaussian(0, Fraction(-2)), Gaussian(0, Fraction(1, 3))]
        values = [sum((1 / (node - root) for root in roots), Gaussian(0)) for node in nodes]
    points = []
    identifiers = []
    for index, (node, value) in enumerate(zip(nodes, values)):
        identifier = f"p{index}"
        identifiers.append(identifier)
        points.append({
            "id": identifier,
            "x": fraction_json(node.real),
            "t": fraction_json(center + node.imag),
            "f_via_xi": rectangle(value),
            "f_via_parts": rectangle(value),
            "zeta_abs_lower": {"mantissa": "1", "exponent": 0},
        })
    channel = {
        "id": "packet",
        "kind": "complex-matched-pole-rayleigh",
        "points": identifiers,
        "vector": [value.to_json() for value in vector],
        "model_center_t": fraction_json(center),
        "model_d": fraction_json(model_d),
    }
    return {
        "schema": "riemann.xi-passivity-value-balls.v1",
        "points": points,
        "channels": [channel],
        "declared_channel_ids": ["packet"],
    }


class CrossHeightVerifierTests(unittest.TestCase):
    def test_off_line_pair_is_negative(self):
        result = verify_certificate(make_certificate(True))
        self.assertEqual(result["channels"][0]["status"], "CERTIFIED_NEGATIVE")
        self.assertTrue(result["negative_channels"])

    def test_critical_line_model_is_nonnegative(self):
        result = verify_certificate(make_certificate(False))
        self.assertEqual(result["channels"][0]["status"], "CERTIFIED_NONNEGATIVE")
        self.assertFalse(result["negative_channels"])

    def test_vector_mutation_is_rejected(self):
        certificate = make_certificate(True)
        mutated = copy.deepcopy(certificate)
        mutated["channels"][0]["vector"][0]["real"] = fraction_json(Fraction(999))
        with self.assertRaises(CertificateError):
            verify_certificate(mutated)

    def test_declared_manifest_is_closed(self):
        certificate = make_certificate(True)
        certificate["declared_channel_ids"] = []
        with self.assertRaises(CertificateError):
            verify_certificate(certificate)


if __name__ == "__main__":
    unittest.main()
