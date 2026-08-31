"""Exact controls and scoped numerical-scout contracts; not analytic certification."""

import copy
import importlib.util
import json
import unittest
from fractions import Fraction
from pathlib import Path
from unittest import mock

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


MODULE = load(
    "xi_global_exact", ROOT / "research/exploratory/xi_global_odd_order_saddle.py"
)
SCOUT = load("xi_global_scout", MODULE.SCOUT)


class GlobalXiSaddleTests(unittest.TestCase):
    def test_primitive_authentication(self):
        row = MODULE.authenticate_sources()
        self.assertEqual(row["source_count"], 4)
        self.assertFalse(row["ancestral_code_executed_by_exact_producer"])
        self.assertTrue(row["ancestral_code_executed_by_separate_scout"])

    def test_complete_symbolic_phase(self):
        row = MODULE.symbolic_phase_controls()
        self.assertEqual(len(row["complete_symbolic_identities"]), 10)
        self.assertEqual(row["kernel_amplitude_branches"], 2)

    def test_rational_theta_bounds(self):
        row = MODULE.theta_bound_controls()
        self.assertLess(Fraction(row["theta_derivative_majorant"]), 3)
        self.assertEqual(Fraction(row["B_upper"]), Fraction(1024, 961))

    def test_literal_current_heldouts_both_sides(self):
        for k in (3, 17, 73, 127):
            for q in (Fraction(11, 3), Fraction(101, 7)):
                for d in (0, q / 2, q, 2 * q, 100):
                    row = MODULE.current_factor_control(k, q, d)
                    r = (q - d) / (q + d)
                    self.assertEqual(Fraction(row["minus_bracket"]), 1 - r**k)
                    self.assertEqual(Fraction(row["plus_bracket"]), 1 + r**k)

    def test_current_endpoint(self):
        self.assertEqual(MODULE.current_factor_control(127, 2, 0)["minus_bracket"], "0")
        self.assertEqual(MODULE.current_factor_control(127, 2, 2)["plus_bracket"], "1")

    def test_exact_types_and_bits(self):
        for bad in (True, False, 1.0, "2", None, float("nan")):
            with self.assertRaises(TypeError):
                MODULE.exact(bad)
        for bad in (2**64, Fraction(1, 2**64)):
            with self.assertRaises(ValueError):
                MODULE.exact(bad)

    def test_current_order_caps(self):
        for bad in (True, 0, 2, 129, 3.0, Fraction(3), "3"):
            with self.assertRaises(ValueError):
                MODULE.current_factor_control(bad, 2, 1)
        for q, d in ((1, 0), (2, -1)):
            with self.assertRaises(ValueError):
                MODULE.current_factor_control(3, q, d)

    def test_normal_response_independent_recurrence(self):
        expected = Fraction(1)
        for row in MODULE.gaussian_response_coefficients():
            self.assertEqual(Fraction(row["coefficient"]), expected)
            expected /= 2 * (row["j"] + 1)

    def test_normal_moment_caps(self):
        for bad in (True, -1, 13, 1.0, "3"):
            with self.assertRaises(ValueError):
                MODULE.gaussian_response_coefficients(bad)

    def test_manifest_mutations_rejected(self):
        row = MODULE.expected_manifest()
        mutants = []
        for key in ("normalization", "scout_firewall", "authoring_base"):
            m = copy.deepcopy(row)
            m[key] = "wrong"
            mutants.append(m)
        m = copy.deepcopy(row)
        m["sources"].pop()
        mutants.append(m)
        for m in mutants:
            with self.assertRaises(ValueError):
                MODULE.authenticate_sources(m)

    def test_source_bytes_replayed(self):
        with (
            mock.patch.object(MODULE.subprocess, "check_output", return_value=b"wrong"),
            self.assertRaises(ValueError),
        ):
            MODULE.authenticate_sources()

    def test_report_rebuild(self):
        row = json.loads(MODULE.FIXTURE.read_text(encoding="utf-8"))
        MODULE.validate_report(row)
        self.assertEqual(row["current_grid_rows"], 2048)

    def test_report_mutations_rejected(self):
        row = MODULE.build_report()
        for key in row["scopes"]:
            m = copy.deepcopy(row)
            m["scopes"][key] = True
            with self.assertRaises(ValueError):
                MODULE.validate_report(m)
        m = copy.deepcopy(row)
        m["normal_response_coefficients"][2]["coefficient"] = "1/4"
        with self.assertRaises(ValueError):
            MODULE.validate_report(m)

    def test_scout_authenticates_before_import(self):
        _, digest = SCOUT.authenticated_parent()
        self.assertEqual(digest, MODULE.SOURCE_ROWS[-1][-1])
        with (
            mock.patch.object(SCOUT.Path, "read_bytes", return_value=b"wrong"),
            self.assertRaises(ValueError),
        ):
            SCOUT.authenticated_parent()

    def test_scout_caps_before_computation(self):
        for args in (
            (True, "2"),
            (1, "2"),
            (33, "2"),
            (2, "nan"),
            (2, "inf"),
            (2, "0.5"),
            (2, "9"),
            (2, "2", "0"),
            (2, "2", "1000001"),
        ):
            with self.assertRaises(ValueError):
                SCOUT.run_case(*args)
        for kwargs in (
            {"dps": 39},
            {"dps": 121},
            {"dps": True},
            {"radius": 15},
            {"radius": 49},
            {"radius": True},
        ):
            with self.assertRaises(ValueError):
                SCOUT.run_case(2, "2", **kwargs)

    def test_scout_saddle_all_branches(self):
        # Ordinary high precision controls, explicitly not interval certificates.
        with mp.workdps(60):
            q = mp.mpf(2)
            kl = 2 * mp.pi * q * (mp.exp(2 * q) - 1)
            kr = 2 * q * (mp.pi * (mp.exp(2 * q) + 1) - mp.mpf("4.5"))
            parent, _ = SCOUT.authenticated_parent()
            corner_k = parent.nearest_odd((kl + kr) / 2)
            for k, wanted in (
                (3, "balanced"),
                (corner_k, "corner"),
                (100001, "unbalanced"),
            ):
                a, j, branch = SCOUT.global_saddle(q, k)
                self.assertEqual(branch, wanted)
                self.assertGreater(j, 0)
                if branch == "corner":
                    self.assertEqual(a, q)
                if branch == "balanced":
                    self.assertLess(
                        abs(a - SCOUT.old_balanced_center(q, k)), mp.mpf("1e-55")
                    )
                if branch == "unbalanced":
                    self.assertLess(a, SCOUT.old_balanced_center(q, k))

    def test_scout_beyond_old_bracket_cap(self):
        with mp.workdps(70):
            q = mp.mpf(32)
            parent, _ = SCOUT.authenticated_parent()
            k = parent.nearest_odd(q * mp.exp(8 * q))
            a, _, branch = SCOUT.global_saddle(q, k)
            self.assertEqual(branch, "unbalanced")
            self.assertGreater(a, 128)
            self.assertGreater(SCOUT.old_balanced_center(q, k), a)

    def test_scout_order_contract(self):
        for k in (True, 0, 2, -1, 2**1025 + 1):
            with self.assertRaises(ValueError):
                SCOUT.global_saddle(mp.mpf(2), k)

    def test_scout_campaign_odd_integer_transport(self):
        data = json.loads(MODULE.SCOUT_RESULTS.read_text(encoding="utf-8"))
        self.assertEqual(MODULE.validate_scout_campaign(data)["case_count"], 10)
        row = data["cases"][7]
        self.assertEqual(row["K"], "8420083094517158086385")
        for bad in (
            8420083094517158086385,
            8.420083094517158e21,
            True,
            "08420083094517158086385",
            "8420083094517158086384",
            "8.420083094517158e21",
        ):
            mutant = copy.deepcopy(data)
            mutant["cases"][7]["K"] = bad
            with self.assertRaises(ValueError):
                MODULE.validate_scout_campaign(mutant)

    def test_scout_campaign_case_source_scope_contract(self):
        data = json.loads(MODULE.SCOUT_RESULTS.read_text(encoding="utf-8"))
        for key, value in (
            ("xi", True),
            ("gamma", "5"),
            ("producer_sha256_lf", "0" * 64),
            ("certified", True),
            ("requested_decimal_digits", 51),
            ("quadrature_upper", "48.0"),
        ):
            mutant = copy.deepcopy(data)
            mutant["cases"][7][key] = value
            with self.assertRaises(ValueError):
                MODULE.validate_scout_campaign(mutant)
        mutant = copy.deepcopy(data)
        mutant["cases"].pop()
        with self.assertRaises(ValueError):
            MODULE.validate_scout_campaign(mutant)

    def test_scout_above_binary64_integer_limit_replay(self):
        row = SCOUT.run_case(12, "4", "1", dps=40, radius=16)
        self.assertIs(type(row["K"]), str)
        self.assertEqual(row["K"], "8420083094517158086385")
        self.assertEqual(int(row["K"]) % 2, 1)


if __name__ == "__main__":
    unittest.main()
