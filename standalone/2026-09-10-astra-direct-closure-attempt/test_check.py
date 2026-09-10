#!/usr/bin/env python3
"""Small adversarial implementation tests, not a theorem verifier."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent


def cli(root, *args):
    flags = ['-I', '-S', '-B']
    if sys.flags.optimize:
        flags.append('-O')
    return subprocess.run([sys.executable, *flags, str(root/'check.py'), *map(str,args)],
                          text=True, capture_output=True, timeout=20)


def seal(root):
    names = sorted(p.name for p in root.iterdir() if p.name != 'SHA256SUMS')
    (root/'SHA256SUMS').write_text(''.join(
        hashlib.sha256((root/name).read_bytes()).hexdigest()+'  '+name+'\n'
        for name in names), encoding='ascii')


class Controls(unittest.TestCase):
    def test_pristine(self):
        r=cli(ROOT)
        self.assertEqual(r.returncode,0,r.stderr)
        v=json.loads(r.stdout)
        self.assertIs(v['rh_proved'],False)
        self.assertIs(v['actual_xi_evaluated'],False)

    def test_receipts(self):
        good=json.loads(cli(ROOT).stdout)
        changed=[]
        a=dict(good); a['rh_proved']=True; changed.append(json.dumps(a))
        a=dict(good); a['rh_proved']=0; changed.append(json.dumps(a))
        a=json.loads(json.dumps(good)); a['groups']['inverse_power_models']=16.0
        changed.append(json.dumps(a))
        changed.append('{"rh_proved":false,"rh_proved":false}')
        changed.append('{}')
        with tempfile.TemporaryDirectory() as temp:
            p=Path(temp)/'receipt.json'
            p.write_text(json.dumps(good),encoding='utf8')
            self.assertEqual(cli(ROOT,'--expect',p).returncode,0)
            for text in changed:
                p.write_text(text,encoding='utf8')
                self.assertNotEqual(cli(ROOT,'--expect',p).returncode,0,text)

    def test_payload(self):
        for case in ('proof','extra','manifest','source','producer'):
            with self.subTest(case=case), tempfile.TemporaryDirectory() as temp:
                r=Path(temp)/'packet'; shutil.copytree(ROOT,r)
                if case=='proof':
                    with (r/'ATTEMPT.md').open('a') as f: f.write('\nALTERED\n')
                elif case=='extra':
                    (r/'EXTRA').write_text('x')
                elif case=='manifest':
                    (r/'SHA256SUMS').write_text('')
                elif case=='source':
                    v=json.loads((r/'SOURCES.json').read_text())
                    v['parent']['commit']='0'*40
                    (r/'SOURCES.json').write_text(json.dumps(v))
                    seal(r)
                elif case=='producer':
                    p=r/'check.py'; old=p.read_text()
                    needle='+ 4 * a.im * (qp * q.conj()).im)'
                    self.assertEqual(old.count(needle),1)
                    p.write_text(old.replace(needle,'+ 3 * a.im * (qp * q.conj()).im)'))
                    seal(r)
                self.assertNotEqual(cli(r).returncode,0,case)


if __name__=='__main__':
    unittest.main(verbosity=2)
