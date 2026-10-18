"""Exact continuum certificate for a CONDITIONAL U^(6/5) mixed-mean consumer.

The interval subdivision covers every closed parameter cell. It does not
sample the arithmetic mean, which remains an open hypothesis.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def main():
    ell = F(6, 35)
    x = y = (1 - ell) / 2
    h = (1 + 3 * ell) / 2
    boundary = F(437, 500)
    mean_exponent = F(6, 5)
    gap = F(1, 1000000)
    constant = F(1, 6) - ell / 2 - boundary
    delta_min, delta_max = F(1, 50), F(3, 4)
    amplitude_max = F(1, 2)

    def dx(t):
        return 3 - F(17, 9) * t

    def px(t):
        return (2 - F(8, 9) * t) * (1 - t)

    # D and P are positive and decreasing on [0,1/2]. Their derivatives
    # are -17/9 and -26/9+16t/9 respectively. All denominator bounds below
    # are positive. Rmix=A-3delta/2 remains positive on this whole domain.
    require(dx(amplitude_max) > 0 and px(amplitude_max) > 0,
            'positive count factors')
    require(-F(26, 9) + F(16, 9) * amplitude_max < 0,
            'monotone P')
    require(mean_exponent - F(3, 2) * delta_max > 0,
            'the mixed count has no extra breakpoint')

    pending = [(delta_min, delta_max, F(0), amplitude_max, 0)]
    leaves = 0
    deepest = 0
    minimum_margin = None
    leaf_hash = hashlib.sha256()
    while pending:
        dl, dh, tl, th, depth = pending.pop()
        # The resulting mixed high exponent is decreasing in delta and
        # increasing in amplitude, so its maximum is at (dl,th).
        mix_upper = constant + h * mean_exponent + dl * (
            -h / 2 - ell / 2 + th * ell)
        require(-h / 2 - ell / 2 + th * ell < 0,
                'mixed exponent monotonicity')
        j_lower = (F(5, 6) - dh) * dx(th) + dl * px(th)
        require(j_lower > 0, 'positive source denominator')
        source_r_upper = 1 - dl + (
            (F(5, 6) - dl) * dh * px(tl) / (2 * j_lower))
        source_upper = constant + h * source_r_upper + dh * (
            h - ell / 2 + th * ell)
        upper = min(mix_upper, source_upper)
        if upper < -gap:
            leaves += 1
            deepest = max(deepest, depth)
            minimum_margin = (-upper if minimum_margin is None else
                              min(minimum_margin, -upper))
            leaf_hash.update(('|'.join(map(str, (
                dl, dh, tl, th, upper))) + '\n').encode('ascii'))
            continue
        require(depth < 40, 'unresolved parameter cell')
        # Each split replaces one closed rectangle by its two closed
        # halves. Thus successful termination proves a complete cover,
        # including every shared boundary, with no mesh interpolation.
        if dh - dl >= th - tl:
            mid = (dl + dh) / 2
            pending.extend([(dl, mid, tl, th, depth + 1),
                            (mid, dh, tl, th, depth + 1)])
        else:
            mid = (tl + th) / 2
            pending.extend([(dl, dh, tl, mid, depth + 1),
                            (dl, dh, mid, th, depth + 1)])

    a0 = F(51, 100)
    floor = (a0 - boundary - a0 * y - ell / 2 + F(1, 100) * ell
             + h * (1 + a0 - F(2, 3)))
    frequency_zero = h * (F(7, 8) + F(17, 50) - F(1, 6)) - boundary - ell
    small_rows = h * (F(17, 50) - F(1, 6)) - y / 2 + F(63, 5000)
    low_margin = boundary - (F(11, 12) - ell / 4)
    supply_margin = ell / h - F(7, 37)
    require(0 < ell < F(1, 5) and x > ell, 'physical geometry')
    require(all(v < 0 for v in (floor, frequency_zero, small_rows)),
            'all other physical comparisons are strict')
    require(low_margin > 0 and supply_margin > 0, 'signal and prime supply')

    # The old count by itself does not prove this boundary: a concrete
    # exact cell stays above it. This guards against erasing the open
    # mixed hypothesis or presenting the optimization as a new result.
    d, t = F(777, 2000), F(1, 2)
    j = (F(5, 6) - d) * dx(t) + d * px(t)
    r = 1 - d + (F(5, 6) - d) * d * px(t) / (2 * j)
    old_only = constant + h * r + d * (h - ell / 2 + t * ell)
    require(old_only > 0, 'the existing source count alone must fail')

    data = {
        'status': 'PASS',
        'conditional_open_input': 'COMPLETE robust mixed mean << U^(6/5+epsilon)',
        'boundary': str(boundary), 'boundary_decimal': float(boundary),
        'ell': str(ell), 'x': str(x), 'y': str(y), 'h': str(h),
        'closed_delta_interval': [str(delta_min), str(delta_max)],
        'closed_amplitude_interval': ['0', str(amplitude_max)],
        'interval_cover_leaves': leaves, 'maximum_depth': deepest,
        'leaf_stream_sha256': leaf_hash.hexdigest(),
        'minimum_nonfloor_margin': str(minimum_margin),
        'reserved_nonfloor_margin': str(gap),
        'low_signal_margin': str(low_margin),
        'floor_frequency_h_upper': str(floor),
        'frequency_zero_upper': str(frequency_zero),
        'small_row_upper_dmin_1_100': str(small_rows),
        'prime_supply_margin': str(supply_margin),
        'old_source_only_positive_regression': str(old_only),
        'scope': 'Exact exponent algebra; the complete arithmetic mean remains OPEN.'}
    Path(__file__).with_name('RELAXED_MIXED_CONSUMER_CHECKS.json').write_text(
        json.dumps(data, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(data, indent=2))


if __name__ == '__main__':
    main()
