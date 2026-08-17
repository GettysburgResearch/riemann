from __future__ import annotations

import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve()
VERIFY_PATH = HERE.parents[1] / "verify.py"
spec = importlib.util.spec_from_file_location("x97300_verify", VERIFY_PATH)
verify = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(verify)


class ReconstructionTests(unittest.TestCase):
    def test_parity(self) -> None:
        self.assertTrue(all(verify.parity_and_owner_checks()["history_character_checks"].values()))

    def test_ratio(self) -> None:
        data = verify.ratio_symbolic_checks()
        self.assertLess(Fraction(data["tail_cancellation"]["2"]), 0)

    def test_scalar_tradeoff(self) -> None:
        data = verify.scalar_tradeoff_checks()
        self.assertLess(Fraction(data["scalar_exact"]["delta_row2"]), 0)
        self.assertGreater(Fraction(data["scalar_exact"]["delta_row3"]), 0)

    def test_imported_witnesses(self) -> None:
        data = verify.imported_certificate_checks()
        self.assertFalse(data["reverse_target_hall_feasible"])

    def test_lorenz(self) -> None:
        self.assertTrue(verify.lorenz_lp_checks()["greedy_equals_vertex_equals_dual"])

    def test_mutations(self) -> None:
        for mutation in verify.MUTATIONS:
            with self.assertRaises(verify.ContractError):
                verify.reject_mutation(mutation)

    def test_payload_status(self) -> None:
        payload = verify.build_payload()
        self.assertFalse(payload["former_candidate_complete_claim_survives"])
        self.assertFalse(payload["rh_established"])
        self.assertEqual(payload["verdict"], verify.VERDICT)


if __name__ == "__main__":
    unittest.main(verbosity=2)
