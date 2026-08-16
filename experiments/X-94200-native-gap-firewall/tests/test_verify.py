#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("verify", HERE / "verify.py")
verify = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(verify)

control = json.loads((HERE / "certificates" / "control.json").read_text())
result = verify.run(control)
assert result["ok"] is True
assert result["rh_established"] is False
assert result["verdict"] == "PASS_NATIVE_GAP_FIREWALL_AND_ARITHMETIC_RESET"
assert result["elementary_X3_counterexample"]["F_lambda_upper"] == "-289/5000"
print("PASS_TEST_NATIVE_GAP_FIREWALL")
