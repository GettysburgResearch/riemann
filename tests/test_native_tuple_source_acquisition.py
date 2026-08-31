"""Independent exact controls for the bounded native-source acquisition."""

import copy
import importlib.util
import unittest
from fractions import Fraction as Q
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/exploratory/native_tuple_source_acquisition.py"
SPEC = importlib.util.spec_from_file_location("native_acquisition", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class TestNativeAcquisition(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = M.build_report()

    def reseal(self, report):
        report.pop("payload_sha256", None)
        return M.seal(report)

    def test_tuple(self):
        row = self.report["tuple"]
        self.assertEqual(row["physical_N_M"], [1005930209094, 997518551435])
        self.assertEqual(row["balanced_coefficients"], [0, 2])
        self.assertEqual(row["literal_diagonal"], [1, 150])

    def test_entire_histories(self):
        row = self.report["tuple"]
        self.assertEqual(len(row["left_histories"]), 12)
        self.assertEqual(len(row["right_histories"]), 2)
        self.assertEqual(row["bilateral_coefficients"].count([1, 60]), 12)
        self.assertEqual(row["bilateral_coefficients"].count([-1, 60]), 12)

    def test_half_source_closed_formula(self):
        primes = (71, 73, 79, 83, 89)
        self.assertEqual(M.half_source((), 64), 0)
        for n in range(1, 6):
            expected = -(Q(1, 2) ** n - Q(-1, 2) ** n)
            self.assertEqual(M.half_source(primes[:n], 64), expected)
            self.assertEqual(M.balanced_half(primes[:n], 64), 1 + (-1) ** n)

    def test_beta_integrals(self):
        left, right = self.report["parameters"]
        self.assertEqual(left["Beta_integral"], [0, 1])
        self.assertEqual(right["Beta_integral"], [1, 3])
        self.assertEqual(right["source_first_owner_integral"], [1, 6])
        self.assertEqual(right["source_first_core_integral"], [1, 6])

    def test_raw_mixed_is_different_map(self):
        self.assertEqual(M.beta_owner(3), (Q(-1, 10), Q(1, 10)))
        self.assertEqual(M.beta_owner(2), (Q(1, 6), Q(-1, 6)))

    def test_beta_factorial_route(self):
        for j in range(1, 9):
            owner, core = M.beta_owner(j)
            self.assertEqual(owner, Q(2 * (-1) ** j, (j + 1) * (j + 2)))
            self.assertEqual(owner + core, 0)

    def test_character_coverage(self):
        self.assertEqual(len(self.report["characters"]), 44)
        self.assertEqual(
            [
                sum(row["degree"] == n for row in self.report["characters"])
                for n in range(1, 8)
            ],
            [1, 2, 3, 5, 7, 11, 15],
        )

    def test_s3_virtual_character(self):
        for partition, expected in (
            ((1, 1, 1), (6, 6)),
            ((2, 1), (2, 0)),
            ((3,), (0, 0)),
        ):
            self.assertEqual(M.character_direct(M.representative(partition)), expected)

    def test_odd_transpositions(self):
        for degree in (3, 5, 7):
            sigma = M.representative((2,) + (1,) * (degree - 2))
            self.assertEqual(M.character_formula(sigma), 2)
            plus, minus = M.character_direct(sigma)
            self.assertEqual(plus - minus, 2)

    def test_held_out_depth_eight(self):
        for partition in ((8,), (4, 4), (2, 2, 2, 2), (1,) * 8, (3, 3, 2)):
            sigma = M.representative(partition)
            plus, minus = M.character_direct(sigma)
            self.assertEqual(plus - minus, M.character_formula(sigma))

    def test_native_gate_is_open(self):
        self.assertIs(self.report["contract"]["native_reconstruction_complete"], False)
        self.assertEqual(
            self.report["contract"]["native_zero_or_nonzero"], "undetermined"
        )

    def test_resealed_completion_attack(self):
        bad = copy.deepcopy(self.report)
        bad["contract"]["native_reconstruction_complete"] = True
        with self.assertRaisesRegex(ValueError, "fresh reconstruction"):
            M.check_report(self.reseal(bad))

    def test_resealed_character_attack(self):
        bad = copy.deepcopy(self.report)
        bad["characters"][0]["virtual_character"] = 1
        with self.assertRaisesRegex(ValueError, "fresh reconstruction"):
            M.check_report(self.reseal(bad))

    def test_resealed_measure_attack(self):
        bad = copy.deepcopy(self.report)
        bad["parameters"][1]["source_first_core_integral"] = [-1, 6]
        with self.assertRaisesRegex(ValueError, "fresh reconstruction"):
            M.check_report(self.reseal(bad))

    def test_resealed_diagonal_attack(self):
        bad = copy.deepcopy(self.report)
        bad["tuple"]["literal_diagonal"] = [0, 1]
        with self.assertRaisesRegex(ValueError, "fresh reconstruction"):
            M.check_report(self.reseal(bad))

    def test_payload_attack(self):
        bad = copy.deepcopy(self.report)
        bad["tuple"]["U"] = 65
        with self.assertRaisesRegex(ValueError, "payload seal"):
            M.check_report(bad)

    def test_source_attack(self):
        with (
            mock.patch.object(M, "read_source", return_value=b"forged\n"),
            self.assertRaisesRegex(ValueError, "Git blob"),
        ):
            M.authenticate()

    def test_manifest_attack(self):
        altered = M.manifest()
        altered["schema"] = "forged"
        original = Path.read_bytes

        def read(path):
            return M.canonical(altered) if path == M.MANIFEST else original(path)

        with (
            mock.patch.object(Path, "read_bytes", read),
            self.assertRaisesRegex(ValueError, "manifest mismatch"),
        ):
            M.authenticate()

    def test_source_size_cap(self):
        with self.assertRaises(ValueError):
            M.lf(b"x" * (M.MAX_BYTES + 1))

    def test_unicode_and_control(self):
        self.assertEqual(M.lf("Γ\r\n".encode()), "Γ\n".encode())
        for raw in (b"x\x00", b"x\x7f", "\u0085".encode()):
            with self.assertRaises(ValueError):
                M.lf(raw)

    def test_strict_integers(self):
        for value in (True, False, 3.0, "3", Q(3), None):
            with self.assertRaises(ValueError):
                M.integer(value, 1, 8)

    def test_strict_rationals(self):
        for value in (True, False, 0.5, "1/2", complex(1), None, 1 << 257):
            with self.assertRaises(ValueError):
                M.rational(value)

    def test_support_validation(self):
        for values in ((71, 71), (1,), (True,), (72,), tuple(range(9)), "71"):
            with self.assertRaises(ValueError):
                M.support(values)

    def test_permutation_validation(self):
        for values in ((), (1,), (0, 0), (False,), (0.0,), tuple(range(9)), "0"):
            with self.assertRaises(ValueError):
                M.permutation(values)

    def test_cycle_validation(self):
        for values in ((), (0,), (True,), (1.0,), (9,), "3"):
            with self.assertRaises(ValueError):
                M.representative(values)

    def test_polynomial_caps(self):
        for values in ([0] * 25, [True], [1.5], "0"):
            with self.assertRaises(ValueError):
                M.integral(values)

    def test_json_duplicate(self):
        with self.assertRaises(ValueError):
            M.load_json(b'{"x":1,"x":2}')

    def test_json_number_types(self):
        for raw in (b'{"x":NaN}', b'{"x":Infinity}', b'{"x":1.0}'):
            with self.assertRaises(ValueError):
                M.load_json(raw)

    def test_json_tree_caps(self):
        value = 0
        for _ in range(22):
            value = [value]
        with self.assertRaises(ValueError):
            M.canonical(value)
        with self.assertRaises(ValueError):
            M.canonical({"x": 1 << 257})

    def test_seal_guard(self):
        with self.assertRaises(ValueError):
            M.seal(self.report)

    def test_schema_exact(self):
        bad = copy.deepcopy(self.report)
        bad["extra"] = 0
        with self.assertRaisesRegex(ValueError, "fresh reconstruction"):
            M.check_report(self.reseal(bad))

    def test_boolean_is_not_integer(self):
        bad = copy.deepcopy(self.report)
        bad["characters"][0]["virtual_character"] = False
        with self.assertRaisesRegex(ValueError, "fresh reconstruction"):
            M.check_report(self.reseal(bad))

    def test_release_arithmetic_taxonomy(self):
        expected = {
            "arithmetic_class": "MIXED",
            "components": ["EXACT_RATIONAL", "CERTIFIED_INTEGER_COVERAGE"],
            "rounding": "none",
        }
        for key, value in expected.items():
            self.assertEqual(self.report["contract"][key], value)
            for replacement in (None, "incorrect"):
                bad = copy.deepcopy(self.report)
                if replacement is None:
                    bad["contract"].pop(key)
                else:
                    bad["contract"][key] = replacement
                with (
                    self.subTest(key=key, replacement=replacement),
                    self.assertRaisesRegex(ValueError, "fresh reconstruction"),
                ):
                    M.check_report(self.reseal(bad))


if __name__ == "__main__":
    unittest.main()
