"""Directed certificate for the factor 57/50 in nov18b-goldbach-parity.md."""

from flint import acb, arb, ctx


def main():
    ctx.prec = 96
    ordinates = [root.imag for root in acb.zeta_zeros(1, 160)]
    split = ordinates[-1]
    assert ordinates[0] > 14
    assert all(a < b for a, b in zip(ordinates, ordinates[1:]))
    lengths = [arb(13 * p) / 10000 for p in (51, 34, 15)]
    assert sum(lengths) + arb(1) / 4000 < (arb(57) / 50).log()

    reciprocal_bound = (1 + arb(1) / 784) * (
        2 + arb.const_euler() - (4 * arb.pi()).log()
    ) / 2
    low_mass = sum(g ** -2 for g in ordinates)
    tail_mass = reciprocal_bound - low_mass
    assert tail_mass > 0
    gamma_constant = (2 * arb.pi()).sqrt()
    low_pairs = arb(0)
    for i, a in enumerate(ordinates):
        for j in range(i + 1):
            frequency = a + ordinates[j]
            weight = arb(1)
            for length in lengths:
                weight *= abs((length * frequency / 2).sinc())
            multiplicity = 2 if i == j else 4
            low_pairs += multiplicity * gamma_constant * weight / (
                frequency * frequency.sqrt()
            )

    mixed_weights = arb(0)
    for g in ordinates:
        r = g / split
        mixed_weights += (16 * r**2 / (1 + r)**4) / g**2
    amplitude = 8 / (lengths[0] * lengths[1] * lengths[2])
    tail_pairs = (2 * gamma_constant * amplitude / (16 * split.sqrt())) * (
        tail_mass**2 + 2 * tail_mass * mixed_weights
    )
    # With the new three widths the opposite-sign cost still stays below 1e-10.
    opposite = arb(1) / 10**10
    m = arb(14)
    assert 8 * arb.pi() * m**4 * (-arb.pi() * m).exp() < opposite
    assert 12 * amplitude * (-arb.pi() * m).exp() / m.sqrt() < opposite
    assert 2 * reciprocal_bound**2 < 1
    bound = low_pairs + tail_pairs + opposite
    assert bound < arb(496) / 1000
    print("finite pairs", low_pairs)
    print("remaining equal-sign pairs", tail_pairs)
    print("all signs", bound)


if __name__ == "__main__":
    main()
