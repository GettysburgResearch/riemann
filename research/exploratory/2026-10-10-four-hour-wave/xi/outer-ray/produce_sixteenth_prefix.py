#!/usr/bin/env python3
"""Candidate-only refinement below2048 for a count-free sixteenth-moment replay."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import flint
from flint import acb, ctx


def main() -> None:
    ctx.prec = 320
    directory = Path(__file__).resolve().parent
    original = directory/'native_candidates.json'
    data = json.loads(original.read_text())
    count = sum(hi < 2048*data['denominator'] for lo,hi in data['interval_numerators'])
    denominator = 2**160
    intervals = []
    for candidate in acb.zeta_zeros(1,count):
        lo = (candidate.imag.mid()*denominator).floor().unique_fmpz()
        if lo is None:
            raise SystemExit('FAIL: exact candidate quantization')
        lo = int(lo)
        intervals.append([lo,lo+1])
    result = {
        'status':'SIXTEENTH_MOMENT_PREFIX_CANDIDATES_NOT_A_CENSUS',
        'normalization':'Xi(z)=xi(1/2+i*z)', 'denominator':denominator,
        'prefix_cutoff':2048, 'refined_count':count, 'interval_numerators':intervals,
        'original_candidates_sha256':hashlib.sha256(original.read_bytes()).hexdigest(),
        'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'python_flint_version':flint.__version__, 'flint_version':flint.__FLINT_VERSION__,
    }
    (directory/'sixteenth_prefix_candidates.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print('PRODUCED_SIXTEENTH_MOMENT_PREFIX',count,flush=True)


if __name__ == '__main__':
    main()
