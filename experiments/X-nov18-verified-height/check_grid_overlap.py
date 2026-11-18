"""Re-isolate across the default/explicit grid transition using both native configurations."""

import hashlib
import json
from pathlib import Path
import lzma

from check_frontier import decode
from isolate import ANCHOR, BLOCK_SIZE, NativeIsolator, canonical, check_brackets, intersection
from shifted_isolator import ShiftedIsolator


def main():
    boundary = ANCHOR + 50 * BLOCK_SIZE
    start = boundary - 1000
    requested, precision = 3500, 104
    directory = Path(__file__).parent / "blocks"
    archives = {}
    for number in (49, 50):
        data = lzma.decompress((directory / f"{number:04d}.xz").read_bytes())
        manifest = json.loads((directory / f"{number:04d}.json").read_text())
        if hashlib.sha256(data).hexdigest() != manifest["stream_sha256"]:
            raise ValueError("Corrupt comparison stream")
        archives[number] = (decode(data), manifest["stream_sha256"])
    native, shifted = NativeIsolator(), ShiftedIsolator()
    output = {"start_index": start, "configuration_boundary_index": boundary,
              "requested": requested, "precision": precision,
              "archive_streams": {n: item[1] for n, item in archives.items()}}
    for name, engine in [("default", native), ("explicit", shifted)]:
        raw = engine.batch(start, requested, precision)
        check_brackets(raw)
        if start + len(raw) <= boundary + 1:
            raise ArithmeticError("Native batch did not cross the configuration transition")
        for index, bracket in enumerate(raw, start=start):
            number, row = divmod(index - ANCHOR, BLOCK_SIZE)
            intersection(bracket, archives[number][0][row])
        output[name] = {"matched_intervals": len(raw),
                        "intervals_beyond_boundary": start+len(raw)-1-boundary,
                        "raw_stream_sha256": hashlib.sha256(canonical(raw)).hexdigest()}
        if name == "explicit":
            output[name]["grid_parameters"] = dict(engine.last_parameters)
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
