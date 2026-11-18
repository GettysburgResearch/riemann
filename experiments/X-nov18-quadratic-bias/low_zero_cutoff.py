"""A uniform conductor cutoff for the single low-zero coefficient test."""
from flint import arb, ctx


ctx.prec = 112
width = arb(5)/3
radius = arb(743)/1000
denominator = 96*width**4


def transform(v):
    if v <= 2*width:
        return (radius**2*(32*width**3-12*width*v**2+3*v**3)
                -24*width+18*v)/denominator
    assert v >= 2*width
    return (radius**2*(4*width-v)**3+6*(4*width-v))/denominator


def regular_difference(v, inner):
    if inner:
        return (radius**2*(12*width*v-3*v**2)-18)/denominator
    return (transform(arb(0)) -
            (radius**2*(4*width-v)**3+6*(4*width-v))/denominator)/v


def psi_kernel(v):
    if v.is_zero():
        return arb(1)/2
    return v/(-(-2*v).expm1())


def arch_lower(parity):
    g0 = transform(arb(0))
    rate = arb(1)/2+parity
    value = g0*(rate/2).digamma()
    panels = 512
    for i in range(2*panels):
        left, right = 2*width*i/panels, 2*width*(i+1)/panels
        v = left.union(right)
        factor = (-rate*v).exp()*psi_kernel(left).union(psi_kernel(right))
        value += 2*(right-left)*regular_difference(v, i<panels)*factor
    # The omitted integral above 4*width has positive sign.
    return value.lower()


def prime_cost():
    bound = 800
    assert arb(bound).log()>4*width
    primes = bytearray([1])*(bound+1)
    total = arb(0)
    for p in range(2, bound+1):
        if not primes[p]:
            continue
        for composite in range(p*p, bound+1, p):
            primes[composite] = 0
        n = p
        while arb(n).log() < 4*width:
            total += 2*abs(transform(arb(n).log()))*arb(p).log()/arb(n).sqrt()
            n *= p
    return total


if __name__ == '__main__':
    cost = prime_cost()
    for a in (0, 1):
        lower = (arb(10**20)/arb.pi()).log()*transform(arb(0))+arch_lower(a)-cost
        assert lower > 0
        print(f'parity {a}: lower margin {lower}')
    assert (arb(1)/4+radius**2)*(arb(9)/4+radius**2)<arb(9)/4
