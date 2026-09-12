#!/usr/bin/env python3
"""Bounded exact tests and actual CLI refusals. No analytic proof certification."""
from __future__ import annotations
import argparse,copy,hashlib,importlib.util,json,subprocess,sys,tempfile,unittest
from pathlib import Path
from fractions import Fraction as F

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('bls_check',ROOT/'check.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
OPT=False

class Tests(unittest.TestCase):
    def test_complete_reconstruction(self):
        mod.authenticate()
        self.assertEqual(mod.canonical(mod.build()),mod.canonical(mod.strict_load(ROOT/'result.json')))

    def test_signed_coefficients(self):
        for th in (F(0),F(1,3),F(1)):
            _,s=mod.normalized_moments(th,6)
            self.assertEqual(mod.moment_b(s)[3],-35*th/(50-th))
        self.assertEqual(mod.w_entry(3,0),F(-7,32))

    def test_tail_telescoping(self):
        # Compare a finite exact tail with the rigorous infinite majorant;
        # this corroborates, but does not replace, its written infinite proof.
        for a,im,J in [(F(1,4),F(1),4),(F(0),F(2),8),(F(1,2),F(3),16)]:
            t=F(1)
            for j in range(J):t*=((j-a)**2+im**2)/F((j+1)*(j+5))
            cap=t*(J+4)/(4+2*a);total=t
            for j in range(J,J+50):
                t*=((j-a)**2+im**2)/F((j+1)*(j+5));total+=t
            self.assertLessEqual(total,cap)

    def test_actual_cli_refusals(self):
        global OPT
        result=mod.build();refused=0
        with tempfile.TemporaryDirectory(prefix='bls26-tests-') as tmp:
            out=Path(tmp)
            command=[sys.executable,'-I','-S','-B']+(['-O'] if OPT else [])+[str(ROOT/'check.py'),'--check']
            def run(p):return subprocess.run(command+[str(p)],capture_output=True,text=True,timeout=60)
            good=out/'good.json';good.write_text(json.dumps(result),encoding='utf8')
            accepted=run(good)
            self.assertEqual(accepted.returncode,0,accepted.stderr)
            mutations=[]
            for label,fn in [
                ('rh',lambda d:d['status'].__setitem__('rh_proved',True)),
                ('collision',lambda d:d['status'].__setitem__('native_collision_sign_proved',True)),
                ('zero',lambda d:d['status'].__setitem__('new_native_zero_certificate',True)),
                ('bool_alias',lambda d:d['status'].__setitem__('rh_proved',0)),
                ('float_alias',lambda d:d['constants']['square_norm_upper'].__setitem__(0,2052000.0)),
                ('pole_factor',lambda d:d['constants']['pole_coefficient_over_pi5'].__setitem__(0,1025)),
                ('wrong_b3',lambda d:d['source_rows'][-1]['b_through_18'][3].__setitem__(0,1)),
                ('omitted_tail',lambda d:d['coverage'].__setitem__('tail_ratio_panels',0)),
                ('forcing_sign',lambda d:d.__setitem__('w30',[7,32])),
            ]:
                bad=copy.deepcopy(result);fn(bad)
                path=out/(label+'.json');path.write_text(json.dumps(bad),encoding='utf8')
                mutations.append((label,path))
            dup=out/'duplicate.json';dup.write_text('{"packet":"BLS26","packet":"BLS26"}',encoding='utf8')
            mutations.append(('duplicate_key',dup))
            for label,path in mutations:
                with self.subTest(label=label):
                    r=run(path);self.assertNotEqual(r.returncode,0,r.stdout)
                    self.assertIn('REJECT:',r.stderr);refused+=1
            self.assertEqual(refused,10)
        print('EXECUTED: one pristine CLI acceptance and ten actual CLI refusals')


def main():
    global OPT
    ap=argparse.ArgumentParser();ap.add_argument('--optimized',action='store_true')
    args=ap.parse_args();OPT=args.optimized
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    run=unittest.TextTestRunner(verbosity=2).run(suite)
    raise SystemExit(0 if run.wasSuccessful() else 1)

if __name__=='__main__':main()
