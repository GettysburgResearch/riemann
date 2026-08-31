"""Exact winding, rational projection controls, and hostile Xi reconstruction."""

import copy
import sys
import unittest
from dataclasses import dataclass
from fractions import Fraction as Q
from pathlib import Path
from unittest import mock

from flint import acb, arb

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "research/exploratory"))
import xi_companion_box_count_compression as M

OA = M.oa


@dataclass(frozen=True)
class Z:
    x: Q = Q(0)
    y: Q = Q(0)

    def __add__(self, other):
        other = other if isinstance(other, Z) else Z(Q(other))
        return Z(self.x + other.x, self.y + other.y)

    __radd__ = __add__

    def __neg__(self):
        return Z(-self.x, -self.y)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        other = other if isinstance(other, Z) else Z(Q(other))
        return Z(
            self.x * other.x - self.y * other.y, self.x * other.y + self.y * other.x
        )

    __rmul__ = __mul__

    def conj(self):
        return Z(self.x, -self.y)

    def __truediv__(self, other):
        other = other if isinstance(other, Z) else Z(Q(other))
        norm = other.x**2 + other.y**2
        if not norm:
            raise ZeroDivisionError
        return self * Z(other.x / norm, -other.y / norm)


def gram(a, b):
    return [[Z(Q(1)) / Z(x.y + y.y, y.x - x.x) for y in b] for x in a]


def adj(a):
    return [[v.conj() for v in row] for row in zip(*a)]


def mul(a, b):
    return [
        [sum((x * y for x, y in zip(row, col)), Z()) for col in zip(*b)] for row in a
    ]


def subtract(a, b):
    return [[x - y for x, y in zip(row, col)] for row, col in zip(a, b)]


def inverse(a):
    n = len(a)
    rows = [row[:] + [Z(Q(i == j)) for j in range(n)] for i, row in enumerate(a)]
    for j in range(n):
        pivot = rows[j][j]
        rows[j] = [v / pivot for v in rows[j]]
        for i in range(n):
            if i != j:
                scale = rows[i][j]
                rows[i] = [v - scale * w for v, w in zip(rows[i], rows[j])]
    return [row[n:] for row in rows]


def phi(z, u):
    return (z - u) / (z - u.conj())


def value_gram(nodes, zeros):
    values = []
    for b in nodes:
        v = Z(Q(1))
        for u in zeros:
            v *= phi(b, u)
        values.append(v)
    g = gram(nodes, nodes)
    return [
        [values[i] * g[i][j] * values[j].conj() for j in range(len(nodes))]
        for i in range(len(nodes))
    ]


def schur_gram(nodes, zeros):
    g, d, r = gram(nodes, nodes), gram(zeros, zeros), gram(zeros, nodes)
    return subtract(g, mul(mul(adj(r), inverse(d)), r))


def unpack(pair):
    return Q(*pair)


def rball(bounds):
    lo, hi = map(unpack, bounds)
    return arb(OA.qarb((lo + hi) / 2), OA.qarb((hi - lo) / 2))


def cball(bounds):
    return acb(rball(bounds["real"]), rball(bounds["imag"]))


def fraction_compression(comp):
    """Independent outward rational intervals: no FLINT matrix operations."""
    dyadic = 2**160

    def rounded(lo, hi):
        return Q((lo * dyadic).__floor__(), dyadic), Q((hi * dyadic).__ceil__(), dyadic)

    def real(x=0):
        return Q(x), Q(x)

    def plus(a, b):
        return rounded(a[0] + b[0], a[1] + b[1])

    def minus(a):
        return -a[1], -a[0]

    def subtract_real(a, b):
        return plus(a, minus(b))

    def times(a, b):
        values = [x * y for x in a for y in b]
        return rounded(min(values), max(values))

    def reciprocal(a):
        if a[0] <= 0 <= a[1]:
            raise ValueError("rational interval reciprocal includes zero")
        return rounded(1 / a[1], 1 / a[0])

    def square(a):
        low = Q(0) if a[0] <= 0 <= a[1] else min(a[0] ** 2, a[1] ** 2)
        return rounded(low, max(a[0] ** 2, a[1] ** 2))

    def complex_point(x=0, y=0):
        return real(x), real(y)

    def add(a, b):
        return plus(a[0], b[0]), plus(a[1], b[1])

    def subtract_complex(a, b):
        return subtract_real(a[0], b[0]), subtract_real(a[1], b[1])

    def conjugate(a):
        return a[0], minus(a[1])

    def multiply(a, b):
        return subtract_real(times(a[0], b[0]), times(a[1], b[1])), plus(
            times(a[0], b[1]), times(a[1], b[0])
        )

    def invert(a):
        den = reciprocal(plus(square(a[0]), square(a[1])))
        return times(a[0], den), times(minus(a[1]), den)

    def total(values):
        result = complex_point()
        for value in values:
            result = add(result, value)
        return result

    def matrix_product(a, b):
        return [
            [total([multiply(x, y) for x, y in zip(row, col)]) for col in zip(*b)]
            for row in a
        ]

    def matrix_inverse(a):
        n = len(a)
        rows = [
            row[:] + [complex_point(int(i == j)) for j in range(n)]
            for i, row in enumerate(a)
        ]
        for j in range(n):
            pivot_inverse = invert(rows[j][j])
            rows[j] = [multiply(v, pivot_inverse) for v in rows[j]]
            for i in range(n):
                if i != j:
                    scale = rows[i][j]
                    rows[i] = [
                        subtract_complex(v, multiply(scale, w))
                        for v, w in zip(rows[i], rows[j])
                    ]
        return [row[n:] for row in rows]

    nodes, values = [], []
    for row in comp["roots"]:
        x, y = map(unpack, row["center"])
        r = unpack(row["radius"])
        nodes.append(((x - r, x + r), (y - r, y + r)))
        values.append(
            tuple(tuple(map(unpack, row["raw_theta"][k])) for k in ("real", "imag"))
        )
    n = len(nodes)
    g = [
        [
            invert(
                (
                    plus(nodes[i][1], nodes[j][1]),
                    subtract_real(nodes[j][0], nodes[i][0]),
                )
            )
            for j in range(n)
        ]
        for i in range(n)
    ]
    h = [
        [multiply(multiply(values[i], g[i][j]), conjugate(values[j])) for j in range(n)]
        for i in range(n)
    ]
    product = matrix_product(matrix_inverse(g), h)
    trace = total([product[i][i] for i in range(n)])[0]
    ray = [complex_point(*p) for p in comp["ray_gaussian_integer_coefficients"]]
    numerator = total(
        [
            multiply(multiply(conjugate(ray[i]), h[i][j]), ray[j])
            for i in range(n)
            for j in range(n)
        ]
    )[0]
    denominator = total(
        [
            multiply(multiply(conjugate(ray[i]), g[i][j]), ray[j])
            for i in range(n)
            for j in range(n)
        ]
    )[0]
    return trace, times(numerator, reciprocal(denominator))


class TestXiBoxCompression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = M.build_report()

    def mutate(self, callback):
        value = copy.deepcopy(self.report)
        value.pop("payload_sha256")
        callback(value)
        with (
            mock.patch.object(M, "build_report", return_value=self.report),
            self.assertRaises(ValueError),
        ):
            M.check_report(M.seal(value))

    def test_01_fixture_fresh_reconstruction(self):
        self.assertEqual(
            M.canonical(M.load_json(M.FIXTURE.read_bytes())), M.canonical(self.report)
        )

    def test_02_complete_counts(self):
        self.assertEqual([v["count"] for v in self.report["boxes"]], [3, 5, 6])
        self.assertEqual(
            [len(v["roots"]) for v in self.report["compressions"]], [3, 5, 6]
        )

    def test_03_exact_boundary_coverage(self):
        for anchor in (32, 64, 128):
            p = M.boundary(anchor)
            self.assertEqual(len(p), 416)
            self.assertEqual(len(set(p)), 416)
            for x, y in zip(p, p[1:] + p[:1]):
                self.assertEqual(abs(x[0] - y[0]) + abs(x[1] - y[1]), Q(1, 16))
            self.assertEqual(
                sum(x[0] * y[1] - x[1] * y[0] for x, y in zip(p, p[1:] + p[:1])), 24
            )

    def test_04_hulls_exclude_zero(self):
        for box in self.report["boxes"]:
            self.assertEqual(len(box["arcs"]), 416)
            for arc in box["arcs"]:
                r, i = [list(map(unpack, arc["image"][k])) for k in ("real", "imag")]
                self.assertTrue(r[0] > 0 or r[1] < 0 or i[0] > 0 or i[1] < 0)

    def test_05_hulls_contain_polygon_edges(self):
        for box in self.report["boxes"]:
            vertices = [[unpack(q) for q in p] for p in box["vertices"]]
            for j, arc in enumerate(box["arcs"]):
                for k, axis in enumerate(("real", "imag")):
                    lo, hi = map(unpack, arc["image"][axis])
                    for p in (vertices[j], vertices[(j + 1) % len(vertices)]):
                        self.assertLessEqual(lo, p[k])
                        self.assertLessEqual(p[k], hi)

    def test_06_independent_ray_rotation_winding(self):
        # Rotate by i; independently count negative-to-positive x crossings of y<0.
        for box in self.report["boxes"]:
            p = [tuple(map(unpack, v)) for v in box["vertices"]]
            rotated = [(-y, x) for x, y in p]
            self.assertEqual(M.winding(rotated), box["count"])
            self.assertEqual(M.winding(list(reversed(p))), -box["count"])

    def test_07_cauchy_tail_positive(self):
        for box in self.report["boxes"]:
            with OA.precision():
                lamlo = OA.endpoint(OA.frozen_lambda(box["anchor"]).lower())
            for arc in box["arcs"]:
                m, tail = unpack(arc["xi_sup"]), unpack(arc["tail"])
                self.assertGreater(m, 0)
                self.assertGreaterEqual(
                    tail,
                    m * (120 * 8**5 + lamlo * 720 * 8**6) * Q(1, 4) ** 32 / Q(3, 4),
                )

    def test_08_root_rouche_independent(self):
        for comp in self.report["compressions"]:
            for row in comp["roots"]:
                a, d, m = (
                    unpack(row["rouche"][key])
                    for key in ("residual", "derivative", "second")
                )
                r = unpack(row["radius"])
                self.assertLess((a + m * r * r / 2) * 2**50, d * r)
                self.assertEqual(a + m * r * r / 2, unpack(row["rouche"]["left"]))

    def test_09_disjoint_inside_roots(self):
        for comp in self.report["compressions"]:
            for j, row in enumerate(comp["roots"]):
                x, y = map(unpack, row["center"])
                r = unpack(row["radius"])
                self.assertTrue(comp["anchor"] - 6 < x - r < x + r < comp["anchor"] + 6)
                self.assertTrue(0 < y - r < y + r < 1)
                for other in comp["roots"][:j]:
                    self.assertGreater(
                        abs(x - unpack(other["center"][0])), r + unpack(other["radius"])
                    )

    def test_10_local_noncommon(self):
        for comp in self.report["compressions"]:
            for row in comp["roots"]:
                self.assertEqual(
                    set(row["nonzero"]), {"C5", "R0", "C0", "f6", "W", "R5prime"}
                )
                self.assertTrue(all(unpack(q) > 0 for q in row["nonzero"].values()))

    def test_11_reflected_jets(self):
        with OA.precision():
            for comp in self.report["compressions"]:
                for row in comp["roots"]:
                    for a, b in zip(
                        row["rectangle_derivatives"],
                        row["reflected_rectangle_derivatives"],
                    ):
                        self.assertTrue(cball(a).overlaps(cball(b)))

    def test_12_raw_corridors_and_subquarter_node(self):
        for comp in self.report["compressions"]:
            for row in comp["roots"]:
                lo, hi = map(unpack, row["raw_modulus"])
                c, d = map(unpack, row["raw_corridor"])
                self.assertTrue(c < lo < hi < d)
        row = self.report["compressions"][2]["roots"][4]
        self.assertLess(unpack(row["raw_modulus"][1]), Q(1, 4))

    def test_13_exact_projection_schur_orientation(self):
        b = [Z(Q(1), Q(1)), Z(Q(3), Q(2)), Z(Q(7), Q(1))]
        for u in ([Z(Q(2), Q(3))], [Z(Q(2), Q(3)), Z(Q(-1), Q(1))]):
            self.assertEqual(value_gram(b, u), schur_gram(b, u))

    def test_14_wrong_conjugation_is_detected(self):
        b, u = [Z(Q(1), Q(1)), Z(Q(3), Q(2))], Z(Q(2), Q(3))
        g, v = gram(b, b), [phi(x, u) for x in b]
        wrong = [[v[i].conj() * g[i][j] * v[j] for j in range(2)] for i in range(2)]
        self.assertNotEqual(wrong, schur_gram(b, [u]))

    def test_15_exact_common_factor_loewner(self):
        b = [Z(Q(1), Q(1)), Z(Q(3), Q(2))]
        u, gamma = Z(Q(2), Q(3)), Z(Q(-1), Q(1))
        difference = subtract(value_gram(b, [u]), value_gram(b, [u, gamma]))
        self.assertGreater(difference[0][0].x, 0)
        self.assertGreater(difference[1][1].x, 0)
        self.assertEqual(difference[0][1], difference[1][0].conj())
        self.assertEqual(
            difference[0][0] * difference[1][1] - difference[0][1] * difference[1][0],
            Z(),
        )

    def test_16_output_projection_order_countercontrol(self):
        # P=I >= Q=projection onto (1,1); Pi onto e1, v=e2.
        ident = [[Z(Q(1)), Z()], [Z(), Z(Q(1))]]
        projection = [[Z(Q(1, 2)), Z(Q(1, 2))]] * 2
        band = [[Z(Q(1)), Z()], [Z(), Z()]]
        vector = [[Z()], [Z(Q(1))]]
        p = mul(mul(band, ident), vector)
        q = mul(mul(band, projection), vector)
        pnorm = sum((row[0].x ** 2 + row[0].y ** 2 for row in p), Q())
        qnorm = sum((row[0].x ** 2 + row[0].y ** 2 for row in q), Q())
        self.assertEqual(pnorm, 0)
        self.assertEqual(qnorm, Q(1, 4))
        self.assertEqual(mul(projection, projection), projection)

    def test_17_actual_gram_hermitian(self):
        with OA.precision():
            for comp in self.report["compressions"]:
                for name in ("gram", "raw_physical_gram"):
                    a = comp[name]
                    for i in range(len(a)):
                        for j in range(len(a)):
                            self.assertTrue(
                                cball(a[i][j]).overlaps(cball(a[j][i]).conjugate())
                            )

    def test_18_determinant_two_routes(self):
        with OA.precision():
            for comp in self.report["compressions"]:
                det = cball(comp["gram_determinant"])
                product = rball(comp["cauchy_determinant_product"])
                self.assertTrue(
                    product > 0 and det.real > 0 and det.real.overlaps(product)
                )

    def test_19_trace_and_ray_rational_floors(self):
        for comp in self.report["compressions"]:
            self.assertGreater(
                unpack(comp["raw_trace"]["real"][0]),
                unpack(comp["conditional_reduced_global_trace_strict_lower"]),
            )
            self.assertGreater(
                unpack(comp["ray_squared_norm_lower_enclosure"][0]),
                unpack(comp["conditional_reduced_global_norm_strict_lower"]) ** 2,
            )
            trace, ray = fraction_compression(comp)
            self.assertGreater(
                trace[0], unpack(comp["conditional_reduced_global_trace_strict_lower"])
            )
            self.assertGreater(
                ray[0],
                unpack(comp["conditional_reduced_global_norm_strict_lower"]) ** 2,
            )

    def test_20_ancestor_nine_centers_preserved(self):
        self.assertTrue(set(OA.DISKS).issubset(set(M.DISKS)))
        self.assertEqual(len(M.DISKS), 14)

    def test_21_resealed_count_attack(self):
        self.mutate(lambda r: r["boxes"][0].update(count=4))

    def test_22_resealed_omitted_arc_attack(self):
        self.mutate(lambda r: r["boxes"][0]["arcs"].pop())

    def test_23_resealed_root_omission_attack(self):
        self.mutate(lambda r: r["compressions"][1]["roots"].pop(0))

    def test_24_resealed_raw_matrix_attack(self):
        self.mutate(
            lambda r: r["compressions"][0]["raw_physical_gram"][0][1]["imag"].reverse()
        )

    def test_25_resealed_metric_attack(self):
        self.mutate(lambda r: r["contract"].update(metric="Vstar G V"))

    def test_26_resealed_scope_attack(self):
        self.mutate(
            lambda r: r["contract"].update(compression="Fourier-band divergence")
        )

    def test_27_resealed_source_attack(self):
        self.mutate(lambda r: r["frozen_sources"][0].update(commit="0" * 40))

    def test_28_resealed_type_attack(self):
        self.mutate(lambda r: r["boxes"][0].update(count=True))

    def test_29_duplicate_json_rejected(self):
        with self.assertRaises(ValueError):
            M.load_json(b'{"a":1,"a":2}')

    def test_30_float_nonfinite_rejected(self):
        for raw in (b"1.0", b"NaN", b"Infinity", b"-Infinity"):
            with self.assertRaises(ValueError):
                M.load_json(raw)

    def test_31_caps(self):
        with self.assertRaises(ValueError):
            M.validate_tree(2**4097)
        value = 0
        for _ in range(26):
            value = [value]
        with self.assertRaises(ValueError):
            M.validate_tree(value)

    def test_32_bool_input_rejected(self):
        with self.assertRaises(ValueError):
            M.boundary(True)
        with OA.precision(), self.assertRaises(ValueError):
            M.root_record((True, 1, 1, 1))

    def test_33_invalid_domains_rejected(self):
        with OA.precision():
            for z in (acb(0), acb(32, 3), acb(151, 0)):
                with self.assertRaises(ValueError):
                    M.xi_series(z)

    def test_34_polygon_origin_rejected(self):
        with self.assertRaises(ValueError):
            M.winding([(1, 0), (-1, 0), (0, 1)])

    def test_35_known_polygon_windings(self):
        self.assertEqual(M.winding([(1, -1), (1, 1), (-1, 1), (-1, -1)]), 1)
        self.assertEqual(M.winding([(2, -1), (4, -1), (4, 1), (2, 1)]), 0)

    def test_36_series_factorials_reflected_route(self):
        with OA.precision():
            c = acb(32, OA.qarb(Q(1, 2)))
            v = M.xi_series(c, 9)
            w = M.xi_series(c, 9, reflected=True)
            d = OA.xi_jet(c)
            for j in range(9):
                self.assertTrue(v[j].overlaps(w[j]))
                self.assertTrue((v[j] * M.math.factorial(j)).overlaps(d[j]))

    def test_37_runtime_and_source_pins(self):
        M.authenticate()
        self.assertEqual(len(M.BINDINGS), 8)

    def test_38_matrix_order_and_input_type(self):
        with self.assertRaises(ValueError):
            M.physical_matrices([], [])
        with self.assertRaises(ValueError):
            M.physical_matrices([acb(1, -1)], [acb(1)])

    def test_39_ray_coefficients_exact(self):
        for comp in self.report["compressions"]:
            self.assertEqual(
                comp["ray_gaussian_integer_coefficients"],
                [list(v) for v in M.RAYS[comp["anchor"]]],
            )

    def test_40_payload_and_artifact_seals(self):
        value = dict(self.report)
        payload = value.pop("payload_sha256")
        self.assertEqual(payload, OA.digest(M.canonical(value)))
        for path, expected in value["artifacts"].items():
            self.assertEqual(OA.digest(OA.lf((ROOT / path).read_bytes())), expected)


if __name__ == "__main__":
    unittest.main()
