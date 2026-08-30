"""Smoke tests for core/exact.py. Run: python3 -m core.test_exact (from pass root)."""
from fractions import Fraction
from .exact import (
    berlekamp_massey, minimal_rational_form, series_of_rational,
    power_sums_from_satake, coefficient_sequence_from_satake,
    satake_poly_from_power_sums, op_sym2, op_ext2, op_adams, op_tensor,
    op_sym_k, count_real_roots_in, certify_root_above, charpoly_of_matrix,
    power_sums_from_elementary, elementary_from_power_sums, poly_mul, F,
)

def test_bm_fibonacci():
    fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    C = berlekamp_massey(fib)
    assert C == [F(1), F(-1), F(-1)], C

def test_newton_roundtrip():
    e = [F(3), F(1), F(-2)]
    p = power_sums_from_elementary(e, 8)
    e2 = elementary_from_power_sums(p, 3)
    assert e2 == e, (e, e2)

def test_satake_pipeline():
    satake = [F(1), F(-1), F(2)]            # 1 - T + 2T^2 : a=1, b=2
    p = power_sums_from_satake(satake, 12)
    assert p[0] == 1 and p[1] == -3, p[:2]  # p1=a, p2=a^2-2b
    h = coefficient_sequence_from_satake(satake, 12)
    for k in range(2, 12):                   # h_k = h_{k-1} - 2 h_{k-2}
        assert h[k] == h[k - 1] - 2 * h[k - 2]
    back = satake_poly_from_power_sums(p[:2], 2)
    assert back == satake, back

def test_sym2_and_rankin_selberg_defect():
    a, b = F(1), F(2)
    satake = [F(1), -a, b]
    p = power_sums_from_satake(satake, 40)
    ps2 = op_sym2(p, 10)
    assert ps2[0] == p[0] ** 2 - b, ps2[0]   # p1(Sym^2) = a^2 - b = alpha^2+ab+b^2... check: a^2-b = 1-2 = -1
    sym2_satake = satake_poly_from_power_sums(ps2[:3], 3)
    # pointwise square of coefficient sequence
    h = coefficient_sequence_from_satake(satake, 20)
    hsq = [x * x for x in h]
    pq = minimal_rational_form(hsq)
    assert pq is not None
    P, Q = pq
    assert Q == sym2_satake, (Q, sym2_satake)          # denominator = Sym^2 local factor
    assert P == [F(1), b], P                            # numerator defect = 1 + b T
    # so: sum h_k^2 T^k = (1 + b T) / det(1 - Sym^2(A) T)   [Rankin-Selberg local identity]

def test_adams_tensor():
    satake = [F(1), F(-1), F(2)]
    p = power_sums_from_satake(satake, 24)
    p2 = op_adams(p, 2, 12)
    assert p2[0] == p[1]
    pt = op_tensor(p, p, 12)
    assert pt[0] == p[0] ** 2

def test_sym_k_matches_sym2():
    satake = [F(1), F(-1), F(2)]
    p = power_sums_from_satake(satake, 40)
    a = op_sym2(p, 8)
    b = op_sym_k(p, 2, 2, 8)
    assert a == b, (a, b)

def test_sturm():
    p = [F(-2), F(0), F(1)]                 # T^2 - 2
    assert count_real_roots_in(p, 1, 2) == 1
    assert count_real_roots_in(p, 2, 3) == 0
    assert certify_root_above([F(-8), F(0), F(1)], 2)      # sqrt 8 > 2
    assert not certify_root_above([F(-8), F(0), F(1)], 3)

def test_charpoly_matrix():
    cp = charpoly_of_matrix([[0, 1], [1, 0]])
    assert cp == [F(-1), F(0), F(1)], cp    # T^2 - 1

def test_series_roundtrip():
    P, Q = [F(1), F(3)], [F(1), F(-1), F(5), F(2)]
    s = series_of_rational(P, Q, 30)
    pq = minimal_rational_form(s)
    assert pq is not None and pq[0] == P and pq[1] == Q, pq

if __name__ == "__main__":
    import sys, inspect
    mod = sys.modules["__main__"]
    fails = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn(); print(f"PASS {name}")
            except AssertionError as e:
                fails += 1; print(f"FAIL {name}: {e}")
    sys.exit(1 if fails else 0)
