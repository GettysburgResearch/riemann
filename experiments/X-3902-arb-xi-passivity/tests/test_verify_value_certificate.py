from __future__ import annotations

import importlib.util
import pathlib
import sys
import unittest
from fractions import Fraction

ROOT = pathlib.Path(__file__).resolve().parents[1]
for name in ("verify_certificate", "verify_value_certificate"):
    spec = importlib.util.spec_from_file_location(name, ROOT / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[name] = module
    spec.loader.exec_module(module)

base = sys.modules["verify_certificate"]
value_checker = sys.modules["verify_value_certificate"]


def b(value: Fraction | int) -> dict[str, object]:
    return base.binary_json(Fraction(value))


def interval(mid: Fraction | int, radius: Fraction = Fraction(0)) -> dict[str, object]:
    mid = Fraction(mid)
    return {"lower": b(mid - radius), "upper": b(mid + radius)}


def rectangle(real: Fraction | int, radius: Fraction = Fraction(0)) -> dict[str, object]:
    return {"real": interval(real, radius), "imag": interval(0, radius)}


def certificate(real: Fraction, radius: Fraction = Fraction(0)) -> dict[str, object]:
    return {
        "schema": value_checker.SCHEMA,
        "points": [
            {
                "id": "p",
                "x": base.fraction_json(Fraction(1, 1024)),
                "t": base.fraction_json(Fraction(3_000_000_000_001)),
                "f_via_xi": rectangle(real, radius),
                "f_via_parts": rectangle(real, radius * 2),
                "zeta_abs_lower": b(Fraction(1, 2)),
            }
        ],
        "channels": [{"id": "scalar", "kind": "scalar", "point": "p"}],
        "declared_channel_ids": ["scalar"],
    }


class ValueCheckerTests(unittest.TestCase):
    def test_negative_scalar(self) -> None:
        result = value_checker.verify_certificate(certificate(Fraction(-1), Fraction(1, 16)))
        self.assertEqual(result["negative_channels"], ["scalar"])

    def test_disjoint_assemblies_fail(self) -> None:
        data = certificate(Fraction(1))
        data["points"][0]["f_via_parts"] = rectangle(Fraction(2))
        with self.assertRaises(base.CertificateError):
            value_checker.verify_certificate(data)

    def test_zero_denominator_fail(self) -> None:
        data = certificate(Fraction(1))
        data["points"][0]["zeta_abs_lower"] = b(0)
        with self.assertRaises(base.CertificateError):
            value_checker.verify_certificate(data)

    def test_point_not_right_of_line_fails(self) -> None:
        data = certificate(Fraction(1))
        data["points"][0]["x"] = base.fraction_json(Fraction(0))
        with self.assertRaises(base.CertificateError):
            value_checker.verify_certificate(data)

    def test_declared_channel_contract(self) -> None:
        data = certificate(Fraction(1))
        data["declared_channel_ids"] = ["scalar", "hidden"]
        with self.assertRaises(base.CertificateError):
            value_checker.verify_certificate(data)


if __name__ == "__main__":
    unittest.main()
