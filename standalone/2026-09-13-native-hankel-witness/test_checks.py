"""Bounded independent algebra checks and actual CLI refusal tests.

--parts must name eight already-produced source partitions. The adverse CLI
runs reassemble those parts and recompute the suffix; they are NOT fresh full
785-cell integral replays. run_all.py produces its own pristine parts first.
"""
import argparse
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import json, shutil, subprocess, sys, tempfile, unittest
import native_check as n

ROOT=Path(__file__).resolve().parent
PARTS=None


def conv(a,b,m):
    return [sum((a[j]*b[k-j] for j in range(max(0,k-len(b)+1),min(k+1,len(a)))),Q(0))
            for k in range(m+1)]


def log_direct(b):
    """Finite nilpotent logarithm, independent of the Newton recursion."""
    m=len(b)-1;x=list(b);x[0]=Q(0);power=[Q(1)]+[Q(0)]*m;out=[Q(0)]*(m+1)
    for j in range(1,m+1):
        power=conv(power,x,m)
        out=[v+Q((-1)**(j+1),j)*w for v,w in zip(out,power)]
    return out


def contained(value,interval):
    return Q(interval.lo,n.SCALE)<=value<=Q(interval.hi,n.SCALE)


class Checks(unittest.TestCase):
    def test_positive_products_and_formal_log(self):
        m=14
        for count in range(1,10):
            nodes=[Q(j,20+j) for j in range(1,count+1)]
            alpha=Q(count,100)
            b=[alpha**k/factorial(k) for k in range(m+1)]
            for a in nodes:b=conv(b,[Q(1),a],m)
            q=n.power_sums([n.I.q(v/Q(200)**k) for k,v in enumerate(b)])
            direct=log_direct(b)
            for k in range(1,m+1):
                exact=sum((x**k for x in nodes),Q(0))+(alpha if k==1 else 0)
                self.assertEqual((-1)**(k+1)*k*direct[k],exact)
                self.assertTrue(contained(exact,q[k]))
            exact_form=sum((a*a*sum(Q(c)*a**j for j,c in enumerate(n.P))**2
                            for a in nodes),Q(0))
            self.assertGreaterEqual(exact_form,0)
            self.assertTrue(contained(exact_form,n.form(q)))

    def test_touchard_against_differential_recursion(self):
        p=n.pi();tau=p*p/3-2*sum((Q(1,k*k) for k in range(1,6)),Q(0)); rr=n.rows()
        pp=n.panels()
        for idx in (0,200,600,784):
            c,d,rho=pp[idx]
            for sign in (-1,1):
                a=n.density_series(c,rho,sign,rr,tau,p,12)
                b=n.density_series_fast(c,rho,sign,rr,tau,p,12)
                for x,y in zip(a,b):
                    self.assertLessEqual(max(x.lo,y.lo),min(x.hi,y.hi))

    def test_complete_cover_and_endpoint_guards(self):
        pp=n.panels();self.assertEqual(len(pp),785)
        p=n.pi();tau=p*p/3-2*sum((Q(1,k*k) for k in range(1,6)),Q(0))
        ratio,gap=n.guards(p,tau,n.rows())
        self.assertLess(ratio,Q(1,4))
        self.assertGreater(gap,n.LHI-n.B)
        self.assertEqual(pp[0][0]-pp[0][1],0)
        self.assertEqual(pp[-1][0]+pp[-1][1],n.B)
        for (c,d,r),(cc,dd,rr) in zip(pp,pp[1:]):self.assertEqual(c+d,cc-dd)

    def test_formal_dual_derivative(self):
        m=14;b=[Q(1)]+[Q(1,factorial(k)*10**k) for k in range(1,m+1)]
        reciprocal=[Q(1)]
        for j in range(1,m+1):reciprocal.append(-sum(b[k]*reciprocal[j-k] for k in range(1,j+1)))
        self.assertEqual(conv(b,reciprocal,m),[Q(1)]+[Q(0)]*m)
        W=[0]*(m+1)
        for i in range(7):
            for j in range(7):W[i+j+2]+=n.P[i]*n.P[j]
        # A dual-number derivative of the finite logarithm, rather than the
        # reciprocal-series derivative used by the accepting bound.
        x=list(b);x[0]=0
        for ell in (1,2,7,14):
            direction=[Q(int(k==ell)) for k in range(m+1)]
            power=[Q(1)]+[Q(0)]*m; deriv=[Q(0)]*(m+1); answer=[Q(0)]*(m+1)
            for j in range(1,m+1):
                deriv=[u+v for u,v in zip(conv(deriv,x,m),conv(power,direction,m))]
                power=conv(power,x,m)
                answer=[u+Q((-1)**(j+1),j)*v for u,v in zip(answer,deriv)]
            lhs=sum((-1)**(k+1)*k*W[k]*answer[k] for k in range(2,m+1))
            rhs=sum((-1)**(k+1)*k*W[k]*reciprocal[k-ell] for k in range(max(ell,2),m+1))
            self.assertEqual(lhs,rhs)
        eps=Q(1,1<<26);u=eps*Q(3,4)*Q(25,128)*71
        self.assertLess(eps*36787+3500000000000*u*u/(2*(1-u)),Q(43,1000))

    def test_actual_cli_refusals(self):
        self.assertIsNotNone(PARTS)
        flags=['-S','-B']+(['-O'] if sys.flags.optimize else [])
        def run(folder,receipt):
            return subprocess.run([sys.executable,*flags,str(folder/'native_check.py'),
                '--finish-parts',str(PARTS),'--check',str(receipt)],capture_output=True,text=True)
        with tempfile.TemporaryDirectory() as tmp:
            target=Path(tmp)
            for name in ('native_check.py','exact_interval.py','certificate.json'):
                shutil.copyfile(ROOT/name,target/name)
            rec=target/'certificate.json'; original=rec.read_text()
            result=run(target,rec)
            self.assertEqual(result.returncode,0,result.stdout+result.stderr)
            for name,key,value in (('false RH','rh_proved',True),
                    ('numeric Boolean alias','rh_proved',0),
                    ('enlarged order','max_raw_moment_degree',30),
                    ('wrong full digest','full_reconstruction_sha256','0'*64)):
                obj=json.loads(original);obj[key]=value;rec.write_text(json.dumps(obj))
                r=run(target,rec);self.assertNotEqual(r.returncode,0,name)
            rec.write_text(original[:-2]+',"rh_proved": false}\n')
            r=run(target,rec);self.assertNotEqual(r.returncode,0,'duplicate key')
            rec.write_text(original)
            source=(target/'native_check.py').read_text()
            changes=[('changed source rates','RATES = (1, 4, 9, 16, 25)','RATES = (1, 4, 9, 16, 26)'),
                     ('reversed logarithmic power sums','q[n] = (-1)**(n+1)*','q[n] = (-1)**n*'),
                     ('unjustified fit radius','epsilon=Q(1,1<<26);','epsilon=Q(1,1<<25);')]
            for name,old,new in changes:
                self.assertEqual(source.count(old),1)
                (target/'native_check.py').write_text(source.replace(old,new))
                r=run(target,rec);self.assertNotEqual(r.returncode,0,name)
            (target/'native_check.py').write_text(source)
            with (target/'exact_interval.py').open('a') as f:f.write('\n# changed primitive\n')
            r=run(target,rec);self.assertNotEqual(r.returncode,0,'primitive drift')
        print('ONE PRISTINE ASSEMBLY/SUFFIX ACCEPTANCE; NINE ACTUAL CLI REFUSALS',flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--parts',type=Path,required=True)
    args=parser.parse_args();PARTS=args.parts.resolve()
    if not all((PARTS/f'part_{i}.json').is_file() for i in range(8)):
        raise SystemExit('Supply eight completed partitions, or use run_all.py.')
    unittest.main(argv=[sys.argv[0]],verbosity=2)
