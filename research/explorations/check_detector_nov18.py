"""Verify the finite ball inequalities in detector-nov18.md with python-flint 0.9.0."""
from flint import acb, acb_series, arb, ctx


def main():
    ctx.prec = 128
    half = arb(1) / 2
    rho = acb.zeta_zero(1)
    assert rho.real == half and rho.imag > 0

    slope = acb_series([rho, 1], prec=2).zeta()[1]
    assert abs(slope) > 0
    ordinate = rho.imag
    s = acb(0, ordinate)
    power = (-rho * arb(2).log()).exp()
    residue = -3 * (power - 1) * (power - 2) / (s**2 * slope)

    degree = 127
    for k in range(3, degree + 1, 2):
        harmonic = acb(half, k * ordinate)
        assert abs(harmonic.zeta()) > 0, k

    mass_bound = 2 * abs(residue) * degree / (arb.pi() * (degree + 1))
    assert mass_bound > arb(536) / 10000
    print(f"rho = {rho}")
    print(f"residue = {residue}")
    print(f"certified mass constant = {mass_bound}")


if __name__ == "__main__":
    main()
