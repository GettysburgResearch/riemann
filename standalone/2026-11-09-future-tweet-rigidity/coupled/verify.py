#!/usr/bin/env python3
"""Exact finite-field checks for the coupled affine/trace-function adapter.

Only the standard library is used. Arithmetic is in Q(zeta_6,zeta_p),
represented in the basis zeta_6^a*zeta_p^b, a=0,1 and 0<=b<p-1.
No floating-point comparison is used. This does not prove FKMS, monodromy,
or any asymptotic estimate for the native arithmetic coefficients.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path


class Field:
    def __init__(self, p: int, degree: int = 1):
        self.p, self.degree, self.q = p, degree, p**degree
        self.d = next((d for d in range(2, p) if pow(d, (p - 1) // 2, p) == p - 1), 0)
        self.nonzero = range(1, self.q)
        factors = []
        n = self.q - 1
        for r in range(2, n + 1):
            if n % r == 0:
                factors.append(r)
                while n % r == 0:
                    n //= r
            if n == 1:
                break
        self.generator = next(g for g in self.nonzero if all(self.pow(g, (self.q - 1) // r) != 1 for r in factors))
        self.logs = {}
        z = 1
        for k in range(self.q - 1):
            self.logs[z] = k
            z = self.mul(z, self.generator)
        if len(self.logs) != self.q - 1:
            raise ValueError("not a multiplicative generator")

    def add(self, x: int, y: int) -> int:
        p = self.p
        return (x % p + y % p) % p + p * ((x // p + y // p) % p)

    def neg(self, x: int) -> int:
        p = self.p
        return (-x % p) + p * (-(x // p) % p)

    def sub(self, x: int, y: int) -> int:
        return self.add(x, self.neg(y))

    def mul(self, x: int, y: int) -> int:
        p = self.p
        a, b, c, d = x % p, x // p, y % p, y // p
        return (a * c + self.d * b * d) % p + p * ((a * d + b * c) % p)

    def pow(self, x: int, n: int) -> int:
        ans = 1
        while n:
            if n & 1:
                ans = self.mul(ans, x)
            x = self.mul(x, x)
            n //= 2
        return ans

    def inv(self, x: int) -> int:
        if not x:
            raise ZeroDivisionError
        return self.pow(x, self.q - 2)

    def trace(self, x: int) -> int:
        return (self.degree * (x % self.p)) % self.p


class Cyclotomic:
    def __init__(self, p: int):
        self.p, self.n = p, p - 1
        self.zero = (0,) * (2 * self.n)
        self.one = self.monomial(0, 0)

    @staticmethod
    def sixth(a: int) -> tuple[int, int]:
        return ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))[a % 6]

    def reduce(self, pairs: list[list[int]]) -> tuple[int, ...]:
        c, d = pairs[-1]
        return tuple(z for a, b in pairs[:-1] for z in (a - c, b - d))

    def monomial(self, sixth: int, additive: int) -> tuple[int, ...]:
        pairs = [[0, 0] for _ in range(self.p)]
        pairs[additive % self.p] = list(self.sixth(sixth))
        return self.reduce(pairs)

    def add(self, x, y):
        return tuple(a + b for a, b in zip(x, y))

    def neg(self, x):
        return tuple(-a for a in x)

    def scale(self, x, n):
        return tuple(n * a for a in x)

    def integer(self, n):
        return self.scale(self.one, n)

    def mul(self, x, y):
        out = [[0, 0] for _ in range(self.p)]
        xi = [(i, x[2 * i], x[2 * i + 1]) for i in range(self.n) if x[2 * i] or x[2 * i + 1]]
        yi = [(j, y[2 * j], y[2 * j + 1]) for j in range(self.n) if y[2 * j] or y[2 * j + 1]]
        for i, a, b in xi:
            for j, c, d in yi:
                k = (i + j) % self.p
                out[k][0] += a * c - b * d
                out[k][1] += a * d + b * c + b * d
        return self.reduce(out)

    def conj(self, x):
        out = [[0, 0] for _ in range(self.p)]
        for i in range(self.n):
            a, b = x[2 * i], x[2 * i + 1]
            k = (-i) % self.p
            out[k][0] += a + b
            out[k][1] -= b
        return self.reduce(out)

    def sum(self, seq):
        ans = self.zero
        for x in seq:
            ans = self.add(ans, x)
        return ans


def run_field(p: int, degree: int, orientation: int) -> dict:
    f, R = Field(p, degree), Cyclotomic(p)
    q = f.q
    counts = Counter()

    def check(name, lhs, rhs):
        counts[name] += 1
        if lhs != rhs:
            raise AssertionError((q, orientation, name, lhs, rhs))

    def chi(x, conjugate=False):
        if not x:
            return R.zero
        k = orientation * f.logs[x]
        return R.monomial(-k if conjugate else k, 0)

    def atom(x, y, z=0):
        if not x or not y:
            return R.zero
        return R.monomial(orientation * (f.logs[x] - f.logs[y]), f.trace(z))

    def additive(x):
        return R.monomial(0, f.trace(x))

    one = 1
    minus_one = f.neg(one)
    S = [R.sum(atom(y, f.sub(y, one), f.mul(z, y)) for y in range(q)) for z in range(q)]
    G = R.sum(R.mul(chi(y), additive(y)) for y in f.nonzero)
    check("gauss_norm", R.mul(G, R.conj(G)), R.integer(q))
    check("zero_frequency", S[0], R.integer(-1))

    # T(h,t) is computed from its unscaled x-expression, not from S(ht).
    for h in range(q):
        for t in range(q):
            lhs = R.sum(atom(x, f.sub(x, h), f.mul(t, x)) for x in range(q))
            rhs = S[f.mul(h, t)] if h else R.integer(q - 1 if not t else -1)
            check("joint_kernel_and_axes", lhs, rhs)

    # All multiplicative dilation correlations determine the complete Gram.
    for a in f.nonzero:
        lhs = R.sum(R.mul(R.conj(S[t]), S[f.mul(t, a)]) for t in f.nonzero)
        rhs = R.add(R.integer(q * q if a == 1 else 0), R.neg(R.add(R.scale(chi(f.inv(a)), q), R.integer(q + 1))))
        # The displayed Gram is indexed (h,k); here h=1,k=a, hence chi(1/a).
        check("complete_dilation_gram", lhs, rhs)

    # Direct (2,1) hypergeometric numerator, including every nonunit zero.
    for z in f.nonzero:
        zi = f.inv(z)
        Hnum = R.zero
        for x in f.nonzero:
            for y in f.nonzero:
                v = f.mul(f.mul(x, y), zi)
                # denominator character is bar(chi), hence its conjugate is chi(v).
                term = R.mul(chi(v), additive(f.sub(f.add(x, y), v)))
                Hnum = R.add(Hnum, term)
        rhs = R.mul(R.mul(chi(minus_one, True), G), S[z])
        check("hypergeometric_2_1", Hnum, rhs)

    # Exact weighted Fourier completion with an arbitrary signed joint weight.
    # q*T = sum W_hat*T_h is checked to avoid rational arithmetic.
    weighted_direct = R.zero
    weighted_completed = R.zero
    for h in range(q):
        weights = [((7 * x + 11 * h + 3 * (x * h)) % 9) - 4 for x in range(q)]
        weighted_direct = R.add(weighted_direct, R.sum(R.scale(atom(x, f.sub(x, h)), weights[x]) for x in range(q)))
        for t in range(q):
            wh = R.sum(R.scale(additive(f.neg(f.mul(t, x))), weights[x]) for x in range(q))
            th = S[f.mul(h, t)] if h else R.integer(q - 1 if not t else -1)
            weighted_completed = R.add(weighted_completed, R.mul(wh, th))
    check("signed_weight_completion", R.scale(weighted_direct, q), weighted_completed)

    # Exact singular-vector energies: constant, chi, and another multiplicative mode.
    for sixth_power in (0, orientation, 2 * orientation):
        b = {h: R.monomial(sixth_power * f.logs[h], 0) for h in f.nonzero}
        energy = R.zero
        for t in f.nonzero:
            v = R.sum(R.mul(S[f.mul(t, h)], b[h]) for h in f.nonzero)
            energy = R.add(energy, R.mul(v, R.conj(v)))
        eig = 1 if sixth_power % 6 == 0 else q if sixth_power % 6 == orientation % 6 else q * q
        check("singular_mode_energy", energy, R.integer((q - 1) * eig))

    # A native-style autocorrelation coefficient has an exact Moyal budget.
    # Rational signed a_x suffice to test all normalization/sign conventions.
    a = [((5 * x + 2) % 7) - 3 for x in range(q)]
    norm = sum(z * z for z in a)
    total = R.zero
    recovered = R.zero
    for h in range(q):
        for t in range(q):
            ambiguity = R.sum(R.scale(additive(f.neg(f.mul(t, x))), a[x] * a[f.sub(x, h)]) for x in range(q))
            total = R.add(total, R.mul(ambiguity, R.conj(ambiguity)))
            th = S[f.mul(h, t)] if h else R.integer(q - 1 if not t else -1)
            recovered = R.add(recovered, R.mul(ambiguity, th))
    character_sum = R.sum(R.scale(chi(x), a[x]) for x in range(q))
    check("moyal_budget", total, R.integer(q * norm * norm))
    check("autocorrelation_reconstruction", recovered, R.scale(R.mul(character_sum, R.conj(character_sum)), q))

    # Negative controls: a missing zero mask, incorrect conjugation and an erased
    # h=0 axis must each disagree with their stated exact identity.
    corrupted_mask = R.add(S[0], R.one)  # assigns a spurious nonzero y=0 term
    check("negative_missing_zero_mask", corrupted_mask == R.integer(-1), False)
    wrong_orientation_witness = any(
        R.sum(R.mul(R.conj(S[t]), S[f.mul(t, a)]) for t in f.nonzero)
        != R.add(R.integer(q*q if a == 1 else 0), R.neg(R.add(R.scale(chi(a), q), R.integer(q+1))))
        for a in f.nonzero
    )
    check("negative_gram_orientation", wrong_orientation_witness, True)
    check("negative_erased_h_axis", S[0] == R.integer(q - 1), False)

    digest = hashlib.sha256(json.dumps(S, separators=(",", ":")).encode()).hexdigest()
    return {"q": q, "characteristic": p, "degree": degree,
            "quadratic_model_d": f.d if degree == 2 else None,
            "multiplicative_generator": f.generator, "sextic_orientation": orientation,
            "exact_checks": dict(sorted(counts.items())), "S_sha256": digest}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    cases = [run_field(p, d, o) for p, d in ((7,1), (13,1), (19,1), (31,1), (5,2), (7,2)) for o in (1,5)]
    result = {"status": "PASS", "arithmetic": "exact integers in Q(zeta_6,zeta_p)",
              "fields": cases, "total_predicates": sum(sum(c["exact_checks"].values()) for c in cases),
              "scope": "finite algebra only; no asymptotic or monodromy certification",
              "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(encoded)
    print(encoded)


if __name__ == "__main__":
    main()
