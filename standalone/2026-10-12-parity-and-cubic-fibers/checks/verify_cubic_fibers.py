#!/usr/bin/env python3
"""Exact finite guards for CUBIC_FIBERS_AND_RIESZ_PRODUCTS.md.

Standard library only. This is finite algebra and native residue arithmetic,
not a verification of any infinite moment, probability-law dichotomy, or zero
statement. All acceptance checks use explicit exceptions, also under python -O.
"""

from argparse import ArgumentParser
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
import json
from math import prod
from pathlib import Path


COUNTS = Counter()


def check(section, condition, message):
    COUNTS[section] += 1
    if not condition:
        raise RuntimeError(section + ": " + message)


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def mul(x, y):
    # omega^2 = -1 - omega.
    return (x[0] * y[0] - x[1] * y[1],
            x[0] * y[1] + x[1] * y[0] - x[1] * y[1])


def scale(a, x):
    return (a * x[0], a * x[1])


def conjugate(x):
    return (x[0] - x[1], -x[1])


def norm(x):
    return x[0] ** 2 - x[0] * x[1] + x[1] ** 2


def power(x, n):
    if n < 0:
        raise ValueError("only nonnegative powers used")
    result = (1, 0)
    for _ in range(n):
        result = mul(result, x)
    return result


ONE = (1, 0)
ZERO = (0, 0)
ZETA = (1, 1)  # exp(pi i/3) = 1 + omega.
ROOTS = tuple(power(ZETA, j) for j in range(6))
PRIMES = ((7, 2), (13, 3), (19, 7))  # ideals (p, omega-root).
NORMS = tuple(p for p, _ in PRIMES)
MASKS = tuple(range(1 << len(PRIMES)))
STATES = tuple(product((-1, 1), repeat=len(PRIMES)))
MODULUS = prod(NORMS)


def bits(mask):
    return tuple(i for i in range(len(PRIMES)) if mask & (1 << i))


def ideal_norm(mask):
    return prod(NORMS[i] for i in bits(mask))


def eval_mod(x, datum):
    p, root = datum
    return (x[0] + x[1] * root) % p


def sextic(x, datum):
    p, root = datum
    v = eval_mod(x, datum)
    if v == 0:
        return ZERO
    residue = pow(v, (p - 1) // 6, p)
    zeta_mod = (1 + root) % p
    candidates = [j for j in range(6) if pow(zeta_mod, j, p) == residue]
    if len(candidates) != 1:
        raise RuntimeError("sextic exponent did not have exactly one match")
    return ROOTS[candidates[0]]


def qchar(x, datum):
    value = power(sextic(x, datum), 3)
    if value not in (ZERO, ONE, (-1, 0)):
        raise RuntimeError("quadratic projection left {0,+1,-1}")
    return value[0]


def cchar(x, datum):
    return power(sextic(x, datum), 4)


def chi_column(x, mask):
    value = ONE
    for i in bits(mask):
        value = mul(value, sextic(x, PRIMES[i]))
    return value


def zmonomial(z, mask):
    return prod(z[i] for i in bits(mask))


def polynomial(coefficients, z):
    value = ZERO
    for mask, coefficient in coefficients.items():
        value = add(value, scale(zmonomial(z, mask), coefficient))
    return value


def probability(z, biases):
    return prod((1 + z[i] * biases[i]) / 2 for i in range(len(PRIMES)))


def expectation(values, biases):
    return sum(probability(z, biases) * values[z] for z in STATES)


def density(z, target, base):
    return prod((1 + target[i] * z[i]) / (1 + base[i] * z[i])
                for i in range(len(PRIMES)))


def centered(z, base, mask):
    return prod(z[i] - base[i] for i in bits(mask))


def variance_product(base, mask):
    return prod(1 - base[i] ** 2 for i in bits(mask))


def projected_density(z, target, base, selected):
    value = F(0)
    for mask in selected:
        coefficient = prod((target[i] - base[i]) / (1 - base[i] ** 2)
                           for i in bits(mask))
        value += coefficient * centered(z, base, mask)
    return value


def comparison_weight(target, base, mask):
    return prod((target[i] - base[i]) ** 2 / (1 - base[i] ** 2)
                for i in bits(mask))


def crt_lift(residues):
    value = 0
    for residue, p in zip(residues, NORMS):
        complementary = MODULUS // p
        value += residue * complementary * pow(complementary, -1, p)
    return value % MODULUS


def arithmetic_checks():
    for p, root in PRIMES:
        check("native_field_setup", (root * root + root + 1) % p == 0,
              "omega root")
        check("native_field_setup",
              len({pow((1 + root) % p, j, p) for j in range(6)}) == 6,
              "chosen zeta has order six")
        local_counts = Counter()
        for residue in range(p):
            x = (residue, 0)
            q = qchar(x, (p, root))
            c = cchar(x, (p, root))
            check("native_field_setup", sextic(x, (p, root)) == scale(q, c),
                  "sextic = quadratic times cubic, including zero")
            if residue:
                local_counts[(q, c)] += 1
        check("native_field_setup", len(local_counts) == 6,
              "six local phase pairs")
        for number in local_counts.values():
            check("native_field_setup", number == (p - 1) // 6,
                  "equal quadratic/cubic local phase multiplicity")

    box = tuple(product(range(-3, 4), repeat=2))
    for u in box:
        check("native_ring", mul(u, conjugate(u)) == (norm(u), 0),
              "conjugation and norm")
        check("native_ring", norm(power(u, 3)) == norm(u) ** 3,
              "cube norm")
        for a in box:
            check("native_ring", norm(mul(u, a)) == norm(u) * norm(a),
                  "norm multiplicativity")
            ua3 = mul(u, power(a, 3))
            for datum in PRIMES:
                check("native_cube_masks",
                      sextic(ua3, datum) ==
                      scale(qchar(a, datum), sextic(u, datum)),
                      "native cube action")
                check("native_cube_masks",
                      cchar(ua3, datum) ==
                      scale(int(eval_mod(a, datum) != 0), cchar(u, datum)),
                      "cubic phase and literal exclusion")
                check("native_cube_masks",
                      qchar(ua3, datum) == qchar(u, datum) * qchar(a, datum),
                      "quadratic phase")

    lifts = set()
    joint_counts = Counter()
    q_counts = Counter()
    units = []
    for residues in product(*(range(p) for p in NORMS)):
        a = crt_lift(residues)
        lifts.add(a)
        for i, p in enumerate(NORMS):
            check("native_crt", a % p == residues[i], "CRT coordinate")
        if all(residues):
            units.append(a)
            q = tuple(qchar((a, 0), datum) for datum in PRIMES)
            c = tuple(cchar((a, 0), datum) for datum in PRIMES)
            q_counts[q] += 1
            joint_counts[(q, c)] += 1
    check("native_crt", lifts == set(range(MODULUS)), "complete CRT coverage")
    check("native_crt", len(units) == prod(p - 1 for p in NORMS),
          "exact unit count")
    check("native_crt", len(joint_counts) == 6 ** len(PRIMES),
          "all quadratic/cubic profiles")
    for count in joint_counts.values():
        check("native_crt", count == prod((p - 1) // 6 for p in NORMS),
              "joint phase independence")
    for z in STATES:
        check("native_crt", q_counts[z] == len(units) // len(STATES),
              "quadratic signs independent on complete unit set")
    return units


def native_coefficients(u, selected=MASKS):
    coefficients = {}
    for mask in selected:
        # Positive rational norm weights, with fixed multiplicative C6 nu.
        weight = F(1 + 3 * mask % 7, mask + 2)
        nu = ROOTS[sum(i + 1 for i in bits(mask)) % 6]
        mu = (-1) ** len(bits(mask))
        coefficients[mask] = scale(mu * weight, mul(nu, chi_column(u, mask)))
    return coefficients


def native_value(u, selected=MASKS):
    return polynomial(native_coefficients(u, selected), (1, 1, 1))


def riesz_checks(units):
    biases_list = (
        tuple(F(1) for _ in PRIMES),
        tuple(F(1, p) for p in NORMS),
        tuple(F(1, p * p) for p in NORMS),
        (F(1, 2), F(2, 3), F(3, 4)),
    )
    rows = ((1, 0), (-1, 0), (2, 1), (3, -1), (7, 0), (13, 0))
    denominator = len(units)
    for biases in biases_list:
        weighted_q = Counter()
        for a in units:
            z = tuple(qchar((a, 0), datum) for datum in PRIMES)
            riesz = prod(1 + biases[i] * z[i] for i in range(len(PRIMES)))
            weighted_q[z] += riesz
        check("riesz_native_law", sum(weighted_q.values()) == denominator,
              "complete Riesz normalization")
        for z in STATES:
            check("riesz_native_law",
                  weighted_q[z] / denominator == probability(z, biases),
                  "native quadratic distribution under positive Riesz weight")

    for u in rows:
        coefficients = native_coefficients(u)
        formal_norms = {z: norm(polynomial(coefficients, z)) for z in STATES}
        complete_sums = {
            (j, k): F(0)
            for j in range(len(biases_list)) for k in (1, 2, 3)
        }
        for a in units:
            z = tuple(qchar((a, 0), datum) for datum in PRIMES)
            ua3 = mul(u, power((a, 0), 3))
            actual_norm = norm(native_value(ua3))
            check("riesz_native_moment", actual_norm == formal_norms[z],
                  "native full polynomial on cube row")
            for j, biases in enumerate(biases_list):
                riesz = prod(1 + biases[i] * z[i] for i in range(len(PRIMES)))
                for k in (1, 2, 3):
                    complete_sums[(j, k)] += riesz * actual_norm ** k
        for j, biases in enumerate(biases_list):
            for k in (1, 2, 3):
                formal = expectation({z: formal_norms[z] ** k for z in STATES},
                                     biases)
                check("riesz_native_moment",
                      complete_sums[(j, k)] / denominator == formal,
                      "native Riesz moment identity")


def projection_checks():
    pairs = (
        (tuple(F(1) for _ in PRIMES), tuple(F(1, p) for p in NORMS)),
        (tuple(F(1, p) for p in NORMS),
         tuple(F(1, p * p) for p in NORMS)),
        ((F(1, 2), F(2, 3), F(3, 4)), (F(1, 5), F(1, 7), F(1, 11))),
    )
    fixtures = []
    for pair_id, (target, base) in enumerate(pairs):
        likelihood = {z: density(z, target, base) for z in STATES}
        gamma = prod(1 + (target[i] - base[i]) ** 2 / (1 - base[i] ** 2)
                     for i in range(len(PRIMES)))
        check("likelihood", expectation(likelihood, base) == 1,
              "likelihood mean one")
        check("likelihood", expectation({z: likelihood[z] ** 2 for z in STATES},
                                        base) == gamma,
              "exact full chi-square product")
        for z in STATES:
            expanded = prod(
                1 + (target[i] - base[i]) * (z[i] - base[i]) /
                (1 - base[i] ** 2) for i in range(len(PRIMES)))
            check("likelihood", likelihood[z] == expanded,
                  "centered local likelihood expansion")
            check("likelihood",
                  probability(z, base) * likelihood[z] ==
                  probability(z, target), "pointwise Radon-Nikodym identity")
        for mask in MASKS:
            for other in MASKS:
                inner = expectation({
                    z: centered(z, base, mask) * centered(z, base, other)
                    for z in STATES}, base)
                expected = variance_product(base, mask) if mask == other else 0
                check("centered_basis", inner == expected,
                      "exact centered orthogonality")
        for cutoff in (1, 7, 10, 13, 19, 50, 91, 133, 247, 400, 1729):
            selected = tuple(mask for mask in MASKS if ideal_norm(mask) <= cutoff)
            for mask in selected:
                for submask in MASKS:
                    if submask & mask == submask:
                        check("projection", submask in selected,
                              "divisor-closed cutoff")
            projected = {
                z: projected_density(z, target, base, selected) for z in STATES
            }
            ksq = sum(comparison_weight(target, base, mask) for mask in selected)
            check("projection",
                  expectation({z: projected[z] ** 2 for z in STATES}, base) == ksq,
                  "projected density norm equals truncated product sum")
            check("projection", expectation(projected, target) == ksq,
                  "extremizer attains the linear functional norm")
            for mask in selected:
                residual_inner = expectation({
                    z: (likelihood[z] - projected[z]) * centered(z, base, mask)
                    for z in STATES}, base)
                check("projection", residual_inner == 0,
                      "orthogonal projection against each selected basis element")
            check("projection", ksq <= gamma, "projected cost never exceeds full")
            fixtures.append({"pair": pair_id, "cutoff": cutoff,
                             "dimension": len(selected), "K_squared": str(ksq)})
        # A complex exact test of the projected Cauchy inequality.
        cutoff = 133
        selected = tuple(mask for mask in MASKS if ideal_norm(mask) <= cutoff)
        test = {
            z: sum((F(mask + 1, mask + 2) * zmonomial(z, mask)
                    for mask in selected), F(0))
            for z in STATES
        }
        test_imag = {
            z: sum((F(2 - mask, mask + 3) * zmonomial(z, mask)
                    for mask in selected), F(0))
            for z in STATES
        }
        # Exact ordinary complex pairs here, independently of Eisenstein basis.
        mean_re, mean_im = expectation(test, target), expectation(test_imag, target)
        test_norm = expectation({z: test[z] ** 2 + test_imag[z] ** 2 for z in STATES},
                                base)
        ksq = sum(comparison_weight(target, base, mask) for mask in selected)
        check("projection", mean_re ** 2 + mean_im ** 2 <= ksq * test_norm,
              "complex projected Cauchy inequality")
    return fixtures


def floor_and_frequency_checks():
    # This exact finite window selects only the prime columns of norm 13,19.
    window = tuple(mask for mask in MASKS if 10 < ideal_norm(mask) < 20)
    check("prime_floor", window == (2, 4), "literal upper-support prime window")
    biases = tuple(F(1, p) for p in NORMS)
    rows = ((1, 0), (7, 0), (13, 0), (19, 0), (2, 1))
    for u in rows:
        coefficients = native_coefficients(u, window)
        centered_coefficients = {}
        for mask in MASKS:
            coefficient = ZERO
            for column, value in coefficients.items():
                if mask & column == mask:
                    remaining = column ^ mask
                    factor = prod(biases[i] for i in bits(remaining))
                    coefficient = add(coefficient, scale(factor, value))
            centered_coefficients[mask] = coefficient
        for prime_mask in (1, 2, 4):
            check("prime_floor",
                  centered_coefficients[prime_mask] ==
                  coefficients.get(prime_mask, ZERO),
                  "prime centered coefficient equals original on upper window")
        moment2 = expectation({
            z: norm(polynomial(coefficients, z)) for z in STATES}, biases)
        orthogonal = sum(norm(value) * variance_product(biases, mask)
                         for mask, value in centered_coefficients.items())
        check("prime_floor", moment2 == orthogonal,
              "exact centered second-moment decomposition")
        prime_variance = sum(norm(coefficients[mask]) *
                             variance_product(biases, mask) for mask in window)
        check("prime_floor", moment2 >= prime_variance,
              "positive prime-chaos floor")
        for k in (1, 2, 3):
            moment = expectation({
                z: norm(polynomial(coefficients, z)) ** k for z in STATES}, biases)
            check("prime_floor", moment >= moment2 ** k,
                  "higher moment Jensen")
    for k in (1, 2, 3):
        for columns in product(window, repeat=2 * k):
            radical = 0
            for mask in columns:
                radical ^= mask
            check("moment_frequency",
                  ideal_norm(radical) <= prod(ideal_norm(mask) for mask in columns),
                  "parity radical divides Hermitian total product")
            check("moment_frequency", ideal_norm(radical) <= 20 ** (2 * k),
                  "actual moment frequency cutoff")

    target = (F(1), F(1), F(1))
    for k in (1, 2):
        cutoff = 20 ** (2 * k)
        ksq = sum(comparison_weight(target, biases, mask)
                  for mask in MASKS if ideal_norm(mask) <= cutoff)
        total_target = F(0)
        total_doubled_base = F(0)
        for u in rows:
            coeff = native_coefficients(u, window)
            values = {z: norm(polynomial(coeff, z)) for z in STATES}
            total_target += expectation({z: values[z] ** k for z in STATES}, target)
            total_doubled_base += expectation(
                {z: values[z] ** (2 * k) for z in STATES}, biases)
        check("moment_frequency",
              total_target ** 2 <= len(rows) * ksq * total_doubled_base,
              "row-summed reverse inequality uses doubled order")

    # Exact exponent identities only; these are not asymptotic estimates.
    exponent_fixtures = []
    for s in (F(0), F(1, 4), F(3, 8), F(1, 2), F(2, 3)):
        for k in range(1, 9):
            cost = k * max(F(1) - 2 * s, F(0))
            exponent_fixtures.append({"s": str(s), "k": k, "comparison_cost": str(cost)})
            if s < F(1, 2):
                check("exponent_algebra", cost / k == 1 - 2 * s,
                      "linear order cost below one half")
            else:
                check("exponent_algebra", cost == 0, "no power above endpoint")
    return exponent_fixtures


def adversarial_checks():
    datum = PRIMES[0]
    a, u = (7, 0), ONE
    check("adversarial_guards", cchar(mul(u, power(a, 3)), datum) == ZERO and
          cchar(u, datum) != ZERO,
          "dropping the auxiliary nonunit mask must be detected")
    a = (2, 1)
    check("adversarial_guards", norm(a) <= 10 < norm(power(a, 3)),
          "linear auxiliary budget does not pay cubic row height")
    witnesses = [x for x in range(1, 7) if qchar((x, 0), datum) == -1]
    if not witnesses:
        raise RuntimeError("no quadratic nonresidue witness")
    a = (witnesses[0], 0)
    check("adversarial_guards",
          sextic(power(a, 3), datum) != sextic(power(a, 6), datum),
          "cube and sixth-power actions are different")
    base = tuple(F(1, p) for p in NORMS)
    target = (F(1), F(1), F(1))
    wrong_target = tuple(-x for x in target)
    selected = (0, 1)
    test = {z: (2 + z[0]) ** 2 for z in STATES}
    check("adversarial_guards",
          expectation(test, target) != expectation(test, wrong_target),
          "reversing the Riesz sign changes the mean law")
    gamma = prod(1 + (target[i] - base[i]) ** 2 / (1 - base[i] ** 2)
                 for i in range(len(PRIMES)))
    ksq = sum(comparison_weight(target, base, mask) for mask in selected)
    check("adversarial_guards", ksq < gamma,
          "full product and truncated-space cost differ")
    # Without downward closure, replacing a Walsh monomial by its centered
    # version changes the one-dimensional space.
    walsh = {z: z[0] * z[1] for z in STATES}
    centered_pair = {z: (z[0] - base[0]) * (z[1] - base[1]) for z in STATES}
    ratios = {centered_pair[z] / walsh[z] for z in STATES}
    check("adversarial_guards", len(ratios) > 1,
          "non-divisor-closed basis replacement is invalid")
    # A centered coefficient at a small prime contains its proper multiples.
    full = native_coefficients(ONE)
    small_prime_centered = ZERO
    for column, value in full.items():
        if column & 1:
            factor = prod(base[i] for i in bits(column ^ 1))
            small_prime_centered = add(small_prime_centered, scale(factor, value))
    check("adversarial_guards", small_prime_centered != full[1],
          "prime coefficient simplification fails without upper support")
    zero_noise = (F(1), F(1), F(1))
    check("adversarial_guards",
          all(variance_product(zero_noise, 1 << i) == 0 for i in range(3)),
          "positive-noise floor cannot be asserted at t=0")
    return 8


def locate_note(explicit):
    if explicit:
        return Path(explicit).resolve()
    here = Path(__file__).resolve().parent
    candidates = (
        here / "attack4_amplification.md",
        here / "CUBIC_FIBERS_AND_RIESZ_PRODUCTS.md",
        here.parent / "CUBIC_FIBERS_AND_RIESZ_PRODUCTS.md",
    )
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    raise RuntimeError("supply --note with the exact proof-note path")


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--note")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    note_path = locate_note(args.note)
    units = arithmetic_checks()
    riesz_checks(units)
    projections = projection_checks()
    exponents = floor_and_frequency_checks()
    adversarial_count = adversarial_checks()
    report = {
        "status": "PASS",
        "arithmetic": "EXACT_INTEGER_AND_RATIONAL",
        "scope": [
            "Eisenstein ring and conjugation arithmetic on the displayed finite box",
            "actual sextic/quadratic/cubic values modulo the three stated prime ideals",
            "complete CRT enumeration, including native zero-mask guards",
            "positive Riesz representation of finite polynomial moments",
            "exact finite Radon-Nikodym products and centered-chaos projections",
            "upper-support prime variance floor and doubled-order reverse inequality",
            "finite rational exponent identities and explicit adversarial guards",
        ],
        "not_verified": [
            "infinite moment estimates or an RH/zero-free conclusion",
            "the infinite product-measure dichotomy by finite enumeration",
            "asymptotic prime-count subsequences or the Mellin analytic argument",
            "uniform pointwise PW_B or any imported analytic theorem",
            "an incomplete physical row average approximating a complete residue system",
            "optimality on the special nonnegative Mobius moment cone",
        ],
        "note_sha256": sha256(note_path.read_bytes()).hexdigest(),
        "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "prime_ideals": [
            {"rational_prime": p, "omega_residue": root, "norm": p}
            for p, root in PRIMES
        ],
        "crt_modulus_norm": MODULUS,
        "crt_unit_classes": len(units),
        "native_ring_box": {"coordinate_min": -3, "coordinate_max": 3},
        "physical_test_rows": 6,
        "adversarial_guards": adversarial_count,
        "predicates_by_section": dict(sorted(COUNTS.items())),
        "total_predicates": sum(COUNTS.values()),
        "projection_fixtures": projections,
        "exponent_fixtures": exponents,
    }
    output = Path(args.output)
    output.write_text(json.dumps(report, sort_keys=True, indent=2) + "\n",
                      encoding="utf-8")
    print(json.dumps({"status": report["status"],
                      "total_predicates": report["total_predicates"],
                      "report_sha256": sha256(output.read_bytes()).hexdigest()},
                     sort_keys=True))


if __name__ == "__main__":
    main()
