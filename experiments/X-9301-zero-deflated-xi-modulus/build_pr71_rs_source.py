#!/usr/bin/env python3
"""Generate the PR #71 exact-ordinate direct-xi C producer from X-7501."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

OLD = "20225875608343121406355"
NEW = "20225875608341108140435"
EXPECTED_OCCURRENCES = 3

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


def patch_source(source: str) -> tuple[str, dict[str, object]]:
    count = source.count(OLD)
    if count != EXPECTED_OCCURRENCES:
        raise ValueError(
            f"expected {EXPECTED_OCCURRENCES} exact ordinate occurrences, found {count}"
        )
    if NEW in source:
        raise ValueError("PR #71 ordinate already present in source")
    output = source.replace(OLD, NEW)
    if output.replace(NEW, OLD) != source:
        raise ValueError("source patch changed more than the exact ordinate")
    return output, {
        "old_ordinate_numerator": OLD,
        "new_ordinate_numerator": NEW,
        "denominator": 1 << 32,
        "occurrences_replaced": count,
        "source_sha256": hashlib.sha256(source.encode("utf-8")).hexdigest(),
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
    args = parser.parse_args()
    source = args.source.read_text(encoding="utf-8")
    output, manifest = patch_source(source)
    output, reflection_manifest = patch_positive_reflection(output)
    manifest.update(reflection_manifest)
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
