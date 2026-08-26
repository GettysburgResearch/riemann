from __future__ import annotations

import importlib.util
import json
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_extra_notch_closed_sector_transport.py"
)
NOTE_PATH = MODULE_PATH.with_name("FFPS_EXTRA_NOTCH_CLOSED_SECTOR_TRANSPORT.md")
JSON_PATH = MODULE_PATH.with_suffix(".json")
SPEC = importlib.util.spec_from_file_location("closed_transport", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load closed-sector transport replay")
closed_transport = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(closed_transport)


class FfpsExtraNotchClosedSectorTransportTest(unittest.TestCase):
    def test_display_math_and_canonical_json(self) -> None:
        depth = 0
        for line in NOTE_PATH.read_text(encoding="utf-8").splitlines():
            if line == r"\[":
                depth += 1
                self.assertEqual(depth, 1)
            elif line == r"\]":
                depth -= 1
                self.assertGreaterEqual(depth, 0)
        self.assertEqual(depth, 0)
        self.assertEqual(
            json.loads(JSON_PATH.read_text(encoding="utf-8")), closed_transport.run()
        )

    def test_frozen_source_blobs(self) -> None:
        closed_transport.check_source_blobs()
        self.assertEqual(sum(map(len, closed_transport.FROZEN_SOURCES.values())), 7)

    def test_type_i_exponents(self) -> None:
        self.assertEqual(
            closed_transport.type_i_exponents(),
            {
                "unrestricted_type_i": -Fraction(1, 6),
                "squarefree_lattice": -Fraction(1, 4),
                "squarefree_type_i": -Fraction(1, 12),
            },
        )

    def test_negative_variation_contraction(self) -> None:
        self.assertEqual(
            closed_transport.negative_variation_contraction(
                Fraction(7, 3), Fraction(1)
            ),
            Fraction(7, 3),
        )
        with self.assertRaises(ValueError):
            closed_transport.negative_variation_contraction(Fraction(1), Fraction(1, 2))

    def test_taxonomy_and_gate_scope(self) -> None:
        result = closed_transport.run()
        self.assertEqual(len(result["parent_t102990_taxonomy"]), 7)
        self.assertIn("open pending", result["adapter_status"]["EXTSRC106150"])
        self.assertIn(
            "proved EXTSRC106150",
            result["adapter_status"]["complete_current_implication"],
        )
        kernel = result["kernel_class"]
        self.assertEqual(
            kernel["epsilon_scope"], "epsilon>0 is fixed independently of Y"
        )
        self.assertTrue(kernel["raw_multiplier"].startswith("q^2*r^2"))
        self.assertIn("vanishes at s=0", kernel["zero_mass_reason"])
        self.assertIn("I-[0,epsilon]", kernel["local_negative_variation"])
        restricted = result["restricted_squarefree_transfer"]
        self.assertEqual(restricted["parent_scope_hypothesis"], "2^omega(R)=Y^o(1)")
        self.assertIn("d|rad(R)", restricted["inclusion_exclusion"])
        self.assertEqual(result["resource_caps"]["source_atoms_enumerated"], 0)


if __name__ == "__main__":
    unittest.main()
