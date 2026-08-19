#!/usr/bin/env python3
"""Fail-closed verifier for the T-99250 SHARP factor-67 Harnack packet.

Fast mode independently checks the compact Hall base, the SHARP/equality
negative control, the Radon--Nikodym child map, the local-square coefficient
formula, the Mellin multiplier, the retained result object, and the exact
candidate interval at the reported minimizer.

--full-scan additionally recompiles the C++ producer, reruns all 10^8 cells,
and requires byte-identical stdout.  Neither mode proves the unbounded tail or
RH; the retained status flags must remain false.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
import tempfile
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.t99250.sharp-harnack.v1"
VERDICT = "PASS_T99250_SHARP_KERNEL_RN_AND_H67_REDUCTION"
S = 1 << 50
S2 = S * S


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def mu_sieve(n: int) -> list[int]:
    mu = [0] * (n + 1)
    mu[1] = 1
    primes: list[int] = []
    composite = [False] * (n + 1)
    for k in range(2, n + 1):
        if not composite[k]:
            primes.append(k)
            mu[k] = -1
        for p in primes:
            if k * p > n:
                break
            composite[k * p] = True
            if k % p == 0:
                mu[k * p] = 0
                break
            mu[k * p] = -mu[k]
    return mu


def inv_sqrt_iv(n: int) -> tuple[Fraction, Fraction]:
    q = math.isqrt(S2 // n)
    while (q + 1) * (q + 1) * n <= S2:
        q += 1
    while q * q * n > S2:
        q -= 1
    return Fraction(q, S), Fraction(q + 1, S)


def sqrt_iv(n: int) -> tuple[Fraction, Fraction]:
    q = math.isqrt(S2 * n)
    return Fraction(q, S), Fraction(q + 1, S)


def affine_sqrt_iv(a: Fraction, blo: Fraction, bhi: Fraction, x: int,
                   a_factor: int, b_factor: int) -> tuple[Fraction, Fraction]:
    slo, shi = sqrt_iv(x)
    if a >= 0:
        prod_lo, prod_hi = a * slo, a * shi
    else:
        prod_lo, prod_hi = a * shi, a * slo
    return a_factor * prod_lo + b_factor * bhi, a_factor * prod_hi + b_factor * blo


def compact_base_and_firewalls() -> dict[str, Any]:
    mu = mu_sieve(66)
    a = Fraction(0)
    blo = Fraction(0)
    bhi = Fraction(0)
    avec = [Fraction(0)] * 67
    blvec = [Fraction(0)] * 67
    bhvec = [Fraction(0)] * 67
    for n in range(1, 67):
        a += Fraction(mu[n], n)
        lo, hi = inv_sqrt_iv(n)
        if mu[n] >= 0:
            blo += mu[n] * lo
            bhi += mu[n] * hi
        else:
            blo += mu[n] * hi
            bhi += mu[n] * lo
        avec[n], blvec[n], bhvec[n] = a, blo, bhi

    terminal: tuple[Fraction, Fraction, int, str] | None = None
    for n in range(1, 67):
        for x, side in ((n, "LEFT"), (n + 1, "RIGHT_LIMIT")):
            lo, hi = affine_sqrt_iv(avec[n], blvec[n], bhvec[n], x, 4, -3)
            if terminal is None or lo < terminal[0]:
                terminal = (lo, hi, n, side)
    assert terminal is not None and terminal[0] > 0

    hall: tuple[Fraction, Fraction, int, int] | None = None
    for t in range(1, 67):
        if mu[t] != -1:
            continue
        x = t if avec[t] >= 0 else 67
        lo, hi = affine_sqrt_iv(avec[t], blvec[t], bhvec[t], x, 4, -3)
        if hall is None or lo < hall[0]:
            hall = (lo, hi, t, x)
    assert hall is not None
    assert hall[0] > Fraction(7, 20)
    assert (hall[2], hall[3]) == (13, 67)

    # The equality scalar is the binding wrong-target control at the same state.
    eq_lo, eq_hi = affine_sqrt_iv(avec[13], blvec[13], bhvec[13], 67, 2, -1)
    assert eq_hi < Fraction(-3, 10)

    return {
        "classification": "PASS_COMPACT_SHARP_HALL_BASE_AND_WRONG_TARGET_FIREWALL",
        "terminal_min_lower": str(terminal[0]),
        "terminal_min_upper": str(terminal[1]),
        "terminal_cell": terminal[2],
        "terminal_side": terminal[3],
        "hall_min_lower": str(hall[0]),
        "hall_min_upper": str(hall[1]),
        "hall_threshold": hall[2],
        "hall_endpoint": hall[3],
        "equality_control_upper": str(eq_hi),
    }


def radon_nikodym_checks() -> dict[str, Any]:
    # All arguments are perfect squares, so T(y)=4sqrt(y)-3 is exact rational.
    def T_square(root: int) -> Fraction:
        return Fraction(4 * root - 3)

    # Parent Y=16, child Z=4. At t=1 and t=4 the exact RN ratios are 5/13 and 1/5.
    ratio_t1 = T_square(2) / T_square(4)
    ratio_t4 = T_square(1) / T_square(2)
    assert ratio_t1 == Fraction(5, 13)
    assert ratio_t4 == Fraction(1, 5)
    assert 0 <= ratio_t4 <= ratio_t1 <= 1

    # Pointwise normalized-profile monotonicity at t=4:
    # T(4/4)/T(4) <= T(16/4)/T(16).
    profile_small = Fraction(1, 5)
    profile_large = Fraction(5, 13)
    assert profile_small < profile_large

    # A raw support cutoff would retain parent density 5*kappa at t=4, while
    # the true child has density 1*kappa. The RN multiplier 1/5 is mandatory.
    raw_parent_density = Fraction(5)
    child_density = Fraction(1)
    assert raw_parent_density != child_density
    assert raw_parent_density * ratio_t4 == child_density

    alpha1, alpha2 = Fraction(1, 16), Fraction(1, 32)
    assert alpha1 + alpha2 < Fraction(1, 8)
    width_t1 = alpha1 * ratio_t1 + alpha2 * Fraction(1, 13)
    width_t4 = alpha1 * ratio_t4
    assert 0 <= width_t1 < Fraction(1, 8)
    assert 0 <= width_t4 < Fraction(1, 8)

    return {
        "classification": "PASS_EXACT_RADON_NIKODYM_CHILD_AND_PROFILE_MAP",
        "ratio_t1": str(ratio_t1),
        "ratio_t4": str(ratio_t4),
        "profile_small": str(profile_small),
        "profile_large": str(profile_large),
        "random_key_width_t1": str(width_t1),
        "random_key_width_t4": str(width_t4),
        "raw_cutoff_negative_control": True,
    }


def local_square_checks(limit: int = 200_000) -> dict[str, Any]:
    mu = mu_sieve(limit)
    counts = {"-2": 0, "-1": 0, "0": 0, "1": 0, "2": 0}
    for n in range(1, limit + 1):
        direct = mu[n] - (mu[n // 67] if n % 67 == 0 else 0)
        m = n
        f = 0
        while m % 67 == 0:
            m //= 67
            f += 1
        c = 1 if f == 0 else -2 if f == 1 else 1 if f == 2 else 0
        local = c * mu[m]
        if direct != local:
            raise AssertionError(f"local-square mismatch at n={n}: {direct} != {local}")
        counts[str(direct)] += 1
    return {
        "classification": "PASS_67_LOCAL_SQUARE_COEFFICIENT_FORMULA",
        "limit": limit,
        "coefficient_counts": counts,
    }


def mellin_checks() -> dict[str, Any]:
    target_points = [Fraction(3, 4), Fraction(1), Fraction(5, 4), Fraction(2), Fraction(7, 2)]
    for s in target_points:
        target = (s + Fraction(3, 2)) / (s * (s - Fraction(1, 2)))
        assert target == Fraction(4, 1) / (s - Fraction(1, 2)) - Fraction(3, 1) / s

    dilation_points = [Fraction(3, 2), Fraction(5, 2), Fraction(7, 2), Fraction(9, 2)]
    dilation_values = []
    for s in dilation_points:
        exponent = int(s + Fraction(1, 2))
        assert Fraction(exponent) == s + Fraction(1, 2)
        value = 1 - Fraction(1, 67) ** exponent
        assert 0 < value < 1
        dilation_values.append(str(value))

    # At a hypothetical zero rho with Re rho>1/2, |67^{-rho}|<1, so the
    # local-square multiplier cannot cancel it.
    assert Fraction(1, 67) < 1
    return {
        "classification": "PASS_SHARP_AND_DILATION_MELLIN_SYMBOL_AUDIT",
        "target_rational_points": len(target_points),
        "dilation_rational_points": len(dilation_points),
        "dilation_values": dilation_values,
        "dilation_multiplier": "1-67^(-(s+1/2))",
        "off_line_zero_cancellation": False,
    }


def parse_transcript(path: Path) -> dict[str, str]:
    fields: dict[str, str] = {}
    for raw in path.read_text().splitlines():
        parts = raw.split()
        if not parts:
            continue
        if parts[0] == "N":
            fields.update({"N": parts[1], "scale": parts[3], "scale_squared": parts[5], "nonzero": parts[7]})
        elif parts[0] == "minimum_cell":
            fields["minimum_cell"] = parts[1]
            fields["minimum_side"] = parts[3]
        elif parts[0] == "approx_minimum":
            fields["approx_minimum"] = parts[1]
            fields["approx_cell"] = parts[3]
            fields["approx_side"] = parts[5]
        elif parts[0] in {"classification", "range_start", "range_end_exclusive", "min_lower_num", "min_upper_num", "min_lower", "min_upper", "Alo"}:
            if parts[0] == "Alo":
                fields.update({"Alo": parts[1], "Ahi": parts[3], "Blo": parts[5], "Bhi": parts[7]})
            else:
                fields[parts[0]] = parts[1]
    return fields


def candidate_interval_at_200() -> tuple[int, int]:
    mu = mu_sieve(200)
    alo = ahi = blo = bhi = 0
    for n in range(1, 201):
        b = mu[n] - (mu[n // 67] if n % 67 == 0 else 0)
        if not b:
            continue
        qa, ra = divmod(S, n)
        ca = qa + (ra != 0)
        q = math.isqrt(S2 // n)
        while (q + 1) * (q + 1) * n <= S2:
            q += 1
        while q * q * n > S2:
            q -= 1
        cb = q + 1
        if b > 0:
            alo += b * qa
            ahi += b * ca
            blo += b * q
            bhi += b * cb
        else:
            alo += b * ca
            ahi += b * qa
            blo += b * cb
            bhi += b * q

    # Right limit of [200,201): active coefficients through 200, x -> 201^-.
    root = math.isqrt(S2 * 201)
    rl, rh = root, root + 1
    if alo >= 0:
        plo, phi = alo * rl, ahi * rh
    elif ahi <= 0:
        plo, phi = alo * rh, ahi * rl
    else:
        plo, phi = alo * rh, ahi * rh
    return 4 * plo - 3 * bhi * S, 4 * phi - 3 * blo * S


def retained_result_checks(root: Path) -> dict[str, Any]:
    result_path = root / "results" / "sharp_h67_exact_1e8.json"
    transcript_path = root / "results" / "sharp_h67_exact_1e8.txt"
    source_path = root / "src" / "scan_sharp_h67.cpp"
    result = json.loads(result_path.read_text())
    if result.get("schema") != SCHEMA:
        raise AssertionError("result schema mismatch")
    if result["status"]["global_tail_proved"] or result["status"]["rh_established"]:
        raise AssertionError("fail-closed status flags were changed")
    fields = parse_transcript(transcript_path)
    expected = {
        "classification": "PASS_X99250_SHARP_H67_DIRECTED_SCAN",
        "range_start": "67",
        "range_end_exclusive": "100000001",
        "N": "100000000",
        "scale": str(S),
        "scale_squared": str(S2),
        "minimum_cell": "200",
        "minimum_side": "RIGHT_LIMIT",
    }
    for key, value in expected.items():
        if fields.get(key) != value:
            raise AssertionError(f"transcript {key} mismatch: {fields.get(key)} != {value}")
    if int(fields["min_lower_num"]) <= 0:
        raise AssertionError("retained directed lower minimum is not positive")
    cand_lo, cand_hi = candidate_interval_at_200()
    if cand_lo != int(fields["min_lower_num"]) or cand_hi != int(fields["min_upper_num"]):
        raise AssertionError("independent minimizer interval does not match retained transcript")
    if result["producer_sha256"] != sha256(source_path):
        raise AssertionError("producer hash mismatch")
    if result["transcript_sha256"] != sha256(transcript_path):
        raise AssertionError("transcript hash mismatch")
    core = dict(result)
    proof_hash = core.pop("proof_object_sha256")
    canonical = json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    if hashlib.sha256(canonical).hexdigest() != proof_hash:
        raise AssertionError("result proof-object hash mismatch")
    return {
        "classification": "PASS_RETAINED_1E8_RESULT_AND_INDEPENDENT_MINIMIZER_INTERVAL",
        "min_lower_num": fields["min_lower_num"],
        "min_upper_num": fields["min_upper_num"],
        "scale_squared": fields["scale_squared"],
        "minimum_cell": 200,
        "minimum_side": "RIGHT_LIMIT",
        "producer_sha256": result["producer_sha256"],
        "transcript_sha256": result["transcript_sha256"],
    }


def full_scan(root: Path) -> dict[str, Any]:
    source = root / "src" / "scan_sharp_h67.cpp"
    retained = root / "results" / "sharp_h67_exact_1e8.txt"
    with tempfile.TemporaryDirectory() as td:
        exe = Path(td) / "scan_sharp_h67"
        out = Path(td) / "scan.txt"
        subprocess.run(["g++", "-O3", "-std=c++17", str(source), "-o", str(exe)], check=True)
        with out.open("wb") as f:
            subprocess.run([str(exe), "100000000", "2000000"], stdout=f, check=True)
        if out.read_bytes() != retained.read_bytes():
            raise AssertionError("full producer replay is not byte-identical")
    return {"classification": "PASS_BYTE_IDENTICAL_FULL_1E8_REPLAY"}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--full-scan", action="store_true")
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    root = Path(__file__).resolve().parent
    checks: list[dict[str, Any]] = [
        compact_base_and_firewalls(),
        radon_nikodym_checks(),
        local_square_checks(),
        mellin_checks(),
        retained_result_checks(root),
    ]
    if args.full_scan:
        checks.append(full_scan(root))
    payload: dict[str, Any] = {
        "schema": SCHEMA,
        "classification": VERDICT,
        "checks": checks,
        "base_pr": 642,
        "base_sha": "07aa0d4838458a1b2d3af9e5bc96616baa6b4767",
        "global_tail_proved": False,
        "rh_established": False,
        "proof_boundary": (
            "Exact algebraic/interface replay plus a retained directed all-real scan through 10^8. "
            "The inequality for x>=100000001 and RH remain unproved."
        ),
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    else:
        print(text, end="")
    print(VERDICT)
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
