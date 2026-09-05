#!/usr/bin/env python3
"""Reject corrupted finite receipts; no mathematical theorem is certified here."""
from __future__ import annotations
import copy
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

HERE=Path(__file__).resolve().parent

class RefusalTests(unittest.TestCase):
    def run_case(self, kind: str, error: str) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)
            for name in ['verify.py','PROOF.md','SOURCE_LOCK.json','result.json']:
                shutil.copyfile(HERE/name,p/name)
            result=json.loads((p/'result.json').read_text())
            if kind=='wrong_dimension':
                result['unit_window']['nonpositive_dimension_upper_bound']=0
            elif kind=='float_alias':
                result['check_count']=float(result['check_count'])
            elif kind=='bool_alias':
                result['rh_proved']=0
            elif kind=='wrong_source_value':
                result['actual_Q3_interval']['upper']+=1
            elif kind=='changed_proof':
                with (p/'PROOF.md').open('a') as f:f.write('\nchanged bytes\n')
            elif kind=='changed_lock':
                lock=json.loads((p/'SOURCE_LOCK.json').read_text())
                lock['publication_base']='0'*40
                (p/'SOURCE_LOCK.json').write_text(json.dumps(lock))
            elif kind=='duplicate_key':
                (p/'result.json').write_text('{"rh_proved":false,"rh_proved":false}')
            else:
                raise ValueError('unknown test case')
            if kind!='duplicate_key':(p/'result.json').write_text(json.dumps(result))
            flags=['-O'] if sys.flags.optimize else []
            run=subprocess.run([sys.executable,*flags,str(p/'verify.py'),'--check',str(p/'result.json')],
                               capture_output=True,text=True,timeout=30)
            self.assertEqual(run.returncode,2,run.stderr)
            self.assertIn(error,run.stderr)
    def test_wrong_dimension(self):self.run_case('wrong_dimension','saved result mismatch')
    def test_float_alias(self):self.run_case('float_alias','saved result mismatch')
    def test_bool_alias(self):self.run_case('bool_alias','saved result mismatch')
    def test_wrong_source_value(self):self.run_case('wrong_source_value','saved result mismatch')
    def test_changed_proof(self):self.run_case('changed_proof','saved result mismatch')
    def test_changed_lock(self):self.run_case('changed_lock','source lock mismatch')
    def test_duplicate_key(self):self.run_case('duplicate_key','duplicate JSON key')

if __name__=='__main__':unittest.main(verbosity=2)
