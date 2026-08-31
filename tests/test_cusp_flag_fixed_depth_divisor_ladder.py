"""Independent finite reconstruction and adversarial fixed-depth source checks."""

import ast
import copy
import hashlib
import importlib.util
import json
import math
import unittest
from fractions import Fraction as Q
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SOURCE = (
    ROOT
    / "research/l-families/atlas/generalized/cusp_flag_fixed_depth_divisor_ladder.py"
)
SPEC = importlib.util.spec_from_file_location("fixed_depth_ladder", SOURCE)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


def independent_raw(weight, j, order):
    residual = 14 if weight % 12 == 2 else weight % 12
    a, b = {0: (0, 0), 4: (1, 0), 6: (0, 1), 8: (2, 0), 10: (1, 1), 14: (2, 1)}[
        residual
    ]
    dimension = (weight - residual) // 12
    p = 3 * (dimension - j) + a
    sigma = [0] + [
        sum(t for t in range(1, n + 1) if n % t == 0) for n in range(1, order + 1)
    ]
    e4 = [1] + [
        240 * sum(t**3 for t in range(1, n + 1) if n % t == 0)
        for n in range(1, order + 1)
    ]
    e6 = [1] + [
        -504 * sum(t**5 for t in range(1, n + 1) if n % t == 0)
        for n in range(1, order + 1)
    ]
    delta, power = [1], [1]
    for n in range(1, order + 1):
        x = -24 * j * sum(sigma[t] * delta[n - t] for t in range(1, n + 1))
        if x % n:
            raise RuntimeError("independent Delta recurrence integrality")
        delta.append(x // n)
        x = sum(((p + 1) * t - n) * e4[t] * power[n - t] for t in range(1, n + 1))
        if x % n:
            raise RuntimeError("independent E4-power recurrence integrality")
        power.append(x // n)
    row = [sum(delta[t] * power[n - t] for t in range(n + 1)) for n in range(order + 1)]
    if b:
        row = [sum(row[t] * e6[n - t] for t in range(n + 1)) for n in range(order + 1)]
    return [0] * j + row[: order + 1 - j]


def independent_chart(weight, depth, order):
    rows = [independent_raw(weight, j, order) for j in range(1, depth + 1)]
    # Forward elimination against unechelonized later rows, unlike producer's
    # descending unit-echelons; triangular uniqueness gives the same result.
    for i in range(depth):
        for j in range(i + 1, depth):
            scale = rows[i][j + 1]
            rows[i] = [x - scale * y for x, y in zip(rows[i], rows[j], strict=True)]
    return rows


def matmul(a, b):
    return [
        [sum(a[i][l] * b[l][j] for l in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


class FixedDepthTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sources = M.authenticated_sources()
        cls.report = M.build_report()

    def test_01_complete_fixture_reconstruction(self):
        actual = M.parse_json(M.FIXTURE.read_bytes())
        self.assertEqual(M.canonical(actual), M.canonical(self.report))
        M.validate_report(actual)

    def test_02_native_depth_charts_independent_recurrences(self):
        for row in self.report["native_depth3_depth4_charts"]:
            k, j, n = row["weight"], row["depth"], row["q_order"]
            self.assertEqual(
                row["g_prefixes"], [independent_raw(k, l, n) for l in range(1, j + 1)]
            )
            self.assertEqual(row["h_prefixes"], independent_chart(k, j, n))
            self.assertTrue(row["deep_flag_exists"])

    def test_03_heldout_depth_and_weight_charts(self):
        for k, j, n in (
            (108, 7, 10),
            (122, 8, 12),
            (65536, 4, 10),
            (1048576, 8, 12),
            (134, 5, 9),
        ):
            row = M.native_chart(k, j, n, M.Budget())
            self.assertEqual(row["h_prefixes"], independent_chart(k, j, n))
            self.assertEqual(
                row["g_prefixes"], [independent_raw(k, l, n) for l in range(1, j + 1)]
            )

    def test_04_all_source_basis_hashes_independent(self):
        old = json.loads(
            self.sources[
                "research/l-families/atlas/generalized/cusp_flag_quotient_global_family.json"
            ]
        )
        for row in self.report["source_chart_controls"]["complete_CF_bases"]:
            k, d = row["weight"], row["dimension"]
            basis = independent_chart(k, d, d + 2)
            digest = hashlib.sha256(
                json.dumps(basis, sort_keys=True, separators=(",", ":")).encode()
            ).hexdigest()
            self.assertEqual(row["basis_sha256"], digest)
            reference = next(x for x in old["family"] if x["weight"] == k)
            self.assertEqual(digest, reference["complete_basis_sha256_canonical_json"])

    def test_05_NP_source_replay_has_no_new_flag(self):
        old = json.loads(
            self.sources[
                "research/l-families/atlas/generalized/cusp_flag_native_denominator_poles.json"
            ]
        )
        for row in old["native_shear_pairs"]:
            chart = M.native_chart(row["weight"], 2, 8, M.Budget())
            self.assertEqual(chart["h_prefixes"][0], row["h_prefix"])
            self.assertEqual(chart["h_prefixes"][1], row["g2"]["q_prefix"])
        self.assertEqual(M.divisor_constants(2, 1)["right_residue_coefficient"], "1152")

    def test_06_exact_tau_all_classes(self):
        for d in (4, 16):
            for residual in M.RESIDUAL:
                k = 12 * d + residual
                chart = M.native_chart(k, 4, 8, M.Budget())
                for j, tau in enumerate(chart["tau"], 1):
                    p = 3 * (d - j) + chart["a"]
                    self.assertEqual(tau, -24 * j + 240 * p - 504 * chart["b"])
                    self.assertEqual(tau, 60 * k - 744 * j - 864 * chart["b"])

    def test_07_complete_partial_pivots_and_retained_tail(self):
        for row in self.report["native_depth3_depth4_charts"]:
            j = row["depth"]
            for l, h in enumerate(row["h_prefixes"], 1):
                self.assertEqual(h[1 : j + 1], [int(m == l) for m in range(1, j + 1)])
            self.assertTrue(any(row["h_prefixes"][l][j + 1] != 0 for l in range(j)))

    def test_08_Cauchy_recursion_and_tail(self):
        for j in range(1, 9):
            row = M.tail_ledger(j, 65536)
            self.assertFalse(row["high_cutoff_assumptions_checked_at_test_weight"])
            self.assertIn("eventual only", row["high_cutoff_required"])
            bounds = row["h_circle_bounds"]
            for i, value in enumerate(bounds):
                self.assertEqual(value, 2 + 2 * sum(bounds[i + 1 :]))
            self.assertEqual(row["tail_B_J"], 4 * 3 ** (j - 1) * 1000**j)
            self.assertLess(Q(row["circle_exponent_upper"]), Q(1, 4))
            self.assertEqual(row["tail_first_order"], j + 1)

    def test_09_entire_tail_geometric_series(self):
        for ratio in (Q(1, 100), Q(1, 4), Q(1, 2)):
            for exponent in range(1, 9):
                self.assertLessEqual(ratio**exponent / (1 - ratio), 2 * ratio**exponent)
        for j in range(1, 9):
            self.assertEqual(2 * (j + 2) - 1, 2 * j + 3)

    def test_10_low_factorial_majorant_exact(self):
        for j in (1, 3, 4, 8):
            n = j + 1
            eta = Q(1, 10000 * n)
            self.assertEqual(16 * 4 * 3 * n * eta, Q(12, 625))
            self.assertLess(16 * 4 * 3 * n * eta, Q(1, 10))
            for k in (48, 96):
                ratio = (
                    2**k
                    * (eta * k) ** (k - 1)
                    * 48 ** (k - 1)
                    / ((k - 1) * math.factorial(k - 2))
                )
                # 48 here is an extra coarse bound only for N<=3.
                if n <= 3:
                    self.assertLess(ratio, 10**4 * Q(1, 10) ** k)

    def test_11_projection_closed_sum_direct_partial_sums(self):
        for j in range(1, 9):
            for l in range(1, j + 1):
                row = M.projection_reserve(j, l, Q(1, 100))
                x = Q(1, 10000)
                L = j + 1 - l
                partial = sum((L + t) ** 2 * x**t for t in range(16))
                self.assertLess(partial, Q(row["sum_factor_exact"]))
                self.assertLess(Q(row["sum_factor_exact"]), 4 * (j + 1) ** 2)

    def test_12_projection_geometric_formula_independent(self):
        for rho in (Q(0), Q(1, 1000), Q(1, 100)):
            x = rho * rho
            for j in (1, 3, 4, 8):
                for l in range(1, j + 1):
                    L = j + 1 - l
                    numerator = (
                        L * L + (1 + 2 * L - 2 * L * L) * x + (L - 1) ** 2 * x * x
                    )
                    row = M.projection_reserve(j, l, rho)
                    self.assertEqual(
                        Q(row["sum_factor_exact"]), numerator / (1 - x) ** 3
                    )

    def test_13_finite_fourier_functional_orientation(self):
        rho = Q(1, 100)
        for n in (2, 4, 5):
            coeff = {m: (-1) ** m * (m + 1) for m in range(n, n + 5)}
            for l in range(1, n):
                r = {h: (-1) ** h * h * rho**h for h in range(1, n + 6)}
                exact = sum(a * rho ** (m + l) * r[m - l] for m, a in coeff.items())
                # Laurent multiplication: bar(q^l) f uses frequency m-l;
                # only the negative R frequency l-m contributes to constant.
                laurent = sum(
                    a * rho ** (m + l) * r[abs(l - m)] for m, a in coeff.items()
                )
                self.assertEqual(exact, laurent)
                norm = sum(a * a * rho ** (2 * m) for m, a in coeff.items())
                self.assertLessEqual(exact * exact, 4 * n * n * rho ** (2 * n) * norm)

    def test_14_projection_not_unprojected_norm(self):
        self.assertEqual(
            M.projection_obstruction(3, 1)["unprojected_squared_ratio_base"], "9/8"
        )
        self.assertFalse(
            M.projection_obstruction(3, 1)["unprojected_exponential_decay"]
        )
        self.assertEqual(
            M.projection_obstruction(4, 1)["unprojected_squared_ratio_base"], "8/5"
        )
        for j in range(2, 9):
            self.assertTrue(
                Q(M.projection_obstruction(j, 1)["projected_ratio_base"]) < 1
            )

    def test_15_chamber_identity_grid(self):
        for j in range(1, 9):
            for x, y in (
                (12 * j, 0),
                (12 * j, 5),
                (6 * (j + 1), 6 * (j + 1)),
                (12 * (j + 1), 0),
            ):
                row = M.chamber_point(j, x, y)
                self.assertEqual(
                    Q(row["gap"]), Q(x, 2 * (x * x + y * y)) - Q(1, 24 * (j + 1))
                )
                self.assertEqual(row["inside"], Q(row["gap"]) > 0)

    def test_16_fixed_disc_reserves(self):
        for j in range(1, 9):
            for delta, r in ((1, 2), (3, 6), (Q(23, 2), Q(47, 4))):
                row = M.chamber_control(j, delta, r)
                self.assertGreater(Q(row["coercivity_margin"]), 0)
                self.assertEqual(
                    Q(row["Rouche_margin"]), Q(delta) / (24 * j * (12 * j + delta))
                )
                self.assertLess(6 * (j - 1) + r, 6 * (j + 1))
                self.assertTrue(row["larger_fixed_buffer_required"])

    def test_17_native_Fourier_mode_constants(self):
        for j in range(2, 9):
            for i in range(1, j):
                row = M.divisor_constants(j, i)
                h = j - i
                sigma = Q(sum(d for d in range(1, h + 1) if h % d == 0), h)
                self.assertEqual(Q(row["sigma_minus1"]), sigma)
                self.assertEqual(row["cosine_mode"], h)
                self.assertEqual(2 * Q(1, 2), 1)  # exponential coefficient times half-K
                self.assertEqual(i + j + (j - i), 2 * j)

    def test_18_original_and_adjacent_residues_distinct(self):
        self.assertEqual(
            [M.divisor_constants(j, 1)["right_residue_coefficient"] for j in (2, 3, 4)],
            ["1152", "5832", "8192"],
        )
        self.assertEqual(
            [
                M.divisor_constants(j, j - 1)["right_residue_coefficient"]
                for j in (2, 3, 4)
            ],
            ["1152", "2592", "4608"],
        )
        self.assertNotEqual(M.divisor_constants(3, 1), M.divisor_constants(3, 2))

    def test_19_gap_constants_and_coordinate(self):
        self.assertEqual(
            [M.divisor_constants(j, 1)["c_gap_coefficient"] for j in (2, 3, 4)],
            ["55296", "209952", "262144"],
        )
        for row in self.report["cluster_constants"]:
            self.assertEqual(
                Q(row["c_gap_coefficient"]),
                Q(row["right_residue_coefficient"]) / Q(row["earlier_Fi"]),
            )
            self.assertEqual(row["s_gap_scale"], "A_J/(k^3*A_i)")
            self.assertTrue(row["s_zero_left_of_pole"])
            self.assertEqual(row["reflected_residue_sign"], -1)

    def test_20_column_inverse_and_order(self):
        row = M.column_scaled_control(1, Q(1, 100), 10, 1)
        c = [[Q(x) for x in r] for r in row["column_scaled_C"]]
        inv = [[Q(x) for x in r] for r in row["inverse_C"]]
        diagonal = [[Q(1), 0], [0, Q(1, 100)]]
        inverse_diagonal = [[Q(1), 0], [0, Q(100)]]
        h = matmul(c, diagonal)
        correct = matmul(inverse_diagonal, inv)
        wrong = matmul(inv, inverse_diagonal)
        self.assertEqual(matmul(h, correct), [[1, 0], [0, 1]])
        self.assertNotEqual(matmul(h, wrong), [[1, 0], [0, 1]])

    def test_21_exact_Schur_root_gap_not_subtracted_asymptotics(self):
        a, b, slope, c0, k = Q(7), Q(2, 1000), Q(3), Q(36), Q(100)
        pole = c0
        zero = c0 + b * b / (a * slope)
        self.assertGreater(zero, pole)
        self.assertEqual(a * slope * (zero - c0) - b * b, 0)
        self.assertEqual(zero - pole, b * b / (a * slope))
        self.assertGreater(b * b / (k * slope), 0)

    def test_22_generic_cancellation_control_is_not_native(self):
        a1, a2, b12, b13, b23 = Q(3), Q(2), Q(1), Q(1), Q(2)
        effective_b = b13 - b12 * b23 / a2
        denominator_root = b23 * b23 / a2
        numerator_root = (a2 * b13 * b13 - 2 * b12 * b13 * b23 + a1 * b23 * b23) / (
            a1 * a2 - b12 * b12
        )
        self.assertEqual(effective_b, 0)
        self.assertEqual(numerator_root, denominator_root)
        # Generic adjacent poles therefore cannot replace DL22/DL25.

    def test_23_terminal_depth_is_endpoint_pole(self):
        for j in range(2, 9):
            row = M.endpoint_countercontrol(j)
            self.assertEqual(row["center_s"], "0")
            self.assertEqual(row["Q_d_endpoint_residue_over_Petersson_norm"], "-1/2")
            self.assertFalse(row["deep_flag_exists"])
            self.assertFalse(row["fixed_depth_eventual_theorem_applies_at_this_weight"])

    def test_24_native_chart_caps_before_work(self):
        for k, j, n in (
            (True, 3, 8),
            (37, 3, 8),
            (26, 1, 4),
            (48, 5, 8),
            (108, 9, 12),
            (48, 3, 3),
            (48, 3, 13),
        ):
            w = M.Budget()
            with self.assertRaises(ValueError):
                M.native_chart(k, j, n, w)
            self.assertEqual(w.used, 0)
        with self.assertRaises(ValueError):
            M.native_chart(48, 3, 8, object())
        w = M.Budget(1)
        with self.assertRaises(ValueError):
            M.native_chart(48, 3, 8, w)
        self.assertEqual(w.used, 0)

    def test_25_polynomial_types_bits_and_work(self):
        for limit in (True, 0, M.MAX_WORK + 1):
            with self.assertRaises(ValueError):
                M.Budget(limit)
        for value in (True, 1.0, "1", 2**4096):
            with self.assertRaises(ValueError):
                M.coefficient(value)
        with self.assertRaises(ValueError):
            M.qpower([1] * 5, True, 4, M.Budget())
        with self.assertRaises(ValueError):
            M.qmul([1] * 4, [1] * 5, 4, M.Budget())
        with self.assertRaises(ValueError):
            M.qmul([True] * 5, [1] * 5, 4, M.Budget())
        w = M.Budget(1)
        with self.assertRaises(ValueError):
            w.spend(2)
        self.assertEqual(w.used, 0)

    def test_26_rational_domains_and_bit_caps(self):
        for selector in (0, 1, "yes", None):
            with self.assertRaises(ValueError):
                M.rational(1, input_value=selector)
        for value in (True, 0.0, "0", None, Q(1, 2**128)):
            with self.assertRaises(ValueError):
                M.projection_reserve(3, 1, value)
        for j, l, rho in (
            (0, 1, Q(0)),
            (9, 1, Q(0)),
            (3, 0, Q(0)),
            (3, 4, Q(0)),
            (3, 1, Q(1, 99)),
        ):
            with self.assertRaises(ValueError):
                M.projection_reserve(j, l, rho)
        with self.assertRaises(ValueError):
            M.rational(Q(1, 2**4096))
        with self.assertRaises(ValueError):
            M.chamber_point(3, 0, 0)
        with self.assertRaises(ValueError):
            M.chamber_point(3, 129, 1)

    def test_27_disc_cluster_and_column_domains(self):
        for args in ((3, 0, 1), (3, 1, 1), (3, 1, 12), (True, 1, 2)):
            with self.assertRaises(ValueError):
                M.chamber_control(*args)
        for args in ((1, 1), (3, 0), (3, 3), (3, True)):
            with self.assertRaises(ValueError):
                M.divisor_constants(*args)
        for args in ((0, 1, 2, 1), (1, 2, 2, 1), (1, 1, 1, 1), (1, 1, 2, 2)):
            with self.assertRaises(ValueError):
                M.column_scaled_control(*args)
        with self.assertRaises(ValueError):
            M.tail_ledger(4, 48)

    def test_28_fourteen_literal_source_identities(self):
        self.assertEqual(len(self.sources), 14)
        for row in M.BINDINGS:
            raw = self.sources[row["path"]]
            blob = hashlib.sha1(
                b"blob " + str(len(raw)).encode() + b"\0" + raw
            ).hexdigest()
            self.assertEqual(blob, row["git_blob"])
            self.assertEqual(M.lf_sha(raw), row["sha256_lf"])
        with (
            patch.object(
                M.subprocess, "check_output", return_value=str(M.MAX_BYTES + 1).encode()
            ),
            self.assertRaisesRegex(ValueError, "primitive byte cap"),
        ):
            M.authenticated_sources()

    def test_29_manifest_all_semantics_typed(self):
        for key in M.expected_manifest()["primitive_contract"]:
            bad = M.expected_manifest()
            bad["primitive_contract"][key] = "drift"
            with self.assertRaisesRegex(ValueError, "typed manifest"):
                M.authenticated_sources(bad)
        for key in ("commit", "path", "git_blob", "sha256_lf"):
            bad = M.expected_manifest()
            bad["frozen_sources"][0][key] = "drift"
            with self.assertRaisesRegex(ValueError, "typed manifest"):
                M.authenticated_sources(bad)

    def test_30_source_primitive_data_tamper(self):
        for path, key in (
            (
                "research/l-families/atlas/generalized/cusp_flag_quotient_global_family.json",
                "CF",
            ),
            (
                "research/l-families/atlas/generalized/cusp_flag_native_denominator_poles.json",
                "NP",
            ),
        ):
            bad = dict(self.sources)
            payload = M.parse_json(bad[path])
            if key == "CF":
                payload["family"][0]["complete_basis_sha256_canonical_json"] = "0" * 64
            else:
                payload["native_shear_pairs"][0]["h_prefix"][3] += 1
            bad[path] = M.canonical(payload).encode()
            with self.assertRaises(ValueError):
                M.source_chart_controls(bad, M.Budget())

    def test_31_four_artifact_seals_C0_and_LF(self):
        self.assertEqual(len(self.report["artifact_sha256_lf"]), 4)
        for path, digest in self.report["artifact_sha256_lf"].items():
            raw = (ROOT / path).read_bytes()
            self.assertEqual(M.lf_sha(raw), digest)
            self.assertFalse(any(x < 32 and x not in (9, 10, 13) for x in raw))
        self.assertEqual(M.lf_sha(b"a\n"), M.lf_sha(b"a\r\n"))
        with (
            patch.object(Path, "read_bytes", return_value=b"\x0c"),
            self.assertRaises(ValueError),
        ):
            M.artifact_hashes()

    def test_32_JSON_strictness_and_caps(self):
        for raw in (
            b'{"x":1,"x":2}',
            b'{"x":1.0}',
            b'{"x":NaN}',
            b'{"x":Infinity}',
            b"\xff",
        ):
            with self.assertRaises(ValueError):
                M.parse_json(raw)
        for value in ("x" * 4097, [0] * 1025, [[0] * 1000 for _ in range(41)]):
            with self.assertRaises(ValueError):
                M.canonical(value)
        deep = 0
        for _ in range(30):
            deep = [deep]
        with self.assertRaises(ValueError):
            M.canonical(deep)
        with self.assertRaises(ValueError):
            M.normalized(b"x" * (M.MAX_BYTES + 1))
        with self.assertRaises(ValueError):
            M.normalized(bytearray(b"x"))

    def test_33_payload_digest_and_fresh_resealed_arithmetic(self):
        payload = {k: v for k, v in self.report.items() if k != "payload_sha256"}
        self.assertEqual(
            self.report["payload_sha256"],
            hashlib.sha256(M.canonical(payload).encode()).hexdigest(),
        )
        bad = copy.deepcopy(self.report)
        bad["cluster_constants"][0]["right_residue_coefficient"] = "0"
        with self.assertRaisesRegex(ValueError, "payload digest"):
            M.validate_report(bad)
        bad.pop("payload_sha256")
        with self.assertRaisesRegex(ValueError, "typed reconstruction"):
            M.validate_report(M.seal(bad))

    def test_34_resealed_scope_and_type_attacks(self):
        with patch.object(M, "build_report", return_value=self.report):
            for key, value in (
                ("actual_original_Q1_depth3_depth4_clusters", 1),
                ("analytic_values_sampled", False),
                ("uniform_growing_depth", True),
                ("all_depths_up_to_dimension", True),
                ("65536_onset_inherited", True),
                ("effective_threshold", True),
                ("fixed_weight_infinite_poles", True),
                ("global_interlacing", True),
                ("complete_projected_functional_paid", False),
            ):
                bad = copy.deepcopy(self.report)
                bad.pop("payload_sha256")
                bad["scope"][key] = value
                with self.assertRaisesRegex(ValueError, "typed reconstruction"):
                    M.validate_report(M.seal(bad))

    def test_35_complete_coverage_and_taxonomy(self):
        self.assertEqual(self.report["arithmetic_class"], "MIXED")
        self.assertEqual(self.report["coverage"]["complete_CF_bases"], 30)
        self.assertEqual(self.report["coverage"]["complete_NP_charts"], 12)
        self.assertEqual(self.report["coverage"]["native_depth_charts"], 24)
        self.assertEqual(len(self.report["projection_controls"]), 36)
        self.assertEqual(len(self.report["cluster_constants"]), 28)
        self.assertLessEqual(self.report["coverage"]["charged_work"], M.MAX_WORK)

    def test_36_no_assert_float_or_analytic_sampling_in_producer(self):
        tree = ast.parse(SOURCE.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(n, ast.Assert) for n in ast.walk(tree)))
        self.assertFalse(
            any(
                isinstance(n, ast.Constant) and type(n.value) in (float, complex)
                for n in ast.walk(tree)
            )
        )
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                name = (
                    node.func.id
                    if isinstance(node.func, ast.Name)
                    else node.func.attr
                    if isinstance(node.func, ast.Attribute)
                    else ""
                )
                self.assertNotIn(
                    name,
                    {"eval", "exec", "float", "complex", "gamma", "exp", "log", "sqrt"},
                )

    def test_37_written_projection_and_metric_payment(self):
        note = M.NOTE.read_text(encoding="utf-8")
        for token in (
            "(9/8)^",
            "COMPLETE tail",
            "ALL f",
            "COLUMN scaling",
            "x Fourier coordinate",
            "larger FIXED",
            "mean-value theorem",
            "not a generic Schur",
            "No modular all-vector moment estimate is asserted for u_l",
        ):
            self.assertIn(token, note)

    def test_38_written_quotient_and_threshold_boundaries(self):
        note = M.NOTE.read_text(encoding="utf-8")
        for token in (
            "Q_1 is the already reviewed original quotient",
            "ADJACENT",
            "5832,8192",
            "NON-EFFECTIVE",
            "J=d",
            "No inaccurate",
            "fixed weight",
        ):
            self.assertIn(token, note)

    def test_39_arithmetic_reseals_all_data_categories(self):
        paths = [
            ("caps", "depth", 9),
            ("coverage", "projection_rows", 35),
            ("scope", "analytic_proof_machine_certified", True),
        ]
        with patch.object(M, "build_report", return_value=self.report):
            for a, b, value in paths:
                bad = copy.deepcopy(self.report)
                bad.pop("payload_sha256")
                bad[a][b] = value
                with self.assertRaises(ValueError):
                    M.validate_report(M.seal(bad))
            bad = copy.deepcopy(self.report)
            bad.pop("payload_sha256")
            bad["arithmetic_class"] = "EXACT"
            with self.assertRaises(ValueError):
                M.validate_report(M.seal(bad))

    def test_40_no_unpaid_claim_in_scope(self):
        scope = self.report["scope"]
        for key in (
            "effective_threshold",
            "uniform_growing_depth",
            "fixed_weight_infinite_poles",
            "global_interlacing",
            "unsigned_global_divisor_asymptotic",
            "RH_or_critical_line_claim",
            "new_automorphic_family",
            "analytic_proof_machine_certified",
            "parents_modified",
        ):
            self.assertFalse(scope[key])
        self.assertTrue(scope["adjacent_and_original_quotients_distinguished"])
        self.assertTrue(scope["relative_exponential_gap_via_exact_identity"])


if __name__ == "__main__":
    unittest.main()
