#!/usr/bin/env python3
"""Verify and install this add-only packet. Never commits or pushes.

Usage: python apply_to_repo.py /path/to/riemann --check
       python apply_to_repo.py /path/to/riemann
Default requires the pinned base as current HEAD. --allow-other-base relaxes
that HEAD equality only; it does not permit overwriting an existing packet.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import sys

BASE='cdb0666fc48d5166f5edd81f394b13e2001a6b5d'
TARGET=Path('standalone/2026-10-16-critical-power-factorization')


def git(root: Path, *args: str) -> str:
    return subprocess.check_output(['git','-C',str(root),*args],text=True,
                                   stderr=subprocess.STDOUT).strip()


def verify(source: Path) -> list[str]:
    manifest=json.loads((source/'MANIFEST.json').read_text())
    paths=[]
    for item in manifest['files']:
        rel=Path(item['path'])
        if rel.is_absolute() or '..' in rel.parts:
            raise ValueError('unsafe manifest path')
        raw=(source/rel).read_bytes()
        if len(raw)!=item['bytes'] or hashlib.sha256(raw).hexdigest()!=item['sha256']:
            raise ValueError('payload mismatch: '+str(rel))
        paths.append(str(rel))
    return paths+['MANIFEST.json']


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('repository',type=Path)
    parser.add_argument('--check',action='store_true')
    parser.add_argument('--allow-other-base',action='store_true')
    args=parser.parse_args()
    source=Path(__file__).resolve().parent
    paths=verify(source)
    root=args.repository.expanduser().resolve()
    if Path(git(root,'rev-parse','--show-toplevel')).resolve()!=root:
        raise ValueError('provide the repository root, not a subdirectory')
    head=git(root,'rev-parse','HEAD')
    if head!=BASE and not args.allow_other_base:
        raise ValueError('HEAD is not pinned base '+BASE+'; choose base explicitly')
    target=root/TARGET
    if target.exists():
        raise FileExistsError('refusing to overwrite '+str(target))
    if args.check:
        print('Verified payload; target absent; no files changed. HEAD='+head)
        return
    target.parent.mkdir(parents=True,exist_ok=True)
    temp=Path(tempfile.mkdtemp(prefix='.critical-power-',dir=target.parent))
    try:
        for name in paths:
            dest=temp/name
            dest.parent.mkdir(parents=True,exist_ok=True)
            shutil.copyfile(source/name,dest)
        if target.exists():
            raise FileExistsError('target appeared during preparation')
        temp.rename(target)
    except BaseException:
        shutil.rmtree(temp,ignore_errors=True)
        raise
    print('Added '+str(TARGET)+'. No commit or push performed.')


if __name__=='__main__':
    try:
        main()
    except (OSError,ValueError,subprocess.CalledProcessError) as exc:
        print('ERROR: '+str(exc),file=sys.stderr)
        sys.exit(1)
