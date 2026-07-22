from __future__ import annotations

import mpmath as mp

from triangular import arch_compact, arch_reduced, g_carrier, h_delta, sinc_pi


def test_sinc_and_real_axis_nonnegativity():
    mp.mp.dps = 60
    assert sinc_pi(0) == 1
    delta = mp.mpf("1.7")
    for x in [0, mp.mpf("0.1"), 3, mp.mpf("17.25")]:
        assert mp.re(h_delta(x, delta)) >= 0
        assert mp.re(g_carrier(x, 14, delta)) >= 0


def test_compact_and_ci_arch_forms_agree():
    mp.mp.dps = 70
    for T, L in [(1, mp.log(5)), (7, mp.log(13)), (14, mp.log(100))]:
        a = arch_compact(T, L, dps=70)
        b = arch_reduced(T, L, dps=70)
        assert abs(a - b) < mp.mpf("1e-50")
