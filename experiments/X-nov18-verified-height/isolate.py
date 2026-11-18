"""Create complete native FLINT Platt/Turing interval blocks with overlap.

Requires the Linux LP64 python-flint 0.9.0 wheel, embedding FLINT 3.6.0.
The checked native function returns certified isolating intervals, not approximations
refined to printed decimal ordinates. Its reported count can be below the request.
"""

import argparse
import ctypes
import hashlib
import json
import lzma
import os
from pathlib import Path
import time

import flint


ANCHOR = 12_363_153_437_138
BLOCK_SIZE = 10_000
DEFAULT_PRECISION = 104


class Arf(ctypes.Structure):
    # FLINT 3.6.0 src/arf_types.h: fmpz exp; slong size; two-limb mantissa union.
    _fields_ = [("exp", ctypes.c_long), ("size", ctypes.c_long),
                ("mantissa", ctypes.c_ulong * 2)]


def bind(library, name, result_type, argument_types):
    function = getattr(library, name)
    function.restype = result_type
    function.argtypes = argument_types
    return function


class NativeIsolator:
    def __init__(self):
        if (flint.__version__ != "0.9.0" or flint.__FLINT_VERSION__ != "3.6.0"
                or ctypes.sizeof(ctypes.c_long) != 8 or ctypes.sizeof(Arf) != 32):
            raise RuntimeError("This binding requires the documented FLINT 3.6.0 LP64 ABI")
        wheel = Path(flint.__file__).resolve().parent.parent
        libraries = list((wheel / "python_flint.libs").glob("libflint*.so*"))
        if len(libraries) != 1:
            raise RuntimeError("Cannot identify a unique matching wheel library")
        self.library = ctypes.CDLL(str(libraries[0]))
        pointer, integer = ctypes.c_void_p, ctypes.c_long
        self.allocate = bind(self.library, "_arf_vec_init", pointer, [integer])
        self.release = bind(self.library, "_arf_vec_clear", None, [pointer, integer])
        self.dump = bind(self.library, "arf_dump_str", pointer, [pointer])
        self.free = bind(self.library, "flint_free", None, [pointer])
        self.isolate = bind(self.library, "acb_dirichlet_platt_isolate_local_hardy_z_zeros",
                            integer, [pointer, ctypes.POINTER(integer), integer, integer])

    def batch(self, first, requested, precision):
        if not (0 < first < 2**61 and 0 < requested <= 100000):
            raise ValueError("Invalid small fmpz index or allocation size")
        # arf_interval_struct in arf_types.h consists of two consecutive arf_structs.
        # _arf_vec_init(2*n) initializes precisely this sequence of managed objects.
        vector = self.allocate(2 * requested)
        try:
            index = ctypes.c_long(first)
            found = self.isolate(vector, ctypes.byref(index), requested, precision)
            return self.unpack(vector, requested, found)
        finally:
            self.release(vector, 2 * requested)

    def unpack(self, vector, requested, found):
        if not 0 <= found <= requested:
            raise ArithmeticError("Invalid certified count from FLINT")
        result = []
        for i in range(found):
            pair = []
            for side in range(2):
                point = vector + (2 * i + side) * ctypes.sizeof(Arf)
                text = self.dump(point)
                try:
                    mantissa, exponent = ctypes.string_at(text).split()
                    pair.append((int(mantissa, 16), int(exponent, 16)))
                finally:
                    self.free(text)
            result.append(tuple(pair))
        return result


def compare(first, second):
    a, b = first
    c, d = second
    shift = min(b, d)
    difference = (a << (b - shift)) - (c << (d - shift))
    return (difference > 0) - (difference < 0)


def check_brackets(intervals):
    previous = None
    for low, high in intervals:
        if low[0] <= 0 or high[0] <= 0 or compare(low, high) >= 0:
            raise ArithmeticError("A root needs a strictly ordered positive bracket")
        if previous is not None and compare(previous, low) > 0:
            raise ArithmeticError("Different indexed open brackets overlap internally")
        previous = high


def intersection(one, two):
    low = one[0] if compare(one[0], two[0]) >= 0 else two[0]
    high = one[1] if compare(one[1], two[1]) <= 0 else two[1]
    if compare(low, high) >= 0:
        raise ArithmeticError("Repeated index brackets must intersect")
    return low, high


def canonical(intervals):
    return b"".join((f"{a:x} {e:x}\t{b:x} {f:x}\n").encode("ascii")
                    for (a, e), (b, f) in intervals)


def create_block(isolator, block, directory, precision, shifted=None):
    first = ANCHOR + block * BLOCK_SIZE
    last = first + BLOCK_SIZE
    path = directory / f"{block:04d}.xz"
    manifest = path.with_suffix(".json")
    if path.exists() and manifest.exists():
        metadata = json.loads(manifest.read_text())
        if (metadata["first_index"] == first and metadata["last_index"] == last
                and hashlib.sha256(path.read_bytes()).hexdigest() == metadata["compressed_sha256"]):
            return
        raise ArithmeticError(f"Existing block {block} differs from its manifest")
    intervals, calls = [], []
    while len(intervals) <= BLOCK_SIZE:
        start = first + max(len(intervals) - 1, 0)
        # A failed local search can be moved backward into a different certified anchor.
        attempts = [(isolator, 0, 0), (isolator, 0, 32), (isolator, 8, 32), (isolator, 64, 64)]
        if shifted is not None:
            attempts.insert(0, (shifted, 0, 0))
        for engine, backup, extra in attempts:
            requested = last - start + 1 + backup
            raw = engine.batch(start - backup, requested, precision + extra)
            check_brackets(raw)
            batch = raw[backup:]
            if len(batch) <= int(bool(intervals)):
                continue
            calls.append({"first_index": start - backup, "requested": requested,
                          "returned": len(raw), "precision": precision + extra,
                          "stream_sha256": hashlib.sha256(canonical(raw)).hexdigest()})
            if shifted is not None and engine is shifted:
                calls[-1]["shifted_parameters"] = dict(shifted.last_parameters)
            if intervals:
                intervals[-1] = intersection(intervals[-1], batch[0])
                intervals.extend(batch[1:])
            else:
                intervals.extend(batch)
            break
        else:
            raise ArithmeticError(f"No certified progress at index {start}")
    if len(intervals) != BLOCK_SIZE + 1:
        raise ArithmeticError("Wrong complete block length")
    check_brackets(intervals)
    stream = canonical(intervals)
    packed = lzma.compress(stream, preset=3)
    temporary = path.with_suffix(f".{os.getpid()}.tmp")
    temporary.write_bytes(packed)
    temporary.replace(path)
    metadata = {"first_index": first, "last_index": last, "count": len(intervals),
                "calls": calls, "stream_sha256": hashlib.sha256(stream).hexdigest(),
                "compressed_sha256": hashlib.sha256(packed).hexdigest()}
    temporary = manifest.with_suffix(f".{os.getpid()}.tmp")
    temporary.write_text(json.dumps(metadata, indent=2) + "\n")
    temporary.replace(manifest)
    print(f"complete block {block}, indices {first} through {last}", flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--first-block", required=True, type=int)
    parser.add_argument("--stop-block", required=True, type=int,
                        help="exclusive block number; each block adds 10,000 new indices")
    parser.add_argument("--stride", type=int, default=1)
    parser.add_argument("--precision", type=int, default=DEFAULT_PRECISION)
    parser.add_argument("--output", type=Path, default=Path(__file__).parent / "blocks")
    parser.add_argument("--deadline-utc", type=int, default=None,
                        help="optional Unix timestamp after which no new block starts")
    parser.add_argument("--shifted", action="store_true",
                        help="try the explicitly centered native grid before the default grid")
    args = parser.parse_args()
    if not 0 <= args.first_block < args.stop_block or args.stride < 1:
        parser.error("invalid range")
    args.output.mkdir(parents=True, exist_ok=True)
    isolator = NativeIsolator()
    shifted = None
    if args.shifted:
        from shifted_isolator import ShiftedIsolator
        shifted = ShiftedIsolator()
    for block in range(args.first_block, args.stop_block, args.stride):
        if args.deadline_utc is not None and time.time() >= args.deadline_utc:
            break
        create_block(isolator, block, args.output, args.precision, shifted)


if __name__ == "__main__":
    main()
