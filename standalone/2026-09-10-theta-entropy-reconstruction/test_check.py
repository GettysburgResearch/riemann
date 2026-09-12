#!/usr/bin/env python3
"""Actual pristine and corrupted command-line replays of this bounded checker."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent


def seal(path):
    names = sorted(p.name for p in path.iterdir() if p.name != 'SHA256SUMS')
    (path/'SHA256SUMS').write_text(''.join(
        hashlib.sha256((path/name).read_bytes()).hexdigest()+'  '+name+'\n'
        for name in names))


def command(path):
    args = [sys.executable, '-I', '-S', '-B']
    if sys.flags.optimize:
        args.append('-O')
    return subprocess.run(args+[str(path/'check.py'),'--check',str(path/'result.json')],
                          text=True,capture_output=True,timeout=20)


class DeliveryTests(unittest.TestCase):
    def test_pristine_and_actual_refusals(self):
        labels = ['false_rh','false_pair','boolean_alias','duplicate_json',
                  'entropy_producer','four_spin_producer','proof_unsealed',
                  'extra_file','parent_drift']
        refused = []
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            pristine = base/'pristine'
            shutil.copytree(ROOT,pristine)
            good = command(pristine)
            self.assertEqual(good.returncode,0,good.stderr)
            expected = (ROOT/'result.json').read_text()
            self.assertEqual(good.stdout,expected)
            for label in labels:
                with self.subTest(label=label):
                    p = base/label
                    shutil.copytree(ROOT,p)
                    if label in {'false_rh','false_pair','boolean_alias'}:
                        result = json.loads((p/'result.json').read_text())
                        if label=='false_rh': result['rh_proved']=True
                        if label=='false_pair': result['pair_realization_proved']=True
                        if label=='boolean_alias': result['schema']=True
                        (p/'result.json').write_text(json.dumps(result))
                        seal(p)
                    elif label=='duplicate_json':
                        text=(p/'result.json').read_text()
                        (p/'result.json').write_text(text.replace('"schema": 1','"schema": 1, "schema": 1',1))
                        seal(p)
                    elif label=='entropy_producer':
                        code=(p/'check.py').read_text()
                        old='return F(1, 2*r*(2*r-1))'
                        self.assertEqual(code.count(old),1)
                        (p/'check.py').write_text(code.replace(old,'return F(1, 2*r*(2*r+1))'))
                        seal(p)
                    elif label=='four_spin_producer':
                        code=(p/'check.py').read_text()
                        old='a[minus] += r if minus%2 else 1'
                        self.assertEqual(code.count(old),1)
                        (p/'check.py').write_text(code.replace(old,'a[minus] += r if minus%2 else 2'))
                        seal(p)
                    elif label=='proof_unsealed':
                        with (p/'PROOF.md').open('a') as f: f.write('\nChanged proof.\n')
                    elif label=='extra_file':
                        (p/'unlisted.txt').write_text('not part of packet')
                    elif label=='parent_drift':
                        data=json.loads((p/'SOURCES.json').read_text())
                        data['parent_commit']='0'*40
                        (p/'SOURCES.json').write_text(json.dumps(data))
                        seal(p)
                    bad=command(p)
                    self.assertNotEqual(bad.returncode,0,label)
                    self.assertIn('REJECT:',bad.stderr)
                    refused.append(label)
        self.assertEqual(refused,labels)
        print('PASSED_PRISTINE_AND_NINE_REFUSALS optimize='+str(bool(sys.flags.optimize)))


if __name__=='__main__':
    unittest.main(verbosity=2)
