#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("verify", root / "verify.py")
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = module
spec.loader.exec_module(module)
result = module.run()

assert result["classification"] == "PASS_T105470_F1_DYADIC_HARDY"
assert result["integer_cell_affine_proved"] is True
assert result["closed_cell_integral_proved"] is True
assert result["two_endpoint_equivalence_proved"] is True
assert result["one_hardy_primitive_proved"] is True
assert result["dyadic_jump_filter_proved"] is True
assert result["jump_ledger_subpower_inherited"] is True
assert result["continuous_discrete_equivalence_proved"] is True
assert result["one_interior_sample_sufficient"] is False
assert result["f1hardy105470_proved"] is False
assert result["f1var105460_proved"] is False
assert result["bci102990_proved"] is False
assert result["rh_established"] is False
assert len(result["hostile_mutations_rejected"]) == 15
assert result["finite_checks"] == 186004
print("PASS_TEST_T105470_F1_DYADIC_HARDY")
