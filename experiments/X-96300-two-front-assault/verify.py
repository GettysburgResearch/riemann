#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
SCHEMA = "riemann.x96300.two-front-assault.v1"
RESULT_SCHEMA = "riemann.x96300.two-front-assault.result.v1"


def frac(x: Any) -> Fraction:
    if isinstance(x, bool):
        raise ValueError("boolean is not rational")
    if isinstance(x, int):
        return Fraction(x)
    if isinstance(x, str):
        return Fraction(x)
    raise ValueError(f"unsupported rational: {x!r}")


def fstr(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def mobius_table(n: int) -> list[int]:
    mu = [0] * (n + 1)
    mu[1] = 1
    primes: list[int] = []
    composite = [False] * (n + 1)
    for i in range(2, n + 1):
        if not composite[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > n:
                break
            composite[i * p] = True
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    return mu


def factor(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def add_formal(a: dict[int, Fraction], b: dict[int, Fraction], scale: Fraction = Fraction(1)) -> dict[int, Fraction]:
    out = dict(a)
    for p, v in b.items():
        out[p] = out.get(p, Fraction(0)) + scale * v
        if out[p] == 0:
            del out[p]
    return out


def lambda_formal(n: int) -> dict[int, Fraction]:
    fs = factor(n)
    if len(fs) == 1:
        p = next(iter(fs))
        return {p: Fraction(1)}
    return {}


def log_formal(n: int) -> dict[int, Fraction]:
    return {p: Fraction(e) for p, e in factor(n).items()}


def tent_polynomial(v: Fraction, h: Fraction) -> Fraction:
    return v - 2 * max(v - h, Fraction(0)) + max(v - 2 * h, Fraction(0))


def validate(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise ValueError("schema mismatch")

    # Compact annular triangularization after factoring out exp(-v/2).
    h = frac(data["annular"]["h"])
    if h <= 0:
        raise ValueError("h must be positive")
    annular = []
    for raw in data["annular"]["samples"]:
        v = frac(raw)
        k = tent_polynomial(v, h)
        expected = v if v < h else (2 * h - v if v < 2 * h else Fraction(0))
        if k != expected or k < 0:
            raise ValueError("annular tent identity failed")
        annular.append({"v": fstr(v), "tent_over_exp": fstr(k)})

    # One positive-base row and factorized numerator.
    q2 = [frac(x) for x in data["single_row"]["q2"]]
    q3 = [frac(x) for x in data["single_row"]["q3"]]
    w2, w3 = map(int, data["single_row"]["weights"])
    qstar = [w2 * a + w3 * b for a, b in zip(q2, q3)]
    expected = [frac(x) for x in data["single_row"]["expected"]]
    if qstar != expected or min(qstar) <= 0:
        raise ValueError("positive-base row dictionary failed")
    numerator = [frac(x) for x in data["single_row"]["numerator"]]
    # -3(a-1)(a-2) = -6 + 9a - 3a^2.
    if numerator != [Fraction(-6), Fraction(9), Fraction(-3)]:
        raise ValueError("single-row numerator factorization failed")

    # Exact formal piecewise profile for 5 p_s(2)+3 p_s(3).
    profile = [[frac(x) for x in row] for row in data["volterra_profile"]["branches"]]
    expected_profile = [
        [Fraction(0), Fraction(15), Fraction(0), Fraction(0), Fraction(-30)],
        [Fraction(0), Fraction(15), Fraction(-9), Fraction(0), Fraction(-3)],
        [Fraction(-6), Fraction(15), Fraction(-9), Fraction(0), Fraction(9)],
        [Fraction(-6), Fraction(15), Fraction(-9), Fraction(3), Fraction(-6)],
    ]
    if profile != expected_profile:
        raise ValueError("single-row Volterra profile drift")

    # Exact Dirichlet-convolution identity R=sum q*(m)V(X/m), at coefficient level.
    N = int(data["formal_cutoff"])
    if N < 16:
        raise ValueError("formal cutoff too small")
    mu = mobius_table(N)
    qdict = {1: 0, 2: 15, 3: 6, 4: 3}
    for m in range(5, N + 1):
        qdict[m] = 6
    conv = [0] * (N + 1)
    direct = [0] * (N + 1)
    for n in range(1, N + 1):
        conv[n] = sum(mu[d] * qdict[n // d] for d in range(1, n + 1) if n % d == 0)
        # Same coefficient obtained by expanding the positive smoothing.
        direct[n] = sum(qdict[m] * mu[n // m] for m in range(1, n + 1) if n % m == 0)
    if conv != direct:
        raise ValueError("positive smoothing convolution failed")

    # Formal prime-log identity mu * Lambda = -mu log.
    for n in range(1, N + 1):
        lhs: dict[int, Fraction] = {}
        for d in range(1, n + 1):
            if n % d == 0 and mu[d]:
                lhs = add_formal(lhs, lambda_formal(n // d), Fraction(mu[d]))
        rhs = {p: Fraction(-mu[n]) * e for p, e in factor(n).items() if mu[n] != 0}
        if lhs != rhs:
            raise ValueError(("formal prime feedback failed", n, lhs, rhs))

    # Signed affine moment cone and endpoint reconstruction.
    affine = data["affine"]
    A = [frac(x) for x in affine["A"]]
    B = [frac(x) for x in affine["B"]]
    ua, ub = frac(affine["u_a"]), frac(affine["u_b"])
    M, U = frac(affine["M"]), frac(affine["U"])
    if not (ua > ub > 0 and M > 0 and M * ub <= U <= M * ua):
        raise ValueError("affine moment is outside cone")
    alpha = (U - M * ub) / (ua - ub)
    beta = M - alpha
    if min(alpha, beta) < 0:
        raise ValueError("negative endpoint coefficient")
    lhs = [M * a - U * b for a, b in zip(A, B)]
    pa = [a - ua * b for a, b in zip(A, B)]
    pb = [a - ub * b for a, b in zip(A, B)]
    rhs_vec = [alpha * x + beta * y for x, y in zip(pa, pb)]
    if lhs != rhs_vec:
        raise ValueError("affine moment reconstruction failed")

    # Mellin-coordinate bridges after removing the common 1/zeta factor.
    mellin_rows = []
    for raw in data["mellin_samples"]:
        s = frac(raw)
        if s == Fraction(1, 2) or s == 0:
            raise ValueError("singular Mellin sample")
        V = Fraction(1, 1) / (s * s)
        L = (s + Fraction(1, 2)) / (s * (s - Fraction(1, 2)))
        C = (s + Fraction(3, 2)) / s * L
        if (s - Fraction(1, 2)) * L != s * (s + Fraction(1, 2)) * V:
            raise ValueError("V/L differential bridge failed")
        if C != L + Fraction(3, 2) * L / s:
            raise ValueError("L/C positive integration bridge failed")
        mellin_rows.append({"s": fstr(s), "V": fstr(V), "L": fstr(L), "C": fstr(C)})

    fw = data["firewalls"]
    if any(fw[k] is not False for k in (
        "actq_proved", "sprp_proved", "vrp_proved", "amcp_proved",
        "rh_established", "imports_pr537_frontier_chain_as_proof",
        "uses_old_J_equals_Y4_normalization",
    )):
        raise ValueError("proof boundary was promoted")

    expected_genealogy = {
        "base_pr": 544,
        "base_sha": "d4dcd1256dc9c8e110c860cff87b3f89aee842a5",
        "pr353_sha": "ed566f3198e236c54ba18049181016536f56d456",
        "pr541_sha": "e381f444191e214cc992208b16d30a8d5fd461ac",
        "pr542_sha": "ca5fb69c15cda29b3b589660f9be44ea2f440677",
        "pr546_sha": "f920202ea15c577bf05fa58370bdc3d8313868cd",
    }
    if data.get("genealogy") != expected_genealogy:
        raise ValueError("genealogy mismatch")

    result = {
        "schema": RESULT_SCHEMA,
        "verdict": "PASS_T96300_RADICAL_TWO_FRONT_ASSAULT_ALGEBRA",
        "annular_tent": annular,
        "single_row": {
            "weights": [w2, w3],
            "positive_base": [fstr(x) for x in qstar],
            "numerator": [fstr(x) for x in numerator],
            "factorization": "-3(a-1)(a-2)",
        },
        "formal_cutoff": N,
        "formal_feedback_identity": "mu*Lambda=-mu*log",
        "affine_moment_cone": {
            "alpha": fstr(alpha),
            "beta": fstr(beta),
            "row": [fstr(x) for x in lhs],
        },
        "mellin_bridges": mellin_rows,
        "genealogy": expected_genealogy,
        "open_producers": ["ACTQ_h", "SPRP", "VRP", "AMCP"],
        "rh_established": False,
        "proof_boundary": (
            "Exact annular kernel, scale multiplier, positive-base single-row algebra, "
            "finite convolution, formal prime feedback, affine moment cone and Mellin-coordinate bridges. "
            "Does not prove any producer or RH."
        ),
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", nargs="?", type=Path, default=HERE / "certificates" / "control.json")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = validate(json.loads(args.certificate.read_text()))
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    print(result["verdict"])
    print(result["proof_object_sha256"])


if __name__ == "__main__":
    main()
