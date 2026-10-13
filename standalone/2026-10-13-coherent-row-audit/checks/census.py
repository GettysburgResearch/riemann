#!/usr/bin/env python3
"""Complete finite row/column census; no asymptotic inference.

Arithmetic is Z[zeta_6]. NumPy handles signed integers only, with an explicit
pre-computation overflow bound. The source helper is pinned in SOURCES.md.
"""
from __future__ import annotations
import argparse
from collections import Counter
from functools import lru_cache
import itertools
import json
import math
from pathlib import Path
import numpy as np
import eisenstein_source as E


def require(value: bool, message: str) -> None:
    if not value:
        raise RuntimeError(message)


def integer_root(n: int, degree: int) -> int:
    if n < 0 or degree < 1:
        raise ValueError("nonnegative integer and positive degree required")
    lo, hi = 0, n + 1
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid ** degree <= n:
            lo = mid
        else:
            hi = mid
    return lo


def ceil_height(d: int) -> int:
    h = integer_root(d ** 21, 20)
    return h if h ** 20 == d ** 21 else h + 1


def epower(z: tuple[int, int], n: int) -> tuple[int, int]:
    out = (1, 0)
    for _ in range(n):
        out = E.emul(out, z)
    return out


@lru_cache(maxsize=None)
def make_primes(cap: int) -> tuple[tuple[int, int], ...]:
    # Every integral ideal is principal. Six unit associates are identified,
    # but conjugate split prime ideals remain distinct.
    generators = sorted({E.canonical(z) for z in E.elements(cap)},
                        key=lambda z: (E.en(z), z))
    primes = []
    for z in generators:
        q = E.en(z)
        if q % 2 == 0 or q % 3 == 0:
            continue
        p = math.isqrt(q)
        if E.prime(q) or (p * p == q and E.prime(p) and p % 3 == 2):
            primes.append(z)
    return tuple(primes)


def make_columns(primes: tuple[tuple[int, int], ...], cap: int):
    """All good squarefree ideals in cap/2 < norm <= cap, exactly once."""
    norms = [E.en(p) for p in primes]
    out = []

    def walk(start, n, factors):
        if 2 * n > cap:
            out.append((n, factors))
        for j in range(start, len(norms)):
            nn = n * norms[j]
            if nn > cap:
                break
            walk(j + 1, nn, factors + (j,))

    walk(0, 1, ())
    return sorted(out)


def char_vec(p, rows):
    """Literal (u/p)_6 exponents, with -1 used ONLY as the zero marker."""
    q = E.en(p)
    if E.prime(q):
        om = (-p[0] * pow(p[1] % q, -1, q)) % q
        inv = {pow((1 + om) % q, j, q): j for j in range(6)}
        tab = np.array([-1] + [inv[pow(x, (q - 1) // 6, q)]
                               for x in range(1, q)], dtype=np.int16)
        return tab[(rows[:, 0] + om * rows[:, 1]) % q]
    r = math.isqrt(q)
    tab = np.array([[(-1 if a == b == 0 else E.prime_character(p, (a, b)))
                     for b in range(r)] for a in range(r)], dtype=np.int16)
    return tab[rows[:, 0] % r, rows[:, 1] % r]


def pmul(a, b):
    return np.stack((a[0] * b[0] - a[1] * b[1],
                     a[0] * b[1] + a[1] * b[0] + a[1] * b[1]))


def principal_reference(primes, columns, H, row_norms):
    """Fourth moment only. Exact product equality and all union masks.

    For each pair product f, m(f) is the ordered factorization count.
    Sum m(f)^2 * sum_{d|rad(f)} mu(d) R_K(floor(H/Nd)).
    Rotation of an ideal lattice preserves the hard norm ball exactly.
    """
    multiplicities = Counter()
    for i, (_, f) in enumerate(columns):
        for j in range(i, len(columns)):
            g = columns[j][1]
            multiplicities[tuple(sorted(f + g))] += 1 if i == j else 2
    masks = Counter()
    norms = [E.en(p) for p in primes]
    unmasked = 0
    for f, count in multiplicities.items():
        weight = count * count
        unmasked += weight
        divs = [(1, 1)]
        for p in sorted(set(f)):
            q = norms[p]
            divs += [(n * q, -s) for n, s in divs if n * q <= H]
        for n, s in divs:
            masks[n] += s * weight
    lattice_count = np.cumsum(np.bincount(row_norms, minlength=H + 1))
    masked = sum(c * int(lattice_count[H // n]) for n, c in masks.items())
    return {"physical": masked, "per_mask_free_row": unmasked,
            "distinct_pair_products": len(multiplicities),
            "mask_norms_used": len(masks)}


def run_case(D: int, H: int, k: int = 2, with_reference: bool = True):
    if D < 2 or H < 1 or k < 1:
        raise ValueError("invalid census domain")
    primes = make_primes(D)
    columns = make_columns(primes, D)
    rows = np.array(E.elements(H), dtype=np.int64)
    row_norms = rows[:, 0] ** 2 - rows[:, 0] * rows[:, 1] + rows[:, 1] ** 2
    N = len(columns)
    require(N > 0, "empty column domain")
    require(16 * len(rows) * N ** (2 * k) < 2 ** 63,
            "int64 safety bound exceeded; use Python big integers instead")
    sixth = {epower(b, 6) for b in E.elements(integer_root(H, 6))}
    unit_sixth = {E.emul(e, z) for e in E.UNITS for z in sixth}
    groups = {"all": np.ones(len(rows), dtype=bool),
              "sixth_powers": np.array([tuple(r) in sixth for r in rows]),
              "unit_times_sixth_powers": np.array([tuple(r) in unit_sixth for r in rows])}
    groups["not_sixth_powers"] = ~groups["sixth_powers"]
    groups["not_unit_times_sixth_powers"] = ~groups["unit_times_sixth_powers"]
    J = max(len(f) for _, f in columns)
    require(6 * J < 2 ** 15, "int16 phase accumulator bound exceeded")
    C = np.zeros((J + 1, 2, len(rows)), dtype=np.int64)
    native = np.zeros((2, len(rows)), dtype=np.int64)
    cache = {}
    roots = np.array(list(E.ROOTS) + [(0, 0)], dtype=np.int64)
    for _, factors in columns:
        phase = np.zeros(len(rows), dtype=np.int16)
        valid = np.ones(len(rows), dtype=bool)
        for j in factors:
            if j not in cache:
                cache[j] = char_vec(primes[j], rows)
            values = cache[j]
            valid &= values >= 0
            phase += values
        values = roots[np.where(valid, phase % 6, 6)].T
        C[len(factors)] += values
        native += ((-1) ** len(factors)) * values
    B = np.zeros((1, 2, len(rows)), dtype=np.int64)
    B[0, 0] = 1
    for _ in range(k):
        nxt = np.zeros((B.shape[0] + J, 2, len(rows)), dtype=np.int64)
        for j, l in itertools.product(range(B.shape[0]), range(J + 1)):
            nxt[j + l] += pmul(B[j], C[l])
        B = nxt
    energy = native[0] ** 2 + native[0] * native[1] + native[1] ** 2
    result = {"D": D, "H": H, "k": k, "rows": len(rows), "columns": N,
              "prime_ideals": len(primes),
              "degree_counts": np.bincount([len(f) for _, f in columns]).tolist(),
              "sixth_power_rows": sorted(map(list, sixth)), "groups": {}}
    for name, sel in groups.items():
        gram = []
        for j in range(len(B)):
            line = []
            a, b = B[j, 0, sel], B[j, 1, sel]
            for l in range(len(B)):
                c, d = B[l, 0, sel], B[l, 1, sel]
                twice_real = int(np.sum(2 * a * c + a * d + b * c + 2 * b * d))
                imaginary_coefficient = int(np.sum(-a * d + b * c))
                require(imaginary_coefficient == 0 and twice_real % 2 == 0,
                        "conjugation-closed real Gram failure")
                line.append(twice_real // 2)
            gram.append(line)
        actual = int(np.sum(energy[sel] ** k))
        trace = sum(gram[j][j] for j in range(len(gram)))
        reconstructed = sum((-1) ** (j + l) * gram[j][l]
                            for j in range(len(gram)) for l in range(len(gram)))
        require(actual == reconstructed, "native/direct versus grade mismatch")
        result["groups"][name] = {"rows": int(sel.sum()), "native_moment": actual,
                                  "degree_energy": trace, "cross_degree": actual - trace,
                                  "gram": gram}
    if with_reference:
        require(k == 2, "product equality is only used in the fourth-order reference")
        ref = principal_reference(primes, columns, H, row_norms)
        # Current census range has no good-prime divisor in a sixth root.
        # This check is REQUIRED before assigning the unmasked principal value.
        require(all(int(C[:, 0, i].sum()) == N and int(C[:, 1, i].sum()) == 0
                    for i in np.flatnonzero(groups["sixth_powers"])),
                "a sixth-power row has a nontrivial mask; do not erase it")
        result["principal_reference"] = ref
        r = int(groups["sixth_powers"].sum())
        for name, val in (("all", ref["physical"]),
                          ("sixth_powers", r * ref["per_mask_free_row"]),
                          ("not_sixth_powers", ref["physical"] - r * ref["per_mask_free_row"])):
            result["groups"][name]["principal_reference"] = val
            result["groups"][name]["native_nonprincipal_remainder"] = (
                result["groups"][name]["native_moment"] - val)
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-D", type=int, default=8192)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    if args.max_D not in (64, 128, 256, 512, 1024, 2048, 4096, 8192):
        ap.error("choose one of the declared doubling endpoints, 64 through 8192")
    cases = []
    d = 64
    while d <= args.max_D:
        cases.append(run_case(d, ceil_height(d)))
        d *= 2
    if args.max_D == 8192:
        cases.append(run_case(8192, 8192))
    report = {"status": "PASS", "scope": "complete finite hard-window columns and hard-ball rows; no asymptotic inference",
              "arithmetic": "exact Z[zeta_6], int64 with proven pre-computation bounds", "cases": cases}
    text = json.dumps(report, separators=(',', ':'), sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
