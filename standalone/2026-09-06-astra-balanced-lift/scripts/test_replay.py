#!/usr/bin/env python3
"""Unit and isolated actual-CLI refusals; no unbounded theorem is tested."""
from __future__ import annotations
import contextlib
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from fractions import Fraction as F
import replay as r


def seal(root: Path) -> None:
    (root/'SHA256SUMS').write_text(''.join(
        hashlib.sha256((root/n).read_bytes()).hexdigest()+'  '+n+'\n'
        for n in sorted(r.FILES)), encoding='utf-8')


class AlgebraAndAcceptance(unittest.TestCase):
    def test_constraints_and_nonsquarefree(self):
        for M in [3,4,8,16]:
            a,_,_,_=r.weights(M)
            self.assertEqual(a[1],1)
            self.assertEqual(sum(v/F(k) for k,v in a.items()),0)
        self.assertEqual(r.weights(16)[0][9],F(-20880,57769))

    def test_typed_cache_refuses_aliases(self):
        # Prime the caches so bool/int or float/int aliasing cannot hide a bypass.
        r.mu(1);r.phi(1);r.jordan(1);r.weights(4);r.gram(2,2)
        for func,args in [(r.mu,(True,)),(r.mu,(1.0,)),(r.phi,(1.0,)),
                          (r.jordan,(True,)),(r.weights,(4.0,)),
                          (r.gram,(2.0,2)),(r.gram,(2,True))]:
            with self.subTest(func=func.__name__,args=args),self.assertRaises(ValueError):
                func(*args)

    def test_resource_refusals(self):
        for func,args in [(r.mu,(129,)),(r.weights,(2,)),(r.weights,(129,)),
                          (r.gram,(33,2)),(r.gram,(1,2)),(r.jordan,(0,))]:
            with self.subTest(func=func.__name__,args=args),self.assertRaises(ValueError):
                func(*args)

    def test_strict_json(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'input.json'
            for raw in ['{"a":1,"a":2}','{"a":1.0}','{"a":NaN}','{"a":Infinity}']:
                p.write_text(raw)
                with self.subTest(raw=raw),self.assertRaises((r.Refusal,ValueError)):
                    r.strict_json(p)

    def test_independent_rational_solver(self):
        self.assertEqual(r.solve_rational([[F(2),F(1)],[F(1),F(2)]],[F(1),F(0)]),
                         [F(2,3),F(-1,3)])
        with self.assertRaises(r.Refusal):
            r.solve_rational([[F(1),F(1)],[F(1),F(1)]],[F(1),F(0)])

    def test_primitive_endpoint(self):
        a={1:F(1),3:F(-3)}
        self.assertEqual([r.primitive(a,n) for n in range(7)],[0,1,1,-1,-1,0,0])
        with self.assertRaises(r.Refusal):r.need(False,'explicit refusal')

    def test_actual_manifest_and_parent_locks(self):
        r.authenticate();r.check_source_lock();r.check_manifest()

    def test_manifest_rejects_empty_duplicate_unknown_and_symlink(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)/'packet'
            shutil.copytree(r.ROOT,root,ignore=shutil.ignore_patterns('__pycache__'))
            original=(root/'SHA256SUMS').read_bytes()
            for raw in [b'',original+original.splitlines()[0]+b'\n']:
                (root/'SHA256SUMS').write_bytes(raw)
                with self.assertRaises(r.Refusal):r.check_manifest(root)
            (root/'SHA256SUMS').write_bytes(original)
            (root/'unexpected.txt').write_text('unknown')
            with self.assertRaises(r.Refusal):r.check_manifest(root)
            (root/'unexpected.txt').unlink()
            link=Path(td)/'linked';link.symlink_to(root,target_is_directory=True)
            with self.assertRaises(r.Refusal):r.check_manifest(link)

    def test_full_reconstruction_matches(self):
        obj=r.reconstruct()
        self.assertEqual(obj['control_total'],3884)
        self.assertEqual(r.canonical(obj),r.canonical(r.strict_json(r.ROOT/'verification.json')))

    def test_actual_cli_corruptions(self):
        # Each case gets a private copy. Semantic edits are resealed to test more than hashes.
        cases=['rh_flag','subpower_flag','result_norm','scope_empty','duplicate_key',
               'float_alias','source_primitive','source_head','parent_bytes',
               'proof_unsealed','empty_manifest','extra_file']
        rows=[]
        for case in cases:
            with self.subTest(case=case),tempfile.TemporaryDirectory() as td:
                base=Path(td)/'standalone';base.mkdir()
                names=['2026-09-06-astra-dilation-observability',
                       '2026-09-06-astra-block-gain',r.ROOT.name]
                for name in names:
                    shutil.copytree(r.BASE/name,base/name,
                                    ignore=shutil.ignore_patterns('__pycache__'))
                packet=base/r.ROOT.name
                data=json.loads((packet/'verification.json').read_text())
                if case=='rh_flag':data['rh_proved']=True
                elif case=='subpower_flag':data['subpower_full_energy_proved']=True
                elif case=='result_norm':data['sources'][0]['full_energy']['lo']='0'
                elif case=='scope_empty':data['config']['full_M']=[]
                if case in ['rh_flag','subpower_flag','result_norm','scope_empty']:
                    (packet/'verification.json').write_bytes(r.canonical(data));seal(packet)
                elif case=='duplicate_key':
                    raw=(packet/'verification.json').read_text()
                    (packet/'verification.json').write_text(raw.replace('{','{"rh_proved":false,',1))
                    seal(packet)
                elif case=='float_alias':
                    raw=(packet/'verification.json').read_text()
                    self.assertIn('"control_total": 3884',raw)
                    (packet/'verification.json').write_text(raw.replace('"control_total": 3884','"control_total": 3884.0'))
                    seal(packet)
                elif case in ['source_primitive','source_head']:
                    lock=json.loads((packet/'SOURCE_LOCK.json').read_text())
                    if case=='source_primitive':lock['primitive_source']='fitted_zeros'
                    else:lock['parent_head']='0'*40
                    (packet/'SOURCE_LOCK.json').write_bytes(r.canonical(lock));seal(packet)
                elif case=='parent_bytes':
                    p=base/'2026-09-06-astra-dilation-observability/scripts/intervals.py'
                    p.write_bytes(p.read_bytes()+b'\n# altered parent\n')
                elif case=='proof_unsealed':
                    p=packet/'PROOF.md';p.write_bytes(p.read_bytes()+b'\nChanged proof.\n')
                elif case=='empty_manifest':(packet/'SHA256SUMS').write_bytes(b'')
                elif case=='extra_file':(packet/'unlisted.txt').write_text('new')
                cmd=[sys.executable]
                if sys.flags.optimize:cmd.append('-O')
                cmd += [str(packet/'scripts/replay.py'),'--check']
                result=subprocess.run(cmd,cwd=packet,env={**os.environ,'PYTHONHASHSEED':'0',
                    'PYTHONDONTWRITEBYTECODE':'1'},text=True,capture_output=True,timeout=30)
                self.assertNotEqual(result.returncode,0,(case,result.stdout,result.stderr))
                self.assertNotIn('PASS_BALANCED_SOURCE_BOUNDED_REPLAY',result.stdout)
                rows.append({'case':case,'returncode':result.returncode,
                             'refused':True})
        print('ACTUAL_CLI_REFUSALS '+json.dumps(rows,sort_keys=True))

if __name__=='__main__':unittest.main(verbosity=2)
