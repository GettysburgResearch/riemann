# Correlation uniformity, the native arithmetic source, and a multiplicative firewall

Status: **PROPOSED elementary lemmas; independent review requested.**

Scope: exact finite correlation identities, quantitative summatory implications,
and an explicit bounded completely multiplicative countermodel. The countermodel
is not Möbius or Liouville and does not contradict a theorem about either source.

Exact dependencies: elementary Cauchy--Schwarz; the classical Chebyshev bounds
`psi(y)<=C y` and `pi(y)>=c y/log y`; and Mertens' prime harmonic estimate
`sum_(p<=y) 1/p=log log y+O(1)`. These classical estimates are unconditional.
The analytic fixed-SHARP adapter is `../arithmetic/ZERO_FREE_MERTENS.md`.

Motivation: OpenAI family 007, frozen at
`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`, proves logarithmic savings for
fixed affine Liouville correlations and a qualitative general Elliott theorem.
The precise source and growing-shift bottlenecks are recorded in
`../literature/TWO_POINT_ARCHITECTURE.md`. No growing-shift or power-saving
estimate is imported from that paper.

## 1. A finite identity that prices every shift

Let `a_1,...,a_N` be complex numbers with `|a_n|<=1`, extended by zero off
`{1,...,N}`. For integers `1<=H<=N`, define

\[
 S_N=\sum_{n=1}^N a_n,\qquad
 C_N(d)=\sum_{n=1}^{N-d}a_{n+d}\overline{a_n}.
\]

The zero extension and both endpoints are part of the source. Put
`B_j=sum_(h=0)^(H-1) a_(j-h)` for `1<=j<=N+H-1`. Every a_n occurs exactly
H times, so `sum B_j=H S_N`. Expanding before taking absolute values gives

\[
 \sum_{j=1}^{N+H-1}|B_j|^2
 =H\sum_{n=1}^N|a_n|^2
       +2\operatorname{Re}\sum_{d=1}^{H-1}(H-d)C_N(d).       \tag{C1}
\]

Each pair of indices at distance d belongs to exactly H-d windows. Hence
Cauchy--Schwarz proves the fully signed inequality

\[
 |S_N|^2\le\frac{N+H-1}{H^2}
 \left[H\sum|a_n|^2+
       2\operatorname{Re}\sum_{d=1}^{H-1}(H-d)C_N(d)\right]. \tag{C2}
\]

Define `A_H=(2/H^2)sum_(d=1)^(H-1)(H-d)|C_N(d)|`. A weaker, convenient
consequence is

\[
 |S_N|^2\le(N+H-1)[N/H+A_H].                         \tag{C3}
\]

If H has size N^delta and `A_H=O_epsilon(N^(1-eta+epsilon))`, where
`0<delta<=1` and `0<eta<=1`, then

\[
 S_N=O_\epsilon\left(N^{1-\min(\delta,\eta)/2+\epsilon}\right). \tag{C4}
\]

The constants and quantifiers must be uniform over the shifts used at that
N. Separate fixed-shift estimates do not provide this contract. Even a
square-root absolute correlation bound (`eta=1/2`) supplies only the
three-quarter summatory exponent through this inequality. The signed sum
in (C2) can be much smaller than its absolute counterpart; preserving it is
a concrete route to a stronger estimate.

## 2. Literal Liouville-to-Möbius-to-SHARP transfer

Let `L(X)=sum_(n<=X) lambda(n)` and `M(X)=sum_(n<=X) mu(n)`. The exact
square-divisor identity, including nonsquarefree integers, is

\[
 \mu(n)=\sum_{d^2\mid n}\mu(d)\lambda(n/d^2),\qquad
 M(X)=\sum_{d\le\sqrt X}\mu(d)L(X/d^2).             \tag{C5}
\]

Indeed, complete multiplicativity gives `lambda(n/d^2)=lambda(n)`, and
`sum_(d^2|n) mu(d)` is the squarefree indicator. For any fixed
`1/2<=theta<1`, a bound `L(X)=O_epsilon(X^(theta+epsilon))` therefore gives
`M(X)=O_epsilon(X^(theta+epsilon))`: choose an internal positive epsilon,
then bound the convergent sum `sum d^(-2theta-2epsilon)`. At theta=1/2 this
step retains that positive epsilon; it does not assert an endpoint bound.

The fixed repository source has prefix
`M_beta(X)=M(X)-M(X/67)`, with both terms retained. Partial summation as in
`../arithmetic/NEGATIVE_MASS.md` then yields

\[
 N(Y)=O_\epsilon(Y^{\theta-1/2+\epsilon}).            \tag{C6}
\]

Together with its nonnegative-transform Landau lemma this excludes zeta
zeros with real part greater than theta. Thus (C4) is a source-faithful
conditional adapter with a completely explicit exponent cost. It supplies
no missing correlation estimate by itself.

## 3. Even uniform logarithmic correlation savings are insufficient

Fix `0<alpha<1` and define the positive, completely multiplicative function

\[
 f_\alpha(n)=\alpha^{\Omega(n)},\qquad f_\alpha(1)=1.
\]

Here Omega counts prime factors with multiplicity. This source has modulus
at most one. For every Dirichlet character chi, every real t, and every X,

\[
 \mathbb D(f_\alpha,\chi n^{it};X)^2
 =\sum_{p\le X}\frac{1-\Re(\alpha\overline{\chi(p)p^{it}})}p
 \ge(1-\alpha)\sum_{p\le X}\frac1p.                 \tag{C7}
\]

Consequently it satisfies uniform nonpretentiousness even with no restriction
on t or on the character conductor. Yet its summatory function has exponent
one: it is at most X and, by retaining only primes, at least
`alpha*pi(X)>=c_alpha X/log X`. No bound `O(X^theta)` with theta<1 holds.

It nevertheless has a logarithmic correlation saving **uniformly over all
integer shifts 0<=h<=X**. Here is an elementary proof, which needs no
Selberg--Delange theorem. Put r=alpha^2 and `g(n)=f_alpha(n)^2=r^Omega(n)`.
Complete multiplicativity and `log n=sum_(d|n) Lambda(d)` give

\[
 \sum_{n\le X}g(n)\log n
 =\sum_{m\le X}g(m)\sum_{d\le X/m}g(d)\Lambda(d)
 \le C X\sum_{m\le X}\frac{g(m)}m.                 \tag{C8}
\]

The last inequality uses `g(d)<=1` and the Chebyshev upper bound for psi.
The positive Euler product and Mertens' estimate imply

\[
 \sum_{m\le X}\frac{g(m)}m
 \le\prod_{p\le X}(1-r/p)^{-1}
 \ll_r(\log X)^r,                                  \tag{C9}
\]

because `-log(1-r/p)=r/p+O_r(1/p^2)` and the square-prime sum converges.
For n>sqrt(X), log n>log(X)/2. The remaining prefix contributes at most
sqrt(X). Therefore, for X>=3,

\[
 \sum_{n\le X}g(n)
 \le\sqrt X+\frac{2C X}{\log X}\sum_{m\le X}\frac{g(m)}m
 \ll_r\frac{X}{(\log X)^{1-r}}.                    \tag{C10}
\]

For every 0<=h<=X, Cauchy--Schwarz and positivity now give

\[
 \left|\sum_{n\le X}f_\alpha(n)f_\alpha(n+h)\right|
 \le\left(\sum_{n\le X}g(n)\right)^{1/2}
       \left(\sum_{m\le2X}g(m)\right)^{1/2}
 \ll_\alpha\frac{X}{(\log X)^{1-\alpha^2}}.         \tag{C11}
\]

For alpha=1/2 this is a uniform three-quarter power of logarithm saving,
alongside an explicit prime lower bound ruling out every summatory power
saving. Thus bounded multiplicativity, very strong uniform nonpretentiousness,
and even all-shift logarithmic correlation control cannot alone supply the
Mertens power needed by (C6). The exact prime signs or another quantitative
native-source property must enter. This is a countermodel to an implication
from those general properties; it is not a countermodel to RH or to family
007's Liouville theorem.

What ran: a finite exact identity checker is supplied separately. Such checks
verify normalization and endpoint handling; the infinite assertions above
are analytic consequences of the displayed proofs and classical inputs.

Smallest remaining gap: a power-scale estimate for the actual signed
Liouville/Möbius correlations, or a direct signed window-energy estimate in
(C2) strong enough to beat the absolute-correlation loss.
