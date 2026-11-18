#!/usr/bin/env python3
"""Check arithmetic constants and extract the explicit tail bounds with Arb."""

from flint import arb, ctx


def tail_bound(height):
    y = arb(height)
    h = (4 * y).log()
    return (6_240_000 / y) * (h**4 + 4 * h**3 + 12 * h**2 + 24 * h + 24)


if __name__ == "__main__":
    ctx.prec = 128
    pi = arb.pi()
    e = arb(1).exp()
    assert 1 + 6 * pi.sqrt() < 12
    assert 12 * e * pi.sqrt() < 60
    assert 12 * pi * e**2 < 300
    assert e**2 * arb(5) / 4 < 10
    assert e**3 < 21
    assert arb(64).log() > 4
    assert 21 * 3000 < 65000
    assert 2 * 65000 * 2 == 260_000
    assert 2 * 6 * 260_000 == 3_120_000
    assert 6_240_000 * arb(103) / 32 < 21_000_000

    one_percent = arb("0.0025253801685456458")
    assert tail_bound(100) < arb("1.715e8")
    assert tail_bound(5 * 10**15) > one_percent
    assert tail_bound(6 * 10**15) < arb("0.00235")
    assert arb("0.00235") + arb("0.00017") < one_percent
    for height in (100, 5 * 10**15, 6 * 10**15):
        print(f"Y={height}: {tail_bound(height)}")
