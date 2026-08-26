#!/usr/bin/env python3
from __future__ import annotations
import importlib.util
from pathlib import Path

here=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("verify",here/"verify.py")
mod=importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)
r=mod.run()

assert r["classification"]=="PASS_T105460_F1_WICK_REFLECTION_HODGE"
assert r["prime_box_boolean_chow_proved"] is True
assert r["beta_pair_green_proved"] is True
assert r["equal_pair_pure_lefschetz_proved"] is True
assert r["configuration_diagonal_split_proved"] is True
assert r["reflection_signature_proved"] is True
assert r["zero_mass_tv_equivalence_proved"] is True
assert r["half_kernel_tp3"] is False
assert r["f1var105460_proved"] is False
assert r["bci102990_proved"] is False
assert r["rh_established"] is False
assert len(r["mutations_rejected"])==13
print("PASS_TEST_T105460_F1_WICK_REFLECTION_HODGE")
