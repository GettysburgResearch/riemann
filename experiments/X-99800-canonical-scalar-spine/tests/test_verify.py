#!/usr/bin/env python3
from __future__ import annotations
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("verify", HERE / "verify.py")
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)
result = module.run()
assert result["classification"] == "PASS_T99800_CANONICAL_SCALAR_SPINE_AND_GPMOC_ALGEBRA"
assert result["exceptional_67_square_checked"] is True
assert result["gpmoc99800_proved"] is False
assert result["rh_established"] is False
assert len(result["mutations_rejected"]) == 9
print("PASS_TEST_T99800_CANONICAL_SCALAR_SPINE")
