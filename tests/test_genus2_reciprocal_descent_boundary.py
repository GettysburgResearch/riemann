from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
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
    / "genus2_reciprocal_descent_boundary.py"
)
OUTPUT_PATH = MODULE_PATH.with_suffix(".json")

SPEC = importlib.util.spec_from_file_location(
    "genus2_reciprocal_descent_boundary", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load reciprocal-descent boundary producer")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class Genus2ReciprocalDescentBoundaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = MODULE.build_fixture()
        cls.disk = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))

    def test_fixture_is_canonical(self) -> None:
        self.assertEqual(self.fixture, self.disk)
        claimed = self.fixture["payload_sha256"]
        payload = dict(self.fixture)
        payload.pop("payload_sha256")
        self.assertEqual(claimed, MODULE._canonical_sha256(payload))

    def test_squarefree_quintic_sieve_is_derived_exactly(self) -> None:
        sieve = self.fixture["squarefree_quintic_sieve"]
        self.assertEqual(
            sieve["identity"],
            "S_5(f)=C_5(f)-(q-ell(f))*C_3(f)+(binom(ell(f)+1,2)+k(f)-q*ell(f))*C_1(f)",
        )
        self.assertEqual(sieve["degree_A_2_closed_form"], "binom(ell+1,2)+k-q*ell")
        terms = sieve["degree_A_2_signed_count"]
        self.assertIn({"coefficient": 1, "powers": {"k": 1}}, terms)
        self.assertIn({"coefficient": -1, "powers": {"ell": 1, "q": 1}}, terms)
        self.assertIn({"coefficient": "1/2", "powers": {"ell": 1}}, terms)
        self.assertIn({"coefficient": "1/2", "powers": {"ell": 2}}, terms)

    def test_exact_functional_equation_phase_panel(self) -> None:
        rows = {
            row["endpoint_d"]: row for row in self.fixture["functional_equation_panel"]
        }
        self.assertEqual(sorted(rows), list(range(2, 21, 2)))
        self.assertEqual(rows[6]["C5_formula"], "C_5=-q^2")
        self.assertEqual(rows[8]["C5_formula"], "C_5=q*(q-1)*(1+C_1)-q*C_2")
        self.assertEqual(
            rows[10]["C5_formula"],
            "C_5=(q-1)*(1+C_1+C_2+C_3)-C_4",
        )
        self.assertTrue(
            all(
                rows[endpoint]["functional_equation_eliminates_C5"]
                for endpoint in range(2, 11, 2)
            )
        )
        self.assertTrue(
            all(
                not rows[endpoint]["functional_equation_eliminates_C5"]
                for endpoint in range(12, 21, 2)
            )
        )
        self.assertEqual(rows[12]["status"], "FREE_CENTRAL_COMPLETED_COEFFICIENT")
        self.assertTrue(
            all(
                rows[endpoint]["status"] == "FREE_PRECENTRAL_COMPLETED_COEFFICIENT"
                for endpoint in range(14, 21, 2)
            )
        )

    def test_non_determination_witnesses_are_exact_and_reciprocal(self) -> None:
        for row in self.fixture["functional_equation_panel"]:
            endpoint = row["endpoint_d"]
            if endpoint < 12:
                self.assertNotIn("non_determination_witness", row)
                continue
            witness = row["non_determination_witness"]
            self.assertEqual(
                witness["common_C_0_through_C_4"],
                ["1", "-1", "0", "0", "0"],
            )
            self.assertEqual(witness["first_C_5"], "0")
            self.assertEqual(witness["second_C_5"], "1")
            self.assertTrue(witness["both_completed_functional_equations_verified"])
            self.assertEqual(
                witness["realizability_status"],
                "FORMAL_FUNCTIONAL_EQUATION_WITNESS_ONLY",
            )

        central_terms = self.fixture["functional_equation_panel"][5][
            "non_determination_witness"
        ]["second_completion_added_terms"]
        self.assertEqual(central_terms, [{"Q_index": 5, "coefficient": "1"}])

    def test_target_cancels_and_only_a_consistency_identity_remains(self) -> None:
        certificate = self.fixture["self_reference_certificate"]
        self.assertEqual(certificate["degree_five_split"], "G5_d=T_d+R5_d")
        self.assertEqual(certificate["target_coefficient_after_substitution"], 0)
        self.assertEqual(
            certificate["consistency_identity"],
            "R5_d-q*G3_d+Lambda3_d+Q1_d=0",
        )
        residual = certificate["exact_residual_sparse_polynomial"]
        self.assertFalse(any("T_d" in term["powers"] for term in residual))

    def test_sym6_and_sym8_are_post_proof_source_locks(self) -> None:
        checks = self.fixture["source_cross_checks"]
        self.assertEqual(checks["sym6"]["cross_checked_formula"], "C_5=-q^2")
        self.assertEqual(
            checks["sym8"]["cross_checked_formula"],
            "C_5=q*(q-1)*(1+C_1)-q*C_2",
        )
        self.assertEqual(
            checks["sym10"]["source_status"],
            "DERIVED_INDEPENDENTLY_NOT_IMPORTED",
        )
        self.assertFalse(
            self.fixture["source_order_firewall"]["untracked_Sym10_used_as_input"]
        )
        self.assertEqual(
            [row["name"] for row in self.fixture["source_manifest"]],
            ["sym6", "sym8"],
        )

    def test_sources_are_loaded_only_after_formal_boundary_closes(self) -> None:
        events: list[str] = []
        original_panel = MODULE._derive_phase_panel
        original_self_reference = MODULE._derive_self_reference
        original_load = MODULE._load_sources

        def observed_panel(guard: object) -> object:
            result = original_panel(guard)
            events.append("panel_closed")
            return result

        def observed_self_reference(guard: object) -> object:
            result = original_self_reference(guard)
            events.append("self_reference_closed")
            return result

        def observed_load(guard: object) -> object:
            events.append("sources_loaded")
            return original_load(guard)

        with (
            mock.patch.object(
                MODULE, "_derive_phase_panel", side_effect=observed_panel
            ),
            mock.patch.object(
                MODULE,
                "_derive_self_reference",
                side_effect=observed_self_reference,
            ),
            mock.patch.object(MODULE, "_load_sources", side_effect=observed_load),
        ):
            MODULE.build_fixture()

        self.assertLess(events.index("panel_closed"), events.index("sources_loaded"))
        self.assertLess(
            events.index("self_reference_closed"), events.index("sources_loaded")
        )

    def test_resource_caps_and_firewalls(self) -> None:
        contract = self.fixture["resource_contract"]
        self.assertLessEqual(
            contract["actual_symbolic_operations"],
            contract["maximum_symbolic_operations"],
        )
        self.assertLessEqual(
            contract["actual_source_atoms"], contract["maximum_source_atoms"]
        )
        self.assertLessEqual(
            contract["actual_source_bytes"], contract["maximum_source_bytes"]
        )
        self.assertEqual(self.fixture["scope"]["finite_fields_enumerated"], 0)
        firewalls = " ".join(self.fixture["firewalls"])
        self.assertIn("not an impossibility theorem", firewalls)
        self.assertIn("not asserted to be realized", firewalls)
        self.assertIn("No memberwise sign, RH, GRH", firewalls)

    def test_audited_resource_and_documentation_repairs(self) -> None:
        definitions = self.fixture["definitions"]
        self.assertEqual(
            definitions["sum_convention"],
            "every polynomial sum is over monic polynomials",
        )
        self.assertIn("Lambda3_d=sum_", definitions["degree_three_marked_row"])
        self.assertIn("Q1_d=sum_", definitions["degree_one_combined_row"])

        replay = self.fixture["replay"]
        prefix = (
            "python research/l-families/atlas/function_field/"
            "genus2_reciprocal_descent_boundary.py"
        )
        self.assertEqual(replay["write"], f"{prefix} --write")
        self.assertEqual(replay["check"], f"{prefix} --check")

        note = MODULE.NOTE_PATH.read_text(encoding="utf-8")
        self.assertIn(r"\(2\le d\le20\)", note)
        self.assertIn(r"\(d\ge12\)", note)
        self.assertNotIn("2le dle20", note)
        self.assertNotIn("Sym(^{", note)

    def test_source_read_is_bounded_before_hashing(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "oversize.json"
            path.write_bytes(b"x" * 64)
            lock = {
                "path": path,
                "lf_sha256": "unused",
                "payload_sha256": "unused",
                "audited_commit": "unused",
            }
            with (
                mock.patch.object(MODULE, "MAX_SOURCE_BYTES", 8),
                mock.patch.object(MODULE, "SOURCE_LOCKS", {"oversize": lock}),
                self.assertRaisesRegex(RuntimeError, "before full read"),
            ):
                MODULE._load_sources(MODULE.ResourceGuard())

    def test_wall_cap_is_checked_after_final_payload_hash(self) -> None:
        events: list[str] = []
        original_hash = MODULE._canonical_sha256

        def observed_hash(value: object) -> str:
            if (
                isinstance(value, dict)
                and value.get("schema") == self.fixture["schema"]
            ):
                events.append("final_payload_hashed")
            return original_hash(value)

        with (
            mock.patch.object(MODULE, "_canonical_sha256", side_effect=observed_hash),
            mock.patch.object(MODULE.time, "perf_counter", side_effect=[0.0, 4.0]),
            self.assertRaisesRegex(RuntimeError, "wall cap"),
        ):
            MODULE.build_fixture()
        self.assertEqual(events, ["final_payload_hashed"])

    def test_sparse_ring_rejects_nonlinear_coefficient_extraction(self) -> None:
        guard = MODULE.ResourceGuard()
        ring = MODULE.PolynomialRing(("x",), guard)
        x = ring.variable("x")
        with self.assertRaises(ArithmeticError):
            ring.coefficient_of_variable(ring.mul(x, x), "x")
        self.assertEqual(ring.scale(x, Fraction(1, 2)), {(1,): Fraction(1, 2)})


if __name__ == "__main__":
    unittest.main()
