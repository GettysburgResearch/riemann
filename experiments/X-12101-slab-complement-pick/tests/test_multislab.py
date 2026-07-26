#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("multislab", ROOT / "verify_multislab.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MOD
SPEC.loader.exec_module(MOD)


def load(name: str):
    return json.loads((ROOT / "certificates" / name).read_text(encoding="utf-8"))


class MultiSlabTests(unittest.TestCase):
    def test_exact_negative(self):
        result = MOD.verify(load("synthetic-multislab-separation.json"))
        self.assertEqual(result["status"], "CERTIFIED_NEGATIVE_SLAB_COMPLEMENT_WITNESS")
        self.assertEqual(result["multislab_residual_interval"]["upper"], "-108800000/296901721")

    def test_positive_control(self):
        result = MOD.verify(load("synthetic-multislab-control.json"))
        self.assertEqual(result["status"], "CERTIFIED_NONNEGATIVE_CONTROL")
        self.assertEqual(result["multislab_residual_interval"]["lower"], "22500/142129")

    def test_higher_moment_mutation_rejected(self):
        payload = load("synthetic-multislab-separation.json")
        payload["vector"][0]["re"] = "2"
        payload["vector"][1]["re"] = "-2"
        with self.assertRaisesRegex(MOD.CertificateError, "moment"):
            MOD.verify(payload)

    def test_overlapping_slabs_rejected(self):
        payload = load("synthetic-multislab-separation.json")
        payload["slabs"][1]["lower"] = "-3/2"
        with self.assertRaisesRegex(MOD.CertificateError, "slabs overlap"):
            MOD.verify(payload)

    def test_incomplete_slab_rejected(self):
        payload = load("synthetic-multislab-separation.json")
        payload["slabs"][0]["exact_zero_count"] = 2
        with self.assertRaisesRegex(MOD.CertificateError, "saturate"):
            MOD.verify(payload)

    def test_bin_assigned_to_wrong_slab_rejected(self):
        payload = load("synthetic-multislab-separation.json")
        payload["zero_bins"][0]["slab_id"] = "right"
        with self.assertRaisesRegex(MOD.CertificateError, "strictly inside"):
            MOD.verify(payload)

    def test_widened_primitive_unresolved(self):
        payload = load("synthetic-multislab-separation.json")
        for key in ("claimed_ordinary_pick", "claimed_weighted_full",
                    "claimed_inside_contribution", "claimed_residual", "claimed_status"):
            payload.pop(key, None)
        payload["points"][0]["f"]["real"] = {"lower": "-1000", "upper": "1000"}
        self.assertEqual(MOD.verify(payload)["status"], "UNRESOLVED_ZERO_TOUCH")

    def test_exact_translation_invariance(self):
        payload = load("synthetic-multislab-separation.json")
        for key in ("claimed_ordinary_pick", "claimed_weighted_full",
                    "claimed_inside_contribution", "claimed_residual", "claimed_status"):
            payload.pop(key, None)
        shift = 10
        payload["origin"] = str(shift)
        for slab in payload["slabs"]:
            slab["lower"] = str(MOD.q(slab["lower"], "a") + shift)
            slab["upper"] = str(MOD.q(slab["upper"], "b") + shift)
        for point in payload["points"]:
            point["t"] = str(MOD.q(point["t"], "t") + shift)
        for zero_bin in payload["zero_bins"]:
            zero_bin["lower"] = str(MOD.q(zero_bin["lower"], "l") + shift)
            zero_bin["upper"] = str(MOD.q(zero_bin["upper"], "u") + shift)
        result = MOD.verify(payload)
        self.assertEqual(result["multislab_residual_interval"]["upper"], "-108800000/296901721")


if __name__ == "__main__":
    unittest.main()
