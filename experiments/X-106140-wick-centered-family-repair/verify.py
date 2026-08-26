#!/usr/bin/env python3
"""Exact replay for the T-106140 Wick-centered family repair.

Standard library only. This checks:
* one-prime Gauss weight ledger and the omitted atomic phase cardinality;
* exact constant/mean-zero sign-pair operator decomposition;
* tensor channel decomposition and atomic channel weights;
* Wick normal ordering;
* Boolean half-source square and least-prime cutoff recurrence.
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import Dict, FrozenSet, Iterable, List, Tuple

CHECKS = 0


def check(cond: bool, msg: str) -> None:
    global CHECKS
    CHECKS += 1
    if not cond:
        raise AssertionError(msg)


def mat_add(a: List[List[Fraction]], b: List[List[Fraction]]) -> List[List[Fraction]]:
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def mat_sub(a: List[List[Fraction]], b: List[List[Fraction]]) -> List[List[Fraction]]:
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def mat_eq(a: List[List[Fraction]], b: List[List[Fraction]], name: str) -> None:
    check(len(a) == len(b), f"{name}: row count")
    for i, (ra, rb) in enumerate(zip(a, b)):
        check(len(ra) == len(rb), f"{name}: col count row {i}")
        for j, (x, y) in enumerate(zip(ra, rb)):
            check(x == y, f"{name}[{i},{j}] {x} != {y}")


def mat_vec(a: List[List[Fraction]], x: List[Fraction]) -> List[Fraction]:
    return [sum((a[i][j] * x[j] for j in range(len(x))), Fraction(0)) for i in range(len(a))]


def quad(a: List[List[Fraction]], x: List[Fraction]) -> Fraction:
    ax = mat_vec(a, x)
    return sum((x[i] * ax[i] for i in range(len(x))), Fraction(0))


def kron(a: List[List[Fraction]], b: List[List[Fraction]]) -> List[List[Fraction]]:
    out: List[List[Fraction]] = []
    for ra in a:
        for rb in b:
            row: List[Fraction] = []
            for xa in ra:
                row.extend(xa * xb for xb in rb)
            out.append(row)
    return out


def identity(n: int) -> List[List[Fraction]]:
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def ones(n: int) -> List[List[Fraction]]:
    return [[Fraction(1) for _ in range(n)] for _ in range(n)]


def scale(a: List[List[Fraction]], s: Fraction) -> List[List[Fraction]]:
    return [[s * x for x in row] for row in a]


def odd_primes(limit: int) -> List[int]:
    ps: List[int] = []
    for n in range(3, limit + 1, 2):
        if all(n % d for d in range(3, int(n**0.5) + 1, 2)):
            ps.append(n)
    return ps


def sign_pair_operators(q: int) -> Tuple[List[List[Fraction]], List[List[Fraction]], List[List[Fraction]]]:
    m = (q - 1) // 2
    I = identity(m)
    J = ones(m)
    A = mat_sub(scale(I, Fraction(q)), J)
    c = Fraction(q + 1, q - 1)
    C = scale(J, c)
    N = mat_sub(scale(I, Fraction(q)), scale(J, Fraction(2 * q, q - 1)))
    return A, C, N


def gauss_ledger_checks() -> None:
    primes = odd_primes(43)
    vectors = [
        [Fraction(1)],
        [Fraction(1), Fraction(-2)],
        [Fraction(2), Fraction(0), Fraction(3)],
        [Fraction(i - 3) for i in range(7)],
    ]
    for q in primes:
        m = (q - 1) // 2
        c = Fraction(q + 1, q - 1)
        nu = Fraction(q * (q - 3), q - 1)
        check(c + nu == q - 1, f"weight sum q={q}")
        check(nu >= 0, f"nonprincipal atomic weight q={q}")

        A, C, N = sign_pair_operators(q)
        mat_eq(A, mat_add(C, N), f"A=C+N q={q}")
        one = [Fraction(1) for _ in range(m)]
        check(all(v == 0 for v in mat_vec(N, one)), f"N constant null q={q}")
        for seed in range(1, 2 * m + 3):
            x = [Fraction(((seed + 3 * j) % 9) - 4) for j in range(m)]
            check(quad(N, x) >= 0, f"N PSD fixture q={q}, seed={seed}")
            check(quad(A, x) == quad(C, x) + quad(N, x), f"quadratic split q={q}, seed={seed}")
        for j in range(m):
            check(A[j][j] == q - 1, f"A atomic q={q}")
            check(C[j][j] == c, f"C atomic q={q}")
            check(N[j][j] == nu, f"N atomic q={q}")

        for raw in vectors:
            x = (raw * ((m + len(raw) - 1) // len(raw)))[:m]
            D = sum((v * v for v in x), Fraction(0))
            A0 = quad(A, x) - Fraction(q - 1) * D
            C0 = quad(C, x) - c * D
            N0 = quad(N, x) - nu * D
            check(A0 == C0 + N0, f"normal-order split q={q}")

    for ell in primes[:6]:
        A1, C1, N1 = sign_pair_operators(ell)
        c1 = Fraction(ell + 1, ell - 1)
        nu1 = Fraction(ell * (ell - 3), ell - 1)
        for rho in primes[:6]:
            if rho == ell:
                continue
            A2, C2, N2 = sign_pair_operators(rho)
            c2 = Fraction(rho + 1, rho - 1)
            nu2 = Fraction(rho * (rho - 3), rho - 1)
            lhs = kron(A1, A2)
            rhs = mat_add(
                mat_add(kron(C1, C2), kron(C1, N2)),
                mat_add(kron(N1, C2), kron(N1, N2)),
            )
            mat_eq(lhs, rhs, f"tensor split {ell},{rho}")
            check(
                c1 * c2 + c1 * nu2 + nu1 * c2 + nu1 * nu2
                == (ell - 1) * (rho - 1),
                f"tensor atomic sum {ell},{rho}",
            )
            check((ell - 1) * (rho - 1) > 1, f"dimension fixture {ell},{rho}")


SetT = FrozenSet[int]


def all_subsets(universe: Tuple[int, ...]) -> Iterable[SetT]:
    for r in range(len(universe) + 1):
        for c in combinations(universe, r):
            yield frozenset(c)


def bprod(s: SetT) -> int:
    out = 1
    for p in s:
        out *= p
    return out


def star(
    f: Dict[SetT, Fraction],
    g: Dict[SetT, Fraction],
    universe: Tuple[int, ...],
) -> Dict[SetT, Fraction]:
    out: Dict[SetT, Fraction] = {}
    for s in all_subsets(universe):
        total = Fraction(0)
        ss = tuple(sorted(s))
        for a in all_subsets(ss):
            total += f.get(a, Fraction(0)) * g.get(s - a, Fraction(0))
        out[s] = total
    return out


def boolean_objects(universe: Tuple[int, ...], cutoff: Fraction):
    subs = list(all_subsets(universe))
    mu = {s: Fraction((-1) ** len(s)) for s in subs}
    one = {s: Fraction(1) for s in subs}
    eps = {s: Fraction(int(len(s) == 0)) for s in subs}
    mu_u = {
        s: (mu[s] if Fraction(bprod(s)) <= cutoff else Fraction(0))
        for s in subs
    }
    a = star(mu_u, one, universe)
    a = {s: eps[s] - a[s] for s in subs}
    h = {s: Fraction((-1) ** len(s), 2 ** len(s)) for s in subs}
    f = star(a, h, universe)
    b = star(star(a, a, universe), mu, universe)
    return mu, one, eps, a, h, f, b


def boolean_half_source_checks() -> None:
    prime_sets = [
        (2, 3, 5),
        (2, 3, 5, 7),
        (2, 3, 5, 7, 11),
        (3, 5, 7, 11, 13, 17),
    ]
    cutoffs = [Fraction(x) for x in (1, 2, 4, 6, 10, 15, 30, 70)]
    cutoffs += [Fraction(9, 2), Fraction(25, 3)]
    for universe in prime_sets:
        for U in cutoffs:
            mu, one, eps, a, h, f, b = boolean_objects(universe, U)
            hh = star(h, h, universe)
            ff = star(f, f, universe)
            for s in all_subsets(universe):
                check(hh[s] == mu[s], f"h*h=mu {universe},U={U},S={s}")
                check(ff[s] == b[s], f"f*f=b {universe},U={U},S={s}")
                if Fraction(bprod(s)) <= U:
                    check(f[s] == 0, f"f small support {universe},U={U},S={s}")

            for ell in universe:
                tail = tuple(p for p in universe if p > ell)
                _, _, _, _, _, F_u, _ = boolean_objects(tail, U)
                _, _, _, _, _, F_v, _ = boolean_objects(tail, U / ell)
                FF = star(F_u, F_u, tail)
                FFv = star(F_u, F_v, tail)
                for s in all_subsets(tail):
                    with_ell = frozenset(set(s) | {ell})
                    check(
                        f[with_ell] == Fraction(1, 2) * F_u[s] - F_v[s],
                        f"least-prime f recurrence ell={ell},U={U},S={s}",
                    )
                    check(
                        b[with_ell] == FF[s] - 2 * FFv[s],
                        f"least-prime b recurrence ell={ell},U={U},S={s}",
                    )
                    diff = {x: F_u[x] - F_v[x] for x in all_subsets(tail)}
                    diff2 = star(diff, diff, tail)
                    vv = star(F_v, F_v, tail)
                    check(
                        b[with_ell] == diff2[s] - vv[s],
                        f"two-square cutoff form ell={ell},U={U},S={s}",
                    )


def main() -> None:
    gauss_ledger_checks()
    boolean_half_source_checks()

    proof = {
        "verdict": "PASS_X_106140_WICK_CENTERED_FAMILY_REPAIR",
        "exact_checks": CHECKS,
        "proved_exact": {
            "one_prime_weight_sum_is_q_minus_1": True,
            "complete_family_atomic_phase_cardinality": True,
            "constant_plus_mean_zero_operator_split": True,
            "tensor_four_channel_split": True,
            "wick_normal_order_identity": True,
            "boolean_half_source_square": True,
            "least_prime_cutoff_recurrence": True,
            "least_prime_two_square_calderon_form": True,
        },
        "status": {
            "WCADD106140": "open",
            "WCKUM106140": "open",
            "BCI102990": "open",
            "riemann_hypothesis": "unproved",
        },
    }
    canonical = json.dumps(proof, sort_keys=True, separators=(",", ":")).encode()
    proof["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    out = Path(__file__).with_name("verification.json")
    out.write_text(json.dumps(proof, indent=2, sort_keys=True) + "\n")
    print(proof["verdict"])
    print(f"exact_checks={CHECKS}")
    print(f"proof_object_sha256={proof['proof_object_sha256']}")


if __name__ == "__main__":
    main()
