#!/usr/bin/env python3
"""Ordinary-high-precision growing D-0001 prime-side reconnaissance.

This script includes every prime power q<=c, the complete released pole block,
and the cutoff-free archimedean block. It uses the exact rational-Leja
Cauchy-frame formulas to select the first and conditional second zero rows.

Classification: NON_DIRECTED_HIGH_PRECISION_RECONNAISSANCE.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import mpmath as mp


def primes_up_to(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            sieve[p*p:limit+1:p] = b"\x00" * (((limit-p*p)//p)+1)
    return [p for p in range(2, limit + 1) if sieve[p]]


def prime_powers(limit: int) -> list[tuple[int, int]]:
    out = []
    for p in primes_up_to(limit):
        q = p
        while q <= limit:
            out.append((q, p))
            if q > limit // p:
                break
            q *= p
    return sorted(out)


def closed_sequences(c: int, nmax: int):
    L = mp.log(c)
    psi_quarter = mp.digamma(mp.mpf("0.25"))
    S, CC, XC = [], [], []
    for n in range(nmax + 1):
        w = 2 * mp.pi * n / L
        z = mp.mpf("0.25") + 1j * mp.pi * n / L
        psi = mp.digamma(z)
        psi1 = mp.polygamma(1, z)
        gs = gcc = gx1 = gx2 = mp.mpf("0")
        k = 0
        while True:
            ck = 2 * k + mp.mpf("0.5")
            ek = mp.exp(-ck * L)
            den = ck * ck + w * w
            gs += ek / den
            if n:
                gcc += ek * w * w / (ck * den)
            gx1 += ek * ck / den
            gx2 += ek * (ck * ck - w * w) / (den * den)
            if ek < mp.mpf("1e-90"):
                break
            k += 1
        S.append(mp.mpf("0") if n == 0 else mp.im(psi) / 2 - w * gs)
        CC.append(
            mp.mpf("0")
            if n == 0
            else -(mp.re(psi) - psi_quarter) / 2 + gcc
        )
        XC.append(mp.re(psi1) / 4 - L * gx1 - gx2)
    return S, CC, XC, L


def full_matrix(c: int, nmax: int):
    S, CC, XC, L = closed_sequences(c, nmax)
    pi = mp.pi
    L2 = L * L
    sixteen_pi_sq = 16 * pi * pi
    prefactor = 32 * L * mp.sinh(L / 4) ** 2
    eL = mp.exp(L)
    kappa = mp.log(4 * pi * (eL - 1) / (eL + 1)) + mp.euler
    U = mp.exp(L / 2)
    J = (
        -2 * mp.log(U + 1)
        + mp.log(U * U + 1)
        + 2 * mp.atan(U)
        + mp.log(2)
        - pi / 2
    )
    weighted = [
        (mp.log(p) / mp.sqrt(q), mp.log(q))
        for q, p in prime_powers(c)
    ]
    nodes = list(range(-nmax, nmax + 1))
    matrix = mp.matrix(len(nodes))

    def signed_s(n: int):
        return S[n] if n >= 0 else -S[-n]

    for ii, n in enumerate(nodes):
        for jj, m in enumerate(nodes[ii:], start=ii):
            pole = (
                prefactor
                * (L2 - sixteen_pi_sq * m * n)
                / (
                    (L2 + sixteen_pi_sq * m * m)
                    * (L2 + sixteen_pi_sq * n * n)
                )
            )
            if n == m:
                arch = (
                    kappa
                    + 2 * CC[abs(n)]
                    + J
                    - (2 / L) * XC[abs(n)]
                )
            else:
                arch = (signed_s(m) - signed_s(n)) / (pi * (n - m))
            prime = mp.mpf("0")
            for weight, y in weighted:
                if n == m:
                    kernel = 2 * (1 - y / L) * mp.cos(2 * pi * n * y / L)
                else:
                    kernel = (
                        mp.sin(2 * pi * m * y / L)
                        - mp.sin(2 * pi * n * y / L)
                    ) / (pi * (n - m))
                prime += weight * kernel
            value = pole - arch - prime
            matrix[ii, jj] = matrix[jj, ii] = value
    return matrix, len(weighted)


def even_matrix(full, nmax: int):
    transform = mp.matrix(nmax + 1, 2 * nmax + 1)
    transform[0, nmax] = 1
    for n in range(1, nmax + 1):
        transform[n, nmax - n] = 1 / mp.sqrt(2)
        transform[n, nmax + n] = 1 / mp.sqrt(2)
    return transform * full * transform.T


def zero_data(c: int, gammas):
    L = mp.log(c)
    out = []
    for index, gamma in enumerate(gammas, start=1):
        mu = L * gamma / (2 * mp.pi)
        x = mu * mu
        scalar = -2 * mp.sin(L * gamma / 2) / (gamma * mp.sqrt(L))
        out.append((index, x, scalar))
    return out


def rational_leja(data, nmax: int):
    selected = []
    pivots = []
    for k in range(nmax + 1):
        best = None
        best_score = mp.mpf("-1")
        for index, x, scalar in data:
            if index in selected:
                continue
            value = scalar
            if k:
                numerator = mp.mpf(1)
                for old in selected:
                    old_x = next(item[1] for item in data if item[0] == old)
                    numerator *= x - old_x
                denominator = mp.mpf(1)
                for n in range(1, k + 1):
                    denominator *= x - n * n
                value = scalar * numerator / denominator
            if abs(value) > best_score:
                best = (index, value)
                best_score = abs(value)
        selected.append(best[0])
        pivots.append(best[1])
    return selected, pivots


def kernel_vector(nmax: int, selected: list[int], data):
    poles = [mp.mpf(n * n) for n in range(1, nmax + 1)]
    lookup = {index: x for index, x, _ in data}

    def Q(x):
        answer = mp.mpf(1)
        for index in selected:
            answer *= x - lookup[index]
        return answer

    residues = [mp.mpf(1)]
    for pole in poles:
        derivative = mp.mpf(1)
        for other in poles:
            if other != pole:
                derivative *= pole - other
        residues.append(Q(pole) / derivative)

    vector = mp.matrix(nmax + 1, 1)
    vector[0] = residues[0] - sum(
        residues[n] / poles[n - 1] for n in range(1, nmax + 1)
    )
    for n in range(1, nmax + 1):
        vector[n] = residues[n] / (mp.sqrt(2) * poles[n - 1])
    return vector


def orthogonal_complement(vector):
    dimension = vector.rows
    unit = vector / mp.norm(vector)
    basis = []
    for i in range(dimension):
        v = mp.matrix(dimension, 1)
        v[i] = 1
        v -= unit * (unit.T * v)[0]
        for old in basis:
            v -= old * (old.T * v)[0]
        norm = mp.norm(v)
        if norm > mp.mpf("1e-50"):
            basis.append(v / norm)
        if len(basis) == dimension - 1:
            break
    result = mp.matrix(dimension, dimension - 1)
    for j, column in enumerate(basis):
        for i in range(dimension):
            result[i, j] = column[i]
    return result


def analyze(c: int, nmax: int, gammas):
    full, prime_power_count = full_matrix(c, nmax)
    operator = even_matrix(full, nmax)
    data = zero_data(c, gammas)
    selected, pivots = rational_leja(data, nmax)
    first = selected[:nmax]
    conditional = selected[nmax]
    kernel = kernel_vector(nmax, first, data)
    metric = (kernel.T * kernel)[0]
    complement = orthogonal_complement(kernel)
    positive = complement.T * operator * complement
    cross = complement.T * operator * kernel
    raw = (kernel.T * operator * kernel)[0]
    schur = raw - (cross.T * mp.inverse(positive) * cross)[0]

    lookup = {index: (x, scalar) for index, x, scalar in data}
    y, scalar = lookup[conditional]
    numerator = mp.mpf(1)
    for index in first:
        numerator *= y - lookup[index][0]
    denominator = mp.mpf(1)
    for n in range(1, nmax + 1):
        denominator *= y - n * n
    evaluation = scalar * numerator / denominator
    selected_ratio = evaluation * evaluation / metric
    floor = schur / metric
    residual = floor - selected_ratio
    eigenvalues, _ = mp.eigsy(operator)

    return {
        "c": c,
        "N": nmax,
        "prime_power_count": prime_power_count,
        "first_frame_zero_indices": first,
        "conditional_zero_index": conditional,
        "rational_leja_pivots": [mp.nstr(x, 24) for x in pivots],
        "kernel_metric": mp.nstr(metric, 30),
        "conditional_evaluation": mp.nstr(evaluation, 30),
        "selected_frame_ratio": mp.nstr(selected_ratio, 30),
        "joint_corrected_residual_ratio": mp.nstr(residual, 30),
        "joint_prime_side_schur_floor": mp.nstr(floor, 30),
        "direct_lowest_eigenvalue": mp.nstr(eigenvalues[0], 30),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--digits", type=int, default=70)
    parser.add_argument("--zero-count", type=int, default=100)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    mp.mp.dps = args.digits
    schedule = [(5, 1), (10, 2), (20, 3), (50, 4), (100, 5), (200, 6), (500, 7)]
    gammas = [mp.im(mp.zetazero(index)) for index in range(1, args.zero_count + 1)]
    result = {
        "schema": "riemann.x20704.growing-prime-side-recon.v1",
        "classification": "NON_DIRECTED_HIGH_PRECISION_RECONNAISSANCE",
        "digits": args.digits,
        "zero_count": args.zero_count,
        "operator": "complete D-0001 polar + archimedean + every prime power q<=c",
        "levels": [analyze(c, n, gammas) for c, n in schedule],
        "proof_boundary": (
            "The matrix formulas are complete, but mpmath values and zeta-zero "
            "ordinates are nondirected. This table nominates directed levels and "
            "tests the structured frame; it is not a proof object."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
