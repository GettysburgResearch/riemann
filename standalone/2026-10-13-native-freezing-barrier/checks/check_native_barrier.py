#!/usr/bin/env python3
"""Exact finite diagnostics for the native prime-freezing barrier.

These tests check algebra and bounded actual Eisenstein characters. They do
not prove prime asymptotics, the Mellin resonance, or an infinite moment.
The helper is an unchanged copy of PR #936's published exact arithmetic.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import math
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

import eisenstein_source as es

COUNTS: dict[str, int] = defaultdict(int)


def check(condition: bool, category: str) -> None:
    COUNTS[category] += 1
    if not condition:
        raise RuntimeError(f"{category}: predicate {COUNTS[category]} failed")


def fproduct(values):
    result = Fraction(1)
    for value in values:
        result *= value
    return result


def norm_coefficients(qs: list[int], signs: bool = True) -> dict[int, int]:
    """Multiply every prime IDEAL factor, retaining repeated rational norms."""
    out = {1: 1}
    for q in qs:
        new = defaultdict(int, out)
        for n, c in out.items():
            new[n * q] += -c if signs else c
        out = dict(new)
    return out


def local_euler_tests() -> dict[str, object]:
    fixtures = [[], [7], [7, 7], [7, 7, 13, 13],
                [7, 7, 13, 13, 19, 19, 25],
                [7, 13, 13, 25, 31]]
    for qs in fixtures:
        signed = norm_coefficients(qs)
        positive = norm_coefficients(qs, False)
        # Independently enumerate the subset expansion, then group by norm.
        subset = defaultdict(int)
        grouped_signs: dict[int, set[int]] = defaultdict(set)
        for bits in itertools.product((0, 1), repeat=len(qs)):
            n = math.prod(q for q, bit in zip(qs, bits) if bit)
            sign = (-1) ** sum(bits)
            subset[n] += sign
            grouped_signs[n].add(sign)
        check(dict(subset) == signed, "finite_euler_subset_identity")
        for n, c in signed.items():
            check(len(grouped_signs[n]) == 1, "quadratic_norm_fiber_sign")
            check(abs(c) == positive[n], "norm_grouped_absolute_mass")
        for s in (1, 2, 3):
            value = sum(Fraction(c, n**s) for n, c in signed.items())
            check(value == fproduct(1-Fraction(1, q**s) for q in qs),
                  "finite_signed_dirichlet_product")
            mass = sum(Fraction(abs(c), n**s) for n, c in signed.items())
            check(mass == fproduct(1+Fraction(1, q**s) for q in qs),
                  "exact_forward_operator_mass")
            # W=1_[1,2] only as a finite Mellin algebra fixture. For one
            # coefficient c at n, its D window is [n/2,n]. Integrate exactly.
            integral = sum(Fraction(c*(2**s-1), s*n**s)
                           for n, c in signed.items())
            check(integral == Fraction(2**s-1, s)*value,
                  "exact_compact_step_mellin_fixture")
        # Full inverse is infinite, so check its finite coefficient identity,
        # NOT equality between a truncated inverse norm and its Euler limit.
        cap = 400
        inv = {1: 1}
        for q in qs:
            new = defaultdict(int)
            for n, c in inv.items():
                v = n
                while v <= cap:
                    new[v] += c
                    v *= q
            inv = dict(new)
        conv = defaultdict(int)
        for a, c in signed.items():
            for b, d in inv.items():
                if a*b <= cap:
                    conv[a*b] += c*d
        for n in range(1, cap+1):
            check(conv[n] == int(n == 1), "finite_inverse_coefficients")
    check(norm_coefficients([7, 7])[7] == -2,
          "negative_control_do_not_merge_split_primes")
    check(norm_coefficients([25])[25] == -1,
          "negative_control_inert_norm_not_rational_prime")
    return {"norm_fixtures": fixtures, "inverse_coefficient_cap": 400,
            "step_test": "W=1_[1,2] used only for finite rational Mellin algebra"}


def native_setup(cap: int):
    ideals = sorted(set(es.canonical(u) for u in es.elements(cap)),
                    key=lambda u: (es.en(u), u))
    good = [u for u in ideals if math.gcd(es.en(u), 6) == 1]
    primes = [u for u in good if es.prime(es.en(u)) or
              (math.isqrt(es.en(u))**2 == es.en(u)
               and es.prime(math.isqrt(es.en(u)))
               and math.isqrt(es.en(u)) % 3 == 2)]
    columns = []
    for n in good:
        factors = tuple(j for j, p in enumerate(primes) if es.divides(p, n))
        if math.prod(es.en(primes[j]) for j in factors) == es.en(n):
            columns.append((n, factors))
    return primes, columns


def epower(x, n: int):
    out = es.ONE
    for _ in range(n):
        out = es.emul(out, x)
    return out


def native_tests() -> dict[str, object]:
    primes, factored = native_setup(256)
    principal_table = []
    nonunit_example = None
    for D in (8, 16, 32, 64, 128):
        selected = [(n, f) for n, f in factored if D <= es.en(n) <= 2*D]
        native_sum = sum((-1)**len(f) for _, f in selected)
        for y in (3, 7, 13, 19, 25, 43):
            used = {p for _, f in selected for p in f}
            rough = tuple(sorted(p for p in used if es.en(primes[p]) > y))
            smooth_sum = sum((-1)**len(f) for _, f in selected
                             if all(es.en(primes[p]) <= y for p in f))
            # A genuine sixth-power row, coprime to all retained small primes.
            bg = next(p for p in primes if es.en(p) > y)
            sixth = epower(bg, 6)
            check(es.en(sixth) == es.en(bg)**6, "sixth_power_norm")
            for u in (es.ONE, sixth):
                chars = [es.prime_character(p, u) for p in primes]
                columns = []
                expectation = es.ZERO
                for _, factors in selected:
                    phase = (None if any(chars[j] is None for j in factors) else
                             (3*len(factors)+sum(chars[j] for j in factors)) % 6)
                    c = es.ZERO if phase is None else es.ROOTS[phase]
                    columns.append((factors, c))
                    if not any(p in rough for p in factors):
                        expectation = es.add(expectation, c)
                check(expectation == (smooth_sum, 0), "native_sixth_row_conditional_mean")
                for k in (1, 2):
                    projected = es.projected_moment(columns, k, rough)
                    check(projected >= abs(smooth_sum)**(2*k), "exact_principal_jensen")
                    if u == es.ONE and k == 2:
                        principal_table.append({"D": D, "y": y,
                            "column_count": len(selected), "native_sum": native_sum,
                            "smooth_mobius_sum": smooth_sum,
                            "native_fourth": native_sum**4,
                            "projected_fourth": projected,
                            "smooth_mean_fourth": smooth_sum**4})
            # Explicitly test that a frozen prime dividing the row is not
            # erased from the character's literal zero mask.
            if y >= 7:
                u = primes[0]
                chars = [es.prime_character(p, u) for p in primes]
                masked = 0
                independent = es.ZERO
                for _, f in selected:
                    if any(es.en(primes[j]) > y for j in f):
                        continue
                    if any(chars[j] is None for j in f):
                        masked += 1
                    else:
                        independent = es.add(independent,
                            es.ROOTS[(3*len(f)+sum(chars[j] for j in f)) % 6])
                if masked and independent != (smooth_sum, 0) and nonunit_example is None:
                    nonunit_example = {"D": D, "y": y, "row": u,
                                       "masked_mean": independent,
                                       "incorrect_unmasked_mean": smooth_sum}
                # The unit smooth row formula is not used on this masked row.
                check(all(chars[j] is None for j, p in enumerate(primes)
                          if es.divides(p, u)), "frozen_prime_zero_mask")
    check(nonunit_example is not None,
          "negative_control_no_unmasked_principal_formula")
    # Small completely enumerated phase fixture with actual ideal characters.
    small_generators = [(-3, -2), (-3, -1), (-4, -3)]
    factor_sets = [(), (0,), (1,), (2,), (0, 1), (0, 2), (1, 2), (0, 1, 2)]
    for u in [es.ONE, (-3, -2), (2, 1), epower((-4, -3), 6)]:
        chars = [es.prime_character(p, u) for p in small_generators]
        columns = []
        for f in factor_sets:
            c = es.ZERO if any(chars[j] is None for j in f) else es.ROOTS[
                (3*len(f)+sum(chars[j] for j in f)) % 6]
            columns.append((f, c))
        for k in (1, 2, 3):
            got = es.projected_moment(columns, k, (1, 2))
            check(got == es.direct_random_average(columns, k, (1, 2)),
                  "actual_character_phase_enumeration")
    # Search actual full-column examples; do not assert monotonicity of
    # either freezing or removal of randomization.
    sign_examples = {}
    for D in (8, 16, 32):
        selected = [(n, f) for n, f in factored if D <= es.en(n) <= 2*D]
        for u in es.elements(16):
            chars = [es.prime_character(p, u) for p in primes]
            columns = []
            for _, f in selected:
                c = es.ZERO if any(chars[j] is None for j in f) else es.ROOTS[
                    (3*len(f)+sum(chars[j] for j in f)) % 6]
                columns.append((f, c))
            total = es.ZERO
            for _, c in columns:
                total = es.add(total, c)
            native = es.norm(total)**2
            used = {j for _, f in selected for j in f}
            for y in (3, 7, 13):
                rough = tuple(sorted(j for j in used if es.en(primes[j]) > y))
                jv = es.projected_moment(columns, 2, rough)
                diff = native - jv
                key = "negative" if diff < 0 else "positive" if diff > 0 else None
                if key and key not in sign_examples:
                    sign_examples[key] = {"D": D, "u": u, "Nu": es.en(u),
                                          "y": y, "native": native,
                                          "projected": jv, "difference": diff}
            if len(sign_examples) == 2:
                break
        if len(sign_examples) == 2:
            break
    check(set(sign_examples) == {"negative", "positive"},
          "negative_control_no_native_projection_monotonicity")
    alias = es.projected_moment([((), es.ONE), ((0,), (-1, 0))], 6, (0,))
    check(alias == 926 and alias != math.comb(12, 6),
          "negative_control_retain_sixth_aliases")
    return {"scope": "all squarefree good ideal columns D<=Nn<=2D at the listed D; hard window only",
            "principal_table": principal_table, "signed_examples": sign_examples,
            "nonunit_example": nonunit_example}


def exponent_tests() -> dict[str, object]:
    cases = []
    for k in range(1, 21):
        for h in (Fraction(1, 2), Fraction(1), Fraction(21, 20), Fraction(3, 2)):
            if h >= Fraction(6*k, 5):
                continue
            beta = Fraction(1, 2)+Fraction(5, 12*k)*h
            critical = 1/(1-beta)
            check(critical == Fraction(12*k)/(6*k-5*h), "cutoff_threshold_identity")
            A = critical+1
            alpha = (beta+1-1/A)/2
            sigma = (alpha+1-1/A)/2
            delta = 2*k*(alpha-beta)
            check(0 < alpha < sigma < 1-1/A < 1, "strict_mellin_window")
            check(h/6+2*k*alpha == h+k+delta, "replica_exponent_identity")
            check(delta > 0 and 1-sigma > 1/A, "strict_positive_gaps")
    k, h, A = 2, Fraction(21, 20), Fraction(4)
    beta = Fraction(1, 2)+Fraction(5, 12*k)*h
    alpha, sigma = Fraction(47, 64), Fraction(95, 128)
    delta = 2*k*(alpha-beta)
    check(beta == Fraction(23, 32), "concrete_beta")
    check(delta == Fraction(1, 16), "concrete_delta")
    check(alpha < sigma < 1-1/A and 1-sigma == Fraction(33, 128), "concrete_contour")
    check(Fraction(4) > Fraction(32, 9), "concrete_strict_cutoff")
    def admissible(cutoff_power, scalar_exponent, contour):
        return 0 < scalar_exponent < contour < 1-1/cutoff_power
    check(not admissible(A, alpha, alpha),
          "negative_control_no_endpoint_substitution")
    return {"fourth_example": {"h": str(h), "A": str(A), "beta": str(beta),
                               "alpha": str(alpha), "sigma": str(sigma), "delta": str(delta)},
            "h_equals_one_thresholds": {str(k): str(Fraction(12*k, 6*k-5))
                                         for k in (2, 3, 4, 8)}}


def main() -> None:
    helper = Path(__file__).with_name("eisenstein_source.py").read_bytes()
    blob = hashlib.sha1(b"blob "+str(len(helper)).encode()+b"\0"+helper).hexdigest()
    check(blob == "64d21a7f400f5bf5654fd67735743ff1befab067", "pinned_helper_blob")
    report = {"status": "PASS", "arithmetic": "exact integers, fractions, and Z[zeta_6] pairs",
              "scope": "finite diagnostic identities, not infinite analytic certification",
              "helper_git_blob": blob, "euler": local_euler_tests(),
              "native": native_tests(), "exponents": exponent_tests()}
    report["predicate_counts"] = dict(sorted(COUNTS.items()))
    report["total_predicates"] = sum(COUNTS.values())
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
