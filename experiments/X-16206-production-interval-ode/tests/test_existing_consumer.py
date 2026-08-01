from __future__ import annotations
import importlib.util, json, sys, unittest
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
REPO = HERE.parents[1]
CONSUMER = REPO / 'X-16204-directed-cofinal-wrapper' / 'verify.py'
SPEC = importlib.util.spec_from_file_location('x16204_consumer', CONSUMER)
assert SPEC is not None and SPEC.loader is not None
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)

class ProductionPacketTests(unittest.TestCase):
    def test_existing_consumer_accepts_real_radial_packet(self):
        payload = json.loads((HERE / 'results' / 'wrapper-certificate.json').read_text())
        result = module.verify(payload)
        self.assertEqual(result['classification'], 'EXACT_COFINAL_CCM_WRAPPER_BLOCK')
        self.assertEqual(result['proof_object_sha256'], 'b19897442f5274364c02d90274ec2a5537b79afb324f631c8313f9ccfe04f995')
        self.assertEqual(result['cofinal_block']['good_measure_lower'], '79/100')
        self.assertEqual(result['positive_route']['ground_correction_ratio_upper'], '5/4999996')

if __name__ == '__main__':
    unittest.main()
