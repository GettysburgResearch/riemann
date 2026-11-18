from collections import defaultdict
from fractions import Fraction
from math import factorial
from flint import arb, ctx

ctx.prec = 256
degree = 70
shift = Fraction(13, 2)
q = {j: shift**j / factorial(j) for j in range(degree+1)}

def multiply_by_y(coefficients):
    result = defaultdict(Fraction)
    for j, coefficient in coefficients.items():
        result[j+1] += coefficient
        if j:
            result[j-1] += j*coefficient
    return result

def pairing(coefficients):
    return sum((value * coefficients.get(j, 0) * factorial(j)
                for j, value in q.items()), Fraction())

n0 = pairing(q)
previous = {}
current = q
ratios = []
for k in range(5):
    ratios.append(pairing(current)/n0)
    following = multiply_by_y(current)
    for j, coefficient in previous.items():
        following[j] -= k*coefficient
    previous, current = current, following
assert ratios[0] == 1

def ball(x):
    return arb(x.numerator) / arb(x.denominator)

sigma = (arb(2).log() / 2).sqrt()
s = 1 / (20 * sigma)
q_prime = 7 / (12000 * sigma)
coefficients = (1, q_prime - 4*s, 6*s*s - s*q_prime, -4*s**3, s**4)
result = sum((a*ball(b) for a,b in zip(coefficients,ratios)),arb(0))
assert result < arb('-0.00118')
assert result.overlaps(arb('[-0.0011820826117612421070700877231385172065234035734122633 +/- 5.66e-56]'))
print(result)
