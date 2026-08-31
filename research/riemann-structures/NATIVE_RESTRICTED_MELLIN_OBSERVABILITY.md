# A native restricted Mellin member has many exact modes and small mass

Status: **exact coefficient-level source adapter, linear realization theorem,
and absolute estimate for a specified restricted packet; exploratory, not an
integration verdict**. RH and GRH remain unproved.

The object below is a specified **coefficient-level finite-shell projection**
of the frozen Boolean balanced source. It retains the actual Boolean
coefficients, equal-pair shares, reciprocal weights and Mellin exponents.
It does not assert that the complete carrier-, marked-prime-, renewal- and
selector-weighted assembly equals this projection, or that complementary
source contributions cannot cancel it. Extracting retained formal source
labels is a permitted source operation here, not an estimate for their final
recombination.

Sources and exact identities are locked in
[the manifest](native_restricted_mellin_observability.sources.json).
The parent [fixed-conductor theorem](LIVE_FIXED_CONDUCTOR_MULTIPLICITY.md)
and [quantitative sequel](FIXED_CONDUCTOR_POWER_RANK_BARRIER.md) are frozen
at `9547f4cdc2c8e27a36704029fd74470de844d401`; their independent review is
[preserved separately](FIXED_CONDUCTOR_MULTIPLICITY_REVIEW_9547F4CD.md).
No claim about those reviewed identities is silently strengthened here.

What is checked: two inherited exact live panels, distinct rational Mellin
ratios, symbolic positive native coefficient squares, a rational
Vandermonde surrogate certifying distinctness, and bounded refusal/control
tests. No floating logarithms or square roots are evaluated. The proof of
minimal realization and the all-horizon estimate are mathematical arguments,
not extrapolations from those panels.

## 1. The source projection and its exact normalization

Use one owner-disjoint rectangle from FCM-1 or FCM-3. Thus

\[
 U=2^k,\quad Y=U^6,\quad U^2/4<g<U^2/3,\qquad
 N_i=25g^2P_i,\quad M_j=49g^2Q_j\in(Y,11Y/10).
\tag{1.1}
\]

The two full squarefree cores are `5g` and `7g`. Each has exactly two
ordered Boolean balanced histories, each with coefficient `+1`. Each
one-sided occurrence has six labels, and the selected owner pair receives
the canonical share `1/binom(6,2)=1/15`. All owner labels are globally
distinct and avoid the core and 5, 7, 67.

The projection is defined in this order:

1. Keep the scalar coefficient coordinate of the balanced squarefree source
   in L-106080, with the dyadic cutoff frozen at `U`. Keep the declared
   carrier and other formal labels separate; do not sum their coefficients
   or replace that sum by one.
2. Select the listed left owners with finite core shell `{5g}` and the
   listed right owners with finite core shell `{7g}`. Use the principal
   character coordinate. Any principal character modulo an opposite owner
   takes value one here by the checked clean owner/core coprimality.
3. Keep the canonical equal-pair coefficient `1/15` on each side and add
   exactly the two ordered Boolean histories at each selected arithmetic
   atom. No coefficient is chosen as a free parameter.
4. Form the product of these two restricted one-sided scalar packets. The
   grid is clean and has common source windows, so this product retains
   precisely its `mn` selected bilateral arithmetic pairs. Additional
   coupled masks are not inserted or discarded.

The existence of this coefficient projection does **not** assert that an
arbitrary further source label has a nonzero coefficient or that the full
physical source can be recovered from this projection alone.

Put `kappa(u)=K_L(e^u)` and use the Fourier convention
`kappahat(t)=integral kappa(u) exp(-itu) du` of L-106026. Its exact finite
shell formula gives the restricted fields

\[
 V_L(u)=\sum_i\frac{2}{15\sqrt{N_i}}\kappa(u-\log N_i),\qquad
 V_R(u)=\sum_j\frac{2}{15\sqrt{M_j}}\kappa(u-\log M_j).
\tag{1.2}
\]

Indeed `beta_sf(5g)=beta_sf(7g)=2` by the Boolean history calculation,
and L-106026's coefficient is `beta/(a sqrt(P))`. Substituting `a=5g`
or `7g` and then the share `1/15` proves (1.2). L-106080 is the exact
Boolean replacement coordinate for the same fixed detector; the Fourier
calculation is a finite sum and requires no Dirichlet-series continuation.

Writing `Vhat_L=kappahat A` and `Vhat_R=kappahat B` gives

\[
 A(t)=\sum_i\frac{2}{75g\sqrt{P_i}}N_i^{-it},\qquad
 B(t)=\sum_j\frac{2}{105g\sqrt{Q_j}}M_j^{-it}.
\tag{1.3}
\]

Use the bilateral orientation `conj(A) B` of L-106120. Its exact
restricted principal Mellin member is

\[
 \boxed{F(t)=\overline{A(t)}B(t)
       =\sum_{i,j}c_{ij}r_{ij}^{it}},\qquad
 r_{ij}=\frac{N_i}{M_j}=\frac{25P_i}{49Q_j},\qquad
 c_{ij}=\frac{4}{225\cdot35g^2\sqrt{P_iQ_j}}>0.
\tag{1.4}
\]

Complex conjugating the entire convention replaces every frequency by its
negative and does not affect the results. Source-dual rescaling in
L-106191 is equally exact:

\[
 \widetilde F(t)=35gF(t),\qquad
 \widetilde c_{ij}=\frac4{225g\sqrt{P_iQ_j}}>0.
\tag{1.5}
\]

These irrational square-root weights are retained. The replay represents
their **squares** as positive rationals and keeps the positive-root branch;
it never changes the source to a rational-weight model.

## 2. Arithmetic separation of every Mellin mode

**NMO-1 (distinct modes in a single residue cell).** All `mn` numbers
`r_ij` in (1.4) are different. They lie in `(10/11,11/10)`, whereas every
pair has the same raw residue cell `(1,4)` modulo `(5,7)`.

The ratio bounds follow from (1.1). If `r_ij=r_ab`, then
`P_i Q_b=P_a Q_j`. A prime factor of `P_i` occurs in no other left owner
and in no right owner. Comparing its valuations forces `i=a`; then the
right owner products give `j=b`. This uses exact prime disjointness,
not a numerically observed gap between logarithms. The residue statement
is inherited from the authenticated FCM construction.

In particular `lambda_ij=i log(r_ij)` are distinct. Four literal history
atoms per pair have the **same** frequency; their aggregation to the
coefficient (1.4) is exact and positive. Thus the count is `mn`, not `4mn`.

## 3. Exact autonomous linear realization

An exact finite autonomous linear realization of `F` means a complex
vector space `E`, a constant linear map `T:E->E`, a vector `v`, and a
constant linear functional `L`, such that

\[
 F(t)=L(e^{tT}v)
\tag{3.1}
\]

on a nonempty open real interval. The dimension counted is `dim(E)`.
Both coefficients and the initial vector may be tailored to this single
fixed source packet. No correctness for other source vectors is required.

**NMO-2 (minimal dimension).** For the coefficient projection (1.4), the
minimum dimension in (3.1) is exactly `mn`. Its monic minimal
constant-coefficient differential annihilator is

\[
 \boxed{\prod_{i,j}(D-i\log r_{ij})},\qquad D=\frac d{dt}.
\tag{3.2}
\]

To prove this, let `p(D)F=0`. Then

\[
 \sum_{i,j}c_{ij}p(i\log r_{ij})e^{it\log r_{ij}}=0.
\]

Exponentials with distinct exponents are linearly independent on every
open interval: differentiating through orders zero to `mn-1` at an
interior point produces a Vandermonde matrix with determinant
`product_(a<b)(lambda_b-lambda_a)`, multiplied by nonzero exponential
column factors. Every `c_ij` is nonzero, so `p` must vanish at all `mn`
different exponents. Hence its degree is at least `mn`, while (3.2)
annihilates `F` directly. For (3.1), Cayley-Hamilton gives an annihilator
of degree `dim(E)`. Conversely the diagonal map with entries
`i log r_ij`, vector with entries `c_ij`, and sum readout realizes `F`
in dimension `mn`.

This realization has an explicit parent before listing its bilateral modes.
On `C^m tensor C^n`, take

\[
 T=i\operatorname{diag}(\log N_i)\otimes I
   -iI\otimes\operatorname{diag}(\log M_j).
\tag{3.2a}
\]

Use the tensor product of the actual one-sided positive coefficient vectors
`(2/(15 sqrt(N_i)))` and `(2/(15 sqrt(M_j)))` as the initial vector and
the tensor sum as readout. This generator comes directly from the two
physical source lists and yields (1.4); the preceding proof makes it
minimal. It is not a recurrence fitted to an observed zero or trace list.

Equivalently, the `mn`-by-`mn` derivative Hankel matrix at any real `t0`
has determinant

\[
 \left(\prod_{i,j}c_{ij}e^{it_0\log r_{ij}}\right)
 \prod_{a<b}(i\log r_b-i\log r_a)^2\ne0.
\tag{3.3}
\]

The replay does not approximate (3.3). It authenticates its nonzero factors
by exact rational distinctness of the `r` values and positivity of the
`c` values. Its rational Vandermonde control uses the `r` values only to
verify that separation certificate; it is not mislabeled as the native
derivative Hankel matrix.

FCM-3 therefore supplies specified native projections with

\[
 \dim E\ge\frac{36}{10^8}\frac{Y^{1/3}}{(\log Y)^2}
\tag{3.4}
\]

for every sufficiently large declared dyadic horizon. This conclusion does
not assume a faithful `K^X`-module or arbitrary native coefficient freedom.
It assumes **exact finite autonomous linear realization** instead.

It gives no lower bound for approximate realization at fixed tolerance,
stable numerical rank, or conditioning. Indeed Section 5 proves that the
zero approximation already has small uniform absolute error. The frequencies lie in a short
interval and may be very close. Time-dependent generators/readouts,
nonlinear models, a sheaf over a growing source space, and general derived
or signed pushforwards are outside the class (3.1). Continuous `t` is
essential to this statement; a discretely sampled trace can alias distinct
frequencies and requires its own sampling contract.

## 4. The fixed kernel does not erase these exact modes

The frozen `K_L` is compactly supported and nonzero; for example
`K_L(y)=8-4sqrt(y)>0` on `1<y<2`. Thus its Fourier transform is not
identically zero and is nonzero on some real open interval. If two finite
exponential polynomials satisfy

\[
 |\widehat\kappa(t)|^2F_1(t)
 =|\widehat\kappa(t)|^2F_2(t)\quad\hbox{for every real }t,
\]

division on that interval and exponential independence give `F_1=F_2`.
The same assertion holds for the one-sided filter `kappahat`.
The known zero `kappahat(0)=0` therefore does not identify distinct finite
Mellin members.

This is injectivity of a known filter on the stated function class. It is
**not** a statement that the filtered function itself admits an autonomous
linear realization of the same dimension. It also says nothing about
recovery from the single scalar integral

\[
 \int F(t)\,d\mu(t),\qquad
 d\mu(t)=\frac1{2\pi}|\widehat\kappa(t)|^2dt.
\tag{4.1}
\]

Only retaining the complete filtered function allows division. The original
Mellin integral or a later complementary source sum can lose information.

## 5. The rank witness is absolutely small analytically

The exact coefficients prevent a misleading interpretation of (3.4).
Since `N_i,M_j>Y`,

\[
 S:=\sum_{i,j}c_{ij}=F(0)
 \le\frac{4mn}{225Y}.
\tag{5.1}
\]

For every real `t`, `|F(t)|<=S`. FCM-4 proves
`mn<=pi(U)^2/4` in this fully owner-disjoint window/core class. The prime
number theorem, already imported for FCM-3, consequently gives

\[
 \boxed{\sup_t|F(t)|
 =O\!\left(\frac{Y^{-2/3}}{(\log Y)^2}\right)},\qquad
 \boxed{\sup_t|\widetilde F(t)|
 =O\!\left(\frac{Y^{-1/3}}{(\log Y)^2}\right)}.
\tag{5.2}
\]

The second bound uses `35g<35U^2/3`. These are upper bounds for every
rectangle in the stated class, not merely the growing example. At `t=0`
the positivity of all coefficients also yields the exact lower bound
`S>8mn/(495Y)`. Thus no cancellation was needed for (5.2).

For the source-dual literal Wick form of this **restricted** same-cell
packet, write `Ztilde_ij(t)=ctilde_ij r_ij^(it)`. The four histories per
pair are equal; the literal diagonal is therefore

\[
 \widetilde D=\frac14\sum_{i,j}\widetilde c_{ij}^{2}.
\]

The frozen centered-incidence coefficient is `d=24/35`. Hence its complete
restricted literal Wick form is exactly

\[
 C_{\rm grid}(t)=\frac{24}{35}
 \left(|\widetilde F(t)|^2
       -\frac14\sum_{i,j}\widetilde c_{ij}^{2}\right).
\tag{5.3}
\]

Put `Stilde=sum ctilde`. Then `|Ftilde|^2` lies in `[0,Stilde^2]`
and `Dtilde<=Stilde^2/4`, so `|C_grid(t)|<=d Stilde^2`. The bilateral
Wick measure is exactly (4.1), as specified in T-106140.3. Also
`mu(R)=||kappa||_2^2<infinity` by Plancherel. We have proved

\[
 \boxed{\int|C_{\rm grid}(t)|\,d\mu(t)
 =O\!\left(\frac{Y^{-2/3}}{(\log Y)^4}\right)}.
\tag{5.4}
\]

The restricted principal and Kummer forms have the same parenthesis in
(5.3), with factors `2/35` and `22/35` respectively. Thus the same absolute
order bound holds for all three restricted channels, consistently with
their exact additive-minus-Kummer-equals-principal identity.

This bound includes only interactions whose two literal atoms both belong
to this selected grid. It does not estimate cross terms with complementary
source atoms, a sum over all common cores or conductors, or the complete
signed current. In particular it neither closes nor contradicts WCADD,
WCKUM or WCCORR. It proves that the present large-rank witness is an
absolutely inexpensive restricted packet.

## 6. Replay, interpretation, and next gate

The producer imports the predecessor only after authenticating its exact
frozen source and its current executable bytes. It reruns its source and
live-panel checks. For each of the inherited `3x3` and held-out `4x3`
panels it records every exact ratio, the positive rational square of each
native and source-dual coefficient, their scaling identity, and rational
upper bounds in (5.1)--(5.3). The maximum mode count is twelve, with a hard
cap of sixteen. Source blobs and all current proof/checker files are hashed.

The controls include repeated ratios, a zero coefficient, signed
cancellation at a repeated frequency, distinct ratios despite a common
residue cell, a one-mode case, rejected owner overlap, and source tampering.
These test precisely the hypotheses needed for the noncancellation and
realization claims. Neither prime-distribution asymptotics nor transcendental
logarithms are numerically certified by these controls.

The new bridge is explicit: literal Boolean history projection -> canonical
finite log-field -> exact Mellin member -> minimal autonomous linear
realization. The next native question is whether a proposed source parent
must retain this projected **function**, rather than only its final
integral or another quotient. If it need not, (3.4) is not an obstruction to
that parent. For the analytic problem the concrete remaining task is to
control the complementary cross terms; the isolated grid is already paid
by (5.4). Neither task is settled by a mode count alone.
