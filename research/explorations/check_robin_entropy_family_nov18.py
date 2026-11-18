"""Certify a finite family in a prescribed near-Robin interval using python-flint."""
from flint import arb, ctx

from check_robin_lcm_fixed_nov18 import events


def main():
    ctx.prec = 128
    cutoff = 10_000_000
    prime_pairs = 4_000
    target_log = 4_342_945 * arb(10).log()
    log_start = arb(0)
    abundancy = arb(0)
    below = []
    above = []
    for q, p in events(cutoff + 100_000):
        if q == p and p > cutoff - 100_000:
            (below if p <= cutoff else above).append(p)
        if q > cutoff:
            continue
        log_start += arb(p).log()
        abundancy += (arb(p - 1) / (p * (q - 1))).log1p()
        if p == q and cutoff < p * p <= 2 * cutoff:
            log_start += arb(p).log()
            abundancy += (arb(1) / (p * (p + 1))).log1p()

    assert len(below) >= prime_pairs and len(above) >= prime_pairs
    max_log = log_start
    min_abundancy = abundancy
    for low, high in zip(reversed(below[-prime_pairs:]), above[:prime_pairs]):
        assert low * low > 2 * cutoff and low <= cutoff < high
        max_log += (arb(high) / low).log()
        min_abundancy += (arb(1) / high).log1p() - (arb(1) / low).log1p()
    relative_width = (max_log - target_log).exp()
    corrected_log = target_log + relative_width.log1p()
    normalized = (min_abundancy - arb.const_euler() - corrected_log.log().log())
    normalized *= corrected_log.sqrt() * corrected_log.log()
    max_multiplier = (target_log - log_start).exp() + 1
    count_log10 = (prime_pairs * arb(2).log() - max_multiplier.log()) / arb(10).log()
    print("log of starting integer", log_start)
    print("largest uncorrected log", max_log)
    print("relative interval width", relative_width)
    print("lower bound for normalized log Robin ratio", normalized)
    print("lower bound for base-10 log of distinct count", count_log10)
    assert relative_width < 5 * arb(10) ** -48
    assert normalized > -1
    assert count_log10 > 1145


if __name__ == "__main__":
    main()
