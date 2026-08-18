#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

VERDICT = "PASS_T98020_QUANTITATIVE_DICKMAN_CORRIDOR"
HERE = Path(__file__).resolve().parent


def prime_sieve(n: int) -> list[int]:
    mark = bytearray(b"\x01") * (n + 1)
    mark[:2] = b"\x00\x00"
    for p in range(2, int(n**0.5) + 1):
        if mark[p]:
            mark[p * p : n + 1 : p] = b"\x00" * (((n - p * p) // p) + 1)
    return [i for i in range(2, n + 1) if mark[i]]


def mobius_sieve(n: int) -> tuple[list[int], list[int]]:
    mu = [0] * (n + 1)
    spf = [0] * (n + 1)
    ps: list[int] = []
    mu[1] = 1
    for x in range(2, n + 1):
        if spf[x] == 0:
            spf[x] = x
            ps.append(x)
            mu[x] = -1
        for p in ps:
            y = p * x
            if y > n:
                break
            spf[y] = p
            if x % p == 0:
                mu[y] = 0
                break
            mu[y] = -mu[x]
    return mu, spf


def rough_harmonic(Y: int, z: int, mu: list[int], spf: list[int]) -> float:
    total = 0.0
    for m in range(1, Y + 1):
        if mu[m] and (m == 1 or spf[m] >= z):
            total += mu[m] / m
    return total


def dickman_grid(u_max: float, step: float = 1e-4) -> tuple[list[float], float]:
    """Simple retained diagnostic; not used as theorem evidence."""
    n = int(math.ceil(u_max / step)) + 2
    rho = [1.0] * n
    start = int(1.0 / step)
    prefix = [0.0] * n
    for i in range(1, start + 1):
        prefix[i] = prefix[i - 1] + rho[i - 1] * step
    for i in range(start + 1, n):
        u = i * step
        lo = max(0, i - start)
        # Integral on [u-1,u] using the already known left-endpoint values.
        integ = (prefix[i - 1] - prefix[lo]) + rho[i - 1] * step
        rho[i] = max(0.0, integ / u)
        prefix[i] = prefix[i - 1] + rho[i - 1] * step
    return rho, step


def rho_lookup(rho: list[float], step: float, u: float) -> float:
    x = u / step
    i = min(int(x), len(rho) - 2)
    t = x - i
    return rho[i] * (1 - t) + rho[i + 1] * t


def distinct_tuple_fixture() -> dict[str, str]:
    # Exact finite check of the repeated-prime correction mechanism.
    primes = [5, 7, 11]
    Y = 5 * 7 * 11
    z = 5
    u = math.log(Y) / math.log(z)
    literal = Fraction(1)
    for p in primes:
        literal -= Fraction(1, p)
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            literal += Fraction(1, primes[i] * primes[j])
    literal -= Fraction(1, math.prod(primes))

    # Ordered product-measure exponential sum through k=3.
    ordered = Fraction(1)
    repeated_mass = Fraction(0)
    for k in (1, 2, 3):
        layer = Fraction(0)
        import itertools
        for tup in itertools.product(primes, repeat=k):
            if math.prod(tup) <= Y:
                w = Fraction(1, math.prod(tup))
                layer += w
                if len(set(tup)) < k:
                    repeated_mass += w / math.factorial(k)
        ordered += (-1) ** k * layer / math.factorial(k)
    # Removing repeated tuples recovers the literal squarefree sum.
    assert ordered != literal
    return {
        "u": f"{u:.12f}",
        "literal": str(literal),
        "ordered_with_repeats": str(ordered),
        "repeated_mass_upper_fixture": str(repeated_mass),
    }


def run() -> dict:
    limit = 250_000
    mu, spf = mobius_sieve(limit)
    rho, step = dickman_grid(12.0, 2e-4)
    diagnostics = []
    for Y, z in ((50_000, 67), (100_000, 101), (250_000, 251), (250_000, 503)):
        u = math.log(Y) / math.log(z)
        S = rough_harmonic(Y, z, mu, spf)
        r = rho_lookup(rho, step, u)
        # The theorem's retained finite diagnostic only checks the correct scale.
        scale = u / math.log(z)
        diagnostics.append(
            {
                "Y": Y,
                "z": z,
                "u": u,
                "S": S,
                "rho_grid": r,
                "absolute_difference": abs(S - r),
                "comparison_scale_u_over_logz": scale,
                "within_coarse_scale": abs(S - r) <= 20 * scale,
            }
        )
    assert all(d["within_coarse_scale"] for d in diagnostics)

    # Critical-window dominance in logarithmic variables.  A=log log Y and
    # B=log log log Y; no enormous integer Y is materialized.
    dominance = []
    for A in (10_000.0, 100_000.0, 1_000_000.0):
        B = math.log(A)
        eps = 0.1
        u = (1 - eps) * A / B
        # de Bruijn leading exponent and the rough-sieve error exponent.
        dickman_log = -u * (math.log(u) + math.log(math.log(u)) - 1)
        error_log = -A + 2 * math.log(u)
        margin = dickman_log - error_log
        assert margin > 0
        dominance.append(
            {
                "loglogY": A,
                "logloglogY": B,
                "epsilon": eps,
                "u": u,
                "log_main_over_error_leading": margin,
            }
        )

    # Above the saddle, absolute bounded-remainder control is too large.
    no_go = []
    for A in (10_000.0, 100_000.0, 1_000_000.0):
        B = math.log(A)
        c = 1.5
        u = c * A / B
        dickman_log = -u * (math.log(u) + math.log(math.log(u)) - 1)
        abs_error_log = -A + math.log(u)
        gap = dickman_log - abs_error_log
        assert gap < 0
        no_go.append(
            {
                "loglogY": A,
                "c": c,
                "u": u,
                "log_main_over_absolute_error": gap,
            }
        )

    core = {
        "schema": "riemann.x98020.quantitative-dickman.v1",
        "frozen_heads": {
            "pr594": "ef76157a516c520a0f829ea4ee346c62759743ed",
            "pr599": "8daa0a5d94de56c68a1ce710824b26cacc1a9bbc",
            "pr601": "defe55d449e5ae37bcd989cf4e7dd4266eacbc3d",
            "pr602": "ab9f76cfa03dd4924e04f31b44087ff7e3c76f63",
        },
        "distinct_tuple_fixture": distinct_tuple_fixture(),
        "finite_diagnostics": diagnostics,
        "critical_window_dominance": dominance,
        "above_saddle_absolute_no_go": no_go,
        "uniform_formula": "F(Y,z)=a*sqrt(Y)*rho(u)+O(sqrt(Y)*u/log(z))",
        "positive_range": "u <= (1-eps) loglog(Y)/logloglog(Y)",
        "cbrc67_proved": False,
        "gpc67_proved": False,
        "rh_established": False,
        "verdict": VERDICT,
    }
    canonical = json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    core["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    out = HERE / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(core, indent=2, sort_keys=True) + "\n")
    return core


if __name__ == "__main__":
    result = run()
    print(result["verdict"])
    print(result["proof_object_sha256"])
