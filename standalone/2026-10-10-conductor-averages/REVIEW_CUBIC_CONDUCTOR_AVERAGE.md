# Independent reconstruction of the cubic-conductor average

**Reviewer:** the separate signed-average research agent. This is an
independent AI-agent reconstruction of the deduction, not human peer review
or proof-assistant certification. The reviewer authored the companion
rational-prime note and its separate composition with this result, but did
not author the cubic-conductor mean reviewed here.

**Reviewed object:** the complete
[CUBIC_CONDUCTOR_AVERAGE.md](CUBIC_CONDUCTOR_AVERAGE.md), 24,307 bytes,
SHA-256

    74d9063bd36128d2b510a11d96dda8055539bd7c7a2f2d07f5cc3a105223ea61

This receipt binds file content. The exact source-commit receipt is to be
added only after the mathematical source is frozen.

**Verdict:** the displayed uniform twisted mean, its complete-row
adapter, and the all-order positive accounting theorem are valid
deductions at their stated source-dependent scope. The imported analytic
input is de Faveri's Proposition 8.1, not the fixed-background statement
of his Theorem 1.2. The reviewer found and requested repair of a missing
plus sign in equation (2.7); the reviewed content includes that repair.
The reviewed version also explicitly preserves the primitive product's
bad-prime coefficients when local conductors cancel. The updated content
includes the explicit Eisenstein family normalization, the class-number
argument in the unit adapter, the anisotropic Corollary 4.3, and the
comparison with PR #926's different signed complete-block estimate.

## 1. Sources inspected

The reviewer independently opened the primary version
[arXiv:2610.04045v1](https://arxiv.org/html/2610.04045v1), inspected
Proposition 8.1 and the proof of Theorem 1.2, especially equation (8.4),
and checked the residue-symbol and fixed-ray construction in
Sections 2.2--2.5, including the stated Eisenstein normalization in
Example 2.2. Its squarefree inner index, unrestricted two outer
ideal indices, fixed family data, and coefficient norm are the ones
used in the reviewed note.

The source's full proof of Proposition 8.1 was not independently
certified. This review treats that explicitly named proposition as an
imported theorem. It also relies on the usual Hecke functional equation
and smoothed approximate functional equation, checking their uniform
application here.

The pinned PR #925 complete-row and mask proof and PR #919
small-gcd remainder were read as specified in the reviewed note.
No native Möbius second moment or common zero-free premise was
introduced in the reconstruction.

## 2. Reconstruction of the moving-conductor mean

For fixed primitive background \(\psi\), write \(R\) for its good
conductor norm. The imposed coprimality gives conductor
\(\mathfrak r ab\) outside the fixed bad set. Thus its analytic
conductor is comparable, up to fixed local data, to
\[
R\,Na\,Nb(2+|t|)^2.
\]
This is the correct conductor variable for the approximate functional
equation. A moving conductor must not be incorporated into the fixed
bad set of the imported large sieve, and the note explicitly forbids
that enlargement.

The approximate functional equation is handled separately on its
direct and dual pieces. Its root number has modulus one and lies
outside the corresponding polynomial; the two-piece square
inequality is sufficient. No invalid factorization of a root number
over the two cubic labels is required.

On a positive Mellin line \(\Re z=\delta\), the real conductor factor
costs only an arbitrarily small power. Its imaginary part is a bounded
row multiplier. The Gaussian auxiliary factor and the gamma ratio
give an integrable Mellin kernel with polynomial dependence on \(t\).
The common cutoff may be taken at
\[
Y=(RAB)^{1/2+\delta}(2+|t|)^{C_\delta}.
\]
The coefficients on the good indices are then independent of \(a,b\)
and have the form
\(\psi(n)(Nn)^{-1/2-\delta-i\tau}\). This common-coefficient
property is essential; it is present in the proof.

The passage from the unrestricted approximate-functional-equation
index to the squarefree index of Proposition 8.1 is valid. The unique
factorization
\[
n=sqr^2,\qquad s\mid S^\infty,\quad q,r\in I(S),\quad q\text{ squarefree}
\]
places no coprimality condition on \(q,r\). Weighted
Cauchy--Schwarz uses
\[
\sum_{s\mid S^\infty}\sum_r(N(sr^2))^{-1/2-\delta}<\infty.
\]
The square-part and bad-prime character values are bounded row
multipliers for each fixed \(s,r\). The good inner coefficient keeps
the moving zeros of \(\psi(q)\). At a bad prime, the actual primitive
product character's value is used, rather than an imprimitive
product which might have an erroneous zero.

On every squarefree \(q\)-block,
\[
\sum_{q\sim Q}|\psi(q)(Nq)^{-1/2-\delta-i\tau}|^2
\ll_\delta Q^{-2\delta}\ll_\delta1.
\]
The finite ray partition translates reciprocity into a bounded
coefficient factor. Row coprimality and class restrictions are
removed only after obtaining a nonnegative square. This is precisely
the setting of the imported proposition.

Substituting \(Q\le Y\), and reassigning small losses, yields the three
terms in the repaired (2.7). I independently reduced their ratios
to \(AB=MN\):
\[
\frac{M^{2/3}N^{1/3}(RMN)^{1/2}}{MN}
=R^{1/2}(M/N)^{1/6},
\]
\[
\frac{M^{1/3}N^{2/3}(RMN)^{1/3}}{MN}
=(R/M)^{1/3}.
\]
Both are at most \(R^{1/2}\) for \(R,M\ge1\), \(M\le N\).
Hence the asserted second mean is \(O(ABR^{1/2})\), up to the
stated small loss and polynomial vertical factor. A constant
depending arbitrarily on the moving character has not been hidden.

## 3. Element rows, ray classes, and the exact conductor split

The radial row sum vanishes on a character nontrivial on units.
Otherwise all six generators of each nonzero ideal are present.
The factor six and Mellin identity (3.5) are therefore correct.
No squarefree-row restriction or removal of sixth-power copies is
introduced.

A residual prime appearing twice in the full tuple is nonprincipal
only if its two occurrences lie on the same Hermitian side. Its
sextic exponents are consequently \(2\) or \(4\), exactly the cubic
pair \(\xi_a\xi_b^2\). After the background exponents and fixed
ray classes are frozen, the correction between this ideal family
and the original element symbols is fixed. The remaining background
character has good conductor
\[
R=Ng_1\prod_{m\ge3}Ng_m.
\]
It is independent of the varying \(a,b\) inside the class. The
uncorrected element background need not itself be unit-trivial;
the proof correctly passes to the quotient of the total
unit-trivial character by the fixed cubic Hecke character. Once
the local components at the good primes and the fixed bad set
are determined, class number one excludes a remaining finite-order
unramified character. This supplies the independence statement
without silently identifying characters only from their conductors.

The principal mask is represented by its exact finite Euler
polynomial before bounding it. On the half line its modulus is at
most
\(\prod_{p\mid q_0}(1+(Np)^{-1/2})\ll_\eta(Nq_0)^\eta\),
uniformly in the varying character and height. This upper bound
allows the later count without erasing the nonunit-zero identity.
Only \(L\) is shifted, so no reciprocal-\(L\) or zero-free premise
is involved.

## 4. Reconstruction of the all-order accounting theorem

Fix the nonprincipal labels and their residual exponents.
The principal-mask norm cutoff from the original support is
\[
Nq_0\le
(B_0D)^k(Ng_1)^{-1/2}(Nab)^{-1}
\prod_{m\ge3}(Ng_m)^{-m/2}.
\]
If the cutoff is below one, the corresponding collection is empty.
The finite assignment of primes to column positions, including
the finite choices of frozen residual exponents, costs \(D^\epsilon\)
for fixed \(k\). These are actual positive counts, so arbitrary
coefficient phases are harmless for this step.

For \(a\sim A,b\sim B\), Cauchy--Schwarz on the proved second mean
gives the first mean
\[
\sum_{a,b}|L(1/2+it,\psi_{\rm bg}\xi_{ab^2})|
\ll (RAB)^\epsilon(2+|t|)^C ABR^{1/4}.
\]
The number of choices supplies \((AB)^{1/2}\); this is not a
missing factor. The resulting \(AB\) cancels the exact
\((Nab)^{-1}\) from the principal-mask count on that block.
Only logarithmically many blocks are physically nonempty.

After the Mellin integral, the remaining weight is
\[
D^{k+\epsilon}H^{1/2}
(Ng_1)^{-1/4}\prod_{m\ge3}(Ng_m)^{-m/2+1/4}.
\]
The \(g_1\)-block sums to \(O(L^{3/4})\). Every other ideal sum
converges, with exponent \(-5/4\) already at \(m=3\); preliminary
positive losses can be kept below that strict margin. This proves
the complete stated estimate
\[
\mathcal Q_L^\Phi\ll D^{k+\epsilon}H^{1/2}L^{3/4}.
\]
It sums every cubic double-prime conductor rather than holding its
size bounded. The consequence \(Ng_1\le H^{2/3}\) follows by
dyadic summation and is valid under arbitrary further tuple
restrictions through positive accounting.

I also checked the later anisotropic refinement, Corollary 4.3.
Retaining the first line of (2.1), instead of replacing its bracket
by \(R^{1/2}\), gives the three factors
\[
1,\qquad R^{1/4}(M/N)^{1/12},\qquad
R^{1/6}M^{-1/6}
\]
after the first-moment Cauchy--Schwarz step. Multiplication by
the same principal-mask count and summation over the \(g_1\)
block yields respectively
\[
L^{1/2},\qquad L^{3/4}(M/N)^{1/12},\qquad
L^{2/3}M^{-1/6}.
\]
Every higher-multiplicity sum converges separately, since each
positive background exponent is at most \(1/4\). Requiring these
three quantities to be at most \(H^{1/2}\) gives exactly
\[
L\le H,\qquad L^9 M/N\le H^6,\qquad L^4\le H^3M.
\]
These agree with (4.10), up to the harmless fixed constants
introduced by dyadic ranges. The tuple support remains in force;
the corollary does not assert that arbitrary chosen triples of
scales can be realized by actual columns.

## 5. Numerical scope checks and the surviving gap

I independently recomputed the fourth-moment example with
side exponent \(3/5\), principal cross exponent \(7/30\), and
singleton exponent \(1/6\). Each factor has exponent one.
At \(h=21/20\), the new excess is \(-1/40\), the old completion
excess is \(13/60\), and the old Wu excess is \(353/1920>0\).
Even the old balanced-divisor branch has excess \(43/360>0\).
The common-gcd exponent \(3/5\) is below \(99/140\), and also
below the separately conditional PR #926 cutoff \(69/110\).
These are comparisons of bounds, not lower bounds for the true
arithmetic contribution.

The updated source also explicitly compares the example with
PR #926, Theorem 6.2. Its quoted two-axis exponent arithmetic is
consistent: the two cubic axes each cost \(13/40\), and the other
labels cost \(2/3+7/15\), giving \(107/60\). Consequently the
new absolute accounting estimate must not be described as
improving every known signed complete-block bound. The review
accepts the stated narrower distinction: the new bound controls
the sum of individual absolute tuple kernels and therefore every
additional tuple selector, whereas the cited prior estimate
controls a complete signed block with its source's structured
coefficients. That source theorem is a scope comparison and is
not an input to the proof in Sections 1--4.

The literal signed-remainder subtraction is legitimate because
the removed sector has a positive absolute accounting bound.
Hermitian-side interchange preserves the selection, so the
remainder is real and inherits the stated lower bound from the
nonnegative full residual norm. An upper bound for that remaining
signed sum is not proved. The revised source explicitly preserves
the inherited range \(1<h\le11/10\), native coefficients, smooth
tests, normalization, and other hypotheses for this remainder
consequence; the arbitrary-coefficient theorem itself does not
silently extend that inherited decomposition.

The scope statement is accurate: fully separated top-scale
singletons still have \(Ng_1\asymp D^{2k}\), outside the new
diagonal region near \(H=D\). This result is neither the full
generalized moment nor a new zero-free boundary. Its smallest
external dependency is Proposition 8.1; the most sensitive native
bridge is the uniform approximate-functional-equation reduction
with the finite unit/ray adapter. Both are explicit in the
reviewed source.
