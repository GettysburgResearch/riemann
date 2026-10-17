#!/usr/bin/env python3
"""Exact finite fixtures for COMPLETION_AND_COVARIANCE.md.

These check coefficient identities, original separate caps, BV superposition,
and the maximal endpoint construction. They do not test an asymptotic bound,
the imported common zero-free strip, global novelty, or RH.
"""
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from math import gcd
from pathlib import Path
import json

N = 256
digest = sha256()
counts = {}


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def require_rejection(condition, label):
    try:
        require(condition, label)
    except AssertionError:
        count("rejected_negative_controls")
        return
    raise AssertionError("corruption passed: " + label)


def count(name, amount=1):
    counts[name] = counts.get(name, 0) + amount


def record(tag, values):
    digest.update((tag + ":" + ",".join(str(v) for v in values) + "\n").encode())


def primes(n):
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for p in range(2, n + 1):
        if sieve[p]:
            yield p
            for j in range(p * p, n + 1, p):
                sieve[j] = False


def mu(n):
    answer = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            answer = -answer
            if n % p == 0:
                return 0
            while n % p == 0:
                n //= p
        p += 1
    return -answer if n > 1 else answer


def chi3(n):
    return (0, 1, -1)[n % 3]


def twist(n, kind):
    return 1 if kind == "one" else (0, 1, 0, -1)[n % 4]


def convolution(a, b, cap):
    out = [F(0) for _ in range(cap + 1)]
    for d in range(1, min(cap, len(a) - 1) + 1):
        if a[d]:
            for m in range(1, min(cap // d, len(b) - 1) + 1):
                if b[m]:
                    out[d * m] += a[d] * b[m]
    return out


def ideal_primes(cap):
    for p in primes(cap):
        if p == 3:
            yield "3", 3, 0
        elif p % 3 == 1:
            yield str(p) + "a", p, 0
            yield str(p) + "b", p, 1
        elif p * p <= cap:
            yield str(p), p * p, 0


def local_polynomials(family, degree, q, side, excluded, cap):
    powers = [1]
    while powers[-1] <= cap // q:
        powers.append(powers[-1] * q)
    top = len(powers) - 1
    source = [F(0) for _ in powers]
    correction = [F(0) for _ in powers]
    source[0] = correction[0] = F(1)
    profile = (F(1), F(-1, 2), F(0))[(q + side) % 3]
    powerful = profile * q ** (degree // 2 - 1)
    if excluded:
        correction = [F(1) for _ in powers]
    elif family == "native":
        if top:
            source[1] = -1
    elif family == "coupled":
        if top:
            source[1] = -1 + F(1, q)
        if degree <= top:
            source[degree] -= powerful
        for j in range(1, top + 1):
            correction[j] = F(1, q) - (powerful if j >= degree else 0)
    elif family == "two_channel":
        if top:
            source[1] = -1
        if degree <= top:
            source[degree] -= powerful
            correction[degree] -= powerful
        if degree + 1 <= top:
            source[degree + 1] += powerful
    elif family == "geometric":
        for j in range((top - 1) // degree + 1):
            source[1 + j * degree] = -(1 - F(1, q)) * powerful ** j
        for j in range(1, top + 1):
            h = (j - 1) // degree
            correction[j] = F(1, q) + (F(1, q) - 1) * sum(
                (powerful ** t for t in range(1, h + 1)), F(0)
            )
    else:
        raise AssertionError(family)
    for j in range(top + 1):
        require(source[j] == correction[j] - (correction[j - 1] if j else 0),
                "ideal-local completion identity")
        count("ideal_local_coefficients_checked")
    return powers, source, correction


def euler_multiply(old, powers, poly, cap):
    out = [F(0) for _ in range(cap + 1)]
    for d, value in zip(powers, poly):
        if value:
            for m in range(1, cap // d + 1):
                if old[m]:
                    out[d * m] += value * old[m]
    return out


mobius = [0] + [mu(n) for n in range(1, N + 1)]
mu_chi = [0] + [mobius[n] * chi3(n) for n in range(1, N + 1)]
native = convolution(mobius, mu_chi, N)
archives = {}
families = [("native", 2)] + [(f, m) for f in
    ("coupled", "two_channel", "geometric") for m in (2, 4, 6)]

for family, degree in families:
    for mask_name, mask in (("empty", set()), ("asymmetric", {"3", "7a"})):
        source = [F(0) for _ in range(N + 1)]
        correction = source.copy()
        source[1] = correction[1] = F(1)
        for label, q, side in ideal_primes(N):
            powers, f, b = local_polynomials(family, degree, q, side,
                                            label in mask, N)
            source = euler_multiply(source, powers, f, N)
            correction = euler_multiply(correction, powers, b, N)
        for character in ("one", "chi4"):
            a = [native[n] * twist(n, character) for n in range(N + 1)]
            b = [correction[n] * twist(n, character) for n in range(N + 1)]
            c = [source[n] * twist(n, character) for n in range(N + 1)]
            require(convolution(a, b, N) == c, "complete norm identity")
            key = (family, degree, mask_name, character)
            archives[key] = (a, b, c)
            count("complete_norm_cases")
            count("complete_norm_coefficients_checked", N)
            record(str(key), c[1:])

# Reject deleting the inverse-native repair at an excluded ramified prime.
control_a, control_b, control_c = archives[("native", 2, "asymmetric", "one")]
broken_b = control_b.copy()
broken_b[3] = F(0)
require_rejection(convolution(control_a, broken_b, N) == control_c,
                  "excluded-prime repair deleted")

# Independent exact tuple enumeration. Fractional caps preserve L<n<=U.
def tuples_with_product(cap, bounds, arrays=None):
    def walk(i, remaining, chosen, total):
        if i == len(bounds):
            yield tuple(chosen), total
            return
        lo, hi = bounds[i]
        low = max(1, lo.numerator // lo.denominator + 1)
        high = min(remaining, hi.numerator // hi.denominator)
        for n in range(low, high + 1):
            if arrays is None or arrays[i][n]:
                yield from walk(i + 1, remaining // n, chosen + [n], total * n)
    yield from walk(0, cap, [], 1)


def tensor(arrays, cap, bounds):
    out = [F(0) for _ in range(cap + 1)]
    for ns, total in tuples_with_product(cap, bounds, arrays):
        value = F(1)
        for i, n in enumerate(ns):
            value *= arrays[i][n]
        out[total] += value
    return out


columns = [archives[("coupled", 2, "asymmetric", "one")],
           archives[("geometric", 4, "empty", "chi4")],
           archives[("two_channel", 2, "empty", "one")]]

for k in (1, 2, 3):
    cap = 96
    bounds = [(F(0), F(80)), (F(2), F(72)), (F(0), F(48))][:k]
    arrays = [x[0] for x in columns[:k]]
    expected = tensor(arrays, cap, bounds)
    grouped = [F(0) for _ in range(cap + 1)]
    ownership = {}
    for owner in range(k):
        other_indices = [i for i in range(k) if i != owner]
        other_bounds = [bounds[i] for i in other_indices]
        for others, a in tuples_with_product(cap, other_bounds):
            if a ** k > cap ** (k - 1):
                continue
            fixed = dict(zip(other_indices, others))
            lo = bounds[owner][0].numerator // bounds[owner][0].denominator
            for i, n in fixed.items():
                lo = max(lo, n if i < owner else n - 1)
            hi = min(cap // a, int(bounds[owner][1]))
            for free in range(lo + 1, hi + 1):
                ns = tuple(free if i == owner else fixed[i] for i in range(k))
                ownership[ns] = ownership.get(ns, 0) + 1
                value = F(1)
                for i, n in enumerate(ns):
                    value *= arrays[i][n]
                grouped[a * free] += value
    literal_tuples = [ns for ns, _ in tuples_with_product(cap, bounds)]
    require(set(ownership) == set(literal_tuples), "complete tuple partition")
    require(all(v == 1 for v in ownership.values()), "unique largest-factor owner")
    require(grouped == expected, "largest-factor coefficient equality")
    count("largest_factor_cases")
    count("largest_factor_tuples_checked", len(literal_tuples))
    count("tie_tuples_retained", sum(len(set(ns)) < k for ns in literal_tuples))
    count("shared_prime_tuples_retained", sum(any(gcd(ns[i], ns[j]) > 1
        for i in range(k) for j in range(i)) for ns in literal_tuples))
    record("largest" + str(k), grouped[1:])

    # Expand correction norms FIRST, rescale every original cap by its own
    # d_i, retain the exact total-product cutoff, and regroup n=d*m.
    completed = tensor([x[2] for x in columns[:k]], cap, bounds)
    regrouped = [F(0) for _ in range(cap + 1)]
    wrong_caps = [F(0) for _ in range(cap + 1)]
    corrections = [x[1] for x in columns[:k]]
    free_bounds = [(F(0), F(cap))] * k
    for ds, d in tuples_with_product(cap, free_bounds, corrections):
        value = F(1)
        rescaled = []
        for i, di in enumerate(ds):
            value *= corrections[i][di]
            rescaled.append((bounds[i][0] / di, bounds[i][1] / di))
        inner = tensor(arrays, cap // d, rescaled)
        for m in range(1, len(inner)):
            regrouped[d * m] += value * inner[m]
        if k == 2:
            # Deliberately omit the separate d_i rescaling of original caps.
            broken = tensor(arrays, cap // d, bounds)
            for m in range(1, len(broken)):
                wrong_caps[d * m] += value * broken[m]
        count("correction_norm_tuples_checked")
    require(completed == regrouped, "exact individually rescaled caps")
    if k == 2:
        require_rejection(completed == wrong_caps, "individual cap rescaling omitted")
    count("complete_cap_cases")
    count("complete_cap_coefficients_checked", cap)
    record("completed_cap" + str(k), completed[1:])

# An exact nonmonotone left-continuous BV step weight in each original
# column, including a cap beyond every inspected norm (no deletion at X).
cap = 96
atoms = [[(7, F(1)), (27, F(-3, 2)), (1000, F(2, 3))],
         [(4, F(-1, 3)), (35, F(5, 4)), (1000, F(1, 2))]]
weighted = []
for i in range(2):
    weighted.append([columns[i][2][n] * sum((weight for bound, weight in atoms[i]
                     if n <= bound), F(0)) for n in range(cap + 1)])
literal_bv = convolution(weighted[0], weighted[1], cap)
measure_bv = [F(0) for _ in range(cap + 1)]
for choice in product(*atoms):
    bounds = [(F(0), F(bound)) for bound, _ in choice]
    weight = choice[0][1] * choice[1][1]
    row = tensor([columns[0][2], columns[1][2]], cap, bounds)
    for n in range(1, cap + 1):
        measure_bv[n] += weight * row[n]
    count("bv_atomic_tensor_terms")
require(literal_bv == measure_bv, "left-continuous BV cap superposition")
count("bv_coefficients_checked", cap)
record("bv", literal_bv[1:])

# Quantile endpoints isolate heavy atoms. Everything below is rational;
# no sampled Fourier transform or floating point threshold is used.
small = 16
g = [F(0)] + [F((7 * n) % 11 - 5) for n in range(1, 2 * small + 1)]
g2 = sum((v * v for v in g), F(0))
test_sources = [columns[0][2][:small + 1],
                [F(0)] + [F(100 if n == 8 else (n % 5 - 2))
                           for n in range(1, small + 1)],
                [F(0)] + [F(0) if n != 16 else F(-17)
                           for n in range(1, small + 1)]]

def gv(n):
    return g[n] if 1 <= n <= 2 * small else F(0)


for case, a in enumerate(test_sources):
    mass = [F(0)]
    for n in range(1, small + 1):
        mass.append(mass[-1] + a[n] ** 2)
    total = mass[-1]
    correlations = {}
    for h in range(-small, 2 * small + 1):
        row = [F(0)]
        for n in range(1, small + 1):
            row.append(row[-1] + a[n] * gv(n + h))
        correlations[h] = row
    for y in range(small + 1):
        lhs = sum((row[y] ** 2 for row in correlations.values()), F(0))
        rhs = sum((a[n] * a[m] * sum((gv(n + h) * gv(m + h)
                   for h in range(-small, 2 * small + 1)), F(0))
                   for n in range(1, y + 1) for m in range(1, y + 1)), F(0))
        require(lhs == rhs, "finite full-shift quadratic expansion")
        count("full_shift_quadratic_expansions")
    for bins in range(1, 9):
        endpoints = {0, small}
        for j in range(1, bins):
            index = next(n for n in range(1, small + 1)
                         if mass[n] >= F(j, bins) * total)
            endpoints.update((index - 1, index))
        require(len(endpoints) <= 2 * bins, "endpoint count")
        for y in range(small + 1):
            previous = max(e for e in endpoints if e <= y)
            require(mass[y] - mass[previous] <= total / bins, "residual square mass")
            count("maximal_residual_prefixes_checked")
        for h in range(1, small + 1):
            row = correlations[h]
            maximum2 = max(v * v for v in row)
            majorant = 2 * sum((row[e] ** 2 for e in endpoints), F(0))
            majorant += 2 * (total / bins) * g2
            require(maximum2 <= majorant, "maximal endpoint inequality")
            count("maximal_endpoint_inequalities_checked")
        count("maximal_partition_cases")
    record("maximal_mass" + str(case), mass)
    if case == 1:
        # A regular index grid can strand the mass-10000 atom in a residual.
        require_rejection(mass[8] - mass[4] <= total / 4,
                          "index grid substituted for square-mass quantiles")

for k in range(1, 7):
    theta = F(7, 8)
    native_exponent = (1 + theta) / 2
    beta = 1 - (1 - native_exponent) / k
    require(native_exponent == F(15, 16), "native exponent")
    require(beta == 1 - F(1, 16 * k), "complete cap exponent")
    require(2 * beta - 1 == 1 - F(1, 8 * k), "shift threshold")
    require((1 - beta) / 2 == F(1, 32 * k), "full shift range saving")
    count("exact_exponent_cases")
    record("exponent" + str(k), [native_exponent, beta, 2 * beta - 1, (1 - beta) / 2])

report = {
    "status": "PASS",
    "arithmetic": "exact integers and fractions; no floating point",
    "norm_cutoff": N,
    "tensor_cutoff": 96,
    "counts": counts,
    "exact_stream_sha256": digest.hexdigest(),
    "scope": "finite coefficient, cap, BV, and maximal-partition fixtures only; not a proof of the imported strip or an asymptotic power bound",
}
output = json.dumps(report, indent=2, sort_keys=True) + "\n"
Path(__file__).with_name("CAPPED_CHECK_RESULTS.json").write_text(output)
print(output, end="")
