import importlib.util
from fractions import Fraction as F
from pathlib import Path
import unittest

MODULE_PATH = Path(__file__).resolve().parents[1] / "verify.py"
spec = importlib.util.spec_from_file_location("x105231_verify", MODULE_PATH)
m = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(m)


class WeightedCompoundTests(unittest.TestCase):
    def test_weighted_variance(self):
        w = [F(1, 2), F(2, 3), F(3, 4)]
        r = [F(-2), F(-1, 2), F(1, 3)]
        *_, d = m.weighted_scalar_defect(w, r)
        self.assertEqual(d, m.scalar_pair_energy(w, r))

    def test_centered_hilbert_variance(self):
        w = [F(1), F(1), F(1)]
        y = [(F(1), F(0)), (F(-1), F(0)), (F(0), F(0))]
        self.assertEqual(
            m.vector_pair_energy(w, y),
            m.centered_trace_energy(w, m.gram(y)),
        )

    def test_projection_contraction(self):
        w = [F(1), F(1), F(1)]
        rho = [F(-1), F(1), F(0)]
        x = (F(1), F(0))
        y = [(F(1), F(0)), (F(-1), F(0)), (F(0), F(0))]
        *_, d = m.weighted_scalar_defect(w, rho)
        self.assertLessEqual(d, m.norm2(x) * m.vector_pair_energy(w, y))

    def test_diagonal_firewall(self):
        w = [F(1), F(1), F(1)]
        orth = [(F(1), F(0), F(0)),
                (F(0), F(1), F(0)),
                (F(0), F(0), F(1))]
        aligned = [(F(1), F(0), F(0))] * 3
        self.assertEqual(
            [m.gram(orth)[i][i] for i in range(3)],
            [m.gram(aligned)[i][i] for i in range(3)],
        )
        self.assertEqual(m.centered_trace_energy(w, m.gram(orth)), F(6))
        self.assertEqual(m.centered_trace_energy(w, m.gram(aligned)), F(0))


if __name__ == "__main__":
    unittest.main()
