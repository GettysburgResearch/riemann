#!/usr/bin/env python3
"""Recover thirteen unchanged original files; refuse overwrites and unsafe tar paths."""
from pathlib import Path
import argparse
import hashlib
import io
import json
import subprocess
import sys
import tarfile

ARCHIVE_SHA256='966fc4099801404d5f5922614e687c18c5c383028d3fd5d5b59a88250abddf57'
ORIGINAL_TREE='a80cb7e2404e0f6835c47017597b6acbeb9cb264'
PARTS=[
 'c45287575383e9f4827eef4dbc7aa69969afef72c94bd9003d543184182f85b5',
 '2f5104bed2096d02af669f00964d2bbc049f032e06fba826801089f98a0230c5',
 '6a116ea42f2ce88681fcd11df05ebd164340b4610a96df5130ed1904dc40ed45',
 'c94ebcb3d42d067b3775b2692624c63939730307a1efd1c99d2f9b9ced5f318b']

def git_hash(kind, data):
    return hashlib.sha1(kind.encode()+b' '+str(len(data)).encode()+b'\0'+data).hexdigest()

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('destination',type=Path,help='new, nonexistent directory')
    ap.add_argument('--replay',action='store_true',help='also execute the original manifest/checker in normal and optimized Python')
    args=ap.parse_args()
    root=Path(__file__).resolve().parent
    blocks=[]
    for i,digest in enumerate(PARTS,1):
        data=(root/f'archive.part{i:02}').read_bytes()
        if len(data)!=7864 or hashlib.sha256(data).hexdigest()!=digest:
            raise ValueError(f'part {i} failed authentication')
        blocks.append(data)
    data=b''.join(blocks)
    if hashlib.sha256(data).hexdigest()!=ARCHIVE_SHA256:
        raise ValueError('archive checksum')
    files={}
    with tarfile.open(fileobj=io.BytesIO(data),mode='r:xz') as tf:
        for member in tf.getmembers():
            if not member.isfile() or '/' in member.name or member.name in ('','.','..') or member.name in files:
                raise ValueError('unsafe or duplicate archive member')
            stream=tf.extractfile(member)
            if stream is None: raise ValueError('missing member')
            files[member.name]=stream.read()
    tree=b''.join(b'100644 '+name.encode()+b'\0'+bytes.fromhex(git_hash('blob',files[name])) for name in sorted(files))
    if len(files)!=13 or git_hash('tree',tree)!=ORIGINAL_TREE:
        raise ValueError('original thirteen-file Git tree differs')
    manifest=json.loads(files['MANIFEST.json'])
    for name, record in manifest['files'].items():
        if name not in files or hashlib.sha256(files[name]).hexdigest()!=record['sha256']:
            raise ValueError(f'original manifest mismatch: {name}')
    args.destination.mkdir(parents=True,exist_ok=False)
    for name,payload in files.items(): (args.destination/name).write_bytes(payload)
    if args.replay:
        subprocess.run([sys.executable,'verify_manifest.py'],cwd=args.destination,check=True)
        for flags in ([],['-O']):
            done=subprocess.run([sys.executable,*flags,'verify.py'],cwd=args.destination,check=True,capture_output=True)
            if done.stdout!=files['CHECKS.json']: raise ValueError('original checker changed')
    print(json.dumps({'status':'PASS','files':13,'tree':ORIGINAL_TREE,'replayed':args.replay},sort_keys=True))

if __name__=='__main__': main()
