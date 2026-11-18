#!/usr/bin/env python3
"""Check the sharper block constants and optionally certify two Hardy integrals per block."""

from argparse import ArgumentParser

from flint import __FLINT_VERSION__, acb, acb_series, arb, ctx


def analytic_tail(height):
    """Dyadic majorant with the exact radius switch at log(T)=8."""
    height = arb(height)
    finite = arb(0)
    while height.log() < 8:
        finite += 3600 * 64 * height.log() / height
        height *= 2
    assert height.log() >= 8
    h, b = height.log(), arb(2).log()
    polynomial = 2*h**4 + 8*b*h**3 + 36*b**2*h**2 + 104*b**3*h + 150*b**4
    return finite + (450 / height) * polynomial


def check_constants():
    e, pi = arb(1).exp(), arb.pi()
    assert (2*pi/arb("0.89")).log() + pi/89 + arb(9)/(32*89**2) < 2
    assert e.sqrt() < arb(5) / 3
    assert 2*pi - arb("4.02") > 2
    assert 1 + arb("4.02") / 9 < arb(3) / 2
    assert (arb("2.01")**2 + (arb(3)/400)**2).sqrt() * 2 < arb("4.04")
    assert arb("4.04") * 3 / pi + arb("0.5") + arb("0.51")/arb("0.89") < 6
    assert arb("1.12") * 120 * e**2 < 1000
    gaussian_factor = arb("0.49").exp() * pi.sqrt() * arb("0.8")
    assert gaussian_factor * (1 + 2*pi.sqrt()*arb("0.51")/arb("0.8")) < arb("7.6")
    assert e**2 / arb(100).log() + arb(2).sinh() / 2 < arb("3.5")
    assert 1000 < arb("2.2") * 100 * arb(100).log()
    assert (arb(45).sqrt() + arb("2.2").sqrt())**2 < 68
    x = arb(1) / 400
    assert 24 * 68 * (1 + 15*x) * (2 + 30*x + 600*x*x) < 3600
    assert analytic_tail(100) + arb("0.25253801685456460") < 24959
    assert analytic_tail(10**12) < arb("0.0006")
    assert analytic_tail(2 * 10**11) < arb("0.002312")
    assert arb("0.002312") + arb("0.00021") < arb("0.0025253801685456458")


def hardy_derivative_square(t, order, cutoff, height, log_pi):
    # On this rectangle every argument of lgamma has positive real part,
    # and zeta's pole is outside the rectangle. This checks analyticity for
    # the integrator's complex evaluation balls as well as real samples.
    if not abs(t.imag) < arb(1) / 4:
        return acb(arb("nan"))
    w = acb_series([t, 1], order + 1)
    s = arb(1)/2 + 1j*w
    log_a = ((s/2).lgamma() - ((1-s)/2).lgamma() - (s-arb(1)/2)*log_pi)/2
    hardy = log_a.exp() * s.zeta()
    if cutoff:
        x = 10*w/height - 9
        hardy *= 3*x*x - 2*x*x*x
    derivative = hardy[order] * (2 if order == 2 else 1)
    return derivative * derivative


def integrate_block(height):
    integrals = {}
    log_pi = arb.pi().log()
    left = arb(9*height) / 10
    for order in (1, 2):
        total = acb(0)
        for lo, hi, cutoff in ((left, height, True), (height, 2*height, False)):
            while lo < hi:
                right = lo + 50
                if right > hi:
                    right = hi
                part = acb.integral(
                    lambda t, _: hardy_derivative_square(t, order, cutoff, height, log_pi),
                    lo, right, abs_tol=arb("0.01"), rel_tol=arb("0.00001"),
                    eval_limit=15000,
                )
                assert part.is_finite() and part.imag.contains(0), (height, order, lo, right)
                total += part
                lo = right
        assert total.real > 0
        integrals[order] = total.real
    # Reflection, the factor 2 in the variation integral, and |Q_2|^2<6.
    upper = 24 * (integrals[1] * integrals[2]).sqrt() / (height * height)
    print(f"Y={height}, first and second squared norms: {integrals}; contribution <= {upper}",
          flush=True)
    return upper


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--blocks", type=int, default=0, choices=range(3))
    args = parser.parse_args()
    ctx.prec = 128
    check_constants()
    print(f"FLINT {__FLINT_VERSION__}, analytic tail at 100: {analytic_tail(100)}")
    print(f"Analytic tail at 10^12: {analytic_tail(10**12)}", flush=True)
    if args.blocks:
        ctx.prec = 64
        total = arb(0)
        for index in range(args.blocks):
            total += integrate_block(100 * 2**index)
        final = total + analytic_tail(100 * 2**args.blocks)
        cutoff = arb("14350.499") if args.blocks == 1 else arb("8248.95")
        assert final < cutoff
        print(f"Spliced upper bound on the complete tail at 100: {final}")
