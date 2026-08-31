"""Independent native q-series, divisor convolution, and symmetric-subspace controls."""

from __future__ import annotations

import ast
import copy
import hashlib
import importlib.util
import itertools
import json
import math
import subprocess
import sys
import unittest
from fractions import Fraction as F
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/l-families/atlas/generalized/cusp_weight36_subspace_divisors.py"
SPEC = importlib.util.spec_from_file_location("subspace_divisors_source", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


def multiply(z, w):
    return z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0]


def conjugate(z):
    return z[0], -z[1]


def sign(permutation):
    return (-1) ** sum(
        permutation[i] > permutation[j]
        for i in range(len(permutation))
        for j in range(i + 1, len(permutation))
    )


def determinant(matrix):
    out = (F(0), F(0))
    for permutation in itertools.permutations(range(len(matrix))):
        value = (F(sign(permutation)), F(0))
        for i, j in enumerate(permutation):
            value = multiply(value, matrix[i][j])
        out = add(out, value)
    return out


def readz(value):
    return F(*value[0]), F(*value[1])


def numeric_restriction(v, entries):
    x, y, z, a, b, c = entries
    matrix = [[x, a, b], [a, y, c], [b, c, z]]
    rank = len(v[0])
    out = [[(F(0), F(0)) for _ in range(rank)] for _ in range(rank)]
    for i in range(rank):
        for j in range(rank):
            for k in range(3):
                for l in range(3):
                    out[i][j] = add(
                        out[i][j],
                        multiply(multiply(conjugate(v[k][i]), matrix[k][l]), v[l][j]),
                    )
    return determinant(out)


def eval_polynomial(rows, entries):
    out = (F(0), F(0))
    for row in rows:
        value = readz(row["coefficient"])
        for entry, exponent in zip(entries, row["exponents"]):
            for _ in range(exponent):
                value = multiply(value, entry)
        out = add(out, value)
    return out


def qmul(a, b):
    return [sum(a[j] * b[n - j] for j in range(n + 1)) for n in range(len(a))]


def qpow(a, exponent):
    out = [1] + [0] * (len(a) - 1)
    for _ in range(exponent):
        out = qmul(out, a)
    return out


def basis_from_euler_product():
    order = 18
    delta = [1] + [0] * order
    for h in range(1, order + 1):
        factor = [0] * (order + 1)
        for j in range(min(24, order // h) + 1):
            factor[j * h] = (-1) ** j * math.comb(24, j)
        delta = qmul(delta, factor)
    delta = [0] + delta[:order]
    e4 = [1] + [
        240 * sum(d**3 for d in range(1, n + 1) if n % d == 0)
        for n in range(1, order + 1)
    ]
    rows = [qmul(qpow(delta, j), qpow(e4, 3 * (3 - j))) for j in range(1, 4)]
    # Forward, all-row elimination, independent of HC's backward echelon.
    for pivot in range(3):
        if rows[pivot][pivot + 1] != 1:
            raise ValueError("primitive pivot")
        for i in range(3):
            if i != pivot:
                multiple = rows[i][pivot + 1]
                rows[i] = [a - multiple * b for a, b in zip(rows[i], rows[pivot])]
    return rows


def convolution(a, b):
    out = [F(0)] * len(a)
    for i in range(1, len(a)):
        for j in range(1, (len(a) - 1) // i + 1):
            out[i * j] += a[i] * b[j]
    return out


def cubic_disc(poly):
    c, b, a, leading = poly
    if leading != 1:
        raise ValueError("monic cubic required")
    return a * a * b * b - 4 * b**3 - 4 * a**3 * c - 27 * c * c + 18 * a * b * c


class SubspaceDivisors(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.saved = M.decode(PATH.with_suffix(".json").read_bytes())
        cls.actual = M.fixture()
        cls.source = cls.actual["native_source"]
        cls.rows = cls.actual["subspaces"]
        cls.by_label = {row["label"]: row for row in cls.rows}

    def reject(self, value):
        with self.assertRaises(M.Rejected):
            M.validate(value)

    def reseal(self, value):
        value.pop("payload_sha256", None)
        value["payload_sha256"] = M.digest(M.encoded(value))
        return value

    def test_01_fixture_and_declared_coverage(self):
        self.assertEqual(self.saved, self.actual)
        self.assertEqual(len(self.rows), 27)
        self.assertEqual(sum(r["dimension"] == 1 for r in self.rows), 13)
        self.assertEqual(sum(r["dimension"] == 2 for r in self.rows), 14)
        self.assertEqual(
            sum(r["class"] == "pole_free_Hecke_line" for r in self.rows), 3
        )

    def test_02_independent_primitive_basis(self):
        self.assertEqual(basis_from_euler_product(), self.source["basis"])

    def test_03_complete_hecke_actions_and_eigen_q3_relation(self):
        basis = basis_from_euler_product()
        for prime in (2, 3):
            matrix = self.source[f"T{prime}"]
            for n in range(1, 18 // prime + 1):
                for j, f in enumerate(basis):
                    actual = f[prime * n] + (
                        prime**35 * f[n // prime] if n % prime == 0 else 0
                    )
                    self.assertEqual(
                        actual, sum(matrix[i][j] * basis[i][n] for i in range(3))
                    )
        t2, t3 = self.source["T2"], self.source["T3"]
        for i in range(3):
            for j in range(3):
                square = sum(t2[i][k] * t2[k][j] for k in range(3))
                self.assertEqual(
                    72 * t3[i][j],
                    (34416831456 if i == j else 0) + 194184 * t2[i][j] - square,
                )

    def test_04_characteristic_polynomial_at_four_points(self):
        poly = [F(*x) for x in self.source["P"]]
        for point in (-2, 0, 1, 3):
            matrix = [
                [
                    (F(point * (i == j) - self.source["T2"][i][j]), F(0))
                    for j in range(3)
                ]
                for i in range(3)
            ]
            self.assertEqual(
                determinant(matrix), (sum(c * point**i for i, c in enumerate(poly)), 0)
            )
        self.assertEqual(cubic_disc(poly), F(*self.source["discriminant"]))

    def test_05_three_real_nonzero_nonopposite_roots(self):
        poly = [F(*x) for x in self.source["P"]]
        for row in self.source["root_intervals"]:
            a, b = row["interval"]
            fa = sum(c * a**i for i, c in enumerate(poly))
            fb = sum(c * b**i for i, c in enumerate(poly))
            self.assertLess(fa * fb, 0)
        self.assertNotEqual(poly[0], 0)
        s1, s2, s3 = -poly[2], poly[1], -poly[0]
        self.assertEqual(
            F(*self.source["opposite_resultant"]), -8 * s3 * (s1 * s2 - s3) ** 2
        )
        self.assertNotEqual(s1 * s2 - s3, 0)

    def test_06_all_seven_prime2_inputs_distinct(self):
        square = [F(*x) for x in self.source["square_polynomial"]]
        product = [F(*x) for x in self.source["pair_product_polynomial"]]
        self.assertEqual(cubic_disc(square), F(*self.source["square_discriminant"]))
        self.assertEqual(
            cubic_disc(product), F(*self.source["pair_product_discriminant"])
        )
        self.assertGreater(cubic_disc(square), 0)
        self.assertGreater(cubic_disc(product), 0)
        self.assertEqual(
            self.actual["controls"]["primitive_degrees"], [1, 3, 3, 3, 4, 4, 4]
        )

    def test_07_independent_full_dirichlet_determinant_all36(self):
        basis = basis_from_euler_product()
        entries = [
            [
                [F(0)]
                + [F(f[n] * g[n], n**35) if n <= 18 else F(0) for n in range(1, 37)]
                for g in basis
            ]
            for f in basis
        ]
        det = [F(0)] * 37
        for permutation in itertools.permutations(range(3)):
            term = [F(0), F(sign(permutation))] + [F(0)] * 35
            for i, j in enumerate(permutation):
                term = convolution(term, entries[i][j])
            det = [a + b for a, b in zip(det, term)]
        zeta2 = [F(int(n > 0 and math.isqrt(n) ** 2 == n)) for n in range(37)]
        for _ in range(3):
            det = convolution(det, zeta2)
        factor = F(*self.source["discriminant"]) / 72**2
        expected = [factor * x for x in det[1:]]
        self.assertEqual(
            expected,
            [
                F(*r["coefficient"])
                for r in self.actual["full_determinant_coefficients"]
            ],
        )

    def test_08_heldout6_and8_predictions_and_square_divisors(self):
        rows = self.actual["full_determinant_coefficients"]
        a6, a8 = F(*rows[5]["coefficient"]), F(*rows[7]["coefficient"])
        self.assertEqual(a8 * 8**35 / (a6 * 6**35), 5184)
        self.assertGreater(a6, 0)
        for n in (1, 2, 3, 4, 5, 7):
            self.assertEqual(rows[n - 1]["coefficient"], [0, 1])
        self.assertEqual(M.ordered_divisors3(2), 3)
        self.assertEqual(M.ordered_divisors3(4), 6)
        self.assertEqual(M.ordered_divisors3(6), 9)

    def test_09_literal_symbolic_determinant(self):
        expected = {
            (1, 1, 1, 0, 0, 0): F(1),
            (0, 0, 0, 1, 1, 1): F(2),
            (1, 0, 0, 0, 0, 2): F(-1),
            (0, 1, 0, 0, 2, 0): F(-1),
            (0, 0, 1, 2, 0, 0): F(-1),
        }
        self.assertEqual(
            {
                tuple(r["exponents"]): readz(r["coefficient"])
                for r in self.actual["symmetric_determinant"]
            },
            {k: (v, 0) for k, v in expected.items()},
        )

    def test_10_all_restrictions_match_direct_complex_congruence(self):
        entries = tuple((F(i - 2), F(2 - i % 3)) for i in range(6))
        for row in self.rows:
            v = [[readz(z) for z in r] for r in row["coefficient_matrix"]]
            self.assertEqual(
                eval_polynomial(row["P_W"], entries),
                numeric_restriction(v, entries),
                row["label"],
            )

    def test_11_positive_pluecker_diagonal_and_gram_scale(self):
        entries = (
            (F(2), F(0)),
            (F(3), F(0)),
            (F(5), F(0)),
            (F(0), F(0)),
            (F(0), F(0)),
            (F(0), F(0)),
        )
        for row in self.rows:
            v = [[readz(z) for z in r] for r in row["coefficient_matrix"]]
            self.assertEqual(
                eval_polynomial(row["diagonal_character"], entries),
                numeric_restriction(v, entries),
            )
            self.assertTrue(
                all(
                    readz(r["coefficient"])[0] > 0 and readz(r["coefficient"])[1] == 0
                    for r in row["diagonal_character"]
                )
            )
            self.assertGreater(readz(row["gram_determinant"])[0], 0)

    def test_12_all_zero_targets_are_noncancelling(self):
        for row in self.rows:
            target = tuple(readz(z) for z in row["zero"]["matrix_entries"])
            self.assertTrue(all(z != (0, 0) for z in target))
            self.assertEqual(
                eval_polynomial(self.actual["symmetric_determinant"], target), (0, 0)
            )
            self.assertNotEqual(eval_polynomial(row["P_W"], target), (0, 0))

    def test_13_all_pole_targets_are_noncancelling(self):
        for row in self.rows:
            for control in row["pole"]:
                target = tuple(readz(z) for z in control["matrix_entries"])
                self.assertTrue(all(z != (0, 0) for z in target))
                self.assertEqual(eval_polynomial(row["P_W"], target), (0, 0))
                self.assertNotEqual(
                    eval_polynomial(self.actual["symmetric_determinant"], target),
                    (0, 0),
                )

    def test_14_explicit_hecke_plane_and_canonical_plane(self):
        target = tuple((F(x), F(0)) for x in (1, 1, 1, 1, 1, 2))
        row = self.by_label["plane_chart_0_0"]
        self.assertEqual(eval_polynomial(row["P_W"], target), (0, 0))
        self.assertEqual(
            eval_polynomial(self.actual["symmetric_determinant"], target), (-1, 0)
        )
        canonical = self.by_label["canonical_first_coefficient_plane"]
        self.assertEqual(canonical["class"], "genuine_poles")
        for j in range(2):
            self.assertEqual(
                tuple(
                    sum(readz(r[j])[i] for r in canonical["coefficient_matrix"])
                    for i in range(2)
                ),
                (0, 0),
            )

    def test_15_no_plane_is_monomial(self):
        for row in self.rows:
            if row["dimension"] == 2:
                self.assertGreater(len(row["P_W"]), 1)
            self.assertEqual(
                len(row["P_W"]) == 1, row["class"] == "pole_free_Hecke_line"
            )

    def test_16_annuli_and_bounded_target_search(self):
        for row in self.rows:
            for target in [row["zero"], *row["pole"]]:
                radius = F(*target["annulus_radius"])
                self.assertLessEqual(target["attempts"], 729)
                self.assertGreaterEqual(radius, 2)
                for value in target["matrix_entries"]:
                    a, b = readz(value)
                    self.assertLessEqual(a * a + b * b, radius**2)
                    self.assertGreaterEqual(a * a + b * b, 1 / radius**2)

    def test_17_scalar_matrix_and_polynomial_guards(self):
        for value in (True, 1.0, "1", None):
            with self.assertRaises(M.Rejected):
                M.integer(value)
        for v in ([], [[M.ONE]], [[M.ONE]] * 4, [[M.ONE], [M.ONE, M.ONE], [M.ONE]]):
            with self.assertRaises(M.Rejected):
                M.vector_matrix(v)
        for p in (
            {(True, 0, 0, 0, 0, 0): M.ONE},
            {(4, 0, 0, 0, 0, 0): M.ONE},
            {(0, 0): M.ONE},
            {M.EXP0: M.ZERO},
        ):
            with self.assertRaises(M.Rejected):
                M.polynomial(p)

    def test_18_field_division_integer_and_work_caps(self):
        with self.assertRaises(M.Rejected):
            M.zd(M.ONE, M.ZERO)
        with self.assertRaises(M.Rejected):
            M.integer(1 << 4096)
        for value in (True, 0, -1, M.CAPS["work"] + 1):
            with self.assertRaises(M.Rejected):
                M.Budget(value)
        with self.assertRaises(M.Rejected):
            M.Budget(1).charge(2)
        with self.assertRaises(M.Rejected):
            M.pm({(3, 0, 0, 0, 0, 0): M.ONE}, M.variable(0), M.Budget())

    def test_19_remainder_and_target_fail_closed(self):
        with self.assertRaises(M.Rejected):
            M.remainder([F(1)], [F(0)], M.Budget())
        with self.assertRaises(M.Rejected):
            M.sturm([F(1)], M.Budget())
        with (
            mock.patch.dict(M.CAPS, {"target_attempts": 0}),
            self.assertRaises(M.Rejected),
        ):
            M.protected_target(M.variable(0), M.variable(1), M.Budget())

    def test_20_json_duplicate_scalar_and_tree_caps(self):
        for raw in (
            b'{"x":true}',
            b'{"x":null}',
            b'{"x":1.0}',
            b'{"x":NaN}',
            b'{"x":1,"x":2}',
        ):
            with self.assertRaises(M.Rejected):
                M.decode(raw)
        for v in ([0] * 1025, "x" * 4097, {1: 2}):
            with self.assertRaises(M.Rejected):
                M.typed(v)
        v = 0
        for _ in range(26):
            v = [v]
        with self.assertRaises(M.Rejected):
            M.typed(v)
        with self.assertRaises(M.Rejected):
            M.decode(b" " * (M.CAPS["json_bytes"] + 1))

    def test_21_resealed_schema_scope_caps(self):
        for key, value in (
            ("schema", "new"),
            ("weight", True),
            ("weight", 48),
            ("scope", "all_weights"),
            ("caps", {}),
            ("not_claimed", []),
        ):
            v = copy.deepcopy(self.actual)
            v[key] = value
            self.reject(self.reseal(v))

    def test_22_resealed_native_arithmetic_and_coverage(self):
        for change in ("P", "disc", "coefficient", "drop"):
            v = copy.deepcopy(self.actual)
            if change == "P":
                v["native_source"]["P"][0][0] += 1
            elif change == "disc":
                v["native_source"]["discriminant"][0] += 1
            elif change == "coefficient":
                v["full_determinant_coefficients"][-1]["coefficient"][0] += 1
            else:
                v["full_determinant_coefficients"].pop()
            self.reject(self.reseal(v))

    def test_23_resealed_subspace_and_noncancellation(self):
        for change in ("drop", "duplicate", "target", "class"):
            v = copy.deepcopy(self.actual)
            if change == "drop":
                v["subspaces"].pop()
            elif change == "duplicate":
                v["subspaces"][-1] = v["subspaces"][0]
            elif change == "target":
                v["subspaces"][-1]["pole"][0]["protected_value"] = [[0, 1], [0, 1]]
            else:
                v["subspaces"][-1]["class"] = "pole_free_Hecke_line"
            self.reject(self.reseal(v))

    def test_24_seven_sources_and_literal_drift(self):
        self.assertEqual(len(M.manifest()["frozen_sources"]), 7)
        self.assertEqual(
            M.decode(PATH.with_suffix(".sources.json").read_bytes()), M.manifest()
        )
        with mock.patch.object(M, "PINS", M.PINS[:-1]), self.assertRaises(M.Rejected):
            M.authenticate()
        original = M.git_bytes

        def changed(commit, path):
            raw = original(commit, path)
            return raw + b"\n" if path == M.PINS[0][1] else raw

        with (
            mock.patch.object(M, "git_bytes", side_effect=changed),
            self.assertRaises(M.Rejected),
        ):
            M.fixture()

    def test_25_artifact_drift_and_bad_digest(self):
        original = M.file_bytes

        def changed(path):
            raw = original(path)
            return raw + b"\n" if path == ROOT / M.ARTIFACTS[0] else raw

        with mock.patch.object(M, "file_bytes", side_effect=changed):
            self.reject(self.actual)
        v = copy.deepcopy(self.actual)
        v["payload_sha256"] = "0" * 64
        self.reject(v)

    def test_26_independent_payload_seal(self):
        v = copy.deepcopy(self.actual)
        seal = v.pop("payload_sha256")
        raw = (json.dumps(v, sort_keys=True, indent=2) + "\n").encode("ascii")
        self.assertEqual(hashlib.sha256(raw).hexdigest(), seal)
        self.assertEqual(len(v["artifact_sha256_lf"]), 4)

    def test_27_arithmetic_and_analytic_scope(self):
        self.assertEqual(self.actual["arithmetic_class"], "MIXED")
        self.assertEqual(
            self.actual["components"], ["EXACT_RATIONAL", "CERTIFIED_INTEGER_COVERAGE"]
        )
        self.assertEqual(self.actual["rounding"], "none")
        self.assertEqual(self.actual["analytic_claims_machine_certified"], "no")
        self.assertEqual(
            self.actual["controls"]["source_majorants"],
            {"line": [3, 4], "plane": [6, 8], "full": [6, 12]},
        )
        proof = (ROOT / M.ARTIFACTS[0]).read_text(encoding="utf-8")
        for phrase in (
            "fixed dimension",
            "not asserted Hermitian",
            "all seven",
            "not an exhaustive Grassmannian census",
            "not machine-certified",
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
        self.assertIn(b"36 determinant coefficients", result.stdout)

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

    def test_31_cli_action_guard(self):
        for args in ([], ["--unknown"], ["--check", "--emit-fixture"]):
            result = subprocess.run(
                [sys.executable, str(PATH), *args], capture_output=True, check=False
            )
            self.assertNotEqual(result.returncode, 0)

    def test_32_normal_optimized_strict_scalar_rejection(self):
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
