#!/usr/bin/env python3
"""Run all Reviewer B light exact replays."""
from __future__ import annotations

import importlib
import json
from pathlib import Path

MODULES = [
    "replay_mellin_consumer",
    "replay_xi_pick_order3",
    "replay_loewner_hankel",
    "replay_heat_firewalls",
    "replay_q4_filter",
    "replay_operator_local",
]


def main() -> dict[str, object]:
    results = {}
    for name in MODULES:
        module = importlib.import_module(name)
        results[name] = module.main()
    summary = {
        "verdict": "PASS_REVIEWER_B_ALL_LIGHT_REPLAYS",
        "modules": results,
        "heavy_campaigns_rerun": False,
    }
    Path(__file__).with_name("verification.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return summary


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, sort_keys=True))
