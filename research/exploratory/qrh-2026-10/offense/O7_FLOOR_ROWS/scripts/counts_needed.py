#!/usr/bin/env python3
"""O7: row-count exponent R(delta) needed above the raised floor delta0 = 1/3 for sigma0 = 28/33, at the
LP geometry (3/11, 6/11, 2/11), top dyad d = h, slot amplitude x = 1/2.  Exact Fractions.  PROPOSED."""
from fractions import Fraction as Fr
lx, ly, l = Fr(3, 11), Fr(6, 11), Fr(2, 11); h = 1 - lx + l; s = Fr(28, 33)
def Rmax(d):
    a = (1 + d)/2
    return (s - a*(1 - ly) + l/2 - d*l/2)/h - d/2 + Fr(1, 6)
for d in (Fr(1, 3), Fr(2, 5), Fr(1, 2), Fr(3, 5), Fr(23, 33)):
    print(d, Rmax(d), float(Rmax(d)), 'DH', 1 - d)
print('Rmax(delta) =', Rmax(Fr(0)), '+', Rmax(Fr(1)) - Rmax(Fr(0)), '* delta')
