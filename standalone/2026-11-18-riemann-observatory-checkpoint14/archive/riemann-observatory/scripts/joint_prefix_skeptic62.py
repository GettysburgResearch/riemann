"""Positive-coefficient numerical checks for the two finite-prefix regimes."""

from mpmath import mp


def scaled_cost(m, s):
    """Evaluate c_m/m^2 at s=b/(1-b) via the integrated Taylor square."""
    coefficient = mp.mpf(m * (m - 1))
    terms = [coefficient]
    for j in range(1, m - 1):
        terms.append(terms[-1] * ((m - 1 - j) * (m + j)) * s / (j * (j + 1)))
    integral = s * mp.fsum(
        left * right / (i + j + 1)
        for i, left in enumerate(terms)
        for j, right in enumerate(terms)
    )
    return 1 + integral / (m * m)


def bessel_limit(r):
    z = 2 * mp.sqrt(r)
    return mp.besseli(0, z) ** 2 - mp.besseli(1, z) ** 2


def legendre_asymptotic(m, s):
    eta = 2 * mp.asinh(mp.sqrt(s))
    return mp.exp((2 * m - 1) * eta) / (8 * mp.pi * s * (1 + s) * m * m)


def main():
    mp.dps = 55
    print("m | m times relative error at r=10 | Legendre ratios at b=1/m, fixed b=1/2, b=1-2^-m | Bessel ratio at r=m^(4/3)")
    for m in (16, 64, 256, 512):
        r = mp.mpf(10)
        relative_error = m * (scaled_cost(m, r / m**2) / bessel_limit(r) - 1)
        odds = (1 / mp.mpf(m - 1), mp.mpf(1), mp.mpf(2) ** m - 1)
        ratios = [scaled_cost(m, s) / legendre_asymptotic(m, s) for s in odds]
        critical_r = mp.mpf(m) ** (mp.mpf(4) / 3)
        critical_ratio = scaled_cost(m, critical_r / m**2) / bessel_limit(critical_r)
        print(m, *(mp.nstr(value, 11) for value in (relative_error, *ratios, critical_ratio)))
    print("Critical limiting ratio:", mp.nstr(mp.exp(-mp.mpf(2) / 3), 11))


if __name__ == "__main__":
    main()
