#!/usr/bin/env python3
"""Exact finite replay of the moving active-prime compensator.

All source coefficients come from ordered old input pairs. This independently
constructs the harmonic renormalization and compares the complete reduced
denominator source to its rectangular/square expression, including changing
prime endpoints. No finite check proves the asymptotic norm theorem.
"""
import argparse
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import json
import subprocess
import sys

import verify as v


COUNTS = Counter()
MUTATION = "none"
MUTATIONS = ("freeze_middle_support", "omit_renormalization",
             "replace_incidence_by_owner", "drop_shared_square",
             "admit_empty_active_cell", "erase_exceptional_prime_cost",
             "lower_annular_cutoff")


def need(ok, gate):
    COUNTS[gate] += 1
    if not ok:
        raise RuntimeError("REJECT:" + gate)


def integer_root(n, degree):
    lo, hi = 0, 1
    while hi ** degree <= n:
        hi *= 2
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid ** degree <= n:
            lo = mid
        else:
            hi = mid
    return lo


def cutoff(y, k):
    x = y + 1
    while 2 * x <= k:
        x *= 2
    return integer_root(x ** 13, 24)


def divisor_three(n):
    out = 1
    for _, e in v.factors(n):
        out *= (e + 1) * (e + 2) // 2
    return out


def run():
    ys = [24, 32, 48, 64, 96, 128]
    v.prepare_harmonics((max(ys) + 1) ** 2)
    cases = []
    budget = F(1) if MUTATION == "erase_exceptional_prime_cost" else F(35, 27)
    for n in range(1, 2001):
        if any(e > 2 for _, e in v.factors(n)):
            continue
        acore = F(1)
        for p, e in v.factors(n):
            if e == 1:
                acore *= 2 + F(1, p)
        sigma = sum(v.divisors(n))
        need(acore * F(sigma, n) <= budget * divisor_three(n),
             "complete_exceptional_prime_cost")
    for y in ys:
        _, c = v.source(y)
        primes = [p for p in range(2, y + 1) if v.factors(p) == ((p, 1),)]
        p1 = [p for p in primes if 2 * p > y]
        p2 = [p for p in primes if 3 * p > y and 2 * p <= y]
        h1 = sum((F(1, p) for p in p1), F(0))
        static_h2 = sum((F(1, p) for p in p2), F(0))
        need(bool(p1) and bool(p2), "two_nonempty_strata")
        start, stop = max(2 * y, (y * y + 31) // 32), y * p2[-1]
        if y <= 32:
            cells = list(range(start, stop))
        else:
            cells = sorted({start, start + 1, (start + stop) // 2, stop - 2, stop - 1,
                            *(p * y + e for p in p2 for e in (-1, 0, 1)
                              if start <= p * y + e < stop),
                            *(k for k in v.sample_cells(y, False) if start <= k < stop)})
        if MUTATION == "admit_empty_active_cell":
            cells.append(stop)
        max_lam = F(0)
        for k in cells:
            active = [p for p in p2 if p * y > k]
            if MUTATION == "freeze_middle_support":
                active = p2
            h2 = sum((F(1, p) for p in active), F(0))
            need(h2 > 0, "active_stratum_nonempty")
            lam = -2 * h1 / (static_h2 if MUTATION == "omit_renormalization" else h2)
            max_lam = max(max_lam, abs(lam))
            w = {p: F(1) for p in p1}
            w.update({p: lam for p in active})
            need(all(p * y > k for p in w), "complete_cell_active_support")
            need(h1 + lam * h2 / 2 == 0, "moving_common_profile")
            need(sum((abs(wp) / p for p, wp in w.items()), F(0)) == 3 * h1,
                 "harmonic_mass_budget")
            need(sum((abs(wp) / (p * p) for p, wp in w.items()), F(0)) <= 9 * h1 / y,
                 "square_correction_pointwise_resource")
            for i, p in enumerate(p1):
                for ell in p1[i + 1:]:
                    omega = sum((wp for prime, wp in w.items() if p * ell % prime == 0), F(0))
                    if MUTATION == "replace_incidence_by_owner":
                        omega = F(1)
                    need(omega == 2, "all_target_pairs_retained")
            direct = v.weighted_direct(y, k, c, w)
            c1 = sum((v.log_int(p) * (wp * v.mobius_prefix(y // p) / p)
                      + v.log_prefix(y // p) * (wp / p)
                      for p, wp in w.items()), v.Linear())
            rhs = -c1 * (2 * v.mobius_prefix(y))
            # This combination is independent of the moving active set.
            rhs += (v.T(y, k, 2) - v.T(y, k)) * (2 * h1)
            for p, wp in w.items():
                j = y // p
                rhs += (-v.Z(j, k, p * p) + 2 * v.Z(j, k, p) - v.Z(j, k)) \
                    * (wp / (p * p))
            need(direct == rhs, "complete_moving_source_identity")
            qmax = cutoff(y, k)
            if MUTATION == "lower_annular_cutoff":
                qmax -= 1
            annular_x = 2 ** ((k // (y + 1)).bit_length() - 1) * (y + 1)
            need(annular_x <= k < 2 * annular_x, "exact_native_annulus")
            need(qmax ** 24 <= annular_x ** 13, "annular_cutoff_lower")
            need((qmax + 1) ** 24 > annular_x ** 13, "annular_cutoff_upper")
            low, highcore, small = v.Linear(), v.Linear(), v.Linear()
            for q, cq in c.items():
                if q == 1:
                    continue
                omega = sum((wp for p, wp in w.items() if q % p == 0), F(0))
                if not omega:
                    continue
                term = v.mode(q, k) * (omega * cq)
                if q <= qmax:
                    low += term
                    selected = [p for p in w if q % p == 0]
                    if qmax < F(y * y, 9):
                        need(len(selected) == 1 and q % (selected[0] ** 2) != 0,
                             "complete_low_denominator_incidence")
                elif v.core(q) < F(y, 3):
                    small += term
                    selected = [p for p in w if q % (p * p) == 0]
                    need(len(selected) == 1, "small_core_unique_squared_prime")
                    p = selected[0]
                    expected = ({1: F(1, p * p)} if y // p == 1 else
                                {1: F(1, 4 * p * p), 2: F(-3, 4 * p * p),
                                 4: F(1, 4 * p * p)})
                    if MUTATION == "drop_shared_square":
                        expected.pop(2, None)
                    need(q // (p * p) in expected and expected[q // (p * p)] == cq,
                         "all_shared_square_coefficients")
                else:
                    highcore += term
            need(direct == low + small + highcore, "complete_mask_partition")
        cases.append({"Y": y, "physical_window": [start, stop - 1],
                      "checked_cells": len(cells), "all_window_cells": y <= 32,
                      "all_support_change_endpoints_checked": True,
                      "maximum_middle_weight": {"num": max_lam.numerator,
                                                "den": max_lam.denominator}})
    return {"status": "PASS", "arithmetic": "EXACT_RATIONAL_AND_FORMAL_LOGARITHMS",
            "cases": cases, "checks_by_gate": dict(sorted(COUNTS.items())),
            "total_checks_including_guards": sum(COUNTS.values()),
            "not_checked": ["infinite norm inequalities", "PNT", "full rough-core bound", "RH"]}


def main():
    global MUTATION
    p = argparse.ArgumentParser()
    p.add_argument("--mutate", choices=("none",) + MUTATIONS, default="none")
    p.add_argument("--mutations", action="store_true")
    p.add_argument("--report", type=Path)
    a = p.parse_args()
    MUTATION = a.mutate
    report = run()
    if a.mutations:
        rows = []
        for mutation in MUTATIONS:
            r = subprocess.run([sys.executable, "-B", "-O", str(Path(__file__).resolve()),
                                "--mutate", mutation], capture_output=True, text=True)
            need(r.returncode != 0 and "REJECT:" in r.stderr, "mutation_rejected")
            rows.append({"mutation": mutation, "status": "REJECTED",
                         "gate": r.stderr.rsplit("REJECT:", 1)[-1].splitlines()[0]})
        report["mutations"] = rows
    encoded = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if a.report:
        a.report.write_text(encoded, encoding="utf-8", newline="\n")
    print(encoded, end="")


if __name__ == "__main__":
    main()
