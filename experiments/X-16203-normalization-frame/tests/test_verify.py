from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x16203_verify", ROOT / "verify.py")
assert SPEC is not None and SPEC.loader is not None
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


def certificate():
    return {
        "schema": module.SCHEMA,
        "chi": [3, 5],
        "positive_ray_components": [[2, 5], [2, 5]],
        "negative_ray_components": [[2, 5], [2, 5]],
        "defects": [1, 2, 5, 10, 17],
        "point_values": [2, 3, 5, 7, 11],
        "endpoint_ledger": {
            "p": 2,
            "derivative_l1_upper": 3,
            "zeta_tail_upper": [2, 3],
            "pi_lower": 3,
            "lambda": 2,
            "v": 2,
            "claimed_point_bound": [1, 72],
            "claimed_l2_sq_bound": [1, 7776],
        },
    }


class ExactAuditTests(unittest.TestCase):
    def test_valid(self):
        result = module.verify(certificate())
        self.assertEqual(result["leakage"]["positive_ray_norm_squared"], "8/25")
        self.assertEqual(result["frame"]["radical_dimension"], 3)
        self.assertEqual(result["endpoint_ledger"]["point_alias_bound"], "1/72")

    def test_wrong_leakage_rejected(self):
        payload = certificate()
        payload["positive_ray_components"][0] = [1, 5]
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_unequal_rays_rejected(self):
        payload = certificate()
        payload["negative_ray_components"][0] = [1, 5]
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_nonmonotone_defects_rejected(self):
        payload = certificate()
        payload["defects"][2] = 1
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_zero_point_value_rejected(self):
        payload = certificate()
        payload["point_values"][2] = 0
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_p_one_rejected(self):
        payload = certificate()
        payload["endpoint_ledger"]["p"] = 1
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_understated_point_bound_rejected(self):
        payload = certificate()
        payload["endpoint_ledger"]["claimed_point_bound"] = [1, 73]
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_understated_l2_bound_rejected(self):
        payload = certificate()
        payload["endpoint_ledger"]["claimed_l2_sq_bound"] = [1, 7777]
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_boolean_rejected(self):
        payload = certificate()
        payload["endpoint_ledger"]["p"] = True
        with self.assertRaises(module.CertificateError):
            module.verify(payload)


if __name__ == "__main__":
    unittest.main()
