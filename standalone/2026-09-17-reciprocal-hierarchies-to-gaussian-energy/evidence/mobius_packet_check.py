#!/usr/bin/env python3
"""Exact finite checks for signed Mobius moment packets.

Standard library only. This verifies finite identities, not RH or an
all-scale estimate. Floating-point numbers occur only in display fields.

Run:
    python mobius_packet_check.py --output mobius_packet_check_results.json
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
from math import comb, factorial, gcd, isqrt, prod
from pathlib import Path
from typing import Mapping
import json


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ArithmeticError(message)


def mobius_sieve(limit: int) -> list[int]:
    if limit < 1:
        raise ValueError("The sieve limit must be positive.")
    mu = [0] + [1] * limit
    prime = bytearray(b'\x01') * (limit + 1)
    prime[0:2] = b'\x00\x00'
    for p in range(2, limit + 1):
        if prime[p]:
            for n in range(p, limit + 1, p):
                mu[n] = -mu[n]
                if n > p:
                    prime[n] = 0
            for n in range(p * p, limit + 1, p * p):
                mu[n] = 0
    return mu


def trial_factor(n: int) -> dict[int, int]:
    if n < 1:
        raise ValueError("Trial factorization needs a positive integer.")
    factors: dict[int, int] = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            factors[p] = factors.get(p, 0) + 1
            n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def trial_mobius(n: int) -> int:
    factors = trial_factor(n)
    return 0 if any(e > 1 for e in factors.values()) else (-1) ** len(factors)


def energy_direct(coeff: Mapping[int, Fraction | int], j: int = 0) -> Fraction:
    total = Fraction(0)
    for a, ca in coeff.items():
        for b, cb in coeff.items():
            total += Fraction(2 ** (2*j+1) * (a*b) ** (j+1), (a+b) ** (2*j+3)) * ca * cb
    return total


def energy_grouped(coeff: Mapping[int, Fraction | int]) -> Fraction:
    # Independent accumulation through the squared exponential polynomial.
    by_sum: dict[int, Fraction] = defaultdict(Fraction)
    for a, ca in coeff.items():
        for b, cb in coeff.items():
            by_sum[a+b] += a * b * ca * cb
    return sum((2*c / s**3 for s, c in by_sum.items()), Fraction(0))


def rising(n: int, k: int) -> int:
    return prod(range(n, n+k))


def falling(n: int, k: int) -> int:
    return 0 if k > n else prod(range(n-k+1, n+1))


def derivative_square(j: int, k: int) -> Fraction:
    return Fraction(factorial(2*k) * rising(j+2, k), 2**(2*k+2) * factorial(k))


def derivative_square_by_integral(j: int, k: int) -> Fraction:
    # Leibniz derivative, squared and integrated termwise against a gamma weight.
    answer = Fraction(0)
    for ell in range(min(k, j+1)+1):
        for r in range(min(k, j+1)+1):
            power = 2*k-ell-r
            coefficient = comb(k, ell)*comb(k, r)*falling(j+1, ell)*falling(j+1, r)*(-1)**power
            answer += Fraction(coefficient * rising(2*j+3, power), 2**(power+2))
    return answer


def sqrt_upper(value: Fraction, precision: int = 10**12) -> Fraction:
    if value < 0:
        raise ValueError("Cannot bound a negative square root.")
    a = isqrt(value.numerator * precision**2 // value.denominator)
    candidate = Fraction(a, precision)
    return candidate if candidate*candidate == value else Fraction(a+1, precision)


def floor_root(value: int, degree: int) -> int:
    lo, hi = 0, 1
    while hi**degree <= value:
        hi *= 2
    while hi-lo > 1:
        mid = (lo+hi)//2
        if mid**degree <= value:
            lo = mid
        else:
            hi = mid
    return lo


def sign_changes(coeff: Mapping[int, Fraction]) -> int:
    signs = [1 if coeff[n] > 0 else -1 for n in sorted(coeff) if coeff[n]]
    return sum(a != b for a, b in zip(signs, signs[1:]))


def extract_packets(original: Mapping[int, Fraction], k: int) -> tuple[list[dict[int, Fraction]], dict[int, Fraction]]:
    """Remove sign-compatible barycentric circuits; retain every remainder."""
    remaining = {n: Fraction(c) for n, c in original.items() if c}
    packets: list[dict[int, Fraction]] = []
    while True:
        chosen: list[int] = []
        for n in sorted(remaining):
            if not chosen or (remaining[n] > 0) != (remaining[chosen[-1]] > 0):
                chosen.append(n)
            if len(chosen) == k+1:
                break
        if len(chosen) < k+1:
            break
        den = {n: prod(abs(n-m) for m in chosen if m != n) for n in chosen}
        scale = min(abs(remaining[n]) * den[n] for n in chosen)
        packet = {n: (1 if remaining[n] > 0 else -1) * scale / den[n] for n in chosen}
        for r in range(k):
            require(sum(c*n**r for n, c in packet.items()) == 0, "Packet moment did not vanish")
        for n, c in packet.items():
            require(c * original[n] > 0, "Packet changed an arithmetic sign")
            require(abs(c) <= abs(remaining[n]), "Packet overdrew a coefficient")
            remaining[n] -= c
            if not remaining[n]:
                del remaining[n]
        packets.append(packet)
    require(sign_changes(remaining) <= k-1, "Remainder has too many sign changes")
    reconstruction: dict[int, Fraction] = defaultdict(Fraction)
    for packet in packets:
        for n, c in packet.items():
            reconstruction[n] += c
    for n, c in remaining.items():
        reconstruction[n] += c
    require(all(reconstruction[n] == c for n, c in original.items()), "Reconstruction mismatch")
    require(sum(abs(c) for p in packets for c in p.values()) + sum(abs(c) for c in remaining.values()) == sum(abs(c) for c in original.values()), "Absolute mass was not preserved")
    return packets, remaining


def packet_budget(packet: Mapping[int, Fraction], j: int, k: int) -> Fraction:
    a, b = min(packet), max(packet)
    constant = sqrt_upper(derivative_square(j, k)) / factorial(k)
    return constant * Fraction((b-a)**k, a**k) * sqrt_upper(Fraction(1, a)) * sum(abs(c) for c in packet.values())


def check_decomposition(mu: list[int], cutoff: int, k: int) -> dict:
    packets: list[dict[int, Fraction]] = []
    residual: dict[int, Fraction] = {}
    bins = []
    x = 1
    while x <= cutoff:
        end = min(2*x-1, cutoff)
        width = max(1, floor_root(x**(2*k-1), 2*k))
        for start in range(x, end+1, width):
            stop = min(start+width-1, end)
            original = {n: Fraction(mu[n]) for n in range(start, stop+1) if mu[n]}
            p, r = extract_packets(original, k)
            packets.extend(p)
            residual.update(r)
            bins.append([start, stop, len(p), sign_changes(r)])
        x *= 2
    original = {n: mu[n] for n in range(1, cutoff+1) if mu[n]}
    budget = sum((packet_budget(p, 0, k) for p in packets), Fraction(0))
    residual_cost = sum((abs(c) * sqrt_upper(Fraction(1, n))/2 for n, c in residual.items()), Fraction(0))
    budget += residual_cost
    energy = energy_grouped(original)
    require(energy <= budget*budget, "Certified upper bound failed")
    naive = sum((sqrt_upper(Fraction(1, n))/2 for n in original), Fraction(0))
    payload = {"packets": [[[n, str(c)] for n, c in sorted(p.items())] for p in packets], "residual": [[n, str(c)] for n, c in sorted(residual.items())]}
    digest = sha256(json.dumps(payload, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    return {"cutoff": cutoff, "order": k, "bins": bins, "packet_count": len(packets), "residual_support": len(residual), "residual_mass": float(sum(abs(c) for c in residual.values())), "residual_norm_budget": float(residual_cost), "total_norm_budget": float(budget), "naive_norm_budget": float(naive), "actual_energy": float(energy), "energy_below_budget_squared_exact": True, "decomposition_sha256": digest}


def run(limit: int, cutoff: int) -> dict:
    mu = mobius_sieve(max(limit, cutoff, 64))
    require(all(mu[n] == trial_mobius(n) for n in range(1, max(cutoff, 64)+1)), "Independent prefix Mobius values disagree")
    packets = []
    for k, step in [(2, 2), (3, 6), (4, 30)]:
        target = [(-1)**i.bit_count() for i in range(2**k)]
        found = None
        for a in range(1, limit-(2**k-1)*step+1):
            if mu[a] and all(mu[a+i*step] == mu[a]*target[i] for i in range(2**k)):
                found = [a+i*step for i in range(2**k)]
                break
        if found is None:
            packets.append({"order": k, "step": step, "found": False})
            continue
        coefficients = {n: mu[n] for n in found}
        factors = {n: trial_factor(n) for n in found}
        require(all(trial_mobius(n) == mu[n] for n in found), "Independent Mobius evaluation disagrees")
        moments = [sum(c*n**r for n, c in coefficients.items()) for r in range(k+1)]
        require(all(v == 0 for v in moments[:k]), "Found packet lacks claimed moments")
        energy = energy_direct(coefficients)
        require(energy == energy_grouped(coefficients), "Energy implementations disagree")
        diagonal = sum((Fraction(1, 4*n) for n in found), Fraction(0))
        for j in [0, 1, 4]:
            bound = packet_budget({n: Fraction(c) for n, c in coefficients.items()}, j, k)
            require(energy_direct(coefficients, j) <= bound*bound, "Packet derivative bound failed")
        primes = {p for f in factors.values() for p in f}
        p_rad = prod(primes)
        dilations = []
        for r in range(2, 1000):
            if gcd(r, p_rad) == 1 and trial_mobius(r):
                require(all(trial_mobius(r*n) == trial_mobius(r)*c for n, c in coefficients.items()), "Dilation signs failed")
                dilation = {r*n: trial_mobius(r)*c for n, c in coefficients.items()}
                require(energy_direct(dilation) == energy/r, "Energy scaling failed")
                dilations.append(r)
                if len(dilations) == 4:
                    break
        packets.append({"order": k, "step": step, "found": True, "nodes": found, "mu": list(coefficients.values()), "factorizations": factors, "moments": moments, "energy_fraction": str(energy), "diagonal_fraction": str(diagonal), "energy_to_diagonal": float(energy/diagonal), "independent_factorization_passed": True, "two_energy_implementations_agree": True, "verified_dilations": dilations})
    derivative_cases = 0
    for j in [0, 1, 2, 5, 20]:
        for k in range(7):
            require(derivative_square(j, k) == derivative_square_by_integral(j, k), "Derivative constants disagree")
            derivative_cases += 1
    decompositions = [check_decomposition(mu, cutoff, k) for k in [1, 2, 3, 4]]
    # Independent direct/grouped full-prefix comparisons at smaller cutoffs.
    for n in [1, 2, 3, 8, 16, 32, 64]:
        c = {m: mu[m] for m in range(1, n+1) if mu[m]}
        require(energy_direct(c) == energy_grouped(c), "Full prefix energy implementations disagree")
    return {"scope": "Finite exact identities and finite source decompositions only; no all-scale estimate and no RH claim.", "search_limit": limit, "packets": packets, "derivative_exact_cases": derivative_cases, "decompositions": decompositions, "small_prefix_energy_checks": 7}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--limit', type=int, default=500_000)
    parser.add_argument('--cutoff', type=int, default=512)
    parser.add_argument('--output', type=Path, default=Path('mobius_packet_check_results.json'))
    args = parser.parse_args()
    if args.limit < 1 or args.cutoff < 1:
        parser.error('limit and cutoff must both be positive')
    result = run(args.limit, args.cutoff)
    args.output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({"derivative_exact_cases": result['derivative_exact_cases'], "packets": [{"order":p['order'], "nodes":p.get('nodes'), "ratio":p.get('energy_to_diagonal')} for p in result['packets']], "decompositions": [{k:d[k] for k in ['order','packet_count','residual_mass','residual_norm_budget','total_norm_budget','naive_norm_budget','actual_energy']} for d in result['decompositions']]}, indent=2))


if __name__ == '__main__':
    main()
