#!/usr/bin/env python3
"""Authenticate this fixed regular-file packet; optionally reconstruct its certificate."""
from __future__ import annotations
import argparse
import hashlib
from pathlib import Path
import re
import shutil
import stat
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parent
FILES=('README.md','PROOF.md','NUMERICS.md','SOURCES.json','CLAIMS.json','VALIDATION.md',
       'theta_moments.py','test_checks.py','verify_packet.py','moments.json','tests.json')

def require(ok,message):
    if not ok:raise ValueError(message)

def authenticate(root):
    names={p.name for p in root.iterdir()}
    require(names==set(FILES)|{'SHA256SUMS'},'missing or additional packet entry')
    for name in names:
        p=root/name
        require(stat.S_ISREG(p.lstat().st_mode),'nonregular file: '+name)
        require(p.stat().st_size<=2_000_000,'oversized file: '+name)
    manifest={}
    for line in (root/'SHA256SUMS').read_text(encoding='ascii').splitlines():
        match=re.fullmatch(r'([0-9a-f]{64})  ([A-Za-z0-9_.-]+)',line)
        require(match is not None,'invalid manifest line')
        digest,name=match.groups()
        require(name not in manifest,'duplicate manifest path')
        manifest[name]=digest
    require(set(manifest)==set(FILES),'manifest coverage mismatch')
    for name,digest in manifest.items():
        require(hashlib.sha256((root/name).read_bytes()).hexdigest()==digest,'hash mismatch: '+name)
    return hashlib.sha256((root/'SHA256SUMS').read_bytes()).hexdigest()

def command(script):
    return [sys.executable,'-I','-S','-B']+(['-O'] if sys.flags.optimize else [])+[str(script)]

def self_test():
    results=[]
    cases=['pristine','extra_file','missing_file','altered_proof','empty_manifest','duplicate_manifest','symlink']
    with tempfile.TemporaryDirectory() as temp:
        for case in cases:
            dst=Path(temp)/case;shutil.copytree(ROOT,dst)
            if case=='extra_file':(dst/'extra.txt').write_text('extra')
            elif case=='missing_file':(dst/'moments.json').unlink()
            elif case=='altered_proof':(dst/'PROOF.md').write_bytes((dst/'PROOF.md').read_bytes()+b'changed')
            elif case=='empty_manifest':(dst/'SHA256SUMS').write_text('')
            elif case=='duplicate_manifest':
                p=dst/'SHA256SUMS';p.write_text(p.read_text()+p.read_text().splitlines()[0]+'\n')
            elif case=='symlink':
                p=dst/'PROOF.md';p.unlink();p.symlink_to(ROOT/'PROOF.md')
            run=subprocess.run(command(dst/'verify_packet.py'),capture_output=True,text=True,timeout=30)
            require((run.returncode==0)==(case=='pristine'),'incorrect copied-CLI outcome: '+case)
            results.append(case)
    print('PASS_PACKET_SELF_TEST pristine=1 refusals=6 skipped=0')

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--full',action='store_true');p.add_argument('--self-test',action='store_true')
    args=p.parse_args()
    before=authenticate(ROOT)
    if args.full:
        subprocess.run(command(ROOT/'theta_moments.py')+['--check',str(ROOT/'moments.json')],check=True)
        require(authenticate(ROOT)==before,'packet changed during reconstruction')
    if args.self_test:self_test()
    print('PASS_PACKET_BYTES '+before+(' FULL_SOURCE_REPLAY' if args.full else ' INVENTORY_ONLY'))

if __name__=='__main__':
    try:main()
    except (OSError,ValueError,subprocess.SubprocessError) as error:
        print('FAIL_PACKET: '+str(error),file=sys.stderr);sys.exit(1)
