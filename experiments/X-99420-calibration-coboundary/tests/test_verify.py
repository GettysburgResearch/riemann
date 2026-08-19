#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("verify", HERE / "verify.py")
verify = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(verify)

r = verify.run()
assert r["verdict"] == "PASS_T99420_CALIBRATION_COBOUNDARY_CLOSURE_ALGEBRA"
assert r["resolved_calibration_equals_root_potential"] is True
assert r["generationwise_overcount_detected"] is True
assert r["rh_established"] is False
print("PASS_TEST_T99420_CALIBRATION_COBOUNDARY")
