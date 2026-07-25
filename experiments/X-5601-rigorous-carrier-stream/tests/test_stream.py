"""Adversarial tests for the X-5601 rigorous carrier stream.

Agent: opus5-01   Issue: #55 / #28

Every test here is fail-closed: it either establishes a bound or fails.  The
oracle used by `test_oracle_agreement` is `reference_stream.py`, an independent
mpmath implementation that shares no code path with the C producer.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

import numpy as np
import pytest
from mpmath import mp, mpf

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)

import analyze_stream as A                                   # noqa: E402
import reference_stream as R                                 # noqa: E402

BIN = os.path.join(HERE, "carrier_stream")
BIN_ALT = os.path.join(HERE, "carrier_stream_alt")

# Known values of pi(10^k).
PI_10K = {3: 168, 4: 1229, 5: 9592, 6: 78498, 7: 664579, 8: 5761455,
          9: 50847534, 10: 455052511, 11: 4118054813}


def run_producer(binary, power10, cells, threads, tmp_path):
    os.makedirs(str(tmp_path), exist_ok=True)
    out = os.path.join(str(tmp_path), f"s{power10}-{cells}.json")
    subprocess.run([binary, "--cutoff-power10", str(power10),
                    "--cells", str(cells), "--threads", str(threads),
                    "--out", out], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return A.load_stream(out)


@pytest.mark.parametrize("power10,cells", [(3, 8), (4, 16), (5, 16), (6, 1024)])
def test_oracle_agreement(power10, cells, tmp_path):
    """The C producer must match an independent 60-digit mpmath computation."""
    st = run_producer(BIN, power10, cells, 4, tmp_path)
    ref = R.stream(10 ** power10, cells, 94184072727073, 20, 60)
    mp.dps = 60
    worst = mpf(0)
    for name in ("z_real", "z_imag", "weight"):
        for fast, exact in zip(st[name], ref[name]):
            fr = A.dd_fraction(fast)
            got = mpf(fr.numerator) / mpf(fr.denominator)
            worst = max(worst, abs(got - mpf(exact)))
    # The L-5601 model allows W_d * sqrt(2) * 1e-17 per lag; the observed
    # agreement is many orders of magnitude better.  Assert both.
    model = float(st["_btot"]) * 1.5e-17
    assert float(worst) <= model, "producer exceeds its own error model"
    assert float(worst) < 1e-18, f"unexpectedly weak agreement {float(worst)}"


def test_counts(tmp_path):
    """Complete prime-power enumeration, checked against known pi(10^k)."""
    for power10 in (5, 6, 7):
        st = run_producer(BIN, power10, 32, 4, tmp_path)
        assert st["prime_count"] == PI_10K[power10]
        # higher prime powers, counted independently here
        n = 10 ** power10
        expect = 0
        sieve = bytearray([1]) * (int(n ** 0.5) + 2)
        for i in range(2, len(sieve)):
            if sieve[i]:
                for j in range(i * i, len(sieve), i):
                    sieve[j] = 0
        for p in range(2, len(sieve)):
            if sieve[p]:
                q = p * p
                while q <= n:
                    expect += 1
                    q *= p
        assert st["higher_prime_power_count"] == expect


def test_thread_invariance(tmp_path):
    """Accumulation order must not move the result beyond the model bound."""
    a = run_producer(BIN, 6, 1024, 1, tmp_path / "a")
    b = run_producer(BIN, 6, 1024, 4, tmp_path / "b")
    for name in ("z_real", "z_imag"):
        worst = max(abs(A.dd_fraction(x) - A.dd_fraction(y))
                    for x, y in zip(a[name], b[name]))
        assert float(worst) < 1e-25


@pytest.mark.skipif(not os.path.exists(BIN_ALT), reason="alt binary not built")
def test_table_invariance(tmp_path):
    """A completely different argument reduction must give the same stream.

    `carrier_stream_alt` is built with JBITS=14 and TRIGBITS=10, so every
    mantissa anchor, every residual z and every trigonometric anchor differs.
    """
    a = run_producer(BIN, 6, 1024, 4, tmp_path / "a")
    b = run_producer(BIN_ALT, 6, 1024, 3, tmp_path / "b")
    for name in ("z_real", "z_imag"):
        worst = max(abs(A.dd_fraction(x) - A.dd_fraction(y))
                    for x, y in zip(a[name], b[name]))
        assert float(worst) < 1e-18


def test_longdouble_regression(tmp_path):
    """Reproduce the failure mode the directed reduction exists to avoid.

    The np.longdouble phase reduction used by the earlier discovery streams
    must disagree with the directed stream by far more than the leading margin
    when it is extrapolated to the target amplitude.
    """
    st = run_producer(BIN, 7, 1024, 4, tmp_path)
    cutoff, cells = 10 ** 7, 1024
    carrier = np.longdouble("4709203636353.65")
    two_pi = np.longdouble(2) * np.longdouble(np.pi)
    n = cutoff
    sieve = bytearray([1]) * (n + 1)
    sieve[0:2] = b"\x00\x00"
    i = 2
    while i * i <= n:
        if sieve[i]:
            sieve[i * i:: i] = bytearray(len(range(i * i, n + 1, i)))
        i += 1
    primes = np.array([p for p in range(2, n + 1) if sieve[p]], dtype=np.int64)
    q = primes.astype(np.longdouble)
    logq = np.log(q)
    logc = np.log(np.longdouble(cutoff))
    phase = np.remainder(carrier * logq, two_pi).astype(np.float64)
    amp = (np.log(q) / (np.longdouble(np.pi) * np.sqrt(q))).astype(np.float64)
    r = (cells * (logq / logc)).astype(np.float64)
    d = np.floor(r).astype(np.int64)
    f = r - d
    zre = np.zeros(cells)
    zim = np.zeros(cells)
    for lag, w in ((d, (1 - f) * amp), (d + 1, f * amp)):
        ok = (lag >= 0) & (lag < cells)
        np.add.at(zre, lag[ok], (w * np.cos(phase))[ok])
        np.add.at(zim, lag[ok], (-w * np.sin(phase))[ok])
    # ordinary primes only on both sides, so compare the prime-only difference
    dev = max(abs(zre[i] - float(st["_zre"][i])) + abs(zim[i] - float(st["_zim"][i]))
              for i in range(cells))
    # at c=1e7 the total amplitude is ~2000; the deviation must already dwarf
    # any bound the L-5601 model would give
    assert dev > 1e-6, ("the long-double reduction was unexpectedly accurate; "
                        "re-derive the regression threshold before trusting it")


def test_gram_bound_brackets_known_spectrum():
    """The universal bound must be an upper bound and must not be absurd."""
    rng = np.random.default_rng(20260725)
    n = 64
    x = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    mat = (x + x.conj().T) / (2 * np.sqrt(n))
    true_max = float(np.linalg.eigvalsh(mat)[-1])
    got = None
    for extra in (1e-9, 1e-8, 1e-7, 1e-6):
        got = A.gram_upper_bound(mat, true_max + extra)
        if got is not None:
            break
    assert got is not None
    assert got["lambda_max_upper"] >= true_max
    assert got["lambda_max_upper"] - true_max < 1e-5


def test_gram_bound_fails_closed():
    """Below the true lambda_max the factorization must not succeed."""
    n = 48
    mat = np.diag(np.linspace(0.5, 3.0, n)).astype(np.complex128)
    assert A.gram_upper_bound(mat, 2.0) is None       # 2.0 < lambda_max = 3.0
    assert A.gram_upper_bound(mat, 3.001) is not None


def test_symbol_bound_is_an_upper_bound():
    """sup sigma must dominate lambda_max of the finite section."""
    rng = np.random.default_rng(7)
    k = 128
    zre = rng.normal(size=k)
    zim = rng.normal(size=k)
    zim[0] = 0.0
    st = {"cells": k,
          "_zre": [A.Fraction(v).limit_denominator(10 ** 12) for v in zre],
          "_zim": [A.Fraction(v).limit_denominator(10 ** 12) for v in zim]}
    sym = A.symbol_sup(st, 16)
    mat = A.toeplitz_matrix(st)
    assert float(np.linalg.eigvalsh(mat)[-1]) <= sym["sup_upper"]
    assert float(np.linalg.eigvalsh(mat)[0]) >= sym["inf_lower"]


def test_lag_error_model_is_monotone_and_positive():
    st = {"cells": 4,
          "_w": [A.Fraction(1), A.Fraction(10), A.Fraction(100), A.Fraction(0)],
          "_btot": A.Fraction(111)}
    errs = A.lag_error_bounds(st)
    assert all(e > 0 for e in errs)
    assert errs[2] > errs[1] > errs[0] > errs[3]


def test_exact_autocorrelation_matches_direct_product():
    rng = np.random.default_rng(11)
    k, bits = 9, 20
    re = [int(v) for v in rng.integers(-1000, 1000, k)]
    im = [int(v) for v in rng.integers(-1000, 1000, k)]
    corr = A.exact_autocorrelation(re, im, bits)
    w = (np.array(re) + 1j * np.array(im)) / float(1 << bits)
    for d in range(k):
        direct = complex(np.dot(np.conj(w[:k - d]), w[d:]))
        assert abs(float(corr[d][0]) - direct.real) < 1e-12
        assert abs(float(corr[d][1]) - direct.imag) < 1e-12


def test_correction_gate_hypothesis_and_size():
    g = A.correction_gate(10 ** 11, 1024, 94184072727073, 20)
    assert g["b_le_1_over_20"] is True
    assert 1e-10 < g["B_arch_float"] < 2e-10
    assert g["R_norm_float"] < 1e-16
    assert abs(g["ell_T_float"] - 4.3517199520883178) < 1e-12


def test_explicit_formula_dictionary_small():
    """Guard the D-0801 normalization against genuine zeta zeros (T-5601).

    Small and fast: the point is to catch a factor of 2, a factor of 2*pi, a
    sign flip, or a Gamma(s) vs Gamma(s/2) slip, all of which would show up as
    a discrepancy of tens of percent.  The residual here is dominated by the
    density-tail approximation of the zero sum.
    """
    import verify_dictionary as V
    from mpmath import mp, mpf, mpc, log, pi, zetazero

    mp.dps = 20
    cutoff, k = 30, 3
    L = log(mpf(cutoff))
    delta = L / (2 * pi)
    T = zetazero(1).imag
    v = [mpc(1, 0), mpc(0, mpf(1) / 2), mpc(mpf(-1) / 3, mpf(1) / 4)]
    prime, _ = V.prime_side(v, delta, T, cutoff)
    arch = V.arch_compact(v, delta, T, L)
    pole = 2 * mp.re(V.g_test(mpc(0, mpf(1) / 2), v, delta, T))
    rhs = arch + pole - prime
    zsum, ztail, _ = V.zero_sum(v, delta, T, 60, T + 200)
    lhs = zsum + ztail
    rel = abs(rhs - lhs) / abs(rhs)
    assert float(rel) < 2e-3, f"dictionary mismatch, relative {float(rel)}"
