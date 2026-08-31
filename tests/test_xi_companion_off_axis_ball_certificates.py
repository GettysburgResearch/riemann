"""Independent local controls and hostile replay tests for actual Xi certificates."""

import copy
import importlib.util
import unittest
from fractions import Fraction as Q
from pathlib import Path
from unittest import mock

from flint import acb, arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/exploratory/xi_companion_off_axis_ball_certificates.py"
SPEC = importlib.util.spec_from_file_location("xi_off_axis", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


def unpack(row):
    return Q(row[0], row[1])


def real_ball(bounds):
    a, b = map(unpack, bounds)
    return arb(M.qarb((a + b) / 2), M.qarb((b - a) / 2))


def complex_ball(bounds):
    return acb(real_ball(bounds["real"]), real_ball(bounds["imag"]))


class TestXiOffAxis(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = M.build_report()

    def mutated(self, function):
        report = copy.deepcopy(self.report)
        report.pop("payload_sha256")
        function(report)
        with self.assertRaises(ValueError):
            M.check_report(M.seal(report))

    def test_01_exact_coverage(self):
        rows = self.report["disks"]
        self.assertEqual(len(rows), 9)
        self.assertEqual([r["anchor"] for r in rows], [32] * 3 + [64] * 3 + [128] * 3)
        self.assertEqual([r["id"] for r in rows], list(range(9)))

    def test_02_independent_rational_rouche(self):
        for row in self.report["disks"]:
            proof = row["rouche"]
            a, d, m = (
                unpack(proof[k])
                for k in ("residual_upper", "derivative_lower", "second_upper")
            )
            r = unpack(row["radius"])
            self.assertGreater(d, 0)
            left, right = a + m * r * r / 2, d * r
            self.assertEqual(left, unpack(proof["left"]))
            self.assertEqual(right, unpack(proof["right"]))
            self.assertLess(left * 2**50, right)
            self.assertEqual(proof["zeros_counted_with_multiplicity"], 1)

    def test_03_exact_rectangles(self):
        for row in self.report["disks"]:
            x, y = map(unpack, row["center"])
            r = unpack(row["radius"])
            self.assertEqual(r, Q(1, 2**120))
            self.assertEqual(
                list(map(unpack, row["rectangle"]["real"])), [x - r, x + r]
            )
            self.assertEqual(
                list(map(unpack, row["rectangle"]["imag"])), [y - r, y + r]
            )
            self.assertGreater(y - r, 0)
            self.assertLess(y + r, 1)
            self.assertGreater(x - r, row["anchor"] - 6)
            self.assertLess(x + r, row["anchor"] + 6)

    def test_04_exact_disjointness(self):
        for j, row in enumerate(self.report["disks"]):
            for other in self.report["disks"][:j]:
                if row["anchor"] == other["anchor"]:
                    delta = abs(unpack(row["center"][0]) - unpack(other["center"][0]))
                    self.assertGreater(
                        delta, unpack(row["radius"]) + unpack(other["radius"])
                    )

    def test_05_raw_corridors(self):
        for row in self.report["disks"]:
            lo, hi = map(unpack, row["raw_Theta0_modulus"])
            coarse_lo, coarse_hi = map(unpack, row["raw_Theta0_coarse_strict_bounds"])
            self.assertGreater(lo, coarse_lo)
            self.assertLess(hi, coarse_hi)
            self.assertGreater(lo, Q(1, 4))

    def test_06_nonzero_guards(self):
        for row in self.report["disks"]:
            self.assertEqual(
                set(row["positive_modulus_lower"]),
                {"C5", "R0", "C0", "f6", "W", "R5prime"},
            )
            self.assertTrue(
                all(unpack(q) > 0 for q in row["positive_modulus_lower"].values())
            )

    def test_07_reflected_route(self):
        with M.precision():
            for row in self.report["disks"]:
                for kind in ("point", "rectangle"):
                    direct = row[kind + "_Xi_derivatives_0_to_8"]
                    reflected = row["reflected_" + kind + "_Xi_derivatives_0_to_8"]
                    self.assertEqual(len(direct), 9)
                    for a, b in zip(direct, reflected):
                        self.assertTrue(complex_ball(a).overlaps(complex_ball(b)))

    def test_08_independent_quotient_jets(self):
        with M.precision(384):
            for row in self.report["disks"]:
                j = list(map(complex_ball, row["rectangle_Xi_derivatives_0_to_8"]))
                ilam = acb(0, 1) * real_ball(row["lambda"])
                r = [j[k] - ilam * j[k + 1] for k in range(3)]
                c = [j[k] + ilam * j[k + 1] for k in range(3)]
                result = [
                    r[0] / c[0],
                    (r[1] * c[0] - r[0] * c[1]) / c[0] ** 2,
                    (
                        r[2] * c[0] ** 2
                        - r[0] * c[2] * c[0]
                        - 2 * r[1] * c[0] * c[1]
                        + 2 * r[0] * c[1] ** 2
                    )
                    / c[0] ** 3,
                ]
                actual = row["rectangle_raw_Theta0_derivatives_0_to_2"]
                for a, b in zip(result, actual):
                    self.assertTrue(a.overlaps(complex_ball(b)))

    def test_09_higher_precision_primitive(self):
        with M.precision(384):
            for row in self.report["disks"]:
                high = M.record(row["id"], 384)
                self.assertTrue(
                    real_ball(high["raw_Theta0_modulus"]).overlaps(
                        real_ball(row["raw_Theta0_modulus"])
                    )
                )
                for a, b in zip(
                    high["point_Xi_derivatives_0_to_8"],
                    row["point_Xi_derivatives_0_to_8"],
                ):
                    self.assertTrue(complex_ball(a).overlaps(complex_ball(b)))

    def test_10_residue_identity(self):
        with M.precision():
            for row in self.report["disks"]:
                q = {k: complex_ball(v) for k, v in row["rectangle_companions"].items()}
                residue = q["R0"] * q["C5"] / (q["C0"] * q["R5prime"])
                claimed = complex_ball(row["native_quotient_residue_at_root"])
                self.assertTrue(residue.overlaps(claimed))
                self.assertGreater(claimed.abs_lower(), 0)

    def test_11_independent_w_identity(self):
        with M.precision():
            for row in self.report["disks"]:
                j = list(map(complex_ball, row["rectangle_Xi_derivatives_0_to_8"]))
                lam = real_ball(row["lambda"])
                r0, c0 = j[0] - acb(0, 1) * lam * j[1], j[0] + acb(0, 1) * lam * j[1]
                r5, c5 = j[5] - acb(0, 1) * lam * j[6], j[5] + acb(0, 1) * lam * j[6]
                w = j[0] * j[6] - j[1] * j[5]
                self.assertTrue(
                    (r0 * c5 - c0 * r5 - 2 * acb(0, 1) * lam * w).contains(0)
                )

    def test_12_actual_lambda_not_asymptotic(self):
        with M.precision():
            for anchor in (32, 64, 128):
                exact = M.frozen_lambda(anchor)
                leading = 2 / (M.qarb(anchor) / (2 * arb.pi())).log()
                self.assertGreater(exact, 0)
                self.assertFalse(exact.overlaps(leading))

    def test_13_context_restored(self):
        old = ctx.prec, ctx.cap
        with M.precision(384):
            self.assertEqual((ctx.prec, ctx.cap), (384, 9))
        self.assertEqual((ctx.prec, ctx.cap), old)
        with self.assertRaises(ValueError), M.precision(384):
            raise ValueError("intentional")
        self.assertEqual((ctx.prec, ctx.cap), old)

    def test_14_source_and_runtime(self):
        self.assertEqual(len(M.authenticate()), 6)
        self.assertEqual(M.runtime(), M.RUNTIME)
        self.assertEqual(M.RUNTIME["native_files"], 44)

    def test_15_fixture(self):
        self.assertTrue(M.check_report(M.load_json(M.FIXTURE.read_bytes())))

    def test_16_resealed_center(self):
        self.mutated(lambda r: r["disks"][0]["center"][0].__setitem__(0, 1))

    def test_17_resealed_radius(self):
        self.mutated(lambda r: r["disks"][0].__setitem__("radius", [1, 2]))

    def test_18_resealed_parameter(self):
        self.mutated(lambda r: r["disks"][0].__setitem__("lambda", [[1, 1], [1, 1]]))

    def test_19_resealed_guard(self):
        self.mutated(
            lambda r: r["disks"][0]["positive_modulus_lower"].__setitem__("W", [0, 1])
        )

    def test_20_resealed_count(self):
        self.mutated(
            lambda r: r["disks"][0]["rouche"].__setitem__(
                "zeros_counted_with_multiplicity", 2
            )
        )

    def test_21_resealed_bool_count(self):
        self.mutated(
            lambda r: r["disks"][0]["rouche"].__setitem__(
                "zeros_counted_with_multiplicity", True
            )
        )

    def test_22_resealed_coverage(self):
        self.mutated(lambda r: r["disks"].pop())

    def test_23_resealed_source(self):
        self.mutated(lambda r: r["frozen_sources"][0].__setitem__("commit", "0" * 40))

    def test_24_resealed_artifact(self):
        self.mutated(
            lambda r: r["artifacts"].__setitem__(next(iter(r["artifacts"])), "0" * 64)
        )

    def test_25_resealed_scope(self):
        self.mutated(
            lambda r: r["contract"].__setitem__("physical_capture", "infinite")
        )

    def test_26_resealed_jet(self):
        self.mutated(
            lambda r: r["disks"][0]["point_Xi_derivatives_0_to_8"][0].__setitem__(
                "real", [[0, 1], [0, 1]]
            )
        )

    def test_27_forged_source_bytes(self):
        with (
            mock.patch.object(M, "read_source", return_value=b"forged\n"),
            self.assertRaises(ValueError),
        ):
            M.authenticate()

    def test_28_forged_runtime(self):
        with (
            mock.patch.object(M, "runtime", return_value={}),
            self.assertRaises(ValueError),
        ):
            M.authenticate()

    def test_29_json_duplicates_and_numbers(self):
        for raw in (b'{"a":1,"a":2}', b'{"x":1.0}', b'{"x":NaN}', b'{"x":Infinity}'):
            with self.assertRaises(ValueError):
                M.load_json(raw)

    def test_30_json_caps(self):
        with self.assertRaises(ValueError):
            M.load_json(b" " * (M.MAX_BYTES + 1))
        with self.assertRaises(ValueError):
            M.validate_tree(1 << M.MAX_BITS)
        deep = 0
        for _ in range(M.MAX_DEPTH + 1):
            deep = [deep]
        with self.assertRaises(ValueError):
            M.validate_tree(deep)

    def test_31_strict_arithmetic(self):
        for bad in (True, 1.0, "1"):
            with self.assertRaises(ValueError):
                M.rational(bad)
            with self.assertRaises(ValueError):
                M.integer(bad, 0, 10)
        for pair in ([True, 1], [1, True], [2, 2], [1, 0], [1, 1 << 5000]):
            with self.assertRaises(ValueError):
                M.unpair(pair)

    def test_32_false_rouche_rejected(self):
        for args in (
            (1, 1, 0, 1),
            (2, 1, 0, 1),
            (0, 0, 0, 1),
            (0, 1, 0, 0),
            (0, 1, -1, 1),
        ):
            with self.assertRaises(ValueError):
                M.rouche_bounds(*args)

    def test_33_domain_and_context_caps(self):
        for p in (True, 191, 513):
            with self.assertRaises(ValueError), M.precision(p):
                pass
        with M.precision():
            for z in (acb(1, 1), acb(32, -1), acb(1000, 1), acb(32, 2)):
                with self.assertRaises(ValueError):
                    M.xi_jet(z)
            with self.assertRaises(ValueError):
                M.xi_jet(acb(32, arb("1/2")), reflected=1)
            for a in (True, 33, 1024):
                with self.assertRaises(ValueError):
                    M.frozen_lambda(a)

    def test_34_payload_not_resealed(self):
        report = copy.deepcopy(self.report)
        report["precision_bits"] = 255
        with self.assertRaises(ValueError):
            M.check_report(report)

    def test_35_resealed_raw_reduced_confusion(self):
        self.mutated(
            lambda r: r["disks"][0].__setitem__("reduced_numerator_upper", [1, 4])
        )

    def test_36_resealed_residue(self):
        self.mutated(
            lambda r: r["disks"][0].__setitem__(
                "native_quotient_residue_at_root",
                {"real": [[0, 1], [0, 1]], "imag": [[0, 1], [0, 1]]},
            )
        )


if __name__ == "__main__":
    unittest.main()
