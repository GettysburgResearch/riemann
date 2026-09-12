"""Bounded exact tests and real CLI refusal controls; no theta integral replay."""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('sne_check', ROOT/'check.py')
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)


def command(root):
    return [sys.executable, '-I', '-S', '-B'] + (['-O'] if sys.flags.optimize else []) + [
        str(root/'check.py'), '--check', str(root/'results.json')]


def seal(root):
    rows = []
    for p in sorted(root.iterdir()):
        if p.name != 'SHA256SUMS':
            rows.append(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name)
    (root/'SHA256SUMS').write_text('\n'.join(rows)+'\n')


def mutate_json(root, fn):
    p = root/'results.json'
    d = json.loads(p.read_text())
    fn(d)
    p.write_text(json.dumps(d, sort_keys=True, indent=2)+'\n')


class Tests(unittest.TestCase):
    def test_01_domains(self):
        for bad in ([[F(0)]], [[F(-1)]], [[F(1),F(2)],[F(0),F(1)]],
                    [[F(1),F(2)],[F(2),F(1)]]):
            with self.assertRaises(ValueError):
                c.spd(bad)
        with self.assertRaises(ValueError):
            c.inv([[F(1),F(2)],[F(2),F(4)]])

    def test_02_complete_couplings(self):
        t = [[F(0),F(-1)],[F(1),F(0)]]
        data = c.blocks(t, 1)
        self.assertEqual(data, ([[F(0)]],[[F(1)]],[[F(1)]],F(0)))
        for g in (F(1,2),F(1),F(2),F(3)):
            self.assertEqual(c.energy(data,[[g]]),g+1/g)
            self.assertGreaterEqual(c.energy(data,[[g]]),2)

    def test_03_nontrivial_global_optimizer(self):
        data = ([[F(0)]],[[F(1)]],[[F(7)]],F(0))
        self.assertEqual(c.energy(data,[[F(2)]],F(1)),6)
        self.assertEqual(c.gradient(data,[[F(2)]],F(1)),[[F(0)]])
        for g in (F(1,4),F(1),F(3),F(8)):
            gg = [[g]]; lg=c.gradient(data,gg,F(1)); val=c.energy(data,gg,F(1))
            self.assertLessEqual(val-c.tr(c.prod(gg,lg,gg,lg))/4,6)
            self.assertGreaterEqual(val,6)

    def test_04_pristine_cli(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'packet';shutil.copytree(ROOT,p)
            run=subprocess.run(command(p),capture_output=True,text=True)
            self.assertEqual(run.returncode,0,run.stderr)
            self.assertTrue(run.stdout.startswith('PASS_BOUNDED_CONTROLS '))
        print('PRISTINE_CLI=1',flush=True)

    def test_05_actual_cli_refusals(self):
        cases = ['false_rh','false_native','scope_reduction','boolean_integer_alias',
                 'duplicate','float','missing_coupling','gradient_primitive','source_drift','extra_file']
        completed=0
        for case in cases:
            with self.subTest(case=case), tempfile.TemporaryDirectory() as td:
                p=Path(td)/'packet';shutil.copytree(ROOT,p)
                if case=='false_rh':
                    mutate_json(p,lambda d:d.update(rh_proved=True))
                elif case=='false_native':
                    mutate_json(p,lambda d:d.update(native_theta_energy_evaluated=True))
                elif case=='scope_reduction':
                    mutate_json(p,lambda d:d['counts'].update(geodesic_values=1))
                elif case=='boolean_integer_alias':
                    mutate_json(p,lambda d:d.update(native_theta_energy_evaluated=0))
                elif case=='duplicate':
                    q=p/'results.json';q.write_text(q.read_text().replace('{','{"rh_proved": false,',1))
                elif case=='float':
                    q=p/'results.json';q.write_text(q.read_text().replace('"dimension": 6','"dimension": 6.0'))
                elif case=='missing_coupling':
                    q=p/'check.py';q.write_text(q.read_text().replace('COUPLING_FACTOR = 1','COUPLING_FACTOR = 0'))
                elif case=='gradient_primitive':
                    q=p/'check.py'
                    old='return plus(plus(prod(a, w, tp(a)), r), plus('
                    new='return plus(plus(prod(a, w, tp(a)), zeros(len(g))), plus('
                    self.assertIn(old,q.read_text());q.write_text(q.read_text().replace(old,new))
                elif case=='source_drift':
                    q=p/'PROOF.md';q.write_text(q.read_text()+'\nUnsealed change.\n')
                elif case=='extra_file':
                    (p/'unexpected.txt').write_text('extra')
                if case not in ('source_drift','extra_file'):
                    seal(p)
                run=subprocess.run(command(p),capture_output=True,text=True)
                self.assertNotEqual(run.returncode,0,case+' was accepted')
                self.assertNotIn('PASS_BOUNDED_CONTROLS ',run.stdout)
                completed+=1
        self.assertEqual(completed,len(cases))
        print('ACTUAL_NONSYMLINK_REFUSALS='+str(completed),flush=True)

    def test_06_symlink_refusal(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'packet';shutil.copytree(ROOT,p)
            target=Path(td)/'receipt.json';shutil.copyfile(p/'results.json',target)
            (p/'results.json').unlink()
            try:
                os.symlink(target,p/'results.json')
            except (OSError,NotImplementedError) as exc:
                self.skipTest('Host cannot create symlinks; refusal unperformed: '+str(exc))
            run=subprocess.run(command(p),capture_output=True,text=True)
            self.assertNotEqual(run.returncode,0,run.stdout)
            self.assertIn('not a regular file',run.stderr)
        print('ACTUAL_SYMLINK_REFUSALS=1',flush=True)


if __name__=='__main__':
    unittest.main(verbosity=2)
