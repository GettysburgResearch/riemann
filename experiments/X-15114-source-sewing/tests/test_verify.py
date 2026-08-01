from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CERT = json.loads((ROOT / "certificates/redundant-readout-order4.json").read_text())
SPEC = importlib.util.spec_from_file_location("source_sewing_verify", ROOT / "verify.py")
MOD = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MOD)


class SourceSewingTests(unittest.TestCase):
    def test_retained_control_passes(self) -> None:
        out = MOD.verify(copy.deepcopy(CERT))
        self.assertEqual(
            out["status"],
            "CERTIFIED_SOURCE_SEWING_AND_LINEAR_SCALAR_OBSTRUCTION",
        )
        self.assertEqual(out["direct_order_four"], 31)
        self.assertEqual(out["homogeneity_gap"], 434)

    def assert_rejected(self, mutate) -> None:
        bad = copy.deepcopy(CERT)
        mutate(bad)
        with self.assertRaises((ValueError, KeyError, TypeError)):
            MOD.verify(bad)

    def test_wrong_gram_rejected(self) -> None:
        self.assert_rejected(lambda d: d["claimed_gram"][0].__setitem__(0, 2))

    def test_wrong_pseudoinverse_rejected(self) -> None:
        self.assert_rejected(
            lambda d: d["claimed_gram_pseudoinverse"][0].__setitem__(0, 1)
        )

    def test_wrong_seam_form_rejected(self) -> None:
        self.assert_rejected(lambda d: d["claimed_seam_form"][2].__setitem__(2, 4))

    def test_wrong_trace_moment_rejected(self) -> None:
        self.assert_rejected(lambda d: d["claimed_trace_moments"].__setitem__("4", 30))

    def test_wrong_direct_order_four_rejected(self) -> None:
        self.assert_rejected(lambda d: d.__setitem__("claimed_direct_order_four", 32))

    def test_singular_coordinate_change_rejected(self) -> None:
        self.assert_rejected(
            lambda d: d.__setitem__(
                "coordinate_change_C", [[1, 0, 0], [0, 1, 0], [0, 0, 0]]
            )
        )

    def test_false_linear_normalization_rejected(self) -> None:
        self.assert_rejected(
            lambda d: d["fixed_linear_probe_weights"][0].__setitem__(0, 15)
        )

    def test_false_homogeneity_gap_rejected(self) -> None:
        self.assert_rejected(lambda d: d.__setitem__("claimed_homogeneity_gap", 433))

    def test_small_hilbert_schmidt_bound_rejected(self) -> None:
        self.assert_rejected(lambda d: d.__setitem__("hilbert_schmidt_bound", 2))

    def test_invalid_series_radius_rejected(self) -> None:
        self.assert_rejected(
            lambda d: d.__setitem__(
                "series_radius", {"numerator": 1, "denominator": 3}
            )
        )

    def test_boolean_injection_rejected(self) -> None:
        self.assert_rejected(lambda d: d["synthesis_U"][0].__setitem__(0, True))

    def test_nonsurjective_synthesis_rejected(self) -> None:
        self.assert_rejected(
            lambda d: d.__setitem__("synthesis_U", [[1, 0, 1], [2, 0, 2]])
        )


if __name__ == "__main__":
    unittest.main()
