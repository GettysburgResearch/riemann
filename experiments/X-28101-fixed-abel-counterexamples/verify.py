from fractions import Fraction
from math import comb


def mobius_sieve(limit: int) -> list[int]:
    mu = [0] * (limit + 1)
    mu[1] = 1
    primes: list[int] = []
    composite = [False] * (limit + 1)
    for n in range(2, limit + 1):
        if not composite[n]:
            primes.append(n)
            mu[n] = -1
        for p in primes:
            if n * p > limit:
                break
            composite[n * p] = True
            if n % p == 0:
                mu[n * p] = 0
                break
            mu[n * p] = -mu[n]
    return mu


def abel_target(endpoint: int, order: int) -> list[int]:
    target = [0] * (endpoint + 1)
    for q in range(2, endpoint + 1):
        target[q] = comb(endpoint - q + order - 1, order - 1)
    return target


def producer(endpoint: int, order: int) -> list[Fraction]:
    mu = mobius_sieve(endpoint)
    target = abel_target(endpoint, order)

    # Multiple-Mobius transform U(m)=sum_k mu(k) w(mk).
    U = [0] * (endpoint + 2)
    for k in range(1, endpoint + 1):
        if mu[k] == 0:
            continue
        muk = mu[k]
        for m in range(1, endpoint // k + 1):
            U[m] += muk * target[m * k]

    source = [0] * (endpoint + 2)
    for m in range(1, endpoint + 1):
        source[m] = U[m] - U[m + 1]

    # Exact half-binary/half-ternary descending producer.
    A = [Fraction(0) for _ in range(endpoint + 2)]
    incoming = [Fraction(0) for _ in range(endpoint + 2)]
    for m in range(endpoint, 1, -1):
        A[m] = Fraction(source[m]) + incoming[m]
        half = A[m] / 2
        ternary_left = (m + 2) // 3
        ternary_right = m - ternary_left
        binary_left = m // 2
        binary_right = m - binary_left
        for child in (
            ternary_left,
            ternary_right,
            binary_left,
            binary_right,
        ):
            if child >= 2:
                incoming[child] += half
    return A


def check(endpoint: int, order: int, node: int, expected: Fraction) -> None:
    value = producer(endpoint, order)[node]
    if value != expected:
        raise AssertionError(
            f"wrong witness at X={endpoint}, r={order}, n={node}: "
            f"got {value}, expected {expected}"
        )
    if value >= 0:
        raise AssertionError("counterexample is not negative")


def main() -> None:
    witnesses = [
        (520, 3, 15, Fraction(-91, 256)),
        (4500, 4, 19, Fraction(-11921994153, 4096)),
        (23500, 5, 15, Fraction(-164644438459306823, 131072)),
    ]
    for witness in witnesses:
        check(*witness)

    print("REFUTE_FIXED_ORDER_ABEL_PRODUCER_POSITIVITY")
    for endpoint, order, node, expected in witnesses:
        print(endpoint, order, node, expected)


if __name__ == "__main__":
    main()
