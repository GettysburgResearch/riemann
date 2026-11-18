"""Independent interval replay of the finite Lagarias and CA table checks."""
from fractions import Fraction

from mpmath import iv

iv.dps = 45
last = 5041
sigma = [0] * (last + 1)
for divisor in range(1, last + 1):
    for multiple in range(divisor, last + 1, divisor):
        sigma[multiple] += divisor

harmonic = iv.mpf(0)
for n in range(1, last + 1):
    harmonic += iv.mpf(1) / n
    product_gap = iv.exp(harmonic) * iv.ln(harmonic) - sigma[n]
    gap = harmonic + product_gap
    if n == 1:
        assert gap == 0
    elif n == 2:
        minimum = gap
        assert minimum > iv.mpf("0.3171685434")
    else:
        assert gap > minimum, (n, gap)
    if n == 60:
        assert product_gap < 0
    if n > 60:
        assert product_gap > 0, (n, product_gap)

x = iv.ln(3)
assert iv.ln(x + 1) < iv.ln(x) + 1 / iv.ln(4)
assert iv.ln(10) > iv.mpf(137) / 60
loglog12 = iv.ln(iv.ln(12))
coefficient = (iv.mpf(7) / 3 - iv.exp(iv.euler) * loglog12) * loglog12
assert iv.mpf("0.64821364942179") < coefficient < iv.mpf("0.64821364942181")

primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41)


def threshold(p, exponent):
    return iv.ln(1 + 1 / iv.mpf(sum(p**j for j in range(1, exponent + 1)))) / iv.ln(p)


assert threshold(2, 16) < threshold(41, 1)
events = [(threshold(p, a), p, a) for p in primes for a in range(1, 16)]
events.sort(key=lambda event: float(event[0].mid), reverse=True)
assert all(left[0] > right[0] for left, right in zip(events, events[1:]))

expected = (
    (2, 2, 1, 1500),
    (6, 3, 1, 2000),
    (12, 2, 2, 2333),
    (60, 5, 1, 2800),
    (120, 2, 3, 3000),
    (360, 3, 2, 3250),
    (2520, 7, 1, 3714),
    (5040, 2, 4, 3838),
    (55440, 11, 1, 4187),
    (720720, 13, 1, 4509),
    (1441440, 2, 5, 4581),
    (4324320, 3, 3, 4699),
    (21621600, 5, 2, 4855),
    (367567200, 17, 1, 5141),
    (6983776800, 19, 1, 5412),
    (160626866400, 23, 1, 5647),
    (321253732800, 2, 6, 5692),
    (9316358251200, 29, 1, 5888),
    (288807105787200, 31, 1, 6078),
    (2021649740510400, 7, 2, 6187),
    (6064949221531200, 3, 4, 6238),
    (224403121196654400, 37, 1, 6407),
)
n = 1
ratio = Fraction(1)
for (_, p, a), (row_n, row_prime, row_exponent, displayed) in zip(events, expected):
    n *= p
    ratio *= Fraction(p ** (a + 1) - 1, p * (p**a - 1))
    assert (n, p, a) == (row_n, row_prime, row_exponent)
    assert (ratio * 1000).__floor__() == displayed, (n, ratio, displayed)

next_event = events[len(expected)]
assert next_event[1:] == (41, 1)
assert n * next_event[1] == 9200527969062830400 > 10**18
print(f"Lagarias and Kaneko finite intervals passed. Minimum additive gap: {minimum}")
print(f"Constant at n=12: {coefficient}")
print(f"Certified CA rows: {len(expected)}. First omitted nontrivial CA n: {n * next_event[1]}")
