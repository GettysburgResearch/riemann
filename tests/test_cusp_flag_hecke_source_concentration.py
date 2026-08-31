"""Bounded exact controls and fail-closed tests; not an analytic proof engine."""

import copy
import importlib.util
import itertools
import json
import math
import unittest
from fractions import Fraction
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
PATH = (
    ROOT
    / "research/l-families/atlas/generalized/cusp_flag_hecke_source_concentration.py"
)
SPEC = importlib.util.spec_from_file_location("hecke_concentration", PATH)
P = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(P)


def product(a, b):
    return [sum(a[i] * b[n - i] for i in range(n + 1)) for n in range(len(a))]


def power(a, n):
    out = [1] + [0] * (len(a) - 1)
    for _ in range(n):
        out = product(out, a)
    return out


def delta_product(order):
    out = [1] + [0] * (order - 1)
    for n in range(1, order):
        factor = [0] * order
        for j in range(min(24, (order - 1) // n) + 1):
            factor[j * n] = (-1) ** j * math.comb(24, j)
        out = product(out, factor)
    return [0] + out


def independent_basis(d, r, order):
    a, b = {0: (0, 0), 4: (1, 0), 6: (0, 1), 8: (2, 0), 10: (1, 1), 14: (2, 1)}[r]
    e4 = [1] + [
        240 * sum(j**3 for j in range(1, n + 1) if n % j == 0)
        for n in range(1, order + 1)
    ]
    e6 = [1] + [
        -504 * sum(j**5 for j in range(1, n + 1) if n % j == 0)
        for n in range(1, order + 1)
    ]
    delta = delta_product(order)
    basis = [
        product(power(delta, j), product(power(e4, 3 * (d - j) + a), power(e6, b)))
        for j in range(1, d + 1)
    ]
    # Forward pivot row operations, in a different order from the producer.
    for pivot in range(1, d):
        for earlier in range(pivot):
            coefficient = basis[earlier][pivot + 1]
            basis[earlier] = [
                x - coefficient * y for x, y in zip(basis[earlier], basis[pivot])
            ]
    return basis


def reseal(value):
    value.pop("payload_sha256", None)
    value["payload_sha256"] = P.digest(P.encoded(value))
    return value


class TestHeckeConcentration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.expected = P.fixture()

    def test_01_fixture(self):
        P.validate(P.read_json(ROOT / P.DIR / f"{P.STEM}.json"))

    def test_02_source_authentication(self):
        P.authenticate_sources()
        self.assertEqual(len(P.PINS), 7)

    def test_03_independent_delta(self):
        self.assertEqual(delta_product(18), P.modular_series(18, P.Budget())[2])

    def test_04_independent_all_echelon_prefixes(self):
        for row in self.expected["q_rows"]:
            self.assertEqual(
                independent_basis(row["d"], row["residual"], row["q_order"]),
                row["basis"],
            )

    def test_05_weight24_charpoly_and_eigenvectors(self):
        row = self.expected["q_rows"][0]
        t2, t3 = row["T2"], row["T3"]
        self.assertEqual(t2[0][0] + t2[1][1], 1080)
        self.assertEqual(t2[0][0] * t2[1][1] - t2[0][1] * t2[1][0], -20468736)
        self.assertEqual(1080**2 + 4 * 20468736, 24**2 * 144169)
        self.assertEqual(
            t3,
            [
                [195660 - 48 * t2[0][0], -48 * t2[0][1]],
                [-48 * t2[1][0], 195660 - 48 * t2[1][1]],
            ],
        )
        # Eigenvectors (1,alpha) satisfy alpha^2=1080alpha+20468736 exactly.
        self.assertEqual(t2[1], [20468736, 1080])

    def test_06_independent_hecke_six(self):
        for row in self.expected["q_rows"]:
            d, k = row["d"], row["k"]
            order = 6 * d
            basis = independent_basis(d, row["residual"], order)
            t6 = [
                [
                    sum(
                        h ** (k - 1) * basis[j][6 * n // (h * h)]
                        for h in (1, 2, 3, 6)
                        if n % h == 0
                    )
                    for j in range(d)
                ]
                for n in range(1, d + 1)
            ]
            t2, t3 = row["T2"], row["T3"]
            actual = [
                [sum(t2[i][a] * t3[a][j] for a in range(d)) for j in range(d)]
                for i in range(d)
            ]
            self.assertEqual(t6, actual)

    def test_07_trace_not_diagonal(self):
        vectors = [(Fraction(1), Fraction(2)), (Fraction(3), Fraction(-1))]
        weights = [Fraction(1, 7), Fraction(2, 9)]
        gram = [
            [sum(w * v[i] * v[j] for w, v in zip(weights, vectors)) for j in range(2)]
            for i in range(2)
        ]
        trace = gram[0][0] + gram[1][1]
        self.assertNotEqual(gram[0][1], 0)
        for x, y in itertools.product(range(-3, 4), repeat=2):
            quadratic = gram[0][0] * x * x + 2 * gram[0][1] * x * y + gram[1][1] * y * y
            self.assertGreaterEqual(quadratic, 0)
            self.assertLessEqual(quadratic, trace * (x * x + y * y))

    def test_08_gamma_moments(self):
        for k, pair in self.expected["controls"]["gamma_fourth"]:
            self.assertEqual(
                Fraction(*pair),
                Fraction(math.factorial(k + 3), math.factorial(k - 1) * k**4),
            )
            self.assertLessEqual(Fraction(*pair), 24)

    def test_09_floor_sums(self):
        for n, left, gap in self.expected["controls"]["floor"]:
            self.assertEqual(left, sum(range(1, n // 2 + 1)))
            self.assertEqual(Fraction(*gap), Fraction(n, 2) ** 2 - left)

    def test_10_divisor_domination(self):
        for n in range(1, 65):
            divisors = [d for d in range(1, n + 1) if n % d == 0]
            d4 = sum(
                1
                for a in divisors
                for b in divisors
                for c in divisors
                if n % (a * b * c) == 0
            )
            self.assertLessEqual(len(divisors) ** 2, d4)
            self.assertLessEqual(len(divisors) ** 2, 4 * n)

    def test_11_harmonic_direct_grouping(self):
        for n, actual, upper in self.expected["controls"]["harmonic"]:
            if n > 8:
                continue
            left = sum(
                (
                    Fraction(1, a * b * c * d)
                    for a, b, c, d in itertools.product(range(1, n + 1), repeat=4)
                    if a * b * c * d <= n
                ),
                Fraction(),
            )
            self.assertEqual(left, Fraction(*actual))
            self.assertLessEqual(left, Fraction(*upper))

    def test_12_completion_and_cusp_constants(self):
        for k in range(24, 63, 2):
            # Powers of2 in A_k(s) and the product of the two completed factors.
            for s in (2, 3, 7):
                self.assertEqual((-2 * s - 2 * k + 2) - (3 - 2 * s - k), -k - 1)
            self.assertEqual(Fraction(2 * (k - 1), 4), Fraction(k - 1, 2))
        for row in self.expected["controls"]["cusp_constants"]:
            eta, k = Fraction(*row["eta"]), row["k"]
            self.assertGreaterEqual(eta * k, 1)
            self.assertEqual(
                Fraction(*row["mass_coefficient_over_L"]), 1 / (2 * eta**2 * k)
            )

    def test_13_dimension_caps(self):
        for value in (True, 2.0, 1, 5, -1):
            with self.assertRaises(P.Rejected):
                P.echelon(value, 0, 12, 0, P.Budget())

    def test_14_class_and_order_caps(self):
        for residual in (2, 12, True, 0.0):
            with self.assertRaises(P.Rejected):
                P.echelon(2, residual, 12, 0, P.Budget())
        for order in (0, 19, True, 12.0):
            with self.assertRaises(P.Rejected):
                P.echelon(2, 0, order, 0, P.Budget())

    def test_15_work_budget(self):
        with self.assertRaises(P.Rejected):
            P.modular_series(18, P.Budget(1))
        for limit in (0, True, 1.0, P.CAPS["work"] + 1):
            with self.assertRaises(P.Rejected):
                P.Budget(limit)

    def test_16_series_arithmetic_caps(self):
        for vector in ([0, True], [0, 1.0], [0, 1 << 4097], [0], [0] * 20):
            with self.assertRaises(P.Rejected):
                P.mul(vector, vector, P.Budget())

    def test_17_prime_and_action_coverage(self):
        basis = self.expected["q_rows"][0]["basis"]
        for prime in (True, 2.0, 1, 5):
            with self.assertRaises(P.Rejected):
                P.hecke(basis, 24, prime, P.Budget())
        with self.assertRaises(P.Rejected):
            P.hecke([b[:9] for b in basis], 24, 3, P.Budget())

    def test_18_malformed_matrix(self):
        for a in (None, [[1, 2]], [[True]], [[1 << 4097]]):
            with self.assertRaises(P.Rejected):
                P.matmul(a, a, P.Budget())
        huge = 1 << 3000
        with self.assertRaises(P.Rejected):
            P.matmul(
                [[huge, -huge], [huge, -huge]], [[huge, huge], [huge, huge]], P.Budget()
            )

    def test_19_duplicate_keys(self):
        with self.assertRaises(P.Rejected):
            P.decode(b'{"x":1,"x":2}')

    def test_20_nonfinite_and_type_drift(self):
        for text in (b"NaN", b"Infinity", b"-Infinity", b"true", b"null", b"1.0"):
            with self.assertRaises(P.Rejected):
                P.decode(text)

    def test_21_json_caps(self):
        for value in ([0] * 1025, "x" * 4097, 1 << 4097):
            with self.assertRaises(P.Rejected):
                P.typed(value)
        value = 0
        for _ in range(26):
            value = [value]
        with self.assertRaises(P.Rejected):
            P.typed(value)
        with self.assertRaises(P.Rejected):
            P.decode(b" " * (P.CAPS["json_bytes"] + 1))

    def test_22_resealed_q_coefficient(self):
        bad = copy.deepcopy(self.expected)
        bad["q_rows"][0]["basis"][0][3] += 1
        with self.assertRaises(P.Rejected):
            P.validate(reseal(bad))

    def test_23_resealed_hecke(self):
        bad = copy.deepcopy(self.expected)
        bad["q_rows"][0]["T2"][1][0] += 1
        with self.assertRaises(P.Rejected):
            P.validate(reseal(bad))

    def test_24_resealed_coverage(self):
        for field in ("q_rows", "controls"):
            bad = copy.deepcopy(self.expected)
            if field == "q_rows":
                bad[field].pop()
            else:
                bad[field]["floor"].pop()
            with self.assertRaises(P.Rejected):
                P.validate(reseal(bad))

    def test_25_resealed_scopes(self):
        for field, value in (
            ("support_threshold", "constant"),
            ("operator_threshold", "o(k/log(k))"),
            ("completion_ratio_exponent", "-k"),
            ("scope", "effective_all_weight"),
        ):
            bad = copy.deepcopy(self.expected)
            bad[field] = value
            with self.assertRaises(P.Rejected):
                P.validate(reseal(bad))

    def test_26_resealed_constants(self):
        bad = copy.deepcopy(self.expected)
        bad["controls"]["moment_majorant_constants"][-1] = 99
        with self.assertRaises(P.Rejected):
            P.validate(reseal(bad))

    def test_27_resealed_caps(self):
        bad = copy.deepcopy(self.expected)
        bad["caps"]["dimension"] = 5
        with self.assertRaises(P.Rejected):
            P.validate(reseal(bad))

    def test_28_source_manifest_drift(self):
        for field in ("commit", "git_blob", "sha256_lf", "path"):
            bad = P.manifest()
            bad["frozen_sources"][0][field] += "0"
            with (
                patch.object(P, "read_json", return_value=bad),
                self.assertRaises(P.Rejected),
            ):
                P.authenticate_sources()

    def test_29_artifact_and_payload_seals(self):
        for path in P.ARTIFACTS:
            bad = copy.deepcopy(self.expected)
            bad["artifact_sha256_lf"][path] = "0" * 64
            with self.assertRaises(P.Rejected):
                P.validate(reseal(bad))
        bad = copy.deepcopy(self.expected)
        bad["payload_sha256"] = "0" * 64
        with self.assertRaises(P.Rejected):
            P.validate(bad)

    def test_30_missing_extra_fields(self):
        bad = copy.deepcopy(self.expected)
        bad["extra"] = 1
        with self.assertRaises(P.Rejected):
            P.validate(reseal(bad))
        bad = copy.deepcopy(self.expected)
        del bad["scope"]
        with self.assertRaises(P.Rejected):
            P.validate(reseal(bad))

    def test_31_numeric_json_drift(self):
        for value in (24.0, True):
            bad = copy.deepcopy(self.expected)
            bad["q_rows"][0]["k"] = value
            with self.assertRaises(P.Rejected):
                P.validate(reseal(bad))
        self.assertEqual(P.decode(P.encoded({"x": 24})), {"x": 24})

    def test_32_proof_controls_and_scope(self):
        proof = (ROOT / P.ARTIFACTS[0]).read_text(encoding="utf-8")
        self.assertFalse(any(ord(c) < 32 and c not in "\n\r\t" for c in proof))
        for marker in (
            "(HC3)",
            "(HC10)",
            "(HC13)",
            "(HC19)",
            "(HC22)",
            "codimension-fixed",
            "No numerical sufficient-weight threshold",
        ):
            self.assertIn(marker, proof)
        self.assertEqual(len(self.expected["q_rows"]), 18)
        self.assertEqual(len(self.expected["artifact_sha256_lf"]), 4)
        self.assertLess(self.expected["work_used"], P.CAPS["work"])
        self.assertEqual(json.loads(P.encoded(self.expected)), self.expected)


if __name__ == "__main__":
    unittest.main()
