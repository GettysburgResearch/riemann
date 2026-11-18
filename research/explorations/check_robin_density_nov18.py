"""Upper bounds for the signed-ordinate high-zero *absolute* moment.

For H=3e12 and every 1 <= x <= U, bound
    sum_{rho: |Im rho|>H} x**max(Re rho-1/2, 0)/Im(rho)**2.
Imported density bounds are Chourasiya--Simonic, arXiv:2507.15184,
Corollary 1 Table 1 and equation (119) Table 4 (multiplicities included).
Constants are the stated decimal upper coefficients, here encoded as Arb balls.
The starting full inverse-square tail is the certified 3.1e-12 bound in the
companion finite Robin note. No zero list or density table was recomputed.
"""

from flint import arb, ctx

# Table 1 rows are consecutive intervals of width 1/32 starting at 1/2.
INGHAM = (
    ("5.069", "9.461", "167.8"),
    ("6.046", "9.168", "162.6"),
    ("7.077", "8.875", "157.4"),
    ("8.185", "8.582", "152.2"),
    ("9.387", "8.290", "147.0"),
    ("10.70", "7.997", "141.9"),
    ("12.11", "7.704", "136.7"),
    ("13.66", "7.411", "131.5"),
    ("15.35", "7.118", "126.3"),
    ("17.21", "6.826", "121.1"),
    ("19.31", "6.533", "115.9"),
    ("21.77", "6.240", "110.7"),
    ("24.83", "5.745", "101.9"),
    ("29.01", "5.463", "96.87"),
    ("35.35", "5.180", "91.86"),
    ("46.06", "4.897", "86.84"),
)

# Table 4. Left endpoints are exact integer multiples of 1/6400.
KADIRI = (
    (4000, "2.900", "5.027"),
    (4200, "3.474", "4.789"),
    (4400, "4.149", "4.536"),
    (4600, "4.940", "4.296"),
    (4800, "5.860", "4.042"),
    (5000, "6.925", "3.800"),
    (5200, "8.148", "3.546"),
    (5400, "9.543", "3.301"),
    (5600, "11.12", "3.055"),
    (5800, "12.88", "2.807"),
    (6000, "14.81", "2.558"),
    (6200, "15.21", "2.301"),
    (6240, "15.62", "2.249"),
    (6280, "16.04", "2.204"),
    (6320, "16.46", "2.153"),
    (6360, "16.89", "2.101"),
)


def upper_masses():
    """Upper weights 1/gamma^2 for Re(rho)>i/6400, both ordinate signs."""
    height = arb(3) * 10**12
    log_h = height.log()
    full_mass = arb("3.1e-12")

    def integrated_term(coefficient, power, log_power):
        # Two signs and Stieltjes partial summation contribute a factor four.
        # For t>=H, (log t/log H)^k <= (t/H)^(k/log H).
        gap = 2 - power - log_power / log_h
        assert gap > 0
        return 4 * coefficient * height ** (power - 2) * log_h**log_power / gap

    masses = []
    density_row = 0
    for i in range(3200, 6400):
        sigma = arb(i) / 6400
        a, b, c = map(arb, INGHAM[(i - 3200) // 200])
        power = 3 * (1 - sigma) / (2 - sigma)
        log_power = (7 - 5 * sigma) / (2 - sigma)
        ingham = integrated_term(a, power, log_power)
        ingham += integrated_term(b, arb(0), arb(2))
        ingham += integrated_term(c, arb(0), arb(1))

        # beta>sigma>=1/2: reflection rho -> 1-conj(rho) accounts for a
        # disjoint equal-weight companion on the other side of the line.
        bound = min(full_mass / 2, ingham)
        if i >= KADIRI[0][0]:
            while density_row + 1 < len(KADIRI) and KADIRI[density_row + 1][0] <= i:
                density_row += 1
            _, a, b = KADIRI[density_row]
            kadiri = integrated_term(arb(a), 8 * (1 - sigma) / 3, 2 * (3 - 2 * sigma))
            kadiri += integrated_term(arb(b), arb(0), arb(2))
            bound = min(bound, kadiri)
        masses.append(bound)
    return masses


def high_zero_bound(log_upper, masses):
    """Bound the full high-zero moment for 1<=x<=exp(log_upper)."""
    assert log_upper >= 0 and len(masses) == 3200
    total = arb("3.1e-12")
    step = (log_upper / 6400).exp()
    weight = step - 1
    for mass in masses:
        # Integrate d(U^(sigma-1/2)) exactly on this cell using the upper
        # bound for the decreasing projected zero mass at its left end.
        total += weight * mass
        weight *= step
    return total


def main():
    ctx.prec = 160
    masses = upper_masses()
    log_ten = arb(10).log()
    for exponent, limit in [(34, "0.0143"), (35, "0.0346"), (36, "0.0854"),
                            (37, "0.216"), (38, "0.554"), (47, "5500"), (48, "2e4"), (49, "5e4")]:
        bound = high_zero_bound(exponent * log_ten, masses)
        assert bound < arb(limit)
        print(f"U=10^{exponent}: full high-zero moment <= {bound}")


if __name__ == "__main__":
    main()
