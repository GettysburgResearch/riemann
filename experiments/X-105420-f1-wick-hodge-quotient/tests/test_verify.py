#!/usr/bin/env python3
import importlib.util
from pathlib import Path

here=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('verify',here/'verify.py')
mod=importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)
r=mod.run()
assert r['classification']=='PASS_T105420_F1_WICK_HODGE_QUOTIENT'
assert r['first_chaos_detector_fraction']=='1/769'
assert r['wick_hodge_quotient_identified'] is True
assert r['unquotiented_f1ato105405_valid'] is False
assert r['f1wnc105420_proved'] is False
assert r['rh_established'] is False
assert len(r['mutations_rejected'])==8
print('PASS_TEST_T105420_F1_WICK_HODGE_QUOTIENT')
