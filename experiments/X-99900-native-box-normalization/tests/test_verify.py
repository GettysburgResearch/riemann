#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("verify", HERE / "verify.py")
verify = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(verify)

result = verify.run()
assert result["classification"] == "PASS_T99900_NATIVE_BOX_HALF_ORDER_AND_HARDY_TAIL"
assert result["native_normalized_prime_exponent"] == "-1"
assert result["native_collar_exponent"] == "-1/2"
assert result["gpmoc99800_proved"] is False
assert result["rh_established"] is False
assert len(result["mutations_rejected"]) == 8
print("PASS_TEST_T99900_NATIVE_BOX_NORMALIZATION")
