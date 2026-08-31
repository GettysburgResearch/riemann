"""Independent exact controls and fail-closed attacks for the MP finite packet."""

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
from fractions import Fraction as Q
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/l-families/atlas/generalized/cusp_matrix_period_positivity.py"
SPEC = importlib.util.spec_from_file_location("mp", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


def zmul(a, b):
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def zadd(a, b):
    return a[0] + b[0], a[1] + b[1]


def zconj(a):
    return a[0], -a[1]


def unpack(a):
    return [[tuple(map(Q, v)) for v in row] for row in a]


def rawdet(a):
    n = len(a)
    answer = Q(0), Q(0)
    for perm in itertools.permutations(range(n)):
        term = (
            Q(
                (-1)
                ** sum(perm[i] > perm[j] for i in range(n) for j in range(i + 1, n))
            ),
            Q(0),
        )
        for i, j in enumerate(perm):
            term = zmul(term, a[i][j])
        answer = zadd(answer, term)
    return answer


def rawgram(rows, frequencies, weights, order):
    n = len(rows[0])
    out = [[(Q(0), Q(0)) for _ in range(n)] for _ in range(n)]
    for row, nu, w in zip(rows, frequencies, weights):
        weight = w * nu**order
        for i, j in itertools.product(range(n), repeat=2):
            out[i][j] = zadd(
                out[i][j], zmul((weight, Q(0)), zmul(zconj(row[i]), row[j]))
            )
    return out


def rawproduct(a, b):
    out = []
    for row in a:
        r = []
        for j in range(len(b[0])):
            s = Q(0), Q(0)
            for k in range(len(row)):
                s = zadd(s, zmul(row[k], b[k][j]))
            r.append(s)
        out.append(r)
    return out


def rawstar(a):
    return [[zconj(a[i][j]) for i in range(len(a))] for j in range(len(a[0]))]


def rawcongruence(a, c):
    return rawproduct(rawproduct(rawstar(c), a), c)


def conv(a, b, n):
    return [
        sum((a[j] * b[k - j] for j in range(k + 1) if j < len(a) and k - j < len(b)), 0)
        for k in range(n + 1)
    ]


def reseal(value):
    value = copy.deepcopy(value)
    value.pop("payload_sha256", None)
    value["payload_sha256"] = hashlib.sha256(M.canonical(value)).hexdigest()
    return value


class MatrixPeriodTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.value = M.fixture()

    def setUp(self):
        M.WORK = 0

    def reject(self, value):
        with self.assertRaises((ValueError, TypeError, RecursionError)):
            M.check(reseal(value))

    def test_01_all_frozen_sources(self):
        M.authenticate()
        self.assertEqual(len(M.BINDINGS), 7)
        for row in M.BINDINGS:
            raw = subprocess.check_output(
                ["git", "show", row["commit"] + ":" + row["path"]], cwd=ROOT
            )
            self.assertEqual(
                hashlib.sha1(
                    b"blob " + str(len(raw)).encode() + b"\0" + raw
                ).hexdigest(),
                row["git_blob"],
            )
            self.assertEqual(
                hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest(),
                row["sha256_lf"],
            )

    def test_02_fixture_full_rebuild(self):
        self.assertEqual(M.decode(M.file_bytes(PATH.with_suffix(".json"))), self.value)
        self.assertTrue(M.check(self.value))

    def test_03_delta_independent_log_derivative(self):
        u = [1]
        for n in range(1, 4):
            value = -24 * sum(
                sum(d for d in range(1, j + 1) if j % d == 0) * u[n - j]
                for j in range(1, n + 1)
            )
            self.assertEqual(value % n, 0)
            u.append(value // n)
        self.assertEqual([0] + u, self.value["native"]["delta"])

    def test_04_delta_independent_E6(self):
        e4 = [1] + [
            240 * sum(d**3 for d in range(1, n + 1) if n % d == 0) for n in range(1, 5)
        ]
        e6 = [1] + [
            -504 * sum(d**5 for d in range(1, n + 1) if n % d == 0) for n in range(1, 5)
        ]
        e43 = conv(conv(e4, e4, 4), e4, 4)
        e62 = conv(e6, e6, 4)
        numer = [a - b for a, b in zip(e43, e62)]
        self.assertTrue(all(x % 1728 == 0 for x in numer))
        self.assertEqual([x // 1728 for x in numer], self.value["native"]["delta"])

    def test_05_actual_Miller_shear(self):
        native = self.value["native"]
        delta = native["delta"]
        e4 = native["E4"]
        f0 = conv(delta, conv(conv(e4, e4, 4), e4, 4), 4)
        b = conv(delta, delta, 4)
        self.assertEqual(f0, native["f0"])
        self.assertEqual(b, native["b"])
        self.assertEqual([a - 696 * c for a, c in zip(f0, b)], native["g"])
        self.assertEqual(
            native["q_rows"], [[1, 0], [0, 1], [195660, -48], [12080128, 1080]]
        )

    def test_06_formal_log_det_independent_permutations(self):
        rows = self.value["native"]["q_rows"]
        for l2, l3 in ((Q(1), Q(2)), (Q(2, 3), Q(5, 4)), (Q(5), Q(7))):
            logs = [0, l2, l3, 2 * l2]
            stack = [
                [(Q(v), Q(0)) for v in row + [logs[j] * x for x in row]]
                for j, row in enumerate(rows)
            ]
            det = rawdet(stack)
            self.assertEqual(det, (l2 * (211312800 * l3 + 1159692288 * (l3 - l2)), 0))
            self.assertGreater(det[0], 0)
        self.assertEqual(
            self.value["native"]["formal_log_determinant_L2_L3"],
            [[1, 1, 1371005088], [2, 0, -1159692288]],
        )

    def test_07_all48_derivatives_independent_Stirling(self):
        stirling = [[1]]
        for r in range(1, 17):
            prev = stirling[-1]
            stirling.append(
                [0]
                + [
                    (prev[j - 1] if j - 1 < len(prev) else 0)
                    + (j * prev[j] if j < len(prev) else 0)
                    for j in range(1, r + 1)
                ]
            )
        for row in self.value["derivative_panel"]:
            r, q = row["order"], Q(row["q"])
            target = q + sum(
                (
                    stirling[r][j]
                    * q**j
                    * (-1) ** j
                    * math.factorial(j)
                    / (1 + q) ** (j + 1)
                    for j in range(1, r + 1)
                ),
                Q(0),
            )
            self.assertEqual(target, Q(row["value"]))

    def test_08_full_derivative_coverage_and_negative_controls(self):
        rows = self.value["derivative_panel"]
        self.assertEqual(
            [(r["order"], r["q"]) for r in rows],
            [(n, q) for n in range(1, 17) for q in ("1/3", "1/2", "2/3")],
        )
        negatives = [(r["order"], r["q"]) for r in rows if Q(r["value"]) < 0]
        self.assertEqual(len(negatives), 12)
        self.assertEqual(negatives[0], (7, "1/3"))
        self.assertEqual(M.derivative(7, Q(1, 3)), Q(-3311, 12288))

    def test_09_synthetic_positive_matrix_and_scalar_quotient(self):
        for q in (Q(1, 3), Q(1, 2), Q(2, 3)):
            a = [[(1 + q, 0), (q, 0)], [(q, 0), (q + q * q, 0)]]
            self.assertGreater(rawdet(a)[0], 0)
            self.assertEqual(rawdet(a)[0] / (q + q * q), 1 + q * q / (1 + q))

    def test_10_kernel_postscout_independent(self):
        row = self.value["post_scout_kernel"]
        nodes = list(map(Q, row["q_nodes"]))
        for q in nodes:
            self.assertLess(2 * q * q, 1)  # z=-log(q)/log2 >1/2.
        kernel = [
            [(1 + (q * r) ** 2 / (1 + q * r), Q(0)) for r in nodes] for q in nodes
        ]
        self.assertEqual(kernel, unpack(row["matrix"]))
        self.assertEqual(rawdet(kernel), (Q(-81, 8808800), Q(0)))
        leading = [Q(1)] + [rawdet([r[:j] for r in kernel[:j]])[0] for j in range(1, 4)]
        self.assertEqual(
            [leading[j] / leading[j - 1] for j in range(1, 4)],
            list(map(Q, row["LDL_pivots"])),
        )
        self.assertEqual(row["LDL_pivots"], ["91/90", "1189/89180", "-5103/7481188"])
        self.assertFalse(row["preregistered_before_first_scout"])

    def test_11_three_feature_definitions(self):
        rows = self.value["features"]
        self.assertEqual([r["id"] for r in rows], [1, 2, 3])
        self.assertEqual(rows[1]["frequencies"], ["1", "2", "3", "4"])
        self.assertEqual(rows[1]["weights"], [str(Q(1, n**25)) for n in range(1, 5)])
        self.assertIn("NOT log n", self.value["coverage"]["feature_frequencies"])

    def test_12_independent_moment_Gram_rebuild(self):
        for record in self.value["features"]:
            rows = unpack(record["rows"])
            nu = list(map(Q, record["frequencies"]))
            weights = list(map(Q, record["weights"]))
            for j in range(3):
                self.assertEqual(
                    rawgram(rows, nu, weights, j), unpack(record["moments"][j])
                )

    def test_13_independent_complex_congruences(self):
        for record in self.value["features"]:
            c = unpack(record["basis"])
            self.assertNotEqual(rawdet(c), (0, 0))
            for j in range(3):
                a = unpack(record["moments"][j])
                self.assertEqual(
                    rawcongruence(a, c), unpack(record["transformed_moments"][j])
                )
            self.assertEqual(
                rawcongruence(unpack(record["variance"]), c),
                unpack(record["transformed_variance"]),
            )

    def test_14_all_principal_minors_independent(self):
        for record in self.value["features"]:
            m0, m1, m2 = map(unpack, record["moments"])
            block = [a + b for a, b in zip(m0, m1)] + [a + b for a, b in zip(m1, m2)]
            for key, a in (
                ("moment0_positive_minors", m0),
                ("block_positive_semidefinite_minors", block),
                ("variance_positive_semidefinite_minors", unpack(record["variance"])),
            ):
                rows = record[key]
                expected = [
                    ind
                    for n in range(1, len(a) + 1)
                    for ind in itertools.combinations(range(len(a)), n)
                ]
                self.assertEqual([tuple(r["indices"]) for r in rows], expected)
                for item in rows:
                    inds = item["indices"]
                    det = rawdet([[a[i][j] for j in inds] for i in inds])
                    self.assertEqual(det, (Q(item["determinant"]), 0))
                    self.assertGreaterEqual(det[0], 0)

    def test_15_variance_block_determinants_and_rank(self):
        dets = []
        for record in self.value["features"]:
            a, b, c = map(unpack, record["moments"])
            block = [x + y for x, y in zip(a, b)] + [x + y for x, y in zip(b, c)]
            vd = rawdet(unpack(record["variance"]))[0]
            self.assertEqual(rawdet(block)[0], rawdet(a)[0] * vd)
            self.assertEqual(record["variance"], record["residual_gram"])
            dets.append(vd)
        self.assertEqual(dets[0], 0)
        self.assertGreater(dets[1], 0)
        self.assertEqual(dets[2], 0)

    def test_16_soft_exact_complete_coverage(self):
        target = [
            (i, r, str(t))
            for i, d in ((1, 2), (2, 2), (3, 3))
            for r in range(1, d)
            for t in (Q(3, 2), Q(2), Q(5))
        ]
        self.assertEqual(
            [
                (r["system"], r["quotient_dimension"], r["t"])
                for r in self.value["soft_reciprocal_pairs"]
            ],
            target,
        )
        self.assertEqual(len(target), 12)
        self.assertIn(
            "not one theta function", self.value["coverage"]["reciprocal_pair_contract"]
        )

    def test_17_soft_pair_reciprocity_entrywise(self):
        for item in self.value["soft_reciprocal_pairs"]:
            t = Q(item["t"])
            q, qr = (
                unpack(item["quotient_vacuum_difference"]),
                unpack(item["reciprocal_difference"]),
            )
            for i, j in itertools.product(range(len(q)), repeat=2):
                self.assertEqual(
                    q[i][j], (qr[i][j][0] / t + (1 / t - 1) * (i == j), qr[i][j][1] / t)
                )

    def test_18_soft_complex_quotient_congruence(self):
        for item in self.value["soft_reciprocal_pairs"]:
            r = item["quotient_dimension"]
            a = unpack(item["adapted_basis"])
            self.assertNotEqual(rawdet(a), (0, 0))
            self.assertTrue(
                all(a[i][j] == (0, 0) for i in range(r) for j in range(r, len(a)))
            )
            aq = [row[:r] for row in a[:r]]
            q = unpack(item["quotient_vacuum_difference"])
            self.assertEqual(
                rawcongruence(q, aq), unpack(item["transformed_difference"])
            )

    def test_19_soft_minors_and_quotient_determinant_ratios(self):
        for item in self.value["soft_reciprocal_pairs"]:
            r = item["quotient_dimension"]
            m0 = unpack(item["R_t"])
            h = [
                [zadd(m0[i][j], (Q(i == j), Q(0))) for j in range(len(m0))]
                for i in range(len(m0))
            ]
            q = unpack(item["quotient_vacuum_difference"])
            sh = [
                [zadd(q[i][j], (Q(i == j), Q(0))) for j in range(r)] for i in range(r)
            ]
            bottom = [row[r:] for row in h[r:]]
            self.assertEqual(rawdet(h)[0], rawdet(sh)[0] * rawdet(bottom)[0])
            for key, field in (
                ("positive_minors", "quotient_vacuum_difference"),
                ("reciprocal_positive_minors", "reciprocal_difference"),
                ("congruence_positive_minors", "transformed_difference"),
            ):
                mat = unpack(item[field])
                for minor in item[key]:
                    inds = minor["indices"]
                    self.assertEqual(
                        rawdet([[mat[i][j] for j in inds] for i in inds]),
                        (Q(minor["determinant"]), 0),
                    )
                    self.assertGreater(Q(minor["determinant"]), 0)

    def test_20_dropping_transformed_vacuum_is_detected(self):
        item = self.value["soft_reciprocal_pairs"][0]
        # Schur(A* I A)=A_Q* A_Q=2, not the scalar identity1.
        g = unpack(item["transformed_vacuum"])
        quotient = rawdet(g)[0] / g[1][1][0]
        self.assertEqual(quotient, 2)
        self.assertNotEqual(quotient, 1)

    def test_21_gaussian_inverse_and_scalar_guards(self):
        a = M.matrix([[(1, 1), 2], [(0, 1), 3]])
        self.assertEqual(M.product(a, M.inverse(a)), M.eye(2))
        self.assertEqual(M.product(M.inverse(a), a), M.eye(2))
        with self.assertRaises(ValueError):
            M.inverse([[1, 2], [2, 4]])
        with self.assertRaises(ValueError):
            M.div(1, 0)
        for bad in (True, False, 1.0, "1", None, 2**4097, Q(1, 2**4097)):
            with self.assertRaises(ValueError):
                M.rational(bad)

    def test_22_matrix_and_feature_caps(self):
        for bad in ([], [[1]] * 7, [[1] * 7], [[1, 2], [3]], [[True]], [[1.0]]):
            with self.assertRaises(ValueError):
                M.matrix(bad)
        with self.assertRaises(ValueError):
            M.gram([[1]] * 6, [1] * 6)
        with self.assertRaises(ValueError):
            M.gram([[1]], [-1])
        with self.assertRaises(ValueError):
            M.schur([[1, 0], [0, 1]], True)
        with self.assertRaises(ValueError):
            M.psd_minors([[1]], 1)
        with self.assertRaises(ValueError):
            M.formal_log_determinant([[1, 0]] * 5)
        with self.assertRaises(ValueError):
            M.formal_log_determinant([[True, 0]] * 4)

    def test_23_derivative_polynomial_resource_guards(self):
        for r in (True, -1, 17, 10000):
            with self.assertRaises(ValueError):
                M.derivative(r, Q(1, 3))
        for q in (0, 1, -1, True, 0.5):
            with self.assertRaises(ValueError):
                M.derivative(2, q)
        with self.assertRaises(ValueError):
            M.polynomial([1] * 21)
        with self.assertRaises(ValueError):
            M.convolution([1], [1], 5)
        with (
            mock.patch.object(M, "WORK", M.CAPS["work_units"]),
            self.assertRaises(ValueError),
        ):
            M.charge()

    def test_24_JSON_fail_closed(self):
        for raw in (
            b'{"x":1,"x":2}',
            b'{"x":1.0}',
            b'{"x":NaN}',
            b'{"x":Infinity}',
            b"null",
            b"[" * 26 + b"0" + b"]" * 26,
            b" " * 3000001,
        ):
            with self.assertRaises((ValueError, RecursionError)):
                M.decode(raw)
        with self.assertRaises(ValueError):
            M.typed({"x" * 4097: 1})

    def test_25_resealed_native_and_derivative_mutations(self):
        mutations = [
            lambda v: v["native"]["q_rows"][2].__setitem__(0, 195661),
            lambda v: v["native"]["formal_log_determinant_L2_L3"][0].__setitem__(2, 1),
            lambda v: v["derivative_panel"][0].__setitem__("value", "0"),
            lambda v: v["derivative_panel"].pop(),
            lambda v: v["post_scout_kernel"].__setitem__(
                "preregistered_before_first_scout", True
            ),
        ]
        for change in mutations:
            value = copy.deepcopy(self.value)
            change(value)
            self.reject(value)

    def test_26_resealed_moment_and_flag_mutations(self):
        mutations = [
            lambda v: v["features"][1]["frequencies"].__setitem__(0, "log(1)"),
            lambda v: v["features"][0]["variance"][0][0].__setitem__(0, "1"),
            lambda v: v["soft_reciprocal_pairs"].pop(),
            lambda v: v["soft_reciprocal_pairs"][0]["transformed_difference"][0][
                0
            ].__setitem__(0, "0"),
            lambda v: v["soft_reciprocal_pairs"][0].__setitem__(
                "quotient_dimension", True
            ),
        ]
        for change in mutations:
            value = copy.deepcopy(self.value)
            change(value)
            self.reject(value)

    def test_27_resealed_scope_type_caps(self):
        for field, new in (("schema", "wrong"), ("extra", 1), ("work_units", 0)):
            value = copy.deepcopy(self.value)
            value[field] = new
            self.reject(value)
        for key, val in (
            ("arithmetic_class", "FLOAT"),
            ("rounding", "nearest"),
            ("analytic_claims_machine_certified", True),
        ):
            value = copy.deepcopy(self.value)
            value["contract"][key] = val
            self.reject(value)
        value = copy.deepcopy(self.value)
        value["coverage"]["derivatives"] = True
        self.reject(value)

    def test_28_source_seal_mutations(self):
        for j in range(7):
            value = copy.deepcopy(self.value)
            value["sources"][j]["sha256_lf"] = "0" * 64
            self.reject(value)

    def test_29_true_source_bytes_corruption(self):
        original = M.subprocess.check_output
        for selected in M.BINDINGS:

            def corrupted(args, *, cwd, chosen=selected):
                raw = original(args, cwd=cwd)
                return (
                    raw + b"\n"
                    if args[2] == chosen["commit"] + ":" + chosen["path"]
                    else raw
                )

            with (
                mock.patch.object(M.subprocess, "check_output", side_effect=corrupted),
                self.assertRaises(ValueError),
            ):
                M.authenticate()

    def test_30_artifact_hash_mutations(self):
        for path in M.ARTIFACTS:
            value = copy.deepcopy(self.value)
            value["artifact_sha256_lf"][path] = "0" * 64
            self.reject(value)
        actual = Path.read_bytes
        for selected in M.ARTIFACTS:

            def corrupt(path, chosen=ROOT / selected):
                raw = actual(path)
                return raw + b" " if path == chosen else raw

            with (
                mock.patch.object(Path, "read_bytes", corrupt),
                self.assertRaises(ValueError),
            ):
                M.check(self.value)

    def test_31_independent_payload_digest(self):
        unsigned = copy.deepcopy(self.value)
        seal = unsigned.pop("payload_sha256")
        self.assertEqual(
            hashlib.sha256(
                json.dumps(
                    unsigned, sort_keys=True, separators=(",", ":"), allow_nan=False
                ).encode()
            ).hexdigest(),
            seal,
        )
        self.assertEqual(len(unsigned["artifact_sha256_lf"]), 4)

    def test_32_no_assert_author_acceptance(self):
        tree = ast.parse(PATH.read_text(encoding="utf8"))
        self.assertFalse(any(isinstance(n, ast.Assert) for n in ast.walk(tree)))

    def test_33_science_vs_finite_boundary(self):
        c = self.value["contract"]
        self.assertEqual(c["arithmetic_class"], "MIXED")
        self.assertEqual(
            c["components"], ["EXACT_RATIONAL", "CERTIFIED_INTEGER_COVERAGE"]
        )
        self.assertEqual(c["rounding"], "none")
        self.assertFalse(c["analytic_claims_machine_certified"])
        self.assertTrue(c["no_period_theta_gamma_zeta_zero_evaluation"])
        self.assertIn("period Schur equals source quotient", self.value["not_claimed"])

    def test_34_cli_check(self):
        result = subprocess.run(
            [sys.executable, "-B", str(PATH), "--check"],
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr.decode())
        self.assertIn(b"48 derivatives", result.stdout)

    def test_35_cli_emits(self):
        for action, suffix in (
            ("--emit", ".json"),
            ("--emit-sources", ".sources.json"),
        ):
            data = subprocess.check_output([sys.executable, "-B", str(PATH), action])
            self.assertEqual(
                data.replace(b"\r\n", b"\n"),
                PATH.with_suffix(suffix).read_bytes().replace(b"\r\n", b"\n"),
            )

    def test_36_cli_and_optimized_hostile_controls(self):
        for args in ([], ["--unknown"], ["--check", "--emit"]):
            self.assertNotEqual(
                subprocess.run(
                    [sys.executable, "-B", str(PATH), *args],
                    capture_output=True,
                    check=False,
                ).returncode,
                0,
            )
        code = (
            "import importlib.util;p=r'"
            + str(PATH)
            + "';s=importlib.util.spec_from_file_location('m',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);m.derivative(True,m.Q(1,3))"
        )
        for flags in ([], ["-O"]):
            p = subprocess.run(
                [sys.executable, "-B", *flags, "-c", code],
                capture_output=True,
                check=False,
            )
            self.assertNotEqual(p.returncode, 0)
            self.assertIn(b"integer type/range", p.stderr)


if __name__ == "__main__":
    unittest.main()
