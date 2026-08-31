# A positive observed Boolean block at the subcritical common-core scale

Status: **proposed exact cofinal coefficient-projection theorem; not a bound or
counterexample for the complete carrier-weighted source**.

Scope: the literal squarefree Boolean balanced row, canonical equal-pair
weights, one prescribed prime-window restriction, and the exact finite-shell
physical Mellin pairing of L-106026. All Boolean histories in this restriction
are summed. The remaining carrier, colour, endpoint and renewal assembly is
not declared to be this projection.

Exact source dependencies: L-106080, L-106026, L-106090 and L-106120 at
86cac1d64364015ec2cc0f8fbb6fc75dc041c12b; L-102746 and L-102880 at
ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc. The external counting input is the
ordinary prime number theorem, for example
[Kedlaya, Theorem 4.12](https://kskedlaya.org/ant/chap-primes-in-ap.html)
with modulus one.

What was actually run: the coordinating agent's bounded scout produced three
fully certified prime-window panels at j=52,56,60. The published producer
verifies those fixed parameters without repeating the search. The complete
producer/test replay is recorded separately at its final frozen review.

Smallest remaining gap for the original programme: determine the contribution
of the complementary source and the full carrier transport. Positivity of a
coefficient restriction cannot provide a lower bound for their signed sum.

## 1. Exact source-owned windows

Let U=2^j tend to infinity and set Y=U^6. Choose eight primes independently in
the following disjoint open windows:

| label | window |
|---|---|
| A | (101U/100, 51U/50) |
| B | (U^(3/4), 101U^(3/4)/100) |
| ell | (51U^(1/4)/50, 409U^(1/4)/400) |
| rho | (411U^(1/4)/400, 103U^(1/4)/100) |
| p | (3200U/4000, 3201U/4000) |
| q | (4800U/4000, 4801U/4000) |
| r | (3203U/4000, 3204U/4000) |
| s | (4803U/4000, 4804U/4000) |

For all sufficiently large U the eight primes are pairwise distinct, none is
the marked prime 67, and ell<rho. Set

\[
 g=AB,\quad c=\ell,\quad d=\rho,\quad P=pq,\quad Q=rs,
 \qquad N=P(g\ell)^2,\quad M=Q(g\rho)^2.             \tag{1}
\]

Then g is squarefree, gcd(c,d)=1, both owner pairs are internally distinct and
are disjoint from each other and from both cores. The common core is exactly
g. The least reduced-core selectors are ell and rho, with the least-discrepancy
orientation already ell<rho. The clean owner/core conditions are literal.

All completed products lie in the same physical shell:

\[
 Y<N,M<\frac{11}{10}Y.                              \tag{2}
\]

Indeed 10302/10000 < g ell/U^2, g rho/U^2 < 530553/500000, while
24/25 < P/U^2,Q/U^2 < 962001/1000000. Squaring the core bounds and multiplying
the owner bounds proves (2) by exact rational arithmetic. In particular the
source ratio-eight condition holds. Moreover

\[
 g\asymp Y^{7/24},\qquad \ell,\rho\asymp Y^{1/24}. \tag{3}
\]

The owner gauge used here is the canonical equal-pair gauge, not the
deterministic largest-two gauge. All five labels on a one-sided occurrence
are below the horizon-safe exceptional-prime threshold 4 sqrt(Y), so the
selected owners are legal equal-pair owners.

## 2. SCB-1: the complete balanced history coefficient is exactly -2

Use the frozen Boolean definition a_U=epsilon-mu_(<=U) star 1_sf and
b_U=a_U star a_U star mu_sf. For the left core {A,B,ell}, A>U, B,ell<U and
U<B ell<2U for all sufficiently large U. Thus

\[
 a_U(A)=-1,\qquad a_U(B\ell)=1,\qquad
 a_U(B)=a_U(\ell)=a_U(1)=0.                         \tag{4}
\]

Every balanced factorization has two nonempty disjoint factors with nonzero
a_U. Since the core has only three labels, the only possibilities are
(A,B ell,1) and (B ell,A,1). All splittings that place B or ell alone in one
of the first two factors vanish. A nonempty third factor also forces such a
vanishing singleton or a unit. Therefore both retained histories have
coefficient -1, and

\[
 b_U(g\ell)=b_U(g\rho)=-2.                         \tag{5}
\]

This is a complete history enumeration, not a selected positive history. It
does not use an endpoint approximation at U: every window inequality is strict.

Each one-sided occurrence has five labels, so its canonical owner share is
1/binom(5,2)=1/10. Its complete principal coefficient is consequently

\[
 a_{P,\ell}=-{1\over5g\ell\sqrt P},\qquad
 b_{Q,\rho}=-{1\over5g\rho\sqrt Q}.                 \tag{6}
\]

Their bilateral coefficient is positive:

\[
 \overline{a_{P,\ell}}b_{Q,\rho}
 ={1\over25g^2\ell\rho\sqrt{PQ}}={1\over25\sqrt{NM}}.\tag{7}
\]

The four literal history-pair coefficients are each 1/(100 sqrt(NM)); (7)
is their exact sum. No coefficient freedom or sign replacement is used.

## 3. SCB-2: the actual physical Mellin pairing is uniformly positive

Use the exact L-106026 kernel and measure

\[
 \kappa(u)=K_L(e^u),\qquad
 d\mu(t)=|\widehat\kappa(t)|^2dt/(2\pi).
\]

Its real autocorrelation is

\[
 \Gamma(v)=\int_{\mathbb R}\kappa(u)\kappa(u-v)\,du
          =\int_{\mathbb R}e^{itv}\,d\mu(t).         \tag{8}
\]

This is the physical Gram kernel. It is not a point evaluation of K_L at an
invented average of N and M. The piecewise formula in L-102880 gives exactly

\[
 \|\kappa\|_\infty=8\sqrt2,\quad
 \operatorname{TV}(\kappa)=32\sqrt2,\quad
 \|\kappa\|_2^2=(384+128\sqrt2)\log2-288.            \tag{9}
\]

Total variation includes the jumps at u=0,log2,log4,log8. The three interval
contributions to the squared norm are respectively

\[
 64\log2+144-128\sqrt2,\quad
 (192+128\sqrt2)\log2-192,\quad
 128\log2-240+128\sqrt2.
\]

For a bounded BV function, its translation difference has L1 norm at most
TV(kappa)|v| and sup norm at most 2||kappa||_infinity. Hence

\[
 \Gamma(v)=\|\kappa\|_2^2-\tfrac12\|\kappa-\kappa(\cdot-v)\|_2^2
 \ge\|\kappa\|_2^2-512|v|.                          \tag{10}
\]

Using log2>2/3, sqrt2>7/5, and log(11/10)<1/10 gives

\[
 |v|<\log(11/10)\quad\Longrightarrow\quad
 \Gamma(v)>544/15>36.                              \tag{11}
\]

Also |Gamma(v)|<=||kappa||_2^2<384. Thus every Gram interaction in (1) is
strictly positive and bounded above and below by absolute constants. The
zero of khat at t=0 does not contradict this physical near-diagonal positivity.

## 4. SCB-3: the observed subcritical restriction saturates its unsigned scale

Define the complete ordered coefficient restriction, with all eight prime
windows and all its Boolean histories included, by

\[
 J_U=\sum_{A,B,\ell,\rho,p,q,r,s}
       {\Gamma(\log(N/M))\over25\sqrt{NM}}.          \tag{12}
\]

Equations (6)--(8) identify (12) with the exact physical cross pairing of the
finite-shell source projection, equivalently its native Mellin integral.
This precedes the additional bilateral-family square. It is neither the
quartic Wick tensor moment nor its source-dual amplification.

The complete sum over the nonzero h,k phase labels recombines to this member:
the two complete Ramanujan sums in L-106120 multiply to one. No phase-cardinality factor is
introduced into (12). All owner-class labels can be retained and summed before
this linear pairing. The construction is unphased principal coefficient data,
not a replacement of a nonprincipal character by one.

The prime number theorem in fixed proportional intervals gives an exact order
for the number of terms:

\[
 \#\{\hbox{allowed eight-tuples}\}
 \asymp {U^{1+3/4+1/4+1/4+1+1+1+1}\over(\log U)^8}
 ={U^{25/4}\over(\log U)^8}.                        \tag{13}
\]

Every tuple gives a distinct ordered interaction: its prime factors recover
the eight disjoint window labels. By (2), (7), and (11), each summand is
bounded between two positive constant multiples of U^-6. Therefore

\[
 \boxed{J_U\asymp {U^{1/4}\over(\log U)^8}
                  \asymp {Y^{1/24}\over(\log Y)^8}.} \tag{14}
\]

No PNT error term uniform in a growing modulus is needed. The eight fixed
proportional intervals are evaluated at U, U^(3/4), or U^(1/4).

### The correct unsigned baseline

For original coefficients bounded by Y^epsilon/(g^2 c d sqrt(PQ)) and a
bounded physical Gram kernel, physical support implies
P<=constant Y/(g^2 c^2), and similarly for Q. Since sum_(n<=T) n^-1/2<=2sqrt(T),
the absolute envelope on g~G, c~C, d~D is

\[
 Y^{1+\varepsilon}\sum_{g\asymp G}g^{-4}
                  \sum_{c\asymp C}c^{-2}
                  \sum_{d\asymp D}d^{-2}
 \ll {Y^{1+\varepsilon}\over G^3CD}.                \tag{15}
\]

This uses a stated multiplicity/amplitude bound in the chosen coefficient
chart; it is not imported for every unspecified carrier-history refinement.
For the Boolean equal-pair coefficient projection itself the needed bound is
elementary: at a core with k prime labels, at most 3^k history allocations and
at most 2^k in the two truncated-divisor factors give |b_U|<=6^k. This is
Y^o(1) on the physical horizon, and each equal-pair share is at most one.
At the scales (3), (15) is Y^(1/24+epsilon), rather than the coarser Y^(1/8)
obtained by discarding the reduced-core windows. The improvement in that
baseline is unsigned. Equation (14) shows no power saving over its exponent
can hold uniformly under the allowed coefficient restrictions (12).

## 5. Wick, source-dual and completion boundaries

The physical pairs N,M here have different squarefree owner kernels and are
never equal. The four owner windows are disjoint; this linear cross restriction
contains no literal one-sided diagonal and no same-owner cross term. All
four Boolean history pairs are deliberately retained.

If this restriction is subsequently put inside the T-106140 bilateral family
square, its own literal atom diagonal must still be subtracted there. Its
source-dual coefficients are g ell rho times (7), and its positive principal
weight is p_iota=c_ell c_rho/(ell rho). Those operations produce a different,
quartic quantity. No bound or lower bound for that quantity is inferred from
(14), and no Wick correction is silently discarded.

The result rules out a proposed cancellation estimate required to survive
every such source-owned Boolean coefficient restriction. It does not rule out
cancellation with other reduced cores, owner windows, carrier terms, or source
regions in the complete original current. The original programme may require
precisely those complementary interactions. No full-source positivity,
RH-facing lower bound, or RH/GRH conclusion is asserted.

## 6. Bounded prime fixtures and their exact arithmetic contract

The optional fixture scout uses only three dyadic exponents j=52,56,60, a
fixed finite list of bases, and at most 5000 candidates per prime window.
The small phase primes are checked by trial division. A large accepted prime
n has a certificate n=k 2^e+1, with k odd, 0<k<2^e, and
a^((n-1)/2)=-1 modulo n. This is an exact Proth certificate.

For completeness, if a prime divisor r of n existed, reduction modulo r
would force the multiplicative order of a to have exact 2-adic valuation e.
Hence r is at least 2^e+1, which is larger than sqrt(n). Two prime factors,
including a repeated factor, are then impossible; therefore n is prime.
This proof uses no probable-prime assumption or floating arithmetic.

The fixtures can authenticate the strict windows, all eight distinct labels,
the complete Boolean history signs, canonical owner shares, physical bounds,
and exact kernel constants. They cannot prove the cofinal prime-counting
estimate or identify the projection with the complete carrier assembly.
