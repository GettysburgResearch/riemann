#!/usr/bin/env python3
"""Exact native-window fixtures and symbolic autocorrelation constants for SCB."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import product
from math import comb, gcd, isqrt, prod
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
NOTE = HERE / "SUBCRITICAL_OBSERVED_BOOLEAN_BLOCK.md"
LOCK = HERE / "subcritical_observed_boolean_block.sources.json"
FIXTURE = HERE / "subcritical_observed_boolean_block.json"
TEST = ROOT / "tests" / "test_subcritical_observed_boolean_block.py"
SCOUT = HERE / "subcritical_boolean_scout.py"
MAX_BYTES = 131_072
OLD = "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc"
FAMILY = "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b"
SOURCES = {
    (
        FAMILY,
        "claims/lemmas/L-106080-squarefree-boolean-vaughan-keeps-the-balanced-core-literal.md",
    ): "346cc52420ec65457c2a5accc045d4a85635cc24",
    (
        FAMILY,
        "claims/lemmas/L-106026-mellin-plancherel-normal-form-for-owner-conductor-moment.md",
    ): "388c7e166a0e6e534d7e908685f71a16de246575",
    (
        FAMILY,
        "claims/lemmas/L-106090-least-discrepancy-prime-triangularizes-the-coprime-boolean-core.md",
    ): "dadf3a4a65d2575983d692dafc0c94142c9a038d",
    (
        FAMILY,
        "claims/lemmas/L-106120-bilateral-least-prime-phases-form-a-tensor-kummer-family.md",
    ): "a8d829dc10611adb7bfb4853902bdff0ab02a065",
    (
        OLD,
        "claims/lemmas/L-102746-wick-tail-has-a-canonical-equal-pair-owner.md",
    ): "db018c64dde45ff4ad17541eb6ba00b4f6fa9d49",
    (
        OLD,
        "claims/lemmas/L-102880-logarithmic-derivative-outer-detector-has-zero-square-lattice-moment.md",
    ): "d7330d114ebba1a7a16e22fa9ba6aa6b5eb7cdd6",
}

WINDOWS = {
    "A": (Fraction(101, 100), Fraction(51, 50), 4),
    "B": (Fraction(1), Fraction(101, 100), 3),
    "ell": (Fraction(51, 50), Fraction(409, 400), 1),
    "rho": (Fraction(411, 400), Fraction(103, 100), 1),
    "p": (Fraction(3200, 4000), Fraction(3201, 4000), 4),
    "q": (Fraction(4800, 4000), Fraction(4801, 4000), 4),
    "r": (Fraction(3203, 4000), Fraction(3204, 4000), 4),
    "s": (Fraction(4803, 4000), Fraction(4804, 4000), 4),
}

# Each large-prime tuple is (prime, Proth exponent, witness); a zero exponent
# invokes exact trial division. The coordinating agent's bounded scout chose
# these parameters. Published replay verifies them without repeating a search.
PANELS = {
    52: {
        "A": (4548640815185921, 27, 3),
        "B": (549800902657, 20, 5),
        "ell": (8363, 0, 0),
        "rho": (8419, 0, 0),
        "p": (3602895190622209, 27, 7),
        "q": (5404323928342529, 27, 3),
        "r": (3606258150014977, 27, 5),
        "s": (5407698967330817, 27, 3),
    },
    56: {
        "A": (72778253579845633, 29, 5),
        "B": (4398310752257, 22, 3),
        "ell": (16729, 0, 0),
        "rho": (16843, 0, 0),
        "p": (57646182926647297, 29, 5),
        "q": (86469113597132801, 29, 3),
        "r": (57700136305819649, 29, 3),
        "s": (86523162539327489, 29, 3),
    },
    60: {
        "A": (1164450727985152001, 31, 3),
        "B": (35184414031873, 23, 5),
        "ell": (33427, 0, 0),
        "rho": (33679, 0, 0),
        "p": (922337314066137089, 31, 3),
        "q": (1383505875536183297, 31, 3),
        "r": (923201942522429441, 31, 3),
        "s": (1384370718740840449, 31, 7),
    },
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def canonical(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def authenticate_sources() -> list[dict[str, object]]:
    raw = LOCK.read_bytes()
    require(len(raw) <= MAX_BYTES, "manifest cap")
    manifest = json.loads(raw)
    require(
        manifest.get("schema") == "riemann.subcritical_boolean.sources.v1",
        "source schema",
    )
    rows = manifest.get("sources")
    require(type(rows) is list and len(rows) == len(SOURCES), "source count")
    seen, result = set(), []
    for row in rows:
        require(type(row) is dict, "source row type")
        key = (row.get("commit"), row.get("path"))
        require(key in SOURCES and key not in seen, "source identity/duplicate")
        require(row.get("git_blob") == SOURCES[key], "manifest blob mismatch")
        ref = f"{key[0]}:{key[1]}"
        size = int(
            subprocess.run(
                ["git", "cat-file", "-s", ref],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=True,
            ).stdout
        )
        require(0 < size <= MAX_BYTES, "primitive source cap")
        source = subprocess.run(
            ["git", "show", ref], cwd=ROOT, capture_output=True, check=True
        ).stdout
        require(len(source) == size, "primitive source length")
        actual = sha1(b"blob " + str(size).encode() + b"\0" + source).hexdigest()
        require(actual == SOURCES[key], "primitive source bytes")
        seen.add(key)
        result.append({**row, "bytes": size})
    require(seen == set(SOURCES), "source coverage")
    return result


def verify_prime(certificate: tuple[int, int, int]) -> dict[str, object]:
    require(
        type(certificate) is tuple and len(certificate) == 3, "prime certificate tuple"
    )
    n, exponent, witness = certificate
    require(all(type(v) is int for v in certificate), "prime certificate integer type")
    require(2 <= n < 2**64, "prime size cap")
    if exponent == 0:
        require(witness == 0 and n < 100_000, "trial division cap")
        require(all(n % d for d in range(2, isqrt(n) + 1)), "composite trial input")
        return {"prime": n, "method": "EXACT_TRIAL_DIVISION"}
    require(2 <= exponent <= 32 and 1 < witness < n, "Proth exponent/witness")
    step = 2**exponent
    odd_part, remainder = divmod(n - 1, step)
    require(remainder == 0 and odd_part % 2 == 1 and 0 < odd_part < step, "Proth form")
    require(pow(witness, (n - 1) // 2, n) == n - 1, "Proth witness failed")
    return {
        "prime": n,
        "method": "PROTH",
        "exponent": exponent,
        "odd_part": odd_part,
        "witness": witness,
    }


def a_u(labels: tuple[int, ...], cutoff: int) -> int:
    require(type(labels) is tuple and len(labels) <= 3, "Boolean label cap")
    require(type(cutoff) is int and cutoff > 0, "Boolean cutoff")
    require(all(type(p) is int and p > 1 for p in labels), "Boolean integer labels")
    require(len(set(labels)) == len(labels), "Boolean repeated label")
    answer = int(not labels)
    for mask in product((0, 1), repeat=len(labels)):
        divisor = prod(p for p, use in zip(labels, mask, strict=True) if use)
        if divisor <= cutoff:
            answer -= (-1) ** sum(mask)
    return answer


def histories(labels: tuple[int, ...], cutoff: int) -> list[dict[str, object]]:
    require(type(labels) is tuple and len(labels) == 3, "three-label source required")
    result = []
    for allocation in product(range(3), repeat=3):
        groups = tuple(
            tuple(p for p, side in zip(labels, allocation, strict=True) if side == i)
            for i in range(3)
        )
        coefficient = (
            a_u(groups[0], cutoff) * a_u(groups[1], cutoff) * (-1) ** len(groups[2])
        )
        if coefficient:
            result.append(
                {
                    "groups": [list(group) for group in groups],
                    "coefficient": coefficient,
                }
            )
    return result


# Quadratic numbers a+b sqrt(2) use exact rational pairs.
def q2(a=0, b=0):
    return (Fraction(a), Fraction(b))


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def neg(x):
    return (-x[0], -x[1])


def mul(x, y):
    return (x[0] * y[0] + 2 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def sign(x):
    a, b = x
    if b == 0:
        return (a > 0) - (a < 0)
    if a == 0:
        return (b > 0) - (b < 0)
    if a * b > 0:
        return (a > 0) - (a < 0)
    comparison = a * a - 2 * b * b
    require(comparison != 0, "nonzero rational sqrt2 separation")
    return ((a > 0) - (a < 0)) * ((comparison > 0) - (comparison < 0))


def absolute(x):
    return x if sign(x) >= 0 else neg(x)


def kernel_record() -> dict[str, object]:
    roots = (q2(1), q2(0, 1), q2(2), q2(0, 2))
    coefficients = ((q2(8), q2(-4)), (q2(-8, -8), q2(0, 4)), (q2(0, 8), q2(-2)))
    variation, maximum = q2(), q2()
    log_coefficient, constant = q2(), q2()
    last = q2()
    pieces = []
    for i, (a, b) in enumerate(coefficients):
        left = add(a, mul(b, roots[i]))
        right = add(a, mul(b, roots[i + 1]))
        variation = add(variation, absolute(add(left, neg(last))))
        variation = add(variation, absolute(add(right, neg(left))))
        for value in (absolute(left), absolute(right)):
            if sign(add(value, neg(maximum))) > 0:
                maximum = value
        log_part = mul(a, a)
        constant_part = add(
            mul(q2(4), mul(mul(a, b), add(roots[i + 1], neg(roots[i])))),
            mul(mul(b, b), q2(2 ** (i + 1) - 2**i)),
        )
        log_coefficient = add(log_coefficient, log_part)
        constant = add(constant, constant_part)
        pieces.append(
            {
                "log2_coefficient": list(map(str, log_part)),
                "constant": list(map(str, constant_part)),
            }
        )
        last = right
    variation = add(variation, absolute(last))
    require(
        maximum == q2(0, 8) and variation == q2(0, 32), "kernel sup and full variation"
    )
    require(
        log_coefficient == q2(384, 128) and constant == q2(-288), "exact squared norm"
    )
    penalty = mul(maximum, variation)
    require(penalty == q2(512), "translation penalty")
    lower = (
        (Fraction(384) + Fraction(128) * Fraction(7, 5)) * Fraction(2, 3)
        - 288
        - Fraction(512, 10)
    )
    require(lower == Fraction(544, 15) and lower > 36, "rational Gram lower bound")
    return {
        "pieces": pieces,
        "supremum": list(map(str, maximum)),
        "total_variation": list(map(str, variation)),
        "norm_log2_coefficient": list(map(str, log_coefficient)),
        "norm_constant": list(map(str, constant)),
        "translation_penalty": str(penalty[0]),
        "strict_gram_lower": str(lower),
        "accepted_simple_gram_lower": 36,
        "gram_upper": 384,
        "floating_evaluations": False,
        "log_or_sqrt_evaluations": False,
    }


def panel_record(
    j: int, certificates: dict[str, tuple[int, int, int]]
) -> dict[str, object]:
    require(type(j) is int and j in (52, 56, 60), "fixture exponent coverage")
    require(
        type(certificates) is dict and set(certificates) == set(WINDOWS),
        "eight source labels",
    )
    u, y = 2**j, 2 ** (6 * j)
    rows, values = {}, {}
    for label, certificate in certificates.items():
        row = verify_prime(certificate)
        lower, upper, quarter_power = WINDOWS[label]
        scale = 2 ** (j * quarter_power // 4)
        n = row["prime"]
        require(lower * scale < n < upper * scale, "strict source window")
        rows[label] = {**row, "lower": str(lower * scale), "upper": str(upper * scale)}
        values[label] = n
    require(
        len(set(values.values())) == 8 and 67 not in values.values(),
        "all physical labels distinct",
    )
    a, b, ell, rho = (values[k] for k in ("A", "B", "ell", "rho"))
    p, q, r, s = (values[k] for k in ("p", "q", "r", "s"))
    g, owner_p, owner_q = a * b, p * q, r * s
    n, m = owner_p * (g * ell) ** 2, owner_q * (g * rho) ** 2
    require(
        y < n < Fraction(11, 10) * y and y < m < Fraction(11, 10) * y, "physical shell"
    )
    require(
        Fraction(10, 11) < Fraction(n, m) < Fraction(11, 10), "autocorrelation window"
    )
    require(gcd(g * ell, g * rho) == g and ell < rho, "common core and orientation")
    require(
        gcd(owner_p, owner_q * g * ell * rho) == 1 and gcd(owner_q, g * ell * rho) == 1,
        "clean owners",
    )
    require(max(values.values()) < 4 * 2 ** (3 * j), "horizon-safe owner range")
    left, right = histories((a, b, ell), u), histories((a, b, rho), u)
    require(len(left) == len(right) == 2, "complete two-history coverage")
    require(
        all(row["coefficient"] == -1 for row in left + right),
        "literal negative history signs",
    )
    require(a_u((a,), u) == -1 and a_u((b, ell), u) == 1, "frozen a_U convention")
    share = Fraction(1, comb(5, 2))
    coefficient_square = Fraction(1, 625 * n * m)
    literal_square = Fraction(1, 10000 * n * m)
    require(
        coefficient_square == 16 * literal_square, "four histories sum before square"
    )
    dual_square = (g * ell * rho) ** 2 * coefficient_square
    principal_weight = (
        Fraction(ell + 1, ell - 1) * Fraction(rho + 1, rho - 1) / (ell * rho)
    )
    original_weight = (
        g * g * ell * rho * Fraction(ell + 1, ell - 1) * Fraction(rho + 1, rho - 1)
    )
    require(
        principal_weight * dual_square == original_weight * coefficient_square,
        "principal source-dual conversion",
    )
    return {
        "j": j,
        "U": u,
        "Y": y,
        "primes": rows,
        "g": g,
        "P": owner_p,
        "Q": owner_q,
        "N": n,
        "M": m,
        "physical_ratio": str(Fraction(n, m)),
        "left_histories": left,
        "right_histories": right,
        "equal_pair_share": str(share),
        "bilateral_literal_histories": 4,
        "aggregate_coefficient_square": str(coefficient_square),
        "one_literal_coefficient_square": str(literal_square),
        "literal_bilateral_diagonal": str(4 * literal_square),
        "source_dual_coefficient_square": str(dual_square),
        "principal_source_dual_weight": str(principal_weight),
        "term_strict_lower": str(Fraction(72, 55 * y)),
        "term_upper": str(Fraction(384, 25 * y)),
        "complete_carrier_binding_asserted": False,
    }


def build() -> dict[str, object]:
    sources = authenticate_sources()
    hashes = {}
    for path in (Path(__file__), NOTE, LOCK, TEST, SCOUT):
        raw = path.read_bytes()
        require(len(raw) <= MAX_BYTES, "local source cap")
        hashes[path.relative_to(ROOT).as_posix()] = sha256(
            raw.replace(b"\r\n", b"\n")
        ).hexdigest()
    result = {
        "schema": "riemann.subcritical_observed_boolean.v1",
        "sources": sources,
        "source_hashes": hashes,
        "arithmetic": "EXACT_INTEGER_RATIONAL_QUADRATIC_SYMBOLIC",
        "kernel": kernel_record(),
        "panels": [panel_record(j, panel) for j, panel in PANELS.items()],
        "prime_counting_theorem_replayed": False,
        "full_source_lower_bound_asserted": False,
        "production_search_performed": False,
    }
    result["proof_object_sha256"] = sha256(canonical(result).encode()).hexdigest()
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.write:
        FIXTURE.write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
    else:
        candidate = json.loads(FIXTURE.read_text(encoding="utf-8"))
        require(
            canonical(candidate) == canonical(result),
            "canonical primitive replay mismatch",
        )
    print(
        json.dumps(
            {"status": "PASS", "proof_object_sha256": result["proof_object_sha256"]}
        )
    )


if __name__ == "__main__":
    main()
