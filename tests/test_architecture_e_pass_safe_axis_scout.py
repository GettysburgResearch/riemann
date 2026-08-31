"""Acceptance and scope controls for the bounded safe-axis scout."""

import hashlib
import importlib.util
import unittest
from fractions import Fraction as Q
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
PATH = (
    ROOT
    / "research/riemann-structures/native-five-hour-pass/architecture-e/safe_axis_scout.py"
)
SPEC = importlib.util.spec_from_file_location("architecture_e_safe_scout", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class ScoutTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw = M.ARTIFACT.read_text(encoding="utf-8")
        cls.record = M.strict_json(cls.raw)

    def test_exact_registered_census(self):
        self.assertEqual(len(M.packets()), 1911)
        self.assertEqual(self.record["panel_count"], 1911)

    def test_endpoint_removable_path_does_not_differentiate_zeta(self):
        M.fvalue.cache_clear()
        with patch.object(
            M.mp, "diff", side_effect=RuntimeError("no infinity cancellation")
        ):
            value = M.fvalue(1, 2, 80)
        with M.mp.workdps(80):
            expected = 1 + M.mp.euler / 2 - M.mp.log(4 * M.mp.pi) / 2
            self.assertEqual(value, expected)

    def test_cache_key_includes_precision(self):
        M.fvalue.cache_clear()
        M.fvalue(1, 1, 50)
        M.fvalue(1, 1, 60)
        info = M.fvalue.cache_info()
        self.assertEqual(info.misses, 2)
        self.assertEqual(info.currsize, 2)

    def test_all_finalists_stable_and_status_guarded(self):
        self.assertEqual(len(self.record["finalists"]), 24)
        self.assertTrue(
            all(row["agrees_60_digits"] for row in self.record["finalists"])
        )
        self.assertEqual(self.record["status"], "POSITIVE_ON_REGISTERED_GRID")

    def test_smallest_registered_endpoint_panel(self):
        first = self.record["finalists"][0]
        self.assertEqual(
            first["nodes"],
            [
                "1/2",
                "2147483649/4294967296",
                "1073741825/2147483648",
                "2147483651/4294967296",
            ],
        )
        self.assertGreater(M.mp.mpf(first["minimum_200"]), 0)

    def test_no_continuum_or_zero_census_claim(self):
        scope = self.record["scope"]
        self.assertFalse(scope["continuum_theorem_inferred"])
        self.assertFalse(scope["xi_zero_census_used"])
        self.assertTrue(scope["bounded_reconnaissance_only"])

    def test_artifact_body_digest(self):
        body = {k: v for k, v in self.record.items() if k != "proof_sha256"}
        self.assertEqual(
            hashlib.sha256(M.canonical(body).encode()).hexdigest(),
            self.record["proof_sha256"],
        )

    def test_owned_and_source_bindings(self):
        self.assertEqual(
            self.record["producer_sha256"],
            hashlib.sha256(PATH.read_bytes()).hexdigest(),
        )
        self.assertEqual(
            self.record["test_sha256"],
            hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        )
        self.assertEqual(
            self.record["preregistration_sha256"],
            hashlib.sha256(M.PREREG.read_bytes()).hexdigest(),
        )
        self.assertEqual(len(self.record["sources"]), 2)

    def test_artifact_cap(self):
        self.assertLessEqual(len(self.raw.encode()), M.MAX_BYTES)

    def test_strict_json_hostile_tokens(self):
        for raw in ('{"x":1,"x":2}', '{"x":1.0}', '{"x":NaN}', '{"x":Infinity}'):
            with self.assertRaises(ValueError):
                M.strict_json(raw)

    def test_changed_source_refused(self):
        with (
            patch.object(M.subprocess, "check_output", return_value=b"changed"),
            self.assertRaises(ValueError),
        ):
            M.authenticate()

    def test_one_direct_matrix_replay(self):
        panel = (Q(1, 2), Q(9, 16), Q(3, 4), Q(1))
        result = M.spectral(panel, 100)
        stored = next(
            row
            for row in self.record["panels"]
            if row["nodes"] == ["1/2", "9/16", "3/4", "1/1"]
        )
        self.assertEqual(result["minimum"], stored["minimum"])


if __name__ == "__main__":
    unittest.main()
