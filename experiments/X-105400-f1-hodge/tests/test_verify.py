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
assert result["classification"] == "PASS_T105400_F1_NATIVE_SOURCE_FINITE_HODGE"
assert result["finite_native_functor_proved"] is True
assert result["finite_hodge_gap_proved"] is True
assert result["three_ray_primitive_trace_proved"] is True
assert result["f1pe105403_proved"] is False
assert result["rh_established"] is False
assert len(result["mutations_rejected"]) == 9
print("PASS_TEST_T105400_F1_HODGE")
