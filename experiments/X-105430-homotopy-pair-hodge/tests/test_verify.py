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

assert result["classification"] == "PASS_T105430_HOMOTOPY_COHERENT_PAIR_HODGE"
assert result["homotopy_variance_proved"] is True
assert result["degree_two_hodge_proved"] is True
assert result["extreme_pair_transfer_proved"] is True
assert result["isolated_wick_energy_subpower"] is False
assert result["f1star105431_proved"] is False
assert result["f1cycle105431_proved"] is False
assert result["f1hcnc105430_proved"] is False
assert result["rh_established"] is False
assert len(result["mutations_rejected"]) == 9
print("PASS_TEST_T105430_HOMOTOPY_PAIR_HODGE")
