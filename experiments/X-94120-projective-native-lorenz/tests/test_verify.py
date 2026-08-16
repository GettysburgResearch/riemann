import importlib.util
from pathlib import Path
import tempfile
import unittest

HERE=Path(__file__).resolve().parents[1]

def load(name,path):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);assert s.loader;s.loader.exec_module(m);return m
pg=load('pg94120',HERE/'projective_gluing.py')
vr=load('vr94120',HERE/'verify.py')

class TestProjective(unittest.TestCase):
    def test_registry_and_budget(self):
        x=pg.build()
        self.assertEqual(x['registry_summary']['squarefree_count'],327)
        self.assertEqual(x['registry_summary']['finite_occurrence_count'],2473)
        for b in x['hazard_budgets'].values():
            self.assertLess(float(b['gamma_sum']),0.125)
    def test_formal_commuting_square(self):
        x=pg.formal_commuting_square_audit()
        self.assertTrue(x['commutes_exactly'])
        self.assertTrue(x['parity_drop_detected'])
    def test_q2_obstruction_retained(self):
        x=pg.q2_obstruction();self.assertEqual(x['rational_lower'],'1/9');self.assertEqual(x['oriented_child_upper'],'-1/9')
    def test_mutations_fail(self):
        with tempfile.TemporaryDirectory() as d:
            p=vr.run(Path(d)/'v.json',mutations=True)
            self.assertGreaterEqual(p['hostile_mutations_rejected'],16)

if __name__=='__main__':unittest.main()
