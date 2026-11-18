"""Bound the first 600 ordinate responses and the full RH tail using Arb."""
from fractions import Fraction
from flint import acb, arb, ctx


def main():
    ctx.prec = 128
    halfwidth = arb(2).log() / 2
    # (1-v^2)^3 (2+3v^2+11v^4) on [-1,1]
    coefficients = [0] * 11
    for i, b in enumerate((1, -3, 3, -1)):
        for j, c in enumerate((2, 3, 11)):
            coefficients[2 * (i + j)] += b * c
    mass = sum(2 * halfwidth * c / (j+1) for j, c in enumerate(coefficients))
    poly = coefficients.copy()
    endpoints = []
    while poly:
        endpoints.append(sum(poly))
        poly = [i * c for i, c in enumerate(poly) if i]
    loss = arb(0)
    for n in range(1, 601):
        rho = acb.zeta_zero(n)
        assert rho.real == arb(1)/2
        frequency = acb(0, rho.imag * halfwidth)
        phase = frequency.exp()
        inverse = 1 / frequency
        power = inverse
        integral = acb(0)
        for j, endpoint in enumerate(endpoints):
            integral += power * endpoint * (phase - (-1)**j * phase.conjugate())
            power *= -inverse
        loss += 2 * halfwidth * abs(integral)
    cutoff = rho.imag.lower()
    # Bound |K(t)| <= C/t^4 beyond the cutoff, by the same finite endpoint sum.
    tail_constant = sum(2 * abs(c) / (halfwidth**j * cutoff**(j-3))
                        for j, c in enumerate(endpoints) if j >= 3)
    # Under RH, sum over signed ordinates (1/4+gamma^2)^-1 < 0.05.
    tail = tail_constant * arb("0.05") * (1 + 1/(4*cutoff**2)) / cutoff**2

    # Exact polynomial integrals majorize the norm of e^(-u/2)(k'-k/2).
    def squared_integral(coefs):
        return sum((Fraction(2*c*d, i+j+1)
                    for i,c in enumerate(coefs) for j,d in enumerate(coefs)
                    if (i+j)%2 == 0), Fraction(0))
    norm0 = squared_integral(coefficients)
    norm1 = squared_integral([i*c for i,c in enumerate(coefficients) if i])
    def ball(value):
        return arb(value.numerator)/value.denominator
    norm_bound = (ball(norm1)/halfwidth).sqrt() + (ball(norm0)*halfwidth).sqrt()/2
    lower = (mass/2-loss-tail)/norm_bound
    print("mass",mass,"finite loss",loss,"tail bound",tail,"lower bound",lower)
    assert lower > arb("0.0128")


if __name__ == "__main__":
    main()
