#!/usr/bin/env python3
import importlib.util
from pathlib import Path
HERE=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("verify",HERE/"verify.py")
m=importlib.util.module_from_spec(spec);assert spec.loader is not None;spec.loader.exec_module(m)
r=m.run()
assert r["classification"]=="PASS_T105410_F1_ORTHOGONAL_ATO_REDUCTION"
assert r["positive_box_spline_proved"]
assert r["orthogonal_primitive_split_proved"]
assert r["adelic_gram_reduction_proved"]
assert not r["f1ato105405_proved"]
assert not r["rh_established"]
print("PASS_TEST_T105410_F1_ORTHOGONAL_ATO")
