from __future__ import annotations

import importlib.util
from fractions import Fraction as F
from pathlib import Path
import unittest

MODULE_PATH = Path(__file__).resolve().parents[1] / "verify.py"
spec = importlib.util.spec_from_file_location("verify_t105300", MODULE_PATH)
verify = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(verify)


class TraceFormTests(unittest.TestCase):
    def test_all_real_cubic_signature(self) -> None:
        h, _ = verify.trace_form([F(3, 2), F(-3), F(0), F(1)])
        self.assertEqual(verify.inertia(h), (3, 0, 0))

    def test_nonreal_pair_signature(self) -> None:
        h, _ = verify.trace_form([F(0), F(3), F(0), F(1)])
        self.assertEqual(verify.inertia(h), (2, 1, 0))

    def test_zero_real_quartic_signature(self) -> None:
        h, _ = verify.trace_form([F(2), F(0), F(-2), F(0), F(1)])
        self.assertEqual(verify.inertia(h), (2, 2, 0))

    def test_polynomial_weight_preserves_inertia(self) -> None:
        p = [F(3, 2), F(-3), F(0), F(1)]
        h0, _ = verify.trace_form(p)
        h1, _ = verify.trace_form(p, [F(2), F(1)])
        self.assertEqual(verify.inertia(h0), verify.inertia(h1))

    def test_weighted_matrix_is_exact_congruence(self) -> None:
        p = [F(3, 2), F(-3), F(0), F(1)]
        h0, _ = verify.trace_form(p)
        h1, _ = verify.trace_form(p, [F(2), F(1)])
        b0, b1 = verify.critical_block(h0), verify.critical_block(h1)
        w = verify.weight_multiplication_matrix(p, [F(2), F(1)])
        self.assertEqual(verify.matmul(verify.transpose(w), verify.matmul(b0, w)), b1)

    def test_entire_window_residue_moments_match_trace_form(self) -> None:
        p = [F(3, 2), F(-3), F(0), F(1)]
        h, _ = verify.trace_form(p)
        self.assertEqual(verify.residue_moment_matrix(p, [F(-1), F(1)]), verify.critical_block(h))

    def test_non_coprime_weight_is_singular(self) -> None:
        p = [F(3, 2), F(-3), F(0), F(1)]
        h, _ = verify.trace_form(p, [F(-1), F(1)])
        self.assertGreater(verify.inertia(h)[2], 0)

    def test_every_principal_compression_is_safe(self) -> None:
        p = [F(2), F(0), F(-2), F(0), F(1)]
        h, _ = verify.trace_form(p)
        b = verify.critical_block(h)
        for i in range(len(b)):
            c = verify.principal_submatrix(b, (i,))
            self.assertLessEqual(verify.compression_lower_bound(c, len(b), 1), 0)

    def test_coherence_firewall(self) -> None:
        r1, r2 = F(-7, 12), F(-1, 12)
        c = (-(r1 + r2)) ** 2 / (F(2) * (r1 * r1 + r2 * r2))
        self.assertEqual(c, F(16, 25))

    def test_record_threshold(self) -> None:
        p1 = F(5429, 6250)
        alpha = F(269, 400)
        threshold = (1 + alpha / p1) / 2
        self.assertEqual(threshold, F(77057, 86864))
        self.assertGreater(p1 * F(4, 5), alpha)


if __name__ == "__main__":
    unittest.main()
