"""Exact fixed-face obstruction; see README. Requires SymPy."""
import runpy
from pathlib import Path
import sympy as s

ns = runpy.run_path(str(Path(__file__).with_name('check_rows.py')))
R = s.Rational
D = R(223, 500)
p = R(1, 2)
point_windows = [(i, n) for i, (n, a, b, lo) in enumerate(ns['windows'], 1)
                 if a <= D <= b and lo <= p <= R(1, 2)]
assert point_windows == [(7, 'C'), (12, 'C'), (14, 'C'), (15, 'C'), (16, 'C'), (17, 'C')]

B, L = R(96232839, 10**8), R(3853, 2000)
PB, PL = R(49283557, 50000000), R(4503, 2000)
V = R(5, 6) - D
C0 = 1 - 2*p*B/L
U = (1-p)*C0
J = V*(3-p-4*p/L) + D*(1-p)*(2-4*p/L)
count = s.factor((1-D)+V*D*U/J)
assert count == R(137478360780643, 225606975000000)

k = s.symbols('k', real=True)
oldD = 3-p-2*p/(3*k)
oldC = 2*(1-p)*(1-p/(3*k))
oldJ = V*oldD + D*oldC
old = s.factor(1-D + D*oldC*V/(2*oldJ))
old_derivative = s.factor(s.diff(old, k))
assert old_derivative == 225828309/(1000*(12729*k-1831)**2)
old_margin = s.factor(old.subs(k, R(373, 500)) - count)
assert old_margin == R(2927366587426695869, 864620006308575000000) and old_margin > 0

T, h = s.symbols('T h', real=True)
ell = R(11, 3)-4*T
# This conductor line is an upper bound on newCapacity at d=h.
line = (PB*h-4*ell)/PL
base = R(1, 2)+R(13, 75)*h-(h-2*ell)/2-ell/2-R(9, 100)*h+D/2+D*p*(ell-line/2)
gap = s.factor(base+R(3, 4)*h*count-T)
h_slope = s.factor(s.diff(gap, h)); t_slope = s.factor(s.diff(gap, T))
assert h_slope == -R(11447677710517817,1354544277900000000) and h_slope < 0
assert t_slope == -R(5273419,1125750) and t_slope < 0
margin = s.factor(gap.subs({T:R(43693,50000),h:R(403,500)}))
assert margin == R(88261806706387247,2031816416850000000000) and margin > 0
threshold = R(8317278773899883959247,9517760867980200000000)
assert gap.subs({T:threshold,h:R(403,500)}) == 0
assert R(873,1000) < threshold < R(7,8)
gain = R(43693617,50000000)-threshold
assert gain == R(29187362404488421,9517760867980200000000)
print('available windows:', point_windows)
print('C count:', count, 'old excess at k=373/500:', old_margin)
print('h slope:', h_slope, 'theta slope:', t_slope)
print('gap at theta=0.87386,h=0.806:', margin, '≈', float(margin))
print('threshold:', threshold, '≈',float(threshold), 'maximum gain:',gain, '≈',float(gain))
# Quantify the physical-line bottleneck at this one parameter point.
t0, h0 = R(43693,50000), R(403,500)
e0 = R(11,3)-4*t0
y0 = h0-2*e0
base0 = R(1,2)+R(13,75)*h0-y0/2-e0/2-R(9,100)*h0+D/2+D*p*e0
c_required = s.factor(2*(base0+R(3,4)*h0*count-t0)/(D*p))
c_line = s.factor((PB*h0-4*e0)/PL)
b_required = s.factor((PL*c_required+4*e0)/h0)
lambda_max = s.factor((PB*h0-4*e0)/c_required)
assert c_required == R(2467396034273387,50310355425000000) and c_required > c_line
assert c_line == R(8215820413,168862500000)
assert b_required == R(80026480008237061661,81100292945100000000)
assert lambda_max == R(5511211267813337207,2467396034273387000)
print('one-point physical-line thresholds:', c_required, c_line, b_required, lambda_max)
