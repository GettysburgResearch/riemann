"""Controls for the pinned primitive gate, without modifying frozen files."""
from pathlib import Path
from types import ModuleType
from unittest.mock import patch
import hashlib
import json
import sys
import unittest
import source_provenance as p


class Tests(unittest.TestCase):
    def test_pristine_frozen_bytes(self):
        sources = p.verified_sources()
        self.assertEqual(set(sources), set(p.EXPECTED_SHA256))
        for name, raw in sources.items():
            self.assertEqual(hashlib.sha256(raw).hexdigest(), p.EXPECTED_SHA256[name])

    def test_changed_source_with_resealed_receipt_rejected_before_execution(self):
        original_bytes = Path.read_bytes
        original_text = Path.read_text
        altered = original_bytes(p.HERE / 'predecessor' / 'native_theta.py') + b'\nraise RuntimeError("must not execute")\n'
        receipt = p.expected_receipt()
        receipt['files'][1]['sha256'] = hashlib.sha256(altered).hexdigest()

        def read_bytes(path):
            return altered if path.name == 'native_theta.py' else original_bytes(path)

        def read_text(path, *args, **kwargs):
            return json.dumps(receipt) if path.name == 'predecessor-provenance.json' else original_text(path, *args, **kwargs)

        with patch.object(Path, 'read_bytes', read_bytes), patch.object(Path, 'read_text', read_text), patch('builtins.exec') as execute:
            with self.assertRaisesRegex(p.SourceAuthenticationError, 'native_theta.py'):
                p.load_primitives()
            execute.assert_not_called()

    def test_receipt_alone_cannot_change_commit(self):
        receipt = p.expected_receipt()
        receipt['commit'] = '0' * 40
        with patch.object(Path, 'read_text', return_value=json.dumps(receipt)):
            with self.assertRaisesRegex(p.SourceAuthenticationError, 'receipt'):
                p.verified_sources()

    def test_preloaded_import_substitute_is_ignored_and_restored(self):
        substitute = ModuleType('exact_interval')
        substitute.I = object()
        with patch.dict(sys.modules, {'exact_interval': substitute}):
            modules = p.load_primitives()
            self.assertIsNot(modules['exact_interval'], substitute)
            self.assertEqual(modules['exact_interval'].I.q(1).bounds(), ['1', '1'])
            self.assertIs(sys.modules['exact_interval'], substitute)


if __name__ == '__main__':
    unittest.main()
