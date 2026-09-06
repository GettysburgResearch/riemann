#!/usr/bin/env python3
"""Authenticate the scoped release checkout before running the frozen resolver.

This is a source-integrity/navigation check, NOT a proof checker, Lean build,
complete historical audit, or public-launch clearance. No network is used.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import posixpath
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import unicodedata
from urllib.parse import unquote, urlsplit

RELEASE = 'integration/2026-09-06'
ROOT = Path(__file__).resolve().parents[3]
TREE_PINS = {
    'reviews/A': '67660b470e7b7b8946d9c1918f1cf25946a9a87d',
    'reviews/B': '893b62b195d8e2508226d437a861a37a191cb50c',
    'reviews/C': '24312b3398f050d7995f0a909d6e70237a32c395',
    'reviews/D': 'd3a136e4558b574c906ca679793bf9b67389278d',
    'reviews/D-final': '5b37dae592cb49614f8e9b5819d53aea0eb0ea16',
    'reviews/D-pass3': 'e0ec904c81b2d080a2a42abef35e7987254040cc',
    'reviews/D-pass4': '1eec1698d5a55dc84246ed04de6a108d21914619',
}
HISTORY_PINS = {
    'integration/2026-08-01': '59278229101a644b95dbd4b8c587bb384040e145',
    'integration/2026-08-11': 'd1e4a28811bc2fd31ee6f57ca713f7a83a296afa',
    'integration/2026-08-16': '38f3ff967596e1c5e5b8cfea39c7f09e3febfc6f',
    'integration/2026-08-18': 'f83ab26de56df0e21672fa2b5c8ac236a5b82cb8',
    'integration/2026-08-20': '9f7e7e77ef63ca98762387e9a6ef88026746edc1',
    'integration/2026-08-22': '6680eaa16d47318e3407cdc973fd1d1c765acd30',
}
FROZEN_TREES = dict(TREE_PINS, **HISTORY_PINS)
PAYLOAD_PINS = {
    'validate.py': 'b0f557189916ab1698a0170d4055fcc756a78199',
    'independent_fixtures.py': '873d56759ea517943286706670fe373cd7dbd1df',
    'RELEASE.json': '7bd18c3adfe624f9604c32516074bafd2733d3e1',
    'SOURCE_FREEZE.json': '33bf88880aee3846d6cf69374b8f529eb39127fc',
    'DECISIONS.json': '094d75445611b0b155b6edf309e02732f6bca593',
    'PROGRAMMES.json': 'ef32cb825cca80d8f13f53c8744da1aebd87c5cf',
    'REVIEW_TABLES.json': 'd102f7c62cd9c436530b69a85f7289f1435466c8',
    'FRONTIER_GRAPH.json': '88dbd3f04bb4e15531591082563fffad58492ce6',
    'PROOF_PAYLOADS.json': '563283b1f3201e9563d5d923dc60331a32357c25',
}
NAVIGATION = (
    'README.md', 'STATUS.md', 'RESULTS.md', 'PROOF_GRAPH.md', 'OPEN_CUTS.md',
    'REFUTATIONS.md', 'COMPUTATIONS.md', 'HISTORY.md', 'PROGRAMMES.md',
    'FORMALIZATION.md', 'FORMAL_STATUS.md', 'RELEASE_READINESS.md',
    'AGENTS.md', 'CONTRIBUTING.md', 'docs/REVIEWING.md', 'formal/README.md',
    'canonical/README.md', 'canonical/2026-09-06/README.md',
    'research/README.md', 'research/RESULTS_INDEX.md', 'research/integrated/README.md',
    'research/integrated/CURRENT_RESULTS.md',
    'research/integrated/2026-09-06/README.md',
    'research/integrated/2026-09-06/MATHEMATICS.md',
    'research/integrated/2026-09-06/proof-extracts/README.md',
    RELEASE + '/hardening/README.md',
)
SCOPES = ('reviews', 'canonical/2026-08-22', 'canonical/2026-09-06',
          'canonical/CURRENT.json', RELEASE, 'research/integrated/2026-09-06',
          '.github/workflows/integration-2026-09-06.yml') + NAVIGATION


def require(value: bool, message: str) -> None:
    if not value:
        raise ValueError(message)


def pairs(items):
    result = {}
    for key, value in items:
        require(key not in result, 'duplicate JSON key: ' + key)
        result[key] = value
    return result


def decode_json(data: bytes):
    def bad_number(value):
        raise ValueError('nonfinite JSON number: ' + value)
    return json.loads(data, object_pairs_hook=pairs, parse_constant=bad_number)


def blob(data: bytes) -> str:
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()


def safe_path(root: Path, name: str) -> Path:
    require(type(name) is str and bool(name), 'empty/nonstring source path')
    p = PurePosixPath(name)
    require(not p.is_absolute() and '..' not in p.parts and '.' not in p.parts
            and '.git' not in p.parts and ':' not in name and '\\' not in name
            and not any(ord(c) < 32 for c in name), 'unsafe source path: ' + name)
    current = root
    for part in p.parts:
        current = current / part
        require(not current.is_symlink(), 'symlink source component: ' + name)
    return current


def git(root: Path, *args: str) -> bytes:
    env = dict(os.environ, GIT_NO_REPLACE_OBJECTS='1', GIT_TERMINAL_PROMPT='0')
    return subprocess.check_output(
        ['git', '-c', 'core.hooksPath=/dev/null', *args], cwd=root, env=env)


def tracked_tree(root: Path) -> dict[str, tuple[str, str, str]]:
    result = {}
    for cell in git(root, 'ls-tree', '-r', '-z', '--full-tree', 'HEAD').split(b'\0'):
        if not cell:
            continue
        header, raw_path = cell.split(b'\t', 1)
        mode, kind, oid = header.decode('ascii').split()
        name = raw_path.decode('utf-8')
        safe_path(root, name)
        require(name not in result, 'duplicate tracked source path')
        result[name] = (mode, kind, oid)
    require(bool(result), 'empty committed tree')
    return result


def read_committed(root: Path, tree: dict, name: str) -> bytes:
    p = safe_path(root, name)
    require(name in tree, 'untracked/missing input: ' + name)
    mode, kind, oid = tree[name]
    require(kind == 'blob' and mode in {'100644', '100755'}, 'unsupported input mode: ' + name)
    require(p.is_file(), 'missing working-tree file: ' + name)
    require(p.stat().st_size <= 8_000_000, 'input exceeds bounded file size: ' + name)
    data = p.read_bytes()
    require(blob(data) == oid, 'working bytes do not match HEAD: ' + name)
    return data


def authenticate(root: Path, tree: dict, scopes=SCOPES, pins=FROZEN_TREES) -> dict:
    for path, expected in pins.items():
        actual = git(root, 'rev-parse', 'HEAD:' + path).decode().strip()
        require(actual == expected, 'frozen source tree changed: ' + path)
    names = sorted(n for n in tree if any(n == s or n.startswith(s + '/') for s in scopes))
    require(bool(names), 'empty authentication scope')
    total = 0
    seal = hashlib.sha256()
    for name in names:
        data = read_committed(root, tree, name)
        total += len(data)
        require(total <= 150_000_000, 'authentication scope exceeds byte budget')
        seal.update(name.encode() + b'\0' + tree[name][2].encode() + b'\0')
    # Include ignored files too: they must not shadow an authenticated input.
    extra = git(root, 'ls-files', '--others', '-z', '--', *scopes)
    require(not extra, 'untracked files inside authenticated scope')
    return {'files': len(names), 'bytes': total, 'path_blob_sha256': seal.hexdigest()}


def prose(text: str) -> str:
    lines = []
    fence = None
    for line in text.splitlines():
        mark = re.match(r'^\s*(`{3,}|~{3,})', line)
        if mark:
            token = mark.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is None:
            lines.append(line)
    return '\n'.join(lines)


def anchors(text: str) -> set[str]:
    text = prose(text)
    answer = set(re.findall(r'<a\s+(?:id|name)=[\"\']([^\"\']+)', text, re.I))
    used = {}
    for match in re.finditer(r'^\s{0,3}#{1,6}\s+(.+?)\s*#*$', text, re.M):
        title = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', match.group(1))
        title = re.sub(r'<[^>]+>', '', title).lower()
        title = ''.join(c for c in title if c in ' _-' or unicodedata.category(c)[0] in 'LN')
        title = title.replace(' ', '-')
        number = used.get(title, 0)
        used[title] = number + 1
        answer.add(title if number == 0 else title + '-' + str(number))
    return answer


def check_links(root: Path, tree: dict, documents=NAVIGATION) -> dict:
    checked = 0
    external = 0
    for name in documents:
        text = prose(read_committed(root, tree, name).decode('utf-8'))
        # Math divided differences such as [a,b](f) are not Markdown links.
        text = re.sub(r'\\\[.*?\\\]', '', text, flags=re.S)
        text = re.sub(r'\\\(.*?\\\)', '', text, flags=re.S)
        text = re.sub(r'\$\$.*?\$\$', '', text, flags=re.S)
        text = re.sub(r'(?<!\$)\$(?!\$)[^\n$]*\$', '', text)
        # Inline and reference-definition links, excluding literal inline code.
        text = re.sub(r'(`+).*?\1', '', text)
        links = re.findall(r'\[[^\]\n]*\]\((<[^>]+>|[^\s)]+)(?:\s+[\"\'][^\n]*?[\"\'])?\)', text)
        links += re.findall(r'^\s*\[[^\]]+\]:\s*(\S+)', text, re.M)
        for url in links:
            url = url.strip('<>')
            u = urlsplit(url)
            if u.scheme or u.netloc:
                require(u.scheme in {'https', 'http', 'mailto'} or (not u.scheme and bool(u.netloc)), 'unsafe link scheme in ' + name)
                external += 1
                continue
            raw = unquote(u.path)
            # Git/Markdown paths are POSIX, regardless of the host OS.
            p = PurePosixPath(name).parent / raw if raw else PurePosixPath(name)
            if raw.startswith('/'):
                p = PurePosixPath(raw.lstrip('/'))
            normalized = posixpath.normpath(p.as_posix())
            require(normalized != '..' and not normalized.startswith('../'), 'escaping link in ' + name)
            target = normalized
            if target not in tree:
                target = target.rstrip('/') + '/README.md'
            require(target in tree, 'broken local link: ' + name + ' -> ' + url)
            if u.fragment and target.endswith('.md'):
                available = anchors(read_committed(root, tree, target).decode('utf-8'))
                require(unquote(u.fragment) in available, 'broken local anchor: ' + name + ' -> ' + url)
            checked += 1
    return {'documents': len(documents), 'local_links_and_anchors': checked,
            'external_links_not_fetched': external,
            'scope': 'explicit current entry pages; not archived proof/report internals'}


def verify_pointer(pointer: dict) -> None:
    require(pointer == {
        'release': '2026-09-06', 'manifest': RELEASE + '/RELEASE.json',
        'resolver': RELEASE + '/hardening/verify.py', 'previous_release': '2026-08-22',
        'rh_proved': False,
    } and type(pointer.get('rh_proved')) is bool, 'current resolver pointer mismatch')


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    root = ROOT.resolve()
    out = args.output.resolve()
    require(not out.is_relative_to(root), 'output must be outside the repository')
    require(not out.exists() or (out.is_dir() and not any(out.iterdir())), 'output must be new or empty')
    head = git(root, 'rev-parse', 'HEAD').decode().strip()
    tree = tracked_tree(root)
    before = authenticate(root, tree)
    for name, expected in PAYLOAD_PINS.items():
        require(blob(read_committed(root, tree, RELEASE + '/' + name)) == expected, 'published payload pin changed: ' + name)
    verify_pointer(decode_json(read_committed(root, tree, 'canonical/CURRENT.json')))
    links = check_links(root, tree)
    # Only the two pinned integrator modules execute. Archived research does not.
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', GIT_NO_REPLACE_OBJECTS='1')
    completed = subprocess.run(
        [sys.executable, '-I', '-S', '-B', *(['-O'] if sys.flags.optimize else []),
         str(root / RELEASE / 'validate.py'), '--output', str(out)],
        cwd=root, env=env, check=True, capture_output=True)
    old = decode_json((out / 'validation.json').read_bytes())
    require(old['marker'] == 'PASS_SCOPED_INTEGRATION_FULL_CHECKOUT', 'wrong underlying validation mode')
    require(old['checkout_commit'] == head, 'underlying checkout changed')
    require(git(root, 'rev-parse', 'HEAD').decode().strip() == head, 'HEAD changed during verification')
    require(authenticate(root, tracked_tree(root)) == before, 'inputs changed during verification')
    (out / 'resolver.stdout').write_bytes(completed.stdout)
    report = {
        'marker': 'PASS_AUTHENTICATED_SCOPED_RELEASE', 'checkout_commit': head,
        'checkout_tree': git(root, 'rev-parse', 'HEAD^{tree}').decode().strip(),
        'authenticated_inputs': before, 'navigation': links, 'frozen_review_trees': len(TREE_PINS),
        'frozen_payload_files': len(PAYLOAD_PINS), 'historical_release_trees': len(HISTORY_PINS),
        'legacy_validation': old['marker'],
        'whole_repository_checked': False, 'archived_programs_executed': False,
        'fresh_lean_build': False, 'public_launch_cleared': False, 'rh_proved': False,
    }
    (out / 'hardening.json').write_text(json.dumps(report, sort_keys=True, indent=2) + '\n')
    print(json.dumps(report, sort_keys=True, indent=2))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        print('FAIL_AUTHENTICATED_SCOPED_RELEASE: ' + str(error), file=sys.stderr)
        sys.exit(1)
