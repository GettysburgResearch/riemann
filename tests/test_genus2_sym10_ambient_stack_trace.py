"""Focused tests for the exact marked Sym10 ambient-stack trace packet."""

from __future__ import annotations

import importlib.util
import json
import sys
import time
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
PRODUCER_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "genus2_sym10_ambient_stack_trace.py"
)
FIXTURE_PATH = PRODUCER_PATH.with_suffix(".json")

SPEC = importlib.util.spec_from_file_location(
    "genus2_sym10_ambient_stack_trace", PRODUCER_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load Sym10 ambient-stack producer")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def _terms(rows: list[dict[str, int]]) -> dict[tuple[int, int, int, int], int]:
    return {
        (
            row["L_power"],
            row["Delta_power"],
            row["f_(8,2)_power"],
            row["g_(10,2)_power"],
        ): row["coefficient"]
        for row in rows
    }


class Genus2Sym10AmbientStackTraceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = MODULE.build_fixture()
        cls.disk = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))

    def test_fixture_replays_and_hashes_canonically(self) -> None:
        self.assertEqual(self.fixture, self.disk)
        payload = dict(self.fixture)
        claimed = payload.pop("payload_sha256")
        self.assertEqual(claimed, MODULE._canonical_sha256(payload))

    def test_exact_theorem_and_scope(self) -> None:
        self.assertEqual(
            self.fixture["status"],
            "PROVED_EXACT_AMBIENT_TRACE_ALL_ODD_PRIME_POWERS",
        )
        theorem = self.fixture["theorem"]
        self.assertEqual(
            theorem["formula"],
            "Tr(F_q,e_c(A_2(w^1),V_(10,0)))=2-4*q-2*q*Theta_Delta(q)",
        )
        self.assertEqual(theorem["quantifier"], "every odd prime power q")
        scope = self.fixture["scope"]
        self.assertEqual(scope["finite_fields_enumerated"], 0)
        self.assertEqual(scope["curves_enumerated"], 0)
        self.assertEqual(scope["cohomology_groups_enumerated"], 0)

    def test_sym10_branching_and_dimension(self) -> None:
        branch = self.fixture["exact_proof"]["branching_certificate"]
        self.assertEqual(branch["direct_composition_monomials"], 286)
        self.assertEqual(branch["total_dimension"], 286)
        self.assertEqual(
            branch["summand_dimensions"],
            [11, 20, 27, 32, 35, 36, 35, 32, 27, 20, 11],
        )
        self.assertEqual(sum(branch["summand_dimensions"]), 286)

    def test_level_two_old_new_decomposition(self) -> None:
        certificate = self.fixture["exact_proof"]["modular_dimension_certificate"]
        rows = {
            row["weight"]: (
                row["dim_S_level_1"],
                row["dim_S_Gamma0_2"],
                row["dim_old_Gamma0_2"],
                row["dim_new_Gamma0_2"],
            )
            for row in certificate["rows"]
        }
        self.assertEqual(
            rows,
            {
                4: (0, 0, 0, 0),
                6: (0, 0, 0, 0),
                8: (0, 1, 0, 1),
                10: (0, 1, 0, 1),
                12: (1, 2, 2, 0),
            },
        )
        self.assertEqual(
            certificate["identifications"]["weight_12_old"],
            "Delta(z) direct_sum Delta(2z)",
        )

    def test_eichler_shimura_boundary_rows(self) -> None:
        boundary = self.fixture["exact_proof"]["decomposable_boundary"]
        self.assertIn("no S_2 quotient", boundary["geometry"])
        inputs = boundary["standard_eichler_shimura_inputs"]
        self.assertEqual(inputs["A_1_W_r_even_positive"], "-S[r+2]-1")
        self.assertEqual(
            inputs["Y_0(2)_W_r_even_positive"],
            "-S[Gamma_0(2),r+2]-2",
        )
        rows = {row["i"]: row for row in boundary["rows"]}
        for odd in (1, 3, 5, 7, 9):
            self.assertEqual(rows[odd]["contribution"], [])
            self.assertTrue(rows[odd]["vanishes_by_unmarked_central_involution"])
        self.assertEqual(
            _terms(rows[6]["contribution"]),
            {(0, 0, 1, 0): 1, (0, 0, 0, 0): 2},
        )
        self.assertEqual(
            _terms(rows[8]["contribution"]),
            {(0, 0, 0, 1): 1, (0, 0, 0, 0): 2},
        )

    def test_boundary_and_ambient_formal_expressions(self) -> None:
        proof = self.fixture["exact_proof"]
        boundary = _terms(proof["decomposable_boundary"]["boundary_expression"])
        self.assertEqual(
            boundary,
            {
                (0, 0, 0, 0): 9,
                (1, 0, 0, 0): -3,
                (0, 1, 0, 0): 1,
                (1, 1, 0, 0): -3,
                (0, 0, 1, 0): 1,
                (0, 0, 0, 1): 1,
            },
        )
        ambient = _terms(proof["ambient_expression"])
        self.assertEqual(
            ambient,
            {
                (0, 0, 0, 0): 2,
                (1, 0, 0, 0): -4,
                (1, 1, 0, 0): -2,
            },
        )
        self.assertEqual(proof["channel_cancellation"]["Theta_(8,2)"], "-1+1=0")
        self.assertEqual(proof["channel_cancellation"]["Theta_(10,2)"], "-1+1=0")

    def test_modular_q_expansions_and_prime_power_trace(self) -> None:
        modular = self.fixture["exact_proof"]["modular_q_series_certificate"]
        coefficients = modular["coefficients_0_through_9"]
        self.assertEqual(
            coefficients["Delta"],
            [0, 1, -24, 252, -1472, 4830, -6048, -16744, 84480, -113643],
        )
        self.assertEqual(
            coefficients["f_(8,2)"],
            [0, 1, -8, 12, 64, -210, -96, 1016, -512, -2043],
        )
        self.assertEqual(
            coefficients["g_(10,2)"],
            [0, 1, 16, -156, 256, 870, -2496, -952, 4096, 4653],
        )
        self.assertEqual(
            MODULE._prime_power_trace(coefficients["Delta"], 12, 9), -290790
        )
        self.assertEqual(
            MODULE._prime_power_trace(coefficients["f_(8,2)"], 8, 9), -4230
        )
        self.assertEqual(
            MODULE._prime_power_trace(coefficients["g_(10,2)"], 10, 9), -15030
        )

    def test_q_3_5_7_9_controls(self) -> None:
        rows = self.fixture["exact_proof"]["controls"]
        self.assertEqual(
            [
                (
                    row["q"],
                    row["open_trace"],
                    row["boundary_trace"],
                    row["ambient_trace"],
                )
                for row in rows
            ],
            [
                (3, 638, -2160, -1522),
                (5, 18648, -66966, -48318),
                (7, -100542, 334932, 234390),
                (9, -2307076, 7541262, 5234186),
            ],
        )
        q9 = rows[-1]
        self.assertEqual(q9["Theta_Delta"], -290790)
        self.assertIn("FROBENIUS-ROOT POWER SUM", q9["status"])

    def test_source_locks_include_exact_commits(self) -> None:
        manifest = self.fixture["source_manifest"]
        by_id = {row["id"]: row for row in manifest}
        self.assertEqual(len(manifest), 12)
        self.assertEqual(
            by_id["sym10_json"]["commit"],
            "42910253be8173c6cd0de19a7a7403d0c31b5c22",
        )
        self.assertEqual(
            by_id["chi04_json"]["commit"],
            "e0da0f790f96f6dc5c03b363a9a01b91621ee113",
        )
        self.assertEqual(
            by_id["adapter_json"]["commit"],
            "c8eff406f49daf9f09c0bb3e63e21659275d224e",
        )
        self.assertTrue(all(len(row["git_blob"]) == 40 for row in manifest))

    def test_conjectural_compatibility_is_not_a_proof_input(self) -> None:
        dependency = self.fixture["proof_dependency_graph"]
        self.assertIn("BFG", dependency["explicit_non_input"])
        compatibility = self.fixture["BFG_compatibility"]
        self.assertEqual(
            compatibility["status"],
            "CONJECTURAL_COMPATIBILITY_ONLY_UNUSED_BY_EXACT_PROOF",
        )
        events: list[str] = []
        original_exact = MODULE._build_exact_proof
        original_compatibility = MODULE._build_compatibility_context

        def exact_wrapper(*args: object, **kwargs: object) -> object:
            result = original_exact(*args, **kwargs)
            events.append("exact_closed")
            return result

        def compatibility_wrapper(*args: object, **kwargs: object) -> object:
            events.append("compatibility_opened")
            return original_compatibility(*args, **kwargs)

        with (
            mock.patch.object(MODULE, "_build_exact_proof", side_effect=exact_wrapper),
            mock.patch.object(
                MODULE,
                "_build_compatibility_context",
                side_effect=compatibility_wrapper,
            ),
        ):
            MODULE.build_fixture()
        self.assertLess(
            events.index("exact_closed"), events.index("compatibility_opened")
        )

    def test_primary_source_ledger_preserves_logical_roles(self) -> None:
        ledger = self.fixture["primary_source_ledger"]
        self.assertEqual(len(ledger), 5)
        roles = {row["role_in_this_packet"] for row in ledger}
        self.assertIn("STANDARD_STACK_TRACE_INPUT", roles)
        self.assertIn("LEVEL_ONE_ELLIPTIC_EICHLER_SHIMURA_INPUT_ONLY", roles)
        self.assertIn("MODULI_DEFINITIONS_ONLY; CONJECTURAL_FORMULAS_UNUSED", roles)
        self.assertTrue(
            all("no network access" in row["replay_boundary"] for row in ledger)
        )

    def test_trace_vs_motive_firewall(self) -> None:
        text = " ".join(self.fixture["firewalls"])
        self.assertIn("not an isomorphism of motives", text)
        self.assertIn("does not exclude canceling cohomological pieces", text)
        self.assertIn("BFG compatibility is conjectural and unused", text)
        self.assertIn("No external novelty claim", text)

    def test_resource_caps_fail_closed(self) -> None:
        contract = self.fixture["provenance"]["resource_contract"]
        self.assertLessEqual(
            contract["actual_exact_operations"],
            contract["maximum_exact_operations"],
        )
        self.assertEqual(
            contract["actual_source_files"], contract["maximum_source_files"]
        )
        self.assertLessEqual(
            contract["actual_source_bytes"], contract["maximum_source_bytes_total"]
        )
        guard = MODULE.ResourceGuard()
        with self.assertRaises(RuntimeError):
            guard.operation("forced overflow", MODULE.MAX_EXACT_OPERATIONS + 1)
        with self.assertRaises(RuntimeError):
            guard.source(MODULE.MAX_SOURCE_BYTES_EACH + 1)
        expired = MODULE.Deadline(
            started=time.monotonic() - MODULE.MAX_WALL_SECONDS - 1.0
        )
        with self.assertRaises(RuntimeError):
            expired.check("forced expiry")

    def test_producer_uses_no_optimization_sensitive_asserts(self) -> None:
        source = PRODUCER_PATH.read_text(encoding="utf-8")
        self.assertNotIn("\n    assert ", source)
        self.assertNotIn("\nassert ", source)


if __name__ == "__main__":
    unittest.main()
