import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from matched_pole_expanded_scan import (
    EXPANDED_DIMENSIONS,
    EXPANDED_MODEL_FRACTIONS,
    EXPANDED_NODES,
    build_template,
)
from matched_pole_scan import HEIGHTS


class ExpandedMatchedPoleScanTests(unittest.TestCase):
    def test_exact_manifest_size_and_range(self) -> None:
        template, metadata = build_template()
        expected = (
            len(HEIGHTS)
            * (len(EXPANDED_NODES) - 1)
            * len(EXPANDED_MODEL_FRACTIONS)
            * len(EXPANDED_DIMENSIONS)
        )
        self.assertEqual(len(template["points"]), 76)
        self.assertEqual(expected, 8640)
        self.assertEqual(len(template["channels"]), expected)
        self.assertEqual(len(metadata), expected)
        self.assertEqual(EXPANDED_NODES[0].numerator, 1)
        self.assertEqual(EXPANDED_NODES[0].denominator, 100000)
        self.assertEqual(EXPANDED_NODES[-1].numerator, 499)
        self.assertEqual(EXPANDED_NODES[-1].denominator, 1000)

    def test_all_declared_ids_are_unique(self) -> None:
        template, _metadata = build_template()
        ids = template["declared_channel_ids"]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(ids, [channel["id"] for channel in template["channels"]])


if __name__ == "__main__":
    unittest.main()
