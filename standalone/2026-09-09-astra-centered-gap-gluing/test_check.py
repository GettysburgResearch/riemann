#!/usr/bin/env python3
"""Real CLI adversarial checks. No result is inferred from a skipped command."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parent
MODE=['-O'] if sys.flags.optimize else []


def reseal(p):
    names=sorted(x.name for x in p.iterdir() if x.name!='SHA256SUMS')
    (p/'SHA256SUMS').write_text(''.join(hashlib.sha256((p/n).read_bytes()).hexdigest()+'  '+n+'\n' for n in names))


class Rejections(unittest.TestCase):
    def invoke(self,p):
        return subprocess.run([sys.executable,'-I','-S','-B']+MODE+[str(p/'check.py'),'--check',str(p/'verification.json')],
                              capture_output=True,text=True,timeout=35)
    def case(self,mutate,label):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'packet';shutil.copytree(ROOT,p)
            mutate(p)
            proc=self.invoke(p)
            self.assertNotEqual(proc.returncode,0,label)
            self.assertIn('REJECT_CGG26',proc.stderr,label+': '+proc.stderr)
    def test_pristine(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'packet';shutil.copytree(ROOT,p)
            proc=self.invoke(p)
            self.assertEqual(proc.returncode,0,proc.stderr)
            self.assertTrue(proc.stdout.startswith('PASS_CGG26_BOUNDED '))
    def test_results(self):
        def edit(fn):
            def apply(p):
                v=json.loads((p/'verification.json').read_text());fn(v)
                (p/'verification.json').write_text(json.dumps(v,sort_keys=True,indent=2)+'\n');reseal(p)
            return apply
        edits=[
          ('false_rh',lambda v:v.update(rh_proved=True)),
          ('boolean_alias',lambda v:v['actual_log_prime_rayleigh_certificates'][0].update(enumerated_A_nonconstant_modes=True)),
          ('wrong_root_mass',lambda v:v['actual_log_prime_rayleigh_certificates'][0].update(Z_A=[5,2])),
          ('lost_prime',lambda v:v['actual_log_prime_rayleigh_certificates'][-1].update(B_prime_count=1697)),
          ('wrong_interval',lambda v:v['actual_log_prime_rayleigh_certificates'][0]['rayleigh_lower_witness'].update(lo_hex='1')),
          ('false_enumeration',lambda v:v['actual_log_prime_rayleigh_certificates'][-1].update(enumerated_B_vertices=True)),
        ]
        for label,fn in edits:
            with self.subTest(label=label):self.case(edit(fn),label)
        def duplicate(p):
            s=(p/'verification.json').read_text();s=s.replace('"rh_proved": false','"rh_proved": true, "rh_proved": false')
            (p/'verification.json').write_text(s);reseal(p)
        self.case(duplicate,'duplicate_key')
        def floats(p):
            s=(p/'verification.json').read_text();s=s.replace('"prime_count": 1900','"prime_count": 1900.0')
            self.assertIn('1900.0',s);(p/'verification.json').write_text(s);reseal(p)
        self.case(floats,'float_alias')
    def test_packages(self):
        self.case(lambda p:(p/'README.md').unlink(),'missing_file')
        self.case(lambda p:(p/'extra').write_text('x'),'extra_file')
        self.case(lambda p:(p/'SHA256SUMS').write_text(''),'empty_manifest')
        def drift(p):
            v=json.loads((p/'SOURCE_LOCK.json').read_text());v['sources'][0]['commit']='0'*40
            (p/'SOURCE_LOCK.json').write_text(json.dumps(v));reseal(p)
        self.case(drift,'resealed_source_drift')
        def link(p):
            x=p.parent/'outside';x.write_bytes((p/'README.md').read_bytes());(p/'README.md').unlink();(p/'README.md').symlink_to(x)
        self.case(link,'symlink')
    def test_producer_mutations(self):
        changes=[('double_root','z=za+zb-1','z=za+zb'),
                 ('missing_p2_edge','for n in ss if n%p]','for n in ss if n%p and p!=2]')]
        for label,old,new in changes:
            def change(p,old=old,new=new):
                s=(p/'check.py').read_text();self.assertIn(old,s);s=s.replace(old,new,1)
                (p/'check.py').write_text(s);reseal(p)
            with self.subTest(label=label):self.case(change,label)


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--part',choices=['all','pristine','results','packages','producer_mutations'],default='all')
    ns=ap.parse_args()
    names=['test_'+ns.part] if ns.part!='all' else ['test_pristine','test_results','test_packages','test_producer_mutations']
    result=unittest.TextTestRunner(verbosity=2).run(unittest.TestSuite(Rejections(n) for n in names))
    raise SystemExit(0 if result.wasSuccessful() else 1)
