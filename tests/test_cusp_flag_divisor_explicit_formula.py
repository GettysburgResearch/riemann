"""Independent exact controls; analytic growth and divisor limits are written proofs."""

from __future__ import annotations

import ast
import copy
import hashlib
import importlib.util
import math
import unittest
from fractions import Fraction as Q
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SOURCE = (
    ROOT / "research/l-families/atlas/generalized/cusp_flag_divisor_explicit_formula.py"
)
SPEC = importlib.util.spec_from_file_location("cusp_flag_explicit", SOURCE)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


def decode(raw):
    return {Q(key): Q(value) for key, value in raw.items()}


def valuation(value, prime):
    result = 0
    numerator, denominator = value.numerator, value.denominator
    while numerator % prime == 0:
        result += 1
        numerator //= prime
    while denominator % prime == 0:
        result -= 1
        denominator //= prime
    return result


def independent_log(series, cutoff):
    """Use D_p A=-A D_p B, with additive prime valuations, not Taylor powers."""
    generators = sorted(
        frequency for frequency, value in series.items() if frequency > 1 and value
    )
    monoid, pending = {Q(1)}, [Q(1)]
    while pending:
        current = pending.pop()
        for generator in generators:
            candidate = current * generator
            if candidate <= cutoff and candidate not in monoid:
                monoid.add(candidate)
                pending.append(candidate)
                if len(monoid) > 2048:
                    raise ValueError("independent control cap")
    coefficients = {}
    for frequency in sorted(monoid - {Q(1)}):
        numerator = frequency.numerator
        prime = next(
            (p for p in range(2, math.isqrt(numerator) + 1) if numerator % p == 0),
            numerator,
        )
        divisor = valuation(frequency, prime)
        if divisor <= 0:
            raise ValueError("positive numerator valuation required")
        cross = sum(
            (
                coefficient
                * valuation(frequency / u, prime)
                * coefficients.get(frequency / u, Q(0))
                for u, coefficient in series.items()
                if 1 < u < frequency and frequency / u in monoid
            ),
            Q(0),
        )
        coefficients[frequency] = -series.get(frequency, Q(0)) - cross / divisor
    return {key: value for key, value in coefficients.items() if value}


class ExplicitFormulaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parent = M.authenticated_sources()
        cls.report = M.build_report()

    def test_01_frozen_fixture_exact_reconstruction(self):
        fixture = M.parse_json(M.FIXTURE.read_bytes())
        self.assertEqual(M.canonical(fixture), M.canonical(self.report))
        M.validate_report(fixture)

    def test_02_all_twelve_logs_independent_valuation_recurrence(self):
        for row, control in zip(
            self.parent["frequency_controls"],
            self.report["frequency_controls"],
            strict=True,
        ):
            cutoff = Q(row["cutoff"])
            for source, target in (
                ("bare_F", "minus_log_F_w"),
                ("zeta_times_F", "minus_log_L_w"),
            ):
                with self.subTest(weight=row["weight"], source=source):
                    self.assertEqual(
                        independent_log(decode(row[source]), cutoff),
                        decode(control[target]),
                    )

    def test_03_heldout_collision_log(self):
        source = {Q(1): Q(1), Q(3, 2): Q(2), Q(9, 4): Q(-1)}
        actual, _, _ = M.minus_log_prefix(source, Q(8))
        self.assertEqual(actual, independent_log(source, Q(8)))
        self.assertEqual(actual[Q(9, 4)], Q(3))
        self.assertEqual(M.exp_minus_prefix(actual, Q(8)), source)

    def test_04_heldout_single_atom_and_inclusive_cutoff(self):
        actual, depth, next_word = M.minus_log_prefix({1: 1, 2: 1}, 16)
        self.assertEqual(
            actual, {Q(2): -1, Q(4): Q(1, 2), Q(8): Q(-1, 3), Q(16): Q(1, 4)}
        )
        self.assertEqual((depth, next_word), (4, 32))
        self.assertNotIn(Q(16), M.minus_log_prefix({1: 1, 2: 1}, 15)[0])

    def test_05_constant_only(self):
        self.assertEqual(M.minus_log_prefix({1: 1}, 1), ({}, 0, None))
        self.assertEqual(M.exp_minus_prefix({}, 1), {Q(1): Q(1)})

    def test_06_all_exponential_inverse_prefixes(self):
        for row, control in zip(
            self.parent["frequency_controls"],
            self.report["frequency_controls"],
            strict=True,
        ):
            for source, target in (
                ("bare_F", "minus_log_F_w"),
                ("zeta_times_F", "minus_log_L_w"),
            ):
                self.assertEqual(
                    M.exp_minus_prefix(decode(control[target]), Q(row["cutoff"])),
                    decode(row[source]),
                )

    def test_07_fractional_atoms_and_exceptional_weights(self):
        for row, control in zip(
            self.parent["frequency_controls"],
            self.report["frequency_controls"],
            strict=True,
        ):
            d, k = row["dimension"], row["weight"]
            target = Q((d + 1) ** 2, d - (k in (124, 248)))
            self.assertEqual(Q(control["fractional_frequency"]), target)
            self.assertEqual(
                Q(control["fractional_b_w"]), -row["first_fractional_coefficient_w"]
            )
            smaller = [
                Q(key)
                for key, value in row["zeta_times_F"].items()
                if value and 1 < Q(key) < target
            ]
            self.assertTrue(all(rho.denominator == 1 for rho in smaller))
        first = self.report["frequency_controls"][0]
        self.assertEqual(first["fractional_frequency"], "9/2")
        self.assertEqual(first["fractional_b_w"], "88203653222400")

    def test_08_coordinate_shift_and_lambda_not_discarded(self):
        for control in self.report["frequency_controls"]:
            old = decode(control["minus_log_L_w"])
            new = decode(control["minus_log_L_in_s"])
            self.assertEqual(
                new, {rho: b * rho ** (1 - control["weight"]) for rho, b in old.items()}
            )
            target = Q(control["fractional_frequency"])
            self.assertEqual(
                Q(control["fractional_PN_rational_multiplier_s"]), new[target]
            )
            self.assertEqual(
                control["PN_mass_contract"],
                "mass at t=log(rho) is log(rho) times minus_log_L_in_s[rho]",
            )

    def test_09_independent_zeta_prime_power_correction(self):
        for k in (24, 124, 248):
            expected = {
                Q(4): -Q(2 ** (2 * k - 2)),
                Q(9): -Q(3 ** (2 * k - 2)),
                Q(16): -Q(2 ** (4 * k - 4), 2),
                Q(25): -Q(5 ** (2 * k - 2)),
            }
            self.assertEqual(M.zeta_minus_log(k, 28), expected)
        for row in self.report["frequency_controls"]:
            difference = decode(row["minus_log_L_w"])
            for frequency, coefficient in decode(row["minus_log_F_w"]).items():
                difference[frequency] = difference.get(frequency, 0) - coefficient
            self.assertEqual(
                {key: value for key, value in difference.items() if value},
                decode(row["zeta_minus_log_difference"]),
            )

    def test_10_both_atomic_signs(self):
        for row in self.report["frequency_controls"]:
            values = decode(row["minus_log_L_w"])
            self.assertLess(values[min(values)], 0)
            self.assertGreater(values[Q(row["fractional_frequency"])], 0)
            self.assertEqual(row["actual_zero_or_pole_samples"], 0)

    def test_11_gamma_ladder_overlap_independent_enumeration(self):
        for k in (2, 24, 124, 248, 302):
            control = M.completion_control(k)
            left = [Q(-n) for n in range(k + 1)]
            right = [Q(-(k - 1) - n) for n in range(k + 1)]
            for text, order in control["A_gamma_signed_orders"].items():
                s = Q(text)
                self.assertEqual(order, -left.count(s) - right.count(s))
            self.assertEqual(
                control["kernel_contract"], "-(1+exp(-(k-1)*t))/(1-exp(-t)) for t>0"
            )

    def test_12_native_endpoints_are_net_cancellations(self):
        for row in self.report["completion_controls"]:
            self.assertEqual(row["source_Q_endpoint_orders"], {"0": -1, "1": -1})
            self.assertEqual(row["L_in_s_endpoint_orders"], {"0": 0, "1": -1})
            self.assertFalse(row["unknown_actual_determinant_divisor_supplied"])

    def test_13_theta_amgm_exact_algebra(self):
        for x in (Q(1), Q(3, 2), Q(7)):
            for y in (Q(1), Q(5, 3), Q(8)):
                row = M.theta_jensen_control(x, y, 1)
                self.assertEqual(
                    Q(row["theta_gap_divided_by_pi"]), (2 * y - x) ** 2 / (2 * y)
                )
                self.assertGreaterEqual(Q(row["theta_gap_divided_by_pi"]), 0)

    def test_14_jensen_shifted_center_geometry(self):
        for r in (Q(1), Q(3, 2), Q(8)):
            row = M.theta_jensen_control(1, 1, r)
            self.assertEqual(row["Jensen_center"], 2)
            self.assertEqual(Q(row["inner_radius"]), r + 2)
            self.assertEqual(Q(row["outer_radius"]), 2 * (r + 2))
            self.assertEqual(Q(row["global_outer_radius"]), 2 * r + 6)
            self.assertFalse(row["numerical_theta_Gamma_or_Jensen_value"])

    def test_15_mellin_substitution_integer_calibration(self):
        for row in self.report["Mellin_integer_controls"]:
            r = row["R"]
            factorial = 1
            for j in range(1, 2 * r + 2):
                factorial *= j
            self.assertEqual(row["power_of_c_in_denominator"], 2 * r + 2)
            self.assertEqual(
                row["integral_0_infinity_u_to_R_exp_minus_c_sqrt_u_multiplier"],
                2 * factorial,
            )

    def test_16_strict_rational_types_and_flags(self):
        for value in (True, False, 1.0, "1", None):
            with self.subTest(value=value), self.assertRaises(ValueError):
                M.rational(value)
        with self.assertRaises(ValueError):
            M.rational(1, internal=1)
        with self.assertRaises(ValueError):
            M.checked_series({1: 1}, 2, constant=1)

    def test_17_rational_text_canonical_and_bits(self):
        for value in ("01", "2/2", "+1", "1.0", "1e2", "1/0", " 1", "--1", "1/-2"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                M.qtext(value)
        self.assertEqual(M.qtext("9/2"), Q(9, 2))
        for value in (2**32, Q(1, 2**32)):
            with self.assertRaises(ValueError):
                M.rational(value)
        with self.assertRaises(ValueError):
            M.rational(2**4096, internal=True)

    def test_18_series_domain_and_normalization(self):
        for series in (
            {},
            {1: 2},
            {1: True},
            {1: 1, 0: 2},
            {1: 1, Q(1, 2): 3},
            {1: 1, 29: 1},
        ):
            with self.subTest(series=series), self.assertRaises(ValueError):
                M.minus_log_prefix(series, 28)
        for series in ({1: 1}, {0: 2}, {Q(1, 2): 3}):
            with self.assertRaises(ValueError):
                M.exp_minus_prefix(series, 28)

    def test_19_cutoffs_weights_and_calibration_caps(self):
        for cutoff in (True, 0, 29, 1.0):
            with self.assertRaises(ValueError):
                M.minus_log_prefix({1: 1}, cutoff)
        for weight in (True, 1, 303, 24.0):
            with self.assertRaises(ValueError):
                M.completion_control(weight)
            with self.assertRaises(ValueError):
                M.zeta_minus_log(weight, 28)
        for args in ((0, 1, 1), (1, 33, 1), (1, 1, True)):
            with self.assertRaises(ValueError):
                M.theta_jensen_control(*args)

    def test_20_word_limit_fails_closed(self):
        with self.assertRaisesRegex(ValueError, "word degree cap"):
            M.minus_log_prefix({1: 1, Q(101, 100): 1}, 2)
        with self.assertRaises(ValueError):
            M.word_degree(1, 28)
        self.assertEqual(M.word_degree(2, 16), (4, Q(32)))

    def test_21_support_and_precharged_work_caps(self):
        oversize = {Q(1) + Q(i, 1024): Q(1) for i in range(513)}
        with self.assertRaisesRegex(ValueError, "support cap"):
            M.minus_log_prefix(oversize, 2)
        budget = M.Budget(1)
        with self.assertRaisesRegex(ValueError, "before expansion"):
            M.product({1: 1, 2: 1}, {1: 1}, 2, budget)
        self.assertEqual(budget.used, 0)
        with self.assertRaises(ValueError):
            M.minus_log_prefix({1: 1, 2: 1}, 16, M.Budget(1))

    def test_22_budget_types_and_internal_product_guards(self):
        for value in (True, 0, M.MAX_WORK + 1, 1.0):
            with self.assertRaises(ValueError):
                M.Budget(value)
        with self.assertRaises(ValueError):
            M.Budget().spend(True)
        for left in ({True: 1}, {1: True}, {0: 1}, {Q(1, 2): 1}, []):
            with self.assertRaises(ValueError):
                M.product(left, {1: 1}, 2, M.Budget())
        with self.assertRaises(ValueError):
            M.accumulate({}, 0, 1)
        with self.assertRaises(ValueError):
            M.accumulate([], 1, 1)

    def test_23_source_row_semantic_guards(self):
        mutations = (
            ("dimension", True),
            ("weight", True),
            ("residual", True),
            ("weight", 25),
            ("residual", 2),
            ("complete_tail_and_word_coverage_by_CF9", 1),
            ("first_fractional_frequency", "4"),
            ("first_fractional_coefficient_w", True),
        )
        for field, value in mutations:
            row = copy.deepcopy(self.parent["frequency_controls"][0])
            row[field] = value
            with self.subTest(field=field, value=value), self.assertRaises(ValueError):
                M.frequency_control(row)

    def test_24_source_map_canonical_integer_and_coverage_guards(self):
        for raw in ({"1": True}, {"01": 1}, {"1": "1"}, {"1": 1, "4/2": 2}):
            with self.assertRaises(ValueError):
                M.decode_parent_map(raw, 12)
        row = copy.deepcopy(self.parent["frequency_controls"][0])
        row["bare_F"]["9/2"] += 1
        with self.assertRaisesRegex(ValueError, "target collision"):
            M.frequency_control(row)

    def test_25_six_sources_and_four_current_artifacts(self):
        self.assertEqual(len(M.BINDINGS), 6)
        self.assertEqual(len(self.report["artifact_sha256_lf"]), 4)
        for path, digest in self.report["artifact_sha256_lf"].items():
            raw = (
                (ROOT / path).read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            )
            self.assertEqual(hashlib.sha256(raw).hexdigest(), digest)
        self.assertEqual(
            M.canonical(self.report["frozen_sources"]), M.canonical(M.BINDINGS)
        )

    def test_26_manifest_strict_contract_tampering(self):
        for field, value in (
            ("authoring_base", "0" * 40),
            ("schema", "other"),
            ("extra", True),
        ):
            manifest = M.manifest_expected()
            manifest[field] = value
            with self.assertRaisesRegex(ValueError, "typed manifest"):
                M.authenticated_sources(manifest)
        manifest = M.manifest_expected()
        manifest["external_context"][0]["remote_bytes_authenticated"] = 0
        with self.assertRaises(ValueError):
            M.authenticated_sources(manifest)

    def test_27_manifest_copy_not_global_alias(self):
        manifest = M.manifest_expected()
        manifest["frozen_sources"][0]["commit"] = "0" * 40
        manifest["external_context"][0]["role"] = "altered"
        self.assertNotEqual(M.BINDINGS[0]["commit"], "0" * 40)
        self.assertNotEqual(M.EXTERNAL[0]["role"], "altered")
        self.assertEqual(M.parse_json(M.MANIFEST.read_bytes()), M.manifest_expected())

    def test_28_source_primitive_hash_and_size_rejection(self):
        with (
            patch.object(M.subprocess, "check_output", side_effect=[b"1", b"x"]),
            self.assertRaisesRegex(ValueError, "primitive identity"),
        ):
            M.authenticated_sources()
        with patch.object(
            M.subprocess, "check_output", return_value=str(M.MAX_BYTES + 1).encode()
        ) as mocked:
            with self.assertRaisesRegex(ValueError, "primitive byte cap"):
                M.authenticated_sources()
            self.assertEqual(mocked.call_count, 1)

    def test_29_lf_normalization(self):
        self.assertEqual(M.lf_sha(b"a\nb\n"), M.lf_sha(b"a\r\nb\r\n"))
        self.assertEqual(M.lf_sha(b"a\nb\n"), M.lf_sha(b"a\rb\r"))
        with self.assertRaises(ValueError):
            M.normalized("bytes required")
        with self.assertRaises(ValueError):
            M.normalized(b"x" * (M.MAX_BYTES + 1))

    def test_30_json_duplicates_floats_nonfinite(self):
        for raw in (
            b'{"x":1,"x":2}',
            b'{"x":NaN}',
            b'{"x":Infinity}',
            b'{"x":-Infinity}',
            b'{"x":1.0}',
            b'{"x":1e2}',
            b"{",
        ):
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                M.parse_json(raw)

    def test_31_json_structural_resource_caps(self):
        for value in ([0] * 1025, {"x": "a" * 4097}, {1: "key"}, 2**4096):
            with self.assertRaises(ValueError):
                M.canonical(value)
        with self.assertRaises(ValueError):
            M.parse_json(b"[" * 30 + b"0" + b"]" * 30)
        with self.assertRaises(ValueError):
            M.parse_json(b" " * (M.MAX_BYTES + 1))

    def test_32_digest_tamper_rejection(self):
        report = copy.deepcopy(self.report)
        report["payload_sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "payload digest"):
            M.validate_report(report)
        with self.assertRaises(ValueError):
            M.seal(report)

    def test_33_resealed_payload_semantic_tamper_rejection(self):
        variants = []
        for key, value in (
            ("schema", "other"),
            ("arithmetic_class", "EXACT"),
            ("arithmetic_components", ["EXACT_RATIONAL"]),
            ("rounding_contract", "floating"),
            ("status", "APPROVED"),
        ):
            payload = copy.deepcopy(self.report)
            payload.pop("payload_sha256")
            payload[key] = value
            variants.append(payload)
        payload = copy.deepcopy(self.report)
        payload.pop("payload_sha256")
        payload["caps"]["work"] = True
        variants.append(payload)
        payload = copy.deepcopy(self.report)
        payload.pop("payload_sha256")
        payload["scope"]["actual_zero_or_pole_samples"] = False
        variants.append(payload)
        with patch.object(M, "build_report", return_value=self.report):
            for payload in variants:
                with (
                    self.subTest(payload=payload["schema"]),
                    self.assertRaisesRegex(ValueError, "typed reconstruction"),
                ):
                    M.validate_report(M.seal(payload))

    def test_34_canonical_arithmetic_and_coverage(self):
        self.assertEqual(self.report["arithmetic_class"], "MIXED")
        self.assertEqual(
            self.report["arithmetic_components"],
            ["CERTIFIED_INTEGER_COVERAGE", "EXACT_RATIONAL"],
        )
        self.assertIn("no rounding", self.report["rounding_contract"])
        self.assertIn("log(rho) is symbolic", self.report["rounding_contract"])
        coverage = self.report["coverage"]
        self.assertEqual(coverage["complete_parent_prefixes"], 6)
        self.assertEqual(coverage["F_and_L_log_prefixes"], 12)
        self.assertIs(coverage["parent_q_word_producer_rerun"], False)
        self.assertLessEqual(coverage["charged_work"], M.MAX_WORK)

    def test_35_scope_firewalls(self):
        scope = self.report["scope"]
        for key in (
            "L_divisor_assigned_same_strip",
            "pointwise_zero_exponential_series_asserted",
            "origin_delta_discarded_for_tests_meeting_zero",
            "finite_zero_census_substituted",
            "numerical_growth_constants_or_Jensen_anchors",
            "analytic_proof_machine_certified",
            "positive_Weil_RH_GRH_or_novelty_claim",
        ):
            self.assertIs(scope[key], False)
        self.assertIs(scope["Q_net_divisor_finite_vertical_strip"], True)
        self.assertEqual(scope["test_space"], "C_c^infinity((0,infinity))")

    def test_36_no_assert_or_float_or_analytic_numeric_calls(self):
        tree = ast.parse(SOURCE.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(tree)))
        self.assertFalse(
            any(
                isinstance(node, ast.Constant) and type(node.value) is float
                for node in ast.walk(tree)
            )
        )
        prohibited = {"exp", "log", "gamma", "lgamma", "sin", "cos", "sqrt"}
        self.assertFalse(
            any(
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr in prohibited
                for node in ast.walk(tree)
            )
        )


if __name__ == "__main__":
    unittest.main()
