"""JSON helpers that tolerate numpy scalars in reconnaissance dumps."""

from __future__ import annotations

import json
from typing import Any


def to_plain(obj: Any) -> Any:
    if isinstance(obj, dict):
        return {str(k): to_plain(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [to_plain(v) for v in obj]
    if hasattr(obj, "item") and callable(obj.item):
        try:
            return obj.item()
        except Exception:  # noqa: BLE001
            pass
    if isinstance(obj, (str, int, float, bool)) or obj is None:
        return obj
    return str(obj)


def dumps(obj: Any, **kwargs) -> str:
    return json.dumps(to_plain(obj), **kwargs)
