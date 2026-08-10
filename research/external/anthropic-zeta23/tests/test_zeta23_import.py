#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import math
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def load(name: str, relative: str):
    path = ROOT / relative
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


constants = load(
    "zeta23_constants",
    "experiments/X-zeta23-constants/reproduce_constants.py",
)
rank_trace = load(
    "zeta23_rank_trace",
    "experiments/X-zeta23-rank-trace/stress_rank_trace.py",
)
multiplicity = load(
    "zeta23_multiplicity",
    "experiments/X-zeta23-multiplicity-frontier/frontier.py",
)
optimizer = load(
    "zeta23_optimizer",
    "experiments/X-zeta23-support-optimizer/optimize_support.py",
)


class TestConstants(unittest.TestCase):
    def test_scalar_constants(self) -> None:
        constants.run_self_checks()
        self.assertAlmostEqual(constants.h(1.0), 2.0 / 3.0, places=13)
        self.assertAlmostEqual(constants.hd(1.0), 5.0 / 6.0, places=13)
        self.assertAlmostEqual(constants.f(1.0), 3.0 / 4.0, places=13)

    def test_montgomery_taylor(self) -> None:
        c = constants.c_opt(1.0)
        self.assertTrue(0.75329 < c < 0.75330)
        self.assertTrue(0.67249 < 2.0 - 1.0 / c < 0.67251)


class TestMultiplicity(unittest.TestCase):
    def test_exact_frontier_identities(self) -> None:
        multiplicity.verify(100)


class TestRankTrace(unittest.TestCase):
    def test_random_and_equality_cases(self) -> None:
        summary = rank_trace.run(trials=150, n=10, seed=20260810)
        self.assertEqual(summary.failures, 0)
        self.assertLess(abs(summary.equality_gap), 1e-10)


class TestConditionalOptimizer(unittest.TestCase):
    def test_support_one_reproduces_cosine(self) -> None:
        numerical = optimizer.solve(1.0, 128)
        analytic = optimizer.analytic_efficiency_unsaturated(1.0)
        self.assertLess(abs(numerical.efficiency - analytic), 2e-5)
        self.assertGreater(numerical.profile_min, 0.0)

    def test_flat_formula_is_dominated(self) -> None:
        for lam in (0.7, 1.0, 1.3, 2.0):
            self.assertGreaterEqual(
                optimizer.solve(lam, 96).efficiency + 3e-8,
                optimizer.flat_efficiency(lam),
            )

    def test_seventy_percent_support(self) -> None:
        lam, attained = optimizer.support_for_target(
            0.70, nodes=96, iterations=18
        )
        self.assertLess(abs(lam - 1.043), 0.01)
        self.assertLess(abs(attained - 0.70), 2e-5)


if __name__ == "__main__":
    unittest.main()
