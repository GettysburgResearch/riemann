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


def v2(n):
    r = 0
    while n % 2 == 0:
        n //= 2
        r += 1
    return r


def b_eta(n, mu):
    r = v2(n)
    m = n >> r
    if r == 0:
        return mu[m]
    return (1 << (r - 1)) * mu[m]


def value(f, n):
    if 0 <= n < len(f):
        return f[n]
    return Fraction(0)


def unshifted(f, nmax):
    out = [Fraction(0)] * (nmax + 1)
    for q in range(1, nmax + 1):
        total = Fraction(0)
        k = 1
        while 2 * k * q <= nmax:
            total += value(f, 2 * k * q)
            if (2 * k + 1) * q <= nmax:
                total -= value(f, (2 * k + 1) * q)
            k += 1
        out[q] = total
    return out


def shifted(f, nmax):
    out = [Fraction(0)] * (nmax + 1)
    for q in range(1, nmax + 1):
        total = Fraction(0)
        k = 1
        while 2 * k * q - 1 <= nmax:
            total += value(f, 2 * k * q - 1)
            if (2 * k + 1) * q <= nmax:
                total -= value(f, (2 * k + 1) * q)
            k += 1
        out[q] = total
    return out


def reciprocal_eta_apply(g, nmax, b):
    out = [Fraction(0)] * (nmax + 1)
    for q in range(1, nmax + 1):
        out[q] = sum(
            b[d] * value(g, d * q)
            for d in range(1, nmax // q + 1)
        )
    return out


def sparse_k(f, nmax):
    out = [Fraction(0)] * (nmax + 1)
    for q in range(1, nmax + 1):
        total = Fraction(0)
        power = 1
        while 2 * power * q - 1 <= nmax:
            total += power * (
                value(f, 2 * power * q - 1)
                - value(f, 2 * power * q)
            )
            power *= 2
        out[q] = total
    return out


def main():
    nmax = 256
    mu = mobius_sieve(nmax)
    b = [0] * (nmax + 1)
    for n in range(1, nmax + 1):
        b[n] = b_eta(n, mu)

    divisor_checks = 0
    for h in range(1, nmax + 1):
        observed = sum(b[d] for d in range(1, h + 1) if h % d == 0)
        expected = h if h & (h - 1) == 0 else 0
        assert observed == expected, (h, observed, expected)
        divisor_checks += 1

    f = [Fraction(0)] * (nmax + 1)
    for n in range(1, nmax + 1):
        f[n] = Fraction(((17 * n * n + 11 * n + 5) % 43) - 21, 37)

    u = unshifted(f, nmax)
    c = shifted(f, nmax)
    e = [c[i] - u[i] for i in range(nmax + 1)]
    be = reciprocal_eta_apply(e, nmax, b)
    kf = sparse_k(f, nmax)

    sparse_checks = 0
    for q in range(1, nmax + 1):
        assert be[q] == kf[q], (q, be[q], kf[q])
        sparse_checks += 1

    i_minus_k = [f[i] - kf[i] for i in range(nmax + 1)]
    u_i_minus_k = unshifted(i_minus_k, nmax)
    rhs = [i_minus_k[i] - u_i_minus_k[i] for i in range(nmax + 1)]

    factorization_checks = 0
    for q in range(1, nmax + 1):
        lhs = f[q] - c[q]
        assert lhs == rhs[q], (q, lhs, rhs[q])
        factorization_checks += 1

    coefficient_checks = 0
    for ell in range(1, 65):
        # For tau=1, k_(1,ell)=1/[2(2^ell-1)].
        closed = Fraction(1, 2 * ((1 << ell) - 1))
        formula = Fraction(1, 1 << (ell + 1)) / (
            Fraction(1) - Fraction(1, 1 << ell)
        )
        assert closed == formula
        coefficient_checks += 1

    R = Fraction(1, 16)
    d = Fraction(31, 32)
    c0 = Fraction(16, 31)
    assert R / (2 * d) == Fraction(1, 31)
    assert c0 == 1 / (2 * d)

    result = {
        "N": nmax,
        "divisor_checks": divisor_checks,
        "sparse_operator_checks": sparse_checks,
        "factorization_checks": factorization_checks,
        "tau1_coefficient_checks": coefficient_checks,
        "R": str(R),
        "d": str(d),
        "c": str(c0),
        "verdict": "PASS_EXACT_ETA_PRECONDITIONED_SHIFT_FACTORIZATION",
    }
    proof_object = json.dumps(
        result, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    result["proof_object_sha256"] = hashlib.sha256(proof_object).hexdigest()
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
