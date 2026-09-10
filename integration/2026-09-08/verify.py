#!/usr/bin/env python3
"""Check the committed integration candidate, not a theorem or publication verdict.

Offline, standard library only. No archived research program executes. Run the
unchanged published-baseline verifier separately as documented in README.md.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import posixpath
import re
import subprocess
import sys
import unicodedata
from urllib.parse import unquote, urlsplit

BASE = 'f99d9e3908dde4865377c75d9ca051c1f545bf4f'
BASE_TREE = '8bddd12122e8a772683c9ed0b37dbcb945036893'
REVIEW = 'reviews/2026-09-08-postintegration'
REVIEW_TREE = '52836cd65e9e5c5bbe6f8b70e4e43da0aae382fa'
RELEASE = 'integration/2026-09-08'
GUIDE = 'research/integrated/native_sources'
EDITABLE = {
    'README.md', 'STATUS.md', 'RESULTS.md', 'PROGRAMMES.md', 'PROOF_GRAPH.md',
    'OPEN_CUTS.md', 'REFUTATIONS.md', 'COMPUTATIONS.md', 'research/README.md',
    'research/integrated/CURRENT_RESULTS.md', 'integration/README.md',
}
FIELDS = ['packet', 'current_statement', 'principal_files', 'mandatory_repairs']


def require(condition, message):
    if not condition:
        raise ValueError(message)


def pairs(items):
    result = {}
    for key, value in items:
        require(key not in result, 'duplicate JSON key: ' + key)
        result[key] = value
    return result


def decode(data):
    def bad(value):
        raise ValueError('nonfinite number: ' + value)
    return json.loads(data, object_pairs_hook=pairs, parse_constant=bad)


def blob(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()


def safe_name(name):
    require(type(name) is str and bool(name), 'empty/nonstring path')
    p = PurePosixPath(name)
    require(not p.is_absolute() and all(x not in {'.', '..', '.git', ''} for x in name.split('/'))
            and '\\' not in name and ':' not in name and not any(ord(c) < 32 for c in name),
            'unsafe path: ' + name)
    return name


def git(root, *args):
    env = dict(os.environ, GIT_NO_REPLACE_OBJECTS='1', GIT_TERMINAL_PROMPT='0')
    return subprocess.check_output(['git', '-c', 'core.hooksPath=/dev/null', *args], cwd=root, env=env)


def tree(root, ref):
    answer = {}
    for cell in git(root, 'ls-tree', '-r', '-z', '--full-tree', ref).split(b'\0'):
        if cell:
            header, raw = cell.split(b'\t', 1)
            name = safe_name(raw.decode('utf-8'))
            require(name not in answer, 'duplicate path')
            answer[name] = tuple(header.decode('ascii').split())
    require(bool(answer), 'empty tree')
    return answer


def read(root, index, name):
    safe_name(name)
    require(name in index, 'missing committed file: ' + name)
    mode, kind, oid = index[name]
    require(mode in {'100644', '100755'} and kind == 'blob', 'unsupported mode: ' + name)
    p = root
    for part in name.split('/'):
        p = p / part
        require(not p.is_symlink(), 'symlink: ' + name)
    require(p.is_file() and p.stat().st_size <= 8_000_000, 'missing/oversized file: ' + name)
    data = p.read_bytes()
    require(blob(data) == oid, 'working bytes differ from HEAD: ' + name)
    return data


def inside(name, roots):
    return any(name == p or name.startswith(p + '/') for p in roots)


def check_preservation(old, current, roots):
    for name, value in old.items():
        require(name in current, 'baseline deletion: ' + name)
        require(current[name] == value or name in EDITABLE, 'unauthorized baseline change: ' + name)
    for name in current.keys() - old.keys():
        require(inside(name, roots) or name == 'standalone/README.md', 'unselected addition: ' + name)


def rows(data, fields=None):
    reader = csv.DictReader(io.StringIO(data.decode('utf-8')), delimiter='\t')
    require(reader.fieldnames is not None and len(set(reader.fieldnames)) == len(reader.fieldnames), 'bad TSV header')
    if fields is not None:
        require(reader.fieldnames == fields, 'unexpected TSV schema')
    result = list(reader)
    require(bool(result) and all(None not in r and all(type(v) is str for v in r.values()) for r in result), 'malformed TSV row')
    return result


def check_selection(selected, reviewed, current):
    expected = {r['packet']: r for r in reviewed}
    require(len(reviewed) == len(expected) == 45, 'review must have exactly 45 distinct packets')
    require(len(selected) == 45 and {r['packet'] for r in selected} == set(expected), 'selection coverage mismatch')
    enriched = []
    for r in selected:
        require(set(r) == set(FIELDS), 'unexpected selection fields')
        source = expected[r['packet']]
        require(r['mandatory_repairs'] == source['mandatory_repairs'], 'repair drift: ' + r['packet'])
        require(r['current_statement'].startswith(GUIDE + '/') and r['current_statement'] in current, 'missing current statement')
        names = r['principal_files'].split(';')
        require(len(names) == len(set(names)) and bool(names), 'invalid principal file list')
        for name in names:
            require(safe_name(source['packet_path'] + '/' + name) in current, 'missing principal source: ' + r['packet'] + '/' + name)
        enriched.append(dict(source, **r))
    return enriched


def prose(text):
    kept, fence = [], None
    for line in text.splitlines():
        mark = re.match(r'^\s*(`{3,}|~{3,})', line)
        if mark:
            token = mark.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
        elif fence is None:
            kept.append(line)
    return '\n'.join(kept)


def anchors(text):
    text = prose(text)
    found = set(re.findall(r'<a\s+(?:id|name)=[\"\']([^\"\']+)', text, re.I))
    used = {}
    for title in re.findall(r'^\s{0,3}#{1,6}\s+(.+?)\s*#*$', text, re.M):
        title = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', title)
        title = re.sub(r'<[^>]+>', '', title).lower()
        title = ''.join(c for c in title if c in ' _-' or unicodedata.category(c)[0] in 'LN').replace(' ', '-')
        count = used.get(title, 0)
        used[title] = count + 1
        found.add(title if count == 0 else title + '-' + str(count))
    return found


def link_target(document, url):
    u = urlsplit(url.strip('<>'))
    if u.scheme or u.netloc:
        require(u.scheme in {'http', 'https', 'mailto'} or (not u.scheme and u.netloc), 'unsafe link scheme')
        return None, None
    raw = unquote(u.path)
    path = (posixpath.join(posixpath.dirname(document), raw) if raw else document)
    if raw.startswith('/'):
        path = raw.lstrip('/')
    return safe_name(posixpath.normpath(path)), unquote(u.fragment)


def check_links(root, current, documents):
    count, external = 0, 0
    for name in documents:
        text = prose(read(root, current, name).decode('utf-8'))
        for pattern in [r'\\\[.*?\\\]', r'\\\(.*?\\\)', r'\$\$.*?\$\$']:
            text = re.sub(pattern, '', text, flags=re.S)
        text = re.sub(r'(?<!\$)\$(?!\$)[^\n$]*\$', '', text)
        text = re.sub(r'(`+).*?\1', '', text)
        urls = re.findall(r'\[[^\]\n]*\]\((<[^>]+>|[^\s)]+)(?:\s+[\"\'][^\n]*?[\"\'])?\)', text)
        urls += re.findall(r'^\s*\[[^\]]+\]:\s*(\S+)', text, re.M)
        for url in urls:
            target, anchor = link_target(name, url)
            if target is None:
                external += 1
                continue
            if target not in current:
                target += '/README.md'
            require(target in current, 'broken link: ' + name + ' -> ' + url)
            if anchor and target.endswith('.md'):
                require(anchor in anchors(read(root, current, target).decode('utf-8')), 'broken anchor: ' + name + ' -> ' + url)
            count += 1
    return {'documents': len(documents), 'local_links_and_anchors': count, 'external_links_not_fetched': external}


def check_candidate(root, expected_head):
    require(bool(re.fullmatch(r'[0-9a-f]{40}', expected_head)), 'full expected SHA required')
    head = git(root, 'rev-parse', 'HEAD').decode().strip()
    require(head == expected_head, 'HEAD is not the requested review checkpoint')
    require(git(root, 'rev-parse', BASE + '^{tree}').decode().strip() == BASE_TREE, 'wrong baseline tree')
    git(root, 'merge-base', '--is-ancestor', BASE, 'HEAD')
    old, current = tree(root, BASE), tree(root, 'HEAD')
    sources = decode(read(root, current, RELEASE + '/SOURCE_TREES.json'))
    require(sources['base_main'] == BASE and sources['base_tree'] == BASE_TREE, 'baseline manifest drift')
    require(sources['review_tree'] == REVIEW_TREE and sources['review_path'] == REVIEW, 'review manifest drift')
    pins = {r['path']: r['tree'] for r in sources['frozen_sources']}
    require(len(pins) == len(sources['frozen_sources']) == 35, 'expected 35 distinct source roots')
    pins[REVIEW] = REVIEW_TREE
    for name, oid in pins.items():
        safe_name(name)
        require(bool(re.fullmatch(r'[0-9a-f]{40}', oid)), 'invalid tree SHA')
        require(git(root, 'rev-parse', 'HEAD:' + name).decode().strip() == oid, 'changed frozen tree: ' + name)
    roots = tuple(pins) + (RELEASE, GUIDE)
    check_preservation(old, current, roots)
    release = decode(read(root, current, RELEASE + '/RELEASE.json'))
    require(release['status'] == 'INTEGRATION_CANDIDATE' and release['final_review'] == 'PENDING'
            and release['rh_proved'] is False and release['published_baseline_activated'] is False, 'release status mismatch')
    require(read(root, current, 'canonical/CURRENT.json') == git(root, 'show', BASE + ':canonical/CURRENT.json'), 'published pointer changed')
    selected = rows(read(root, current, RELEASE + '/PACKETS.tsv'), FIELDS)
    reviewed = rows(read(root, current, REVIEW + '/pass4/EXTRACTION.tsv'))
    selected = check_selection(selected, reviewed, current)
    require({'/'.join(r['packet_path'].split('/')[:2]) for r in selected} == set(pins) - {REVIEW}, 'source-root coverage mismatch')
    for source in sources['frozen_sources']:
        require(set(source['packets']) == {r['packet'] for r in selected if inside(r['packet_path'], [source['path']])}, 'packet/root map mismatch')
        require(all(r['source_commit'] == source['source_commit'] for r in selected if inside(r['packet_path'], [source['path']])), 'source commit mismatch')
    repairs = decode(read(root, current, RELEASE + '/REPAIRS.json'))
    require(len(repairs) == 6 and {r['id'] for r in repairs} == {'R01','R02','R03','R04','R05','R06'}, 'repair coverage mismatch')
    for repair in repairs:
        target, anchor = link_target(RELEASE + '/REPAIRS.json', repair['current'])
        require(target in current and anchor in anchors(read(root, current, target).decode('utf-8')), 'missing current repair')
    scopes = roots + tuple(EDITABLE) + ('standalone/README.md', 'canonical/CURRENT.json')
    names = sorted(n for n in current if inside(n, scopes))
    require(not git(root, 'ls-files', '--others', '-z', '--', *scopes), 'untracked additions in candidate scope')
    seal, total = hashlib.sha256(), 0
    for name in names:
        data = read(root, current, name)
        total += len(data)
        require(total <= 150_000_000, 'candidate scope exceeds byte budget')
        seal.update(name.encode() + b'\0' + current[name][2].encode() + b'\0')
    docs = sorted(set(EDITABLE) | {n for n in current if n.startswith((GUIDE + '/', RELEASE + '/')) and n.endswith('.md')} | {'standalone/README.md'})
    links = check_links(root, current, docs)
    # Confirm files and HEAD again after consuming links and registries.
    require(git(root, 'rev-parse', 'HEAD').decode().strip() == head and tree(root, 'HEAD') == current, 'HEAD changed during validation')
    for name in names:
        read(root, current, name)
    require(not git(root, 'ls-files', '--others', '-z', '--', *scopes), 'late untracked candidate addition')
    return {'marker': 'PASS_SCOPED_INTEGRATION_CANDIDATE', 'checkout_commit': head,
            'checkout_tree': git(root, 'rev-parse', 'HEAD^{tree}').decode().strip(),
            'base_commit': BASE, 'packets': len(selected), 'frozen_source_roots': 35,
            'review_tree': REVIEW_TREE, 'repairs': 6, 'authenticated_files': len(names),
            'authenticated_bytes': total, 'path_blob_sha256': seal.hexdigest(), 'navigation': links,
            'mathematical_replay': False, 'baseline_resolver_executed': False,
            'fresh_lean_build': False, 'final_review': 'PENDING', 'rh_proved': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--expect-head', required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    print(json.dumps(check_candidate(root, args.expect_head), indent=2, sort_keys=True))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, KeyError, TypeError, subprocess.CalledProcessError) as exc:
        print('FAIL_SCOPED_INTEGRATION_CANDIDATE: ' + str(exc), file=sys.stderr)
        sys.exit(1)
