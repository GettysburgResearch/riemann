#!/usr/bin/env python3
"""Exact finite regression for the full Hardy delay colligation.

For Theta(z)=z^m, H2 splits as K_Theta plus z^m H2. Raw Laurent delay is
resolved into a forced model coordinate, a returned amplitude coordinate, and
an escaped negative-power prefix. All arithmetic is over Gaussian integers.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict, Iterable, Tuple

Gaussian = Tuple[int, int]
Vector = Dict[int, Gaussian]
State = Tuple[Vector, Vector]


def gadd(a: Gaussian, b: Gaussian) -> Gaussian:
    return (a[0] + b[0], a[1] + b[1])


def gmul(a: Gaussian, b: Gaussian) -> Gaussian:
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def gconj(a: Gaussian) -> Gaussian:
    return (a[0], -a[1])


def clean(v: Vector) -> Vector:
    return {e: z for e, z in v.items() if z != (0, 0)}


def vadd(*vectors: Vector) -> Vector:
    out: Vector = {}
    for v in vectors:
        for e, z in v.items():
            out[e] = gadd(out.get(e, (0, 0)), z)
    return clean(out)


def vscale(c: Gaussian, v: Vector) -> Vector:
    return clean({e: gmul(c, z) for e, z in v.items()})


def shift(v: Vector, amount: int) -> Vector:
    return {e + amount: z for e, z in v.items()}


def raw_delay(v: Vector, delay: int) -> Vector:
    if delay < 0:
        raise ValueError("delay must be nonnegative")
    return shift(v, -delay)


def inner(v: Vector, w: Vector) -> Gaussian:
    out: Gaussian = (0, 0)
    for e in set(v).intersection(w):
        out = gadd(out, gmul(gconj(v[e]), w[e]))
    return out


def norm2(v: Vector) -> int:
    z = inner(v, v)
    assert z[1] == 0 and z[0] >= 0
    return z[0]


def model_part(v: Vector, m: int) -> Vector:
    return {e: z for e, z in v.items() if 0 <= e < m}


def amplitude_coordinate(v: Vector, m: int) -> Vector:
    return {e - m: z for e, z in v.items() if e >= m}


def escaped(v: Vector) -> Vector:
    return {e: z for e, z in v.items() if e < 0}


def embed_state(state: State, m: int) -> Vector:
    g, q = state
    return vadd(g, shift(q, m))


def state_transition(state: State, delay: int, m: int) -> State:
    raw = raw_delay(embed_state(state, m), delay)
    return model_part(raw, m), amplitude_coordinate(raw, m)


def state_blocks(state: State, delay: int, m: int) -> State:
    g, q = state
    t_g = model_part(raw_delay(g, delay), m)
    b_q = model_part(raw_delay(shift(q, m), delay), m)
    d_q = {e: z for e, z in raw_delay(q, delay).items() if e >= 0}
    return vadd(t_g, b_q), d_q


def leakage(state: State, delay: int, m: int) -> Vector:
    return escaped(raw_delay(embed_state(state, m), delay))


def deterministic_state(m: int, qdim: int, seed: int, offset: int) -> State:
    g: Vector = {}
    q: Vector = {}
    for e in range(m):
        z = (
            ((seed * (e + 1) + offset) % 11) - 5,
            ((seed * (e + 3) + 2 * offset) % 13) - 6,
        )
        if z != (0, 0):
            g[e] = z
    for e in range(qdim):
        z = (
            ((seed * (e + 2) + 3 * offset) % 9) - 4,
            ((seed * (e + 5) + offset) % 15) - 7,
        )
        if z != (0, 0):
            q[e] = z
    return g, q


def packet_sum(
    states: Iterable[State],
    delays: Iterable[int],
    coeffs: Iterable[Gaussian],
    m: int,
    channel: str,
) -> Vector:
    pieces = []
    for state, delay, c in zip(states, delays, coeffs, strict=True):
        if channel == "raw":
            v = raw_delay(embed_state(state, m), delay)
        elif channel == "model":
            v = state_transition(state, delay, m)[0]
        elif channel == "amplitude":
            v = state_transition(state, delay, m)[1]
        elif channel == "leakage":
            v = leakage(state, delay, m)
        else:
            raise ValueError(channel)
        pieces.append(vscale(c, v))
    return vadd(*pieces)


def run() -> dict:
    m = 11
    qdim = 9
    seeds = [3, 5, 8, 13, 21]
    states = [
        deterministic_state(m, qdim, seed, j + 1)
        for j, seed in enumerate(seeds)
    ]
    delays = [0, 2, 4, 7, 9]
    coeffs: list[Gaussian] = [(2, 1), (-3, 2), (1, -4), (5, 0), (-2, -3)]

    block_checks = 0
    for state in states:
        for k in range(10):
            if state_transition(state, k, m) != state_blocks(state, k, m):
                raise AssertionError(f"block formula failed at delay {k}")
            block_checks += 1

    pairwise_checks = 0
    for i, (state_i, k_i) in enumerate(zip(states, delays, strict=True)):
        for j, (state_j, k_j) in enumerate(zip(states, delays, strict=True)):
            raw_i = raw_delay(embed_state(state_i, m), k_i)
            raw_j = raw_delay(embed_state(state_j, m), k_j)
            model_i, amp_i = state_transition(state_i, k_i, m)
            model_j, amp_j = state_transition(state_j, k_j, m)
            leak_i = leakage(state_i, k_i, m)
            leak_j = leakage(state_j, k_j, m)
            split = gadd(
                gadd(inner(model_i, model_j), inner(amp_i, amp_j)),
                inner(leak_i, leak_j),
            )
            if inner(raw_i, raw_j) != split:
                raise AssertionError(f"cross-Gram failure at {(i, j)}")
            pairwise_checks += 1

    semigroup_checks = 0
    leakage_cocycle_checks = 0
    for state in states:
        for sigma in range(7):
            for tau in range(7):
                first = state_transition(state, sigma, m)
                lhs_state = state_transition(first, tau, m)
                rhs_state = state_transition(state, sigma + tau, m)
                if lhs_state != rhs_state:
                    raise AssertionError(f"state semigroup failed at {(tau, sigma)}")
                semigroup_checks += 1

                lhs_leak = leakage(state, sigma + tau, m)
                new_leak = leakage(first, tau, m)
                old_leak_shifted = raw_delay(leakage(state, sigma, m), tau)
                if lhs_leak != vadd(new_leak, old_leak_shifted):
                    raise AssertionError(f"leakage cocycle failed at {(tau, sigma)}")
                leakage_cocycle_checks += 1

    raw_packet = packet_sum(states, delays, coeffs, m, "raw")
    model_packet = packet_sum(states, delays, coeffs, m, "model")
    amplitude_packet = packet_sum(states, delays, coeffs, m, "amplitude")
    leakage_packet = packet_sum(states, delays, coeffs, m, "leakage")

    raw_norm = norm2(raw_packet)
    model_norm = norm2(model_packet)
    amplitude_norm = norm2(amplitude_packet)
    leakage_norm = norm2(leakage_packet)
    if raw_norm != model_norm + amplitude_norm + leakage_norm:
        raise AssertionError("three-channel packet identity failed")

    forcing_example = state_blocks(states[2], 7, m)[0]
    model_only = model_part(raw_delay(states[2][0], 7), m)
    forcing_nonzero = forcing_example != model_only
    if not forcing_nonzero:
        raise AssertionError("amplitude-to-model forcing unexpectedly vanished")

    return {
        "verdict": "PASS_FULL_HARDY_DELAY_COLLIGATION",
        "arithmetic": "exact Gaussian integers; no floating point",
        "finite_model": "Theta(z)=z^m; H2=K_Theta orthogonal-sum z^m H2",
        "model_dimension_m": m,
        "amplitude_test_dimension": qdim,
        "packet_size": len(states),
        "delays": delays,
        "block_formula_checks": block_checks,
        "pairwise_cross_gram_identities_checked": pairwise_checks,
        "state_semigroup_identities_checked": semigroup_checks,
        "leakage_cocycle_identities_checked": leakage_cocycle_checks,
        "amplitude_to_model_forcing_nonzero": forcing_nonzero,
        "packet_raw_norm_squared": raw_norm,
        "packet_model_norm_squared": model_norm,
        "packet_amplitude_norm_squared": amplitude_norm,
        "packet_leakage_norm_squared": leakage_norm,
        "three_channel_pythagorean_identity": (
            raw_norm == model_norm + amplitude_norm + leakage_norm
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, default=None)
    args = parser.parse_args()
    result = run()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json is None:
        print(text, end="")
    else:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
