from fractions import Fraction as Q
import importlib.util
from pathlib import Path
import sys
import unittest

SPEC = importlib.util.spec_from_file_location(
    "verify_complex_pick",
    Path(__file__).parents[1] / "verify_complex_pick.py",
)
MOD = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MOD
assert SPEC.loader is not None
SPEC.loader.exec_module(MOD)


def fraction(value: Q) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def binary(value: Q) -> dict[str, str | int]:
    denominator = value.denominator
    assert denominator & (denominator - 1) == 0
    return {
        "mantissa": str(value.numerator),
        "exponent": -(denominator.bit_length() - 1),
    }


def interval(value: Q) -> dict[str, object]:
    return {"lower": fraction(value), "upper": fraction(value)}


def rectangle(value: MOD.Gaussian) -> dict[str, object]:
    return {"real": interval(value.real), "imag": interval(value.imag)}


def point(identifier: str, x: Q, t: Q, value: MOD.Gaussian) -> dict[str, object]:
    return {
        "id": identifier,
        "x": fraction(x),
        "t": fraction(t),
        "f_via_xi": rectangle(value),
        "f_via_parts": rectangle(value),
        "zeta_abs_lower": binary(Q(1, 2)),
    }


def gaussian(real: int, imag: int = 0) -> dict[str, object]:
    return {"real": fraction(Q(real)), "imag": fraction(Q(imag))}


class ExactComplexPickTests(unittest.TestCase):
    def test_complex_contraction_matches_direct_gram(self) -> None:
        xs = [Q(1), Q(2)]
        values = [
            MOD.Gaussian(1 / x + x / (x * x + 1), -Q(1, x * x + 1))
            for x in xs
        ]
        data = {
            "schema": MOD.SCHEMA,
            "points": [
                point(f"p{index}", x, Q(0), value)
                for index, (x, value) in enumerate(zip(xs, values))
            ],
            "checks": [
                {
                    "id": "q",
                    "kind": "complex-pick-rayleigh",
                    "points": ["p0", "p1"],
                    "vector": [gaussian(1, 1), gaussian(2, -1)],
                }
            ],
        }
        output = MOD.verify(data)
        checked = output["checks"][0]
        self.assertEqual(checked["status"], "CERTIFIED_NONNEGATIVE")

        vector = [MOD.Gaussian(1, 1), MOD.Gaussian(2, -1)]
        direct = Q(0)
        for y in [Q(0), Q(1)]:
            amplitude = MOD.Gaussian()
            for value, x in zip(vector, xs):
                amplitude += value.conjugate() / MOD.Gaussian(x, y)
            direct += amplitude.abs_squared()
        norm = sum(value.abs_squared() for value in vector)
        lower = MOD.parse_fraction(checked["normalized_interval"]["lower"], "lower")
        self.assertEqual(lower, direct / norm)

    def test_synthetic_offline_pair_is_negative(self) -> None:
        data = {
            "schema": MOD.SCHEMA,
            "points": [point("p", Q(1), Q(0), MOD.Gaussian(Q(-2, 3), 0))],
            "checks": [
                {
                    "id": "q",
                    "kind": "complex-pick-rayleigh",
                    "points": ["p"],
                    "vector": [gaussian(1, 1)],
                }
            ],
        }
        self.assertEqual(MOD.verify(data)["checks"][0]["status"], "CERTIFIED_NEGATIVE")

    def test_whole_matrix_positive_definite_control(self) -> None:
        xs = [Q(1), Q(2)]
        values = [
            MOD.Gaussian(1 / x + x / (x * x + 1), -Q(1, x * x + 1))
            for x in xs
        ]
        data = {
            "schema": MOD.SCHEMA,
            "points": [
                point(f"p{index}", x, Q(0), value)
                for index, (x, value) in enumerate(zip(xs, values))
            ],
            "checks": [
                {
                    "id": "pd",
                    "kind": "whole-pick-positive-definite",
                    "points": ["p0", "p1"],
                    "delta": fraction(Q(1, 100)),
                }
            ],
        }
        self.assertEqual(
            MOD.verify(data)["checks"][0]["status"],
            "CERTIFIED_POSITIVE_DEFINITE",
        )

    def test_disjoint_assemblies_are_rejected(self) -> None:
        value = point("p", Q(1), Q(0), MOD.Gaussian(1, 0))
        value["f_via_parts"] = rectangle(MOD.Gaussian(2, 0))
        with self.assertRaises(MOD.CertificateError):
            MOD.verify({"schema": MOD.SCHEMA, "points": [value], "checks": []})


if __name__ == "__main__":
    unittest.main()
