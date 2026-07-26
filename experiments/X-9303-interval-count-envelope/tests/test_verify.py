from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "verify_interval_count_deflation", ROOT / "verify_interval_count_deflation.py"
)
VERIFY = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = VERIFY
SPEC.loader.exec_module(VERIFY)

CERT = json.loads(
    (ROOT / "certificates" / "synthetic-overlap-profile.json").read_text(encoding="utf-8")
)


def resign(data: dict) -> dict:
    data.pop("certificate_sha256", None)
    data["certificate_sha256"] = VERIFY.canonical_sha(data)
    return data


class IntervalCountProfileTests(unittest.TestCase):
    def test_overlap_profile_exposes_hidden_row(self) -> None:
        result = VERIFY.verify(copy.deepcopy(CERT))
        statuses = {row["id"]: row["status"] for row in result["rows"]}
        self.assertEqual(statuses["raw-hidden"], "CERTIFIED_NONNEGATIVE")
        self.assertEqual(statuses["outer-only-hidden"], "CERTIFIED_NONNEGATIVE")
        self.assertEqual(statuses["optimal-profile-exposes"], "CERTIFIED_NEGATIVE")
        self.assertEqual(result["verdict"], "SYNTHETIC_OVERLAP_COUNT_SEPARATION")

    def test_profile_counts_are_exact(self) -> None:
        result = VERIFY.verify(copy.deepcopy(CERT))
        self.assertEqual(
            [(row["forced_count"], row["increment"]) for row in result["profile"]],
            [(22, 22), (24, 2)],
        )

    def test_bad_dual_is_rejected(self) -> None:
        bad = copy.deepcopy(CERT)
        bad["profiles"][0]["dual_multipliers"][0]["numerator"] = 2
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify(resign(bad))

    def test_bad_primal_is_rejected(self) -> None:
        bad = copy.deepcopy(CERT)
        bad["profiles"][0]["primal_cell_counts"][1] = 19
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify(resign(bad))

    def test_false_count_is_rejected(self) -> None:
        bad = copy.deepcopy(CERT)
        bad["count_constraints"][2]["exact_count"] = 25
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify(resign(bad))

    def test_wrong_gate_is_rejected(self) -> None:
        bad = copy.deepcopy(CERT)
        bad["count_constraints"][0]["gate"]["status"] = (
            "CERTIFIED_EXACT_TOTAL_ZERO_COUNT_ZERO_FREE_ENDPOINTS"
        )
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify(resign(bad))

    def test_nonmonotone_profile_is_rejected(self) -> None:
        bad = copy.deepcopy(CERT)
        bad["profiles"][1]["forced_count"] = 19
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify(resign(bad))

    def test_missing_boundary_is_rejected(self) -> None:
        bad = copy.deepcopy(CERT)
        bad["profiles"][0]["radius"] = {"numerator": 6, "denominator": 5}
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify(resign(bad))

    def test_boolean_count_is_rejected(self) -> None:
        bad = copy.deepcopy(CERT)
        bad["count_constraints"][0]["exact_count"] = True
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify(resign(bad))

    def test_missing_point_digest_is_rejected(self) -> None:
        bad = copy.deepcopy(CERT)
        bad["points"][0].pop("point_sha256")
        with self.assertRaisesRegex(VERIFY.CertificateError, "point_sha256"):
            VERIFY.verify(resign(bad))

    def test_false_certificate_digest_is_rejected(self) -> None:
        bad = copy.deepcopy(CERT)
        bad["certificate_sha256"] = "0" * 64
        with self.assertRaisesRegex(VERIFY.CertificateError, "certificate_sha256 mismatch"):
            VERIFY.verify(bad)

    def test_production_relabel_is_rejected_without_source_adapter(self) -> None:
        bad = copy.deepcopy(CERT)
        bad["classification"] = "RIEMANN_XI_DIRECTED"
        for constraint in bad["count_constraints"]:
            constraint["gate"]["status"] = VERIFY.PRODUCTION_COUNT_GATE
        with self.assertRaisesRegex(VERIFY.CertificateError, "provenance binding"):
            VERIFY.verify(resign(bad))


if __name__ == "__main__":
    unittest.main()
