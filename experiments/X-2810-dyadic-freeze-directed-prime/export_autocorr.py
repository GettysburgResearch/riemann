#!/usr/bin/env python3
"""Export exact Gaussian-integer autocorrelations on one common dyadic scale."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from exact_vector import parse_vector, autocorrelation_numerators


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("vector", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    data = json.loads(args.vector.read_text(encoding="utf-8"))
    cells, bits, real, imag, _digest = parse_vector(data)
    auto_real, auto_imag = autocorrelation_numerators(real, imag)
    with args.output.open("w", encoding="utf-8") as stream:
        stream.write(f"{cells} {2 * bits}\n")
        for re, im in zip(auto_real, auto_imag):
            stream.write(f"{re} {im}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
