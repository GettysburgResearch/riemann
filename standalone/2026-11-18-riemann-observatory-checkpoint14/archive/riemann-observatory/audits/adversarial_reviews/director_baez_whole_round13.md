# Báez-Duarte: one work, complete journal audit, and ordered limits

18 November 2026. The director read the complete original 2003 Lincei article, pp. 5–11, and both independent complete reconstructions, followed by the third source-and-dependency reconciliation. The preferred manifestation is the BDIM journal scan with two archive front sheets and seven article pages, SHA-256 `9bfb3943ec8d7690d452b8ac7d50fb10614b4e814738dc091390e6ab4994f0b8`. The exact registered version is `2003 Lincei journal scan, pp. 5–11, with two BDIM front sheets`. Plain HTTP delivered the authoritative archive copy; the equivalent HTTPS download failed. No journal-specific DOI was verified.

The integer-dilation criterion, its corollary and the RH-conditional constructive rate survive reconstruction with the local qualifications below. This is whole-work Level 3 for the pinned journal manifestation. Its exact cited standard inputs, independent replacements and edition boundaries remain explicit. It is neither a proof of RH nor a new rate theorem.

## Identity correction before counting

PAPER-E001, arXiv:math/0205003v1, is an expanded preprint of this work, not a separate research work from PAPER-E014, arXiv:math/0202141. The May abstract explicitly calls the February deposit the “first version of this paper” and describes itself as the second version adding the quantitative theorem. The author's independent May 2003 self-citation in arXiv:math/0305191v1, p. 2 reference 1, identifies math/0205003 as the preprint for the Lincei article. The unsuffixed journal article incorporates that addition as Theorem 2 and reproduces its proof and attribution. Two independent source-identity reviews agree.

Thus E001 becomes a stable work alias for E014. Both repository IDs, their DataCite identifiers, manuscript/registration dates, exact PDFs and document-specific locators remain separately citable. May Proposition 3.1 is journal Theorem 2; work identity does not renumber a historical source passage. The two February versions have no quantitative theorem. This correction lowers the selected-work count by one, rather than padding the corpus to a round target. The delivered checkpoint 9 retains its historical byte identity and counts.

The merge must explicitly retain the full May source record and override the lexical first-wins builder's preferred fields with the journal identity. Otherwise a bare alias would leave a canonical E014 carrying the May title and source. The original track records remain unchanged; the late director overlay records this preference and every manifestation.

[Identity review and independent author self-citation](analytic87_baez_identity_review.md) · [Independent identity and merge review](uniform87_baez_identity_review.md)

## Exact results and Hilbert spaces

Let `H=L²((0,infinity),dx)`, `rho_a(x)={1/(a x)}`, and `chi=1_(0,1]`. Let B_nat be the finite linear span of rho_n for **all integers n≥1**. Journal Theorem 1 states

```text
RH if and only if chi belongs to the H-closure of B_nat.
```

The corollary equivalently requires H-convergence of the finite damped sums `f_(epsilon,n)=sum_(a≤n) mu(a)a^(−epsilon)rho_a` for all sufficiently small fixed positive epsilon. A null sequence of such dampings suffices; an unbounded cutoff subsequence for each damping also suffices by the same pointwise-limit obstruction.

Theorem 2 states that under RH there exists a fixed c>0 such that

```text
||chi + sum_(a≤n) mu(a) exp[−c log(a)/loglog(n)] rho_a||_H
  = O((loglog n)^(−1/3)), as n→infinity.
```

This is an upper bound, with constants and sufficiently large n, not an asymptotic equivalence, practical threshold or optimal rate. The paper credits the quantitative statement and proof to Balazard, the parallel shift suggestion to Bombieri, and the ratio input to Burnol.

Each generator lies in H by boundedness near zero and its exact scalar 1/x tail. Endpoint values are immaterial to H and kept in pointwise identities. Removing the integer generator n=1 changes the criterion: on 1<y=1/x<2 all n≥2 give only scalar multiples of y, which cannot approximate chi's constant value. Real dilations a>1 versus a≥1 have the same norm closure by dominated continuity as a decreases to 1. The unweighted full-half-axis span is not simply the original constrained interval formulation without a change of spaces.

The source's “much larger” continuous span can be made precise: on 1<y<2, all integer generators lie in a closed affine two-dimensional space, while real a in (1,2) introduce distinct jumps at y=a. Distinct such jumps are independent modulo that affine space. Hence the quotient of the continuous by the integer norm closures is infinite-dimensional, even if RH holds. Containment of the single target chi does not make the two spaces equal.

## Qualitative proof, checked with its hypotheses

For every epsilon>0 the pointwise damped series is absolutely convergent and its floor decomposition gives

```text
f_epsilon(x)=1/[x zeta(1+epsilon)]
 − sum_(a≤1/x) mu(a)a^(−epsilon) floor(1/(a x)).
```

The pointwise limit as epsilon decreases to zero is −chi, by the finite divisor identity. This unconditional pointwise statement supplies no norm domination.

For the unnormalized Mellin map `Mf(t)=integral_0^infinity x^(−1/2+it)f(x)dx`, the substitution x=exp(u) gives target measure **dt/(2π)** in Plancherel. The printed dt/sqrt(2π) in journal p. 7 is a local normalization slip. The exact chi witness has transform 1/(1/2+it) and ordinary squared integral 2π, so the printed density cannot give an isometry. The fixed scalar does not change convergence, and journal p. 10 already uses the correct 2π norm-square relation.

For 0<Re s<1, absolute Mellin integration gives `Mellin(rho_a)(s)=−a^(−s)zeta(s)/s`. Weighting by X_epsilon=x^(−epsilon) yields the finite transform

```text
M(X_epsilon f_(2epsilon,n))(t)
 = −zeta(1/2−epsilon+it)/(1/2−epsilon+it)
     × sum_(a≤n) mu(a)a^(−1/2−epsilon−it).
```

For each fixed 0<epsilon<1/2, RH and the correctly quantified Balazard–Saias fixed-gap lemma give convergence of the Dirichlet sum. Keep its arbitrary subpower exponent eta separate from epsilon. Reflected Lindelöf gives error bounded by `C_(epsilon,eta)n^(−epsilon/3)(1+|t|)^(−1+epsilon+2eta)`. Choose `0<eta<(1/2−epsilon)/2` for square integrability. The printed particular envelope `(1+|t|)^(−1+2epsilon)` is square-integrable only for epsilon<1/4, and diverges logarithmically at equality. That smaller range already suffices for the theorem; the free exponent gives the full fixed weighted range. No uniform fixed-gap constants as epsilon decreases are inferred here.

The symmetric ratio lemma is unconditional. The functional equation and conjugation give its modulus exactly as

```text
π^(−epsilon) |Gamma(1/4+epsilon/2+it/2)/Gamma(1/4−epsilon/2+it/2)|
 ≤ C_(epsilon0)(1+|t|)^epsilon, 0≤epsilon≤epsilon0<1/2.
```

Uniform Stirling and compact-height continuity prove the estimate. Common zero singularities are removable along the t-line, or ignored on a null set in L². The journal corrects the February preprints' duplicate plus sign in the gamma denominator; that earlier typo is not assigned to the journal.

The fixed-epsilon weighted norm limit agrees a.e. with the pointwise function by a subsequence. Multiplication by x^epsilon is contractive on (0,1); on (1,infinity), the exact tail is `x^−1 sum_(a≤n)mu(a)a^(−1−2epsilon)`. Equation (2.9) needs 2epsilon in that exponent. Absolute scalar convergence supplies the missing tail and puts f_(2epsilon) in the closed integer span.

Only then send epsilon to zero. The analytic ratio kernels converge unconditionally in L² to −1/(1/2+it), with a uniform integrable envelope from the ratio lemma. Identifying these kernels with the original pointwise damped functions still uses the preceding RH-dependent norm limit. The source's phrase “without the assumption” at this point cannot be used to assert unconditional H-convergence of the actual f_epsilon. Burnol's contemporary discussion and the explicit pole obstruction below fix that interpretation. Under RH, contraction on (0,1) and the scalar tail on (1,infinity) finish f_epsilon→−chi.

The converse can be checked directly, without assuming the original Hardy-space criterion. For a zero rho with 1/2<Re rho<1, the bounded H-functional

```text
Lambda_rho(F)=integral_0^1 F(x)x^(rho−1)dx
 +[1/(1−rho)] integral_1^infinity F(x)dx/x
```

equals the convergent Mellin value on the generators because of their scalar tails. It vanishes there and on their closure, while Lambda_rho(chi)=1/rho. Reflection then excludes both off-line sides.

For the corollary, if f_epsilon is in H, its (0,1) Mellin transform is holomorphic for Re s>1/2. Its independently continued formula is

```text
1/[(s−1)zeta(1+epsilon)] − zeta(s)/[s zeta(s+epsilon)].
```

An off-line zero rho on the right gives a pole at rho−epsilon for every sufficiently small epsilon>0: isolation of zeros makes its numerator nonzero there. Thus f_epsilon cannot lie in H along any null sequence off RH. This identifies exactly why an unconditional analytic-kernel limit cannot be substituted for the damped function limit.

## Quantitative proof and the shrinking-gap input

Correct Plancherel splits the squared approximation error into a truncated Möbius term I_(n,epsilon) and a ratio defect J_epsilon, both weighted by |1/2+it|^−2. The two independent full reviews reconstruct both terms. The previous director adjudication already established THM-E-D202–D204, and this audit does not count them again.

For J, separate delta-neighborhoods of zero ordinates. Burnol's one-sided RH ratio bound and the unit-window zero count give total contribution O(delta). Away from those neighborhoods, horizontal integration of the local logarithmic derivative gives a logarithmic change bounded by `C(epsilon/delta)log(2+|t|)`. For sufficiently small epsilon/delta, exponentiation and an integrable quarter-power allowance give O(epsilon²/delta²). With delta=epsilon^(2/3), J=O(epsilon^(2/3)). Neither zero simplicity nor separation is assumed.

For I, the printed p. 10 special estimate needs genuine uniformity as epsilon shrinks; the fixed-gap Lemma 1 alone is insufficient. The accepted reconstruction uses the actual near-line regions of Titchmarsh–Heath-Brown §14.14 together with a fixed-strip bridge, not just its equality-line display. A pole-removed Borel–Carathéodory estimate supplies low heights. A half-integer Perron cutoff n+1/2 and height (n+1/2)^4 moves to −epsilon/2. For epsilon≥c/loglog n and sufficiently large fixed c, the reciprocal growth loss and endpoint errors are absorbed into a margin epsilon log n/6. This yields the stated uniform `n^(−epsilon/3) exp(O(log(|t|+3)/loglog(|t|+3)))` error. The RH critical-line bound and the weighted integral give I=O(n^(−2epsilon/3)). Setting epsilon=c/loglog n and taking square roots proves Theorem 2. No practical n-threshold follows from this proof.

## Coverage, accepted inputs and findings

All seven article pages, both lemmas, both ordered limits, the converse, corollary, quantitative sketch, acknowledgments and eighteen reference roles are covered. The director independently checked the transform constants, variable shifts, gamma convention, integrability endpoints, continuity functional, pole obstruction and quantitative error balance. The original Balazard–Saias text is a degraded primary reproduction and quoted precisely in the journal; its fixed-gap proof and the stronger shrinking-gap supplement have separate reconstructions. Burnol's actual relevant passages and the revised Titchmarsh near-line input were checked by the independent reviewers. The cited 1951 book and all antecedents were not recertified as whole works. Stirling and standard local zero count are accepted matched inputs.

Existing finding handles for the epsilon envelope, norm normalization, tail exponent and conditional identification are updated with the journal evidence and identity alias. They are not duplicated as newly found issues. The main criteria and rate remain valid with the documented reconstructions. Bounded correction-history searches located no separately verified corrigendum; absence is not proved. The original raw Möbius approximant's divergence and distance lower bound retain their stated historical roles and are not premises secretly substituted for the ordered norm limits.

[Complete advocate](analytic74_baez_whole_advocate.md) · [Complete independent skeptic](weighted74_baez_whole_skeptic.md) · [Third reconciliation](uniform80_baez_adjudication_input.md) · [Earlier uniform-dependency adjudication](director_round3_adjudication.md) · [Original BDIM source](http://www.bdim.eu/item?fmt=pdf&id=RLIN_2003_9_14_1_5_0)
