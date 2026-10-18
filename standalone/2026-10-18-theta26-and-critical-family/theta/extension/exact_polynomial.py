"""Standard-library polynomial primitives, with no optimizer imports.

The formulas operate on Fractions, Decimals, directed intervals, or Duals
over those scalars.  No numerical summation truncation is involved.
"""
from math import comb


def cumulants(mu):
    zero=mu[0]*0
    k=[zero for _ in mu]
    for n in range(1,len(mu)):
        k[n]=mu[n]-sum((comb(n-1,j-1)*k[j]*mu[n-j] for j in range(1,n)),zero)
    return k


def unit_cumulants(degree=20):
    return cumulants([int(n%2==0) for n in range(degree+1)])


class Dual:
    __slots__=('v','d')
    def __init__(self,v,d):
        self.v=v
        self.d=tuple(d)
    def __add__(self,other):
        if isinstance(other,Dual):
            return Dual(self.v+other.v,[a+b for a,b in zip(self.d,other.d)])
        return Dual(self.v+other,self.d)
    __radd__=__add__
    def __neg__(self):
        return Dual(-self.v,[-a for a in self.d])
    def __sub__(self,other):
        return self+-other
    def __rsub__(self,other):
        return -self+other
    def __mul__(self,other):
        if isinstance(other,Dual):
            return Dual(self.v*other.v,[a*other.v+self.v*b for a,b in zip(self.d,other.d)])
        return Dual(self.v*other,[a*other for a in self.d])
    __rmul__=__mul__
    def __truediv__(self,other):
        if isinstance(other,Dual):
            return Dual(self.v/other.v,[(a*other.v-self.v*b)/(other.v*other.v)
                                       for a,b in zip(self.d,other.d)])
        return Dual(self.v/other,[a/other for a in self.d])
    def __pow__(self,n):
        if n==0:return Dual(self.v*0+1,[a*0 for a in self.d])
        return Dual(self.v**n,[n*self.v**(n-1)*a for a in self.d])


def linear_solve(matrix,rhs):
    n=len(rhs)
    if len(matrix)!=n or any(len(row)!=n for row in matrix):
        raise ValueError('square system required')
    a=[list(row)+[v] for row,v in zip(matrix,rhs)]
    for j in range(n):
        pivot=max(range(j,n),key=lambda i:abs(a[i][j]))
        if a[pivot][j]==0:raise ArithmeticError('singular system')
        a[j],a[pivot]=a[pivot],a[j]
        scale=a[j][j]
        a[j]=[v/scale for v in a[j]]
        for i in range(n):
            if i!=j:
                q=a[i][j]
                a[i]=[v-q*w for v,w in zip(a[i],a[j])]
    return [row[-1] for row in a]
