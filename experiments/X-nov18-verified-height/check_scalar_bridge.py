"""Replay the full scalar Hardy-sign verification on the first historical bridge."""
import lzma
from pathlib import Path
from flint import arb, ctx
from check_scalar_signs import exact_dyadic, hardy_sign


def main():
    ctx.prec = 96
    data = lzma.decompress(Path(__file__).with_name("scalar-bridge.tsv.xz").read_bytes())
    first, last, previous_sign = None, None, 0
    rows = data.decode("ascii").splitlines()
    if len(rows) != 2220:
        raise ArithmeticError("Unexpected scalar point count")
    for i, row in enumerate(rows):
        m, e, expected, original = row.split(maxsplit=3)
        t = exact_dyadic(int(m), int(e))
        sign = hardy_sign(t)
        if sign != int(expected) or sign == previous_sign or not sign * arb(original) > 0:
            raise ArithmeticError(f"Scalar sign mismatch at separator {i}")
        if last is not None and not last < t:
            raise ArithmeticError("Scalar heights not strictly increasing")
        first = t if first is None else first
        last, previous_sign = t, sign
        if (i+1) % 250 == 0:
            print(f"Checked {i+1} scalar signs", flush=True)
    if first != 3_000_175_332_800 or last != arb("3000175333318.5"):
        raise ArithmeticError("Incorrect scalar bridge endpoints")
    for t, expected in [(first, 12_363_153_437_138), (last, 12_363_153_439_357)]:
        count = t.zeta_nzeros()
        if not count.is_exact() or count != expected:
            raise ArithmeticError("Generic full-strip count mismatch")
    print("Verified all 2,219 zeros of the scalar bridge by signs and total counts.")


if __name__ == "__main__":
    main()
