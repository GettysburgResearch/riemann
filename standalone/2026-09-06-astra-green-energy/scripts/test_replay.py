#!/usr/bin/env python3
"""Bounded unit and actual-CLI rejection tests. No broad computation."""
import copy, hashlib, importlib.util, json, os, shutil, subprocess, sys, tempfile, unittest
from fractions import Fraction as F
from pathlib import Path

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('green_replay_tests',HERE/'replay.py')
r=importlib.util.module_from_spec(spec);sys.modules[spec.name]=r
exec(compile((HERE/'replay.py').read_bytes(),str(HERE/'replay.py'),'exec'),r.__dict__)
m=r.load_math()

class Tests(unittest.TestCase):
    def test_manifest(self):r.manifest();r.authentic_parent()
    def test_numeric_types(self):
        for bad in (True,False,1.0,'1'):
            with self.assertRaises((TypeError,ValueError)):m.balanced(bad)
            with self.assertRaises((TypeError,ValueError)):m.I.of(bad)
        for bad in (0,2,257):
            with self.assertRaises(ValueError):m.balanced(bad)
    def test_interval_guards(self):
        with self.assertRaises(ValueError):m.I(1,0)
        with self.assertRaises(TypeError):m.I(True,1)
        with self.assertRaises(ZeroDivisionError):m.I.of(1)/m.I.bounds(-1,1)
        self.assertTrue((m.I.bounds(-2,3).square()).contains(0))
        self.assertTrue((m.I.bounds(-2,3).square()).contains(9))
    def test_balancing_is_required(self):
        for bad in ({},{1:F(1)},{1:F(1),2:F(-2)},{1:True,3:F(-3)}):
            with self.assertRaises((TypeError,ValueError)):m.frequencies(bad)
    def test_primitive_cases(self):
        lam,*_=m.balanced(4)
        self.assertEqual(lam,{1:F(1),3:F(-3)})
        self.assertEqual([m.source(lam,2*j) for j in range(1,7)],[1,-1,0,1,-1,0])
        self.assertEqual(m.balanced(16)[0][9],F(-20880,57769))
    def test_trigonometry(self):
        for q,s,c in ((F(0),0,1),(F(1,2),1,0),(F(1),0,-1),(F(3,2),-1,0),(F(2),0,1)):
            sn,cs=m.trig(q);self.assertTrue(sn.contains(s));self.assertTrue(cs.contains(c))
        sn,cs=m.trig(F(1,3));self.assertTrue(cs.contains(F(1,2)))
        self.assertTrue(sn.square().contains(F(3,4)))
    def test_exact_energy(self):
        lam,*_=m.balanced(4);E,rows,tails,pieces=m.energy(lam)
        self.assertEqual(len(rows),1)
        self.assertTrue((2*E/m.pi()).square().contains(F(1,3)))
        self.assertTrue(m.partial_energy(rows,tails,F(10)).overlaps(E))
        with self.assertRaises(ValueError):m.partial_energy(rows,tails,F(-1))
    def test_strict_json(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'x'
            for text in ('{"a":1,"a":2}','{"a":1.0}','{"a":NaN}'):
                p.write_text(text)
                with self.assertRaises(r.Refusal):r.strict_json(p)
    def test_cli_mutations(self):
        cases=('rh_flag','float_alias','duplicate_json','missing_mesh_row','delete_nonsquarefree',
               'energy_endpoint','empty_manifest','unknown_file','symbolic_file','parent_bytes',
               'lock_head','flip_global_orientation')
        for case in cases:
            with self.subTest(case=case), tempfile.TemporaryDirectory() as td:
                base=Path(td);root=base/r.ROOT.name
                shutil.copytree(r.ROOT,root,ignore=shutil.ignore_patterns('__pycache__'))
                par=base/r.PARENT.name;par.mkdir()
                for n in r.PINS:shutil.copyfile(r.PARENT/n,par/n)
                data=json.loads((root/'verification.json').read_text())
                if case=='rh_flag':data['rh_proved']=True
                elif case=='float_alias':data['config']['bits']=224.0
                elif case=='missing_mesh_row':data['sources'][-1]['mesh'].pop()
                elif case=='delete_nonsquarefree':del data['sources'][2]['weights']['9']
                elif case=='energy_endpoint':data['sources'][0]['full_energy']['lo']='0'
                if case in ('rh_flag','float_alias','missing_mesh_row','delete_nonsquarefree','energy_endpoint'):
                    (root/'verification.json').write_text(json.dumps(data,sort_keys=True,indent=2)+'\n')
                elif case=='duplicate_json':
                    p=root/'verification.json';p.write_text(p.read_text().replace('{','{"rh_proved": false,',1))
                elif case=='unknown_file':(root/'unlisted.txt').write_text('not in inventory\n')
                elif case=='symbolic_file':os.symlink('PROOF.md',root/'unexpected_link')
                elif case=='parent_bytes':
                    p=par/'PROOF.md';p.write_bytes(p.read_bytes()+b'\nchanged\n')
                elif case=='lock_head':
                    p=root/'SOURCE_LOCK.json';x=json.loads(p.read_text());x['head']='0'*40;p.write_text(json.dumps(x))
                elif case=='flip_global_orientation':
                    p=root/'scripts/mathcore.py';text=p.read_text()
                    old="'charge':(-1)**(r+1)*l*cs/sn"
                    self.assertEqual(text.count(old),1)
                    p.write_text(text.replace(old,"'charge':(-1)**r*l*cs/sn"))
                # Reseal semantic/source mutations: exercise reconstruction, not only digest failure.
                manifest=''.join(hashlib.sha256((root/n).read_bytes()).hexdigest()+'  '+n+'\n' for n in sorted(r.FILES))
                (root/'SHA256SUMS').write_text('' if case=='empty_manifest' else manifest)
                cmd=[sys.executable]+(['-O'] if sys.flags.optimize else [])+[str(root/'scripts/replay.py'),'--check']
                run=subprocess.run(cmd,capture_output=True,text=True,timeout=35,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})
                self.assertNotEqual(run.returncode,0,(case,run.stdout,run.stderr))
                self.assertIn('REFUSED:',run.stderr)
        print('CLI_CORRUPTIONS_REJECTED=12 mode='+('optimized' if sys.flags.optimize else 'normal'))

if __name__=='__main__':unittest.main(verbosity=2)
