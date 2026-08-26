"""Optimized-safe tests for the Sym12 master-adapter contradiction audit."""

from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "genus2_sym12_master_adapter_contradiction_audit.py"
)
OUTPUT_PATH = MODULE_PATH.with_suffix(".json")

SPEC = importlib.util.spec_from_file_location(
    "genus2_sym12_master_adapter_contradiction_audit", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load Sym12 contradiction-audit producer")
subject = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = subject
SPEC.loader.exec_module(subject)


class Genus2Sym12MasterAdapterContradictionAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()
        cls.stored = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))

    def test_canonical_fixture_and_self_hash(self) -> None:
        self.assertEqual(self.fixture, self.stored)
        payload = dict(self.stored)
        claimed = payload.pop("payload_sha256")
        self.assertEqual(claimed, subject._canonical_sha256(payload))
        self.assertEqual(
            OUTPUT_PATH.read_text(encoding="utf-8"), subject._serialized(self.stored)
        )

    def test_five_committed_sources_are_content_locked(self) -> None:
        expected = {
            "marked_stack_adapter": "c8eff406f49daf9f09c0bb3e63e21659275d224e",
            "sym12_inventory": "482e32c53f26517906143cd0d99c74d8b4edf3be",
            "sym12_finite_scout": "c463d4896e62057139454cb0ae2beb868506fee4",
            "conditional_closure": "20abcc478c310a17917b2276f85e525ad966f1c2",
            "one_tate_no_go": "86be60a01e39651d4501fd704afc664a251f97a8",
        }
        manifest = {row["id"]: row for row in self.stored["source_manifest"]}
        self.assertEqual(
            {key: row["commit"] for key, row in manifest.items()}, expected
        )
        for row in manifest.values():
            raw = (ROOT / row["path"]).read_bytes()
            self.assertEqual(subject._git_blob(raw), row["git_blob"])
            self.assertEqual(subject._lf_sha256(raw), row["lf_sha256"])

    def test_exact_stack_arithmetic_and_boundary_arrows_pass(self) -> None:
        arrows = self.stored["exact_arrow_audit"]
        self.assertEqual(arrows["all_statuses"], "PASS")
        self.assertEqual(arrows["stack_group_order"], "q*(q-1)")
        self.assertIn("(q+1)*G3hat", arrows["reciprocal_preclosure"])
        self.assertEqual(arrows["linear_row"], "Q1hat=3*q-9")
        self.assertIn("11-3*q", arrows["ordered_boundary"])
        self.assertEqual(arrows["stable_channel"], "Genuine=0")

    def test_raw_T_residual_is_minus_p(self) -> None:
        block = self.stored["finite_raw_T_contradiction"]
        self.assertTrue(block["not_independent_of_inventory"])
        expected = {3: (-4_587, -3), 5: (267_251, -5), 7: (-382_735, -7)}
        for row in block["rows"]:
            direct_t, residual = expected[row["p"]]
            self.assertEqual(row["direct_T_(12,0)"], direct_t)
            self.assertEqual(
                row["project_minus_Shmakov_from_raw_T_plus_inventory"], residual
            )
            self.assertEqual(row["Shmakov_required_minus_arithmetic_branch"], row["p"])
        self.assertIn("inventory", block["provenance"])

    def test_smallest_arrow_and_formal_repair_are_caveated(self) -> None:
        arrow = self.stored["smallest_unproved_arrow"]
        self.assertIn("associated-graded", arrow["arrow"])
        self.assertIn("Galois", arrow["arrow"])
        repair = self.stored["unique_formal_repair_within_displayed_ledger"]
        self.assertEqual(repair["carrier"], "[5,1] tensor L")
        self.assertEqual(repair["effect_on_Eisenstein_projection"], "2-4*L -> 2-5*L")
        self.assertIn("not an all-q", repair["grade"])

    def test_scope_and_resources_are_bounded(self) -> None:
        self.assertEqual(
            self.stored["status"],
            "EXACT_SOURCE_RELATIVE_THREE_PRIME_CONTRADICTION_LOCALIZATION",
        )
        self.assertEqual(
            self.stored["scope"]["all_q_cohomological_correction"], "NOT_PROVED"
        )
        firewalls = " ".join(self.stored["firewalls"])
        for marker in ("PROVENANCE FIREWALL", "FINITE FIREWALL", "GALOIS FIREWALL"):
            self.assertIn(marker, firewalls)
        resources = self.stored["resource_contract"]
        self.assertEqual(resources["source_files"]["actual"], 5)
        self.assertEqual(resources["source_bytes"]["actual_total"], 90_961)
        self.assertEqual(resources["finite_row_checks"]["actual"], 3)
        self.assertEqual(resources["runtime_external_access"], "NONE")

    def test_caps_and_hash_drift_fail_explicitly(self) -> None:
        guard = subject.ResourceGuard(row_checks=subject.MAX_ROW_CHECKS)
        with self.assertRaises(RuntimeError):
            guard.row()
        damaged = dict(subject.SOURCE_LOCKS[0])
        damaged["lf_sha256"] = "0" * 64
        original = subject.SOURCE_LOCKS
        subject.SOURCE_LOCKS = (damaged, *original[1:])
        try:
            with self.assertRaises(ValueError):
                subject._load_sources(subject.ResourceGuard())
        finally:
            subject.SOURCE_LOCKS = original


if __name__ == "__main__":
    unittest.main()
