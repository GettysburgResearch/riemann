from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_selector_stable_tail_transport.py"
)
SPEC = importlib.util.spec_from_file_location(
    "ffps_selector_stable_tail_transport", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load stable-tail transport module")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class SelectorStableTailTransportTest(unittest.TestCase):
    def test_exact_replay(self) -> None:
        payload = MODULE.run(check_sources=False)
        self.assertFalse(payload["scope"]["global_extension_constructed"])
        self.assertFalse(payload["scope"]["all_degree_optimum_proved"])
        self.assertFalse(payload["scope"]["linear_programming_used"])
        self.assertEqual(payload["scope"]["maximum_tail_size"], 8)
        self.assertEqual(len(payload["panels"]), 8)

    def test_transport_coefficients(self) -> None:
        expected = {
            (): 1,
            (1,): 2,
            (2,): 2,
            (1, 1): 3,
            (2, 1): 5,
            (3, 1): 7,
            (3, 2): 12,
            (3, 2, 1): 42,
        }
        for partition, coefficient in expected.items():
            self.assertEqual(MODULE.transport_coefficient(partition), coefficient)

    def test_column_boundary_and_error(self) -> None:
        degree = 32
        for height in range(9):
            column = (1,) * height
            self.assertEqual(MODULE.transport_coefficient(column), height + 1)
            self.assertEqual(
                MODULE.transport_error(degree, column),
                MODULE.column_error(degree, height),
            )

    def test_stable_error_recursion(self) -> None:
        degree = 32
        for size in range(2, 9):
            for partition in MODULE.partitions(size):
                if MODULE.is_column(partition):
                    continue
                expected = MODULE.dimension(
                    MODULE.stable_ambient_shape(degree, partition)
                ) + sum(
                    MODULE.transport_error(degree, pred)
                    for pred in MODULE.predecessors(partition)
                )
                self.assertEqual(MODULE.transport_error(degree, partition), expected)

    def test_three_row_cancellation(self) -> None:
        for index in range(2, 8):
            panel = MODULE.verify_three_row_cancellation(index)
            self.assertEqual(panel["current_three_row_coefficient"], 2 * index + 1)
            self.assertEqual(panel["signed_sum"], 0)

    def test_hook_transpose(self) -> None:
        for degree in range(5, 33):
            MODULE.verify_hook_transpose(degree)

    def test_validation(self) -> None:
        with self.assertRaises(ValueError):
            MODULE.verify_tail(4, (2,))
        with self.assertRaises(ValueError):
            MODULE.verify_tail(5, (3, 2))
        with self.assertRaises(ValueError):
            MODULE.transport_coefficient((1, 2))
        with self.assertRaises(ValueError):
            MODULE.transport_coefficient((9,))
        with self.assertRaises(ValueError):
            MODULE.verify_three_row_cancellation(1)


if __name__ == "__main__":
    unittest.main()
