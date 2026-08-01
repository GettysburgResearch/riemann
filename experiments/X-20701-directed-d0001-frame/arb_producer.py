#!/usr/bin/env python3
"""Directed producer for the first actual zeta-data conditional-frame ladder.

The primitive operator is the cutoff-free D-0001 / X-0001 Weil block.  Every
prime power q <= c is included.  Pole and archimedean entries use the released
cutoff-free digamma/polygamma formulas, with explicit geometric-tail balls.

For this first production ladder N=1, so the even packet has dimension two.
A frozen dyadic near-kernel direction r and its exact orthogonal complement w
are conditioned by the first two certified critical-line zeta zeros:

    Z = {gamma_1},   Y = {gamma_2}.

The producer emits only outward Arb intervals and exact integer provenance.  A
standard-library checker reconstructs the graph, conditional frame, joint
Schur-corrected residual, and all strict signs.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import math
import platform
from pathlib import Path
from typing import Any, Iterable, Sequence

from flint import acb, acb_series, arb, ctx

SCHEMA = "riemann.x20701.d0001-frame.balls.v1"


class ProducerError(RuntimeError):
    pass


def parse_int(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise ProducerError(f"{name} must not be bool")
    try:
        return int(value)
    except (TypeError, ValueError) as exc:
        raise ProducerError(f"{name} must be an integer") from exc


def exact_binary_json(value: arb) -> dict[str, str | int]:
    mantissa, exponent = value.man_exp()
    return {"mantissa": str(int(mantissa)), "exponent": int(exponent)}


def arb_interval_json(value: arb) -> dict[str, object]:
    return {
        "lower": exact_binary_json(value.lower()),
        "upper": exact_binary_json(value.upper()),
    }


def canonical_digest(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def unique_integer(value: arb, name: str) -> int:
    integer = value.unique_fmpz()
    if integer is None:
        raise ProducerError(f"{name} was not isolated as an integer: {value}")
    return int(integer)


def primes_up_to(limit: int) -> list[int]:
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
    return [p for p in range(2, limit + 1) if sieve[p]]


def prime_powers_up_to(limit: int) -> list[tuple[int, int]]:
    out: list[tuple[int, int]] = []
    for p in primes_up_to(limit):
        q = p
        while q <= limit:
            out.append((q, p))
            if q > limit // p:
                break
            q *= p
    out.sort()
    return out


def zero_ball(radius: arb) -> arb:
    return arb(0, radius.upper())


def series_constant(series: acb_series) -> acb:
    coefficients = series.coeffs()
    return coefficients[0] if coefficients else acb(0)


def psi_and_psi1(z: acb) -> tuple[acb, acb]:
    """Compute psi(z) and psi'(z) from a rigorous gamma series."""
    x = acb_series([z, 1], prec=4)
    gamma = x.gamma()
    psi_series = gamma.derivative() / gamma
    coefficients = psi_series.coeffs()
    if len(coefficients) < 2:
        raise ProducerError("gamma-series cap did not produce psi and psi-prime")
    return coefficients[0], coefficients[1]


def geometric_sums(n: int, L: arb, tail_bits: int) -> tuple[arb, arb, arb, arb, dict[str, object]]:
    if n < 0:
        raise ProducerError("geometric-sum index must be nonnegative")
    target = arb(2) ** (-tail_bits)
    w = 2 * arb.pi() * n / L
    w2 = w * w
    ratio = (-2 * L).exp()
    one_minus_ratio = 1 - ratio
    if not (one_minus_ratio > 0):
        raise ProducerError("invalid geometric ratio")

    g_s = arb(0)
    g_cc = arb(0)
    g_x1 = arb(0)
    g_x2 = arb(0)
    for k in range(1_000_000):
        ck = arb(2 * k) + arb(1) / 2
        ek = (-ck * L).exp()
        den = ck * ck + w2
        g_s += ek / den
        if n:
            g_cc += ek * w2 / (ck * den)
        g_x1 += ek * ck / den
        g_x2 += ek * (ck * ck - w2) / (den * den)

        cnext = ck + 2
        envelope = (-cnext * L).exp() / one_minus_ratio
        b_sq = envelope / (cnext * cnext)
        b_lin = envelope / cnext
        largest = b_lin if n else max(b_sq, b_lin)
        if largest.upper() < target:
            g_s += zero_ball(b_sq)
            if n:
                g_cc += zero_ball(b_lin)
            g_x1 += zero_ball(b_lin)
            g_x2 += zero_ball(b_sq)
            return g_s, g_cc, g_x1, g_x2, {
                "terms": k + 1,
                "g_s_tail": arb_interval_json(zero_ball(b_sq)),
                "g_cc_tail": arb_interval_json(arb(0) if not n else zero_ball(b_lin)),
                "g_x1_tail": arb_interval_json(zero_ball(b_lin)),
                "g_x2_tail": arb_interval_json(zero_ball(b_sq)),
            }
    raise ProducerError("geometric series did not reach the requested tail")


def closed_sequences(c: int, tail_bits: int) -> tuple[list[arb], list[arb], list[arb], arb, list[dict[str, object]]]:
    """Return the X-0001 S, CC, XC sequences for n=0,1."""
    L = arb(c).log()
    psi_quarter, _ = psi_and_psi1(acb(arb(1) / 4))
    S: list[arb] = []
    CC: list[arb] = []
    XC: list[arb] = []
    tails: list[dict[str, object]] = []
    for n in (0, 1):
        w = 2 * arb.pi() * n / L
        z = acb(arb(1) / 4, arb.pi() * n / L)
        psi, psi1 = psi_and_psi1(z)
        g_s, g_cc, g_x1, g_x2, tail = geometric_sums(n, L, tail_bits)
        if n == 0:
            s_n = arb(0)
            cc_n = arb(0)
        else:
            s_n = psi.imag / 2 - w * g_s
            cc_n = -(psi.real - psi_quarter.real) / 2 + g_cc
        xc_n = psi1.real / 4 - L * g_x1 - g_x2
        S.append(s_n)
        CC.append(cc_n)
        XC.append(xc_n)
        tail["n"] = n
        tails.append(tail)
    return S, CC, XC, L, tails


def signed_odd(values: Sequence[arb], n: int) -> arb:
    return values[n] if n >= 0 else -values[-n]


def build_full_matrix(c: int, tail_bits: int) -> tuple[list[list[arb]], dict[str, object]]:
    S, CC, XC, L, tails = closed_sequences(c, tail_bits)
    pi = arb.pi()
    L2 = L * L
    sixteen_pi_sq = 16 * pi * pi
    prefactor = 32 * L * (L / 4).sinh() ** 2
    eL = L.exp()
    kappa = (4 * pi * (eL - 1) / (eL + 1)).log() + arb.const_euler()
    U = (L / 2).exp()
    J = -2 * (U + 1).log() + (U * U + 1).log() + 2 * U.atan() + arb(2).log() - pi / 2

    powers = prime_powers_up_to(c)
    weighted_positions = [
        (arb(p).log() / arb(q).sqrt(), arb(q).log(), q, p) for q, p in powers
    ]
    nodes = (-1, 0, 1)
    matrix = [[arb(0) for _ in nodes] for _ in nodes]
    for i, n in enumerate(nodes):
        for j in range(i, len(nodes)):
            m = nodes[j]
            numerator = L2 - sixteen_pi_sq * m * n
            denominator = (L2 + sixteen_pi_sq * m * m) * (L2 + sixteen_pi_sq * n * n)
            w_02 = prefactor * numerator / denominator

            if n == m:
                w_r = kappa + 2 * CC[abs(n)] + J - (2 / L) * XC[abs(n)]
            else:
                w_r = (signed_odd(S, m) - signed_odd(S, n)) / (pi * (n - m))

            w_p = arb(0)
            for weight, y, _q, _p in weighted_positions:
                if n == m:
                    kernel = 2 * (1 - y / L) * (2 * pi * n * y / L).cos()
                else:
                    kernel = ((2 * pi * m * y / L).sin() - (2 * pi * n * y / L).sin()) / (pi * (n - m))
                w_p += weight * kernel

            value = w_02 - w_r - w_p
            matrix[i][j] = value
            matrix[j][i] = value

    return matrix, {
        "L": arb_interval_json(L),
        "prime_power_count": len(powers),
        "prime_power_last": powers[-1][0] if powers else None,
        "geometric_tails": tails,
    }


def even_matrix(full: Sequence[Sequence[arb]]) -> list[list[arb]]:
    root2 = arb(2).sqrt()
    return [
        [full[1][1], (full[1][0] + full[1][2]) / root2],
        [
            (full[0][1] + full[2][1]) / root2,
            (full[0][0] + full[0][2] + full[2][0] + full[2][2]) / 2,
        ],
    ]


def zero_row(c: int, gamma: arb) -> tuple[list[arb], list[arb]]:
    """Return simplified and direct-even evaluation rows."""
    L = arb(c).log()
    pi = arb.pi()
    mu = L * gamma / (2 * pi)
    factor = L.sqrt() / pi * (pi * mu).sin()
    simplified = [
        -factor / mu,
        factor * arb(2).sqrt() * mu / (1 - mu * mu),
    ]
    full = [factor / (-1 - mu), factor / (-mu), factor / (1 - mu)]
    direct = [full[1], (full[0] + full[2]) / arb(2).sqrt()]
    for a, b in zip(simplified, direct):
        if not a.overlaps(b):
            raise ProducerError("direct and simplified critical-line evaluation rows disagree")
    return simplified, direct


def dot(row: Sequence[arb], vector: Sequence[arb]) -> arb:
    if len(row) != len(vector):
        raise ProducerError("dot-product dimension mismatch")
    value = arb(0)
    for a, b in zip(row, vector):
        value += a * b
    return value


def mat_quad(matrix: Sequence[Sequence[arb]], left: Sequence[arb], right: Sequence[arb]) -> arb:
    value = arb(0)
    for i in range(len(left)):
        for j in range(len(right)):
            value += left[i] * matrix[i][j] * right[j]
    return value


def level_payload(raw: dict[str, Any], zero_rows: dict[int, list[arb]], tail_bits: int) -> dict[str, object]:
    c = parse_int(raw.get("c"), "level.c")
    N = parse_int(raw.get("N"), "level.N")
    if c < 2 or N != 1:
        raise ProducerError("this first production producer requires integer c>=2 and N=1")
    r_raw = raw.get("r")
    if not isinstance(r_raw, list) or len(r_raw) != 2:
        raise ProducerError("level.r must have two integer entries")
    r = [arb(parse_int(value, "level.r")) for value in r_raw]
    if r[0] == 0 and r[1] == 0:
        raise ProducerError("zero near-kernel vector")
    w = [-r[1], r[0]]
    z_index = parse_int(raw.get("z_index"), "level.z_index")
    y_index = parse_int(raw.get("y_index"), "level.y_index")
    if z_index == y_index or z_index not in zero_rows or y_index not in zero_rows:
        raise ProducerError("invalid or repeated zero-frame indices")
    z = zero_rows[z_index]
    y = zero_rows[y_index]

    full, metadata = build_full_matrix(c, tail_bits)
    A = even_matrix(full)
    if not A[0][1].overlaps(A[1][0]):
        raise ProducerError("even matrix symmetry gate failed")

    zr = dot(z, r)
    zw = dot(z, w)
    if not (zw.abs_lower() > 0):
        raise ProducerError("first-frame scalar B contains zero")
    alpha = -zr / zw
    k = [r[i] + alpha * w[i] for i in range(2)]
    graph_metric = dot(k, k)
    if not (graph_metric > 0):
        raise ProducerError("graph metric is not positive")

    conditional = dot(y, k)
    selected = conditional * conditional
    selected_ratio = selected / graph_metric

    complement_block = mat_quad(A, w, w)
    if not (complement_block.lower() > 0):
        raise ProducerError("positive-sector block was not certified positive")
    cross = mat_quad(A, w, k)
    kernel_raw = mat_quad(A, k, k)
    schur = kernel_raw - cross * cross / complement_block
    schur_ratio = schur / graph_metric
    residual_corrected = schur - selected
    residual_ratio = residual_corrected / graph_metric

    if residual_ratio.lower() >= 0:
        nu_upper = arb(0)
    else:
        nu_upper = -residual_ratio.lower()
    margin_lower = selected_ratio.lower() - nu_upper

    t = cross / complement_block
    lambda_trace = 2 + alpha * alpha + (t - alpha) * (t - alpha)

    return {
        "id": f"c{c}-N1",
        "c": c,
        "N": N,
        "near_kernel_integer": [str(int(value)) for value in r_raw],
        "first_zero_index": z_index,
        "second_zero_index": y_index,
        "matrix_even": [[arb_interval_json(entry) for entry in row] for row in A],
        "first_zero_row": [arb_interval_json(entry) for entry in z],
        "second_zero_row": [arb_interval_json(entry) for entry in y],
        "derived_diagnostics": {
            "alpha": arb_interval_json(alpha),
            "conditional_evaluation": arb_interval_json(conditional),
            "graph_metric": arb_interval_json(graph_metric),
            "selected_frame_ratio": arb_interval_json(selected_ratio),
            "positive_sector_block": arb_interval_json(complement_block),
            "raw_kernel": arb_interval_json(kernel_raw),
            "cross": arb_interval_json(cross),
            "schur": arb_interval_json(schur),
            "schur_ratio": arb_interval_json(schur_ratio),
            "joint_corrected_residual_ratio": arb_interval_json(residual_ratio),
            "joint_negative_endpoint_upper": exact_binary_json(nu_upper),
            "conditional_margin_lower": exact_binary_json(margin_lower),
            "triangular_metric_trace_upper": exact_binary_json(lambda_trace.upper()),
        },
        "source_metadata": metadata,
    }


def build_certificate(config: dict[str, Any], precision_bits: int | None) -> dict[str, object]:
    if config.get("schema") != "riemann.x20701.d0001-frame.config.v1":
        raise ProducerError("unexpected config schema")
    precision = precision_bits or parse_int(config.get("precision_bits"), "precision_bits")
    tail_bits = parse_int(config.get("geometric_tail_bits"), "geometric_tail_bits")
    if precision < 128 or tail_bits < 80 or tail_bits >= precision:
        raise ProducerError("require precision>=128 and 80<=tail_bits<precision")
    ctx.prec = precision
    ctx.cap = 6

    zero_count = parse_int(config.get("zero_count"), "zero_count")
    if zero_count < 2:
        raise ProducerError("at least two certified critical-line zeros are required")
    zeros = acb.zeta_zeros(1, zero_count)
    if len(zeros) != zero_count:
        raise ProducerError("unexpected zeta-zero count")
    count_at_25 = unique_integer(arb(25).zeta_nzeros(), "N(25)")
    if count_at_25 != 2:
        raise ProducerError(f"expected N(25)=2, got {count_at_25}")

    zero_payload = []
    zero_rows_by_level: dict[int, dict[int, list[arb]]] = {}
    levels_raw = config.get("levels")
    if not isinstance(levels_raw, list) or not levels_raw:
        raise ProducerError("levels must be a nonempty array")
    cutoffs = [parse_int(level.get("c"), "level.c") for level in levels_raw]
    for c in cutoffs:
        rows: dict[int, list[arb]] = {}
        for index, zero in enumerate(zeros, start=1):
            simplified, direct = zero_row(c, zero.imag)
            rows[index] = [a.intersection(b) for a, b in zip(simplified, direct)]
        zero_rows_by_level[c] = rows

    for index, zero in enumerate(zeros, start=1):
        zero_payload.append({
            "index": index,
            "gamma": arb_interval_json(zero.imag),
            "multiplicity_lower": 1,
            "source": "python-flint acb.zeta_zeros",
        })

    levels = [level_payload(raw, zero_rows_by_level[parse_int(raw.get("c"), "level.c")], tail_bits) for raw in levels_raw]
    certificate: dict[str, object] = {
        "schema": SCHEMA,
        "producer": {
            "backend": "python-flint/Arb",
            "python_flint_version": importlib.metadata.version("python-flint"),
            "python_version": platform.python_version(),
            "platform": platform.platform(),
            "precision_bits": precision,
            "geometric_tail_bits": tail_bits,
            "operator": "D-0001 cutoff-free finite Weil block, even sector, N=1",
            "zero_row_gate": "direct full-coordinate and simplified even-coordinate formulas intersect",
            "classification": "directed single-backend production; exact consumer decides signs",
        },
        "zero_census": {
            "positive_zero_count": zero_count,
            "N_25": count_at_25,
            "zeros": zero_payload,
        },
        "levels": levels,
        "proof_boundary": (
            "Actual D-0001 finite zeta-data blocks and actual critical-line zeros. "
            "This ladder certifies the declared finite even packets only; it does not "
            "identify them with the complete Suzuki low hierarchy required by T-14302."
        ),
    }
    certificate["certificate_sha256"] = canonical_digest(certificate)
    return certificate


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("config", type=Path)
    parser.add_argument("--precision-bits", type=int)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    config = json.loads(args.config.read_text(encoding="utf-8"))
    if not isinstance(config, dict):
        raise ProducerError("config root must be an object")
    certificate = build_certificate(config, args.precision_bits)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "certificate_sha256": certificate["certificate_sha256"],
        "level_count": len(certificate["levels"]),
        "precision_bits": certificate["producer"]["precision_bits"],
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
