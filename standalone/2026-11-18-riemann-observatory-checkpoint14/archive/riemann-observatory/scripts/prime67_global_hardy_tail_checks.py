#!/usr/bin/env python3
"""Arb verification of the global Hardy variation bound."""
import argparse
import json
from fractions import Fraction
from math import factorial

from flint import __FLINT_VERSION__, arb, ctx

RATIO = Fraction(3, 2)
TRUNCATION = Fraction(7, 25)
WINDOW = 100
RADIUS = ("0", "0.16", "0.32")


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


def remainder_norms(t, length):
    d = ball(TRUNCATION)
    phase_speed = arb("5.36")
    two_pi = 2*arb.pi()
    modes = (1/(two_pi-phase_speed) + 1/two_pi
             + (arb.pi()**2/6-1)*(1/(two_pi-phase_speed/2)+1/two_pi))/arb.pi()
    constant = d+2/t+arb("0.5")+phase_speed*modes
    norms = []
    for j, radius in enumerate(RADIUS):
        rad = arb(radius)
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


def block(height, end):
    t, u = ball(height), ball(end)
    center = ((t*u).sqrt()/(2*arb.pi())).log()/2
    phase = (u/t).log()/4+arb.pi()/(2*t)+1/(16*t**2)
    m = (height*TRUNCATION).__ceil__()
    return hardy_norms(polynomial_norms(height, end, center, m),
                       remainder_norms(t, 1/t-1/u), phase, 1/t)


def residual_coefficients(height):
    """Bounds for ||G^(j)/t|| on all blocks T>=height, normalized by log(T)^(j+.5)/sqrt(T)."""
    t = ball(height)
    h = t.log()
    d = ball(TRUNCATION)
    r = ball(RATIO)
    phase = r.log()/4+arb.pi()/(2*t)+1/(16*t**2)
    length = 1-1/r
    # All resulting normalized coefficients decrease as the base t increases.
    v = []
    for j in range(3):
        p = 2*j
        omega = 1+2/h
        diagonal = omega**(p+1)/(p+1)+(3+2*(arb(2).log()+2/(d*t)))*omega**p/h
        hilbert = diagonal/t + (2*d+5/t)*omega**p/h
        v.append(((length*diagonal+3*arb.pi()*hilbert)/2**p).sqrt())
    e = [x*t.sqrt()/(h**j*h.sqrt()) for j, x in
         enumerate(remainder_norms(t, length/t))]
    return hardy_norms(v, e, phase/h, 1/(t*h*h), scale=h)


def residual(height):
    t = ball(height)
    h, b = t.log(), ball(RATIO).log()
    # exp((2j+1)*bk/h) bounds (1+bk/h)^(2j+1).
    return [c**2*h**(2*j+1)/t/(1-(b*(arb(2*j+1)/h-1)).exp())
            for j,c in enumerate(residual_coefficients(height))]


def check(height, blocks):
    start = height-WINDOW
    assert start >= 9900
    assert blocks >= 1
    t = arb(start)
    r = ball(RATIO)
    d = ball(TRUNCATION)
    assert (r+arb("0.4")/t+arb("0.9")/t)/d < arb("5.36")
    assert (2*arb.pi()/(1-arb("0.4")/t)).log()+arb.pi()/(t-arb("0.4")) + 1/t**2 < arb("1.86")
    assert d**2*t > 1
    assert d*arb("0.4")+arb("0.8")/t < 1
    assert 2*(d+1/t) < 1
    assert 1/t+arb.pi()/4 < 1
    assert (4*(d+1/t)*arb.pi()/r.sqrt()).log() < 2

    sums = [arb(0) for _ in range(3)]
    for k in range(blocks):
        low = start*RATIO**k
        norms = block(low, low*RATIO)
        sums = [total+norm**2 for total, norm in zip(sums, norms)]
    rem = residual(start*RATIO**blocks)
    a0, a1, a2 = [(finite+rest).sqrt() for finite, rest in zip(sums, rem)]
    b0, b1, _ = block(Fraction(start), Fraction(height))
    cutoff1 = arb(3)/(2*WINDOW)
    cutoff2 = arb(6)/WINDOW**2
    h1 = a1+a0/t+cutoff1*b0
    h2 = a2+2*a1/t+2*a0/t**2+2*cutoff1*(b1+b0/t)+cutoff2*b0
    tail_upper = 2*h1*h2
    if height == 10000 and blocks == 28:
        assert tail_upper < arb("0.48494")
        assert tail_upper + arb("0.61649875288731141830") < arb("1.10144")
    if height == 3000000 and blocks == 28:
        assert tail_upper < arb("0.0059909")
        assert tail_upper + arb("0.00017") < arb("0.61649875288731141829")/100
    return {"flint": __FLINT_VERSION__, "precision": ctx.prec,
            "height": height, "blocks": blocks,
            "norms": [str(x) for x in (a0, a1, a2)],
            "infinite_remainder_norm_squares": [str(x) for x in rem],
            "lower_transition_norms": [str(x) for x in (b0, b1)],
            "tail_upper_expression": str(tail_upper)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--height", type=int, default=10000)
    parser.add_argument("--blocks", type=int, default=28)
    parser.add_argument("--precision", type=int, default=128)
    args = parser.parse_args()
    ctx.prec = args.precision
    print(json.dumps(check(args.height, args.blocks), indent=2))
