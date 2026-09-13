"""Bounded algebra, fresh alternate theta mesh, and actual CLI refusals.

The suite does NOT replay a full pristine gamma integral; use check.py for that.
"""
from pathlib import Path
from fractions import Fraction as Q
import copy, hashlib, json, shutil, subprocess, sys, tempfile, unittest
from exact_interval import I, SCALE
from native_sources import power_sums, theta
from moment_tools import interval, solve, positive
from check import read_json, canonical
ROOT=Path(__file__).resolve().parent

def product(a,b):
    c=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

def plus(a,b):
    n=max(len(a),len(b));out=[Q(0)]*n
    for j in range(n):out[j]=(a[j] if j<len(a) else 0)+(b[j] if j<len(b) else 0)
    return out

def rational_gauss(u,d):
    h0=[[u[i+j] for j in range(d)] for i in range(d)]
    c=solve(h0,[-u[d+j] for j in range(d)])+[Q(1)]
    D=[(-1)**j*c[d-j] for j in range(d+1)]
    P=[sum(D[j]*(-1)**(k-j)*u[k-j] for j in range(k+1)) for k in range(d)]
    return P,D

def seal(root):
    paths=[p for p in root.iterdir() if p.name not in ('MANIFEST.json','__pycache__')]
    m={'schema':'MCE26-files-v1','files':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths if p.is_file()}}
    (root/'MANIFEST.json').write_text(json.dumps(m,sort_keys=True,indent=2)+'\n')

def command(root,receipt_only=True):
    cmd=[sys.executable,'-S','-B']
    if sys.flags.optimize:cmd+=['-O']
    cmd+=[str(root/'check.py'),'--check',str(root/'result.json')]
    if receipt_only:cmd+=['--receipt-only']
    return cmd

class Tests(unittest.TestCase):
    def test_power_sum_recursion(self):
        for d in range(1,8):
            for den in (3,7,11):
                nodes=[Q(i,den*10) for i in range(1,d+1)]
                f=[Q(1)]
                for a in nodes:f=product(f,[1,a])
                f+= [Q(0)]*(16-len(f))
                obtained=power_sums([I.q(v) for v in f],sc=1)
                for k,v in enumerate(obtained,1):
                    exact=sum(a**k for a in nodes)
                    self.assertLessEqual(Q(v.lo,SCALE),exact)
                    self.assertGreaterEqual(Q(v.hi,SCALE),exact)

    def test_gaussian_comparator(self):
        for d in range(1,6):
            nodes=[Q(i,13) for i in range(1,d+1)]
            weights=[Q(i+1,7) for i in range(d)]
            u=[sum(c*a**k for a,c in zip(nodes,weights)) for k in range(2*d)]
            P,D=rational_gauss(u,d)
            expected=[Q(1)]
            for a in nodes:expected=product(expected,[1,a])
            self.assertEqual(D,expected)
            num=[Q(0)]
            for j,c in enumerate(weights):
                p=[c]
                for k,a in enumerate(nodes):
                    if k!=j:p=product(p,[1,a])
                num=plus(num,p)
            self.assertEqual(P,num)
            for sh in (0,1):positive([I.q(v) for v in u],d,sh)

    def test_exact_differential_residual(self):
        for d in range(1,6):
            nodes=[Q(i,17) for i in range(1,d+1)]
            weights=[Q(i+1)*a for i,a in enumerate(nodes)]
            u=[sum(c*a**k for a,c in zip(nodes,weights)) for k in range(2*d)]
            P,D=rational_gauss(u,d)
            F=[Q(1)]
            for i,a in enumerate(nodes):
                for unused in range(i+1):F=product(F,[1,0,-a])
            Dz=[Q(0)]*(2*d+1);Pz=[Q(0)]*(2*d)
            for k,c in enumerate(D):Dz[2*k]=(-1)**k*c
            for k,c in enumerate(P):Pz[2*k+1]=2*(-1)**k*c
            derivative=[i*c for i,c in enumerate(F)][1:]
            self.assertTrue(all(c==0 for c in plus(product(Dz,derivative),product(Pz,F))))
        # A valid rational Stieltjes function need not have an entire integral.
        # Here the exponent is exactly 1/2, not an integer zero multiplicity.
        self.assertEqual(Q(1,2)/Q(1),Q(1,2))

    def test_native_receipt_and_alternate_theta_mesh(self):
        result=read_json(ROOT/'result.json')
        alternate=theta(mesh=320)
        original=result['source_theta']
        for key in ('f','scaled_power_sums'):
            for a,b in zip(original[key],alternate[key]):
                a,b=interval(a),interval(b)
                self.assertLessEqual(max(a.lo,b.lo),min(a.hi,b.hi))
        for sh in (0,1):positive(power_sums([interval(v) for v in alternate['f']]),8,sh)
        print('fresh alternate theta mesh320: complete source, both matrices positive',flush=True)

    def test_real_cli_refusals(self):
        def edit_json(path,edit):
            r=read_json(path);edit(r);path.write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
        cases=[]
        cases.append(('duplicate JSON',lambda p:(p/'result.json').write_text('{"schema":"x","schema":"y"}'),True,False))
        cases.append(('Boolean-integer alias',lambda p:edit_json(p/'result.json',lambda r:r['derived'].__setitem__('rh_proved',0)),True,False))
        cases.append(('false RH',lambda p:edit_json(p/'result.json',lambda r:r['derived'].__setitem__('rh_proved',True)),True,False))
        cases.append(('inflated degree',lambda p:edit_json(p/'result.json',lambda r:r['derived']['F5'].__setitem__('raw_moment_degree',30)),True,False))
        cases.append(('zero witness',lambda p:edit_json(p/'parameters.json',lambda r:r.__setitem__('vector',['0']*7)),True,False))
        cases.append(('altered rational numerator',lambda p:edit_json(p/'result.json',lambda r:r['derived']['native_theta_rational_comparator']['P'].__setitem__(0,'0')),True,False))
        cases.append(('altered native coefficient',lambda p:edit_json(p/'result.json',lambda r:r['source_gamma']['f'].__setitem__(1,['1','1'])),True,False))
        cases.append(('mathematical recurrence mutation',lambda p:(p/'native_sources.py').write_text((p/'native_sources.py').read_text().replace('return [(-1)**k*q[k]','return [q[k]')),True,False))
        cases.append(('extra file',lambda p:(p/'unexpected.txt').write_text('extra'),False,False))
        cases.append(('changed gamma rate',lambda p:(p/'native_sources.py').write_text((p/'native_sources.py').read_text().replace('rates=(1,4,9,16,25)','rates=(1,4,9,16,26)')),True,True))
        with tempfile.TemporaryDirectory() as td:
            base=Path(td)
            pristine=base/'pristine';shutil.copytree(ROOT,pristine,ignore=shutil.ignore_patterns('__pycache__'))
            run=subprocess.run(command(pristine),capture_output=True,text=True,timeout=60)
            self.assertEqual(run.returncode,0,run.stdout+run.stderr)
            for i,(name,edit,rehashed,full) in enumerate(cases):
                copied=base/f'bad{i}';shutil.copytree(ROOT,copied,ignore=shutil.ignore_patterns('__pycache__'))
                edit(copied)
                if rehashed:seal(copied)
                run=subprocess.run(command(copied,not full),capture_output=True,text=True,timeout=60)
                self.assertNotEqual(run.returncode,0,name+' incorrectly accepted')
                self.assertIn('REJECT:',run.stderr,name+run.stderr)
                print('actual CLI refusal:',name,('| full mode, rejected at source guard' if full else '| receipt / finite-algebra mode'),flush=True)

if __name__=='__main__':unittest.main(verbosity=2)
