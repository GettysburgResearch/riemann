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
    / "genus2_sym10_marked_trace_average.py"
)
OUTPUT_PATH = MODULE_PATH.with_suffix(".json")

SPEC = importlib.util.spec_from_file_location(
    "genus2_sym10_marked_trace_average", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load Sym10 marked-trace producer")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class Genus2Sym10MarkedTraceAverageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = MODULE.build_fixture()
        cls.disk = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))

    def test_fixture_is_canonical(self) -> None:
        self.assertEqual(self.fixture, self.disk)
        payload = dict(self.fixture)
        claimed = payload.pop("payload_sha256")
        self.assertEqual(claimed, MODULE._canonical_sha256(payload))

    def test_exact_all_q_theorem_and_normalization(self) -> None:
        definitions = self.fixture["definitions"]
        self.assertEqual(definitions["family_size"], "#H_5(q)=q^4*(q-1)")
        self.assertEqual(
            definitions["central_normalization"],
            "r_D(10)=q^5*chi_(10,0)(U_D)",
        )
        theorem = self.fixture["theorem"]
        self.assertEqual(
            theorem["marked_stack_trace"],
            "T_(10,0)(q)=(q-1)*Theta_Delta(q)-Theta_(8,2)(q)-Theta_(10,2)(q)-q-7",
        )
        self.assertEqual(
            theorem["reciprocal_total"],
            "sum_D r_D(10)=q*(q-1)*T_(10,0)(q)",
        )
        final = self.fixture["final_normalized_trace_expression"]
        self.assertEqual(final["tate"], [[-7, 1], [-1, 1]])
        self.assertEqual(final["Theta_Delta"], [[-1, 1], [1, 1]])
        self.assertEqual(final["Theta_(8,2)"], [[-1, 1]])
        self.assertEqual(final["Theta_(10,2)"], [[-1, 1]])

    def test_functional_equation_and_euler_recurrence(self) -> None:
        reduction = self.fixture["degree_ten_reciprocal_reduction"]
        self.assertEqual(
            reduction["even_functional_equation"],
            "C_5=(q-1)*(1+C_1+C_2+C_3)-C_4",
        )
        self.assertEqual(reduction["G_2"], [[0, 1]])
        formal = self.fixture["formal_euler_recurrence_certificate"]
        self.assertEqual(formal["ring"], "Z[q,s,N]")
        self.assertEqual(len(formal["g_10"]), 6)
        self.assertEqual(len(formal["lambda_10"]), 30)
        self.assertIn(
            {
                "q_degree": 0,
                "s_degree": 10,
                "N_degree": 0,
                "coefficient": 1,
            },
            formal["lambda_10"],
        )
        self.assertIn(
            {
                "q_degree": 4,
                "s_degree": 0,
                "N_degree": 1,
                "coefficient": -1,
            },
            formal["lambda_10"],
        )

    def test_cubic_channel_uses_marked_tower(self) -> None:
        cubic = self.fixture["cubic_channel_over_q_q_minus_1"]
        self.assertEqual(cubic["full_G_3"]["Theta_Delta"], [[-1, 1]])
        squarefree = cubic["squarefree_Lambda_3"]
        self.assertEqual(squarefree["tate"], [[-14, 1], [1, 1]])
        self.assertEqual(squarefree["Theta_Delta"], [[-1, 1]])
        self.assertEqual(squarefree["Theta_(8,2)"], [[-1, 1]])
        self.assertEqual(squarefree["Theta_(10,2)"], [[-1, 1]])
        full = cubic["full_Lambda_3"]
        self.assertEqual(full["tate"], [[0, 1], [-4, 1]])

    def test_quartic_telescope_and_repeated_strata(self) -> None:
        quartic = self.fixture["quartic_channel"]
        self.assertEqual(quartic["telescope_verified_in"], "Z[q,a]")
        self.assertEqual(quartic["repeated_count"], [[0, 1], [0, 1], [0, 1], [1, 1]])
        self.assertEqual(quartic["repeated_G4"], [[0, 1], [5, 1], [-6, 1], [1, 1]])
        self.assertEqual(
            quartic["full_G4_over_q_q_minus_1"]["Theta_Delta"],
            [[1, 1], [-1, 1]],
        )
        rows = quartic["repeated_strata"]
        self.assertEqual(
            [row["stratum"] for row in rows],
            [
                "L^4",
                "L^3*M",
                "L^2*M^2",
                "Q^2",
                "L^2*M*N",
                "L^2*Q",
            ],
        )
        signs = quartic["two_sign_sums_per_fixed_L"]
        self.assertEqual(signs["unordered_distinct_linear_pair"], [[1, 2], [-1, 2]])
        self.assertEqual(signs["irreducible_quadratic"], [[1, 2], [-1, 2]])

    def test_linear_modulus_markings(self) -> None:
        row = self.fixture["linear_modulus_channel"]
        self.assertEqual(row["lambda_10"], [[1, 1], [-1, 1]])
        self.assertEqual(
            row["binom_ell_2_lambda_10"],
            [[13, 2], [-17, 2], [2, 1]],
        )
        self.assertEqual(row["quadratic_factor_mark_kappa_10"], [[-1, 2], [1, 2]])
        self.assertEqual(row["Q_1"], [[0, 1], [7, 1], [-10, 1], [3, 1]])

    def test_reciprocal_coefficient_recurrence(self) -> None:
        for q, a_value, b_value in ((3, 0, -2), (5, 2, 3), (7, -4, 9), (11, 5, -6)):
            coefficients = [1]
            for degree in range(1, 11):
                coefficients.append(
                    MODULE.reciprocal_coefficient_10(a_value, b_value, q)
                    if degree == 10
                    else self._coefficient_at(degree, a_value, b_value, q)
                )
            numerator = [1, a_value, b_value, q * a_value, q * q]
            product = [0] * 11
            for left_index, left_value in enumerate(numerator):
                for right_index, right_value in enumerate(coefficients):
                    if left_index + right_index <= 10:
                        product[left_index + right_index] += left_value * right_value
            self.assertEqual(product, [1] + [0] * 10)

    @staticmethod
    def _coefficient_at(degree: int, a_value: int, b_value: int, q: int) -> int:
        values = [1]
        for index in range(1, degree + 1):
            value = -a_value * values[index - 1]
            if index >= 2:
                value -= b_value * values[index - 2]
            if index >= 3:
                value -= q * a_value * values[index - 3]
            if index >= 4:
                value -= q * q * values[index - 4]
            values.append(value)
        return values[degree]

    def test_modular_forms_and_prime_power_consequence(self) -> None:
        modular = self.fixture["modular_form_certificate"]
        self.assertEqual(
            modular["f_(8,2)_coefficients_0_through_9"],
            [0, 1, -8, 12, 64, -210, -96, 1016, -512, -2043],
        )
        self.assertEqual(
            modular["g_(10,2)_coefficients_0_through_9"],
            [0, 1, 16, -156, 256, 870, -2496, -952, 4096, 4653],
        )
        self.assertEqual(modular["q_9"]["Theta_Delta(9)"], -290790)
        self.assertEqual(modular["q_9"]["Theta_(8,2)(9)"], -4230)
        self.assertEqual(modular["q_9"]["Theta_(10,2)(9)"], -15030)
        self.assertEqual(modular["q_9"]["T_(10,0)(9)"], -2307076)

    def test_held_out_controls_are_proof_independent(self) -> None:
        rows = self.fixture["held_out_falsification_controls"]
        self.assertEqual(
            [
                (row["q"], row["theorem_T_(10,0)"], row["theorem_sum_r_D_10"])
                for row in rows
            ],
            [(3, 638, 3828), (5, 18648, 372960), (7, -100542, -4222764)],
        )
        self.assertEqual([row["difference"] for row in rows], [0, 0, 0])
        self.assertEqual(sum(row["joint_law_atoms"] for row in rows), 251)
        self.assertTrue(
            all(row["status"] == "HELD_OUT_FALSIFICATION_CONTROL_ONLY" for row in rows)
        )
        self.assertEqual(
            self.fixture["scope"]["sampled_q_values_used_as_theorem_input"], []
        )

    def test_controls_load_only_after_proof_and_modular_certificate(self) -> None:
        events: list[tuple[str, tuple[str, ...] | None]] = []
        original_load = MODULE._load_sources
        original_symbolic = MODULE._build_symbolic_theorem
        original_modular = MODULE._build_modular_certificate

        def observed_load(names: tuple[str, ...]) -> dict[str, dict[str, object]]:
            events.append(("load", names))
            return original_load(names)

        def observed_symbolic(sources: object, guard: object) -> object:
            result = original_symbolic(sources, guard)
            events.append(("symbolic_closed", None))
            return result

        def observed_modular(source: object, guard: object) -> object:
            result = original_modular(source, guard)
            events.append(("modular_closed", None))
            return result

        with (
            mock.patch.object(MODULE, "_load_sources", side_effect=observed_load),
            mock.patch.object(
                MODULE, "_build_symbolic_theorem", side_effect=observed_symbolic
            ),
            mock.patch.object(
                MODULE, "_build_modular_certificate", side_effect=observed_modular
            ),
        ):
            MODULE.build_fixture()

        theorem_load = ("load", MODULE.THEOREM_SOURCE_NAMES)
        control_load = ("load", MODULE.HELD_OUT_SOURCE_NAMES)
        self.assertLess(
            events.index(theorem_load), events.index(("symbolic_closed", None))
        )
        self.assertLess(
            events.index(("symbolic_closed", None)),
            events.index(("modular_closed", None)),
        )
        self.assertLess(
            events.index(("modular_closed", None)), events.index(control_load)
        )

    def test_resource_caps_and_firewalls(self) -> None:
        contract = self.fixture["resource_contract"]
        self.assertLessEqual(
            contract["actual_exact_operations"], contract["maximum_exact_operations"]
        )
        self.assertEqual(contract["actual_held_out_atoms"], 251)
        self.assertEqual(contract["actual_reciprocal_updates"], 2510)
        self.assertEqual(contract["new_finite_fields_enumerated"], [])
        text = " ".join(self.fixture["firewalls"])
        self.assertIn("not a memberwise sign theorem", text)
        self.assertIn("No external novelty claim", text)
        self.assertIn("no RH, GRH", text)

    def test_polynomial_helpers_are_exact(self) -> None:
        guard = MODULE.ResourceGuard()
        left = MODULE.poly(1, -2, 1)
        right = MODULE.poly(-1, 1)
        self.assertEqual(MODULE.p_mul(right, right, guard), left)
        self.assertEqual(MODULE.p_eval(left, 7), Fraction(36))


if __name__ == "__main__":
    unittest.main()
