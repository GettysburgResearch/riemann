from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "native_qadic_wavelet_square_integral_spectrum.py"
)
OUTPUT_PATH = MODULE_PATH.with_suffix(".json")

SPEC = importlib.util.spec_from_file_location(
    "native_qadic_wavelet_square_integral_spectrum", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load square integral-spectrum producer")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def canonical_sha256(value: object) -> str:
    return hashlib.sha256(MODULE._canonical_bytes(value)).hexdigest()


class NativeQadicWaveletSquareIntegralSpectrumTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = MODULE.build_fixture()
        cls.disk = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))

    def test_fixture_is_canonical(self) -> None:
        self.assertEqual(self.fixture, self.disk)
        claimed = self.fixture["payload_sha256"]
        payload = dict(self.fixture)
        payload.pop("payload_sha256")
        self.assertEqual(claimed, canonical_sha256(payload))

    def test_signed_divisor_bijection_rows(self) -> None:
        rows = self.fixture["compact_intersection"]["cross_sections"]
        self.assertEqual([row["s"] for row in rows], [3, 5, 7, 9, 11, 13])
        self.assertEqual(
            [row["signed_divisors_tested"] for row in rows],
            [16, 48, 36, 48, 60, 48],
        )
        self.assertEqual(
            [row["integral_zero_curve_points"] for row in rows],
            [6, 12, 16, 12, 30, 12],
        )
        self.assertEqual(
            [row["compact_integral_points"] for row in rows],
            [5, 7, 10, 4, 15, 4],
        )
        for row in rows:
            s_value = row["s"]
            c_value = row["C_s"]
            for point in row["compact_rows"]:
                a_value = point["a"]
                b_value = point["b"]
                t_value = point["t"]
                self.assertEqual(t_value, 2 * a_value + s_value + 1)
                self.assertEqual(c_value % t_value, 0)
                self.assertEqual(
                    t_value * b_value,
                    a_value
                    * (
                        a_value * a_value
                        + (s_value + 1) * a_value
                        + s_value * (s_value + 1)
                    ),
                )
                self.assertTrue(MODULE.compact_admissible(a_value, b_value, s_value))

    def test_independent_compact_scan_for_two_small_s(self) -> None:
        expected = {
            row["s"]: {
                (point["a"], point["b"], point["t"]) for point in row["compact_rows"]
            }
            for row in self.fixture["compact_intersection"]["cross_sections"]
        }
        for s_value in (3, 5):
            found: set[tuple[int, int, int]] = set()
            for a_value in range(-4 * s_value, 4 * s_value + 1):
                t_value = 2 * a_value + s_value + 1
                if t_value == 0:
                    continue
                numerator = a_value * (
                    a_value * a_value
                    + (s_value + 1) * a_value
                    + s_value * (s_value + 1)
                )
                if numerator % t_value:
                    continue
                b_value = numerator // t_value
                if MODULE.compact_admissible(a_value, b_value, s_value):
                    found.add((a_value, b_value, t_value))
            self.assertEqual(found, expected[s_value])

    def test_universal_K_zero_points(self) -> None:
        for s_value in (3, 5, 9, 13, 25):
            expected = {
                (0, 0, s_value + 1),
                (s_value - 1, s_value * (s_value - 1), 3 * s_value - 1),
                (-2 * s_value, 2 * s_value * s_value, -(3 * s_value - 1)),
                (-s_value - 1, s_value * (s_value + 1), -(s_value + 1)),
            }
            recovered = set()
            for _, _, t_value in expected:
                point = MODULE.point_from_divisor(s_value, t_value)
                self.assertIsNotNone(point)
                assert point is not None
                self.assertEqual(point["K_sign"], 0)
                recovered.add((point["a"], point["b"], point["t"]))
            self.assertEqual(recovered, expected)

    def test_K_factorization_and_sign_chambers(self) -> None:
        for s_value in (3, 7, 11):
            c_value = (s_value + 1) ** 2 * (3 * s_value - 1)
            for t_value in MODULE.signed_divisors(c_value):
                point = MODULE.point_from_divisor(s_value, t_value)
                if point is None:
                    continue
                a_value = point["a"]
                b_value = point["b"]
                left = (
                    t_value
                    * t_value
                    * (s_value * s_value * a_value * a_value - b_value * b_value)
                )
                right = (
                    a_value**3
                    * (a_value + 2 * s_value)
                    * (s_value - 1 - a_value)
                    * (a_value + s_value + 1)
                )
                self.assertEqual(left, right)
                self.assertEqual(
                    point["K_sign"],
                    (right > 0) - (right < 0),
                )

    def test_resource_and_claim_firewalls(self) -> None:
        resources = self.fixture["resource_contract"]
        self.assertLessEqual(
            resources["symbolic_coefficient_operations"],
            resources["maximum_symbolic_coefficient_operations"],
        )
        self.assertEqual(resources["divisor_trials"], 271)
        self.assertLessEqual(
            resources["divisor_trials"],
            resources["maximum_divisor_trials"],
        )
        self.assertEqual(resources["signed_divisors_evaluated"], 256)
        self.assertLessEqual(
            resources["signed_divisors_evaluated"],
            resources["maximum_signed_divisors"],
        )
        self.assertEqual(
            self.fixture["upstream_payload_lock"], MODULE.EXPECTED_UPSTREAM_PAYLOAD
        )
        firewall = " ".join(self.fixture["firewalls"])
        self.assertIn("not curves", firewall)
        self.assertIn("does not assert", firewall)
        self.assertIn("not a memberwise RH criterion", firewall)
        self.assertIn("novelty", firewall)


if __name__ == "__main__":
    unittest.main()
