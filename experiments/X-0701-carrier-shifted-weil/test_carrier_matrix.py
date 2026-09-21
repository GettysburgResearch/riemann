from __future__ import annotations

import mpmath as mp

from carrier_matrix import carrier_f_transform, convolution_kernel, gram_entry


def test_compact_support_and_symmetry():
    mp.mp.dps = 60
    delta = mp.mpf("1.3")
    a = mp.mpf("4.2")
    b = mp.mpf("5.1")
    assert convolution_kernel(delta + mp.mpf("1e-10"), a, b, delta) == 0
    for xi in [0, mp.mpf("0.1"), mp.mpf("-0.7")]:
        assert abs(convolution_kernel(xi, a, b, delta) - convolution_kernel(-xi, a, b, delta)) < mp.mpf("1e-55")
        assert abs(convolution_kernel(xi, a, b, delta) - convolution_kernel(xi, b, a, delta)) < mp.mpf("1e-55")


def test_kernel_matches_direct_convolution():
    mp.mp.dps = 60
    delta = mp.mpf("1.1")
    a = mp.mpf("3.25")
    b = mp.mpf("4.75")
    for xi in [mp.mpf("-0.8"), mp.mpf("0.15"), mp.mpf("0.9")]:
        lo = max(-delta / 2, xi - delta / 2)
        hi = min(delta / 2, xi + delta / 2)
        direct = mp.quad(
            lambda x: mp.cos(2 * mp.pi * a * x) * mp.cos(2 * mp.pi * b * (xi - x)),
            [lo, hi],
        )
        assert abs(direct - convolution_kernel(xi, a, b, delta)) < mp.mpf("1e-50")


def test_gram_matches_direct_inner_product_and_transform_value():
    mp.mp.dps = 60
    delta = mp.mpf("0.9")
    a = mp.mpf("6.1")
    b = mp.mpf("7.4")
    direct = mp.quad(
        lambda x: mp.cos(2 * mp.pi * a * x) * mp.cos(2 * mp.pi * b * x),
        [-delta / 2, delta / 2],
    )
    assert abs(direct - gram_entry(a, b, delta)) < mp.mpf("1e-50")
    z = mp.mpf("2.3")
    value = carrier_f_transform(z, a, delta) * carrier_f_transform(z, b, delta)
    assert abs(mp.im(value)) < mp.mpf("1e-55")
