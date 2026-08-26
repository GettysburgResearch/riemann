"""Optimized-safe tests for the conditional Sym12 endoscopic closure."""

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
    / "genus2_sym12_conditional_endoscopic_closure.py"
)
OUTPUT_PATH = MODULE_PATH.with_suffix(".json")

SPEC = importlib.util.spec_from_file_location(
    "genus2_sym12_conditional_endoscopic_closure", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load conditional Sym12 closure producer")
subject = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = subject
SPEC.loader.exec_module(subject)


class Genus2Sym12ConditionalEndoscopicClosureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()
        cls.stored = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))

    def test_canonical_fixture_and_payload_self_hash(self) -> None:
        self.assertEqual(self.fixture, self.stored)
        payload = dict(self.stored)
        claimed = payload.pop("payload_sha256")
        self.assertEqual(claimed, subject._canonical_sha256(payload))
        rendered = subject._serialized(self.stored)
        self.assertEqual(OUTPUT_PATH.read_text(encoding="utf-8"), rendered)
        self.assertLessEqual(len(rendered.encode("utf-8")), subject.MAX_OUTPUT_BYTES)

    def test_committed_source_locks_and_transitive_manifests(self) -> None:
        expected = {
            "sym12_inventory": {
                "commit": "482e32c53f26517906143cd0d99c74d8b4edf3be",
                "git_blob": "68907aa3ee65ced500807c79123f116da05f0ece",
                "sha256_lf_normalized": (
                    "94f0647a91aff299c62f24019947846e6923863f3ecba3c2f9cf95008407d4f6"
                ),
                "payload_sha256": (
                    "fba1c85c8dc3d60b276635ae5e3ed84db3ded06f4960afeaa9b92b4055f9211f"
                ),
            },
            "sym12_finite_scout": {
                "commit": "c463d4896e62057139454cb0ae2beb868506fee4",
                "git_blob": "68acd63d703d3569f282cd32a4160dcdd7bf76fa",
                "sha256_lf_normalized": (
                    "06cc45904ee427fa6b2d2812b6c54d2312d6b9d41e12cd4689d28b7def360d2e"
                ),
                "payload_sha256": (
                    "1c794190e4e83778de852d1f12df5a35fccbce414c27df67eeeb6f87ed7ee1d1"
                ),
            },
            "sym12_marked_valuation_kernel": {
                "commit": "a0871416abb4ac58132b53dd4ae30faeed9719bd",
                "git_blob": "6e9fcc3d42f1a7acf74759dd408259fd507c79f0",
                "raw_worktree_blob": "5a6449e035ced7fcf666ca29be0fe80b0075bb06",
                "sha256_lf_normalized": (
                    "9e833cb7778c6613d0f4c7ef22a72319864c05ce41c50addc9dee778d5446076"
                ),
            },
        }
        manifest = {row["id"]: row for row in self.stored["source_manifest"]}
        self.assertEqual(set(manifest), set(expected))
        for source_id, sentinels in expected.items():
            row = manifest[source_id]
            for key, value in sentinels.items():
                self.assertEqual(row[key], value)
            path = ROOT / row["path"]
            raw = path.read_bytes()
            self.assertEqual(subject._lf_sha256(raw), row["sha256_lf_normalized"])
            if source_id == "sym12_marked_valuation_kernel":
                self.assertEqual(subject._raw_git_blob(raw), row["raw_worktree_blob"])
            else:
                self.assertEqual(subject._git_blob(raw), row["git_blob"])
            source = json.loads(raw.decode("utf-8"))
            if source_id == "sym12_marked_valuation_kernel":
                self.assertEqual(
                    row["content_kind"],
                    "EXACT_RAW_FIXTURE_WITH_COMMIT_AND_DUAL_HASH_LOCK",
                )
                self.assertEqual(row["transitive_packet_files"], [])
                self.assertEqual(
                    source["representative_boundary_valuation"]["combined_matrix"][
                        "nullity"
                    ],
                    0,
                )
            else:
                claimed = source.pop("payload_sha256")
                self.assertEqual(claimed, row["payload_sha256"])
                self.assertEqual(claimed, subject._canonical_sha256(source))
                self.assertEqual(len(row["transitive_packet_files"]), 3)
            for transitive in row["transitive_packet_files"]:
                transitive_raw = (ROOT / transitive["path"]).read_bytes()
                self.assertEqual(
                    subject._lf_sha256(transitive_raw),
                    transitive["sha256_lf_normalized"],
                )

        for packet_source in self.stored["packet_manifest"]:
            raw = (ROOT / packet_source["path"]).read_bytes()
            self.assertEqual(
                subject._lf_sha256(raw),
                packet_source["sha256_lf_normalized"],
            )

    def test_exact_S6_to_S5_branching(self) -> None:
        branching = self.stored["S6_to_S5_branching"]
        rows = branching["rows"]
        self.assertEqual(len(rows), 11)
        self.assertEqual(branching["partitions_with_invariants"], ["[6]", "[5,1]"])
        invariant_rows = {
            row["S6_partition"]: row["S5_invariant_multiplicity"]
            for row in rows
            if row["S5_invariant_multiplicity"]
        }
        self.assertEqual(invariant_rows, {"[6]": 1, "[5,1]": 1})
        self.assertEqual(branching["status"], "EXACT_STANDARD_BRANCHING_RULE_REPLAY")

    def test_BFG_endoscopic_specialization_projects_to_fplus_2fminus(self) -> None:
        block = self.stored["BFG_endoscopic_specialization"]
        self.assertEqual(block["parameters"], {"l": 12, "m": 0, "k": 16, "k_prime": 14})
        self.assertEqual(
            block["tau_specialization"],
            {
                "tau_(1,16)": 1,
                "tau_(2,16)": 1,
                "tau_16_plus": 1,
                "tau_16_minus": 0,
            },
        )
        channels = block["projected_channels"]
        self.assertEqual(channels["S14_Gamma0(4)_new"]["projected_multiplicity"], 0)
        self.assertEqual(channels["S14_Gamma0(2)_new"]["projected_multiplicity"], 1)
        self.assertEqual(
            channels["S14_Gamma0(2)_new_plus"]["projected_multiplicity"], 0
        )
        self.assertEqual(
            channels["S14_Gamma0(2)_new_minus"]["projected_multiplicity"], 1
        )
        self.assertEqual(channels["S14_SL2Z"]["dimension"], 0)
        self.assertEqual(block["expanded_endoscopy"], "-L*(f_plus+2*f_minus)")
        self.assertEqual(block["BFG_status"], "CONJECTURAL_IN_BFG_2008")
        self.assertIn("Roesner", block["later_theorem_support"])
        self.assertIn("Shmakov", block["later_theorem_support"])

    def test_nonregular_eisenstein_is_caveated_and_discrepancy_is_exact(self) -> None:
        block = self.stored["nonregular_Eisenstein_specialization"]
        self.assertEqual(
            block["dimensions"],
            {
                "dim_S14_Gamma0(2)": 2,
                "dim_S16_Gamma0(2)": 3,
                "dim_S14_SL2Z": 0,
            },
        )
        self.assertEqual(block["nonregular_convention"], "S[2]=-L-1")
        self.assertEqual(block["formal_result"], "2-5*L")
        self.assertIn("CONJECTURAL", block["BFG_status"])
        discrepancy = block["later_source_discrepancy"]
        self.assertEqual(discrepancy["Shmakov_Siegel_Eisenstein"], "2-2*L")
        self.assertEqual(discrepancy["Shmakov_Klingen"], "0")
        self.assertEqual(discrepancy["Shmakov_Borel"], "-2*L")
        self.assertEqual(discrepancy["Shmakov_printed_specialization"], "2-4*L")
        self.assertEqual(discrepancy["difference_BFG_minus_Shmakov"], "-L")
        self.assertIn("[5,1]", discrepancy["missing_channel"])
        self.assertEqual(discrepancy["status"], "UNRESOLVED_ONE_TATE_DISCREPANCY")
        self.assertIn("same ambient", discrepancy["normalization_check"])
        self.assertIn("no open/ambient", discrepancy["normalization_check"])

    def test_stable_vanishing_uses_exact_marked_zero_and_form_adapter(self) -> None:
        stable = self.stored["stable_invariant_vanishing_certificate"]
        exact = stable["exact_marked_modular_zero"]
        self.assertEqual(exact["preholomorphic_highest_weight_dimension"], 66)
        self.assertEqual(
            exact["corrected_two_orientation_matrix"],
            {
                "rows": 9902,
                "columns": 66,
                "rank_over_Q": 66,
                "rank_mod_1000003": 66,
                "rank_mod_1000033": 66,
                "nullity": 0,
            },
        )
        self.assertEqual(exact["conclusion"], "S_(12,3)(Gamma_2(w^1))=0")
        adapter = stable["form_to_stable_channel_adapter"]
        self.assertIn("four-dimensional", adapter["Roesner_theorem"])
        self.assertIn("including m=0", adapter["holomorphic_component"])
        self.assertIn("Genuine=", adapter["conclusion"])
        self.assertEqual(stable["exact_conclusion"], "Genuine=0")

        official = stable["official_conditional_corroboration"]
        self.assertEqual(official["total_dimension_checksum"], 30)
        self.assertEqual(official["S5_invariant_dimension_from_these_rows"], 0)
        self.assertEqual(
            [row["S6_partition"] for row in official["isotypical_rows"]],
            ["[3,1,1,1]", "[2,2,2]", "[2,2,1,1]", "[2,1,1,1,1]", "[1,1,1,1,1,1]"],
        )
        self.assertIn("CONDITIONAL", official["source_grade"])
        self.assertEqual(official["runtime_access"].split(";")[0], "NONE")
        self.assertIn("semisimplified", stable["firewall"])

    def test_exact_conditional_iff_and_one_Tate_shift(self) -> None:
        algebra = self.stored["exact_internal_algebra"]
        project = algebra["project_ambient"]
        self.assertEqual(
            project["vector"],
            {"one": 2, "L": -5, "L_f_plus": -1, "L_f_minus": -1, "Hhat_12": 1},
        )
        general = algebra["master_target_before_exact_stable_specialization"]
        self.assertEqual(
            general["project_minus_target"],
            {
                "L_f_minus": 1,
                "Hhat_12": 1,
                "Epsilon_Eis": -1,
                "Genuine": 1,
            },
        )
        self.assertEqual(
            general["equality_iff"],
            "Hhat_12=-L*f_minus+Epsilon_Eis-Genuine",
        )
        closed = algebra["target_after_exact_stable_vanishing"]
        self.assertEqual(closed["project_minus_target"], {"L_f_minus": 1, "Hhat_12": 1})
        self.assertEqual(closed["equality_iff"], "Hhat_12=-L*f_minus")
        self.assertIn("EXACT_STABLE_SPECIALIZATION", closed["status"])
        alternate = algebra["one_Tate_discrepancy_effect"]
        self.assertEqual(
            alternate["if_Eisenstein_is_2_minus_4L_before_stable_vanishing"][
                "project_minus_target"
            ],
            {"L": -1, "L_f_minus": 1, "Hhat_12": 1, "Genuine": 1},
        )
        self.assertEqual(
            alternate["if_Eisenstein_is_2_minus_4L_before_stable_vanishing"][
                "equality_iff"
            ],
            "Hhat_12=L-L*f_minus-Genuine",
        )
        self.assertEqual(
            alternate["if_Eisenstein_is_2_minus_4L_and_Genuine_is_zero"][
                "project_minus_target"
            ],
            {"L": -1, "L_f_minus": 1, "Hhat_12": 1},
        )
        self.assertEqual(
            alternate["if_Eisenstein_is_2_minus_4L_and_Genuine_is_zero"][
                "equality_iff"
            ],
            "Hhat_12=L-L*f_minus",
        )

    def test_finite_scout_is_corroboration_only(self) -> None:
        finite = self.stored["finite_scout_corroboration"]
        expected = {
            3: (-3_708, 1_236),
            5: (287_250, -57_450),
            7: (-449_624, 64_232),
        }
        for row in finite["rows"]:
            hhat, coefficient = expected[row["p"]]
            self.assertEqual((row["Hhat_12"], row["a_p(f_minus)"]), (hhat, coefficient))
            self.assertEqual(hhat, -row["p"] * coefficient)
            self.assertEqual(row["BFG_required_Hhat"], hhat)
            self.assertEqual(
                row["Shmakov_2_minus_4L_required_Hhat_if_Genuine_zero"],
                hhat + row["p"],
            )
            self.assertEqual(row["Shmakov_required_minus_observed"], row["p"])
            self.assertEqual(
                row["Shmakov_required_Genuine_trace_to_match_observed"], row["p"]
            )
            self.assertTrue(row["Hhat_12_is_inventory_derived"])
            self.assertEqual(
                row["raw_T_plus_inventory_project_minus_Shmakov_target"],
                -row["p"],
            )
            self.assertTrue(row["BFG_match"])
            self.assertTrue(row["match"])
        self.assertEqual(
            finite["role"],
            "EXACT_RAW_T_PLUS_INVENTORY_CONSEQUENCE_NOT_AN_INDEPENDENT_"
            "INVENTORY_AUDIT_OR_INTERPOLATION",
        )
        self.assertIn("only T_(12,0) is replayed directly", finite["firewall"])
        self.assertIn("not an independent audit", finite["firewall"])
        self.assertIn("misses each stored row by +p", finite["one_Tate_check"])
        self.assertIn("E_project-E_Shmakov equals -p", finite["raw_T_check"])

    def test_status_firewalls_caps_and_no_runtime_external_access(self) -> None:
        self.assertEqual(
            self.stored["status"],
            "EXACT_STABLE_CHANNEL_CLOSURE_ONE_EISENSTEIN_GATE_NOT_ALL_Q",
        )
        statement = self.stored["conditional_statement"]
        self.assertIn("Genuine", statement["unconditional_conclusion"])
        self.assertEqual(len(statement["premises"]), 3)
        self.assertEqual(len(statement["unresolved_premises"]), 1)
        self.assertIn("Epsilon_Eis-Genuine", statement["master_reduction"])
        self.assertIn("Genuine=", statement["exact_stable_closure"])
        self.assertIn("alpha_{-,p}^r", self.stored["prime_power_trace_convention"])
        text = " ".join(self.stored["firewalls"])
        for marker in (
            "CONDITIONAL-REDUCTION FIREWALL",
            "NONREGULAR FIREWALL",
            "ONE-TATE FIREWALL",
            "AMBIENT-NORMALIZATION FIREWALL",
            "STABLE-SPACE CLOSURE",
            "DIMENSION FIREWALL",
            "COHOMOLOGY FIREWALL",
            "FINITE-SCOUT PROVENANCE FIREWALL",
            "No motivic isomorphism",
        ):
            self.assertIn(marker, text)

        resources = self.stored["resource_contract"]
        expected_actuals = {
            "source_files": 9,
            "branching_partitions": 11,
            "branching_row_tests": 35,
            "removable_corners": 19,
            "endoscopic_projection_terms": 11,
            "hook_boxes": 30,
            "symbolic_component_operations": 70,
            "finite_corroboration_rows": 3,
        }
        for key, value in expected_actuals.items():
            self.assertEqual(resources[key]["actual"], value)
            self.assertLessEqual(resources[key]["actual"], resources[key]["maximum"])
        self.assertEqual(resources["source_bytes"]["actual_total"], 174_029)
        self.assertEqual(
            resources["runtime_web_or_database_calls"], "FORBIDDEN_AND_NOT_PERFORMED"
        )
        self.assertEqual(
            resources["field_polynomial_curve_enumeration"],
            "FORBIDDEN_AND_NOT_PERFORMED",
        )
        source_text = MODULE_PATH.read_text(encoding="utf-8")
        for marker in (
            "import requests",
            "from requests",
            "urllib.request",
            "import httpx",
            "import sqlite3",
            "import subprocess",
        ):
            self.assertNotIn(marker, source_text)

    def test_caps_and_source_hash_failures_are_explicit(self) -> None:
        guard = subject.ResourceGuard(
            branching_partitions=subject.MAX_BRANCHING_PARTITIONS
        )
        with self.assertRaises(RuntimeError):
            guard.partition()
        bad_lock = dict(subject.SOURCE_LOCKS[0])
        bad_lock["payload_sha256"] = "0" * 64
        with self.assertRaises(ValueError):
            subject._load_locked_packet(bad_lock, subject.ResourceGuard())
        bad_marked_lock = dict(subject.MARKED_ZERO_LOCK)
        bad_marked_lock["lf_sha256"] = "0" * 64
        original = subject.MARKED_ZERO_LOCK
        subject.MARKED_ZERO_LOCK = bad_marked_lock
        try:
            with self.assertRaises(ValueError):
                subject._load_marked_zero(subject.ResourceGuard())
        finally:
            subject.MARKED_ZERO_LOCK = original


if __name__ == "__main__":
    unittest.main()
