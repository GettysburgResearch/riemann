"""Integer-directed intervals. No floating point is used for acceptance."""
from functools import lru_cache
from math import isqrt

BITS = 112
S = 1 << BITS
ZERO = (0, 0)
ONE = (S, S)

def ceildiv(a, b):
    if b <= 0:
        raise ValueError("positive denominator required")
    return -((-a) // b)

def rat(a, b=1):
    return (a*S//b, ceildiv(a*S, b))

def add(a, b):
    return (a[0]+b[0], a[1]+b[1])

def neg(a):
    return (-a[1], -a[0])

def sub(a, b):
    return add(a, neg(b))

def scale(a, n, d=1):
    vals = (a[0]*n, a[1]*n)
    return (min(vals)//d, ceildiv(max(vals), d))

def mul(a, b):
    vals = [x*y for x in a for y in b]
    return (min(vals)//S, ceildiv(max(vals), S))

def inv(a):
    if a[0] <= 0:
        raise ValueError("strictly positive interval required")
    return (S*S//a[1], ceildiv(S*S, a[0]))

def sqrt_iv(a):
    if a[0] < 0:
        raise ValueError("nonnegative interval required")
    lo = isqrt(a[0]*S)
    hi = isqrt(a[1]*S)
    return (lo, hi+(hi*hi < a[1]*S))

def root4_int(n):
    if n <= 0:
        raise ValueError("positive integer required")
    lo = isqrt(isqrt(n*S**4))
    return (lo, lo+(lo**4 < n*S**4))

def intersect(a, b):
    return max(a[0], b[0]) <= min(a[1], b[1])

def maximum(xs):
    xs = list(xs)
    if not xs:
        raise ValueError("empty maximum")
    return (max(x[0] for x in xs), max(x[1] for x in xs))

def _log_reduced(num, den):
    # 1 <= num/den <= 2, hence 0 <= z <= 1/3.
    if not den <= num <= 2*den:
        raise ValueError("range reduction failed")
    a, b = num-den, num+den
    if not a:
        return ZERO
    terms = 48
    lo = 0
    for j in range(terms):
        e = 2*j+1
        lo += (2*S*a**e)//((2*j+1)*b**e)
    e = 2*terms+1
    # Tail <= 2*z^e/[e*(1-z^2)].
    tail = ceildiv(2*S*a**e*b*b, e*b**e*(b*b-a*a))
    return (lo, lo+terms+tail)

@lru_cache(maxsize=None)
def log_int(n):
    if n < 1:
        raise ValueError("positive integer required")
    power = n.bit_length()-1
    return add(scale(_log_reduced(2, 1), power),
               _log_reduced(n, 1 << power))

def decode(a):
    if (not isinstance(a, list) or len(a) != 2 or
        any(type(x) is not int for x in a) or a[0] > a[1]):
        raise ValueError("invalid typed interval")
    return tuple(a)

def describe(a):
    # Display only, never an acceptance input.
    return (a[0]/S, a[1]/S)
