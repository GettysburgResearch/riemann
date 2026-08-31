"""Exact source and hostile controls for live FFPS residue collisions."""

from __future__ import annotations

import ast
import copy
import importlib.util
import json
import subprocess
import sys
import unittest
from fractions import Fraction
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_live_shared_fibre_collisions.py"
)
SPEC = importlib.util.spec_from_file_location(
    "ffps_live_shared_fibre_collisions", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load live FFPS collision producer")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class LiveSharedFibreCollisionTests(unittest.TestCase):
    def test_exact_source_locks_resolve(self) -> None:
        self.assertEqual(len(MODULE.check_source_locks()), 11)

    def test_source_manifest_rejects_missing_duplicate_and_changed_rows(self) -> None:
        payload = json.loads(MODULE.SOURCE_LOCK_PATH.read_text(encoding="utf-8"))
        MODULE.validate_source_manifest(payload)
        for mutation in ("missing", "duplicate", "blob", "schema"):
            damaged = copy.deepcopy(payload)
            if mutation == "missing":
                damaged["sources"].pop()
            elif mutation == "duplicate":
                damaged["sources"][-1] = copy.deepcopy(damaged["sources"][0])
            elif mutation == "blob":
                damaged["sources"][0]["git_blob"] = "0" * 40
            else:
                damaged["schema"] = "counterfeit"
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                MODULE.validate_source_manifest(damaged)

    def test_frozen_cutoffs_are_exact_integer_sixth_roots(self) -> None:
        expected = ((2**24, 16), (2**30, 32), (2**33, 45), (2**54, 512))
        for horizon, cutoff in expected:
            with self.subTest(horizon=horizon):
                self.assertEqual(MODULE.floor_sixth_root(horizon), cutoff)
                self.assertLessEqual(cutoff**6, horizon)
                self.assertGreater((cutoff + 1) ** 6, horizon)
        for horizon in (1, 63, 64, 65, 728, 729, 730, 2**60):
            cutoff = MODULE.floor_sixth_root(horizon)
            self.assertLessEqual(cutoff**6, horizon)
            self.assertGreater((cutoff + 1) ** 6, horizon)

    def test_cutoff_rejects_boolean_float_zero_and_over_budget(self) -> None:
        for horizon in (True, 0, -1, 1.0, "64", 2**60 + 1):
            with self.subTest(horizon=horizon), self.assertRaises(ValueError):
                MODULE.floor_sixth_root(horizon)

    def test_boolean_a_u_values_are_exact(self) -> None:
        self.assertEqual(MODULE.boolean_a_u((), 16), 0)
        self.assertEqual(MODULE.boolean_a_u((13,), 16), 0)
        self.assertEqual(MODULE.boolean_a_u((17,), 16), -1)
        self.assertEqual(MODULE.boolean_a_u((17, 43), 16), -1)
        self.assertEqual(MODULE.boolean_a_u((11, 13), 512), 0)
        self.assertEqual(MODULE.boolean_a_u((11, 13, 17), 512), -1)
        self.assertEqual(MODULE.boolean_a_u((11, 13, 17, 19), 512), -3)

    def test_two_prime_histories_are_two_distinct_equal_coefficients(self) -> None:
        rows = MODULE.balanced_representations((17, 43), 16)
        self.assertEqual(len(rows), 2)
        self.assertEqual([row["coefficient"] for row in rows], [1, 1])
        self.assertEqual(rows[0]["first"], rows[1]["second"])
        self.assertEqual(rows[0]["second"], rows[1]["first"])
        self.assertEqual(rows[0]["tail"], [])
        self.assertEqual(MODULE.balanced_vaughan_coefficient((17, 43), 16), 2)

    def test_vaughan_identity_replays_independently_on_cutoff_controls(self) -> None:
        supports = (
            (),
            (3,),
            (3, 5),
            (5, 7, 11),
            (11, 13, 17, 19),
            (11, 13, 17, 19, 521),
        )
        for support in supports:
            for cutoff in (1, 5, 16, 32, 143, 512):
                with self.subTest(support=support, cutoff=cutoff):
                    direct = sum(
                        row["coefficient"]
                        for row in MODULE.balanced_representations(support, cutoff)
                    )
                    self.assertEqual(
                        direct, MODULE.balanced_vaughan_coefficient(support, cutoff)
                    )

    def test_support_validation_is_fail_closed(self) -> None:
        bad_supports = (
            [3, 5],
            (3, 3),
            (3, 9),
            (True, 5),
            (3.0, 5),
            (5003,),
            (2, 3, 5, 7, 11, 13, 17),
        )
        for support in bad_supports:
            with self.subTest(support=support), self.assertRaises(ValueError):
                MODULE.balanced_representations(support, 16)
        for cutoff in (0, -1, True, 16.0, 5001):
            with self.subTest(cutoff=cutoff), self.assertRaises(ValueError):
                MODULE.boolean_a_u((17, 43), cutoff)

    def test_small_live_history_calibration_has_no_native_variance(self) -> None:
        report = MODULE.history_calibration()
        self.assertEqual(report["physical_pair"]["N"], 3206166)
        self.assertEqual(report["physical_pair"]["M"], 22344035)
        self.assertEqual(report["physical_pair"]["cell"], [42, 2])
        self.assertEqual(report["bilateral_history_coefficient_ratios"], [1, 1, 1, 1])
        self.assertEqual(
            report["coefficient_statistics"]["kernel_projection_energy"], "0"
        )

    def test_arithmetic_control_survives_single_side_aggregation(self) -> None:
        report = MODULE.arithmetic_panel(**MODULE.ARITHMETIC_CONTROL)
        self.assertEqual(report["cell"], [3, 36])
        self.assertEqual((report["sigma"], report["tau"]), (1, 1))
        self.assertEqual(report["left_owner_difference_over_rho"], 1)
        self.assertEqual(report["right_owner_difference_over_ell"], 2)
        records = report["arithmetic_atoms_after_one_sided_equal_product_aggregation"]
        self.assertEqual({row["N"] for row in records}, {392348555, 511318762})
        self.assertEqual({row["M"] for row in records}, {1242913731, 1502988137})
        self.assertEqual(len({(row["N"], row["M"]) for row in records}), 4)
        self.assertEqual(report["same_cell_arithmetic_atom_lower_bound"], 4)
        self.assertEqual(report["same_cell_literal_history_atom_lower_bound"], 16)
        self.assertEqual(
            report["kernel_dimension_lower_bound_after_history_aggregation"], 3
        )
        self.assertEqual(
            report["kernel_dimension_lower_bound_at_literal_history_resolution"], 15
        )
        self.assertEqual(report["aggregate_equal_pair_share_per_side"], "1/3")

    def test_independent_held_out_conductors_and_nonperfect_cutoff(self) -> None:
        report = MODULE.arithmetic_panel(**MODULE.ARITHMETIC_HELD_OUT)
        self.assertEqual(report["frozen_cutoff"], 45)
        self.assertEqual((report["ell"], report["rho"]), (59, 61))
        self.assertEqual(report["cell"], [5, 44])
        self.assertEqual(report["same_cell_arithmetic_atom_lower_bound"], 4)
        self.assertEqual(
            report["native_coefficient_family_nonfactorization"], "NOT_PROVED"
        )

    def test_both_owner_panels_allow_reversed_orientation(self) -> None:
        for panel in (MODULE.ARITHMETIC_CONTROL, MODULE.ARITHMETIC_HELD_OUT):
            reversed_panel = dict(panel)
            reversed_panel.update(
                name=panel["name"] + "_reversed",
                ell=panel["rho"],
                rho=panel["ell"],
                left_owners=panel["right_owners"],
                right_owners=panel["left_owners"],
            )
            report = MODULE.arithmetic_panel(**reversed_panel)
            self.assertEqual(report["same_cell_arithmetic_atom_lower_bound"], 4)
            for row in report[
                "arithmetic_atoms_after_one_sided_equal_product_aggregation"
            ]:
                self.assertEqual(
                    row["cell"],
                    [
                        (-(report["rho"] ** 2) * row["Q"]) % report["ell"],
                        (report["ell"] ** 2 * row["P"]) % report["rho"],
                    ],
                )

    def test_owner_panel_rejects_overlap_wrong_congruence_and_wrong_horizon(
        self,
    ) -> None:
        mutations = (
            {"left_owners": ((5, 31), (2, 103))},
            {"left_owners": ((5, 31), (5, 101))},
            {"left_owners": ((37, 31), (2, 101))},
            {"right_owners": ((3, 67), (7, 71))},
            {"left_owners": ((5.0, 31), (2, 101))},
            {"g": 31},
            {"g": 39},
            {"ell": 47},
            {"ell": 2},
            {"rho": 49},
            {"horizon": 2**20},
            {"left_owners": ((5, 31),)},
        )
        for mutation in mutations:
            damaged = {**MODULE.ARITHMETIC_CONTROL, **mutation}
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                MODULE.arithmetic_panel(**damaged)

    def test_same_cell_operator_has_exact_kernel_and_signed_rayleigh_controls(
        self,
    ) -> None:
        for ell, rho in ((43, 47), (59, 61)):
            diagonal = MODULE.atomic_diagonal(ell, rho)
            self.assertEqual(
                MODULE.same_cell_wick(ell, rho, (1, -1) + (0,) * 14), -2 * diagonal
            )
            self.assertEqual(
                MODULE.same_cell_wick(ell, rho, (1,) * 16), 16 * 15 * diagonal
            )
            self.assertEqual(MODULE.same_cell_wick(ell, rho, (1,)), 0)

    def test_signed_history_pattern_and_fixed_native_variance(self) -> None:
        report = MODULE.signed_history_panel()
        self.assertEqual(report["physical_pair"]["g"], 46189)
        self.assertEqual(report["physical_pair"]["cell"], [230, 205])
        self.assertEqual(
            report["left_source"]["coefficient_histogram"], {"-1": 8, "3": 2}
        )
        self.assertEqual(report["right_source"]["balanced_coefficient"], -2)
        self.assertEqual(
            report["bilateral_coefficient_histogram"], {"-3": 32, "1": 64, "9": 4}
        )
        self.assertEqual(report["coefficient_statistics"]["sum"], "4")
        self.assertEqual(
            report["coefficient_statistics"]["literal_diagonal_energy"], "676"
        )
        self.assertEqual(
            report["coefficient_statistics"]["kernel_projection_energy"], "16896/25"
        )
        self.assertEqual(report["wick_value_as_multiple_of_d"], -660)
        self.assertEqual(report["common_bilateral_owner_share"], "1/441")

    def test_internal_zero_sum_subset_is_not_promoted_to_native_freedom(self) -> None:
        report = MODULE.signed_history_panel()
        subset = report["internal_zero_sum_subset"]
        self.assertEqual(subset["native_coefficient_ratios"], [-3, 1, 1, 1])
        self.assertEqual(subset["statistics"]["sum"], "0")
        self.assertEqual(subset["statistics"]["literal_diagonal_energy"], "12")
        self.assertIn("NOT_AN_ADMISSIBLE_FULL_NATIVE_INPUT_PAIR", subset["status"])
        self.assertEqual(
            report["native_coefficient_family_nonfactorization"], "NOT_PROVED"
        )

    def test_exact_vector_and_resource_guards(self) -> None:
        report = MODULE.vector_statistics((Fraction(1, 2), Fraction(-1, 2)))
        self.assertEqual(report["kernel_projection_energy"], "1/2")
        for vector in ((), (1,) * 101, (True, -1), (1.0, -1), [1, -1]):
            with self.subTest(vector=vector), self.assertRaises(ValueError):
                MODULE.vector_statistics(vector)
        for ell, rho in ((2, 43), (43, 43), (43, 49), (True, 47), (43.0, 47)):
            with self.subTest(pair=(ell, rho)), self.assertRaises(ValueError):
                MODULE.atomic_diagonal(ell, rho)
        with self.assertRaises(ValueError):
            MODULE.physical_cell(43, 47, 47, 35)

    def test_canonical_output_matches_replay_and_retains_open_gates(self) -> None:
        expected = json.loads(MODULE.FIXTURE_PATH.read_text(encoding="utf-8"))
        actual = MODULE.build_fixture(authenticate=False)
        self.assertEqual(expected, actual)
        self.assertIn(
            "native coefficient-family nonfactorization", actual["not_proved"]
        )
        self.assertIn("RH or GRH", actual["not_proved"])
        self.assertFalse(actual["resource_boundary"]["live_source_family_enumerated"])
        self.assertFalse(
            actual["resource_boundary"]["conductor_family_searched_by_replay"]
        )

    def test_arithmetic_taxonomy_and_content_hashes(self) -> None:
        actual = MODULE.build_fixture(authenticate=False)
        self.assertEqual(actual["arithmetic_class"], "MIXED")
        self.assertEqual(
            actual["arithmetic_components"],
            ["CERTIFIED_INTEGER_COVERAGE", "EXACT_RATIONAL"],
        )
        hashes = actual["artifact_source_sha256_lf_normalized"]
        self.assertEqual(len(hashes), 4)
        for relative, digest in hashes.items():
            data = (ROOT / relative).read_bytes().replace(b"\r\n", b"\n")
            self.assertEqual(digest, sha256(data).hexdigest())

    def test_note_contract_and_no_float_or_assert_proof_checks(self) -> None:
        MODULE.check_note_contract()
        syntax = ast.parse(MODULE_PATH.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(syntax)))
        self.assertFalse(
            any(
                isinstance(node, ast.Constant) and isinstance(node.value, float)
                for node in ast.walk(syntax)
            )
        )

    def test_cli_check_normal_and_optimized(self) -> None:
        for optimized in (False, True):
            command = [sys.executable, "-B"]
            if optimized:
                command.append("-O")
            command.extend((str(MODULE_PATH), "--check"))
            completed = subprocess.run(
                command,
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
                timeout=30,
            )
            self.assertIn("PASS_FFPS_LIVE_SHARED_FIBRE_COLLISIONS", completed.stdout)


if __name__ == "__main__":
    unittest.main()
