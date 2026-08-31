"""Independent ordered-record and input-binding controls for the physical tail."""
from fractions import Fraction as F
import importlib.util
import json
from math import comb
from pathlib import Path
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / 'research/riemann-structures/native-five-hour-pass/infinite-source/physical_horizon_tail.py'
spec = importlib.util.spec_from_file_location('native_horizon_tail_test', TARGET)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def sqrt_minus_coefficient(e):
    return F(1) if e == 0 else -F(comb(2*e, e), 4**e*(2*e-1))


def factor235(n):
    exponents = []
    for p in (2, 3, 5):
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        exponents.append(e)
    return tuple(exponents) if n == 1 else None


class NativeHorizonTailTests(unittest.TestCase):
    def test_original_Gram_binding(self):
        source = m.authenticate_gram(m.core.authenticate())
        self.assertEqual(source['sha256'], m.GRAM_SHA)
        self.assertFalse(source['complete_Gram_recomputed_here'])

    def test_corrupted_core_refused_before_import(self):
        with patch.object(m, 'CORE_SHA', '0'*64):
            with self.assertRaisesRegex(ValueError, 'before import'):
                m.load_core()

    def test_corrupted_Gram_binding_refused(self):
        with patch.object(m, 'GRAM_SHA', '0'*64):
            with self.assertRaisesRegex(ValueError, 'Gram capture'):
                m.authenticate_gram(m.core.authenticate())

    def test_weights_against_central_binomial_closed_coefficients(self):
        w, u = m.weights(61)
        for e in range(62):
            a = sqrt_minus_coefficient(e//2) if e % 2 == 0 else F(0)
            b = sqrt_minus_coefficient(e)
            self.assertEqual(w[e], abs(a)+abs(b-a))
            closed = (F(2) if e == 0 else F(0)) + (-1)**e*b - 2*a
            self.assertEqual(w[e], closed)
            self.assertEqual(u[e], sum(w[i]*w[e-i] for i in range(e+1)))

    def test_complete_smooth_census_against_integer_factorization(self):
        for H in (1, 2, 8, 30, 90, 450, 777):
            literal = {n: factor235(n) for n in range(1, H+1) if factor235(n) is not None}
            acquired = {n: (a, b, c) for n, a, b, c in m.smooth_products(H)}
            self.assertEqual(acquired, literal)
            self.assertEqual(len(acquired), len(list(m.smooth_products(H))))

    def test_literal_ordered_pairs_match_product_convolution(self):
        for H in (1, 2, 8, 30, 90, 450):
            w, u = m.weights(H.bit_length()-1)
            records = [(n, w[a]*w[b]*w[c]) for n, a, b, c in m.smooth_products(H)]
            direct = {}
            for n, a in records:
                for r, b in records:
                    if n*r <= H:
                        direct[n*r] = direct.get(n*r, F(0)) + a*b
            convolution = {n: u[a]*u[b]*u[c] for n, a, b, c in m.smooth_products(H)}
            self.assertEqual(direct, convolution)

    def test_original_weighted_prefix_from_literal_pairs(self):
        arb, _, _, ctx = m.core.arb_import()
        ctx.prec = 192
        H = 90
        w, _ = m.weights(H.bit_length()-1)
        records = [(n, w[a]*w[b]*w[c]) for n, a, b, c in m.smooth_products(H)]
        direct = arb(0)
        for n, a in records:
            for r, b in records:
                if n*r <= H:
                    weight = a*b
                    direct += arb(weight.numerator)/weight.denominator/arb(n*r).sqrt()
        compressed, _, _ = m.prefix(H, arb)
        self.assertTrue(direct.overlaps(compressed))

    def test_decoder_factor_two_bound(self):
        for a in m.core.BITS:
            for b in m.core.BITS:
                self.assertLessEqual(max(map(abs, m.core.decoder(a, b))), 2)

    def test_typed_replay_and_ambiguous_JSON_rejection(self):
        self.assertNotEqual(m.canonical({'value': True}), m.canonical({'value': 1}))
        self.assertNotEqual(m.canonical({'value': 1}), m.canonical({'value': 1.0}))
        for raw in ('{"a":1,"a":2}', '{"a":NaN}', '{"a":Infinity}'):
            with self.assertRaises(ValueError):
                m.strict_load(raw)
        self.assertEqual(m.strict_load(json.dumps({'a': [1, '1', True]})), {'a': [1, '1', True]})

    def test_explicit_caps_and_bool_horizon_refused(self):
        for H in (True, 0, -1, 2**62, 1.5):
            with self.assertRaises(ValueError):
                list(m.smooth_products(H))
        for N in (True, -1, 62, 1.5):
            with self.assertRaises(ValueError):
                m.weights(N)


if __name__ == '__main__':
    unittest.main()
