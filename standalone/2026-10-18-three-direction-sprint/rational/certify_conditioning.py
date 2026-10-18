#!/usr/bin/env python3
"""DIRECTED_INTEGER_INTERVAL exhaustive finite coefficient-budget certificate.

Every defect-change cell is generated from primitive Mobius jumps, then the
entire nuisance vector is independently reconstructed from directed native
prefixes. The Gram inverse is checked by division-free interval inequalities.
This is a finite theorem at one Y, not an asymptotic conditioning theorem.
"""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import hashlib
import json
import subprocess
import sys

import verify as primitive


COUNTS = Counter()
BITS = 160
SCALE = 1 << BITS


def need(value, gate):
    COUNTS[gate] += 1
    if not value:
        raise RuntimeError("REJECT:" + gate)


def ceil_div(a, b):
    return -((-a) // b)


class I:
    __slots__ = ("lo", "hi")
    def __init__(self, lo=0, hi=None):
        self.lo, self.hi = int(lo), int(lo if hi is None else hi)
        if self.lo > self.hi:
            raise ValueError("reversed interval")

    def __add__(self, other):
        return I(self.lo + other.lo, self.hi + other.hi)

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + -other

    def __mul__(self, other):
        q = (self.lo * other.lo, self.lo * other.hi,
             self.hi * other.lo, self.hi * other.hi)
        return I(min(q) // SCALE, ceil_div(max(q), SCALE))

    def square(self):
        a = 0 if self.lo <= 0 <= self.hi else min(self.lo * self.lo, self.hi * self.hi)
        b = max(self.lo * self.lo, self.hi * self.hi)
        return I(a // SCALE, ceil_div(b, SCALE))

    def absolute(self):
        return I(0 if self.lo <= 0 <= self.hi else min(abs(self.lo), abs(self.hi)),
                 max(abs(self.lo), abs(self.hi)))

    def div_integer(self, n):
        return I(self.lo // n, ceil_div(self.hi, n))

    @classmethod
    def rational(cls, value):
        value = F(value)
        a = value.numerator * SCALE
        return cls(a // value.denominator, ceil_div(a, value.denominator))


def total(items):
    out = I()
    for a in items:
        out = out + a
    return out


def dot(a, b):
    return total(x * y for x, y in zip(a, b))


def contains(interval, exact):
    value = F(exact) * SCALE
    return interval.lo <= value <= interval.hi


def interval_unit_checks():
    values = [F(-7, 3), F(-1, 7), F(0), F(1, 11), F(13, 5)]
    for a in values:
        x = I.rational(a)
        need(contains(x, a), "interval_rational_enclosure")
        need(contains(x.square(), a * a), "interval_square_enclosure")
        need(contains(x.div_integer(7), a / 7), "interval_division_enclosure")
        for b in values:
            z = I.rational(b)
            need(contains(x + z, a + b), "interval_addition_enclosure")
            need(contains(x - z, a - b), "interval_subtraction_enclosure")
            need(contains(x * z, a * b), "interval_product_enclosure")
    need(contains(I(-SCALE, SCALE).square(), 0), "interval_square_crosses_zero")


def certify(y, strata, bound, mutation=None, box_bound=None):
    interval_unit_checks()
    need(y >= 64 and strata >= 3, "input_domain")
    need((strata + 1) ** 2 < y, "large_prime_domain")
    maximum = (strata + 1) * (y + 1)
    mu = primitive.mu_sieve(maximum)
    need(all(mu[n] == primitive.mu_trial(n) for n in range(1, maximum + 1)),
         "independent_primitive_mu")
    pref = [F(0)]
    for n in range(1, y + 1):
        pref.append(pref[-1] + F(mu[n], n))
    need(mu[y] != 0 and pref[-2] * pref[-1] <= 0, "native_crossing")
    need(abs(pref[-1]) <= F(1, y), "crossing_size")
    primes = [p for p in range(2, y + 1) if primitive.factors(p) == ((p, 1),)
              and p * (strata + 1) > y]
    need(all(p * p > y for p in primes), "all_selected_primes_large")
    h = [sum((F(1, p) for p in primes if y // p == j), F(0))
         for j in range(1, strata + 1)]
    v_exact = [pref[j] * h[j - 1] for j in range(1, strata + 1)]
    v = [I.rational(a) for a in v_exact]
    aa = total(a.square() for a in v[1:])
    need(aa.lo > 0, "nonzero_common_profile_complement")

    # Independent directed prefix producer, with exactly documented rounding.
    ml, mh = [0], [0]
    for n in range(1, maximum + 1):
        a = mu[n] * SCALE
        ml.append(ml[-1] + a // n)
        mh.append(mh[-1] + ceil_div(a, n))
    if mutation == "corrupt_directed_prefix":
        ml[y + 1] = mh[y + 1] = 0
    exact_prefix = F(0)
    for n in range(1, maximum + 1):
        exact_prefix += F(mu[n], n)
        need(contains(I(ml[n], mh[n]), exact_prefix), "exact_prefix_enclosure")
    start, end = (y * y + 31) // 32, (y + 1) ** 2 - 1
    events = defaultdict(list)
    expected = 0
    for p in primes:
        j = y // p - 1
        for n in range(y + 1, end // p + 1):
            if mu[n]:
                events[p * n].append((j, mu[n]))
                expected += 1
    need(sum(len(a) for a in events.values()) == expected, "complete_nonzero_jump_count")
    need(start > y, "physical_window_domain")
    if mutation in ("omit_primitive_event", "flip_primitive_event"):
        at = min(k for k in events if k > start)
        j, sign = events[at][0]
        if mutation == "omit_primitive_event":
            events[at].pop(0)
        else:
            events[at][0] = (j, -sign)
    # Authenticate EVERY possible change cell independently. This sieve factors
    # k itself, rather than regenerating the producer's p*n loops. Thus an
    # omitted event cannot leave a silently uncertified constant-state gap.
    spf = list(range(end + 1))
    for p in range(2, isqrt(end) + 1):
        if spf[p] == p:
            for n in range(p * p, end + 1, p):
                if spf[n] == n:
                    spf[n] = p
    selected = set(primes)
    authenticated_events = 0
    for k in range(1, end + 1):
        n, independently_expected = k, []
        while n > 1:
            p = spf[n]
            if p in selected and k // p > y and mu[k // p]:
                independently_expected.append((y // p - 1, mu[k // p]))
            while n % p == 0:
                n //= p
        need(sorted(events.get(k, [])) == sorted(independently_expected),
             "independent_all_cell_event_coverage")
        authenticated_events += len(independently_expected)
    need(authenticated_events == expected, "authenticated_total_event_count")
    # All possible jumps are multiples p*n with n>Y; this also authenticates
    # intervals between events as constant nuisance vectors.
    change_cells = [start] + sorted(k for k in events if start < k <= end)
    jump = [I() for _ in range(strata)]
    for k in sorted(k for k in events if k <= start):
        for j, sign in events[k]:
            jump[j] = jump[j] + I.rational(F(sign, k))
    state_count = 0
    covered_cells = 0
    rank1_states = 0
    rank2_states = 0
    min_margin_num = None
    min_box_margin_num = None
    event_hash = hashlib.sha256()
    for at, k in enumerate(change_cells):
        if at:
            for j, sign in events[k]:
                jump[j] = jump[j] + I.rational(F(sign, k))
        # Direct independently reconstructed d_j(k), not the event sums.
        d = [I() for _ in range(strata)]
        exact_zero = True
        for p in primes:
            n = k // p
            if n > y:
                exact_zero = False
                q = I(ml[n] - mh[y], mh[n] - ml[y]).div_integer(p)
                j = y // p - 1
                d[j] = d[j] + q
        for a, b in zip(d, jump):
            need(max(a.lo, b.lo) <= min(a.hi, b.hi), "independent_defect_intervals_overlap")
        if exact_zero:
            # d=0 exactly; use the minimum-norm solution to the one common row.
            for a in v[1:]:
                numerator = -(v[0] * a)
                need(max(abs(numerator.lo), abs(numerator.hi)) <= bound * aa.lo,
                     "rank_one_coefficient_budget")
            rank1_states += 1
            if box_bound is not None:
                capacity = total(a.absolute() for a in v[1:]) * I.rational(box_bound)
                need(v[0].absolute().hi <= capacity.lo, "rank_one_zonotope_budget")
        else:
            bb = total(a.square() for a in d[1:])
            ab = dot(v[1:], d[1:])
            determinant = aa * bb - ab.square()
            need(determinant.lo > 0, "positive_exact_gram_determinant")
            rhs_d = I() if mutation == "erase_defect_rhs" else d[0]
            left = -(v[0] * bb) + rhs_d * ab
            right = v[0] * ab - rhs_d * aa
            numerators = []
            for a, b in zip(v[1:], d[1:]):
                numerator = a * left + b * right
                numerators.append(numerator)
                magnitude = max(abs(numerator.lo), abs(numerator.hi))
                margin = bound * determinant.lo - magnitude
                need(margin >= 0, "rank_two_coefficient_budget")
                min_margin_num = margin if min_margin_num is None else min(min_margin_num, margin)
            for row, rhs in ((v, v[0]), (d, d[0])):
                residual = dot(row[1:], numerators) + rhs * determinant
                need(residual.lo <= 0 <= residual.hi, "independent_nuisance_equation_residual")
            if box_bound is not None:
                # The planar zonotope's facets are perpendicular to a_j.
                # Symmetry means each pair minor is computed only once.
                capacity = [I() for _ in range(strata - 1)]
                for j in range(1, strata):
                    for ell in range(j + 1, strata):
                        minor = (v[j] * d[ell] - d[j] * v[ell]).absolute()
                        capacity[j - 1] = capacity[j - 1] + minor
                        capacity[ell - 1] = capacity[ell - 1] + minor
                for j in range(1, strata):
                    target_minor = (v[j] * d[0] - d[j] * v[0]).absolute()
                    cap = capacity[j - 1] * I.rational(box_bound)
                    margin = cap.lo - target_minor.hi
                    need(margin >= 0, "rank_two_zonotope_budget")
                    min_box_margin_num = margin if min_box_margin_num is None else min(min_box_margin_num, margin)
            rank2_states += 1
        next_cell = change_cells[at + 1] if at + 1 < len(change_cells) else end + 1
        need(next_cell > k, "strict_change_cell_order")
        covered_cells += next_cell - k
        state_count += 1
        event_hash.update((str(k) + ":" + str(next_cell) + ";").encode())
    need(covered_cells == end - start + 1, "complete_physical_cell_coverage")
    need(state_count == rank1_states + rank2_states, "rank_partition")
    result = {"status": "PASS", "arithmetic": "DIRECTED_INTEGER_INTERVAL",
            "fraction_bits": BITS, "Y": y, "strata": strata, "coefficient_bound": bound,
            "physical_window": [start, end], "covered_physical_cells": covered_cells,
            "distinct_nuisance_states": state_count, "rank_one_states": rank1_states,
            "rank_two_states": rank2_states, "selected_prime_count": len(primes),
            "nonzero_primitive_jump_count": expected,
            "all_factorized_physical_and_prephysical_cells": end,
            "minimum_division_free_budget_margin_numerator": min_margin_num,
            "margin_denominator_power_of_two": BITS,
            "primitive_mu_sha256": hashlib.sha256(bytes(a + 1 for a in mu[1:])).hexdigest(),
            "change_partition_sha256": event_hash.hexdigest(),
            "checks_by_gate": dict(sorted(COUNTS.items())),
            "total_checks_including_guards": sum(COUNTS.values()),
            "claim": "At every covered cell the two nuisance equations have an exact real solution with lambda_1=1 and all complementary coefficients bounded in magnitude by the stated integer.",
            "not_proved": ["the same coefficient budget at other prefixes", "uniform cofinal conditioning",
                           "a bound for the full unweighted rough-core source", "RH"]}
    if box_bound is not None:
        result["zonotope_coefficient_bound"] = {"num": box_bound.numerator,
                                                "den": box_bound.denominator}
        result["minimum_zonotope_budget_margin_numerator"] = min_box_margin_num
        result["zonotope_claim"] = "At every covered cell there exists an exact real solution to both nuisance equations with lambda_1=1 and every complementary coefficient bounded by the stated rational. This need not be the minimum-Euclidean-norm solution."
    return result


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--Y", type=int, default=517)
    a.add_argument("--strata", type=int, default=16)
    a.add_argument("--bound", type=int, default=4)
    a.add_argument("--output", type=Path)
    a.add_argument("--box-bound", type=F)
    mutations = ("omit_primitive_event", "flip_primitive_event",
                 "corrupt_directed_prefix", "erase_defect_rhs", "budget_one")
    a.add_argument("--mutation", choices=mutations)
    a.add_argument("--mutations", action="store_true")
    z = a.parse_args()
    if z.mutations:
        rows = []
        for mutation in mutations:
            command = [sys.executable, "-O", __file__, "--Y", str(z.Y),
                       "--strata", str(z.strata), "--bound", str(z.bound),
                       "--mutation", mutation]
            result = subprocess.run(command, capture_output=True, text=True)
            need(result.returncode != 0 and "REJECT:" in result.stderr,
                 "negative_control_rejected")
            rows.append({"mutation": mutation, "status": "REJECTED",
                         "gate": result.stderr.split("REJECT:")[-1].splitlines()[0]})
        report = {"status": "PASS", "negative_controls": rows}
    else:
        report = certify(z.Y, z.strata, 1 if z.mutation == "budget_one" else z.bound,
                         z.mutation, z.box_bound)
    encoded = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if z.output:
        z.output.write_text(encoded, encoding="utf-8", newline="\n")
    print(encoded, end="")


if __name__ == "__main__":
    main()
