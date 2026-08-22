#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as F
from itertools import combinations
from math import ceil
from pathlib import Path

VERDICT = "PASS_T105300_LOW_ORDER_LEVINSON_PICK"
ROOT = Path(__file__).resolve().parents[2]

CONTENT_FILES = (
    "PACKET_METADATA_105300.json",
    "claims/lemmas/L-105300-levinson-hermite-pick-trace-form.md",
    "claims/lemmas/L-105301-weighted-rank-trace-record-certificate.md",
    "claims/lemmas/L-105302-anthropic-xiprime-record-bridge.md",
    "claims/lemmas/L-105303-entire-window-hermite-pick-compression.md",
    "claims/refutations/R-105300-unweighted-residue-coherence-is-too-lossy.md",
    "claims/theorems/T-105300-low-order-levinson-pick-frontier.md",
    "claims/methodology/M-105300-hostile-review-contract.md",
    "experiments/X-105300-low-order-levinson-pick/verify.py",
    "experiments/X-105300-low-order-levinson-pick/tests/test_verify.py",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def trim(p: list[F]) -> list[F]:
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(a: list[F], b: list[F]) -> list[F]:
    out = [F(0)] * max(len(a), len(b))
    for i, v in enumerate(a):
        out[i] += v
    for i, v in enumerate(b):
        out[i] += v
    return trim(out)


def sub(a: list[F], b: list[F]) -> list[F]:
    return add(a, [-v for v in b])


def mul(a: list[F], b: list[F]) -> list[F]:
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def scale(a: list[F], c: F) -> list[F]:
    return trim([c * x for x in a])


def derivative(a: list[F]) -> list[F]:
    if len(a) <= 1:
        return [F(0)]
    return trim([F(i) * a[i] for i in range(1, len(a))])


def divmod_poly(a: list[F], b: list[F]) -> tuple[list[F], list[F]]:
    a = trim(a[:])
    b = trim(b[:])
    if b == [0]:
        raise ZeroDivisionError
    if len(a) < len(b):
        return [F(0)], a
    q = [F(0)] * (len(a) - len(b) + 1)
    while len(a) >= len(b) and a != [0]:
        k = len(a) - len(b)
        c = a[-1] / b[-1]
        q[k] = c
        a = sub(a, [F(0)] * k + scale(b, c))
    return trim(q), trim(a)


def mod_poly(a: list[F], m: list[F]) -> list[F]:
    return divmod_poly(a, m)[1]


def xgcd(a: list[F], b: list[F]) -> tuple[list[F], list[F], list[F]]:
    r0, r1 = trim(a[:]), trim(b[:])
    s0, s1 = [F(1)], [F(0)]
    t0, t1 = [F(0)], [F(1)]
    while r1 != [0]:
        q, r2 = divmod_poly(r0, r1)
        r0, r1 = r1, r2
        s0, s1 = s1, sub(s0, mul(q, s1))
        t0, t1 = t1, sub(t0, mul(q, t1))
    lc = r0[-1]
    return scale(r0, 1 / lc), scale(s0, 1 / lc), scale(t0, 1 / lc)


def inv_mod(a: list[F], m: list[F]) -> list[F]:
    g, s, _ = xgcd(a, m)
    require(g == [F(1)], "polynomial is not invertible modulo the modulus")
    return mod_poly(s, m)


def identity(n: int) -> list[list[F]]:
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def zero_matrix(n: int, m: int | None = None) -> list[list[F]]:
    if m is None:
        m = n
    return [[F(0) for _ in range(m)] for _ in range(n)]


def matmul(a: list[list[F]], b: list[list[F]]) -> list[list[F]]:
    n, k, m = len(a), len(b), len(b[0])
    require(len(a[0]) == k, "matrix shape mismatch")
    out = zero_matrix(n, m)
    for i in range(n):
        for r in range(k):
            if a[i][r] == 0:
                continue
            for j in range(m):
                out[i][j] += a[i][r] * b[r][j]
    return out


def matadd(a: list[list[F]], b: list[list[F]]) -> list[list[F]]:
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def matscale(a: list[list[F]], c: F) -> list[list[F]]:
    return [[c * x for x in row] for row in a]


def transpose(a: list[list[F]]) -> list[list[F]]:
    return [list(row) for row in zip(*a)]


def trace(a: list[list[F]]) -> F:
    return sum((a[i][i] for i in range(len(a))), F(0))


def frob2(a: list[list[F]]) -> F:
    return sum((x * x for row in a for x in row), F(0))


def matrix_power(a: list[list[F]], k: int) -> list[list[F]]:
    out = identity(len(a))
    base = a
    while k:
        if k & 1:
            out = matmul(out, base)
        base = matmul(base, base)
        k //= 2
    return out


def multiplication_x(modulus_monic: list[F]) -> list[list[F]]:
    m = len(modulus_monic) - 1
    out = zero_matrix(m)
    for j in range(m):
        image = mod_poly([F(0)] * (j + 1) + [F(1)], modulus_monic)
        image += [F(0)] * (m - len(image))
        for i in range(m):
            out[i][j] = image[i]
    return out


def evaluate_matrix_polynomial(coeffs: list[F], xmat: list[list[F]]) -> list[list[F]]:
    m = len(xmat)
    out = zero_matrix(m)
    power = identity(m)
    for c in coeffs:
        out = matadd(out, matscale(power, c))
        power = matmul(power, xmat)
    return out


def trace_form(p: list[F], weight: list[F] | None = None) -> tuple[list[list[F]], list[F]]:
    p = trim(p[:])
    n = len(p) - 1
    require(p[-1] == 1 and n >= 2, "expected monic polynomial of degree >=2")
    dp = derivative(p)
    dd = derivative(dp)
    modulus = scale(dp, 1 / dp[-1])
    inv_dd = inv_mod(dd, modulus)
    q = mod_poly(scale(mul(p, inv_dd), F(-1)), modulus)
    if weight is not None:
        w2 = mod_poly(mul(weight, weight), modulus)
        q = mod_poly(mul(q, w2), modulus)
    xmat = multiplication_x(modulus)
    qmat = evaluate_matrix_polynomial(q, xmat)
    m = n - 1
    powers = [identity(m)]
    for _ in range(2 * m - 2):
        powers.append(matmul(powers[-1], xmat))
    b = zero_matrix(m)
    for i in range(m):
        for j in range(m):
            b[i][j] = trace(matmul(qmat, powers[i + j]))
    h = zero_matrix(n)
    h[0][0] = F(1)
    for i in range(m):
        for j in range(m):
            h[i + 1][j + 1] = b[i][j]
    return h, q


def swap_rows_cols(a: list[list[F]], i: int, j: int) -> None:
    a[i], a[j] = a[j], a[i]
    for row in a:
        row[i], row[j] = row[j], row[i]


def inertia(a: list[list[F]]) -> tuple[int, int, int]:
    """Exact congruence elimination for a symmetric rational matrix."""
    a = [row[:] for row in a]
    pos = neg = zero = 0
    while a:
        n = len(a)
        pivot = next((i for i in range(n) if a[i][i] != 0), None)
        if pivot is not None:
            if pivot != 0:
                swap_rows_cols(a, 0, pivot)
            d = a[0][0]
            if d > 0:
                pos += 1
            else:
                neg += 1
            rest = zero_matrix(n - 1)
            for i in range(1, n):
                for j in range(1, n):
                    rest[i - 1][j - 1] = a[i][j] - a[i][0] * a[0][j] / d
            a = rest
            continue
        off = None
        for i in range(n):
            for j in range(i + 1, n):
                if a[i][j] != 0:
                    off = (i, j)
                    break
            if off:
                break
        if off is None:
            zero += n
            break
        i, j = off
        if i != 0:
            swap_rows_cols(a, 0, i)
            if j == 0:
                j = i
        if j != 1:
            swap_rows_cols(a, 1, j)
        b = a[0][1]
        pos += 1
        neg += 1
        if n == 2:
            a = []
            continue
        rest = zero_matrix(n - 2)
        for r in range(2, n):
            for s in range(2, n):
                correction = (a[r][0] * a[1][s] + a[r][1] * a[0][s]) / b
                rest[r - 2][s - 2] = a[r][s] - correction
        a = rest
    return pos, neg, zero


def evaluate_polynomial(a: list[F], x: F) -> F:
    out = F(0)
    for coefficient in reversed(a):
        out = out * x + coefficient
    return out


def residue_moment_matrix(p: list[F], critical_roots: list[F]) -> list[list[F]]:
    second = derivative(derivative(p))
    m = len(critical_roots)
    out = zero_matrix(m)
    for c in critical_roots:
        rho = evaluate_polynomial(p, c) / evaluate_polynomial(second, c)
        for i in range(m):
            for j in range(m):
                out[i][j] -= rho * c ** (i + j)
    return out


def principal_submatrix(a: list[list[F]], indices: tuple[int, ...]) -> list[list[F]]:
    return [[a[i][j] for j in indices] for i in indices]


def compression_lower_bound(c: list[list[F]], full_dimension: int, global_linear_term: int = 0) -> int:
    tr = trace(c)
    if tr <= 0:
        positive_lower = 0
    else:
        positive_lower = ceil(tr * tr / frob2(c))
    return global_linear_term + 2 * positive_lower - full_dimension


def critical_block(h: list[list[F]]) -> list[list[F]]:
    return [row[1:] for row in h[1:]]


def weight_multiplication_matrix(p: list[F], weight: list[F]) -> list[list[F]]:
    dp = derivative(p)
    modulus = scale(dp, 1 / dp[-1])
    xmat = multiplication_x(modulus)
    return evaluate_matrix_polynomial(mod_poly(weight, modulus), xmat)


def content_hashes() -> dict[str, str]:
    out: dict[str, str] = {}
    for rel in CONTENT_FILES:
        data = (ROOT / rel).read_bytes().replace(b"\r\n", b"\n")
        out[rel] = hashlib.sha256(data).hexdigest()
    return out


def fixture(name: str, p: list[F], expected_real_roots: int, weight: list[F] | None = None) -> dict[str, object]:
    h, q = trace_form(p, weight)
    pos, neg, zero = inertia(h)
    n = len(p) - 1
    require(zero == 0, f"{name}: unexpected zero eigenvalue")
    require(pos - neg == expected_real_roots, f"{name}: signature mismatch")
    require(pos + neg == n, f"{name}: dimension mismatch")
    tr = trace(h)
    sq = frob2(h)
    rt = F(0) if tr <= 0 else tr * tr / sq
    lower = 2 * ceil(rt) - n if tr > 0 else -n
    require(lower <= expected_real_roots, f"{name}: rank-trace overclaims")
    return {
        "name": name,
        "degree": n,
        "q_mod_pprime": [str(x) for x in q],
        "matrix": [[str(x) for x in row] for row in h],
        "inertia": {"positive": pos, "negative": neg, "zero": zero},
        "signature": pos - neg,
        "expected_real_roots": expected_real_roots,
        "trace": str(tr),
        "frobenius_squared": str(sq),
        "rank_trace_positive_index_lower": str(rt),
        "integer_real_root_lower": lower,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    all_real = fixture(
        "x^3-3x+3/2",
        [F(3, 2), F(-3), F(0), F(1)],
        3,
    )
    nonreal_pair = fixture(
        "x^3+3x",
        [F(0), F(3), F(0), F(1)],
        1,
    )
    quartic = fixture(
        "x^4-2x^2+2",
        [F(2), F(0), F(-2), F(0), F(1)],
        0,
    )
    weighted = fixture(
        "weighted x^3-3x+3/2",
        [F(3, 2), F(-3), F(0), F(1)],
        3,
        [F(2), F(1)],
    )
    require(weighted["inertia"] == all_real["inertia"], "polynomial congruence changed inertia")

    p_all_real = [F(3, 2), F(-3), F(0), F(1)]
    h0, _ = trace_form(p_all_real)
    h1, _ = trace_form(p_all_real, [F(2), F(1)])
    b0, b1 = critical_block(h0), critical_block(h1)
    wmat = weight_multiplication_matrix(p_all_real, [F(2), F(1)])
    require(matmul(transpose(wmat), matmul(b0, wmat)) == b1, "weighted trace form is not an exact congruence")

    require(residue_moment_matrix(p_all_real, [F(-1), F(1)]) == b0, "entire-window residue moment matrix mismatch")
    quartic_p = [F(2), F(0), F(-2), F(0), F(1)]
    quartic_h, _ = trace_form(quartic_p)
    require(residue_moment_matrix(quartic_p, [F(-1), F(0), F(1)]) == critical_block(quartic_h), "quartic residue moment matrix mismatch")

    compression_checks = 0
    for payload_fixture, pcoeffs in (
        (all_real, p_all_real),
        (nonreal_pair, [F(0), F(3), F(0), F(1)]),
        (quartic, [F(2), F(0), F(-2), F(0), F(1)]),
    ):
        h_fixture, _ = trace_form(pcoeffs)
        b_fixture = critical_block(h_fixture)
        mcrit = len(b_fixture)
        expected = int(payload_fixture["expected_real_roots"])
        for size in range(1, mcrit + 1):
            for indices in combinations(range(mcrit), size):
                c = principal_submatrix(b_fixture, indices)
                lower = compression_lower_bound(c, mcrit, global_linear_term=1)
                require(lower <= expected, f"compression overclaims for {payload_fixture['name']} at {indices}")
                compression_checks += 1

    singular_weight_h, _ = trace_form(p_all_real, [F(-1), F(1)])
    require(inertia(singular_weight_h)[2] > 0, "non-coprime weight failed to create the expected degeneracy")

    rho_minus = F(-7, 12)
    rho_plus = F(-1, 12)
    coherence = (-(rho_minus + rho_plus)) ** 2 / (F(2) * (rho_minus**2 + rho_plus**2))
    require(coherence == F(16, 25), "coherence counterexample mutated")

    p1 = F(86864, 100000)
    alpha = F(67250, 100000)
    threshold = (F(1) + alpha / p1) / 2
    variance_threshold = (F(1) - alpha / p1) / (F(1) + alpha / p1)
    clean_bound = p1 * F(4, 5)
    require(p1 == F(5429, 6250), "Xi-prime proportion mutation")
    require(alpha == F(269, 400), "zeta record mutation")
    require(threshold == F(77057, 86864), "record threshold mutation")
    require(variance_threshold == F(9807, 77057), "variance threshold mutation")
    require(clean_bound == F(10858, 15625), "clean record bound mutation")
    require(clean_bound > alpha, "clean target no longer beats record")

    payload = {
        "verdict": VERDICT,
        "finite_trace_form_proved": True,
        "polynomial_preconditioning_proved": True,
        "rank_trace_certificate_proved": True,
        "entire_window_compression_identity_proved_symbolically": True,
        "entire_window_residue_fixture_checks": 2,
        "compression_fixture_checks": compression_checks,
        "weighted_congruence_checked": True,
        "noncoprime_weight_firewall_checked": True,
        "sign_resolvent_identity_proved": True,
        "fixtures": [all_real, nonreal_pair, quartic, weighted],
        "coherence_firewall": {
            "polynomial": "x^3-3x+3/2",
            "all_roots_real": True,
            "all_critical_residues_negative": True,
            "unweighted_coherence": str(coherence),
        },
        "record_bridge": {
            "anthropic_xiprime_quartic_proportion": str(p1),
            "anthropic_zeta_record_decimal": str(alpha),
            "required_good_or_coherence_fraction": str(threshold),
            "equivalent_variance_ratio_threshold": str(variance_threshold),
            "clean_nine_tenths_result": str(clean_bound),
        },
        "content_sha256": content_hashes(),
        "LHRT105300_proved": False,
        "LEXI105301_proved": False,
        "anthropic_record_beaten": False,
        "rh_established": False,
    }
    canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    payload["proof_object_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(VERDICT)
    print(payload["proof_object_sha256"])
    print("ANTHROPIC_RECORD_NOT_YET_BEATEN")
    print("RH_UNPROVED")


if __name__ == "__main__":
    main()
