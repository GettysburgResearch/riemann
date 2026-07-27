#!/usr/bin/env python3
"""Chunked directed replay of every X-5606 prime-knot cell including terminal."""
from __future__ import annotations

import json
import math
import sys
import time

from flint import arb, ctx


def prime_powers(limit):
    flags = bytearray(b"\x01") * (limit + 1)
    flags[0:2] = b"\x00\x00"
    for prime in range(2, math.isqrt(limit) + 1):
        if flags[prime]:
            start = prime * prime
            flags[start : limit + 1 : prime] = b"\x00" * (
                (limit - start) // prime + 1
            )
    out = []
    for prime in range(2, limit + 1):
        if flags[prime]:
            value = prime
            while value <= limit:
                out.append((value, prime))
                value *= prime
    return sorted(out)


class Smooth:
    def __init__(self):
        self.k1 = (arb(1) / 4).digamma() - arb.pi().log()
        self.constant = arb.pi() ** 2 + 8 * arb.const_catalan()

    def phi(self, t, terms=30):
        z = (-2 * t).exp()
        acc, power = arb(0), arb(1)
        for index in range(terms):
            acc += power / ((arb(index) + arb(1) / 4) ** 2)
            power *= z
        tail = power / (((arb(terms) + arb(1) / 4) ** 2) * (1 - z))
        return acc + tail.union(arb(0))

    def value(self, t):
        return (
            4 * ((t / 2).exp() + (-t / 2).exp() - 2)
            + (t / 2) * self.k1
            + (self.constant - (-t / 2).exp() * self.phi(t)) / 4
        )

    def derivative(self, t, terms=30):
        acc = arb(0)
        for index in range(terms):
            k = 4 * index + 1
            acc += 2 * (-(arb(k) * t) / 2).exp() / k
        k = 4 * terms + 1
        tail = (-(arb(k) * t) / 2).exp() / (2 * (1 - (-2 * t).exp()))
        return (
            2 * ((t / 2).exp() - (-t / 2).exp())
            + self.k1 / 2
            + acc
            + tail.union(arb(0))
        )


def exact_binary(value):
    mantissa, exponent = value.man_exp()
    mantissa, exponent = int(mantissa), int(exponent)
    if exponent >= 0:
        numerator, denominator = mantissa << exponent, 1
    else:
        numerator, denominator = mantissa, 1 << (-exponent)
        while numerator and numerator % 2 == 0:
            numerator //= 2
            denominator //= 2
    return {
        "numerator": str(numerator),
        "denominator": str(denominator),
        "mantissa": str(mantissa),
        "exponent": exponent,
    }


def run(start_index, end_index, output):
    ctx.prec = 128
    cutoff = 10**7
    manifest = prime_powers(cutoff)
    end_index = min(end_index, len(manifest))
    if not 0 <= start_index < end_index <= len(manifest):
        raise ValueError("invalid chunk range")

    smooth = Smooth()
    p0, p1 = arb(0), arb(0)
    previous = arb(1) / 2
    for index in range(start_index):
        value, prime = manifest[index]
        knot = arb(value).log()
        if knot > previous:
            previous = knot
        weight = arb(prime).log() / arb(value).sqrt()
        p0 += weight
        p1 += weight * knot

    minimum = None
    location = None
    all_positive = True
    cells = 0
    worst_depth = 0

    def cell_bound(left, right, prefix0, prefix1, depth=0):
        nonlocal worst_depth
        midpoint = (left + right) / 2
        value = smooth.value(midpoint) - prefix0 * midpoint + prefix1
        derivative = smooth.derivative(midpoint) - prefix0
        bound = value + (
            derivative * (left - midpoint)
        ).min(derivative * (right - midpoint))
        if bound > 0 or depth >= 14:
            worst_depth = max(worst_depth, depth)
            return bound
        return cell_bound(left, midpoint, prefix0, prefix1, depth + 1).min(
            cell_bound(midpoint, right, prefix0, prefix1, depth + 1)
        )

    started = time.time()
    for index in range(start_index, end_index):
        value, prime = manifest[index]
        knot = arb(value).log()
        if knot > previous:
            bound = cell_bound(previous, knot, p0, p1)
            cells += 1
            if not (bound > 0):
                all_positive = False
            lower = bound.lower()
            if minimum is None or lower < minimum:
                minimum = lower
                location = {"kind": "knot", "n": value, "index": index}
            previous = knot
        weight = arb(prime).log() / arb(value).sqrt()
        p0 += weight
        p1 += weight * knot

    terminal = False
    if end_index == len(manifest):
        terminal = True
        bound = cell_bound(previous, arb(cutoff).log(), p0, p1)
        cells += 1
        if not (bound > 0):
            all_positive = False
        lower = bound.lower()
        if minimum is None or lower < minimum:
            minimum = lower
            location = {"kind": "terminal", "n": cutoff, "index": end_index}

    result = {
        "schema": "riemann.x5606-chunked-directed-replay.v1",
        "start_index": start_index,
        "end_index": end_index,
        "total_prime_powers": len(manifest),
        "cells": cells,
        "all_cells_strictly_positive": all_positive,
        "minimum_exact_binary": exact_binary(minimum),
        "minimum_ball": str(minimum),
        "minimum_location": location,
        "terminal_cell_included": terminal,
        "maximum_bisection_depth": worst_depth,
        "elapsed_seconds": time.time() - started,
        "proof_boundary": (
            "Same python-flint/Arb library and D-9501 analytic formula as X-5606; "
            "independently structured prime-power sieve and disjoint chunk replay."
        ),
    }
    with open(output, "w") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    run(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3])
