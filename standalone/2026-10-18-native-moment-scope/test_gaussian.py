"""Primitive numerical rejection tests on small fixtures, with directed balls.

Corruptions affect BOTH producer and replay; mere JSON consistency cannot
reject them. The longer source or separate HNF path must reject them.
"""
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from flint import arb
import gaussian as G
import ideals as I
from replay_gaussian import replay

HERE = Path(__file__).resolve().parent


class DirectedPrimitiveTests(unittest.TestCase):
    def write_fixture(self, directory):
        p = Path(directory)/'fixture.json'
        p.write_text(G.serial(G.produce(max_power=0, B=7, ratio=4096, precision=192)),
                     encoding='utf-8', newline='\n')
        return p

    def temporary(self):
        return tempfile.TemporaryDirectory(prefix='.gaussian-tests-', dir=HERE)

    def test_true_primitive_fixture_replays(self):
        with self.temporary() as directory:
            I.require(Path(directory).resolve().is_relative_to(HERE), 'Temporary path escaped workspace.')
            result = replay(self.write_fixture(directory))
            self.assertEqual(result['authenticated_complete_principal_ideals'], 3)
            self.assertEqual(result['longer_replay_enclosure_comparisons'], 7)

    def test_omitting_the_infinite_tail_in_both_paths_is_rejected(self):
        with self.temporary() as directory:
            I.require(Path(directory).resolve().is_relative_to(HERE), 'Temporary path escaped workspace.')
            with patch.object(G, 'tail_bound', return_value=arb(0)):
                fixture = self.write_fixture(directory)
                with self.assertRaisesRegex(ValueError, 'longer/higher-precision containment'):
                    replay(fixture)

    def test_same_wrong_split_mask_in_producer_and_replay_is_rejected(self):
        correct_coefficients = I.mask_coefficients_from_principal

        def wrong_coefficients(principal, signature):
            signature = tuple((p, 2 if p == 7 and count == 1 else count)
                              for p, count in signature)
            return correct_coefficients(principal, signature)

        with self.temporary() as directory:
            I.require(Path(directory).resolve().is_relative_to(HERE), 'Temporary path escaped workspace.')
            with patch.object(I, 'mask_coefficients_from_principal', wrong_coefficients):
                fixture = self.write_fixture(directory)
                with self.assertRaisesRegex(ValueError, 'Individual-ideal primitive Gaussian'):
                    replay(fixture)

    def test_self_consistent_loss_of_a_conjugate_row_is_rejected(self):
        correct_grouping = G.principal_masks

        def wrong_grouping(B):
            groups = correct_grouping(B)
            groups[((7, 1),)] = groups[((7, 1),)][:1]
            return groups

        with self.temporary() as directory:
            I.require(Path(directory).resolve().is_relative_to(HERE), 'Temporary path escaped workspace.')
            with patch.object(G, 'principal_masks', wrong_grouping):
                fixture = self.write_fixture(directory)
                with self.assertRaisesRegex(ValueError, 'Complete principal ideal B-cap coverage'):
                    replay(fixture)

    def test_tail_domain_requires_the_decreasing_profile(self):
        with self.assertRaisesRegex(ValueError, 'strictly decreasing'):
            G.tail_bound(1, 2**64)

    def test_refined_counting_bound_and_wrong_inert_norm_are_distinguished(self):
        def total(x):
            # Independent exact scalar coefficients of zeta(s)L(s,chi_-3).
            return sum((1 if d % 3 == 1 else -1 if d % 3 == 2 else 0)*(x//d)
                       for d in range(1, x+1))

        counts = {x: total(x)-total(x//3)-total(x//4)+total(x//12)
                  for x in (1, 3, 4, 12, 512, 4096, 65536, 1048576)}

        def authenticate():
            A, B = G.exterior_counting_constants()
            for x, exact in counts.items():
                I.require(I.exterior_ideal_count(x) == exact,
                          'Hyperbola boundary count differs from the independent full divisor sum.')
                I.require(A*x+B*arb(x).sqrt() >= exact,
                          'Exact exterior ideal count exceeds its proposed envelope.')

        authenticate()
        A, B = G.exterior_counting_constants()
        # Treating the inert prime over 2 as norm 2 changes the leading
        # density from kappa/2 to kappa/3. Large exact counts reject it.
        with patch.object(G, 'exterior_counting_constants', return_value=(A*2/3, B)):
            with self.assertRaisesRegex(ValueError, 'Exact exterior ideal count'):
                authenticate()

        correct_count = I.exterior_ideal_count
        with patch.object(I, 'exterior_ideal_count', side_effect=lambda x: correct_count(x)+1):
            with self.assertRaisesRegex(ValueError, 'Hyperbola boundary count'):
                authenticate()

    def test_boundary_count_matches_every_small_hnf_prefix(self):
        by_norm = [0]*513
        for ideal in I.ideals_up_to(512):
            if I.exterior(ideal):
                by_norm[I.norm(ideal)] += 1
        total = 0
        for x, number in enumerate(by_norm):
            total += number
            self.assertEqual(I.exterior_ideal_count(x), total)

    def test_integer_powers_cover_zero_crossings_and_negative_values(self):
        zero_crossing = arb(0, 1)
        squared = G.integer_power(zero_crossing, 2)
        self.assertEqual(str(zero_crossing), str(arb(0, 1)))
        self.assertTrue(squared.is_finite())
        self.assertTrue(squared.contains(0) and squared.contains(1))
        cube = G.integer_power(arb(-2, 1), 3)
        self.assertTrue(cube.contains(-27) and cube.contains(-1))
        self.assertTrue(G.square_ball(zero_crossing).is_finite())


if __name__ == '__main__':
    unittest.main()
