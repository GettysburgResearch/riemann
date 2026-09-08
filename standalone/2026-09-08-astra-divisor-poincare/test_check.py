#!/usr/bin/env python3
"""Actual CLI refusals for DPG26. Runs only bounded isolated copies."""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).absolute().parent
FILES = {
    'PROOF.md','README.md','REVIEW_AND_SOURCES.md','VALIDATION.md','SOURCE_LOCK.json',
    'check.py','test_check.py','verification.json','SHA256SUMS',
}


def seal(root: Path) -> None:
    text=''.join(hashlib.sha256((root/n).read_bytes()).hexdigest()+'  '+n+'\n'
                 for n in sorted(FILES-{'SHA256SUMS'}))
    (root/'SHA256SUMS').write_text(text)


def run(root: Path) -> subprocess.CompletedProcess:
    args=[sys.executable,'-I','-S','-B']
    if sys.flags.optimize: args.append('-O')
    args += [str(root/'check.py')]
    return subprocess.run(args,capture_output=True,text=True,timeout=25)


class ReplayTests(unittest.TestCase):
    def test_pristine(self):
        got=run(ROOT)
        self.assertEqual(got.returncode,0,got.stderr)
        self.assertIn('PASS_DPG26_BOUNDED_EXACT_CONTROLS',got.stdout)

    def mutation(self, label, change, reseal=True):
        with tempfile.TemporaryDirectory(prefix='dpg26-') as td:
            root=Path(td)/'packet'; shutil.copytree(ROOT,root)
            change(root)
            if reseal: seal(root)
            got=run(root)
            self.assertNotEqual(got.returncode,0,label+': accepted corrupt packet')
            self.assertIn('REJECT_DPG26',got.stderr,label+': did not reach controlled rejection')

    def test_semantic_and_binding_refusals(self):
        def result_field(name,value):
            def change(root):
                p=root/'verification.json'; obj=json.loads(p.read_text()); obj[name]=value
                p.write_text(json.dumps(obj,sort_keys=True,indent=2)+'\n')
            return change
        cases=[
            ('false RH',result_field('rh_proved',True)),
            ('wrong constant',result_field('gap_denominator_factor',12)),
            ('Boolean numeric alias',result_field('gap_denominator_factor',True)),
            ('float alias',result_field('gap_denominator_factor',24.0)),
            ('omega replacement',result_field('distinct_factor_depth','Omega')),
            ('dropped powers flag',result_field('all_prime_powers_retained',False)),
        ]
        for label,change in cases:
            with self.subTest(case=label): self.mutation(label,change)
        def bad_source(root):
            p=root/'SOURCE_LOCK.json'; obj=json.loads(p.read_text());obj['graph_commit']='0'*40
            p.write_text(json.dumps(obj,sort_keys=True,indent=2)+'\n')
        self.mutation('wrong source commit',bad_source)
        self.mutation('duplicate JSON',lambda r:(r/'verification.json').write_text('{"rh_proved":false,"rh_proved":true}\n'))
        self.mutation('empty groups',result_field('groups',{}))

    def test_algorithm_refusals(self):
        # Reseal each edit: rejection must come from reconstruction, not file hashes.
        def remove_powers(root):
            p=root/'check.py';s=p.read_text()
            needle='for k in range(1,e+1):'
            if needle not in s: raise RuntimeError('mutation anchor missing')
            p.write_text(s.replace(needle,'for k in range(1,min(e,1)+1):',1))
        self.mutation('remove higher-power edges',remove_powers)
        def reverse_tree(root):
            p=root/'check.py';s=p.read_text()
            needle='par = parents(s); trails = paths(s,par)'
            if needle not in s: raise RuntimeError('mutation anchor missing')
            p.write_text(s.replace(needle,'par = parents(s,True); trails = paths(s,par)',1))
        self.mutation('greatest-prime tree substituted',reverse_tree)
        def false_eigenvalue(root):
            p=root/'check.py';s=p.read_text()
            needle='for e in range(m+1)],j+a'
            if needle not in s: raise RuntimeError('mutation anchor missing')
            p.write_text(s.replace(needle,'for e in range(m+1)],j+a+1',1))
        self.mutation('wrong exact spectrum',false_eigenvalue)

    def test_package_refusals(self):
        self.mutation('altered proof bytes',lambda r:(r/'PROOF.md').write_text('unverified replacement\n'),False)
        self.mutation('missing manifest',lambda r:(r/'SHA256SUMS').unlink(),False)
        self.mutation('extra file',lambda r:(r/'extra.txt').write_text('extra\n'))
        def symlink(root):
            q=root/'PROOF.md'; payload=root.parent/'outside.md';payload.write_bytes(q.read_bytes());q.unlink();q.symlink_to(payload)
        self.mutation('symlink proof',symlink)


if __name__=='__main__':
    unittest.main(verbosity=2)
