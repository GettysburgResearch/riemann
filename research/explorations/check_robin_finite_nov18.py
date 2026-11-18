"""Check monotone endpoint constants in the finite Robin proof with Arb balls."""

from flint import arb, ctx


def main():
    ctx.prec = 160
    x0 = arb(10) ** 13
    upper = arb(10) ** 22
    power_split = arb(10) ** 40
    height = arb(3) * 10**12
    two = arb(2)
    pi = arb.pi()
    log0 = x0.log()
    log2 = two.log()
    y0 = (2 * x0).sqrt()
    eta = arb("0.005")

    def relative_theta_error(v):
        return v.log() ** 2 / (8 * pi * v.sqrt())

    assert arb("4.92") * (upper / upper.log()).sqrt() < height
    assert relative_theta_error(x0) < arb("0.00002")
    assert relative_theta_error(x0.sqrt()) < arb("0.006")
    assert relative_theta_error(y0) < eta
    assert relative_theta_error(upper) < arb("0.01")
    assert 2 + arb.const_euler() - (4 * pi).log() < arb("0.047")

    tail = ((height / (2 * pi)).log() + 1) / (pi * height)
    tail += arb("0.56") * (2 * height.log() + arb("0.5")) / height**2
    assert tail < arb("3.1e-12")

    power_rest = 2 * x0 ** (-arb(1) / 6) + 2 * log0 / (log2 * x0 ** (arb(1) / 4))
    assert arb("1.006") + power_rest < arb("1.069")
    assert 2 + power_rest < 3

    zero_bound = (1 + 1 / log0) * (
        arb("0.047") + arb("3.1e-12") * upper.sqrt() + (2 * pi).log() / x0.sqrt()
    )
    prime_power_bound = 2 * (1 + 1 / log0) * (
        arb("1.069") + 3 * (upper / power_split).sqrt()
    )
    quadratic = log0**4 / (64 * pi**2 * x0.sqrt())
    nicolas = zero_bound + prime_power_bound + quadratic
    assert nicolas < arb("2.59")

    t_rel = arb("1.00002") + 3 / x0.sqrt()
    slope_ratio = 1 / (t_rel * (1 + t_rel.log() / log0))
    assert slope_ratio > arb("0.999")
    assert arb("0.97") * arb("0.999") * (1 + log2 / log0) * (1 + 1 / y0 + 1 / y0**2) < 1
    assert 1 / (1 + 1 / y0 + 1 / y0**2) > arb("0.999")

    first = arb("0.97") * arb("0.999") * (1 - eta) * two.sqrt()
    second = arb("0.999") * two.sqrt() / (1 + log2 / log0)
    second *= (1 - eta) * (1 - 1 / y0.log()) - 2 * eta
    exponent_cost = first + second - 1 / x0.sqrt()
    assert exponent_cost > arb("2.63")
    assert arb("2.997") > arb("2.63")

    assert arb(10).log() * arb(10) ** arb("13.11485") > 2 * x0
    small_mertens = (arb("1.00002") * x0).log() * (arb("2.59") / (x0.sqrt() * log0)).exp()
    assert small_mertens < (2 * x0).log()

    print("Signed reciprocal-square high-zero tail upper bound", tail)
    print("Scaled Nicolas upper bound", nicolas)
    print("Scaled exponent cost lower bound", exponent_cost)


if __name__ == "__main__":
    main()
