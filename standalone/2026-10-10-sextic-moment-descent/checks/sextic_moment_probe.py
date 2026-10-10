"""Finite diagnostic for actual Eisenstein sextic symbols; not a proof of a moment bound.

Field: Z[omega], omega^2 + omega + 1 = 0. Fixed twist nu=1.
Column prime ideals above 2 and 3 are excluded. Every element row in the norm
ball is included. Arithmetic symbols and squarefree factorizations are exact;
the C-infinity bump, complex sums and moments use ordinary binary64 arithmetic.
"""
import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
import numpy as np

UNITS = [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1)]
ROOTS = np.exp(1j * np.pi * np.arange(6) / 3)


def multiply(x, y):
    a, b = x
    c, d = y
    return a*c-b*d, a*d+b*c-b*d


def power(x, n):
    y = (1, 0)
    while n:
        if n & 1:
            y = multiply(y, x)
        x = multiply(x, x)
        n //= 2
    return y


def primes_to(n):
    sieve = np.ones(n+1, dtype=bool)
    sieve[:2] = False
    for p in range(2, math.isqrt(n)+1):
        if sieve[p]:
            sieve[p*p::p] = False
    return [int(p) for p in np.flatnonzero(sieve)]


def prime_ideals(n):
    out = []
    for p in primes_to(n):
        if p in (2, 3):
            continue
        if p % 3 == 1:
            g = 2
            while pow(g, (p-1)//3, p) == 1:
                g += 1
            r = pow(g, (p-1)//3, p)
            for root in sorted((r, r*r % p)):
                if (root*root+root+1) % p:
                    raise RuntimeError("Invalid split prime root")
                out.append({"p": p, "norm": p, "root": root})
        elif p*p <= n:
            out.append({"p": p, "norm": p*p, "root": None})
    return sorted(out, key=lambda q: (q["norm"], q["p"], q["root"] or -1))


def mod_power_array(a, e, p):
    out = np.ones_like(a)
    while e:
        if e & 1:
            out = out*a % p
        a = a*a % p
        e //= 2
    return out


def field_power_array(a, b, e, p):
    x, y = np.ones_like(a), np.zeros_like(a)
    while e:
        if e & 1:
            x, y = (x*a-y*b) % p, (x*b+y*a-y*b) % p
        a, b = (a*a-b*b) % p, (2*a*b-b*b) % p
        e //= 2
    return x, y


def symbols(q, a, b):
    """Return exact exponents 0..5, or -1 for the nonunit zero extension."""
    p = q["p"]
    out = np.full(a.shape, -2, dtype=np.int8)
    if q["root"] is not None:
        z = (a + q["root"]*b) % p
        zpow = mod_power_array(z, (p-1)//6, p)
        out[z == 0] = -1
        for j, (x, y) in enumerate(UNITS):
            out[(z != 0) & (zpow == (x+q["root"]*y) % p)] = j
    else:
        aa, bb = a % p, b % p
        x, y = field_power_array(aa, bb, (p*p-1)//6, p)
        nonzero = (aa != 0) | (bb != 0)
        out[~nonzero] = -1
        for j, (u, v) in enumerate(UNITS):
            out[nonzero & (x == u % p) & (y == v % p)] = j
    if np.any(out == -2):
        raise RuntimeError("Euler exponent did not land among sixth roots")
    return out


def squarefree_columns(ideals, limit):
    columns = [(1, 1, ())]
    def visit(start, norm, mu, factors):
        for j in range(start, len(ideals)):
            new_norm = norm*ideals[j]["norm"]
            if new_norm > limit:
                break
            new_factors = factors+(j,)
            columns.append((new_norm, -mu, new_factors))
            visit(j+1, new_norm, -mu, new_factors)
    visit(0, 1, 1, ())
    return sorted(columns)


def norm_ball(h):
    bound = math.isqrt((4*h+2)//3)+2
    a, b = np.meshgrid(np.arange(-bound, bound+1, dtype=np.int64),
                       np.arange(-bound, bound+1, dtype=np.int64))
    norm = a*a-a*b+b*b
    keep = (norm > 0) & (norm <= h)
    return a[keep], b[keep], norm[keep]


def exact_field_checks(ideals):
    predicates = 0
    for q in ideals:
        if q["norm"] > 100:
            continue
        p = q["p"]
        if q["root"] is not None:
            a, b = np.arange(p, dtype=np.int64), np.zeros(p, dtype=np.int64)
        else:
            a, b = np.meshgrid(np.arange(p, dtype=np.int64), np.arange(p, dtype=np.int64))
            a, b = a.ravel(), b.ravel()
        s = symbols(q, a, b)
        counts = np.bincount(s+1, minlength=7).tolist()
        expected = [1] + [(q["norm"]-1)//6]*6
        if counts != expected:
            raise RuntimeError("Full-residue sextic orthogonality failed")
        predicates += 7
        # Exhaust all u and all v in these small residue fields.
        for c, d, sv in zip(a.tolist(), b.tolist(), s.tolist()):
            product = symbols(q, a*c-b*d, a*d+b*c-b*d)
            expected_product = (s+sv) % 6
            expected_product[(s == -1) | (sv == -1)] = -1
            if not np.array_equal(product, expected_product):
                raise RuntimeError("Finite-field multiplicativity failed")
            predicates += len(s)
    return predicates


def exact_norm_coefficient_checks(limit):
    """Independent norm-series check from zeta_K(s)=zeta(s)L(s,chi_-3).

    Compare the ideal DFS against the rational Dirichlet convolution of
    mu_Z with mu_Z*chi_-3, then remove all coefficients divisible by 2 or 3.
    This checks split and inert prime enumeration, ideal multiplicities,
    squarefreeness and Mobius signs by a separate integer-coefficient route.
    """
    mu = [1]*(limit+1)
    mu[0] = 0
    for p in primes_to(limit):
        for n in range(p, limit+1, p):
            mu[n] *= -1
        for n in range(p*p, limit+1, p*p):
            mu[n] = 0
    expected = [0]*(limit+1)
    for d in range(1, limit+1):
        if mu[d] == 0:
            continue
        for m in range(1, limit//d+1):
            chi = 0 if m % 3 == 0 else (1 if m % 3 == 1 else -1)
            expected[d*m] += mu[d]*mu[m]*chi
    actual = [0]*(limit+1)
    for norm, sign, _ in squarefree_columns(prime_ideals(limit), limit):
        actual[norm] += sign
    for n in range(1, limit+1):
        target = expected[n] if math.gcd(n, 6) == 1 else 0
        if actual[n] != target:
            raise RuntimeError(f"Independent norm coefficient failed at {n}")
    return limit


def sixth_power_ideal_rows(a, b, h):
    cutoff = int(h**(1/6))+2
    while cutoff**6 > h:
        cutoff -= 1
    x, y, _ = norm_ball(cutoff)
    rows = set()
    exact_rows = set()
    for u, v in zip(x.tolist(), y.tolist()):
        z = power((u, v), 6)
        exact_rows.add(z)
        for unit in UNITS:
            rows.add(multiply(unit, z))
    return (np.array([(int(x), int(y)) in rows for x, y in zip(a, b)]),
            np.array([(int(x), int(y)) in exact_rows for x, y in zip(a, b)]))


def ceil_rational_power(base, exponent):
    """Exact ceiling of base**exponent for a positive rational exponent."""
    target = base**exponent.numerator
    degree = exponent.denominator
    lower = 0
    upper = 1 << ((target.bit_length()+degree-1)//degree)
    while lower+1 < upper:
        middle = (lower+upper)//2
        if middle**degree >= target:
            upper = middle
        else:
            lower = middle
    return upper


def probe(d, theta, kmax):
    h = ceil_rational_power(d, 1+theta)
    ideals = prime_ideals(d)
    columns = squarefree_columns(ideals, d)
    a, b, row_norm = norm_ball(h)
    primitive = [symbols(q, a, b) for q in ideals]
    total = np.zeros(len(a), dtype=np.complex128)
    coefficient_energy = 0.0
    used = 0
    for norm, mu, factors in columns:
        z = 4*norm/d-3
        if not -1 < z < 1:
            continue
        weight = math.exp(1 - 1/(1-z*z))
        exponent = np.zeros(len(a), dtype=np.int16)
        nonunit = np.zeros(len(a), dtype=bool)
        for j in factors:
            nonunit |= primitive[j] == -1
            exponent += primitive[j]
        value = ROOTS[exponent % 6].copy()
        value[nonunit] = 0
        total += mu*weight*value
        coefficient_energy += weight*weight
        used += 1
    energy = np.abs(total)**2
    sixth_ideal, sixth_exact = sixth_power_ideal_rows(a, b, h)
    maximum = int(np.argmax(energy))
    mean_energy = float(np.mean(energy))
    moments = []
    for k in range(1, kmax+1):
        values = energy**k
        mass = float(np.sum(values))
        moments.append({
            "k": k, "moment": 2*k,
            "sum": mass, "ratio_to_H_D_power_k": mass/(h*d**k),
            "ratio_to_row_count_empirical_second_power_k":
                mass/(len(a)*mean_energy**k),
            "sixth_power_ideal_row_fraction": float(np.sum(values[sixth_ideal])/mass),
            "exact_sixth_power_row_fraction": float(np.sum(values[sixth_exact])/mass)
        })
    return {
        "D": d, "H": h, "theta": float(theta),
        "theta_exact": str(theta), "rows": len(a),
        "prime_ideals": len(ideals), "nonzero_weight_columns": used,
        "squarefree_column_manifest_sha256":
            hashlib.sha256(json.dumps(columns,separators=(",",":")).encode()).hexdigest(),
        "coefficient_energy": coefficient_energy,
        "sixth_power_ideal_rows": int(np.sum(sixth_ideal)),
        "exact_sixth_power_rows": int(np.sum(sixth_exact)),
        "maximum": {"a": int(a[maximum]), "b": int(b[maximum]),
                    "norm": int(row_norm[maximum]),
                    "absolute_sum": float(abs(total[maximum]))},
        "moments": moments
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scales", default="64,128,256,512,1024,2048,4096,8192")
    parser.add_argument("--theta", type=Fraction, default=Fraction(1, 10))
    parser.add_argument("--kmax", type=int, default=6)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    scales = [int(x) for x in args.scales.split(",")]
    if (not scales or min(scales) < 2 or max(scales) > 8192
            or not 2 <= args.kmax <= 6 or not 0 < args.theta <= Fraction(1, 10)
            or args.theta.denominator > 1000):
        parser.error("Scoped diagnostic: 2 <= scales <= 8192, 2 <= kmax <= 6, "
                     "0 < theta <= 1/10, and theta denominator <= 1000")
    gates = exact_field_checks(prime_ideals(100))
    norm_gates = exact_norm_coefficient_checks(max(scales))
    result = {
        "status": "FINITE_NUMERICAL_DIAGNOSTIC_ONLY",
        "field": "Q(sqrt(-3)); omega^2+omega+1=0",
        "fixed_twist": "nu=1", "excluded_column_primes": [2, 3],
        "weight": "W(x)=exp(1-1/(1-(4x-3)^2)) for 1/2<x<1; zero elsewhere",
        "symbol_arithmetic": "exact finite fields; exponents modulo 6 with nonunit zero",
        "row_cutoff_arithmetic": "H=ceil(D^(1+theta)) by exact rational integer comparison",
        "sum_arithmetic": "ordinary binary64; not directed or certified",
        "exact_small_field_predicates": gates,
        "exact_independent_norm_coefficient_predicates": norm_gates,
        "scope": "All element rows in each finite norm ball; all squarefree ideal columns in the bump support",
        "not_established": ["uniform asymptotic moment bound", "17/24 zero-free boundary", "RH"],
        "panels": []
    }
    for d in scales:
        panel = probe(d, args.theta, args.kmax)
        result["panels"].append(panel)
        args.output.write_text(json.dumps(result, indent=2)+"\n")
        print(json.dumps({"D": d, "rows": panel["rows"],
                          "fourth_ratio": panel["moments"][1]["ratio_to_H_D_power_k"],
                          "max": panel["maximum"]}), flush=True)


if __name__ == "__main__":
    main()
