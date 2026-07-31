from __future__ import annotations
import copy, importlib.util, json, tempfile, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("verify", ROOT / "verify.py")
verify = importlib.util.module_from_spec(spec); spec.loader.exec_module(verify)
BASE = json.loads((ROOT / "certificates/five-notch-x0.json").read_text())

class TestX17801(unittest.TestCase):
    def run_data(self, data):
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
            json.dump(data, f); name=f.name
        return verify.main(name)

    def test_replay(self): self.assertEqual(self.run_data(BASE), 0)
    def test_tail_bounds(self):
        self.assertLess(verify.fourier_tail(0), verify.F("1.4e-29"))
        self.assertLess(verify.fourier_tail(4), verify.F("1.5e-15"))
    def test_bad_term_count(self):
        d=copy.deepcopy(BASE); d["runs"][1]["prime_power_terms"]-=1
        with self.assertRaises(ValueError): self.run_data(d)
    def test_non_nested(self):
        d=copy.deepcopy(BASE); d["runs"][1]["prime_upper"]="7e-11"
        with self.assertRaises(ValueError): self.run_data(d)
    def test_old_midpoint_inside_rejected(self):
        d=copy.deepcopy(BASE); d["old_linear_midpoint"]=d["runs"][1]["prime_center"]
        with self.assertRaises(ValueError): self.run_data(d)
    def test_model_outside_rejected(self):
        d=copy.deepcopy(BASE); d["ordinary_zero_plus_trivial_model"]="1e-8"
        with self.assertRaises(ValueError): self.run_data(d)
    def test_boolean_rejected(self):
        with self.assertRaises(TypeError): verify.F(True)

if __name__ == "__main__": unittest.main()
