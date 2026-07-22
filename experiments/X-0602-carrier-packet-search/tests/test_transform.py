import math
import unittest


def taylor_bound(weight_sum: float, K: int, M: int, order: int) -> float:
    eta = K * math.pi / M
    return weight_sum * math.exp(eta) * eta ** (order + 1) / math.factorial(order + 1)


class TransformBoundTests(unittest.TestCase):
    def test_bound_contracts_with_order(self):
        values = [taylor_bound(1000.0, 64, 4096, r) for r in range(4, 11)]
        self.assertTrue(all(a > b for a, b in zip(values, values[1:])))

    def test_calibration_scale(self):
        self.assertLess(taylor_bound(2000.0, 64, 4096, 10), 1e-17)


if __name__ == "__main__":
    unittest.main()
