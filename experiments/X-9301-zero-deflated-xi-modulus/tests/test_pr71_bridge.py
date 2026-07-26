from __future__ import annotations

import copy
import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "build_pr71_certificate", ROOT / "build_pr71_certificate.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

VERIFY_SPEC = importlib.util.spec_from_file_location(
    "verify_zero_deflated_modulus_bridge", ROOT / "verify_zero_deflated_modulus.py"
)
VERIFY = importlib.util.module_from_spec(VERIFY_SPEC)
assert VERIFY_SPEC.loader is not None
sys.modules[VERIFY_SPEC.name] = VERIFY
VERIFY_SPEC.loader.exec_module(VERIFY)


def rat(n, d=1):
    return {"numerator": n, "denominator": d}


def binval(m, e):
    return {"mantissa": str(m), "exponent": str(e)}


class PR71BridgeTests(unittest.TestCase):
    @staticmethod
    def resign(certificate):
        body = copy.deepcopy(certificate)
        body.pop("certificate_sha256", None)
        certificate["certificate_sha256"] = MODULE.canonical_sha(body)

    def primitives(self):
        return {
            "schema": MODULE.PRIMITIVE_SCHEMA,
            "normalization_id": MODULE.NORMALIZATION,
            "precision_bits": 192,
            "common_xi_scale_power_of_two": 123,
            "ordinate": rat(10),
            "points": [
                {
                    "id": "x-2",
                    "x": rat(1, 4),
                    "xi_rectangle": {
                        "real": {"lower": rat(1), "upper": rat(2)},
                        "imag": {"lower": rat(-1), "upper": rat(1)},
                    },
                    "functional_equation_residual_contains_zero": True,
                },
                {
                    "id": "x-1",
                    "x": rat(1, 2),
                    "xi_rectangle": {
                        "real": {"lower": rat(2), "upper": rat(3)},
                        "imag": {"lower": rat(-1), "upper": rat(1)},
                    },
                    "functional_equation_residual_contains_zero": True,
                },
            ],
        }

    def gap(self):
        return {
            "schema": MODULE.GAP_SCHEMA,
            "target": rat(10),
            "lower_hardy_zero_ball": {
                "lower": binval(35, -2),
                "upper": binval(36, -2),
            },
            "upper_hardy_zero_ball": {
                "lower": binval(44, -2),
                "upper": binval(45, -2),
            },
            "classification": "CERTIFIED_EMPTY_FULL_STRIP_INTERIOR_SLAB",
        }

    def config(self):
        return {
            "schema": MODULE.CONFIG_SCHEMA,
            "log_terms": 128,
            "rows": [
                {
                    "id": "m",
                    "kind": "deflated-monotonicity",
                    "left": "x-2",
                    "right": "x-1",
                }
            ],
        }

    def test_builds_two_certified_bins(self):
        primitives, gap = self.primitives(), self.gap()
        output = MODULE.build(primitives, gap, self.config())
        self.assertEqual(output["classification"], "RIEMANN_XI_DIRECTED")
        self.assertEqual(len(output["zero_bins"]), 2)
        self.assertEqual(output["zero_bins"][0]["count_lower"], 1)
        self.assertEqual(output["points"][0]["u"], rat(1, 16))
        self.assertEqual(output["common_xi_scale_power_of_two"], 123)
        arithmetic = VERIFY.verify(output)
        self.assertFalse(arithmetic["source_artifacts_verified"])
        bindings = VERIFY.verify_source_artifacts(output, primitives, gap)
        self.assertEqual(bindings["gap_sha256"], output["source"]["gap_sha256"])

    def test_mutated_gap_artifact_is_rejected(self):
        primitives, gap = self.primitives(), self.gap()
        output = MODULE.build(primitives, gap, self.config())
        mutated = copy.deepcopy(gap)
        mutated["precision_bits"] = 999
        with self.assertRaisesRegex(VERIFY.CertificateError, "gap artifact digest"):
            VERIFY.verify_source_artifacts(output, primitives, mutated)

    def test_rehashed_certificate_point_drift_is_rejected(self):
        primitives, gap = self.primitives(), self.gap()
        output = MODULE.build(
            copy.deepcopy(primitives), copy.deepcopy(gap), self.config()
        )
        point = output["points"][0]
        point["xi_rectangle"]["real"]["lower"]["numerator"] += 1
        canonical = {
            "id": point["id"],
            "u": point["u"],
            "xi_rectangle": point["xi_rectangle"],
        }
        point["point_sha256"] = MODULE.canonical_sha(canonical)
        self.resign(output)
        with self.assertRaisesRegex(
            VERIFY.CertificateError, "differs from primitive artifact"
        ):
            VERIFY.verify_source_artifacts(output, primitives, gap)

    def test_rehashed_certificate_zero_drift_is_rejected(self):
        primitives, gap = self.primitives(), self.gap()
        output = MODULE.build(primitives, gap, self.config())
        output["zero_bins"][0]["count_lower"] = 2
        self.resign(output)
        with self.assertRaisesRegex(
            VERIFY.CertificateError, "differs from gap artifact"
        ):
            VERIFY.verify_source_artifacts(output, primitives, gap)

    def test_ordinate_mismatch_rejected(self):
        primitives = self.primitives()
        primitives["ordinate"] = rat(11)
        with self.assertRaises(MODULE.BridgeError):
            MODULE.build(primitives, self.gap(), self.config())

    def test_nonbracketing_balls_rejected(self):
        gap = self.gap()
        gap["upper_hardy_zero_ball"]["lower"] = binval(39, -2)
        with self.assertRaises(MODULE.BridgeError):
            MODULE.build(self.primitives(), gap, self.config())

    def test_unclassified_gap_rejected(self):
        gap = self.gap()
        gap["classification"] = "EMPIRICAL"
        with self.assertRaises(MODULE.BridgeError):
            MODULE.build(self.primitives(), gap, self.config())


if __name__ == "__main__":
    unittest.main()
