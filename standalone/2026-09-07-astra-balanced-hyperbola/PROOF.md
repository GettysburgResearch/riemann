# Balanced hyperbola inversion: exact main-term cancellation and the remaining arithmetic orientation

Status: proposed component proofs; independent mathematical review required.
**RH, uniform full-source block gain, and the near-linear quadratic bound remain unproved.**
This is an author continuation of PR #805 at
`ea66cd5b152e7960ad51ea51b154734eebc9b96a`, not an independent acceptance.

The underlying short-Mobius hyperbola identities are classical; in particular
Huxley--Watt (2018), equations (1.5)--(1.10), give a general hierarchy.
Here we reconstruct the identities with the parent's EXACT terminal balance,
including smoothing at the support boundary. This removes the entire pole main
term before any norm estimate. The resulting fixed compact kernel is small,
but its size does not give the needed bound on the literal arithmetic vector.
No novelty or priority is asserted for the classical ingredients.

## 0. Literal source and conventions

All Dirichlet convolutions in this note are on positive odd integers. Let
`u(n)=1`, let `e` be the convolution identity, and let `mu` be the ordinary
Mobius function restricted to odd integers. Thus `u*mu=e`. Write

\[
 M_o(x)=\sum_{n\le x,\ n\ \text{ odd}}\mu(n),\qquad
 m_o(x)=\sum_{n\le x,\ n\ \text{ odd}}\mu(n)/n,\qquad
 Q(x)=M_o(x)-x m_o(x) .                                      \tag{0.1}
\]
Set all three to zero below 1. In particular Q(1)=0. For an odd integer Y>=3,
let the finite source be

\[
 \lambda_{k,Y}=\mu(k)-Y m_o(Y){\bf1}_{k=Y},
 \quad k\le Y\text{ odd},                                   \tag{0.2}
\]
zero at other indices. Then

\[
 \lambda_{1,Y}=1,\quad\sum_k\lambda_{k,Y}/k=0,\quad
 \sum_k\lambda_{k,Y}=Q(Y).                                  \tag{0.3}
\]
The terminal correction is not omitted at nonsquarefree Y. For example
lambda_(9,9)=-102/35 although mu(9)=0.

For any finite sequence a, put

\[
 \mathcal Q_X(a)=\sum_{n\le X}a(n)(1-X/n).
\]
The weight at n=X is ZERO. This is essential in section 1. Coefficients of
all displayed finite objects come from divisor arithmetic, not from zeros.

We will use the elementary all-cutoff bound |m_o(x)|<=2. Indeed
sum_(n<=N) mu(n) floor(N/n)=1 gives |sum_(n<=N)mu(n)/n|<=1;
separating 2-adic valuations expresses the odd sum as
sum_(2^j<=N)2^(-j) sum_(n<=N/2^j)mu(n)/n. Consequently

\[
 |Q(x)|\le 3x\quad(x\ge1).                                \tag{0.4}
\]
These facts require neither PNT nor RH.

## 1. HP26.1 -- an exact balanced Newton hierarchy

Let L=lambda_(.,Y), and let b=e-u*L. Finite divisor inversion gives

\[
 b(n)=0\ (n<Y),\qquad b(Y)=Y m_o(Y).                       \tag{1.1}
\]
For every integer d>=1 define the locally finite arithmetic sequence

\[
 N_{d,Y}=\sum_{r=1}^d(-1)^{r-1}\binom dr\ u^{*(r-1)}*L^{*r}.
                                                                    \tag{1.2}
\]
Here u^(*0)=e. Formal multiplication in the Dirichlet convolution ring gives

\[
 u*N_{d,Y}=e-b^{*d},\qquad
 \mu-N_{d,Y}=\mu*b^{*d}.                                  \tag{1.3}
\]
Thus N_(d,Y)(n)=mu(n) for every n<Y^d. At the boundary itself,

\[
 \mu(Y^d)-N_{d,Y}(Y^d)=(Y m_o(Y))^d.                      \tag{1.4}
\]
Only the combination with n_1=...=n_d=Y can attain that first support point.
The coefficient at Y^d is generally NOT reproduced. Nevertheless

\[
 \boxed{Q(Y^d)=\mathcal Q_{Y^d}(N_{d,Y})}                  \tag{1.5}
\]
because its weight is zero. This proves the identity at the closed endpoint,
without extending a coefficient identity beyond its actual support domain.
All ring operations are coefficientwise finite; no infinite analytic Euler
product or inverse-operator convergence has been assumed.

For j>=1 define the elementary kernel

\[
 W_j(z)=\sum_{n\le z,\ n\ \text{ odd}}d_j(n)(z/n-1),
 \qquad d_j=u^{*j};                                      \tag{1.6}
\]
set W_j(z)=0 for z<1. The integer d_j(n) counts ordered j-tuples of odd
factors with product n. For j=1 this is simply

\[
 W(z)=z H_o(z)-C_o(z),\quad
 H_o(z)=\sum_{n\le z,\ n\ \text{ odd}}1/n,\quad
 C_o(z)=\#\{n\le z:n\text{ odd}\}.                        \tag{1.7}
\]
Insert (1.2) into (1.5) and exchange finite sums. Exact balance cancels the
X/k part of the r=1 term. The result is

\[
 \boxed{Q(Y^d)=d Q(Y)+\sum_{r=2}^d(-1)^r\binom dr
 \sum_{k_1,...,k_r\le Y\ \text{ odd}}
 \lambda_{k_1,Y}\cdots\lambda_{k_r,Y}
 W_{r-1}\left(\frac{Y^d}{k_1\cdots k_r}\right).}           \tag{1.8}
\]
The missing-prime range is not thrown away: it is encoded by the completely
specified divisor-count kernels. Only the Mobius INPUT range has shortened.
There is no claim that the number of arithmetic operations is Y or d.

At d=2 put

\[
 \mathcal B_Y=\sum_{a,b\le Y\ \text{ odd}}
 \lambda_{a,Y}\lambda_{b,Y}W(Y^2/(ab)).
\]
Then

\[
 \boxed{Q(Y^2)=2Q(Y)+\mathcal B_Y.}                        \tag{1.9}
\]
This is an exact formula for the parent's scalar at the squared cutoff,
using only its existing balanced vector at Y. Every cross term is included.

There is a second independent derivation, useful for checking signs. Let
v(n)=mu(n)1_(n<=Y). Since mu-v is supported above Y,
mu=2v-u*v*v+u*(mu-v)*(mu-v) gives, at X=Y^2,

\[
 Q(Y^2)=2(M_o(Y)-Y^2m_o(Y))+
        \sum_{a,b\le Y\ \text{ odd}}\mu(a)\mu(b)W(Y^2/(ab)).
\]
Also the exact row sum is
sum_(a<=Y odd) mu(a)W(Y/a)=Y-1, by u*mu=e. Substituting
lambda=v-Ym_o(Y)e_Y, using W(1)=0, reduces this to (1.9). In particular
none of the large linear terms is bounded separately and then lost.

## 2. HP26.2 -- all pole main terms vanish exactly

If c is any finite odd source with sum c_k/k=0, r>=2, X>0, and P is a
polynomial of degree at most r-1, then

\[
 \sum_{k_1,...,k_r}c_{k_1}\cdots c_{k_r}
 \frac{X}{k_1\cdots k_r}
 P\left(\log\frac{X}{k_1\cdots k_r}\right)=0.             \tag{2.1}
\]
Expand the polynomial. Each monomial has total log degree less than r, so
at least one of the r index sums contains no log factor; it is sum c_k/k=0.
This is an algebraic identity, not an estimate for an oscillating sum.

For context, writing Z_o(s)=(1-2^(-s))zeta(s), absolute convergence gives

\[
 \int_1^\infty W_j(z)z^{-s-1}dz
 =\frac{Z_o(s)^j}{s(s-1)}\quad(\Re s>1).                  \tag{2.2}
\]
At s=1 the pole has order j+1. Its residue term is z times a polynomial in
log z of degree j. For j=r-1 that entire term is annihilated by (2.1).
We do NOT replace W_j by this term, nor assume the remainder is small.

For the quadratic kernel the main term is explicit. With gamma denoting
Euler's constant, define, for z>=1,

\[
 R(z)=W(z)-\tfrac z2(\log z+\gamma+\log2-1).
\]
Then every balanced finite source satisfies

\[
 \boxed{\sum_{a,b}c_ac_bW(Y^2/(ab))
       =\sum_{a,b}c_ac_bR(Y^2/(ab)).}                     \tag{2.3}
\]
All indices here are odd and <=Y, so every argument is >=1. Although R
uses gamma and logs, the quadratic form (2.3) is RATIONAL for rational c,
as is manifest on its W side. No transcendental evaluation is needed to
compute the exact scalar.

## 3. HP26.3 -- a uniform remainder and a genuinely small continuum operator

For every real z>=1,

\[
 \boxed{-\frac{3}{8z}<R(z)<\frac{3}{16z},\quad
        |R(z)|<\frac{3}{8z}.}                            \tag{3.1}
\]

Proof. Set m=floor((z+1)/2), so C_o(z)=m and -1<2m-z<=1. The standard
digamma integral, subtracted from Frullani's integral for log m, gives

\[
 \psi(m+\tfrac12)-\log m
 =\int_0^\infty e^{-mt}
   \left(\frac1t-\frac1{2\sinh(t/2)}\right)dt.
\]
The integrand's bracket lies strictly between 0 and t/24. To prove the
upper bound, put v=t/2. For v>=sqrt(6) it follows from 1/v<=v/6. For
0<v<sqrt(6), use (2j+1)!>=6^j in the power series to obtain
sinh(v)<=v/(1-v^2/6), and rearrange. Integration therefore proves

\[
 H_o(z)=\tfrac12\log(2m)+\tfrac12(\gamma+\log2)+r_m,
 \qquad 0<r_m<1/(48m^2).                                 \tag{3.2}
\]
This also follows from the midpoint harmonic-sum remainder. No zero or
prime-distribution input occurs.

Put v=(2m-z)/z. It belongs to (-1/3,1]. For v in this interval,
0<=v-log(1+v)<=3v^2/4. For v>=0 integrate t/(1+t)<=t; for v<0 integrate
t/(1-t)<=3t/2 over 0<=t<=|v|. Now

\[
 R(z)=\tfrac z2(\log(1+v)-v)+z r_m.
\]
The first term is between -3/(8z) and 0; the second is between 0 and
3/(16z), because z<2m+1<=3m. This proves (3.1).

Define the symmetric kernel on the unit square by

\[
 \mathcal R(u,v)=R(1/(uv))\quad(u,v>0),\qquad
 \mathcal R(u,0)=\mathcal R(0,v)=0.
\]
W is continuous at its odd breakpoints, and (3.1) makes this extension
continuous. The associated integral operator on L2(0,1) is compact,
self-adjoint, and Hilbert--Schmidt, with

\[
 \boxed{\|\mathcal R\|_{\rm op}\le\|\mathcal R\|_{\rm HS}
       \le\tfrac18.}                                    \tag{3.3}
\]
Indeed |mathcal R(u,v)|<=3uv/8 and the square integral of u*v is 1/9.

THIS IS NOT A CONTRACTION RECURRENCE FOR Q. The finite arithmetic form is
not a normalized continuum L2 pairing. Its discrete matrix R_Y has

\[
 \|R_Y\|_{\ell^2\to\ell^2}
 \le\frac{3}{8Y^2}\sum_{a\le Y,\ a\ \text{ odd}}a^2
 =\frac{(Y+1)(Y+2)}{16Y}.                                \tag{3.4}
\]
The identity sum_odd a^2=Y(Y+1)(Y+2)/6 and a rank-one absolute majorant
prove (3.4). The unweighted matrix norm grows linearly, rather than being
bounded by 1/8. Discretization normalization and the source mass matter.

For the uncorrected short Mobius vector, its actual diagonal contribution
is bounded by (Y+1)(Y+2)/(16Y)=O(Y). This does not include its off-diagonal
terms or the terminal-normalization correction. For the complete terminal
vector, (3.1) gives only

\[
 |\mathcal B_Y|\le\frac3{8Y^2}
 \left(\sum_a a|\lambda_{a,Y}|\right)^2<4Y^2.              \tag{3.5}
\]
Here sum a|lambda| <= (Y+1)^2/4+2Y^2<3Y^2 for Y>=3. Thus the fully
source-preserving elementary estimate still has the wrong power.

## 4. HP26.4 -- explicit, bounded balanced sources defeat a uniform norm shortcut

The following examples are NOT the actual Mobius vector. They test the
proposed general inference from balance, coefficient bounds and the small
kernel norm to a near-linear quadratic bound.

Fix an integer L>=1 and Y=200L+1. All indices below are odd. Let c^+ have
c_a=a/Y at a=110L+2r+1, and c_b=-b/Y at b=130L+2r+1, for 0<=r<L;
let c^- instead use the two blocks 150L+2r+1 and 180L+2r+1. Both obey

\[
 \sum_a c_a/a=0,\quad |c_a|<1,\quad
 \#\operatorname{supp}(c)=2L.
\]
For the quadratic form B_Y(c)=sum c_a c_b W(Y^2/(ab)), one has EXACTLY

\[
 \boxed{B_Y(c^+)=\frac{L^2}{3}-\frac{12721L^4}{Y^2}
       >\frac{1837}{120000}L^2>0,}
\]

\[
 \boxed{B_Y(c^-)=-\frac{900L^4}{Y^2}<0.}                 \tag{4.1}
\]
In particular both signs can have magnitude bounded below by a positive
constant times Y^2 as L grows. There is no universal O(Y times a fixed
power of log Y) estimate for bounded balanced sources.

Proof. For c^+, the lower-lower products lie strictly between Y^2/5 and
Y^2/3; all other products lie between Y^2/3 and Y^2. Thus W includes
r=1,3 on the first square and r=1 elsewhere. The r=1 contribution is
-(sum c)^2, by balance. The extra r=3 contribution is
L^2/3-(sum_lower a/Y)^2. The lower and upper sums of indices are 111L^2
and 131L^2, giving (4.1). Since Y>200L the lower bound follows. For c^-,
all products exceed Y^2/3, so only r=1 contributes; the difference of its
index sums is -30L^2, proving its formula. These region inequalities are
polynomial inequalities valid at every L>=1, not sampled phase claims.

One can also retain the parent's first-cell normalization. Add d_1=1,
d_3=-3 to either c. Then sum (d+c)_a/a=0, (d+c)_1=1, and |(d+c)_a|<=3.
Equation (3.1) bounds the change of quadratic form by less than 8:
sum a|d_a|=10 and sum a|c_a|<=Y^2 give at most 15/2 for both mixed terms,
plus 75/(2Y^2) for the d--d term. Both quadratic signs persist for L>=33.
Consequently the correct first-cell condition also does not repair this
source-blind estimate. Nothing here bounds or refutes the special Mobius
orientation in (0.2).

## 5. HP26.5 -- the precise end-to-end arithmetic target

There is a complete conditional chain from a NEAR-LINEAR bound on the
actual quadratic form to RH. It does not require a uniform block gain.
For example put Y_j=2j^2+1 and X_j=Y_j^2. Then

\[
 \boxed{\mathrm{RH}\ \Longleftrightarrow\
 \forall\epsilon>0:\quad
 |\mathcal B_{Y_j}|=O_\epsilon(Y_j^{1+\epsilon}).}          \tag{5.1}
\]
All cutoffs are fixed in advance. In particular (5.1) is not an assertion
about some subsequence selected after inspecting small values.

Here are the details, including the only conditional analytic import.
From (1.9) and (0.4), the right side implies
Q(X_j)=O_epsilon(X_j^(1/2+epsilon)). The exact interpolation identity for
odd integer endpoints a,b is

\[
 Q(x)-\ell(x)=\sum_{a<k<b,\ k\ {\rm odd}}\frac{\mu(k)}k
 \frac{(\min(x,k)-a)(b-\max(x,k))}{b-a},
 \quad |Q(x)-\ell(x)|\le\frac{(b-a)^2}{8a},              \tag{5.2}
\]
where ell is the line through Q(a),Q(b). Both sides have identical endpoint
values and distributional second derivatives. For consecutive X_j,
X_(j+1)/X_j<=9 and X_(j+1)-X_j<=72j^3; since X_j>=4j^4, the interpolation
error is at most 81 sqrt(x). Thus Q(x)=O_epsilon(x^(1/2+epsilon)) globally.

Absolute convergence initially to the right of 1 gives

\[
 \int_1^\infty Q(x)x^{-s-1}dx
 =-\frac1{s(s-1)(1-2^{-s})\zeta(s)}.                     \tag{5.3}
\]
The proposed bound makes the integral holomorphic for Re s>1/2. Multiplying
by its displayed denominator and applying the identity principle excludes
every zeta zero there. No nontrivial zero cancels any numerator. Reflection
then gives RH. This forward implication uses no RH assumption.

For the converse we explicitly import the classical Littlewood implication
RH => M(x)=O_epsilon(x^(1/2+epsilon)). Odd 2-adic decomposition, convergence
of the harmonic reciprocal series to zero at s=1, and partial summation
give Q(x)=O_epsilon(x^(1/2+epsilon)). Equation (1.9) proves (5.1). This
import is conditional on RH, and is not an unproved input to an unconditional
claim. The parent contains the same analytic boundary in sections 5--6.

The new unproved assertion is therefore the bound in (5.1) for the LITERAL
vector (0.2). General positivity, balance, the norm (3.3), and diagonal
control do not imply it; (4.1) rules out those source-blind shortcuts.

## 6. HP26.6 -- a genuine critical-scale lower obstruction

The sampled actual quadratic form is not expected to stay at its tiny
finite-cutoff values. On ALL odd Y, one has unconditionally

\[
 \boxed{1\le\limsup_{Y\to\infty,\ Y\ \text{ odd}}
 \frac{\log(1+|\mathcal B_Y|)}{\log Y}\le2.}              \tag{6.1}
\]
More generally each zero with real part beta>=1/2 forces the lower limsup
to be at least 2beta. Existence of a critical-line zero is the classical
input for the lower bound 1; no location, simplicity, or zero table is used.

Proof. Suppose |B_Y|=O(Y^b) on all odd Y for some 0<b<2. Between consecutive
odd squares Y^2 and (Y+2)^2, (5.2) has error at most 32/9<4. If
Q(x)=O(x^a) for a>0, (1.9) then yields

\[
 Q(x)=O(x^{\max(a,b)/2}).                               \tag{6.2}
\]
Start with a=1 from (0.4). Finite iteration of (6.2) gives
Q(x)=O(x^(b/2)). A zero with real part greater than b/2 now contradicts
(5.3). Choosing b strictly between the hypothesized limsup exponent and
2beta proves the lower bound, including beta=1/2. The upper bound follows
from (3.5). Thus an eventual O(Y^(1-epsilon)) bound, in particular an O(1)
bound suggested by a small finite panel, is FALSE even if RH holds.

For the coarser grid Y_j=2j^2+1, the same argument from section 5 excludes
b<2beta for beta>1/2; it does not establish the lower bound 1 on that
coarser grid, because its interpolation error already has square-root size.
No liminf conclusion or arbitrary-subsequence assertion is made.

## 7. Attempted closure and what has NOT been achieved

The attempted closing mechanism was to use a small, scale-independent
kernel after removing its dominant pole directions. Equations (1.9) and
(2.3) remove those directions EXACTLY with the existing terminal balance;
(3.3) proves the genuinely small continuum norm. But (3.4) prices the
arithmetic sampling correctly, and the explicit sources (4.1) show that
balance and bounded coefficients still permit quadratic growth of either
sign. The attempted generic contraction is therefore invalid.

The exact arithmetic orientation (0.2) is far more constrained than those
counterexamples. No proof of its near-linear bound has been found here.
The all-order Newton identity also contains large alternating tensor terms;
no norm convergence as d grows is established, and no termwise absolute
estimate is promoted to cancellation. The scalar is now accessible from a
square-root-range source, but this is NOT an analytic square-root saving.

The positive completed result is a source-exact balanced hyperbola hierarchy,
a full main-term cancellation, and a bounded remainder with an explicit
spectral obstruction. Its conditional RH route is complete; its arithmetic
upper estimate remains open. Finite tests validate arithmetic identities,
not the analytic proofs, a uniform estimate, or RH.
