#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("slab_checker", ROOT / "verify_slab_complement.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MOD
SPEC.loader.exec_module(MOD)


def load(name: str):
    return json.loads((ROOT / "certificates" / name).read_text(encoding="utf-8"))


class SlabComplementTests(unittest.TestCase):
    def test_strict_separation_exact_negative(self):
        result = MOD.verify(load("synthetic-strict-separation.json"))
        self.assertEqual(result["status"], "CERTIFIED_NEGATIVE_SLAB_COMPLEMENT_WITNESS")
        self.assertEqual(result["ordinary_pick_interval"]["lower"], "7450901935000/47129216977")
        self.assertEqual(result["slab_complement_residual_interval"]["upper"], "-2956250/33337")

    def test_line_zero_control_positive(self):
        result = MOD.verify(load("synthetic-line-zero-control.json"))
        self.assertEqual(result["status"], "CERTIFIED_NONNEGATIVE_CONTROL")
        self.assertEqual(result["slab_complement_residual_interval"]["lower"], "40377630000/22251597721")

    def test_nonzero_vector_sum_rejected(self):
        payload = load("synthetic-strict-separation.json")
        payload["vector"][0]["re"] = "-1"
        with self.assertRaisesRegex(MOD.CertificateError, "zero sum"):
            MOD.verify(payload)

    def test_incomplete_zero_count_rejected(self):
        payload = load("synthetic-strict-separation.json")
        payload["slab"]["exact_zero_count"] = 2
        with self.assertRaisesRegex(MOD.CertificateError, "multiplicities"):
            MOD.verify(payload)

    def test_overlapping_bins_rejected(self):
        payload = load("synthetic-strict-separation.json")
        payload["slab"]["exact_zero_count"] = 2
        payload["zero_bins"].append(
            {"id": "overlap", "lower": "0", "upper": "1/10", "count": 1, "gate_id": "synthetic"}
        )
        with self.assertRaisesRegex(MOD.CertificateError, "overlap"):
            MOD.verify(payload)

    def test_endpoint_touch_rejected(self):
        payload = load("synthetic-strict-separation.json")
        payload["zero_bins"][0]["lower"] = "-1"
        with self.assertRaisesRegex(MOD.CertificateError, "strictly inside"):
            MOD.verify(payload)

    def test_boolean_count_rejected(self):
        payload = load("synthetic-strict-separation.json")
        payload["zero_bins"][0]["count"] = True
        with self.assertRaisesRegex(MOD.CertificateError, "boolean"):
            MOD.verify(payload)

    def test_blocking_gate_rejected(self):
        payload = load("synthetic-strict-separation.json")
        payload["logical_gates"][0]["state"] = "BLOCKING"
        with self.assertRaisesRegex(MOD.CertificateError, "blocking"):
            MOD.verify(payload)

    def test_false_claim_rejected(self):
        payload = load("synthetic-strict-separation.json")
        payload["claimed_residual"]["upper"] = "-1"
        with self.assertRaisesRegex(MOD.CertificateError, "claimed_residual"):
            MOD.verify(payload)

    def test_widened_primitive_fails_closed(self):
        payload = load("synthetic-strict-separation.json")
        for key in ("claimed_ordinary_pick", "claimed_weighted_full",
                    "claimed_inside_contribution", "claimed_residual", "claimed_status"):
            payload.pop(key, None)
        payload["points"][0]["f"]["real"] = {"lower": "-1000", "upper": "1000"}
        result = MOD.verify(payload)
        self.assertEqual(result["status"], "UNRESOLVED_ZERO_TOUCH")


if __name__ == "__main__":
    unittest.main()
