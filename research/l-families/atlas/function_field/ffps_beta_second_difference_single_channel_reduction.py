#!/usr/bin/env python3
"""Bounded exact replay for the beta second-difference source reduction.

The replay authenticates finite source and primitive-panel algebra only.  It
does not prove COREWAVE, COREAGG, PRIMCAR, PRIMLS, RH, or GRH.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from dataclasses import dataclass
from fractions import Fraction
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
NOTE_PATH = HERE / "FFPS_BETA_SECOND_DIFFERENCE_SINGLE_CHANNEL_REDUCTION.md"
SOURCE_COMMIT = "3a595dda92ef827a41e50d2395309692a93748ad"
SOURCE_BLOBS = {
    (
        "research/l-families/atlas/function_field/"
        "FFPS_BOUNDARY_FIELD_NEAR_CORRELATION_CRITERION.md"
    ): "105837343b6b8ef148488f492c66da8feae0334a",
    (
        "research/l-families/atlas/function_field/"
        "FFPS_BOUNDARY_FIELD_PRIMITIVE_PAIR_LARGE_SIEVE_GATE.md"
    ): "2abd49b975837c924009e33912e786b4b720e29c",
    (
        "research/l-families/atlas/function_field/"
        "FFPS_PRIMITIVE_CORE_WAVELET_CLOSURE.md"
    ): "af735a493a5c74b7158c314079dbf4b72ee11b46",
    (
        "research/l-families/atlas/function_field/"
        "FFPS_HIGH_GCD_PRINCIPAL_FREQUENCY_IDENTITY.md"
    ): "5a14ad1f04cd26a17d202d24f6086bccf9976b85",
}
Q = 67
SOURCE_COEFFICIENTS = (1, -2, 1)
BASE_CAP = 30
CENTRAL_REPLAY_CAP = 90


def check_source_blobs() -> None:
    """Authenticate the exact PR #760 statements extended by this packet."""
    for path, expected in SOURCE_BLOBS.items():
        frozen = subprocess.run(
            ["git", "rev-parse", f"{SOURCE_COMMIT}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=5,
        ).stdout.strip()
        if frozen != expected:
            raise RuntimeError(f"frozen source blob mismatch: {path}")
        working = subprocess.run(
            ["git", "hash-object", path],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=5,
        ).stdout.strip()
        if working != expected:
            raise RuntimeError(f"working source blob mismatch: {path}")


def check_scope_markers() -> None:
    raw = NOTE_PATH.read_bytes().replace(b"\r\n", b"\n")
    if any(byte < 32 and byte not in (9, 10) for byte in raw):
        raise RuntimeError("note contains an unexpected control byte")
    note = NOTE_PATH.read_text(encoding="utf-8")
    for marker in (
        "second multiplicative difference",
        "exact finite inverse",
        "single-channel assembled criterion",
        "positive gates are **not necessary",
        "The half-weight is load-bearing",
        "No COREWAVE, COREAGG, PRIMCAR, PRIMLS, RH, or GRH estimate is proved",
    ):
        if marker not in note:
            raise RuntimeError(f"scope marker missing: {marker}")


def mobius(n: int) -> int:
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    remaining = n
    prime = 2
    sign = 1
    while prime * prime <= remaining:
        if remaining % prime == 0:
            remaining //= prime
            sign = -sign
            if remaining % prime == 0:
                return 0
            while remaining % prime == 0:
                remaining //= prime
        prime = 3 if prime == 2 else prime + 2
    if remaining > 1:
        sign = -sign
    return sign


def qfree_mobius(n: int, q: int) -> int:
    return 0 if n % q == 0 else mobius(n)


def beta_source(n: int, q: int) -> int:
    return mobius(n) - (mobius(n // q) if n % q == 0 else 0)


def second_difference_source(n: int, q: int) -> int:
    value = qfree_mobius(n, q)
    if n % q == 0:
        value -= 2 * qfree_mobius(n // q, q)
    if n % (q * q) == 0:
        value += qfree_mobius(n // (q * q), q)
    return value


def source_replay(q: int) -> dict[str, object]:
    probes = set(range(1, 3 * q + 5))
    for base in (1, 2, 3, 5, 6, 10, 30):
        if base % q:
            for exponent in range(5):
                probes.add(base * q**exponent)
    for n in sorted(probes):
        if beta_source(n, q) != second_difference_source(n, q):
            raise ArithmeticError(f"source factorization failed at q={q}, n={n}")
    local_rows = []
    for exponent in range(5):
        n = q**exponent
        local_rows.append(
            {
                "q_adic_exponent": exponent,
                "beta": beta_source(n, q),
                "second_difference": second_difference_source(n, q),
            }
        )
    return {
        "q": q,
        "probe_count": len(probes),
        "identity": "beta_q=(delta_1-delta_q)^2*mu_qfree",
        "local_rows": local_rows,
    }


FormalField = dict[tuple[int, int], int]


def add_formal(target: FormalField, key: tuple[int, int], value: int) -> None:
    if not value:
        return
    target[key] = target.get(key, 0) + value
    if not target[key]:
        del target[key]


def replay_bases(q: int) -> tuple[int, ...]:
    return tuple(
        n for n in range(1, BASE_CAP + 1) if n % q and qfree_mobius(n, q)
    )


def u_formal_field(horizon: int, q: int) -> FormalField:
    return {
        (base, 0): qfree_mobius(base, q)
        for base in replay_bases(q)
        if base <= horizon
    }


def g_formal_field(horizon: int, q: int) -> FormalField:
    result: FormalField = {}
    for base in replay_bases(q):
        base_coefficient = qfree_mobius(base, q)
        for exponent, coefficient in enumerate(SOURCE_COEFFICIENTS):
            if base * q**exponent <= horizon:
                add_formal(
                    result,
                    (base, exponent),
                    coefficient * base_coefficient,
                )
    return result


def forward_from_u(horizon: int, q: int) -> FormalField:
    result: FormalField = {}
    for exponent, coefficient in enumerate(SOURCE_COEFFICIENTS):
        shifted = u_formal_field(horizon // q**exponent, q)
        for (base, zero_shift), base_coefficient in shifted.items():
            if zero_shift != 0:
                raise AssertionError("unexpected base shift")
            add_formal(
                result,
                (base, exponent),
                coefficient * base_coefficient,
            )
    return result


def inverse_from_g(horizon: int, q: int) -> FormalField:
    result: FormalField = {}
    q_power = 1
    shift = 0
    while q_power <= horizon:
        field = g_formal_field(horizon // q_power, q)
        for (base, local_shift), coefficient in field.items():
            add_formal(
                result,
                (base, shift + local_shift),
                (shift + 1) * coefficient,
            )
        shift += 1
        q_power *= q
    return result


def formal_digest(field: FormalField) -> str:
    payload = json.dumps(
        [[base, shift, value] for (base, shift), value in sorted(field.items())],
        separators=(",", ":"),
    )
    return hashlib.sha256(payload.encode("ascii")).hexdigest()


def prefix_transform_replay(q: int) -> dict[str, object]:
    rows = []
    for level in range(5):
        horizon = BASE_CAP * q**level
        direct_g = g_formal_field(horizon, q)
        forward = forward_from_u(horizon, q)
        inverse = inverse_from_g(horizon, q)
        target_u = u_formal_field(horizon, q)
        if direct_g != forward:
            raise ArithmeticError("sharp-prefix forward transform failed")
        if inverse != target_u:
            raise ArithmeticError("sharp-prefix inverse transform failed")
        rows.append(
            {
                "q_adic_horizon_level": level,
                "formal_beta_atoms": len(direct_g),
                "formal_u_atoms": len(target_u),
                "beta_digest": formal_digest(direct_g),
                "inverse_digest": formal_digest(inverse),
            }
        )
    convolution = []
    for shift in range(13):
        value = sum(
            SOURCE_COEFFICIENTS[local] * (shift - local + 1)
            for local in range(min(2, shift) + 1)
        )
        expected = 1 if shift == 0 else 0
        if value != expected:
            raise ArithmeticError("inverse coefficient convolution failed")
        convolution.append(value)
    return {
        "q": q,
        "identity": "G=(I-q^(-1/2)S)^2 U",
        "inverse": "U=sum_(j>=0)(j+1)q^(-j/2)S^j G; finite at each prefix",
        "rows": rows,
        "inverse_convolution_first_13": convolution,
    }


@dataclass(frozen=True)
class Quadratic:
    """An exact element rational + root*sqrt(Q)."""

    rational: Fraction = Fraction()
    root: Fraction = Fraction()

    def __add__(self, other: Quadratic) -> Quadratic:
        return Quadratic(self.rational + other.rational, self.root + other.root)

    def __sub__(self, other: Quadratic) -> Quadratic:
        return Quadratic(self.rational - other.rational, self.root - other.root)

    def __mul__(self, other: Quadratic) -> Quadratic:
        return Quadratic(
            self.rational * other.rational + Q * self.root * other.root,
            self.rational * other.root + self.root * other.rational,
        )

    def render(self) -> dict[str, str]:
        return {"rational": str(self.rational), "sqrt_67": str(self.root)}


def conditioning_replay() -> dict[str, object]:
    one = Quadratic(Fraction(1))
    inv_sqrt_q = Quadratic(root=Fraction(1, Q))
    lower_amplitude = (one - inv_sqrt_q) * (one - inv_sqrt_q)
    upper_amplitude = (one + inv_sqrt_q) * (one + inv_sqrt_q)
    lower_energy = lower_amplitude * lower_amplitude
    upper_energy = upper_amplitude * upper_amplitude
    inverse_coefficients = [
        {"j": j, "coefficient": f"{j + 1}*67^(-{j}/2)"} for j in range(8)
    ]
    return {
        "frequency_symbol": "h(theta)=(1-67^(-1/2) exp(-i theta log 67))^2",
        "amplitude_annulus": {
            "lower": lower_amplitude.render(),
            "upper": upper_amplitude.render(),
        },
        "energy_annulus": {
            "lower": lower_energy.render(),
            "upper": upper_energy.render(),
        },
        "maximal_norm_conditioning": (
            "(1-67^(-1/2))^2 M_U <= M_G <= "
            "(1+67^(-1/2))^2 M_U"
        ),
        "inverse_coefficients": inverse_coefficients,
        "sigma_phase_boundary": (
            "sum_j (j+1)67^(-j sigma) converges exactly for sigma>0; "
            "at sigma=0 the symbol vanishes at theta=0"
        ),
    }


def is_squarefree(n: int) -> bool:
    return mobius(n) != 0


def toy_kernel(a: int, b: int) -> Fraction:
    small, large = sorted((a, b))
    if large > 16 * small:
        return Fraction()
    return Fraction(16 * small - large + 1, 16 * large)


Radical = dict[int, Fraction]


def add_radical(target: Radical, radicand: int, coefficient: Fraction) -> None:
    if not coefficient:
        return
    target[radicand] = target.get(radicand, Fraction()) + coefficient
    if not target[radicand]:
        del target[radicand]


def normalized_pair_term(a: int, b: int, scale: int = 1) -> tuple[int, Fraction]:
    radicand = a * b
    return radicand, Fraction(mobius(a) * mobius(b), scale * radicand)


def direct_central_shell(x: int, h: int, q: int) -> Radical:
    result: Radical = {}
    eligible = [n for n in range(1, x + 1) if n % q and is_squarefree(n)]
    for m in eligible:
        for n in eligible:
            if m == n:
                continue
            d = gcd(m, n)
            a, b = m // d, n // d
            if not (h < max(a, b) <= 2 * h):
                continue
            weight = toy_kernel(a, b)
            radicand, coefficient = normalized_pair_term(a, b, d)
            add_radical(result, radicand, coefficient * weight)
    return result


def assembled_central_shell(x: int, h: int, q: int) -> Radical:
    result: Radical = {}
    for d in range(1, x // h + 1):
        if d % q == 0 or not is_squarefree(d):
            continue
        upper = min(2 * h, x // d)
        for a in range(1, upper + 1):
            if a % q == 0 or not is_squarefree(a) or gcd(a, d) != 1:
                continue
            for b in range(1, upper + 1):
                if (
                    b % q == 0
                    or not is_squarefree(b)
                    or gcd(b, d) != 1
                    or gcd(a, b) != 1
                    or a == b
                    or not (h < max(a, b) <= upper)
                ):
                    continue
                weight = toy_kernel(a, b)
                radicand, coefficient = normalized_pair_term(a, b, d)
                add_radical(result, radicand, coefficient * weight)
    return result


def radical_summary(value: Radical) -> dict[str, object]:
    rendered = {str(k): str(v) for k, v in sorted(value.items())}
    payload = json.dumps(rendered, separators=(",", ":"), sort_keys=True)
    return {
        "radical_terms": len(rendered),
        "sha256": hashlib.sha256(payload.encode("ascii")).hexdigest(),
        "rational_component": rendered.get("1", "0"),
    }


def central_panel_replay() -> dict[str, object]:
    rows = []
    for h in (1, 2, 4, 8, 16, 32):
        direct = direct_central_shell(CENTRAL_REPLAY_CAP, h, Q)
        assembled = assembled_central_shell(CENTRAL_REPLAY_CAP, h, Q)
        if direct != assembled:
            raise ArithmeticError(f"central common-factor reassembly failed at H={h}")
        rows.append({"H": h, **radical_summary(direct)})
    return {
        "identity": (
            "S_H^U(X)=sum_(d<=X/H,sf,67-free) d^-1 "
            "P_0(d;H,min(2H,X/d))"
        ),
        "X": CENTRAL_REPLAY_CAP,
        "kernel": "symmetric rational ratio-16 toy kernel",
        "rows": rows,
    }


def run(*, check_sources: bool = True) -> dict[str, object]:
    if type(check_sources) is not bool:
        raise TypeError("check_sources must be Boolean")
    if check_sources:
        check_source_blobs()
    check_scope_markers()
    return {
        "architecture": "A: assembled beta / primitive core-wavelet route",
        "exact_theorems": {
            "source_second_difference": True,
            "sharp_prefix_forward_and_inverse": True,
            "uniform_maximal_norm_conditioning": True,
            "beta_energy_equivalent_to_67free_energy": (
                "proved at the all-positive-exponent scale"
            ),
            "single_channel_assembled_equivalent_to_rh": (
                "proved using the frozen beta boundary criterion"
            ),
            "central_gate_chain": (
                "COREWAVE_0 -> COREAGG_0 <=> PRIMCAR_0 -> PRIMLS_0 -> RH"
            ),
        },
        "source_replay": [source_replay(5), source_replay(Q)],
        "prefix_transform_replay": prefix_transform_replay(Q),
        "conditioning_replay": conditioning_replay(),
        "central_panel_replay": central_panel_replay(),
        "scope_firewall": {
            "central_assembled_estimate_proved": False,
            "central_corewave_proved": False,
            "central_coreagg_proved": False,
            "central_primcar_proved": False,
            "central_primls_proved": False,
            "exceptional_positive_gates_shown_unnecessary_for_sufficiency": True,
            "exceptional_positive_gates_implied_by_central_gate": False,
            "rh_or_grh_proved": False,
            "architecture_b_claims": False,
            "same_prefix_fourier_multiplier_identity_claimed": False,
        },
        "source_contract": {
            "commit": SOURCE_COMMIT,
            "git_blobs": SOURCE_BLOBS,
            "frozen_and_working_sources_authenticated": check_sources,
            "current_artifacts_sha256_lf": {
                str(path.relative_to(ROOT)).replace("\\", "/"): hashlib.sha256(
                    path.read_bytes().replace(b"\r\n", b"\n")
                ).hexdigest()
                for path in (
                    NOTE_PATH,
                    Path(__file__).resolve(),
                    ROOT / "tests/test_ffps_beta_second_difference_single_channel_reduction.py",
                )
            },
        },
        "resource_caps": {
            "source_probe_q_values": [5, Q],
            "formal_base_cap": BASE_CAP,
            "central_panel_X": CENTRAL_REPLAY_CAP,
            "zeta_zeros": 0,
            "primes_scanned": 0,
            "finite_fields": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--no-source-lock", action="store_true")
    parser.add_argument("--write-json", type=Path)
    args = parser.parse_args()
    if args.check and args.no_source_lock:
        parser.error("authoritative --check requires source authentication")
    rendered = json.dumps(
        run(check_sources=not args.no_source_lock), indent=2, sort_keys=True
    ) + "\n"
    canonical = Path(__file__).with_suffix(".json")
    if args.check and (
        not canonical.exists() or canonical.read_text(encoding="utf-8") != rendered
    ):
        raise SystemExit("canonical JSON fixture is stale")
    if args.write_json:
        args.write_json.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
