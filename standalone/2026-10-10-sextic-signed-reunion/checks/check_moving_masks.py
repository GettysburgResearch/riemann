#!/usr/bin/env python3
"""Finite exact diagnostics for moving column masks and A2 norm weights.

The residue calculations use actual split Eisenstein prime quotients. The
valuation and norm-weight checks are rational algebra. Neither part proves
a theta transformation, large sieve, convergence theorem, or moment bound.
"""

import argparse
import hashlib
import itertools
import json
from collections import Counter
from fractions import Fraction as F
from pathlib import Path


COUNTS = Counter()
ZERO = None


def require(condition, label):
    COUNTS[label] += 1
    if not condition:
        raise RuntimeError(label)


def times(*phases):
    return ZERO if ZERO in phases else sum(phases) % 6


def char_power(phase, exponent):
    return ZERO if phase is ZERO else phase * exponent % 6


def emul(x, y):
    # Coordinates in Z[omega], omega^2 + omega + 1 = 0.
    return x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0]-x[1]*y[1]


def epow(x, power):
    result = (1, 0)
    while power:
        if power & 1:
            result = emul(result, x)
        x = emul(x, x)
        power //= 2
    return result


def enorm(x):
    return x[0]*x[0]-x[0]*x[1]+x[1]*x[1]


# (rational prime, omega in its quotient, one generator of that prime ideal)
PRIMES = ((7, 4, (3, 1)), (13, 9, (4, 1)), (19, 7, (5, 2)))


def residue(x, data):
    p, omega, _ = data
    value = (x[0] + omega*x[1]) % p
    if value == 0:
        return ZERO
    sixth = pow(value, (p-1)//6, p)
    roots = [j for j in range(6) if pow(omega+1, j, p) == sixth]
    require(len(roots) == 1, "unique_actual_sextic_residue")
    return roots[0]


def element(mask):
    result = (1, 0)
    for i, (_, _, gen) in enumerate(PRIMES):
        if mask >> i & 1:
            result = emul(result, gen)
    return result


def column_symbol(x, mask):
    return times(*(residue(x, p) for i, p in enumerate(PRIMES) if mask >> i & 1))


def check_actual_masks():
    for p, omega, gen in PRIMES:
        require(enorm(gen) == p and (gen[0]+omega*gen[1]) % p == 0,
                "actual_prime_quotient")
        require((omega*omega+omega+1) % p == 0, "actual_eisenstein_quotient")
    rows = [(a,b) for a in range(-10,11) for b in range(-10,11)
            if 0 < enorm((a,b)) <= 60]
    require(sum(enorm(x) == 1 for x in rows) == 6, "all_six_unit_rows")
    labels = range(8)
    zero_rows = sum(any(residue(x,p) is ZERO for p in PRIMES) for x in rows)
    wrong_mask_cases = wrong_overlap_cases = 0
    for row, q0, f in itertools.product(rows, labels, labels):
        q = q0 & ~f
        fixed = emul(row, epow(element(f),4))
        full = emul(fixed, epow(element(q0),6))
        reduced = emul(fixed, epow(element(q),6))
        for n in labels:
            original = column_symbol(fixed,n)
            expected = ZERO if n & q0 else original
            actual = column_symbol(full,n)
            require(actual == expected, "literal_sixth_power_column_exclusion")
            require(actual == column_symbol(reduced,n), "auxiliary_overlap_redundancy")
            wrong_mask_cases += actual != original
            # A false assumption that the exclusion and auxiliary are disjoint.
            wrong_overlap_cases += bool(q0 & f) and actual != ZERO
    require(wrong_mask_cases > 0, "unmasked_sixth_power_negative_control")
    require(wrong_overlap_cases > 0, "false_auxiliary_disjointness_negative_control")
    return {"element_rows":len(rows), "row_ball_norm":60,
            "rows_with_nonunit_symbols":zero_rows,
            "split_prime_norms":[p[0] for p in PRIMES],
            "mask_and_auxiliary_subsets":8,
            "unmasked_sixth_power_failures":wrong_mask_cases,
            "false_auxiliary_disjointness_failures":wrong_overlap_cases}


def check_cube_and_local_zero():
    cube_cases = 0
    for q0, exponents in itertools.product(range(8), itertools.product(range(4),repeat=3)):
        value = 0
        for i, exponent in enumerate(exponents):
            if exponent:
                value = times(value, char_power(residue(epow(element(q0),6), PRIMES[i]), exponent))
        actual = char_power(value,3)
        expected = ZERO if any(e and (q0 >> i & 1) for i,e in enumerate(exponents)) else 0
        require(actual == expected, "literal_cube_index_exclusion")
        cube_cases += 1
    for fixed, e, n, b in itertools.product(range(6),range(6),(ZERO,*range(6)),(ZERO,*range(6))):
        frequency = times(fixed,e,n,char_power(b,3))
        lhs = char_power(frequency,-2)
        rhs = times(char_power(fixed,-2),char_power(e,-2),char_power(n,-2),
                    ZERO if b is ZERO else 0)
        require(lhs == rhs, "active_j0_frequency_separation")
    require(char_power(ZERO,0) is ZERO and char_power(ZERO,6) is ZERO,
            "exponent_zero_keeps_nonunit_mask")
    return {"cube_index_cases":cube_cases,
            "local_scope":"The phase of sqrt(Np) times B_(p,0); its amplitude is checked separately."}


def check_valuation_algebra():
    bases = (6,1,2,3,4,5)
    slopes = (F(-6),F(-12),F(-8))
    base_weights = []
    for nu0 in bases:
        def weights(nu):
            j = nu % 6
            extra = int(j == 4)
            return (F(extra-nu),F(extra+2-2*nu),F(extra)+F(4,3)-F(4,3)*nu)
        initial = weights(nu0)
        base_weights.append(initial)
        for t in range(9):
            require(weights(nu0+6*t) == tuple(a+t*s for a,s in zip(initial,slopes)),
                    "physical_positive_valuation_progression")
            require((nu0+6*t+6) % 6 == (nu0+6*t) % 6,
                    "artificial_sixth_power_preserves_local_exponent")
    require(tuple(max(c) for c in zip(*base_weights)) == (F(-1),F(0),F(0)),
            "deleted_prime_positive_valuation_maxima")
    require(F(-1)+2 == 1 and F(-1)+F(2,3)*2 == F(1,3),
            "active_j0_amplitude_length_costs")
    # j=0 has two branches; their Cauchy square-count is four, even at nu=6.
    require(sum(4 if nu % 6 == 0 else 1 for nu in bases) == 9,
            "inactive_active_branch_square_count")
    return {"six_residue_base_valuations":bases,
            "six_step_slopes":[str(s) for s in slopes],
            "worst_positive_valuation_exponents":["-1","0","0"],
            "active_j0_energy_exponents":["-1","1","1/3"],
            "combined_deleted_prime_cost_exponents":["0","1","1/3"]}


def norm_mask(mask):
    result=1
    for i,(p,_,_) in enumerate(PRIMES):
        if mask >> i & 1:
            result *= p
    return result


def check_a2_child_parameters():
    cases=overlaps=0
    # Each prime is absent, q0-only, f-only, both, c, d, or e.
    for states in itertools.product(range(7),repeat=3):
        q0=f=c=d=e=0
        for i,state in enumerate(states):
            bit=1 << i
            if state in (1,3): q0 |= bit
            if state in (2,3): f |= bit
            if state == 4: c |= bit
            if state == 5: d |= bit
            if state == 6: e |= bit
        q=q0 & ~f
        C=c|d|e
        qchild=(q0|C) & ~(f|e)
        require(qchild == q|c|d, "exact_child_deleted_prime_set")
        J=norm_mask(f)*norm_mask(q)
        Kcubed=norm_mask(f)**2*norm_mask(q)
        Jchild=norm_mask(f|e)*norm_mask(qchild)
        Kchildcubed=norm_mask(f|e)**2*norm_mask(qchild)
        require(Jchild == J*norm_mask(C), "exact_child_J")
        require(Kchildcubed == Kcubed*norm_mask(c)*norm_mask(d)*norm_mask(e)**2,
                "exact_child_K_cubed")
        require(Kcubed <= J**2, "K_at_most_J_two_thirds")
        cases += 1
        overlaps += bool(q0 & f)
    require(overlaps > 0, "original_auxiliary_exclusion_overlaps_present")
    return {"prime_allocation_configurations":cases,"original_overlap_configurations":overlaps}


def vecadd(*vs):
    return tuple(sum(v[j] for v in vs) for j in range(3))


def vecscale(c,v):
    return tuple(c*x for x in v)


def check_a2_weights():
    w=(F(-1),F(-1),F(-3,2))
    small=(F(-1),F(-2),F(-2)) # x <= y
    large=(F(-2),F(-1),F(-2))
    jchild=(F(1),F(1),F(1))
    kchild=(F(1,3),F(1,3),F(2,3))
    for beta in (F(n,24) for n in range(13,25)):
        second=vecadd(w,vecscale(F(1,2),jchild),vecscale(F(1,2),small),
                      vecscale((beta-F(3,2))/2,large))
        require(second == (F(1,2)-beta,-F(3,4)-beta/2,-F(1,2)-beta),
                "A2_short_inverse_second_norm_weight")
        third=vecadd(w,vecscale(F(1,2),kchild),vecscale(F(2,3),small),
                     vecscale(-F(1,3),large))
        require(third == (-F(5,6),-F(11,6),-F(11,6)),
                "A2_short_inverse_third_norm_weight")
        eta=F(7,8)-F(3,4)*beta
        require(-F(1,2)-beta-eta == -F(11,8)-beta/4,
                "A2_remaining_e_sum_exponent")
        require(2*eta == F(7,4)-F(3,2)*beta and eta > 0,
                "A2_cutoff_norm_to_energy_exponent")
    require(F(2)+F(19,216)+F(1,48) == F(911,432), "A2_H_range_fraction")
    require(F(17,12)+F(47,24)*F(16,119) == F(2399,1428), "A2_explicit_gain_fraction")
    require(F(25,12)-3*F(16,119) == F(2399,1428), "A2_balanced_tail_fraction")
    return {"beta_samples":"13/24 through 1 in steps of 1/24; diagnostics only",
            "continuous_scope":"The written proofs separately cover all beta in (1/2,1]."}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    report={"schema":"moving-masks-finite-algebra-v1",
            "status":"PASS_FINITE_ALGEBRA",
            "arithmetic":"Exact integers, sixth-root phase exponents, and rational numbers",
            "actual_residue_masks":check_actual_masks(),
            "cube_and_local_zeros":check_cube_and_local_zero(),
            "valuation_algebra":check_valuation_algebra(),
            "A2_child_parameters":check_a2_child_parameters(),
            "A2_norm_weights":check_a2_weights(),
            "not_checked":["Actual Gauss sums or the theta transformation",
                           "Analytic norm estimates, convergence, conductor uniformity or moment theorems",
                           "The full imported canonical argument or any RH claim"],
            "counts":dict(sorted(COUNTS.items())),
            "checker_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    rendered=json.dumps(report,indent=2,sort_keys=True)+"\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered,end="")


if __name__ == "__main__":
    main()
