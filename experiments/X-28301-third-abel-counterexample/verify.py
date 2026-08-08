from fractions import Fraction
from math import comb


def mobius_sieve(n: int) -> list[int]:
    mu = [0] * (n + 1)
    mu[1] = 1
    primes: list[int] = []
    composite = [False] * (n + 1)
    for i in range(2, n + 1):
        if not composite[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > n:
                break
            composite[i * p] = True
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    return mu


def producer(Q: int) -> list[Fraction]:
    mu = mobius_sieve(Q)
    w = [Fraction(0) for _ in range(Q + 2)]
    for q in range(2, Q + 1):
        w[q] = Fraction(comb(Q - q + 2, 2))

    U = [Fraction(0) for _ in range(Q + 2)]
    for m in range(1, Q + 1):
        U[m] = sum(
            Fraction(mu[k]) * w[m * k]
            for k in range(1, Q // m + 1)
            if mu[k]
        )

    r = [Fraction(0) for _ in range(Q + 2)]
    for m in range(1, Q + 1):
        r[m] = U[m] - U[m + 1]

    A = [Fraction(0) for _ in range(Q + 2)]
    incoming = [Fraction(0) for _ in range(Q + 2)]
    for m in range(Q, 1, -1):
        A[m] = r[m] + incoming[m]
        a3 = (m + 2) // 3
        b3 = m - a3
        a2 = m // 2
        b2 = m - a2
        for child in (a3, b3, a2, b2):
            if child >= 2:
                incoming[child] += A[m] / 2
    return A


def main() -> None:
    A = producer(1000)
    assert A[18] == Fraction(-17337, 32), A[18]
    assert A[19] == Fraction(-740419, 256), A[19]
    assert A[18] < 0 and A[19] < 0
    print("PASS_EXACT_THIRD_ABEL_COUNTEREXAMPLE")
    print("Q", 1000)
    print("A18", A[18])
    print("A19", A[19])


if __name__ == "__main__":
    main()
