from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from fractions import Fraction
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "genus2_sym6_marked_trace_average.py"
)
OUTPUT_PATH = MODULE_PATH.with_suffix(".json")

SPEC = importlib.util.spec_from_file_location(
    "genus2_sym6_marked_trace_average", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load Sym6 marked-trace producer")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class Genus2Sym6MarkedTraceAverageTests(unittest.TestCase):
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

    def test_all_q_theorem_polynomial(self) -> None:
        rows = self.fixture["polynomials_low_to_high"]
        self.assertEqual(rows["all_cubic_g6"], [[0, 1]])
        self.assertEqual(
            rows["all_cubic_ell6"],
            [[0, 1], [0, 1], [2, 1], [-2, 1]],
        )
        self.assertEqual(
            rows["reciprocal_total"],
            [[0, 1], [4, 1], [-4, 1]],
        )
        self.assertEqual(
            self.fixture["theorem"]["marked_stack_trace"],
            "T_(6,0)(q)=-4",
        )

    def test_reciprocal_raw_identity(self) -> None:
        for q, a_value, b_value in (
            (3, 0, -2),
            (5, 2, 3),
            (7, -4, 9),
            (11, 5, -6),
        ):
            recurrence = MODULE.reciprocal_coefficient_6(a_value, b_value, q)
            expanded = (
                a_value**6
                - 5 * a_value**4 * b_value
                + 4 * q * a_value**4
                + 6 * a_value**2 * b_value**2
                - 6 * q * a_value**2 * b_value
                - 2 * q**2 * a_value**2
                - b_value**3
                + 2 * q**2 * b_value
            )
            self.assertEqual(recurrence, expanded)

    def test_held_out_controls_are_not_inputs(self) -> None:
        rows = self.fixture["held_out_falsification_controls"]
        self.assertEqual([row["q"] for row in rows], [3, 5, 7])
        self.assertEqual([row["difference"] for row in rows], [0, 0, 0])
        self.assertTrue(
            all(row["status"] == "HELD_OUT_FALSIFICATION_CONTROL_ONLY" for row in rows)
        )
        self.assertEqual(
            self.fixture["scope"]["sampled_q_values_used_as_theorem_input"], []
        )

    def test_control_fixture_is_loaded_only_after_symbolic_theorem(self) -> None:
        events: list[tuple[str, ...]] = []
        original_load_sources = MODULE._load_sources
        original_symbolic_theorem = MODULE._symbolic_theorem

        def recording_load_sources(names: tuple[str, ...]):
            events.append(("load", *names))
            return original_load_sources(names)

        def recording_symbolic_theorem(guard):
            events.append(("symbolic_theorem",))
            return original_symbolic_theorem(guard)

        with (
            patch.object(MODULE, "_load_sources", recording_load_sources),
            patch.object(MODULE, "_symbolic_theorem", recording_symbolic_theorem),
        ):
            MODULE.build_fixture()

        self.assertLess(
            events.index(("symbolic_theorem",)), events.index(("load", "controls"))
        )
        self.assertTrue(
            self.fixture["resource_contract"][
                "held_out_fixture_loaded_after_symbolic_theorem"
            ]
        )

    def test_resource_cap(self) -> None:
        contract = self.fixture["resource_contract"]
        self.assertLessEqual(
            contract["actual_operations_and_input_atoms"],
            contract["maximum_symbolic_operations_and_input_atoms"],
        )
        self.assertGreater(contract["actual_held_out_input_atoms"], 0)

    def test_polynomial_helpers(self) -> None:
        guard = MODULE.ResourceGuard()
        left = MODULE.poly(1, -2, 1)
        right = MODULE.poly(-1, 1)
        self.assertEqual(MODULE.p_mul(right, right, guard), left)
        self.assertEqual(MODULE.p_eval(left, 7), Fraction(36))

    def test_firewalls(self) -> None:
        text = " ".join(self.fixture["firewalls"])
        self.assertIn("not a memberwise sign theorem", text)
        self.assertIn("not inferred from three-field interpolation", text)
        self.assertIn("no RH, GRH", text)


if __name__ == "__main__":
    unittest.main()
