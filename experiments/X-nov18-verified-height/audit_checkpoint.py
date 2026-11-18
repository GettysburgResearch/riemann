"""Independently decode a pinned bracket census and recompute three full-strip counts."""
import argparse
import hashlib
import json
import lzma
from fractions import Fraction
from pathlib import Path

from flint import arb, ctx

OLD_HEIGHT = 3_000_175_332_800
OLD_COUNT = 12_363_153_437_138
STRIDE = 10_000


def compare(x, y):
    """Compare two signed dyadics with integers alone."""
    a, e = x
    b, f = y
    return (a << max(0, e-f)) - (b << max(0, f-e))


def exact_value(dyadic):
    a, e = dyadic
    return Fraction(a) * Fraction(2) ** e


def audit(path):
    meta = json.loads(path.read_text())
    count = meta["complete_blocks"]
    if not isinstance(count, int) or count <= 0:
        raise ValueError("Invalid block count")
    digest = hashlib.sha256()
    prior_left = prior_right = None
    for block in range(count):
        archive = path.parent / "blocks" / f"{block:04d}.xz"
        info = json.loads(archive.with_suffix(".json").read_text())
        packed = archive.read_bytes()
        raw = lzma.decompress(packed)
        stream = hashlib.sha256(raw).hexdigest()
        if hashlib.sha256(packed).hexdigest() != info["compressed_sha256"] or stream != info["stream_sha256"]:
            raise ValueError(f"SHA-256 mismatch in block {block}")
        digest.update(f"{block}\t{stream}\n".encode())
        if (info["first_index"], info["last_index"]) != (OLD_COUNT + STRIDE*block, OLD_COUNT + STRIDE*(block+1)):
            raise ValueError(f"Unmatched global indices in block {block}")
        rows = raw.splitlines()
        if len(rows) != STRIDE + 1:
            raise ValueError(f"Unexpected row count in block {block}")
        for row, line in enumerate(rows):
            a, e, b, f = (int(x, 16) for x in line.split())
            left, right = (a, e), (b, f)
            if compare(left, right) >= 0:
                raise ValueError(f"Empty interval at {block}:{row}")
            if block == 0 and row == 0 and compare(right, (OLD_HEIGHT, 0)) >= 0:
                raise ValueError("Historical final index does not lie below the published height")
            if block == 0 and row == 1 and compare(left, (OLD_HEIGHT, 0)) <= 0:
                raise ValueError("First new index does not lie above the published height")
            if row == 0 and block:
                if compare(prior_left, right) >= 0 or compare(left, prior_right) >= 0:
                    raise ValueError(f"Repeated endpoint index missing at block {block}")
            elif row and compare(prior_right, left) > 0:
                raise ValueError(f"Overlapping neighboring intervals at {block}:{row}")
            prior_left, prior_right = left, right
    guard = exact_value(prior_left)
    last = OLD_COUNT + STRIDE*count
    if digest.hexdigest() != meta["ordered_stream_digest"] or guard != exact_value(meta["guarded_dyadic_ordinate"]):
        raise ValueError("Checkpoint guard or ordered digest mismatch")
    integer = guard.numerator // guard.denominator
    expected = {"published_height": OLD_HEIGHT, "published_zero_count": OLD_COUNT,
                "new_consecutive_indices": STRIDE*count, "last_certified_index": last,
                "verified_integer_height": integer, "height_extension": integer-OLD_HEIGHT,
                "expected_guarded_count": last-1}
    if any(meta.get(k) != v for k, v in expected.items()):
        raise ValueError("Inconsistent checkpoint summary")
    ctx.prec = max(192, guard.numerator.bit_length()+4)
    points = (("published", Fraction(OLD_HEIGHT), OLD_COUNT),
              ("integer_height", Fraction(integer), None), ("guarded", guard, last-1))
    result = {}
    for name, ordinate, n in points:
        point = arb(ordinate.numerator)/ordinate.denominator
        certified = point.zeta_nzeros()
        if not point.is_exact() or not certified.is_exact():
            raise ArithmeticError(f"Unresolved {name} count")
        total = int(certified.unique_fmpz())
        if n is not None and total != n:
            raise ArithmeticError(f"Wrong global {name} count")
        key = f"independent_{name}_count"
        if meta.get(key) is not None and meta[key] != total:
            raise ArithmeticError(f"Count differs from archived {name} count")
        result[key] = total
    return {"complete_blocks": count, **expected, **result, "ordered_stream_digest": digest.hexdigest()}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checkpoint", type=Path)
    args = parser.parse_args()
    print(json.dumps(audit(args.checkpoint), indent=2))
