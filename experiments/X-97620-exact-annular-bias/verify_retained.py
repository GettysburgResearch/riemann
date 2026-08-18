#!/usr/bin/env python3
from __future__ import annotations

from copy import deepcopy
from decimal import Decimal, getcontext
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
getcontext().prec = 100


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def D(x: str) -> Decimal:
    return Decimal(x)


def validate(v: dict, check_files: bool = True) -> None:
    assert v["ok"] is True
    assert v["verdict"] == "PASS_EXACT_ANNULAR_BIAS_AND_P37_CONTRACTION_CERTIFICATE"
    assert v["frozen_pr565_head"] == "339e3367660f40c74795802a6f8170b15e19b13a"
    assert v["rh_established_by_replay"] is False
    assert v["targeted_crosscheck"]["verdict"] == "PASS_448_TARGETED_CROSSCHECK"
    p = v["p61"]
    assert p["minimum_x"] == 184
    assert D(p["minimum_ratio"]["lo"]) > D(str(float(Fraction(1199, 50000))))
    assert D(p["minimum_ratio"]["lo"]) > D(1) / D(42)
    assert D(p["minimum_left_cell_derivative"]["hi"]) < 0
    assert D(p["minimum_right_cell_derivative"]["lo"]) > 0
    x = v["x184"]
    assert D(x["F_minus_M_over_40"]["hi"]) < 0
    assert D(x["F_minus_M_over_42"]["lo"]) > 0
    assert D(x["discarded_low_children"]["lo"]) > D("1.36")
    assert D(x["true_full_scalar"]["lo"]) > 0
    q = v["p37"]
    assert q["minimum_x"] == 104
    assert D(q["minimum_ratio"]["lo"]) > D(17) / D(500)
    assert D(q["maximum_ratio"]["hi"]) < D(8) / D(125)
    assert v["rational_moats"]["p61_above_one_over_42"] == "179/1050000"

    entries = v["certificate_entries"]
    core = {
        "schema": "riemann.x97620.proof-object.v1",
        "verdict": v["verdict"],
        "frozen_pr565_head": v["frozen_pr565_head"],
        "certificate_entries": entries,
        "crosscheck_verdict": v["targeted_crosscheck"]["verdict"],
        "rh_established": False,
    }
    proof = hashlib.sha256(
        json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    assert proof == v["proof_object_sha256"]

    if check_files:
        full = HERE / "certificates" / "full"
        omitted = []
        retained_lines = 0
        retained_streams = 0
        for entry in entries:
            path = full / entry["file"]
            if not path.is_file():
                omitted.append(entry["file"])
                continue
            assert path.stat().st_size == entry["bytes"]
            assert sha256(path) == entry["sha256"]
            if entry["lines"] is not None:
                with gzip.open(path, "rt", encoding="utf-8") as f:
                    retained_lines += sum(1 for _ in f)
                retained_streams += 1
        assert omitted == ["verification.448.raw.json", "verification.raw.json"]
        assert retained_streams == 8
        assert retained_lines == 1_167_388


def main() -> int:
    path = HERE / "results" / "verification.json"
    v = json.loads(path.read_text())
    validate(v)
    print(v["verdict"])
    print(v["proof_object_sha256"])
    print("RH_ESTABLISHED=false")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
