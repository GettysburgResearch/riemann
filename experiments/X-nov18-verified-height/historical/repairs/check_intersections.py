"""Cross-check all historical eighth-grid brackets with the separate FLINT 3 archive."""
from fractions import Fraction
import hashlib
import json
import lzma
from pathlib import Path

HERE = Path(__file__).resolve().parent


def as_dyadic(pair):
    mant, exp = pair.split()
    return int(mant, 16)*Fraction(2)**int(exp, 16)


def main():
    import sys
    sys.path.insert(0, str(HERE.parent))
    from check_runs import supplemental_sign_grid
    ((left,right,lower,upper),info)=supplemental_sign_grid()
    base = HERE.parent.parent/'blocks'/'0139'
    meta = json.loads(base.with_suffix('.json').read_text())
    packed = base.with_suffix('.xz').read_bytes()
    if hashlib.sha256(packed).hexdigest() != meta['compressed_sha256']:
        raise ValueError('Wrong modern packet digest')
    raw=lzma.decompress(packed)
    if hashlib.sha256(raw).hexdigest() != meta['stream_sha256']:
        raise ValueError('Wrong modern interval digest')
    intervals=raw.decode('ascii').splitlines()
    signs=(HERE/'triple.tsv').read_text().splitlines()[1].split(':')[1]
    if len(intervals) != meta['count'] or set(signs) != {'+','-'}:
        raise ValueError('Unexpected missing interval or indefinite old sign')
    step=(right-left)/(len(signs)-1)
    idx=lower
    for tick,(a,b) in enumerate(zip(signs,signs[1:])):
        if a==b:
            continue
        idx+=1
        mid=idx-meta['first_index']
        if not 0<=mid<len(intervals):
            raise ValueError('Modern archive does not contain matching index')
        lo, hi=map(as_dyadic,intervals[mid].split('\t'))
        oldlo=left+step*tick
        oldhi=oldlo+step
        if not max(lo,oldlo)<min(hi,oldhi):
            raise ValueError(f'Disjoint independent brackets at {idx}')
        if 12_363_154_831_928<=idx<=12_363_154_831_930:
            print(idx,oldlo,oldhi)
    if idx!=upper:
        raise ValueError('Wrong terminal index')
    print(f"All {info['zeros']} independently produced bracket pairs intersect.")


if __name__ == '__main__':
    main()
