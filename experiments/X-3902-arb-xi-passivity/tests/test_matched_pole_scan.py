from fractions import Fraction
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from matched_pole import (
    isolated_pair_quadratic,
    matched_pole_vector,
    model_overlaps,
    moment,
)
from matched_pole_scan import (
    DIMENSIONS,
    HEIGHTS,
    MODEL_FRACTIONS,
    NODES,
    build_template,
    choose_window,
    fraction_json,
    summarize,
)


class MatchedPoleScanTests(unittest.TestCase):
    def test_template_shape_and_unique_ids(self) -> None:
        template, metadata = build_template()
        expected_channels = (
            len(HEIGHTS)
            * (len(NODES) - 1)
            * len(MODEL_FRACTIONS)
            * len(DIMENSIONS)
        )
        self.assertEqual(len(template["points"]), len(HEIGHTS) * len(NODES))
        self.assertEqual(len(template["channels"]), expected_channels)
        self.assertEqual(len(metadata), expected_channels)
        point_ids = [point["id"] for point in template["points"]]
        channel_ids = [channel["id"] for channel in template["channels"]]
        self.assertEqual(len(point_ids), len(set(point_ids)))
        self.assertEqual(len(channel_ids), len(set(channel_ids)))
        self.assertEqual(template["declared_channel_ids"], channel_ids)

    def test_every_window_contains_its_modeled_gap(self) -> None:
        for gap in range(len(NODES) - 1):
            for dimension in DIMENSIONS:
                start, nodes = choose_window(gap, dimension)
                self.assertEqual(len(nodes), dimension)
                self.assertLessEqual(start, gap)
                self.assertGreater(start + dimension, gap + 1)
                self.assertIn(NODES[gap], nodes)
                self.assertIn(NODES[gap + 1], nodes)

    def test_exact_identities_for_representative_channels(self) -> None:
        for gap, dimension, model_fraction in (
            (0, 3, Fraction(1, 3)),
            (4, 4, Fraction(1, 2)),
            (9, 5, Fraction(2, 3)),
        ):
            _start, nodes = choose_window(gap, dimension)
            delta = NODES[gap] + model_fraction * (NODES[gap + 1] - NODES[gap])
            model_d = delta * delta
            vector = matched_pole_vector(nodes, model_d)
            for power in range(dimension - 2):
                self.assertEqual(moment(nodes, vector, power), 0)
            self.assertEqual(model_overlaps(nodes, vector, model_d), (0, -1))
            self.assertEqual(
                isolated_pair_quadratic(nodes, vector, model_d),
                -2 * model_d,
            )

    def test_summary_normalizes_one_exact_interval(self) -> None:
        template, metadata = build_template()
        channel = template["channels"][0]
        identifier = channel["id"]
        verification = {
            "channels": [
                {
                    "id": identifier,
                    "status": "CERTIFIED_NONNEGATIVE",
                    "interval": {
                        "lower": fraction_json(Fraction(1, 10)),
                        "upper": fraction_json(Fraction(1, 5)),
                    },
                }
            ]
        }
        summary = summarize(verification, metadata, 160)
        self.assertEqual(summary["status_counts"]["CERTIFIED_NONNEGATIVE"], 1)
        self.assertEqual(summary["negative_channel_ids"], [])
        self.assertEqual(summary["unresolved_channel_ids"], [])
        self.assertEqual(
            summary["status"],
            "ALL_MATCHED_POLE_CHANNELS_CERTIFIED_NONNEGATIVE",
        )
        row = summary["smallest_normalized_upper_bounds"][0]
        lower = Fraction(
            int(row["normalized_interval"]["lower"]["numerator"]),
            int(row["normalized_interval"]["lower"]["denominator"]),
        )
        upper = Fraction(
            int(row["normalized_interval"]["upper"]["numerator"]),
            int(row["normalized_interval"]["upper"]["denominator"]),
        )
        self.assertLessEqual(lower, upper)

    def test_invalid_window_rejected(self) -> None:
        with self.assertRaises(ValueError):
            choose_window(-1, 3)
        with self.assertRaises(ValueError):
            choose_window(0, 1)
        with self.assertRaises(ValueError):
            choose_window(len(NODES), 3)


if __name__ == "__main__":
    unittest.main()
