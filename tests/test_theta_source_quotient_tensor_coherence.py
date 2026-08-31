"""Independent finite routes and hostile acceptance checks for SC."""

from __future__ import annotations

import copy
import importlib.util
import itertools
import json
import unittest
from fractions import Fraction as Q
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
PATH = (
    ROOT
    / "research/l-families/atlas/generalized/theta_source_quotient_tensor_coherence.py"
)
SPEC = importlib.util.spec_from_file_location("sc", PATH)
m = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(m)


def unmatrix(rows):
    return m.matrix([[(Q(x), Q(y)) for x, y in row] for row in rows])


def permutation_det(a):
    a = m.matrix(a)
    n = len(a)
    result = m.z(0)
    for p in itertools.permutations(range(n)):
        term = m.z((-1) ** sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n)))
        for i in range(n):
            term = m.mul(term, a[i][p[i]])
        result = m.add(result, term)
    return result


def adjugate_inverse(a):
    a = m.matrix(a)
    n = len(a)
    d = permutation_det(a)
    if n == 1:
        return m.matrix([[m.div(1, d)]])
    co = []
    for i in range(n):
        row = []
        for j in range(n):
            minor = m.matrix(
                [[a[r][c] for c in range(n) if c != j] for r in range(n) if r != i]
            )
            row.append(m.div(m.mul((-1) ** (i + j), permutation_det(minor)), d))
        co.append(row)
    return m.matrix([[co[j][i] for j in range(n)] for i in range(n)])


def independent_q(h, p):
    return adjugate_inverse(m.product(m.product(p, adjugate_inverse(h)), m.star(p)))


def reseal(value):
    value.pop("payload_sha256", None)
    value["payload_sha256"] = m.digest(m.canonical(value))
    return value


class Controls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = m.decode(m.file_bytes(ROOT / (m.DIR + m.STEM + ".json")))
        cls.fresh = m.fixture()

    def setUp(self):
        m.WORK = 0

    def test_01_fresh_fixture(self):
        self.assertEqual(self.report, self.fresh)
        self.assertTrue(m.check(self.report))

    def test_02_exact_coverage(self):
        c = self.report["coverage"]
        self.assertEqual(
            [c[k] for k in ("base", "tensor", "direct_sum", "chains", "averaging")],
            [6, 3, 3, 3, 2],
        )
        self.assertEqual(c["parameters"], ["3/2", "2", "3"])
        self.assertEqual(c["stages_per_chain"], 3)

    def test_03_source_primitives(self):
        a, b = m.specifications()
        self.assertEqual(permutation_det(a["G"]), m.z(4))
        self.assertEqual(permutation_det(a["R"]), m.z(1))
        self.assertEqual(permutation_det(b["G"]), m.z(2))
        self.assertEqual(permutation_det(b["R"]), m.z(2))
        for sp in (a, b):
            self.assertNotEqual(permutation_det(sp["C"]), m.z(0))
            self.assertNotEqual(permutation_det(sp["B"]), m.z(0))

    def test_04_base_adjugate_quotients(self):
        for row in self.report["base_cells"]:
            h, g, p = map(unmatrix, (row["H"], row["G"], row["pi"]))
            self.assertEqual(independent_q(h, p), unmatrix(row["source"]["quotient"]))
            self.assertEqual(independent_q(g, p), unmatrix(row["vacuum"]["quotient"]))

    def test_05_minimal_energy_pythagoras(self):
        for sp in m.specifications():
            for t in (Q(3, 2), Q(2), Q(3)):
                h = m.source_value(sp, t)
                p = sp["pi"]
                j = m.lift(h, p)
                projection = m.minus(m.eye(2), m.product(j, p))
                trial = m.matrix([[(1, 1)], [Q(2, 3)]])
                ker = m.product(projection, trial)
                v = m.plus(j, ker)
                self.assertEqual(
                    m.congruence(h, v), m.plus(m.quotient(h, p), m.congruence(h, ker))
                )

    def test_06_all_principal_minors_permutation(self):
        for row in self.report["tensor_cells"]:
            a = m.minus(unmatrix(row["H"]), unmatrix(row["G"]))
            for r in row["source_excess_minors"]:
                self.assertEqual(
                    permutation_det(m.principal(a, r["indices"])),
                    m.z(Q(r["determinant"])),
                )

    def test_07_nonunitary_vacuum(self):
        for row in self.report["base_cells"]:
            h, g, p, c, b = map(
                unmatrix, (row["H"], row["G"], row["pi"], row["C"], row["B"])
            )
            pp = m.product(m.product(adjugate_inverse(b), p), c)
            qh = independent_q(m.congruence(h, c), pp)
            qg = independent_q(m.congruence(g, c), pp)
            self.assertEqual(
                m.scale(m.minus(qh, qg), Q(1, 2)), unmatrix(row["transformed_excess"])
            )
            self.assertNotEqual(m.congruence(g, c), g)

    def test_08_zero_excess_reciprocal_strict(self):
        zero = [r for r in self.report["base_cells"] if r["t"] == "3"]
        self.assertEqual(len(zero), 2)
        for r in zero:
            self.assertEqual(unmatrix(r["excess"]), m.matrix([[0]]))
            self.assertGreater(unmatrix(r["reciprocal_excess"])[0][0][0], 0)

    def test_09_complete_source_reciprocity(self):
        for sp in m.specifications():
            for t in (Q(1, 3), Q(1, 2), Q(2, 3), Q(1), Q(3, 2), Q(2), Q(3)):
                self.assertEqual(
                    m.source_value(sp, t),
                    m.scale(m.source_value(sp, 1 / t), t ** (-sp["alpha"])),
                )

    def test_10_tensor_adjugate(self):
        for row in self.report["tensor_cells"]:
            h, g, p = map(unmatrix, (row["H"], row["G"], row["pi"]))
            self.assertEqual(independent_q(h, p), unmatrix(row["source"]["quotient"]))
            self.assertEqual(independent_q(g, p), unmatrix(row["vacuum"]["quotient"]))

    def test_11_tensor_lift_and_excess(self):
        a, b = m.specifications()
        for t in (Q(3, 2), Q(2), Q(3)):
            h1, h2 = m.source_value(a, t), m.source_value(b, t)
            p = m.tensor(a["pi"], b["pi"])
            self.assertEqual(
                m.lift(m.tensor(h1, h2), p),
                m.tensor(m.lift(h1, a["pi"]), m.lift(h2, b["pi"])),
            )
            q1, q2 = m.quotient(h1, a["pi"]), m.quotient(h2, b["pi"])
            g1, g2 = m.quotient(a["G"], a["pi"]), m.quotient(b["G"], b["pi"])
            c1, c2 = (
                m.scale(m.minus(q1, g1), Q(1, 2)),
                m.scale(m.minus(q2, g2), Q(1, 2)),
            )
            self.assertEqual(
                m.scale(m.minus(m.tensor(q1, q2), m.tensor(g1, g2)), Q(1, 2)),
                m.plus(
                    m.plus(m.tensor(c1, g2), m.tensor(g1, c2)),
                    m.scale(m.tensor(c1, c2), 2),
                ),
            )

    def test_12_sum_identity(self):
        a, b = m.specifications()
        for t in (Q(3, 2), Q(2), Q(3)):
            h1, h2 = m.source_value(a, t), m.source_value(b, t)
            self.assertEqual(
                independent_q(m.direct_sum(h1, h2), m.direct_sum(a["pi"], b["pi"])),
                m.direct_sum(independent_q(h1, a["pi"]), independent_q(h2, b["pi"])),
            )

    def test_13_nested_all_stages_adjugate(self):
        a, b = m.specifications()
        for record in self.report["nested_chains"]:
            t = Q(record["t"])
            for chain in record["chains"]:
                h = (
                    m.tensor(a["G"], b["G"])
                    if chain["kind"] == "vacuum"
                    else m.tensor(m.source_value(a, t), m.source_value(b, t))
                )
                self.assertEqual(len(chain["stages"]), 3)
                for stage in chain["stages"]:
                    p = unmatrix(stage["composite_map"])
                    self.assertEqual(independent_q(h, p), unmatrix(stage["quotient"]))
                    j = unmatrix(stage["lift"])
                    self.assertEqual(m.product(p, j), m.eye(stage["dimension"]))
                    self.assertEqual(m.congruence(h, j), unmatrix(stage["quotient"]))

    def test_14_averaging_block_energy(self):
        for common in (False, True):
            ds, ls, hs, _ = m.averaging_data(common)
            for d, l, h in zip(ds, ls, hs):
                j = m.matrix([*m.eye(2), *m.scale(l, -1)])
                self.assertEqual(m.congruence(h, j), m.eye(2))
                self.assertEqual(permutation_det(h), permutation_det(d))

    def test_15_independent_averaging_defect(self):
        for record in self.report["averaging"]:
            hs = [unmatrix(h) for h in record["H"]]
            weights = [Q(w) for w in record["weights"]]
            p = m.matrix([[1, 0, 0, 0], [0, 1, 0, 0]])
            mean = m.weighted_sum(hs, weights)
            diff = m.minus(
                independent_q(mean, p),
                m.weighted_sum([independent_q(h, p) for h in hs], weights),
            )
            self.assertEqual(diff, unmatrix(record["defect"]))
            self.assertEqual(permutation_det(diff), m.z(Q(record["determinant"])))
        self.assertEqual(self.report["averaging"][0]["determinant"], "77/2316")
        self.assertEqual(self.report["averaging"][1]["determinant"], "0")

    def test_16_averaging_strict_kernel_prediction(self):
        ds, ls, _, _ = m.averaging_data(False)
        stacked = m.matrix([ls[1][0], ls[2][1]])
        self.assertNotEqual(permutation_det(stacked), m.z(0))
        self.assertNotEqual(m.product(ds[0], ds[1]), m.product(ds[1], ds[0]))

    def test_17_observation_independent_polynomial(self):
        for row in self.report["observation"]["evaluations"]:
            s = row["s"]
            l1, l2, l3 = Q(1, 2 * s * (s - 1)), Q(1, s * (s - 2)), Q(3, 2 * s * (s - 3))
            self.assertEqual(l3 - l1 * l2, Q(row["difference"]))
            self.assertNotEqual(l3, l1 * l2)
        # Four integer values identify the preregistered polynomial of degree<=3.
        p = self.report["observation"]["numerator_ascending"]
        for s in (0, 1, 2, 3):
            self.assertEqual(
                sum(v * s**j for j, v in enumerate(p)),
                3 * s * (s - 1) * (s - 2) - (s - 3),
            )

    def test_18_unequal_weights_and_regularity(self):
        self.assertNotEqual(Q(2) ** 1, Q(2) ** 2)
        self.assertLess(Q(self.report["regularity_failure"]["local_exponent"]), 1)
        self.assertGreater(Q(self.report["regularity_failure"]["tensor_exponent"]), 1)
        self.assertFalse(self.report["regularity_failure"]["local_L1_tensor_closed"])

    def test_19_contract(self):
        c = self.report["contract"]
        self.assertEqual(c["arithmetic_class"], "MIXED")
        self.assertEqual(
            c["components"], ["EXACT_RATIONAL", "CERTIFIED_INTEGER_COVERAGE"]
        )
        self.assertEqual(c["rounding"], "none")
        self.assertFalse(c["analytic_claims_machine_certified"])
        self.assertEqual(c["tensor_closed_source_class"], "locally bounded measurable")

    def test_20_all_source_and_artifact_seals(self):
        m.authenticate()
        self.assertEqual(len(m.BINDINGS), 7)
        self.assertEqual(len(self.report["artifact_sha256_lf"]), 4)
        for p, d in self.report["artifact_sha256_lf"].items():
            self.assertEqual(m.digest(m.lf(m.file_bytes(ROOT / p))), d)
        v = copy.deepcopy(self.report)
        d = v.pop("payload_sha256")
        self.assertEqual(d, m.digest(m.canonical(v)))

    def test_21_source_bytes_tamper(self):
        original = m.subprocess.check_output
        for target in m.BINDINGS:

            def corrupted(args, selected=target, **kwargs):
                raw = original(args, **kwargs)
                return (
                    raw + b" "
                    if args[-1] == selected["commit"] + ":" + selected["path"]
                    else raw
                )

            with (
                self.subTest(path=target["path"], commit=target["commit"]),
                mock.patch.object(m.subprocess, "check_output", side_effect=corrupted),
                self.assertRaises(ValueError),
            ):
                m.authenticate()

    def test_22_manifest_resealed_tamper(self):
        original = m.file_bytes
        bad = copy.deepcopy(m.manifest())
        bad["contract"]["local_L1_tensor_closure"] = True
        path = ROOT / (m.DIR + m.STEM + ".sources.json")
        with (
            mock.patch.object(
                m,
                "file_bytes",
                side_effect=lambda p: m.canonical(bad) if p == path else original(p),
            ),
            self.assertRaises(ValueError),
        ):
            m.authenticate()

    def test_23_artifact_bytes_tamper(self):
        original = m.file_bytes
        for target in m.ARTIFACTS:

            def bad(p, selected=target):
                raw = original(p)
                return raw + b" " if p == ROOT / selected else raw

            with (
                mock.patch.object(m, "file_bytes", side_effect=bad),
                self.assertRaises(ValueError),
            ):
                m.check(self.report)

    def test_24_resealed_mathematical_attacks(self):
        for section in (
            "base_cells",
            "tensor_cells",
            "same_weight_sums",
            "nested_chains",
            "averaging",
        ):
            bad = copy.deepcopy(self.report)
            bad[section] = bad[section][:-1]
            with self.subTest(section=section), self.assertRaises(ValueError):
                m.check(reseal(bad))

    def test_25_resealed_semantic_attacks(self):
        mutations = [
            ("tensor_closed_source_class", "locally integrable measurable"),
            ("analytic_claims_machine_certified", True),
            ("rounding", "nearest"),
            ("local_L1_tensor_closure", True),
        ]
        for key, value in mutations:
            bad = copy.deepcopy(self.report)
            bad["contract"][key] = value
            with self.subTest(key=key), self.assertRaises(ValueError):
                m.check(reseal(bad))

    def test_26_scope_and_schema_exact(self):
        for key, value in (("schema", "other"), ("work_units", True), ("sources", [])):
            bad = copy.deepcopy(self.report)
            bad[key] = value
            with (
                mock.patch.object(m, "fixture", return_value=self.fresh),
                self.assertRaises(ValueError),
            ):
                m.check(reseal(bad))

    def test_27_no_float_bool_rational(self):
        for bad in (True, False, 1.0, "1", None, complex(1, 0)):
            with self.assertRaises(ValueError):
                m.rational(bad)
        for bad in (True, 1.0, "2"):
            with self.assertRaises(ValueError):
                m.integer(bad, 1, 4)

    def test_28_matrix_shape_caps(self):
        for bad in ([], [[1], []], [[True]], [[0] * 5], [[0]] * 5, "x"):
            with self.assertRaises(ValueError):
                m.matrix(bad)
        with self.assertRaises(ValueError):
            m.eye(True)
        with self.assertRaises(ValueError):
            m.eye(5)

    def test_29_singular_and_nonpositive_quotients(self):
        for h, p in (
            ([[1, 0], [0, 0]], [[1, 0]]),
            ([[1, 0], [0, -1]], [[1, 0]]),
            ([[1, 1], [0, 1]], [[1, 0]]),
            ([[1, 0], [0, 1]], [[0, 0]]),
            ([[1, 0], [0, 1]], [[1, 0], [2, 0]]),
        ):
            with self.assertRaises(ValueError):
                m.quotient(h, p)
        with self.assertRaises(ValueError):
            m.inverse([[0]])

    def test_30_tensor_sum_block_caps(self):
        with self.assertRaises(ValueError):
            m.tensor(m.eye(3), m.eye(2))
        with self.assertRaises(ValueError):
            m.direct_sum(m.eye(3), m.eye(2))
        with self.assertRaises(ValueError):
            m.block([[1]], [[1], [2]], [[1]], [[1]])
        with self.assertRaises(ValueError):
            m.product([[1, 2]], [[1]])

    def test_31_parameter_and_weight_guards(self):
        sp = m.specifications()[0]
        for t in (0, -1, True, 1.0, Q(1, 101), 101):
            with self.assertRaises(ValueError):
                m.source_value(sp, t)
        for alpha in (True, 0, 3):
            bad = dict(sp, alpha=alpha)
            with self.assertRaises(ValueError):
                m.source_value(bad, 2)
        for weights in ([0], [-1], [True]):
            with self.assertRaises(ValueError):
                m.weighted_sum([m.eye(1)], weights)
        with self.assertRaises(ValueError):
            m.averaging_data(1)

    def test_32_bits_and_work_caps(self):
        with self.assertRaises(ValueError):
            m.rational(1 << 4096)
        with self.assertRaises(ValueError):
            m.rational(Q(1, 1 << 4096))
        m.WORK = m.CAPS["work_units"]
        with self.assertRaises(ValueError):
            m.charge()
        m.WORK = 0
        for bad in (True, -1, 1.0):
            with self.assertRaises(ValueError):
                m.charge(bad)

    def test_33_json_strict(self):
        for raw in (b'{"a":1,"a":2}', b"1.5", b"NaN", b"Infinity", b"null"):
            with self.assertRaises(ValueError):
                m.decode(raw)
        for value in (None, 1.5, {}, {"x": None}):
            if value == {}:
                continue
            with self.assertRaises(ValueError):
                m.typed(value)
        with self.assertRaises(ValueError):
            m.decode("not bytes")

    def test_34_json_caps(self):
        for value in ("x" * 4097, [0] * 5001, 1 << 4096):
            with self.assertRaises(ValueError):
                m.typed(value)
        v = 0
        for _ in range(34):
            v = [v]
        with self.assertRaises(ValueError):
            m.typed(v)
        with self.assertRaises(ValueError):
            m.decode(b" " * 3000001)
        with mock.patch.dict(m.CAPS, json_nodes=2), self.assertRaises(ValueError):
            m.typed([1, 2])

    def test_35_polynomial_caps(self):
        for a, b in (([True], [1]), ([1] * 8, [1] * 8), ([], [1]), ([1 << 4096], [1])):
            with self.assertRaises(ValueError):
                m.polynomial_product(a, b)
        with self.assertRaises(ValueError):
            m.polynomial_product([1 << 3000], [1 << 3000])

    def test_36_LF_and_canonical_json(self):
        self.assertEqual(m.lf(b"a\r\nb\n"), b"a\nb\n")
        self.assertEqual(m.canonical({"b": 1, "a": 2}), b'{"a":2,"b":1}')
        self.assertEqual(json.loads(m.canonical(self.report)), self.report)


if __name__ == "__main__":
    unittest.main()
