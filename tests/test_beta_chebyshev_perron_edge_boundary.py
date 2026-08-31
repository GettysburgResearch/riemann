from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "beta_chebyshev_perron_edge_boundary.py"
)


def load_module():
    spec = importlib.util.spec_from_file_location("beta_chebyshev_perron_edge_boundary", MODULE_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class BetaChebyshevPerronEdgeTests(unittest.TestCase):
    def test_payload(self) -> None:
        module = load_module()
        payload = module.build_payload()
        self.assertEqual(
            payload["classification"],
            "PASS_T108000_BETA_CHEBYSHEV_PERRON_EDGE_BOUNDARY",
        )
        self.assertTrue(payload["subthreshold_boundary_proved"])
        self.assertTrue(payload["plemelj_jump_proved"])
        self.assertTrue(payload["all_threshold_coefficients_proved"])
        self.assertTrue(payload["closed_boundary_profile_zero_free_proved"])
        self.assertFalse(payload["finite_edge_airy_asymptotic_proved"])
        self.assertFalse(payload["beta_source_cancellation_proved"])
        self.assertFalse(payload["rh_established"])

    def test_retained_output(self) -> None:
        module = load_module()
        expected = module.json.dumps(
            module.build_payload(), indent=2, sort_keys=True
        ) + "\n"
        self.assertEqual(module.OUTPUT.read_text(), expected)


if __name__ == "__main__":
    unittest.main()
