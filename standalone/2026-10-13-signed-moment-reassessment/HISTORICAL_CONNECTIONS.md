# What the earlier reductions preserve, and where they stop

Status: source-qualified historical reassessment and proposed research
direction. This document proves no new moment estimate and does not
promote the status of any cited branch component.

Scope: the native signed Möbius program, its September covariance and
completion formulations, and the October finite Hecke-family moment.

What was actually checked: the mathematical sources listed in Section 8
were read at their exact commits. No historical numerical certificate was
rerun for this note. The new signed-trace obstruction in the companion
packet must be assessed from its own proof and independent review.

Smallest remaining gap: an upper bound for a complete signed physical
observable, retaining the original row measure, independent factor
lengths, and all zero masks. Existing identities do not establish it.

## 1. The stable objective behind the changing representations

The October objective is the literal finite-family estimate

\[
 A_u(D;W)=
 \sum_{(\mathfrak n,S)=1}
 \mu_K(\mathfrak n)\nu(\mathfrak n)\chi_{\mathfrak n}(u)
 W(N\mathfrak n/D),\qquad
 \sum_{0<Nu\le H}|A_u(D;W)|^{2k}
 \ll_{\epsilon,k,S,\nu,W}H D^{k+\epsilon},
 \quad H=D^h .
\]

Here the field is the source Eisenstein field, the character \(\nu\) and
the excluded prime set \(S\) are fixed, and the original nonunit zeros
remain in every sextic symbol. The presently relevant range has \(h>1\)
fixed near one. The generalized result concerns every fixed \(k\), with
constants allowed to depend on \(k\). It is not a claim of a uniform
algorithm as \(k\) grows.

The existing sixth-power replica extraction makes the strength of this
goal explicit: an estimate with an extra factor \(D^a\) excludes zeros
to the right of

\[
 \frac12+\frac{5h}{12k}+\frac{a}{2k}
\]

in the corresponding source Hecke family. See the pinned PR #911
complementary-trace contract, CT5--CT6, and its cited extraction source.
Passing through an unbounded hierarchy of fixed orders is therefore a
full-family zero-free assertion approaching the critical line. It is
stronger in scope than a statement only about the Riemann zeta function.

The repeated difficulty is not a shortage of equivalent formulas. Many
formulas have been made exact, including their boundary terms. The
difficulty is that the remaining signed quantity retains the original
size after each affordable transformation.

## 2. Newton compression already isolates the expensive part

NRC32, at PR #905, starts with the literal prefix

\[
 m(k)=\sum_{n\le k}\frac{\mu(n)}n,\qquad
 F_Y=\sum_{k\le Y}m(k)^2.
\]

For \(g=\mu\,1_{n\le Y}\), the Dirichlet-convolution Newton step
\(v=2g-\mathbf1*g*g\) agrees with \(\mu\) at every
\(n<(Y+1)^2\). Consequently its native output is the exact finite
quadratic form

\[
 m(k)=2m(Y)-
 \sum_{r,s\le Y}\frac{\mu(r)\mu(s)}{rs}
 H_{\lfloor k/(rs)\rfloor},
 \qquad Y<k<(Y+1)^2.
\]

NRC32 does more than reconstruct this output. Its orthogonal cubic mesh
uses fewer than \(10(Y+1)\) block means and proves

\[
 F_{(Y+1)^2-1}-F_Y=S_Y+D_Y,\qquad 0\le D_Y<\frac56.
\]

All dense covariance is retained in \(S_Y\), the squared norm of the
coarse means. The detail energy is already paid with a constant error.
Improving resolution, adding more samples, or making the tail estimate
sharper does not bound those means. A subquadratic native bound for
\(S_Y\) is still required for the intended recursive contraction.
The source explicitly supplies a bounded-increment countermodel to
obtaining that contraction from regularity alone.

This connects directly to the October collision-free core. An exact
compression can make the remaining object smaller to describe without
making its signed norm smaller. In both settings, the relevant question
after compression is a new arithmetic upper bound for the compressed
object.

## 3. Completion changes coordinates but can leave the whole bulk fixed

CQT32, at PR #906, identifies a particularly strong invariance. If \(c\)
is a balanced completion of the native prefix and \(h,g\) are balanced
perturbations supported at indices at least \(Y+1\), then, in the strict
native square range,

\[
 Q(c,h)=m_h,\qquad Q(h,g)=0,\qquad
 Q(c+th,c+th)=Q(c,c)+2t\,m_h.
\]

After the perturbation support has ended, \(m_h=0\). The complete
quadratic output on that later bulk is therefore unchanged. Optimizing
particular Fourier denominators or lowering a completion's auxiliary
energy can move terms among representations while leaving the desired
bulk observable exactly fixed.

The same source closes the protected semiprime contribution under all
its attributed divisors. The completed packet vanishes on an early
range, then becomes

\[
 S_Y(k)=
 2\sum_{\substack{p<r,\;3(Y+1)/4<p,r\le Y\\pr\le k}}\frac1{pr}
\]

on the remaining native annulus. Its squared energy is asymptotic to
a positive constant times \(Y^2/(\log Y)^4\). This does not refute the
full signed estimate: the complementary source terms are still present
and may cancel it. It does refute the inference that every fully closed
source-product packet must itself have subpower energy.

The October counterpart is to retain the sum over collision allocations
and the final norm filters before asking for cancellation. A large
allocation or a large unfiltered integrand need not have the size of the
complete physical moment.

## 4. Mellin and phase averages have precise extraction prices

The balanced-source Mellin formula in DMC31 retains the whole covariance:
its energy is an integral of
\(|\zeta(1/2+it)|^2|C(1/2+it)|^4/(1/4+t^2)\).
Its high-frequency estimate does not pay the remaining low frequencies.
The later MHB32 bandwidth composition at PR #904 maps a power exponent
\(\kappa\) to

\[
 \kappa\longmapsto\frac{191+82\kappa}{273}.
\]

This output exceeds \(\kappa\) whenever \(\kappa<1\). Substituting a
better seed exponent into that unchanged composition does not create a
bootstrap toward the critical estimate.

The phase packets ADP37 and CAP36, at PR #907, expose a second extraction
problem. Exact phase averaging can reduce the mean energy to logarithmic
size, but the useful dephasing range requires large phases, of order the
square of the source length. The available native comparison with the
principal phase has a cost that grows with those phases. It is useful
in a different range.

ADP37 also constructs a bounded balanced nonnative source with the same
harmonic kernel whose principal-phase energy has quadratic order in
the source length although its phase mean is logarithmic. Thus a
comparison based only on that kernel cannot extract the principal
member at subpower cost. This is a counterexample to a specified generic
comparison, not a counterexample for the native Möbius coefficients.

The lesson for dense row averages is precise. A new family may average
well while failing to transfer its bound back to the target row or
physical row set. A proposed averaging idea must include that transfer
and its scale cost in the theorem being proved.

## 5. Duality and positivity also retain a difficult direction

The Vasyunin/Nyman--Beurling support audit at PR #901 constructs finite
dual tests satisfying

\[
 \langle b_n,d_r\rangle=-\delta_{nr},\qquad
 \langle 1,d_r\rangle=\mu(r).
\]

Every fixed squarefree coordinate is therefore forced in a successful
approximation. Deleting a composite coordinate is not justified by
calling it a secondary collision. The source gives, for example, a
strict positive lower error when the coordinate at \(6\) is absent.

That packet distinguishes the complete dual Gram matrix \(F\) from the
actual Gram matrix \(G\):

\[
 G=F^{-1}+R,\qquad R\ge0.
\]

Although the available trace bound on \(R\) is uniform, inversion gives
\(G^{-1}\le F\), in the direction that does not supply the missing
approximation upper bound. A small trace perturbation can still matter
on a direction where the main matrix has a very small eigenvalue.
Coefficient matching, a finite positive matrix, and a controlled
remainder trace do not replace the needed lower control in that
direction.

This is the same distinction encountered in finite operator sections:
positivity of an upper section or a finite numerical margin does not
establish a lower estimate for the complete source operator. The
historical sources are useful because they identify the exact direction
in which the available inequality runs.

## 6. The signed information lost by complete residue averaging

The PR #911 CRT translation theorem gives the clearest structural
diagnosis. For a finite set of source primes there is a unit CRT class
\(t\) with \(\chi_{\mathfrak p}(t)=-1\) at every one of those primes.
For squarefree supported coefficients, multiplication by \(t\) converts
the unsigned source exactly into its Möbius-signed counterpart. This
conversion retains every zero at nonunits.

It follows that their complete-residue joint distributions, and all
complete-residue even moments, are identical. The information that
distinguishes the native signed problem is the correlation with the
translated short norm-ball measure. Its location matters.

Consequently, a proof that uses only the complete local distribution of
the sextic symbols cannot distinguish these two coefficient systems.
Generic Parseval or absolute Fourier norms pay for the ambient CRT space
and erase the phase correlation with the short row measure. The source
CRT Fourier calculation makes that cost explicit.

This does not say that Fourier analysis is unavailable. It identifies
the correlation that a Fourier proof must preserve. Nor is a universal
negative fourth cumulant available: the same packet records literal
native counterexamples to that sign shortcut.

There is a parallel arithmetic correction in the SHARP program. The
current source-qualified supercritical certificate reaches every
\(m\ge19/15\), not merely \(m\ge2\). Its critical \(m=1\) obligation
remains open. The native negative-mass exponent is identified with the
rightmost-zero obstruction, while the full-variation activation tail
retains a positive leading term even under stronger cancellation
hypotheses. Replacing signed mass by full variation loses exactly the
information required at the critical endpoint.

## 7. What has already been solved about prime collisions

The all-order collision removal at PR #916 must be credited before
proposing another collision algebra. For \(r\) slots it proves the
local identities

\[
 R_r(\mathbf z)=\frac{\prod_i(1-z_i)}{1-\sum_i z_i},
 \qquad
 Q_r(\mathbf z)=\frac{1-\sum_i z_i}{\prod_i(1-z_i)}.
\]

The coefficients of \(R_r\) are nonnegative; on a binary support of size
\(j\) they are the derangement number \(!j\). The nonconstant
coefficient of \(Q_r\) at a multi-index \(\mathbf a\) is exactly
\(1-|\operatorname{supp}\mathbf a|\).

PR #916 already proves both finite convolution reconstructions between
the product of the source Möbius polynomials and its pairwise-coprime
version. These formulas retain the fixed excluded set, all row zeros,
and independently shortened factor lengths. The same source proves
sharp absolute kernel mass of order

\[
 (\log Z)^{\binom r2}
\]

at the square-root weight. It consequently gives reversible row-norm
comparisons at polylogarithmic cost, provided the bound covers the full
rectangle of shortened factor scales at one common row range.

Its cycle-factorization continuation already uses primitive cyclic
words to factor every bounded collision degree into completed
\(L\)-functions, with an absolutely convergent higher-degree remainder.
The singleton reciprocal factors and their possible zeros remain.
Neither the derangement identity nor the all-degree completion is a
new result of the present reassessment.

These results show that paying for collision bookkeeping is not the
unresolved main theorem. The remaining norm of the collision-free
polynomial still contains the long product-column correlations.
In particular, an estimate only at equal factor lengths does not
automatically supply the rectangular estimate required by the existing
reconstruction.

### The pointwise finite-Euler target requires a separate audit

PR #911 SC4 establishes a whole-integral identity for a rational finite
collision factor multiplied by literal short polynomials. It explicitly
does not claim equality of the unfiltered integrands. The subsequent
CT1 contract asks for an independent-frequency pointwise bound before
the final physical norm filters are applied.

Those are different assertions. Frequencies at which a rational Euler
factor is very large can disappear after the complete coefficient
filtering, so a pointwise majorant may be much stronger than the moment
needed by the program. The companion signed-trace proof investigates
this precise failure and proves that CT1 has superpolynomial violations
at every fixed order. The separate SIGNED_TRACE_INDEPENDENT_REVIEW.md
accepts its mathematical argument at the recorded source-file hash.
That scoped content review is not integrated status or a substitute
for the publication's later exact-commit receipt. Its accepted conclusion
concerns the unfiltered pointwise contract; the physical moment remains
open.

A safe existing alternative is to use PR #916's finite coefficient
convolutions with their explicit shortened windows. This keeps the
physical truncations in the identity and avoids requiring the same
bound for an unfiltered rational integrand. The available comparison
still leaves the signed rectangular norm estimate open. It does not
inherit any particular frequency-tube estimate without another proof.

### An explicit finite replacement and its inherited cost

The following consequence makes that alternative concrete in the
notation of SC1--SC4. Its coefficient formula and kernel bound are
credited to PR #916, Theorems 2.2, 3.1 and 4.1. The norm-filtering step
is the same coefficient argument already used in SC2. This is an
application of those results, not a new collision-removal theorem.

For \(r=2k\), let \(\mathcal P_Y\) retain only ideal monomials whose
coordinate norms all satisfy \(N\mathfrak n_i\le Y\). In the
coordinatewise Dirichlet-convolution algebra,

\[
 \mathcal P_Y(FG)=
 \mathcal P_Y\bigl((\mathcal P_YF)(\mathcal P_YG)\bigr).
 \tag{HC1}
\]

Indeed norms multiply and are at least one. A discarded coordinate of
norm greater than \(Y\) can never return to the retained box when it
is multiplied by another integral ideal. This proves HC1 coefficient
by coefficient, with finite divisor sums.

For a source incidence mask \(Q\), let
\(D_r^{SQ}(\mathfrak d_1,\ldots,\mathfrak d_r)\) be the multiplicative
kernel whose local coefficient is \(1-|\operatorname{supp}\mathbf a|\)
away from the zero multi-index, and one at the zero multi-index.
It vanishes if any coordinate meets \(SQ\). Define the finite
Dirichlet polynomial

\[
 \widehat{\mathcal Q}_{Y,Q,u}(\mathbf s)=
 \sum_{\substack{N\mathfrak d_i\le Y\\1\le i\le r}}
 D_r^{SQ}(\boldsymbol{\mathfrak d})
 \prod_i\theta_{i,u}(\mathfrak d_i)
              (N\mathfrak d_i)^{-s_i}.
 \tag{HC2}
\]

This is the coordinate-norm truncation of the exact collision series.
Its left and right phases may differ, just as in SC1. The underlying
formal identity has separate variables in each slot, so this change of
phases preserves it. No division by a character value occurs.

Apply HC1 to SC1 and the literal truncations \(T_{i,Y,u}\). It gives

\[
 \mathcal P_Y C_{Y,Q,u}
 =
 \mathcal P_Y\left(
    \widehat{\mathcal Q}_{Y,Q,u}\prod_iT_{i,Y,u}
             \right).
 \tag{HC3}
\]

Every source test \(W_i(Nc_iN\mathfrak n_i/D)\) vanishes unless
\(N\mathfrak n_i\le Y/Nc_i\le Y\). Therefore the entire SC4 identity
continues to hold when its rational collision factor is replaced by
the finite polynomial HC2. In full notation, the replacement integral
is

\[
 \frac1{(2\pi)^r}\int_{\mathbb R^r}
 \widehat{\mathcal Q}_{Y,Q,u}(\sigma+i\mathbf t)
 \prod_i
 \left[
 T_{i,Y,u}(\sigma+it_i)
 (D/Nc_i)^{\sigma+it_i}
 \widehat W_i(\sigma+it_i)
 \right]\,d\mathbf t .
 \tag{HC4}
\]

It equals the same tested coefficient sum on the left side of SC4.
All polynomial sums are finite, and the fixed smooth Mellin transforms
decay rapidly, so termwise inversion is legitimate. Summing with the
same exterior multiplier and Schwartz row measure preserves the
identity.

Put \(m_r=\binom r2\). The inherited absolute kernel estimate gives,
uniformly in the row, the incidence mask, and all independent
frequencies,

\[
 \left|
 \widehat{\mathcal Q}_{Y,Q,u}
       (\tfrac12+i\mathbf t)
 \right|
 \le
 \sum_{\prod_iN\mathfrak d_i\le Y^r}
 \frac{|D_r^S(\boldsymbol{\mathfrak d})|}
      {\sqrt{\prod_iN\mathfrak d_i}}
 \ll_{r,S}(1+\log Y)^{m_r}.
 \tag{HC5}
\]

There is no hidden enlargement of the source's fixed \(S\) in HC5.
PR #916 states its simultaneous two-kernel theorem after a convenient
fixed small-prime exclusion. For the inverse kernel used here, each
omitted small-prime absolute local sum is

\[
 2-\frac{1-rt}{(1-t)^r},\qquad t=(N\mathfrak p)^{-1/2}<1,
\]

and is finite. Restore the finitely many such sums as one fixed
multiplicative constant. This proves HC5 for the original \(S\).
Deleting further primes through \(Q\), or retaining a character zero,
only removes terms from its nonnegative coefficient majorant.

For \(0<\sigma\le1/2\), every term in HC2 has
\(\prod_iN\mathfrak d_i\le Y^r\). Multiplying its square-root weight
by \((\prod_iN\mathfrak d_i)^{1/2-\sigma}\) consequently proves

\[
 \boxed{
 \left|\widehat{\mathcal Q}_{Y,Q,u}
                 (\sigma+i\mathbf t)\right|
 \ll_{r,S}
 Y^{\,r(1/2-\sigma)}(1+\log Y)^{m_r}
 =
 Y^{\,k(1-2\sigma)}(1+\log Y)^{k(2k-1)} .
 }
 \tag{HC6}
\]

This removes the artificial superpolynomial cost of the untruncated
rational collision factor while preserving the complete filtered
source identity. HC6 only bounds the finite collision operator. It
does not bound the row trace after multiplication by all short
polynomials, and it does not pay for a further incidence summation.
Neither CT1's desired trace bound nor a new physical moment follows.
The frequency components of HC4 need not agree with the components
of SC4, so the earlier negligible-tube statement cannot be transferred
to HC4 without an additional argument.

## 8. Frozen sources and provenance

The filenames below are paths within their specified commits. All
references are to those frozen objects, not to an unpinned branch head.

| Source | Exact commit | Load-bearing files |
|---|---|---|
| PR #901 | 93126fa9131ebfa93311c1874eeb4cbd93c97864 | standalone/2026-09-18-vasyunin-support-leakage/PROOF.md |
| PR #904 | 8c506696d8ad7772ccaf48fbb8678fcd889e8beb | standalone/2026-09-21-mellin-hankel-bandwidth/PROOF.md |
| PR #905 | 0f82df3bf1d0bc669a1bbca09f8404b77c6fecde | standalone/2026-09-21-native-covariance-compression/PROOF.md; standalone/2026-09-20-anchored-composite-covariance/MELLIN_DENSE.md |
| PR #906 | ddc25eafe85d637b6c7e8a7e276b39e4998fd648 | standalone/2026-09-21-completion-covariance-quotient/PROOF.md |
| PR #907 | aa725eebf89201fcbefbf7f5e209a22ec318ba5a | standalone/2026-09-25-anchored-dephasing/PROOF.md; standalone/2026-09-25-completion-anchored-phase/PROOF.md |
| PR #911 | 2f8b6a3898a722d0602a91dea73bac344a3bb7dd | research/exploratory/2026-10-10-four-hour-wave/arithmetic/ARITHMETIC_COMPLETION.md; correlations/MOBIUS_CRT_TRANSLATION.md and arithmetic/CRT_SHORT_FOURIER.md under the same four-hour-wave root |
| PR #911 continuation | 2f8b6a3898a722d0602a91dea73bac344a3bb7dd | research/exploratory/2026-10-10-two-hour-continuation/literature/SHORT_POLYNOMIAL_COLLISION_TRANSPORT.md; COMPLEMENTARY_SHORT_TRACE_CONTRACT.md under that same literature root |
| PR #916 | dd70e580a5ffdbe5b140784ba6cebd173cb84792 | standalone/2026-10-10-all-order-collision-removal/PROOF.md; continuation-balanced-closure/CYCLE_FACTORIZATION.md under that same packet root |

The new direction justified by this audit is to preserve the final
physical observable through the analytic estimate. The repository has
already shown, in several distinct settings, that removing that
observable's signed correlations can turn an exact reduction into an
unaffordable or false sufficient condition. A successful continuation
must prove a new bound for the surviving signed correlation, or exhibit
a transfer that reaches it at an explicitly affordable cost.
