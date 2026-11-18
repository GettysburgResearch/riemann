#!/usr/bin/env python3
"""Outward bounds for weighted Hardy norms using variable Hilbert coefficients."""
import argparse
from fractions import Fraction
from math import factorial

from flint import acb, acb_series, arb, ctx


def ball(x):
    return arb(x.numerator) / x.denominator if isinstance(x, Fraction) else arb(x)


def progression(a, b, h, p, c, harmonic):
    """Upper bound via the composite trapezoid error and total variation."""
    a, b = arb(a), arb(b)
    u, v = a.log() - c, b.log() - c
    if harmonic:
        ia, ib = u**(p+1)/(p+1), v**(p+1)/(p+1)
        fa, fb = u**p/a, v**p/b
    else:
        ia = a * sum((-1)**k * factorial(p)//factorial(p-k) * u**(p-k)
                     for k in range(p+1))
        ib = b * sum((-1)**k * factorial(p)//factorial(p-k) * v**(p-k)
                     for k in range(p+1))
        fa, fb = u**p, v**p
    points = [fa]
    if p and not (u > 0 or v < 0):
        points.append(arb(0))
    if harmonic and p and not (u > p or v < p):
        points.append(p**p * (-c-p).exp())
    points.append(fb)
    variation = sum(abs(y-x) for x, y in zip(points, points[1:]))
    return (ib-ia)/h + (fa+fb+variation)/2


def coefficient_moments(c, j, m, logs):
    p = 2*j
    first_even = 2*(m//2+1)
    diagonal = (sum((ln-c)**p/n for n, ln in enumerate(logs, 1))
                + progression(len(logs)+1, m, 1, p, c, True)
                + 4*progression(first_even, 2*m, 2, p, c, True))
    gap_sum = (diagonal + progression(1, m, 1, p, c, False)
               + 2*progression(first_even, 2*m, 2, p, c, False))
    if m % 2:
        gap_sum += 2*(arb(first_even).log()-c)**p
    return diagonal, gap_sum


def disk_constants(t, ratio, d, rho):
    pi = arb.pi()
    lower_height = t-rho
    sigma_upper = arb(1)/2+rho
    c_positive = (ratio+(rho+sigma_upper**2/(2*lower_height))/t)/d
    c_negative_lower = lower_height/(d*t+1)
    assert lower_height > 0
    assert c_positive < 2*pi
    multiplier = ((2*pi/(1-rho/t)).log()+pi/lower_height
                  +sigma_upper**2/(2*lower_height**2))
    modes = (1/(2*pi-c_positive)+1/(2*pi+c_negative_lower)
             +(pi**2/6-1)*(1/(2*pi-c_positive/2)+1/(2*pi)))/pi
    euler = (d*t+1)/lower_height+arb(1)/2+c_positive*modes
    return euler, multiplier


def remainder(t, ratio, d, radii, weighted_length):
    euler, multiplier = disk_constants(t, ratio, d, radii[-1])
    out = []
    for j, a in enumerate(radii):
        value = (euler * (multiplier*a/2).exp() * d**(a-arb(1)/2)
                 * t**((a-1)/2) * weighted_length.sqrt())
        out.append(value * (factorial(j)/a**j if j else 1))
    return out


def phase(t, error, upper):
    return (t/(2*arb.pi())).log()/2 + (error if upper else -error)


def phase_error(t):
    return arb.pi()/(2*t)+1/(16*t**2)


def hardy_remainder(e):
    q0 = 1+arb(2).sqrt()
    q1 = arb(2).sqrt()*arb(2).log()
    q2 = q1*arb(2).log()
    return (q0*e[0], q0*e[1]+q1*e[0], q0*e[2]+2*q1*e[1]+q2*e[0])


def block(t_exact, u_exact, d_exact, radii, slices):
    t, u, d = map(ball, (t_exact, u_exact, d_exact))
    m = (d_exact*t_exact).__ceil__()
    c0, c1 = phase(t, phase_error(t), False), phase(u, phase_error(u), True)
    logs = [arb(n).log() for n in range(1, 33)]
    intervals = []
    for k in range(slices):
        a = t+(u-t)*k/slices
        b = t+(u-t)*(k+1)/slices
        intervals.append((a, b, phase(a, phase_error(a), False),
                          phase(b, phase_error(b), True)))
    endpoint_bounds = []
    squares = []
    for j in range(3):
        # D and J are convex functions of the real phase center.
        jl = coefficient_moments(c0, j, m, logs)[1]
        ju = coefficient_moments(c1, j, m, logs)[1]
        endpoint_bounds.append(jl.max(ju))
        jt = coefficient_moments(phase(t, phase_error(t), True), j, m, logs)[1]
        ju_low = coefficient_moments(phase(u, phase_error(u), False), j, m, logs)[1]
        correction = jl.max(jt)/t**2+ju_low.max(ju)/u**2
        diagonal = arb(0)
        for a, b, lo, hi in intervals:
            dl, gl = coefficient_moments(lo, j, m, logs)
            dh, gh = coefficient_moments(hi, j, m, logs)
            diagonal += (1/a-1/b)*dl.max(dh)
            correction += (1/a**2-1/b**2)*gl.max(gh)
        if j:
            correction += (2*j*(1/t-1/u)/t
                           * (endpoint_bounds[j]*endpoint_bounds[j-1]).sqrt())
        squares.append(diagonal+3*arb.pi()/2*correction)
    v = [x.sqrt() for x in squares]
    e = hardy_remainder(remainder(t, u/t, d, radii, 1/t-1/u))
    return v[0]+e[0], v[1]+e[1], v[2]+v[0]/t+e[2]


def residual(base, ratio, d, radii):
    h = base.log()
    radius = (1+3/h)/2
    length = 1-1/ratio
    coef = ((1+6/h)*length
            + 3*arb.pi()/h*((h+6)/base+1+8/base)).sqrt()
    v = [coef*radius**j for j in range(3)]
    beta = ratio.log()/4+phase_error(base)
    e = [val*base.sqrt()/h**(j+arb(1)/2)
         for j, val in enumerate(remainder(base, ratio, d, radii, length/base))]
    q0 = 1+arb(2).sqrt()
    q1 = arb(2).sqrt()*arb(2).log()/h
    q2 = q1*arb(2).log()/h
    g = [v[0]+q0*e[0],
         v[1]+beta/h*v[0]+q0*e[1]+q1*e[0],
         v[2]+2*beta/h*v[1]+(beta**2+1/base)/h**2*v[0]
         +q0*e[2]+2*q1*e[1]+q2*e[0]]
    squares = []
    for j, c in enumerate(g):
        power = 2*j+1
        growth = (1+ratio.log()/h)**power/ratio
        assert growth < 1
        squares.append(c**2*h**power/base/(1-growth))
    return squares


def evaluate(y, w, r, d, radii, blocks=28, slices=4):
    start = y-w
    t, ratio, d_arb = map(ball, (start, r, d))
    a = [ball(x) for x in radii]
    assert start >= 1000 and 0 < w <= (r-1)*start
    assert Fraction(5, 4) <= r <= 2 and 0 < d <= Fraction(1, 2)
    assert radii[0] == 0 and 0 < radii[1] <= radii[2] < Fraction(1, 2)
    assert d_arb**2*t > 1
    assert (d*start).__ceil__() >= 33
    assert arb(1)/t+arb.pi()/4 < 1
    assert 2*(d_arb+1/t)*(2*arb.pi()/ratio.sqrt()).sqrt() < (arb(3)/2).exp()
    assert ((d_arb * t).log()-(ratio.sqrt()*t/(2*arb.pi())).log()/2) > 0
    bounds = [arb(0)]*3
    for k in range(blocks):
        x = start*r**k
        vals = block(x, x*r, d, a, slices)
        bounds = [overall+v**2 for overall, v in zip(bounds, vals)]
    rem = residual(ball(start*r**blocks), ratio, d_arb, a)
    a0, a1, a2 = ((s+q).sqrt() for s, q in zip(bounds, rem))
    b0, b1, _ = block(start, y, d, a, slices)
    width = ball(w)
    zeta = acb_series([acb(arb(1)/2, arb(y)), acb(0, 1)], 2).zeta()
    dlog = arb(2).log()
    q_plus_one = arb(2).sqrt()*acb(0, -arb(y)*dlog).exp()
    q = q_plus_one-1
    dq = acb(0, -dlog)*q_plus_one
    value = q*zeta[0]/y
    derivative = (dq*zeta[0]+q*zeta[1]-value)/y
    boundary = 12*(abs(value)**2/width-(derivative*value.conjugate()).real)/width**2
    f1_squared = (a1+a0/t)**2+6*b0**2/width**2
    f2_squared = (a2+2*a1/t+2*a0/t**2)**2+24*(b1+b0/t)**2/width**2+boundary
    return 2*(f1_squared*f2_squared).sqrt()


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--height", type=int, default=10000)
    p.add_argument("--width", type=Fraction, default=Fraction(22))
    p.add_argument("--ratio", type=Fraction, default=Fraction(1607, 1000))
    p.add_argument("--truncation", type=Fraction, default=Fraction(143, 500))
    p.add_argument("--radius1", type=Fraction, default=Fraction(219, 1000))
    p.add_argument("--radius2", type=Fraction, default=Fraction(433, 1000))
    p.add_argument("--blocks", type=int, default=52)
    p.add_argument("--slices", type=int, default=8)
    p.add_argument("--precision", type=int, default=128)
    p.add_argument("--upper", type=str)
    args = p.parse_args()
    ctx.prec = args.precision
    assert args.blocks > 0 and args.slices > 0
    tail = evaluate(args.height, args.width, args.ratio, args.truncation,
                    [0, args.radius1, args.radius2], args.blocks, args.slices)
    if args.upper is not None:
        assert tail < arb(args.upper), tail
    print(tail)


if __name__ == "__main__":
    main()
