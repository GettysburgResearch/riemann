#!/usr/bin/env python3
from __future__ import annotations

from copy import deepcopy
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("verify_retained", HERE / "verify_retained.py")
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)
base = json.loads((HERE / "results" / "verification.json").read_text())
mod.validate(base, check_files=False)

mutations = []
def mutation(name, fn):
    x = deepcopy(base); fn(x); mutations.append((name, x))

mutation("restore_false_1_over_40", lambda x: x["x184"]["F_minus_M_over_40"].update(hi="0"))
mutation("erase_minimum", lambda x: x["p61"].update(minimum_x=185))
mutation("break_left_derivative", lambda x: x["p61"]["minimum_left_cell_derivative"].update(hi="1"))
mutation("drop_moat", lambda x: x["rational_moats"].update(p61_above_one_over_42="0"))
mutation("erase_low_children", lambda x: x["x184"]["discarded_low_children"].update(lo="0"))
mutation("promote_RH", lambda x: x.update(rh_established_by_replay=True))
mutation("change_frozen_head", lambda x: x.update(frozen_pr565_head="0" * 40))
mutation("forge_proof_hash", lambda x: x.update(proof_object_sha256="0" * 64))
mutation("alter_certificate_ledger", lambda x: x["certificate_entries"][0].update(bytes=0))

caught = 0
for name, item in mutations:
    try:
        mod.validate(item, check_files=False)
    except (AssertionError, KeyError):
        caught += 1
    else:
        raise AssertionError(f"mutation escaped: {name}")
assert caught == len(mutations)
print(f"PASS_T97620_MUTATIONS caught={caught}")
