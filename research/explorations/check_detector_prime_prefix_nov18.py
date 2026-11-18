"""Finite weighted Mertens induction and signed 5:3 deconvolution; python-flint."""
from math import ceil, isqrt

from flint import arb, ctx


def main():
    ctx.prec = 96
    q, p = 10**16, 10**19
    limit = 16
    size = 1 << limit
    composite = bytearray(size)
    for prime in range(2, isqrt(size) + 1):
        if not composite[prime]:
            for multiple in range(prime**2, size, prime):
                composite[multiple] = 1
    values = [arb(0)] * size
    for prime in range(2, size):
        if not composite[prime]:
            multiple = prime
            while multiple < size:
                values[multiple] = arb(prime).log()
                multiple *= prime
    w = [arb(0)] * limit
    small = arb(0)
    for k in range(1, size):
        coefficient = abs(values[k] - 1)
        w[k.bit_length() - 1] += coefficient / k
        if k <= 1000:
            small += coefficient / arb(k)**(arb(3) / 4)
    assert small < arb(25513) / 1000

    bounds = [arb(0)]
    for j in range(1, limit + 1):
        lo = arb(q * 2**(j - 1))
        hi = lo * 2
        forcing = arb('6.1') * lo**(-arb(1)/4) + 3 / lo.sqrt() + 2 * arb(q).sqrt()/lo
        prime_tail = 1 + max(arb(0), (hi / p).log())
        forcing += arb('2.1e-8') * prime_tail
        earlier_integral = sum(bounds[l] / 2**(j-l) for l in range(1, j))
        earlier_sum = sum(w[r] * max(bounds[j-r-1], bounds[j-r]) for r in range(1, j))
        bounds.append((forcing + earlier_integral + earlier_sum) / (lo.log() - arb('1.5')))

    largest = arb(0)
    for j in range(9, limit):
        lo, hi = arb(q * 2**(j-1)), arb(q * 2**j)
        u = hi.log()
        t = 2*u/(3*20000**2)
        # Adjacent boxes cover shifts of log(m) by at most 0.01.
        coeff = arb(0)
        for d, mag in ((0, 6), (1, arb('4.5')), (2, arb('.75'))):
            coeff += mag * max(bounds[j-d-1:j-d+2])
        # Bound using erfc's exact exponentially tilted integral.
        variation = (2*(t/arb.pi()).sqrt() + t/2) * (t/4).exp()
        ratio = (1 + hi.sqrt() * coeff * variation) / lo.log()
        printed_ceiling = ceil(float(ratio.upper()) * 1_000_000) / 1_000_000
        assert ratio < arb(str(printed_ceiling))
        print(f'X <= {q*2**j}: correction/logX < {printed_ceiling:.6f}')
        if j < limit:
            largest = max(largest, ratio)
    assert largest < arb('6.5')
    print(f'Proved strict positivity through {q*2**15}. Small sum {small}.')


if __name__ == '__main__':
    main()
