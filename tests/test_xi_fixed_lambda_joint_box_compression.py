"""Fixed-source exact coverage, matrix routes and hostile reconstruction controls."""

from __future__ import annotations

import copy
import sys
import unittest
from fractions import Fraction as Q
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "research" / "exploratory"))
import xi_fixed_lambda_joint_box_compression as M
from flint import acb, acb_mat, ctx

from tests import test_xi_companion_box_count_compression as BCT

OA, BC = M.oa, M.bc
unpack, cball, rball = BCT.unpack, BCT.cball, BCT.rball


class TestXiFixedLambdaJoint(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = M.build_report()
        cls.comps = {c["label"]: c for c in cls.report["compressions"]}
        cls.fractions = {}
        for comp in cls.report["compressions"]:
            supplied = dict(comp)
            supplied["roots"] = [cls.report["roots"][i] for i in comp["root_indices"]]
            cls.fractions[comp["label"]] = BCT.fraction_compression(supplied)

    def mutate(self, callback, full=False):
        value = copy.deepcopy(self.report)
        value.pop("payload_sha256")
        callback(value)
        value = M.seal(value)
        if full:
            with self.assertRaises(ValueError):
                M.check_report(value)
        else:
            with (
                mock.patch.object(M, "build_report", return_value=self.report),
                self.assertRaises(ValueError),
            ):
                M.check_report(value)

    def test_01_fresh_fixture(self):
        self.assertEqual(
            M.canonical(M.load_json(M.FIXTURE.read_bytes())), M.canonical(self.report)
        )

    def test_02_one_parameter(self):
        self.assertEqual(self.report["parameter_anchor"], 64)
        for row in self.report["roots"] + self.report["boxes"]:
            self.assertEqual(row["parameter_anchor"], 64)
        with OA.precision():
            self.assertEqual(
                self.report["lambda_enclosure"], OA.rbounds(OA.frozen_lambda(64))
            )

    def test_03_complete_counts(self):
        self.assertEqual([b["count"] for b in self.report["boxes"]], [3, 5, 6])
        for w, count in ((32, 3), (64, 5), (128, 6)):
            self.assertEqual(
                sum(r["box_center"] == w for r in self.report["roots"]), count
            )
        self.assertEqual(len(self.report["roots"]), 14)

    def test_04_closed_boundary_exact(self):
        for w in (32, 64, 128):
            p = BC.boundary(w)
            self.assertEqual(len(p), 416)
            self.assertEqual(len(set(p)), 416)
            self.assertEqual(min(y for x, y in p), 0)
            self.assertEqual(max(y for x, y in p), 1)
            edges = list(zip(p, p[1:] + p[:1]))
            self.assertTrue(
                all(abs(x[0] - y[0]) + abs(x[1] - y[1]) == Q(1, 16) for x, y in edges)
            )
            self.assertEqual(sum(x[0] * y[1] - x[1] * y[0] for x, y in edges), 24)

    def test_05_every_image_hull_zero_free(self):
        for box in self.report["boxes"]:
            self.assertEqual(len(box["arcs"]), 416)
            for arc in box["arcs"]:
                x, y = [list(map(unpack, arc["image"][k])) for k in ("real", "imag")]
                self.assertTrue(x[0] > 0 or x[1] < 0 or y[0] > 0 or y[1] < 0)

    def test_06_hulls_contain_polygon_edges(self):
        for box in self.report["boxes"]:
            vertices = [list(map(unpack, v)) for v in box["vertices"]]
            for j, arc in enumerate(box["arcs"]):
                for k, axis in enumerate(("real", "imag")):
                    lo, hi = map(unpack, arc["image"][axis])
                    for v in (vertices[j], vertices[(j + 1) % 416]):
                        self.assertTrue(lo <= v[k] <= hi)

    def test_07_rotated_reverse_winding(self):
        for box in self.report["boxes"]:
            p = [tuple(map(unpack, v)) for v in box["vertices"]]
            self.assertEqual(BC.winding([(-y, x) for x, y in p]), box["count"])
            self.assertEqual(BC.winding(list(reversed(p))), -box["count"])

    def test_08_fixed_lambda_cauchy_tail(self):
        with OA.precision():
            lam = OA.endpoint(OA.frozen_lambda(64).lower())
        for box in self.report["boxes"]:
            for arc in box["arcs"]:
                m, t = unpack(arc["xi_sup"]), unpack(arc["tail"])
                self.assertGreater(m, 0)
                self.assertGreaterEqual(
                    t, m * (120 * 8**5 + lam * 720 * 8**6) * Q(1, 4) ** 32 / Q(3, 4)
                )

    def test_09_exact_rouche(self):
        for row in self.report["roots"]:
            a, d, m = (
                unpack(row["rouche"][k]) for k in ("residual", "derivative", "second")
            )
            r = unpack(row["radius"])
            self.assertEqual(r, Q(1, 2**120))
            self.assertEqual(a + m * r * r / 2, unpack(row["rouche"]["left"]))
            self.assertLess((a + m * r * r / 2) * 2**50, d * r)

    def test_10_disjoint_inside(self):
        for j, row in enumerate(self.report["roots"]):
            x, y = map(unpack, row["center"])
            r, w = unpack(row["radius"]), row["box_center"]
            self.assertTrue(w - 6 < x - r < x + r < w + 6 and 0 < y - r < y + r < 1)
            for other in self.report["roots"][:j]:
                self.assertGreater(
                    abs(x - unpack(other["center"][0])), r + unpack(other["radius"])
                )

    def test_11_noncommon_every_rectangle(self):
        for row in self.report["roots"]:
            self.assertEqual(
                set(row["nonzero"]), {"C5", "R0", "C0", "f6", "W", "R5prime"}
            )
            self.assertTrue(all(unpack(v) > 0 for v in row["nonzero"].values()))

    def test_12_reflected_jet_route(self):
        with OA.precision():
            for row in self.report["roots"]:
                for a, b in zip(
                    row["rectangle_derivatives"], row["reflected_rectangle_derivatives"]
                ):
                    self.assertTrue(cball(a).overlaps(cball(b)))

    def test_13_exact_raw_corridors(self):
        for row in self.report["roots"]:
            a, b = map(unpack, row["raw_modulus"])
            c, d = map(unpack, row["raw_corridor"])
            self.assertTrue(c < a < b < d)
            self.assertGreater(a, Q(1, 4))

    def test_14_middle_baseline_unchanged(self):
        self.assertEqual(
            [d for d in M.DISKS if d[0] == 64], [d for d in BC.DISKS if d[0] == 64]
        )
        with OA.precision():
            for d in M.DISKS:
                if d[0] == 64:
                    old, _, _ = BC.root_record(d)
                    new, _, _ = M.root_record(d)
                    old.pop("anchor")
                    new.pop("box_center")
                    new.pop("parameter_anchor")
                    self.assertEqual(old, new)

    def test_15_declared_matrix_orders(self):
        self.assertEqual(
            [len(c["root_indices"]) for c in self.report["compressions"]],
            [3, 5, 6, 8, 14],
        )
        for c in self.report["compressions"]:
            n = len(c["root_indices"])
            for key in ("gram", "raw_physical_gram"):
                self.assertEqual(len(c[key]), n)
                self.assertTrue(all(len(row) == n for row in c[key]))

    def test_16_hermitian_forms(self):
        with OA.precision():
            for c in self.report["compressions"]:
                for key in ("gram", "raw_physical_gram"):
                    a = c[key]
                    for i in range(len(a)):
                        for j in range(len(a)):
                            self.assertTrue(
                                cball(a[i][j]).overlaps(cball(a[j][i]).conjugate())
                            )

    def test_17_positive_cauchy_determinants(self):
        with OA.precision():
            for c in self.report["compressions"]:
                d, p = (
                    cball(c["gram_determinant"]),
                    rball(c["cauchy_determinant_product"]),
                )
                self.assertTrue(d.real > 0 and p > 0 and d.real.overlaps(p))

    def test_18_inverse_routes(self):
        with OA.precision():
            for c in self.report["compressions"]:
                self.assertTrue(
                    cball(c["raw_trace"]).overlaps(cball(c["row_inverse_trace"]))
                )

    def test_19_independent_fraction_matrix_floors(self):
        for c in self.report["compressions"]:
            tr, ray = self.fractions[c["label"]]
            tf = unpack(c["conditional_reduced_global_trace_strict_lower"])
            nf = unpack(c["conditional_reduced_global_norm_strict_lower"])
            self.assertGreater(tr[0], tf)
            self.assertGreater(ray[0], nf**2)
            self.assertGreater(unpack(c["raw_trace"]["real"][0]), tf)
            self.assertGreater(unpack(c["ray_squared_norm_lower_enclosure"][0]), nf**2)

    def test_20_independent_increment_subtraction(self):
        for row in self.report["orthogonal_input_increments"]:
            before = self.fractions[row["from"]][0]
            after = self.fractions[row["to"]][0]
            floor = unpack(row["conditional_reduced_increment_trace_strict_lower"])
            self.assertGreater(after[0] - before[1], floor)
            self.assertGreater(unpack(row["raw_increment_trace"]["real"][0]), floor)

    def test_21_joint_not_sum(self):
        lo = self.fractions["joint"][0][0]
        hi = sum(self.fractions[k][0][1] for k in ("box32", "box64", "box128"))
        self.assertGreater(lo - hi, Q(1, 100))
        self.assertGreater(
            unpack(self.report["joint_minus_sum_individual_raw_traces"]["real"][0]),
            Q(1, 100),
        )

    def test_22_nested_spans(self):
        a, b, c = [
            self.comps[k]["root_indices"] for k in ("box32", "prefix32_64", "joint")
        ]
        self.assertTrue(set(a) < set(b) < set(c))
        self.assertEqual([len(b) - len(a), len(c) - len(b)], [5, 6])

    def test_23_every_cross_entry_and_principal_block(self):
        joint = self.comps["joint"]
        for comp in self.report["compressions"]:
            for key in ("gram", "raw_physical_gram"):
                for i, gi in enumerate(comp["root_indices"]):
                    for j, gj in enumerate(comp["root_indices"]):
                        self.assertEqual(comp[key][i][j], joint[key][gi][gj])
        with OA.precision():
            for i in range(3):
                for j in range(3, 14):
                    self.assertGreater(cball(joint["gram"][i][j]).abs_lower(), 0)

    def test_24_wrong_orientation_actual_data(self):
        with OA.precision():
            rows = self.report["roots"]
            a, b = cball(rows[0]["raw_theta"]), cball(rows[3]["raw_theta"])
            g = cball(self.comps["joint"]["gram"][0][3])
            correct = cball(self.comps["joint"]["raw_physical_gram"][0][3])
            self.assertTrue((a * g * b.conjugate()).overlaps(correct))
            self.assertFalse((a.conjugate() * g * b).overlaps(correct))

    def test_25_exact_synthetic_common_factor_order(self):
        Z = BCT.Z
        nodes = [Z(Q(1), Q(1)), Z(Q(3), Q(2))]
        u, gamma = Z(Q(2), Q(3)), Z(Q(-1), Q(1))
        diff = BCT.subtract(
            BCT.value_gram(nodes, [u]), BCT.value_gram(nodes, [u, gamma])
        )
        self.assertGreater(diff[0][0].x, 0)
        self.assertGreater(diff[1][1].x, 0)
        self.assertEqual(diff[0][0] * diff[1][1] - diff[0][1] * diff[1][0], Z())

    def test_26_all_source_artifact_seals(self):
        unsigned = dict(self.report)
        digest = unsigned.pop("payload_sha256")
        self.assertEqual(digest, OA.digest(M.canonical(unsigned)))
        for path, digest in unsigned["artifacts"].items():
            self.assertEqual(digest, OA.digest(OA.lf((ROOT / path).read_bytes())))
        self.assertEqual(len(M.BINDINGS), 6)

    def test_27_resealed_count(self):
        self.mutate(lambda r: r["boxes"][0].update(count=4))

    def test_28_resealed_scope(self):
        self.mutate(
            lambda r: r["contract"].update(joint="cofinal Fourier band divergence")
        )

    def test_29_resealed_type(self):
        self.mutate(lambda r: r.update(parameter_anchor=True))

    def test_30_resealed_wrong_parameter(self):
        self.mutate(lambda r: r["roots"][0].update(parameter_anchor=32))

    def test_31_resealed_cross_entry_omission(self):
        self.mutate(lambda r: r["compressions"][-1]["gram"][0].pop(3))

    def test_32_resealed_raw_reduced_confusion(self):
        self.mutate(
            lambda r: r["contract"].update(
                common_factor="Gamma is known constant at lambda64"
            )
        )

    def test_33_resealed_increment(self):
        self.mutate(lambda r: r["orthogonal_input_increments"][0].update(to="box64"))

    def test_34_duplicate_keys(self):
        with self.assertRaises(ValueError):
            M.load_json(b'{"a":1,"a":2}')

    def test_35_floats_nonfinite(self):
        for data in (b"1.0", b"NaN", b"Infinity", b"-Infinity"):
            with self.assertRaises(ValueError):
                M.load_json(data)

    def test_36_caps(self):
        for v in (2**4097, b"bytes"):
            with self.assertRaises(ValueError):
                M.validate_tree(v)
        v = 0
        for _ in range(26):
            v = [v]
        with self.assertRaises(ValueError):
            M.validate_tree(v)
        with self.assertRaises(ValueError):
            M.load_json(b" " * 12_000_001)
        for raw in (b"bad\x00", b"bad\x7f", b"bad\xc2\x80"):
            with self.assertRaises(ValueError):
                M.lf(raw)

    def test_37_parameter_and_matrix_input_guards(self):
        with OA.precision():
            for row in ((True, 1, 1, 1), (33, 1, 1, 1), (32, True, 1, 1)):
                with self.assertRaises(ValueError):
                    M.root_record(row)
            for nodes, values in (
                ([], []),
                ([acb(1, -1)], [acb(1)]),
                ([acb(1, 1)] * 15, [acb(1)] * 15),
            ):
                with self.assertRaises(ValueError):
                    M.physical_matrices(nodes, values)
            with self.assertRaises(ValueError):
                M.compression_report("adaptive", [])

    def test_38_fixed_gaussian_integer_rays(self):
        for c in self.report["compressions"]:
            ray = c["ray_gaussian_integer_coefficients"]
            self.assertEqual(ray, [list(v) for v in M.RAYS[c["label"]]])
            self.assertTrue(
                all(type(x) is int and abs(x) <= 2048 for v in ray for x in v)
            )

    def test_39_precision_context_restored(self):
        old = ctx.prec, ctx.cap
        with OA.precision():
            M.root_record(M.DISKS[0])
        self.assertEqual((ctx.prec, ctx.cap), old)

    def test_40_runtime_and_source_authentication(self):
        M.authenticate()

    def test_41_primitive_zero_jet_attack(self):
        with (
            mock.patch.object(
                BC,
                "xi_series",
                side_effect=lambda z, cap=39, reflected=False: [acb(0)] * cap,
            ),
            self.assertRaises(ValueError),
        ):
            M.box_count(32)

    def test_42_only_lambda64_called(self):
        with mock.patch.object(OA, "frozen_lambda", wraps=OA.frozen_lambda) as called:
            with OA.precision():
                for d in M.DISKS:
                    M.root_record(d)
            M.box_count(32)
        self.assertTrue(called.call_args_list)
        self.assertTrue(all(args.args == (64,) for args in called.call_args_list))

    def test_43_wrong_primitive_matrix_orientation(self):
        original = M.physical_matrices

        def wrong(nodes, values):
            g, _ = original(nodes, values)
            n = len(nodes)
            return g, acb_mat(
                [
                    [values[i].conjugate() * g[i, j] * values[j] for j in range(n)]
                    for i in range(n)
                ]
            )

        with (
            mock.patch.object(M, "physical_matrices", side_effect=wrong),
            self.assertRaises(ValueError),
        ):
            M.check_report(self.report)

    def test_44_full_fresh_resealed_count(self):
        self.mutate(lambda r: r["boxes"][2].update(count=7), full=True)


if __name__ == "__main__":
    unittest.main()
