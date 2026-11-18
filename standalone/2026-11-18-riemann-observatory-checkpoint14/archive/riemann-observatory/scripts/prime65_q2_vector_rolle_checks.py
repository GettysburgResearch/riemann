#!/usr/bin/env python3
"""Arb checks for the weighted vector-variation tail."""

from math import factorial

from flint import __FLINT_VERSION__, arb, ctx


def coefficient(height):
    v = arb(height)
    h = v.log()
    unit, error = [], []
    for j in range(3):
        correction = arb("6.4") + arb("6.6") * (1 + arb("0.70")/h)**(2*j)
        unit.append((arb("1.2")/(2*j+1) + correction/h).sqrt() / 2**j)
        error.append(arb("32.4")*factorial(j)*4**j*v**(-arb(3)/8)/(h**j*h.sqrt()))
    phase = arb("0.67")
    a0 = unit[0] + error[0]
    a1 = unit[1] + phase*unit[0]/h + error[1]
    a2 = unit[2] + 2*phase*unit[1]/h + (phase**2+1/v)*unit[0]/h**2 + error[2]
    return 2*(a1+15*a0/(v*h))*(a2+30*a1/(v*h)+600*a0/(v*h)**2)


def tail_bound(height, blocks):
    total = arb(0)
    for index in range(blocks):
        low = height*2**index
        total += coefficient(low)*arb(low).log()**4/low
    low = height*2**blocks
    h, b = arb(low).log(), arb(2).log()
    polynomial = 2*h**4 + 8*b*h**3 + 36*b**2*h**2 + 104*b**3*h + 150*b**4
    return total + coefficient(low)*polynomial/low


if __name__ == "__main__":
    ctx.prec = 128
    assert arb(2).log() + (1+arb(1)/200).log() < arb("0.70")
    assert 2*(arb(2).log()+arb(1)/199)<arb("1.4")
    assert arb("1.2")*arb("1.4")+3*arb.pi()*(arb("0.5025")+arb("4.4")/400)<arb("6.6")
    assert 1+arb(2)**(arb(3)/4)<arb("2.7")
    bound = tail_bound(10000, 8)
    assert bound<arb("1.790676")
    assert arb("0.616499")+arb("1.790676")<arb("2.40718")
    print(f"FLINT {__FLINT_VERSION__}, vector-variation tail at 10000: {bound}")
