from fractions import Fraction
import hashlib
import json


def mobius_sieve(n):
    mu = [0] * (n + 1)
    mu[1] = 1
    primes = []
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


def divisors(n):
    out = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
        d += 1
    return out


def conv(a, b, nmax):
    out = [Fraction(0) for _ in range(nmax + 1)]
    for n in range(1, nmax + 1):
        out[n] = sum(a[d] * b[n // d] for d in divisors(n))
    return out


def dirichlet_inverse(a, nmax):
    assert a[1] != 0
    inv = [Fraction(0) for _ in range(nmax + 1)]
    inv[1] = 1 / a[1]
    for n in range(2, nmax + 1):
        tail = sum(a[d] * inv[n // d] for d in divisors(n) if d != 1)
        inv[n] = -tail / a[1]
    return inv


def largest_power_two(n):
    return 1 << (n.bit_length() - 1)


def phi(n):
    if n == 1:
        return 0
    return largest_power_two(n) - 1


def is_mersenne(n):
    return n >= 3 and (n + 1) & n == 0


def allowed_splits(n):
    L = largest_power_two(n)
    if is_mersenne(n):
        return [1, n - 1]
    return list(range(n - L + 1, L))


def rational_target(X, q):
    if q > X:
        return Fraction(0)
    return Fraction((X - q) * (X + q), X * q)


def main():
    N = 512
    X = 192
    mu = mobius_sieve(N)

    split_checks = 0
    minimum_defect = None
    equality_rows = 0
    for n in range(2, N + 1):
        for j in allowed_splits(n):
            defect = phi(n) - phi(j) - phi(n - j)
            assert defect >= 0, (n, j, defect)
            split_checks += 1
            if minimum_defect is None or defect < minimum_defect:
                minimum_defect = defect
            if defect == 0:
                equality_rows += 1

    delta = [Fraction(0) for _ in range(N + 1)]
    for n in range(1, N + 1):
        delta[n] = Fraction(phi(n) - (phi(n - 1) if n > 1 else 0))

    for n in range(1, N + 1):
        expected = (
            Fraction(2 ** (n.bit_length() - 2))
            if n >= 2 and n & (n - 1) == 0
            else Fraction(0)
        )
        assert delta[n] == expected, (n, delta[n], expected)

    mu_frac = [Fraction(x) for x in mu]
    a = conv(mu_frac, delta, N)

    eta = [Fraction(0) for _ in range(N + 1)]
    for n in range(1, N + 1):
        eta[n] = Fraction(1 if n % 2 else -1)
    eta_inv = dirichlet_inverse(eta, N)
    shifted = [Fraction(0) for _ in range(N + 1)]
    for n in range(2, N + 1, 2):
        shifted[n] = eta_inv[n // 2]
    assert a == shifted

    one = [Fraction(0)] + [Fraction(1) for _ in range(N)]
    one_a = conv(one, a, N)
    for n in range(1, N + 1):
        assert one_a[n] == delta[n], (n, one_a[n], delta[n])

    for m in range(1, N + 1):
        reconstructed = sum(a[q] * (m // q) for q in range(1, m + 1))
        assert reconstructed == phi(m), (m, reconstructed, phi(m))

    w = [Fraction(0) for _ in range(X + 1)]
    for q in range(2, X + 1):
        w[q] = rational_target(X, q)

    U = [Fraction(0) for _ in range(X + 2)]
    for m in range(1, X + 1):
        U[m] = sum(
            Fraction(mu[k]) * w[m * k]
            for k in range(1, X // m + 1)
        )
    R = [Fraction(0) for _ in range(X + 1)]
    for m in range(1, X + 1):
        R[m] = U[m] - U[m + 1]

    lhs = sum(R[m] * phi(m) for m in range(2, X + 1))
    rhs = sum(a[q] * w[q] for q in range(2, X + 1))
    assert lhs == rhs

    mutation_n = 14
    mutation_j = 2
    assert mutation_j not in allowed_splits(mutation_n)
    assert phi(mutation_n) - phi(mutation_j) - phi(mutation_n - mutation_j) < 0

    payload = {
        "classification": "EXACT_MCF_DYADIC_DUAL_ALGEBRA_VERIFIED",
        "N": N,
        "rational_target_endpoint": X,
        "allowed_split_checks": split_checks,
        "minimum_allowed_dual_defect": str(minimum_defect),
        "allowed_dual_equalities": equality_rows,
        "eta_inverse_shift_rows": N - 1,
        "floor_reconstruction_rows": N,
        "pairing_identity": str(lhs),
        "forbidden_edge_mutation": {
            "n": mutation_n,
            "j": mutation_j,
            "dual_defect": str(
                phi(mutation_n)
                - phi(mutation_j)
                - phi(mutation_n - mutation_j)
            ),
        },
        "proof_boundary": (
            "Finite exact algebra only; the Landau sign-oscillation proof "
            "is in R-28501."
        ),
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["proof_object_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
