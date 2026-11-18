"""Verify two hash-selected native brackets per block using generic scalar zeta.

With --full-block, verify every bracket of that block. Requires python-flint.
No producer code, Platt interpolation, or archived Hardy signs are imported.
"""
import argparse
import hashlib
import json
import lzma
from pathlib import Path

from flint import acb, arb, ctx


def exact_dyadic(mantissa, exponent):
    ctx.prec = max(ctx.prec, abs(mantissa).bit_length() + 32)
    point = arb(mantissa) * arb(2) ** exponent
    if not point.is_exact():
        raise ArithmeticError("Rounded dyadic test endpoint")
    return point


def hardy_sign(t):
    initial = ctx.prec
    try:
        while True:
            half = arb(1) / 2
            phase = acb(half / 2, t / 2).lgamma().imag - t * arb.pi().log() / 2
            value = acb(0, phase).exp() * acb(half, t).zeta()
            if 0 not in value.imag:
                raise ArithmeticError("Expected a real Hardy value")
            if value.real > 0:
                return 1
            if value.real < 0:
                return -1
            if ctx.prec >= 512 or not t.is_exact():
                raise ArithmeticError(f"Undetermined sign at {t}")
            ctx.prec *= 2
    finally:
        ctx.prec = initial


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--blocks", type=Path, default=Path(__file__).parent / "blocks")
    parser.add_argument("--first", type=int, default=0)
    parser.add_argument("--stop", type=int, required=True, help="exclusive block index")
    parser.add_argument("--full-block", action="store_true")
    args = parser.parse_args()
    if not 0 <= args.first < args.stop:
        parser.error("invalid block range")
    ctx.prec = 112
    for i in range(args.first, args.stop):
        archive = args.blocks / f"{i:04d}.xz"
        raw = lzma.decompress(archive.read_bytes())
        info = json.loads(archive.with_suffix(".json").read_text())
        digest = hashlib.sha256(raw).digest()
        rows = raw.splitlines()
        if digest.hex() != info["stream_sha256"] or len(rows) != 10_001:
            raise ArithmeticError(f"Corrupt block {i}")
        first = int.from_bytes(digest[:16], "big") % len(rows)
        second = (first + 1 + int.from_bytes(digest[16:], "big") % (len(rows) - 1)) % len(rows)
        selected = range(len(rows)) if args.full_block else sorted((first, second))
        for row in selected:
            a, e, b, f = (int(x, 16) for x in rows[row].split())
            low = exact_dyadic(a, e)
            high = exact_dyadic(b, f)
            left, right = hardy_sign(low), hardy_sign(high)
            if not low < high or left == right:
                raise ArithmeticError(f"No strict crossing in block {i}, row {row}")
            print(f"{i}\t{row}\t{12_363_153_437_138 + 10_000 * i + row}\t{left}\t{right}", flush=True)


if __name__ == "__main__":
    main()
