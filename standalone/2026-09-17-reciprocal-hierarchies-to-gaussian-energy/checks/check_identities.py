#!/usr/bin/env python3
"""RHG26 bounded exact checks. No infinite estimate or RH conclusion.

Run from any directory:
    python checks/check_identities.py --output checks/results.json
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import importlib.util
import json
from math import comb, factorial
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    'mobius_packet_check.py': 'd8b87123900d07c9db074f8d6c030e251b5f24eb5aab56cbc55b3850cfff81fa',
    'mobius_packet_check_results.json': 'cadabefd169b0f3e61739d7d647cc647bf93f765c1adfe2dfa00b7471e79c061',
}


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ArithmeticError(message)


def multiply(a: list[F], b: list[F], degree: int) -> list[F]:
    return [sum((a[i] * b[k-i] for i in range(k+1)
                 if i < len(a) and k-i < len(b)), F(0))
            for k in range(degree+1)]


def inverse(a: list[F], degree: int) -> list[F]:
    require(a[0] != 0, 'Singular formal series')
    b = [1/a[0]]
    for k in range(1, degree+1):
        b.append(-sum((a[i]*b[k-i] for i in range(1, k+1)), F(0))/a[0])
    return b


def exponential(a: list[F], degree: int) -> list[F]:
    require(a[0] == 0, 'Exponential input needs zero constant')
    b = [F(1)]
    for k in range(1, degree+1):
        b.append(sum((i*a[i]*b[k-i] for i in range(1, k+1)), F(0))/k)
    return b


def bernoulli(maximum: int) -> list[F]:
    b = [F(1)]
    for n in range(1, maximum+1):
        b.append(-sum((comb(n+1, k)*b[k] for k in range(n)), F(0))/(n+1))
    return b


def rejection(action, label: str) -> str:
    try:
        action()
    except (ArithmeticError, ValueError):
        return label
    raise ArithmeticError('Expected rejection did not occur: ' + label)


def run() -> dict:
    for name, digest in EXPECTED.items():
        require(sha256((ROOT/'evidence'/name).read_bytes()).hexdigest() == digest,
                'Altered inherited artifact: ' + name)
    spec = importlib.util.spec_from_file_location('packet_checks', ROOT/'evidence'/'mobius_packet_check.py')
    require(spec is not None and spec.loader is not None, 'Cannot load inherited checker')
    old = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(old)
    mu = old.mobius_sieve(200)

    # Native Newton coefficient identity, including its exact support boundary.
    newton_cases = 0
    for y in range(1, 13):
        for x in range(y, (y+1)**2):
            rhs = 2*sum(mu[1:y+1]) - sum(mu[a]*mu[b]*(x//(a*b))
                                        for a in range(1, y+1) for b in range(1, y+1))
            require(rhs == sum(mu[1:x+1]), 'Newton prefix identity failed')
            newton_cases += 1
    wrong_boundary = 2*sum(mu[1:3])-sum(mu[a]*mu[b]*(9//(a*b))
                                     for a in range(1, 3) for b in range(1, 3))

    # Ordinary-power packet derivative formula, independently integrated.
    derivative_cases = 0
    for j in (0, 1, 2, 5, 20):
        for k in range(7):
            require(old.derivative_square(j, k) == old.derivative_square_by_integral(j, k),
                    'Derivative constant failed')
            derivative_cases += 1

    # Pólya-Gamma cumulants via even-zeta/Bernoulli values vs cosh power series.
    degree = 8
    bern = bernoulli(2*degree)
    cosh = [F(1, 2**(2*k)*factorial(2*k)) for k in range(degree+1)]
    sech = inverse(cosh, degree)
    pg_cases = 0
    for r in (1, 3, 5, 11):
        power = [F(1)] + [F(0)]*degree
        for _ in range(r):
            power = multiply(power, sech, degree)
        log_laplace = [F(0)]
        for k in range(1, degree+1):
            cumulant = F(r*factorial(k-1)*(2**(3*k-1)-2**(k-1)), factorial(2*k))*abs(bern[2*k])
            log_laplace.append(F((-1)**k, 2**k*factorial(k))*cumulant)
        alternative = exponential(log_laplace, degree)
        require(power == alternative, 'Polya-Gamma formal mixture coefficients failed')
        pg_cases += degree+1

    # Exactly positive native covariance disproves the stronger sign shortcut.
    source = {1: 1, 2: -1, 3: -1}
    diagonal = F(11, 24)
    covariance = old.energy_direct(source, 8)-diagonal
    expected_covariance = -F(2**27, 3**19)-F(3**9, 2**20)+F(2**27*3**9, 5**19)
    require(covariance == expected_covariance and covariance > 0, 'Native sign control failed')

    # Finite source homogeneity and independent energy accumulation.
    energy_cases = 0
    for n in (1, 2, 3, 8, 16, 32, 64):
        c = {i: mu[i] for i in range(1, n+1) if mu[i]}
        require(old.energy_direct(c) == old.energy_grouped(c), 'Energy forms disagree')
        for dilation in (2, 3):
            for j in (0, 1, 4):
                require(old.energy_direct({dilation*i: v for i,v in c.items()}, j)
                        == old.energy_direct(c, j)/dilation, 'Dilation homogeneity failed')
                energy_cases += 1

    # Gaussian prefactor after factoring out sqrt(pi): H^2 is indispensable.
    for h in (F(1), F(2), F(7), F(3, 2)):
        require(2*h*h/(2*h) == h, 'Gaussian normalization failed')

    refusals = [
        rejection(lambda: require(wrong_boundary == sum(mu[1:10]), 'End support is wrong'),
                  'Extending Newton support to (y+1)^2'),
        rejection(lambda: require(covariance <= 0, 'Covariance is positive'),
                  'Claiming all native covariances are nonpositive'),
        rejection(lambda: old.sqrt_upper(F(-1)), 'Negative rational square-root input'),
        rejection(lambda: require(sum(c*n for n,c in {15:1,17:-1,19:-1,21:-1}.items()) == 0,
                                  'Altered packet first moment'), 'Altered packet sign'),
        rejection(lambda: require(F(2)*2/(2*2) == 2, 'Missing Gaussian H factor'),
                  'Using H instead of H^2 in Gaussian Fourier formula'),
        rejection(lambda: require(sha256(b'altered').hexdigest() == EXPECTED['mobius_packet_check.py'],
                                  'Source hash mismatch'), 'Altered artifact hash'),
    ]
    return {
        'scope': 'Bounded exact identities and explicit false-claim controls only; no RH or asymptotic certification.',
        'inherited_sha256': EXPECTED,
        'newton_prefix_cases': newton_cases,
        'derivative_constant_cases': derivative_cases,
        'polya_gamma_formal_coefficients': pg_cases,
        'energy_dilation_cases': energy_cases,
        'native_positive_covariance': str(covariance),
        'expected_refusals': refusals,
        'refusal_count': len(refusals),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('results.json'))
    args = parser.parse_args()
    result = run()
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n', encoding='utf-8')
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
