"""Fail-closed tests for the bounded chi_(0,3) trace reconciliation."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import genus2_chi03_stack_trace_reconciliation as subject


class Genus2Chi03StackTraceReconciliationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.certificate = subject.build_certificate()

    def test_character_alias_and_adapter_boundary_are_locked(self) -> None:
        alias = self.certificate["character_alias"]
        self.assertEqual(alias["project_character"], "chi_(0,3)")
        self.assertEqual(alias["literature_local_system"], "V_(3,3)")
        self.assertEqual(alias["fundamental_weight"], [0, 3])
        self.assertEqual(alias["highest_weight_e_basis"], [3, 3])
        self.assertEqual(alias["local_system_weight"], 6)
        self.assertEqual(alias["status"], "PROVED_BY_MARKED_STACK_ADAPTER")

    def test_exact_marked_unmarked_mixed_equivalence(self) -> None:
        for q in (3, 5, 7, 9, 11, 25, 27, 49):
            required = subject.mixed_trace_required_by_candidate(q)
            self.assertEqual(required, -(q**4) - q**2)
            self.assertEqual(
                subject.marked_trace_from_mixed(q, required),
                subject.candidate_marked_trace(q),
            )
            self.assertEqual(subject.unmarked_trace(q), -q - 1)
        for function in (
            subject.unmarked_trace,
            subject.candidate_marked_trace,
            subject.mixed_trace_required_by_candidate,
        ):
            with self.assertRaises(ValueError):
                function(0)

    def test_branch_theorem_closes_the_formerly_missing_identity(self) -> None:
        self.assertIn("PROVED_ON_BRANCH", self.certificate["status"])
        theorem = self.certificate["branch_local_theorem"]
        self.assertEqual(theorem["status"], "PROVED_EXACT_ALL_ODD_PRIME_POWERS")
        self.assertEqual(theorem["chi_(0,3)_mean"], "(q^4-2*q-1)/q^6")
        self.assertEqual(theorem["marked_stack_trace"], "T_(0,3)(q)=q^4-2*q-1")
        self.assertEqual(theorem["signature_count"], 23)
        self.assertEqual(theorem["signature_partition"], "q^6")

        consequence = self.certificate["mixed_trace_consequence"]
        self.assertEqual(consequence["target"], "M_33(q)=-q^4-q^2")
        self.assertEqual(consequence["status"], "PROVED_ON_BRANCH_AS_EXACT_CONSEQUENCE")
        self.assertEqual(
            consequence["coefficient_vectors_in_increasing_q_power"][
                "required_mixed_M_33"
            ],
            [0, 0, -1, 0, -1],
        )
        self.assertEqual(
            self.certificate["literature_verdict"]["published_table_import"],
            "NOT_FOUND_AND_NOT_CLAIMED",
        )

    def test_frozen_rows_are_finite_controls_only(self) -> None:
        expected = {
            3: (74, -90),
            5: (614, -650),
            7: (2386, -2450),
        }
        controls = self.certificate["finite_controls"]
        self.assertEqual(
            {
                row["q"]: (
                    row["marked_stack_trace"],
                    row["implied_mixed_ramification_trace"],
                )
                for row in controls
            },
            expected,
        )
        self.assertTrue(
            all(
                row["status"] == "EXACT_FINITE_CONTROL_NOT_USED_AS_ALL_Q_PROOF"
                for row in controls
            )
        )

    def test_literature_ledger_has_locators_hashes_and_erratum(self) -> None:
        literature = {row["key"]: row for row in self.certificate["primary_literature"]}
        self.assertEqual(
            set(literature),
            {
                "bergstrom_pointed_hyperelliptic",
                "bergstrom_faber_vandergeer_level_two",
                "bergstrom_2025_author_erratum",
            },
        )
        for row in literature.values():
            self.assertTrue(row["url"].startswith("https://"))
            self.assertGreater(len(row["locators"]), 0)
            self.assertEqual(len(row["pdf_sha256"]), 64)
        erratum = literature["bergstrom_2025_author_erratum"]
        self.assertIn("-15", erratum["claim_boundary"])
        self.assertIn(
            "Theorem 11.6",
            self.certificate["established_import"]["erratum_boundary"],
        )

    def test_moduli_and_rh_firewalls_are_explicit(self) -> None:
        scope = self.certificate["scope"]
        self.assertEqual(
            scope["arbitrary_point_moduli_problem"],
            "M_(2,1), explicitly distinguished from M_2(w^1)",
        )
        self.assertFalse(scope["rh_or_grh_claim"])
        self.assertFalse(scope["finite_field_or_curve_enumeration"])
        firewalls = " ".join(self.certificate["firewalls"])
        self.assertIn("coordinate equivalences", firewalls)
        self.assertIn("not interpolation", firewalls)
        self.assertIn("not M_2(w^1)", firewalls)
        self.assertIn("no claim of external novelty", firewalls)

    def test_source_locks_and_tamper_rejection(self) -> None:
        for name, lock in subject.SOURCE_LOCKS.items():
            path = FUNCTION_FIELD / name
            self.assertEqual(subject._sha256_lf(path), lock["lf_sha256"])
            parsed = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(parsed["schema"], lock["schema"])
            self.assertEqual(parsed["payload_sha256"], lock["payload_sha256"])
        source = subject.MARKED_ADAPTER_PATH
        lock = subject.SOURCE_LOCKS[source.name]
        with tempfile.TemporaryDirectory() as directory:
            tampered = Path(directory) / source.name
            raw = bytearray(source.read_bytes())
            raw[-2] = (raw[-2] + 1) % 128
            tampered.write_bytes(raw)
            with self.assertRaises(ArithmeticError):
                subject._load_locked_json(tampered, lock)

    def test_resource_cap_and_payload_hash_are_exact(self) -> None:
        resources = self.certificate["provenance"]["resource_contract"]
        self.assertEqual(resources["finite_fields_enumerated"], 0)
        self.assertEqual(resources["curves_enumerated"], 0)
        self.assertEqual(resources["random_samples"], 0)
        self.assertLessEqual(
            resources["exact_operations_used"], resources["exact_operation_cap"]
        )
        payload = dict(self.certificate)
        claimed = payload.pop("payload_sha256")
        self.assertEqual(subject._canonical_sha256(payload), claimed)

    def test_fixture_and_cli_replay_under_normal_and_optimized_python(self) -> None:
        stored = json.loads(subject.OUTPUT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(stored, self.certificate)
        local_hashes = stored["provenance"]["source_hashes_lf_sha256"]
        for label, path in {
            "producer": Path(subject.__file__),
            "note": subject.NOTE_PATH,
            "test": Path(__file__),
        }.items():
            self.assertEqual(local_hashes[label], subject._sha256_lf(path))

        for optimization in ([], ["-O"]):
            process = subprocess.run(
                [
                    sys.executable,
                    *optimization,
                    str(Path(subject.__file__)),
                    "--check",
                ],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
                timeout=10,
            )
            self.assertEqual(process.returncode, 0, process.stderr)
            self.assertIn(
                "PASS_GENUS2_CHI03_STACK_TRACE_RECONCILIATION",
                process.stdout,
            )


if __name__ == "__main__":
    unittest.main()
