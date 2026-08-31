"""Independent frozen-source finite replay; imports no author mathematics."""

from __future__ import annotations

import hashlib
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SOURCE = "eaa8e8263bb34b8b669f911580c9dd9e55766ba2"
DIR = "research/l-families/atlas/generalized"
STEM = "cusp_flag_hecke_source_concentration"
PARAMS = {0: (0, 0), 4: (1, 0), 6: (0, 1), 8: (2, 0), 10: (1, 1), 14: (2, 1)}


def need(ok, message):
    if not ok:
        raise ValueError(message)


def raw(spec):
    out = subprocess.run(
        ["git", "--no-replace-objects", "show", spec],
        cwd=ROOT,
        capture_output=True,
        check=True,
    ).stdout
    need(len(out) <= 2000000, "source size")
    return out


def sha(data):
    return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()


def canonical(obj):
    return (
        json.dumps(obj, sort_keys=True, indent=2, ensure_ascii=True, allow_nan=False)
        + "\n"
    ).encode("ascii")


def mul(a, b):
    return [sum(a[j] * b[n - j] for j in range(n + 1)) for n in range(len(a))]


def power(a, n):
    out = [1] + [0] * (len(a) - 1)
    for _ in range(n):
        out = mul(out, a)
    return out


def basis(d, residual, order):
    need(
        type(d) is int and 2 <= d <= 4 and residual in PARAMS and 1 <= order <= 35,
        "chart cap",
    )
    a, b = PARAMS[residual]
    e4 = [1] + [
        240 * sum(j**3 for j in range(1, n + 1) if n % j == 0)
        for n in range(1, order + 1)
    ]
    e6 = [1] + [
        -504 * sum(j**5 for j in range(1, n + 1) if n % j == 0)
        for n in range(1, order + 1)
    ]
    # Independent finite Euler product, with exact binomial coefficients.
    dp = [1] + [0] * (order - 1)
    for n in range(1, order):
        fac = [0] * order
        for j in range(min(24, (order - 1) // n) + 1):
            fac[j * n] = (-1) ** j * math.comb(24, j)
        dp = mul(dp, fac)
    delta = [0] + dp
    rows = [
        mul(power(delta, j), mul(power(e4, 3 * (d - j) + a), power(e6, b)))
        for j in range(1, d + 1)
    ]
    # Forward elimination differs from the producer's descending elimination.
    for pivot in range(1, d):
        for i in range(pivot):
            c = rows[i][pivot + 1]
            rows[i] = [x - c * y for x, y in zip(rows[i], rows[pivot])]
    need(
        all(rows[i][j + 1] == int(i == j) for i in range(d) for j in range(d)), "pivots"
    )
    return rows


def matrix(rows, k, m, action_through):
    d = len(rows)

    def coefficient(j, n):
        return sum(
            h ** (k - 1) * rows[j][m * n // (h * h)]
            for h in range(1, m + 1)
            if m % h == 0 and n % h == 0
        )

    ans = [[coefficient(j, n) for j in range(d)] for n in range(1, d + 1)]
    for n in range(1, action_through + 1):
        for j in range(d):
            need(
                coefficient(j, n) == sum(ans[i][j] * rows[i][n] for i in range(d)),
                "full held-out Hecke action",
            )
    return ans


def mm(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def replay():
    fixture = json.loads(raw(f"{SOURCE}:{DIR}/{STEM}.json"))
    manifest = json.loads(raw(f"{SOURCE}:{DIR}/{STEM}.sources.json"))
    seals = {}
    for row in manifest["frozen_sources"]:
        data = raw(row["commit"] + ":" + row["path"])
        blob = hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()
        need(
            blob == row["git_blob"] and sha(data) == row["sha256_lf"],
            "literal source binding",
        )
    for path, expected in fixture["artifact_sha256_lf"].items():
        seals[path] = sha(raw(SOURCE + ":" + path))
        need(seals[path] == expected, "artifact binding")
    unsealed = dict(fixture)
    wanted = unsealed.pop("payload_sha256")
    need(sha(canonical(unsealed)) == wanted, "payload binding")
    records = []
    for row in fixture["q_rows"]:
        d, k, r = row["d"], row["k"], row["residual"]
        order = 5 * (d + 3)
        bs = basis(d, r, order)
        need(
            [b[: row["q_order"] + 1] for b in bs] == row["basis"], "source full prefix"
        )
        mats = {m: matrix(bs, k, m, d + 3) for m in (2, 3, 4, 5)}
        need(mats[2] == row["T2"] and mats[3] == row["T3"], "original matrices")
        square = mm(mats[2], mats[2])
        t4 = [
            [square[i][j] - (2 ** (k - 1) if i == j else 0) for j in range(d)]
            for i in range(d)
        ]
        need(t4 == mats[4], "preregistered T4")
        need(mm(mats[2], mats[5]) == mm(mats[5], mats[2]), "preregistered T2T5")
        records.append(
            {
                "k": k,
                "dimension": d,
                "order": order,
                "action_through": d + 3,
                "T4": mats[4],
                "T5": mats[5],
            }
        )
    # Derive the d4 convolution by grouping integer quadruples, not source rows.
    for n, actual, upper in fixture["controls"]["harmonic"]:
        divisor_counts = []
        for t in range(1, n + 1):
            div = [a for a in range(1, t + 1) if t % a == 0]
            count = sum(
                1 for a in div for b in div for c in div if t % (a * b * c) == 0
            )
            divisor_counts.append(count)
        left = sum(
            (Fraction(a, t) for t, a in enumerate(divisor_counts, 1)), Fraction()
        )
        need(left == Fraction(*actual), "all harmonic rows")
        need(left <= Fraction(*upper), "harmonic upper")
    # A symbolic local Euler factor, represented as exact Laurent dictionaries.
    # h_r(alpha,alpha^-1)^2 has weights -2r,-2r+2,...,2r with triangular multiplicities.
    # Multiplication by (1-X)^2(1-alpha^2 X)(1-alpha^-2 X) leaves 1-X^2.
    seq = []
    for r in range(25):
        cur = {}
        for i in range(r + 1):
            for j in range(r + 1):
                weight = 2 * r - 2 * i - 2 * j
                cur[weight] = cur.get(weight, 0) + 1
        seq.append(cur)
    factors = [
        {0: 1},
        {0: -2, 2: -1, -2: -1},
        {0: 2, 2: 2, -2: 2},
        {0: -2, 2: -1, -2: -1},
        {0: 1},
    ]
    # Independent polynomial product for the four factors avoids fitted coefficients.
    ds = [{0: 1}]
    for weight in (0, 0, 2, -2):
        nxt = [{} for _ in range(len(ds) + 1)]
        for i, poly in enumerate(ds):
            for w, v in poly.items():
                nxt[i][w] = nxt[i].get(w, 0) + v
                nxt[i + 1][w + weight] = nxt[i + 1].get(w + weight, 0) - v
        ds = nxt
    need(ds == factors, "local Euler denominator expansion")
    for n in range(25):
        out = {}
        for j in range(min(4, n) + 1):
            for a, x in ds[j].items():
                for b, y in seq[n - j].items():
                    out[a + b] = out.get(a + b, 0) + x * y
        out = {w: v for w, v in out.items() if v}
        need(
            out == ({0: 1} if n == 0 else {0: -1} if n == 2 else {}),
            "local Euler factor",
        )
    return {
        "source": SOURCE,
        "arithmetic_class": "MIXED",
        "arithmetic_components": ["CERTIFIED_INTEGER_COVERAGE", "EXACT_RATIONAL"],
        "rounding": "none; integer and Fraction operations only",
        "source_bindings": len(manifest["frozen_sources"]),
        "artifact_sha256_lf": seals,
        "source_payload_sha256": wanted,
        "records": records,
        "complete_harmonic_rows": 32,
        "local_euler_orders": 25,
        "analytic_estimates_machine_certified": "no",
    }


if __name__ == "__main__":
    print(canonical(replay()).decode("ascii"), end="")
