"""Independent finite controls and strict hostile-input checks for FI."""

from __future__ import annotations

import copy
import importlib.util
import json
import math
import subprocess
import sys
import unittest
from fractions import Fraction as F
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
PATH = (
    ROOT
    / "research/l-families/atlas/generalized/cusp_weight24_fixed_divisor_infinity.py"
)
SPEC = importlib.util.spec_from_file_location("fixed_divisor", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


def independent_basis(order: int) -> tuple[list[int], list[int]]:
    def multiply(a, b):
        return [sum(a[i] * b[n - i] for i in range(n + 1)) for n in range(order + 1)]

    product = [1] + [0] * order
    for j in range(1, order + 1):
        factor = [0] * (order + 1)
        for e in range(min(24, order // j) + 1):
            factor[j * e] = (-1) ** e * math.comb(24, e)
        product = multiply(product, factor)
    delta = [0] + product[:order]
    e4 = [1] + [
        240 * sum(d**3 for d in range(1, n + 1) if n % d == 0)
        for n in range(1, order + 1)
    ]
    b = multiply(delta, delta)
    g0 = multiply(delta, multiply(e4, multiply(e4, e4)))
    return [x - 696 * y for x, y in zip(g0, b)], b


def independent_coefficients(g: list[int], b: list[int]) -> list[dict]:
    order = len(g) - 1

    def lift(n, a, c):
        return sum(
            (
                F(a[n // (m * m)] * c[n // (m * m)], (n // (m * m)) ** 23)
                for m in range(1, math.isqrt(n) + 1)
                if n % (m * m) == 0
            ),
            F(),
        )

    gg = [F()] + [lift(n, g, g) for n in range(1, order + 1)]
    bb = [F()] + [lift(n, b, b) for n in range(1, order + 1)]
    gb = [F()] + [lift(n, g, b) for n in range(1, order + 1)]
    rows = []
    for n in range(1, order + 1):
        det = sum(
            (
                gg[d] * bb[n // d] - gb[d] * gb[n // d]
                for d in range(1, n + 1)
                if n % d == 0
            ),
            F(),
        )
        # Independent expansion of the quadratic eigenform coefficients.
        u = gg[n] + 1080 * gb[n] + (540**2 + 144169 * 144) * bb[n]
        v = 24 * gb[n] + 12960 * bb[n]
        c = gg[n] + 1080 * gb[n] + (540**2 - 144169 * 144) * bb[n]
        rows.append(
            {
                "n": n,
                "diag_rational": M.wire(u),
                "diag_sqrt": M.wire(v),
                "cross": M.wire(c),
                "H": M.wire(83041344 * bb[n]),
                "N": M.wire(83041344 * det),
            }
        )
    return rows


class FixedDivisorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.actual = M.fixture()

    def reject(self, value):
        with self.assertRaises(M.Rejected):
            M.validate(value)

    def reseal(self, value):
        value = copy.deepcopy(value)
        value.pop("payload_sha256", None)
        value["payload_sha256"] = M.digest(M.encoded(value))
        return value

    def test_01_complete_independent_q(self):
        self.assertEqual(list(independent_basis(64)), self.actual["basis"])

    def test_02_complete_independent_dirichlet(self):
        self.assertEqual(
            independent_coefficients(*independent_basis(64)),
            self.actual["dirichlet_coefficients"],
        )

    def test_03_eigen_quadratic_and_discriminant(self):
        a, b, c = self.actual["eigen_equation"]
        self.assertEqual(b * b - 4 * a * c, 576 * 144169)
        self.assertEqual(540**2 + b * 540 + c + 144 * 144169, 0)
        self.assertEqual(24 * 1080, self.actual["square_difference_sqrt_coefficient"])

    def test_04_t2_and_t3_native_action(self):
        g, b = independent_basis(64)
        t2 = self.actual["T2"]
        t3 = [[195660, -48], [-982499328, 143820]]
        for p, t in ((2, t2), (3, t3)):
            for j, a in enumerate((g, b)):
                for n in range(1, 64 // p + 1):
                    self.assertEqual(
                        a[p * n] + (p**23 * a[n // p] if n % p == 0 else 0),
                        t[0][j] * g[n] + t[1][j] * b[n],
                    )

    def test_05_local_tensor_generic_algebra(self):
        # Direct tensor matrix determinant at exact sample traces, not FI recurrence.
        import sympy as s

        X = s.Symbol("X")
        for a, b in ((0, 0), (1, 2), (F(3, 2), F(-4, 3))):
            A = s.Matrix([[a, -1], [1, 0]])
            B = s.Matrix([[b, -1], [1, 0]])
            actual = s.Poly((s.eye(4) - X * s.kronecker_product(A, B)).det(), X)
            self.assertEqual(
                list(reversed(actual.all_coeffs())),
                [1, -a * b, a * a + b * b - 2, -a * b, 1],
            )

    def test_06_guarded_targets(self):
        pole, zero, cancelled = self.actual["controls"]["targets"]
        self.assertEqual((pole["H"], pole["N"]), ([0, 1], [-9, 4]))
        self.assertEqual((zero["H"], zero["N"]), ([1, 1], [0, 1]))
        self.assertEqual((cancelled["H"], cancelled["N"]), ([0, 1], [0, 1]))

    def test_07_symbolic_schur_and_target_slope(self):
        import sympy as s

        z, x, y, c = s.symbols("z x y c")
        H = z * (x + y) - 2 * c
        N = z * z * x * y - c * c
        self.assertEqual(
            s.expand(4 * N - H * (z * (x + y) + 2 * c) + z * z * (x - y) ** 2), 0
        )
        self.assertEqual(s.diff(H, c), -2)
        self.assertEqual(s.expand(s.rem(N, H, c) + z * z * (x - y) ** 2 / 4), 0)

    def test_08_valuation_factor_two(self):
        rows = self.actual["controls"]["valuation_rows_m_r_poleJoverH_poleQ"]
        self.assertIn([2, 1, 1, 0], rows)
        self.assertIn([3, 1, 2, 1], rows)
        for m, r, j, q in rows:
            self.assertEqual(j, max(m - r, 0))
            self.assertEqual(q, max(m - 2 * r, 0))

    def test_09_leading_coefficient_and_square_factors(self):
        rows = self.actual["dirichlet_coefficients"]
        self.assertEqual(rows[0]["H"], [0, 1])
        self.assertEqual(rows[0]["N"], [0, 1])
        self.assertEqual(rows[1]["H"], [1297521, 131072])
        self.assertEqual(rows[1]["H"], rows[1]["N"])
        _g, b = self.actual["basis"]
        self.assertEqual(
            F(*rows[7]["H"]), 83041344 * (F(b[8] ** 2, 8**23) + F(1, 2**23))
        )

    def test_10_common_twist_convolution(self):
        # Gaussian rationals: chi(2)=i, chi(other primes)=1.
        def phase(n):
            e = 0
            while n % 2 == 0:
                n //= 2
                e += 1
            return ((1, 0), (0, 1), (-1, 0), (0, -1))[e % 4]

        def mul(a, b):
            return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])

        for n in range(1, 65):
            for d in range(1, n + 1):
                if n % d == 0:
                    self.assertEqual(mul(phase(d), phase(n // d)), phase(n))
        self.assertEqual(phase(2), (0, 1))

    def test_11_divisor_majorants_complete(self):
        # Ordered-factorization recursion, and the exact harmonic version of A_r(x).
        for r in (4, 8):
            counts = [0] + [1] * 64
            for _ in range(r - 1):
                counts = [0] + [
                    sum(counts[d] for d in range(1, n + 1) if n % d == 0)
                    for n in range(1, 65)
                ]
            for n in range(1, 65):
                harmonic = sum((F(1, d) for d in range(1, n + 1)), F())
                self.assertLessEqual(sum(counts[1 : n + 1]), n * harmonic ** (r - 1))

    def test_12_tail_integral_formula(self):
        import sympy as s

        u = s.Symbol("u", nonnegative=True)
        for r in (4, 8):
            for j in (1, 2, 4):
                actual = s.integrate(
                    (1 + j + u) ** (r - 1) * s.exp(-u), (u, 0, s.oo)
                ) * s.Rational(2, 2**j)
                row = next(
                    x
                    for x in self.actual["controls"]["tail_majorant_a2_M2powerj"]
                    if x[:2] == [r, j]
                )
                self.assertEqual(actual, F(*row[2]))

    def test_13_manifest_authentication(self):
        self.assertEqual(
            M.read_json(ROOT / M.DIR / f"{M.STEM}.sources.json"), M.manifest()
        )
        self.assertEqual(len(M.PINS), 6)

    def test_14_seals_and_fixture_identity(self):
        disk = M.read_json(ROOT / M.DIR / f"{M.STEM}.json")
        self.assertEqual(disk, self.actual)
        body = copy.deepcopy(disk)
        seal = body.pop("payload_sha256")
        self.assertEqual(seal, M.digest(M.encoded(body)))
        for path, expected in disk["artifact_sha256_lf"].items():
            self.assertEqual(M.digest(M.lf((ROOT / path).read_bytes())), expected)

    def test_15_resealed_scientific_tampering(self):
        for field in ("H", "N", "cross", "diag_rational", "diag_sqrt"):
            v = copy.deepcopy(self.actual)
            v["dirichlet_coefficients"][3][field][0] += 1
            self.reject(self.reseal(v))

    def test_16_resealed_chart_and_target_tampering(self):
        for action in (
            lambda v: v["basis"][0].__setitem__(63, 1),
            lambda v: v["controls"]["targets"][0]["N"].__setitem__(0, 9),
            lambda v: v.__setitem__("scope", "RH"),
            lambda v: v["controls"].__setitem__("rounding", "float"),
        ):
            v = copy.deepcopy(self.actual)
            action(v)
            self.reject(self.reseal(v))

    def test_17_resealed_digest_tampering(self):
        v = copy.deepcopy(self.actual)
        v["artifact_sha256_lf"][M.ARTIFACTS[0]] = "0" * 64
        self.reject(self.reseal(v))

    def test_18_duplicate_extra_and_missing(self):
        with self.assertRaises(M.Rejected):
            M.decode(b'{"a":1,"a":2}')
        v = copy.deepcopy(self.actual)
        v["extra"] = 1
        self.reject(self.reseal(v))
        v = copy.deepcopy(self.actual)
        del v["weight"]
        self.reject(self.reseal(v))

    def test_19_forbidden_json_types(self):
        for raw in (
            b"true",
            b"false",
            b"null",
            b"1.0",
            b"NaN",
            b"Infinity",
            b"-Infinity",
        ):
            with self.assertRaises(M.Rejected):
                M.decode(raw)
        for value in (True, False, None, 1.0):
            with self.assertRaises(M.Rejected):
                M.typed(value)

    def test_20_json_caps(self):
        for value in (
            [1] * 1025,
            "a" * 4097,
            2**4096,
            {str(i): 1 for i in range(1025)},
        ):
            with self.assertRaises(M.Rejected):
                M.typed(value)
        with self.assertRaises(M.Rejected):
            M.decode(b" " * 2000001)
        deep = 0
        for _ in range(26):
            deep = [deep]
        with self.assertRaises(M.Rejected):
            M.typed(deep)
        with self.assertRaises(M.Rejected):
            M.typed([list(range(1000)) for _ in range(101)])

    def test_21_budget_caps(self):
        for value in (True, 0, -1, 2000001):
            with self.assertRaises(M.Rejected):
                M.Budget(value)
        budget = M.Budget(1)
        budget.charge()
        with self.assertRaises(M.Rejected):
            budget.charge()
        with self.assertRaises(M.Rejected):
            M.source_basis(64, M.Budget(1))

    def test_22_source_and_arithmetic_domains(self):
        for value in (True, 3, 65, 1.0):
            with self.assertRaises(M.Rejected):
                M.source_basis(value, M.Budget())
        for a, b in (([0, 1], [0]), ([0, True], [0, 1]), ([0, 2**4096], [0, 1])):
            with self.assertRaises(M.Rejected):
                M.qmul(a, b, M.Budget())
        with self.assertRaises(M.Rejected):
            M.dconv([F(), F(1)], [F()], M.Budget())
        with self.assertRaises(M.Rejected):
            M.dseries([F(1), F()])
        with self.assertRaises(M.Rejected):
            M.rat(1)
        for order in (True, 1, 65):
            with self.assertRaises(M.Rejected):
                M.primepowers(order, [F(), F(1)], [F(), F(1)], M.Budget())
        with self.assertRaises(M.Rejected):
            M.primepowers(2, [F(), F(1)], [F(), F(1)], M.Budget())

    def test_23_frozen_source_failure_closed(self):
        with (
            patch.object(M, "git_bytes", side_effect=M.Rejected("missing")),
            self.assertRaises(M.Rejected),
        ):
            M.fixture()
        original = M.read_json

        def altered(path):
            out = original(path)
            if str(path).endswith(".sources.json"):
                out["frozen_sources"][0]["sha256_lf"] = "0" * 64
            return out

        with (
            patch.object(M, "read_json", side_effect=altered),
            self.assertRaises(M.Rejected),
        ):
            M.fixture()

    def test_24_normal_and_optimized_cli(self):
        for mode in ([], ["-O"]):
            p = subprocess.run(
                [sys.executable, *mode, str(PATH), "--check"],
                capture_output=True,
                check=False,
            )
            self.assertEqual(p.returncode, 0, p.stderr.decode())

    def test_25_emits_exact(self):
        for mode in ([], ["-O"]):
            for option, suffix in (
                ("--emit-fixture", ".json"),
                ("--emit-sources", ".sources.json"),
            ):
                p = subprocess.run(
                    [sys.executable, *mode, str(PATH), option],
                    capture_output=True,
                    check=False,
                )
                self.assertEqual(p.returncode, 0, p.stderr.decode())
                self.assertEqual(
                    M.lf(p.stdout),
                    M.lf((ROOT / M.DIR / f"{M.STEM}{suffix}").read_bytes()),
                )

    def test_26_cli_requires_action(self):
        for args in ([], ["--check", "--emit-fixture"], ["--unknown"]):
            p = subprocess.run(
                [sys.executable, str(PATH), *args], capture_output=True, check=False
            )
            self.assertNotEqual(p.returncode, 0)

    def test_27_proof_scope_and_controls(self):
        proof = (ROOT / M.ARTIFACTS[0]).read_text(encoding="utf-8")
        for phrase in (
            "MIXED: EXACT_RATIONAL",
            "No weight limit",
            "not machine-certified",
            "positive lower",
            "2018 correction",
            "distinct-point",
        ):
            self.assertIn(phrase, proof)
        for path in M.ARTIFACTS + (f"{M.DIR}/{M.STEM}.json",):
            data = (ROOT / path).read_bytes()
            self.assertFalse(any(b < 32 and b not in (9, 10, 13) for b in data), path)

    def test_28_local_rows_complete(self):
        primes = [
            p for p in range(2, 65) if all(p % d for d in range(2, math.isqrt(p) + 1))
        ]
        self.assertEqual([r["prime"] for r in self.actual["local_tensor_rows"]], primes)
        for row in self.actual["local_tensor_rows"]:
            self.assertLessEqual(row["powers"][-1], 64)
            self.assertGreater(row["powers"][-1] * row["prime"], 64)

    def test_29_work_and_taxonomy(self):
        self.assertLessEqual(self.actual["work_used"], self.actual["caps"]["work"])
        self.assertEqual(self.actual["controls"]["rounding"], "none")
        self.assertEqual(
            self.actual["controls"]["analytic_imports_machine_certified"], "no"
        )

    def test_30_json_roundtrip(self):
        self.assertEqual(M.decode(M.encoded(self.actual)), self.actual)
        self.assertEqual(json.loads(M.encoded(self.actual)), self.actual)

    def test_31_rational_encodings_resealed(self):
        v = copy.deepcopy(self.actual)
        v["dirichlet_coefficients"][1]["H"] = [2595042, 262144]
        self.reject(self.reseal(v))
        v = copy.deepcopy(self.actual)
        v["dirichlet_coefficients"][1]["H"] = [1, 0]
        self.reject(self.reseal(v))

    def test_32_no_false_numeric_certificate(self):
        self.assertEqual(self.actual["controls"]["prime_cutoff"], [3, 2])
        self.assertEqual(self.actual["controls"]["target_annulus_radius"], [4, 1])
        self.assertIn("certified_divisor_location", self.actual["not_claimed"])
        self.assertIn("unsigned_asymptotic", self.actual["not_claimed"])


if __name__ == "__main__":
    unittest.main()
