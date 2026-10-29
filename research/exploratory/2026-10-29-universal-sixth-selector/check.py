from fractions import Fraction as F

v = F(297617, 1000000)
p = F(61939, 1000000)
s = 2*v*p
rj = 3*(1-s)*(1-v)/(3-v-2*s)
r0 = (15-16*v)/(15-6*v)
assert 0 < s < F(1,6) and rj < r0
print('proxy slope:', s, float(s))
print('joint exponent:', rj, float(rj))
print('unmarked exponent:', r0, float(r0))
print('density gain:', r0-rj, float(r0-rj))

theta = F(43643617,50000000)
h = F(4,5)
v = F(313264,1000000)
p = F(266015,1000000)
s = 2*v*p
assert s < F(1,6) and p < F(3,8)
ell = F(11,3)-4*theta
y = h-2*ell
kappa = 2*theta-1
d = h+F(1,10**10)
bp = F(49283557,50000000)
lp = F(4503,2000)
capacity = min(F(619,10000)*d, (2*y-(2-bp)*d)/lp)
D = 3-p-2*p/(3*kappa)
P = 2*(1-p)*(1-p/(3*kappa))
V = F(5,6)-v
J = V*D+v*P
r = 1-v+v*P*V/(2*J)
base = F(1,2)+F(13,75)*h-y/2-ell/2-F(9,100)*d+v/2+v*p*(ell-capacity/2)
gap = base+F(3,4)*d*r-theta
assert gap > 0
assert gap == F(6126846623895440724696345220996823334100321,43091984449575605704331250000000000000000000000)
print('point slope:', s, float(s))
print('physical capacity:', capacity)
print('row excess:', gap, float(gap))
