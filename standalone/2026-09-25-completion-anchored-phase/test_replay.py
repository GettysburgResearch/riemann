#!/usr/bin/env python3
"""CAP36 actual CLI acceptance/refusal tests, also valid under python -O."""
from __future__ import annotations
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent


class ReplayTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.receipt = json.loads((ROOT/'receipt.json').read_text(encoding='utf-8'))

    def run_checker(self, raw: str, optimized=False):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/'input.json'
            path.write_text(raw, encoding='utf-8')
            output = Path(directory)/'output.json'
            cmd = [sys.executable, '-I', '-S', '-B']
            if optimized:
                cmd.append('-O')
            cmd += [str(ROOT/'check.py'), '--check', str(path), '--output', str(output)]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=45)
            data = output.read_bytes() if output.exists() else None
            return result, data

    def check_mutation(self, mutate, optimized=False):
        bad = copy.deepcopy(self.receipt)
        mutate(bad)
        result, data = self.run_checker(json.dumps(bad), optimized)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('REJECT:', result.stderr)
        self.assertIsNone(data)

    def test_pristine_normal_and_optimized(self):
        raw = (ROOT/'receipt.json').read_text(encoding='utf-8')
        for opt in [False, True]:
            result, data = self.run_checker(raw, opt)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(data, raw.encode('utf-8'))

    def test_altered_completion_width(self):
        self.check_mutation(lambda r: r['cap_panels'][-1].__setitem__('width', 7))

    def test_altered_primitive_hash(self):
        self.check_mutation(lambda r: r.__setitem__('mobius_sha256', '0'*64))

    def test_altered_complex_pairing(self):
        def mutate(r):
            value = r['rational_product_kernel_panels'][1]['difference']['im']
            value['num'] += 1
        self.check_mutation(mutate, optimized=True)

    def test_missing_scope(self):
        self.check_mutation(lambda r: r.pop('scope'))

    def test_boolean_number_substitution(self):
        def mutate(r):
            r['predicates']['corrupted primitive rejected'] = True
        self.check_mutation(mutate)

    def test_malformed_json(self):
        result, data = self.run_checker('{')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('REJECT:', result.stderr)
        self.assertIsNone(data)

    def test_duplicate_json_key(self):
        raw = json.dumps(self.receipt)
        raw = '{"packet":"CAP36",'+raw[1:]
        result, data = self.run_checker(raw, optimized=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('duplicate JSON key', result.stderr)
        self.assertIsNone(data)


if __name__ == '__main__':
    unittest.main()
