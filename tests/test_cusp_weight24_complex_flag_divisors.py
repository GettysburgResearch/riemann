"""Independent exact flag algebra, native Fourier reconstruction, and hostile gates."""

from __future__ import annotations

import ast
import copy
import hashlib
import importlib.util
import json
import math
import subprocess
import sys
import unittest
from fractions import Fraction as F
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
PATH = (
    ROOT
    / "research/l-families/atlas/generalized/cusp_weight24_complex_flag_divisors.py"
)
SPEC = importlib.util.spec_from_file_location("complex_flag_source", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


def zadd(a, b):
    return a[0] + b[0], a[1] + b[1]


def zmul(a, b):
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def zconj(a):
    return a[0], -a[1]


def zneg(a):
    return -a[0], -a[1]


def qmul(a, b):
    return [sum(a[j] * b[n - j] for j in range(n + 1)) for n in range(len(a))]


def independent_basis():
    n = 64
    product = [1] + [0] * n
    for h in range(1, n + 1):
        factor = [0] * (n + 1)
        for j in range(min(24, n // h) + 1):
            factor[h * j] = (-1) ** j * math.comb(24, j)
        product = qmul(product, factor)
    delta = [0] + product[:n]
    e4 = [1] + [
        240 * sum(d**3 for d in range(1, h + 1) if h % d == 0) for h in range(1, n + 1)
    ]
    b = qmul(delta, delta)
    g = [x - 696 * y for x, y in zip(qmul(delta, qmul(qmul(e4, e4), e4)), b)]
    return g, b


class ComplexFlags(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture = M.decode(PATH.with_suffix(".json").read_bytes())
        cls.actual = M.fixture()
        cls.by_label = {r["label"]: r for r in cls.actual["flags"]}

    def reject(self, value):
        with self.assertRaises(M.Rejected):
            M.validate(value)

    def reseal(self, value):
        value.pop("payload_sha256", None)
        value["payload_sha256"] = M.digest(M.encoded(value))
        return value

    def test_01_complete_fixture(self):
        self.assertEqual(self.fixture, self.actual)
        self.assertEqual(len(self.actual["flags"]), 32)
        self.assertEqual(sum(r["class"] == "mixed" for r in self.actual["flags"]), 30)

    def test_02_primitive_euler_product_and_all_native_coefficients(self):
        g, b = independent_basis()
        for row in self.actual["flags"]:
            r = None if not row["r"] else tuple(F(*v) for v in row["r"])
            expected = []
            for n in range(1, 65):
                aa, bb = F(), F()
                for j in range(1, math.isqrt(n) + 1):
                    if n % (j * j):
                        continue
                    h = n // (j * j)
                    c0, c1 = g[h] + 540 * b[h], 12 * b[h]
                    if r is None:
                        ra, rb = F(c0 * c0 + 144169 * c1 * c1), F(-2 * c0 * c1)
                    else:
                        x, y = r
                        size = 1 + x * x + y * y
                        ra = (
                            (size + 2 * x) * c0 * c0 + 144169 * (size - 2 * x) * c1 * c1
                        ) / size
                        rb = 2 * c0 * c1 * (2 - size) / size
                    aa += ra / h**23
                    bb += rb / h**23
                expected.append(
                    [[aa.numerator, aa.denominator], [bb.numerator, bb.denominator]]
                )
            self.assertEqual(row["native_denominator_prefix"], expected, row["label"])

    def test_03_complex_basis_congruence_not_transpose(self):
        a, b = (F(1), F(1)), (F(2), F(-1))
        v, w = (zneg(zconj(b)), zconj(a)), (a, b)
        x, y, c = (F(1), F(2)), (F(3), F(-1)), (F(5), F(1))
        mat = ((x, c), (c, y))

        def form(left, right):
            total = (F(0), F(0))
            for i in range(2):
                for j in range(2):
                    total = zadd(total, zmul(zmul(zconj(left[i]), mat[i][j]), right[j]))
            return total

        det = zadd(zmul(form(v, v), form(w, w)), zneg(zmul(form(v, w), form(w, v))))
        numerator = zadd(zmul(x, y), zneg(zmul(c, c)))
        self.assertEqual(det, zmul((F(49), F(0)), numerator))
        # p=2, q=5, d=2 Re(conj(a)b)=2, before normalizing by seven.
        denominator = zadd(
            zadd(zmul((F(2), F(0)), x), zmul((F(5), F(0)), y)), zmul((F(2), F(0)), c)
        )
        self.assertEqual(form(w, w), denominator)

    def test_04_protected_poles_every_declared_mixed_line(self):
        for row in self.actual["flags"]:
            p, q, d = (F(*v) for v in row["weights"])
            if p == 0 or q == 0:
                self.assertEqual(row["pole"], [])
                continue
            witness = row["pole"][0]
            z, plus, minus, c = [tuple(F(*v) for v in a) for a in witness["target"]]
            x, y = zmul(z, plus), zmul(z, minus)
            den = zadd(zadd(zmul((p, F(0)), x), zmul((q, F(0)), y)), zmul((d, F(0)), c))
            num = zadd(zmul(x, y), zneg(zmul(c, c)))
            self.assertEqual(den, (0, 0))
            self.assertEqual(num, ((1 - p * q) / q**2, -d / q**2))
            self.assertGreaterEqual(num[0], F(3, 4) / q**2)

    def test_05_zero_targets_include_eigenlines(self):
        for row in self.actual["flags"]:
            d = F(*row["weights"][2])
            self.assertEqual(row["zero"]["N"], [[0, 1], [0, 1]])
            self.assertEqual(F(*row["zero"]["D"][0]), 1 + abs(d))

    def test_06_imaginary_mixture_has_no_cross_term_but_pole_target(self):
        row = self.by_label["grid_0_1"]
        self.assertEqual(row["weights"], [[1, 2], [1, 2], [0, 1]])
        self.assertEqual(row["pole"][0]["N"], [[3, 1], [0, 1]])
        target = row["pole"][0]["target"]
        c = tuple(F(*v) for v in target[-1])
        self.assertNotEqual(c, (0, 0))  # Replaced d by 2|ab| would destroy D=0.

    def test_07_antidiagonal_first_coefficient_is_zero_not_identity(self):
        row = self.by_label["grid_-1_0"]
        self.assertEqual(row["native_denominator_prefix"][0], [[0, 1], [0, 1]])
        self.assertEqual(
            row["native_denominator_prefix"][1], [[1297521, 262144], [0, 1]]
        )
        self.assertEqual(row["zero"]["target"][-1], [[-1, 1], [0, 1]])

    def test_08_conjugate_flags_share_the_source_quotient(self):
        for x in range(-2, 3):
            for y in range(1, 3):
                plus, minus = (
                    self.by_label[f"grid_{x}_{y}"],
                    self.by_label[f"grid_{x}_{-y}"],
                )
                self.assertEqual(plus["weights"], minus["weights"])
                self.assertEqual(
                    plus["native_denominator_prefix"],
                    minus["native_denominator_prefix"],
                )

    def test_09_annulus_controls_complete(self):
        for row in self.actual["flags"]:
            for witness in row["pole"]:
                radius = F(*witness["annulus_radius"])
                epsilon = F(*witness["epsilon"])
                self.assertEqual(radius, 2 / epsilon**2)
                for z in witness["target"]:
                    a, b = (F(*v) for v in z)
                    self.assertGreaterEqual(a * a + b * b, 1 / radius**2)
                    self.assertLessEqual(a * a + b * b, radius**2)

    def test_10_no_fixed_annulus_near_eigenline_control(self):
        near = self.by_label["near_imag_plus"]["pole"][0]
        far = self.by_label["grid_0_1"]["pole"][0]
        self.assertGreater(F(*near["annulus_radius"]), F(*far["annulus_radius"]))

    def test_11_euler_common_factor_polynomial_identity(self):
        for trace in range(-5, 6):
            quad = [1, -trace, 1]
            cubic = [quad[0], quad[1] - quad[0], quad[2] - quad[1], -quad[2]]
            self.assertEqual(cubic, [1, -(trace + 1), trace + 1, -1])
        controls = self.actual["controls"]["ratio_majorants"]
        self.assertEqual(controls["Y_over_X"], [4, 2])
        self.assertEqual(controls["C_over_X"], [8, 4])

    def test_12_local_euler_bounds(self):
        for row in self.actual["controls"]["local_euler_bounds"]:
            t = F(*row["t"])
            ratio = (1 + t) / (1 - t)
            self.assertEqual(F(*row["M4_local"]), ratio**2)
            self.assertLess(F(*row["M4_local"]), F(*row["M6_local"]))
            self.assertEqual(F(*row["M8_local"]), ratio**4)

    def test_13_escape_exact_budgets(self):
        rows = self.actual["controls"]["escape_controls"]
        self.assertEqual(len(rows), 12)
        for row in rows:
            delta = F(*row["delta"])
            x, y = (F(*z) for z in row["r"])
            first, second, total = (F(*z) for z in row["budgets"])
            self.assertEqual(first, 16 * (x * x + y * y) / delta**4)
            self.assertEqual(second, 512 * abs(x) / delta**8)
            self.assertEqual(total, first + second)
            self.assertLessEqual(total, F(9, 128))
            if row["kind"] == "imaginary":
                self.assertEqual(second, 0)

    def test_14_invalid_line_weights_and_eigenline_pole(self):
        for values in (
            (F(-1), F(2), F(0)),
            (F(1), F(1), F(0)),
            (F(1, 2), F(1, 2), F(2)),
            (F(1), F(0), F(1)),
        ):
            with self.assertRaises(M.Rejected):
                M.weights(*values)
        for values in ((F(1), F(0), F(0)), (F(0), F(1), F(0))):
            with self.assertRaises(M.Rejected):
                M.pole_target(*values)

    def test_15_rational_and_field_type_guards(self):
        for value in (True, 1, 1.0, "1", None):
            with self.assertRaises(M.Rejected):
                M.rational(value)
        with self.assertRaises(M.Rejected):
            M.mul((F(1), F(1)), (F(1), F(1)), True)
        for value in ([2, 4], [1, 0], [True, 1], [1, -2]):
            with self.assertRaises(M.Rejected):
                M.unwire(value)

    def test_16_overflow_and_work_caps(self):
        with self.assertRaises(M.Rejected):
            M.integer(1 << 4096)
        for value in (True, 0, -1, M.CAPS["work"] + 1):
            with self.assertRaises(M.Rejected):
                M.Budget(value)
        with self.assertRaises(M.Rejected):
            M.Budget(1).charge(2)
        with self.assertRaises(M.Rejected):
            M.pole_target(1 - F(1, 2**3000), F(1, 2**3000), F(1, 2**1500))

    def test_17_json_scalar_and_duplicate_rejections(self):
        for raw in (
            b'{"x":true}',
            b'{"x":null}',
            b'{"x":1.0}',
            b'{"x":NaN}',
            b'{"x":1,"x":2}',
            b"not JSON",
        ):
            with self.assertRaises(M.Rejected):
                M.decode(raw)

    def test_18_tree_string_byte_and_key_caps(self):
        for value in ("x" * 4097, [0] * 1025, {1: 2}):
            with self.assertRaises(M.Rejected):
                M.typed(value)
        nested = 0
        for _ in range(26):
            nested = [nested]
        with self.assertRaises(M.Rejected):
            M.typed(nested)
        with self.assertRaises(M.Rejected):
            M.decode(b" " * (M.CAPS["json_bytes"] + 1))

    def test_19_resealed_schema_scope_and_caps(self):
        for key, value in (
            ("schema", "new"),
            ("weight", True),
            ("weight", 36),
            ("scope", "RH"),
            ("caps", {}),
            ("not_claimed", []),
        ):
            mutated = copy.deepcopy(self.actual)
            mutated[key] = value
            self.reject(self.reseal(mutated))

    def test_20_resealed_flag_coverage(self):
        for operation in ("drop", "duplicate", "order"):
            v = copy.deepcopy(self.actual)
            if operation == "drop":
                v["flags"].pop()
            elif operation == "duplicate":
                v["flags"][-1] = v["flags"][0]
            else:
                v["flags"].reverse()
            self.reject(self.reseal(v))

    def test_21_resealed_native_coefficients(self):
        v = copy.deepcopy(self.actual)
        v["flags"][0]["native_denominator_prefix"][-1][0][0] += 1
        self.reject(self.reseal(v))
        v = copy.deepcopy(self.actual)
        v["flags"][0]["native_denominator_prefix"].pop()
        self.reject(self.reseal(v))

    def test_22_resealed_protected_target_and_escape(self):
        v = copy.deepcopy(self.actual)
        v["flags"][0]["pole"][0]["N"][0][0] += 1
        self.reject(self.reseal(v))
        v = copy.deepcopy(self.actual)
        v["controls"]["ratio_majorants"]["Y_over_X"] = [6, 3]
        self.reject(self.reseal(v))
        v = copy.deepcopy(self.actual)
        v["controls"]["escape_reserve"] = [9, 127]
        self.reject(self.reseal(v))

    def test_23_source_manifest_and_all_six_pins(self):
        expected = M.manifest()
        self.assertEqual(len(expected["frozen_sources"]), 6)
        self.assertEqual(
            M.decode(PATH.with_suffix(".sources.json").read_bytes()), expected
        )
        with mock.patch.object(M, "PINS", M.PINS[:-1]), self.assertRaises(M.Rejected):
            M.authenticate()

    def test_24_literal_source_drift_rejected_before_replay(self):
        original = M.git_bytes

        def changed(commit, path):
            raw = original(commit, path)
            return raw + b"\n" if path == M.PINS[0][1] else raw

        with (
            mock.patch.object(M, "git_bytes", side_effect=changed),
            self.assertRaises(M.Rejected),
        ):
            M.fixture()

    def test_25_artifact_drift_and_digest_rejected(self):
        original = M.file_bytes

        def changed(path):
            raw = original(path)
            return raw + b"\n" if path == ROOT / M.ARTIFACTS[0] else raw

        with mock.patch.object(M, "file_bytes", side_effect=changed):
            self.reject(self.actual)
        v = copy.deepcopy(self.actual)
        v["payload_sha256"] = "0" * 64
        self.reject(v)

    def test_26_independent_payload_digest(self):
        v = copy.deepcopy(self.actual)
        digest = v.pop("payload_sha256")
        raw = (json.dumps(v, sort_keys=True, indent=2) + "\n").encode("ascii")
        self.assertEqual(hashlib.sha256(raw).hexdigest(), digest)
        self.assertEqual(len(v["artifact_sha256_lf"]), 4)

    def test_27_taxonomy_and_proof_scope(self):
        self.assertEqual(self.actual["arithmetic_class"], "MIXED")
        self.assertEqual(
            self.actual["components"], ["EXACT_RATIONAL", "CERTIFIED_INTEGER_COVERAGE"]
        )
        self.assertEqual(self.actual["rounding"], "none")
        self.assertEqual(self.actual["analytic_claims_machine_certified"], "no")
        proof = (ROOT / M.ARTIFACTS[0]).read_text(encoding="utf-8")
        for phrase in (
            "no** common positive pole width",
            "first period argument is conjugate-linear",
            "not asymptotic",
            "not called exhaustive",
            "all of `CP^1`",
        ):
            self.assertIn(phrase, proof)

    def test_28_no_assert_acceptance_gates(self):
        tree = ast.parse(PATH.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(tree)))

    def test_29_cli_check(self):
        result = subprocess.run(
            [sys.executable, str(PATH), "--check"], capture_output=True, check=False
        )
        self.assertEqual(result.returncode, 0, result.stderr.decode())
        self.assertIn(b"all 64 native coefficients", result.stdout)

    def test_30_emit_protocols(self):
        for action, suffix in (
            ("--emit-fixture", ".json"),
            ("--emit-sources", ".sources.json"),
        ):
            out = subprocess.check_output([sys.executable, str(PATH), action])
            self.assertEqual(
                out.replace(b"\r\n", b"\n"),
                PATH.with_suffix(suffix).read_bytes().replace(b"\r\n", b"\n"),
            )

    def test_31_cli_requires_action(self):
        for args in ([], ["--unknown"], ["--check", "--emit-fixture"]):
            result = subprocess.run(
                [sys.executable, str(PATH), *args], capture_output=True, check=False
            )
            self.assertNotEqual(result.returncode, 0)

    def test_32_normal_and_optimized_strict_payload_attack(self):
        code = (
            "import importlib.util;from pathlib import Path;p=Path(r'"
            + str(PATH)
            + "');s=importlib.util.spec_from_file_location('attack',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);v=m.fixture();v['weight']=True;m.validate(v)"
        )
        for flags in ([], ["-O"]):
            result = subprocess.run(
                [sys.executable, *flags, "-c", code], capture_output=True, check=False
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn(b"Rejected", result.stderr)


if __name__ == "__main__":
    unittest.main()
