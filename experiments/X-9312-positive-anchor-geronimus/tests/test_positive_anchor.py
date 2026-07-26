from fractions import Fraction
from pathlib import Path
import unittest

import positive_anchor as pa


class PositiveAnchorTests(unittest.TestCase):
    def test_recurrence(self):
        old = [Fraction(3), Fraction(5), Fraction(11), Fraction(29), Fraction(83)]
        w = Fraction(2)
        b = pa.augmented_moments(old, w, Fraction(7))
        self.assertEqual([b[k + 1] + w * b[k] for k in range(len(old))], old)

    def test_adapted_schur_witnesses(self):
        # Strict Stieltjes moments of atoms 1,3,5 through degree four.
        old = [Fraction(3), Fraction(9), Fraction(35), Fraction(153), Fraction(707)]
        w = Fraction(2)
        gate = pa.positive_anchor_gate(old, w)
        lower, upper = gate["lower"], gate["upper"]
        self.assertLess(lower, upper)

        below = lower - Fraction(1, 17)
        b = pa.augmented_moments(old, w, below)
        z = gate["lower_solve"]
        value0 = b[0] - 2 * pa.dot(z, old[:2])
        c0 = [
            [old[i + j + 1] + w * old[i + j] for j in range(2)]
            for i in range(2)
        ]
        value0 += sum(
            z[i] * c0[i][j] * z[j] for i in range(2) for j in range(2)
        )
        self.assertEqual(value0, below - lower)
        self.assertLess(value0, 0)

        above = upper + Fraction(1, 19)
        z = gate["upper_solve"]
        value1 = old[0] - w * above - 2 * pa.dot(z, old[1:3])
        c1 = [
            [old[i + j + 2] + w * old[i + j + 1] for j in range(2)]
            for i in range(2)
        ]
        value1 += sum(
            z[i] * c1[i][j] * z[j] for i in range(2) for j in range(2)
        )
        self.assertEqual(value1, w * (upper - above))
        self.assertLess(value1, 0)

    def test_reduced_replay_identity(self):
        nodes = [Fraction(1, 16), Fraction(1, 4), Fraction(1)]
        w = Fraction(2)
        replay = pa.reduced_replay(nodes, w, reference_index=1)
        values = [Fraction(13), Fraction(17), Fraction(23), Fraction(31)]
        direct = sum(c * f for c, f in zip(replay["augmented_beta"], values))
        reduced = replay["beta_anchor"] * (values[0] - values[2])
        old_values = values[1:]
        old_basis_values = []
        for degree in range(len(nodes) - 1):
            beta = pa.response_basis_vector(nodes, degree)
            old_basis_values.append(sum(c * f for c, f in zip(beta, old_values)))
        reduced += sum(
            coefficient * value
            for coefficient, value in zip(
                replay["old_response_coefficients"], old_basis_values
            )
        )
        self.assertEqual(direct, reduced)

    def test_zero_anchor_limit_lower_gate(self):
        old = [Fraction(3), Fraction(9), Fraction(35), Fraction(153), Fraction(707)]
        m = 2
        r = old[:m]
        c = [[old[i + j + 1] for j in range(m)] for i in range(m)]
        expected = pa.dot(r, pa.exact_solve(c, r))
        tiny = Fraction(1, 10**8)
        gate = pa.positive_anchor_gate(old, tiny)
        self.assertLess(abs(gate["lower"] - expected), Fraction(1, 1000))

    def test_duplicate_anchor_rejected(self):
        with self.assertRaises(pa.GateError):
            pa.reduced_replay([Fraction(1), Fraction(2)], Fraction(1))

    def test_pr103_w4_gate_regression(self):
        experiments = Path(__file__).resolve().parents[2]
        basis = (
            experiments
            / "X-9306-real-log-portfolio-search"
            / "results"
            / "basis.json"
        )
        data, intervals = pa.load_basis(basis)
        result = pa.build_result(data, intervals, Fraction(4))
        self.assertEqual(
            result["gate"]["lower_decimal"],
            "27375115.77715610683338270942781224884018061645431803605379046514229193",
        )
        self.assertEqual(
            result["gate"]["upper_decimal"],
            "27375115.77715610684289268397858616575745335517506270982011990857512056",
        )


if __name__ == "__main__":
    unittest.main()
