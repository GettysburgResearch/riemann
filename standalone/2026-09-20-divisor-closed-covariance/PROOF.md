# DCN26: divisor closure and near-integer-ratio covariance

**Proposed component proofs for independent review. No bound for the full
remaining native covariance and no RH/GRH proof is asserted.** Parent:
`530cc8f706b1f1e3dc7aff77efdced82e4ac73ad`, PR #903. This packet keeps TWO
observables distinct: PET26's physical prime transport, and PCR26/RCB26's
actual centered-harmonic Newton covariance. Theorems below are proved in the
kernel named in each theorem. Classical convolution, divisor estimates and
the RCB26 overlap estimate are credited, not claimed as new general tools.

## 1. Divisor-comparable closure changes the sign of the old matched sector

Let nonnegative real weights a_p be assigned to primes, and let
h(p)=a_p, h(n)=0 otherwise. All expressions can be truncated at a finite
observation endpoint, so no convergence assumption is needed. Set

$$A=h*\mu,\quad A_x=\sum_{n\le x}A(n),\quad M(x)=\sum_{n\le x}\mu(n).$$

For b>=2, X=b^2, N=X-1, write

$$w_b(n)=\left(\frac1{\max(b,n)}-\frac1X\right)_+.$$

The physical prime transport is exactly

$$P_b(a)=\sum_{m,t\le N}\mu(m)A(t)w_b(\max(m,t))
 =\sum_{p\le N}a_p\int_b^X M(x)M(x/p)\frac{dx}{x^2}.\tag{1}$$

The original PET26 observable is a_p=log p. Coalescing t=pn does not lose
sign information here. If t is squarefree, all nonzero summands of A(t)
have the same sign; if t=p^2 r with r squarefree and p not dividing r,
there is just one. More explicitly,

$$A(t)=-\mu(t)\sum_{p\mid t}a_p\quad(t\text{ squarefree},t>1),$$
$$A(p^2r)=-\mu(r)a_p,\quad p\nmid r,\quad r\text{ squarefree},\tag{2}$$

and A vanishes elsewhere. In particular, for a_p=log p, |A(t)|<=log t.

Call (m,t) comparable if m divides t or t divides m, including the diagonal
ONCE. Let P_div be (1) restricted to these pairs.

**DCN26-1 (exact favorable closure).** For every choice of nonnegative
prime weights,

$$\boxed{P_{\rm div}(a)=
 \sum_{\substack{n\le N\;\text{squarefree}\ n\text{ composite}}}
 \left(\sum_{p\mid n}a_p\right)w_b(n)\ \ge0.}\tag{3}$$

In fact the assertion holds before integration, at every real cutoff x:
the comparable part of M(x)A_x equals the corresponding sum over n<=x.
It therefore holds against ANY nonnegative observation measure, not just
one square annulus. Prime weights may select an arbitrary prime interval.

Proof. The entire orientation m|t, including m=t, sums to

$$\sum_{t\le x}A(t)\sum_{m\mid t}\mu(m)=0,\tag{4}$$

because 1*mu=delta and A(1)=0. This is a sum of COMPLETE divisor fibres:
every divisor is <=t, so the cutoff and the max-kernel do not split a fibre.
The other orientation is t|m with t<m. Since 1*A=h,

$$\sum_{m\le x}\mu(m)\sum_{\substack{t\mid m\\t<m}}A(t)
 =\sum_{m\le x}\mu(m)[h(m)-A(m)].\tag{5}$$

Only squarefree m matter. For prime m the summand is zero. For squarefree
composite m, (2) makes it sum_{p|m}a_p. This proves the pointwise identity
and then (3) after integration. QED.

**Relation to STC26, not a change of observable.** For its empty bank, the
old transport-matched condition is m=sf(t), since m is squarefree. This
always has m|t. Thus EVERY old matched negative term is contained in the
zero orientation (4). The additional native divisor terms cancel them
exactly. The reverse proper orientation (5) is nonnegative. We have not
bounded only an unrelated sector or discarded the negative matched mass.

For a_p=log p,

$$P_{\rm div}=\sum_{\substack{n<X,\ \mu(n)^2=1\\n\text{ composite}}}
 \log n\,w_b(n)\le\tfrac32(\log b)^2.\tag{6}$$

Indeed the counting numerator at x is at most x log x. Elementary
squarefree counting and Chebyshev's theta(x)=O(x) also give

$$P_{\rm div}=\frac9{\pi^2}(\log b)^2+O(\log b).\tag{7}$$

For details, mu(n)^2=sum_{d^2|n}mu(d) gives
sum_{n<=x}mu(n)^2=(6/pi^2)x+O(sqrt x). Partial summation gives its
log-weighted version (6/pi^2)(x log x-x)+O(sqrt x log x). Integrate on
[b,b^2]; removing the prime contribution costs O(log b). No PNT error or
RH hypothesis is used. Formula (3), not the asymptotic, is the main result.

## 2. A further disjoint family of EXACTLY zero incomparable blocks

Let t=p^2 r have nonzero A(t) in (2), and write R=rad(t)=pr. For any
squarefree k with

$$2\le k\le p,\qquad (k,R)=1,$$

take the complete fibre

$$\mathcal F(t,k)=\{(m,t):m=kd,\ d\mid R\}.\tag{8}$$

Every m is <=kR<=pR=t. The common kernel is w_b(t), and

$$\sum_{(m,t)\in\mathcal F(t,k)}\mu(m)A(t)w_b(t)
 =\mu(k)A(t)w_b(t)\sum_{d\mid R}\mu(d)=0.\tag{9}$$

These fibres are disjoint: the part of squarefree m outside R is the
unique k=m/gcd(m,R). They do not overlap the comparable sector because
k>1 has a prime outside t, and m<=t. Thus they can be removed as WHOLE
zero blocks, without changing (1). For example t=75, k=2 gives
m=2,6,10,30; their signs -,+,+,- sum to zero.

The endpoint k=p is harmless (usually excluded by coprimality). Extending
k beyond p without checking kd<=t is NOT justified: the cutoff can split
the divisor fibre. Neither an antichain assertion nor an average supplies
this exact cancellation. The executed packet tests this boundary.

## 3. Near-integer-ratio transport: a polylogarithmic absolute budget

For 1<=d<e define the canonical signed nearest-multiple remainder r by

$$e=q d+r,\qquad -d/2<r\le d/2,\tag{10}$$

with the positive remainder chosen at a tie. Let rho(d,e)=|r|. Given an
integer H>=0, after removing ALL comparable pairs and ALL complete zero
fibres (8), retain remaining pairs with rho(min(m,t),max(m,t))<=H.
Call their signed transport P_near,H and their absolute original-triple
envelope B_near,H. Keep the two orientations separately for the absolute
sum; do not take the absolute value of their sum.

**DCN26-2.** For the log-prime weights,

$$\boxed{|P_{\rm near,H}|\le B_{\rm near,H}
 \le 8H\log N\,H_{N+H}^2.}\tag{11}$$

Here H_n denotes a harmonic number. The statement is zero when H=0.
It remains valid on ANY subset of the selected triples.

Proof. For e=max(m,t), the kernel is at most 1/e. By (2), the absolute
coalesced weight for each orientation is at most log e. The prime terms
within A(t) have a common sign, so this is also an absolute TRIPLE bound.
For fixed nonzero r with |r|<=H, any possible smaller coordinate d divides
e-r. The number of choices is at most tau(e-r). Since |r|<=d/2<e/2,
1/e<=2/(e-r), and e-r<=N+H. Thus, including both orientations,

$$B_{\rm near,H}\le
 2\log N\sum_{0<|r|\le H}\sum_e\frac{\tau(e-r)}e
 \le 8H\log N\sum_{n\le N+H}\frac{\tau(n)}n
 \le8H\log N H_{N+H}^2.$$

Dropping the comparable and zero-fibre restrictions only increases the
positive majorant. The last inequality follows by expanding tau=1*1 and
enlarging the product-restricted harmonic double sum. QED.

Let P_far,H be the exact remainder after these ordered removals. Then

$$P_b=P_{\rm div}+0+P_{\rm near,H}+P_{\rm far,H},$$
$$\boxed{(-P_b)_+\le8H\log N H_{N+H}^2+(-P_{\rm far,H})_+.}\tag{12}$$

For fixed H this costs O(log^3 X); for H=X^{o(1)} it costs X^{o(1)}.
The FAR native negative part remains OPEN. Zero fibres can have points on
both sides of the near/far division, so they MUST be removed whole first.
The computation uses that priority, rather than declaring arbitrary pieces
of a zero fibre to be zero.

## 4. Direct control in the ORIGINAL harmonic Newton covariance

This is a separate theorem in the original PCR26/RCB26 kernel, not a
transfer of the signs in (3). Let |c(n)|<=K, c supported on [1,L], D=L^2,
and let z=c*c, coalescing equal products. For integer k>=1 set

$$K_d(k)=\frac{H_{\lfloor k/d\rfloor}-H_k+\log d}{d},\qquad
 Q(k)=\sum_{d\le D}z(d)K_d(k).\tag{13}$$

Products d above the observation endpoint are NOT zero in (13). No moment
condition is needed for this theorem. For the ordered near-ratio pairs put

$$\mathcal B_H=2\sum_{1\le d<e\le D\atop\rho(d,e)\le H}
 |z(d)z(e)|\sum_{k\ge1}|K_d(k)K_e(k)|.\tag{14}$$

Thus it dominates the absolute values of both signs of this entire
covariance sector on EVERY finite or infinite set of observation integers.

**DCN26-3.** For any integer H>=0,

$$\boxed{\mathcal B_H\le128K^4(2H+1)(1+\log D)^2 H_{D+H}^7.}\tag{15}$$

For exact multiples alone one has the sharper bound

$$\boxed{\mathcal B_0\le64K^4(1+\log D)^2 H_D^6.}\tag{16}$$

This controls arbitrary quotients q, including quotients with arbitrarily
many prime factors and primes far beyond every small bank. H=1 also covers
all consecutive product indices e=d+1; it is not a parity-core restriction.
For H=D^{o(1)} (15) is subpower. For fixed H it is O_K(log^9 D), and (16)
is O_K(log^8 D). No best-possible log exponent is claimed.

### 4.1 The complete kernel bound used, credited to RCB26

For 1<=d<=e, RCB26 proves

$$\sum_{k\ge1}|K_d(k)K_e(k)|\le
 \frac{32(1+\log(e/d))^2}{e}.\tag{17}$$

Here is the derivation used by this packet. Put
r(t)=H_floor(t)-log t-gamma. Harmonic integral inequalities give
|r(t)|<=1/t for t>=1 and |r(t)|<=log(1/t)+1 for 0<t<1. Consequently
|K_d(k)|<=(log(d/k)+2)/d when k<d and <=2/k when k>=d.
Put u=log(e/d), and split at d,e. The three absolute sums are bounded by
(3u+10)/e, (u^2+6u+4)/e, and 8/e respectively. The first follows from
integrating the decreasing function (-log t+2)(u-log t+2) on (0,1);
the second from its first discrete summand and its integral; the last
from sum_{k>=e}k^-2<=2/e. Their sum is at most 32(1+u)^2/e.
This also proves convergence of the ENTIRE tail in (17).

### 4.2 Shifted divisor sums, not a shifted-Mobius assumption

The elementary coefficient bound is |z(d)|<=K^2 tau(d). Fix r from (10).
Sum over d|e-r, enlarging the divisor set. Since sum_{d|n}tau(d)=tau_3(n),
(17) gives

$$\mathcal B_H\le64K^4(1+\log D)^2
 \sum_{|r|\le H}\sum_{e\text{ admissible}}
 \frac{\tau(e)\tau_3(e-r)}e.\tag{18}$$

Weighted Cauchy--Schwarz bounds the inner sum by

$$\left(\sum_{e\le D}\frac{\tau(e)^2}e\right)^{1/2}
 \left(\sum_{e\text{ admissible}}\frac{\tau_3(e-r)^2}e\right)^{1/2}
 \le\sqrt2\,H_{D+H}^{13/2}.\tag{19}$$

Indeed tau^2<=tau_4 and tau_3^2<=tau_9. At each prime these inequalities
follow by mapping a nonnegative 2x2 or 3x3 matrix of exponents to its row
and column sums: every pair of prescribed margins has at least one matrix.
Also sum_{n<=T}tau_j(n)/n<=H_T^j by a harmonic j-fold product. The shifted
sum uses 1/e<=2/(e-r), which was verified in (10), not presumed uniformly
for arbitrary shifts. Now 64sqrt(2)<=128 and H_{D+H}>=1 prove (15).
For r=0, tau(e)tau_3(e)<=tau_6(e), proving (16) directly.

These estimates do NOT assume cancellation in shifted Mobius sums and do
not claim to prove Chowla-type estimates. They are valid for every bounded
source c. Source-specific structure is essential later, for the remaining
uncontrolled covariance, and in Theorem 1 above.

## 5. Exact combination with RCB26 and the existing energy consumer

For a bank S, write a_S(d) for the parity core outside S and let

$$D_S=\sum_a\left\|\sum_{a_S(d)=a}z(d)K_d\right\|_I^2.$$

First retain the RCB26 within-core sector. Add the near-ratio pairs ONLY
when a_S(d)!=a_S(e), avoiding overlap. Let C_near be this additional ordered
covariance and C_far the rest. Then, in this SAME harmonic norm,

$$\|Q\|_I^2=D_S+C_{\rm near}+C_{\rm far},$$
$$D_S\le B_S^{\rm RCB},\qquad |C_{\rm near}|\le\mathcal B_H.\tag{20}$$

This does NOT assert the geometric set is an equivalence relation, or
that its signed sum is positive semidefinite. It is a disjoint partition
of matrix entries, with a separately proved absolute envelope.

For the native capped completion, let b=Y+1, B=b^2-1,
m(k)=sum_{n<=k}mu(n)/n, m_c(k)=sum_{n<=k}c(n)/n. Inherited PCR26 gives

$$F_Y=\sum_{k\le Y}m(k)^2,\quad
 T_Y=\sum_{k=b}^B m_c(k)^2\le F_Y,\quad Q(k)=2m_c(k)-m(k).$$

Hence the COMPLETE innovation update is

$$F_B=F_Y+4T_Y-4\langle m_c,Q\rangle+\|Q\|^2
 \le9F_Y+2\|Q\|^2$$
$$\boxed{F_B\le9F_Y+2(B_S^{\rm RCB}+\mathcal B_H)+2C_{\rm far}.}\tag{21}$$

No completion mean has been dropped: this is the established one-moment
innovation state. The full physical two-moment A state and both signed means
are separately replayed in transport_result.json. They are not numerically
identified with the harmonic Gram diagonal.

Equation (21) shows the exact remaining upper-bound task. With a subpower
bank and H=D^{o(1)}, BOTH displayed budgets are subpower. A native subpower
upper bound for C_far would feed the existing cofinal energy argument.
**No such bound is proved here.** The comparable transport sign (3) cannot
be inserted as a sign statement for harmonic C_near: those are different
observables. The finite data indeed show different signs.

## 6. Falsification and scope

The divisor closure is genuinely native. For a general source a and
A=h*a, put d=1*a. Its comparable sector is exactly

$$\sum_n w_b(n)\{A(n)d(n)+a(n)(h*d)(n)-a(n)A(n)\}.\tag{22}$$

Replacing d by delta is allowed for mu, not for an arbitrary twist or
an elliptic reciprocal. The all-minus consistent sign twist gives a=mu^2
and negative prime weights; even the first prime gives a negative comparable
sector. A signed source with a(1)=1,a(2)=-2 and positive h(2)=1 also gives
-1 at cutoff 2, refuting a generic-source version even with nonnegative
prime weights. LFAMILY.md provides the actual E_17 good-prime instance.

Native finite far remainders are reported with their observed signs; none
is promoted to a theorem. Increasing H need not improve a SIGNED remainder.
The absolute envelopes here are deliberately conservative and do not prove
sharp finite constants. This is broader, correctly located component control,
not a completed solution of the native covariance problem.
