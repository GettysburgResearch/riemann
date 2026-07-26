#!/usr/bin/env python3
"""Generate the PR #71 exact-ordinate direct-xi C producer from X-7501."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

OLD = "20225875608343121406355"
NEW = "20225875608341108140435"
EXPECTED_OCCURRENCES = 3
REVIEWED_SOURCE_SHA256 = (
    "1ff4f391dc78aecd2fc2e73a4da507551a77618c7850d005733ea06c3f90ec5c"
)
XI_COMMON_SCALE_POWER = 5_335_951_715_288
DEFAULT_X_BITS = (20, 18, 16, 14, 12, 10, 8, 6, 5)

OLD_REFLECTION = """    acb_one(reflected_s);
    acb_sub(reflected_s, reflected_s, s, prec);
    evaluate_xi(xi, s, prec);
    evaluate_xi(reflected_xi, reflected_s, prec);
"""

NEW_REFLECTION = """    /*
       Evaluate xi(1-s) without sending a negative ordinate to the
       Riemann--Siegel backend.  For r = 1-conj(s),

           conj(xi(r)) = xi(1-s),

       by conjugation symmetry.  This preserves the emitted functional-
       equation rectangle while both RS evaluations stay at positive height.
    */
    acb_conj(reflected_s, s);
    acb_neg(reflected_s, reflected_s);
    acb_add_ui(reflected_s, reflected_s, 1, prec);
    evaluate_xi(xi, s, prec);
    evaluate_xi(reflected_xi, reflected_s, prec);
    acb_conj(reflected_xi, reflected_xi);
"""

SCALE_DECLARATION_NEEDLE = (
    f'static const char *T_MANTISSA = "{NEW}";\n'
)
SCALE_DECLARATION_REPLACEMENT = (
    SCALE_DECLARATION_NEEDLE
    + f"static const slong XI_COMMON_SCALE_POWER = {XI_COMMON_SCALE_POWER}L;\n"
)
SCALE_VALUE_NEEDLE = "    mul4(xi, A, B, G, jet + 0, prec);\n"
SCALE_VALUE_REPLACEMENT = (
    SCALE_VALUE_NEEDLE
    + "    acb_mul_2exp_si(xi, xi, XI_COMMON_SCALE_POWER);\n"
)
SCALE_METADATA_NEEDLE = (
    '    flint_printf("\\"precision_bits\\":%wd,\\n", prec);\n'
)
SCALE_METADATA_REPLACEMENT = (
    SCALE_METADATA_NEEDLE
    + '    flint_printf("\\"common_xi_scale_power_of_two\\":%wd,\\n", '
    + "XI_COMMON_SCALE_POWER);\n"
)
X_BITS_DECLARATION = (
    "#define X_COUNT 9\n"
    "static const int X_BITS[X_COUNT] = {20, 18, 16, 14, 12, 10, 8, 6, 5};\n"
)


def patch_source(
    source: str, ordinate_numerator: str = NEW
) -> tuple[str, dict[str, object]]:
    if (
        re.fullmatch(r"[1-9][0-9]*", ordinate_numerator) is None
        or ordinate_numerator == OLD
    ):
        raise ValueError("new ordinate numerator must be positive and differ")
    source_sha256 = hashlib.sha256(source.encode("utf-8")).hexdigest()
    if source_sha256 != REVIEWED_SOURCE_SHA256:
        raise ValueError(
            "X-7501 source digest mismatch: review source drift before regenerating"
        )
    count = source.count(OLD)
    if count != EXPECTED_OCCURRENCES:
        raise ValueError(
            f"expected {EXPECTED_OCCURRENCES} exact ordinate occurrences, found {count}"
        )
    if ordinate_numerator in source:
        raise ValueError("requested ordinate already present in source")
    output = source.replace(OLD, ordinate_numerator)
    if output.replace(ordinate_numerator, OLD) != source:
        raise ValueError("source patch changed more than the exact ordinate")
    return output, {
        "old_ordinate_numerator": OLD,
        "new_ordinate_numerator": ordinate_numerator,
        "denominator": 1 << 32,
        "occurrences_replaced": count,
        "source_sha256": source_sha256,
        "patched_sha256": hashlib.sha256(output.encode("utf-8")).hexdigest(),
    }


def patch_positive_reflection(source: str) -> tuple[str, dict[str, object]]:
    count = source.count(OLD_REFLECTION)
    if count != 1:
        raise ValueError(
            f"expected one exact negative-height reflection block, found {count}"
        )
    output = source.replace(OLD_REFLECTION, NEW_REFLECTION)
    if output.replace(NEW_REFLECTION, OLD_REFLECTION) != source:
        raise ValueError("positive-height reflection patch changed unexpected text")
    return output, {
        "reflection_identity": "conj(xi(1-conj(s))) = xi(1-s)",
        "reflection_blocks_replaced": count,
        "negative_height_rs_calls_removed": True,
    }


def patch_horizontal_nodes(
    source: str, x_bits: tuple[int, ...]
) -> tuple[str, dict[str, object]]:
    if (
        len(x_bits) < 2
        or len(set(x_bits)) != len(x_bits)
        or any(isinstance(value, bool) or value < 1 or value > 62 for value in x_bits)
        or any(x_bits[index] <= x_bits[index + 1] for index in range(len(x_bits) - 1))
    ):
        raise ValueError("x-bit nodes must be unique integers decreasing from 1..62")
    if source.count(X_BITS_DECLARATION) != 1:
        raise ValueError("expected one exact horizontal-node declaration")
    replacement = (
        f"#define X_COUNT {len(x_bits)}\n"
        "static const int X_BITS[X_COUNT] = {"
        + ", ".join(str(value) for value in x_bits)
        + "};\n"
    )
    output = source.replace(X_BITS_DECLARATION, replacement)
    if output.replace(replacement, X_BITS_DECLARATION) != source:
        raise ValueError("horizontal-node patch changed unexpected text")
    encoded = json.dumps(list(x_bits), separators=(",", ":")).encode("ascii")
    return output, {
        "x_bits": list(x_bits),
        "x_bits_sha256": hashlib.sha256(encoded).hexdigest(),
    }


def patch_common_xi_scale(
    source: str, ordinate_numerator: str = NEW
) -> tuple[str, dict[str, object]]:
    declaration_needle = f'static const char *T_MANTISSA = "{ordinate_numerator}";\n'
    declaration_replacement = (
        declaration_needle
        + f"static const slong XI_COMMON_SCALE_POWER = {XI_COMMON_SCALE_POWER}L;\n"
    )
    replacements = (
        (declaration_needle, declaration_replacement),
        (SCALE_VALUE_NEEDLE, SCALE_VALUE_REPLACEMENT),
        (SCALE_METADATA_NEEDLE, SCALE_METADATA_REPLACEMENT),
    )
    output = source
    for needle, replacement in replacements:
        count = output.count(needle)
        if count != 1:
            raise ValueError(f"expected one common-scale patch target, found {count}")
        output = output.replace(needle, replacement)
    return output, {
        "common_xi_scale_power_of_two": XI_COMMON_SCALE_POWER,
        "common_scale_is_exact": True,
        "common_scale_scope": "all emitted xi rectangles",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source",
        type=Path,
        default=Path(__file__).resolve().parents[1]
        / "X-7501-xi-modulus"
        / "rs_modulus.c",
    )
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--ordinate-numerator", default=NEW)
    parser.add_argument("--x-bits", type=int, nargs="+")
    args = parser.parse_args()
    source = args.source.read_text(encoding="utf-8")
    output, manifest = patch_source(source, args.ordinate_numerator)
    if args.x_bits is not None:
        output, node_manifest = patch_horizontal_nodes(output, tuple(args.x_bits))
        manifest.update(node_manifest)
    else:
        encoded = json.dumps(
            list(DEFAULT_X_BITS), separators=(",", ":")
        ).encode("ascii")
        manifest.update(
            {
                "x_bits": list(DEFAULT_X_BITS),
                "x_bits_sha256": hashlib.sha256(encoded).hexdigest(),
            }
        )
    output, reflection_manifest = patch_positive_reflection(output)
    output, scale_manifest = patch_common_xi_scale(
        output, args.ordinate_numerator
    )
    manifest.update(reflection_manifest)
    manifest.update(scale_manifest)
    manifest["patched_sha256"] = hashlib.sha256(output.encode("utf-8")).hexdigest()
    args.output.write_text(output, encoding="utf-8")
    if args.manifest:
        args.manifest.write_text(
            json.dumps(manifest, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    print(json.dumps(manifest, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
