"""Crosscheck each historical endpoint inside a frozen modern strip census."""
import argparse
from collections import defaultdict
from fractions import Fraction
import hashlib
import json
import lzma
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent))
from check_runs import INDEX, read_all, supplemental_sign_grid
from check_scalar_signs import exact_dyadic, hardy_sign


def point(s):
    a,e=map(lambda b:int(b,16),s.split())
    return a*Fraction(2)**e


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('historical',type=Path)
    p.add_argument('modern',type=Path)
    p.add_argument('--full',action='store_true',help='require every historical endpoint to be covered')
    a=p.parse_args()
    hist=json.loads(a.historical.read_text())
    m=json.loads(a.modern.read_text())
    block_count=m['complete_blocks']
    if m['last_certified_index'] != INDEX+10000*block_count:
        raise ValueError('Modern block count and last index disagree')
    stream_hash=hashlib.sha256()
    for b in range(block_count):
        base=HERE.parent/'blocks'/f'{b:04d}.json'
        meta=json.loads(base.read_text())
        if meta['first_index']!=INDEX+10000*b or meta['last_index']!=INDEX+10000*(b+1):
            raise ValueError('Wrong modern manifest indices')
        stream_hash.update(f"{b}\t{meta['stream_sha256']}\n".encode('ascii'))
    if stream_hash.hexdigest()!=m['ordered_stream_digest']:
        raise ValueError('Modern manifests disagree with the frozen snapshot digest')
    good,_,_=read_all(HERE/'runs',hist['transcripts'])
    if hist['result'].get('supplementary_grid'):
        interval,info=supplemental_sign_grid()
        if info != hist['result']['supplementary_grid']:
            raise ValueError('Supplement differs from frozen snapshot')
        good.append(interval)
    points=sorted({(t,n) for b,e,lo,hi in good for t,n in [(b,lo),(e,hi)]})
    needed=defaultdict(set)
    checks=[]
    for t,n in points:
        if not INDEX<=n<m['last_certified_index']:
            continue
        checks.append((t,n))
        for z in (n,n+1):
            # Use preceding block's shared terminal entry at the right guard.
            b=min((z-INDEX)//10000,(m['last_certified_index']-INDEX)//10000-1)
            needed[b].add(z)
    if a.full and len(checks)!=len(points):
        raise ArithmeticError('Frozen modern archive does not cover every historical endpoint')
    roots={}
    for b,indices in needed.items():
        base=HERE.parent/'blocks'/f'{b:04d}'
        meta=json.loads(base.with_suffix('.json').read_text())
        raw=lzma.decompress(base.with_suffix('.xz').read_bytes())
        if hashlib.sha256(raw).hexdigest()!=meta['stream_sha256']:
            raise ValueError('Invalid block stream hash')
        rows=raw.splitlines()
        for z in indices:
            roots[z]=tuple(point(v) for v in rows[z-meta['first_index']].split(b'\t'))
    direct=scalar=0
    for t,n in checks:
        (lo,hi),(lo1,hi1)=roots[n],roots[n+1]
        if not lo<t<hi1 or hi>lo1:
            raise ArithmeticError(f'Historical count conflicts with modern neighboring roots at {t}')
        if hi<=t<=lo1:
            direct+=1
        else:
            if t.denominator & (t.denominator-1):
                raise ValueError('Historical endpoint is not dyadic')
            w=exact_dyadic(t.numerator,1-t.denominator.bit_length())
            if hardy_sign(w) != (1 if n%2 else -1):
                raise ArithmeticError(f'Scalar Hardy parity disagrees at {t}')
            scalar+=1
    print(json.dumps({'historical_snapshot':a.historical.name,'modern_snapshot':a.modern.name,
                      'distinct_historical_endpoints':len(points),'crosschecked':len(checks),
                      'between_brackets':direct,'confirmed_by_scalar_parity':scalar},indent=2))


if __name__=='__main__':
    main()
