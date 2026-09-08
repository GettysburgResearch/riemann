#!/usr/bin/env python3
"""Authenticate the exact local packet inventory; optionally replay bounded checks."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

FILES = {
    'ATTEMPT.md', 'CLAIMS.tsv', 'EDGES.tsv', 'PROOF.md', 'README.md',
    'SOURCES.json', 'VALIDATION.md', 'checks.py', 'checks.normal.json',
    'checks.optimized.json', 'validate.py', 'rejections.py', 'rejections.json',
    'SHA256SUMS'
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--replay',action='store_true')
    args=p.parse_args()
    root=Path(__file__).resolve().parent
    entries=list(root.iterdir())
    require({x.name for x in entries}==FILES, 'packet inventory mismatch')
    require(all(x.is_file() and not x.is_symlink() for x in entries),'nonregular packet entry')
    seen=set()
    for line in (root/'SHA256SUMS').read_text().splitlines():
        digest,name=line.split('  ')
        require(name in FILES-{'SHA256SUMS'} and name not in seen,'bad manifest entry')
        require(hashlib.sha256((root/name).read_bytes()).hexdigest()==digest,'changed bytes: '+name)
        seen.add(name)
    require(seen==FILES-{'SHA256SUMS'},'incomplete manifest')
    require((root/'checks.normal.json').read_bytes()==(root/'checks.optimized.json').read_bytes(),
            'normal and optimized results differ')
    if args.replay:
        for mode,result in [(False,'checks.normal.json'),(True,'checks.optimized.json')]:
            command=[sys.executable]+(['-O'] if mode else [])
            command += ['-B',str(root/'checks.py'),'--check',str(root/result)]
            run=subprocess.run(command,capture_output=True,text=True,timeout=45)
            require(run.returncode==0,run.stderr)
    print(json.dumps({'status':'PASS_PACKET_INVENTORY','files':len(FILES),
                      'replayed':bool(args.replay),'analytic_proof_machine_verified':False},sort_keys=True))


if __name__=='__main__':
    main()
