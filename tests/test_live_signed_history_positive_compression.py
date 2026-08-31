from __future__ import annotations

import hashlib
import importlib.util
import json
import unittest
from fractions import Fraction
from pathlib import Path

MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "research"
    / "riemann-structures"
    / "live_signed_history_positive_compression.py"
)


def load_module():
    spec = importlib.util.spec_from_file_location(
        "live_signed_history_positive_compression",
        MODULE_PATH,
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class LiveSignedHistoryPositiveCompressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()
        cls.payload = cls.module.build_payload()

    def test_classification_and_boundary(self) -> None:
        payload = self.payload
        self.assertEqual(
            payload["classification"],
            "PASS_T108102_LIVE_SIGNED_HISTORY_POSITIVE_COMPRESSION",
        )
        self.assertTrue(payload["live_source_bound_to_positive_quotient"])
        self.assertTrue(payload["factor_4225_input_energy_compression_proved"])
        self.assertTrue(
            payload["complete_one_cell_positive_negative_spectrum_proved"]
        )
        self.assertTrue(payload["zero_sum_subpacket_has_zero_positive_debt"])
        self.assertFalse(payload["full_live_fibre_positive_trace_evaluated"])
        self.assertFalse(payload["signed_conductor_recombination_proved"])
        self.assertFalse(payload["principal_binding_proved"])
        self.assertFalse(payload["rh_established"])
        self.assertFalse(payload["grh_established"])

    def test_live_exact_invariants(self) -> None:
        module = self.module
        self.assertEqual(len(module.LIVE_RATIOS), 100)
        self.assertEqual(module.signed_total(module.LIVE_RATIOS), 4)
        self.assertEqual(module.diagonal_energy(module.LIVE_RATIOS), 676)
        self.assertEqual(
            module.atomic_diagonal(module.LIVE_ELL, module.LIVE_RHO),
            Fraction(535600, 537151),
        )

    def test_factor_4225_projection(self) -> None:
        ledger = self.module.ambient_projection_ledger(
            self.module.LIVE_RATIOS,
            100,
        )
        self.assertEqual(ledger["quotient_input_energy"], "4/25")
        self.assertEqual(ledger["kernel_energy"], "16896/25")
        self.assertEqual(ledger["aggregation_coherence"], "1/4225")

    def test_one_cell_ledger(self) -> None:
        diagonal = self.module.atomic_diagonal(
            self.module.LIVE_ELL,
            self.module.LIVE_RHO,
        )
        ledger = self.module.complete_one_cell_ledger(
            self.module.LIVE_RATIOS,
            diagonal,
        )
        self.assertEqual(ledger["negative_to_positive_ratio"], "128/3")
        self.assertEqual(ledger["full_magnitude_to_positive_ratio"], "125/3")
        self.assertEqual(
            ledger["full_wick_value"],
            "-353496000/537151",
        )

    def test_zero_sum_subpacket(self) -> None:
        diagonal = self.module.atomic_diagonal(
            self.module.LIVE_ELL,
            self.module.LIVE_RHO,
        )
        self.assertEqual(
            self.module.signed_total(self.module.ZERO_SUM_SUBPACKET),
            0,
        )
        self.assertEqual(
            self.module.direct_one_cell_wick(
                self.module.ZERO_SUM_SUBPACKET,
                diagonal,
            ),
            -12 * diagonal,
        )

    def test_proof_object(self) -> None:
        core = {
            "marked_conductors": self.payload["marked_conductors"],
            "live_history_block": self.payload["live_history_block"],
            "zero_sum_internal_subpacket": self.payload[
                "zero_sum_internal_subpacket"
            ],
        }
        expected = hashlib.sha256(
            json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest()
        self.assertEqual(self.payload["proof_object_sha256"], expected)

    def test_retained_output(self) -> None:
        expected = json.dumps(
            self.payload,
            indent=2,
            sort_keys=True,
        ) + "\n"
        self.assertEqual(self.module.OUTPUT.read_text(), expected)


if __name__ == "__main__":
    unittest.main()
