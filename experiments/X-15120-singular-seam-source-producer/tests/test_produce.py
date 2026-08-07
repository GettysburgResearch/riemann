import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("producer", HERE / "produce.py")
producer = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = producer
assert spec.loader is not None
spec.loader.exec_module(producer)

def load(name):
    return json.loads((HERE / "certificates" / name).read_text())

class TestProducer(unittest.TestCase):
    def test_incomplete_public_source_fails_closed(self):
        out = producer.verify_complete(load("shimizu-public-source-v8-v6-audit.json"))
        self.assertEqual(out["status"], "SOURCE_SPECIFICATION_INCOMPLETE")
        self.assertIn("chain.lci_matrix", out["missing_fields"])
        self.assertIn("classical.a4_linear_interval", out["missing_fields"])
        self.assertEqual(out["missing_count"], 17)

    def test_complete_exact_row(self):
        out = producer.verify_complete(load("synthetic-complete-row.json"))
        self.assertEqual(out["status"], "CERTIFIED_SOURCE_BOUND_QUARTIC_ROW")
        self.assertEqual(out["trace_A4"], 1250)
        self.assertEqual(out["trace_K4"], 799)
        self.assertEqual(out["c4_norm_squared"], 1)
        self.assertEqual(out["jet_schatten4_fourth_power"], 7)

    def test_wrong_schema_rejected(self):
        d = load("synthetic-complete-row.json")
        d["schema"] = "wrong"
        with self.assertRaises(ValueError):
            producer.verify_complete(d)

    def test_nonhermitian_seam_rejected(self):
        d = load("synthetic-complete-row.json")
        d["chain"]["seam_involution"] = [[1, 1], [0, -1]]
        with self.assertRaises(ValueError):
            producer.verify_complete(d)

    def test_noninvolutive_seam_rejected(self):
        d = load("synthetic-complete-row.json")
        d["chain"]["seam_involution"] = [[2, 0], [0, 1]]
        with self.assertRaises(ValueError):
            producer.verify_complete(d)

    def test_nonprojection_rejected(self):
        d = load("synthetic-complete-row.json")
        d["chain"]["projection_matrix"] = [[1, 1], [0, 1]]
        with self.assertRaises(ValueError):
            producer.verify_complete(d)

    def test_nonpositive_gram_rejected(self):
        d = load("synthetic-complete-row.json")
        d["readout"]["gram"] = [[1, 0], [0, -1]]
        with self.assertRaises(ValueError):
            producer.verify_complete(d)

    def test_dimension_drift_rejected(self):
        d = load("synthetic-complete-row.json")
        d["chain"]["jet_coordinate_matrix"] = [[0, 1, 0], [1, 1, 0]]
        with self.assertRaises(ValueError):
            producer.verify_complete(d)

    def test_reversed_target_rejected(self):
        d = load("synthetic-complete-row.json")
        d["target"]["tau4_interval"] = [2, 1]
        with self.assertRaises(ValueError):
            producer.verify_complete(d)

    def test_boolean_injection_rejected(self):
        d = load("synthetic-complete-row.json")
        d["readout"]["gram"][0][0] = True
        with self.assertRaises(ValueError):
            producer.verify_complete(d)

    def test_basis_change_invariance(self):
        d = load("synthetic-complete-row.json")
        baseline = producer.verify_complete(d)
        # Source-coordinate change C; Gram -> C* G C and coordinate matrices -> X C.
        C = [[1, 1], [0, 1]]
        G = producer.matrix(d["readout"]["gram"], "G")
        Xr = producer.matrix(d["chain"]["raw_coordinate_matrix"], "Xr")
        Xj = producer.matrix(d["chain"]["jet_coordinate_matrix"], "Xj")
        Cq = producer.matrix(C, "C")
        G2 = producer.mm(producer.adj(Cq), producer.mm(G, Cq))
        Xr2 = producer.mm(Xr, Cq)
        Xj2 = producer.mm(Xj, Cq)
        Cinv = producer.invert(Cq)
        v = producer.vector(d["readout"]["quartic_jet_coordinate"], "v")
        v2 = producer.mv(Cinv, v)
        def dump_matrix(A):
            return [[producer.out_q(z) for z in row] for row in A]
        d["readout"]["gram"] = dump_matrix(G2)
        d["chain"]["raw_coordinate_matrix"] = dump_matrix(Xr2)
        d["chain"]["jet_coordinate_matrix"] = dump_matrix(Xj2)
        d["readout"]["quartic_jet_coordinate"] = [producer.out_q(z) for z in v2]
        changed = producer.verify_complete(d)
        self.assertEqual(changed["trace_A4"], baseline["trace_A4"])
        self.assertEqual(changed["trace_K4"], baseline["trace_K4"])
        self.assertEqual(changed["c4_norm_squared"], baseline["c4_norm_squared"])
        self.assertEqual(changed["jet_schatten4_fourth_power"],
                         baseline["jet_schatten4_fourth_power"])

    def test_zero_jet_pass_manifest(self):
        d = load("synthetic-complete-row.json")
        d["chain"]["jet_coordinate_matrix"] = [[0, 0], [0, 0]]
        d["classical"]["a4_linear_interval"] = [1250, 1250]
        d["target"]["tau4_interval"] = [1250, 1250]
        out = producer.verify_complete(d)
        self.assertEqual(out["quartic_verdict"], "QUARTIC_ROW_OVERLAPS_TARGET")
        self.assertEqual(out["trace_A4"], out["trace_K4"])
        self.assertEqual(out["c4_norm_squared"], 0)
        self.assertEqual(out["jet_schatten4_fourth_power"], 0)

if __name__ == "__main__":
    unittest.main()
