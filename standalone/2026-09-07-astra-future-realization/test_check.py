#!/usr/bin/env python3
"""Bounded CLI and semantic rejection tests, meaningful under python -O."""
from fractions import Fraction as F
import hashlib,json,os
from pathlib import Path
import shutil,subprocess,sys,tempfile,unittest
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parent

def load_check():
 import types
 m=types.ModuleType('fr26_test_driver');m.__file__=str(ROOT/'check.py')
 exec(compile((ROOT/'check.py').read_bytes(),str(ROOT/'check.py'),'exec'),m.__dict__)
 return m

class Tests(unittest.TestCase):
 def test_strict_json(self):
  c=load_check()
  for text in ['{"x":1,"x":2}','{"x":1.0}','{"x":NaN}']:
   with self.assertRaises(ValueError):c.strict_json(text)
 def test_floor_types(self):
  c=load_check();core,p=c.authenticate(ROOT)
  for bad in [-1,True,1.0,'4']:
   with self.assertRaises(ValueError):p.gram_floor(bad)
  self.assertEqual(p.gram_floor(0),F(1,2**26))
 def test_coefficients_and_source(self):
  c=load_check();core,p=c.authenticate(ROOT)
  self.assertEqual(sum(abs(x)for x in p.COEFFS),F(8435,10000))
  self.assertEqual(sum(p.COEFFS),F(133,10000))
  for x in [True,2.0,F(0)]:
   if type(x) is F:
    with self.assertRaises(ValueError):core.logq(x)
   else:
    with self.assertRaises(TypeError):core.I.of(x)
 def test_kernel_phase(self):
  c=load_check();core,p=c.authenticate(ROOT)
  z=core.C(1,2);r=(z-F(1,2))/(z+F(1,2))
  lhs=sum((x*r**j for j,x in enumerate(p.COEFFS)),core.C(0))
  self.assertNotEqual(lhs,-lhs)
 def test_actual_cli_rejections(self):
  c=load_check()
  def seal(q):
   names=sorted(c.EXPECTED-{'SHA256SUMS'})
   (q/'SHA256SUMS').write_text(''.join(hashlib.sha256((q/n).read_bytes()).hexdigest()+'  '+n+'\n'for n in names))
  variants=['empty_manifest','duplicate_json','float_alias','false_status','bool_degree','narrow_coverage',
            'rehashed_false_energy','changed_core','changed_lock','extra_path','symlink']
  for which in variants:
   with self.subTest(which=which),tempfile.TemporaryDirectory() as td:
    q=Path(td)/'packet';shutil.copytree(ROOT,q)
    if which=='empty_manifest':(q/'SHA256SUMS').write_text('')
    elif which=='duplicate_json':
     p=q/'verification.json';text=p.read_text();p.write_text(text.replace('{','{"rh_proved":false,',1));seal(q)
    elif which=='float_alias':
     p=q/'verification.json';p.write_text(p.read_text().replace('"half_cells": 4094','"half_cells": 4094.0'));seal(q)
    elif which in ['false_status','bool_degree','narrow_coverage','rehashed_false_energy']:
     p=q/'verification.json';x=json.loads(p.read_text())
     if which=='false_status':x['rh_proved']=True
     elif which=='bool_degree':x['scope']['degree']=True
     elif which=='narrow_coverage':x['scope']['half_cells']=1022
     else:x['actual_source']['ideal_full_error']['hi']=str(int(x['actual_source']['ideal_full_error']['hi'])+1)
     p.write_text(c.canonical(x));seal(q)
    elif which=='changed_core':
     p=q/'interval_core.py';p.write_text(p.read_text()+'\n# changed primitive\n');seal(q)
    elif which=='changed_lock':
     p=q/'SOURCE_LOCK.json';x=json.loads(p.read_text());x['unknown_zeros_are_inputs']=True;p.write_text(c.canonical(x));seal(q)
    elif which=='extra_path':(q/'unexpected.txt').write_text('extra')
    elif which=='symlink':
     p=q/'README.md';p.unlink();p.symlink_to(ROOT/'README.md')
    cmd=[sys.executable]+(['-O']if sys.flags.optimize else[])+['-B',str(q/'check.py')]
    result=subprocess.run(cmd,text=True,capture_output=True,timeout=25)
    self.assertNotEqual(result.returncode,0,which+' unexpectedly accepted')
    self.assertIn('REJECT:',result.stderr)

if __name__=='__main__':unittest.main(verbosity=2)
