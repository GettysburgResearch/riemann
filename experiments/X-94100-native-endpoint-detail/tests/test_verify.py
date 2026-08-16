from pathlib import Path
import importlib.util
import json
import unittest

HERE = Path(__file__).resolve().parent
EXP = HERE.parent
SPEC = importlib.util.spec_from_file_location("x94100", EXP / "verify.py")
MOD = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MOD)


class NativeEndpointDetailTests(unittest.TestCase):
    def test_small_detail_grid(self):
        from decimal import localcontext
        with localcontext() as ctx:
            ctx.prec = 60
            for T in range(3, 40):
                for q in range(2, T):
                    self.assertGreater(MOD.detail(T, q), 0)

    def test_harmonic_grid(self):
        from decimal import localcontext
        with localcontext() as ctx:
            ctx.prec = 60
            for N in range(1, 500):
                lhs, rhs = MOD.harmonic_inequality(N)
                self.assertLess(lhs, rhs)

    def test_greedy_feasible(self):
        from decimal import localcontext
        with localcontext() as ctx:
            ctx.prec = 60
            result = MOD.native_greedy(64)
        self.assertGreaterEqual(result["largest_slack_column"], 1)
        self.assertGreater(result["positive_coefficients"], 0)


if __name__ == "__main__":
    unittest.main()
