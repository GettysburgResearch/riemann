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

assert result["classification"] == "PASS_T105480_F1_HARDY_GRAM"
assert result["hardy_from_square_proved"] is True
assert result["continuous_discrete_l2_equivalence_proved"] is True
assert result["positive_semidefinite_gram_proved"] is True
assert result["diagonal_gram_subpower_inherited"] is True
assert result["square_offdiagonal_equivalence_proved"] is True
assert result["mellin_plancherel_coordinate_proved"] is True
assert result["source_blind_gram_bound"] is False
assert result["f1gram105480_proved"] is False
assert result["f1hcnc105481_proved"] is False
assert result["f1hardy105470_proved"] is False
assert result["bci102990_proved"] is False
assert result["rh_established"] is False
assert len(result["hostile_mutations_rejected"]) == 16
print("PASS_TEST_T105480_F1_HARDY_GRAM")
