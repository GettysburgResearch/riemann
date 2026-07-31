#!/usr/bin/env python3
"""Exact finite audit of determinant dependence on Sobolev smoothing data."""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction


def dump(x: Fraction):
    if x.denominator == 1:
        return x.numerator
    return {"numerator": x.numerator, "denominator": x.denominator}


def spectrum(reference: tuple[int, ...], raw: tuple[int, ...], exponent: int):
    if len(reference) != len(raw) or exponent <= 0:
        raise ValueError("bad data")
    # S=(I+A)^(-a), K=S B S.
    return tuple(Fraction(b, (1 + lam) ** (2 * exponent)) for lam, b in zip(reference, raw))


def traces(values: tuple[Fraction, ...], max_order: int):
    return {m: sum(x ** m for x in values) for m in range(2, max_order + 1)}


def verify():
    raw = (1, 3)
    k1 = spectrum((1, 4), raw, 1)
    k2 = spectrum((1, 4), raw, 2)
    kswap = spectrum((4, 1), raw, 1)
    t1 = traces(k1, 6)
    t2 = traces(k2, 6)
    ts = traces(kswap, 6)
    if k1 != (Fraction(1, 4), Fraction(3, 25)):
        raise AssertionError("K1 mismatch")
    if k2 != (Fraction(1, 16), Fraction(3, 625)):
        raise AssertionError("K2 mismatch")
    if kswap != (Fraction(1, 25), Fraction(3, 4)):
        raise AssertionError("swapped chart mismatch")
    if t1[2] != Fraction(769, 10000):
        raise AssertionError("K1 second trace mismatch")
    if t2[2] != Fraction(392929, 100000000):
        raise AssertionError("K2 second trace mismatch")
    if t1 == t2 or t1 == ts or t2 == ts:
        raise AssertionError("gauge dependence disappeared")
    data = {
        "status": "CERTIFIED_REGULARIZER_CHANGES_DET2_MOMENTS",
        "raw_form_diagonal": list(raw),
        "reference_diagonal": [1, 4],
        "spectrum_exponent_1": [dump(x) for x in k1],
        "spectrum_exponent_2": [dump(x) for x in k2],
        "spectrum_swapped_chart": [dump(x) for x in kswap],
        "trace2_exponent_1": dump(t1[2]),
        "trace2_exponent_2": dump(t2[2]),
        "trace2_swapped_chart": dump(ts[2]),
        "det2_zero_moduli_exponent_1": [dump(1 / abs(x)) for x in k1],
        "det2_zero_moduli_exponent_2": [dump(1 / abs(x)) for x in k2],
        "det2_zero_moduli_swapped_chart": [dump(1 / abs(x)) for x in kswap],
        "scope": "synthetic finite regularization audit; no Riemann evaluation",
    }
    payload = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    data["proof_sha256"] = hashlib.sha256(payload).hexdigest()
    return data


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2, sort_keys=True))
