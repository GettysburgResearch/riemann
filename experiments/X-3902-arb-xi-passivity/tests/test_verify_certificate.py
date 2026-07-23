from __future__ import annotations

import importlib.util
import pathlib
import sys
import unittest
from fractions import Fraction

ROOT = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("verify_certificate", ROOT / "verify_certificate.py")
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = module
spec.loader.exec_module(module)

CertificateError = module.CertificateError
binary_json = module.binary_json
fraction_json = module.fraction_json
verify_certificate = module.verify_certificate


def b(value: Fraction | int) -> dict[str, object]:
    return binary_json(Fraction(value))


def interval(mid: Fraction | int, radius: Fraction = Fraction(0)) -> dict[str, object]:
    mid = Fraction(mid)
    return {"lower": b(mid - radius), "upper": b(mid + radius)}


def rectangle(real: Fraction | int, imag: Fraction | int = 0, radius: Fraction = Fraction(0)) -> dict[str, object]:
    return {"real": interval(real, radius), "imag": interval(imag, radius)}


def point(identifier: str, x: Fraction, t: Fraction, real: Fraction, radius: Fraction = Fraction(0)) -> dict[str, object]:
    return {
        "id": identifier,
        "x": fraction_json(x),
        "t": fraction_json(t),
        "f_via_xi": rectangle(real, 0, radius),
        "f_via_parts": rectangle(real, 0, radius * 2),
        "zeta_abs_lower": b(Fraction(1, 2)),
        "reflected": {
            "x": fraction_json(-x),
            "t": fraction_json(-t),
            "f_via_xi": rectangle(-real, 0, radius),
            "f_via_parts": rectangle(-real, 0, radius * 2),
            "zeta_abs_lower": b(Fraction(1, 2)),
        },
    }


def certificate(points: list[dict[str, object]], channels: list[dict[str, object]]) -> dict[str, object]:
    return {
        "schema": module.SCHEMA,
        "producer": {"backend": "synthetic exact test"},
        "points": points,
        "channels": channels,
        "declared_channel_ids": [str(channel["id"]) for channel in channels],
    }


class CheckerTests(unittest.TestCase):
    def test_scalar_negative(self) -> None:
        data = certificate(
            [point("p", Fraction(1), Fraction(10), Fraction(-1), Fraction(1, 16))],
            [{"id": "scalar", "kind": "scalar", "point": "p"}],
        )
        result = verify_certificate(data)
        self.assertEqual(result["negative_channels"], ["scalar"])

    def test_positive_values_negative_two_channel_B(self) -> None:
        data = certificate(
            [point("p1", Fraction(1), Fraction(20), Fraction(10)), point("p2", Fraction(2), Fraction(20), Fraction(1))],
            [{"id": "B", "kind": "two-channel-B", "points": ["p1", "p2"]}],
        )
        result = verify_certificate(data)
        channel = result["channels"][0]
        self.assertEqual(channel["status"], "CERTIFIED_NEGATIVE")
        self.assertEqual(Fraction(int(channel["interval"]["upper"]["numerator"]), int(channel["interval"]["upper"]["denominator"])), Fraction(-8, 3))

    def test_positive_values_negative_two_channel_A(self) -> None:
        data = certificate(
            [point("p1", Fraction(1), Fraction(20), Fraction(1)), point("p2", Fraction(2), Fraction(20), Fraction(10))],
            [{"id": "A", "kind": "two-channel-A", "points": ["p1", "p2"]}],
        )
        self.assertEqual(verify_certificate(data)["channels"][0]["status"], "CERTIFIED_NEGATIVE")

    def test_real_pick_contracts_before_enclosure(self) -> None:
        data = certificate(
            [point("p1", Fraction(1), Fraction(20), Fraction(1)), point("p2", Fraction(2), Fraction(20), Fraction(4))],
            [{"id": "pick", "kind": "real-pick-rayleigh", "points": ["p1", "p2"], "vector": [fraction_json(Fraction(1)), fraction_json(Fraction(-1))]}],
        )
        channel = verify_certificate(data)["channels"][0]
        self.assertEqual(channel["status"], "CERTIFIED_NEGATIVE")
        coefficients = [Fraction(int(x["numerator"]), int(x["denominator"])) for x in channel["reconstruction"]["contracted_coefficients"]]
        self.assertEqual(coefficients, [Fraction(1, 3), Fraction(-1, 6)])

    def test_divided_difference_orientation(self) -> None:
        points = [point(identifier, x, Fraction(30), x) for identifier, x in [("a", Fraction(1)), ("b", Fraction(2)), ("c", Fraction(3))]]
        data = certificate(points, [{"id": "dd2", "kind": "bernstein-divided-difference", "points": ["a", "b", "c"]}])
        self.assertEqual(verify_certificate(data)["channels"][0]["status"], "CERTIFIED_NONNEGATIVE")

    def test_zero_touch_is_unresolved(self) -> None:
        data = certificate([point("p", Fraction(1), Fraction(10), Fraction(0), Fraction(1, 16))], [{"id": "scalar", "kind": "scalar", "point": "p"}])
        self.assertEqual(verify_certificate(data)["unresolved_channels"], ["scalar"])

    def test_disjoint_assemblies_rejected(self) -> None:
        data = certificate([point("p", Fraction(1), Fraction(10), Fraction(1))], [{"id": "scalar", "kind": "scalar", "point": "p"}])
        data["points"][0]["f_via_parts"] = rectangle(2)
        with self.assertRaises(CertificateError):
            verify_certificate(data)

    def test_functional_equation_failure_rejected(self) -> None:
        data = certificate([point("p", Fraction(1), Fraction(10), Fraction(1))], [{"id": "scalar", "kind": "scalar", "point": "p"}])
        data["points"][0]["reflected"]["f_via_xi"] = rectangle(1)
        data["points"][0]["reflected"]["f_via_parts"] = rectangle(1)
        with self.assertRaises(CertificateError):
            verify_certificate(data)

    def test_zero_denominator_gate_rejected(self) -> None:
        data = certificate([point("p", Fraction(1), Fraction(10), Fraction(1))], [{"id": "scalar", "kind": "scalar", "point": "p"}])
        data["points"][0]["zeta_abs_lower"] = b(0)
        with self.assertRaises(CertificateError):
            verify_certificate(data)

    def test_wrong_reflected_point_rejected(self) -> None:
        data = certificate([point("p", Fraction(1), Fraction(10), Fraction(1))], [{"id": "scalar", "kind": "scalar", "point": "p"}])
        data["points"][0]["reflected"]["t"] = fraction_json(Fraction(10))
        with self.assertRaises(CertificateError):
            verify_certificate(data)

    def test_hidden_or_decorative_channel_rejected(self) -> None:
        data = certificate([point("p", Fraction(1), Fraction(10), Fraction(1))], [{"id": "scalar", "kind": "scalar", "point": "p"}])
        data["declared_channel_ids"] = ["scalar", "decorative"]
        with self.assertRaises(CertificateError):
            verify_certificate(data)

    def test_mutated_claim_rejected(self) -> None:
        data = certificate([point("p", Fraction(1), Fraction(10), Fraction(1))], [{"id": "scalar", "kind": "scalar", "point": "p", "claimed_status": "CERTIFIED_NEGATIVE"}])
        with self.assertRaises(CertificateError):
            verify_certificate(data)


if __name__ == "__main__":
    unittest.main()
