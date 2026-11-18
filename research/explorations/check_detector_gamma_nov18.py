"""Certify the small real-rate blocks for the gamma-sampled 5:3 detector."""
from flint import acb, acb_series, arb, ctx


def main():
    ctx.prec = 160
    log_two = arb(2).log()
    half = arb(1) / 2

    def numerator(z):
        y = (-z * log_two).exp()
        return -3 * (y-1) * (y-2)

    ctx.cap = 2
    w = acb_series([half, 1], prec=2)
    affine = 6 + numerator(w) / w.zeta()
    a, b = affine[0].real, affine[1].real
    assert 6 < a < 10 and -1 < b < 1
    assert abs(acb(half).zeta()) > 1
    assert (half*(half-1)*arb.pi()**(-half/2)*(half/2).gamma()*acb(half).zeta()/2).real > arb('.4')

    # The Taylor coefficient has derivative order k-1. Set the global cap too.
    for rate in range(2, 8):
        first, last = 2**(rate-2), 2**(rate-1)-1
        ctx.cap = last
        s = acb_series([rate, 1], prec=last)
        f = (6+numerator(s+half)/(s+half).zeta())/(s*s)
        for k in range(first, last+1):
            m = f[k-1].real * ((-1)**(k-1) * rate**k)
            assert m > 0, (rate, k, m)
    print('Certified individual derivatives k=1 through 63.')

    accepted = 0
    for rate in range(8, 50):
        first = 2**(rate-2)
        radius = min(arb(rate+2), arb(rate**2+100).sqrt())
        max_allowed = (a*first/rate+b-1) / (rate * (arb(rate)/radius)**(first-1))
        count = 128
        pieces = [(arb(j)/count, arb(j+1)/count) for j in range(count)]
        while pieces:
            lo, hi = pieces.pop()
            arg = 2 * arb.pi() * lo.union(hi)
            s = rate + radius*acb(arg.cos(), arg.sin())
            z = s + half
            centered = (6+numerator(z)/z.zeta()-a-b*s)/(s*s)
            if abs(centered) < max_allowed:
                accepted += 1
            else:
                assert hi-lo > arb(1)/2**30, (rate, lo, hi, centered, max_allowed)
                mid = (lo+hi)/2
                pieces.extend(((lo,mid),(mid,hi)))
    print(f'Certified circles at all integer rates 8 through 49 in {accepted} boxes.')


if __name__ == '__main__':
    main()
