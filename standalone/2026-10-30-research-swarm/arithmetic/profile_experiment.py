"""Illustrative finite-scale checks of progression_profile.md.

Not an analytic certificate: von Mangoldt weights and Euler products use
ordinary binary floats. The asymptotic theorem is proved in the note.
Python standard library only. Run: python profile_experiment.py > profile_experiment.json
"""
from math import floor, log, prod
import json


def sieve(n):
    flags = bytearray(b"\x01") * (n + 1)
    flags[:2] = b"\x00\x00"
    for p in range(2, int(n**0.5) + 1):
        if flags[p]:
            flags[p * p : n + 1 : p] = b"\x00" * ((n - p * p) // p + 1)
    return [p for p in range(2, n + 1) if flags[p]]


def factor_set(n):
    factors = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            factors.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        factors.append(n)
    return factors


def constant(k, artin):
    return artin * prod((p*p - 1) / (p*p - p - 1) for p in factor_set(k))


def profile(u, artin):
    return 0.5 * (u*u - sum(constant(k, artin) * (u*u/(k*k) - 1)
                           for k in range(1, floor(u) + 1) if k < u))


if __name__ == "__main__":
    prime_cutoff = 1_000_000
    primes = sieve(prime_cutoff)
    artin = prod(1 - 1 / (p*(p - 1)) for p in primes)
    q_values = (200, 1000, 5000, 20000)
    u_values = (0.5, 1.0, 1.25, 1.5, 1.75, 2.0, 3.0, 4.0)
    nmax = 4 * max(q_values) + 1
    phis = list(range(nmax + 1))
    lam = [0.0] * (nmax + 1)
    for p in primes:
        if p > nmax:
            break
        for n in range(p, nmax + 1, p):
            phis[n] -= phis[n] // p
        power = p
        while power <= nmax:
            lam[power] = log(p)
            power *= p
    rows = []
    for Q in q_values:
        bound = 4 * Q
        weight = [0] * (bound + 1)
        for q in range(2, Q + 1):
            for n in range(q, bound + 1, q):
                weight[n] += phis[q]
        prefix = [0.0] * (bound + 1)
        for n in range(2, bound + 1):
            prefix[n] = prefix[n - 1] + lam[n] * weight[n - 1]
        for u in u_values:
            x = int(u * Q)
            actual = prefix[x] / (Q - 1) / Q
            k = min(Q, x)
            naive = ((k - 1)*x - k*(k + 1)/2 + 1) / (Q - 1) / Q
            target = profile(u, artin)
            rows.append({"Q": Q, "u": u, "actual_Psi_over_Q": actual,
                         "profile": target, "profile_error": actual - target,
                         "naive_cutoff_error": actual - naive})
    weighted_prime_rows = []
    for k in range(1, 5):
        Y = 20000
        value = sum(phis[m] * lam[k*m + 1] for m in range(1, Y + 1))
        weighted_prime_rows.append({"k": k, "Y": Y,
                                   "observed_2V_over_Y_squared": 2*value/(Y*Y),
                                   "predicted_C_k": constant(k, artin)})
    print(json.dumps({
        "scope": "illustration; floating point, not interval certification",
        "prime_cutoff": prime_cutoff,
        "Artin_product_truncation": artin,
        "analytic_tail_statement": "Exact truncated product A_P bounds A_P*(1-1/P) <= A <= A_P; floating rounding not certified here.",
        "progression_profile": rows,
        "weighted_linear_prime_check": weighted_prime_rows,
    }, indent=2))
