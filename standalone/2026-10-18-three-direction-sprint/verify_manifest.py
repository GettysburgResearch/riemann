"""Authenticate raw packet bytes; this does not validate mathematical claims."""
from pathlib import Path, PurePosixPath
import argparse
import hashlib
import json

ROOT=Path(__file__).resolve().parent

def require(condition,message):
    if not condition:
        raise ValueError(message)

def unique_pairs(items):
    result={}
    for key,value in items:
        require(key not in result,'Duplicate manifest key: '+key)
        result[key]=value
    return result

def no_float(value):
    raise ValueError('Noninteger numeric manifest input: '+value)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--strict-inventory',action='store_true',
                        help='For a fresh export: reject unlisted non-cache files.')
    args=parser.parse_args()
    raw=(ROOT/'MANIFEST.json').read_bytes()
    manifest=json.loads(raw,object_pairs_hook=unique_pairs,
                        parse_float=no_float,parse_constant=no_float)
    require(manifest['schema']=='riemann-three-direction-packet.v1','Unknown manifest schema.')
    entries=manifest['files']
    require(type(entries) is list and type(manifest['file_count']) is int,
            'Invalid manifest types.')
    require(len(entries)==manifest['file_count'],'File count mismatch.')
    seen=set()
    total=0
    previous=''
    for entry in entries:
        require(set(entry)=={'path','bytes','sha256','git_blob_sha1'},'Unexpected entry fields.')
        name=entry['path']
        require(type(name) is str and name>previous,'Paths must be sorted and unique.')
        require('\\' not in name and ':' not in name,'Nonportable manifest path.')
        relative=PurePosixPath(name)
        require(not relative.is_absolute() and '..' not in relative.parts,
                'Escaping manifest path.')
        require(name!='MANIFEST.json','Manifest cannot hash itself.')
        file=(ROOT/name).resolve()
        require(file.is_relative_to(ROOT.resolve()),'Resolved path escapes packet.')
        content=file.read_bytes()
        require(type(entry['bytes']) is int and len(content)==entry['bytes'],
                'Byte length mismatch: '+name)
        require(hashlib.sha256(content).hexdigest()==entry['sha256'],
                'SHA256 mismatch: '+name)
        blob=hashlib.sha1(b'blob '+str(len(content)).encode()+b'\0'+content).hexdigest()
        require(blob==entry['git_blob_sha1'],'Git blob identity mismatch: '+name)
        total+=len(content)
        seen.add(name)
        previous=name
    require(total==manifest['payload_bytes'],'Payload byte count mismatch.')
    if args.strict_inventory:
        actual={p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*')
                if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc'}
        require(actual==seen|{'MANIFEST.json'},'Unlisted or missing files in strict inventory.')
    print(json.dumps({'status':'PASS','file_count':len(entries),'payload_bytes':total,
                      'manifest_sha256':hashlib.sha256(raw).hexdigest(),
                      'strict_inventory':args.strict_inventory,
                      'scope':'Raw byte and inventory authentication only; no theorem acceptance.'}))

if __name__=='__main__':
    main()
