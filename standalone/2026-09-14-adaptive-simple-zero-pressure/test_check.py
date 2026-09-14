"""Finite arithmetic and CLI tests; not independent analytic review."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('adaptive_check',ROOT/'check.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
Q = mod.Q


class Tests(unittest.TestCase):
    def test_constant_brackets(self):
        c = mod.constants()
        self.assertGreater(Q(c['new_proportion'][0]),Q('0.67304418'))
        self.assertLess(Q(c['old_280'][1]),Q('0.67300966'))
        self.assertGreater(Q(c['fixed_outer_proportion'][0]),Q('0.673043'))
        lo,hi = mod.h0_bounds(20)
        lo2,hi2 = mod.h0_bounds(40)
        self.assertLessEqual(lo,lo2)
        self.assertGreaterEqual(hi,hi2)

    def test_nonmonotone_pressure_and_empty_tail(self):
        self.assertEqual(mod.greedy([],Q(1,4),Q(1,2),2,Q(1)),([], (0,0)))
        points = [Q(x) for x in (0,0,0,10,10,10,10,10,10,10,10,10)]
        self.assertEqual(mod.greedy(points,Q(1,4),Q(1,2),2,Q(1)),
                         mod.direct_blocks(points,Q(1,4),Q(1,2),2,Q(1)))
        mod.check_partition(points,Q(1,4),Q(1,2),2,Q(1))
        dense=[Q(0)]*12
        blocks,tail=mod.greedy(dense,Q(1,4),Q(1,2),2,Q(1))
        self.assertEqual(blocks,[(0,4),(4,8),(8,12)])
        self.assertEqual(tail,(12,12))

    def test_exhaustive_partitions_and_offsets(self):
        c=mod.partition_controls()
        self.assertEqual(c['exhaustive_small_gap_lists'],6560)
        self.assertEqual(c['outer_size_offset_panels'],451)

    def test_spectral_and_pinching_controls(self):
        c=mod.spectral_controls()
        self.assertEqual(c['four_point_spectra'],969)
        self.assertEqual(c['exact_pinching_panels'],2907)
        with self.assertRaises(ValueError):
            mod.psi(-1)

    def test_invalid_inputs_and_exact_square_roots(self):
        for a in range(20):
            lo,hi=mod.sqrt_bounds(Q(a,7))
            self.assertLessEqual(lo*lo,Q(a,7))
            self.assertGreaterEqual(hi*hi,Q(a,7))
        self.assertEqual(mod.sqrt_bounds(Q(9,16)),(Q(3,4),Q(3,4)))
        with self.assertRaises(ValueError):
            mod.greedy([Q(1),Q(0)],Q(1),Q(1),1,Q(1))
        with self.assertRaises(ValueError):
            mod.greedy([Q(0)],Q(1),Q(0),1,Q(1))
        with self.assertRaises(ValueError):
            mod.h0_bounds(19)

    def test_real_cli_and_ten_corruptions(self):
        expected=json.loads((ROOT/'results.json').read_text())
        flags=['-I','-S','-B']+(['-O'] if sys.flags.optimize else [])
        cmd=[sys.executable,*flags,str(ROOT/'check.py'),'--check']
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'receipt.json'
            p.write_text(json.dumps(expected))
            good=subprocess.run(cmd+[str(p)],capture_output=True,text=True)
            self.assertEqual(good.returncode,0,good.stderr)
            bad=[]
            for field in ('rh_proved','seven_gap_replayed','external_analytic_inputs_reproved'):
                d=copy.deepcopy(expected);d[field]=True;bad.append(json.dumps(d))
            d=copy.deepcopy(expected);d['constants']['window_loss']=True;bad.append(json.dumps(d))
            d=copy.deepcopy(expected);d['constants']['sqrt_bits']=256.0;bad.append(json.dumps(d))
            d=copy.deepcopy(expected);d['constants']['new_proportion'][0]='0.7';bad.append(json.dumps(d))
            d=copy.deepcopy(expected);d['constants']['alpha']='1/3000';bad.append(json.dumps(d))
            d=copy.deepcopy(expected);del d['partitions']['outer_size_offset_panels'];bad.append(json.dumps(d))
            d=copy.deepcopy(expected);d['status']='ACCEPTED_RH_PROOF';bad.append(json.dumps(d))
            bad.append('{"rh_proved":false,'+json.dumps(expected)[1:])
            self.assertEqual(len(bad),10)
            for i,text in enumerate(bad):
                with self.subTest(case=i):
                    p.write_text(text)
                    proc=subprocess.run(cmd+[str(p)],capture_output=True,text=True)
                    self.assertNotEqual(proc.returncode,0)
                    self.assertNotIn('PASS_ADAPTIVE',proc.stdout)
        print('CLI: one pristine acceptance, ten actual refusals')


if __name__ == '__main__':
    unittest.main(verbosity=2)
