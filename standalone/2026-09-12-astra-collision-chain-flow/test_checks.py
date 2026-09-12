#!/usr/bin/env python3
"""Finite mathematical controls plus actual CLI acceptances/refusals."""
import sys
sys.dont_write_bytecode=True
import hashlib,json,shutil,subprocess,tempfile,unittest
from pathlib import Path
from fractions import Fraction as Q
import check,native_theta,research_algebra,calibrated_chain,gamma_score
from exact_interval import I,SCALE,exp,pi,log_q

ROOT=Path(__file__).resolve().parent
COUNTS={'cli_acceptances':0,'cli_refusals':0,'complete_native_meshes':0}

def seal(root):
    lines=[]
    for p in sorted(root.iterdir()):
        if p.name!='SHA256SUMS':lines.append(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name)
    (root/'SHA256SUMS').write_text('\n'.join(lines)+'\n',encoding='utf-8')

def cli(root,receipt):
    cmd=[sys.executable,'-B']
    if sys.flags.optimize:cmd+=['-O']
    cmd +=[str(root/'check.py'),'--check',str(receipt)]
    return subprocess.run(cmd,capture_output=True,text=True,timeout=180)

class Checks(unittest.TestCase):
    def test_01_elementary_enclosures(self):
        for a in range(-4,5):
            for b in range(-4,5):
                x=Q(a,7);y=Q(b,11)
                for out,truth in ((I.q(x)+I.q(y),x+y),(I.q(x)*I.q(y),x*y)):
                    self.assertLessEqual(Q(out.lo,SCALE),truth);self.assertGreaterEqual(Q(out.hi,SCALE),truth)
        for x in (Q(1,9),Q(2),Q(7,3),Q(10)):
            out=exp(log_q(x));self.assertLessEqual(Q(out.lo,SCALE),x);self.assertGreaterEqual(Q(out.hi,SCALE),x)
        self.assertTrue(pi().inside('3.1415926535897932384626','3.1415926535897932384627'))
        self.assertGreater(exp(Q(3,4)).lo,I.q(2).hi)
        self.assertGreater(exp(6).lo,I.q(400).hi)
        for bad in (True,0.5):
            with self.assertRaises(TypeError):I.q(bad)

    def test_02_exact_markov_and_gamma_algebra(self):
        c=research_algebra.chain_controls();g=research_algebra.gamma_controls()
        self.assertEqual(c['exact_chain_instances'],21)
        self.assertEqual(c['sixth_joint_cumulant_partition_cases'],96)
        self.assertEqual(g['positive_density_jet_checks'],570)
        self.assertEqual(g['score_product_checks'],540)
        self.assertFalse(g['defect_extinction_proved'])

    def test_03_complete_two_mesh_source_and_chain_roots(self):
        a=native_theta.report(128);b=native_theta.report(160);COUNTS['complete_native_meshes']+=2
        for x,y in zip(a['normalized_even_moments'],b['normalized_even_moments']):
            self.assertLessEqual(max(Q(x[0]),Q(y[0])),min(Q(x[1]),Q(y[1])))
        for data in (a,b):
            r=calibrated_chain.seed_certificate(data)
            self.assertEqual(r['even_moments_matched_in_complete_limit'],6)
            self.assertLess(Q(r['contraction_upper']),Q(1,10**6))
            self.assertLess(Q(r['standardized_eighth_moment_mismatch'][1]),0)

    def test_04_positive_score_and_input_boundaries(self):
        self.assertEqual(gamma_score.report()['complete_positive_score_panels'],18)
        for args in ((1,Q(1),Q(1)),(2,Q(-1),Q(1)),(2,Q(3),Q(1)),(2,Q(1),Q(0)),(2,Q(1),Q(100))):
            with self.assertRaises(ValueError):gamma_score.score(*args)
        with self.assertRaises(TypeError):gamma_score.score(2,0.5,Q(1))

    def test_05a_cli_acceptance_status_and_json_refusals(self):
        pristine=cli(ROOT,ROOT/'results.json')
        self.assertEqual(pristine.returncode,0,pristine.stderr);COUNTS['cli_acceptances']+=1
        base=check.strict_json(ROOT/'results.json')
        with tempfile.TemporaryDirectory() as td:
            receipt=Path(td)/'receipt.json'
            base['rh_proved']=True;receipt.write_bytes(check.canonical(base))
            bad=cli(ROOT,receipt);self.assertNotEqual(bad.returncode,0);COUNTS['cli_refusals']+=1
            for text in ('{"a":1,"a":2}','{"numeric_alias":0.0}'):
                receipt.write_text(text,encoding='utf-8');bad=cli(ROOT,receipt)
                self.assertNotEqual(bad.returncode,0);COUNTS['cli_refusals']+=1

    def test_05b_cli_mathematical_receipt_refusals(self):
        base=check.strict_json(ROOT/'results.json')
        with tempfile.TemporaryDirectory() as td:
            receipt=Path(td)/'receipt.json'
            mutations=[lambda d:d.__setitem__('rh_proved',0),
                       lambda d:d['ising'].__setitem__('even_moments_matched_in_complete_limit',8),
                       lambda d:d['ising'].__setitem__('beta_upper','0')]
            for mutation in mutations:
                data=json.loads(json.dumps(base));mutation(data);receipt.write_bytes(check.canonical(data))
                bad=cli(ROOT,receipt);self.assertNotEqual(bad.returncode,0);COUNTS['cli_refusals']+=1

    def test_06_actual_source_mutation_and_inventory_refusals(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)/'packet';shutil.copytree(ROOT,root)
            source=root/'native_theta.py';before=source.read_text(encoding='utf-8')
            changed=before.replace('(4*(p**2)*nn**2*e9','(5*(p**2)*nn**2*e9')
            self.assertNotEqual(before,changed)
            source.write_text(changed,encoding='utf-8');seal(root)
            bad=cli(root,root/'results.json');self.assertNotEqual(bad.returncode,0)
            self.assertIn('variance boundary failed',bad.stderr);COUNTS['cli_refusals']+=1
            shutil.rmtree(root);shutil.copytree(ROOT,root)
            with (root/'GAMMA.md').open('a',encoding='utf-8') as f:f.write('\nUNSEALED_CHANGE\n')
            bad=cli(root,root/'results.json');self.assertNotEqual(bad.returncode,0)
            self.assertIn('hash mismatch',bad.stderr);COUNTS['cli_refusals']+=1
            shutil.rmtree(root);shutil.copytree(ROOT,root);(root/'UNEXPECTED.txt').write_text('extra',encoding='utf-8')
            bad=cli(root,root/'results.json');self.assertNotEqual(bad.returncode,0)
            self.assertIn('inventory mismatch',bad.stderr);COUNTS['cli_refusals']+=1

if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--partition',choices=('all','unit','source','cli-a','cli-b','integrity'),default='all')
    args=parser.parse_args()
    names={
      'unit':['test_01_elementary_enclosures','test_02_exact_markov_and_gamma_algebra','test_04_positive_score_and_input_boundaries'],
      'source':['test_03_complete_two_mesh_source_and_chain_roots'],
      'cli-a':['test_05a_cli_acceptance_status_and_json_refusals'],
      'cli-b':['test_05b_cli_mathematical_receipt_refusals'],
      'integrity':['test_06_actual_source_mutation_and_inventory_refusals']}
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(Checks) if args.partition=='all' else unittest.TestSuite(Checks(n) for n in names[args.partition])
    run=unittest.TextTestRunner(verbosity=2).run(suite)
    print(json.dumps({'successful':run.wasSuccessful(),'partition':args.partition,'tests':run.testsRun,'failures':len(run.failures),
                      'errors':len(run.errors),'skips':len(run.skipped),'optimize':sys.flags.optimize,**COUNTS},sort_keys=True))
    raise SystemExit(0 if run.wasSuccessful() else 1)
