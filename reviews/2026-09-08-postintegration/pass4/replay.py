#!/usr/bin/env python3
"""Source-pinned final-review replays. Not an RH verifier or a proof kernel.

The archived producer modules are compiled from authenticated bytes, not loaded
through the import path. --expect uses duplicate-free, float-free JSON and a
canonical comparison; --emit is an explicitly named reconstruction mode.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import sys
import types

ROOT = Path(__file__).resolve().parent
PINS = {
    'FR/interval_core.py': '92f484bc6bc7b12bf26313bd7d323c637cd834b9',
    'FR/certificate.py': 'dbf67ac52636916a59a9c7a11aa87356518143bc',
    'CD/certificate.py': 'a0f15cd4fdef7cc6aa24bfea2939e04b08d19525',
    'MW/certify.py': '3d1e3b10135a8504a5d3639b507211014be7eecc',
    'SSQ/check.py': 'a8e35ea57c3a5cad5872e5b9d1134ae42ca35e6a',
}
RESULT_SHA256 = {
    'FR': 'ef76ca01c9b32456db9f214f6a210f304f8b10563bbaa7b8f014e32d87d84bcf',
    'CD': '2fb2b2961ad9d6ec1a24fe60a3e05c500ca3a4bd246ce2e1965f80ab046f3ecb',
    'MW': 'ddaa01ec89167f7604939711c548ce80e856eb8197bf34b566e69439883dc9d6',
    'SSQ': 'e7a80214068439ae01bb3714825634dd821480117d6ac1f478546725d2edbe06',
}


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def canonical(obj: object) -> str:
    return json.dumps(obj, sort_keys=True, indent=2, ensure_ascii=True,
                      allow_nan=False) + '\n'


def strict_json(raw: str) -> object:
    def pairs(items):
        out = {}
        for key, value in items:
            require(key not in out, 'duplicate JSON key: ' + key)
            out[key] = value
        return out
    def bad(value):
        raise ValueError('floating/nonfinite JSON value: ' + value)
    return json.loads(raw, object_pairs_hook=pairs,
                      parse_float=bad, parse_constant=bad)


def authenticate(source_root: Path) -> dict[str, bytes]:
    require(source_root.is_dir() and not source_root.is_symlink(), 'source root')
    actual = set()
    for path in source_root.rglob('*'):
        require(not path.is_symlink(), 'source symlink')
        rel = path.relative_to(source_root).as_posix()
        if path.is_dir():
            require(rel in {'FR', 'CD', 'MW', 'SSQ'}, 'unexpected source directory')
        else:
            require(path.is_file(), 'nonregular source')
            actual.add(rel)
    require(actual == set(PINS), 'source inventory mismatch')
    consumed = {}
    for name, expected in PINS.items():
        raw = (source_root/name).read_bytes()
        blob = hashlib.sha1(f'blob {len(raw)}\0'.encode()+raw).hexdigest()
        require(blob == expected, 'source blob mismatch: '+name)
        consumed[name] = raw
    return consumed


def module(raw: bytes, name: str) -> types.ModuleType:
    m = types.ModuleType(name)
    sys.modules[name] = m
    exec(compile(raw, name, 'exec'), m.__dict__)
    return m


def reconstruct(packet: str, source_root: Path = ROOT/'sources') -> dict:
    consumed = authenticate(source_root)
    if packet == 'FR':
        core = module(consumed['FR/interval_core.py'], 'review_fr_core')
        p = module(consumed['FR/certificate.py'], 'review_fr_producer')
        observed = p.full_certificate(core)
        require(observed['half_cells'] == 4094, 'FR cell coverage')
        require(int(observed['ideal_full_error']['hi'])*1200 < core.SCALE,
                'FR full-tail threshold')
    elif packet == 'CD':
        observed = module(consumed['CD/certificate.py'], 'review_cd').run()
    elif packet == 'MW':
        observed = module(consumed['MW/certify.py'], 'review_mw').compute()
    elif packet == 'SSQ':
        observed = module(consumed['SSQ/check.py'], 'review_ssq').run()
    else:
        raise ValueError('unknown packet')
    digest = hashlib.sha256(canonical(observed).encode()).hexdigest()
    require(digest == RESULT_SHA256[packet], 'frozen reconstructed output changed')
    return observed


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--packet', choices=tuple(RESULT_SHA256), required=True)
    ap.add_argument('--source-root', type=Path, default=ROOT/'sources')
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument('--expect', type=Path)
    mode.add_argument('--emit', action='store_true')
    args = ap.parse_args()
    try:
        retained = None
        if args.expect:
            require(args.expect.is_file() and not args.expect.is_symlink(), 'receipt file')
            require(args.expect.stat().st_size <= 1048576, 'receipt size cap')
            retained = strict_json(args.expect.read_text(encoding='utf-8'))
            require(type(retained) is dict, 'receipt must be an object')
            # Early refusal is a type/content check, never a substitute for replay.
            require(hashlib.sha256(canonical(retained).encode()).hexdigest()
                    == RESULT_SHA256[args.packet], 'typed frozen receipt mismatch')
        observed = reconstruct(args.packet, args.source_root)
        if retained is not None:
            require(canonical(retained) == canonical(observed), 'primitive replay mismatch')
            print(canonical({'status': 'PASS_SOURCE_PINNED_REPLAY', 'packet': args.packet,
                             'result_sha256': RESULT_SHA256[args.packet],
                             'rh_proved': False}), end='')
        else:
            print(canonical(observed), end='')
        return 0
    except (ValueError, TypeError, KeyError, OSError, ArithmeticError) as exc:
        print('REJECT: '+str(exc), file=sys.stderr)
        return 2

if __name__ == '__main__':
    raise SystemExit(main())
