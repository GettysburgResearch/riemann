"""Check constants for the pointwise free-tangent Robin range."""

from flint import arb, ctx


def main():
    ctx.prec = 160
    lower = arb(9) * 10**21
    upper = arb(10) ** 38
    interface_limit = arb(10) ** 40
    prime_power_limit = arb(10) ** 48
    height = arb(3) * 10**12
    eta = arb("0.0001")
    two = arb(2)
    pi = arb.pi()
    log_lower = lower.log()

    def max_theta_relative(v):
        return v.log() ** 2 / (8 * pi * v.sqrt())

    q = (2 * lower).sqrt()
    max_needed = 100 * (2 * interface_limit).sqrt()
    assert 100 * q < lower / 2
    assert prime_power_limit.sqrt() > max_needed
    max_needed = prime_power_limit.sqrt()
    assert arb("4.92") * (max_needed / max_needed.log()).sqrt() < height
    assert max_theta_relative(lower.sqrt()) < eta
    assert lower.sqrt() > 599

    prime_powers = 1 + eta + 2 * lower ** (-arb(1) / 6)
    prime_powers += 2 * log_lower / (two.log() * lower ** (arb(1) / 4))
    assert prime_powers < arb("1.002")

    gain = (1 - eta) + (1 - eta) * (1 - 1 / q.log()) - 2 * eta - arb(1) / 100
    cost = two.sqrt() * gain / (1 + two.log() / log_lower)
    assert cost > arb("2.72")

    def nicolas_bound(endpoint, high_zero_moment):
        power_cost = 2 * (arb("1.002") + 3 * (endpoint / prime_power_limit).sqrt())
        return (1 + 1 / log_lower) * (
            arb("0.047") + high_zero_moment + (2 * pi).log() / lower.sqrt() + power_cost
        )

    assert nicolas_bound(interface_limit, arb("0.60")) < cost
    paid = nicolas_bound(upper, arb("0.554"))
    assert paid < cost
    print("Upper scaled prime discrepancy", paid)
    print("Lower scaled exponent cost", cost)


if __name__ == "__main__":
    main()
