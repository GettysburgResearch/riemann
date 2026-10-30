"""Check exact rational arithmetic; analytic sieve/detector inputs are not checked."""
from fractions import Fraction as Q

sigma = Q(437, 500)
theta = Q(4369347, 5000000)
delta = 2 * sigma - 1
assert theta < sigma < Q(7, 8)
khale = 4 * (1 - sigma) / sigma

def f(n, c, x):
    return max(1 - delta*x, c + (1-delta)*x,
               1-c + (Q(2, n)-delta)*x)

def natural_density(n):
    d = delta * (delta*n*n-(1+3*delta)*n+3)
    d /= delta*(2-delta)*n*n-2*(1+delta)*n+2
    return 1-d

for n, a, expected in ((4, Q(31,375), Q(163,300)),
                        (5, Q(29,300), Q(51,100))):
    c = (1+(n-2)*a)/n
    R = 1-Q(5,6)*delta+Q(2,3*n)
    assert R == expected
    assert f(n,c,Q(2,3)) == f(n,c,Q(1)) == R
    assert f(n,c,Q(0)) > R  # The detector's split is essential.
    comparator = (1+(n-2)*a)*natural_density(n)
    assert comparator > R and khale > R
    if n == 4:
        quadratic = 1-delta/2-delta*delta/2
        assert quadratic == Q(43281,125000) and quadratic < R
        assert comparator == Q(179303,305700)
        assert R/3 == Q(163,900)
    else:
        assert comparator == Q(6181293,9915500)
        assert R/4 == Q(51,400)
    print(f'n={n} a={a} R={R} disc={R/(n-1)} deF={comparator} Khale={khale}')

n = 11
c = Q(1,n)
t = Q(3*(n-2),1) / (n*(3-delta)-4)
L = 2*t/3
R = c+(1-delta)*t
assert Q(1)<t<Q(3,2) and Q(1,2)<L<1
assert f(n,c,L) == f(n,c,t) == R == Q(2656,6347)
assert R/10 == Q(1328,31735)
assert natural_density(n) == Q(2100479,4803751) > R
assert khale > R
print(f'n={n} a=0 t={t} L={L} R={R} disc={R/10} deF={natural_density(n)} Khale={khale}')
print('All rational checks passed; no analytic theorem or kernel admission was checked.')
