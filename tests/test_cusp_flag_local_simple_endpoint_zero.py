"""Exact complex-domain controls and source firewalls; no period/zero sampling."""

import ast
import copy
import hashlib
import importlib.util
import unittest
from fractions import Fraction as Q
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SOURCE = (
    ROOT
    / "research/l-families/atlas/generalized/cusp_flag_local_simple_endpoint_zero.py"
)
SPEC = importlib.util.spec_from_file_location("local_simple_endpoint", SOURCE)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


def independent_prefix(k, j, n):
    r = 14 if k % 12 == 2 else k % 12
    pairs = {0: (0, 0), 4: (1, 0), 6: (0, 1), 8: (2, 0), 10: (1, 1), 14: (2, 1)}
    a, b = pairs[r]
    d = (k - r) // 12
    p = 3 * (d - j) + a
    sigma1 = [0] + [
        sum(x for x in range(1, t + 1) if t % x == 0) for t in range(1, n + 1)
    ]
    e4 = [1] + [
        240 * sum(x**3 for x in range(1, t + 1) if t % x == 0) for t in range(1, n + 1)
    ]
    e6 = [1] + [
        -504 * sum(x**5 for x in range(1, t + 1) if t % x == 0) for t in range(1, n + 1)
    ]
    delta, power = [1], [1]
    for t in range(1, n + 1):
        num = -24 * j * sum(sigma1[i] * delta[t - i] for i in range(1, t + 1))
        if num % t:
            raise RuntimeError("independent Delta integrality")
        delta.append(num // t)
        num = sum(((p + 1) * i - t) * e4[i] * power[t - i] for i in range(1, t + 1))
        if num % t:
            raise RuntimeError("independent E4 integrality")
        power.append(num // t)
    values = [sum(delta[i] * power[t - i] for i in range(t + 1)) for t in range(n + 1)]
    if b:
        values = [
            sum(values[i] * e6[t - i] for i in range(t + 1)) for t in range(n + 1)
        ]
    return [0] * j + values[: n + 1 - j]


class LocalSimpleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sources = M.authenticated_sources()
        cls.aw = M.source_module(cls.sources, "allweight")
        cls.ep = M.source_module(cls.sources, "endpoint")
        cls.report = M.build_report()

    def test_01_fixture_complete(self):
        fixture = M.parse_json(M.FIXTURE.read_bytes())
        self.assertEqual(M.canonical(fixture), M.canonical(self.report))
        M.validate_report(fixture)

    def test_02_disc_identity_independent_grid(self):
        for x in (1, 3, 6, 12, 18, 24, 30):
            for y in (-15, -7, 0, 4, 12):
                row = M.point_control(x, y)
                gap = Q(x, 2 * (x * x + y * y)) - Q(1, 48)
                self.assertEqual(Q(row["coercivity_gap"]), gap)
                self.assertEqual(gap > 0, (x - 12) ** 2 + y * y < 144)

    def test_03_gaussian_fraction_points(self):
        for x, y in ((Q(1, 3), Q(1, 7)), (Q(25, 2), Q(-7, 3)), (Q(47, 2), 0)):
            row = M.point_control(x, y)
            c_inverse = M.zdiv((1, 0), (x, y))
            self.assertEqual(Q(row["coercivity_gap"]), c_inverse[0] / 2 - Q(1, 48))
            conjugate = M.point_control(x, -y)
            self.assertEqual(row["coercivity_gap"], conjugate["coercivity_gap"])

    def test_04_boundary_and_exterior_not_coercive(self):
        for x, y in ((24, 0), (12, 12), (12, -12)):
            self.assertEqual(M.point_control(x, y)["coercivity_gap"], "0")
        for x, y in ((25, 0), (-1, 0), (12, 13)):
            self.assertLess(Q(M.point_control(x, y)["coercivity_gap"]), 0)
        with self.assertRaisesRegex(ValueError, "pole"):
            M.point_control(0, 0)

    def test_05_fixed_radius_exact_lower_bounds(self):
        for delta, radius in ((1, 2), (3, 6), (6, 9), (Q(23, 2), Q(47, 4))):
            row = M.radius_control(delta, radius)
            self.assertEqual(
                Q(row["m_R"]), Q(144 - radius**2) / (48 * (12 + radius) ** 2)
            )
            self.assertEqual(Q(row["Rouche_lower"]), Q(delta) / (24 * (12 + delta)))
            self.assertEqual(Q(row["kappa_R"]), Q(row["m_R"]) / 2)
            self.assertGreater(Q(row["pole_distance"]), 0)

    def test_06_radius_sharp_real_boundary_control(self):
        for radius in (Q(1, 2), Q(3), Q(11)):
            row = M.radius_control(radius / 2, radius)
            point = M.point_control(12 + radius, 0)
            self.assertEqual(row["m_R"], point["coercivity_gap"])
            delta = radius / 2
            f = Q(1, 24) - 1 / (2 * (12 + delta))
            self.assertEqual(f, Q(row["Rouche_lower"]))

    def test_07_true_analytic_Schur(self):
        row = M.orientation_control()
        self.assertEqual(row["actual_correction"], ["-1", "1"])
        self.assertEqual(row["false_adjoint_correction"], ["1", "1"])
        self.assertNotEqual(row["actual_correction"], row["false_adjoint_correction"])
        self.assertFalse(row["native_cusp_matrix"])

    def test_08_general_determinant_Schur_conjugation(self):
        for a, b, c, d in (
            ((2, 3), (1, -2), (-3, 1), (-1, 2)),
            ((Q(1, 2), 0), (0, 1), (2, 3), (-4, -1)),
        ):
            whole = [[a, b], [c, d]]
            schur = M.zadd(a, M.zneg(M.zdiv(M.zmul(b, c), d)))
            self.assertEqual(schur, M.zdiv(M.determinant(whole), d))
            star = M.adjoint(whole)
            self.assertEqual(M.zdiv(M.determinant(star), star[1][1]), M.zconj(schur))

    def test_09_nonnormal_inverse_exact(self):
        d = [[(-2, 0), (0, 1)], [(0, 1), (-1, 0)]]
        inv = [[(-Q(1, 3), 0), (0, -Q(1, 3))], [(0, -Q(1, 3)), (-Q(2, 3), 0)]]
        identity = M.matrix([[(1, 0), (0, 0)], [(0, 0), (1, 0)]])
        self.assertEqual(M.matmul(inv, d), identity)
        self.assertEqual(M.matmul(d, inv), identity)
        self.assertNotEqual(M.matmul(M.adjoint(d), d), M.matmul(d, M.adjoint(d)))
        row = M.nonnormal_control()
        self.assertEqual(row["principal_minors"], [4, 3])
        self.assertFalse(row["normal"])

    def test_10_nonnormal_inverse_inequality_on_vectors(self):
        d = [[(-2, 0), (0, 1)], [(0, 1), (-1, 0)]]
        for v in (((1, 0), (0, 0)), ((1, 2), (3, -1)), ((0, 1), (1, 0))):
            out = [M.zadd(M.zmul(row[0], v[0]), M.zmul(row[1], v[1])) for row in d]
            norm = lambda z: sum(a * a + b * b for a, b in z)
            self.assertGreaterEqual(norm(out), norm(v))

    def test_11_power_accounting_no_dimension_tax(self):
        row = M.power_accounting()
        self.assertEqual(row["row"] + row["inverse"] + row["column"], 1)
        self.assertEqual(row["normalized_power"], 0)
        self.assertFalse(row["complex_Schur_smallness_required"])

    def test_12_native_six_prefixes_independent(self):
        rows = self.report["native_six_class_prefixes"]
        self.assertEqual(len(rows), 12)
        self.assertEqual({r["r"] for r in rows}, {0, 4, 6, 8, 10, 14})
        for row in rows:
            self.assertEqual(
                row["q_prefix"],
                independent_prefix(row["weight"], row["delta_power"], row["q_order"]),
            )

    def test_13_native_leading_coefficients_and_flag(self):
        for row in self.report["native_six_class_prefixes"]:
            j = row["delta_power"]
            self.assertEqual(row["q_prefix"][:j], [0] * j)
            self.assertEqual(row["q_prefix"][j], 1)
            self.assertEqual(
                row["q_prefix"][j + 1], -24 * j + 240 * row["E4_power"] - 504 * row["b"]
            )
            self.assertEqual(row["is_in_W"], j == 2)
            if row["r"] == 14:
                self.assertEqual(row["dimension"], (row["weight"] - 14) // 12)

    def test_14_inherited_real_fine_ledger_not_simplicity(self):
        row = self.report["unchanged_real_location_ledger"]
        self.assertEqual(row, self.ep.location_ledger())
        self.assertEqual(row["first_scale"], 12)
        self.assertEqual(row["log_k_over_4pi_shift"], "288")
        self.assertFalse(row["uniqueness_or_simplicity"])
        self.assertTrue(self.report["scope"]["eventual_each_fixed_disc_unique_simple"])

    def test_15_taxonomy_and_caps(self):
        self.assertEqual(self.report["arithmetic_class"], "MIXED")
        self.assertEqual(
            self.report["arithmetic_components"],
            ["CERTIFIED_INTEGER_COVERAGE", "EXACT_RATIONAL"],
        )
        self.assertIn("no rounding", self.report["rounding_contract"])
        self.assertLessEqual(self.report["coverage"]["charged_work"], M.MAX_WORK)
        self.assertLessEqual(
            self.report["coverage"]["charged_source_work"], M.SOURCE_WORK
        )
        self.assertEqual(self.report["caps"]["matrix_size"], 2)

    def test_16_strict_point_inputs(self):
        for value in (True, False, 1.0, "1", None, Q(1, 2**128)):
            with self.assertRaises(ValueError):
                M.point_control(value, 1)
        for value in (33, -33):
            with self.assertRaises(ValueError):
                M.point_control(value, 1)

    def test_17_strict_radius_domain(self):
        for pair in (
            (0, 1),
            (1, 1),
            (2, 1),
            (1, 12),
            (1, 13),
            (True, 2),
            (1, "2"),
            (1, Q(1, 2**128)),
        ):
            with self.assertRaises(ValueError):
                M.radius_control(*pair)

    def test_18_gaussian_type_and_output_caps(self):
        for value in ((1,), (1, 2, 3), (True, 0), (1.0, 0), (1, "0"), complex(1, 1)):
            with self.assertRaises(ValueError):
                M.gaussian(value)
        with self.assertRaises(ValueError):
            M.rational(Q(1, 2**4096))
        with self.assertRaises(ValueError):
            M.zmul((2**4095, 0), (2, 0))
        with self.assertRaisesRegex(ValueError, "zero divisor"):
            M.zdiv((1, 0), (0, 0))

    def test_19_matrix_shape_caps(self):
        for value in (
            [],
            [[(1, 0)]],
            [[(1, 0)] * 3] * 3,
            [[(1, 0)] * 2, [(1, 0)]],
            True,
        ):
            with self.assertRaises(ValueError):
                M.matrix(value)
        with self.assertRaises(ValueError):
            M.matmul([[(1, 0)] * 2] * 2, [[(True, 0)] * 2] * 2)

    def test_20_work_and_source_budget(self):
        for limit in (True, 0, M.MAX_WORK + 1):
            with self.assertRaises(ValueError):
                M.Budget(limit)
        work = M.Budget(1)
        with self.assertRaises(ValueError):
            work.spend(2)
        self.assertEqual(work.used, 0)
        with self.assertRaises(ValueError):
            work.spend(True)
        with self.assertRaises(ValueError):
            M.native_controls(self.sources, self.aw, M.Budget())
        with self.assertRaises(ValueError):
            M.native_controls(self.sources, self.aw, self.aw.Budget(M.SOURCE_WORK + 1))
        with self.assertRaises(ValueError):
            M.native_controls(self.sources, self.aw, self.aw.Budget(1))

    def test_21_source_identity_before_execution(self):
        self.assertEqual(len(self.sources), 10)
        for name, stem in (
            ("allweight", "all_weight_endpoint_separation"),
            ("endpoint", "effective_endpoint_separation"),
        ):
            bad = dict(self.sources)
            path = "research/l-families/atlas/generalized/cusp_flag_" + stem + ".py"
            bad[path] += b"\n"
            with self.assertRaisesRegex(ValueError, "before execution"):
                M.source_module(bad, name)
        with (
            patch.object(
                M.subprocess, "check_output", return_value=str(M.MAX_BYTES + 1).encode()
            ),
            self.assertRaisesRegex(ValueError, "primitive byte cap"),
        ):
            M.authenticated_sources()

    def test_22_manifest_typed_and_fixed_enum(self):
        for key in ("AW", "EP", "new_complex", "normal_family", "Rouche", "excluded"):
            bad = M.expected_manifest()
            bad["primitive_contract"][key] = "drift"
            with self.assertRaisesRegex(ValueError, "typed manifest"):
                M.authenticated_sources(bad)
        for name in (True, None, "../allweight", "family"):
            with self.assertRaises(ValueError):
                M.source_module(self.sources, name)
        bad = M.expected_manifest()
        bad["frozen_sources"][0]["commit"] = "drift"
        self.assertEqual(M.BINDINGS[0]["commit"], M.BASE)

    def test_23_all_artifact_seals_and_C0_guard(self):
        self.assertEqual(len(self.report["artifact_sha256_lf"]), 4)
        for path, digest in self.report["artifact_sha256_lf"].items():
            raw = (ROOT / path).read_bytes()
            self.assertEqual(
                hashlib.sha256(
                    raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
                ).hexdigest(),
                digest,
            )
            self.assertFalse(any(v < 32 and v not in (9, 10, 13) for v in raw))
        with (
            patch.object(Path, "read_bytes", return_value=b"\x0c"),
            self.assertRaises(ValueError),
        ):
            M.artifact_hashes()

    def test_24_JSON_byte_and_depth_caps(self):
        for raw in (b'{"x":1,"x":2}', b'{"x":NaN}', b'{"x":1.0}', b"\xff"):
            with self.assertRaises(ValueError):
                M.parse_json(raw)
        for value in ([0] * 1025, "x" * 4097, [[0] * 1000 for _ in range(21)]):
            with self.assertRaises(ValueError):
                M.canonical(value)
        deep = 0
        for _ in range(26):
            deep = [deep]
        with self.assertRaises(ValueError):
            M.canonical(deep)
        with self.assertRaises(ValueError):
            M.normalized(b"x" * (M.MAX_BYTES + 1))
        self.assertEqual(M.lf_sha(b"a\nb\n"), M.lf_sha(b"a\r\nb\r\n"))

    def test_25_payload_digest(self):
        payload = {k: v for k, v in self.report.items() if k != "payload_sha256"}
        self.assertEqual(
            self.report["payload_sha256"],
            hashlib.sha256(M.canonical(payload).encode()).hexdigest(),
        )
        bad = copy.deepcopy(self.report)
        bad["scope"]["global_uniqueness"] = True
        with self.assertRaisesRegex(ValueError, "payload digest"):
            M.validate_report(bad)
        with self.assertRaises(ValueError):
            M.seal(self.report)

    def test_26_resealed_scope_type_attacks(self):
        with patch.object(M, "build_report", return_value=self.report):
            for key, value in (
                ("effective_simplicity_k0", True),
                ("65536_simplicity_inherited", True),
                ("complex_matrix_Hermitian_assumed", True),
                ("complex_Schur_correction_nonnegative", True),
                ("global_uniqueness", True),
                ("varying_delta", True),
                ("eventual_each_fixed_disc_unique_simple", 1),
                ("analytic_values_sampled", False),
            ):
                bad = copy.deepcopy(self.report)
                bad.pop("payload_sha256")
                bad["scope"][key] = value
                with self.assertRaisesRegex(ValueError, "typed reconstruction"):
                    M.validate_report(M.seal(bad))

    def test_27_resealed_arithmetic_control_attack(self):
        bad = copy.deepcopy(self.report)
        bad.pop("payload_sha256")
        bad["disc_point_controls"][0]["coercivity_gap"] = "1"
        with self.assertRaisesRegex(ValueError, "typed reconstruction"):
            M.validate_report(M.seal(bad))
        with patch.object(M, "build_report", return_value=self.report):
            bad["arithmetic_class"] = "EXACT"
            with self.assertRaises(ValueError):
                M.validate_report(M.seal(bad))

    def test_28_source_prefix_tamper(self):
        bad = dict(self.sources)
        path = "research/l-families/atlas/generalized/cusp_flag_all_weight_endpoint_separation.json"
        old = M.parse_json(bad[path])
        old["native_first_effective_prefixes"][0]["q_prefix"][2] += 1
        bad[path] = M.canonical(old).encode()
        with self.assertRaisesRegex(ValueError, "prefix agreement"):
            M.native_controls(bad, self.aw, self.aw.Budget(M.SOURCE_WORK))

    def test_29_heldout_native_prefixes(self):
        for k in (65548, 65550, 65552, 65554, 65556, 65558):
            for j in (1, 2):
                row = self.aw.native_prefix(k, j, 7, self.aw.Budget(M.SOURCE_WORK))
                self.assertEqual(row["q_prefix"], independent_prefix(k, j, 7))

    def test_30_no_assert_float_or_analytic_sampling(self):
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
                    name, {"float", "complex", "eval", "exp", "log", "gamma", "sqrt"}
                )

    def test_31_written_load_bearing_native_proof(self):
        note = M.NOTE.read_text(encoding="utf-8")
        for token in (
            "HERMITIAN PART",
            "O_R(\\log k)",
            "Weighted Cauchy--Schwarz",
            "EVERY subsequential",
            "COUNTING MULTIPLICITY",
            "two off-diagonal blocks",
            "no complex error-rate claim",
            "No numerical or effective rate",
        ):
            self.assertIn(token, note)

    def test_32_scope_not_global_or_effective(self):
        scope = self.report["scope"]
        for key in (
            "effective_simplicity_k0",
            "global_uniqueness",
            "whole_open_chamber_uniform_uniqueness",
            "varying_delta",
            "RH_or_new_automorphic_family",
            "analytic_proof_machine_certified",
            "parents_modified",
        ):
            self.assertFalse(scope[key])
        self.assertEqual(scope["analytic_values_sampled"], 0)
        self.assertTrue(scope["normal_family_no_complex_rate"])
        self.assertEqual(
            M.canonical(M.parse_json(M.MANIFEST.read_bytes())),
            M.canonical(M.expected_manifest()),
        )


if __name__ == "__main__":
    unittest.main()
