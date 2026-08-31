"""Independent finite FI audit: no author-module import or numerical divisor search."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DIR = "research/l-families/atlas/generalized"
SCIENCE = "ec5bdd9b02ea68bddfcf34ac40a85d283faf64cf"
PARENT = "eaa8e8263bb34b8b669f911580c9dd9e55766ba2"
STEM = "cusp_weight24_fixed_divisor_infinity"
SELF = "weight24_divisor_independent_audit_ec5bdd9b"
ORDER = 64
DELTA2 = 83041344
FILES = (
    f"{DIR}/CUSP_WEIGHT24_FIXED_DIVISOR_INFINITY.md",
    f"{DIR}/{STEM}.py",
    f"{DIR}/{STEM}.json",
    f"{DIR}/{STEM}.sources.json",
    f"tests/test_{STEM}.py",
)


def need(value: bool, reason: str) -> None:
    if not value:
        raise ValueError(reason)


def enc(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2) + "\n").encode("ascii")


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest()


def git(spec: str) -> bytes:
    return subprocess.check_output(
        ["git", "--no-replace-objects", "show", spec], cwd=ROOT
    )


def mul(left: list[int], right: list[int]) -> list[int]:
    return [sum(left[j] * right[n - j] for j in range(n + 1)) for n in range(ORDER + 1)]


def divisor_sum(n: int, power: int) -> int:
    return sum(d**power for d in range(1, n + 1) if n % d == 0)


def tau(n: int) -> int:
    return divisor_sum(n, 0)


def basis() -> tuple[list[int], list[int]]:
    # A third primitive construction, unlike the author's logarithmic Delta
    # recurrence and the resident tests' Euler product.
    e4 = [1] + [240 * divisor_sum(n, 3) for n in range(1, ORDER + 1)]
    e6 = [1] + [-504 * divisor_sum(n, 5) for n in range(1, ORDER + 1)]
    cube, square = mul(mul(e4, e4), e4), mul(e6, e6)
    delta = []
    for x, y in zip(cube, square):
        need((x - y) % 1728 == 0, "modular identity integrality")
        delta.append((x - y) // 1728)
    b = mul(delta, delta)
    g = [x - 696 * y for x, y in zip(mul(delta, cube), b)]
    need(g[1:3] == [1, 0] and b[1:3] == [0, 1], "canonical, not eigenline, flag")
    return g, b


def coefficients(g: list[int], b: list[int]) -> list[dict]:
    rows = []
    for n in range(1, ORDER + 1):
        h, numerator = F(), F()
        for m in range(1, math.isqrt(n) + 1):
            if n % (m * m):
                continue
            v = n // (m * m)
            h += F(DELTA2 * b[v] ** 2, v**23)
            # Direct Cauchy--Binet pairs: no eigen-coefficient or Dirichlet
            # convolution implementation is shared with the author.
            for a in range(1, math.isqrt(v) + 1):
                if v % a:
                    continue
                c = v // a
                if a < c:
                    wedge = g[a] * b[c] - g[c] * b[a]
                    numerator += F(DELTA2 * tau(m) * wedge**2, v**23)
        rows.append(
            {
                "n": n,
                "H": [h.numerator, h.denominator],
                "N": [numerator.numerator, numerator.denominator],
            }
        )
    need(rows[0]["H"] == rows[0]["N"] == [0, 1], "constant cancellation")
    need(rows[1]["H"] == rows[1]["N"] == [1297521, 131072], "first term")
    return rows


def add(a: dict, b: dict) -> dict:
    out = a.copy()
    for key, value in b.items():
        out[key] = out.get(key, 0) + value
        if not out[key]:
            del out[key]
    return out


def pmul(a: dict, b: dict) -> dict:
    out = {}
    for (i, j), v in a.items():
        for (k, l), w in b.items():
            key = (i + k, j + l)
            out[key] = out.get(key, 0) + v * w
    return {key: value for key, value in out.items() if value}


def tensor_identity() -> dict:
    # Formal Laurent variables u,v, through a held-out degree twelve.
    # Independent multiplication of four geometric series vs h_a(u)h_a(v).
    limit = 12
    out = [{(0, 0): 1}] + [{} for _ in range(limit)]
    for x in (-1, 1):
        for y in (-1, 1):
            geometric = [{(x * n, y * n): 1} for n in range(limit + 1)]
            out = [
                sum_polynomials(pmul(out[j], geometric[n - j]) for j in range(n + 1))
                for n in range(limit + 1)
            ]
    terms = []
    for n in range(limit + 1):
        row = {(n - 2 * i, n - 2 * j): 1 for i in range(n + 1) for j in range(n + 1)}
        actual = (
            add(out[n], {k: -v for k, v in out[n - 2].items()}) if n >= 2 else out[n]
        )
        need(actual == row, "FI6 universal numerator is 1-X^2")
        terms.append(len(actual))
    return {"degree": limit, "weight_counts": terms}


def sum_polynomials(polys) -> dict:
    out = {}
    for poly in polys:
        out = add(out, poly)
    return out


def replay() -> dict:
    source = {}
    for path in FILES:
        raw = git(f"{SCIENCE}:{path}")
        need(sha((ROOT / path).read_bytes()) == sha(raw), "frozen science drift")
        source[path] = sha(raw)
    value = json.loads(git(f"{SCIENCE}:{DIR}/{STEM}.json"))
    manifest = json.loads(git(f"{SCIENCE}:{DIR}/{STEM}.sources.json"))
    for row in manifest["frozen_sources"]:
        raw = git(row["commit"] + ":" + row["path"])
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        need(blob == row["git_blob"] and sha(raw) == row["sha256_lf"], "source seal")
    for path, digest in value["artifact_sha256_lf"].items():
        need(source[path] == digest, "artifact seal")
    unsealed = value.copy()
    payload = unsealed.pop("payload_sha256")
    need(hashlib.sha256(enc(unsealed)).hexdigest() == payload, "payload seal")
    g, b = basis()
    need(value["basis"] == [g, b], "independent modular basis")
    rows = coefficients(g, b)
    need(
        rows
        == [
            {k: row[k] for k in ("n", "H", "N")}
            for row in value["dirichlet_coefficients"]
        ],
        "complete direct pair coefficient comparison",
    )
    for n in range(1, ORDER // 2 + 1):
        for f, expected in ((g, 20468736 * b[n]), (b, g[n] + 1080 * b[n])):
            actual = f[2 * n] + (2**23 * f[n // 2] if n % 2 == 0 else 0)
            need(actual == expected, "Hecke action full held-out prefix")
    return {
        "schema": "independent-weight24-divisor-audit-v1",
        "arithmetic_class": "MIXED",
        "components": ["EXACT_RATIONAL", "CERTIFIED_INTEGER_COVERAGE"],
        "rounding": "none",
        "science": SCIENCE,
        "parent": PARENT,
        "science_sha256_lf": source,
        "frozen_source_count": len(manifest["frozen_sources"]),
        "artifact_count": len(value["artifact_sha256_lf"]),
        "science_payload_sha256": payload,
        "q_order": ORDER,
        "third_route_basis": [g, b],
        "direct_cauchy_binet_coefficients": rows,
        "formal_tensor_identity": tensor_identity(),
        "analytic_proof_machine_certified": "no",
        "scope": "independent finite identity and seal audit, not numerical zeros or primes",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--emit", action="store_true")
    args = parser.parse_args()
    out = replay()
    if args.emit:
        print(enc(out).decode("ascii"), end="")
    else:
        need(
            json.loads((ROOT / DIR / f"{SELF}.json").read_bytes()) == out,
            "review fixture",
        )
        print(
            "PASS: third modular route, 64 Cauchy-Binet pairs, formal FI6 through 12, all seals"
        )


if __name__ == "__main__":
    main()
