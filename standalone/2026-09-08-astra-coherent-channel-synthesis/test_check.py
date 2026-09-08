#!/usr/bin/env python3
"""Exercise the real command line on pristine and deliberately corrupted copies."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parent


def reseal(root):
    paths=sorted(p for p in root.iterdir() if p.name!='SHA256SUMS')
    (root/'SHA256SUMS').write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name+'\n'
                                       for p in paths if p.is_file()))


class AdversarialReplay(unittest.TestCase):
    def run_copy(self,mutator=None,seal=False,accept=False):
        with tempfile.TemporaryDirectory() as tmp:
            dest=Path(tmp)/'packet';shutil.copytree(ROOT,dest)
            if mutator is not None:mutator(dest)
            if seal:reseal(dest)
            cmd=[sys.executable,'-I','-S','-B']+(['-O'] if sys.flags.optimize else [])+[str(dest/'check.py')]
            run=subprocess.run(cmd,capture_output=True,text=True,timeout=15)
            self.assertEqual(run.returncode==0,accept,run.stdout+run.stderr)
            if accept:self.assertIn('PASS_CCS26_BOUNDED_REPLAY',run.stdout)
            else:self.assertIn('REJECT:',run.stderr)

    def test_pristine(self):self.run_copy(accept=True)

    def test_resealed_results(self):
        def change(path,operation):
            file=path/'verification.json';x=json.loads(file.read_text());operation(x)
            file.write_text(json.dumps(x))
        operations=[
            lambda x:x.__setitem__('rh_proved',True),
            lambda x:x.__setitem__('primitive_range',True),
            lambda x:x['native_coherent_panels'][1].__setitem__('J',[1,3]),
            lambda x:x['native_coherent_panels'][1].__setitem__('future_tail',[1,1]),
            lambda x:x['literal_root_certificates'][0].__setitem__('optimal_anchored_constant',[[1,1],[1,1]]),
            lambda x:x['native_coherent_panels'].pop(),
        ]
        for operation in operations:
            self.run_copy(lambda p,operation=operation:change(p,operation),seal=True)
        self.run_copy(lambda p:(p/'verification.json').write_text('{"rh_proved":false,"rh_proved":false}'),seal=True)
        self.run_copy(lambda p:(p/'verification.json').write_text((p/'verification.json').read_text().replace('"primitive_range": 256','"primitive_range": 256.0')),seal=True)

    def test_package_and_lock(self):
        self.run_copy(lambda p:(p/'PROOF.md').write_text('changed proof'))
        self.run_copy(lambda p:(p/'extra.txt').write_text('extra'))
        self.run_copy(lambda p:(p/'SHA256SUMS').write_text(''))
        self.run_copy(lambda p:(p/'SOURCE_LOCK.json').write_text((p/'SOURCE_LOCK.json').read_text().replace('e4a486d3fd4009e3722e9e93f35710b834fbd195','0'*40)),seal=True)
        def symlink(p):
            target=p.parent/'target.md';shutil.copy2(p/'PROOF.md',target)
            (p/'PROOF.md').unlink();(p/'PROOF.md').symlink_to(target)
        self.run_copy(symlink)

    def test_resealed_producers(self):
        self.run_copy(lambda p:(p/'check.py').write_text((p/'check.py').read_text().replace('rate=weights[i]/p;','rate=weights[i];')),seal=True)
        self.run_copy(lambda p:(p/'check.py').write_text((p/'check.py').read_text().replace('q*=p\n            direct[p]', 'q=N+1\n            direct[p]')),seal=True)


if __name__=='__main__':unittest.main(verbosity=2)
