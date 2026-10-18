#!/usr/bin/env python3
"""Independent exact check of cross-stratum compensation and its transition.

Imports only the primitive rational/log arithmetic and literal source from
verify.py. The compensator and rectangular continuation are constructed here.
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
MUTATIONS = ("drop_middle_stratum", "drop_transition_defect",
             "drop_shared_two", "drop_square_four", "replace_with_deletion")


def need(value, gate):
    COUNTS[gate] += 1
    if not value:
        raise RuntimeError("REJECT:" + gate)


def run():
    ys = [24, 32, 48, 64, 80, 96]
    v.prepare_harmonics((max(ys) + 1) ** 2)
    cases = []
    for y in ys:
        z, c = v.source(y)
        primes = [p for p in range(2, y + 1) if v.factors(p) == ((p, 1),)]
        p1 = [p for p in primes if 2 * p > y]
        p2 = [p for p in primes if 3 * p > y and 2 * p <= y]
        h1 = sum((F(1, p) for p in p1), F(0))
        h2 = sum((F(1, p) for p in p2), F(0))
        need(h2 > 0, "middle_stratum_nonempty")
        lam = -2 * h1 / h2
        if MUTATION == "drop_middle_stratum":
            lam = F(0)
        w = {p: F(1) for p in p1}
        w.update({p: lam for p in p2})
        need(h1 + lam * h2 / 2 == 0, "cross_stratum_common_profile")
        c1 = sum((v.log_int(p) * (wp * v.mobius_prefix(y // p) / p)
                  + v.log_prefix(y // p) * (wp / p)
                  for p, wp in w.items()), v.Linear())
        c1_alt = sum((v.log_int(p) * F(1, p) for p in p1), v.Linear()) \
            - sum((v.log_int(p) * F(h1, h2 * p) for p in p2), v.Linear()) \
            + v.log_int(2) * h1
        need(c1 == c1_alt, "logarithmic_profile_identity")
        allowed_small = set()
        for p in p1:
            need(c.get(p * p) == F(1, p * p), "top_square_coefficient")
            allowed_small.add(p * p)
        for p in p2:
            need(c.get(p * p) == F(1, 4 * p * p), "middle_square_coefficient")
            expected_two = F(0) if MUTATION == "drop_shared_two" else F(-3, 4 * p * p)
            expected_four = F(0) if MUTATION == "drop_square_four" else F(1, 4 * p * p)
            need(c.get(2 * p * p) == expected_two, "shared_two_coefficient")
            need(c.get(4 * p * p) == expected_four, "square_four_coefficient")
            allowed_small.update((p * p, 2 * p * p, 4 * p * p))
        for q, cq in c.items():
            if q == 1:
                continue
            omega = sum((wp for p, wp in w.items() if q % p == 0), F(0))
            if omega and v.core(q) < F(y, 3):
                need(q in allowed_small, "complete_small_core_support")
        for i, p in enumerate(p1):
            for ell in p1[i + 1:]:
                omega = sum((wp for prime, wp in w.items() if p * ell % prime == 0), F(0))
                need(omega == 2, "target_prime_pairs_retained")
        lo = max(y + 1, (y * y + 31) // 32)
        hi = y * y // 16
        window = list(range(lo, hi + 1)) if y <= 64 else [lo, (lo + hi) // 2, hi]
        cells = sorted(set(window + v.sample_cells(y, False)
                           + [y * y, y * y + 1, (y + 1) ** 2 - 2, (y + 1) ** 2 - 1]))
        for k in cells:
            direct = v.weighted_direct(y, k, c, w)
            if MUTATION == "replace_with_deletion":
                direct = sum((v.mode(p * ell, k) * F(4, p * ell)
                              for i, p in enumerate(p1) for ell in p1[i + 1:]), v.Linear())
            rhs = -c1 * (2 * v.mobius_prefix(y))
            rhs += v.T(y, k) * (2 * h1)
            rhs += (v.T(y, k) - v.T(y, k, 2) * F(1, 2)) * (2 * lam * h2)
            defect = F(0)
            for p, wp in w.items():
                j = y // p
                rhs += (-v.Z(j, k, p * p) + 2 * v.Z(j, k, p) - v.Z(j, k)) \
                    * (wp / (p * p))
                if k >= p * y:
                    defect += 2 * wp / p * (v.mobius_prefix(k // p) - v.mobius_prefix(y))
            if MUTATION != "drop_transition_defect":
                rhs += v.Linear(defect)
            need(direct == rhs, "global_compensator_identity")
            if k in window and y >= 64:
                need(defect == 0, "obstruction_window_has_no_transition")
            # Exact rectangular inverse, through the entire stated continuation.
            for p in p1 + p2:
                j = y // p
                u = F(k, p)
                need(u < (y + 1) * (j + 1), "rectangular_strict_source_range")
                h = sum((F(v.mu_trial(a) * v.mu_trial(n), a * n)
                         * v.harmonic(k // (p * a * n))
                         for a in range(1, y + 1) for n in range(1, j + 1)), F(0))
                expected = v.mobius_prefix(min(k // p, y)) \
                    + v.mobius_prefix(j) - v.mobius_prefix(k // p)
                need(h == expected, "rectangular_inverse_transition")
        cases.append({"Y": y, "complete_witness_window_cells": len(window) if y <= 64 else None,
                      "checked_cells": len(cells), "top_primes": len(p1), "middle_primes": len(p2),
                      "lambda": {"num": lam.numerator, "den": lam.denominator}})
    return {"status": "PASS", "arithmetic": "EXACT_RATIONAL_AND_FORMAL_LOGARITHMS",
            "cases": cases, "checks_by_gate": dict(sorted(COUNTS.items())),
            "total_checks_including_guards": sum(COUNTS.values()),
            "not_checked": ["PNT asymptotics", "infinite L2 estimates", "uniform adaptive conditioning", "RH"]}


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
    s = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if a.report:
        a.report.write_text(s, encoding="utf-8", newline="\n")
    print(s, end="")


if __name__ == "__main__":
    main()
