"""Verify finite predicates for detector-diffusion-nov18.md using python-flint 0.9.0."""
from flint import acb, acb_series, arb, ctx


def mobius_table(limit):
    values = [1] * (limit + 1)
    marked = bytearray(limit + 1)
    for p in range(2, limit + 1):
        if marked[p]:
            continue
        for n in range(p, limit + 1, p):
            marked[n] = 1
            values[n] *= -1
        for n in range(p * p, limit + 1, p * p):
            values[n] = 0
    return values


def verify_arithmetic_prefix():
    last = 3000
    assert arb(last).log() > 8
    mu = mobius_table(last)
    value = arb(0)
    slope = arb(0)
    for n in range(1, last):
        q = 6 * (n == 1) - 6 * mu[n]
        if n % 2 == 0:
            q += 9 * mu[n // 2]
        if n % 4 == 0:
            q -= 3 * mu[n // 4]
        slope += q / arb(n).sqrt()
        value += slope * (arb(n + 1) / n).log()
        if n == 1:
            assert value == 0
        else:
            assert value > 0
    assert arb(2).log() < arb(7) / 10
    assert arb(3).log() > arb(21) / 20
    assert arb(15) / arb(2).sqrt() > 10


def main():
    ctx.prec = 96
    verify_arithmetic_prefix()
    half = arb(1) / 2
    log_two = arb(2).log()

    def numerator(z):
        dyadic = (-z * log_two).exp()
        return -3 * (dyadic - 1) * (dyadic - 2)

    z = acb_series([half, 1], prec=2)
    coefficients = 6 + numerator(z) / z.zeta()
    assert coefficients[0].real > 6 and coefficients[1].real > -1

    height = 2000
    residue_loss = arb(0)
    count = 0
    zeros = acb.zeta_zeros(1, 1600)
    assert zeros[-1].imag > height
    for rho in zeros:
        if rho.imag > height:
            break
        assert rho.imag < height and rho.real == half
        derivative = acb_series([rho, 1], prec=2).zeta()[1]
        assert abs(derivative) > 0
        residue = numerator(rho) / ((rho - half)**2 * derivative)
        residue_loss += 2 * abs(residue)
        count += 1
    assert count == 1517 and residue_loss < arb(37) / 100

    pieces = 256
    for j in range(pieces):
        left = -1 + arb(2) * j / pieces
        right = -1 + arb(2) * (j + 1) / pieces
        s = acb(left.union(right), height)
        z = s + half
        value = (6 + numerator(z) / z.zeta()) / s**2
        assert abs(value) < 1

    print(f"Positive prefix through n=3000, {count} enclosed positive ordinates below {height}")
    print(f"A = {coefficients[0]}, B = {coefficients[1]}")
    print(f"Total signed-ordinate residue bound = {residue_loss}")
    print(f"All {pieces} horizontal contour boxes satisfy |F| < 1")


if __name__ == "__main__":
    main()
