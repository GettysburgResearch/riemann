"""Certified finite frequency data for the dyadic variance bound (python-flint 0.9)."""

from flint import acb, arb, ctx


def main():
    ctx.prec = 128
    log_two = arb(2).log()
    period = 2 * arb.pi() / log_two
    ordinates = [arb(0)]
    for index in range(1, 65):
        zero = acb.zeta_zero(index)
        assert zero.real == arb(1) / 2
        ordinates.append(zero.imag)
        ordinates.append(-zero.imag)

    rotations = [(acb(0, t * log_two)).exp() for t in ordinates]
    for i, rotation in enumerate(rotations):
        assert all(abs(rotation - earlier) > 0 for earlier in rotations[:i])

    lower_square = arb(0)
    for i, t in enumerate(ordinates):
        z = acb(arb(1) / 2, t)
        # Translate into the interval below the first nontrivial ordinate.
        shift = int(round(float(t.mid() / period.mid()))) or 1
        delta = shift * period
        w = z - acb(0, delta)
        assert abs(w.imag) < 14 and abs(w.imag) > 0
        cross = z * w.conjugate() / acb(1, delta)
        norm_square = (abs(z)**2 + abs(w)**2) / 2 - cross.real
        assert norm_square > 0
        residue = arb(1) / 2 if i == 0 else arb(1)
        lower_square += (residue * log_two)**2 / norm_square

    print(lower_square.sqrt())
    assert lower_square.sqrt() > arb("0.1969")


if __name__ == "__main__":
    main()
