#!/usr/bin/env python3
"""Native Eisenstein sextic source and Gauss-frame diagnostics.

Exact arithmetic builds ideals, squarefreeness and sixth-root character values.
Finite-field rank certificates are exact. Gauss phases and projections are
floating-point diagnostics, not interval-certified analytic estimates.
Only numpy and Python's standard library are required.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from functools import lru_cache
import hashlib
import json
import math
from pathlib import Path

import numpy as np


ONE = (1, 0)
ZERO = (0, 0)


def mul(x, y):
    a, b = x
    c, d = y
    return a * c - b * d, a * d + b * c - b * d


def norm(x):
    return x[0] ** 2 - x[0] * x[1] + x[1] ** 2


def conjugate(x):
    return x[0] - x[1], -x[1]


def quotient_if_integral(x, y):
    numerator = mul(x, conjugate(y))
    q = norm(y)
    if numerator[0] % q or numerator[1] % q:
        return None
    return numerator[0] // q, numerator[1] // q


ROOTS = [ONE]
for _ in range(5):
    ROOTS.append(mul(ROOTS[-1], (1, 1)))
ROOT_VALUES = np.array([complex(a - b / 2, math.sqrt(3) * b / 2) for a, b in ROOTS])


def is_prime(n):
    if n < 2:
        return False
    return all(n % d for d in range(2, math.isqrt(n) + 1))


def bezout(a, b):
    r0, r1, x0, x1, y0, y1 = a, b, 1, 0, 0, 1
    while r1:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    if r0 < 0:
        r0, x0, y0 = -r0, -x0, -y0
    return r0, x0, y0


class PrimeRing:
    def __init__(self, generator):
        self.generator = generator
        self.q = norm(generator)
        a, b = generator
        g, x, y = bezout(b, a - b)
        self.h11, self.h22 = self.q // g, g
        self.h12 = (a * x - b * y) % self.h11
        self.lookup = {self.reduce(root): i for i, root in enumerate(ROOTS)}
        if len(self.lookup) != 6:
            raise ValueError("six distinct roots required")

    def reduce(self, z):
        d, rem = divmod(z[1], self.h22)
        return (z[0] - d * self.h12) % self.h11, rem

    @lru_cache(maxsize=None)
    def phase(self, z):
        x = self.reduce(z)
        if x == ZERO:
            return -1
        if self.h22 == 1:
            answer = (pow(x[0], (self.q - 1) // 6, self.q), 0)
        else:
            answer, exponent = ONE, (self.q - 1) // 6
            while exponent:
                if exponent & 1:
                    answer = self.reduce(mul(answer, x))
                x = self.reduce(mul(x, x))
                exponent //= 2
        return self.lookup[answer]

    @lru_cache(maxsize=None)
    def gamma(self):
        a, b = self.generator
        terms = []
        for y in range(self.h22):
            for x in range(self.h11):
                phase = self.phase((x, y))
                if phase >= 0:
                    additive = ((a * y - b * x) % self.q) / self.q
                    terms.append(ROOT_VALUES[phase] * np.exp(2j * np.pi * additive))
        answer = sum(terms) / math.sqrt(self.q)
        if abs(abs(answer) - 1) > 1e-10:
            raise ArithmeticError(("nonunit prime Gauss phase", self.generator, answer))
        return answer


class Arithmetic:
    def __init__(self, cap):
        bound = math.isqrt((4 * cap + 2) // 3) + 2
        self.ideals = sorted(
            [(a, b) for a in range(-bound, bound + 1)
             for b in range(-bound, bound + 1)
             if a % 3 == 1 and b % 3 == 0 and 0 < norm((a, b)) <= cap
             and math.gcd(norm((a, b)), 6) == 1],
            key=lambda z: (norm(z), z),
        )
        self.primes = []
        for z in self.ideals:
            q = norm(z)
            p = math.isqrt(q)
            if is_prime(q) or (p * p == q and p % 3 == 2 and is_prime(p)):
                self.primes.append(z)
        self.prime_set = set(self.primes)
        self.rings = {p: PrimeRing(p) for p in self.primes}
        self.factors = {}
        for z in self.ideals:
            remaining = z
            factors = []
            for p in self.primes:
                if remaining == ONE:
                    break
                if remaining in self.prime_set:
                    factors.append((remaining, 1))
                    remaining = ONE
                    break
                if norm(p) > norm(remaining):
                    break
                exponent = 0
                while (new := quotient_if_integral(remaining, p)) is not None:
                    remaining = new
                    exponent += 1
                if exponent:
                    factors.append((p, exponent))
            if remaining != ONE:
                raise ArithmeticError(("incomplete ideal factorization", z, remaining))
            rebuilt = ONE
            for p, exponent in factors:
                for _ in range(exponent):
                    rebuilt = mul(rebuilt, p)
            if rebuilt != z:
                raise ArithmeticError(("wrong factorization", z, factors))
            self.factors[z] = tuple(factors)

    def squarefree(self, z):
        return all(e == 1 for _, e in self.factors[z])

    def mobius(self, z):
        return (-1) ** len(self.factors[z]) if self.squarefree(z) else 0

    def phase(self, denominator, numerator):
        phase = 0
        for p, exponent in self.factors[denominator]:
            k = self.rings[p].phase(numerator)
            if k < 0:
                return -1
            phase += exponent * k
        return phase % 6

    def gamma(self, z):
        if not self.squarefree(z):
            raise ValueError("gamma is used only on squarefree moduli")
        primes = [p for p, _ in self.factors[z]]
        answer = 1 + 0j
        for i, p in enumerate(primes):
            answer *= self.rings[p].gamma()
            for q in primes[:i]:
                answer *= ROOT_VALUES[(self.rings[p].phase(q) + self.rings[q].phase(p)) % 6]
        return answer


def bump(x):
    if not 1 < x < 2:
        return 0.0
    return math.exp(4 - 1 / ((x - 1) * (2 - x)))


def rank_certificate(pair_matrix, prime=1009):
    """Rank over F_p after omega -> a nontrivial cube root.

    Nonzero pivot minor certifies at least this rank over Q(omega). Integer
    arithmetic is exact: intermediates are below 2*p*p in int64.
    """
    if not is_prime(prime) or prime % 3 != 1:
        raise ValueError("certificate prime must be 1 mod 3")
    omega = next(pow(g, (prime - 1) // 3, prime) for g in range(2, prime)
                 if pow(g, (prime - 1) // 3, prime) != 1)
    raw = np.array(pair_matrix, dtype=np.int64)
    work = (raw[:, :, 0] + omega * raw[:, :, 1]) % prime
    pivot_rows, pivot_columns = [], []
    row_labels = list(range(work.shape[0]))
    rank, determinant, swaps = 0, 1, 0
    for column in range(work.shape[1]):
        candidates = np.flatnonzero(work[rank:, column])
        if not len(candidates):
            continue
        pivot = rank + int(candidates[0])
        if pivot != rank:
            work[[rank, pivot]] = work[[pivot, rank]]
            row_labels[rank], row_labels[pivot] = row_labels[pivot], row_labels[rank]
            swaps += 1
        entry = int(work[rank, column])
        determinant = determinant * entry % prime
        inverse = pow(entry, -1, prime)
        work[rank, column:] = work[rank, column:] * inverse % prime
        if rank + 1 < work.shape[0]:
            coefficients = work[rank + 1:, column].copy()
            work[rank + 1:, column:] = (
                work[rank + 1:, column:] - coefficients[:, None] * work[rank, column:][None, :]
            ) % prime
        pivot_rows.append(row_labels[rank])
        pivot_columns.append(column)
        rank += 1
        if rank == work.shape[0]:
            break
    # Replay the selected minor independently, in its selected row order.
    minor_raw = raw[pivot_rows][:, pivot_columns]
    minor = (minor_raw[:, :, 0] + omega * minor_raw[:, :, 1]) % prime
    replay_determinant = 1
    for j in range(rank):
        pivot = int(minor[j, j])
        if not pivot:
            raise ArithmeticError("selected minor has a zero replay pivot")
        replay_determinant = replay_determinant * pivot % prime
        if j + 1 < rank:
            multipliers = minor[j + 1:, j] * pow(pivot, -1, prime) % prime
            minor[j + 1:, j:] = (minor[j + 1:, j:] - multipliers[:, None] * minor[j, j:]) % prime
    if replay_determinant != determinant:
        raise ArithmeticError("independent minor replay disagrees")
    return {"prime": prime, "omega_image": omega, "rank_lower_bound": rank,
            "matrix_shape": list(work.shape), "pivot_rows": pivot_rows,
            "pivot_columns": pivot_columns, "ordered_pivot_minor_residue": determinant,
            "minor_replay_verified": True,
            "rank_is_exact_by_dimension": rank == min(work.shape),
            "full_row_rank": rank == work.shape[0]}


def verify_native_gauss(arithmetic):
    """Check the CRT assembly against complete additive sums on composites."""
    cases = []
    for z in arithmetic.ideals:
        if norm(z) > 300:
            break
        if not arithmetic.squarefree(z) or len(arithmetic.factors[z]) < 2:
            continue
        ring = PrimeRing(z)  # Only its exact quotient-lattice coordinates.
        a, b = z
        terms = []
        for y in range(ring.h22):
            for x in range(ring.h11):
                phase = arithmetic.phase(z, (x, y))
                if phase >= 0:
                    terms.append(ROOT_VALUES[phase] * np.exp(2j * np.pi * ((a * y - b * x) % ring.q) / ring.q))
        direct = sum(terms) / math.sqrt(norm(z))
        error = abs(direct - arithmetic.gamma(z))
        if error > 1e-10:
            raise ArithmeticError(("CRT Gauss phase orientation mismatch", z, error))
        cases.append({"generator": z, "norm": norm(z), "absolute_error": float(error)})
    if not cases:
        raise ArithmeticError("no composite Gauss check performed")
    return cases


def minimum_rank(eigenvalues, required):
    if required <= 0:
        return 0
    return int(np.searchsorted(np.cumsum(eigenvalues), required, side="left")) + 1


def run_case(arithmetic, D, U, label_caps):
    # Discard only rows on which the specified smooth weight is exactly zero.
    rows = [z for z in arithmetic.ideals if arithmetic.squarefree(z) and U < norm(z) < 2 * U]
    columns = [n for n in arithmetic.ideals if arithmetic.squarefree(n) and D < norm(n) < 2 * D]
    row_sqrt = np.array([math.sqrt(bump(norm(z) / U)) for z in rows])
    coefficients = np.array([arithmetic.mobius(n) * bump(norm(n) / D) / math.sqrt(norm(n))
                             for n in columns])
    phases = np.array([[arithmetic.phase(n, z) for n in columns] for z in rows], dtype=np.int16)
    table = np.concatenate((ROOT_VALUES, np.array([0j])))
    chars = table[np.where(phases < 0, 6, phases)]
    A = row_sqrt[:, None] * chars
    y = A @ coefficients
    gamma = np.array([arithmetic.gamma(z) for z in rows])
    norm_groups = sorted({norm(n) for n in columns})
    lookup = {m: i for i, m in enumerate(norm_groups)}
    packets = np.zeros((len(rows), len(norm_groups)), dtype=complex)
    exact_packets = np.zeros((len(rows), len(norm_groups), 2), dtype=np.int64)
    seen_mobius = {}
    for j, n in enumerate(columns):
        m, group = norm(n), lookup[norm(n)]
        mu = arithmetic.mobius(n)
        if m in seen_mobius and seen_mobius[m] != mu:
            raise ArithmeticError("Mobius must agree on equal-norm squarefree ideals")
        seen_mobius[m] = mu
        packets[:, group] += A[:, j] * coefficients[j]
        for i in range(len(rows)):
            k = int(phases[i, j])
            if k >= 0:
                exact_packets[i, group] += np.array(ROOTS[k])
    certificate = rank_certificate(exact_packets)
    mean_energy = float(np.linalg.norm(packets) ** 2)
    covariance_eigenvalues = np.maximum(np.linalg.eigvalsh(packets @ packets.conj().T), 0)[::-1]
    packet_singular = np.linalg.svd(packets, compute_uv=False)
    finite_twists = [0.0, .5, 1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0]
    result = {"D": D, "U": U, "row_count": len(rows), "column_count": len(columns),
              "distinct_norm_count": len(norm_groups), "rows": rows,
              "source_norms": norm_groups,
              "packet_rank_certificate": certificate,
              "packet_smallest_singular_value": float(packet_singular[-1]),
              "native_t0_energy": float(np.linalg.norm(y) ** 2),
              "norm_twist_mean_energy": mean_energy,
              "max_prime_gauss_modulus_error": float(max(abs(abs(g) - 1) for g in gamma)),
              "coherent_packet_reconstruction_error": float(np.linalg.norm(packets.sum(axis=1) - y)),
              "literal_common_prime_zero_count": int(np.count_nonzero(phases < 0)),
              "frames": []}
    for K in label_caps:
        labels = [R for R in arithmetic.ideals if arithmetic.squarefree(R) and norm(R) <= K]
        frame_phases = np.array([[arithmetic.phase(z, R) for R in labels] for z in rows], dtype=np.int16)
        raw_frame = table[np.where(frame_phases < 0, 6, (-frame_phases) % 6)]
        V = (row_sqrt * gamma / math.sqrt(U))[:, None] * raw_frame
        gram = V.conj().T @ V
        singular = np.linalg.svd(V, compute_uv=False)
        rank = int(np.count_nonzero(singular > max(V.shape) * np.finfo(float).eps * singular[0]))
        if rank != len(labels):
            raise ArithmeticError(("rank-deficient chosen finite frame", D, U, K, rank, len(labels)))
        Q, _ = np.linalg.qr(V, mode="reduced")
        observed_packets = Q.conj().T @ packets
        residual_packets = packets - Q @ observed_packets
        residual_eigenvalues = np.maximum(np.linalg.eigvalsh(residual_packets @ residual_packets.conj().T), 0)[::-1]
        projected_y = Q @ (Q.conj().T @ y)
        actual_capture = float(np.linalg.norm(projected_y) ** 2 / np.linalg.norm(y) ** 2)
        mean_capture = float(np.linalg.norm(observed_packets) ** 2 / mean_energy)
        frame_pairs = np.zeros((len(rows), len(labels), 2), dtype=np.int64)
        for i in range(len(rows)):
            for j in range(len(labels)):
                k = int(frame_phases[i, j])
                if k >= 0:
                    frame_pairs[i, j] = ROOTS[(-k) % 6]
        # Certify full column rank by transposing; common nonzero row factors
        # and the Gauss phase preserve rank.
        frame_certificate = rank_certificate(frame_pairs.transpose(1, 0, 2))
        twists = []
        for t in finite_twists:
            yt = packets @ np.exp(1j * t * np.log(np.array(norm_groups) / D))
            twists.append({"t": t, "energy": float(np.linalg.norm(yt) ** 2),
                           "capture_fraction": float(np.linalg.norm(Q.conj().T @ yt) ** 2 / np.linalg.norm(yt) ** 2)})
        result["frames"].append({
            "K": K, "labels": labels, "rank": rank,
            "within_K_le_sqrtU": K <= math.sqrt(U),
            "within_K_le_D_pow_1over7": K <= D ** (1 / 7),
            "gram_min_eigenvalue": float(np.linalg.eigvalsh(gram)[0]),
            "gram_condition_number": float(np.linalg.cond(gram)),
            "native_t0_capture_fraction": actual_capture,
            "norm_twist_mean_capture_fraction": mean_capture,
            "best_possible_rank_r_mean_capture_fraction": float(covariance_eigenvalues[:rank].sum() / mean_energy),
            "best_extra_ranks_for_total_mean_capture": {
                str(target): minimum_rank(residual_eigenvalues, target * mean_energy - np.linalg.norm(observed_packets) ** 2)
                for target in (.5, .9, .99)},
            "residual_covariance_eigenvalues": residual_eigenvalues.tolist(),
            "frame_rank_certificate": frame_certificate,
            "native_profile_invisible_dimension_lower_bound": max(0, certificate["rank_lower_bound"] - rank),
            "orthogonal_energy_replay_error": float(abs(np.linalg.norm(y) ** 2 - np.linalg.norm(projected_y) ** 2
                                                         - np.linalg.norm(y - projected_y) ** 2)),
            "sampled_twists": twists,
        })
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cases", default="256:128,1024:512,4096:2048")
    parser.add_argument("--label-caps", default="1,7,13,25,43")
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("NATIVE_RESULTS.json"))
    args = parser.parse_args()
    cases = [tuple(map(int, case.split(":"))) for case in args.cases.split(",")]
    caps = list(map(int, args.label_caps.split(",")))
    arithmetic = Arithmetic(max(max(2 * D, 2 * U, max(caps)) for D, U in cases))
    gauss_checks = verify_native_gauss(arithmetic)
    results = []
    for D, U in cases:
        admissible_caps = [K for K in caps if K <= math.sqrt(U)]
        case = run_case(arithmetic, D, U, admissible_caps)
        results.append(case)
        print(json.dumps({"D": D, "U": U, "rows": case["row_count"], "columns": case["column_count"],
                          "packet_rank": case["packet_rank_certificate"]["rank_lower_bound"],
                          "frames": [{k: f[k] for k in ("K", "rank", "native_t0_capture_fraction",
                                                        "norm_twist_mean_capture_fraction", "best_extra_ranks_for_total_mean_capture")}
                                     for f in case["frames"]]}, sort_keys=True), flush=True)
    report = {"status": "completed", "arithmetic": "Native Z[omega] ideals; all good squarefree rows and columns in the displayed open norm annuli; actual sixth-power residue symbols including natural zero masks; normalized sextic Gauss phases; Mobius coefficients.",
              "scope": "Finite-field rank certificates exact; all projection and covariance-energy numbers are floating-point diagnostics. No analytic bound or fixed-t asymptotic claim is verified.",
              "composite_gauss_CRT_replay": gauss_checks,
              "source_profile": "W(x)=w(x)=exp(4-1/((x-1)*(2-x))) on 1<x<2, zero elsewhere; Q=1; trivial ray character.",
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), "cases": results}
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
