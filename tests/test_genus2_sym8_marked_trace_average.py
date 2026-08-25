from __future__ import annotations

import importlib.util
import json
import sys
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
    / "genus2_sym8_marked_trace_average.py"
)
OUTPUT_PATH = MODULE_PATH.with_suffix(".json")

SPEC = importlib.util.spec_from_file_location(
    "genus2_sym8_marked_trace_average", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load Sym8 marked-trace producer")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class Genus2Sym8MarkedTraceAverageTests(unittest.TestCase):
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

    def test_exact_reduction_to_marked_cubic_sixth_moment(self) -> None:
        rows = self.fixture["polynomials_low_to_high"]
        self.assertEqual(rows["all_cubic_g8"], [[0, 1]])
        self.assertEqual(rows["degree_2_g8"], [[0, 1]])
        self.assertEqual(
            self.fixture["mobius_euler_reduction"]["direct_reduction"],
            "sum_D r_D(8)=J_6-q*(q-1)*(5*q^4-5*q^3-18*q^2-9*q+4)",
        )
        self.assertEqual(
            self.fixture["theorem"]["marked_stack_trace"],
            "T_(8,0)(q)=-Theta_(8,2)(q)-q-6",
        )

    def test_euler_recurrence_is_derived_formally(self) -> None:
        certificate = self.fixture["formal_euler_recurrence_certificate"]
        self.assertEqual(certificate["ring"], "Z[q,s,N]")
        self.assertEqual(len(certificate["g_8"]), 5)
        self.assertEqual(len(certificate["lambda_8"]), 20)
        self.assertIn(
            {
                "q_degree": 0,
                "s_degree": 8,
                "N_degree": 0,
                "coefficient": 1,
            },
            certificate["lambda_8"],
        )
        self.assertIn(
            {
                "q_degree": 2,
                "s_degree": 2,
                "N_degree": 1,
                "coefficient": -6,
            },
            certificate["lambda_8"],
        )

    def test_reciprocal_raw_identity(self) -> None:
        for q, a_value, b_value in (
            (3, 0, -2),
            (5, 2, 3),
            (7, -4, 9),
            (11, 5, -6),
        ):
            recurrence = MODULE.reciprocal_coefficient_8(a_value, b_value, q)
            expanded = (
                a_value**8
                - 7 * a_value**6 * b_value
                + 6 * q * a_value**6
                + 15 * a_value**4 * b_value**2
                - 20 * q * a_value**4 * b_value
                + q**2 * a_value**4
                - 10 * a_value**2 * b_value**3
                + 12 * q * a_value**2 * b_value**2
                + 9 * q**2 * a_value**2 * b_value
                - 6 * q**3 * a_value**2
                + b_value**4
                - 3 * q**2 * b_value**2
                + q**4
            )
            self.assertEqual(recurrence, expanded)

    def test_eta_product_and_prime_power_trace(self) -> None:
        certificate = self.fixture["eta_product_certificate"]
        self.assertEqual(
            certificate["independent_truncated_product_coefficients_c_0_through_c_9"],
            [0, 1, -8, 12, 64, -210, -96, 1016, -512, -2043],
        )
        consequence = self.fixture["prime_power_consequence"]
        self.assertEqual(consequence["Theta_(8,2)(9)"], -4230)
        self.assertEqual(consequence["T_(8,0)(9)"], 4215)
        self.assertEqual(
            consequence["status"], "THEOREM_CONSEQUENCE_NOT_FIELD_ENUMERATION"
        )

    def test_held_out_controls_are_not_inputs(self) -> None:
        rows = self.fixture["held_out_falsification_controls"]
        self.assertEqual([row["q"] for row in rows], [3, 5, 7])
        self.assertEqual([row["difference"] for row in rows], [0, 0, 0])
        self.assertEqual(sum(row["joint_law_atoms"] for row in rows), 251)
        self.assertTrue(
            all(row["observed_sum_r_D_8"] == row["theorem_sum_r_D_8"] for row in rows)
        )
        self.assertTrue(
            all(row["status"] == "HELD_OUT_FALSIFICATION_CONTROL_ONLY" for row in rows)
        )
        self.assertEqual(
            self.fixture["scope"]["sampled_q_values_used_as_theorem_input"], []
        )

    def test_held_out_sources_are_loaded_after_proof_and_eta(self) -> None:
        events: list[tuple[str, tuple[str, ...] | None]] = []
        original_load = MODULE._load_sources
        original_theorem = MODULE._symbolic_theorem
        original_eta = MODULE.eta_product_coefficients

        def observed_load(names: tuple[str, ...]) -> dict[str, dict[str, object]]:
            events.append(("load", names))
            return original_load(names)

        def observed_theorem(guard: object) -> object:
            result = original_theorem(guard)
            events.append(("theorem_closed", None))
            return result

        def observed_eta(max_degree: int, guard: object) -> list[int]:
            result = original_eta(max_degree, guard)
            events.append(("eta_closed", None))
            return result

        with (
            mock.patch.object(MODULE, "_load_sources", side_effect=observed_load),
            mock.patch.object(
                MODULE, "_symbolic_theorem", side_effect=observed_theorem
            ),
            mock.patch.object(
                MODULE,
                "eta_product_coefficients",
                side_effect=observed_eta,
            ),
        ):
            MODULE.build_fixture()

        theorem_load = ("load", MODULE.THEOREM_SOURCE_NAMES)
        held_out_load = ("load", MODULE.HELD_OUT_SOURCE_NAMES)
        self.assertEqual(events.count(theorem_load), 1)
        self.assertEqual(events.count(held_out_load), 1)
        self.assertLess(
            events.index(theorem_load), events.index(("theorem_closed", None))
        )
        self.assertLess(
            events.index(("theorem_closed", None)), events.index(("eta_closed", None))
        )
        self.assertLess(events.index(("eta_closed", None)), events.index(held_out_load))

    def test_resource_cap(self) -> None:
        contract = self.fixture["resource_contract"]
        self.assertLessEqual(
            contract["actual_operations_and_input_atoms"],
            contract["maximum_symbolic_operations_and_input_atoms"],
        )
        self.assertLess(
            contract["actual_symbolic_operations_before_eta_expansion"],
            contract["actual_symbolic_operations_before_controls"],
        )
        self.assertEqual(contract["actual_held_out_input_atoms"], 254)

    def test_polynomial_helpers(self) -> None:
        guard = MODULE.ResourceGuard()
        left = MODULE.poly(1, -2, 1)
        right = MODULE.poly(-1, 1)
        self.assertEqual(MODULE.p_mul(right, right, guard), left)
        self.assertEqual(MODULE.p_eval(left, 7), Fraction(36))

    def test_firewalls(self) -> None:
        text = " ".join(self.fixture["firewalls"])
        self.assertIn("not a memberwise sign theorem", text)
        self.assertIn("no RH, GRH", text)
        self.assertIn("not inferred from three-field interpolation", text)
        self.assertIn("not enumerated", text)


if __name__ == "__main__":
    unittest.main()
