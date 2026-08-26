"""Focused exact tests for the FFPS cyclic physical-source gate."""

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
    / "ffps_cyclic_source_realization_gate.py"
)
OUTPUT_PATH = MODULE_PATH.with_suffix(".json")
NOTE_PATH = MODULE_PATH.with_name("FFPS_CYCLIC_SOURCE_REALIZATION_GATE.md")

SPEC = importlib.util.spec_from_file_location(
    "ffps_cyclic_source_realization_gate", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load FFPS cyclic source-realization producer")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class FFPSCyclicSourceRealizationGateTests(unittest.TestCase):
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
            "EXACT_FIXED_FIBRE_CYCLIC_SOURCE_GATE_WITH_WICK_FIREWALL",
        )

    def test_ternary_raw_core_character_fails_physical_collapse(self) -> None:
        row = self.fixture["exact_theorems"]["exact_2k_root_orientation"][
            "raw_core_failure"
        ]
        self.assertEqual(row["prime"], 7)
        self.assertEqual(row["character_order"], 3)
        self.assertEqual(row["first"]["physical"], 1)
        self.assertEqual(row["second"]["physical"], 1)
        self.assertEqual(row["first"]["raw_core_exponent_mod_3"], 0)
        self.assertEqual(row["second"]["raw_core_exponent_mod_3"], 1)
        self.assertEqual(row["first"]["oriented_physical_exponent_mod_3"], 0)
        self.assertEqual(row["second"]["oriented_physical_exponent_mod_3"], 0)

    def test_2k_root_orientation_is_physical_and_balanced(self) -> None:
        guard = MODULE.ResourceGuard()
        for prime in (7, 13):
            for owner in MODULE.square_coset(prime, 1):
                for core in range(1, prime):
                    physical = owner * core * core % prime
                    self.assertEqual(
                        MODULE.source_cyclic_exponent(owner, core, 1, prime, 3, guard),
                        MODULE.cyclic_oriented_exponent(physical, 1, prime, 3, guard),
                    )
        audits = self.fixture["exact_theorems"]["exact_2k_root_orientation"][
            "finite_invariance_audits"
        ]
        self.assertEqual(
            {(row["prime"], row["sector_representative"]) for row in audits},
            {(7, 1), (7, 3), (13, 1), (13, 2)},
        )
        self.assertTrue(all(row["oriented_fibres_are_singletons"] for row in audits))
        self.assertTrue(
            all(
                row["raw_core_character_mixes_on_some_physical_fibre"] for row in audits
            )
        )
        self.assertTrue(
            all(
                len(set(row["orientation_distribution"].values())) == 1
                for row in audits
            )
        )

    def test_sector_gauge_is_one_constant_cyclic_rotation(self) -> None:
        audit = MODULE.gauge_audit(13, 3, 1, 2, MODULE.ResourceGuard())
        self.assertEqual(audit["new_representative"], 4)
        self.assertEqual(audit["constant_exponent_shift"], 2)
        for physical in MODULE.square_coset(13, 1):
            old = MODULE.cyclic_oriented_exponent(physical, 1, 13, 3)
            new = MODULE.cyclic_oriented_exponent(physical, 4, 13, 3)
            self.assertEqual((new - old) % 3, 2)

    def test_live_mode_identification_is_double_nonprincipal(self) -> None:
        row = self.fixture["exact_theorems"]["live_L_106120_mode_identification"]
        self.assertIn("chi(Q)*eta(d)*psi(P)*theta(c)", row["product"])
        self.assertIn("(eta^r,theta^r)", row["fourier_modes"])
        self.assertTrue(row["all_modes_double_nonprincipal"])
        self.assertTrue(row["hard_support_not_supplied_by_WCKUM"])

    def test_ternary_hard_full_soft_ordering_is_exact(self) -> None:
        row = self.fixture["exact_theorems"]["hard_versus_soft_metric"]
        self.assertEqual(row["quotient_value_counts"], {"0": 6, "1": 6, "2": 6})
        self.assertEqual(row["support_size"], 12)
        self.assertEqual(row["restricted_gram_denominator"], 588)
        self.assertEqual(row["restricted_row_sum"], [49, 1])
        self.assertEqual(row["sharp_uniform_retained_weight"], [3, 2])
        hard = Fraction(*row["sharp_restricted_leverage"])
        complete = Fraction(*row["complete_tensor_leverage"])
        soft = Fraction(*row["same_zero_extended_weight_in_complete_inverse_metric"])
        self.assertEqual(hard, Fraction(27, 49))
        self.assertEqual(complete, Fraction(9, 14))
        self.assertEqual(soft, Fraction(135, 182))
        self.assertLess(hard, complete)
        self.assertLess(complete, soft)

    def test_universal_atomic_threshold_theorem(self) -> None:
        row = self.fixture["exact_theorems"][
            "universal_improvement_implies_positive_wick_residual"
        ]
        self.assertEqual(row["r_2"], [25, 24])
        self.assertEqual(row["r_3"], [49, 72])
        self.assertEqual(row["r_2_times_r_3"], [1225, 1728])
        self.assertIn("Every proper cyclic hard mask", row["theorem"])
        for control in row["finite_controls"]:
            self.assertTrue(control["improvement_threshold_exceeds_atomic_threshold"])
            self.assertTrue(control["strictly_improves_complete"])
            self.assertTrue(control["wick_residual_positive"])
        quadratic, ternary = row["finite_controls"]
        self.assertEqual(quadratic["wick_residual"], [980, 43])
        self.assertEqual(ternary["wick_residual"], [7335, 196])

    def test_atomic_threshold_formulas_recompute_exactly(self) -> None:
        ternary = MODULE.atomic_threshold_audit((7, 13), 3, 2)
        self.assertEqual(ternary["leverage_improvement_threshold"], [4, 9])
        self.assertEqual(ternary["positive_atomic_residual_threshold"], [91, 1359])
        self.assertEqual(ternary["density"], [2, 3])
        kernel = MODULE.atomic_threshold_audit((7, 13), 3, 1)
        self.assertFalse(kernel["strictly_improves_complete"])
        self.assertTrue(kernel["wick_residual_positive"])

    def test_positive_ternary_wick_residual_is_exact(self) -> None:
        row = self.fixture["exact_theorems"]["wick_atomic_firewall"]
        self.assertEqual(row["phase_atomic_coefficient"], 72)
        self.assertEqual(row["hard_observation_atomic_coefficient"], [9, 4])
        self.assertEqual(row["normal_ordering_residual"], [7335, 196])
        self.assertEqual(
            row["each_selected_double_nonprincipal_gauss_weight"], [91, 18]
        )
        self.assertEqual(
            row["coefficient_weighted_external_gauss_diagnostic"], [91, 36]
        )
        self.assertEqual(row["literal_centered_identity_atomic_coefficient"], [1, 2])
        self.assertTrue(row["residual_is_positive"])

    def test_centered_three_projector_identity_cancels_atoms(self) -> None:
        row = self.fixture["exact_theorems"]["cyclic_centered_projector_identity"][
            "ternary_control"
        ]
        self.assertEqual(row["fourier_weight_abs_squared"]["r=1"], [1, 4])
        self.assertEqual(row["fourier_weight_abs_squared"]["r=2"], [1, 4])
        self.assertEqual(row["principal_centered"], row["reconstructed_centered"])
        self.assertTrue(row["atomic_cancellation"])
        self.assertEqual(
            row["identity"],
            "P_circ=(O_0_circ+O_1_circ+O_2_circ)/3-(H_1_circ+H_2_circ)/4",
        )

    def test_prerequisite_packets_are_hash_and_payload_locked(self) -> None:
        manifest = {
            row["id"]: row for row in self.fixture["source_contract"]["prerequisites"]
        }
        self.assertEqual(set(manifest), set(MODULE.PREREQUISITE_LOCKS))
        for source_id, lock in MODULE.PREREQUISITE_LOCKS.items():
            raw = lock["path"].read_bytes()
            self.assertEqual(MODULE._lf_sha256(raw), lock["lf_sha256"])
            self.assertEqual(MODULE._git_blob_sha1(raw), lock["git_blob"])
            self.assertEqual(manifest[source_id]["git_blob"], lock["git_blob"])
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

    def test_all_live_claim_paths_resolve_to_locked_blobs(self) -> None:
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

    def test_scope_preserves_hard_soft_and_global_firewalls(self) -> None:
        scope = self.fixture["scope"]
        self.assertIn(
            "one fixed live bilateral fibre", scope["proved_source_realization"]
        )
        self.assertIn("does not turn", scope["forbidden_inference"])
        for gate in ("WCADD106140", "WCKUM106140", "BCI102990", "RH", "GRH"):
            self.assertIn(gate, scope["open_arithmetic"])
        firewalls = " ".join(self.fixture["firewalls"])
        self.assertIn("no canonical global mask", firewalls)
        self.assertIn("selected weighted subcombination", firewalls)
        self.assertIn("No principal member", firewalls)

    def test_note_records_load_bearing_formulas_and_boundaries(self) -> None:
        note = NOTE_PATH.read_text(encoding="utf-8")
        for marker in (
            "2k\\)-th-root orientation",
            "raw core character",
            "L-106120 channels",
            "hard/soft separation",
            "{135\\over182}",
            "{7335\\over196}",
            "every hard cyclic mask that improves leverage",
            "centered repair",
            "WCKUM106140",
            "not canonical",
        ):
            self.assertIn(marker, note)

    def test_invalid_panels_and_source_coordinates_fail_closed(self) -> None:
        with self.assertRaisesRegex(ValueError, "congruent"):
            MODULE.cyclic_oriented_exponent(1, 1, 5, 3)
        with self.assertRaisesRegex(ValueError, "outside"):
            MODULE.cyclic_oriented_exponent(3, 1, 7, 3)
        with self.assertRaises(ValueError):
            MODULE.atomic_threshold_audit((7, 7), 3, 2)
        with self.assertRaises(ValueError):
            MODULE.atomic_threshold_audit((7, 13), 3, 3)
        for helper in (
            MODULE.primitive_root,
            lambda prime: MODULE.square_coset(prime, 1),
            lambda prime: MODULE.cyclic_oriented_exponent(1, 1, prime, 3),
        ):
            with self.assertRaisesRegex(ValueError, "cap|capped"):
                helper(10**12 + 39)

    def test_source_byte_cap_is_checked_before_read(self) -> None:
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
                    side_effect=AssertionError("read occurred before byte preflight"),
                ),
                self.assertRaisesRegex(RuntimeError, "per-source byte cap"),
            ):
                MODULE._read_prerequisites(MODULE.ResourceGuard(), MODULE.Deadline())

    def test_resource_caps_are_real_and_exact_algebra_precedes_sources(self) -> None:
        resources = self.fixture["resource_contract"]
        self.assertLess(
            resources["actual_exact_operations"],
            resources["maximum_exact_operations"],
        )
        self.assertLess(
            resources["actual_matrix_cells"], resources["maximum_matrix_cells"]
        )
        self.assertLess(
            resources["actual_residue_atoms"], resources["maximum_residue_atoms"]
        )
        self.assertEqual(
            resources["actual_exact_operations"], resources["operations_before_sources"]
        )
        self.assertEqual(
            resources["actual_matrix_cells"], resources["matrix_cells_before_sources"]
        )
        self.assertEqual(
            resources["actual_residue_atoms"], resources["residue_atoms_before_sources"]
        )
        self.assertFalse(resources["heavy_computation"])

        with self.assertRaises(RuntimeError):
            MODULE.ResourceGuard(
                exact_operations=MODULE.MAX_EXACT_OPERATIONS
            ).operation("overflow")
        with self.assertRaises(RuntimeError):
            MODULE.ResourceGuard(matrix_cells=MODULE.MAX_MATRIX_CELLS).matrix(1)
        with self.assertRaises(RuntimeError):
            MODULE.ResourceGuard(residue_atoms=MODULE.MAX_RESIDUE_ATOMS).atom()
        with self.assertRaises(RuntimeError):
            MODULE.ResourceGuard(source_files=MODULE.MAX_SOURCE_FILES).source(1)
        with self.assertRaises(RuntimeError):
            MODULE.ResourceGuard(git_objects=MODULE.MAX_GIT_OBJECTS).git_object()
        with self.assertRaises(RuntimeError):
            MODULE.Deadline(started=time.monotonic() - 10).check("expired")

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
        self.assertIn("PASS_FFPS_CYCLIC_SOURCE_REALIZATION_GATE", completed.stdout)

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
        self.assertIn("PASS_FFPS_CYCLIC_SOURCE_REALIZATION_GATE", completed.stdout)
        self.assertEqual(before, OUTPUT_PATH.read_bytes())

        with tempfile.TemporaryDirectory() as directory:
            drifted = Path(directory) / "fixture.json"
            drifted.write_text("{}\n", encoding="utf-8")
            with mock.patch.object(MODULE, "OUTPUT_PATH", drifted):
                original = sys.argv
                try:
                    sys.argv = [str(MODULE_PATH), "--check"]
                    with self.assertRaises(RuntimeError):
                        MODULE.main()
                finally:
                    sys.argv = original


if __name__ == "__main__":
    unittest.main()
