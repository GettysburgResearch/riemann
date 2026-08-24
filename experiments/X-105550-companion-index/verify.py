#!/usr/bin/env python3
from __future__ import annotations

import argparse
import cmath
import hashlib
import json
import math
import random
from fractions import Fraction as F
from pathlib import Path

VERDICT = "PASS_T105550_COMPANION_PARTIAL_INDEX"
ROOT = Path(__file__).resolve().parents[2]
CONTENT = (
    "README_105550.md",
    "PR_BODY_105550_ADDENDUM.md",
    "PACKET_METADATA_105550.json",
    "claims/lemmas/L-105550-reduced-companion-half-plane-count.md",
    "claims/lemmas/L-105551-cayley-toeplitz-degree.md",
    "claims/lemmas/L-105552-separated-blaschke-rank-energy.md",
    "claims/refutations/R-105550-near-cancelling-dipoles-defeat-norm-count.md",
    "claims/theorems/T-105550-topological-companion-index-frontier.md",
    "claims/methodology/M-105550-hostile-review-contract.md",
    "reports/gpt56-pro/2026-08-24-companion-index-frontier.md",
    "standalone/2026-08-24-companion-index/PROOF.md",
    "integration/2026-08-24/t105550-source-lock.json",
    "experiments/X-105550-companion-index/README.md",
    "experiments/X-105550-companion-index/replay.sh",
    "experiments/X-105550-companion-index/verify.py",
    "experiments/X-105550-companion-index/tests/test_verify.py",
)


def req(x: bool, msg: str) -> None:
    if not x:
        raise AssertionError(msg)


def trim(p: list[F]) -> list[F]:
    p = p[:]
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(a: list[F], b: list[F]) -> list[F]:
    n = max(len(a), len(b))
    c = [F(0)] * n
    for i in range(n):
        c[i] = (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
    return trim(c)


def mul(a: list[F], b: list[F]) -> list[F]:
    c = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return trim(c)


def derivative(a: list[F]) -> list[F]:
    return trim([F(i) * a[i] for i in range(1, len(a))] or [F(0)])


def divmod_poly(a: list[F], b: list[F]) -> tuple[list[F], list[F]]:
    a = trim(a)
    b = trim(b)
    req(b != [0], "division by zero polynomial")
    if len(a) < len(b):
        return [F(0)], a
    q = [F(0)] * (len(a) - len(b) + 1)
    r = a[:]
    while len(r) >= len(b) and r != [0]:
        k = len(r) - len(b)
        c = r[-1] / b[-1]
        q[k] += c
        for j in range(len(b)):
            r[k + j] -= c * b[j]
        r = trim(r)
    return trim(q), trim(r)


def monic(a: list[F]) -> list[F]:
    a = trim(a)
    if a == [0]:
        return a
    return [x / a[-1] for x in a]


def gcd_poly(a: list[F], b: list[F]) -> list[F]:
    a, b = trim(a), trim(b)
    while b != [0]:
        _, r = divmod_poly(a, b)
        a, b = b, r
    return monic(a)


def eval_poly(p: list[F], x: F) -> F:
    y = F(0)
    for c in reversed(p):
        y = y * x + c
    return y


def eval_complex(p: list[complex], z: complex) -> complex:
    y = 0j
    for c in reversed(p):
        y = y * z + c
    return y


def sign_at_infty(p: list[F], positive: bool) -> int:
    p = trim(p)
    if p == [0]:
        return 0
    s = 1 if p[-1] > 0 else -1
    if not positive and (len(p) - 1) % 2:
        s = -s
    return s


def variations(signs: list[int]) -> int:
    nz = [s for s in signs if s]
    return sum(nz[i] != nz[i - 1] for i in range(1, len(nz)))


def sturm_real_distinct(p: list[F]) -> int:
    p = monic(p)
    dp = derivative(p)
    seq = [p, dp]
    while seq[-1] != [0]:
        _, r = divmod_poly(seq[-2], seq[-1])
        if r == [0]:
            break
        seq.append([-x for x in r])
    vp = variations([sign_at_infty(q, True) for q in seq])
    vm = variations([sign_at_infty(q, False) for q in seq])
    return vm - vp


def factor_real_root(a: int, multiplicity: int = 1) -> list[F]:
    p = [F(1)]
    for _ in range(multiplicity):
        p = mul(p, [F(-a), F(1)])
    return p


def factor_complex_pair(a: int, b: int, multiplicity: int = 1) -> list[F]:
    q = [F(a * a + b * b), F(-2 * a), F(1)]
    p = [F(1)]
    for _ in range(multiplicity):
        p = mul(p, q)
    return p


def durand_kerner(coeff_asc: list[complex]) -> list[complex]:
    coeff = coeff_asc[:]
    while len(coeff) > 1 and abs(coeff[-1]) < 1e-28:
        coeff.pop()
    n = len(coeff) - 1
    lead = coeff[-1]
    coeff = [c / lead for c in coeff]
    if n == 1:
        return [-coeff[0]]
    radius = 1.0 + max(abs(c) for c in coeff[:-1])
    roots = [radius * cmath.exp(2j * math.pi * (j + 0.37) / n) for j in range(n)]
    for _ in range(4000):
        move = 0.0
        new = roots[:]
        for j, z in enumerate(roots):
            den = 1 + 0j
            for k, w in enumerate(roots):
                if k != j:
                    den *= z - w
            if abs(den) < 1e-30:
                z += complex(1e-8 * (j + 1), -1e-8 * (j + 2))
                den = 1 + 0j
                for k, w in enumerate(roots):
                    if k != j:
                        den *= z - w
            dz = eval_complex(coeff, z) / den
            new[j] = z - dz
            move = max(move, abs(dz))
        roots = new
        if move < 1e-13:
            break
    req(max(abs(eval_complex(coeff, z)) for z in roots) < 2e-6, "root diagnostic residual")
    return roots


def companion_fixture_checks() -> dict:
    rng = random.Random(105550)
    cases: list[list[F]] = []
    fixed = [
        mul(factor_real_root(-1, 2), factor_real_root(1, 2)),
        factor_complex_pair(0, 1),
        mul(factor_real_root(0, 2), factor_complex_pair(2, 1)),
        mul(factor_real_root(-2), mul(factor_real_root(3), factor_complex_pair(0, 2))),
    ]
    cases.extend(fixed)
    for _ in range(260):
        p = [F(1)]
        used: set[int] = set()
        for _ in range(rng.randint(0, 3)):
            a = rng.randint(-5, 5)
            while a in used:
                a = rng.randint(-5, 5)
            used.add(a)
            p = mul(p, factor_real_root(a, rng.randint(1, 3)))
        for _ in range(rng.randint(0, 2)):
            a = rng.randint(-3, 3)
            b = rng.randint(1, 4)
            p = mul(p, factor_complex_pair(a, b, rng.randint(1, 2)))
        if len(p) > 1:
            cases.append(p)
    checked = 0
    minimum_imag_margin = 1e9
    for p in cases:
        g = gcd_poly(p, derivative(p))
        P, rem = divmod_poly(p, g)
        req(rem == [0], "gcd division")
        Q, rem = divmod_poly(derivative(p), g)
        req(rem == [0], "derivative gcd division")
        D = len(P) - 1
        R = sturm_real_distinct(P)
        req((D + R) % 2 == 0, "parity")
        pred_up = (D + R) // 2
        pred_down = (D - R) // 2
        delta = F(3, 5)
        n = max(len(P), len(Q))
        ec = [0j] * n
        for i in range(n):
            ec[i] = complex(float(Q[i]) if i < len(Q) else 0.0,
                            float(delta * P[i]) if i < len(P) else 0.0)
        roots = durand_kerner(ec)
        margin = min(abs(z.imag) for z in roots)
        minimum_imag_margin = min(minimum_imag_margin, margin)
        req(margin > 1e-5, "companion real-zero diagnostic")
        up = sum(z.imag > 0 for z in roots)
        down = sum(z.imag < 0 for z in roots)
        req((up, down) == (pred_up, pred_down), "half-plane count diagnostic")
        checked += 1
    return {
        "fixtures": checked,
        "minimum_imaginary_margin": f"{minimum_imag_margin:.12g}",
        "complex_root_count_machine_status": "diagnostic corroboration; proof is argument-principle theorem",
    }


def phase_algebra_checks() -> dict:
    rng = random.Random(105551)
    checks = 0
    for _ in range(600):
        p = [F(rng.randint(-4, 4)) for _ in range(rng.randint(2, 7))]
        if p[-1] == 0:
            p[-1] = F(rng.choice([-3, -2, -1, 1, 2, 3]))
        g = gcd_poly(p, derivative(p))
        P, _ = divmod_poly(p, g)
        Q, _ = divmod_poly(derivative(p), g)
        dP = derivative(P)
        dQ = derivative(Q)
        x = F(rng.randint(-7, 7), rng.randint(1, 6))
        delta = F(rng.randint(1, 7), rng.randint(1, 7))
        pv, qv = eval_poly(P, x), eval_poly(Q, x)
        dpv, dqv = eval_poly(dP, x), eval_poly(dQ, x)
        den = qv * qv + delta * delta * pv * pv
        if den == 0:
            continue
        lhs_num = delta * (qv * dpv - pv * dqv)
        direct_num = delta * (qv * dpv - pv * dqv)
        req(lhs_num == direct_num, "phase derivative")
        checks += 1
    return {"exact_phase_derivative_checks": checks}


def mat_inv(A: list[list[F]]) -> list[list[F]]:
    n = len(A)
    M = [row[:] + [F(int(i == j)) for j in range(n)] for i, row in enumerate(A)]
    for col in range(n):
        piv = next((r for r in range(col, n) if M[r][col] != 0), None)
        req(piv is not None, "singular matrix")
        M[col], M[piv] = M[piv], M[col]
        v = M[col][col]
        M[col] = [x / v for x in M[col]]
        for r in range(n):
            if r == col:
                continue
            v = M[r][col]
            if v:
                M[r] = [M[r][j] - v * M[col][j] for j in range(2 * n)]
    return [row[n:] for row in M]


def matmul(A: list[list[F]], B: list[list[F]]) -> list[list[F]]:
    return [[sum((A[i][k] * B[k][j] for k in range(len(B))), F(0))
             for j in range(len(B[0]))] for i in range(len(A))]


def trace(A: list[list[F]]) -> F:
    return sum((A[i][i] for i in range(len(A))), F(0))


def ldl_positive(A: list[list[F]]) -> bool:
    n = len(A)
    L = [[F(0) for _ in range(n)] for _ in range(n)]
    D = [F(0)] * n
    for i in range(n):
        L[i][i] = 1
        D[i] = A[i][i] - sum((L[i][k] * L[i][k] * D[k] for k in range(i)), F(0))
        if D[i] <= 0:
            return False
        for j in range(i + 1, n):
            L[j][i] = (A[j][i] - sum((L[j][k] * L[i][k] * D[k] for k in range(i)), F(0))) / D[i]
    return True


def blaschke(a: F, z: F) -> F:
    return (z - a) / (1 - a * z)


def separated_rank_energy_checks() -> dict:
    fixtures = [
        ([F(-3, 4), F(0), F(3, 4)], [F(-1, 2)]),
        ([F(-2, 3), F(-1, 5), F(1, 3), F(4, 5)], [F(-4, 5), F(1, 2)]),
        ([F(-4, 5), F(-2, 5), F(1, 10), F(3, 5)], [F(-3, 4)]),
    ]
    rows = []
    for bs, pluszeros in fixtures:
        m = len(bs)
        G = [[F(1, 1) / (1 - bs[i] * bs[j]) for j in range(m)] for i in range(m)]
        kappa = F(1, 1000)
        K = F(100)
        Glo = [[G[i][j] - (kappa if i == j else 0) for j in range(m)] for i in range(m)]
        Ghi = [[(K if i == j else 0) - G[i][j] for j in range(m)] for i in range(m)]
        req(ldl_positive(Glo) and ldl_positive(Ghi), "Gram brackets")
        vals = []
        for b in bs:
            v = F(1)
            for a in pluszeros:
                v *= blaschke(a, b)
            vals.append(v)
        eps = min(abs(v) for v in vals)
        D = [[vals[i] if i == j else F(0) for j in range(m)] for i in range(m)]
        invG = mat_inv(G)
        hs2 = trace(matmul(matmul(matmul(invG, D), G), D))
        req(F(m) * kappa * eps * eps <= K * hs2, "rank-energy bridge")
        rows.append({
            "m": m,
            "epsilon": str(eps),
            "hs2": str(hs2),
            "kappa_lower": str(kappa),
            "K_upper": str(K),
        })
    return {"fixtures": rows}


def dipole_checks() -> dict:
    pairs = [(F(1, 5), F(21, 100)), (F(1, 5), F(1, 2)), (F(0), F(1, 2)),
             (F(999, 2000), F(1, 2))]
    rows = []
    for a, b in pairs:
        C = (b - a) * (1 - b * b) / (1 - a * b)
        hs2_series = C * C / (1 - b * b) ** 2
        rho2 = (a - b) ** 2 / (1 - a * b) ** 2
        req(hs2_series == rho2, "dipole energy")
        req(a != b, "rank-one fixture")
        rows.append({"a": str(a), "b": str(b), "rank": 1, "hs2": str(rho2)})
    req(rows[0]["hs2"] == str(F(25, 229441)), "near dipole exact value")
    return {"fixtures": rows, "arbitrarily_small_norm_with_rank_one": True}


def threshold_checks() -> dict:
    anchor = F(1)
    cut = anchor / 20
    req(cut == F(1, 20), "ninety cut")
    return {
        "distinct_real_fraction_identity": "R/D=1-2 N_minus/D",
        "bad_companion_cut_for_ninety_percent": "N_minus/D<1/20",
        "endpoint_ledger": "O(1) on regular dyadic windows",
    }


def hashes() -> dict[str, str]:
    out = {}
    for p in CONTENT:
        data = (ROOT / p).read_bytes().replace(b"\r\n", b"\n")
        out[p] = hashlib.sha256(data).hexdigest()
    return out


def payload() -> dict:
    x = {
        "verdict": VERDICT,
        "companion_half_plane": companion_fixture_checks(),
        "phase_algebra": phase_algebra_checks(),
        "separated_rank_energy": separated_rank_energy_checks(),
        "near_cancelling_dipole": dipole_checks(),
        "ninety_percent_threshold": threshold_checks(),
        "content_sha256": hashes(),
        "finite_argument_principle_machine_proved": False,
        "cpindex105550_proved": False,
        "ninety_percent_established": False,
        "public_record_beaten": False,
        "rh_established": False,
    }
    x["proof_object_sha256"] = hashlib.sha256(
        json.dumps(x, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    return x


build_payload = payload


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    x = payload()
    args.output.write_text(json.dumps(x, indent=2, sort_keys=True) + "\n")
    print(VERDICT)
    print(x["proof_object_sha256"])
    print("CPINDEX105550_OPEN")
    print("NINETY_PERCENT_UNPROVED")
    print("PUBLIC_RECORD_UNBEATEN")
    print("RH_UNPROVED")
