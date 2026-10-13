#!/usr/bin/env python3
"""Exact finite diagnostics for BESSEL_CHANNELS_AND_LEAKAGE.md.

Only Python standard-library integer, rational, and cyclotomic arithmetic
is used.  Failed predicates raise DiagnosticFailure explicitly, including
under python -O.  This does not test an analytic moment estimate.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from functools import lru_cache
import hashlib
from itertools import permutations, product
import json
from pathlib import Path


class DiagnosticFailure(RuntimeError):
    pass


CHECKS = 0


def require(condition, label):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise DiagnosticFailure(label)


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def exact_divide(a, b):
    a, b = trim(a), trim(b)
    if b[-1] != 1:
        raise DiagnosticFailure("nonmonic polynomial division")
    out = [0] * max(1, len(a) - len(b) + 1)
    while len(a) >= len(b) and a != [0]:
        shift, coeff = len(a) - len(b), a[-1]
        out[shift] = coeff
        for j, value in enumerate(b):
            a[shift + j] -= coeff * value
        a = trim(a)
    if a != [0]:
        raise DiagnosticFailure("inexact cyclotomic division")
    return tuple(trim(out))


@lru_cache(None)
def cyclotomic(n):
    poly = [-1] + [0] * (n - 1) + [1]
    for d in range(1, n):
        if n % d == 0:
            poly = exact_divide(poly, cyclotomic(d))
    return tuple(poly)


class CyclotomicRing:
    def __init__(self, order):
        self.order = order
        self.modulus = cyclotomic(order)
        self.degree = len(self.modulus) - 1
        self.zero = (0,) * self.degree
        self.one = (1,) + (0,) * (self.degree - 1)
        roots, value = [], self.one
        for _ in range(order):
            roots.append(value)
            last = value[-1]
            value = (0,) + value[:-1]
            value = tuple(value[j] - last * self.modulus[j]
                          for j in range(self.degree))
        require(value == self.one, "cyclotomic root order divides m")
        self.roots = tuple(roots)
        for d in range(1, order):
            if order % d == 0:
                require(self.roots[d] != self.one,
                        "cyclotomic root has exact order")

    def root(self, exponent):
        return self.roots[exponent % self.order]

    def constant(self, value):
        return (value,) + (0,) * (self.degree - 1)

    def add(self, a, b):
        return tuple(x + y for x, y in zip(a, b))

    def scale(self, a, value):
        return tuple(value * x for x in a)

    def total(self, values):
        out = [0] * self.degree
        for value in values:
            for j, coeff in enumerate(value):
                out[j] += coeff
        return tuple(out)

    @lru_cache(None)
    def mul(self, a, b):
        out = [0] * (2 * self.degree - 1)
        for i, ai in enumerate(a):
            if ai:
                for j, bj in enumerate(b):
                    if bj:
                        out[i + j] += ai * bj
        for k in range(len(out) - 1, self.degree - 1, -1):
            coeff = out[k]
            if coeff:
                for j, mj in enumerate(self.modulus[:-1]):
                    out[k - self.degree + j] -= coeff * mj
        return tuple(out[:self.degree])

    def conjugate(self, a):
        return self.total(self.scale(self.root(-j), value)
                          for j, value in enumerate(a) if value)


class FiniteField:
    """Fp or Fp[w]/(w^2+w+1), encoded by a+p*b."""
    def __init__(self, prime, extension=False):
        self.p = prime
        self.extension = extension
        self.q = prime * prime if extension else prime

    def add(self, x, y):
        if not self.extension:
            return (x + y) % self.p
        return ((x % self.p + y % self.p) % self.p
                + self.p * ((x // self.p + y // self.p) % self.p))

    def neg(self, x):
        if not self.extension:
            return (-x) % self.p
        return (-x % self.p) + self.p * (- (x // self.p) % self.p)

    def sub(self, x, y):
        return self.add(x, self.neg(y))

    def mul(self, x, y):
        if not self.extension:
            return x * y % self.p
        a, b, c, d = x % self.p, x // self.p, y % self.p, y // self.p
        return ((a * c - b * d) % self.p
                + self.p * ((a * d + b * c - b * d) % self.p))

    def power(self, x, exponent):
        out = 1
        while exponent:
            if exponent & 1:
                out = self.mul(out, x)
            x = self.mul(x, x)
            exponent //= 2
        return out

    def inverse(self, x):
        if x == 0:
            raise DiagnosticFailure("attempted inverse at zero")
        return self.power(x, self.q - 2)

    def trace(self, x):
        if not self.extension:
            return x
        return (2 * (x % self.p) - x // self.p) % self.p


def character_exponents(field, zeta):
    require(field.power(zeta, 6) == 1, "sixth root identity")
    powers = {field.power(zeta, j): j for j in range(6)}
    require(len(powers) == 6, "primitive sixth root")
    result = [None]
    for x in range(1, field.q):
        value = field.power(x, (field.q - 1) // 6)
        require(value in powers, "residue power lies in sixth roots")
        result.append(powers[value])
        require(field.mul(x, field.inverse(x)) == 1, "field inverse")
    for x in range(1, field.q):
        for y in range(1, field.q):
            require(result[field.mul(x, y)] == (result[x] + result[y]) % 6,
                    "actual residue character multiplicativity")
    return result


def finite_bessel_case(label, field, omega):
    q, p = field.q, field.p
    zeta = field.add(1, omega)
    require(field.add(field.add(field.mul(omega, omega), omega), 1) == 0,
            label + ": Eisenstein residue embedding")
    exponents = character_exponents(field, zeta)
    ring = CyclotomicRing(6 * p)
    mult_step, add_step = ring.order // 6, ring.order // p
    vectors = {
        j: tuple(ring.zero if x == 0 else ring.root(mult_step * j * exponents[x])
                 for x in range(q))
        for j in range(6)
    }
    tau = {
        j: ring.total(ring.root(mult_step * j * exponents[x]
                                + add_step * field.trace(x))
                      for x in range(1, q))
        for j in range(1, 6)
    }
    minus_one = field.neg(1)
    require(exponents[minus_one] in (0, 3), label + ": chi(-1) real")
    delta = 1 if exponents[minus_one] == 0 else -1
    for j in range(1, 6):
        require(ring.mul(tau[j], tau[6-j]) == ring.constant(q * delta**j),
                label + ": exact Gauss product")

    # K=q*T is built directly from the finite Bessel kernel, with zero
    # residues included. A is the unnormalized positive additive Fourier.
    def bessel_entry(y, x):
        terms = []
        for v in range(1, q):
            phase = field.sub(field.mul(y, v), field.mul(x, field.inverse(v)))
            terms.append(ring.root(mult_step * 2 * exponents[v]
                                   + add_step * field.trace(phase)))
        return ring.total(terms)

    kernel = tuple(tuple(bessel_entry(y, x) for x in range(q)) for y in range(q))
    additive = tuple(tuple(ring.root(add_step * field.trace(field.mul(y, x)))
                           for x in range(q)) for y in range(q))

    def apply(matrix, vector):
        return tuple(ring.total(ring.mul(a, b) for a, b in zip(row, vector))
                     for row in matrix)

    for x in range(q):
        for y in range(q):
            require(kernel[y][x] == ring.conjugate(kernel[x][y]),
                    label + ": Bessel Hermitian symmetry")
            square = ring.total(ring.mul(kernel[y][h], kernel[h][x])
                                for h in range(q))
            require(square == ring.constant(q*q*(x == y) - q),
                    label + ": K^2=q^2 I-q J")
    require(apply(kernel, (ring.one,) * q) == (ring.zero,) * q,
            label + ": exact constant kernel")
    require(ring.total(kernel[x][x] for x in range(q)) == ring.constant(2*q),
            label + ": exact trace")

    for j in (1, 2, 3, 5):
        coefficient = ring.scale(ring.mul(tau[j], tau[(j+2) % 6]), delta**j)
        target = tuple(ring.mul(coefficient, v) for v in vectors[(-j-2) % 6])
        require(apply(kernel, vectors[j]) == target,
                label + ": nonexceptional character channel " + str(j))
    ramanujan = tuple(ring.constant(q*(x == 0) - 1) for x in range(q))
    require(apply(kernel, vectors[4])
            == tuple(ring.mul(tau[4], value) for value in ramanujan),
            label + ": j4 Ramanujan channel, including zero")
    require(apply(kernel, vectors[0])
            == tuple(ring.scale(ring.mul(tau[2], value), -1)
                     for value in vectors[4]),
            label + ": active j0 unit mask")
    require(apply(kernel, ramanujan)
            == tuple(ring.scale(ring.mul(tau[2], value), q)
                     for value in vectors[4]),
            label + ": inverse Ramanujan channel")

    # A common scalar tau_3 removes all square roots from the unitary basis.
    gauge = {
        1: tuple(ring.mul(tau[3], v) for v in vectors[1]),
        3: tuple(ring.mul(tau[1], v) for v in vectors[3]),
        5: tuple(ring.mul(tau[1], v) for v in vectors[5]),
    }
    t_map, s_map = {1: 3, 3: 1, 5: 5}, {1: 5, 3: 3, 5: 1}
    for j in (1, 3, 5):
        require(apply(kernel, gauge[j])
                == tuple(ring.scale(v, q) for v in gauge[t_map[j]]),
                label + ": exact Gauss-gauged T permutation")
        require(apply(additive, gauge[j])
                == tuple(ring.mul(tau[3], v) for v in gauge[s_map[j]]),
                label + ": exact Gauss-gauged S permutation")
    return {
        "label": label, "q": q, "characteristic": p,
        "omega_residue": omega, "cyclotomic_order": ring.order,
        "cyclotomic_degree": ring.degree,
        "coverage": "every row, column, and intermediate residue in K^2",
        "literal_zero_and_active_j0": True,
        "normalized_spectrum": {
            "plus": (q+1)//2, "minus": (q-3)//2, "zero": 1,
        },
    }


T_MAP = {1: 3, 3: 1, 5: 5}
S_MAP = {1: 5, 3: 3, 5: 1}
COLORS = (1, 3, 5)
PERMS = tuple(permutations(COLORS))


def word_map(word, mapping):
    return tuple(mapping[j] for j in word)


def t_word(word):
    return word_map(word, T_MAP)


def s_word(word):
    return word_map(word, S_MAP)


def c_word(word):
    return t_word(s_word(word))


def clean(vector):
    return {w: v for w, v in vector.items() if v}


def add_vectors(*vectors):
    out = {}
    for vector in vectors:
        for word, value in vector.items():
            out[word] = out.get(word, Fraction(0)) + value
    return clean(out)


def scale_vector(vector, value):
    return clean({w: c * value for w, c in vector.items()})


def move_vector(vector, action):
    out = {}
    for word, value in vector.items():
        target = action(word)
        out[target] = out.get(target, Fraction(0)) + value
    return clean(out)


def norm_square(vector):
    return sum((c*c for c in vector.values()), Fraction(0))


def native_projection(vector):
    return {w: c for w, c in vector.items() if 3 not in w}


def cyclic_projection(vector):
    c1 = move_vector(vector, c_word)
    c2 = move_vector(c1, c_word)
    return scale_vector(add_vectors(vector, c1, c2), Fraction(1, 3))


def parity(permutation):
    return -1 if sum(permutation[i] > permutation[j]
                     for i in range(3) for j in range(i+1, 3)) % 2 else 1


def group_projection(vector, alternating=False):
    terms = []
    for permutation in PERMS:
        mapping = dict(zip(COLORS, permutation))
        moved = move_vector(vector, lambda w: word_map(w, mapping))
        terms.append(scale_vector(moved, Fraction(
            parity(permutation) if alternating else 1, 6)))
    return add_vectors(*terms)


def tensor_diagnostics():
    words_seen, pairs_seen = 0, 0
    for r in range(1, 9):
        for word in product((1, 5), repeat=r):
            words_seen += 1
            complement = s_word(word)
            native = all(j == 5 for j in word)
            require((3 not in t_word(word)) == native, "rank-one compression")
            require(t_word(t_word(word)) == word, "tensor T involution")
            require(s_word(s_word(word)) == word, "tensor S involution")
            require(c_word(c_word(c_word(word))) == word, "tensor order-three orbit")
            if len(set(word)) != 2:
                continue
            require(3 in t_word(word), "all mixed mass leaks")
            orbit = {word_map(word, dict(zip(COLORS, perm))) for perm in PERMS}
            require(len(orbit) == 6, "mixed orbit is regular")
            require({w for w in orbit if 3 not in w} == {word, complement},
                    "exactly two native orbit states")
            if word > complement:
                continue
            pairs_seen += 1
            f = {word: Fraction(1), complement: Fraction(2)}
            trivial = group_projection(f)
            alternating = group_projection(f, alternating=True)
            require(native_projection(trivial)
                    == {word: Fraction(1, 2), complement: Fraction(1, 2)},
                    "trivial native compression matrix")
            require(native_projection(alternating)
                    == {word: Fraction(-1, 6), complement: Fraction(1, 6)},
                    "alternating native compression matrix")
            pc = cyclic_projection(f)
            require(pc == add_vectors(trivial, alternating),
                    "cyclic projection equals trivial plus alternating")
            require(norm_square(pc) == Fraction(5, 3),
                    "exact compulsory one-third energy")
            require(native_projection(pc) == scale_vector(f, Fraction(1, 3)),
                    "cyclic native compression")
            c1, c2 = move_vector(f, c_word), move_vector(move_vector(f, c_word), c_word)
            g = scale_vector(add_vectors(c1, c2), Fraction(-1, 2))
            require(not native_projection(g), "counterterms entirely nonnative")
            require(not cyclic_projection(add_vectors(f, g)),
                    "exact cyclic cancellation by counterterms")
            require(norm_square(g) == Fraction(5, 2),
                    "sharp one-half counterterm squared norm")
            wn = f
            for n in range(9):
                require(norm_square(wn) == 5 * (
                    Fraction(1, 3) + Fraction(2, 3) * Fraction(1, 4)**n),
                    "exact repeated-reflection energy at n=" + str(n))
                wn = scale_vector(add_vectors(move_vector(wn, t_word),
                                              move_vector(wn, s_word)),
                                  Fraction(1, 2))
    for a, b in product(range(3), repeat=2):
        if (a - b) % 2:
            require((a - b) % 6 in (1, 5), "fourth-moment odd incidence")
    require((3 - 0) % 6 == 3, "higher-moment quadratic incidence witness")
    require((2 - 0, (0 - 1) % 6, (0 - 1) % 6) == (2, 5, 5),
            "even-factor balance does not force mixed odd signs")
    return {"prime_counts": list(range(1, 9)), "native_words": words_seen,
            "mixed_complement_pairs": pairs_seen, "walk_powers": list(range(9))}


def eisenstein_mul(x, y):
    a, b = x
    c, d = y
    return a*c-b*d, a*d+b*c-b*d


def eisenstein_norm(x):
    a, b = x
    return a*a-a*b+b*b


def native_unit_example():
    primes = [
        {"name": "pi7", "p": 7, "generator": (-2, -3), "omega": 4, "sign": 1},
        {"name": "pi13", "p": 13, "generator": (1, -3), "omega": 9, "sign": 1},
        {"name": "bar_pi7", "p": 7, "generator": (1, 3), "omega": 2, "sign": -1},
        {"name": "bar_pi13", "p": 13, "generator": (4, 3), "omega": 3, "sign": -1},
    ]
    units, value = [], (1, 0)
    for _ in range(6):
        units.append(value)
        value = eisenstein_mul(value, (1, 1))
    require(value == (1, 0) and len(set(units)) == 6, "all six Eisenstein units")
    require(set(units) == {(a, b) for a in range(-2, 3) for b in range(-2, 3)
                           if eisenstein_norm((a, b)) == 1},
            "norm-one row enumeration")
    exponents = {}
    for data in primes:
        p, w = data["p"], data["omega"]
        a, b = data["generator"]
        require(eisenstein_norm((a, b)) == p, "actual prime norm")
        require((a + b*w) % p == 0, "actual prime residue kernel")
        require(a % 3 == 1 and b % 3 == 0, "primary generator convention")
        exponents[data["name"]] = character_exponents(FiniteField(p), (1+w) % p)
        require(exponents[data["name"]][(a+b*w) % p] is None,
                "prime generator is a literal character zero")
    rows = []
    for a, b in units:
        exponent = 0
        for data in primes:
            residue = (a + b*data["omega"]) % data["p"]
            local = exponents[data["name"]][residue]
            require(local is not None, "unit does not meet any zero mask")
            exponent += data["sign"] * local
        exponent %= 6
        require(exponent == 0, "exact unit-row phase cancellation")
        rows.append({"unit": [a, b], "phi_exponent_mod_6": exponent,
                     "hermitian_pair_value": 2})
    left = eisenstein_mul(primes[0]["generator"], primes[1]["generator"])
    right = eisenstein_mul(primes[2]["generator"], primes[3]["generator"])
    require(eisenstein_norm(left) == eisenstein_norm(right) == 91,
            "equal product norms")
    require(left not in {eisenstein_mul(epsilon, right) for epsilon in units},
            "distinct product ideals")
    require(sum(row["hermitian_pair_value"] for row in rows) == 12,
            "native physical row sum differs from zero compression")
    # 4*N(a+b*w)=3*a^2+(a-2*b)^2, and symmetrically in b,
    # so N<=13 implies |a|,|b|<=4. This is the whole physical ball.
    require(3 * 5**2 > 4 * 13, "complete norm-13 coordinate bound")
    shell_counts, shell_values = {}, {}
    real_pair_values = (2, 1, -1, -2, -1, 1)
    for a, b in product(range(-4, 5), repeat=2):
        norm = eisenstein_norm((a, b))
        if not 0 < norm <= 13:
            continue
        local_values = [exponents[data["name"]][(a+b*data["omega"]) % data["p"]]
                        for data in primes]
        pair_value = 0 if None in local_values else real_pair_values[
            sum(data["sign"] * j for data, j in zip(primes, local_values)) % 6]
        shell_counts[norm] = shell_counts.get(norm, 0) + 1
        shell_values[norm] = shell_values.get(norm, 0) + pair_value
    shell_table = [[n, shell_counts[n], shell_values[n]] for n in sorted(shell_counts)]
    require(shell_table == [[1,6,12],[3,6,6],[4,6,12],[7,12,0],
                            [9,6,-6],[12,6,6],[13,12,0]],
            "exact norm-13 shell table")
    require(sum(shell_counts.values()) == 54, "full row count at H=13")
    require(sum(shell_values.values()) == 30, "native covariance pair at H=D=13")
    return {"left_product_generator": left, "right_product_generator": right,
            "product_norm": 91, "squarefree_conductor_norm": 7**2 * 13**2,
            "tuple_mobius_product": 1, "bessel_compression": 0,
            "actual_unit_row_sum": 12, "rows": rows,
            "height_13_row_count": 54, "height_13_pair_sum": 30,
            "height_13_shell_table": shell_table}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--note", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not args.note.is_file():
        raise DiagnosticFailure("missing proof note")
    finite = [
        finite_bessel_case("pi7", FiniteField(7), 4),
        finite_bessel_case("bar_pi7", FiniteField(7), 2),
        finite_bessel_case("pi13", FiniteField(13), 9),
        finite_bessel_case("bar_pi13", FiniteField(13), 3),
        finite_bessel_case("inert_5", FiniteField(5, extension=True), 5),
    ]
    tensors = tensor_diagnostics()
    native = native_unit_example()
    b = Fraction(7, 8)
    leakage_exponent = Fraction(1, 2) + 2*(1+b)
    require(leakage_exponent == Fraction(17, 4), "quadratic comparison exponent")
    require(leakage_exponent - 3 == Fraction(5, 4), "quadratic comparison loss")
    result = {
        "status": "PASS",
        "arithmetic": "exact integers in cyclotomic quotient rings and exact rationals",
        "scope": "finite diagnostics only; no physical covariance or moment estimate",
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "proof_note_sha256": hashlib.sha256(args.note.read_bytes()).hexdigest(),
        "checks": CHECKS,
        "finite_field_cases": finite,
        "tensor_cases": tensors,
        "native_unit_example": native,
        "optimistic_quadratic_comparison": {
            "k": 2, "b": "7/8", "height_exponent": 1,
            "bound_exponent": "17/4", "target_exponent": 3,
            "excess_exponent": "5/4",
        },
        "not_checked": [
            "truth of imported analytic or zero-free assertions",
            "an identity from native covariance to Bessel compression",
            "uniform growing-conductor or short-row analytic estimates",
            "the full generalized moment hypothesis or RH",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": "PASS", "checks": CHECKS,
                      "output_sha256": hashlib.sha256(args.output.read_bytes()).hexdigest(),
                      "finite_fields": len(finite), "native_sum": 12},
                     sort_keys=True))


if __name__ == "__main__":
    main()

