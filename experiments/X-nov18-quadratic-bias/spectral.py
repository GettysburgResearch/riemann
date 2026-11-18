"""Certify additional sign changes from a single low Dirichlet zero."""
import csv
from math import gcd
from pathlib import Path

from flint import arb, ctx, dirichlet_char

from census import character


def primitive_character(d):
    q = abs(d)
    odd = q
    while odd % 2 == 0:
        odd //= 2
    for j in range(odd-1, q, odd):
        if gcd(j, q) != 1:
            continue
        chi = dirichlet_char(q, j)
        if chi.is_primitive() and chi.is_real() and chi.parity() == int(d < 0):
            model = character(d)
            assert all(chi(n)==int(model[n % q]) for n in range(1, 36))
            return chi
    raise ValueError(f'missing primitive character {d}')


def low_zero(d):
    chi = primitive_character(d)
    prev = chi.hardy_z(0).real
    assert prev > 0 or prev < 0
    # 19/26 = .7308..., inside the strict Fourier coefficient threshold.
    for i in range(1, 20):
        right = arb(i)/26
        here = chi.hardy_z(right).real
        if here*prev < 0:
            amplitude = 1/((arb(1)/4+right**2)*(arb(9)/4+right**2)).sqrt()
            assert amplitude > arb(2)/3
            return i, int((1000*amplitude).lower().floor().unique_fmpz())
        prev = here
    return 0, 0


if __name__ == '__main__':
    ctx.prec = 80
    with Path('refined.tsv').open() as handle:
        ds = [int(r['discriminant']) for r in csv.DictReader(handle, delimiter='\t')
              if r['decision']=='open']
    with Path('low-zero.tsv').open('w') as handle:
        out = csv.writer(handle, delimiter='\t', lineterminator='\n')
        out.writerow(('discriminant','right_numerator_over_26','amplitude_lower_milli'))
        for d in ds:
            out.writerow((d, *low_zero(d)))
            handle.flush()
