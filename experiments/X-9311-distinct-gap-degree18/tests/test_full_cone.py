from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


builder = load_module("builder", ROOT / "build_moments.py")
checker = load_module("checker", ROOT / "verify_full_cone.py")


def basis_payload(moments: list[int]) -> dict:
    return {
        "schema": checker.MOMENT_SCHEMA,
        "classification": "SYNTHETIC",
        "response_degree_bound": len(moments) - 1,
        "basis_rows": [
            {
                "degree": index,
                "lower_exact_decimal": str(value),
                "upper_exact_decimal": str(value),
            }
            for index, value in enumerate(moments)
        ],
    }


def verify_payload(payload: dict) -> dict:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "moments.json"
        path.write_text(json.dumps(payload), encoding="utf-8")
        return checker.verify(path)


class KernelTests(unittest.TestCase):
    def test_basis_polynomial_identity(self) -> None:
        nodes = [Fraction(1), Fraction(2), Fraction(4)]
        for degree in range(2):
            beta = builder.basis_vector(nodes, degree)
            self.assertEqual(sum(beta), 0)
            self.assertEqual(
                builder.response_polynomial(nodes, beta),
                [Fraction(0)] * degree + [Fraction(1)],
            )

    def test_exact_log_enclosure(self) -> None:
        log = builder.ExactLogEncloser(80)
        value = log(Fraction(3, 2))
        self.assertLess(value.lower, Fraction(406, 1000))
        self.assertGreater(value.upper, Fraction(405, 1000))
        self.assertLess(value.upper - value.lower, Fraction(1, 10**60))

    def test_binary_log_reduction_large_and_small(self) -> None:
        for value in (Fraction(3 * (1 << 100), 2), Fraction(3, 1 << 101)):
            reduced, _ = builder.ExactLogEncloser._reduce(value)
            self.assertGreaterEqual(reduced, 1)
            self.assertLess(reduced, 2)

    def test_positive_full_degree4_cone(self) -> None:
        # Moments of delta_1 + delta_2 + delta_4.
        result = verify_payload(basis_payload([3, 7, 21, 73, 273]))
        self.assertEqual(result["verdict"], "CERTIFIED_POSITIVE_FULL_DEGREE18_HALF_LINE_CONE")
        self.assertEqual(result["h0_dimension"], 3)
        self.assertEqual(result["h1_dimension"], 2)

    def test_negative_square_is_exactly_replayed(self) -> None:
        result = verify_payload(basis_payload([3, 7, 21, 73, -100]))
        self.assertEqual(result["verdict"], "CERTIFIED_NEGATIVE_DEGREE18_SQUARE_WITNESS")
        interval = result["h0_witness_interval"]
        self.assertLess(int(interval["upper"]["numerator"]), 0)

    def test_rejects_nonconsecutive_degrees(self) -> None:
        payload = basis_payload([3, 7, 21])
        payload["basis_rows"][1]["degree"] = 2
        with self.assertRaises(checker.VerificationError):
            verify_payload(payload)

    def test_wide_interval_remains_unresolved(self) -> None:
        payload = basis_payload([3, 7, 21, 73, 273])
        payload["basis_rows"][0]["lower_exact_decimal"] = "-1000"
        payload["basis_rows"][0]["upper_exact_decimal"] = "1000"
        result = verify_payload(payload)
        self.assertEqual(result["verdict"], "UNRESOLVED_DEGREE18_HALF_LINE_CONE")


if __name__ == "__main__":
    unittest.main()
