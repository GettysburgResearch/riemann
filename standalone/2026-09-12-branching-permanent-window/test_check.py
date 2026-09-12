"""Bounded exact unit controls and real accepting/rejecting CLI executions.
--part fast excludes expensive full reconstructions, explicitly; no skipped
analytic proof is counted as a passed test. --part full includes one fresh
complete acceptance and one altered numerical receipt refused after recomputation.
"""
from fractions import Fraction as Q
from math import comb,factorial
from pathlib import Path
import argparse,copy,hashlib,json,os,shutil,subprocess,sys,tempfile,unittest
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import check
import certificate as c
from intervals import I,C,S,exp_i,pi_i
OPT='--optimized' in sys.argv
REFUSALS=[]

def copied(root):
    for name in check.NAMES:shutil.copyfile(HERE/name,root/name)

def reseal(root):
    (root/'SHA256SUMS').write_text(''.join(hashlib.sha256((root/name).read_bytes()).hexdigest()+'  '+name+'\n' for name in sorted(check.NAMES) if name!='SHA256SUMS'))

def command(root,receipt=None):
    return [sys.executable,'-I','-S','-B']+(['-O'] if OPT else [])+[str(root/'check.py'),'--check',str(receipt or root/'result.json')]

def invoke(root,expected,receipt=None):
    r=subprocess.run(command(root,receipt),text=True,capture_output=True,timeout=240)
    if (r.returncode==0)!=expected:raise AssertionError('CLI outcome: '+r.stdout+r.stderr)
    token='PASS_BPW26_FULL' if expected else 'REJECT_BPW26'
    if token not in r.stdout+r.stderr:raise AssertionError('missing explicit result')
    return r

class Fast(unittest.TestCase):
    def test_exact_interval_primitives(self):
        vals=[Q(-7,3),Q(-1,7),Q(),Q(2,11),Q(3,2)]
        def inside(i,x):self.assertLessEqual(Q(i.lo,S),x);self.assertGreaterEqual(Q(i.hi,S),x)
        for a in vals:
            for b in vals:
                inside(I.of(a)+b,a+b);inside(I.of(a)*b,a*b)
                if b:inside(I.of(a)/b,a/b)
        with self.assertRaises(TypeError):I.of(0.5)
        with self.assertRaises(TypeError):I.of(True)
        with self.assertRaises(ZeroDivisionError):I.of(1)/I(-1,1)
        inside(exp_i(0),Q(1))
        for x in [Q(1,8),Q(1,2),Q(1),Q(2)]:
            t=sum((x**j/factorial(j) for j in range(100)),Q())
            rem=x**100/factorial(100)/(1-x/101)
            e=exp_i(x)
            self.assertLessEqual(Q(e.lo,S),t+rem);self.assertGreaterEqual(Q(e.hi,S),t)
            inside(e*exp_i(-x),Q(1))
        p=pi_i();self.assertGreater(Q(p.lo,S),Q(314159,100000));self.assertLess(Q(p.hi,S),Q(314160,100000))

    def test_source_derivative_and_orbit(self):
        self.assertEqual(c.derivative_bounds(),[Q(60),Q(366),Q(3135),Q(71463,2),Q(2044911,4)])
        m=[Q(1),Q(1),Q(7,5),Q(63,25),Q(693,125)]
        for n in range(18):
            self.assertEqual(m[1],1);self.assertEqual(m[2],Q(7,5))
            self.assertEqual(m[3],Q(93,35)-Q(24,175)*Q(31,80)**n)
            m=[m[0]]+[(1-Q(2)**(1-2*j))/Q(2*j-1)*sum((comb(j,k)*m[k]*m[j-k] for k in range(j+1)),Q()) for j in range(1,5)]
        self.assertEqual(Q(6,175)*(2*31**3+3),Q(71502,35))
        self.assertLess(Q(71502,35)*Q(31,80)**32,Q(14,10**11))
        self.assertEqual(Q(5,2)**3/Q(4*3*2)*Q(127,7),Q(15875,1344))

    def test_polynomial_jets(self):
        def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
        def power(z,n):
            a=(Q(1),Q())
            for _ in range(n):a=mul(a,z)
            return a
        coeff=[Q(1),Q(1,3),Q(2,5),Q(1,7),Q(3,11)]
        for z in [(Q(),Q()),(Q(3,2),Q(1,4)),(Q(-2),Q(1,5)),(Q(30),Q(1,2))]:
            v=c.jets([I.of(x) for x in coeff],C(*z))
            for j in range(4):
                a=b=Q()
                for k,x in enumerate(coeff):
                    if 2*k<j:continue
                    f=(-1)**k*x*comb(2*k,j)/32**(2*k);u,w=power(z,2*k-j)
                    a+=f*u;b+=f*w
                for iv,x in [(v[j].re,a),(v[j].im,b)]:
                    self.assertLessEqual(Q(iv.lo,S),x);self.assertGreaterEqual(Q(iv.hi,S),x)

    def test_complete_contours_and_future_margin(self):
        diamond=[(2,0),(0,2),(-2,0),(0,-2),(2,0)]
        self.assertEqual(c.winding(diamond),1);self.assertEqual(c.winding(diamond[::-1]),-1)
        self.assertEqual(c.winding([(a+5,b) for a,b in diamond]),0)
        # The even polynomial z²-1 has two real roots; all segments, not samples.
        coeff=[I.of(-1),I.of(-1024)]
        r=c.contour(coeff,[-2,2,Q(-1,2),Q(1,2)],Q(1,20),Q(1,1000),2)
        self.assertEqual(r['count'],2)
        r=c.contour(coeff,[Q(9,10),Q(11,10),Q(-1,10),Q(1,10)],Q(1,100),Q(1,1000),1)
        self.assertEqual(r['count'],1)
        with self.assertRaises(ValueError):c.contour(coeff,[-2,2,Q(-1,2),Q(1,2)],Q(1,10),Q(10),2)
        r=check.read_json(HERE/'result.json');check.preflight(r)
        coeff=[I(int(x,16),int(y,16)) for x,y in r['polynomial_coefficients']]
        self.assertEqual({k:str(v) for k,v in c.bounds(coeff).items()},r['bounds'])
        for x in r['root_slopes']:
            self.assertLess(4*Q(r['bounds']['orbit_error']),Q(x['absolute_slope_lower'])/2)

    def test_fast_cli_refusals(self):
        cases=['false-rh','false-cofinal','bool-depth','float-height','duplicate-json',
               'missing-tail','missing-boundary','unsealed-proof','extra-file','source-drift','resealed-derivative-primitive']
        for name in cases:
            with tempfile.TemporaryDirectory() as td:
                root=Path(td);copied(root);r=check.read_json(root/'result.json')
                if name=='false-rh':r['rh_proved']=True
                elif name=='false-cofinal':r['cofinal_height_confinement_proved']=True
                elif name=='bool-depth':r['all_depths_from']=True
                elif name=='float-height':r['window_height']=30.0
                elif name=='duplicate-json':
                    text=(root/'result.json').read_text().replace('{','{"schema":"BPW26-1",',1);(root/'result.json').write_text(text)
                elif name=='missing-tail':del r['bounds']['index_tail']
                elif name=='missing-boundary':r['contours'].pop()
                elif name=='unsealed-proof':(root/'PROOF.md').write_text('altered proof\n')
                elif name=='extra-file':(root/'extra.txt').write_text('unaccounted')
                elif name=='source-drift':
                    sr=check.read_json(root/'SOURCES.json');sr['base_commit']='0'*40;(root/'SOURCES.json').write_text(json.dumps(sr))
                elif name=='resealed-derivative-primitive':
                    p=root/'certificate.py';s=p.read_text();s=s.replace('Q(71463,2)','Q(71465,2)')
                    p.write_text(s)
                if name not in ['duplicate-json','unsealed-proof','extra-file','source-drift','resealed-derivative-primitive']:(root/'result.json').write_text(json.dumps(r))
                if name not in ['unsealed-proof','extra-file']:reseal(root)
                invoke(root,False);REFUSALS.append(name)

    def test_symlink_refusal(self):
        with tempfile.TemporaryDirectory() as td:
            base=Path(td);root=base/'packet';root.mkdir();copied(root)
            p=root/'PROOF.md';q=base/'original-proof.md';p.replace(q)
            try:p.symlink_to(q)
            except OSError as e:self.skipTest('host lacks symlink capability: '+str(e))
            invoke(root,False);REFUSALS.append('symlink')

class Full(unittest.TestCase):
    def test_full_acceptance(self):
        r=invoke(HERE,True);self.assertIn('PASS_BPW26_FULL',r.stdout)
    def test_recomputed_numeric_refusal(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);copied(root);r=check.read_json(root/'result.json')
            r['contours'][0]['minimum_linf_margin']='1/100000000'
            (root/'result.json').write_text(json.dumps(r));reseal(root)
            result=invoke(root,False);self.assertIn('primitive reconstruction mismatch',result.stderr)
            REFUSALS.append('resealed-numerical-margin-after-full-reconstruction')

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--part',choices=['fast','full','all'],default='all');ap.add_argument('--optimized',action='store_true');args=ap.parse_args()
    suites=[]
    if args.part in ('fast','all'):suites.append(unittest.defaultTestLoader.loadTestsFromTestCase(Fast))
    if args.part in ('full','all'):suites.append(unittest.defaultTestLoader.loadTestsFromTestCase(Full))
    result=unittest.TextTestRunner(verbosity=2).run(unittest.TestSuite(suites))
    print(json.dumps({'part':args.part,'optimized_subprocesses':OPT,'tests_run':result.testsRun,
                      'skips':len(result.skipped),'failures':len(result.failures),'errors':len(result.errors),
                      'executed_cli_refusals':len(REFUSALS),'refusal_names':REFUSALS},sort_keys=True))
    raise SystemExit(0 if result.wasSuccessful() else 1)
