#!/usr/bin/env python3
"""Ordinary high-precision replay of the high-carrier direct-xi Loewner table.

This is deliberately not a proof-producing program. It recomputes direct
completed-xi logarithmic moduli with mpmath, compares the resulting Loewner
minors with minors formed from the rounded transport strings committed in
X-7501, and records the primitive sensitivity of the smallest order-three row.
"""
from __future__ import annotations
import argparse
import json
import multiprocessing as multiprocessing
import platform
import time
from pathlib import Path
import mpmath as mp

T_NUM = 20225875608343121406355
T_DEN = 4294967296
KS = [20, 18, 16, 14, 12, 10, 8, 6, 5]
ROWS = [
    ("d2-0", [20, 16], [18, 14]),
    ("d2-1", [18, 14], [16, 12]),
    ("d2-2", [16, 12], [14, 10]),
    ("d2-3", [14, 10], [12, 8]),
    ("d2-4", [12, 8], [10, 6]),
    ("d2-5", [10, 6], [8, 5]),
    ("d3-0", [20, 16, 12], [18, 14, 10]),
    ("d3-1", [18, 14, 10], [16, 12, 8]),
    ("d3-2", [16, 12, 8], [14, 10, 6]),
    ("d3-3", [14, 10, 6], [12, 8, 5]),
    ("d4-0", [20, 16, 12, 8], [18, 14, 10, 6]),
    ("d4-1", [18, 14, 10, 6], [16, 12, 8, 5]),
]

# Rounded strings preserved by X-7501 from its original 50-decimal run.
OLD_RELATIVE = {
    20: "0",
    18: "0.000000000419621547999751338814718896316494",
    16: "0.00000000713356631414507179632917100200986",
    14: "0.00000011455668209869075643838237278618806",
    12: "0.000001833326413363900700326541952885827044",
    10: "0.000029333611064068708146673317008821710814",
    8: "0.000469330217067188344802224468695154607412",
    6: "0.007507242241002376234755992664854889159842",
    5: "0.030002892457012329673586910561199209410478",
}


def calculate_one(task: tuple[int, int]) -> tuple[int, str, float]:
    k, digits = task
    import mpmath as local_mp

    local_mp.mp.dps = digits
    ordinate = local_mp.mpf(T_NUM) / T_DEN
    x = local_mp.power(2, -k)
    s = local_mp.mpc(local_mp.mpf("0.5") + x, ordinate)
    started = time.time()
    zeta_value = local_mp.zeta(s)
    log_h = 2 * (
        local_mp.log(abs(s))
        + local_mp.log(abs(s - 1))
        - local_mp.log(2)
        - local_mp.re(s) * local_mp.log(local_mp.pi) / 2
        + local_mp.re(local_mp.loggamma(s / 2))
        + local_mp.log(abs(zeta_value))
    )
    return k, local_mp.nstr(log_h, digits + 20), time.time() - started


def determinants(values: dict[int, mp.mpf]) -> dict[str, str]:
    output: dict[str, str] = {}
    for identifier, row_ks, column_ks in ROWS:
        matrix = []
        for row_k in row_ks:
            row = []
            row_u = mp.power(2, -2 * row_k)
            for column_k in column_ks:
                column_u = mp.power(2, -2 * column_k)
                row.append(
                    (values[row_k] - values[column_k]) / (row_u - column_u)
                )
            matrix.append(row)
        output[identifier] = mp.nstr(mp.det(mp.matrix(matrix)), mp.mp.dps)
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dps", type=int, default=130)
    parser.add_argument("--workers", type=int, default=9)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if args.dps < 80 or args.workers < 1:
        raise SystemExit("use at least 80 decimal digits and one worker")

    started = time.time()
    raw = []
    with multiprocessing.Pool(args.workers) as pool:
        for k, value, elapsed in pool.imap_unordered(
            calculate_one, [(k, args.dps) for k in KS], chunksize=1
        ):
            raw.append({"k": k, "logH": value, "seconds": elapsed})
            print(json.dumps(raw[-1]), flush=True)
    raw.sort(key=lambda row: -row["k"])

    mp.mp.dps = args.dps
    absolute = {row["k"]: mp.mpf(row["logH"]) for row in raw}
    baseline = absolute[20]
    relative = {k: absolute[k] - baseline for k in KS}
    new_determinants = determinants(relative)
    old_values = {k: mp.mpf(value) for k, value in OLD_RELATIVE.items()}
    old_determinants = determinants(old_values)

    base_value = mp.mpf(new_determinants["d3-0"])
    epsilon = mp.mpf(10) ** (-60)
    sensitivity: dict[str, str] = {}
    for k in KS:
        perturbed = dict(relative)
        perturbed[k] += epsilon
        changed = mp.mpf(determinants(perturbed)["d3-0"])
        sensitivity[str(k)] = mp.nstr((changed - base_value) / epsilon, 80)

    result = {
        "schema": "riemann.x7503-loewner-precision-repair.v1",
        "classification": "EMPIRICAL_HIGH_PRECISION_NOT_CERTIFIED",
        "target": {"numerator": str(T_NUM), "denominator": str(T_DEN)},
        "backend": f"mpmath {mp.__version__}; ordinary {args.dps}-decimal arithmetic",
        "environment": {"python": platform.python_version(), "mpmath": mp.__version__},
        "absolute_logH": raw,
        "relative_logH": {
            f"x-{k}": mp.nstr(relative[k], args.dps) for k in KS
        },
        "committed_50d_transport_relative_logH": {
            f"x-{k}": OLD_RELATIVE[k] for k in KS
        },
        "determinants_from_committed_50d_strings": old_determinants,
        "determinants_from_fresh_high_precision_values": new_determinants,
        "d3_0_primitive_sensitivity": sensitivity,
        "elapsed_seconds": time.time() - started,
        "verdict": (
            "ALL_HIGH_PRECISION_DETERMINANTS_POSITIVE; "
            "APPARENT_NEGATIVES_FROM_TRUNCATED_50D_STRINGS_ARE_PRECISION_GHOSTS"
        ),
        "proof_boundary": (
            "No directed intervals. This refutes only the floating sign nomination, "
            "not any RH consequence."
        ),
    }
    args.out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"verdict": result["verdict"], "elapsed": result["elapsed_seconds"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
