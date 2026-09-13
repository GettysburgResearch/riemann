"""Independent bounded algebra and actual CLI refusal tests.

--part bounded does not replay the whole source; --part full does. Run both
parts in normal and optimized mode. Neither mode is an independent backend.
"""
from __future__ import annotations
import argparse, itertools, json, shutil, subprocess, sys, tempfile, unittest
from fractions import Fraction as Q
from math import comb, factorial
from pathlib import Path
import certify_chain as c
import check_components as b

HERE=Path(__file__).resolve().parent
OPT='-O' in sys.orig_argv

def contains(ball,value):return Q(ball.lo,c.SCALE)<=value<=Q(ball.hi,c.SCALE)

def enumeration(weights,q,param):
    n=len(weights);raw=[Q(0)]*11;dot=[Q(0)]*11
    for spins in itertools.product((-1,1),repeat=n):
        fac=[(1+q*spins[j]*spins[j+1])/2 for j in range(n-1)]
        p=Q(1,2)
        for f in fac:p*=f
        dp=Q(0)
        if param=='q':
            dp=p*sum((Q(spins[j]*spins[j+1],2)/fac[j] for j in range(n-1)),Q(0))
        x=sum((a*s for a,s in zip(weights,spins)),Q(0))
        dx=Q(0) if param=='q' else Q(spins[param])
        for k in range(11):
            raw[k]+=p*x**k
            dot[k]+=dp*x**k+(p*k*x**(k-1)*dx if k else 0)
    kap=[Q(0)]*11;dk=[Q(0)]*11
    for k in range(1,11):
        kap[k]=raw[k]-sum((comb(k-1,j-1)*kap[j]*raw[k-j] for j in range(1,k)),Q(0))
        dk[k]=dot[k]-sum((comb(k-1,j-1)*(dk[j]*raw[k-j]+kap[j]*dot[k-j]) for j in range(1,k)),Q(0))
    return kap,dk

def cli(root):
    args=[sys.executable,'-S','-B']+(['-O'] if OPT else [])
    return subprocess.run(args+[str(root/'certify_chain.py'),'--check',str(root/'chain_result.json')],
                          capture_output=True,text=True,timeout=600)

class Bounded(unittest.TestCase):
    def test_components(self):
        r=b.check();self.assertEqual(r['arithmetic']['native_prefix_checks'],3854)
        self.assertEqual(r['ferromagnetic']['bond_panels'],28)
    def test_majorant(self):self.assertEqual(c.majorant_guard(),9)
    def test_series_and_derivatives(self):
        for weights in ([Q(1,7),Q(1,11),Q(2,13)], [Q(1,9)]*3+[Q(1,12),Q(1,10)]):
            for q in (Q(0),Q(1,32),Q(1,4)):
                for param in ('q',0,len(weights)-1):
                    kap,dk=enumeration(weights,q,param);qd=c.variable(q,0,1) if param=='q' else c.D(q,(c.ZERO,))
                    s=[qd.other(0)]*5;ell=s[:]
                    for j,w in enumerate(weights):
                        a=c.variable(w,0,1) if param==j else qd.other(w)
                        s,ell=c.step(s,ell,a,qd)
                    for r in range(5):
                        k=2*r+2;sgn=(-1)**r
                        self.assertTrue(contains(ell[r].v*factorial(k),sgn*kap[k]))
                        self.assertTrue(contains(ell[r].d[0]*factorial(k),sgn*dk[k]))
                # Independent check of the reversal/join convention, all moments.
                qd=c.variable(q,0,1);zero=qd.other(0);one=qd.other(1)
                states=[]
                for ws in (weights[:2],list(reversed(weights[2:]))):
                    ss=[zero]*5;ls=ss[:]
                    for w in ws:ss,ls=c.step(ss,ls,qd.other(w),qd)
                    states.append((ss,ls))
                sl,ll=states[0];sr,lr=states[1]
                u=[zero]+[qd*sum((sl[i]*sr[r-1-i] for i in range(r)),zero) for r in range(1,6)]
                extra=c.neglog_one_minus(u,zero,one);kap,dk=enumeration(weights,q,'q')
                for r in range(5):
                    got=(ll[r]+lr[r]+extra[r])*factorial(2*r+2)
                    self.assertTrue(contains(got.v,(-1)**r*kap[2*r+2]))
                    self.assertTrue(contains(got.d[0],(-1)**r*dk[2*r+2]))
    def test_actual_fast_refusals(self):
        cases=('duplicate','type_alias','wrong_status','parent_drift')
        for case in cases:
            with tempfile.TemporaryDirectory() as tmp:
                root=Path(tmp)/'closure-bridge';root.mkdir()
                for name in c.EXPECTED_PARENT:shutil.copyfile(c.PARENT/name,root.parent/name)
                for name in ('certify_chain.py','parameters.json','chain_result.json'):shutil.copyfile(HERE/name,root/name)
                path=root/'parameters.json';data=json.loads(path.read_text())
                if case=='duplicate':path.write_text(path.read_text().replace('{','{"status":"bad",',1))
                elif case=='type_alias':data['center'][0]=True;path.write_text(json.dumps(data))
                elif case=='wrong_status':data['status']='RH proved';path.write_text(json.dumps(data))
                else:(root.parent/'native_theta.py').write_text((root.parent/'native_theta.py').read_text()+'\n# changed\n')
                result=cli(root)
                self.assertNotEqual(result.returncode,0,case)
                wanted={'duplicate':'duplicate JSON key','type_alias':'typed parameter vector',
                        'wrong_status':'parameter status','parent_drift':'parent source identity mismatch'}[case]
                self.assertIn(wanted,result.stderr,case)

class Full(unittest.TestCase):
    def test_complete_cli_acceptance(self):
        result=cli(HERE);self.assertEqual(result.returncode,0,result.stderr)
    def test_changed_receipt_after_fresh_reconstruction(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)/'closure-bridge';root.mkdir()
            for name in c.EXPECTED_PARENT:shutil.copyfile(c.PARENT/name,root.parent/name)
            for name in ('certify_chain.py','parameters.json','chain_result.json'):shutil.copyfile(HERE/name,root/name)
            data=json.loads((root/'chain_result.json').read_text())
            data['box_image_radius_upper']='0.000000000000000000000000000000'
            (root/'chain_result.json').write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
            result=cli(root);self.assertNotEqual(result.returncode,0)
            self.assertIn('receipt mismatch',result.stderr)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--part',choices=('bounded','full','all'),required=True);args=p.parse_args()
    suite=unittest.TestSuite()
    for cls in ([Bounded] if args.part=='bounded' else [Full] if args.part=='full' else [Bounded,Full]):
        suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(cls))
    ok=unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful()
    sys.exit(0 if ok else 1)
