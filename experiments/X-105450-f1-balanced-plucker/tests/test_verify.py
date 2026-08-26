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
assert r["classification"]=="PASS_T105450_F1_BALANCED_PLUCKER_LOCAL_SYSTEM"
assert r["all_shared_owner_renewal_proved"] is True
assert r["balanced_pluecker_local_system_proved"] is True
assert r["f1rect_positive_energy_controlling"] is False
assert r["f1bpt105450_proved"] is False
assert r["rh_established"] is False
assert len(r["mutations_rejected"])==11
print("PASS_TEST_T105450_F1_BALANCED_PLUCKER")
