#!/usr/bin/env python3
"""Authenticate and restore twelve historical files to a NEW directory; no code execution."""
from pathlib import Path
import argparse,hashlib,io,json,lzma,tarfile
SHA256='a9466b8d907140a62dd70bbdebd08e31032191fd4ff5ddf294501f8fb27f6d4b'
TREE='a640884946f2ff627361212eae669d02e342e1f7'
NAMES=set('CERTIFICATES.json CHECKS.json COMPOSITION.md INPUTS_AND_AUDIT.md MANIFEST.json MUTATIONS.json README.md REFLECTED_NUMERATOR.md STRATA.json VALIDATION.md replay.py verify.py'.split())

def git_hash(kind,data):
    return hashlib.sha1(kind.encode()+b' '+str(len(data)).encode()+b'\0'+data).hexdigest()
def restore():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path);args=ap.parse_args()
    root=Path(__file__).resolve().parent
    archive=b''.join((root/'parts'/f'part-{i:02}').read_bytes() for i in range(7))
    if len(archive)!=41468 or hashlib.sha256(archive).hexdigest()!=SHA256:raise ValueError('archive identity')
    files={}
    with tarfile.open(fileobj=io.BytesIO(lzma.decompress(archive)),mode='r:') as tf:
        for m in tf:
            if not m.isfile() or m.name not in NAMES or m.name in files:raise ValueError('unsafe archive member')
            stream=tf.extractfile(m)
            if stream is None:raise ValueError('missing member')
            files[m.name]=stream.read()
    if set(files)!=NAMES:raise ValueError('incomplete archive')
    tree=b''.join(b'100644 '+name.encode()+b'\0'+bytes.fromhex(git_hash('blob',data)) for name,data in sorted(files.items()))
    if git_hash('tree',tree)!=TREE:raise ValueError('original Git tree')
    for item in json.loads(files['MANIFEST.json'])['files']:
        data=files[item['path']]
        if len(data)!=item['bytes'] or hashlib.sha256(data).hexdigest()!=item['sha256'] or git_hash('blob',data)!=item['git_blob']:raise ValueError('original manifest')
    if args.output:
        args.output.mkdir(parents=True,exist_ok=False)
        for name,data in files.items():(args.output/name).write_bytes(data)
    print(json.dumps({'original_files':len(files),'original_git_tree':TREE,'archive_sha256':SHA256,'extracted_to':str(args.output) if args.output else None,'executed_recovered_code':False},sort_keys=True,indent=2))
if __name__=='__main__':restore()
