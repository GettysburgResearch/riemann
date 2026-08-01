"""Shared exact helpers for X-16206."""
from __future__ import annotations
import hashlib, json
from fractions import Fraction
from pathlib import Path
from typing import Any
from flint import arb

SCHEMA = "riemann.x16206-directed-interval-ode-emitter.v1"
PRIMITIVE_SCHEMA = "riemann.x16206-directed-interval-ode-primitive.v1"
WRAPPER_SCHEMA = "riemann.x16204-directed-cofinal-wrapper.v1"
GAMMA = 100_000
MODES = (0, 4, 8, 12)
BLOCK_INDICES = (0, 2, 4, 6)
APPROX_DIM = 4096
STURM_DIM = 65536
STURM_RADIUS = Fraction(1, 10_000)
FROBENIUS_TERMS = 700
FROBENIUS_PREC_BITS = 4096
POLE_OFFSET = Fraction(1, GAMMA)
RADIAL_Z_CUTOFF = 4096


def canonical(obj: Any) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()


def sha_obj(obj: Any) -> str:
    return hashlib.sha256(canonical(obj)).hexdigest()


def sha_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fstr(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def exact_arb(x: Fraction) -> arb:
    return arb(x.numerator) / x.denominator


def interval_arb(lo: Fraction, hi: Fraction) -> arb:
    mid = (lo + hi) / 2
    rad = (hi - lo) / 2
    return arb(fstr(mid), fstr(rad))


def arb_point_fraction(x: arb) -> Fraction:
    m, e = x.man_exp()
    m = int(m)
    e = int(e)
    return Fraction(m << e, 1) if e >= 0 else Fraction(m, 1 << (-e))


def arb_bounds(x: arb) -> tuple[Fraction, Fraction]:
    return arb_point_fraction(x.lower()), arb_point_fraction(x.upper())


def _decimal_exponent(x: Fraction) -> int:
    if x <= 0:
        raise ValueError("decimal exponent requires a positive fraction")
    e = len(str(x.numerator)) - len(str(x.denominator))
    if e >= 0:
        while x < 10 ** e:
            e -= 1
        while x >= 10 ** (e + 1):
            e += 1
    else:
        while x < Fraction(1, 10 ** (-e)):
            e -= 1
        while x >= Fraction(1, 10 ** (-(e + 1))):
            e += 1
    return e


def sci_outward(x: Fraction, upward: bool, sig: int = 48) -> str:
    if x == 0:
        return "0"
    if x < 0:
        return "-" + sci_outward(-x, not upward, sig)
    e = _decimal_exponent(x)
    shift = sig - 1 - e
    scaled = x * (10 ** shift) if shift >= 0 else x / (10 ** (-shift))
    q, r = divmod(scaled.numerator, scaled.denominator)
    n = q + (1 if upward and r else 0)
    digits = str(n)
    if len(digits) > sig:
        e += len(digits) - sig
        digits = digits[:sig]
    digits = digits.rjust(sig, "0")
    mantissa = digits[0] + ("." + digits[1:] if sig > 1 else "")
    return mantissa + "e" + str(e)


def arb_interval_json(x: arb) -> list[str]:
    lo, hi = arb_bounds(x)
    return [sci_outward(lo, False), sci_outward(hi, True)]


def upper_json(x: Fraction) -> str:
    return sci_outward(x, True)


def write_json(path: Path, obj: Any) -> str:
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return sha_file(path)
