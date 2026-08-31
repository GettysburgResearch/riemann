"""Hostile finite algebra and source-boundary tests; no numerical analytic proof."""

import ast
import copy
import importlib.util
import itertools
import math
import subprocess
import sys
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = (
    ROOT
    / "research/l-families/atlas/function_field/ffps_canonical_boolean_principal_diagonal.py"
)
SPEC = importlib.util.spec_from_file_location("canonical_boolean_diagonal", PRODUCER)
m = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = m
SPEC.loader.exec_module(m)

ATOM = ((5, 31), (3, 137), (37,), (43,), (47,))
HELD_OUT = ((2, 101), (7, 71), (37,), (43,), (47,))


class CanonicalBooleanDiagonalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = m.build_report()

    def test_fixture_exact_and_sealed(self):
        m.check_fixture(m.read_json_bytes(m.FIXTURE.read_bytes()), self.report)
        self.assertEqual(self.report["schema"], m.SCHEMA)

    def test_unit_core_is_zero_for_all_control_cutoffs(self):
        for cutoff in (1, 2, 32, m.MAX_CUTOFF):
            self.assertEqual(m.a_coefficient((), cutoff), 0)
            self.assertEqual(m.boolean_coefficients((), cutoff), (0, 0, Fraction()))

    def test_independent_direct_subset_convolution(self):
        # Independent bit-subset multiplication, rather than producer's ternary allocations.
        primes = (2, 5, 11, 13)
        full = (1 << len(primes)) - 1
        for cutoff in (1, 7, 22, 143, 1430):
            a = {}
            for mask in range(full + 1):
                total = 0
                sub = mask
                while True:
                    product = math.prod(primes[j] for j in range(4) if sub & (1 << j))
                    if product <= cutoff:
                        total += (-1) ** sub.bit_count()
                    if sub == 0:
                        break
                    sub = (sub - 1) & mask
                a[mask] = int(mask == 0) - total
            original = 0
            for left in range(full + 1):
                available = full ^ left
                right = available
                while True:
                    rest = available ^ right
                    original += a[left] * a[right] * (-1) ** rest.bit_count()
                    if right == 0:
                        break
                    right = (right - 1) & available
            self.assertEqual(m.boolean_coefficients(primes, cutoff)[0], original)

    def test_beta_integral_reconstructs_binomial(self):
        for depth in range(m.MAX_SUPPORT + 1):
            integral = 2 * (Fraction(1, depth + 1) - Fraction(1, depth + 2))
            self.assertEqual(integral, Fraction(1, math.comb(depth + 2, 2)))

    def test_source_coefficient_controls(self):
        for values in ((37, 43), (37, 47)):
            original, expanded, canonical = m.boolean_coefficients(values, 32)
            self.assertEqual((original, expanded, canonical), (2, 2, Fraction(1, 3)))
            self.assertEqual(canonical / 2, Fraction(1, 6))

    def test_exhausted_cutoff_controls_and_majorant(self):
        rows = self.report["boolean"]["rows"]
        self.assertGreater(len(rows), 50)
        for row in rows:
            self.assertEqual(row["original"], row["expanded"])
            self.assertLessEqual(
                abs(Fraction(row["canonical"])), 3 ** len(row["support"])
            )

    def test_boolean_inputs_fail_closed(self):
        for value in (True, False, 0, -1, 1.0, "1", m.MAX_CUTOFF + 1):
            with self.subTest(value=value), self.assertRaises(ValueError):
                m.boolean_coefficients((2, 3), value)

    def test_prime_support_inputs_fail_closed(self):
        for values in (
            [2, 3],
            (3, 2),
            (2, 2),
            (4,),
            (67,),
            (True,),
            (2.0,),
            (1009,),
            (2, 3, 5, 7, 11, 13, 17),
        ):
            with self.subTest(values=values), self.assertRaises(ValueError):
                m.boolean_coefficients(values, 1)

    def test_principal_constant_sharp_including_two(self):
        self.assertEqual(m.principal_constant(2, 3), 6)
        self.assertEqual(m.principal_constant(3, 5), 3)
        self.assertGreater(m.principal_constant(2, 3), 4)
        for p, q in itertools.combinations((2, 3, 5, 7, 11, 13, 17), 2):
            self.assertLessEqual(m.principal_constant(p, q), 6)
        for pair in ((2, 2), (67, 3), (True, 3)):
            with self.assertRaises(ValueError):
                m.principal_constant(*pair)

    def test_original_principal_and_source_dual_normalization(self):
        for atom in (ATOM, HELD_OUT):
            row = m.atom_control(atom, 32, 2**30)
            p, q, g, c, d = row["arithmetic_tuple"]
            ell, rho = row["least_primes"]
            square = Fraction(1, 81 * g**4 * c**2 * d**2 * p * q)
            original = g**2 * ell * rho * m.principal_constant(ell, rho) * square
            self.assertEqual(
                Fraction(row["original_principal_squared_amplitude"]), original
            )
            self.assertEqual(
                row["original_principal_squared_amplitude"],
                row["source_dual_principal_squared_amplitude"],
            )
            self.assertLessEqual(original, Fraction(row["pointwise_majorant"]))

    def test_phase_uses_full_physical_cores_and_cancels_common_g(self):
        row = m.atom_control(ATOM, 32, 2**30)
        p, q, g, c, d = row["arithmetic_tuple"]
        self.assertEqual(row["phase"], f"exp(i*t*log({p * c * c}/{q * d * d}))")
        self.assertNotEqual(Fraction(p * c**2, q * d**2), Fraction(p, q))
        self.assertEqual(
            Fraction(p * (g * c) ** 2, q * (g * d) ** 2), Fraction(p * c * c, q * d * d)
        )

    def test_principal_is_not_complete_additive_weight(self):
        row = m.atom_control(ATOM, 32, 2**30)
        ell, rho = row["least_primes"]
        complete = (ell - 1) * (rho - 1)
        self.assertGreater(complete, 1000 * m.principal_constant(ell, rho))

    def test_masks_exact_rational_and_bounded(self):
        base = Fraction(
            m.atom_control(ATOM, 32, 2**30)["original_principal_squared_amplitude"]
        )
        for mask, expected in (
            ((0, 0), Fraction()),
            ((0, 1), Fraction(1)),
            ((Fraction(3, 5), Fraction(4, 5)), Fraction(1)),
            ((Fraction(1, 2), 0), Fraction(1, 4)),
        ):
            row = m.atom_control(ATOM, 32, 2**30, mask)
            self.assertEqual(
                Fraction(row["original_principal_squared_amplitude"]), base * expected
            )
        for mask in ([1, 0], (True, 0), (1.0, 0), (1, 1), (Fraction(1, 2**65), 0)):
            with self.subTest(mask=mask), self.assertRaises(ValueError):
                m.mask_norm(mask)

    def test_chart_guards(self):
        bad_atoms = (
            ((5,), ATOM[1], ATOM[2], ATOM[3], ATOM[4]),
            (ATOM[0], ATOM[1], ATOM[2], (), ATOM[4]),
            (ATOM[0], ATOM[1], (37, 43), (43,), (47,)),
            (ATOM[0], (5, 137), ATOM[2], ATOM[3], ATOM[4]),
            (ATOM[0], ATOM[1], (67,), ATOM[3], ATOM[4]),
        )
        for atom in bad_atoms:
            with self.subTest(atom=atom), self.assertRaises(ValueError):
                m.atom_control(atom, 32, 2**30)
        for horizon in (1, True, 1.0, m.MAX_Y + 1):
            with self.assertRaises(ValueError):
                m.atom_control(ATOM, 32, horizon)

    def test_exact_tuple_multiplicity_is_rejected(self):
        with self.assertRaises(ValueError):
            m.panel_control((ATOM, ATOM), 32, 2**30)
        for atoms in ((), [ATOM], (ATOM,) * (m.MAX_ATOMS + 1)):
            with self.assertRaises(ValueError):
                m.panel_control(atoms, 32, 2**30)

    def test_kernel_exact_coefficients(self):
        self.assertEqual(m.kernel_norm()["exact_coefficients"], [-288, 0, 384, 128])

        # Independent expansion in x=sqrt(y): integral 2(A+Bx)^2 dx/x.
        def multiply(x, y):
            return (x[0] * y[0] + 2 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])

        def add(x, y):
            return tuple(a + b for a, b in zip(x, y))

        def scale(x, factor):
            return tuple(factor * a for a in x)

        total_constant, total_log2 = (0, 0), (0, 0)
        endpoints = ((1, 0), (0, 1), (2, 0), (0, 2))
        ab = (((8, 0), (-4, 0)), ((-8, -8), (0, 4)), ((0, 8), (-2, 0)))
        for i, (a, b) in enumerate(ab):
            lo, hi = endpoints[i : i + 2]
            linear = scale(multiply(multiply(a, b), add(hi, scale(lo, -1))), 4)
            quadratic = multiply(
                multiply(b, b), add(multiply(hi, hi), scale(multiply(lo, lo), -1))
            )
            total_constant = add(total_constant, add(linear, quadratic))
            total_log2 = add(total_log2, multiply(a, a))
        self.assertEqual((total_constant, total_log2), ((-288, 0), (384, 128)))

    def test_divisor_coefficients_independent_word_enumeration(self):
        limit, order = 12, 3
        direct = [0] * (limit + 1)
        for factors in itertools.product(range(1, limit + 1), repeat=order):
            product = math.prod(factors)
            if product <= limit:
                direct[product] += 1
        self.assertEqual(m.divisor_convolution(limit, order), direct)
        self.assertEqual(
            direct[1:], [m.divisor_count(n, order) for n in range(1, limit + 1)]
        )

    def test_squarefree_divisor_identity_and_convolution(self):
        for order in (1, 2, 9, 81):
            for n in (1, 2, 6, 30):
                self.assertEqual(
                    m.divisor_count(n, order), order ** len(m.factor_exponents(n))
                )
            convolution = m.divisor_convolution(32, order)
            self.assertEqual(
                convolution[1:], [m.divisor_count(n, order) for n in range(1, 33)]
            )

    def test_finite_majorants_and_harmonic_exponents(self):
        report = self.report["divisor_majorants"]
        self.assertLessEqual(
            Fraction(report["squarefree_weighted_sum"]),
            Fraction(report["divisor_weighted_sum"]),
        )
        self.assertLessEqual(
            Fraction(report["divisor_weighted_sum"]),
            Fraction(report["harmonic_power_upper"]),
        )
        self.assertEqual(sum(report["harmonic_components"]), 22)
        self.assertEqual(report["g_exponent"], 81)
        for row in report["finite_euler_rows"]:
            self.assertLessEqual(Fraction(row["left"]), Fraction(row["right"]))

    def test_sum_and_order_caps(self):
        for n in (True, 0, -1, 1.0, m.MAX_SUM + 1):
            with self.assertRaises(ValueError):
                m.harmonic(n)
            with self.assertRaises(ValueError):
                m.majorant_control(n)
        for order in (True, 0, 1.0, m.MAX_ORDER + 1):
            with self.assertRaises(ValueError):
                m.divisor_convolution(4, order)

    def test_all_primitive_source_identities_and_roles(self):
        sources = self.report["sources"]["frozen_sources"]
        self.assertEqual(len(sources), 12)
        self.assertEqual(sum(row["kind"] == "scientific_source" for row in sources), 11)
        self.assertEqual(len({row["id"] for row in sources}), 12)
        self.assertEqual({len(row["sha256_lf"]) for row in sources}, {64})
        self.assertEqual({len(row["git_blob"]) for row in sources}, {40})

    def test_literal_kernel_and_canonical_source_markers(self):
        by_id = {row["id"]: row for row in m.SOURCE_ROWS}
        for source_id, markers in (
            ("kernel", ("L-102880.2", r"8-4\sqrt y", r"-8(1+\sqrt2)+4\sqrt2\sqrt y")),
            (
                "canonical",
                ("L-106133.11", r"\binom{k}{2}", "pair of distinct labelled copies"),
            ),
            ("principal", ("L-106121.9", "COMPLETE-MOMENT ATOMIC CLAIM RETRACTED")),
            (
                "target",
                ("T-106140.9", "carrier, endpoint-colour", "Neither gate is proved"),
            ),
        ):
            row = by_id[source_id]
            raw = subprocess.check_output(
                ["git", "show", row["commit"] + ":" + row["path"]],
                cwd=ROOT,
                timeout=10,
            )
            m.authenticate_raw(row, row["git_blob"], raw)
            for marker in markers:
                self.assertIn(marker, raw.decode("utf-8"))

    def test_source_manifest_changes_rejected(self):
        expected = {"schema": m.SOURCE_SCHEMA, "sources": copy.deepcopy(m.SOURCE_ROWS)}
        m.validate_manifest(expected)
        for key in ("commit", "path", "git_blob", "sha256_lf", "kind", "role"):
            changed = copy.deepcopy(expected)
            changed["sources"][0][key] = "forged"
            with self.subTest(key=key), self.assertRaises(ValueError):
                m.validate_manifest(changed)
        for replacement in (True, 1, [], {"schema": "wrong", "sources": m.SOURCE_ROWS}):
            with self.assertRaises(ValueError):
                m.validate_manifest(replacement)

    def test_raw_blob_authentication_rejects_tampering(self):
        row = m.SOURCE_ROWS[0]
        raw = subprocess.check_output(
            ["git", "show", row["commit"] + ":" + row["path"]], cwd=ROOT, timeout=10
        )
        m.authenticate_raw(row, row["git_blob"], raw)
        with self.assertRaises(ValueError):
            m.authenticate_raw(row, row["git_blob"], raw + b"x")
        with self.assertRaises(ValueError):
            m.authenticate_raw(row, "0" * 40, raw)
        with self.assertRaises(ValueError):
            m.authenticate_raw({**row, "kind": "untyped"}, row["git_blob"], raw)

    def test_lf_normalization_and_byte_caps(self):
        self.assertEqual(m.digest(b"a\nb\n"), m.digest(b"a\r\nb\r\n"))
        self.assertEqual(m.digest(b"a\nb\n"), m.digest(b"a\rb\r"))
        for raw in ("text", b"x" * (m.MAX_BYTES + 1)):
            with self.assertRaises(ValueError):
                m.digest(raw)

    def test_json_duplicate_nonfinite_and_shape_guards(self):
        for raw in (b'{"a":1,"a":2}', b'{"a":NaN}', b'{"a":Infinity}', b"{"):
            with self.assertRaises(ValueError):
                m.read_json_bytes(raw)
        with self.assertRaises(ValueError):
            m.read_json_bytes(b" " * (m.MAX_BYTES + 1))

    def test_fixture_digest_schema_type_and_key_guards(self):
        for key, value in (
            ("schema", "wrong"),
            ("payload_sha256", "0" * 64),
            ("arithmetic_class", "EXACT"),
            ("extra", 1),
        ):
            changed = copy.deepcopy(self.report)
            changed[key] = value
            with self.subTest(key=key), self.assertRaises(ValueError):
                m.check_fixture(changed, self.report)
        changed = copy.deepcopy(self.report)
        changed.pop("payload_sha256")
        changed["scope"]["ordinary_prime_67_free_chart_only"] = 1
        with self.assertRaises(ValueError):
            m.check_fixture(m.seal(changed), self.report)
        for actual, expected in ((True, 1), (1.0, 1), ([1], [True])):
            with self.assertRaises(ValueError):
                m.exact_match(actual, expected)

    def test_artifact_hashes_are_current_and_typed(self):
        artifacts = self.report["sources"]["current_artifacts"]
        self.assertEqual(len(artifacts), 4)
        for path, record in artifacts.items():
            self.assertEqual(record["kind"], "current_artifact")
            self.assertEqual(record["sha256_lf"], m.digest((ROOT / path).read_bytes()))
        payload = copy.deepcopy(self.report)
        payload.pop("payload_sha256")
        first = next(iter(payload["sources"]["current_artifacts"].values()))
        first["sha256_lf"] = "0" * 64
        with self.assertRaises(ValueError):
            m.check_fixture(m.seal(payload), self.report)

    def test_no_assert_or_float_in_producer(self):
        tree = ast.parse(PRODUCER.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(tree)))
        self.assertFalse(
            any(
                isinstance(node, ast.Constant) and type(node.value) is float
                for node in ast.walk(tree)
            )
        )

    def test_scope_firewalls_are_binding(self):
        scope = self.report["scope"]
        self.assertTrue(scope["one_atom_per_exact_arithmetic_tuple"])
        self.assertTrue(scope["ordinary_prime_67_free_chart_only"])
        self.assertFalse(scope["native_masked_bilateral_identity_proved"])
        self.assertFalse(scope["full_principal_moment_difference_paid"])
        self.assertFalse(scope["native_sign_or_RH_consequence"])
        self.assertEqual(scope["unpaid_term"], "P_nat-P_B")
        note = m.NOTE.read_text(encoding="utf-8")
        for marker in (
            "CBPD13",
            "FIRST difference is unpaid",
            "67 completely",
            "ONE atom",
        ):
            self.assertIn(marker, note)


if __name__ == "__main__":
    unittest.main()
