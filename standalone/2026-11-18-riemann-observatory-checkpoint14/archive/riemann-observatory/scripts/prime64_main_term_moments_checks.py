#!/usr/bin/env python3
"""Arb checks for the centered Hardy derivative moment and dyadic tail bounds."""

from math import factorial

from flint import __FLINT_VERSION__, arb, ctx


def coefficient(height):
    v = arb(height)
    h = v.log()
    unit, error = [], []
    for j in range(3):
        unit.append((arb("1.2") / (2*j+1) + arb("6.4") / h).sqrt() / 2**j)
        error.append(12 * factorial(j) * 4**j * v**(-arb(3)/8) / (h**j * h.sqrt()))
    phase = arb("0.67")
    a0 = unit[0] + error[0]
    a1 = unit[1] + phase * unit[0] / h + error[1]
    a2 = unit[2] + 2 * phase * unit[1] / h + (phase**2 + 1/v) * unit[0] / h**2 + error[2]
    return 12 * (a1 + 15*a0/(v*h)) * (a2 + 30*a1/(v*h) + 600*a0/(v*h)**2)


def tail_bound(height, blocks):
    total = arb(0)
    for index in range(blocks):
        low = height * 2**index
        total += coefficient(low) * arb(low).log()**4 / low
    low = height * 2**blocks
    h, b = arb(low).log(), arb(2).log()
    polynomial = 2*h**4 + 8*b*h**3 + 36*b**2*h**2 + 104*b**3*h + 150*b**4
    return total + coefficient(low) * polynomial / low


def check_constants():
    pi, height = arb.pi(), arb(400)
    assert 2 * pi - arb("4.22") > 2
    assert 1 + arb("4.22") / 9 < arb("1.5")
    assert 2*(arb("2.11")**2 + (arb("0.75")/height)**2).sqrt() < arb("4.23")
    assert arb("0.5025") / arb("0.89") < arb("0.57")
    assert arb("4.23") * 3 / pi + arb("0.5") + arb("0.57") < 6
    t = arb("0.89") * height
    assert (2*pi/arb("0.89")).log() + pi/t + arb(9)/(32*t*t) < 2
    assert (arb(1)/2).exp() < arb(5)/3
    phase_deviation = (2*pi*arb("0.5025")/arb("0.9")).log() / 2
    t = arb("0.9") * height
    assert phase_deviation + (pi/t + arb(1)/(8*t*t))/2 < arb("0.67")
    assert 1 / (arb("0.9")**2 * height) + pi / arb("3.6") < 1
    assert 1 + 2/arb(200).sqrt() < arb("1.15")
    assert arb("1.2")*arb("1.15") + 3*pi*(arb("0.5025") + (height.log() + arb("1.15"))/height) < arb("6.4")
    assert arb("28.8") / arb(960).sqrt() < arb("0.93")


if __name__ == "__main__":
    ctx.prec = 128
    check_constants()
    tail_at_400 = tail_bound(400, 8)
    tail_at_200_million = tail_bound(2*10**8, 8)
    assert tail_at_400 < arb("83.05")
    assert arb("83.05") + arb("2.22") + arb("2.13") + arb("0.253") < arb("87.66")
    assert tail_at_200_million < arb("0.00192")
    assert arb("0.00192") + arb("0.00060") < arb("0.0025253801685456458")
    print(f"FLINT {__FLINT_VERSION__}, analytic tail majorant at 400: {tail_at_400}")
    print(f"Analytic tail majorant at 2e8: {tail_at_200_million}")
