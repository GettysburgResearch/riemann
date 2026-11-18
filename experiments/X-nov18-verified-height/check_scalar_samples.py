"""Audit deterministic scalar-Hardy sample transcripts against archived brackets."""
import argparse
import hashlib
import json
import lzma
from pathlib import Path


def verify(data, blocks):
    lines = data.splitlines()
    if not lines or len(lines) % 2:
        raise ValueError("Expected two scalar witnesses per block")
    for block in range(len(lines) // 2):
        archive = blocks / f"{block:04d}.xz"
        raw = lzma.decompress(archive.read_bytes())
        digest = hashlib.sha256(raw).digest()
        meta = json.loads(archive.with_suffix(".json").read_text())
        if digest.hex() != meta["stream_sha256"] or len(raw.splitlines()) != 10001:
            raise ValueError(f"Bracket stream digest or length mismatch in block {block}")
        first = int.from_bytes(digest[:16], "big") % 10001
        second = (first + 1 + int.from_bytes(digest[16:], "big") % 10000) % 10001
        for offset, row in enumerate(sorted((first, second))):
            b, j, index, left, right = map(int, lines[2 * block + offset].split())
            if ((b, j, index) != (block, row, 12363153437138 + block * 10000 + row)
                    or abs(left) != 1 or right != -left):
                raise ValueError(f"Invalid scalar crossing at block {block}, row {row}")
    return len(lines) // 2


def main():
    root = Path(__file__).parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=root / "scalar-samples.tsv.xz")
    parser.add_argument("--blocks", type=Path, default=root / "blocks")
    parser.add_argument("--archive", type=Path, help="write a compressed copy after validation")
    args = parser.parse_args()
    data = args.input.read_bytes()
    if args.input.suffix == ".xz":
        data = lzma.decompress(data)
    count = verify(data, args.blocks)
    if args.archive:
        temp = args.archive.with_suffix(".tmp")
        temp.write_bytes(lzma.compress(data))
        temp.replace(args.archive)
    print(f"Validated {2 * count} scalar Hardy crossings in {count} consecutive blocks")


if __name__ == "__main__":
    main()
