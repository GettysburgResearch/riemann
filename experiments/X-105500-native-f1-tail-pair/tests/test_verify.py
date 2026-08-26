from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


def test_native_f1_tail_pair_replay() -> None:
    root = Path(__file__).resolve().parents[1]
    spec = importlib.util.spec_from_file_location("x105500_verify", root / "verify.py")
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)

    result = module.run()
    assert result["classification"] == "PASS_T105500_NATIVE_F1_TAIL_PAIR"
    assert result["finite_checks"] == 161264
    assert result["proof_object_sha256"] == (
        "e25255643bfd11e9fc931b4484189d0f6178bcf5537f39d734acb0b3da84a386"
    )
    assert result["qpti_semiprime_main_transfers_to_balanced_source"] is False
    assert result["balanced_core_vanishes_below_u_squared"] is True
    assert result["native_f1xd105504_proved"] is False
    assert result["native_cell105504_proved"] is False
    assert result["rh_established"] is False
