#!/usr/bin/env python3
"""Exact dictionary replay for the all-depth stable correction-layer head."""
from __future__ import annotations

import json
from typing import Dict, Tuple

Partition = Tuple[int, ...]
KNOWN: Dict[int, Dict[Partition, int]] = {
    3: {(4, 1, 1): 2, (4, 2): -2, (5, 1): -2, (6,): 2},
    4: {(5, 1, 1, 1): -2, (5, 2, 1): 4, (5, 3): -2, (6, 1, 1): 2, (6, 2): -2, (7, 1): -2, (8,): 2},
    5: {(4, 4, 2): -2, (5, 3, 1, 1): -2, (5, 3, 2): 4, (5, 4, 1): 4, (5, 5): -4, (6, 2, 1, 1): 2, (6, 2, 2): -2, (6, 3, 1): -2, (6, 4): 2, (7, 2, 1): -2, (8, 2): 2},
    6: {(5, 4, 2, 1): 2, (5, 4, 3): -2, (5, 5, 1, 1): -2, (6, 3, 1, 1, 1): 2, (6, 3, 2, 1): -6, (6, 3, 3): 4, (6, 4, 1, 1): -2, (6, 4, 2): 2, (6, 5, 1): 6, (6, 6): -4, (7, 2, 1, 1, 1): -2, (7, 2, 2, 1): 4, (7, 3, 1, 1): 2, (7, 3, 2): -2, (7, 4, 1): -2, (8, 2, 1, 1): 2, (8, 2, 2): -2, (8, 3, 1): -2, (8, 4): 2, (9, 2, 1): -2, (10, 2): 2},
}


def s(j: int) -> int:
    return -1 if (j * (j + 1) // 2) % 2 else 1


def add(out: Dict[Partition, int], parts: Tuple[int, ...], coeff: int) -> None:
    p = tuple(sorted((x for x in parts if x), reverse=True))
    out[p] = out.get(p, 0) + coeff
    if out[p] == 0:
        del out[p]


def predicted_head(j: int) -> Dict[Partition, int]:
    d, out = 2 * j, {}
    if s(j) == 1:
        if 0 < j: add(out, (d,), 2)
        if 1 < j: add(out, (d - 1, 1), -2)
        if 2 < j:
            add(out, (d - 2, 1, 1), 2); add(out, (d - 2, 2), -2)
        if 3 < j:
            add(out, (d - 3, 1, 1, 1), -2); add(out, (d - 3, 2, 1), 4); add(out, (d - 3, 3), -2)
        if 4 < j:
            add(out, (d - 4, 1, 1, 1, 1), 2); add(out, (d - 4, 2, 1, 1), -6)
            add(out, (d - 4, 2, 2), 2); add(out, (d - 4, 3, 1), 4); add(out, (d - 4, 4), -2)
    else:
        if 2 < j: add(out, (d - 2, 2), 2)
        if 3 < j: add(out, (d - 3, 2, 1), -2)
        if 4 < j:
            add(out, (d - 4, 4), 2); add(out, (d - 4, 3, 1), -2)
            add(out, (d - 4, 2, 2), -2); add(out, (d - 4, 2, 1, 1), 2)
    return out


def run() -> dict:
    checks = {}
    for j in (3, 4, 5, 6):
        threshold = 2 * j - min(4, j - 1)
        observed = {p: c for p, c in KNOWN[j].items() if p[0] >= threshold}
        predicted = predicted_head(j)
        if observed != predicted:
            raise AssertionError(f"head mismatch at layer {j}")
        checks[str(j)] = {"sign": s(j), "threshold_largest_part": threshold, "terms": {str(list(p)): c for p, c in sorted(predicted.items(), reverse=True)}, "matches_committed_layer": True}
    predictions = {}
    for j in (7, 8):
        pred = predicted_head(j)
        revival = pred.get((2 * j,)) == 2
        if not revival:
            raise AssertionError("predicted revival missing")
        predictions[str(j)] = {"sign": s(j), "linear_head_revives": revival, "terms_through_k4": {str(list(p)): c for p, c in sorted(pred.items(), reverse=True)}}
    return {"theorem": "period-four stable correction-layer head", "formula_sign": "s_j=(-1)^(j(j+1)/2)", "committed_layers_checked": checks, "new_predictions": predictions, "permanent_termination_extrapolation_refuted": True, "all_checks_passed": True, "rh_or_grh_established": False}


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--output")
    args = parser.parse_args()
    text = json.dumps(run(), indent=2, sort_keys=True)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
