"""Interval replay for the prime-ideal oscillation in Q(sqrt(-163))."""
from flint import acb, arb, ctx, dirichlet_char


def main():
    ctx.prec = 128
    modulus = 163
    chi = dirichlet_char(modulus, modulus - 1)
    assert chi.is_primitive() and chi.order() == 2 and chi.parity() == 1

    partial = 0
    max_abs = 0
    for n in range(1, modulus + 1):
        residue = pow(n, (modulus - 1) // 2, modulus)
        partial += int(residue == 1) - int(residue == modulus - 1)
        max_abs = max(max_abs, abs(partial))
    assert partial == 0 and max_abs == 9
    derivative_bound = 4 * max_abs
    grid = 512
    for j in range(grid // 2, grid + 1):
        value = acb(arb(j) / grid).dirichlet_l(chi)
        assert value.real > arb(67) / 1000 > arb(derivative_bound) / (2 * grid)
    print("L(s,chi) positive on [1/2,1]")

    lower, upper = arb(1) / 5, arb(21) / 100
    assert chi.hardy_z(lower).real > 0 and chi.hardy_z(upper).real < 0
    for _ in range(75):
        middle = (lower + upper) / 2
        value = chi.hardy_z(middle).real
        if value > 0:
            lower = middle
        elif value < 0:
            upper = middle
        else:
            raise ArithmeticError("Hardy sign not resolved")
    gamma = lower.union(upper)
    print("Positive zero ordinate in", gamma)

    order = 128
    for k in range(2, order + 1):
        s = acb(arb(1) / 2, k * gamma)
        assert not s.zeta().contains(0)
        assert not s.dirichlet_l(chi).contains(0)
    shift = (arb(2) * order / (order + 1)) / (arb(1) / 4 + gamma**2)
    print("Upper bound for liminf in", 2 - shift)
    print("Lower bound for limsup in", 2 + shift)


if __name__ == "__main__":
    main()
