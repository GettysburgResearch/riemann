"""Focused optimized-safe tests for the finite Sym12 cusp-trace scout."""

from __future__ import annotations

import hashlib
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
    / "genus2_sym12_finite_cusp_trace_scout.py"
)
OUTPUT_PATH = MODULE_PATH.with_suffix(".json")

SPEC = importlib.util.spec_from_file_location(
    "genus2_sym12_finite_cusp_trace_scout", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load finite Sym12 scout producer")
subject = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = subject
SPEC.loader.exec_module(subject)


class Genus2Sym12FiniteCuspTraceScoutTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()
        cls.stored = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))

    def test_canonical_fixture_and_self_hash(self) -> None:
        self.assertEqual(self.fixture, self.stored)
        payload = dict(self.stored)
        claimed = payload.pop("payload_sha256")
        self.assertEqual(claimed, subject._canonical_sha256(payload))
        rendered = subject._serialized(self.stored)
        self.assertEqual(OUTPUT_PATH.read_text(encoding="utf-8"), rendered)
        self.assertLessEqual(len(rendered.encode("utf-8")), subject.MAX_OUTPUT_BYTES)

    def test_source_locks_are_exact_and_packet_sources_are_hashed(self) -> None:
        expected = {
            "balanced_joint_laws": {
                "commit": "955ea1e25160075fb4b498018319c80f7e4db9d5",
                "git_blob": "377c8c03d6a9ccf5a505a9b1a19acc360c59ff44",
                "sha256_lf_normalized": (
                    "c3494ae852fda4e754b3b0da7cb30a26e3e38ec1c87e2619cd6fee6cdc68b68e"
                ),
                "payload_sha256": (
                    "50fd136eb0483387246766c5f2426c3e727c69cd9a89943f9268368db0f9d39c"
                ),
            },
            "modular_trace_rows": {
                "commit": "42910253be8173c6cd0de19a7a7403d0c31b5c22",
                "git_blob": "561caa7dc504dfb158908aef9229e91af0707a1e",
                "sha256_lf_normalized": (
                    "4f91ac00193805207088e9fc6aea2b464645267b17dc54f71165a1ae3b9d45ce"
                ),
                "payload_sha256": (
                    "0fbf48768fdea477b2bee4f53c8f1e547a167155c665b5e97bc201961971ec77"
                ),
            },
            "sym12_arithmetic_inventory": {
                "commit": "70dd4a130e702a2d6df4b0fb96a0182a560009a4",
                "git_blob": "b48963d7b9bc6459046024507a2f2cb8ccbbcd40",
                "sha256_lf_normalized": (
                    "e966b54fe909570eaac7d9253f635c8067c5f874ed47c9daf485c8fd88bfbd85"
                ),
                "payload_sha256": (
                    "557ab6465a16bb6080caa2a249c3d0935f8d36fb49bdf54898a0fe72b372496f"
                ),
            },
        }
        manifest = {row["id"]: row for row in self.stored["source_manifest"]}
        self.assertEqual(set(manifest), set(expected))
        for source_id, sentinels in expected.items():
            for key, value in sentinels.items():
                self.assertEqual(manifest[source_id][key], value)
            path = ROOT / manifest[source_id]["path"]
            raw = path.read_bytes()
            self.assertEqual(
                subject._lf_sha256(raw),
                manifest[source_id]["sha256_lf_normalized"],
            )
            self.assertEqual(subject._git_blob(raw), manifest[source_id]["git_blob"])
            source_payload = json.loads(raw.decode("utf-8"))
            claimed = source_payload.pop("payload_sha256")
            self.assertEqual(claimed, manifest[source_id]["payload_sha256"])
            self.assertEqual(claimed, subject._canonical_sha256(source_payload))

        for packet_source in self.stored["packet_manifest"]:
            path = ROOT / packet_source["path"]
            normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            self.assertEqual(
                hashlib.sha256(normalized).hexdigest(),
                packet_source["sha256_lf_normalized"],
            )

    def test_reciprocal_recurrence_multiplies_back_to_one(self) -> None:
        for q, a_value, b_value in ((3, -3, 5), (5, 2, 3), (7, -4, 9)):
            reciprocal = subject.reciprocal_coefficients(q, a_value, b_value, 12)
            numerator = [1, a_value, b_value, q * a_value, q * q]
            product = [0] * 13
            for left_index, left_value in enumerate(numerator):
                for right_index, right_value in enumerate(reciprocal):
                    if left_index + right_index <= 12:
                        product[left_index + right_index] += left_value * right_value
            self.assertEqual(product, [1] + [0] * 12)

    def test_lower_recurrence_controls_and_degree_twelve_values(self) -> None:
        expected = {
            3: {
                "totals": [-24, -126, 3_828, -27_522],
                "T12": -4_587,
                "Hhat": -3_708,
                "H": -22_248,
            },
            5: {
                "totals": [-80, 3_980, 372_960, 5_345_020],
                "T12": 267_251,
                "Hhat": 287_250,
                "H": 5_745_000,
            },
            7: {
                "totals": [-168, -43_218, -4_222_764, -16_074_870],
                "T12": -382_735,
                "Hhat": -449_624,
                "H": -18_884_208,
            },
        }
        for row in self.stored["finite_rows"]:
            q = row["q"]
            totals = row["reciprocal_totals"]
            self.assertEqual(
                [
                    totals["sum_D_r_D(6)"],
                    totals["sum_D_r_D(8)"],
                    totals["sum_D_r_D(10)"],
                    totals["sum_D_r_D(12)"],
                ],
                expected[q]["totals"],
            )
            self.assertEqual(row["T_(12,0)"], expected[q]["T12"])
            self.assertEqual(row["Hhat_12"], expected[q]["Hhat"])
            self.assertEqual(row["H_12"], expected[q]["H"])
            self.assertIn("not a direct Q_5 average", row["Hhat_12_provenance"])
            self.assertTrue(
                all(
                    control["match"]
                    for control in row["lower_recurrence_checks"].values()
                )
            )

    def test_explicit_fricke_negative_q_expansion_and_finite_match(self) -> None:
        target = self.stored["explicit_weight_14_level_2_target"]
        self.assertEqual(target["Fricke_sign"], -1)
        self.assertEqual(
            target["coefficients_Q0_through_Q7"],
            [0, 1, 64, 1_236, 4_096, -57_450, 79_104, 64_232],
        )
        self.assertIn("f_-(Q)=", target["construction"])
        expected = {3: 1_236, 5: -57_450, 7: 64_232}
        for row in self.stored["finite_rows"]:
            q = row["q"]
            self.assertEqual(row["a_p(f_-)"], expected[q])
            self.assertEqual(row["Hhat_12"], -q * expected[q])
            self.assertEqual(row["-p*a_p(f_-)"], row["Hhat_12"])
            self.assertTrue(row["finite_match"])
        provenance = self.stored["coefficient_provenance"]
        self.assertFalse(provenance["database_orbit_label_used"])
        self.assertIn("Clery--van der Geer", provenance["primary_reference"])

    def test_resource_caps_are_exact_and_no_enumerator_is_imported(self) -> None:
        resources = self.stored["resource_contract"]
        expected_actuals = {
            "source_files": 3,
            "source_bytes": 219_771,
            "joint_law_atoms": 251,
            "reciprocal_updates": 3_012,
            "reciprocal_scalar_terms": 10_542,
            "weighted_accumulations": 1_004,
            "Eisenstein_divisor_tests": 56,
            "Eisenstein_divisor_terms": 32,
            "q_series_convolution_terms": 72,
            "q_series_linear_combinations": 8,
            "finite_row_checks": 3,
        }
        for name, expected in expected_actuals.items():
            key = "actual_total" if name == "source_bytes" else "actual"
            self.assertEqual(resources[name][key], expected)
            maximum_key = "maximum_total" if name == "source_bytes" else "maximum"
            self.assertLessEqual(resources[name][key], resources[name][maximum_key])
        self.assertEqual(resources["nonoverlapping_exact_step_total"], 11_685)
        self.assertIn("subset", resources["counter_nesting"])
        self.assertEqual(resources["new_q_values_enumerated"], [])
        self.assertEqual(
            resources["field_or_polynomial_enumeration"],
            "FORBIDDEN_AND_NOT_PERFORMED",
        )
        source_text = MODULE_PATH.read_text(encoding="utf-8")
        forbidden = (
            "import balanced_control_family_scan",
            "from balanced_control_family_scan",
            "import genus2_q_scan",
            "from genus2_q_scan",
            "itertools.product",
            "build_field_tables",
        )
        for marker in forbidden:
            self.assertNotIn(marker, source_text)

    def test_caps_and_source_hash_failures_raise_explicitly(self) -> None:
        guard = subject.ResourceGuard(reciprocal_updates=subject.MAX_RECIPROCAL_UPDATES)
        with self.assertRaises(RuntimeError):
            guard.recurrence(0)

        bad_lock = dict(subject.SOURCE_LOCKS[0])
        bad_lock["lf_sha256"] = "0" * 64
        with self.assertRaises(ValueError):
            subject._load_locked_source(bad_lock, subject.ResourceGuard())

    def test_finite_interpolation_and_prime_power_firewalls_are_literal(self) -> None:
        scope = self.stored["scope"]
        self.assertEqual(scope["tested_q_values"], [3, 5, 7])
        self.assertEqual(scope["all_q_statement"], "NOT_PROVED")
        self.assertEqual(scope["prime_power_statement"], "NOT_TESTED_AND_NOT_PROVED")
        text = " ".join(self.stored["firewalls"])
        self.assertIn("FINITE INTERPOLATION FIREWALL", text)
        self.assertIn("(q-3)*(q-5)*(q-7)", text)
        self.assertIn("PRIME-POWER FIREWALL", text)
        self.assertIn("not the naive composite-index Fourier coefficient", text)
        self.assertIn("No motive, compatible system", text)
        self.assertIn("PROVENANCE FIREWALL", text)
        provenance = self.stored["provenance_boundary"]
        self.assertIn("sum_D r_D(12)", provenance["directly_replayed"])
        self.assertIn("arithmetic-inventory", provenance["imported_exact_theorem"])
        self.assertIn("not an independent audit", provenance["logical_use"])
        self.assertIn("No RH, GRH", text)
        self.assertEqual(
            self.stored["finite_match"]["status"],
            "EXACT_THREE_PRIME_CONSEQUENCE_OF_RAW_T12_PLUS_INVENTORY_"
            "NOT_AN_INDEPENDENT_INVENTORY_AUDIT",
        )

    def test_inventory_conversion_drift_is_rejected(self) -> None:
        inventory = subject._load_locked_source(
            subject.SOURCE_LOCKS[2], subject.ResourceGuard()
        )
        subject._validate_inventory(inventory)
        damaged = dict(inventory)
        dependency = dict(damaged["degree_twelve_dependency"])
        dependency["marked_open_formula"] = "T_(12,0)=Hhat_12"
        damaged["degree_twelve_dependency"] = dependency
        with self.assertRaises(ValueError):
            subject._validate_inventory(damaged)


if __name__ == "__main__":
    unittest.main()
