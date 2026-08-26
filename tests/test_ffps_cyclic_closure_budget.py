"""Focused exact tests for the FFPS cyclic closure-budget packet."""

from __future__ import annotations

import ast
import importlib.util
import json
import subprocess
import sys
import tempfile
import time
import unittest
from fractions import Fraction
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_cyclic_closure_budget.py"
)
OUTPUT_PATH = MODULE_PATH.with_suffix(".json")
NOTE_PATH = MODULE_PATH.with_name("FFPS_CYCLIC_CLOSURE_BUDGET.md")

SPEC = importlib.util.spec_from_file_location("ffps_cyclic_closure_budget", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load FFPS cyclic closure-budget producer")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class FFPSCyclicClosureBudgetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = MODULE.build_fixture()
        cls.disk = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))

    def test_fixture_is_canonical_and_payload_locked(self) -> None:
        self.assertEqual(self.fixture, self.disk)
        payload = dict(self.fixture)
        claimed = payload.pop("payload_sha256")
        self.assertEqual(claimed, MODULE._canonical_sha256(payload))
        self.assertEqual(
            self.fixture["status"],
            "EXACT_CONDITIONAL_CLOSURE_AND_COEFFICIENT_CONE_NO_GO",
        )

    def test_linear_relations_and_kernel_are_exact(self) -> None:
        row = self.fixture["exact_theorems"]["linear_closure_certificate"]
        self.assertEqual(row["measurement_matrix_rows"]["A_additive"], [1, 0, 1])
        self.assertEqual(
            row["measurement_matrix_rows"]["K_complete_nonprincipal"], [0, 1, 1]
        )
        self.assertEqual(row["common_growth_kernel"], [1, 1, -1])
        criterion = row["exact_target_closure_criterion"]
        self.assertEqual(criterion["if_and_only_if"], "w=u+v")
        self.assertIn("u*A+v*K", criterion["row_span_representation"])
        self.assertIn("u+v-w", criterion["necessity_certificate"])
        self.assertTrue(row["exact_relations"]["P_equals_A_minus_K"])
        self.assertIn(
            "coefficient one on each gate", row["sharp_whole_identity_budget"]
        )

    def test_quadratic_atomic_budget_reproduces_checkerboard(self) -> None:
        row = self.fixture["exact_theorems"]["atomic_coefficient_formula"][
            "quadratic_5_13"
        ]
        self.assertEqual(row["principal_weight_c_ell_c_rho"], [7, 4])
        self.assertEqual(row["selected_to_full_channel_weight_ratio"], [21, 65])
        self.assertEqual(row["hard_average_atomic_coefficient_B_C"], [7, 2])
        self.assertEqual(row["selected_trace_atomic_coefficient_B_S"], [7, 4])
        self.assertEqual(row["residual_trace_atomic_coefficient_B_R"], [89, 2])
        self.assertTrue(all(row["atomic_splits"].values()))

    def test_ternary_coefficients_and_atomic_splits_are_exact(self) -> None:
        row = self.fixture["exact_theorems"]["atomic_coefficient_formula"][
            "ternary_7_13"
        ]
        panel = row["panel_budget"]
        self.assertEqual(panel["principal_weight_c_ell_c_rho"], [14, 9])
        self.assertEqual(panel["double_nonprincipal_weight"], [91, 18])
        self.assertEqual(panel["selected_to_full_channel_weight_ratio"], [4, 13])
        self.assertEqual(panel["hard_average_atomic_coefficient_B_C"], [7, 3])
        self.assertEqual(panel["selected_trace_atomic_coefficient_B_S"], [7, 9])
        self.assertEqual(
            panel["complete_nonprincipal_atomic_coefficient_B_K"], [634, 9]
        )
        self.assertEqual(panel["residual_trace_atomic_coefficient_B_R"], [209, 3])
        self.assertEqual(row["individual_lambda_r"], [1, 13])
        self.assertEqual(row["selected_lambda_sum"], [2, 13])
        self.assertEqual(
            row["residual_fraction_on_each_selected_weighted_channel"], [12, 13]
        )

    def test_finite_scalar_witness_lies_in_declared_cone(self) -> None:
        row = self.fixture["exact_theorems"]["atomic_coefficient_formula"][
            "ternary_7_13"
        ]
        witness = row["finite_scalar_no_go_witness_at_D_equals_1"]
        self.assertEqual(witness["C_hard"], [50, 1])
        self.assertEqual(witness["S_selected"], [50, 1])
        self.assertEqual(witness["R_residual"], [-50, 1])
        self.assertEqual(witness["A_additive"], [0, 1])
        self.assertEqual(witness["K_complete_nonprincipal"], [0, 1])
        self.assertEqual(witness["P_principal"], [0, 1])
        self.assertTrue(row["witness_respects_R_lower_atomic_bound"])

    def test_general_panel_budget_identities(self) -> None:
        for primes, order, retained in (
            ((5, 13), 2, 1),
            ((7, 13), 3, 1),
            ((7, 13), 3, 2),
        ):
            row = MODULE.cyclic_panel_budget(primes, order, retained)
            c = Fraction(*row["principal_weight_c_ell_c_rho"])
            bc = Fraction(*row["hard_average_atomic_coefficient_B_C"])
            bs = Fraction(*row["selected_trace_atomic_coefficient_B_S"])
            bk = Fraction(*row["complete_nonprincipal_atomic_coefficient_B_K"])
            br = Fraction(*row["residual_trace_atomic_coefficient_B_R"])
            d0 = row["phase_atomic_coefficient_D0"]
            self.assertEqual(bc + br, d0)
            self.assertEqual(bs + br, bk)
            self.assertEqual(bc, Fraction(order, retained) * c)

    def test_whole_identity_and_single_gate_are_distinguished(self) -> None:
        row = self.fixture["exact_theorems"][
            "whole_identity_localization_and_single_gate"
        ]
        self.assertIn("|P_E|<=D_total+|A|+|K|", row["whole_identity_bound"])
        self.assertEqual(row["single_missing_inequality"]["name"], "CYSEL(k,S)")
        self.assertIn("one-sided", row["single_missing_inequality"]["statement"])
        self.assertIn("C_E>=-(k/t)*D_E", row["automatic_one_sided_budgets"]["C_hard"])
        self.assertIn(
            "S_E>=-(k/t-1)*D_E",
            row["automatic_one_sided_budgets"]["S_selected"],
        )
        self.assertIn("dimension-bearing", row["cauchy_firewall"])

    def test_open_gate_status_is_not_overclaimed(self) -> None:
        row = self.fixture["exact_theorems"][
            "whole_identity_localization_and_single_gate"
        ]
        self.assertIn("open RH-bearing", row["logical_status"])
        self.assertIn("conditional", self.fixture["scope"])
        firewalls = " ".join(self.fixture["firewalls"])
        self.assertIn("open estimates", firewalls)
        self.assertIn("RH and GRH remain unproved", firewalls)

    def test_prerequisite_packet_is_commit_blob_hash_and_payload_locked(self) -> None:
        manifest = {
            row["id"]: row for row in self.fixture["source_contract"]["prerequisites"]
        }
        self.assertEqual(set(manifest), set(MODULE.PREREQUISITE_LOCKS))
        for source_id, lock in MODULE.PREREQUISITE_LOCKS.items():
            raw = lock["path"].read_bytes()
            self.assertEqual(MODULE._lf_sha256(raw), lock["lf_sha256"])
            self.assertEqual(MODULE._git_blob_sha1(raw), lock["git_blob"])
            self.assertEqual(manifest[source_id]["commit"], lock["commit"])
            completed = subprocess.run(
                [
                    "git",
                    "rev-parse",
                    f"{lock['commit']}:{lock['path'].relative_to(ROOT).as_posix()}",
                ],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
                timeout=2.0,
            )
            self.assertEqual(completed.stdout.strip(), lock["git_blob"])
            if lock["kind"] == "json":
                parsed = json.loads(raw.decode("utf-8"))
                self.assertEqual(parsed["schema"], lock["schema"])
                self.assertEqual(parsed["payload_sha256"], lock["payload_sha256"])

    def test_all_live_claim_blobs_resolve(self) -> None:
        manifest = {
            row["claim_id"]: row
            for row in self.fixture["source_contract"]["live_claim_blobs"]
        }
        self.assertEqual(set(manifest), set(MODULE.LIVE_CLAIM_LOCKS))
        for claim_id, lock in MODULE.LIVE_CLAIM_LOCKS.items():
            completed = subprocess.run(
                [
                    "git",
                    "rev-parse",
                    f"{MODULE.LIVE_PR_751_HEAD}:{lock['path']}",
                ],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
                timeout=2.0,
            )
            self.assertEqual(completed.stdout.strip(), lock["git_blob"])
            self.assertEqual(manifest[claim_id]["git_blob"], lock["git_blob"])

    def test_note_records_load_bearing_boundaries(self) -> None:
        note = NOTE_PATH.read_text(encoding="utf-8")
        for marker in (
            "not currently proved inequalities",
            "P=C-S",
            "(C+T,S+T,R-T)",
            "w=u+v",
            "\\lambda_r",
            "B_R",
            "{209\\over3}",
            "CYSEL",
            "whole centered cyclic identity",
            "triangle and Cauchy",
            "RH, or GRH",
        ):
            self.assertIn(marker, note)

    def test_invalid_inputs_and_caps_fail_before_work(self) -> None:
        with self.assertRaises(ValueError):
            MODULE.cyclic_panel_budget((7, 7), 3, 2)
        with self.assertRaisesRegex(ValueError, "2k"):
            MODULE.cyclic_panel_budget((5, 13), 3, 2)
        with self.assertRaises(ValueError):
            MODULE.cyclic_panel_budget((7, 13), 3, 3)
        with self.assertRaisesRegex(ValueError, "cap"):
            MODULE.cyclic_panel_budget((7, 10**12 + 39), 3, 2)
        with self.assertRaises(RuntimeError):
            MODULE.ResourceGuard(
                exact_operations=MODULE.MAX_EXACT_OPERATIONS
            ).operation("overflow")
        with self.assertRaises(RuntimeError):
            MODULE.ResourceGuard(source_files=MODULE.MAX_SOURCE_FILES).source(1)
        with self.assertRaises(RuntimeError):
            MODULE.ResourceGuard(git_objects=MODULE.MAX_GIT_OBJECTS).git_object()
        with self.assertRaises(RuntimeError):
            MODULE.Deadline(started=time.monotonic() - 10).check("expired")

    def test_source_cap_is_pre_read(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            oversized = Path(directory) / "oversized.md"
            oversized.write_bytes(b"x" * (MODULE.MAX_SOURCE_BYTES_EACH + 1))
            lock = {
                "path": oversized,
                "commit": "unused",
                "git_blob": "unused",
                "lf_sha256": "unused",
                "kind": "text",
                "role": "cap regression",
            }
            with (
                mock.patch.object(MODULE, "PREREQUISITE_LOCKS", {"oversized": lock}),
                mock.patch.object(
                    Path,
                    "read_bytes",
                    side_effect=AssertionError("read happened before byte preflight"),
                ),
                self.assertRaisesRegex(RuntimeError, "per-source byte cap"),
            ):
                MODULE._read_prerequisites(MODULE.ResourceGuard(), MODULE.Deadline())

    def test_resource_ledger_is_light_and_algebra_precedes_sources(self) -> None:
        row = self.fixture["resource_contract"]
        self.assertLess(row["actual_exact_operations"], row["maximum_exact_operations"])
        self.assertEqual(
            row["actual_exact_operations"], row["operations_before_sources"]
        )
        self.assertLess(row["actual_source_bytes"], row["maximum_source_bytes_total"])
        self.assertLessEqual(row["actual_git_objects"], row["maximum_git_objects"])
        self.assertFalse(row["heavy_computation"])
        scope = self.fixture["scope"]
        for label in (
            "residue_fields_enumerated",
            "primes_enumerated",
            "conductors_enumerated",
            "characters_enumerated",
            "l_functions_enumerated",
        ):
            self.assertEqual(scope[label], 0)

    def test_no_python_assert_statements_and_optimized_replay(self) -> None:
        tree = ast.parse(MODULE_PATH.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(tree)))
        completed = subprocess.run(
            [sys.executable, "-O", str(MODULE_PATH), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=10.0,
        )
        self.assertIn("PASS_FFPS_CYCLIC_CLOSURE_BUDGET", completed.stdout)

    def test_check_mode_is_read_only_and_detects_drift(self) -> None:
        before = OUTPUT_PATH.read_bytes()
        completed = subprocess.run(
            [sys.executable, str(MODULE_PATH), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=10.0,
        )
        self.assertIn("PASS_FFPS_CYCLIC_CLOSURE_BUDGET", completed.stdout)
        self.assertEqual(before, OUTPUT_PATH.read_bytes())

        with tempfile.TemporaryDirectory() as directory:
            drifted = Path(directory) / "fixture.json"
            drifted.write_text("{}\n", encoding="utf-8")
            with (
                mock.patch.object(MODULE, "OUTPUT_PATH", drifted),
                self.assertRaisesRegex(RuntimeError, "stale"),
            ):
                MODULE.main(["--check"])


if __name__ == "__main__":
    unittest.main()
