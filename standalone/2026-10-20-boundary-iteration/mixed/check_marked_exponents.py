"""Exact algebra checks for MARKED_CANONICAL_MEAN.md; not analytic proofs."""

from fractions import Fraction as F
from itertools import product
import json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def mu(exponents):
    return 0 if max(exponents) > 1 else (-1) ** sum(exponents)


def monomial(exponents, values):
    result = F(1)
    for exponent, value in zip(exponents, values):
        result *= value ** exponent
    return result


def residual(exponents, shifts):
    answer = tuple(a - b for a, b in zip(exponents, shifts))
    return answer if min(answer) >= 0 else None


def inverse_coefficient(exponents, values):
    return mu(exponents) * monomial(exponents, values)


def arithmetic_checks():
    # Formal Euler coefficients: norm factors are multiplicative monomials
    # and can be removed. Values 0 retain character zero extensions.
    count = 0
    repeated_power_witnesses = 0
    puncture = {0, 2}
    lists = ((0, 1), (2,))
    weights = (F(2, 3), F(-3, 5), F(4, 7))
    for values in product((F(0), F(1), F(-1)), repeat=3):
        for exponents in product(range(5), repeat=3):
            plain = inverse_coefficient(exponents, values)
            expected = plain if all(exponents[i] == 0 for i in puncture) else 0
            expanded = F(0)
            for powers in product(*(range(exponents[i] + 1) if i in puncture else (0,) for i in range(3))):
                remainder = residual(exponents, powers)
                expanded += monomial(powers, values) * inverse_coefficient(remainder, values)
            require(expanded == expected, "full puncture Euler identity")
            count += 1

            amplifier = 1
            masked = plain if exponents[amplifier] == 0 else F(0)
            previous = list(exponents)
            previous[amplifier] -= 1
            correction = F(0)
            if min(previous) >= 0 and previous[amplifier] == 0:
                correction = values[amplifier] * inverse_coefficient(tuple(previous), values)
            require(masked - correction == plain, "prime sixth-power amplifier identity")
            count += 1

            mark = F(1)
            for prime_list in lists:
                mark *= sum((weights[i] for i in prime_list if exponents[i]), F(0))
            expected_marked = plain * mark
            extracted = F(0)
            first_powers_only = F(0)
            for chosen in product(*lists):
                for powers in product(*(range(1, exponents[i] + 1) for i in chosen)):
                    shift = [0, 0, 0]
                    coefficient = F(1)
                    for i, power in zip(chosen, powers):
                        shift[i] += power
                        coefficient *= -weights[i] * values[i] ** power
                    remainder = residual(exponents, shift)
                    term = coefficient * inverse_coefficient(remainder, values)
                    extracted += term
                    if all(power == 1 for power in powers):
                        first_powers_only += term
            require(extracted == expected_marked, "complete divisor-mark extraction")
            repeated_power_witnesses += first_powers_only != expected_marked
            count += 1
    require(repeated_power_witnesses > 0, "truncating repeated primes must fail somewhere")
    return count, repeated_power_witnesses


def exponent_checks():
    # Substitute T0=D^2 F^2/K into K/(FD) times the three inverse branches.
    # Vectors have coordinates (log K, log D, log F, log P).
    root = (F(1), F(-1), F(-1), F(0))
    t0 = (F(-1), F(2), F(2), F(0))

    def add(*vectors):
        return tuple(sum(values, F(0)) for values in zip(*vectors))

    def scale(scalar, vector):
        return tuple(scalar * entry for entry in vector)

    direct = add(root, t0)
    first = add(root, scale(F(1, 6), t0), (F(0), F(5, 6), F(0), F(5, 6)))
    second = add(root, scale(F(1, 6), t0), (F(0), F(5, 9), F(0), F(5, 3)))
    require(direct == (0, 1, 1, 0), "DF substitution")
    require(first == (F(5, 6), F(1, 6), F(-2, 3), F(5, 6)), "first marked substitution")
    require(second == (F(5, 6), F(-1, 9), F(-2, 3), F(5, 3)), "second marked substitution")

    # At D=K,F=1 compare last branch to K P^(5/6).
    require(F(1) - (second[0] + second[1]) == F(5, 18), "balanced row difference")
    require(second[3] - F(5, 6) == F(5, 6), "balanced mark difference")
    require(F(5, 18) / F(5, 6) == F(1, 3), "P <= K^(1/3) gain range")

    # Requiring each marked branch <= D gives exactly source margins.
    require(first[0] / (1 - first[1]) == 1, "first canonical row margin")
    require(first[3] / (1 - first[1]) == 1, "first canonical prime margin")
    require(second[0] / (1 - second[1]) == F(3, 4), "second canonical row margin")
    require(second[3] / (1 - second[1]) == F(3, 2), "second canonical prime margin")

    # 0 <= 2g <= delta <= 5/6 suffices for positive overlong slopes.
    require(F(5, 3) - F(5, 6) == F(5, 6), "first overlong minimum slope")
    require(F(20, 9) - F(5, 6) == F(25, 18), "second overlong minimum slope")
    require(F(17, 12) - F(6, 5) == F(13, 60), "unchanged pure inverse edge gap")
    return 13


def main():
    identities, repeated_power_witnesses = arithmetic_checks()
    exponent_count = exponent_checks()
    print(json.dumps({
        "status": "pass",
        "exact_euler_identity_checks": identities,
        "first_power_truncation_counterexamples": repeated_power_witnesses,
        "exact_exponent_checks": exponent_count,
        "canonical_admission_region": ["d >= k+z", "4d >= 3k+6z"],
        "balanced_marked_gain": "K*P^(5/6) for P <= K^(1/3)",
        "global_zero_free_improvement": False,
        "analytic_inputs_verified_by_this_script": False,
    }, indent=2))


if __name__ == "__main__":
    main()
