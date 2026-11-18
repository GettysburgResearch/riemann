"""Directed endpoint checks for the smoothed finite Robin estimate."""
from flint import arb, ctx


def main():
    ctx.prec = 180
    one = arb(1)
    two = arb(2)
    pi = arb.pi()
    height = arb(3) * 10**12
    sigma = 8 / height
    width = 16 * sigma
    theta_limit = two * 10**25
    first = arb(10)**21
    split = arb(10)**40
    last = arb(3) * 10**46
    minimum = first * (-width).exp()
    maximum = last * width.exp()
    eta = arb("0.0002")
    stop = 75

    # Every theta argument in the local costs and square-prime estimate.
    assert arb("4.92") * (theta_limit / theta_limit.log()).sqrt() < height
    v = minimum.sqrt()
    assert v > 599
    theta_relative = v.log()**2 / (8 * pi * v.sqrt())
    assert theta_relative < eta
    assert stop * (2 * maximum).sqrt() < theta_limit
    assert stop * (2 * minimum).sqrt() < minimum / 2
    rest = 2 * minimum**(-one/6) + 2 * minimum.log() / (two.log() * minimum**(one/4))
    assert one + eta + rest < arb("1.002")
    assert two + rest < arb("2.002")

    # Conditional truncated Gaussian transform, for Re(s) in [-2,0].
    transform = ((2*sigma**2-32).exp() + two.sqrt()*(4*sigma**2-64).exp()) / (one-2*arb(-128).exp())
    assert transform < arb("1.27e-14")

    for lower, upper in ((first, split), (split, last)):
        log_min = lower.log()
        reduced = log_min - width
        ratio = log_min / reduced
        extra = one + one/reduced

        low_zeros = arb("0.047") * (width/2).exp() * ratio * extra
        high_zeros = arb("3.1e-12") * (
            upper.sqrt() * transform * (one+one/log_min)
            + (2*width).exp() * ratio * (2+one/reduced) / lower.sqrt()
        )
        archimedean = (2*pi).log() * width.exp() * ratio / lower.sqrt()
        prime_powers = 2 * ratio * extra * (
            arb("1.002")*(width/2).exp() + upper.sqrt()/theta_limit
        )
        curvature = upper.sqrt()*sigma**2*width.exp()*ratio*extra/2
        paid = low_zeros + high_zeros + archimedean + prime_powers + curvature

        log_q = (reduced + two.log())/2
        cost = (-width/2).exp() * log_min/(log_min+width) * two.sqrt() / (one+two.log()/reduced)
        cost *= (one-eta) + (one-eta)*(one-one/log_q-one/stop) - 2*eta
        assert paid < cost
        print("log(n) range", lower, upper)
        print("upper error and lower cost", paid, cost)


def density_extension():
    from check_robin_density_nov18 import high_zero_bound, upper_masses

    one = arb(1)
    two = arb(2)
    height = arb(3) * 10**12
    lower = arb(3) * 10**46
    upper = arb(27) * 10**46
    sigma = arb(24).sqrt()/height
    width = 16*sigma
    v_min = lower*(-width).exp()
    arg_min = v_min.sqrt()
    eta = arb("1e-9")
    assert arb(55).exp() < arb(2)*10**25
    assert arg_min.log()**2/(8*arb.pi()*arg_min.sqrt()) < eta
    extra_powers = 2*v_min**(-one/6)+2*v_min.log()/(two.log()*v_min**(one/4))
    assert eta + extra_powers < arb("2e-7")
    assert 10**5*(2*v_min).sqrt() < v_min/2

    moment = high_zero_bound(upper.log(), upper_masses())
    assert moment < 8702
    log_min = lower.log()
    reduced = log_min-width
    ratio = log_min/reduced
    extra = one+one/reduced
    transform = ((2*sigma**2-12).exp()+two.sqrt()*(4*sigma**2-64).exp())/(one-2*arb(-128).exp())
    high = 8702*transform*(one+one/log_min)
    high += arb("3.1e-12")*(2*width).exp()*ratio*(2+one/reduced)/lower.sqrt()
    low = arb("0.047")*(width/2).exp()*ratio*extra
    arch = (2*arb.pi()).log()*width.exp()*ratio/lower.sqrt()
    curvature = upper.sqrt()*sigma**2*width.exp()*ratio*extra/2
    powers = (one+arb("2e-7"))*(width/2).exp()*ratio*(2-2/(upper.log()+width)+8/reduced**2)
    paid = high+low+arch+curvature+powers
    cost = (-width/2).exp()*log_min/(log_min+width)*(2/(one+two.log()/reduced)).sqrt()
    cost *= (one-eta)+(one-eta)*(one-2/reduced-arb("1e-5"))-2*eta
    assert paid < arb("2.784") and cost > arb("2.792")
    print("Density-assisted upper error and lower cost", paid, cost)


if __name__ == "__main__":
    import sys

    main()
    if "--density" in sys.argv[1:]:
        density_extension()
