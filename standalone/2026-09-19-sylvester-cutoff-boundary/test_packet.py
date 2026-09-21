#!/usr/bin/env python3
"""Regression checks. Run with -I -S; no assert-based acceptance."""
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / (name+'.py'))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

B, L = load('boundary'), load('lfamily')

class Regression(unittest.TestCase):
    def test_kernel_and_structural_controls(self):
        self.assertEqual(B.small_exact_tests()['fake_divisor_failure'], 6)
    def test_input_guard(self):
        for value in (True, 1, 256, -1, 3.0):
            with self.assertRaises(ValueError): B.native(value)
    def test_duplicate_keys(self):
        with self.assertRaises(ValueError):
            json.loads('{"Y":15,"Y":3}', object_pairs_hook=B.no_duplicates)
    def test_type_alias_and_result_mutations(self):
        a = {'value':1,'sign':-1,'endpoint':16}
        for key, value in [('value',True),('sign',1),('endpoint',15)]:
            changed=dict(a);changed[key]=value
            self.assertNotEqual(B.canonical(a), B.canonical(changed))
    def test_boundary_singleton_and_nonsquarefree(self):
        self.assertEqual(B.boundary_atoms(3,6), (2,[(3,-1)]))
        self.assertEqual(B.boundary_atoms(3,12), (2,[(3,-1)]))
        self.assertEqual(B.boundary_atoms(3,5), (5,[(1,1)]))
    def test_field_laws(self):
        f=L.Field(17,(4,3))
        for i in range(1,13):
            a=f.elt((i,1,2,3,4,5));b=f.elt((3,i,5,1,0,2));c=f.elt(i)
            self.assertEqual(a*(b+c),a*b+a*c)
            self.assertEqual(a/a,1)
            self.assertEqual((a*b)*c,a*(b*c))
    def test_field_hypothesis_failures(self):
        for p,v in [(53,(4,3)),(7,(4,3)),(15,(4,3)),(17,(0,0))]:
            with self.assertRaises(ValueError): L.Field(p,v)
    def test_sylvester_local_fixtures(self):
        self.assertEqual(L.local_fixture(13,17)['epsilon'],1)
        self.assertEqual(L.local_fixture(13,107)['epsilon'],-1)
        self.assertEqual(L.local_fixture(31,17)['epsilon'],1)
    def test_projector_orders(self):
        self.assertEqual(len(L.projector_checks()),10)
    def test_gl2_inert_and_split_cases(self):
        r=L.gl2_checks()
        self.assertEqual(r['local_traces']['5'],0)
        self.assertNotEqual(r['local_traces']['7'],0)
        self.assertGreater(r['boundary_instances'],0)

if __name__=='__main__': unittest.main()
