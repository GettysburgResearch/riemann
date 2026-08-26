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
                "commit": "70dd4a130e702a2d6df4b0fb96a0182a560009a4",
                "git_blob": "b48963d7b9bc6459046024507a2f2cb8ccbbcd40",
                "sha256_lf_normalized": (
                    "e966b54fe909570eaac7d9253f635c8067c5f874ed47c9daf485c8fd88bfbd85"
                ),
                "payload_sha256": (
                    "557ab6465a16bb6080caa2a249c3d0935f8d36fb49bdf54898a0fe72b372496f"
                ),
            },
            "sym12_finite_scout": {
                "commit": "0e89f3ae989c0ef81f9f0fcfd359116d57f83f32",
                "git_blob": "4741ef79f8dd84634680df612cdd8b1d93d3e8bf",
                "sha256_lf_normalized": (
                    "8827b08f86fa0bd3a77698f250f9d40aea193a39b5c80e180f9a1f3acbac6ff9"
                ),
                "payload_sha256": (
                    "3572d443f7f5371771a0123b1ebcb1c08e010f02a65c3413d935216b1fcd3168"
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
            self.assertEqual(subject._git_blob(raw), row["git_blob"])
            source = json.loads(raw.decode("utf-8"))
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

    def test_stable_vanishing_is_only_conditional_data_evidence(self) -> None:
        stable = self.stored["stable_invariant_vanishing_evidence"]
        self.assertEqual(stable["total_dimension_checksum"], 30)
        self.assertEqual(stable["S5_invariant_dimension_from_these_rows"], 0)
        self.assertEqual(
            [row["S6_partition"] for row in stable["official_data_isotypical_rows"]],
            ["[3,1,1,1]", "[2,2,2]", "[2,2,1,1]", "[2,1,1,1,1]", "[1,1,1,1,1,1]"],
        )
        self.assertIn("CONDITIONAL", stable["source_grade"])
        self.assertIn("not imply", stable["dimension_firewall"])
        self.assertIn("do not evaluate", stable["negative_source_result"])
        self.assertIn("A2[w]=A2[2]/S5", stable["latest_structural_source"])
        self.assertIn("does not compute", stable["latest_structural_source"])
        self.assertEqual(stable["runtime_access"].split(";")[0], "NONE")

    def test_exact_conditional_iff_and_one_Tate_shift(self) -> None:
        algebra = self.stored["exact_internal_algebra"]
        project = algebra["project_ambient"]
        self.assertEqual(
            project["vector"],
            {"one": 2, "L": -5, "L_f_plus": -1, "L_f_minus": -1, "Hhat_12": 1},
        )
        general = algebra["master_target_before_specializing_the_two_open_channels"]
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
        closed = algebra["conditional_target_with_stable_vanishing"]
        self.assertEqual(closed["project_minus_target"], {"L_f_minus": 1, "Hhat_12": 1})
        self.assertEqual(closed["equality_iff"], "Hhat_12=-L*f_minus")
        self.assertIn("CONDITIONAL_PREMISES", closed["status"])
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
            self.assertTrue(row["BFG_match"])
            self.assertTrue(row["match"])
        self.assertEqual(
            finite["role"], "CORROBORATION_ONLY_NOT_A_PREMISE_AND_NOT_INTERPOLATION"
        )
        self.assertIn("do not prove", finite["firewall"])
        self.assertIn("misses each stored row by +p", finite["one_Tate_check"])

    def test_status_firewalls_caps_and_no_runtime_external_access(self) -> None:
        self.assertEqual(
            self.stored["status"],
            "EXACT_CONDITIONAL_REDUCTION_NOT_AN_ALL_Q_THEOREM",
        )
        statement = self.stored["conditional_statement"]
        self.assertEqual(statement["unconditional_conclusion"], "NONE")
        self.assertEqual(len(statement["premises"]), 3)
        self.assertEqual(len(statement["unresolved_premises"]), 2)
        self.assertIn("Epsilon_Eis-Genuine", statement["master_reduction"])
        self.assertIn("alpha_{-,p}^r", self.stored["prime_power_trace_convention"])
        text = " ".join(self.stored["firewalls"])
        for marker in (
            "CONDITIONAL-REDUCTION FIREWALL",
            "NONREGULAR FIREWALL",
            "ONE-TATE FIREWALL",
            "AMBIENT-NORMALIZATION FIREWALL",
            "STABLE-SPACE FIREWALL",
            "DIMENSION FIREWALL",
            "2026-STRUCTURAL FIREWALL",
            "FINITE-SCOUT FIREWALL",
            "No motivic isomorphism",
        ):
            self.assertIn(marker, text)

        resources = self.stored["resource_contract"]
        expected_actuals = {
            "source_files": 8,
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
        self.assertEqual(resources["source_bytes"]["actual_total"], 150_269)
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


if __name__ == "__main__":
    unittest.main()
