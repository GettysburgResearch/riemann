"""Authenticate and load the exact frozen #875 primitive source bytes.

Expected hashes are pinned in this consumer, independently of the receipt.
All source bytes are checked before any primitive executes. The loader compiles
those same verified bytes, so normal import resolution and cached bytecode do
not substitute a different primitive implementation.
"""
from pathlib import Path
from types import ModuleType
import hashlib
import json
import subprocess
import sys

HERE = Path(__file__).resolve().parent
PINNED_COMMIT = 'be149104721ae7b65b624c100118edfd7b76b69b'
PINNED_BASE = 'standalone/2026-09-12-astra-collision-chain-flow/'
EXPECTED_SHA256 = {
    'exact_interval.py': '083ef417bc5249e189fb08f1c7b9009ff69a97a19073ba2778e02512515bf427',
    'native_theta.py': '263271e3dac4f3316b20c0ac5d0e5e98ffef9ccd0573ed2aac3c9cd876f3d652',
    'research_algebra.py': '8a42a824a03944d808a1405edbefd7c0088fbba848d3aacc10facc65f2f9628b',
    'calibrated_chain.py': '59472097136edce1d39d81ff5707e86ad0d18852707ebea08bb99e1d2c859d98',
}


class SourceAuthenticationError(RuntimeError):
    pass


def expected_receipt():
    return {'commit': PINNED_COMMIT,
            'files': [{'path': PINNED_BASE + name, 'sha256': digest}
                      for name, digest in EXPECTED_SHA256.items()]}


def authenticate_bytes(name, raw):
    if hashlib.sha256(raw).hexdigest() != EXPECTED_SHA256[name]:
        raise SourceAuthenticationError('Pinned primitive source mismatch: ' + name)
    return raw


def verified_sources(directory=None):
    root = Path(directory) if directory is not None else HERE
    # Validate against consumer constants, never against hashes read from JSON.
    sources = {name: authenticate_bytes(name, (root / 'predecessor' / name).read_bytes())
               for name in EXPECTED_SHA256}
    receipt = json.loads((root / 'predecessor-provenance.json').read_text(encoding='utf-8'))
    if receipt != expected_receipt():
        raise SourceAuthenticationError('Pinned predecessor receipt mismatch')
    return sources


def load_primitives(directory=None):
    root = Path(directory) if directory is not None else HERE
    sources = verified_sources(root)  # Check ALL files before executing the first.
    loaded = {}
    absent = object()
    saved = {}
    try:
        for filename, raw in sources.items():
            name = filename[:-3]
            module = ModuleType(name)
            module.__file__ = str(root / 'predecessor' / filename)
            module.__package__ = ''
            saved[name] = sys.modules.get(name, absent)
            sys.modules[name] = module
            exec(compile(raw, module.__file__, 'exec'), module.__dict__)
            loaded[name] = module
    finally:
        for name, previous in saved.items():
            if previous is absent:
                sys.modules.pop(name, None)
            else:
                sys.modules[name] = previous
    return loaded


def find_repository(explicit=None):
    candidates = [Path(explicit)] if explicit is not None else [HERE, Path.cwd()]
    for directory in candidates:
        result = subprocess.run(
            ['git', '-C', str(directory), 'rev-parse', '--show-toplevel'],
            capture_output=True, text=True, check=False)
        if result.returncode == 0:
            repository = Path(result.stdout.strip()).resolve()
            present = subprocess.run(
                ['git', '-C', str(repository), 'cat-file', '-e', PINNED_COMMIT + '^{commit}'],
                capture_output=True, text=True, check=False)
            if present.returncode == 0:
                return repository
    raise RuntimeError('No Git checkout containing the pinned #875 commit was found; '
                       'pass --repo PATH to such a checkout. No fetch is performed.')


def read_pinned_file(repository, name):
    return subprocess.check_output(
        ['git', '-C', str(repository), 'show', PINNED_COMMIT + ':' + PINNED_BASE + name])
