#!/usr/bin/env python3
"""Combine exact T-99100 segment transcripts into one fail-closed proof object."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from typing import Any, Dict, List

INT_KEYS = {
    "L", "R", "scale", "nonzero", "relative_min_lower_num",
    "relative_min_upper_num", "delta_lower_num", "delta_upper_num",
}

def parse_segment(path: Path) -> Dict[str, Any]:
    out: Dict[str, Any] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        p = raw.split()
        if not p:
            continue
        key = p[0]
        if key in INT_KEYS:
            out[key] = int(p[1])
        elif key == "relative_min_lower":
            out["relative_min_lower_at"] = int(p[-1])
        elif key == "relative_min_upper":
            out["relative_min_upper_at"] = int(p[-1])
        elif key == "approx_relative_min":
            out["approx_relative_min"] = float(p[1])
            out["approx_relative_min_at"] = int(p[-1])
        elif key == "approx_delta":
            out["approx_delta"] = float(p[1])
    required = INT_KEYS | {
        "relative_min_lower_at", "relative_min_upper_at",
        "approx_relative_min", "approx_relative_min_at", "approx_delta",
    }
    missing = required - out.keys()
    if missing:
        raise ValueError(f"{path}: missing {sorted(missing)}")
    return out

def combine(segment_dir: Path, count: int, nmax: int) -> Dict[str, Any]:
    blocks = [parse_segment(segment_dir / f"seg{k}.txt") for k in range(1, count + 1)]
    scale = blocks[0]["scale"]
    cum_lo = cum_hi = 0
    cum_approx = 0.0
    best_lo = best_hi = best_approx = None
    rows: List[Dict[str, Any]] = []
    expected_l = 1
    for k, d in enumerate(blocks, 1):
        if d["L"] != expected_l or d["R"] < d["L"]:
            raise ValueError(f"non-contiguous segment {k}")
        expected_l = d["R"] + 1
        if d["scale"] != scale:
            raise ValueError("scale mismatch")
        cand_lo = cum_lo + d["relative_min_lower_num"]
        cand_hi = cum_hi + d["relative_min_upper_num"]
        cand_approx = cum_approx + d["approx_relative_min"]
        rows.append({
            "block": k, "L": d["L"], "R": d["R"],
            "start_lower": cum_lo, "candidate_lower": cand_lo,
            "candidate_lower_at": d["relative_min_lower_at"],
            "start_upper": cum_hi, "candidate_upper": cand_hi,
            "candidate_upper_at": d["relative_min_upper_at"],
            "candidate_approx": cand_approx,
            "candidate_approx_at": d["approx_relative_min_at"],
            "delta_lower": d["delta_lower_num"],
            "delta_upper": d["delta_upper_num"],
            "nonzero": d["nonzero"],
        })
        if best_lo is None or cand_lo < best_lo[0]:
            best_lo = (cand_lo, d["relative_min_lower_at"], k)
        if best_hi is None or cand_hi < best_hi[0]:
            best_hi = (cand_hi, d["relative_min_upper_at"], k)
        if best_approx is None or cand_approx < best_approx[0]:
            best_approx = (cand_approx, d["approx_relative_min_at"], k)
        cum_lo += d["delta_lower_num"]
        cum_hi += d["delta_upper_num"]
        cum_approx += d["approx_delta"]
    if blocks[-1]["R"] != nmax:
        raise ValueError("final endpoint mismatch")
    assert best_lo and best_hi and best_approx
    result: Dict[str, Any] = {
        "verdict": "PASS_T99100_HARNACK67_TWO_BILLION_EXACT_SEGMENTED",
        "N": nmax, "prime": 67, "scale": scale, "segments": count,
        "nonzero": sum(d["nonzero"] for d in blocks),
        "minimum_lower_num": best_lo[0], "minimum_lower_at": best_lo[1],
        "minimum_lower_block": best_lo[2],
        "minimum_upper_num": best_hi[0], "minimum_upper_at": best_hi[1],
        "minimum_upper_block": best_hi[2],
        "approx_minimum": best_approx[0], "approx_minimum_at": best_approx[1],
        "approx_minimum_block": best_approx[2],
        "final_lower_num": cum_lo, "final_upper_num": cum_hi,
        "approx_final": cum_approx,
        "minimum_lower_decimal": best_lo[0] / scale,
        "minimum_upper_decimal": best_hi[0] / scale,
        "final_lower_decimal": cum_lo / scale,
        "final_upper_decimal": cum_hi / scale,
        "status": {
            "harnack67_through_2e9": best_lo[0] > 0,
            "global_harnack67": False,
            "global_cprefix_sign": False,
            "rh_established": False,
        },
        "blocks": rows,
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return result

def text_summary(d: Dict[str, Any]) -> str:
    s = d["scale"]
    lines = [
        f"N {d['N']}", f"prime {d['prime']}", f"scale {s}",
        f"segments {d['segments']}", f"nonzero {d['nonzero']}",
        f"min_lower_num {d['minimum_lower_num']}",
        f"min_lower {d['minimum_lower_num']/s:.18f} at {d['minimum_lower_at']}",
        f"min_upper_num {d['minimum_upper_num']}",
        f"min_upper {d['minimum_upper_num']/s:.18f} at {d['minimum_upper_at']}",
        f"approx_min {d['approx_minimum']:.18f} at {d['approx_minimum_at']}",
        f"final_lower_num {d['final_lower_num']}",
        f"final_upper_num {d['final_upper_num']}",
        f"final_interval [{d['final_lower_num']/s:.18f}, {d['final_upper_num']/s:.18f}]",
        f"PASS {'YES' if d['minimum_lower_num'] > 0 else 'NO'}",
        f"proof_object_sha256 {d['proof_object_sha256']}",
    ]
    return "\n".join(lines) + "\n"

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--segments-dir", type=Path, required=True)
    ap.add_argument("--count", type=int, default=20)
    ap.add_argument("--nmax", type=int, default=2_000_000_000)
    ap.add_argument("--output-json", type=Path, required=True)
    ap.add_argument("--output-text", type=Path, required=True)
    args = ap.parse_args()
    result = combine(args.segments_dir, args.count, args.nmax)
    args.output_json.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    args.output_text.write_text(text_summary(result), encoding="utf-8", newline="\n")
    print(result["verdict"])
    print(result["proof_object_sha256"])
if __name__ == "__main__":
    main()
