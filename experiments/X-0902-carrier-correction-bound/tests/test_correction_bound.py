import unittest

from correction_bound import correction_bound, evaluate_ladder


class CorrectionBoundTests(unittest.TestCase):
    def test_rejects_invalid_parameters(self):
        for args in ((1, 1.0, 1), (2, 0.0, 1), (2, 1.0, 0)):
            with self.assertRaises(ValueError):
                correction_bound(*args)

    def test_archimedean_bound_decreases_with_carrier(self):
        low = correction_bound(10**11, 1.0e12, 1024)
        high = correction_bound(10**11, 2.0e12, 1024)
        self.assertLess(high.archimedean_bound, low.archimedean_bound)
        self.assertAlmostEqual(
            low.archimedean_bound / high.archimedean_bound, 2.0, places=12
        )

    def test_pole_bound_has_inverse_square_scaling(self):
        low = correction_bound(10**11, 1.0e12, 1024)
        high = correction_bound(10**11, 2.0e12, 1024)
        self.assertAlmostEqual(low.pole_bound / high.pole_bound, 4.0, places=12)

    def test_target_bound_is_far_below_margin(self):
        result = correction_bound(10**11, 4709203636353.65, 1024)
        self.assertLess(result.total_bound, 4.5e-10)
        self.assertGreater(0.00026896626427230785 / result.total_bound, 600000)

    def test_ladder_never_promotes_candidate(self):
        data = evaluate_ladder(
            4709203636353.65,
            [(10**8, 1024, 0.006643091775833554)],
        )
        self.assertIsNone(data["counterexample_candidate"])
        self.assertFalse(data["cells"][0]["correction_can_reverse_reported_sign"])


if __name__ == "__main__":
    unittest.main()
