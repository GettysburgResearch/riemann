"""Check certified integer logarithmic phases and all omitted-zero bounds."""
import argparse
import json
import lzma
from pathlib import Path

from flint import acb, arb, ctx

from classify_li import reciprocal_sum
from spectral import primitive_character


def check(record):
    d = record['d']
    precision = record['p']
    t = int(record['t'])
    ctx.prec = precision + 100
    chi = primitive_character(d)
    first = reciprocal_sum(d, arb(0))
    second = reciprocal_sum(d, arb.pi()/2)
    partial = arb(0)
    previous = 0
    for left, right in record['brackets']:
        left, right = int(left), int(right)
        assert previous < left < right
        previous = right
        lower, upper = arb(left)/2**precision, arb(right)/2**precision
        # Opposite definite signs certify at least one positive zero.
        assert chi.hardy_z(lower).real * chi.hardy_z(upper).real < 0
        gamma = lower.union(upper)
        first -= 2/(arb(1)/4 + gamma**2)
        second -= 2/(arb(9)/4 + gamma**2)
        coefficient = 1/(acb(arb(1)/2,gamma)*acb(arb(3)/2,gamma))
        partial += 2*(coefficient*acb(0,t*gamma).exp()).real
    assert first > 0 and second > 0
    lower_amplitude = -partial-(first*second).sqrt()
    assert lower_amplitude > arb(2)/3
    return int((1000*lower_amplitude).lower().floor().unique_fmpz())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('archive', type=Path, nargs='?', default='phase-witnesses.json.xz')
    args = parser.parse_args()
    data = json.loads(lzma.decompress(args.archive.read_bytes()))
    for record in data:
        lower = check(record)
        print(f'{record["d"]}\t{len(record["brackets"])}\t{lower}')
