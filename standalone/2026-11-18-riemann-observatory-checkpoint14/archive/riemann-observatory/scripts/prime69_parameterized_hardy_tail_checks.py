#!/usr/bin/env python3
"""Arb verification of the global Hardy variation bound."""
import argparse
import json
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from math import factorial

from flint import __FLINT_VERSION__, acb, acb_series, arb, ctx

@dataclass(frozen=True)
class Parameters:
    ratio: Fraction
    truncation: Fraction
    window: Fraction
    radii: tuple[Fraction, Fraction]

    @property
    def disk(self):
        return max(self.radii)


SELECTED = Parameters(Fraction(1607, 1000), Fraction(143, 500), Fraction(22),
                      (Fraction(219, 1000), Fraction(433, 1000)))


def ball(q):
    return arb(q.numerator) / q.denominator if isinstance(q, Fraction) else arb(q)


def moment(a, b, step, power, center, harmonic):
    """Upper bound on the moment on an integer progression, endpoints included."""
    a, b = arb(a), arb(b)

    def density(x):
        return (x.log() - center)**power / (x if harmonic else 1)

    def primitive(x):
        u = x.log() - center
        if harmonic:
            return u**(power+1) / (power+1)
        return x * sum((-1)**k * (factorial(power)//factorial(power-k))
                       * u**(power-k) for k in range(power+1))

    # Total variation is the sum of differences at the turning points.
    # If a critical point overlaps an endpoint ball, include it anyway:
    # this only overestimates variation on the integration interval.
    heights = [density(a)]
    if power and not (center.exp() < a or center.exp() > b):
        heights.append(arb(0))
    if harmonic and power and not ((center+power).exp() < a
                                   or (center+power).exp() > b):
        heights.append((-(center+power)).exp()*power**power)
    heights.append(density(b))
    variation = sum(abs(y-x) for x, y in zip(heights, heights[1:]))
    return (primitive(b)-primitive(a))/step + (heights[0]+heights[-1]+variation)/2


def polynomial_norms(height, end, center, m):
    t, u = ball(height), ball(end)
    length = 1/t - 1/u
    first_even = 2*(m//2+1)
    out = []
    for j in range(3):
        power = 2*j
        head = sum((arb(n).log()-center)**power/n for n in range(1, 33))
        head += moment(33, m, 1, power, center, True)
        tail = 4*moment(first_even, 2*m, 2, power, center, True)
        diagonal = head + tail
        exception = 2*(arb(first_even).log()-center)**power if m % 2 else 0
        hilbert = diagonal + moment(1, m, 1, power, center, False) + 2*moment(
            first_even, 2*m, 2, power, center, False) + exception
        out.append((length*diagonal+3*arb.pi()/t**2*hilbert).sqrt())
    return out


def remainder_norms(t, length, ratio, p):
    d, a = ball(p.truncation), ball(p.disk)
    sigma = arb("0.5")+a
    positive_speed = (ratio+a/t)/d
    absolute_speed = positive_speed + sigma**2/(2*d*t*(t-a))
    negative_speed = (1-a/t)/(d+1/t)
    two_pi = 2*arb.pi()
    n_max = 8
    modes = sum(1/(n*(two_pi*n-positive_speed)) +
                1/(n*(two_pi*n+negative_speed)) for n in range(1, n_max+1))
    zeta_tail = arb.pi()**2/6 - sum(arb(1)/n**2 for n in range(1, n_max+1))
    modes += zeta_tail*(1/(two_pi-positive_speed/(n_max+1))+1/two_pi)
    constant = (d+1/t)/(1-a/t)+arb("0.5")+absolute_speed*modes/arb.pi()
    norms = []
    for j, radius in enumerate((Fraction(), *p.radii)):
        rad = ball(radius)
        sup = constant*(arb("1.86")*rad/2).exp()*d**(rad-arb("0.5"))*t**(
            (rad-1)/2)
        norms.append(factorial(j)*sup/(rad**j if j else 1)*length.sqrt())
    return norms


def hardy_norms(polynomial, remainder, phase, curvature, scale=1):
    p0 = 1+arb(2).sqrt()
    p1 = arb(2).sqrt()*arb(2).log()/scale
    p2 = p1*arb(2).log()/scale
    v0, v1, v2 = polynomial
    e0, e1, e2 = remainder
    return (v0+p0*e0,
            v1+phase*v0+p0*e1+p1*e0,
            v2+2*phase*v1+(phase**2+curvature)*v0+p0*e2+2*p1*e1+p2*e0)


def block(height, end, p):
    t, u = ball(height), ball(end)
    center = ((t*u).sqrt()/(2*arb.pi())).log()/2
    phase = (u/t).log()/4+arb.pi()/(2*t)+1/(16*t**2)
    m = (height*p.truncation).__ceil__()
    return hardy_norms(polynomial_norms(height, end, center, m),
                       remainder_norms(t, 1/t-1/u, u/t, p), phase, 1/t)


def residual_coefficients(height, p):
    """Bounds for ||G^(j)/t|| on all blocks T>=height, normalized by log(T)^(j+.5)/sqrt(T)."""
    t = ball(height)
    h = t.log()
    d = ball(p.truncation)
    r = ball(p.ratio)
    phase = r.log()/4+arb.pi()/(2*t)+1/(16*t**2)
    length = 1-1/r
    # All resulting normalized coefficients decrease as the base t increases.
    v = []
    for j in range(3):
        power = 2*j
        omega = 1+2/h
        diagonal = omega**(power+1)/(power+1)+(3+2*(arb(2).log()+2/(d*t)))*omega**power/h
        hilbert = diagonal/t + (2*d+5/t)*omega**power/h
        v.append(((length*diagonal+3*arb.pi()*hilbert)/2**power).sqrt())
    e = [x*t.sqrt()/(h**j*h.sqrt()) for j, x in
         enumerate(remainder_norms(t, length/t, r, p))]
    return hardy_norms(v, e, phase/h, 1/(t*h*h), scale=h)


def residual(height, p):
    t = ball(height)
    h, b = t.log(), ball(p.ratio).log()
    # exp((2j+1)*bk/h) bounds (1+bk/h)^(2j+1).
    return [c**2*h**(2*j+1)/t/(1-(b*(arb(2*j+1)/h-1)).exp())
            for j,c in enumerate(residual_coefficients(height, p))]


@lru_cache(maxsize=16)
def endpoint(height, precision):
    """Norm square and real radial derivative product of G(t)/t."""
    t = arb(height)
    i = acb(0, 1)
    exponent = arb(2).log()
    exponential = arb(2).sqrt()*(-i*t*exponent).exp()
    q, dq = exponential-1, -i*exponent*exponential
    z = acb_series([acb(arb("0.5"), t), i], 2).zeta()
    value = q*z[0]/t
    derivative = (dq*z[0]+q*z[1]-value)/t
    return abs(value)**2, (derivative*value.conjugate()).real


def calculate(height, blocks, p):
    start = height-p.window
    assert 0 < p.window < height
    assert p.ratio > 1
    assert p.truncation > 0
    assert all(0 < radius < Fraction(1, 2) for radius in p.radii), "disk reaches outside the positive strip"
    assert blocks >= 1
    t, r, d, a = ball(start), ball(p.ratio), ball(p.truncation), ball(p.disk)
    assert t.log() > 5
    assert start*p.truncation >= 34
    assert height <= start*p.ratio, "transition exceeds a ratio block"
    assert (r+a/t)/d < 2*arb.pi(), "positive Fourier mode may be stationary"
    assert r+a/t < 2*arb.pi()
    assert (2*arb.pi()/(1-a/t)).log()+arb.pi()/(t-a)+arb("0.5")/(t-a)**2 < arb("1.86")
    assert d**2*t > 1
    assert 1/t+arb.pi()/4 < 1
    # The envelope |log(x)-center| <= (log(T)+2)/2 on subsequent blocks.
    assert r.sqrt() <= 2*arb.pi()
    assert (2*(d+1/t))**2*2*arb.pi()/r.sqrt() < arb(2).exp(), "log-moment envelope fails"

    sums = [arb(0) for _ in range(3)]
    for k in range(blocks):
        low = start*p.ratio**k
        norms = block(low, low*p.ratio, p)
        sums = [total+norm**2 for total, norm in zip(sums, norms)]
    rem = residual(start*p.ratio**blocks, p)
    a0, a1, a2 = [(finite+rest).sqrt() for finite, rest in zip(sums, rem)]
    b0, b1, _ = block(start, Fraction(height), p)
    width = ball(p.window)
    value_squared, radial_product = endpoint(height, ctx.prec)
    endpoint_correction = 12*(value_squared/width-radial_product)/width**2
    h1 = ((a1+a0/t)**2 + 6*b0**2/width**2).sqrt()
    h2 = ((a2+2*a1/t+2*a0/t**2)**2 + 24*(b1+b0/t)**2/width**2
          + endpoint_correction).sqrt()
    return 2*h1*h2, (a0, a1, a2), (b0, b1), rem, endpoint_correction


def check(height, blocks, p):
    tail_upper, norms, transition, residual_squares, correction = calculate(height, blocks, p)
    if p == SELECTED and blocks == 64:
        if height == 10000:
            assert tail_upper < arb("0.45906151")
            assert tail_upper+arb("0.61649875288731141830") < arb("1.075561")
        if height == 2800000:
            assert tail_upper < arb("0.00591413")
            assert tail_upper+arb("0.00025") < arb("0.61649875288731141829")/100
    return {"flint": __FLINT_VERSION__, "precision": ctx.prec,
            "height": height, "blocks": blocks,
            "parameters": {"ratio": str(p.ratio), "truncation": str(p.truncation),
                           "window": str(p.window), "radii": list(map(str, p.radii))},
            "norms": list(map(str, norms)),
            "infinite_remainder_norm_squares": list(map(str, residual_squares)),
            "lower_transition_norms": list(map(str, transition)),
            "signed_endpoint_correction": str(correction),
            "tail_upper_expression": str(tail_upper)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--height", type=int, default=10000)
    parser.add_argument("--blocks", type=int, default=64)
    parser.add_argument("--precision", type=int, default=128)
    parser.add_argument("--ratio", type=Fraction, default=SELECTED.ratio)
    parser.add_argument("--truncation", type=Fraction, default=SELECTED.truncation)
    parser.add_argument("--window", type=Fraction, default=SELECTED.window)
    parser.add_argument("--radius1", type=Fraction, default=SELECTED.radii[0])
    parser.add_argument("--radius2", type=Fraction, default=SELECTED.radii[1])
    args = parser.parse_args()
    ctx.prec = args.precision
    params = Parameters(args.ratio, args.truncation, args.window, (args.radius1, args.radius2))
    print(json.dumps(check(args.height, args.blocks, params), indent=2))
