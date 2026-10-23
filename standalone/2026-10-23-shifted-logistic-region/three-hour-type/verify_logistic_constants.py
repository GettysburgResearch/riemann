"""Exact rational enclosures for the logistic analytic adapter.

No floating-point comparison is used for any pass/fail decision.
This checks constants, not the analytic explicit formula or a zero-free theorem.
"""
from fractions import Fraction as Q
import json


class I:
    def __init__(self, lo, hi=None):
        self.lo = Q(lo)
        self.hi = Q(lo if hi is None else hi)
        if self.lo > self.hi:
            raise ValueError("reversed interval")

    @staticmethod
    def get(x):
        return x if isinstance(x, I) else I(x)

    def __add__(self, other):
        o = I.get(other)
        return I(self.lo + o.lo, self.hi + o.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-I.get(other))

    def __rsub__(self, other):
        return I.get(other) - self

    def __mul__(self, other):
        o = I.get(other)
        p = [self.lo*o.lo, self.lo*o.hi, self.hi*o.lo, self.hi*o.hi]
        return I(min(p), max(p))

    __rmul__ = __mul__

    def reciprocal(self):
        if self.lo <= 0 <= self.hi:
            raise ZeroDivisionError("interval contains zero")
        return I(1/self.hi, 1/self.lo)

    def __truediv__(self, other):
        return self * I.get(other).reciprocal()

    def __rtruediv__(self, other):
        return I.get(other) / self


checks = 0


def check(condition, label):
    global checks
    checks += 1
    if not condition:
        raise RuntimeError(label)


def sincos(x, sine):
    """Alternating series enclosure, x in [0, 2.3]."""
    x = Q(x)
    term = x if sine else Q(1)
    total = term
    for j in range(1, 24):
        left = 2*j if sine else 2*j-1
        term *= -x*x / (left*(left+1))
        total += term
    j = 24
    left = 2*j if sine else 2*j-1
    nxt = term * (-x*x)/(left*(left+1))
    return I(min(total,total+nxt),max(total,total+nxt))


def atan_unit(q):
    q = Q(q)
    total = Q(0)
    for j in range(40):
        total += (-1)**j * q**(2*j+1) / (2*j+1)
    nxt = q**81 / 81
    return I(total,total+nxt)


def log_one_to_two(q):
    q = Q(q)
    z = (q-1)/(q+1)
    total = sum((2*z**(2*j+1)/Q(2*j+1) for j in range(80)), Q(0))
    rem = 2*z**161 / (161*(1-z*z))
    return I(total,total+rem)


LOG2 = log_one_to_two(Q(2))


def log_rational(q):
    q = Q(q)
    if q <= 0:
        raise ValueError("log domain")
    k = 0
    while q >= 2:
        q /= 2
        k += 1
    while q < 1:
        q *= 2
        k -= 1
    return log_one_to_two(q) + k*LOG2


def log_interval(q):
    return I(log_rational(q.lo).lo,log_rational(q.hi).hi)


def exp_lower(q, degree):
    term = Q(1)
    total = term
    for j in range(1, degree+1):
        term *= q/Q(j)
        total += term
    return total


theta = Q(5669,5000)
sin_t, cos_t = sincos(theta,True), sincos(theta,False)
sin_2t = sincos(2*theta,True)
sec2, tan_t, cot_t = 1/(cos_t*cos_t),sin_t/cos_t,cos_t/sin_t
w0 = sec2*(theta*tan_t+3*theta*cot_t-3)
check(sec2.hi < Q(25,4),"secant bound")
check(tan_t.hi < Q(12,5),"tangent bound")
check((theta*cot_t).hi < Q(11,20),"support bound")
check((1/sin_t).hi < Q(28,25),"cosecant bound")
check((1/sin_2t).hi < Q(67,50),"double cosecant bound")
check(w0.lo > Q(567,100) and w0.hi < 6,"w0 bounds")

S,T,U,C1,C2 = Q(25,4),Q(12,5),Q(11,20),Q(28,25),Q(67,50)
W = [S*(S*U+2*U+C2+2+2*C1)]
for j in range(1,4):
    W.append(S*(S*(U*T**j+Q(j,2)*T**(j-1))
                 +(1 if j==1 else 0)+(C2+2*C1)*T**j))
for j,bound in enumerate(W):
    check(bound < 1000,"derivative bound "+str(j))
check(W[2] < 350,"sharper second derivative")

# f>=f0 for u<=10: endpoint controls u^2/(1-exp(-a*u)).
eta = Q(3,400)
check(exp_lower(Q(49,5),30)>10000,"exponential 9.8 lower bound")
check(1000*eta**2*100 < Q(567,100)*Q(9999,10000),"positive initial segment")
check(exp_lower(Q(299,100),12)>19,"exponential 2.99 lower bound")
check(19**10>10**12,"exponential 29.9 lower bound")
check(exp_lower(Q(20),2)>2,"denominator tail bound")
tail = 3*Q(1,10**12)/(Q(299,100)*Q(1,2))
check(tail<Q(1,10**10),"E0 tail")

# Trigonometric polynomial is exactly a squared modulus.
c=[4,-8,2,20,-9,-34,27,91,-27,-201,32,895,1949,2389,1896,949,239]
ak=[Q(sum(c[j]*c[j+k] for j in range(17-k))*(1 if k==0 else 2),14912370)
    for k in range(17)]
check(ak[0]==1 and all(x>=0 for x in ak),"polynomial coefficient signs")
check(ak[1]==Q(865534,497079),"a1")
aa=sum(ak[1:])
check(aa==Q(2919857,828465),"a sum")
pi=16*atan_unit(Q(1,5))-4*atan_unit(Q(1,239))
check(Q(314159,100000)<pi.lo<pi.hi<Q(314160,100000),"Machin enclosure")
# gamma > H_N-log N-1/(2N), from the trapezoidal inequality for 1/x.
hn=sum((Q(1,j) for j in range(1,101)),Q(0))
gamma_lower=hn-log_rational(Q(100))-Q(1,200)
carch=1-gamma_lower/2-(1+aa/2)*LOG2-(1+aa)/2*log_interval(pi)
carch += sum((ak[k]/2*log_rational(Q(k)) for k in range(1,17)),I(0))
check(carch.hi < Q(-15063,5000),"Carch <= -3.0126")

# Negative controls are intentionally false versions of claimed conclusions.
negative_controls=0
for false_condition in [w0.lo>6, tail>Q(1,10**10), carch.lo>Q(-3), ak[0]==2]:
    if false_condition:
        raise RuntimeError("negative control unexpectedly accepted")
    negative_controls+=1

print(json.dumps({
    "status":"pass",
    "scope":"exact rational constants for logistic smoothing; no global zero-free theorem",
    "checks":checks,
    "negative_controls":negative_controls,
    "w0_interval_decimal":[float(w0.lo),float(w0.hi)],
    "derivative_bounds_rational":[str(x) for x in W],
    "E0_over_eta_upper_rational":str(tail),
    "Carch_upper_decimal":float(carch.hi),
    "Carch_certified_upper":"-3.0126"
},sort_keys=True))
