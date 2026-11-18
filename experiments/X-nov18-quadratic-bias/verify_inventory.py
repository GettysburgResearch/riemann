"""Verify disjoint, exhaustive conductor coverage and the conditional list."""
import csv
import json
import lzma
from pathlib import Path

from census import character, DISCRIMINANT_LIMIT


def read_table(name):
    loader = lzma.open if name.endswith('.xz') else open
    with loader(name, 'rt') as handle:
        return list(csv.DictReader(handle, delimiter='\t'))


if __name__=='__main__':
    first = {int(r['discriminant']) for r in read_table('witnesses.tsv.xz')}
    refined = read_table('refined.tsv')
    second = {int(r['discriminant']) for r in refined if r['decision']=='both_signs'}
    negative = {int(r['discriminant']) for r in refined if r['decision']=='negative_on_grh'}
    low = {int(r['discriminant']) for r in read_table('low-zero.tsv')
           if int(r['right_numerator_over_26'])}
    records = json.loads(lzma.decompress(Path('phase-witnesses.json.xz').read_bytes()))
    phase = {r['d'] for r in records}
    assert len(phase)==len(records)
    groups = [first,second,low,phase,negative]
    for i, group in enumerate(groups):
        assert all(group.isdisjoint(other) for other in groups[i+1:])
    universe = {d for d in range(-DISCRIMINANT_LIMIT,DISCRIMINANT_LIMIT+1)
                if abs(d)>1 and character(d) is not None}
    assert set.union(*groups)==universe
    assert negative=={int(r['discriminant']) for r in read_table('small-norms.tsv')
                      if r['li_decision']=='negative'}
    print('signed witness groups', [len(g) for g in groups[:4]])
    print('negative on GRH', sorted(negative))
    for sign in (-1,1):
        print('sign',sign,'unconditional both signs',sum(sign*d>0 for d in universe-negative))
