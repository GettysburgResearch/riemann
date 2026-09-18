"""Finite algebra checks only; no test here establishes an asymptotic RH estimate."""
from __future__ import annotations
import json
import math
from pathlib import Path


def mobius_sieve(n: int) -> list[int]:
    if n < 1:
        raise ValueError('n must be positive')
    mu = [1] * (n + 1)
    prime = [True] * (n + 1)
    mu[0] = 0
    for p in range(2, n + 1):
        if prime[p]:
            for k in range(p, n + 1, p):
                prime[k] = False
                mu[k] = -mu[k]
            for k in range(p*p, n + 1, p*p):
                mu[k] = 0
    return mu


def main() -> None:
    max_error = 0.0
    checks = 0
    for N in [2, 3, 7, 16, 31, 64]:
        K = 3 * N
        mu = mobius_sieve(K)
        logN = math.log(N)
        weights = [0.0] + [mu[d] * math.log(N / d) for d in range(1, N + 1)]
        tau = math.fsum(weights[d] / d for d in range(1, N + 1))
        assert abs(tau) <= 5.0
        lam = [0.0] * (K + 1)
        for d in range(1, N + 1):
            for k in range(d, K + 1, d):
                lam[k] += weights[d]
        cumul = 0.0
        psi = 0.0
        for k in range(1, K + 1):
            cumul += lam[k]
            A_direct = -math.fsum(weights[d] * ((k % d) / d) for d in range(2, N + 1)) / logN
            A_floor = (cumul - k * tau) / logN
            max_error = max(max_error, abs(A_direct - A_floor))
            assert abs(A_direct - A_floor) < 1e-10
            if k <= N:
                mangoldt = -math.fsum(mu[d]*math.log(d) for d in range(1,k+1) if k % d == 0)
                psi += mangoldt
                expected_lam = logN if k == 1 else mangoldt
                assert abs(lam[k] - expected_lam) < 1e-11
                assert abs((1.0 - A_direct) - (k*tau - psi)/logN) < 1e-10
                assert abs(1.0-A_direct) <= 8.0*k/logN + 1e-12
            checks += 1
    result = {
        'status': 'passed',
        'scope': 'finite algebraic identities, not asymptotic bounds or RH certification',
        'sequence_values_checked': checks,
        'max_direct_vs_divisor_sum_float_error': max_error,
        'N_values': [2,3,7,16,31,64]
    }
    print(json.dumps(result, indent=2))
    Path(__file__).with_name('checks.json').write_text(json.dumps(result, indent=2) + '\n')

if __name__ == '__main__':
    main()
