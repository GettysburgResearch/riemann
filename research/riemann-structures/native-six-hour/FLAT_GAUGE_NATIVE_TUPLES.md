# Native flat-gauge coinvariants and two complete primitive tuple calculations

Status: proposed exact finite-source theorems and source-authenticated bounded replay.
Scope: the complementary-temperature primitive of L-102901, its endpoint-colour
probability measure, and its product versus ratio observations. This is not an
identification of every post-renewal gamma amplitude in T-106140.
What was actually run: pending the parent agent's serialized validation.
Smallest remaining gap: the exact transport from this primitive, including its
closed-sector remainders and native measures, to the complete amplified member.

## 1. An explicit primitive, not invented history weights

Freeze the labelled source of L-102901. At one ordinary prime put

\[
 f_\tau(x)=(1-x)(1+x)^\tau,
 \qquad x=p^{-1/2}U_p.
\]

For arbitrary primewise temperatures, its complementary factors satisfy

\[
 \sigma_{\boldsymbol\tau}*\sigma_{\mathbf1-\boldsymbol\tau}
 =\prod_p(1-x_p)(1-x_p^2)=\Gamma_{1/2}.                 \tag{1}
\]

All coefficients below are taken after a finite physical-degree truncation,
so every binomial and logarithmic series is coefficientwise finite. The two
labelled copies of 67 are not collapsed. The concrete tuples avoid 67.

The temperature is a permitted source parameter. No Lebesgue probability
measure on temperatures is asserted. A different, explicitly native measure
is provided by L-102904: independent uniform endpoint colours. At each prime
the two factors are either

\[
 E(x)\otimes C(y)\quad\hbox{or}\quad C(x)\otimes E(y),
 \qquad E=1-x,\quad C=1-x^2,
\]

with probability one half. Their expectation is

\[
 M(x)M(y)-D(x)D(y),\quad
 M=1-x/2-x^2/2,\quad D=(-x+x^2)/2.                   \tag{2}
\]

This endpoint expectation is not the tensor of two geometric midpoint
factors f_(1/2). Both have the same arithmetic product (1). The Beta parameter
theta in L-106133 is also distinct: its measure is (1-theta)dtheta and supplies
the canonical equal-pair share, not the complementary-temperature measure.

## 2. FG-1: the exact universal coinvariant quotient

For r labelled primes and D>=1 let

\[
 A_{r,D}=\mathbf Q[x_1,y_1,\ldots,x_r,y_r]/\mathfrak m^{D+1},
 \quad\mathfrak m=(x_1,y_1,\ldots,x_r,y_r).
\]

Here x and y denote the two tensor slots before arithmetic convolution.
The finite logarithmic connection generators are

\[
 L_j=\log(1+x_j)-\log(1+y_j).
\]

This theorem concerns module coinvariants for multiplication by L_j. It is
not a quotient by the differential operator partial_tau-L_j on functions of
temperature. Define the product-collapse algebra map

\[
 C:A_{r,D}\longrightarrow
 B_{r,D}=\mathbf Q[z_1,\ldots,z_r]/(z_1,\ldots,z_r)^{D+1},
 \qquad x_j,y_j\mapsto z_j.
\]

Then

\[
 \boxed{(L_1,\ldots,L_r)=(x_1-y_1,\ldots,x_r-y_r)=\ker C.}       \tag{3}
\]

Indeed,

\[
 L_j=(x_j-y_j)
 \sum_{n=1}^{D}{(-1)^{n+1}\over n}
 \sum_{a=0}^{n-1}x_j^{n-1-a}y_j^a.
\]

The second factor has constant coefficient one. Its inverse is the finite
geometric series in its nilpotent nonconstant part. Thus each L_j generates
the same ideal as x_j-y_j. The kernel of substitution x_j=y_j is the stated
difference ideal, also after the common total-degree truncation. Consequently

\[
 A_{r,D}/(L_j)\simeq B_{r,D},\qquad
 \dim B_{r,D}=\binom{r+D}{D}.                         \tag{4}
\]

For a linear readout lambda on A, the following are equivalent:

* lambda(L_j a)=0 for every j and a;
* lambda(exp(sum_j s_j L_j)a)=lambda(a) for every a and every parameter vector;
* lambda factors through C.

Differentiating the second statement gives the first. Conversely every
nonconstant exponential term belongs to the ideal, and (3) gives the last
equivalence. The universal quantifier over source multipliers a is essential.
Invariance on a single selected source vector does not imply this theorem's
factorization criterion.

## 3. FG-2: the ratio readout does not descend to these coinvariants

For real Mellin frequency t define a linear map on the monomial basis by

\[
 R_t(x^a y^b)
 =\prod_jp_j^{-(a_j+b_j)/2}
   \exp\!\left(it\sum_j(a_j-b_j)\log p_j\right).       \tag{5}
\]

It is a linear physical readout of the truncated source. It is not an algebra
homomorphism from a ring whose positive-degree elements are nilpotent.

For a degree-one connection difference,

\[
 R_t(x_j-y_j)=2i p_j^{-1/2}\sin(t\log p_j).             \tag{6}
\]

Thus phasewise descent requires t log(p_j) in pi Z for every prime. With two
distinct physical primes p,q this is possible only at t=0: otherwise the
ratio log p/log q would be rational, contradicting unique factorization.
At t=0, (5) depends only on a_j+b_j and does factor through C. Hence

\[
 \boxed{R_t\text{ is universally flat-gauge invariant iff }t=0}
                                                               \tag{7}
\]

for at least two distinct primes. Repeated labels of the same physical prime
alone do not provide that two-prime argument.

Use the original L-106026 measure

\[
 d\nu(t)=|\widehat\kappa(t)|^2dt/(2\pi),\qquad
 \kappa(u)=K_L(e^u).
\]

It is atomless and nonzero. Equation (6) is nonzero in L2(nu) even for one
ordinary prime, because its zero set is discrete and nu is absolutely
continuous. Therefore the Hilbert-valued ratio observation does not factor
through C. No nonzero almost-everywhere family of phasewise invariant Mellin
readouts exists for two distinct primes.

This does not exclude an integrated linear functional with extra signed
cancellation, a different target norm, or a source-restricted intertwiner.
In particular integrating an odd function against an even measure can give
zero. The conclusion is about preserving the actual amplitude readout, not
about all scalar integrated quantities.

## 4. FG-3: the zero-Boolean chart has a nonzero raw primitive tuple

Use the exact PR765 diagnostic

\[
 U=64,\quad P=2\cdot3,\quad Q=5\cdot7,\quad g=1,
 \quad c=71\cdot73\cdot79,\quad d=401\cdot421,
 \quad N=Pc^2,\quad M=Qd^2.                            \tag{8}
\]

Its complete Boolean row has twelve left histories and two right histories.
After equal-pair shares 1/10 and 1/6, twelve bilateral coefficients are +1/60
and twelve are -1/60. The canonical bilateral scalar is therefore zero.
The replay reconstructs a_U from its defining subset sum and enumerates every
three-factor Boolean allocation; it does not assume individual histories have
constant sign.

Now ask a different, fully defined question: the coefficient of the raw
two-slot physical tuple (N,M) in sigma_tau tensor sigma_(1-tau). Strip only
its common physical factor 1/sqrt(NM). Since

\[
 [x]f_\tau=\tau-1,\quad
 [x^2]f_\tau=\tau(\tau-3)/2,
\]

the exact stripped coefficient is

\[
 \boxed{
 q_0(\tau)=
 {\tau^5(\tau-1)^4(\tau-3)^3(\tau+2)^2\over32}.}       \tag{9}
\]

In particular q_0(0)=q_0(1)=0 but

\[
 q_0(1/2)=-3125/524288.                                \tag{10}
\]

All nine primes in (8) are on just one side. At endpoint temperatures,
exactly one of the 2^9 colour choices realizes the tuple: each exponent one
must be placed in E and each exponent two in C. Its stripped coefficient is
-1, and every other colour coefficient is zero. Thus the COMPLETE native
colour expectation and its probability-space diagonal are

\[
 \mathbb E q_\epsilon=-1/512,\qquad
 \mathbb E|q_\epsilon|^2=1/512.                        \tag{11}
\]

The diagonal after replacing all colours by their one averaged coefficient
is instead 1/512^2. In the normalized Walsh transform every one of the 512
characters has coefficient of modulus 1/512; Parseval gives (11). This is a
real source probability measure, not a freely weighted 24-history example.

The observations in (9)--(11) use the raw primitive tensor. The canonical
construction first takes the arithmetic product (1), then its squarefree
quotient, which is exactly prod(1-z_p), and then applies the Boolean core
construction, owner shares, and completion. That construction gives the
zero in (8) at every temperature. It uses the corresponding one-sided source
copies before their bilateral pairing. It is not raw coefficient extraction
at (N,M). Thus the comparison proves a mismatch of two explicit maps; it does
not establish a nonzero post-renewal T-106140 gamma coefficient.

## 5. Held-out positive tuple and the complete contraction at its common prime

Retain the frozen dense source's first pair, at U=2^20, with

\[
 P=pq,\ Q=rs,\quad N=P(g\ell)^2,\ M=Q(g\rho)^2.
\]

The seven prime labels and all physical indices are authenticated from the
published dense artifact. Each core has two positive histories and owner
share 1/6, so the canonical stripped bilateral coefficient is 1/9.

In the raw complementary tensor, the shared prime g has exponents (2,2).
The complete endpoint-colour coefficient is zero for every one of its 128
colour choices: the E factor cannot supply exponent two. At a common
temperature tau, however, the raw coefficient is

\[
 \boxed{
 q_+(\tau)=
 {\tau^4(\tau-1)^4(\tau-3)^2(\tau+2)^2\over16},\qquad
 q_+(1/2)=625/65536.}                                  \tag{12}
\]

The common-prime product exponent is four. Its complete five-allocation
convolution coefficient vanishes because (1-x)(1-x^2) has degree three.
At the geometric midpoint those five coefficients are

\[
 (-13/128,\ -3/32,\ 25/64,\ -3/32,\ -13/128),
 \qquad\text{sum}=0.                                  \tag{13}
\]

The nonzero (2,2) coefficient is exactly canceled in the product observation
by the other four genuine allocations. No arbitrary cancellation weights
were introduced. Neither this cancellation nor the endpoint zero cancels the
positive canonically completed source, whose input and operations differ.

## 6. An exact observed norm control, without numerical Fourier integration

The actual kernel K_L is supported in [1,8], so Gamma(v)=integral exp(itv)dnu
vanishes for |v|>=log 8. For a single odd prime p and total exponent n, the
ratio frequencies of the complete allocations are (2a-n)log p. Distinct
allocations are therefore orthogonal in this original measure, because
their separation is at least 2log p>log 8. Writing

\[
 F_{n,\tau}(t)=p^{-n/2}
 \sum_{a=0}^{n} f_{\tau,a}f_{1-\tau,n-a}
 e^{it(2a-n)\log p},
\]

one gets the exact formula

\[
 \boxed{\|F_{n,\tau}\|_{L^2(\nu)}^2
 =\Gamma(0)p^{-n}
 \sum_{a=0}^{n}|f_{\tau,a}f_{1-\tau,n-a}|^2.}           \tag{14}
\]

For n=1 the normalized factor is 1-2tau(1-tau), so endpoints and midpoint
have different norms despite their identical arithmetic product coefficient
-1. For n=4,tau=1/2, the product coefficient is zero but (13) gives

\[
 \|F_{4,1/2}\|^2=\Gamma(0)p^{-4}\,1563/8192>0.         \tag{15}
\]

These are complete one-prime allocation fields of an explicit primitive,
not selected scalar histories. They are absolutely small, not a growing
native-moment counterexample. They make the non-descent in Section 3 visible
in the original observation measure, including the actual contraction.

## 7. Exact remaining boundary and replay contract

The positive result is a complete source-module coinvariant classification,
with two fully reconstructed primitive tuple coefficients, the true endpoint
probability diagonal, source-permitted temperature deformations, and an exact
observed allocation norm. It is more than assigning labels to four abstract
sectors. It does not identify core parity, class Walsh averaging, or the
within-class residue mean projector with this endpoint-colour average.

The complete post-renewal member still requires its occurrence, measure and
transport to be specified. L-106026.8 retains literal coefficients omega_i;
L-106093 retains complete anchor amplitudes and incidence masks. Neither
display sets those weights equal to (9), (11), or the canonical zero. The
present packet therefore does not call the raw tuple a counterexample to
that as-yet-unidentified complete source.

The producer authenticates all frozen primitives, reconstructs binomial
coefficients, complete endpoint colours and the original Boolean subset sums,
and checks exact ideal/reduction controls. Physical square roots remain the
positive factor 1/sqrt(NM); only their squares are rationalized. Infinite
unique-factorization and almost-everywhere assertions are proved above, not
inferred from finite frequency samples. No large prime search, zero scan,
numerical Fourier quadrature or unpinned executable is used.

The adjacent producer contains the full commit:path:blob locks and binds
this proof, its own code and its tests to its artifact. A failed source lock
is a failed replay, not permission to alter a historical dependency.
