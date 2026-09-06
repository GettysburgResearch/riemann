"""Bounded rejection tests. Run with python -B scripts/test_replay.py."""
from __future__ import annotations
import hashlib, json, shutil, subprocess, sys, tempfile, unittest
from fractions import Fraction as F
from pathlib import Path
import replay as r

class Tests(unittest.TestCase):
    def test_exact_types(self):
        for q in [True,False,1.0,'1',None]:
            with self.assertRaises((TypeError,ValueError)):r.exact(q)
        for q in [True,0,514,3.0]:
            with self.assertRaises((TypeError,ValueError)):r.integer(q)
    def test_source_requires_odd(self):
        with self.assertRaises(r.Refusal):r.terminal(4,r.mobius_table(8))
    def test_small_terminal(self):
        mu=r.mobius_table(9)
        self.assertEqual(r.terminal(3,mu),{1:F(1),3:F(-3)})
        self.assertEqual(sum(r.terminal(9,mu).values()),F(-172,35))
    def test_harmonic_exact(self):
        (a,b,c),rows=r.harmonic_polynomial({1:F(1),3:F(-3)})
        self.assertEqual((a,b,c),(F(1),F(),F()))
        self.assertEqual(rows,[['0','1/4','0']])
    def test_frozen_parent(self):
        m=r.parent();self.assertEqual(m.BITS,224)
        with self.assertRaises(ValueError):m.validate_source({1:F(1),3:F(-1)})
    def test_manifest(self):r.manifest()
    def test_cli_refusals(self):
        cases=['rh-claim','false-as-zero','wrong-scalar','wrong-coefficient','empty-panel',
               'duplicate-json','changed-proof','extra-file','missing-file',
               'parent-code','parent-proof','symlink']
        for case in cases:
            with self.subTest(case=case),tempfile.TemporaryDirectory(prefix='terminal-reject-') as d:
                base=Path(d);new=base/r.ROOT.name;par=base/r.PARENT.name
                shutil.copytree(r.ROOT,new,ignore=shutil.ignore_patterns('__pycache__'))
                par.mkdir()
                for name in r.PINS:
                    p=par/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes((r.PARENT/name).read_bytes())
                v=new/'verification.json';obj=json.loads(v.read_text())
                if case=='rh-claim':obj['rh_proved']=True
                elif case=='false-as-zero':obj['uniform_full_gain_proved']=0
                elif case=='wrong-scalar':obj['scalar_grid'][1]['Q']='0'
                elif case=='wrong-coefficient':obj['panels'][0]['weights']['3']='-1'
                elif case=='empty-panel':obj['panels']=[]
                elif case=='duplicate-json':v.write_text('{"rh_proved":false,"rh_proved":false}\n')
                elif case=='changed-proof':
                    p=new/'PROOF.md';p.write_bytes(p.read_bytes()+b'\nchanged\n')
                elif case=='extra-file':(new/'EXTRA').write_text('unbound')
                elif case=='missing-file':(new/'SOURCES.md').unlink()
                elif case=='parent-code':
                    p=par/'scripts/mathcore.py';p.write_bytes(p.read_bytes()+b'\n# changed\n')
                elif case=='parent-proof':
                    p=par/'PROOF.md';p.write_bytes(p.read_bytes()+b'\nchanged\n')
                elif case=='symlink':
                    p=new/'SOURCES.md';target=base/'outside';p.rename(target);p.symlink_to(target)
                if case in ['rh-claim','false-as-zero','wrong-scalar','wrong-coefficient','empty-panel']:
                    v.write_bytes(r.canonical(obj))
                    # Reseal semantic mutations so they must fail beyond checksum validation.
                    out=[]
                    for line in (new/'SHA256SUMS').read_text().splitlines():
                        sha,name=line.split('  ',1)
                        if name=='verification.json':sha=hashlib.sha256(v.read_bytes()).hexdigest()
                        out.append(sha+'  '+name)
                    (new/'SHA256SUMS').write_text('\n'.join(out)+'\n')
                cmd=[sys.executable]+(['-O'] if sys.flags.optimize else [])+['-B',str(new/'scripts/replay.py'),'--check']
                run=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,timeout=30)
                self.assertNotEqual(run.returncode,0,case)
                self.assertIn('REFUSED:',run.stderr,case)
        print('CLI_REFUSALS=12',flush=True)

if __name__=='__main__':unittest.main()
