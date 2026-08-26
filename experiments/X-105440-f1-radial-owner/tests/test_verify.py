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
assert result["classification"] == "PASS_T105440_F1_RADIAL_OWNER_AND_PLUCKER_RECTANGLES"
assert result["radial_owner_decomposition_proved"] is True
assert result["endpoint_difference_factorization_proved"] is True
assert result["four_cycle_plucker_factorization_proved"] is True
assert result["t105430_complete_pair_composition_valid"] is False
assert result["f1eot105441_proved"] is False
assert result["f1rect105443_proved"] is False
assert result["rh_established"] is False
assert len(result["mutations_rejected"]) == 10
print("PASS_TEST_T105440_F1_RADIAL_OWNER")
