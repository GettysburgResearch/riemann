"""Check the strict Gaussian margin from Trudgian–Yang, Theorem 2.4."""
from fractions import Fraction as Q


# log(T/(2*pi)) can replace log(2*T) after a fixed positive margin.
HEAT = Q(397, 625)
ENDPOINTS = [
    Q(1, 2), Q(88225, 153852), Q(521, 796), Q(53141, 76066),
    Q(3620, 5119), Q(52209, 69128), Q(1389, 1736), Q(134765, 163248),
    Q(18193, 21906), Q(249, 280), Q(9, 10), Q(1),
]
# mu(sigma) <= (a - b*sigma)/d. Interpolate the last section to mu(1)=0.
PLANES = [
    (31, 36, 84), (220633, 251324, 620612), (1333, 1508, 3825),
    (405, 454, 1202), (49318855, 52938216, 170145110),
    (471957, 502648, 1682490), (2841, 3016, 10316),
    (859, 908, 3214), (43535, 45335, 180277), (29, 30, 130),
    (2, 2, 13),
]


def minimum_margin(c):
    margins = []
    for (a, b, d), left, right in zip(PLANES, ENDPOINTS, ENDPOINTS[1:]):
        stationary = Q(1, 2) + c * (1 - 2 * Q(b, d))
        sigma = min(right, max(left, stationary))
        margin = (c + Q(1, 2) - sigma) ** 2 / (4 * c) - (a - b * sigma) / d
        margins.append(margin)
    return min(margins)


if __name__ == "__main__":
    margin = minimum_margin(HEAT)
    print("Minimum gap:", margin)
    assert margin > Q(1, 30_000)
