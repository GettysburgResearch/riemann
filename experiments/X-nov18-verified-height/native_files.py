"""Emit sha256sum-compatible checksums for a counted native checkpoint and all its call records."""
import argparse
import hashlib
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checkpoint", type=Path)
    args = parser.parse_args()
    base = args.checkpoint.resolve().parent
    checkpoint = json.loads(args.checkpoint.read_text())
    if (not isinstance(checkpoint.get("independent_guarded_count"), int)
            or checkpoint["expected_guarded_count"] != checkpoint["independent_guarded_count"]):
        raise ValueError("Checkpoint lacks matching independent guarded count")
    paths = [args.checkpoint.resolve()]
    paths.extend(base / name for name in ["isolate.py", "shifted_isolator.py", "check_frontier.py",
                                          "capture_default_grid.c", "check_grid_errors.py", "native_files.py"])
    ordered = hashlib.sha256()
    for number in range(checkpoint["complete_blocks"]):
        header = base / "blocks" / f"{number:04d}.json"
        archive = header.with_suffix(".xz")
        sidecar = base / "grid-errors" / header.name
        metadata = json.loads(header.read_text())
        errors = json.loads(sidecar.read_text())
        if (hashlib.sha256(archive.read_bytes()).hexdigest() != metadata["compressed_sha256"]
                or errors["stream_sha256"] != metadata["stream_sha256"] or errors["block"] != number):
            raise ArithmeticError(f"Archive or error-record mismatch for block {number}")
        for category, shifted in [("default_grid_calls", False), ("explicit_grid_calls", True)]:
            expected = [c["stream_sha256"] for c in metadata["calls"] if ("shifted_parameters" in c) == shifted]
            actual = [c["raw_stream_sha256"] for c in errors.get(category, [])]
            if actual != expected:
                raise ArithmeticError(f"Incomplete {category} error capture in block {number}")
        ordered.update(f"{number}\t{metadata['stream_sha256']}\n".encode("ascii"))
        paths.extend([header, archive, sidecar])
    if ordered.hexdigest() != checkpoint["ordered_stream_digest"]:
        raise ArithmeticError("Ordered native stream differs from counted checkpoint")
    for path in sorted(paths):
        print(f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.relative_to(base)}")


if __name__ == "__main__":
    main()
