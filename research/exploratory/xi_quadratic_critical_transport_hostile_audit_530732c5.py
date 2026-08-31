"""Independent rejection harness; calls frozen producer solely to test acceptance."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
SPEC = importlib.util.spec_from_file_location(
    "qt_frozen", HERE / "xi_quadratic_critical_transport.py"
)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


def require(ok, message):
    if not ok:
        raise ValueError(message)


def rejected(call):
    try:
        call()
    except (ValueError, M.ReplayFailure):
        return True
    raise RuntimeError("hostile input accepted")


def main():
    source = M.decode(M.FIXTURE.read_bytes())
    guards = 0
    task = {"route": "outer_direct", "center": [256, 1], "radius": [7, 8], "bits": 256}
    for key, value in (
        ("route", True),
        ("route", "third_other"),
        ("bits", True),
        ("bits", 128),
        ("bits", 2048),
        ("center", [True, 1]),
        ("center", [20, 1]),
        ("center", [1100, 1]),
        ("center", [2**4097, 1]),
        ("radius", [0, 1]),
        ("radius", [7, 0]),
        ("radius", [1, 2]),
    ):
        bad = copy.deepcopy(task)
        bad[key] = value
        rejected(lambda bad=bad: M.native_task(bad))
        guards += 1
    for raw in (b'{"a":0,"a":1}', b'{"a":0.0}', b'{"a":NaN}', b'{"a":Infinity}'):
        rejected(lambda raw=raw: M.decode(raw))
        guards += 1
    for mutation in (
        lambda h: h.update(wallcap_seconds=True),
        lambda h: h["entries"].pop(),
        lambda h: h["entries"][0]["outcome"].update(upper=[0, 1]),
    ):
        history = copy.deepcopy(source["environmental_attempt_history"])
        mutation(history)
        rejected(lambda history=history: M.NativeRunner(history))
        guards += 1
    # No patched reconstruction/cache: each mode performs one complete fresh
    # primitive rebuild before rejecting its independently resealed false report.
    bad = copy.deepcopy(source)
    if sys.flags.optimize:
        attack = "invented complete-cover count"
        bad["records"][25]["jet_tiers"][-1]["outer_scalar_bound"]["fixed_cover"][
            "finite_cells"
        ] = 255
    else:
        attack = "promote unresolved same-point case to impossible"
        bad["postresult_necessary_bound"]["records"][18]["ratios"][3][
            "criterion_impossible"
        ] = True
    bad.pop("payload_sha256")
    bad["payload_sha256"] = M.oa.digest(M.canonical(bad))
    start = time.monotonic()
    rejected(lambda: M.check_report(bad))
    print(
        json.dumps(
            {
                "mode": "optimized" if sys.flags.optimize else "normal",
                "strict_guards_rejected": guards,
                "fresh_resealed_attack": attack,
                "accepted": False,
                "elapsed_seconds": round(time.monotonic() - start, 3),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
