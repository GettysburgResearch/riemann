import importlib.util
from pathlib import Path
import unittest

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("verify", HERE / "verify.py")
verify = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verify)


class TestT99160(unittest.TestCase):
    def test_verdict_and_status(self):
        result = verify.build_result()
        self.assertEqual(
            result["verdict"],
            "PASS_T99160_SAME_ROW_DEFECT_RESOLVENT_AND_OVERTHINNING_FIREWALL",
        )
        self.assertFalse(result["rh_established"])

    def test_augmented_resolvent(self):
        result = verify.build_result()
        self.assertTrue(result["augmented_resolvent_exact"])
        self.assertEqual(result["equality_score"], "26")
        self.assertEqual(result["physical_score"], "47/2")
        self.assertEqual(result["defect_score"], "5/2")

    def test_overthinning_firewall(self):
        result = verify.build_result()
        self.assertFalse(result["voluntary_overthinning_repairs_inherited_stronger_row"])
        self.assertTrue(result["constant_thinning_claim_must_be_withdrawn_or_defected"])
        self.assertTrue(result["same_row_lock_required"])

    def test_compact_hall_fixture(self):
        self.assertTrue(verify.hall_gate())


if __name__ == "__main__":
    unittest.main()
