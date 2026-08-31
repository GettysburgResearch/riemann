"""Preregistered high-precision reconnaissance of the unresolved four-node chamber."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import subprocess
import time
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PREREG = HERE / "FOUR_NODE_SAFE_AXIS_SCOUT_PREREGISTRATION.md"
ARTIFACT = HERE / "four_node_safe_axis_scout.json"
TEST = ROOT / "tests/test_architecture_e_pass_safe_axis_scout.py"
MAX_BYTES = 8_000_000
PINS = (
    (
        "686df46fab25eadfc4564808f036e2b4fc1e4b3e",
        "research/riemann-structures/native-five-hour-pass/architecture-e/FOUR_NODE_HIGH_AXIS.md",
        "39509c6babd3f943e986805946e7f02ea4cc7285",
    ),
    (
        "9421846721cd788ab01615c8b6d459d9de849df7",
        "research/integrated/xi_pick/ORDER_THREE_CANONICAL.md",
        "f16e936294172dc272e67edcdffc822ba6edf5e6",
    ),
)
GRID = (
    Q(1, 2),
    Q(9, 16),
    Q(3, 4),
    Q(1),
    Q(3, 2),
    Q(2),
    Q(3),
    Q(4),
    Q(6),
    Q(8),
    Q(12),
    Q(16),
    Q(24),
    Q(32),
    Q(48),
    Q(64),
)
CENTERS = (Q(1, 2), Q(1), Q(2), Q(4), Q(8), Q(16), Q(32))
PAIR_CENTERS = (*CENTERS, Q(64))
KS_SINGLE = (8, 16, 24, 32)
KS_PAIR = (12, 24, 32)


def need(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def blob_id(raw):
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


def strict_json(raw):
    need(type(raw) is str and len(raw.encode()) <= MAX_BYTES, "JSON byte cap")

    def unique(pairs):
        result = {}
        for key, value in pairs:
            need(key not in result, "duplicate JSON key")
            result[key] = value
        return result

    def refuse(_):
        raise ValueError("floating/nonfinite JSON token")

    return json.loads(
        raw, object_pairs_hook=unique, parse_float=refuse, parse_constant=refuse
    )


def authenticate():
    records = []
    for commit, path, blob in PINS:
        raw = subprocess.check_output(
            ["git", "cat-file", "blob", f"{commit}:{path}"], cwd=ROOT
        )
        need(len(raw) < 1_000_000 and blob_id(raw) == blob, "source pin mismatch")
        records.append(
            {
                "commit": commit,
                "path": path,
                "blob": blob,
                "sha256": hashlib.sha256(raw).hexdigest(),
            }
        )
    return records


def packets():
    result = set(itertools.combinations(GRID, 4))
    for c in CENTERS:
        for k in KS_SINGLE:
            step = Q(1, 2**k)
            panel = tuple(c + j * step for j in range(4))
            if panel[-1] <= 64:
                result.add(panel)
    for c, d in itertools.combinations(PAIR_CENTERS, 2):
        for k in KS_PAIR:
            step = Q(1, 2**k)
            panel = (c, c + step, d, d + step)
            if panel[-1] <= 64:
                result.add(panel)
    return tuple(sorted(result))


def qstr(x):
    return f"{x.numerator}/{x.denominator}"


def mval(x):
    return mp.mpf(x.numerator) / x.denominator


@lru_cache(maxsize=1024)
def fvalue(numerator, denominator, dps):
    x = Q(numerator, denominator)
    with mp.workdps(dps):
        if x == Q(1, 2):
            return 1 + mp.euler / 2 - mp.log(4 * mp.pi) / 2
        s = mval(x) + mp.mpf("0.5")
        return (
            1 / s
            + 1 / (s - 1)
            - mp.log(mp.pi) / 2
            + mp.digamma(s / 2) / 2
            + mp.diff(mp.zeta, s) / mp.zeta(s)
        )


def matrices(panel, dps):
    values = [fvalue(x.numerator, x.denominator, dps) for x in panel]
    h = mp.matrix(4)
    c = mp.matrix(4)
    for i in range(4):
        for j in range(4):
            denominator = mval(panel[i] + panel[j])
            h[i, j] = (values[i] + values[j]) / denominator
            c[i, j] = 1 / denominator
    return h, c


def spectral(panel, dps):
    with mp.workdps(dps):
        h, c = matrices(panel, dps)
        l = mp.cholesky(c)
        inv = mp.inverse(l)
        normalized = inv * h * inv.T
        values = mp.eigsy(normalized, eigvals_only=True)
        ce = mp.eigsy(c, eigvals_only=True)
        minimum = values[0]
        condition = ce[-1] / ce[0]
        digits = 80 if dps == 100 else 120
        return {
            "minimum": mp.nstr(minimum, digits),
            "condition_C": mp.nstr(condition, digits),
            "H": [[mp.nstr(h[i, j], digits) for j in range(4)] for i in range(4)],
            "C": [[mp.nstr(c[i, j], digits) for j in range(4)] for i in range(4)],
        }


def confluent_control(dps):
    with mp.workdps(dps):
        x = mp.mpf(256)
        n = mp.matrix(4)
        for i in range(4):
            for j in range(4):
                n[i, j] = 0 if i == j else (512 if i < j else 0)
        fa = mp.matrix(4)
        power = mp.eye(4)
        for k in range(4):
            derivative = mp.diff(lambda z: fvalue_mp(z), x, k)
            fa += derivative / mp.factorial(k) * power
            power = power * n
        hermitian = fa + fa.T
        values = mp.eigsy(hermitian, eigvals_only=True)
        return mp.nstr(values[0], 80)


def fvalue_mp(x):
    s = x + mp.mpf("0.5")
    return (
        1 / s
        + 1 / (s - 1)
        - mp.log(mp.pi) / 2
        + mp.digamma(s / 2) / 2
        + mp.diff(mp.zeta, s) / mp.zeta(s)
    )


def build():
    sources = authenticate()
    panels = packets()
    need(len(panels) == 1911, "registered panel census changed")
    rows = []
    for panel in panels:
        record = spectral(panel, 100)
        record["nodes"] = [qstr(x) for x in panel]
        rows.append(record)
    order = sorted(range(len(rows)), key=lambda i: mp.mpf(rows[i]["minimum"]))[:24]
    finalists = []
    stable = True
    for i in order:
        rerun = spectral(panels[i], 200)
        a = mp.mpf(rows[i]["minimum"])
        b = mp.mpf(rerun["minimum"])
        agrees = abs(a - b) <= mp.mpf("1e-60") * max(1, abs(b))
        stable &= agrees
        finalists.append(
            {
                "index": i,
                "nodes": rows[i]["nodes"],
                "minimum_100": rows[i]["minimum"],
                "minimum_200": rerun["minimum"],
                "agrees_60_digits": agrees,
            }
        )
    values = [mp.mpf(row["minimum"]) for row in rows]
    if not stable or any(abs(v) <= mp.mpf("1e-50") for v in values):
        status = "PRECISION_UNRESOLVED"
    elif any(v < -mp.mpf("1e-50") for v in values):
        status = "NEGATIVE_SCOUT"
    else:
        status = "POSITIVE_ON_REGISTERED_GRID"
    high = spectral((Q(256), Q(257), Q(300), Q(1024)), 100)
    result = {
        "schema": "architecture-e-safe-axis-scout-v1",
        "status": status,
        "sources": sources,
        "preregistration_sha256": hashlib.sha256(PREREG.read_bytes()).hexdigest(),
        "producer_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "test_sha256": hashlib.sha256(TEST.read_bytes()).hexdigest(),
        "panel_count": len(rows),
        "panels": rows,
        "finalists": finalists,
        "high_control": dict(high, nodes=["256", "257", "300", "1024"]),
        "full_confluence_256_source_basis_minimum": confluent_control(100),
        "scope": {
            "continuum_theorem_inferred": False,
            "xi_zero_census_used": False,
            "adaptive_grid_used": False,
            "bounded_reconnaissance_only": True,
        },
    }
    result["proof_sha256"] = hashlib.sha256(
        json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    text = json.dumps(result, sort_keys=True, indent=2) + "\n"
    need(len(text.encode()) <= MAX_BYTES, "artifact byte cap")
    return result, text


def main():
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    started = time.monotonic()
    result, text = build()
    if args.write:
        ARTIFACT.write_text(text, encoding="utf-8")
    else:
        candidate = strict_json(ARTIFACT.read_text(encoding="utf-8"))
        need(
            canonical(candidate) == canonical(result),
            "fresh scout reconstruction mismatch",
        )
    print(
        json.dumps(
            {
                "status": result["status"],
                "panels": result["panel_count"],
                "minimum": result["finalists"][0]["minimum_200"],
                "proof_sha256": result["proof_sha256"],
                "elapsed_seconds": round(time.monotonic() - started, 3),
            }
        )
    )


if __name__ == "__main__":
    main()
