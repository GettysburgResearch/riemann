#!/usr/bin/env python3
"""Generate one audited FLINT producer for an exact barycentric Pick finalist.

The source template is the proof-grade PR #56 frozen Pick producer.  This script
changes only two finite exact data blocks:

* the ordinate numerator ``T0 + j*2^27`` over the common denominator ``2^32``;
* the integer-scaled barycentric vector for the fixed dyadic node ladder.

It reconstructs the vector from the nodes and checks all moment cancellations
before touching the C source.  The generated C program still evaluates every
primitive ``xi'/xi`` value in two directed assemblies and leaves the sign to the
standard-library exact checker.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from functools import reduce
from math import gcd, lcm
from pathlib import Path
import re

X_BITS = [17, 15, 13, 11, 10, 9, 7, 5]
T0_NUMERATOR = 20225875608343121406355
VECTOR_RE = re.compile(
    r"static const char \*VECTOR\[NPOINTS\] = \{.*?\n\};",
    re.DOTALL,
)
T_RE = re.compile(r'static const char \*T_NUM = "[0-9-]+";')


def primitive_integer_vector() -> list[int]:
    nodes = [Fraction(1, 1 << bits) for bits in X_BITS]
    weights: list[Fraction] = []
    for i, x_i in enumerate(nodes):
        denominator = Fraction(1)
        for j, x_j in enumerate(nodes):
            if i != j:
                denominator *= x_i - x_j
        weights.append(1 / denominator)

    common = 1
    for value in weights:
        common = lcm(common, value.denominator)
    integers = [value.numerator * (common // value.denominator) for value in weights]
    divisor = reduce(gcd, (abs(value) for value in integers))
    integers = [value // divisor for value in integers]

    # Eight barycentric nodes annihilate monomials through degree six.
    for power in range(len(nodes) - 1):
        moment = sum(
            Fraction(coefficient) * node**power
            for coefficient, node in zip(integers, nodes)
        )
        if moment != 0:
            raise RuntimeError(f"barycentric moment {power} did not vanish: {moment}")
    if not any(integers):
        raise RuntimeError("generated zero vector")
    return integers


def generate(template: str, offset_index: int) -> str:
    vector = primitive_integer_vector()
    vector_lines = ",\n".join(f'    "{value}"' for value in vector)
    vector_block = "static const char *VECTOR[NPOINTS] = {\n" + vector_lines + "\n};"
    result, count = VECTOR_RE.subn(vector_block, template)
    if count != 1:
        raise RuntimeError(f"expected one VECTOR block, found {count}")

    numerator = T0_NUMERATOR + offset_index * (1 << 27)
    result, count = T_RE.subn(
        f'static const char *T_NUM = "{numerator}";', result
    )
    if count != 1:
        raise RuntimeError(f"expected one T_NUM declaration, found {count}")

    marker = "This file does not itself claim a counterexample."
    replacement = (
        marker
        + f"  Generated for exact offset j={offset_index} and the primitive "
        + "eight-node barycentric vector."
    )
    if marker in result:
        result = result.replace(marker, replacement, 1)
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("template", type=Path)
    parser.add_argument("offset_index", type=int)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    if not -32 <= args.offset_index <= 32:
        raise SystemExit("offset_index must lie in [-32,32]")
    source = args.template.read_text(encoding="utf-8")
    generated = generate(source, args.offset_index)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(generated, encoding="utf-8")
    print(
        {
            "offset_index": args.offset_index,
            "t_numerator": T0_NUMERATOR + args.offset_index * (1 << 27),
            "t_denominator": 1 << 32,
            "vector": primitive_integer_vector(),
        }
    )


if __name__ == "__main__":
    main()
