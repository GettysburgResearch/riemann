"""Verify the contiguous archived prefix, optionally replay a primitive block and counts."""

import argparse
import hashlib
import json
import lzma
from pathlib import Path

from flint import arb, ctx
from isolate import ANCHOR, BLOCK_SIZE, NativeIsolator, canonical, check_brackets, compare, intersection


PUBLISHED_HEIGHT = 3_000_175_332_800


def decode(data):
    intervals = []
    for line in data.splitlines():
        a, e, b, f = (int(item, 16) for item in line.split())
        intervals.append(((a, e), (b, f)))
    return intervals


def replay(metadata, expected):
    native = NativeIsolator()
    shifted = None
    accumulated = []
    first = metadata["first_index"]
    for call in metadata["calls"]:
        args = (call["first_index"], call["requested"], call["precision"])
        if "shifted_parameters" in call:
            if shifted is None:
                from shifted_isolator import ShiftedIsolator
                shifted = ShiftedIsolator()
            raw = shifted.batch_from_parameters(*args, call["shifted_parameters"])
        else:
            raw = native.batch(*args)
        check_brackets(raw)
        if len(raw) != call["returned"] or hashlib.sha256(canonical(raw)).hexdigest() != call["stream_sha256"]:
            raise ArithmeticError("Primitive Platt/Turing replay differs from its signed bracket stream")
        next_index = first + max(0, len(accumulated) - 1)
        offset = next_index - call["first_index"]
        if not 0 <= offset < len(raw):
            raise ArithmeticError("A native call does not cover the next required index")
        new = raw[offset:]
        if accumulated:
            accumulated[-1] = intersection(accumulated[-1], new[0])
            accumulated.extend(new[1:])
        else:
            accumulated.extend(new)
    if accumulated != expected:
        raise ArithmeticError("Replayed intervals differ from the archive")


def dyadic_arb(endpoint):
    mantissa, exponent = endpoint
    ctx.prec = max(ctx.prec, mantissa.bit_length() + 32)
    point = arb(mantissa) * arb(2)**exponent
    if not point.is_exact():
        raise ArithmeticError("Selected dyadic ordinate was rounded")
    return point


def integer_floor(endpoint):
    mantissa, exponent = endpoint
    return mantissa << exponent if exponent >= 0 else mantissa >> -exponent


def exact_count(point):
    precision = ctx.prec
    try:
        while ctx.prec <= max(4096, precision):
            count = arb(point).zeta_nzeros()
            if count.is_exact() and count.is_integer():
                return int(count.fmpz())
            ctx.prec *= 2
        raise ArithmeticError(f"The independent total zero count was not exact: {count}")
    finally:
        ctx.prec = precision


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--blocks", type=Path, default=Path(__file__).parent / "blocks")
    parser.add_argument("--max-blocks", type=int)
    parser.add_argument("--replay-block", type=int)
    parser.add_argument("--count", action="store_true",
                        help="also run generic Riemann–Siegel/Turing counts at both endpoints")
    args = parser.parse_args()
    if args.max_blocks is not None and args.max_blocks < 1:
        parser.error("max-blocks must be positive")
    directory = args.blocks
    previous = None
    count = 0
    root_hash = hashlib.sha256()
    last_metadata = None
    final = None
    while args.max_blocks is None or count < args.max_blocks:
        archive = directory / f"{count:04d}.xz"
        manifest = archive.with_suffix(".json")
        # A concurrently created archive is visible before its atomic manifest.
        if not manifest.is_file():
            break
        metadata = json.loads(manifest.read_text())
        data = archive.read_bytes()
        stream = lzma.decompress(data)
        if (hashlib.sha256(data).hexdigest() != metadata["compressed_sha256"]
                or hashlib.sha256(stream).hexdigest() != metadata["stream_sha256"]):
            raise ArithmeticError(f"Hash mismatch in block {count}")
        intervals = decode(stream)
        if (metadata["first_index"] != ANCHOR + count * BLOCK_SIZE
                or metadata["last_index"] != ANCHOR + (count + 1) * BLOCK_SIZE
                or len(intervals) != BLOCK_SIZE + 1 or metadata["count"] != len(intervals)
                or canonical(intervals) != stream):
            raise ArithmeticError(f"Invalid indexing or canonical encoding in block {count}")
        check_brackets(intervals)
        if previous is not None:
            intersection(previous, intervals[0])
        if args.replay_block == count:
            replay(metadata, intervals)
        root_hash.update(f"{count}\t{metadata['stream_sha256']}\n".encode("ascii"))
        count += 1
        previous = intervals[-1]
        last_metadata, final = metadata, intervals
    if not count:
        raise SystemExit("No contiguous complete block beginning at the historical anchor")
    if args.max_blocks is not None and count < args.max_blocks:
        raise SystemExit(f"Only {count} contiguous blocks available")
    if args.replay_block is not None and not 0 <= args.replay_block < count:
        raise SystemExit("Requested replay block is outside the checked prefix")
    index = last_metadata["last_index"]
    lower = final[-1][0]
    height = integer_floor(lower)
    # At the lower endpoint of the final open sign bracket, exactly index-1
    # zeros have occurred. Its position is known exactly as a dyadic rational.
    ctx.prec = 128
    guarded = dyadic_arb(lower)
    result = {"published_height": PUBLISHED_HEIGHT, "published_zero_count": ANCHOR,
              "complete_blocks": count, "new_consecutive_indices": index - ANCHOR,
              "last_certified_index": index, "verified_integer_height": height,
              "height_extension": height - PUBLISHED_HEIGHT,
              "guarded_dyadic_ordinate": list(lower), "expected_guarded_count": index - 1,
              "ordered_stream_digest": root_hash.hexdigest(),
              "primitive_block_replayed": args.replay_block}
    if args.count:
        old_count = exact_count(PUBLISHED_HEIGHT)
        guarded_count = exact_count(guarded)
        height_count = exact_count(height)
        if (old_count != ANCHOR or guarded_count != index - 1
                or not ANCHOR <= height_count <= guarded_count):
            raise ArithmeticError("Independent endpoint counts disagree")
        # At an integer falling inside one open bracket the count may be on
        # either side of that root; in a certified gap it is uniquely specified.
        first = last_metadata["first_index"]
        min_count = first - 1 + sum(compare(high, (height, 0)) <= 0 for _, high in final)
        max_count = first - 1 + sum(compare(low, (height, 0)) < 0 for low, _ in final)
        if not min_count <= height_count <= max_count:
            raise ArithmeticError("Integer-height count contradicts the index stream")
        result.update({"independent_published_count": old_count,
                       "independent_guarded_count": guarded_count,
                       "independent_integer_height_count": height_count})
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
