"""Independent Gaussian/cofactor/orthogonalization controls and hostile inputs."""

import ast
import copy
import hashlib
import importlib.util
import itertools
import unittest
from dataclasses import dataclass
from fractions import Fraction as Q
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "research/exploratory/coprime_infinite_height_physical_capture.py"
SPEC = importlib.util.spec_from_file_location("cp_tested", SOURCE)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


@dataclass(frozen=True)
class Z:
    r: Q = Q(0)
    i: Q = Q(0)

    def __add__(self, other):
        other = cast(other)
        return Z(self.r + other.r, self.i + other.i)

    __radd__ = __add__

    def __neg__(self):
        return Z(-self.r, -self.i)

    def __sub__(self, other):
        return self + (-cast(other))

    def __rsub__(self, other):
        return cast(other) + (-self)

    def __mul__(self, other):
        other = cast(other)
        return Z(
            self.r * other.r - self.i * other.i, self.r * other.i + self.i * other.r
        )

    __rmul__ = __mul__

    def conjugate(self):
        return Z(self.r, -self.i)

    def square_norm(self):
        return self.r**2 + self.i**2

    def __truediv__(self, other):
        other = cast(other)
        out = self * other.conjugate()
        d = other.square_norm()
        return Z(out.r / d, out.i / d)

    def __rtruediv__(self, other):
        return cast(other) / self


def cast(x):
    return x if type(x) is Z else Z(Q(x))


def decoded(a):
    return [[Z(Q(v[0]), Q(v[1])) for v in row] for row in a]


def determinant(a):
    n = len(a)
    out = Z()
    for p in itertools.permutations(range(n)):
        v = cast((-1) ** sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n)))
        for i in range(n):
            v *= a[i][p[i]]
        out += v
    return out


def inverse(a):
    n = len(a)
    det = determinant(a)
    return [
        [
            cast((-1) ** (i + j))
            * determinant(
                [[a[u][v] for v in range(n) if v != i] for u in range(n) if u != j]
            )
            / det
            for j in range(n)
        ]
        for i in range(n)
    ]


def ip(a, b, g):
    return sum(
        a[i].conjugate() * g[i][j] * b[j] for i in range(len(a)) for j in range(len(b))
    )


def orthogonal_coefficients(g):
    out = []
    for j in range(len(g)):
        v = [cast(int(j == k)) for k in range(len(g))]
        for q, norm in out:
            coefficient = ip(q, v, g) / norm
            v = [a - coefficient * b for a, b in zip(v, q)]
        norm = ip(v, v, g)
        if norm.i != 0 or norm.r <= 0:
            raise ValueError("independent Gram-Schmidt positivity")
        out.append((v, norm.r))
    return out


def independent_schur(g, d, cross):
    h = [row[:] for row in g]
    for q, norm in orthogonal_coefficients(d):
        overlap = [
            sum(q[j].conjugate() * cross[j][k] for j in range(len(d)))
            for k in range(len(g))
        ]
        for i in range(len(g)):
            for j in range(len(g)):
                h[i][j] -= overlap[i].conjugate() * overlap[j] / norm
    return h


def physical_by_orthogonalization(g, h):
    return sum(ip(q, q, h) / norm for q, norm in orthogonal_coefficients(g))


class CaptureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = M.build_report()

    def test_01_fixture_payload_and_complete_reconstruction(self):
        data = M.parse_json(M.FIXTURE.read_bytes())
        M.validate_report(data)
        self.assertEqual(M.canonical(data), M.canonical(self.report))

    def test_02_independent_Gram_entries(self):
        for row in self.report["two_route_finite_projection_controls"]:
            bn = [(Q(a), Q(y)) for a, y in row["B_nodes"]]
            un = [(Q(a), Q(y)) for a, y in row["U_nodes"]]
            for key, left, right in [
                ("Gram_unnormalized", bn, bn),
                ("U_Gram_unnormalized", un, un),
                ("cross_Gram_U_B", un, bn),
            ]:
                expected = [
                    [1 / Z(y + eta, a - x) for a, eta in right] for x, y in left
                ]
                self.assertEqual(decoded(row[key]), expected)

    def test_03_all_inverses_by_cofactor(self):
        for row in self.report["two_route_finite_projection_controls"]:
            self.assertEqual(
                inverse(decoded(row["Gram_unnormalized"])), decoded(row["Gram_inverse"])
            )

    def test_04_normalized_determinant_by_permutations(self):
        for row in self.report["two_route_finite_projection_controls"]:
            g = decoded(row["Gram_unnormalized"])
            det = determinant([[2 * z for z in r] for r in g])
            self.assertEqual(det, Z(Q(row["normalized_B_Gram_determinant"])))
            self.assertGreater(det.r, Q(3, 4) ** len(g))

    def test_05_projection_Schur_by_orthogonalization(self):
        for row in self.report["two_route_finite_projection_controls"]:
            h = independent_schur(
                decoded(row["Gram_unnormalized"]),
                decoded(row["U_Gram_unnormalized"]),
                decoded(row["cross_Gram_U_B"]),
            )
            self.assertEqual(h, decoded(row["physical_Gram_values"]))
            self.assertEqual(h, decoded(row["physical_Gram_Schur"]))

    def test_06_physical_trace_by_B_orthogonalization(self):
        for row in self.report["two_route_finite_projection_controls"]:
            out = physical_by_orthogonalization(
                decoded(row["Gram_unnormalized"]), decoded(row["physical_Gram_values"])
            )
            self.assertEqual(out, Z(Q(row["physical_trace"])))

    def test_07_product_values_with_direct_linear_factors(self):
        for row in self.report["two_route_finite_projection_controls"]:
            roots = [Z(Q(a), Q(y)) for a, y in row["U_nodes"]]
            expected = []
            for a, y in row["B_nodes"]:
                z, value = Z(Q(a), Q(y)), cast(1)
                for u in roots:
                    value *= (1 - z / u) / (1 - z / u.conjugate())
                expected.append([str(value.r), str(value.i)])
            self.assertEqual(expected, row["U_values_at_B_nodes"])

    def test_08_matched_factor_strict_global_bounds(self):
        for row in self.report["two_route_finite_projection_controls"]:
            if row["all_matching_factors_present"]:
                values = [Z(Q(v[0]), Q(v[1])) for v in row["U_values_at_B_nodes"]]
                self.assertEqual(
                    sum(z.square_norm() for z in values),
                    Q(row["actual_projection_kernel_mass"]),
                )
                self.assertLess(Q(row["physical_trace"]), Q(1, 9))
                for n, z in enumerate(values, 1):
                    self.assertLessEqual(z.square_norm(), Q(1, (2 ** (n + 1) + 1) ** 2))

    def test_09_missing_matching_factor_is_not_small(self):
        row = M.finite_control(2, 1)
        self.assertFalse(row["all_matching_factors_present"])
        self.assertIsNone(row["matching_factor_mass_bound"])
        self.assertGreater(Q(row["physical_trace"]), 1)
        self.assertFalse(row["global_1_over_9_bound_applies_to_this_finite_control"])

    def test_10_heldout_all_prefix_pairs(self):
        for n, m in [(1, 4), (3, 1), (4, 2), (4, 3), (1, 2), (2, 3)]:
            row = M.finite_control(n, m)
            g, h = (
                decoded(row["Gram_unnormalized"]),
                decoded(row["physical_Gram_values"]),
            )
            self.assertEqual(
                physical_by_orthogonalization(g, h), Z(Q(row["physical_trace"]))
            )

    def test_11_Gram_Riesz_bounds_by_principal_minors(self):
        g = [
            [2 * z for z in r]
            for r in decoded(M.finite_control(4, 4)["Gram_unnormalized"])
        ]
        for n in range(1, 5):
            low = [
                [g[i][j] - Q(3, 4) * int(i == j) for j in range(n)] for i in range(n)
            ]
            high = [
                [Q(5, 4) * int(i == j) - g[i][j] for j in range(n)] for i in range(n)
            ]
            for a in [low, high]:
                det = determinant(a)
                self.assertEqual(det.i, 0)
                self.assertGreater(det.r, 0)

    def test_12_row_and_cross_bounds_no_square_roots(self):
        for n in range(1, 9):
            for m in range(1, 9):
                if m == n:
                    continue
                delta = 16 * (2**n - 2**m)
                square = Q(4, 4 + delta**2)
                self.assertLess(square, Q(1, 8 * abs(2**n - 2**m)) ** 2)
                if m < n:
                    self.assertLess(square, Q(1, 4 * 2**n) ** 2)
            row = M.geometric_control(n)
            self.assertLessEqual(Q(row["left_row_majorant"]), Q(1, 8))
            self.assertLessEqual(Q(row["right_infinite_row_majorant"]), Q(1, 8))

    def test_13_coprime_distinct_and_infinite_height_prefixes(self):
        for n in range(1, 9):
            b, u = M.point(n), M.point(n, True)
            self.assertEqual(b[0], u[0])
            self.assertNotEqual(b[1], u[1])
            self.assertGreaterEqual(b[1], 1)
            self.assertGreater(u[1], 1)
            self.assertEqual(
                Q(M.geometric_control(n)["U_height_prefix"]),
                sum(M.point(k, True)[1] for k in range(1, n + 1)),
            )
            for m in range(1, 9):
                self.assertNotEqual(b, M.point(m, True))

    def test_14_one_node_projection_is_pseudohyperbolic(self):
        row = M.finite_control(1, 1)
        self.assertEqual(row["physical_trace"], "1/25")
        for n in range(1, 9):
            value = M.factor_at(M.point(n), M.point(n, True))
            self.assertEqual(M.norm2(value), Q(1, (2 ** (n + 1) + 1) ** 2))

    def test_15_geometric_tail_arithmetic(self):
        for n in range(1, 9):
            row = M.geometric_control(n)
            exact_tail = Q(1, 4) * Q(1, 4 ** (n + 1)) / (1 - Q(1, 4))
            self.assertEqual(Q(row["kernel_mass_tail_bound"]), exact_tail)
            self.assertEqual(
                Q(row["cross_Gram_squared_HS_bound"]),
                Q(n, 16) * Q(1, 4 ** (n + 1)) / (1 - Q(1, 4)),
            )
            self.assertLessEqual(n, 2**n)

    def test_16_overlap_corrected_tail_coefficients(self):
        for n in range(1, 9):
            row = M.geometric_control(n)
            overlap = Q(row["prefix_overlap_squared_operator_bound"])
            residual = 2 * (Q(row["kernel_mass_tail_bound"]) + overlap / 9)
            self.assertEqual(Q(row["residual_frame_squared_HS_bound"]), residual)
            self.assertEqual(
                Q(row["orthogonal_source_squared_HS_tail_bound"]), Q(4, 3) * residual
            )
            self.assertGreater(
                Q(row["orthogonal_source_squared_HS_tail_bound"]),
                Q(4, 3) * Q(row["kernel_mass_tail_bound"]),
            )

    def test_17_prefix_capture_difference_orthogonal_coordinates(self):
        for row in self.report["orthogonal_prefix_controls"]:
            data = M.finite_control(row["full_finite_B"], row["fixed_finite_U"])
            g, h = (
                decoded(data["Gram_unnormalized"]),
                decoded(data["physical_Gram_values"]),
            )
            tail = sum(
                ip(q, q, h) / norm
                for q, norm in orthogonal_coefficients(g)[row["retained"] :]
            )
            self.assertEqual(tail, Z(Q(row["orthogonal_source_tail"])))
            self.assertLessEqual(tail.r, Q(row["analytic_tail_upper"]))
            self.assertGreaterEqual(tail.r, 0)

    def test_18_Riesz_residual_Schur_lower_bound(self):
        data = M.finite_control(4, 4)
        g = [[2 * z for z in r] for r in decoded(data["Gram_unnormalized"])]
        for n in range(1, 4):
            prefix = [r[:n] for r in g[:n]]
            cross = [r[n:] for r in g[:n]]
            tail = [r[n:] for r in g[n:]]
            residual = independent_schur(tail, prefix, cross)
            lower = [
                [v - Q(3, 4) * int(i == j) for j, v in enumerate(row)]
                for i, row in enumerate(residual)
            ]
            for k in range(1, len(lower) + 1):
                det = determinant([r[:k] for r in lower[:k]])
                self.assertEqual(det.i, 0)
                self.assertGreater(det.r, 0)

    def test_19_strict_rational_Gaussian_types_and_bits(self):
        for value in [True, False, 1.0, "1", None, 2**32, Q(1, 2**32), complex(1)]:
            with self.assertRaises(ValueError):
                M.gaussian(value)
        for value in [[1], [1, 2, 3], [True, 1], [Q(1), 1.0]]:
            with self.assertRaises(ValueError):
                M.gaussian(value)
        with self.assertRaises(ValueError):
            M.rational(2**4096, internal=True)
        with self.assertRaises(ValueError):
            M.gaussian(1, internal=1)

    def test_20_scalar_and_node_caps(self):
        for n in [True, 0, 9, 1.0]:
            with self.assertRaises(ValueError):
                M.point(n)
        with self.assertRaises(ValueError):
            M.point(1, 1)
        for rows in [[], [(1, 0)], [(1, 3)], [(4097, 1)], [(1, 1)] * 2, [(1, 1, 1)]]:
            with self.assertRaises(ValueError):
                M.nodes(rows)
        for n, m in [(0, 1), (1, 5), (True, 1), (1, 1.0)]:
            with self.assertRaises(ValueError):
                M.finite_control(n, m)

    def test_21_matrix_and_work_caps_before_expansion(self):
        for a in [[], [[]], [[1]] * 5, [[1, 1], [1]], [[True]]]:
            with self.assertRaises(ValueError):
                M.matrix(a)
        for v in [True, 0, 200001, 1.0]:
            with self.assertRaises(ValueError):
                M.Budget(v)
        work = M.Budget(1)
        with self.assertRaises(ValueError):
            M.kernel_gram([M.point(1), M.point(2)], [M.point(1), M.point(2)], work)
        self.assertEqual(work.used, 0)
        with self.assertRaises(ValueError):
            M.finite_control(1, 1, object())
        with self.assertRaises(ValueError):
            M.inverse_det([[0]], M.Budget())
        with self.assertRaises(ValueError):
            M.prefix_control(2, 3, 2)

    def test_22_sources_and_artifact_locks(self):
        M.authenticate()
        self.assertEqual(len(M.BINDINGS), 2)
        self.assertEqual(len(self.report["artifact_sha256_lf"]), 4)
        for path, digest in self.report["artifact_sha256_lf"].items():
            raw = (
                (ROOT / path).read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            )
            self.assertEqual(hashlib.sha256(raw).hexdigest(), digest)

    def test_23_manifest_operator_and_source_tampering(self):
        for key, value in [
            ("projection", "P_KU"),
            ("construction", "common zeros"),
            ("tail", "vary U"),
        ]:
            manifest = M.expected_manifest()
            manifest["primitive_contract"][key] = value
            with self.assertRaises(ValueError):
                M.authenticate(manifest)
        manifest = M.expected_manifest()
        manifest["external_context"]["remote_bytes_authenticated"] = 0
        with self.assertRaises(ValueError):
            M.authenticate(manifest)

    def test_24_primitive_bytes_fail_closed(self):
        with (
            patch.object(M.subprocess, "check_output", side_effect=[b"1", b"x"]),
            self.assertRaisesRegex(ValueError, "primitive identity"),
        ):
            M.authenticate()
        with patch.object(
            M.subprocess, "check_output", return_value=b"2000001"
        ) as mock:
            with self.assertRaisesRegex(ValueError, "byte cap"):
                M.authenticate()
            self.assertEqual(mock.call_count, 1)

    def test_25_JSON_duplicate_nonfinite_float_and_caps(self):
        for raw in [
            b'{"x":1,"x":2}',
            b'{"x":NaN}',
            b'{"x":Infinity}',
            b'{"x":1.0}',
            b'{"x":1e3}',
            b"{",
            b" " * 2000001,
            b"[" * 26 + b"0" + b"]" * 26,
        ]:
            with self.assertRaises(ValueError):
                M.parse_json(raw)
        for data in [[0] * 1025, {"x": "a" * 4097}, 2**4096, {1: "x"}]:
            with self.assertRaises(ValueError):
                M.canonical(data)

    def test_26_LF_manifest_copy_and_seal_tamper(self):
        self.assertEqual(M.lf_sha(b"a\r\nb\r"), M.lf_sha(b"a\nb\n"))
        manifest = M.expected_manifest()
        manifest["frozen_sources"][0]["commit"] = "x"
        self.assertNotEqual(M.BINDINGS[0]["commit"], "x")
        data = copy.deepcopy(self.report)
        data["payload_sha256"] = "0" * 64
        with self.assertRaises(ValueError):
            M.validate_report(data)
        with self.assertRaises(ValueError):
            M.seal(self.report)

    def test_27_resealed_physical_and_conjugation_tamper(self):
        variants = []
        for field, value in [
            ("physical_trace", "0"),
            ("all_matching_factors_present", 1),
            ("normalized_B_Gram_determinant", "2"),
            ("actual_projection_kernel_mass", "0"),
        ]:
            data = copy.deepcopy(self.report)
            data.pop("payload_sha256")
            data["two_route_finite_projection_controls"][0][field] = value
            variants.append(data)
        data = copy.deepcopy(self.report)
        data.pop("payload_sha256")
        data["two_route_finite_projection_controls"][1]["physical_Gram_values"][0][1][
            1
        ] = "0"
        variants.append(data)
        with patch.object(M, "build_report", return_value=self.report):
            for data in variants:
                with self.assertRaisesRegex(ValueError, "typed reconstruction"):
                    M.validate_report(M.seal(data))

    def test_28_resealed_scope_and_overlap_tamper(self):
        for section, field, value in [
            ("scope", "actual_Xi_physical_capture", True),
            ("scope", "global_numerator_transmitted_trace_finite", True),
            ("scope", "denominator_already_reduced", False),
            ("scope", "numerical_transcendental_samples", False),
            ("caps", "work", True),
            (
                "analytic_constants",
                "orthogonal_tail_bound",
                "sum omitted kernel masses",
            ),
        ]:
            data = copy.deepcopy(self.report)
            data.pop("payload_sha256")
            data[section][field] = value
            with (
                patch.object(M, "build_report", return_value=self.report),
                self.assertRaises(ValueError),
            ):
                M.validate_report(M.seal(data))

    def test_29_scope_firewalls(self):
        scope = self.report["scope"]
        for key in [
            "global_numerator_transmitted_trace_finite",
            "bounded_band_numerator_transmitted_verdict",
            "actual_Xi_physical_capture",
            "physical_T_uniformity",
            "RH_or_GRH_claim",
            "analytic_limits_machine_certified",
            "novelty_claim",
        ]:
            self.assertIs(scope[key], False)
        for key in [
            "both_unweighted_heights_infinite",
            "coprime_inner_divisors",
            "denominator_already_reduced",
            "corrected_physical_global_trace_finite",
            "bare_every_positive_measure_band_trace_infinite",
        ]:
            self.assertIs(scope[key], True)

    def test_30_arithmetic_taxonomy_and_coverage(self):
        self.assertEqual(self.report["arithmetic_class"], "MIXED")
        self.assertEqual(
            self.report["arithmetic_components"],
            ["CERTIFIED_INTEGER_COVERAGE", "EXACT_RATIONAL"],
        )
        self.assertEqual(self.report["coverage"]["finite_models"], 7)
        self.assertEqual(self.report["coverage"]["projection_routes"], 2)
        self.assertEqual(self.report["coverage"]["prefix_controls"], 5)
        self.assertLessEqual(self.report["coverage"]["charged_work"], M.MAX_WORK)

    def test_31_no_assert_float_complex_or_transcendental_calls(self):
        tree = ast.parse(SOURCE.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(n, ast.Assert) for n in ast.walk(tree)))
        self.assertFalse(
            any(
                isinstance(n, ast.Constant) and type(n.value) in (float, complex)
                for n in ast.walk(tree)
            )
        )
        prohibited = {"exp", "log", "sqrt", "gamma", "sin", "cos", "complex", "float"}
        for n in ast.walk(tree):
            if isinstance(n, ast.Call):
                name = (
                    n.func.id
                    if isinstance(n.func, ast.Name)
                    else n.func.attr
                    if isinstance(n.func, ast.Attribute)
                    else ""
                )
                self.assertNotIn(name, prohibited)

    def test_32_Gaussian_arithmetic_and_guarded_domains(self):
        for a, b in [((Q(1, 3), Q(-2, 5)), (Q(7, 4), Q(3))), ((1, 2), (3, -1))]:
            z, w = Z(*map(Q, a)), Z(*map(Q, b))
            for function, expected in [
                (M.zadd, z + w),
                (M.zsub, z - w),
                (M.zmul, z * w),
                (M.zdiv, z / w),
            ]:
                self.assertEqual(function(a, b), (expected.r, expected.i))
        with self.assertRaises(ValueError):
            M.zdiv(1, 0)
        with self.assertRaises(ValueError):
            M.real((1, 1))
        with self.assertRaises(ValueError):
            M.product_at(M.point(1), [M.point(1, True)], object())


if __name__ == "__main__":
    unittest.main()
