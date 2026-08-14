#!/usr/bin/env python3
from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x19882_verify", ROOT / "verify.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class ThreeRouteVerifierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.control = json.loads((ROOT / "certificates" / "control.json").read_text())

    def test_control_passes(self) -> None:
        result = MOD.verify(copy.deepcopy(self.control))
        self.assertEqual(result["verdict"], "PASS_THREE_ROUTE_NATIVE_SLACK_PACKET")
        self.assertEqual(
            result["proof_object_sha256"],
            "40097c04506b682b960086650a6d99ead02c5af877686d3de7285904bedd13b4",
        )

    def test_root_capacity_identity_mutation_fails(self) -> None:
        bad = copy.deepcopy(self.control)
        bad["slack_cocycle"]["omega"][0] = 11
        with self.assertRaises(MOD.CertificateError):
            MOD.verify(bad)

    def test_negative_root_slack_fails(self) -> None:
        bad = copy.deepcopy(self.control)
        bad["slack_cocycle"]["root_slack"][1] = "-1/2"
        with self.assertRaises(MOD.CertificateError):
            MOD.verify(bad)

    def test_child_overallocation_fails(self) -> None:
        bad = copy.deepcopy(self.control)
        bad["slack_cocycle"]["children"][0]["alpha"] = "1/8"
        with self.assertRaises(MOD.CertificateError):
            MOD.verify(bad)

    def test_child_slack_above_capacity_fails(self) -> None:
        bad = copy.deepcopy(self.control)
        bad["slack_cocycle"]["children"][1]["slack"][0] = 33
        with self.assertRaises(MOD.CertificateError):
            MOD.verify(bad)

    def test_noncontractive_recurrence_fails(self) -> None:
        bad = copy.deepcopy(self.control)
        bad["subcritical_recurrence"]["rho"] = 1
        with self.assertRaises(MOD.CertificateError):
            MOD.verify(bad)

    def test_graph_depth_mutation_fails(self) -> None:
        bad = copy.deepcopy(self.control)
        bad["depth_graph"]["environment_depth_diagonal"][0] = 4
        with self.assertRaises(MOD.CertificateError):
            MOD.verify(bad)

    def test_graph_feature_mutation_fails(self) -> None:
        bad = copy.deepcopy(self.control)
        bad["depth_graph"]["environment_features"][0][1] = 2
        with self.assertRaises(MOD.CertificateError):
            MOD.verify(bad)

    def test_negative_passive_weight_fails(self) -> None:
        bad = copy.deepcopy(self.control)
        bad["passive_string"]["atoms"][1]["weight"] = -5
        with self.assertRaises(MOD.CertificateError):
            MOD.verify(bad)

    def test_duplicate_passive_node_fails(self) -> None:
        bad = copy.deepcopy(self.control)
        bad["passive_string"]["nodes"][2] = 2
        with self.assertRaises(MOD.CertificateError):
            MOD.verify(bad)

    def test_bad_geometric_parameter_fails(self) -> None:
        bad = copy.deepcopy(self.control)
        bad["passive_string"]["geometric_parameter"] = "3/2"
        with self.assertRaises(MOD.CertificateError):
            MOD.verify(bad)


if __name__ == "__main__":
    unittest.main()
