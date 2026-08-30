"""Finite replay plus independent q/ungrouped-word reconstructions; no analytic oracle."""

import copy
import importlib.util
import json
import math
import sys
import unittest
from fractions import Fraction as F
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
PATH = (
    ROOT / "research/l-families/atlas/generalized/cusp_flag_quotient_global_family.py"
)
SPEC = importlib.util.spec_from_file_location("cusp_flag_tested", PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("producer import unavailable")
m = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = m
SPEC.loader.exec_module(m)


def independent_basis(d, r, order):
    """Delta via its logarithmic derivative; no calls to producer mathematics."""

    def multiply(a, b):
        return [sum(a[j] * b[n - j] for j in range(n + 1)) for n in range(order + 1)]

    def power(a, n):
        result = [1] + [0] * order
        for _ in range(n):
            result = multiply(result, a)
        return result

    e4 = [1] + [
        240 * sum(t**3 for t in range(1, n + 1) if n % t == 0)
        for n in range(1, order + 1)
    ]
    e6 = [1] + [
        -504 * sum(t**5 for t in range(1, n + 1) if n % t == 0)
        for n in range(1, order + 1)
    ]
    unit = [1]
    for n in range(1, order):
        value = -24 * sum(
            sum(t for t in range(1, h + 1) if h % t == 0) * unit[n - h]
            for h in range(1, n + 1)
        )
        if value % n:
            raise ValueError("independent Delta recurrence")
        unit.append(value // n)
    delta = [0] + unit
    a, b = {0: (0, 0), 4: (1, 0), 6: (0, 1), 8: (2, 0), 10: (1, 1), 14: (2, 1)}[r]
    rows = [
        multiply(power(delta, j), multiply(power(e4, a), power(e6, 2 * (d - j) + b)))
        for j in range(1, d + 1)
    ]
    for j in range(d - 1, -1, -1):
        for i in range(j):
            scale = rows[i][j + 1]
            rows[i] = [x - scale * y for x, y in zip(rows[i], rows[j])]
    return tuple(tuple(row) for row in rows)


def independent_words(d, r, cutoff):
    """Recursively visit ungrouped ordered words, instead of grouped-state transitions."""
    order = max(d + 2, cutoff.numerator // cutoff.denominator)
    rows = independent_basis(d, r, order)
    c, N = rows[0], d + 1
    result = {F(n): c[n] ** 2 for n in range(1, order + 1) if n <= cutoff and c[n]}
    count = 0

    def visit(j, frequency, value, depth):
        nonlocal count
        for n in range(N, order + 1):
            factor = c[n] * rows[j - 1][n]
            key = frequency * n
            if key <= cutoff and factor:
                result[key] = result.get(key, 0) + (-1) ** (depth + 1) * value * factor
                count += 1
        # Every extension strictly increases frequency; N bounds final closure.
        for new in range(2, d + 1):
            for n in range(N, order + 1):
                factor = rows[j - 1][n] * rows[new - 1][n]
                key = frequency * F(n, new)
                if factor and key * N <= cutoff:
                    visit(new, key, value * factor, depth + 1)

    for j in range(2, d + 1):
        for n in range(N, order + 1):
            value = c[n] * rows[j - 1][n]
            if value and F(n, j) * N <= cutoff:
                visit(j, F(n, j), value, 0)
    result = {key: value for key, value in result.items() if value}
    zeta = {}
    for key, value in result.items():
        for a in range(1, math.isqrt(cutoff.numerator // cutoff.denominator) + 1):
            if key * a * a <= cutoff:
                f = key * a * a
                zeta[f] = zeta.get(f, 0) + value * a ** (24 * d + 2 * r - 2)
    return result, {key: value for key, value in zeta.items() if value}, count


class CuspFlagTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = m.build_report()

    def test_complete_fixture(self):
        m.validate_report(m.read_json(m.FIXTURE))

    def test_complete_family_coverage(self):
        self.assertEqual(len(self.report["family"]), 138)
        self.assertEqual(
            {(v["dimension"], v["residual"]) for v in self.report["family"]},
            {(d, r) for d in range(2, 25) for r in (0, 4, 6, 8, 10, 14)},
        )

    def test_independent_complete_bases(self):
        for d, r in ((2, 0), (3, 0), (3, 14), (10, 4), (20, 8), (24, 8)):
            with self.subTest(d=d, r=r):
                self.assertEqual(m.miller_basis(d, r), independent_basis(d, r, d + 2))

    def test_basis_prefix_consistency(self):
        large = m.miller_basis(4, 6, 12)
        self.assertEqual(m.miller_basis(4, 6), tuple(row[:7] for row in large))

    def test_weight36_calibration(self):
        rows = m.miller_basis(3, 0)
        self.assertEqual((rows[0][4], rows[2][4]), (57093088, -72))
        self.assertEqual(-((rows[0][4] * rows[2][4]) ** 2), -16897873695195856896)

    def test_signs_all_finite_rows(self):
        for row in self.report["family"]:
            self.assertGreater(
                row["c_N"] * (1 if row["residual"] in (0, 4, 8) else -1), 0
            )
            self.assertEqual(row["c_N"], row["dual_c_N"])

    def test_retained_top_exceptions(self):
        rows = [v for v in self.report["family"] if v["top_b_N"] == 0]
        self.assertEqual(
            [(v["weight"], v["active_b_N"]) for v in rows],
            [(124, 169884), (248, 142884)],
        )
        self.assertEqual(
            [v["first_fractional_frequency"] for v in rows], ["121/9", "441/19"]
        )

    def test_exception_c_values(self):
        rows = {v["weight"]: v for v in self.report["family"]}
        self.assertEqual(rows[124]["c_N"], 274199916600352164708)
        self.assertEqual(rows[248]["c_N"], 56759176303803625378304458445779330578)

    def test_partition_ratio_majorant(self):
        self.assertLess(F(14400, 12167), F(6, 5))
        for d in (2, 3, 10, 20, 24):
            p = m.colored_partitions(d, m.Budget())
            self.assertLess(p[d], 44 * p[d - 1])
            self.assertLess(p[d], 3828 * p[d - 2])

    def test_first_N_direction_not_singleton(self):
        for row in self.report["family"]:
            self.assertIn(1, row["first_N_direction_support"])
            self.assertIn(row["active_pivot"], row["first_N_direction_support"])
            self.assertGreaterEqual(len(row["first_N_direction_support"]), 2)

    def test_all_ungrouped_word_prefixes(self):
        for row in self.report["frequency_controls"]:
            with self.subTest(weight=row["weight"]):
                bare, zeta, count = independent_words(
                    row["dimension"], row["residual"], F(row["cutoff"])
                )
                self.assertEqual({str(k): v for k, v in bare.items()}, row["bare_F"])
                self.assertEqual(
                    {str(k): v for k, v in zeta.items()}, row["zeta_times_F"]
                )
                self.assertGreaterEqual(count, row["closing_grouped_state_pairs"])

    def test_fractional_frequency_survives_zeta(self):
        for row in self.report["frequency_controls"]:
            first = row["first_fractional_frequency"]
            self.assertEqual(row["bare_F"][first], row["zeta_times_F"][first])
            self.assertLess(row["bare_F"][first], 0)

    def test_no_prior_fractional_frequency(self):
        for row in self.report["frequency_controls"]:
            first = F(row["first_fractional_frequency"])
            self.assertTrue(
                all(F(f).denominator == 1 for f in row["bare_F"] if F(f) < first)
            )

    def test_zeta_integer_frequency_four(self):
        row = self.report["frequency_controls"][0]
        self.assertEqual(row["zeta_times_F"]["4"] - row["bare_F"]["4"], 2**46)

    def test_frozen_weight24_parent_reduction(self):
        ref = (
            m.PARENT + ":" + m.SOURCE_DIR + "rankin_selberg_quotient_global_parent.json"
        )
        old = json.loads(m.subprocess.check_output(["git", "show", ref], cwd=ROOT))
        old_row = next(v for v in old["frequency_controls"] if F(v["cutoff"]) == 12)
        new_row = self.report["frequency_controls"][0]
        self.assertEqual(
            new_row["bare_F"], {k: int(v) for k, v in old_row["bare_F"].items()}
        )
        self.assertEqual(
            new_row["zeta_times_F"],
            {k: int(v) for k, v in old_row["L_Q_zeta_times_F"].items()},
        )

    def test_frequency_prefix_restriction(self):
        for d, r, cutoff in ((3, 0, F(16, 3)), (10, 4, F(121, 9)), (20, 8, F(441, 19))):
            small = m.frequency_control(d, r, cutoff)
            large = next(
                v
                for v in self.report["frequency_controls"]
                if (v["dimension"], v["residual"]) == (d, r)
            )
            self.assertEqual(
                small["bare_F"],
                {F(k): v for k, v in large["bare_F"].items() if F(k) <= cutoff},
            )

    def test_depth_coverage(self):
        for row in self.report["frequency_controls"]:
            self.assertGreater(F(row["next_depth_lower_bound"]), F(row["cutoff"]))
            self.assertGreaterEqual(row["source_q_order"], F(row["cutoff"]).__floor__())

    def test_dimension_caps_types(self):
        for d in (True, 2.0, "3", 1, 25, -1):
            with self.subTest(d=d), self.assertRaises(ValueError):
                m.miller_basis(d, 0)

    def test_residual_caps_types(self):
        for r in (False, 0.0, "0", 2, 12, -2):
            with self.subTest(r=r), self.assertRaises(ValueError):
                m.miller_basis(3, r)

    def test_order_caps_types(self):
        for order in (True, 5.0, "6", 4, 29):
            with self.subTest(order=order), self.assertRaises(ValueError):
                m.miller_basis(3, 0, order)

    def test_method_types(self):
        for method in (True, 4, "other"):
            with self.assertRaises(ValueError):
                m.miller_basis(3, 0, method=method)

    def test_caps_before_primitive_expansion(self):
        with mock.patch.object(m, "primitives", side_effect=RuntimeError("expanded")):
            for args in ((25, 0, 28), (3, 2, 5), (3, 0, 29)):
                with self.assertRaises(ValueError):
                    m.miller_basis(*args)

    def test_cutoff_caps_before_basis(self):
        with mock.patch.object(m, "miller_basis", side_effect=RuntimeError("expanded")):
            for cutoff in (True, 6.0, "6", 1, 29, F(1, 2**32)):
                with self.assertRaises(ValueError):
                    m.frequency_control(3, 0, cutoff)
            with self.assertRaises(ValueError):
                m.frequency_control(10, 4, F(121, 10))

    def test_exact_rational_bit_caps(self):
        for value in (True, 1.0, "1", 2**32, F(1, 2**32)):
            with self.assertRaises(ValueError):
                m.exact(value)
        with self.assertRaises(ValueError):
            m.exact(2**4096, internal=True)
        with self.assertRaises(ValueError):
            m.exact(1, internal=1)

    def test_polynomial_types_shape_bits(self):
        for value in ((0,), [True] * 5, [F(1)] * 5, [2**4096] * 5, "abcde"):
            with self.assertRaises(ValueError):
                m.polynomial(value, 4)

    def test_budget_before_q_multiplication(self):
        work = m.Budget(1)
        with self.assertRaises(ValueError):
            m.qmul((1,) * 5, (1,) * 5, 4, work)
        self.assertEqual(work.used, 0)

    def test_budget_limits_types(self):
        for value in (True, 1.0, 0, m.MAX_WORK + 1):
            with self.assertRaises(ValueError):
                m.Budget(value)

    def test_support_cap_before_allocation(self):
        out = {F(n): 1 for n in range(1, m.MAX_TERMS + 1)}
        with self.assertRaises(ValueError):
            m.insert(out, F(m.MAX_TERMS + 1), 1, m.MAX_TERMS)
        self.assertEqual(len(out), m.MAX_TERMS)

    def test_manifest_missing_extra_type_primitive(self):
        for field, value in (
            ("frozen_sources", []),
            ("extra", True),
            ("authoring_base", 8),
            ("primitive_definitions", {}),
        ):
            manifest = copy.deepcopy(m.expected_manifest())
            manifest[field] = value
            with self.assertRaises(ValueError):
                m.authenticate_sources(manifest)

    def test_manifest_every_source_identity_tamper(self):
        for index in range(6):
            for key in ("commit", "path", "git_blob", "sha256_lf"):
                manifest = copy.deepcopy(m.expected_manifest())
                manifest["frozen_sources"][index][key] = "tampered"
                with self.assertRaises(ValueError):
                    m.authenticate_sources(manifest)

    def test_git_source_drift(self):
        with (
            mock.patch.object(m.subprocess, "check_output", return_value=b"wrong"),
            self.assertRaises(ValueError),
        ):
            m.authenticate_sources(m.expected_manifest())

    def test_fixture_schema_type_coefficient_tamper(self):
        for kind in ("missing", "extra", "bool", "float", "coefficient", "digest"):
            bad = copy.deepcopy(self.report)
            if kind == "missing":
                bad["family"].pop()
            elif kind == "extra":
                bad["extra"] = 1
            elif kind == "bool":
                bad["scope"]["new_automorphic_representation"] = 0
            elif kind == "float":
                bad["caps"]["max_dimension"] = 24.0
            elif kind == "coefficient":
                bad["family"][0]["c_N"] += 1
            else:
                bad["artifact_sha256_lf"][next(iter(bad["artifact_sha256_lf"]))] = (
                    "0" * 64
                )
            with (
                mock.patch.object(m, "build_report", return_value=self.report),
                self.assertRaises(ValueError),
            ):
                m.validate_report(bad)

    def test_actual_artifact_bytes_affect_hashes(self):
        expected = m.artifact_digests()
        original = Path.read_bytes
        for path in (m.NOTE, m.Path(m.__file__), m.TEST, m.MANIFEST):

            def changed(p, target=path):
                return original(p) + (b"tampered" if p == target else b"")

            with mock.patch.object(Path, "read_bytes", changed):
                actual = m.artifact_digests()
            self.assertNotEqual(
                actual[path.relative_to(ROOT).as_posix()],
                expected[path.relative_to(ROOT).as_posix()],
            )

    def test_json_duplicates_and_nonfinite(self):
        for raw in (
            '{"a":1,"a":2}',
            '{"a":{"b":1,"b":2}}',
            '{"a":NaN}',
            '{"a":Infinity}',
            '{"a":-Infinity}',
            '{"a":1e9999}',
        ):
            with (
                mock.patch.object(Path, "read_text", return_value=raw),
                self.assertRaises(ValueError),
            ):
                m.read_json(Path("unused"))

    def test_scope_boundaries(self):
        scope = self.report["scope"]
        for key in (
            "uniform_in_weight_halfplane",
            "all_nontrivial_block_decompositions_excluded",
            "generalized_prime_systems_excluded",
            "new_automorphic_representation",
            "analytic_proof_machine_verified",
            "RH_GRH_or_exhaustive_novelty_claim",
        ):
            self.assertIs(scope[key], False)
        self.assertLessEqual(self.report["coverage"]["work_units"], m.MAX_WORK)
        self.assertEqual(json.loads(m.canonical(self.report)), self.report)


if __name__ == "__main__":
    unittest.main()
