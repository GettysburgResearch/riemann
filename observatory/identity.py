"""Stable artifact identities across Python JSON and browser JSON round-trips.

For schema 2, finite JSON numbers within binary64's exact integer range are
encoded by their IEEE-754 value, not incidental `1` versus `1.0` formatting.
Exact large integers/coordinates must be decimal strings at API boundaries.
This is a versioned application encoding, NOT an implementation of RFC 8785.
"""
from __future__ import annotations
import hashlib
import json
import math

ALGORITHM = 'observatory-f64-v1'


def canonical_bytes(value):
    def normalize(obj):
        if obj is None:
            return ['null']
        if isinstance(obj, bool):
            return ['bool', obj]
        if isinstance(obj, int) and abs(obj) > 2**53:
            return ['integer', str(obj)]
        if isinstance(obj, (int, float)):
            number = float(obj)
            if not math.isfinite(number):
                raise ValueError('Nonfinite numbers cannot identify a numerical artifact')
            return ['number', (0.0 if number == 0 else number).hex()]
        if isinstance(obj, str):
            return ['string', obj]
        if isinstance(obj, list):
            return ['array', [normalize(v) for v in obj]]
        if isinstance(obj, dict) and all(isinstance(k, str) for k in obj):
            return ['object', [[k, normalize(obj[k])] for k in sorted(obj)]]
        raise ValueError(f'Unsupported artifact type: {type(obj).__name__}')
    return json.dumps(normalize(value), ensure_ascii=True, separators=(',', ':'), allow_nan=False).encode()


def content_id(value):
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def result_id(result):
    body = {k: v for k, v in result.items() if k != 'result_id'}
    if body.get('schema_version') == 1:
        # Retained solely for exact old-file imports. A v1 browser round-trip may
        # change numeric spelling; refusal is safer than silently repairing a hash.
        raw = json.dumps(body, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()
        return hashlib.sha256(raw).hexdigest()
    if body.get('schema_version') != 2 or body.get('hash_algorithm') != ALGORITHM:
        raise ValueError('Unknown result schema or hash algorithm')
    return content_id(body)


def strict_loads(raw):
    def pairs(items):
        out = {}
        for key, value in items:
            if key in out:
                raise ValueError(f'Duplicate JSON key: {key}')
            out[key] = value
        return out
    def nonfinite(value):
        raise ValueError(f'Nonfinite JSON token: {value}')
    return json.loads(raw, object_pairs_hook=pairs, parse_constant=nonfinite)
