"""Exact controls and fresh-reconstruction attacks for the fixed physical frame."""

import copy
import importlib.util
import itertools
import json
import math
import unittest
from fractions import Fraction as Q
from pathlib import Path

from flint import acb, arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/exploratory/native_physical_coercivity_pass4.py"
SPEC = importlib.util.spec_from_file_location("physical_pass4", PATH)
P = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(P)


def q(pair):
    return Q(*pair)


def reseal(report):
    report.pop("payload_sha256", None)
    report["payload_sha256"] = P.digest(P.canonical(report).encode())
    return report


class PhysicalCoercivity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record = P.strict_json(P.FIXTURE.read_bytes())
        ctx.prec = P.BITS

    def test_01_fresh_fixture(self):
        P.check_report(self.record)

    def test_02_fixed_contract(self):
        self.assertEqual(P.NODES, tuple(range(1, 65)))
        self.assertEqual(P.PRIMES, (2, 3, 5))
        self.assertEqual(P.BITS, 1024)
        self.assertEqual(len(self.record["frozen_sources"]), 25)
        self.assertEqual(self.record["contract"]["arithmetic_class"], "MIXED")
        self.assertEqual(
            self.record["contract"]["arithmetic_components"],
            ["CERTIFIED_BALL", "EXACT_RATIONAL", "CERTIFIED_INTEGER_COVERAGE"],
        )
        self.assertEqual(
            self.record["contract"]["measure"],
            "abs(kappahat(t))^2 dt/(2*pi), unchanged",
        )

    def test_03_recorded_powers(self):
        values = self.record["powers"]
        self.assertEqual(
            [
                values[k]
                for k in (
                    "inverse_infinity_upper_2pow",
                    "evaluation_sigma_lower_2negpow",
                    "kappa_modulus_lower_2negpow",
                    "interval_radius_2negpow",
                    "physical_gram_lower_2negpow",
                )
            ],
            [33, 36, 12, 51, 153],
        )

    def test_04_residual_certificate(self):
        error = q(self.record["midpoint_inverse_residual_upper"])
        norm = q(self.record["midpoint_inverse_norm_upper"])
        bound = q(self.record["neumann_inverse_norm_upper"])
        self.assertLess(error, Q(1, 2))
        self.assertEqual(bound, norm / (1 - error))
        self.assertLessEqual(bound, 2**33)
        self.assertLessEqual(max(map(q, self.record["inverse_row_norm_upper"])), 2**33)

    def test_05_modulus_coverage(self):
        self.assertEqual(len(self.record["kappa_modulus_lower"]), 64)
        self.assertGreaterEqual(
            min(map(q, self.record["kappa_modulus_lower"])), Q(1, 2**12)
        )

    def test_06_interval_to_integral_exact(self):
        delta, sigma, eta = Q(1, 2**51), Q(1, 2**36), Q(1, 2**12)
        self.assertLess(delta, Q(1, 4))
        self.assertLessEqual(8 * 2048 * delta, sigma / 2)
        self.assertLessEqual(54 * delta, eta / 2)
        self.assertEqual(delta * sigma * sigma * eta * eta / 64, Q(1, 2**153))

    def test_07_coarse_analytic_constants(self):
        self.assertGreater(sum(Q(3**j, math.factorial(j)) for j in range(8)), 8)
        self.assertGreater(sum(Q(4**j, math.factorial(j)) for j in range(8)), 30)
        self.assertLess(Q(1, 2), Q(9, 16))
        self.assertLess(432, 2**9)
        self.assertEqual(512**2 * 2**9, 2**27)
        self.assertEqual(8 * 2048, 2**14)

    def test_08_horizon_bound(self):
        self.assertEqual(Q(2**17, 2**95), Q(1, 2**78))
        self.assertLess(Q(1, 2**156), Q(1, 2**155))
        self.assertEqual(self.record["powers"]["finite_horizon_threshold_2pow"], 190)

    def test_09_coordinate_congruence(self):
        local = ((1, 0), (-1, 1))
        inverse = ((1, 0), (1, 1))
        for i, j in itertools.product(range(2), repeat=2):
            self.assertEqual(
                sum(local[i][k] * inverse[k][j] for k in range(2)), int(i == j)
            )
        self.assertLess(sum(x * x for row in local for x in row), 4)
        self.assertLess(sum(x * x for row in inverse for x in row), 4)
        self.assertEqual(
            self.record["powers"]["original_monomial_gram_lower_2negpow"], 153 + 12
        )

    def test_10_phase_reflection(self):
        for t in (1, 17, 64):
            positive = P.source_row(t)
            negative = P.source_row(-t)
            self.assertTrue(
                all((a.conjugate() - b).contains(0) for a, b in zip(positive, negative))
            )
            self.assertTrue((P.kappa_hat(t).conjugate() - P.kappa_hat(-t)).contains(0))

    def test_11_exact_zero_moment(self):
        root2 = arb(2).sqrt()
        constants = (8, -8 * (1 + root2), 8 * root2)
        exponents = (-4, 4 * root2, -2)
        value = acb(0)
        for j, (a, b) in enumerate(zip(constants, exponents)):
            value += a * arb(2).log() + 2 * b * (root2 ** (j + 1) - root2**j)
        self.assertTrue(value.contains(0))

    def test_12_tuple_complete_coverage(self):
        value = self.record["tuple_control"]
        primes = (2, 3, 5, 7, 71, 73, 79, 401, 421)
        self.assertEqual(len(primes), len(set(primes)))
        for n in primes:
            self.assertTrue(all(n % d for d in range(2, math.isqrt(n) + 1)))
        self.assertEqual(len(value["left_histories"]), 12)
        self.assertEqual(len(value["right_histories"]), 2)
        signs = list(map(q, value["bilateral_coefficients"]))
        self.assertEqual(signs.count(Q(1, 60)), 12)
        self.assertEqual(signs.count(Q(-1, 60)), 12)
        self.assertEqual(sum(signs), 0)
        self.assertEqual(sum(x * x for x in signs), Q(1, 150))

    def test_13_independent_boolean_definition(self):
        def au(support):
            return int(not support) - sum(
                (-1) ** sum(bits)
                for bits in itertools.product((0, 1), repeat=len(support))
                if math.prod(p for p, bit in zip(support, bits) if bit) <= 64
            )

        for support in ((71, 73, 79), (401, 421)):
            total = 0
            for tags in itertools.product(range(3), repeat=len(support)):
                parts = [
                    tuple(p for p, tag in zip(support, tags) if tag == j)
                    for j in range(3)
                ]
                total += au(parts[0]) * au(parts[1]) * (-1) ** len(parts[2])
            self.assertEqual(total, 0 if len(support) == 3 else 2)

    def test_14_tuple_physical_constants(self):
        value = self.record["tuple_control"]
        self.assertEqual(value["phase_primes"], [71, 401])
        self.assertEqual(value["quadratic_classes"], [-1, -1])
        self.assertEqual(q(value["principal_conductor_weight"]), Q(51504039, 1750))
        self.assertEqual(
            q(value["common_physical_modulus_squared"]), Q(1, 1003434045020153543749890)
        )
        self.assertEqual(value["native_weighted_sum"], "UNDETERMINED")

    def test_15_power_rounding(self):
        for exponent in range(12):
            self.assertEqual(P.upper_power(Q(2**exponent)), exponent)
            self.assertEqual(P.lower_power(Q(1, 2**exponent)), exponent)
        self.assertEqual(P.upper_power(Q(17, 8)), 2)
        self.assertEqual(P.lower_power(Q(3, 8)), 2)
        for function in (P.upper_power, P.lower_power):
            with self.assertRaises(ValueError):
                function(Q(0))

    def test_16_strict_json_guards(self):
        cases = [
            b'{"a":1,"a":2}',
            b'{"a":1.0}',
            b'{"a":NaN}',
            json.dumps(2**4097).encode(),
            json.dumps("a" * 4097).encode(),
            json.dumps([0] * 4097).encode(),
            b"[" * 21 + b"0" + b"]" * 21,
            b" " * 4_000_001,
        ]
        for raw in cases:
            with self.subTest(raw=raw[:30]), self.assertRaises(ValueError):
                P.strict_json(raw)

    def test_17_bad_payload_stops_early(self):
        value = copy.deepcopy(self.record)
        value["payload_sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "payload seal"):
            P.check_report(value)

    def test_18_fully_resealed_hostiles(self):
        mutations = (
            lambda v: v["powers"].__setitem__("physical_gram_lower_2negpow", 1),
            lambda v: v["contract"].__setitem__(
                "measure", "counting measure on 64 nodes"
            ),
            lambda v: v["contract"]["nodes"].__setitem__(0, True),
            lambda v: v["tuple_control"].__setitem__("native_weighted_sum", "ZERO"),
            lambda v: v["frozen_sources"][0].__setitem__("git_blob", "0" * 40),
            lambda v: v["artifact_sha256_lf"].__setitem__(
                P.ARTIFACT_PATHS[1], "0" * 64
            ),
        )
        for mutate in mutations:
            value = copy.deepcopy(self.record)
            mutate(value)
            reseal(value)
            with (
                self.subTest(mutation=mutate),
                self.assertRaisesRegex(ValueError, "fresh source reconstruction"),
            ):
                P.check_report(value)

    def test_19_all_resident_files_no_hidden_controls(self):
        for relative in P.ARTIFACT_PATHS:
            raw = (ROOT / relative).read_bytes()
            self.assertFalse(any(x < 32 and x not in (9, 10, 13) for x in raw))

    def test_20_source_mask_typing_control(self):
        # Formal two-history control only: not an arbitrary native reweighting.
        signs = (Q(1, 60), Q(-1, 60))
        self.assertEqual(sum(signs), 0)
        self.assertNotEqual(sum(a * b for a, b in zip(signs, (1, 2))), 0)
        for mask in (Q(0), Q(1, 3), Q(1)):
            self.assertEqual(sum(mask * x for x in signs), mask * sum(signs))


if __name__ == "__main__":
    unittest.main()
