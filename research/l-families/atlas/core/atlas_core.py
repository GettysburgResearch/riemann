from __future__ import annotations

import hashlib
import json
import unicodedata
from pathlib import Path
from typing import Any


ATLAS_ROOT = Path(__file__).resolve().parents[1]


def normalize_json(value: Any) -> Any:
    if isinstance(value, str):
        return unicodedata.normalize("NFC", value)
    if isinstance(value, list):
        return [normalize_json(item) for item in value]
    if isinstance(value, dict):
        normalized: dict[str, Any] = {}
        for key, item in value.items():
            if not isinstance(key, str):
                raise TypeError("JSON object keys must be strings")
            normalized_key = unicodedata.normalize("NFC", key)
            if normalized_key in normalized:
                raise ValueError(f"duplicate key after NFC normalization: {normalized_key!r}")
            normalized[normalized_key] = normalize_json(item)
        return normalized
    if value is None or isinstance(value, (bool, int, float)):
        return value
    raise TypeError(f"unsupported JSON value: {type(value).__name__}")


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        normalize_json(value),
        allow_nan=False,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def sha256_hex(value: Any) -> str:
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def semantic_identity(kind: str, slug: str, identity_kernel: dict[str, Any]) -> tuple[str, str]:
    digest = sha256_hex(identity_kernel)
    return f"ATLAS.{kind}.{slug}.H{digest[:32]}", digest


def fraction_json(numerator: int, denominator: int) -> dict[str, int | str]:
    if denominator <= 0:
        raise ValueError("denominator must be positive")
    from math import gcd

    divisor = gcd(numerator, denominator)
    numerator //= divisor
    denominator //= divisor
    return {
        "numerator": numerator,
        "denominator": denominator,
        "text": f"{numerator}/{denominator}" if denominator != 1 else str(numerator),
    }


def _reject_duplicate_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        normalized_key = unicodedata.normalize("NFC", key)
        if normalized_key in result:
            raise ValueError(f"duplicate JSON key in {key!r}")
        result[normalized_key] = value
    return result


def _reject_constant(value: str) -> None:
    raise ValueError(f"non-finite JSON constant is forbidden: {value}")


def read_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(
            handle,
            object_pairs_hook=_reject_duplicate_pairs,
            parse_constant=_reject_constant,
        )


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(normalize_json(value), handle, allow_nan=False, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")
