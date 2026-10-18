"""Exact generic moment map for one additional ferromagnetic cross edge.

The two selected components are distinct copies conditional on the fair hub.
The extra edge has correlation q=tanh(J).  Multiplying the conditional law
by (1+q*sigma_i*sigma_j)/(1+q*E sigma_i E sigma_j) gives the exact cyclic
Ising law.  No expansion in q is taken.  Scalars may be Fractions, Decimal,
or outward intervals.  This file alone is not an existence certificate.
"""
from math import comb


class Dual:
    __slots__ = ('v', 'd')
    def __init__(self, v, d):
        self.v, self.d = v, tuple(d)
    def __add__(self, o):
        if isinstance(o, Dual):
            return Dual(self.v+o.v, [a+b for a, b in zip(self.d, o.d)])
        return Dual(self.v+o, self.d)
    __radd__ = __add__
    def __neg__(self):
        return Dual(-self.v, [-a for a in self.d])
    def __sub__(self, o): return self+-o
    def __rsub__(self, o): return -self+o
    def __mul__(self, o):
        if isinstance(o, Dual):
            return Dual(self.v*o.v, [a*o.v+self.v*b for a, b in zip(self.d, o.d)])
        return Dual(self.v*o, [a*o for a in self.d])
    __rmul__ = __mul__
    def __truediv__(self, o):
        if isinstance(o, Dual):
            v = self.v/o.v
            return Dual(v, [(a-v*b)/o.v for a, b in zip(self.d, o.d)])
        return Dual(self.v/o, [a/o for a in self.d])
    def __rtruediv__(self, o):
        v = o/self.v
        return Dual(v, [-v*a/self.v for a in self.d])
    def __pow__(self, n):
        if n == 0: return Dual(self.v*0+1, [a*0 for a in self.d])
        if n == 1: return self
        v = self.v**(n-1)
        return Dual(v*self.v, [n*v*a for a in self.d])


def cumulants(mu):
    zero = mu[0]*0
    kap = [zero]*len(mu)
    for n in range(1, len(mu)):
        kap[n] = mu[n]-sum((comb(n-1, j-1)*kap[j]*mu[n-j]
                           for j in range(1, n)), zero)
    return kap


def moments(kap):
    zero = kap[0]*0
    mu = [zero+1]
    for n in range(1, len(kap)):
        mu.append(sum((comb(n-1, j-1)*kap[j]*mu[n-j]
                       for j in range(1, n+1)), zero))
    return mu


def convolve(a, b):
    zero = a[0]*0
    return [sum((comb(n, j)*a[j]*b[n-j] for j in range(n+1)), zero)
            for n in range(min(len(a), len(b)))]


def unit_cumulants(degree):
    return cumulants([int(n % 2 == 0) for n in range(degree+1)])


def block(z, i, eta, degree, vertex):
    zero, one = z[0]*0, z[0]*0+1
    A, B, p = z[3*i:3*i+3]
    magnitude = [one]+[(A**n if i == 0 else p*A**n+(one-p)*B**n)
                       for n in range(1, degree+1)]
    mu = [v*(one if n % 2 == 0 else eta) for n, v in enumerate(magnitude)]
    if vertex == 'root':
        score = [v*(eta if n % 2 == 0 else one)
                 for n, v in enumerate(magnitude)]
    elif vertex == 'child' and i:
        signed_magnitude = [2*p-one]+[p*A**n-(one-p)*B**n
                                       for n in range(1, degree+1)]
        score = [v*(eta if n % 2 == 0 else one)
                 for n, v in enumerate(signed_magnitude)]
    else:
        raise ValueError('a component has no such vertex')
    return mu, score


def evaluate(zq, counts, eta, degree, types, vertices=('root', 'root')):
    if len(zq) != 3*len(counts)+1:
        raise ValueError('complete tree parameters plus cross correlation required')
    i, j = types
    if not (0 <= i <= j < len(counts)) or i == j and counts[i] < 2:
        raise ValueError('cross edge requires distinct component copies')
    zero, one = zq[0]*0, zq[0]*0+1
    eta, q = one*eta, zq[-1]
    total = [zero]*(degree+1)
    for k, count in enumerate(counts):
        mu, _ = block(zq, k, eta, degree, 'root')
        kap = cumulants(mu)
        total = [a+count*b for a, b in zip(total, kap)]
        if k in types:
            total = [a-(2 if i == j else 1)*b for a, b in zip(total, kap)]
    left, score_left = block(zq, i, eta, degree, vertices[0])
    right, score_right = block(zq, j, eta, degree, vertices[1])
    original, score = convolve(left, right), convolve(score_left, score_right)
    normalizer = one+q*score[0]
    pair = [(a+q*b)/normalizer for a, b in zip(original, score)]
    total = [a+b for a, b in zip(total, cumulants(pair))]
    raw = [x if n % 2 == 0 else zero for n, x in enumerate(moments(total))]
    kap, unit = cumulants(raw), unit_cumulants(degree)
    return [kap[2*r]/unit[2*r] for r in range(1, degree//2+1)], raw


def jet(zq, counts, eta, degree, active, types, vertices=('root', 'root')):
    zero, one = zq[0]*0, zq[0]*0+1
    zz = [Dual(x, [one if j == k else zero for k in active])
          for j, x in enumerate(zq)]
    values, raw = evaluate(zz, counts, eta, degree, types, vertices)
    return [x.v for x in values], [list(x.d) for x in values], [x.v for x in raw]
