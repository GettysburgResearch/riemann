"""Enclose the spectral input for the unsmoothed 5:3 positivity prefix."""
import argparse
from flint import acb, acb_series, arb, ctx


def verify(height):
    if height < 2000:
        raise ValueError("the analytic bound requires height at least 2000")
    ctx.prec = 96
    half = arb(1) / 2
    log_two = arb(2).log()

    def numerator(z):
        term = (-z * log_two).exp()
        return -3 * (term - 1) * (term - 2)

    z = acb_series([half, 1], prec=2)
    affine = 6 + numerator(z) / z.zeta()
    assert affine[0].real > arb(677) / 100
    assert affine[1].real > -half
    residue_sum = arb(0)
    next_index = 1
    finished = False
    while not finished:
        for rho in acb.zeta_zeros(next_index, 256):
            if rho.imag > height:
                finished = True
                break
            assert rho.imag < height and rho.real == half
            derivative = acb_series([rho, 1], prec=2).zeta()[1]
            assert abs(derivative) > 0
            residue_sum += 2 * abs(numerator(rho) / ((rho - half)**2 * derivative))
            next_index += 1
    assert residue_sum < 1
    print(f"Completed {next_index-1} zeros below {height}", flush=True)

    # Rectangles cover the full continuous top edge; bisect any overwide enclosure.
    coarse = [-1 + arb(151) * j / (100 * 256) for j in range(257)]
    pieces = list(zip(coarse, coarse[1:]))
    accepted = 0
    while pieces:
        lo, hi = pieces.pop()
        s = acb(lo.union(hi), height)
        z = s + half
        value = (6 + numerator(z) / z.zeta()) / s**2
        if abs(value) < 1:
            accepted += 1
        else:
            assert hi - lo > arb(1) / 2**30, "edge failed to certify"
            mid = (lo + hi) / 2
            pieces.extend(((lo, mid), (mid, hi)))

    horizon = 5 * height**4 // 4
    print(f"H={height}, {next_index-1} positive ordinates, residue sum {residue_sum}")
    print(f"Accepted horizontal boxes={accepted}, certified upper X={horizon}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--height", type=int, default=2000)
    verify(parser.parse_args().height)
