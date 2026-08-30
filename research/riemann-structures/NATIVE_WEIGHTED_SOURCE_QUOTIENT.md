# Native weighted source quotients: a carrier normalization obstruction and a renewal map

Status: **exact finite-source identities and a Boolean renewal counting theorem;
the complete amplified source quotient remains open**.

Scope: the finite labelled prime algebra of L-102741, and the deterministic
largest-two Boolean renewal chart of L-102830/831/862. The original
T-106140 principal diagonal is not redefined. In particular, the ordered-word
diagonal below is not asserted to be the atom convention of T-106140.

Exact sources: L-102741, L-102830, L-102831, L-102860 and L-102862 at
ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc; T-106140 and L-106121 at
86cac1d64364015ec2cc0f8fbb6fc75dc041c12b; the history-only quotient
FFPS_SIGNED_HISTORY_RECOMBINATION.md at a30276a5be049749ebb2147f30f000dd5659298b.

What was actually run: the first replay passed all nine then-existing tests
in ordinary and optimized mode, all three producer modes, and Ruff. An
independent read found a numeric-type acceptance weakness in artifact comparison;
the corrected canonical comparison and tenth hostile test await their final
replay. All computational jobs were run serially by the coordinating agent.

Smallest remaining gap: identify the complete principal atom measure and its
carrier/renewal chart maps, including each change of diagonal, before importing
the paid principal diagonal into a quotient forgetting all representation labels.

## 1. The target and its two different energies

Retain the frozen fibre iota=(g,ell,rho,sigma,tau), the source-dual amplitudes
ztilde=g ell rho z, and

\[
 d\mu(t)=|\widehat\kappa(t)|^2dt/(2\pi),\qquad
 p_\iota={c_\ell c_\rho\over\ell\rho},\quad c_q={q+1\over q-1}.
\]

If lambda ranges over representation labels with the same retained physical
output a=(iota,N,M), put Z_a(t)=sum_lambda ztilde_(a,lambda)(t). The desired
*equal-output* diagonal estimate would be

\[
 \sum_a p_\iota\|Z_a\|_{L^2(\mu)}^2
 \le Y^{o(1)}\mathfrak D_{\rm PP}(Y).                 \tag{1}
\]

This is different from bounding the full principal moment
sum_iota p_iota ||sum_(N,M) Z_(iota,N,M)||^2. Distinct physical outputs still
interfere in the latter. Even a proof of (1) does not prove the RH-facing
principal estimate.

All extra labels that change the family feature, exterior weight or observation
must either be retained or summed as actual functions in their original measure.
Replacing a probability average by a counting sum with its probabilities hidden
inside coefficients generally changes the literal diagonal.

## 2. NQ-1: the native carrier has a factorial word-resolution defect

Let S consist of k>=2 distinct physical prime labels, with no repeated marked
67 label, and write x_S=product_(p in S) x_p. Use the finite nilpotent source
algebra and exact L-102741 definitions

\[
 E=\prod_p(1-x_p),\quad S_2=\prod_p(1-x_p^2),\quad
 R=\prod_p{e^{x_p}\over1+x_p},\quad L=\sum_p x_p.
\]

The native identity is E-S_2=RS_2(e^(-L)-1)+(R-1)S_2. For a squarefree
monomial x_S of degree k, its complete coefficient is (-1)^k. Moreover, its
only contribution on the right is the constant coefficient of RS_2 times
the degree-k squarefree coefficient of e^(-L). Indeed,

\[
 RS_2=\prod_p(1-x_p)e^{x_p},
\]

and each local factor has coefficient zero in degree one. The same is true
of every nonconstant squarefree coefficient of R and of S_2.

Now expand e^(-L) as sum_(j>=0) (-1)^j L^j/j! and retain the literal ordered
words in L^k. There are exactly k! words using S once each. Each word has
coefficient (-1)^k/k!, so their complete coefficient and counting diagonal are

\[
 Z_S=(-1)^k,\qquad D_{\rm word}(S)={1\over k!},
 \qquad |Z_S|^2-D_{\rm word}(S)=1-{1\over k!}.       \tag{2}
\]

The ratio is exactly k!, with no freely chosen source coefficients. Restoring
the native p^(-1/2) weights multiplies both sides by 1/n, where n=product S;
a common nonzero observation vector or positive principal weight also cancels
from the ratio. This is a failure of a proposed *uniform local* subpower
diagonal comparison, not a lower bound for the complete native principal moment.

For S the first k distinct primes, the prime number theorem gives
log n=(1+o(1))k log k, while log(k!)=(1+o(1))k log k. Hence

\[
 k!=n^{1+o(1)}.                                    \tag{3}
\]

At horizons Y=n, or Y=n^A for a fixed A>0, (3) is not Y^o(1). The PNT is the
only analytic input; see Kedlaya, Analytic Number Theory,
[Theorem 4.12](https://kskedlaya.org/ant/chap-primes-in-ap.html), with modulus one.

The example is native to the exact carrier identity, including its complete
squarefree coefficient. It does **not** establish that the frozen T-106140
literal atoms are ordered Taylor words. That missing identification is exactly
why one cannot import its paid diagonal into an unspecified carrier expansion.
Nor is this a source-admissible counterexample to the full principal bound.

## 3. NQ-2: the exact occupation/measure repair

For a multiplicity vector alpha=(alpha_p) with total degree k, the number of
ordered words is m_alpha=k!/product_p alpha_p!. Their coefficients are all
(-1)^k/k!, whereas the coefficient of the occupation atom is

\[
 c_\alpha={(-1)^k\over\prod_p\alpha_p!}.
\]

Thus D_word(alpha)=|c_alpha|^2/m_alpha. Occupation aggregation is an exact
source identity but changes the counting diagonal by
(1-1/m_alpha)|c_alpha|^2. One cannot erase that correction.

Equivalently, put the uniform probability measure on the m_alpha words and
use the integrand c_alpha, rather than counting measure and coefficient
c_alpha/m_alpha. Both have complete coefficient c_alpha, but only the former
has diagonal |c_alpha|^2. These two resolutions are different Hilbert inputs.

For any Hilbert-valued family f on a probability fibre, Jensen gives
||integral f dnu||^2 <= integral ||f||^2 dnu. For a positive finite measure
of mass B the factor is B. In a signed or complex source expansion, absorb its
phase into f and retain its total-variation measure; the same factor is the
total-variation mass. This is the appropriate weighted quotient criterion.
It is not a proof that the complete source satisfies that criterion relative
to its already fixed diagonal.

Native endpoint colour averaging in L-102904 is likewise a probability
average. Homotopy integration in L-102707 is a genuine parameter integral.
Neither is a new collection of counting atoms whose probabilities may be
squared again. Conversely, the source total-variation bound on R in L-102741
does not identify the diagonal of an arbitrary Taylor-history refinement.

## 4. NQ-3: deterministic Boolean renewal has subpower terminal multiplicity

Here is an explicit chart, rather than a claim about every carrier expansion.
At a hard state retain two finite sets A,B of physical primes. Each has at
least two elements. Its owners are its deterministic two largest elements;
other elements are completed square-core primes. The four owners are distinct.
The physical products are therefore

\[
 N=\prod_{p\in\operatorname{Top}_2(A)}p
       \prod_{p\in A\setminus\operatorname{Top}_2(A)}p^2,
\quad
 M=\prod_{p\in\operatorname{Top}_2(B)}p
       \prod_{p\in B\setminus\operatorname{Top}_2(B)}p^2.
\]

An eligible renewal prime is an owner on one side and a core prime on the
other. There are at most four. Extracting its common copy changes the local
exponents (1,2) to (0,1), or conversely. Remove the prime from the side where
it disappears; keep it on the other; then apply the same deterministic owner
rule and completion to the retained squarefree occurrence. Stop on a closed
sector or when no eligible prime remains. Common-square data are retained and
reinserted in the output; no prime support is discarded through that quotient.

These operations are the support maps in L-102830/831/862. Owner reallocation
uses only labels already present, and completion changes their exponent but
not their presence. Thus the union S=A union B is invariant. Once extracted,
a prime is absent from one side forever, so it cannot be extracted again.

In fact every extraction goes in the same direction and there are at most
two choices per step. If p is an owner of A and a core prime of B, then
second(A)<=p<second(B). An overlap in the reverse direction would force the
opposite strict inequality. Thus only the side with the smaller second owner
can lose a prime. Its second owner decreases after deletion; the higher side
retains its entire support. Stop before a side has fewer than two owners.

For fixed terminal supports A,B, an ancestry deleting from A has initial
support A union T for some T subset B minus A, while B is unchanged. For
each extracted set T there are at most 2^|T| paths. The analogous count holds
in the opposite direction. Including the zero path only once gives

\[
 \#\{\hbox{ancestral deterministic Boolean support paths to the output}\}
 \le3^{|B\setminus A|}+3^{|A\setminus B|}-1
 \le2\,3^{|S|}=Y^{o(1)}.                          \tag{4}
\]

Here all original products lie below a fixed power of Y. The last estimate
uses the standard bound omega(n)=O(log n/log log n); alternatively it follows
by comparing the product of |S| distinct primes with |S|!.

This proves a terminal-path bound, not merely a fixed-ancestor bound. The
support invariant is the reason the ancestor count is still subpower.

If each extraction additionally carries an absolute factor C/p, with C fixed,
the same tree bound gives the corrected path majorant

\[
 \sum_{\mathrm{paths}}\prod_{p\ \mathrm{extracted}}{C\over p}
 \le\prod_{p\in S}\left(1+{2C\over p}\right).       \tag{5}
\]

This supplies the ordered-path bookkeeping missing from a direct iteration
of the sum in L-102862.2. It does not independently prove the analytic
per-step estimate or change the domain of the radial observation.

### Exact limitations of the chart

The deterministic largest-two chart has already combined the equal-pair
shares of each occurrence. If those shares are kept as extra literal histories
at every renewal step, (4) is not their count. Nor may one multiply the
log-squared norm cost of each reallocation for omega(Y) steps and call the
result subpower without proof. Arbitrary carrier Taylor histories are excluded;
NQ-1 explains why their inclusion can be fatal to a counting-diagonal argument.

Even on this deterministic chart, the support map does not automatically
preserve the Mellin observable. The following obstruction is part of the
theorem's scope, not an optional warning.

## 5. NQ-4: support renewal does not intertwine the physical Mellin phase

Use the actual Top2 completed supports

\[
 A=\{2,3,5,7\},\qquad B=\{5,7,11,13\}.
\]

Their physical products are N=1260 and M=175175. Extract the eligible common
owner/core prime 7. The literal reduced products are (180,25025), so their
ratio agrees with N/M exactly, as required by L-102860/862. Reapplying the
deterministic owner rule and completion to the reduced squarefree supports
gives instead

\[
 A'=\{2,3,5\},\quad B'=B,\quad
 (N',M')=(60,175175),\quad {N/M\over N'/M'}=21.      \tag{6}
\]

The reason is visible prime by prime: 3 is promoted from a squared core to an
owner, while 7, still in B, is completed from exponent one back to two.
An ensuing extraction of 5 reaches the clean terminal supports
({2,3},{5,7,11,13}) and products (6,175175). Starting at (A',B') reaches
the same clean terminal pair, but has a different original physical ratio.
All owners at each hard state are distinct; the final owner pairs {2,3} and
{11,13} are clean across the opposite cores.

For the native Mellin phase r^it, the two ancestral fields at this common
terminal tuple therefore have different frequencies. No t-independent
scalar coefficient at that terminal ratio represents both on a nonempty
open t-interval. Indeed exp(it log r_1) and exp(it log r_2) are linearly
independent when r_1!=r_2. This uses the exact source products, not arbitrary
test coefficients or a fitted frequency.

The minimal extra datum for this particular phase obstruction is the
transport ratio delta=(N/M)/(N_terminal/M_terminal), or equivalently the
original physical ratio. Each path contributes delta^it times its true
transport amplitude. Keeping a Hilbert-valued coefficient function is also
valid; silently replacing it by a constant is not. Additional masks,
exterior weights and endpoint kernels may require additional labels.

Thus (4) controls discrete source-support path counts. It does not say that
the terminal physical tuple is the correct observable quotient. The exact
common-translation identity applies to the extraction step, and cannot be
extended through a subsequent completion without the explicit operator
transport. This is compatible with the historical source-level gauge identity.

If the transport functions and every remaining feature/weight are retained,
the finite sum of paths satisfies its ordinary Hilbert-valued multiplicity
bound. Its principal Wick correction is p_iota times the grouped-minus-literal
diagonal. Neither this fact nor (4) identifies the resulting chart diagonal
with the original T-106140 diagonal.

## 6. Remaining source map

A complete positive answer to (1) still needs an explicit source map that
records: the canonical carrier occupation convention; primitive colour and
homotopy measures; owner-share recombination and its diagonal cost; renewal
ancestor/terminal maps; all physical and region masks; and the common outer
observation. The map must either preserve the original diagonal or supply its
complete correction. Merely bounding each assembled gamma pointwise does not
provide this information.

The carrier example is a concrete native obstruction to a chart-independent
answer. The renewal theorem removes one narrower counting obstacle. Neither
is a new signed cancellation estimate, a complete marked-source pushforward,
an RH proof, or an unconditional rejection of the principal programme.
