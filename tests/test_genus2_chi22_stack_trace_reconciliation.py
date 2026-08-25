"""Fail-closed tests for the bounded chi_(2,2) trace reconciliation."""

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

import genus2_chi22_stack_trace_reconciliation as subject


class Genus2Chi22StackTraceReconciliationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.certificate = subject.build_certificate()

    def test_character_alias_and_adapter_boundary_are_locked(self) -> None:
        alias = self.certificate["character_alias"]
        self.assertEqual(alias["project_character"], "chi_(2,2)")
        self.assertEqual(alias["literature_local_system"], "V_(4,2)")
        self.assertEqual(alias["fundamental_weight"], [2, 2])
        self.assertEqual(alias["highest_weight_e_basis"], [4, 2])
        self.assertEqual(alias["local_system_weight"], 6)
        self.assertEqual(alias["central_character"], 1)
        self.assertEqual(alias["status"], "PROVED_BY_MARKED_STACK_ADAPTER")

    def test_exact_marked_unmarked_arbitrary_mixed_equivalence(self) -> None:
        for q in (3, 5, 7, 9, 11, 25, 27, 49):
            self.assertEqual(subject.unmarked_trace(q), q**3)
            self.assertEqual(subject.arbitrary_point_trace(q), q**4 + q**3)
            self.assertEqual(subject.marked_trace(q), 2 * q**3 - q**2 - 2 * q - 2)
            self.assertEqual(subject.mixed_trace(q), q**4 - q**3 + q**2 + 2 * q + 2)
            self.assertEqual(
                subject.marked_trace_from_mixed(q, subject.mixed_trace(q)),
                subject.marked_trace(q),
            )
        for function in (
            subject.unmarked_trace,
            subject.arbitrary_point_trace,
            subject.marked_trace,
            subject.mixed_trace,
        ):
            with self.assertRaises(ValueError):
                function(0)
        with self.assertRaises(TypeError):
            subject.marked_trace_from_mixed(3, True)

    def test_branch_theorems_and_b3_dependency_are_locked(self) -> None:
        self.assertIn("PROVED_ON_BRANCH", self.certificate["status"])
        theorem = self.certificate["branch_local_theorem"]
        self.assertEqual(theorem["status"], "PROVED_EXACT_ALL_ODD_PRIME_POWERS")
        self.assertEqual(theorem["chi_(0,3)_mean"], "(q^4-2*q-1)/q^6")
        self.assertEqual(theorem["chi_(2,2)_mean"], "(2*q^3-q^2-2*q-2)/q^6")
        self.assertEqual(theorem["marked_stack_trace"], "T_(2,2)(q)=2*q^3-q^2-2*q-2")
        self.assertEqual(theorem["M22_signature_count"], 20)
        self.assertEqual(
            theorem["B3_dependency_payload_sha256"],
            subject.SOURCE_LOCKS[subject.B3_THEOREM_PATH.name]["payload_sha256"],
        )

    def test_published_and_branch_local_boundaries_are_separate(self) -> None:
        imported = self.certificate["established_import"]
        self.assertEqual(imported["formula"], "U_42(q)=q^3")
        self.assertEqual(imported["characteristic"], "odd")
        self.assertIn("Theorem 11.6", imported["source"])

        consequence = self.certificate["mixed_trace_consequence"]
        self.assertEqual(consequence["target"], "M_42(q)=q^4-q^3+q^2+2*q+2")
        self.assertEqual(consequence["status"], "PROVED_ON_BRANCH_AS_EXACT_CONSEQUENCE")
        vectors = consequence["coefficient_vectors_in_increasing_q_power"]
        self.assertEqual(vectors["unmarked_U_42"], [0, 0, 0, 1])
        self.assertEqual(vectors["arbitrary_point_A_42"], [0, 0, 0, 1, 1])
        self.assertEqual(vectors["marked_T_(2,2)"], [-2, -2, -1, 2])
        self.assertEqual(vectors["mixed_M_42"], [2, 2, 1, -1, 1])

        verdict = self.certificate["literature_verdict"]
        self.assertEqual(verdict["published_unmarked_formula"], "FOUND: U_42(q)=q^3")
        self.assertIn("NOT_FOUND", verdict["published_marked_formula"])
        self.assertIn("NOT_FOUND", verdict["published_mixed_formula"])

    def test_arbitrary_point_and_marked_weierstrass_are_distinguished(self) -> None:
        scope = self.certificate["scope"]
        self.assertEqual(
            scope["arbitrary_point_moduli_problem"],
            "M_(2,1), one arbitrary rational point",
        )
        self.assertEqual(
            scope["marked_moduli_problem"],
            "M_2(w^1), one rational Weierstrass point",
        )
        arbitrary = self.certificate["arbitrary_point_distinction"]
        self.assertEqual(arbitrary["trace"], "A_42(q)=q^4+q^3")
        self.assertIn("NOT_THE_MARKED_WEIERSTRASS_TRACE", arbitrary["status"])
        forgetful = self.certificate["forgetful_fibre_identity"]
        self.assertEqual(forgetful["rational_Weierstrass_count"], "R_1(C)=q+1-r_1(C)")
        self.assertEqual(
            forgetful["exact_identity"],
            "T_(2,2)(q)=(q+1)*U_42(q)-M_42(q)",
        )

    def test_exact_specializations_are_not_proof_inputs(self) -> None:
        expected = {
            3: (27, 108, 37, 71),
            5: (125, 750, 213, 537),
            7: (343, 2744, 621, 2123),
        }
        rows = self.certificate["exact_specializations"]
        self.assertEqual(
            {
                row["q"]: (
                    row["unmarked_trace_U_42"],
                    row["arbitrary_point_trace_A_42"],
                    row["marked_Weierstrass_trace_T_(2,2)"],
                    row["mixed_ramification_trace_M_42"],
                )
                for row in rows
            },
            expected,
        )
        self.assertTrue(
            all(
                row["status"] == "EXACT_SPECIALIZATION_NOT_AN_ALL_Q_PROOF_INPUT"
                for row in rows
            )
        )

    def test_literature_ledger_has_locators_hashes_and_corrected_v42_row(self) -> None:
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
        self.assertIn("V_(4,2)", erratum["claim_boundary"])
        self.assertIn(
            "Theorem 11.6",
            self.certificate["established_import"]["erratum_boundary"],
        )

        pointed = literature["bergstrom_pointed_hyperelliptic"]
        self.assertEqual(
            pointed["locators"],
            [
                (
                    "Section 2, geometric Frobenius and arbitrary-point groupoid "
                    "count (arXiv PDF pp. 3-4)"
                ),
                "Section 7.3, incomplete degree-six u_g inventory (arXiv PDF p. 17)",
                (
                    "Section 11.1 (arXiv PDF p. 26) and Theorem 11.6 "
                    "(arXiv PDF p. 29), e_c(M_2,V_(4,2))=L^3"
                ),
                (
                    "Definition 12.1 (arXiv PDF p. 29), Lemma 12.8 "
                    "(pp. 30-31), and Remark 12.9 (p. 31)"
                ),
            ],
        )
        level_two = literature["bergstrom_faber_vandergeer_level_two"]
        self.assertEqual(level_two["version"], "arXiv v2, 20 April 2008")
        self.assertEqual(
            level_two["locators"],
            [
                (
                    "Sections 2-3, definitions of M_2(w^n), A_2(w^n), and "
                    "V_(l,m) (arXiv PDF pp. 2-3)"
                ),
                "Section 5, finite-field computation for odd q<=37 (arXiv PDF pp. 6-8)",
                "Section 9, numerical A_2(w^1) dimension checks (arXiv PDF p. 12)",
                "Section 10, conjectural A_2[2], V_(4,2) example row (arXiv PDF p. 12)",
            ],
        )

    def test_alternative_route_records_new_degree_seven_burden(self) -> None:
        route = self.certificate["bounded_alternative_route"]
        self.assertEqual(route["status"], "OUTLINED_NOT_EXECUTED")
        self.assertIn("degree-six or degree-seven", route["next_step"])
        self.assertIn("new degree-seven general terms", route["next_step"])

    def test_moduli_novelty_and_rh_firewalls_are_explicit(self) -> None:
        scope = self.certificate["scope"]
        self.assertFalse(scope["rh_or_grh_claim"])
        self.assertFalse(scope["finite_field_or_curve_enumeration"])
        firewalls = " ".join(self.certificate["firewalls"])
        self.assertIn("not M_2(w^1)", firewalls)
        self.assertIn("coordinate equivalences", firewalls)
        self.assertIn("not interpolation", firewalls)
        self.assertIn("no claim of external novelty", firewalls)

    def test_source_locks_and_tamper_rejection(self) -> None:
        for name, lock in subject.SOURCE_LOCKS.items():
            path = FUNCTION_FIELD / name
            self.assertEqual(subject._sha256_lf(path), lock["lf_sha256"])
            parsed = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(parsed["schema"], lock["schema"])
            self.assertEqual(parsed["payload_sha256"], lock["payload_sha256"])
            self.assertEqual(len(lock["commit"]), 40)
        source = subject.M22_THEOREM_PATH
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
                "PASS_GENUS2_CHI22_STACK_TRACE_RECONCILIATION",
                process.stdout,
            )


if __name__ == "__main__":
    unittest.main()
