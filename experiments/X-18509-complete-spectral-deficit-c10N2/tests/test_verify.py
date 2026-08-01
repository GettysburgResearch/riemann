import copy
import importlib.util
import json
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("verify", HERE / "verify.py")
verify = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(verify)

PRIMITIVE = json.loads((HERE / "certificates/c10-N2-p768-primitive.json").read_text())
CONFIG = json.loads((HERE / "config.json").read_text())


class TestVerifier(unittest.TestCase):
    def run_bad(self, mutate):
        cfg = copy.deepcopy(CONFIG)
        primitive = copy.deepcopy(PRIMITIVE)
        mutate(cfg, primitive)
        with self.assertRaises((ValueError, ZeroDivisionError, AssertionError)):
            verify.verify(primitive, cfg)

    def test_central(self):
        result = verify.verify(copy.deepcopy(PRIMITIVE), copy.deepcopy(CONFIG))
        self.assertEqual(result["classification"], "CERTIFIED_SOURCE_NOT_CANONICAL_TRUE_DEFICIT_PACKET_DIRECT_SHORT_POSITIVE")
        self.assertEqual(result["direct_short"]["Delta"], "0")
        self.assertFalse(result["source_flag"]["equals_deficit_canonical"])
        self.assertEqual(result["canonical_projector"]["rank_P_D"], 2)

    def test_deficit_not_positive(self):
        self.run_bad(lambda c, p: c.__setitem__("g", "1/10"))

    def test_threshold_crosses_second_eigenvalue(self):
        def m(c, p):
            c["Gamma"] = "1/100000"
            c["theta"] = str(verify.F(c["g"]) - verify.F(c["Gamma"]))
        self.run_bad(m)

    def test_source_flag_mutation(self):
        self.run_bad(lambda c, p: c["source_flag"][0].__setitem__(0, -1))

    def test_projector_center_mutation(self):
        self.run_bad(lambda c, p: c["Y_C_center"].__setitem__(2, 0))

    def test_projector_radius_too_small(self):
        self.run_bad(lambda c, p: c.__setitem__("projector_radius", "1/100000000000000000000000000000000000000000000000000000000000"))

    def test_canonical_floor_too_high(self):
        self.run_bad(lambda c, p: c.__setitem__("canonical_floor", "1/100000000"))

    def test_safe_floor_too_high(self):
        self.run_bad(lambda c, p: c.__setitem__("safe_floor", "9/50"))

    def test_primitive_matrix_mutation(self):
        def m(c, p):
            p["P_even"][0][0]["lower"]["mantissa"] = str(int(p["P_even"][0][0]["lower"]["mantissa"]) + 10**220)
        self.run_bad(m)

    def test_boolean_metric(self):
        self.run_bad(lambda c, p: c["metric_diagonal"].__setitem__(0, True))


if __name__ == "__main__":
    unittest.main()
