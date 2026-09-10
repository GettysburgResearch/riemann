"""Bounded tests. Success is reported only by unittest's actual exit status."""
import copy, importlib.util, json, subprocess, sys, tempfile, unittest
from fractions import Fraction as Q
from pathlib import Path
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('bdr_check',HERE/'check.py')
c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)

class Tests(unittest.TestCase):
    def test_beta_weight_sum(self):
        for a in [Q(1),Q(5,2),Q(5),Q(10)]:
            for n in range(15):
                got=c.beta_pair([Q(1)]*(n+1),a)
                self.assertEqual(got,[Q(1)]*(n+1))
    def test_distinct_means(self):
        # The gamma factor is independent of its scale, not mean one.
        raw=c.raw_orbit(6,6)
        for n,row in enumerate(raw):
            self.assertEqual(row[1],1);self.assertEqual(row[2],Q(7,5))
            self.assertEqual(row[3],Q(93,35)-Q(24,175)*Q(31,80)**n)
    def test_central_moments(self):
        r=c.central_w(70)
        self.assertEqual(r[1],Q(-1,5));self.assertEqual(r[2],Q(11,75))
        for j,x in enumerate(r):
            self.assertGreaterEqual((-1)**j*x,0)
    def test_complete_replay(self):
        self.assertEqual(c.canonical(c.read_json(HERE/'result.json')),c.canonical(c.result()))
    def test_real_cli_refusals(self):
        obj=c.read_json(HERE/'result.json')
        changed=[]
        for field,val in [('rh_proved',True),('orbit_zero_preservation_proved',True),
                          ('source_pr',True),('source_head','0'*40)]:
            x=copy.deepcopy(obj);x[field]=val;changed.append(x)
        for field,val in [('beta_shape',2),('gamma_pair_shape',4),('depth',2),
                          ('point_imaginary',22),('degree',239)]:
            x=copy.deepcopy(obj);x['phase'][field]=val;changed.append(x)
        x=copy.deepcopy(obj);x['phase']['D']['lo_hex']='0x0';changed.append(x)
        command=[sys.executable,'-I','-S','-B']
        if sys.flags.optimize:command+=['-O']
        command+=[str(HERE/'check.py'),'--check']
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'case.json'
            p.write_text(json.dumps(obj))
            ok=subprocess.run(command+[str(p)],capture_output=True,text=True)
            self.assertEqual(ok.returncode,0,ok.stderr)
            for i,x in enumerate(changed):
                p.write_text(json.dumps(x))
                run=subprocess.run(command+[str(p)],capture_output=True,text=True)
                self.assertNotEqual(run.returncode,0,('accepted mutation',i))
            for txt in ['{"rh_proved":false,"rh_proved":false}',
                        '{"x":1.5}']:
                p.write_text(txt)
                run=subprocess.run(command+[str(p)],capture_output=True,text=True)
                self.assertNotEqual(run.returncode,0,txt)

if __name__=='__main__':unittest.main(verbosity=2)
