from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "research"
    / "riemann-structures"
    / "shared_fibre_positive_quotient.py"
)


def load_module():
    spec = importlib.util.spec_from_file_location(
        "shared_fibre_positive_quotient", MODULE_PATH
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class SharedFibrePositiveQuotientTests(unittest.TestCase):
    def test_payload(self) -> None:
        module = load_module()
        payload = module.build_payload()
        self.assertEqual(
            payload["classification"],
            "PASS_T108100_SHARED_FIBRE_POSITIVE_QUOTIENT",
        )
        self.assertTrue(payload["exact_atom_to_quotient_decomposition"])
        self.assertTrue(
            payload["positive_part_residue_sufficient_without_injectivity"]
        )
        self.assertTrue(payload["within_cell_history_debt_purely_negative"])
        self.assertTrue(payload["full_wick_operator_traceless"])
        self.assertTrue(payload["partial_frobenius_orbit_criterion_proved"])
        self.assertFalse(payload["signed_conductor_recombination_proved"])
        self.assertFalse(payload["rh_established"])

    def test_retained_output(self) -> None:
        module = load_module()
        expected = module.json.dumps(
            module.build_payload(), indent=2, sort_keys=True
        ) + "\n"
        self.assertEqual(module.OUTPUT.read_text(), expected)


if __name__ == "__main__":
    unittest.main()
