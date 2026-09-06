#!/usr/bin/env python3
"""Independent synthetic Git/Markdown/JSON regression, not the Riemann checkout."""
from __future__ import annotations
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('release_hardening', HERE / 'verify.py')
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


class ContractTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / 'repo'
        self.root.mkdir()
        self.call('init', '-q')
        self.call('config', 'core.autocrlf', 'false')
        self.call('config', 'user.name', 'Synthetic fixture')
        self.call('config', 'user.email', 'fixture@example.invalid')
        self.write('reviews/A/CLAIMS.tsv', 'id\tverdict\nA1\tHOLD\n')
        self.write('README.md', '# Start\n\n[Evidence](reviews/A/REPORT.md#exact-scope)\n')
        self.write('reviews/A/REPORT.md', '# Review\n\n## Exact scope\nNo proof claim.\n')
        self.call('add', '.')
        self.call('commit', '-qm', 'synthetic source')
        self.pins = {'reviews/A': self.call('rev-parse', 'HEAD:reviews/A').decode().strip()}
        self.tree = v.tracked_tree(self.root)

    def tearDown(self):
        self.temp.cleanup()

    def call(self, *args):
        return subprocess.check_output(['git', '-c', 'core.hooksPath=/dev/null', *args], cwd=self.root,
                                       stderr=subprocess.DEVNULL)

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(text.encode('utf-8'))

    def auth(self):
        return v.authenticate(self.root, self.tree, ('reviews/A', 'README.md'), self.pins)

    def symlink(self, path, target, *, directory=False):
        try:
            path.symlink_to(target, target_is_directory=directory)
        except OSError as error:
            if os.name == 'nt' and getattr(error, 'winerror', None) == 1314:
                self.skipTest('Windows account lacks symbolic-link privilege')
            raise

    def test_clean_snapshot(self):
        self.assertEqual(self.auth()['files'], 3)

    def test_changed_bytes(self):
        self.write('reviews/A/CLAIMS.tsv', 'id\tverdict\nA1\tVERIFIED\n')
        with self.assertRaisesRegex(ValueError, 'working bytes'):
            self.auth()

    def test_assume_unchanged_does_not_hide_mutation(self):
        self.call('update-index', '--assume-unchanged', 'reviews/A/CLAIMS.tsv')
        self.write('reviews/A/CLAIMS.tsv', 'id\tverdict\nA1\tVERIFIED\n')
        self.assertEqual(self.call('status', '--porcelain').strip(), b'')
        with self.assertRaisesRegex(ValueError, 'working bytes'):
            self.auth()

    def test_staged_data_not_in_head(self):
        self.write('reviews/A/CLAIMS.tsv', 'id\tverdict\nA1\tVERIFIED\n')
        self.call('add', '.')
        with self.assertRaisesRegex(ValueError, 'working bytes'):
            self.auth()

    def test_missing_working_file(self):
        (self.root / 'reviews/A/CLAIMS.tsv').unlink()
        with self.assertRaisesRegex(ValueError, 'missing working-tree'):
            self.auth()

    def test_leaf_symlink_even_with_matching_bytes(self):
        p = self.root / 'reviews/A/CLAIMS.tsv'
        outside = self.root.parent / 'copy.tsv'
        outside.write_bytes(p.read_bytes())
        p.unlink()
        self.symlink(p, outside)
        with self.assertRaisesRegex(ValueError, 'symlink'):
            self.auth()

    def test_parent_symlink(self):
        old = self.root / 'reviews/A'
        moved = self.root.parent / 'A'
        old.rename(moved)
        self.symlink(old, moved, directory=True)
        with self.assertRaisesRegex(ValueError, 'symlink'):
            self.auth()

    def test_untracked_file(self):
        self.write('reviews/A/extra.py', 'raise SystemExit(0)\n')
        with self.assertRaisesRegex(ValueError, 'untracked files'):
            self.auth()

    def test_ignored_file_still_untracked(self):
        self.write('.gitignore', 'reviews/A/extra.py\n')
        self.write('reviews/A/extra.py', 'raise SystemExit(0)\n')
        with self.assertRaisesRegex(ValueError, 'untracked files'):
            self.auth()

    def test_changed_committed_review_tree(self):
        self.write('reviews/A/CLAIMS.tsv', 'id\tverdict\nA1\tVERIFIED\n')
        self.call('add', '.')
        self.call('commit', '-qm', 'bad source replacement')
        self.tree = v.tracked_tree(self.root)
        with self.assertRaisesRegex(ValueError, 'frozen source tree'):
            self.auth()

    def test_no_scope_is_not_success(self):
        with self.assertRaisesRegex(ValueError, 'empty authentication scope'):
            v.authenticate(self.root, self.tree, ('absent',), {})

    def test_clean_navigation(self):
        self.assertEqual(v.check_links(self.root, self.tree, ('README.md',))['local_links_and_anchors'], 1)

    def nav_fixture(self, text):
        self.write('README.md', text)
        self.call('add', '.')
        self.call('commit', '-qm', 'navigation mutation')
        self.tree = v.tracked_tree(self.root)
        return v.check_links(self.root, self.tree, ('README.md',))

    def test_missing_local_target(self):
        with self.assertRaisesRegex(ValueError, 'broken local link'):
            self.nav_fixture('[Bad](missing.md)\n')

    def test_missing_local_anchor(self):
        with self.assertRaisesRegex(ValueError, 'broken local anchor'):
            self.nav_fixture('[Bad](reviews/A/REPORT.md#absent)\n')

    def test_fenced_examples_are_not_navigation(self):
        r = self.nav_fixture('# Start\n```md\n[Example](missing.md)\n```\n')
        self.assertEqual(r['local_links_and_anchors'], 0)

    def test_inline_examples_are_not_navigation(self):
        self.assertEqual(self.nav_fixture('`[Example](missing.md)`\n')['local_links_and_anchors'], 0)

    def test_latex_divided_differences_are_not_links(self):
        r = self.nav_fixture(r"\[ [a,b,c](1/p) \]" + "\n" + r"\( [a,b](tp) \)" + "\n")
        self.assertEqual(r['local_links_and_anchors'], 0)

    def test_dollar_math_is_not_navigation(self):
        r = self.nav_fixture("$$ [a,b](missing) $$\n$[a,b](missing)$\n")
        self.assertEqual(r['local_links_and_anchors'], 0)

    def test_directory_target(self):
        self.write('reviews/A/README.md', '# Directory\n')
        self.assertEqual(self.nav_fixture('[Read](reviews/A/)\n')['local_links_and_anchors'], 1)

    def test_parent_path_escape(self):
        with self.assertRaisesRegex(ValueError, 'escaping link'):
            self.nav_fixture('[Bad](../../outside.md)\n')

    def test_unsafe_scheme(self):
        with self.assertRaisesRegex(ValueError, 'unsafe link scheme'):
            self.nav_fixture('[Bad](javascript://invalid)\n')

    def test_reference_definition(self):
        with self.assertRaisesRegex(ValueError, 'broken local link'):
            self.nav_fixture('[Read][x]\n\n[x]: missing.md\n')

    def test_source_path_escape(self):
        for p in ('../x', '/x', 'x/../../y', '.git/config', 'a\\b', 'a:b', 'a\nb'):
            with self.subTest(path=p), self.assertRaises(ValueError):
                v.safe_path(self.root, p)

    def test_duplicate_json(self):
        with self.assertRaisesRegex(ValueError, 'duplicate JSON'):
            v.decode_json(b'{"status":false,"status":true}')

    def test_nonfinite_json(self):
        for number in ('NaN', 'Infinity', '-Infinity'):
            with self.subTest(number=number), self.assertRaises(ValueError):
                v.decode_json(('{"x":' + number + '}').encode())

    def test_pointer_bool_not_integer(self):
        pointer = {'release':'2026-09-06', 'manifest':v.RELEASE+'/RELEASE.json',
                   'resolver':v.RELEASE+'/hardening/verify.py', 'previous_release':'2026-08-22',
                   'rh_proved':False}
        v.verify_pointer(pointer)
        pointer['rh_proved'] = 0
        with self.assertRaises(ValueError):
            v.verify_pointer(pointer)

    def test_pointer_rejects_unknown_fields(self):
        pointer = {'release':'2026-09-06', 'manifest':v.RELEASE+'/RELEASE.json',
                   'resolver':v.RELEASE+'/hardening/verify.py', 'previous_release':'2026-08-22',
                   'rh_proved':False, 'proof_accepted':True}
        with self.assertRaises(ValueError):
            v.verify_pointer(pointer)

    def test_anchor_duplicates_and_explicit_id(self):
        self.assertEqual(v.anchors('# Same\n# Same\n<a id="Exact"></a>\n## A & B\n'),
                         {'same', 'same-1', 'Exact', 'a--b'})

    def test_live_cli_rejects_output_inside_repository(self):
        result = subprocess.run([sys.executable, '-I', '-S', '-B',
                                 *(['-O'] if sys.flags.optimize else []),
                                 str(HERE/'verify.py'), '--output', str(HERE/'must-not-create')],
                                capture_output=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn(b'output must be outside', result.stderr)
        self.assertFalse((HERE/'must-not-create').exists())


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(ContractTests)
    result = unittest.TextTestRunner(stream=sys.stderr, verbosity=1).run(suite)
    marker = ('PASS_SYNTHETIC_HARDENING_CONTRACTS_WITH_SKIPS' if result.skipped
              else 'PASS_SYNTHETIC_HARDENING_CONTRACTS') if result.wasSuccessful() else 'FAIL'
    payload = {'marker':marker,
               'tests':result.testsRun, 'failures':len(result.failures), 'errors':len(result.errors),
               'skipped':len(result.skipped),
               'real_riemann_checkout':False, 'remote_ci':False, 'lean_build':False,
               'rh_proved':False}
    print(json.dumps(payload, sort_keys=True, indent=2))
    sys.exit(0 if result.wasSuccessful() else 1)
