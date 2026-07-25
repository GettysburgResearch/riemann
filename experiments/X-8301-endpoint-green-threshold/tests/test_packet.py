from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x8301_packet", ROOT / "verify_packet.py")
PACKET = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = PACKET
SPEC.loader.exec_module(PACKET)
CERT = ROOT / "certificates" / "synthetic-corner-packets.json"


class CornerPacketTests(unittest.TestCase):
    def load(self):
        return json.loads(CERT.read_text(encoding="utf-8"))

    def test_committed_packet_certificate(self):
        out = PACKET.verify_certificate(self.load())
        self.assertEqual(out["status"], "EXACT_COHERENT_PACKET_CERTIFICATES_RECONSTRUCTED")
        statuses = {case["id"]: case["status"] for case in out["cases"]}
        self.assertEqual(statuses["coherent-subcritical-events-cross"], "PACKET_CROSSING_AT_ENDPOINT")
        self.assertEqual(statuses["opposite-phase-events-cancel"], "PACKET_POSITIVE_ON_MESH_CELL")

    def test_individual_events_subcritical_but_packet_crosses(self):
        out = PACKET.verify_certificate(self.load())
        case = next(x for x in out["cases"] if x["id"] == "coherent-subcritical-events-cross")
        self.assertEqual(case["component_secular_values"], [
            {"numerator": "16", "denominator": "25"},
            {"numerator": "16", "denominator": "25"},
        ])
        self.assertEqual(case["secular_left"], {"numerator": "-11", "denominator": "25"})

    def test_opposite_phase_cancellation_is_exact(self):
        out = PACKET.verify_certificate(self.load())
        case = next(x for x in out["cases"] if x["id"] == "opposite-phase-events-cancel")
        self.assertEqual(case["Z_left"], {"re": "0", "im": "0"})
        self.assertEqual(case["secular_left"], {"numerator": "1", "denominator": "1"})

    def test_component_sum_mutation_rejected(self):
        data = self.load()
        data["cases"][0]["components"][1]["re"] = "1/50"
        with self.assertRaisesRegex(PACKET.CertificateError, "do not sum"):
            PACKET.verify_certificate(data)

    def test_reversed_mesh_rejected(self):
        data = self.load()
        data["cases"][2]["x_interval"] = [2, 1]
        with self.assertRaisesRegex(PACKET.CertificateError, "reversed"):
            PACKET.verify_certificate(data)

    def test_altered_endpoint_claim_rejected(self):
        data = self.load()
        data["cases"][2]["claimed"]["f_left"] = "1"
        with self.assertRaisesRegex(PACKET.CertificateError, "endpoint mismatch"):
            PACKET.verify_certificate(data)


if __name__ == "__main__":
    unittest.main()
