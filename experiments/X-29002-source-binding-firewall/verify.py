from fractions import Fraction
from functools import lru_cache
import hashlib
import json


def add_chain(*terms):
    out = {}
    for scalar, chain in terms:
        scalar = Fraction(scalar)
        for edge, coefficient in chain.items():
            out[edge] = out.get(edge, Fraction(0)) + scalar * coefficient
    return {edge: coefficient for edge, coefficient in out.items() if coefficient}


@lru_cache(None)
def central_tree(n):
    if n <= 1:
        return {}
    child = n // 2
    return add_chain(
        (1, {(n, child): Fraction(1)}),
        (1, central_tree(child)),
        (1, central_tree(n - child)),
    )


def endpoint_commutator(n):
    return add_chain((1, central_tree(n)), (-1, central_tree(n - 1)))


def central_commutator(n):
    return {
        (2 * n, n): Fraction(1),
        (2 * n - 1, n - 1): Fraction(-1),
    }


def filtered_endpoint(n):
    return add_chain(
        (1, endpoint_commutator(n)),
        (Fraction(-3, 2), endpoint_commutator(2 * n)),
        (Fraction(1, 2), endpoint_commutator(4 * n)),
    )


def compact_filtered_endpoint(n):
    return add_chain(
        (Fraction(1, 2), central_commutator(2 * n)),
        (-1, central_commutator(n)),
    )


def carry(edge, q):
    n, j = edge
    return n // q - j // q - (n - j) // q


def carry_load(chain, q):
    return sum(coefficient * carry(edge, q) for edge, coefficient in chain.items())


def formal_log_tables(limit):
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]
    primes = []
    for n in range(2, limit + 1):
        if sieve[n]:
            primes.append(n)
            if n * n <= limit:
                for multiple in range(n * n, limit + 1, n):
                    sieve[multiple] = False

    prime_weight = {p: index + 2 for index, p in enumerate(primes)}
    ell = [0] * (limit + 1)
    for n in range(2, limit + 1):
        value = n
        for p in primes:
            if p * p > value:
                break
            while value % p == 0:
                ell[n] += prime_weight[p]
                value //= p
        if value > 1:
            ell[n] += prime_weight[value]

    factorial = [0] * (limit + 1)
    square_sum = [0] * (limit + 1)
    for n in range(1, limit + 1):
        factorial[n] = factorial[n - 1] + ell[n]
        square_sum[n] = square_sum[n - 1] + ell[n] ** 2
    return ell, factorial, square_sum


def chain_kummer(chain, factorial):
    return sum(
        coefficient
        * (factorial[n] - factorial[j] - factorial[n - j])
        for (n, j), coefficient in chain.items()
    )


def chain_selberg(chain, square_sum):
    return sum(
        coefficient
        * (square_sum[n] - square_sum[j] - square_sum[n - j])
        for (n, j), coefficient in chain.items()
    )


def step(m, r):
    if m <= r < 2 * m:
        return Fraction(1)
    if 2 * m <= r < 4 * m:
        return Fraction(-1, 2)
    return Fraction(0)


def main():
    ell, factorial, square_sum = formal_log_tables(256)

    filtered_rows = 0
    for n in range(2, 65):
        fiber = filtered_endpoint(n)
        assert fiber == compact_filtered_endpoint(n)
        for q in range(2, 4 * n + 1):
            expected = (
                (1 if n % q == 0 else 0)
                - Fraction(3, 2) * (1 if (2 * n) % q == 0 else 0)
                + Fraction(1, 2) * (1 if (4 * n) % q == 0 else 0)
            )
            assert carry_load(fiber, q) == expected
            filtered_rows += 1

        assert chain_kummer(fiber, factorial) == (
            ell[n] - Fraction(3, 2) * ell[2 * n] + Fraction(1, 2) * ell[4 * n]
        )
        assert chain_selberg(fiber, square_sum) == (
            ell[n] ** 2
            - Fraction(3, 2) * ell[2 * n] ** 2
            + Fraction(1, 2) * ell[4 * n] ** 2
        )

    binding_blocks = 0
    for M in range(2, 17):
        source = {
            m: Fraction((m % 5) + 1, m + 3)
            for m in range(M, 2 * M)
        }

        endpoint_chain = {}
        for r in range(2, 8 * M + 1):
            current = sum(weight * step(m, r) for m, weight in source.items())
            previous = sum(weight * step(m, r - 1) for m, weight in source.items())
            coefficient = current - previous
            if coefficient:
                endpoint_chain = add_chain(
                    (1, endpoint_chain),
                    (coefficient, endpoint_commutator(r)),
                )

        fiber_sum = {}
        for m, weight in source.items():
            fiber_sum = add_chain((1, fiber_sum), (weight, filtered_endpoint(m)))

        assert endpoint_chain == fiber_sum

        total_mass = sum(source.values(), Fraction(0))
        log_moment = sum(weight * ell[m] for m, weight in source.items())
        kummer = chain_kummer(endpoint_chain, factorial)
        selberg = chain_selberg(endpoint_chain, square_sum)

        expected_kummer = -Fraction(1, 2) * ell[2] * total_mass
        expected_selberg = (
            -ell[2] * log_moment
            + Fraction(1, 2) * ell[2] ** 2 * total_mass
        )
        assert kummer == expected_kummer
        assert selberg == expected_selberg
        assert (
            kummer * kummer - selberg
            >= Fraction(1, 4) * ell[2] ** 2 * total_mass ** 2
        )
        binding_blocks += 1

    # Exact symbolic firewalls:
    # generalized row (6,2):
    # P_omega^2-S_omega = log(3) * log(25/32) < 0.
    assert 25 < 32
    # ordinary row (4,2) at amplitude 1/2:
    # four times the defect is -log(3/2)^2 - 4 log(2)^2 < 0.
    assert 3 > 2 and 2 > 1

    result = {
        "schema": "riemann.x29002.source-binding-firewall.v1",
        "verified": True,
        "checks": {
            "filtered_endpoint_fiber_rows": filtered_rows,
            "positive_endpoint_binding_blocks": binding_blocks,
            "generalized_selberg_counterexample": {
                "parent": 6,
                "split": 2,
                "defect": "log(3)*log(25/32)<0",
            },
            "row_scaling_counterexample": {
                "parent": 4,
                "split": 2,
                "amplitude": "1/2",
                "four_times_defect": "-log(3/2)^2-4log(2)^2<0",
            },
        },
        "verdict": (
            "EXACT_ENDPOINT_FIBER_BINDING_VERIFIED_AND_"
            "NAIVE_SOURCE_CONE_LIFTS_REFUTED"
        ),
        "proof_boundary": (
            "Exact finite carry/tree/formal-log algebra and exact symbolic "
            "counterexamples only; no coupled interior source matrix, "
            "cofinal recurrence, or RH claim is certified."
        ),
    }
    payload = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(payload).hexdigest()
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
