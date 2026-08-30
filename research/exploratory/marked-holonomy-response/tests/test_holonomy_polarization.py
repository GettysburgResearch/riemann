"""Exact controls for the separately reviewed positive-defect sequel."""

import hashlib
import importlib.util
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
SOURCE = HERE / "holonomy_response.py"
EXPECTED = "5d1b7596344ce028c4c1cbe8c045a3ad485b427d73ccb8cdfe9355336db623dc"
if hashlib.sha256(SOURCE.read_bytes().replace(b"\r\n", b"\n")).hexdigest() != EXPECTED:
    raise ValueError("reviewed e7fc8b0a holonomy producer changed before import")
spec = importlib.util.spec_from_file_location("polarized_holonomy", SOURCE)
h = importlib.util.module_from_spec(spec)
spec.loader.exec_module(h)
c = h.c


def sub(a, b):
    return c.matrix(
        [
            [x - y for x, y in zip(ar, br, strict=True)]
            for ar, br in zip(a, b, strict=True)
        ]
    )


def scale(a, value):
    return c.matrix([[value * x for x in row] for row in a])


def defect(u, v):
    k = h.word_operator(u, v, True)
    half_sum = c.matrix(
        [[(k[i][j] + k[j][i]) / 2 for j in range(len(k))] for i in range(len(k))]
    )
    return sub(c.eye(len(k)), half_sum)


class HolonomyPolarizationTests(unittest.TestCase):
    def test_gram_factorizations_for_every_predeclared_pair(self):
        pairs = [([1, 0, 2], [0, 2, 1]), *h.SOURCE["held_out_s4_pairs"]]
        for p, q in pairs:
            u, v = c.permutation(p), c.permutation(q)
            delta = sub(c.mul(u, v), c.mul(v, u))
            k_delta = sub(c.eye(len(p)), h.word_operator(u, v, True))
            self.assertEqual(
                defect(u, v), scale(c.mul(c.transpose(delta), delta), c.Q(1, 2))
            )
            self.assertEqual(
                defect(u, v), scale(c.mul(c.transpose(k_delta), k_delta), c.Q(1, 2))
            )

    def test_principal_kernel_and_s3_exact_spectrum(self):
        u, v = c.permutation([1, 0, 2]), c.permutation([0, 2, 1])
        a = defect(u, v)
        self.assertEqual([sum(row) for row in a], [0, 0, 0])
        self.assertEqual(c.trace(a), 3)
        self.assertEqual(c.det_poly_leibniz(a), [1, -3, c.Q(9, 4)])
        self.assertEqual(c.mul(a, a), scale(a, c.Q(3, 2)))

    def test_orthogonal_strict_defect_and_abelian_zero(self):
        u, v = c.matrix([[0, 1], [1, 0]]), c.matrix([[1, 0], [0, -1]])
        self.assertEqual(defect(u, v), scale(c.eye(2), 2))
        self.assertEqual(defect(u, u), c.matrix([[0, 0], [0, 0]]))

    def test_full_transfer_unitarity_positive_identity_and_reciprocity(self):
        u, v = c.matrix([[0, 1], [1, 0]]), c.matrix([[1, 0], [0, -1]])
        identity = c.eye(6)
        for reverse in (False, True):
            t = h.transfer(u, v, reverse)
            self.assertEqual(c.mul(c.transpose(t), t), identity)
            cube = c.mul(c.mul(t, t), t)
            delta = sub(identity, cube)
            real = scale(
                c.matrix(
                    [[delta[i][j] + delta[j][i] for j in range(6)] for i in range(6)]
                ),
                c.Q(1, 2),
            )
            self.assertEqual(real, scale(c.mul(c.transpose(delta), delta), c.Q(1, 2)))
            polynomial = c.det_poly_leibniz(t)
            self.assertEqual(polynomial, polynomial[::-1])
        self.assertEqual(
            c.mul(c.mul(h.transfer(u, v), h.transfer(u, v)), h.transfer(u, v)), identity
        )

    def test_covariance_of_positive_defect(self):
        u, v = c.permutation([1, 0, 2]), c.permutation([0, 2, 1])
        q = c.matrix([[c.Q(3, 5), -c.Q(4, 5), 0], [c.Q(4, 5), c.Q(3, 5), 0], [0, 0, 1]])

        def conjugate(a):
            return c.mul(c.mul(c.transpose(q), a), q)

        self.assertEqual(defect(conjugate(u), conjugate(v)), conjugate(defect(u, v)))


if __name__ == "__main__":
    unittest.main()
