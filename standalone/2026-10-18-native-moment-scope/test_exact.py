"""Small exact integration and deliberate-corruption tests; no third-party dependency."""
import json
from pathlib import Path
import subprocess
import sys
import unittest

import ideals as I

HERE = Path(__file__).resolve().parent


class ExactReplayTests(unittest.TestCase):
    def run_checker(self, *args, optimized=False):
        command = [sys.executable, '-B']
        if optimized:
            command.append('-O')
        command.extend([str(HERE/'verify.py'), *args])
        return subprocess.run(command, cwd=HERE, text=True, capture_output=True, timeout=120)

    def test_deposited_complete_coverage_reproduces_in_both_modes(self):
        expected = (HERE/'CHECKS.json').read_text(encoding='utf-8')
        for optimized in (False, True):
            with self.subTest(optimized=optimized):
                result = self.run_checker(optimized=optimized)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stdout, expected)

    def test_corrupted_models_fail_at_their_intended_gates(self):
        mutations = {
            'drop-nonunit-mask': 'complete-principal-mask',
            'collapse-split-mask': 'complete-principal-mask',
            'truncate-smooth-powers': 'infinite-mask-convolution',
            'use-H-for-principal-count': 'principal-replica-count',
        }
        for mutation, gate in mutations.items():
            for optimized in (False, True):
                with self.subTest(mutation=mutation, optimized=optimized):
                    result = self.run_checker('--mutation', mutation, optimized=optimized)
                    self.assertNotEqual(result.returncode, 0)
                    self.assertIn(gate+':', result.stderr)

    def test_invalid_lattices_and_bad_coverage_fail_closed(self):
        self.assertFalse(I.valid((3, 1, 1)))
        with self.assertRaisesRegex(ValueError, 'Rank-two'):
            I.hnf(((1, 0), (2, 0)))
        result = self.run_checker('--column-cap', '0')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Column cap', result.stderr)

    def test_compact_integer_storage_preserves_the_exact_source(self):
        for signature in ((), ((7, 1),), ((7, 2),), ((5, 1),), ((7, 1), (13, 1))):
            with self.subTest(signature=signature):
                self.assertEqual(list(I.norm_mobius_coefficients(4096, signature, compact=True)),
                                 I.norm_mobius_coefficients(4096, signature))

    def test_complete_Kummer_source_reproduces_in_both_modes(self):
        expected = (HERE/'KUMMER_CHECKS.json').read_text(encoding='utf-8')
        for optimized in (False, True):
            command = [sys.executable, '-B']+(['-O'] if optimized else [])
            result = subprocess.run(command+[str(HERE/'verify_kummer.py')],
                                    cwd=HERE, text=True, capture_output=True, timeout=120)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout, expected)

    def test_Euler_deletion_recurrence_matches_the_independent_local_factors(self):
        original = I.norm_mobius_coefficients(8192, compact=True)
        saved = original[:]
        signatures = {I.mask_signature(b) for b in I.ideals_up_to(512) if I.exterior(b)}
        for signature in signatures:
            with self.subTest(signature=signature):
                fast = I.mask_coefficients_from_principal(original, signature)
                self.assertEqual(list(fast), I.norm_mobius_coefficients(8192, signature))
        self.assertEqual(original, saved)
        with self.assertRaisesRegex(ValueError, 'Exterior'):
            I.mask_coefficients_from_principal(original, ((2, 1),))


if __name__ == '__main__':
    unittest.main()
