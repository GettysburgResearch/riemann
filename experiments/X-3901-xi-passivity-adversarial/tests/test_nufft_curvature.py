import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from nufft_curvature import direct_no_remainder, scan


class CurvatureGridTests(unittest.TestCase):
    def test_moderate_height_grid_and_direct_minimum(self) -> None:
        result = scan(
            center_text="1000000",
            spacing_text="0.001",
            points=1024,
            order=12,
        )
        summary = result["summary"]
        self.assertEqual(summary["negative_count"], 0)
        self.assertEqual(summary["minimum_t"], "1000000.181")
        self.assertAlmostEqual(
            summary["minimum_curvature"], 20.482258588268053, places=9
        )
        direct = direct_no_remainder("1000000.181")
        self.assertAlmostEqual(
            direct["curvature_no_remainder"],
            summary["minimum_curvature"],
            places=9,
        )

    def test_non_power_of_two_rejected(self) -> None:
        with self.assertRaises(ValueError):
            scan(
                center_text="1000000",
                spacing_text="0.001",
                points=1000,
                order=12,
            )


if __name__ == "__main__":
    unittest.main()
