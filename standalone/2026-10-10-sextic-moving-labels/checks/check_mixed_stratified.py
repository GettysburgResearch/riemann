#!/usr/bin/env python3
"""Exact arithmetic diagnostics for mixed labels, stratified inversion, and A2.

The program checks finite identities and rational exponent calculations.
It does not evaluate a theta series, certify an analytic bound, authenticate
the imported automorphy theorem, or prove an infinite moment statement.
"""

from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import json
import math


ZERO, ONE = (0, 0), (1, 0)
ROOTS = (ONE, (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))
VALUES = (ZERO,) + ROOTS


def require(condition, detail):
    if not condition:
        raise RuntimeError(detail)


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


def mul(z, w):
    a, b = z
    c, d = w
    return a * c - b * d, a * d + b * c + b * d


def scale(c, z):
    return c * z[0], c * z[1]


def power(z, n):
    result = ONE
    for _ in range(n):
        result = mul(result, z)
    return result


def sum_values(values):
    result = ZERO
    for value in values:
        result = add(result, value)
    return result


def unit_mask(z):
    return 0 if z == ZERO else 1


def check_local_label_identities():
    relabel_checks = cube_relabel_checks = cube_mask_checks = 0
    for k, f_only, q_only, common in product(VALUES, repeat=4):
        # q=q_only*common and f=f_only*common; the common support is not
        # silently presumed coprime. All 7^4 phase/zero assignments are used.
        f = mul(f_only, common)
        q = mul(q_only, common)
        left = mul(mul(k, power(f, 4)), power(q_only, 6))
        right = scale(unit_mask(q), mul(k, power(f, 4)))
        require(left == right, ("redundant overlap and relabel", k, f_only, q_only, common))
        relabel_checks += 1
        expected_cube = scale(unit_mask(f) * unit_mask(q_only), power(k, 3))
        require(power(left, 3) == expected_cube,
                ("cubed effective-row relabel", k, f_only, q_only, common))
        cube_relabel_checks += 1

    for k, outer_a, f, q in product(VALUES, repeat=4):
        for lam in ROOTS:
            psi_without_angular = scale(unit_mask(q), mul(k, power(mul(outer_a, f), 4)))
            left = mul(power(lam, 3), power(psi_without_angular, 3))
            right = scale(unit_mask(outer_a) * unit_mask(f) * unit_mask(q),
                          mul(power(lam, 3), power(k, 3)))
            require(left == right, ("cube inverse zero mask", k, outer_a, f, q, lam))
            cube_mask_checks += 1
    return {"all_zero_or_sixth_root_values_per_character": 7,
            "overlap_relabel_identities": relabel_checks,
            "cubed_relabel_identities": cube_relabel_checks,
            "cube_inverse_mask_identities": cube_mask_checks}


def check_valuation_strata():
    one_prime_checks = two_prime_checks = shared_cases = 0
    for valuation in range(25):
        quotient, remainder = divmod(valuation, 6)
        require(0 <= remainder <= 5 and valuation == 6 * quotient + remainder,
                ("division by six", valuation))
        for z in VALUES:
            original = power(z, valuation)
            factor = unit_mask(z) if quotient else 1
            require(original == scale(factor, power(z, remainder)),
                    ("sixth-power mask", valuation, z))
            one_prime_checks += 1
    for valuations in product(range(13), repeat=2):
        quotients = tuple(v // 6 for v in valuations)
        remainders = tuple(v % 6 for v in valuations)
        shared = any(q > 0 and r > 0 for q, r in zip(quotients, remainders))
        for phases in product(VALUES, repeat=2):
            original = ONE
            residual = ONE
            mask = 1
            for valuation, q, r, z in zip(valuations, quotients, remainders, phases):
                original = mul(original, power(z, valuation))
                residual = mul(residual, power(z, r))
                if q:
                    mask *= unit_mask(z)
            require(original == scale(mask, residual),
                    ("two-prime sixth-power decomposition", valuations, phases))
            two_prime_checks += 1
            shared_cases += int(shared)
    require(shared_cases > 0, "no shared v/k0 prime tested")

    # Exact one-prime support bookkeeping for q_v after f redundancy.
    exclusion_checks = 0
    for q_flag, f_flag, s_flag, v_exp in product((0, 1), (0, 1), (0, 1), range(5)):
        q_star = q_flag and not f_flag and not s_flag
        q_v = (q_flag or v_exp > 0) and not f_flag and not s_flag
        require(int(q_v) <= int(q_star) + v_exp,
                ("Q_v <= Q Nv local exponent", q_flag, f_flag, s_flag, v_exp))
        exclusion_checks += 1
    return {"one_prime_character_identity_checks": one_prime_checks,
            "two_prime_character_identity_checks": two_prime_checks,
            "checks_with_shared_v_and_k0_prime": shared_cases,
            "moving_exclusion_exponent_checks": exclusion_checks,
            "maximum_prime_valuation_tested": 24}


def check_local_energy_exponents():
    length_powers = (F(0), F(1), F(2, 3))
    exclusion_branches = ((F(0), F(0)), (F(-1), F(2)))
    auxiliary_branches = ((F(-1), F(2)), (F(0), F(1)), (F(-1), F(-1)))
    exclusion_costs = [max(amplitude + t * length for amplitude, length in exclusion_branches)
                       for t in length_powers]
    auxiliary_costs = [max(amplitude + t * length for amplitude, length in auxiliary_branches)
                       for t in length_powers]
    require(exclusion_costs == [F(0), F(1), F(1, 3)], "exclusion branch exponent table")
    require(auxiliary_costs == [F(0), F(1), F(2, 3)], "auxiliary branch exponent table")

    progressions = []
    checks = 0
    for name, start, shift, targets in (
        ("exclusion_positive_valuation", 1, 0, (F(-1), F(0), F(0))),
        ("auxiliary_positive_valuation", 1, 4, (F(-1), F(0), F(0))),
        ("ordinary_powerful_row_factor", 2, 0, (F(-2), F(-2), F(-4, 3))),
    ):
        for height_power, radical_power, target in zip((F(1), F(2), F(4, 3)),
                                                       (F(0), F(2), F(4, 3)), targets):
            first = []
            for valuation in range(start, start + 6):
                residue = (valuation + shift) % 6
                amplitude = int(residue == 4)
                branch_count = 4 if residue == 0 else 1
                exponent = F(amplitude) + radical_power - height_power * valuation
                require(exponent <= target, ("local progression leading exponent", name, valuation))
                first.append((str(exponent), branch_count))
                for extra in range(1, 5):
                    other = valuation + 6 * extra
                    other_residue = (other + shift) % 6
                    other_exponent = F(int(other_residue == 4)) + radical_power - height_power * other
                    require(other_exponent == exponent - 6 * height_power * extra,
                            ("geometric residue progression", name, valuation, extra))
                    require((4 if other_residue == 0 else 1) == branch_count,
                            ("branch multiplicity progression", name, valuation, extra))
                    checks += 1
            require(max(F(x) for x, _ in first) == target, ("sharp leading exponent in table", name))
            step = 6 * height_power
            require(step.denominator == 1, "integer geometric step")
            uniform_constant = F(24) / (1 - F(1, 2 ** int(step)))
            progressions.append({"sector": name, "height_power": str(height_power),
                                 "leading_exponent": str(target), "residue_terms": first,
                                 "geometric_step": str(step),
                                 "elementary_majorant_constant_for_norm_p_at_least_2": str(uniform_constant)})
    return {"exclusion_energy_powers": list(map(str, exclusion_costs)),
            "auxiliary_energy_powers": list(map(str, auxiliary_costs)),
            "residue_progression_checks": checks,
            "progressions": progressions,
            "scope": "Exact monomial and residue data; no analytic norm inequality is numerically certified."}


def check_finite_masked_cube_inverse():
    primes = (7, 13)
    masks = tuple(range(4))
    norms_sf = [math.prod(p for i, p in enumerate(primes) if mask >> i & 1) for mask in masks]
    cap = 200
    support_bound = cap ** 3
    ideals = tuple(exponents for exponents in product(range(3), repeat=2)
                   if math.prod(p ** e for p, e in zip(primes, exponents)) <= cap)
    norms = {d: math.prod(p ** e for p, e in zip(primes, d)) for d in ideals}
    radical = {d: sum(1 << i for i, e in enumerate(d) if e) for d in ideals}
    squarefree = tuple(d for d in ideals if max(d) <= 1)
    mu = {d: (-1) ** sum(d) if max(d) <= 1 else 0 for d in ideals}
    cutoffs = (F(1, 2), F(1), F(7), F(13), F(49), F(91), F(169), F(cap))
    lambda_prime = (ROOTS[1], ROOTS[2])
    identity_checks = tail_checks = empty_short_checks = capped_empty_checks = 0
    repeated_factor_witnesses = inner_overlap_witnesses = outer_inverse_overlap_witnesses = 0

    for phases in product(VALUES, repeat=2):
        row_sf = []
        for mask in masks:
            value = ONE
            for bit in range(2):
                if mask >> bit & 1:
                    value = mul(value, phases[bit])
            row_sf.append(value)
        cube_weight = {}
        for d in ideals:
            value = ONE
            for lam, phase, exponent in zip(lambda_prime, phases, d):
                value = mul(value, power(mul(power(lam, 3), power(phase, 3)), exponent))
            cube_weight[d] = scale(F(1, norms[d]), value)

        for q, f, outer in product(masks, repeat=3):
            excluded = q | f
            allowed = tuple(d for d in ideals if not radical[d] & excluded)
            allowed_h = tuple(h for h in squarefree if not radical[h] & excluded)
            # The sampled P values below are arbitrary exact finite physical
            # data with the true support and mask incidences. The convolution
            # identities hold for every such data table, including the true
            # normalized Gauss polynomial. This model does not compute Gauss
            # coefficients or theta transforms.
            raw = {}
            for d in allowed:
                value = ZERO
                outer_mask = outer | radical[d]
                for aa, nn in product(masks, repeat=2):
                    if aa & nn or (aa | nn) & excluded or aa & outer_mask:
                        continue
                    argument = norms_sf[nn] * norms[d] ** 3
                    if argument > support_bound:
                        continue
                    test_value = (2 + norms_sf[aa] % 7) * (1 + argument % 11)
                    coefficient = mul(row_sf[aa], row_sf[nn])
                    # A multiplicative fourth-power f twist with literal
                    # zeros is already enforced by (aa|nn)&f above.
                    for bit in range(2):
                        if (aa | nn) >> bit & 1:
                            coefficient = mul(coefficient, power(ROOTS[(bit + 1) * f.bit_count() % 6], 4))
                    value = add(value, scale(test_value, coefficient))
                    if nn & radical[d] and coefficient != ZERO:
                        inner_overlap_witnesses += 1
                raw[d] = value

            completed_at_h = {}
            for h in allowed_h:
                value = ZERO
                for b in allowed:
                    d = tuple(x + y for x, y in zip(h, b))
                    if d not in raw:
                        continue
                    term = mul(cube_weight[b], raw[d])
                    value = add(value, term)
                    if any(x and y for x, y in zip(h, b)) and term != ZERO:
                        repeated_factor_witnesses += 1
                completed_at_h[h] = value

            full = sum_values(scale(mu[h], mul(cube_weight[h], completed_at_h[h])) for h in allowed_h)
            require(full == raw[(0, 0)], ("full masked inverse", phases, q, f, outer))
            identity_checks += 1
            for h in allowed_h:
                if radical[h] & outer and mul(cube_weight[h], completed_at_h[h]) != ZERO:
                    outer_inverse_overlap_witnesses += 1

            for cutoff in cutoffs:
                short = sum_values(scale(mu[h], mul(cube_weight[h], completed_at_h[h]))
                                   for h in allowed_h if norms[h] <= cutoff)
                long = sum_values(scale(mu[h], mul(cube_weight[h], completed_at_h[h]))
                                  for h in allowed_h if norms[h] > cutoff)
                regrouped = ZERO
                for d in allowed:
                    c_r = sum(mu[h] for h in allowed_h
                              if norms[h] > cutoff and all(x <= y for x, y in zip(h, d)))
                    if norms[d] <= cutoff:
                        require(c_r == 0, ("tail support", d, cutoff))
                    regrouped = add(regrouped, scale(c_r, mul(cube_weight[d], raw[d])))
                require(long == regrouped, ("truncated repeated-factor inverse", phases, q, f, outer, cutoff))
                require(add(short, long) == raw[(0, 0)], ("short+long inverse", phases, q, f, outer, cutoff))
                if cutoff < 1:
                    require(short == ZERO, "cutoff below one must have empty short part")
                    empty_short_checks += 1
                if cutoff >= cap:
                    require(long == ZERO, "physical cap must have exactly empty tail")
                    require(not [h for h in allowed_h if norms[h] > cutoff], "capped inverse support not empty")
                    capped_empty_checks += 1
                tail_checks += 1

    for witness, label in ((repeated_factor_witnesses, "shared h,b prime"),
                           (inner_overlap_witnesses, "inner n/d overlap"),
                           (outer_inverse_overlap_witnesses, "outer r/h overlap")):
        require(witness > 0, ("missing live overlap case", label))
    row_cutoff_checks = 0
    for base, v_norm in product((F(1, 2), F(1), F(7), F(49), F(200)), (1, 7, 13, 49, 91, 169)):
        cutoff = min(F(cap), base * v_norm)
        require(cutoff <= base * v_norm, "capped cutoff domination")
        if cutoff == cap:
            require(all(norms[h] <= cutoff for h in squarefree), "capped stratum tail support")
        else:
            require(cutoff == base * v_norm, "uncapped cutoff exact equality")
        row_cutoff_checks += 1
    return {"prime_norms": primes, "cube_support_cap": cap,
            "cube_ideals": [list(d) for d in ideals],
            "full_inverse_identities": identity_checks, "truncated_inverse_identities": tail_checks,
            "empty_short_part_checks": empty_short_checks, "exactly_empty_capped_tail_checks": capped_empty_checks,
            "stratum_cutoff_checks": row_cutoff_checks,
            "nonzero_repeated_h_b_factor_terms": repeated_factor_witnesses,
            "nonzero_inner_n_d_overlap_terms": inner_overlap_witnesses,
            "nonzero_outer_r_h_overlap_terms": outer_inverse_overlap_witnesses,
            "scope": "Finite exact convolution on sampled physical data; no Gauss coefficient or theta evaluation."}


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def plus(x, y):
    return tuple(a + b for a, b in zip(x, y))


def times(c, x):
    return tuple(c * a for a in x)


def raw_term_exponents(beta):
    # Coordinates D,H,F,Q,R.
    kappa = F(9, 2) - 3 * beta
    return [
        (F(1), F(1), F(0), F(0), F(0)),
        (beta - F(1, 2), F(2), F(1), F(1), kappa),
        (F(2, 3), F(4, 3), F(2, 3), F(1, 3), F(2)),
        (F(0), F(1), F(0), F(0), F(0)),
        (F(2), F(0), F(0), F(0), F(-3)),
        (F(4, 3), F(2, 3), F(0), F(0), F(-2)),
    ]


def substitute_cutoff(term, cutoff):
    return plus(term[:4], times(term[4], cutoff))


def check_optimization_and_v_exponents():
    reports = []
    for beta in (F(1), F(11, 12)):
        delta = 5 - 2 * beta
        kappa = F(9, 2) - 3 * beta
        r1 = (F(4, 15), F(-4, 15), F(-2, 15), F(-1, 15))
        r2 = (F(1, 3), -4 / (3 * delta), -2 / (3 * delta), -2 / (3 * delta))
        e1 = (F(6, 5), F(4, 5), F(2, 5), F(1, 5))
        e2 = (F(1), 4 / delta, 2 / delta, 2 / delta)
        terms = raw_term_exponents(beta)
        require(substitute_cutoff(terms[2], r1) == substitute_cutoff(terms[4], r1) == e1,
                ("R1 exact balance", beta))
        require(substitute_cutoff(terms[1], r2) == substitute_cutoff(terms[4], r2) == e2,
                ("R2 exact balance", beta))

        # The feasible log-exponent region is a tetrahedron. Splitting it by
        # r1=r2 gives affine regions. Its vertices and edge intersections
        # suffice for the six affine inequalities, at these exact beta values.
        vertices = [(F(0), F(0), F(0)), (delta / 4, F(0), F(0)),
                    (F(0), delta / 2, F(0)), (F(0), F(0), delta / 2)]
        difference = plus(r1, times(-1, r2))
        points = set(vertices)
        for x, y in combinations(vertices, 2):
            dx = dot(difference, (F(1),) + x)
            dy = dot(difference, (F(1),) + y)
            if dx * dy < 0:
                t = dx / (dx - dy)
                points.add(plus(x, times(t, plus(y, times(-1, x)))))
        for point in points:
            base = (F(1),) + point
            cutoff = min(dot(r1, base), dot(r2, base))
            energy = max(dot(e1, base), dot(e2, base))
            require(F(0) <= cutoff <= F(1, 3), ("admissible optimal cutoff", beta, point))
            require(energy <= 2, ("diagonal envelope regime", beta, point))
            values = [dot(term, base + (cutoff,)) for term in terms]
            require(max(values) == energy, ("all six optimized terms", beta, point, values))
            transition = -delta + 8 * beta * point[0] + 4 * beta * point[1] + (5 + 2 * beta) * point[2]
            require(dot(plus(e2, times(-1, e1)), base) == transition / (5 * delta),
                    ("mixed-label transition equation", beta, point))

        short_v = (F(-6), F(-12) + 1 + kappa, F(-8) + F(1, 3) + 2)
        long_v = (F(-6), F(-3), F(-4) - 2)
        require(short_v == (F(-6), F(-13, 2) - 3 * beta, F(-17, 3)), ("short v powers", beta))
        require(long_v == (F(-6), F(-3), F(-6)), "long v powers")
        require(max(short_v + long_v) < -1, ("summable v exponents", beta))
        reports.append({"beta": str(beta), "d_beta": str(delta),
                        "cutoff_vectors_D_H_F_Q": [list(map(str, r1)), list(map(str, r2))],
                        "optimized_energy_vectors_D_H_F_Q": [list(map(str, e1)), list(map(str, e2))],
                        "affine_region_vertices_checked": len(points),
                        "short_v_powers": list(map(str, short_v)), "long_v_powers": list(map(str, long_v))})

    require(F(379, 228) - F(31, 19) == F(7, 228), "saving over previous raw exponent")
    require(F(25, 12) - F(31, 19) == F(103, 228), "saving over classical exponent")
    require(F(1) + F(24, 19) * F(1, 2) == F(31, 19), "angular example")
    require(F(1) + F(4, 3) * F(1, 2) == F(5, 3), "counting example")
    require(F(19, 24) > F(114, 151), "larger arithmetic row-height range")
    return {"regimes": reports, "angular_transition_h": "19/44", "counting_transition_h": "3/8",
            "angular_example_exponent": "31/19", "counting_example_exponent": "5/3",
            "saving_over_previous_raw_exponent": "7/228", "saving_over_classical_exponent": "103/228"}


def check_a2_exponents_and_overlap():
    # Correction-label coordinates u=Nc, v=Nd, w=Ne.
    at = (F(-1), F(-2), F(-2))
    bt = (F(-2), F(-1), F(-2))
    ft = (F(0), F(0), F(1))
    qt = (F(1), F(1), F(0))
    rt = times(F(1, 3), bt)
    exterior = (F(-1), F(-1), F(-3, 2))
    normalization = plus((F(1, 2),) * 3, times(F(1, 2), plus(at, bt)))
    require(normalization == exterior, "A2 normalized projection weight")
    expected = ((F(-3, 2), F(-2), F(-5, 2)),
                (F(-1), F(-3, 2), F(-2)),
                (F(-3, 2), F(-13, 6), F(-5, 2)),
                (F(-1), F(-1), F(-3, 2)),
                (F(-3, 2), F(-2), F(-5, 2)),
                (F(-4, 3), F(-5, 3), F(-13, 6)))
    checks = 0
    for beta in (F(1), F(11, 12), F(3, 4)):
        kappa = F(9, 2) - 3 * beta
        energies = [
            at,
            plus(plus(ft, qt), plus(at, plus(times(beta - F(3, 2), bt), times(kappa, rt)))),
            plus(plus(times(F(2, 3), ft), times(F(1, 3), qt)),
                 plus(times(F(4, 3), at), plus(times(F(-2, 3), bt), times(F(2), rt)))),
            (F(0), F(0), F(0)),
            plus(plus(at, bt), times(F(-3), rt)),
            plus(times(F(2, 3), plus(at, bt)), times(F(-2), rt)),
        ]
        require(energies[1] == (F(0), F(-1), F(-1)), ("beta cancellation in A2 angular child", beta))
        require(energies[2] == (F(-1), F(-7, 3), F(-2)), "A2 mixed child")
        for row, target in zip(energies, expected):
            norm_exponents = plus(exterior, times(F(1, 2), row))
            require(norm_exponents == target, ("A2 exterior-weighted norm exponents", beta, row))
            require(max(norm_exponents) <= -1, "A2 norm summation has growing ideal power")
            checks += 1
    harmonic_counts = [sum(exponent == -1 for exponent in row) for row in expected]
    require(harmonic_counts == [0, 1, 0, 2, 0, 0], "A2 harmonic norm sums")

    overlap_checks = 0
    for q0, f0, c, d, e in product((0, 1), repeat=5):
        if c + d + e > 1 or (c or d or e) and (q0 or f0):
            continue
        qt_flag = q0 or c or d or e
        ft_flag = f0 or e
        child_effective = qt_flag and not ft_flag
        expected_effective = (q0 and not f0) or c or d
        require(child_effective == expected_effective, ("A2 q/f overlap removal", q0, f0, c, d, e))
        overlap_checks += 1
    return {"correction_scale_vectors": {"A_t": list(map(str, at)), "B_t": list(map(str, bt)),
                                          "R_t": list(map(str, rt))},
            "six_exterior_weighted_norm_triples": [list(map(str, row)) for row in expected],
            "norm_exponent_checks": checks, "harmonic_ideal_sums_per_term": harmonic_counts,
            "one_prime_A2_overlap_checks": overlap_checks,
            "scope": "Exact normalization and exponent arithmetic; this does not prove the child analytic theorem."}


def main():
    report = {
        "scope": "Finite exact arithmetic and rational exponents only; no numerical certification of analytic mean-square bounds.",
        "manuscripts": ["MIXED_LABEL_COMPLETION.md", "SIXTH_POWER_STRATIFIED_INVERSE.md",
                        "ANISOTROPIC_A2_NORM_TRANSFER.md"],
        "local_character_identities": check_local_label_identities(),
        "sixth_power_strata": check_valuation_strata(),
        "local_energy_and_valuation_tables": check_local_energy_exponents(),
        "finite_masked_cube_inverse": check_finite_masked_cube_inverse(),
        "stratified_optimization": check_optimization_and_v_exponents(),
        "A2_normalization_and_exponents": check_a2_exponents_and_overlap(),
    }
    payload = json.dumps(report, indent=2) + "\n"
    Path(__file__).with_name("mixed_stratified_checks.json").write_text(payload)
    print(json.dumps({"status": "PASS", "output": "mixed_stratified_checks.json",
                      "sections": len(report) - 2,
                      "scope": report["scope"]}, indent=2))


if __name__ == "__main__":
    main()
