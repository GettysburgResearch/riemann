"""Bound a recurrent prime-error profile by interval integration (python-flint 0.9)."""

from flint import arb, ctx


def main():
    ctx.prec = 96
    start = 1024
    stop = 2 * start
    parts = 8
    jumps = [arb(0) for _ in range(stop)]
    composite = bytearray(stop)
    for p in range(2, stop):
        if composite[p]:
            continue
        for multiple in range(2 * p, stop, p):
            composite[multiple] = 1
        power = p
        while power < stop:
            jumps[power] = arb(p).log()
            power *= p

    psi = sum(jumps[:start])
    first = arb(0)
    second = arb(0)
    for integer in range(start, stop):
        psi += jumps[integer]
        for j in range(parts):
            left = arb(integer) + arb(j) / parts
            right = left + arb(1) / parts
            t = left.union(right)
            # Add 1 and omit a constant; neither changes centered variance.
            profile = 1 + (psi - t + (1 - 1 / t**2).log() / 2) / 32 - (t / start).sqrt()
            weight = (right / left).log()
            first += weight * profile
            second += weight * profile**2

    variance = second - first**2 / arb(2).log()
    print(variance.sqrt())
    assert variance > arb("0.26")**2


if __name__ == "__main__":
    main()
