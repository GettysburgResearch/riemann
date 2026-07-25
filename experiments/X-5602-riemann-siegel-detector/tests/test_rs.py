"""Validation tests for the X-5602 Riemann-Siegel detector.

Agent: opus5-01   Issue: #55

The oracle is `mpmath.zetazero`, which computes zeros of zeta by an entirely
different route (Euler-Maclaurin / Riemann-Siegel inside mpmath's own zeta,
plus root isolation) and shares no code with `rs_zeta.c`.
"""
from __future__ import annotations

import json
import os
import subprocess

import pytest
from mpmath import mp, zetazero

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BIN = os.path.join(HERE, "rs_zeta")

pytestmark = pytest.mark.skipif(not os.path.exists(BIN),
                                reason="rs_zeta not built")


def eval_Z(t):
    out = subprocess.run([BIN, "--at", repr(t)], check=True,
                         capture_output=True, text=True)
    return float(out.stdout.split()[1])


def scan(t0, span, per_gram, tmp_path, emit=True):
    os.makedirs(str(tmp_path), exist_ok=True)
    js = os.path.join(str(tmp_path), "scan.json")
    zf = os.path.join(str(tmp_path), "zeros.txt")
    cmd = [BIN, "--t0", repr(t0), "--span", repr(span),
           "--per-gram", str(per_gram), "--threads", "2", "--out", js]
    if emit:
        cmd += ["--emit-zeros", "--zeros-file", zf]
    subprocess.run(cmd, check=True, capture_output=True)
    with open(js) as fh:
        res = json.load(fh)
    zeros = [float(x) for x in open(zf)] if emit else []
    return res, zeros


def test_Z_is_small_at_known_zeros():
    """|Z(gamma)| must be far below the O(1) scale of Z between zeros."""
    mp.dps = 25
    for n in (1, 2, 3, 10, 50, 100):
        g = float(zetazero(n).imag)
        z = eval_Z(g)
        # the C0-only remainder error falls like (t/2pi)^{-3/4}
        assert abs(z) < 0.05, (n, g, z)


def test_Z_is_not_small_between_zeros():
    """Guard against a bug that returns ~0 everywhere."""
    mp.dps = 25
    a = float(zetazero(20).imag)
    b = float(zetazero(21).imag)
    z = eval_Z(0.5 * (a + b))
    assert abs(z) > 0.05, z


def test_located_zeros_match_the_oracle(tmp_path):
    res, zeros = scan(1000.0, 60.0, 32, tmp_path)
    assert res["sign_changes"] == len(zeros)
    assert len(zeros) >= 40
    mp.dps = 25
    # locate the oracle index of the first zero above 1000
    lo, hi = 1, 2000
    while lo < hi:
        mid = (lo + hi) // 2
        if float(zetazero(mid).imag) < 1000.0:
            lo = mid + 1
        else:
            hi = mid
    true = [float(zetazero(lo + i).imag) for i in range(len(zeros))]
    err = [abs(x - y) for x, y in zip(zeros, true)]
    assert max(err) < 1e-2, max(err)
    # and the ordering must be strictly increasing with no duplicates
    assert all(zeros[i] < zeros[i + 1] for i in range(len(zeros) - 1))


def test_census_deficit_is_small_at_moderate_height(tmp_path):
    """The count must track (theta(t2)-theta(t1))/pi to within the S(t) range."""
    res, _ = scan(1000.0, 60.0, 32, tmp_path, emit=False)
    assert abs(res["deficit"]) < 3.0, res["deficit"]


def test_grid_convergence(tmp_path):
    """Refining the grid must not keep finding new sign changes."""
    counts = []
    for pg in (16, 32, 64):
        res, _ = scan(1000.0, 60.0, pg, tmp_path / str(pg), emit=False)
        counts.append(res["sign_changes"])
    assert counts[0] == counts[1] == counts[2], counts


def test_refuses_spans_that_change_N(tmp_path):
    """N = floor(sqrt(t/2pi)) constant is a precondition of the table trick."""
    os.makedirs(str(tmp_path), exist_ok=True)
    js = os.path.join(str(tmp_path), "bad.json")
    out = subprocess.run([BIN, "--t0", "100.0", "--span", "100.0",
                          "--per-gram", "8", "--out", js],
                         capture_output=True, text=True)
    assert out.returncode != 0
    assert "N changes" in out.stderr


def test_C0_is_continuous_through_its_removable_singularities():
    """p = 1/4 and 3/4 are removable; a naive C0 would blow up there.

    p = frac(sqrt(t/2pi)), so we hit those p by choosing t = 2 pi (N + p)^2.
    Z must stay O(1) across them rather than spiking.
    """
    import math
    vals = []
    for p in (0.2499, 0.25, 0.2501, 0.7499, 0.75, 0.7501):
        t = 2 * math.pi * (200 + p) ** 2
        vals.append(abs(eval_Z(t)))
    assert max(vals) < 50.0, vals
