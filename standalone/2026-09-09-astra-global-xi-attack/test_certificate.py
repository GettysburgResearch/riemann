"""Small algebra/arithmetic tests. These do not prove RH or the analytic lemmas."""
import importlib.util
import json
from fractions import Fraction as Q
from pathlib import Path
import tempfile
import unittest

spec=importlib.util.spec_from_file_location('cert',Path(__file__).with_name('certify_truncation.py'))
c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)

def contains(a,q):return Q(a.lo,c.S)<=q<=Q(a.hi,c.S)

class Tests(unittest.TestCase):
    def test_outward_arithmetic(self):
        vals=[Q(-3,2),Q(-1),Q(0),Q(1,7),Q(2)]
        for x in vals:
            for y in vals:
                a,b=c.I.of(x),c.I.of(y)
                self.assertTrue(contains(a+b,x+y))
                self.assertTrue(contains(a-b,x-y))
                self.assertTrue(contains(a*b,x*y))
                if y:self.assertTrue(contains(a/b,x/y))
        with self.assertRaises(TypeError):c.I.of(True)
        with self.assertRaises(ZeroDivisionError):c.I.of(1)/c.I(-1,1)

    def test_entire_primitives(self):
        self.assertTrue(contains(c.expi(0),Q(1)))
        e=c.expi(1);self.assertGreater(e.lo*10,27*c.S);self.assertLess(e.hi*10,28*c.S)
        for x in [Q(0),Q(1,7),Q(3,2),Q(68)]:
            z=c.cis(x);self.assertTrue(contains(z.re*z.re+z.im*z.im,Q(1)))
        self.assertGreater(c.pi_interval().lo*113,355*c.S-1*c.S)
        self.assertLess(c.pi_interval().hi,4*c.S)

    def test_boundary_derivative_and_mixed_terms(self):
        # Differentiate exp(u/2) P(q exp(2u)) exp(-q exp(2u)) at u=0.
        P=[Q(0),Q(-6),Q(4)];out=[Q(0)]*4
        for j,p in enumerate(P):
            out[j]+=(Q(1,2)+2*j)*p
            out[j+1]-=2*p
        self.assertEqual(out,[Q(0),Q(-15),Q(30),Q(-8)])
        for a in [Q(1),Q(2),Q(7,5)]:
            A,Ap,App=-2*a,4*a,-12*a
            B,Bp,Bpp=-A,-Ap,-App
            self.assertEqual(Ap*Ap-A*App,-8*a*a)
            self.assertEqual(Bp*Bp-B*Bpp,-8*a*a)
            self.assertEqual(2*Ap*Bp-A*Bpp-B*App,16*a*a)

    def test_analytic_majorants(self):
        self.assertLess(9_000_000*Q(3,8)**190,Q(1,10**70))
        self.assertLess(256*sum((Q(n**4,(6*n*n-5)**3) for n in range(1,4)),Q(0)),1000)
        self.assertLess(Q(2,10**57)+500*c.RADIUS**2,Q(17,10**21)*c.RADIUS)
        self.assertGreater(c.YI-c.RADIUS,0)
        self.assertLess(c.YI+c.RADIUS,Q(1,2))

    def test_receipt_contract(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'x.json'
            for text in ['{}','[]','{"n":1,"n":2}','{"n":1.0}','{"n":NaN}']:
                p.write_text(text)
                with self.assertRaises(ValueError):c.strict_json(p)
            p.write_text('{"rh_proved":false,"theta_terms":3}')
            good=c.strict_json(p)
            # Canonical serialized comparison distinguishes int/boolean aliases.
            changed=dict(good,theta_terms=True)
            self.assertNotEqual(json.dumps(good,sort_keys=True),json.dumps(changed,sort_keys=True))
            link=Path(tmp)/'link';link.symlink_to(p)
            with self.assertRaises(ValueError):c.strict_json(link)

if __name__=='__main__':unittest.main(verbosity=2)
