"""Focused exact tests for the FFPS checkerboard source bridge."""

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
    / "ffps_checkerboard_source_bridge.py"
)
OUTPUT_PATH = MODULE_PATH.with_suffix(".json")
NOTE_PATH = MODULE_PATH.with_name("FFPS_CHECKERBOARD_SOURCE_BRIDGE.md")

SPEC = importlib.util.spec_from_file_location(
    "ffps_checkerboard_source_bridge", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load FFPS checkerboard source-bridge producer")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class FFPSCheckerboardSourceBridgeTests(unittest.TestCase):
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
            "EXACT_FIXED_FIBRE_SOURCE_BRIDGE_WITH_WICK_FIREWALL",
        )

    def test_mod_five_raw_core_parity_fails_physical_collapse(self) -> None:
        row = self.fixture["exact_theorems"]["raw_core_collapse_failure"]
        self.assertEqual(row["first"]["physical"], 1)
        self.assertEqual(row["second"]["physical"], 1)
        self.assertEqual(row["first"]["raw_core_sign"], 1)
        self.assertEqual(row["second"]["raw_core_sign"], -1)
        self.assertEqual(row["first"]["oriented_sign"], 1)
        self.assertEqual(row["second"]["oriented_sign"], 1)

    def test_oriented_sign_is_physical_and_has_owner_core_factorization(self) -> None:
        guard = MODULE.ResourceGuard()
        for prime in (5, 13):
            for owner in MODULE.square_coset(prime, 1):
                for core in range(1, prime):
                    physical = owner * core * core % prime
                    direct = MODULE.oriented_sign(physical, 1, prime, guard)
                    source = MODULE.source_oriented_sign(owner, core, 1, prime, guard)
                    quartic = MODULE.quartic_source_sign(owner, core, 1, prime, guard)
                    self.assertEqual(direct, source)
                    self.assertEqual(direct, quartic)
        audits = self.fixture["exact_theorems"]["quartic_oriented_physical_invariance"][
            "finite_audits"
        ]
        self.assertTrue(all(row["oriented_fibres_are_singletons"] for row in audits))
        self.assertTrue(
            all(row["raw_core_sign_mixes_on_some_physical_fibre"] for row in audits)
        )

    def test_quartic_gauge_only_swaps_projector_labels(self) -> None:
        audit = MODULE.gauge_audit(13, 1, 2, MODULE.ResourceGuard())
        self.assertEqual(audit["new_representative"], 4)
        self.assertEqual(audit["constant_multiplier"], -1)
        self.assertIn("swap", audit["effect"])
        for coordinate in MODULE.square_coset(13, 1):
            self.assertEqual(
                MODULE.oriented_sign(coordinate, 4, 13),
                -MODULE.oriented_sign(coordinate, 1, 13),
            )

    def test_bilateral_checkerboard_is_balanced_and_physical(self) -> None:
        signs = MODULE.checkerboard_signs(5, 13, 1, 1, MODULE.ResourceGuard())
        self.assertEqual(len(signs), 12)
        self.assertEqual(signs.count(1), 6)
        self.assertEqual(signs.count(-1), 6)
        theorem = self.fixture["exact_theorems"]["bilateral_projector"]
        self.assertTrue(theorem["each_projector_has_half_the_complete_fixed_grid"])
        self.assertIn("two-coordinate", theorem["crt_scope"])
        self.assertIn("not generally", theorem["crt_scope"])

    def test_exact_l106120_double_nonprincipal_identification(self) -> None:
        theorem = self.fixture["exact_theorems"]["existing_kummer_channel"]
        indices = theorem["L_106120_indices"]
        self.assertEqual(indices["eta_mod_ell"], "kappa_ell")
        self.assertEqual(indices["theta_mod_rho"], "kappa_rho")
        self.assertTrue(theorem["spectrally_absorbed_by_even_character_family"])
        self.assertTrue(theorem["hard_restricted_gram_not_implied"])

        guard = MODULE.ResourceGuard()
        for prime in (5, 13):
            representative = 1
            for owner in MODULE.square_coset(prime, representative):
                for core in range(1, prime):
                    self.assertEqual(
                        MODULE.quartic_source_sign(
                            owner, core, representative, prime, guard
                        ),
                        MODULE.source_oriented_sign(
                            owner, core, representative, prime, guard
                        ),
                    )

    def test_hard_restricted_metric_improves_but_soft_mode_worsens(self) -> None:
        row = self.fixture["exact_theorems"]["hard_versus_soft_metric"]
        self.assertEqual(row["restricted_denominator_each"], 258)
        self.assertEqual(row["sharp_restricted_leverage"], [24, 43])
        self.assertEqual(row["complete_tensor_leverage"], [4, 7])
        self.assertEqual(row["same_soft_weight_in_complete_inverse_metric"], [344, 455])
        self.assertLess(Fraction(24, 43), Fraction(4, 7))
        self.assertGreater(Fraction(344, 455), Fraction(4, 7))
        self.assertEqual(row["uniform_retained_weight"], [2, 1])
        self.assertTrue(row["hard_improves_complete"])
        self.assertTrue(row["soft_worsens_complete"])

    def test_atomic_normal_ordering_firewall_is_exact(self) -> None:
        row = self.fixture["exact_theorems"]["wick_atomic_firewall"]
        self.assertEqual(row["phase_atomic_coefficient"], 48)
        self.assertEqual(row["doubled_observation_atomic_coefficient"], 4)
        self.assertEqual(row["normal_ordering_residual"], [980, 43])
        self.assertEqual(
            Fraction(*row["selected_quartic_quartic_gauss_weight"]),
            Fraction(65, 12),
        )
        for left, right in ((5, 13), (5, 17), (13, 17), (13, 29)):
            leverage = Fraction(
                4 * (left - 1) * (right - 1),
                5 * left * right + left + right + 1,
            )
            firewall = MODULE.atomic_firewall(
                left,
                right,
                leverage,
            )
            self.assertGreater(Fraction(*firewall["normal_ordering_residual"]), 0)

    def test_centered_projector_identity_cancels_atoms_exactly(self) -> None:
        signs = MODULE.checkerboard_signs(5, 13, 1, 1, MODULE.ResourceGuard())
        audit = MODULE.centered_projector_audit(signs)
        self.assertEqual(
            Fraction(*audit["principal_centered"]),
            Fraction(*audit["reconstructed_centered"]),
        )
        self.assertTrue(audit["atomic_cancellation"])
        self.assertEqual(
            audit["identity"],
            "P_circ=(O_plus_circ+O_minus_circ)/2-H_circ",
        )

    def test_live_claim_paths_resolve_to_exact_blobs(self) -> None:
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

    def test_correlated_packet_is_commit_and_payload_locked(self) -> None:
        manifest = {
            row["id"]: row
            for row in self.fixture["source_contract"]["correlated_sources"]
        }
        self.assertEqual(set(manifest), set(MODULE.CORRELATED_LOCKS))
        for source_id, lock in MODULE.CORRELATED_LOCKS.items():
            raw = lock["path"].read_bytes()
            self.assertEqual(MODULE._lf_sha256_bytes(raw), lock["lf_sha256"])
            self.assertEqual(MODULE._git_blob_sha1(raw), lock["git_blob"])
            completed = subprocess.run(
                [
                    "git",
                    "rev-parse",
                    (
                        f"{MODULE.CORRELATED_COMMIT}:"
                        f"{lock['path'].relative_to(ROOT).as_posix()}"
                    ),
                ],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
                timeout=2.0,
            )
            self.assertEqual(completed.stdout.strip(), lock["git_blob"])
            self.assertEqual(manifest[source_id]["commit"], MODULE.CORRELATED_COMMIT)
        self.assertEqual(
            MODULE.CORRELATED_LOCKS["correlated_json"]["payload_sha256"],
            "ee6c66844a15b4d6a29a6cf5dc252a5efdd5cc8b6052dcd9c27bf76dbe03269a",
        )

    def test_scope_keeps_fixed_fibre_formal_and_global_layers_separate(self) -> None:
        scope = self.fixture["scope"]
        self.assertIn("one fixed", scope["proved_source_realization"])
        self.assertIn("growing-d", scope["formal_only"])
        self.assertIn("two marked phase primes", scope["formal_only"])
        for gate in (
            "CBKM106130",
            "WCADD106140",
            "WCKUM106140",
            "BCI102990",
            "RH",
            "GRH",
        ):
            self.assertIn(gate, scope["open_arithmetic"])
        self.assertIn("Wick-centered", scope["smallest_analytic_lift"])
        self.assertIn("does not re-invert", scope["forbidden_inference"])

    def test_note_records_all_load_bearing_firewalls(self) -> None:
        note = NOTE_PATH.read_text(encoding="utf-8")
        for marker in (
            "quartic orientation",
            "raw core parity fails physical collapse",
            "double-nonprincipal",
            "hard physical deletion",
            "The atomic/Wick obstruction",
            "980\\over43",
            "P_0^\\circ",
            "WCADD106140",
            "WCKUM106140",
            "growing-\\(d\\)",
        ):
            self.assertIn(marker, note)

    def test_resource_caps_are_real_and_fail_closed(self) -> None:
        used = self.fixture["resource_budget"]["used"]
        limits = self.fixture["resource_budget"]["limits"]
        self.assertLess(used["exact_operations"], limits["exact_operations"])
        self.assertLess(used["matrix_cells"], limits["matrix_cells"])
        self.assertLess(used["residue_atoms"], limits["residue_atoms"])
        self.assertLessEqual(used["git_objects"], limits["git_objects"])
        self.assertFalse(self.fixture["resource_budget"]["heavy_computation"])
        self.assertEqual(self.fixture["resource_budget"]["largest_residue_prime"], 13)
        self.assertEqual(
            self.fixture["resource_budget"]["largest_matrix_dimension"], 12
        )

        operation_guard = MODULE.ResourceGuard(
            exact_operations=MODULE.MAX_EXACT_OPERATIONS
        )
        with self.assertRaises(RuntimeError):
            operation_guard.operation("overflow")
        matrix_guard = MODULE.ResourceGuard(matrix_cells=MODULE.MAX_MATRIX_CELLS)
        with self.assertRaises(RuntimeError):
            matrix_guard.matrix(1)
        atom_guard = MODULE.ResourceGuard(residue_atoms=MODULE.MAX_RESIDUE_ATOMS)
        with self.assertRaises(RuntimeError):
            atom_guard.atom()
        source_guard = MODULE.ResourceGuard(source_files=MODULE.MAX_SOURCE_FILES)
        with self.assertRaises(RuntimeError):
            source_guard.source(1)
        git_guard = MODULE.ResourceGuard(git_objects=MODULE.MAX_GIT_OBJECTS)
        with self.assertRaises(RuntimeError):
            git_guard.git_object()
        expired = MODULE.Deadline(started=time.monotonic() - 10)
        with self.assertRaises(RuntimeError):
            expired.check("test")

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
        self.assertIn("PASS_FFPS_CHECKERBOARD_SOURCE_BRIDGE", completed.stdout)

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
        self.assertIn("PASS_FFPS_CHECKERBOARD_SOURCE_BRIDGE", completed.stdout)
        self.assertEqual(before, OUTPUT_PATH.read_bytes())

        with tempfile.TemporaryDirectory() as directory:
            drifted = Path(directory) / "fixture.json"
            drifted.write_text("{}\n", encoding="utf-8")
            with mock.patch.object(MODULE, "OUTPUT_PATH", drifted):
                original = sys.argv
                try:
                    sys.argv = [str(MODULE_PATH), "--check"]
                    with self.assertRaises(SystemExit):
                        MODULE.main()
                finally:
                    sys.argv = original


if __name__ == "__main__":
    unittest.main()
