"""Exact source-weighted signed aggregation and hostile scope controls."""

from __future__ import annotations

import ast
import copy
import importlib.util
import json
import subprocess
import sys
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = (
    ROOT
    / "research/l-families/atlas/function_field/ffps_signed_history_recombination.py"
)
SPEC = importlib.util.spec_from_file_location("ffps_signed_history_recombination", PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load signed-history producer")
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


def group(label, cell, coefficients):
    return {"label": label, "cell": cell, "coefficients": coefficients}


class SignedHistoryRecombinationTests(unittest.TestCase):
    def test_original_and_rescaled_native_weights_agree(self):
        report = module.signed_history_report()
        self.assertEqual(report["matrix_replay"]["group_coefficient_sums"], ["4"])
        self.assertEqual(report["matrix_replay"]["literal_group_energies"], ["676"])
        self.assertEqual(report["matrix_replay"]["group_energy_corrections"], ["-660"])
        weights = module.channel_weights(1031, 521)
        norm = Fraction(report["rescaled_common_norm_prefactor"])
        for channel, weight in weights.items():
            self.assertEqual(
                Fraction(
                    report[
                        "physical_correction_prefactors_multiplying_abs_gamma_squared"
                    ][channel]
                ),
                -660 * weight * norm,
            )

    def test_hundred_history_negativity_is_entirely_a_correction(self):
        report = module.signed_history_report()["matrix_replay"]
        for values in report["Hermitian_polynomial_channels"].values():
            self.assertEqual(values["grouped"], [["0"]])
            self.assertEqual(values["literal"][0][0], values["correction_diagonal"][0])

    def test_all_three_channel_corrections_keep_their_signs(self):
        groups = (group("a", (1, 1), (-3, 1, 1, 1)), group("b", (4, 2), (1, 1)))
        report = module.matrices(5, 7, groups)
        self.assertEqual(report["deltas"], [Fraction(-12), Fraction(2)])
        for i in range(2):
            self.assertEqual(
                report["channels"]["additive"]["correction_diagonal"][i]
                - report["channels"]["Kummer"]["correction_diagonal"][i],
                report["channels"]["principal"]["correction_diagonal"][i],
            )

    def test_same_cell_distinct_arithmetic_groups_are_not_deleted(self):
        groups = (group("a", (1, 1), (1, 1)), group("b", (1, 1), (1, 1)))
        report = module.matrices(5, 7, groups)
        d = module.channel_weights(5, 7)["additive"]
        self.assertEqual(
            report["channels"]["additive"]["grouped"], [[0, 4 * d], [4 * d, 0]]
        )

    def test_equal_tuple_distinct_retained_labels_are_not_paid(self):
        groups = (
            group("same_tuple_colour_0", (1, 1), (1,)),
            group("same_tuple_colour_1", (1, 1), (1,)),
        )
        report = module.matrices(5, 7, groups)
        p = module.channel_weights(5, 7)["principal"]
        self.assertEqual(report["deltas"], [0, 0])
        self.assertEqual(report["channels"]["principal"]["grouped"], [[0, p], [p, 0]])
        self.assertEqual(
            sum(sum(row) for row in report["channels"]["principal"]["grouped"]),
            2 * p,
        )

    def test_distinct_cells_preserve_centered_negative_background(self):
        groups = (
            group("a", (1, 1), (1, -2)),
            group("b", (4, 2), (3,)),
            group("c", (1, 4), (1, 1)),
        )
        report = module.matrices(5, 7, groups)
        self.assertEqual(module.incidence_kernel(5, 7, (1, 1), (4, 2)), Fraction(1, 35))
        self.assertEqual(
            module.incidence_kernel(5, 7, (1, 1), (1, 4)), Fraction(-4, 35)
        )
        self.assertEqual(
            report["channels"]["additive"]["grouped"][0][2], Fraction(8, 35)
        )

    def test_singleton_has_no_history_correction(self):
        report = module.matrices(5, 7, (group("one", (1, 1), (Fraction(-3, 2),)),))
        self.assertEqual(report["deltas"], [0])
        for values in report["channels"].values():
            self.assertEqual(values["literal"], [[0]])

    def test_representation_bounds_include_zero_aggregate(self):
        groups = (
            group("zero_sum", (1, 1), (1, -1)),
            group("aligned", (4, 2), (1, 1, 1)),
        )
        report = module.matrices(5, 7, groups)
        self.assertEqual(report["deltas"], [-2, 6])
        self.assertEqual(report["energies"], [2, 3])

    def test_fixed_weight_ratio_has_conductor_tax(self):
        for ell, rho in ((43, 47), (59, 61), (1031, 521)):
            weights = module.channel_weights(ell, rho)
            expected = Fraction((ell - 1) ** 2 * (rho - 1) ** 2, (ell + 1) * (rho + 1))
            self.assertEqual(weights["additive"] / weights["principal"], expected)
            self.assertGreater(expected, 1)

    def test_both_live_owner_panels_retain_opposite_corners(self):
        for panel in (
            module.collision.ARITHMETIC_CONTROL,
            module.collision.ARITHMETIC_HELD_OUT,
        ):
            report = module.owner_panel_report(panel)
            self.assertEqual(
                report["matrix_replay"]["group_energy_corrections"], ["12"] * 4
            )
            for corner in report["opposite_corner_pairs"]:
                self.assertEqual(corner["distinct_owner_label_count"], 8)
                self.assertEqual(corner["history_correction_on_this_cross_term"], "0")
                self.assertNotEqual(corner["additive_cross_coefficient"], "0")

    def test_reversed_panel_retains_exact_weights(self):
        panel = dict(module.collision.ARITHMETIC_CONTROL)
        panel.update(
            name="reverse",
            ell=47,
            rho=43,
            left_owners=panel["right_owners"],
            right_owners=panel["left_owners"],
        )
        report = module.owner_panel_report(panel)
        self.assertEqual(
            report["matrix_replay"]["group_energy_corrections"], ["12"] * 4
        )

    def test_input_type_shape_and_resource_guards(self):
        base = group("a", (1, 1), (1, 1))
        bad = [
            (),
            [base],
            (base, base),
            (group("a", (0, 1), (1,)),),
            (group("a", (1, 1), (True,)),),
            (group("a", (1, 1), (1.0,)),),
            (group("a", (1, 1), (1 << 65,)),),
            (group("a", (1, 1), (1,) * 101),),
            tuple(group(str(i), (1, 1), (1,)) for i in range(17)),
            (group("a", (1, 1), (1,) * 60), group("b", (1, 1), (1,) * 60)),
        ]
        for groups in bad:
            with self.subTest(groups=groups), self.assertRaises(ValueError):
                module.matrices(5, 7, groups)
        for ell, rho in ((5, 5), (2, 7), (9, 7), (True, 7), (5.0, 7)):
            with self.assertRaises(ValueError):
                module.channel_weights(ell, rho)

    def test_quadratic_source_fibre_is_not_silently_mixed(self):
        with self.assertRaises(ValueError):
            module.matrices(5, 7, (group("a", (1, 1), (1,)), group("b", (2, 1), (1,))))

    def test_fixture_check_is_type_strict_and_rejects_omitted_ledger(self):
        with self.assertRaises(ValueError):
            module.check_fixture({"count": True}, {"count": 1})
        expected = module.encode_matrix_report(
            module.matrices(5, 7, (group("a", (1, 1), (1, 1)),))
        )
        damaged = copy.deepcopy(expected)
        damaged["Hermitian_polynomial_channels"]["principal"]["correction_diagonal"] = [
            "0"
        ]
        with self.assertRaises(ValueError):
            module.check_fixture(damaged, expected)

    def test_source_locks_and_checkout_stable_hashes(self):
        lock = module.source_locks()
        self.assertEqual(len(lock["frozen_sources"]), 9)
        self.assertEqual(lock["upstream_collision_primitive_blobs_reauthenticated"], 11)
        self.assertEqual(module.digest(b"a\r\nb\r\n"), module.digest(b"a\nb\n"))
        self.assertEqual(len(lock["current_source_sha256_lf"]), 4)

    def test_no_float_or_assert_proof_checks(self):
        syntax = ast.parse(PATH.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(syntax)))
        self.assertFalse(
            any(
                isinstance(node, ast.Constant) and type(node.value) is float
                for node in ast.walk(syntax)
            )
        )

    def test_canonical_replay_and_quantifier_firewalls(self):
        report = module.build_report()
        module.check_fixture(
            json.loads(module.FIXTURE.read_text(encoding="utf-8")), report
        )
        self.assertIn(
            "no extra pointwise bound or maximal/supremum",
            report["principal_transfer"]["quantifiers"],
        )
        self.assertFalse(report["finite_coverage"]["complete_native_fibre_enumerated"])
        self.assertFalse(
            report["finite_coverage"]["analytic_imports_reproved_by_computation"]
        )
        self.assertIn(
            "native coefficient-family nonfactorization remains open",
            report["firewalls"],
        )

    def test_cli_normal_and_optimized(self):
        for optimized in (False, True):
            command = [sys.executable, "-B"]
            if optimized:
                command.append("-O")
            command.extend((str(PATH), "--check"))
            completed = subprocess.run(
                command,
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
                timeout=40,
            )
            self.assertIn("PASS_FFPS_SIGNED_HISTORY_RECOMBINATION", completed.stdout)


if __name__ == "__main__":
    unittest.main()
