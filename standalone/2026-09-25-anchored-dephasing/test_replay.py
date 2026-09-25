#!/usr/bin/env python3
"""ADP37 actual CLI acceptance and refusal controls."""
from __future__ import annotations
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

HERE=Path(__file__).resolve().parent


class ReplayTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp=tempfile.TemporaryDirectory()
        cls.root=Path(cls.temp.name)
        cls.quick=cls.root/'quick.json'
        out=subprocess.run([sys.executable,'-I','-S','-B',str(HERE/'check.py'),
                            '--quick','--output',str(cls.quick)],capture_output=True,text=True)
        if out.returncode:
            raise RuntimeError(out.stderr)
        cls.quick_data=json.loads(cls.quick.read_text())

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def invoke(self,path,quick=True,optimized=False):
        cmd=[sys.executable,'-I','-S','-B']
        if optimized:
            cmd.append('-O')
        cmd += [str(HERE/'check.py'),'--check',str(path)]
        if quick:
            cmd.append('--quick')
        return subprocess.run(cmd,capture_output=True,text=True)

    def mutation(self,label,data):
        path=self.root/(label+'.json')
        path.write_text(json.dumps(data))
        return path

    def reject(self,out,needle='REJECT:'):
        self.assertNotEqual(out.returncode,0)
        self.assertIn(needle,out.stderr)

    def test_pristine_full_normal(self):
        out=self.invoke(HERE/'receipt.json',quick=False)
        self.assertEqual(out.returncode,0,out.stderr)

    def test_pristine_full_optimized(self):
        out=self.invoke(HERE/'receipt.json',quick=False,optimized=True)
        self.assertEqual(out.returncode,0,out.stderr)

    def test_actual_harmonic_endpoint_mutation(self):
        data=json.loads((HERE/'receipt.json').read_text())
        data['actual_harmonic_panels'][-1]['diagonal']['hi']['numerator']+=1
        self.reject(self.invoke(self.mutation('actual-endpoint',data),quick=False),
                    'receipt does not match primitive replay')

    def test_coverage_mutation(self):
        data=json.loads(json.dumps(self.quick_data))
        data['arithmetic_coverage']['rectangular_product_pairs']+=1
        self.reject(self.invoke(self.mutation('coverage',data)))

    def test_primitive_hash_mutation(self):
        data=json.loads(json.dumps(self.quick_data))
        data['primitive_sha256']='0'*64
        self.reject(self.invoke(self.mutation('primitive',data),optimized=True))

    def test_missing_field(self):
        data=json.loads(json.dumps(self.quick_data))
        del data['universal_counterexample_constants']
        self.reject(self.invoke(self.mutation('missing',data)))

    def test_duplicate_key(self):
        path=self.root/'duplicate.json'
        path.write_text('{"mode":"quick-controls","mode":"quick-controls"}')
        self.reject(self.invoke(path),'duplicate JSON key')

    def test_nonfinite_and_malformed(self):
        for idx,text in enumerate(('{"value":NaN}', '{"value":')):
            with self.subTest(text=text):
                path=self.root/('malformed'+str(idx)+'.json')
                path.write_text(text)
                self.reject(self.invoke(path))


if __name__=='__main__':
    unittest.main(verbosity=2)
