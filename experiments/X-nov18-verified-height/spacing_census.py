"""Compute certified counts and extremal witnesses for consecutive archived zero gaps."""

import argparse
import hashlib
import heapq
import json
import lzma
from pathlib import Path

PRECISION = 32
UNIT = 1 << PRECISION
# Heights in ordinate units, multiplied by one thousand.
MILLIS = [10, 20, 50, 100, 200, 300, 400, 500, 600]


def outward(mantissa, exponent, upper):
    shift = exponent + PRECISION
    if shift >= 0:
        return mantissa << shift
    if upper:
        return -((-mantissa) >> -shift)
    return mantissa >> -shift


def measure(checkpoint, candidates=12):
    cp = json.loads(checkpoint.read_text())
    if cp.get("independent_guarded_count") != cp.get("last_certified_index") - 1:
        raise ValueError("Need a counted checkpoint")
    directory = checkpoint.parent / "blocks"
    digest = hashlib.sha256()
    nearest = []
    largest = (-1, None)
    smaller = [0] * len(MILLIS)
    larger = [0] * len(MILLIS)
    previous = None
    total = 0
    for block in range(cp["complete_blocks"]):
        manifest = directory / f"{block:04d}.json"
        meta = json.loads(manifest.read_text())
        stream = lzma.decompress(manifest.with_suffix(".xz").read_bytes())
        stream_hash = hashlib.sha256(stream).hexdigest()
        if stream_hash != meta["stream_sha256"]:
            raise ValueError(f"Stream hash mismatch in block {block}")
        digest.update(f"{block}\t{stream_hash}\n".encode())
        rows = stream.splitlines()
        if (len(rows) != 10001 or meta["first_index"] != cp["published_zero_count"] + block * 10000
                or meta["last_index"] != meta["first_index"] + 10000):
            raise ValueError(f"Invalid index coverage in block {block}")
        # Row zero is initially the old anchor, later the previous block's final index.
        for row, line in enumerate(rows[1:], start=1):
            a, e, b, f = (int(word, 16) for word in line.split())
            left = outward(a, e, False)
            right = outward(b, f, True)
            if previous is not None:
                lower, upper = left - previous[1], right - previous[0]
                index = meta["first_index"] + row - 1
                if len(nearest) < candidates:
                    heapq.heappush(nearest, (-upper, index))
                elif upper < -nearest[0][0]:
                    heapq.heapreplace(nearest, (-upper, index))
                if lower > largest[0]:
                    largest = (lower, index)
                for j, cut in enumerate(MILLIS):
                    if 1000 * upper <= cut * UNIT:
                        smaller[j] += 1
                    if 1000 * lower >= cut * UNIT:
                        larger[j] += 1
                total += 1
            previous = (left, right)
    if digest.hexdigest() != cp["ordered_stream_digest"] or total != cp["new_consecutive_indices"] - 1:
        raise ValueError("Census differs from the counted checkpoint")
    return {"checkpoint": checkpoint.name, "ordered_stream_digest": digest.hexdigest(),
            "consecutive_new_gaps": total, "dyadic_exponent": -PRECISION,
            "smallest_upper_witnesses": [{"left_zero_index": idx, "upper_mantissa": -neg}
                                          for neg, idx in sorted(nearest, reverse=True)],
            "largest_lower_witness": {"left_zero_index": largest[1], "lower_mantissa": largest[0]},
            "threshold_counts": [{"threshold_thousandths": cutoff, "certified_below": lo, "certified_above": hi}
                                 for cutoff, lo, hi in zip(MILLIS, smaller, larger)]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checkpoint", type=Path)
    args = parser.parse_args()
    print(json.dumps(measure(args.checkpoint), indent=2))
