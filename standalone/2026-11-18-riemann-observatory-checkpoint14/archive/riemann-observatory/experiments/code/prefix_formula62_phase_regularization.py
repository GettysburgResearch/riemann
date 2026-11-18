"""Exact symbolic checks for the uncentered and centered phase curves."""
import sympy as sy


def main():
    tau, v, z = sy.symbols('tau v z', positive=True)
    alpha = 1 + tau / 4
    i1 = sy.integrate(1 / (1 + v**2), (v, -sy.oo, sy.oo))
    i2 = sy.integrate(1 / (1 + v**2)**2, (v, -sy.oo, sy.oo))
    assert (i1, i2) == (sy.pi, sy.pi / 2)
    cost = 1 / (4 * sy.sqrt(tau) * alpha**sy.Rational(3, 2))
    error = sy.sqrt(tau) * (1 + tau / 2) / (4 * alpha**sy.Rational(3, 2))
    assert sy.simplify(error - tau * (1 / (2 * sy.sqrt(tau * alpha)) - cost)) == 0

    # Parametrize z by a positive variable so every radical has a fixed sign.
    y = sy.symbols('y', positive=True)
    z_uncentered = y / sy.sqrt(1 + y**2)
    assert sy.simplify(error.subs(tau, 4 * y**2) - (z_uncentered + z_uncentered**3) / 2) == 0
    assert sy.simplify(cost.subs(tau, 4 * y**2) - (1 - z_uncentered**2)**2 / (8 * z_uncentered)) == 0

    i = 1 / (1 + sy.sqrt(tau) / 2)
    centered_cost = -sy.diff(i, tau)
    centered_error = 1 - i + tau * sy.diff(i, tau)
    z_centered = y / (1 + y)
    assert sy.simplify(centered_cost.subs(tau, 4*y**2) - (1-z_centered)**3/(8*z_centered)) == 0
    assert sy.simplify(centered_error.subs(tau, 4*y**2) - z_centered*(1+z_centered)/2) == 0
    assert sy.limit(error * cost, tau, 0, dir='+') == sy.Rational(1, 16)
    assert sy.limit(centered_error * centered_cost, tau, 0, dir='+') == sy.Rational(1, 16)
    print('SymPy', sy.__version__)
    print('Uncentered: error squared = (z+z^3)/2; cost squared = (1-z^2)^2/(8z)')
    print('Centered: error squared = z(1+z)/2; cost squared = (1-z)^3/(8z)')
    print('Both squared error-cost products tend to 1/16')


if __name__ == '__main__':
    main()
