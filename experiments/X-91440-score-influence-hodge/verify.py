#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
import argparse
import json


def pi_frac(N, k):
    return Fraction(6 * (k + 1) * (N - k + 1),
                    (N + 1) * (N + 2) * (N + 3))


def lam(N, k):
    return (k + 2) * (N - k)


def mu_rate(N, k):
    return k * (N - k + 2)


def check_mass_fraction():
    checks = 0
    wp44, ws44 = Fraction(1, 2), Fraction(1)
    wp41, ws41 = Fraction(5), Fraction(7)
    assert wp44 == Fraction(1, 2); checks += 1
    assert ws44 == 1; checks += 1
    assert wp41 == 5; checks += 1
    assert ws41 == 7; checks += 1

    target_a = wp44
    target_b = Fraction(1, 10) * wp41
    score_a = ws44
    score_b = Fraction(1, 10) * ws41
    assert target_a == target_b == Fraction(1, 2); checks += 1
    assert target_a / (target_a + target_b) == Fraction(1, 2); checks += 1
    assert score_a / (score_a + score_b) == Fraction(10, 17); checks += 1
    assert score_a > Fraction(1, 2) * (score_a + score_b); checks += 1
    return checks


def capped_geom_probs(p, cap):
    probs = [Fraction(p - 1, p ** (k + 1)) for k in range(cap)]
    probs.append(Fraction(1, p ** cap))
    assert sum(probs) == 1
    return probs


def state_probability(state, probs):
    ans = Fraction(1)
    for j, e in enumerate(state):
        ans *= probs[j][e]
    return ans


def doob_check(primes, caps, weights, cutoff):
    probs = [capped_geom_probs(p, cap) for p, cap in zip(primes, caps)]
    states = list(product(*[range(cap + 1) for cap in caps]))

    def G(state):
        value = Fraction(1)
        for p, e in zip(primes, state):
            if e > 0:
                value *= Fraction(p - 1, p)
        return value

    def H(state):
        return Fraction(max(0, cutoff - sum(w * e for w, e in zip(weights, state))))

    g_values = [G(state) for state in states]
    h_values = [H(state) for state in states]

    def expectation(values):
        return sum((state_probability(state, probs) * value
                    for state, value in zip(states, values)), Fraction(0))

    eg = expectation(g_values)
    eh = expectation(h_values)
    cov = expectation([g * h for g, h in zip(g_values, h_values)]) - eg * eh

    cond_g = [{(): eg}]
    cond_h = [{(): eh}]
    for j in range(1, len(primes) + 1):
        cg, ch = {}, {}
        for prefix in {state[:j] for state in states}:
            total_g = Fraction(0)
            total_h = Fraction(0)
            total_p = Fraction(0)
            for state, gv, hv in zip(states, g_values, h_values):
                if state[:j] != prefix:
                    continue
                prob = Fraction(1)
                for index in range(j, len(primes)):
                    prob *= probs[index][state[index]]
                total_g += prob * gv
                total_h += prob * hv
                total_p += prob
            assert total_p == 1
            cg[prefix] = total_g
            ch[prefix] = total_h
        cond_g.append(cg)
        cond_h.append(ch)

    terms = []
    for j in range(1, len(primes) + 1):
        term = Fraction(0)
        for state in states:
            prob = state_probability(state, probs)
            dg = cond_g[j][state[:j]] - cond_g[j - 1][state[:j - 1]]
            dh = cond_h[j][state[:j]] - cond_h[j - 1][state[:j - 1]]
            term += prob * dg * dh
        assert term >= 0
        terms.append(term)
    assert sum(terms) == cov
    return 1 + len(terms)


def hodge_check(N):
    checks = 0
    pi = [pi_frac(N, k) for k in range(N + 1)]
    assert sum(pi) == 1; checks += 1

    conductance = []
    for k in range(N):
        ck = Fraction(1, 4) * pi[k] * lam(N, k)
        assert ck == Fraction(1, 4) * pi[k + 1] * mu_rate(N, k + 1); checks += 1
        assert ck > 0; checks += 1
        conductance.append(ck)

    current = [Fraction((k + 1) * (k + 2) - 3, N + 3) for k in range(N)]
    test = [Fraction((k + 1) ** 3 - 2 * (k + 1), N + 2)
            for k in range(N + 1)]

    divergence = []
    for k in range(N + 1):
        left = current[k - 1] if k > 0 else Fraction(0)
        right = current[k] if k < N else Fraction(0)
        divergence.append((left - right) / pi[k])

    assert sum((pi[k] * divergence[k] for k in range(N + 1)), Fraction(0)) == 0; checks += 1
    inner = sum((pi[k] * divergence[k] * test[k] for k in range(N + 1)), Fraction(0))
    edge = sum((current[k] * (test[k + 1] - test[k]) for k in range(N)), Fraction(0))
    assert inner == edge; checks += 1

    potential = [Fraction(0)]
    for k in range(N):
        potential.append(potential[-1] + current[k] / conductance[k])

    minus_generator = []
    for k in range(N + 1):
        value = Fraction(0)
        if k < N:
            value += Fraction(lam(N, k), 4) * (potential[k + 1] - potential[k])
        if k > 0:
            value += Fraction(mu_rate(N, k), 4) * (potential[k - 1] - potential[k])
        minus_generator.append(-value)
    assert minus_generator == divergence; checks += 1

    mixed_energy = sum((conductance[k]
                        * (potential[k + 1] - potential[k])
                        * (test[k + 1] - test[k])
                        for k in range(N)), Fraction(0))
    assert mixed_energy == edge; checks += 1

    resistance = sum((current[k] ** 2 / conductance[k] for k in range(N)), Fraction(0))
    potential_energy = sum((conductance[k] * (potential[k + 1] - potential[k]) ** 2
                            for k in range(N)), Fraction(0))
    assert resistance == potential_energy; checks += 1

    test_energy = sum((conductance[k] * (test[k + 1] - test[k]) ** 2
                       for k in range(N)), Fraction(0))
    assert edge + Fraction(1, 2) * (resistance + test_energy) >= 0; checks += 1

    divergence_norm = sum((pi[k] * divergence[k] ** 2 for k in range(N + 1)), Fraction(0))
    assert resistance <= divergence_norm; checks += 1
    return checks


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json")
    args = parser.parse_args()

    mass_checks = check_mass_fraction()
    doob_checks = 0
    for config in [
        ([2, 3, 5], [3, 2, 2], [1, 2, 3], 12),
        ([2, 5, 7], [2, 3, 2], [2, 1, 4], 13),
        ([3, 5, 11], [3, 2, 2], [1, 3, 2], 11),
    ]:
        doob_checks += doob_check(*config)

    hodge_checks = sum(hodge_check(N) for N in range(1, 33))

    result = {
        "brownian_theta_dtn_proved": False,
        "candidate_pr407_proved": False,
        "classification": "PASS_X_91440_SCORE_INFLUENCE_HODGE",
        "doob_influence_checks": doob_checks,
        "green_density_proved": False,
        "hahn_hodge_checks": hodge_checks,
        "mass_fraction_checks": mass_checks,
        "rh_proved": False,
        "scope": "exact two-ledger counterexample, finite product-martingale covariance identities, and finite Hahn Hodge algebra only",
    }
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json:
        with open(args.json, "w", encoding="utf-8") as handle:
            handle.write(text)
    print(text, end="")


if __name__ == "__main__":
    main()
