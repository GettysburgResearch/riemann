#!/usr/bin/env python3
"""Refine certified Hardy-Z sign-chain bins by exact-dyadic bisection.

Requires python-flint. Every retained step is a directed Hardy-Z interval that
excludes zero. Unresolved midpoint balls are never assigned a sign.
"""
from __future__ import annotations
import argparse
import copy
import importlib.util
import json
import multiprocessing as multiprocessing
import platform
import sys
import time
from fractions import Fraction
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "verify_sign_chain", HERE / "verify_sign_chain.py"
)
CHECKER = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = CHECKER
SPEC.loader.exec_module(CHECKER)


def is_dyadic(value: Fraction) -> bool:
    denominator = value.denominator
    return denominator > 0 and denominator & (denominator - 1) == 0


def fraction_from_exact_arb(value: Any) -> Fraction:
    mantissa, exponent = value.man_exp()
    mantissa = int(mantissa)
    exponent = int(exponent)
    if exponent >= 0:
        return Fraction(mantissa << exponent, 1)
    return Fraction(mantissa, 1 << (-exponent))


def fj(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def ij(lower: Fraction, upper: Fraction) -> dict[str, dict[str, int]]:
    return {"lower": fj(lower), "upper": fj(upper)}


def evaluate_one(
    task: tuple[int, int, int, tuple[int, ...]]
) -> dict[str, Any]:
    bin_index, numerator, denominator, ladder = task
    from flint import acb, arb, ctx

    required_bits = max(64, abs(numerator).bit_length() + 20)
    last_unresolved: Any = None
    for requested_precision in ladder:
        precision = max(requested_precision, required_bits)
        ctx.prec = precision
        ordinate = arb(numerator) / arb(denominator)
        if not ordinate.is_exact():
            last_unresolved = f"inexact dyadic at {precision} bits"
            continue
        theta = (
            acb(arb(1) / 4, ordinate / 2).lgamma().imag
            - (ordinate / 2) * arb.pi().log()
        )
        z_value = (
            acb(0, theta).exp() * acb(arb(1) / 2, ordinate).zeta()
        ).real
        lower = fraction_from_exact_arb(z_value.lower())
        upper = fraction_from_exact_arb(z_value.upper())
        exact_ordinate = Fraction(numerator, denominator)
        if lower > 0:
            return {
                "bin_index": bin_index,
                "t": fj(exact_ordinate),
                "z_interval": ij(lower, upper),
                "sign": 1,
                "precision_bits": precision,
            }
        if upper < 0:
            return {
                "bin_index": bin_index,
                "t": fj(exact_ordinate),
                "z_interval": ij(lower, upper),
                "sign": -1,
                "precision_bits": precision,
            }
        last_unresolved = {
            "lower": str(lower),
            "upper": str(upper),
            "precision_bits": precision,
        }
    return {
        "bin_index": bin_index,
        "t": fj(Fraction(numerator, denominator)),
        "unresolved": last_unresolved,
    }


def parse_selected_bins(text: str, total_count: int) -> set[int]:
    if text == "all":
        return set(range(total_count))
    selected: set[int] = set()
    for piece in text.split(","):
        piece = piece.strip()
        if not piece:
            continue
        index = int(piece)
        if index < 0 or index >= total_count:
            raise ValueError(f"bin index {index} lies outside [0,{total_count})")
        selected.add(index)
    if not selected:
        raise ValueError("no bins selected")
    return selected


def state_from_verification(verification: dict[str, Any]) -> dict[int, dict[str, Any]]:
    output: dict[int, dict[str, Any]] = {}
    for row in verification["bins"]:
        output[row["bin_index"]] = {
            "lower": CHECKER.rat(row["lower"], "lower"),
            "upper": CHECKER.rat(row["upper"], "upper"),
            "lower_sign": row["lower_sign"],
            "upper_sign": row["upper_sign"],
        }
    return output


def refinement_map(data: dict[str, Any]) -> dict[int, dict[str, Any]]:
    output: dict[int, dict[str, Any]] = {}
    for item in data.setdefault("refinements", []):
        output[item["bin_index"]] = item
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--bins", default="all")
    parser.add_argument("--rounds", type=int, default=8)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--precision-ladder", default="96,160,256,448")
    args = parser.parse_args()

    if args.rounds < 1 or args.workers < 1:
        raise SystemExit("rounds and workers must be positive")
    ladder = tuple(
        sorted(
            {
                int(piece)
                for piece in args.precision_ladder.split(",")
                if piece.strip()
            }
        )
    )
    if not ladder or ladder[0] < 64:
        raise SystemExit("precision ladder must begin at 64 bits or more")

    data = json.loads(args.certificate.read_text())
    verification = CHECKER.verify(copy.deepcopy(data))
    total_count = verification["total_count"]
    selected = parse_selected_bins(args.bins, total_count)
    states = state_from_verification(verification)
    refinements = refinement_map(data)
    for index in selected:
        refinements.setdefault(index, {"bin_index": index, "steps": []})

    unresolved: list[dict[str, Any]] = []
    precision_histogram: dict[str, int] = {}
    started = time.time()
    with multiprocessing.Pool(args.workers) as pool:
        active = set(selected)
        for round_index in range(args.rounds):
            tasks = []
            for index in sorted(active):
                state = states[index]
                midpoint = (state["lower"] + state["upper"]) / 2
                if not is_dyadic(midpoint):
                    raise RuntimeError("internal midpoint is not dyadic")
                tasks.append(
                    (
                        index,
                        midpoint.numerator,
                        midpoint.denominator,
                        ladder,
                    )
                )
            results = list(pool.imap_unordered(evaluate_one, tasks, chunksize=1))
            next_active: set[int] = set()
            for result in results:
                index = result["bin_index"]
                if "unresolved" in result:
                    unresolved.append({"round": round_index, **result})
                    continue
                precision_key = str(result["precision_bits"])
                precision_histogram[precision_key] = (
                    precision_histogram.get(precision_key, 0) + 1
                )
                refinements[index]["steps"].append(
                    {
                        "t": result["t"],
                        "z_interval": result["z_interval"],
                        "producer_precision_bits": result["precision_bits"],
                    }
                )
                ordinate = CHECKER.rat(result["t"], "refinement.t")
                midpoint_sign = result["sign"]
                state = states[index]
                if midpoint_sign == state["lower_sign"]:
                    state["lower"] = ordinate
                elif midpoint_sign == state["upper_sign"]:
                    state["upper"] = ordinate
                else:
                    raise RuntimeError(
                        "certified midpoint sign matches neither endpoint"
                    )
                if state["lower_sign"] == state["upper_sign"]:
                    raise RuntimeError("lost endpoint sign alternation")
                next_active.add(index)
            active = next_active
            print(
                json.dumps(
                    {
                        "round": round_index + 1,
                        "active": len(active),
                        "unresolved_total": len(unresolved),
                        "elapsed_seconds": time.time() - started,
                    }
                ),
                flush=True,
            )
            if not active:
                break

    data["refinements"] = sorted(
        refinements.values(), key=lambda item: item["bin_index"]
    )
    data["refinement_producer"] = {
        "name": "refine_hardy_z_bins.py",
        "python": platform.python_version(),
        "precision_ladder": list(ladder),
        "rounds_requested": args.rounds,
        "selected_bins": sorted(selected),
        "precision_histogram": precision_histogram,
        "unresolved_midpoints": unresolved,
        "elapsed_seconds": time.time() - started,
    }
    final_verification = CHECKER.verify(copy.deepcopy(data))
    maximum_width = max(
        (
            CHECKER.rat(row["width"], "width")
            for row in final_verification["bins"]
        ),
        default=Fraction(0),
    )
    data["refinement_verification"] = {
        "verdict": final_verification["verdict"],
        "certificate_sha256": final_verification["certificate_sha256"],
        "maximum_width": str(maximum_width),
    }
    args.output.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "verdict": final_verification["verdict"],
                "output": str(args.output),
                "unresolved": len(unresolved),
            },
            indent=2,
        )
    )
    return 0 if not unresolved else 1


if __name__ == "__main__":
    raise SystemExit(main())
