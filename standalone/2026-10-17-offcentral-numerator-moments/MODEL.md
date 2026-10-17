# Exact ceiling of the present positive estimate catalogue

This is an optimization statement about the DISPLAYED UPPER ESTIMATES, not a
lower bound on I, an optimality theorem for the arithmetic, or a no-go for RH.
No negative conclusion about a different source/correction/signed estimate is
inferred. It also does not imply that every limiting parameter is legal.

## 1. Allow asymmetric scales as well

Put X=Z^alpha, Y=Z^beta, alpha,beta>0, M=alpha+beta. The original detector
normalization is b=5/6-alpha/3. The reconstructed reflected square and additive
square give the exponent

    T_theta=[max(M,2M-1)-min(alpha,beta)]/2.               (1)

For M<=1 this is max(alpha,beta)/2. Thus the optimization must retain both
scales; simply interchanging X,Y or varying only one is not an escape.

The nonexceptional family has only its full U row-count bound in the current
catalogue. The best available absolute numerator costs here are r(y)=1 for
y>=1/2 and r(y)=3/2-y for 0<y<1/2. The second mean on the reflected line gives
these; the off-central higher means agree when the count exponent is nu=1.
At the effective upper frequency exponent 1-alpha the good-class cost is

    G=x-1+alpha/2+beta(y-1)+(1-alpha)r(y).                (2)

For M<=1, the unchanged correction domain x>2/3 and 3x+y>5/2 forces

    G>2/3-M/2.                                         (3)

Indeed for y>=1/2 the difference from the right side, after using x>=2/3,
is beta(y-1/2)>=0. For y<1/2 use x>5/6-y/3; the difference is
(M-4/3)(y-1/2)>0. Strict margins can approach zero but may not be erased
inside an analytic application.

## 2. Minimize the complete two-cost model

The limiting boundary issued by this catalogue is at least

    B=5/6-alpha/3+max(max(alpha,beta)/2,2/3-M/2).          (4)

If beta<=alpha, (4) is bounded below by the maximum of

    5/6+alpha/6,   3/2-4alpha/3.

Their intersection is alpha=4/9, with value 49/54. If beta>=alpha and
alpha>=4/9, its first term is at least 5/6+alpha/6>=49/54. If beta>=alpha
and alpha<=4/9, average the two lower bounds

    5/6-alpha/3+beta/2,   3/2-5alpha/6-beta/2.

Their average is 7/6-7alpha/12>=49/54. This proves B>=49/54 in every
subcritical or boundary case, including asymmetric scales.

For M>1, theta alone gives a boundary strictly greater than 11/12. If
beta<=alpha, it is 1/3+2alpha/3+beta/2 >5/6+alpha/6>11/12. If beta>=alpha,
it is 1/3+alpha/6+beta=1/3+M/6+5beta/6>11/12. Thus supercritical asymmetry
cannot improve the catalogue's minimum either.

PROOF.md supplies fifteen legal classes approaching 49/54 with fixed positive
e, at alpha=beta=4/9. The theta, good-class, and principal z-remainder costs
tie in the limit. The off-central moments bring every exceptional class below
them, so the displayed family of estimates reaches its own limiting optimum.

## 3. What a genuinely further step must alter

More density bins or higher numerator moments alone, with the same full good-
family cost and the same correction domain, cannot improve (4). Better bounds
for sparse exceptional rows are not the binding issue at this point.

A plausible next analytic target is the treatment of H_u at primes dividing u.
CT Section 11.1 bounds its local shells by taking separate absolute values;
this imposes x>2/3 and 3x+y>5/2. One would have to re-evaluate the ACTUAL local
coefficient relations, or a weighted sum retaining H_u and the numerator,
rather than simply discarding those domain conditions. Another option is a
stronger signed physical pairing, avoiding the binding Cauchy estimate. Neither
extension is proved here. Both would change a binding hypothesis in (4), unlike
another optimization of the same scalar inequalities.
