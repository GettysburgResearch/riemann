"""Exact finite controls; no actual-cusp derivative or tail-mass oracle."""

import copy
import importlib.util
import itertools
import json
import math
import unittest
from fractions import Fraction as Q
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
PATH = (
    ROOT
    / "research/l-families/atlas/generalized/cusp_flag_positive_spectrum_boundary.py"
)
SPEC = importlib.util.spec_from_file_location("psb_tested", PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("producer import unavailable")
m = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(m)


def formal_quotient(atoms):
    """Independent determinant Taylor division, without solving normal equations."""
    n = len(atoms[0][2])

    def multiply(a, b):
        return [sum(a[j] * b[h - j] for j in range(h + 1)) for h in range(3)]

    def determinant(rows):
        size = len(rows)
        answer = [Q(0)] * 3
        for permutation in itertools.permutations(range(size)):
            inversions = sum(
                permutation[i] > permutation[j]
                for i in range(size)
                for j in range(i + 1, size)
            )
            term = [Q((-1) ** inversions), Q(0), Q(0)]
            for i, j in enumerate(permutation):
                term = multiply(term, rows[i][j])
            answer = [x + y for x, y in zip(answer, term)]
        return answer

    rows = [
        [
            [
                sum(
                    Q(weight) * row[i] * row[j] * Q((-rate) ** h, math.factorial(h))
                    for rate, weight, row in atoms
                )
                for h in range(3)
            ]
            for j in range(n)
        ]
        for i in range(n)
    ]
    numerator = determinant(rows)
    denominator = determinant([[rows[i][j] for j in range(1, n)] for i in range(1, n)])
    answer = []
    for h in range(3):
        answer.append(
            (
                numerator[h]
                - sum(denominator[j] * answer[h - j] for j in range(1, h + 1))
            )
            / denominator[0]
        )
    return answer[0], answer[1], 2 * answer[2]


class PositiveSpectrumTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = m.build_report()

    def test_complete_fixture(self):
        m.validate_report(m.parse_json(m.FIXTURE.read_text()))

    def test_six_frozen_bindings(self):
        source, auth = m.authenticate_sources()
        self.assertEqual(auth["frozen_source_count"], 6)
        self.assertEqual(len(source["family"]), 138)
        self.assertFalse(auth["parent_q_producer_rerun"])

    def test_complete_source_coverage(self):
        self.assertEqual(
            [(row["dimension"], row["residual"]) for row in self.report["family"]],
            [(d, r) for d in range(2, 25) for r in (0, 4, 6, 8, 10, 14)],
        )

    def test_parent_coefficients_unchanged(self):
        source, _ = m.authenticate_sources()
        for old, new in zip(source["family"], self.report["family"]):
            self.assertEqual(
                new["negative_frequency"], old["first_fractional_frequency"]
            )
            self.assertEqual(
                new["negative_coefficient_w_F_and_L"],
                old["first_fractional_coefficient_w"],
            )

    def test_retained_exception_pivots(self):
        rows = [r for r in self.report["family"] if r["top_b_N"] == 0]
        self.assertEqual(
            [(r["weight"], r["active_b_N"]) for r in rows],
            [(124, 169884), (248, 142884)],
        )
        self.assertEqual([r["negative_frequency"] for r in rows], ["121/9", "441/19"])

    def test_gap_controls_all_rows(self):
        for row in self.report["family"]:
            p, upper = row["adjacent_integer_bracket"]
            self.assertLess(p, Q(row["negative_frequency"]))
            self.assertLess(Q(row["negative_frequency"]), upper)
            self.assertTrue(
                all(Q(x) > upper for x in row["nonfirst_correction_lower_bounds"])
            )

    def test_positive_first_atoms(self):
        for row in self.report["family"]:
            N, c, k = row["N"], row["c_N"], row["weight"]
            self.assertEqual(row["F_first_positive_coefficient"], c * c)
            self.assertEqual(row["L_first_positive_frequency"], min(N, 4))
            expected = c * c if N < 4 else 2 ** (2 * k - 2)
            if N == 4:
                expected += c * c
            self.assertEqual(row["L_first_positive_coefficient"], expected)
            self.assertGreater(expected, 0)

    def test_L_frequency_four_collision(self):
        row = next(r for r in self.report["family"] if r["weight"] == 36)
        self.assertEqual(row["L_first_positive_coefficient"], 57093088**2 + 2**70)

    def test_exact_negative_curvature(self):
        row = self.report["finite_gram_controls"][0]
        self.assertEqual(
            [row[k] for k in ("F", "Fprime", "Fsecond", "curvature_loss")],
            ["11/10", "-19/100", "-46/125", "729/500"],
        )

    def test_independent_determinant_Taylor_controls(self):
        for row in self.report["finite_gram_controls"]:
            atoms = [
                (rate, Q(weight), tuple(Q(v) for v in vector))
                for rate, weight, vector in row["atoms_rate_tilted_weight_vector"]
            ]
            answer = formal_quotient(atoms)
            self.assertEqual(
                answer, tuple(Q(row[k]) for k in ("F", "Fprime", "Fsecond"))
            )

    def test_held_out_Gram_panels(self):
        for rate in (1, 2, 7, 16, 32):
            for a in (1, 2, 5):
                atoms = [(0, 1, (1, 0)), (1, Q(2, 3), (0, 1)), (rate, Q(3, 2), (a, 3))]
                out = m.envelope_control(atoms)
                self.assertEqual(
                    formal_quotient(atoms),
                    tuple(out[k] for k in ("F", "Fprime", "Fsecond")),
                )

    def test_stationarity_and_curvature_factor_two(self):
        for row in self.report["finite_gram_controls"]:
            D, D1, _ = [
                [[Q(v) for v in line] for line in mat]
                for mat in row["D_Dprime_Dsecond"]
            ]
            a = [Q(v) for v in row["minimizer_coordinates"]]
            for i in range(1, len(a)):
                self.assertEqual(sum(D[i][j] * a[j] for j in range(len(a))), 0)
            self.assertEqual(
                Q(row["Fprime"]),
                sum(
                    a[i] * D1[i][j] * a[j] for i in range(len(a)) for j in range(len(a))
                ),
            )
            self.assertEqual(
                Q(row["Fsecond"]),
                Q(row["frozen_vector_second_derivative"]) - Q(row["curvature_loss"]),
            )
            self.assertLessEqual(Q(row["Fprime"]), 0)

    def test_positive_curvature_without_optimization_loss(self):
        out = m.envelope_control([(1, 1, (1, 0)), (2, 1, (0, 1))])
        self.assertEqual(
            (out["F"], out["Fprime"], out["Fsecond"], out["curvature_loss"]),
            (1, -1, 1, 0),
        )

    def test_signed_toy_direct_derivatives(self):
        for order in range(1, 33):
            row = m.moving_toy(order)
            t = Q(3, 5) ** order
            direct = 2 * t - 2**order * t**2 + 3**order * t**3
            self.assertEqual(row["signed_derivative"], direct)
            self.assertEqual(
                row["normalized_derivative"],
                2 * Q(5, 6) ** order - 1 + Q(9, 10) ** order,
            )

    def test_eighth_order_strict_negative(self):
        row = m.moving_toy(8)
        self.assertLess(row["signed_derivative"], 0)
        self.assertGreater(m.moving_toy(4)["signed_derivative"], 0)

    def test_toy_ratio_not_claimed_universally_negative(self):
        self.assertGreater(m.moving_toy(8, Q(1, 2))["signed_derivative"], 0)

    def test_toy_positive_polynomial_identities(self):
        for t in (Q(1, 10), Q(1, 2), Q(1), Q(2), Q(7, 3)):
            self.assertEqual(2 - t + t * t, (t - Q(1, 2)) ** 2 + Q(7, 4))
            self.assertEqual(2 - 2 * t + 3 * t * t, 3 * (t - Q(1, 3)) ** 2 + Q(5, 3))

    def test_dimensions_types_caps(self):
        for d in (True, 2.0, Q(2), "2", 1, 25):
            with self.assertRaises(ValueError):
                m.family_control(d, 0, 195660, -48)

    def test_residual_and_pivot_types(self):
        for r in (False, 0.0, "0", 2, 12):
            with self.assertRaises(ValueError):
                m.family_control(2, r, 195660, -48)
        for c, b in (
            (0, -48),
            (-195660, -48),
            (True, -48),
            (195660, True),
            (195660, -47),
        ):
            with self.assertRaises(ValueError):
                m.family_control(2, 0, c, b)

    def test_primitive_rational_types_bits(self):
        for x in (True, 1.0, "1", 2**32, Q(1, 2**32)):
            with self.assertRaises(ValueError):
                m.rat(x)
        with self.assertRaises(ValueError):
            m.rat(1, internal=1)
        with self.assertRaises(ValueError):
            m.rat(2**4096, internal=True)

    def test_coefficient_cap(self):
        for x in (True, 1.0, Q(1), 2**4096):
            with self.assertRaises(ValueError):
                m.coefficient(x)

    def test_matrix_shape_types(self):
        for x in ("bad", [], [[1, 0], [0]], [[True]], [[1.0]], [[0] * 5] * 5):
            with self.assertRaises(ValueError):
                m.matrix(x)

    def test_nonpositive_and_nonsymmetric_solve(self):
        for a in ([[1, 0], [0, 0]], [[1, 2], [2, 1]], [[1, 2], [0, 1]]):
            with self.assertRaises(ValueError):
                m.positive_solve(a, [1, 0], m.Budget())

    def test_atom_shapes_types_caps(self):
        cases = [
            [],
            [(0, 1, (1, 0))] * 9,
            [(0, 1, (1, 0), 7)],
            [(0, -1, (1, 0))],
            [(True, 1, (1, 0))],
            [(33, 1, (1, 0))],
            [(0, 1.0, (1, 0))],
            [(0, 1, (1,))],
            [(0, 1, (True, 0))],
            [(0, 1, (1, 0)), (1, 1, (0, 1, 2))],
        ]
        for atoms in cases:
            with self.assertRaises(ValueError):
                m.envelope_control(atoms)

    def test_toy_caps_types(self):
        for order in (True, 1.0, "1", 0, 33):
            with self.assertRaises(ValueError):
                m.moving_toy(order)
        for ratio in (True, 0.6, "3/5", 0, 1, 2, Q(1, 2**32)):
            with self.assertRaises(ValueError):
                m.moving_toy(8, ratio)

    def test_work_caps_and_precharge(self):
        for limit in (True, 1.0, 0, 200001):
            with self.assertRaises(ValueError):
                m.Budget(limit)
        for fn in (
            lambda w: m.moving_toy(8, work=w),
            lambda w: m.family_control(2, 0, 195660, -48, w),
            lambda w: m.positive_solve([[1, 0], [0, 1]], [1, 0], w),
            lambda w: m.envelope_control([(0, 1, (1, 0)), (1, 1, (0, 1))], w),
        ):
            work = m.Budget(1)
            with self.assertRaises(ValueError):
                fn(work)
            self.assertEqual(work.used, 0)

    def test_manifest_every_source_binding_tamper(self):
        for i in range(6):
            for field in ("commit", "path", "git_blob", "sha256_lf"):
                bad = copy.deepcopy(m.expected_manifest())
                bad["frozen_sources"][i][field] = "tampered"
                with self.assertRaises(ValueError):
                    m.authenticate_sources(bad)

    def test_manifest_primitive_and_schema_drift(self):
        for field, value in (
            ("schema", 1),
            ("primitive_contract", {}),
            ("extra", 1),
            ("frozen_sources", []),
        ):
            bad = copy.deepcopy(m.expected_manifest())
            bad[field] = value
            with self.assertRaises(ValueError):
                m.authenticate_sources(bad)

    def test_manifest_does_not_alias_source_constants(self):
        bad = m.expected_manifest()
        bad["frozen_sources"][0]["commit"] = "tampered"
        self.assertEqual(m.expected_manifest()["frozen_sources"][0]["commit"], m.BASE)

    def test_git_source_drift(self):
        with (
            mock.patch.object(m.subprocess, "check_output", return_value=b"wrong"),
            self.assertRaises(ValueError),
        ):
            m.authenticate_sources(m.expected_manifest())

    def test_fixture_type_schema_coefficient_drift(self):
        with mock.patch.object(m, "build_report", return_value=self.report):
            for kind in ("missing", "extra", "bool", "float", "coefficient", "digest"):
                bad = copy.deepcopy(self.report)
                if kind == "missing":
                    bad["family"].pop()
                elif kind == "extra":
                    bad["extra"] = True
                elif kind == "bool":
                    bad["caps"]["atoms"] = True
                elif kind == "float":
                    bad["family"][0]["dimension"] = 2.0
                elif kind == "coefficient":
                    bad["family"][0]["negative_coefficient_w_F_and_L"] += 1
                else:
                    bad["payload_sha256_canonical_json"] = "0" * 64
                with self.assertRaises(ValueError):
                    m.validate_report(bad)

    def test_json_duplicates_nonfinite(self):
        for raw in (
            '{"a":1,"a":2}',
            '{"a":{"b":0,"b":1}}',
            '{"a":NaN}',
            '{"a":Infinity}',
            '{"a":-Infinity}',
            '{"a":1e99999}',
        ):
            with self.assertRaises(ValueError):
                m.parse_json(raw)

    def test_artifact_bytes_affect_hashes(self):
        expected = m.artifact_digests()
        original = Path.read_bytes
        for target in (m.NOTE, Path(m.__file__), m.MANIFEST, m.TEST):

            def changed(p, target=target):
                return original(p) + (b"tampered" if p == target else b"")

            with mock.patch.object(Path, "read_bytes", changed):
                actual = m.artifact_digests()
            key = target.relative_to(ROOT).as_posix()
            self.assertNotEqual(actual[key], expected[key])

    def test_payload_digest(self):
        copy_report = copy.deepcopy(self.report)
        digest = copy_report.pop("payload_sha256_canonical_json")
        self.assertEqual(
            digest, m.hashlib.sha256(m.canonical(copy_report).encode()).hexdigest()
        )

    def test_scope_firewalls(self):
        scope = self.report["scope"]
        for key in (
            "one_tail_for_all_orders",
            "completed_Q_assigned_same_monotonicity",
            "actual_cusp_second_derivative_negativity",
            "certified_cusp_absolute_tail_mass",
            "effective_cusp_onset_computed",
            "uniform_in_weight_halfplane",
            "every_spectral_representation_excluded",
            "Weil_positivity_RH_GRH_or_novelty_claim",
            "analytic_proof_machine_verified",
        ):
            self.assertIs(scope[key], False)
        self.assertLessEqual(self.report["coverage"]["work_units"], m.MAX_WORK)
        self.assertEqual(json.loads(m.canonical(self.report)), self.report)


if __name__ == "__main__":
    unittest.main()
