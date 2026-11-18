"""Certified one- and two-jet lower bounds for the chi4 distance using python-flint 0.9.0."""

from math import factorial

from flint import acb, arb, ctx


def completed_beta(t):
    s = acb(arb(1) / 2, t)
    beta = 4**(-s) * (s.zeta(arb(1) / 4) - s.zeta(arb(3) / 4))
    return (4 / arb.pi()) ** ((s + 1) / 2) * ((s + 1) / 2).gamma() * beta


def lower_bounds(n, rho, terms=12):
    a = arb.pi() / 2
    cutoff = 1 / arb(n)
    phase = ((4 / arb.pi()) ** (rho - arb(1) / 2)
             * ((rho + 1) / 2).gamma() / ((2 - rho) / 2).gamma()
             * rho / (1 - rho))
    log_derivative = ((4 / arb.pi()).log() + ((rho + 1) / 2).digamma().real
                      + 2 * (1 / rho).real)
    powers = [2 * j - 1 for j in range(1, terms + 1)]
    smooth = [(-1) ** (j + 1) * a ** (2 * j - 1) / factorial(2 * j)
              for j in range(1, terms + 1)]
    remainder = [d * p / (rho + p) for p, d in zip(powers, smooth)]
    cross_gram = sum(
        2 * (phase * c.conjugate() * cutoff ** (p + 1 - rho) / (p + 1 - rho)).real
        for p, c in zip(powers, remainder)
    )
    cross_target = sum(
        d * phase.conjugate() * cutoff ** (p + 1 - rho.conjugate()) / (p + 1 - rho.conjugate())
        for p, d in zip(powers, smooth)
    )
    quadratic_gram = sum(
        (c * e.conjugate()).real * cutoff ** (p + q + 1) / (p + q + 1)
        for p, c in zip(powers, remainder)
        for q, e in zip(powers, remainder)
    )
    quadratic_target = sum(
        d * e.conjugate() * cutoff ** (p + q + 1) / (p + q + 1)
        for p, d in zip(powers, smooth)
        for q, e in zip(powers, remainder)
    )
    cross_off_diagonal = sum(
        2 * phase * c * cutoff ** (p + 1 - rho) / (p + 1 - rho)
        for p, c in zip(powers, remainder)
    )
    quadratic_off_diagonal = sum(
        c * e * cutoff ** (p + q + 1) / (p + q + 1)
        for p, c in zip(powers, remainder)
        for q, e in zip(powers, remainder)
    )
    exponent = 1 - 2 * rho
    off_diagonal = ((1 - phase**2 * cutoff**exponent) / exponent
                    - cross_off_diagonal - quadratic_off_diagonal)
    gram = arb(n).log() + log_derivative - cross_gram - quadratic_gram
    target = 1 / rho - cross_target - quadratic_target

    geometric_ratio = a * a / ((2 * terms + 3) * (2 * terms + 4))
    assert geometric_ratio < 1
    tail = a ** (2 * terms + 1) / factorial(2 * terms + 2) / (1 - geometric_ratio)
    bound = (a.cosh() - 1) / a
    linear_error = tail * cutoff ** (2 * terms + arb(3) / 2) / (2 * terms + arb(3) / 2)
    quadratic_error = 2 * bound * tail * cutoff ** (2 * terms + 3) / (2 * terms + 3)
    gram_error = 2 * linear_error + quadratic_error
    target_error = linear_error + quadratic_error
    gram += arb(0, gram_error)
    off_diagonal += acb(arb(0, gram_error), arb(0, gram_error))
    target += acb(arb(0, target_error), arb(0, target_error))
    determinant = gram**2 - abs(off_diagonal)**2
    assert gram > 0 and determinant > 0
    one = abs(target)**2 / gram
    two = 2 * (gram * abs(target)**2 - (off_diagonal * target**2).real) / determinant
    return one, two


def main():
    ctx.prec = 192
    lo = arb("6.02094890469")
    hi = arb("6.02094890471")
    left = completed_beta(lo)
    right = completed_beta(hi)
    assert left.real > 0 and right.real < 0
    rho = acb(arb(1) / 2, lo.union(hi))
    print("Completed beta endpoint enclosures:", left.real, right.real)
    print("Certified sign-changing ordinate bracket:", lo, hi)
    for n, claimed in ((10, "0.01463"), (100, "0.00903"), (1000, "0.00665"),
                       (1000000, "0.00362")):
        one, two = lower_bounds(n, rho)
        assert two > arb(claimed), (n, two, claimed)
        assert two > one, (n, one, two)
        print(n, "one-jet:", one, "two-jet:", two)


if __name__ == "__main__":
    main()
