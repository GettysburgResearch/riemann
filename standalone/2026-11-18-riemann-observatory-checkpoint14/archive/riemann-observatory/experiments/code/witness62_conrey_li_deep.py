"""Arb enclosures for Conrey--Li (arXiv:math/9812166v1, section 3)."""
import json
from fractions import Fraction

import flint
from flint import acb, acb_series, arb, ctx, fmpq


def xi(s, character):
    if character == 'zeta':
        return s * (s - 1) * (-s * arb.pi().log() / 2).exp() * (s / 2).gamma() * s.zeta()
    # (4/pi)^(s/2) 4^(-s) = (4*pi)^(-s/2).
    return (
        (-s * (4 * arb.pi()).log() / 2).exp()
        * ((s + 1) / 2).gamma()
        * (s.zeta(acb(fmpq(1, 4))) - s.zeta(acb(fmpq(3, 4))))
    )


def signed_ratio(t, offset, character):
    s = acb(1 + arb(offset), arb(t))
    left, right = xi(s, character), xi(s + 1, character)
    assert not left.contains(0) and not right.contains(0)
    printed, actual = (left / right).real, (right / left).real
    assert printed < 0 and actual < 0
    return {'offset': offset, 'printed_real_part': str(printed), 'kernel_ratio_real_part': str(actual)}


def derivative_witness(t, character):
    root_halfwidth = '1e-20'
    mid, width = Fraction(t), Fraction(root_halfwidth)
    lo = xi(acb(fmpq(1, 2), arb(str(mid - width))), character)
    hi = xi(acb(fmpq(1, 2), arb(str(mid + width))), character)
    assert (lo.real < 0 < hi.real) or (hi.real < 0 < lo.real)
    root_box = acb(fmpq(1, 2), arb(str(mid - width)).union(arb(str(mid + width))))
    series = acb_series([root_box, 1], 2)
    derivative = xi(series, character)[1]
    sign = (-derivative * xi(root_box + 1, character)).real
    assert sign < 0
    return {'center': t, 'halfwidth': root_halfwidth, 'endpoint_real_parts': [str(lo.real), str(hi.real)],
            'negative_sign_witness': str(sign)}


def main():
    ctx.prec = 256
    ctx.cap = 2
    data = {'python_flint_version': flint.__version__, 'precision_bits': ctx.prec}
    for name, small_t, large_t in [
        ('zeta', '111.029535543169674524656', '282'),
        ('chi4', '67.6369208635460683980549', '8714.2'),
    ]:
        data[name] = {'ratio_height': large_t,
                      'ratios': [signed_ratio(large_t, x, name) for x in ('0', '0.000001')],
                      'derivative_witness': derivative_witness(small_t, name)}
    print(json.dumps(data, indent=2))


if __name__ == '__main__':
    main()
