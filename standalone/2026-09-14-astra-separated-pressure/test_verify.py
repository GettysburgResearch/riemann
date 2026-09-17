#!/usr/bin/env python3
"""Bounded tests. No test method repeats the exhaustive seven-point search."""
from __future__ import annotations
import hashlib
import json
import math
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from fractions import Fraction as Q
import verify as v

ROOT = Path(__file__).resolve().parent


class Checks(unittest.TestCase):
    def test_exact_majorant_and_constants(self):
        r = v.build()
        self.assertEqual(r['bounded_controls']['majorant']['minimum'], '41/1440')
        self.assertGreater(Q(r['constant_enclosures']['H_separated'][0]), Q('0.6730583253156109'))
        self.assertLess(Q(r['constant_enclosures']['H_separated'][1]), Q('0.6730583253156110'))
        self.assertEqual(r['bounded_controls']['combinatorics']['cluster_gap_patterns'], 8191)

    def test_constant_from_bernoulli_series(self):
        # Independent exact coefficient recurrence for x*cot(x). The classical
        # partial fraction expansion gives the complete geometric tail below.
        bern = [Q(1)]
        for n in range(1,82):
            bern.append(-sum((Q(math.comb(n+1,k))*bern[k]
                               for k in range(n)),Q(0))/Q(n+1))
        low = Q(1,2) + sum((Q(2**n)*abs(bern[2*n])/math.factorial(2*n)
                            for n in range(1,41)),Q(0))
        # zeta(2n)<2 and (x/pi)^2<1/18, so remaining terms are at most
        # 4 sum_{n>=41} 18^-n.
        high = low + 4*Q(1,18)**41/(1-Q(1,18))
        cb = v.constants()['H_MT']
        self.assertLess(low, Q(cb[1]))
        self.assertGreater(high, Q(cb[0]))
        self.assertLess(high-low, Q(1,10**49))

    def test_pristine_and_actual_cli_refusals(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)/'packet'
            shutil.copytree(ROOT,target,ignore=shutil.ignore_patterns('__pycache__'))
            flags = ['-S','-B'] + (['-O'] if sys.flags.optimize else [])
            cmd = [sys.executable,*flags,str(target/'verify.py')]
            def run(expect_good):
                p = subprocess.run(cmd,capture_output=True,text=True)
                self.assertEqual(p.returncode == 0, expect_good, p.stdout+p.stderr)
                if expect_good:
                    self.assertIn('SEVEN_RECEIPT_ONLY',p.stdout)
                else:
                    self.assertIn('REJECT:',p.stderr)
            run(True)
            rp=target/'result.json'; sp=target/'seven_result.json'; vp=target/'verify.py'
            original={p:p.read_bytes() for p in (rp,sp,vp,target/'vendor'/'dyadic_interval.py')}
            cases=[]
            def result_mutation(key,value):
                obj=json.loads(original[rp]); obj[key]=value
                rp.write_text(json.dumps(obj))
            cases.append(lambda:result_mutation('rh_proved',True))
            cases.append(lambda:result_mutation('analytic_review_required',1))
            def altered_bound():
                obj=json.loads(original[rp]); obj['constant_enclosures']['H_separated'][0]='0.674'
                rp.write_text(json.dumps(obj))
            cases.append(altered_bound)
            cases.append(lambda:rp.write_text(original[rp].decode().replace('"rh_proved": false',
                                     '"rh_proved": false, "rh_proved": false')))
            def altered_count():
                obj=json.loads(original[sp]); obj['counts']['nodes']-=1
                sp.write_text(json.dumps(obj))
            cases.append(altered_count)
            cases.append(lambda:vp.write_text(original[vp].decode().replace(
                                      'MAJORANT_SCALE = Q(6, 5)','MAJORANT_SCALE = Q(1)')))
            cases.append(lambda:vp.write_text(original[vp].decode().replace(
                                      "need(3*len(pairs) >= bad", "need(2*len(pairs) >= bad")))
            def changed_vendor():
                p=target/'vendor'/'dyadic_interval.py'
                p.write_bytes(original[p]+b'\n# changed\n')
            cases.append(changed_vendor)
            for mutation in cases:
                for path,data in original.items(): path.write_bytes(data)
                mutation(); run(False)
            self.assertEqual(len(cases),8)


if __name__ == '__main__':
    unittest.main(verbosity=2)
