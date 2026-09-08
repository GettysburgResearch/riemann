#!/usr/bin/env python3
"""Unit and actual subprocess rejection tests; no analytic theorem is tested here."""
from __future__ import annotations
import copy
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import replay as r


class ExactTransferTests(unittest.TestCase):
    def test_primitive_and_cutoff_reconstruction(self):
        fresh = r.compute()
        self.assertEqual(fresh['total_controls'], 4353)
        self.assertEqual(r.canonical(fresh), r.canonical(r.load_json(r.ROOT/'verification.json')))

    def test_rational_input_types(self):
        for value in (True, False, 1.0, '1'):
            with self.assertRaises(TypeError):
                r.exact(value)
        for value in (True, 1.0, '1', 0):
            with self.assertRaises(TypeError):
                r.integer(value, 1)

    def test_cutoff_scope_refusal(self):
        for scope in ({}, {'arithmetic_limit': 96}, dict(r.SCOPE, cutoff_limit=0),
                      dict(r.SCOPE, cutoff_limit=True), dict(r.SCOPE, operator_limit=80)):
            with self.assertRaises((ValueError, TypeError)):
                r.compute(scope)

    def test_inverse_needs_prime_powers(self):
        self.assertEqual(r.op('V',9), {1:r.F(1,64),3:-r.F(5,32),9:r.F(9,64)})
        omit = r.add(r.mul(r.op('V',1),r.op('T',9)), r.mul(r.op('V',3),r.op('T',3)))
        self.assertNotEqual(omit, r.op('B',9))
        self.assertEqual(r.add(omit,r.op('V',9)), r.op('B',9))

    def test_squarefree_target_not_ambient(self):
        f4 = r.dual(4)
        self.assertTrue(f4)
        self.assertEqual(sum((v/r.F(n*(n+1)) for n,v in f4.items()),r.F(0)),0)
        self.assertEqual(sum((r.h(4,n)*v/r.F(n*(n+1)) for n,v in f4.items()),r.F(0)),1)
        self.assertEqual(r.dual(5),{1:r.F(2),4:r.F(20),5:-r.F(30)})

    def test_manifest_and_parent_bytes(self):
        r.authenticate()

    def test_cli_rejections(self):
        """Each named case runs the actual CLI, not only an exception helper."""
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
        mode = ['-O'] if sys.flags.optimize else []
        def command(packet: Path, alternate: Path | None = None) -> subprocess.CompletedProcess:
            argv = [sys.executable,*mode,str(packet/'scripts/replay.py')]
            if alternate is not None:
                argv += ['--check',str(alternate)]
            return subprocess.run(argv,capture_output=True,text=True,env=env,timeout=15)
        def seal(packet: Path):
            (packet/'SHA256SUMS').write_text(''.join(
                hashlib.sha256((packet/p).read_bytes()).hexdigest()+'  '+p+'\n'
                for p in sorted(r.INVENTORY)),encoding='utf-8')
        cases = ['rh_flag','scope_empty','scope_bool','changed_coefficient','extra_key',
                 'duplicate_json','float_alias','bad_parent','missing_prime_power',
                 'proof_byte','manifest_empty','unexpected_file','parent_proof_byte']
        selected = os.environ.get('GT26_CLI_CASES')
        if selected is not None:
            selected = selected.split(',')
            self.assertTrue(selected and len(set(selected)) == len(selected))
            self.assertTrue(set(selected) <= set(cases))
            cases = selected
        with tempfile.TemporaryDirectory(prefix='gt26-rejections-') as tmp:
            parent = Path(tmp)/'standalone'
            packet = parent/r.ROOT.name
            for dep in r.PARENT_SHA256:
                dest = parent/dep
                dest.parent.mkdir(parents=True,exist_ok=True)
                shutil.copyfile(r.ROOT.parent/dep,dest)
            for case in cases:
                with self.subTest(case=case):
                    if packet.exists():
                        shutil.rmtree(packet)
                    shutil.copytree(r.ROOT,packet,ignore=shutil.ignore_patterns('__pycache__'))
                    obj = copy.deepcopy(r.load_json(packet/'verification.json'))
                    if case == 'rh_flag':
                        obj['rh_proved'] = True
                    elif case == 'scope_empty':
                        obj['scope'] = {}
                    elif case == 'scope_bool':
                        obj['scope']['cutoff_limit'] = True
                    elif case == 'changed_coefficient':
                        obj['sample_cutoffs'][-1]['normalized_coefficients'][0][1] += 1
                    elif case == 'extra_key':
                        obj['unreviewed_gain'] = 'proved'
                    elif case == 'missing_prime_power':
                        obj['sample_operator_inverse_at_9'] = []
                    if case in {'rh_flag','scope_empty','scope_bool','changed_coefficient','extra_key','missing_prime_power'}:
                        (packet/'verification.json').write_text(r.canonical(obj),encoding='utf-8')
                        seal(packet)  # Exercise semantic reconstruction, not merely a hash mismatch.
                    elif case == 'duplicate_json':
                        text = (packet/'verification.json').read_text()
                        (packet/'verification.json').write_text(text.replace('{','{"rh_proved": false,',1))
                        seal(packet)
                    elif case == 'float_alias':
                        text = (packet/'verification.json').read_text()
                        (packet/'verification.json').write_text(text.replace('"cutoff_limit": 32','"cutoff_limit": 32.0'))
                        seal(packet)
                    elif case == 'bad_parent':
                        obj2 = r.load_json(packet/'SOURCE_LOCK.json')
                        obj2['parent_commit'] = '0'*40
                        (packet/'SOURCE_LOCK.json').write_text(r.canonical(obj2))
                        seal(packet)
                    elif case == 'proof_byte':
                        with (packet/'PROOF.md').open('a') as fh:
                            fh.write('\nchanged\n')
                    elif case == 'manifest_empty':
                        (packet/'SHA256SUMS').write_text('')
                    elif case == 'unexpected_file':
                        (packet/'unbound.json').write_text('{}')
                    elif case == 'parent_proof_byte':
                        dep = parent/next(iter(r.PARENT_SHA256))
                        with dep.open('a') as fh:
                            fh.write('\nchanged parent\n')
                    print('GT26_CLI_CASE='+case, file=sys.stderr, flush=True)
                    done = command(packet)
                    self.assertEqual(done.returncode,2,done.stdout+done.stderr)
                    self.assertIn('REJECT_GT26:',done.stderr)
                    self.assertNotIn('PASS_GT26',done.stdout)
        print('GT26_CLI_REJECTIONS='+str(len(cases)),flush=True)


if __name__ == '__main__':
    unittest.main(verbosity=2)
