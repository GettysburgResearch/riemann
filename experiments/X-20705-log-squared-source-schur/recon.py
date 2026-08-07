#!/usr/bin/env python3
"""Nondirected source-canonical Schur reconnaissance on c_j=ceil(exp(j)), N_j=j^2.

Loads the complete D-0001 polar/archimedean/prime-power assembly from X-20704.
This script is a high-precision scheduler only; it does not make directed signs.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import math
from pathlib import Path

import mpmath as mp


def load_x20704(path: Path):
    spec = importlib.util.spec_from_file_location("x20704_recon", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def even_unnormalized(full, nmax: int):
    dimension = 2 * nmax + 1
    transform = mp.matrix(dimension, nmax + 1)
    transform[nmax, 0] = 1
    for n in range(1, nmax + 1):
        transform[nmax - n, n] = 1
        transform[nmax + n, n] = 1
    return transform.T * full * transform


def source_schur(module, c: int, nmax: int):
    full, prime_power_count = module.full_matrix(c, nmax)
    operator = even_unnormalized(full, nmax)
    source = mp.matrix([1] * (nmax + 1))
    complement = mp.matrix(nmax + 1, nmax)
    for k in range(nmax):
        complement[0, k] = -2
        complement[k + 1, k] = 1
    block = complement.T * operator * complement
    cross = complement.T * operator * source
    solve = mp.lu_solve(block, cross)
    raw = (source.T * operator * source)[0]
    schur = raw - (cross.T * solve)[0]
    quotient = schur / (1 + 2 * nmax)
    eigenvalues = mp.eigsy(block, eigvals_only=True)
    return quotient, eigenvalues[0], prime_power_count


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--digits", type=int, default=180)
    parser.add_argument("--j-min", type=int, default=2)
    parser.add_argument("--j-max", type=int, default=6)
    parser.add_argument("--x20704", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.j_min < 2 or args.j_max < args.j_min:
        raise SystemExit("invalid j range")
    mp.mp.dps = args.digits
    module = load_x20704(args.x20704)
    levels = []
    for j in range(args.j_min, args.j_max + 1):
        c = math.ceil(math.exp(j))
        nmax = j * j
        quotient, complement_min, prime_power_count = source_schur(module, c, nmax)
        levels.append({
            "j": j,
            "c": c,
            "N": nmax,
            "prime_power_count": prime_power_count,
            "source_schur_quotient": mp.nstr(quotient, 70),
            "log_c_times_quotient": mp.nstr(mp.log(c) * quotient, 70),
            "complement_min_eigenvalue": mp.nstr(complement_min, 60),
        })
    result = {
        "schema": "riemann.x20705.log-squared-source-schur-recon.v1",
        "classification": "NON_DIRECTED_HIGH_PRECISION_RECONNAISSANCE",
        "digits": args.digits,
        "schedule": "c_j=ceil(exp(j)), N_j=j^2",
        "operator": "complete D-0001 polar + cutoff-free archimedean + every prime power q<=c",
        "levels": levels,
        "proof_boundary": (
            "All values are ordinary mpmath approximations. They nominate an explicit "
            "unbounded schedule and directed LDL targets, but prove neither positivity "
            "nor a cofinal lower bound."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
