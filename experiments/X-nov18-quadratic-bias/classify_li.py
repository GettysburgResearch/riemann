"""Classify the full GRH + nonvanishing + independent-ordinate case."""
import csv
from pathlib import Path

from flint import arb, arb_series, ctx

from census import character


def reciprocal_sum(d, theta):
    c = (arb(1)/4 + 2*theta.sin()**2).sqrt()
    s = arb(1)/2+c
    q = abs(d)
    chi = character(d)
    series = arb_series([s, 1], prec=2)
    total = arb_series([0], prec=2)
    for r, sign in enumerate(chi):
        if sign:
            total += int(sign)*series.zeta(arb(r)/q, deflate=True)
    assert not total[0].contains(0)
    log_deriv = total[1]/total[0] - arb(q).log()
    return ((arb(q)/arb.pi()).log() + ((s+int(d < 0))/2).digamma() + 2*log_deriv)/(2*c)


def classify(d):
    mass0 = reciprocal_sum(d, arb(0))
    mass1 = reciprocal_sum(d, arb.pi()/2)
    count = 1
    interiors = arb(0)
    while count < 8192:
        lower = (mass1+interiors)/count
        upper = (mass0+interiors)/count
        if upper < arb(2)/3 or lower > arb(2)/3:
            return (d, 'negative' if upper < arb(2)/3 else 'both_signs',
                    count, int((1000*lower).lower().floor().unique_fmpz()),
                    int((1000*upper).upper().ceil().unique_fmpz()))
        count *= 2
        for j in range(1, count, 2):
            interiors += reciprocal_sum(d, arb.pi()*j/(2*count))
    raise ArithmeticError(f'unresolved threshold for {d}')


if __name__ == '__main__':
    ctx.prec = 96
    z = arb_series([2,1], prec=2).zeta()
    assert -z[1]/z[0] < arb('0.57')
    assert (arb(130)/arb.pi()).log()-arb.const_euler()-arb('1.14')>2
    with Path('small-norms.tsv').open('w') as handle:
        out = csv.writer(handle, delimiter='\t', lineterminator='\n')
        out.writerow(('discriminant','li_decision','panels','norm_lower_milli','norm_upper_milli'))
        for d in range(-129, 130):
            if abs(d)>1 and character(d) is not None:
                out.writerow(classify(d))
