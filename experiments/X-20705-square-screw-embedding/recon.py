#!/usr/bin/env python3
"""Ordinary-high-precision square-support D-0001 reconnaissance.

For M=2,...,13 this builds the complete D-0001 even matrix at
(c,N)=(M^2,M), including every prime power q<=M^2, then evaluates the
structured rational-Leja rank-one Schur pivot. It independently evaluates the
square-screw scalar and checks S(M)=log(M)*A_00.

Classification: NON_DIRECTED_HIGH_PRECISION_RECONNAISSANCE.
"""
from __future__ import annotations
import argparse, json, math
from pathlib import Path
import mpmath as mp


def primes_up_to(limit: int) -> list[int]:
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = b"\x00" * (((limit - p * p) // p) + 1)
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
    psiq = mp.digamma(mp.mpf("0.25"))
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
        CC.append(mp.mpf("0") if n == 0 else -(mp.re(psi) - psiq) / 2 + gcc)
        XC.append(mp.re(psi1) / 4 - L * gx1 - gx2)
    return S, CC, XC, L


def full_matrix(c: int, nmax: int):
    S, CC, XC, L = closed_sequences(c, nmax)
    pi = mp.pi
    L2 = L * L
    p16 = 16 * pi * pi
    pref = 32 * L * mp.sinh(L / 4) ** 2
    eL = mp.exp(L)
    kappa = mp.log(4 * pi * (eL - 1) / (eL + 1)) + mp.euler
    U = mp.exp(L / 2)
    J = -2 * mp.log(U + 1) + mp.log(U * U + 1) + 2 * mp.atan(U) + mp.log(2) - pi / 2
    weighted = [(mp.log(p) / mp.sqrt(q), mp.log(q)) for q, p in prime_powers(c)]
    nodes = list(range(-nmax, nmax + 1))
    A = mp.matrix(len(nodes))

    def signed_s(n):
        return S[n] if n >= 0 else -S[-n]

    for ii, n in enumerate(nodes):
        for jj, m in enumerate(nodes[ii:], start=ii):
            pole = pref * (L2 - p16 * m * n) / ((L2 + p16 * m * m) * (L2 + p16 * n * n))
            if n == m:
                arch = kappa + 2 * CC[abs(n)] + J - (2 / L) * XC[abs(n)]
            else:
                arch = (signed_s(m) - signed_s(n)) / (pi * (n - m))
            prime = mp.mpf("0")
            for weight, y in weighted:
                if n == m:
                    kernel = 2 * (1 - y / L) * mp.cos(2 * pi * n * y / L)
                else:
                    kernel = (mp.sin(2 * pi * m * y / L) - mp.sin(2 * pi * n * y / L)) / (pi * (n - m))
                prime += weight * kernel
            A[ii, jj] = A[jj, ii] = pole - arch - prime
    return A, len(weighted)


def even_matrix(full, N: int):
    T = mp.matrix(N + 1, 2 * N + 1)
    T[0, N] = 1
    for n in range(1, N + 1):
        T[n, N - n] = T[n, N + n] = 1 / mp.sqrt(2)
    return T * full * T.T


def zero_data(c: int, gammas):
    L = mp.log(c)
    out = []
    for index, g in enumerate(gammas, 1):
        mu = L * g / (2 * mp.pi)
        x = mu * mu
        scalar = -2 * mp.sin(L * g / 2) / (g * mp.sqrt(L))
        out.append((index, x, scalar))
    return out


def rational_leja(data, N: int):
    selected, pivots = [], []
    lookup = {i: x for i, x, _ in data}
    for k in range(N + 1):
        best = None
        best_score = mp.mpf("-1")
        for i, x, s in data:
            if i in selected:
                continue
            value = s
            if k:
                value *= mp.fprod(x - lookup[old] for old in selected)
                value /= mp.fprod(x - n * n for n in range(1, k + 1))
            if abs(value) > best_score:
                best = (i, value)
                best_score = abs(value)
        selected.append(best[0])
        pivots.append(best[1])
    return selected, pivots


def kernel_vector(N: int, selected, data):
    poles = [mp.mpf(n * n) for n in range(1, N + 1)]
    lookup = {i: x for i, x, _ in data}

    def Q(x):
        return mp.fprod(x - lookup[i] for i in selected)

    residues = [mp.mpf(1)]
    for pole in poles:
        residues.append(Q(pole) / mp.fprod(pole - other for other in poles if other != pole))
    vector = mp.matrix(N + 1, 1)
    vector[0] = residues[0] - sum(residues[n] / poles[n - 1] for n in range(1, N + 1))
    for n in range(1, N + 1):
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
        if norm > mp.mpf("1e-55"):
            basis.append(v / norm)
        if len(basis) == dimension - 1:
            break
    result = mp.matrix(dimension, dimension - 1)
    for j, column in enumerate(basis):
        for i in range(dimension):
            result[i, j] = column[i]
    return result


def square_screw(M: int):
    M = mp.mpf(M)
    ell = mp.log(M)
    c = M * M
    prime = sum(mp.log(p) / mp.sqrt(q) * mp.log(c / mp.mpf(q)) for q, p in prime_powers(int(c)))
    return (
        4 * (M + 1 / M - 2)
        - prime
        + ell * (mp.digamma(mp.mpf("0.25")) - mp.log(mp.pi))
        - mp.mpf("0.25")
        * (M ** -1 * mp.lerchphi(M ** -4, 2, mp.mpf("0.25")) - mp.lerchphi(1, 2, mp.mpf("0.25")))
    )


def analyze(M: int, gammas):
    c = M * M
    N = M
    full, count = full_matrix(c, N)
    A = even_matrix(full, N)
    data = zero_data(c, gammas)
    selected, pivots = rational_leja(data, N)
    kernel = kernel_vector(N, selected[:N], data)
    metric = (kernel.T * kernel)[0]
    W = orthogonal_complement(kernel)
    positive = W.T * A * W
    cross = W.T * A * kernel
    raw = (kernel.T * A * kernel)[0]
    schur = raw - (cross.T * mp.inverse(positive) * cross)[0]
    eigenvalues = mp.eigsy(A, eigvals_only=True)
    positive_eigs = mp.eigsy(positive, eigvals_only=True)
    S = square_screw(M)
    identity_error = S - mp.log(M) * A[0, 0]
    return {
        "M": M,
        "c": c,
        "N": N,
        "prime_power_count": count,
        "lambda_min": mp.nstr(eigenvalues[0], 32),
        "schur_floor": mp.nstr(schur / metric, 32),
        "kernel_metric": mp.nstr(metric, 32),
        "positive_block_min": mp.nstr(positive_eigs[0], 32),
        "A00": mp.nstr(A[0, 0], 40),
        "square_screw": mp.nstr(S, 40),
        "log_M": mp.nstr(mp.log(M), 40),
        "square_identity_error": mp.nstr(identity_error, 12),
        "first_frame_zero_indices": selected[:N],
        "conditional_zero_index": selected[N],
        "minimum_rational_leja_pivot_abs": mp.nstr(min(abs(x) for x in pivots), 24),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--digits", type=int, default=70)
    parser.add_argument("--max-M", type=int, default=13)
    parser.add_argument("--zero-count", type=int, default=180)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    mp.mp.dps = args.digits
    gammas = [mp.im(mp.zetazero(i)) for i in range(1, args.zero_count + 1)]
    result = {
        "schema": "riemann.x20705.square-screw-embedding-recon.v1",
        "classification": "NON_DIRECTED_HIGH_PRECISION_RECONNAISSANCE",
        "digits": args.digits,
        "schedule": "(N,c)=(M,M^2), M=2,...,max_M",
        "levels": [analyze(M, gammas) for M in range(2, args.max_M + 1)],
        "proof_boundary": (
            "Complete D-0001 formulas and every prime power are used, but mpmath arithmetic and zero ordinates are nondirected. "
            "The exact scalar identity is proved separately in L-20704; this table only records finite matrix reconnaissance."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"level_count": len(result["levels"]), "output": str(args.output)}, indent=2))


if __name__ == "__main__":
    main()
