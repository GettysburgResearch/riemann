#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
from pathlib import Path

here = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("verify", here / "verify.py")
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)
result = module.run()

assert result["classification"] == "PASS_T104100_ROOT_RETURN_ROOT_FREE_QUOTIENT"
assert result["two_key_absorption_proved"] is True
assert result["sorr104100_proved"] is False
assert result["rfcp104100_proved"] is False
assert result["rh_established"] is False
assert len(result["mutations_rejected"]) == 7
print("PASS_TEST_T104100_ROOT_RETURN_QUOTIENT")
