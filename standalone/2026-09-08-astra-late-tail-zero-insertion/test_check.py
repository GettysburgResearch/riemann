#!/usr/bin/env python3
"""Actual CLI rejections; mathematical infinite statements are not tested here."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
import check

ROOT=Path(__file__).resolve().parent


def seal(p:Path):
    names=sorted(check.FILES-{'SHA256SUMS'})
    (p/'SHA256SUMS').write_text(''.join(
        hashlib.sha256((p/name).read_bytes()).hexdigest()+'  '+name+'\n' for name in names))


def edit_result(p:Path, mutation):
    path=p/'verification.json'; obj=json.loads(path.read_text());mutation(obj)
    path.write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n');seal(p)


class LTTests(unittest.TestCase):
    def test_pristine_cli(self):
        cmd=[sys.executable,'-B']+(['-O'] if sys.flags.optimize else [])+[str(ROOT/'check.py')]
        proc=subprocess.run(cmd,capture_output=True,text=True,timeout=15)
        self.assertEqual(proc.returncode,0,proc.stderr)
        self.assertIn('PASS_LT26_BOUNDED_ALGEBRA',proc.stdout)

    def test_strict_exact_types(self):
        for x in (True,1.0,'1'):
            with self.assertRaises((ValueError,TypeError)):
                check.Q(x)
        self.assertFalse(check.same({'n':1},{'n':True}))
        self.assertFalse(check.same({'n':1},{'n':1.0}))

    def test_cli_corruptions(self):
        mutations=[
            ('false_rh', lambda p: edit_result(p,lambda x:x.__setitem__('rh_established',True))),
            ('false_actual_zero',lambda p:edit_result(p,lambda x:x.__setitem__('actual_zero_numerically_evaluated',True))),
            ('source_not_changed',lambda p:edit_result(p,lambda x:x.__setitem__('source_changed',False))),
            ('wrong_U',lambda p:edit_result(p,lambda x:x['interpolation'][0].__setitem__('U','0/1'))),
            ('missing_panel',lambda p:edit_result(p,lambda x:x['interpolation'].pop())),
            ('numeric_alias',lambda p:edit_result(p,lambda x:x['interpolation'][0].__setitem__('r',True))),
            ('float_alias',lambda p:edit_result(p,lambda x:x.__setitem__('total_panels',190.0))),
            ('duplicate_json',lambda p:self.duplicate(p)),
            ('empty_manifest',lambda p:(p/'SHA256SUMS').write_text('')),
            ('extra_input',lambda p:(p/'extra.txt').write_text('not declared\n')),
            ('changed_parent',lambda p:(p.parent/check.PARENT/'PROOF.md').write_text('changed source\n')),
            ('symlink_input',lambda p:self.symlink(p)),
        ]
        for name,fn in mutations:
            with self.subTest(name=name),tempfile.TemporaryDirectory() as td:
                base=Path(td)/'standalone';base.mkdir()
                dest=base/ROOT.name;shutil.copytree(ROOT,dest)
                pd=base/check.PARENT;pd.mkdir()
                shutil.copyfile(ROOT.parent/check.PARENT/'PROOF.md',pd/'PROOF.md')
                fn(dest)
                cmd=[sys.executable,'-B']+(['-O'] if sys.flags.optimize else [])+[str(dest/'check.py')]
                proc=subprocess.run(cmd,capture_output=True,text=True,timeout=15)
                self.assertNotEqual(proc.returncode,0,(name,proc.stdout))
                self.assertIn('REJECT:',proc.stderr)
        print('LT26_COMPLETED_CLI_REFUSALS=12')

    @staticmethod
    def duplicate(p):
        f=p/'verification.json'; text=f.read_text();f.write_text(text.replace('{','{"schema":"duplicate",',1));seal(p)

    @staticmethod
    def symlink(p):
        original=p/'README.md'; replacement=p.parent/'external.md'
        original.rename(replacement);original.symlink_to(replacement)
        # identical bytes and original checksum: reject the path type, not a hash error


if __name__=='__main__':
    unittest.main(verbosity=2)
