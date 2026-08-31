"""Held-out coverage and independent rational Gram/weight reconstruction."""

from __future__ import annotations

import copy
import math
import sys
import unittest
from fractions import Fraction as Q
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "research" / "exploratory"))
import xi_fixed_lambda_heldout_alignment as M
from flint import acb, arb, ctx

OA = M.oa


def unpair(v):
    return Q(*v)


def point(v):
    return Q(v), Q(v)


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def neg(a):
    return -a[1], -a[0]


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    v = [x * y for x in a for y in b]
    return min(v), max(v)


def inv(a):
    if a[0] <= 0 <= a[1]:
        raise ValueError("interval reciprocal")
    return 1 / a[1], 1 / a[0]


def square(a):
    return (
        Q(0) if a[0] <= 0 <= a[1] else min(a[0] ** 2, a[1] ** 2),
        max(a[0] ** 2, a[1] ** 2),
    )


def sqrtq(v):
    if v < 0:
        raise ValueError("negative square root")
    scale = 2**160
    k = math.isqrt((v * scale * scale).__floor__())
    return Q(k, scale), Q(k if Q(k * k, scale * scale) == v else k + 1, scale)


def sqrt_interval(a):
    return sqrtq(a[0])[0], sqrtq(a[1])[1]


def independent_data(roots):
    """Only stdlib Fraction/isqrt: no author or FLINT matrix operations."""
    nodes = []
    weights = []
    for row in roots:
        x, y = map(unpair, row["center"])
        r = unpair(row["radius"])
        nodes.append(((x - r, x + r), (y - r, y + r)))
        u, v = [tuple(map(unpair, row["raw_theta"][k])) for k in ("real", "imag")]
        weights.append(
            mul(mul(add(square(u), square(v)), nodes[-1][1]), inv(nodes[-1][0]))
        )
    matrix = []
    moduli = []
    for i, (x, y) in enumerate(nodes):
        entries = []
        absolute = []
        for j, (xx, yy) in enumerate(nodes):
            if i == j:
                entries.append((point(1), point(0)))
                absolute.append(point(1))
                continue
            a, b = add(y, yy), sub(xx, x)
            denominator = add(square(a), square(b))
            coefficient = mul(point(2), sqrt_interval(mul(y, yy)))
            factor = mul(coefficient, inv(denominator))
            entries.append((mul(factor, a), neg(mul(factor, b))))
            absolute.append(
                sqrt_interval(mul(mul(point(4), mul(y, yy)), inv(denominator)))
            )
        matrix.append(entries)
        moduli.append(absolute)
    return matrix, moduli, weights


class TestHeldoutXi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = M.build_report()
        cls.matrix, cls.moduli, cls.weights = independent_data(cls.report["roots"])

    def mutate(self, callback, full=False):
        v = copy.deepcopy(self.report)
        v.pop("payload_sha256")
        callback(v)
        v = M.seal(v)
        if full:
            with self.assertRaises(ValueError):
                M.check_report(v)
        else:
            with (
                mock.patch.object(M, "build_report", return_value=self.report),
                self.assertRaises(ValueError),
            ):
                M.check_report(v)

    def test_01_fresh_fixture(self):
        self.assertEqual(
            M.canonical(M.load_json(M.FIXTURE.read_bytes())), M.canonical(self.report)
        )

    def test_02_counts_and_complete_nodes(self):
        self.assertEqual([b["count"] for b in self.report["boxes"]], [8, 9, 9])
        self.assertEqual(len(self.report["roots"]), 40)
        self.assertEqual(
            [
                sum(r["box_center"] == w for r in self.report["roots"])
                for w in M.WINDOWS
            ],
            [8, 9, 9],
        )

    def test_03_fixed_tier_records(self):
        self.assertEqual(
            self.report["boundary_tiers"],
            [[256, 16, 32], [512, 32, 40], [1024, 64, 48]],
        )
        attempts = self.report["boxes"][-1]["attempts"]
        self.assertEqual([a["status"] for a in attempts], ["FAILED", "FAILED", "PASS"])
        self.assertEqual([a["arc_index"] for a in attempts[:2]], [194, 389])

    def test_04_boundaries_no_moved_edges(self):
        for w in M.WINDOWS:
            for den in (16, 32, 64):
                p = M.boundary(w, den)
                self.assertEqual(len(p), 26 * den)
                self.assertEqual(len(set(p)), 26 * den)
                self.assertEqual(
                    (
                        min(x for x, y in p),
                        max(x for x, y in p),
                        min(y for x, y in p),
                        max(y for x, y in p),
                    ),
                    (w - 6, w + 6, 0, 1),
                )
                edges = list(zip(p, p[1:] + p[:1]))
                self.assertTrue(
                    all(
                        abs(a[0] - b[0]) + abs(a[1] - b[1]) == Q(1, den)
                        for a, b in edges
                    )
                )
                self.assertEqual(sum(a[0] * b[1] - a[1] * b[0] for a, b in edges), 24)

    def test_05_all_hulls_exclude_zero(self):
        for box in self.report["boxes"]:
            tier = box["attempts"][-1]
            self.assertEqual(len(box["arcs"]), 26 * tier["mesh_denominator"])
            for arc in box["arcs"]:
                a, b = [list(map(unpair, arc["image"][k])) for k in ("real", "imag")]
                self.assertTrue(a[0] > 0 or a[1] < 0 or b[0] > 0 or b[1] < 0)

    def test_06_hulls_contain_endpoint_polygon(self):
        for box in self.report["boxes"]:
            v = [[unpair(q) for q in p] for p in box["vertices"]]
            for j, a in enumerate(box["arcs"]):
                for k, axis in enumerate(("real", "imag")):
                    lo, hi = map(unpair, a["image"][axis])
                    self.assertTrue(
                        lo <= v[j][k] <= hi and lo <= v[(j + 1) % len(v)][k] <= hi
                    )

    def test_07_independent_rotated_winding(self):
        for box in self.report["boxes"]:
            v = [tuple(map(unpair, p)) for p in box["vertices"]]
            self.assertEqual(M.winding([(-y, x) for x, y in v]), box["count"])
            self.assertEqual(M.winding(list(reversed(v))), -box["count"])

    def test_08_exact_cauchy_tails(self):
        for box in self.report["boxes"]:
            tier = box["attempts"][-1]
            with M.precision(tier["bits"]):
                lam = OA.endpoint(M.fixed_lambda().lower())
            h = Q(1, 2 * tier["mesh_denominator"])
            n = tier["terms"]
            for a in box["arcs"]:
                m, t = unpair(a["xi_sup"]), unpair(a["tail"])
                self.assertGreaterEqual(
                    t, m * (120 * 8**5 + lam * 720 * 8**6) * (8 * h) ** n / (1 - 8 * h)
                )

    def test_09_all_seed_outcomes_retained(self):
        for s in self.report["scouts"]:
            self.assertEqual(len(s["seed_log"]), 196)
            expected = {
                ((Q(s["box_center"] - 6) + Q(j, 4)), y)
                for j in range(49)
                for y in (Q(1, 8), Q(3, 8), Q(5, 8), Q(7, 8))
            }
            self.assertEqual(
                {tuple(map(unpair, r["seed"])) for r in s["seed_log"]}, expected
            )
            self.assertTrue(any(r["status"] == "domain exit" for r in s["seed_log"]))
            self.assertTrue(all(0 <= r["steps"] <= 24 for r in s["seed_log"]))

    def test_10_scouts_not_count_proof(self):
        for s, b in zip(self.report["scouts"], self.report["boxes"]):
            self.assertEqual(s["candidates"], M.NEW_CENTERS[s["box_center"]])
            self.assertEqual(len(s["candidates"]), b["count"])
            self.assertGreater(len(s["seed_log"]), b["count"])

    def test_11_rouche_exact(self):
        for r in self.report["roots"]:
            a, d, m = (
                unpair(r["rouche"][k]) for k in ("residual", "derivative", "second")
            )
            radius = unpair(r["radius"])
            self.assertEqual(radius, Q(1, 2**120))
            self.assertLess((a + m * radius**2 / 2) * 2**50, d * radius)

    def test_12_disjoint_inside(self):
        for j, r in enumerate(self.report["roots"]):
            x, y = map(unpair, r["center"])
            d = unpair(r["radius"])
            w = r["box_center"]
            self.assertTrue(w - 6 < x - d < x + d < w + 6 and 0 < y - d < y + d < 1)
            for other in self.report["roots"][:j]:
                self.assertGreater(
                    abs(x - unpair(other["center"][0])), d + unpair(other["radius"])
                )

    def test_13_noncommon_every_rectangle(self):
        for r in self.report["roots"]:
            self.assertEqual(
                set(r["nonzero"]), {"R0", "C0", "C5", "f6", "W", "R5prime"}
            )
            self.assertTrue(all(unpair(v) > 0 for v in r["nonzero"].values()))

    def test_14_one_parameter_and_old_centers(self):
        self.assertEqual(self.report["parameter_anchor"], 64)
        self.assertTrue(all(r["parameter_anchor"] == 64 for r in self.report["roots"]))
        self.assertEqual(self.report["roots"][:14], M.frozen_fc_report()["roots"])
        keys = (
            "box_center",
            "parameter_anchor",
            "center",
            "radius",
            "point_derivatives",
            "rectangle_derivatives",
            "reflected_rectangle_derivatives",
            "rouche",
            "nonzero",
            "raw_theta",
            "raw_modulus",
        )
        science = {
            "roots": [{k: r[k] for k in keys} for r in self.report["roots"]],
            "finite_data": self.report["finite_data"],
        }
        self.assertEqual(
            OA.digest(M.canonical(science)),
            "235c8ff36e3a6e00c0c86ec59be843d1a3aabe3912a4e5940351e1db5e464060",
        )

    def test_15_failed_quarter_pattern(self):
        self.assertLess(unpair(self.report["roots"][14]["raw_modulus"][1]), Q(54, 1000))
        self.assertLess(Q(54, 1000), Q(1, 4))

    def test_16_gram_shape_and_diagonal(self):
        g = self.report["finite_data"]["normalized_gram"]
        self.assertEqual(len(g), 40)
        self.assertTrue(all(len(row) == 40 for row in g))
        for j in range(40):
            self.assertEqual(
                g[j][j], {"real": [[1, 1], [1, 1]], "imag": [[0, 1], [0, 1]]}
            )

    def test_17_all_matrix_entries_independent_intervals(self):
        g = self.report["finite_data"]["normalized_gram"]
        for i in range(40):
            for j in range(40):
                for k, axis in enumerate(("real", "imag")):
                    a, b = map(unpair, g[i][j][axis])
                    c, d = self.matrix[i][j][k]
                    self.assertTrue(a <= d and c <= b)

    def test_18_finite_bessel_ceilings(self):
        for p in self.report["finite_data"]["prefixes"]:
            indices = p["root_indices"]
            c = unpair(p["finite_bessel_strict_upper"])
            for i in indices:
                self.assertLess(sum(self.moduli[i][j][1] for j in indices), c)

    def test_19_weighted_prefixes_independent(self):
        for p in self.report["finite_data"]["prefixes"]:
            indices = p["root_indices"]
            lo = sum(self.weights[i][0] for i in indices)
            hi = sum(self.weights[i][1] for i in indices)
            a, b = map(unpair, p["weighted_alignment"])
            self.assertTrue(a <= hi and lo <= b)
            self.assertGreater(lo, unpair(p["weighted_alignment_strict_lower"]))

    def test_20_weighted_increments_independent(self):
        previous = set()
        for p in self.report["finite_data"]["prefixes"]:
            indices = set(p["root_indices"])
            added = indices - previous
            self.assertGreater(
                sum(self.weights[i][0] for i in added),
                unpair(p["weighted_increment_strict_lower"]),
            )
            previous = indices

    def test_21_prefix_coverage_and_finite_ceiling_values(self):
        p = self.report["finite_data"]["prefixes"]
        self.assertEqual([len(v["root_indices"]) for v in p], [14, 22, 31, 40])
        self.assertEqual(
            [unpair(v["finite_bessel_strict_upper"]) for v in p],
            list(map(Q, ("2.342", "2.396", "2.414", "2.420"))),
        )

    def test_22_transport_exact_quadratic_control(self):
        c = M.transport_control(Q(1), Q(1), Q(-100), Q(0), Q(1, 2))
        self.assertEqual(
            c,
            {
                "q": [1, 100],
                "delta": [1, 50],
                "radius": [1, 2500],
                "raw_alignment_floor": [1, 3],
            },
        )
        q, r = unpair(c["q"]), unpair(c["radius"])
        self.assertGreater(1 - 100 * (q - r) + 50 * (q - r) ** 2, 0)
        self.assertLess(1 - 100 * (q + r) + 50 * (q + r) ** 2, 0)

    def test_23_transport_error_identity(self):
        for a, c, m in ((Q(1), Q(-100), Q(1)), (Q(-2), Q(400), Q(7))):
            lam = Q(3, 2)
            r = M.transport_control(lam, a, c, m, Q(1, 3))
            q = unpair(r["q"])
            delta = unpair(r["delta"])
            self.assertEqual(
                2 * abs(c) * q * q + m * (4 * q**3 / 3 + 2 * lam * q * q),
                delta * abs(a),
            )
            self.assertLess(2 * delta * q, q)

    def test_24_transport_rejects_missing_hypotheses(self):
        for args in (
            (0, 1, -100, 0, Q(1, 2)),
            (1, 1, 100, 0, Q(1, 2)),
            (1, 1, -100, 10**6, Q(1, 2)),
            (1, 1, -100, 0, 1),
        ):
            with self.assertRaises(ValueError):
                M.transport_control(*map(Q, args))

    def test_25_same_lambda_at_all_precisions(self):
        with OA.precision():
            reference = OA.frozen_lambda(64)
        for bits in (256, 512, 1024):
            with M.precision(bits):
                self.assertTrue(M.fixed_lambda().overlaps(reference))

    def test_26_preserved_failed_boundary_tiers(self):
        for bits, den, terms, j in ((256, 16, 32, 194), (512, 32, 40, 389)):
            with M.precision(bits):
                p = M.boundary(1024, den)
                with self.assertRaises(ValueError):
                    M.arc(p[j], p[j + 1], M.fixed_lambda(), terms)

    def test_27_third_tier_resolves_same_segment(self):
        with M.precision(1024):
            p = M.boundary(1024, 64)
            for j in (778, 779):
                self.assertFalse(
                    M.arc(p[j], p[j + 1], M.fixed_lambda(), 48)[0].contains(0)
                )

    def test_28_reflected_extended_domain_jets(self):
        with M.precision():
            for w in M.WINDOWS:
                z = acb(w, arb(1) / 2)
                self.assertTrue(
                    all(a.overlaps(b) for a, b in zip(M.xi_jet(z), M.xi_jet(z, True)))
                )

    def test_29_resealed_omitted_failed_tier(self):
        self.mutate(lambda r: r["boxes"][-1]["attempts"].pop(0))

    def test_30_resealed_seed_erasure(self):
        self.mutate(lambda r: r["scouts"][0]["seed_log"].pop())

    def test_31_resealed_false_divergence(self):
        self.mutate(lambda r: r["contract"].update(weight="physical trace diverges"))

    def test_32_resealed_parameter(self):
        self.mutate(lambda r: r.update(parameter_anchor=1024))

    def test_33_resealed_canonical_class(self):
        self.mutate(
            lambda r: r["contract"].update(arithmetic_class="EXACT_INTEGER_ONLY")
        )

    def test_34_resealed_cross_entry_erasure(self):
        self.mutate(lambda r: r["finite_data"]["normalized_gram"][0].pop(14))

    def test_35_resealed_source_or_boolean(self):
        self.mutate(lambda r: r["frozen_sources"][0].update(commit="0" * 40))
        self.mutate(lambda r: r["boxes"][0].update(count=True))

    def test_36_strict_json(self):
        for raw in (b'{"a":1,"a":2}', b"1.0", b"NaN", b"Infinity"):
            with self.assertRaises(ValueError):
                M.load_json(raw)

    def test_37_caps_and_source_controls(self):
        for v in (2**4097, b"bytes"):
            with self.assertRaises(ValueError):
                M.validate_tree(v)
        v = 0
        for _ in range(26):
            v = [v]
        with self.assertRaises(ValueError):
            M.validate_tree(v)
        with self.assertRaises(ValueError):
            M.load_json(b" " * 24_000_001)
        for raw in (b"bad\x00", b"bad\x7f", b"bad\xc2\x80"):
            with self.assertRaises(ValueError):
                M.lf(raw)

    def test_38_wrapper_caps_types_and_restore(self):
        old = ctx.prec, ctx.cap
        for bits in (True, 192, 2048):
            with self.assertRaises(ValueError), M.precision(bits):
                pass
        with M.precision():
            for z in (acb(20), acb(1100), acb(512, 3)):
                with self.assertRaises(ValueError):
                    M.xi_series(z)
            with self.assertRaises(ValueError):
                M.xi_series(acb(512), 56)
            with self.assertRaises(ValueError):
                M.normalized_gram([acb(1, 1)] * 65)
            with self.assertRaises(ValueError):
                M.boundary(True)
        self.assertEqual((ctx.prec, ctx.cap), old)

    def test_39_wrong_lambda_primitive_root_rejected(self):
        with mock.patch.object(
            M, "fixed_lambda", side_effect=lambda: OA.frozen_lambda(32)
        ):
            row, box, value = M.root_record(256, *M.NEW_CENTERS[256][0])
        self.assertIsNone(box)
        self.assertIsNone(value)
        self.assertEqual([a["status"] for a in row["attempts"]], ["FAILED"] * 3)

    def test_40_runtime_and_source_authentication(self):
        M.authenticate()

    def test_41_source_artifact_payload_seals(self):
        v = dict(self.report)
        digest = v.pop("payload_sha256")
        self.assertEqual(digest, OA.digest(M.canonical(v)))
        for p, d in v["artifacts"].items():
            self.assertEqual(d, OA.digest(M.lf((ROOT / p).read_bytes())))
        self.assertEqual(len(M.BINDINGS), 7)

    def test_42_integer_sqrt_route(self):
        for q in (Q(0), Q(2), Q(7, 13), Q(100, 49)):
            lo, hi = sqrtq(q)
            self.assertTrue(lo * lo <= q <= hi * hi)
            self.assertLessEqual(hi - lo, Q(1, 2**160))

    def test_43_primitive_zero_jet_attack(self):
        with mock.patch.object(M, "xi_jet", return_value=[acb(0)] * 9):
            row, box, value = M.root_record(256, *M.NEW_CENTERS[256][0])
        self.assertIsNone(box)
        self.assertIsNone(value)
        self.assertEqual([a["status"] for a in row["attempts"]], ["FAILED"] * 3)

    def test_44_full_fresh_resealed_count(self):
        self.mutate(lambda r: r["boxes"][-1].update(count=10), full=True)


if __name__ == "__main__":
    unittest.main()
