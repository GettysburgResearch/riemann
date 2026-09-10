#!/usr/bin/env python3
"""Bounded exact/model and real-CLI controls; no actual theta evaluation."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('hci',ROOT/'check.py')
hci=importlib.util.module_from_spec(spec); spec.loader.exec_module(hci)
Q=hci.Q

class Tests(unittest.TestCase):
    def test_full_reconstruction(self):
        expected=hci.load((ROOT/'results.json').read_bytes())
        self.assertTrue(hci.typed_equal(expected,hci.reconstruct()))

    def test_actual_cli(self):
        flags=['-I','-S','-B']+(['-O'] if sys.flags.optimize else [])
        base=[sys.executable,*flags,str(ROOT/'check.py'),'--check']
        r=subprocess.run(base+[str(ROOT/'results.json')],capture_output=True)
        self.assertEqual(r.returncode,0,r.stderr)
        expected=json.loads((ROOT/'results.json').read_text())
        bad=[]
        for key,val in [('rh_proved',True),('actual_theta_boundary_certified',True),
                        ('new_newman_upper_bound',True),('total_certified_segments',878)]:
            item=copy.deepcopy(expected); item[key]=val; bad.append(json.dumps(item))
        item=copy.deepcopy(expected); item['models'][0]['degree']=1; bad.append(json.dumps(item))
        item=copy.deepcopy(expected); item['models'].pop(); bad.append(json.dumps(item))
        item=copy.deepcopy(expected); item['rh_proved']=0; bad.append(json.dumps(item))
        item=copy.deepcopy(expected); item['models'][0]['degree']=-1.0; bad.append(json.dumps(item))
        bad.append('{"schema":"bad",'+json.dumps(expected)[1:])
        bad.extend(['{}','{"value":NaN}'])
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'altered.json'
            for i,text in enumerate(bad):
                p.write_text(text)
                r=subprocess.run(base+[str(p)],capture_output=True)
                self.assertNotEqual(r.returncode,0,f'accepted changed receipt {i}')
        self.assertEqual(len(bad),11)

    def test_missing_and_reordered_coverage(self):
        p=hci.heat(5); box=(-1,1,-6,6)
        cover=hci.produce_cover(p,box)
        bad=copy.deepcopy(cover); bad[0].pop()
        with self.assertRaises(ValueError): hci.verify_cover(p,box,bad)
        bad=copy.deepcopy(cover); side=max(range(4),key=lambda k:len(bad[k]))
        self.assertGreater(len(bad[side]),1)
        bad[side]=list(reversed(bad[side]))
        with self.assertRaises(ValueError): hci.verify_cover(p,box,bad)
        bad=copy.deepcopy(cover); bad[1]=[]
        with self.assertRaises(ValueError): hci.verify_cover(p,box,bad)
        bad=copy.deepcopy(cover); bad[2].insert(0,copy.deepcopy(bad[2][0]))
        with self.assertRaises(ValueError): hci.verify_cover(p,box,bad)

    def test_unpaid_error_and_false_endpoints(self):
        p=hci.heat(8); box=(-1,1,-9,9)
        cover=[[{'lo':[0,1],'hi':[1,1]}] for _ in range(4)]
        with self.assertRaises(ValueError): hci.verify_cover(p,box,cover)
        cover=hci.produce_cover(p,box)
        cover[0][0]['fake_error']=[0,1]
        with self.assertRaises(ValueError): hci.verify_cover(p,box,cover)

    def test_boundary_common_zero_refuses(self):
        with self.assertRaises(ValueError): hci.produce_cover(hci.heat(2),(0,1,0,3))

    def test_zero_time_not_positive_time(self):
        p=hci.heat(2)
        c=hci.produce_cover(p,(Q(1,16),1,-3,3))
        self.assertEqual(hci.verify_cover(p,(Q(1,16),1,-3,3),c)['degree'],0)
        self.assertEqual(p.get((0,0),0),0)

    def test_orientation_and_time_sign(self):
        ccw=[(Q(1),Q(0)),(Q(0),Q(1)),(Q(-1),Q(0)),(Q(0),Q(-1))]
        self.assertEqual(hci.poly_winding(ccw),1)
        self.assertEqual(hci.poly_winding(list(reversed(ccw))),-1)
        p={(0,2):Q(1),(1,0):Q(2)}
        self.assertFalse(hci.is_backward_heat(p))
        self.assertEqual(hci.verify_cover(p,(-1,1,-3,3),hci.produce_cover(p,(-1,1,-3,3)))['degree'],1)

    def test_amplitude_sign(self):
        p=hci.heat(6); box=(-1,1,-7,7)
        for multiplier in (Q(-7),Q(1,13)):
            scaled=hci.p_scale(p,multiplier)
            r=hci.verify_cover(scaled,box,hci.produce_cover(scaled,box))
            self.assertEqual(r['degree'],-3)

    def test_hermite_negative_time_and_derivatives(self):
        # Complete derivative identities and finite negative-time positivity controls.
        # No root isolation is performed; the all-degree proof is in PROOF.md.
        for m in range(2,21):
            self.assertTrue(hci.is_backward_heat(hci.heat(m)))
            self.assertEqual(hci.partial(hci.heat(m),1),hci.p_scale(hci.heat(m-1),Q(m)))
            if m%2==0:
                for x in map(Q,range(-8,9)):
                    self.assertGreater(sum(c*(-1)**i*x**j for (i,j),c in hci.heat(m).items()),0)

    def test_theta_source_recurrence(self):
        self.assertEqual(hci.theta_checks()['formal_jet_checks'],85)
        for u in (Q(1),Q(5,4),Q(2),Q(100)):
            self.assertEqual(16*u**3-u**2-14*u,u*(16*(u-1)**2+31*(u-1)+1))
            self.assertGreater(16*u**3-u**2-14*u,0)

    def test_symmetric_pair_and_partition(self):
        rows=hci.models()
        out=[]
        for row in rows[16:19]:
            _,p,b,w,_=row
            out.append(hci.verify_cover(p,b,hci.produce_cover(p,b))['degree'])
        self.assertEqual(out,[-2,-1,-1])
        self.assertEqual(out[0],sum(out[1:]))

    def test_strict_rationals_and_json(self):
        for x in ([True,1],[1,False],[2,2],[1,0],[1,-2],(1,2)):
            with self.assertRaises((ValueError,TypeError)):hci.decode(x)
        self.assertFalse(hci.typed_equal({'v':0},{'v':False}))
        for x in (b'{"a":1,"a":2}',b'{"a":1.0}',b'{"a":Infinity}'):
            with self.assertRaises(ValueError):hci.load(x)

    def test_inventory_and_symlink_refusals(self):
        import shutil
        with tempfile.TemporaryDirectory() as td:
            dst=Path(td)/'packet'; shutil.copytree(ROOT,dst)
            flags=['-I','-S','-B']+(['-O'] if sys.flags.optimize else [])
            command=[sys.executable,*flags,str(dst/'check.py'),'--check',str(dst/'results.json')]
            (dst/'unexpected.txt').write_text('untrusted')
            self.assertNotEqual(subprocess.run(command,capture_output=True).returncode,0)
            (dst/'unexpected.txt').unlink()
            f=dst/'results.json'; data=f.read_bytes(); f.unlink()
            target=Path(td)/'outside.json'; target.write_bytes(data); f.symlink_to(target)
            self.assertNotEqual(subprocess.run(command,capture_output=True).returncode,0)

if __name__=='__main__':
    result=unittest.TextTestRunner(verbosity=1).run(unittest.defaultTestLoader.loadTestsFromTestCase(Tests))
    print(json.dumps({'methods':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),
                      'skipped':len(result.skipped),'rh_proved':False},sort_keys=True))
    sys.exit(not result.wasSuccessful())
