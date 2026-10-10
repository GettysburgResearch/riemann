# Independent review of the pruned coupled theta estimate

Reviewer: `/root/audit_formalization`, an independent analysis agent in this research pass. Date: 2026-10-10.

**Verdict:** the new deductions pass this scoped mathematical review, subject to the pinned source analytic inputs expressly retained by the author. The result is an estimate for the specified completed two-axis family over squarefree dual rows. The stronger estimate additionally uses the imported infinity-type \(-3\) reciprocal theorem. This review does not establish a full-row moment, the fourth-moment target, or a new zero-free boundary.

## Exact artifact and review scope

- File: `theta/PRUNED_COUPLED_MEAN_SQUARE.md` in the research authoring directory; publication may copy these exact bytes to its packet root.
- Size: 22,426 bytes.
- SHA-256: `411d7b28c0dabc97807d21683d731126e742d16424b1809787c87849dfb9e8d1`.

I read the full note, checked its new normalization and operator arguments, compared the exact cube-completion interface with PR #918, inspected the relevant pinned PR #920 reciprocal statement, and inspected the primary cusp coefficient formulas. This is an independent agent mathematical review, not journal peer review, numerical verification, a Lean proof, or a full independent reconstruction of OpenAI's imported analytic machinery.

The retained sources include OpenAI/math commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`; PR #915 at `9959364671f89b86f3992ec5ed5e19f804eb607b`; and PR #920 at `2edc467ef4dea4aa685219ac6a558a158b88768d`. In particular, the canonical theorem, all-cusp support pruning, and higher-angular analytic continuation from those sources remain dependencies. The present audit checks their stated interfaces where invoked; it does not certify all their proofs anew.

## 1. Every-cusp coefficient adapter

The direct primary reference checked was Dunn–Radziwiłł, *Bias in cubic Gauss sums*, arXiv:2109.07463v3, equations (5.7), (5.13), and (5.14), pages 16–18: https://arxiv.org/pdf/2109.07463v3. The source formulas and the October 5 manuscript's cusp-conjugation identities support the asserted common cubic Gauss structure. Changing cusps changes fixed Gauss numerators, supplementary ray factors, and allowed ramified valuations; it does not replace the variable coefficient by an arbitrary bounded sequence. No RH-dependent estimate from that paper is imported by this step.

The argument correctly separates finitely many squarefree bad-prime patterns. The cube index's bad part runs over the fixed bad primes other than the ramified prime, and its \(1/Nb_S\) mass converges. The ramified valuation is counted separately and has summable weight \(3^{-m/3}\), with a fixed lower bound on \(m\). The final wording explicitly avoids double counting unrestricted ramified powers in the cube part.

After fixing these components, the cubic CRT factor \(\chi_{n'}(e)^4\) and bounded separate coefficient vectors have the orientation needed for the quadratic–cubic sieve. Fixed-denominator additive phases can be split into finitely many residue classes. The reflected indices are allowed to meet the bad set; no forbidden deletion of dual frequencies is used.

## 2. Pruning and norm normalization

The cutoff is inserted at the level where the imported support theorem applies: a complete fixed \((d,g)\) projected group. Only after this insertion does the proof divide positive allocations into \(e,f\), frequencies into dyads, or take norms. Thus the support condition \(G\ll\min(A,\sqrt B)\) is not inferred separately for an individual frequency block.

For the normalized quadratic–cubic vector, the squared prefactor is \(E/(AFG)\). Counting the fixed \(f,g\) labels by Minkowski gives \((FG)^2\), which cancels that prefactor using \(EFG\asymp A\). The cube-index dyad has bounded \(1/Nb'\) mass. Expanding the source's two-sieve expression yields the six terms in (4.2), each bounded by
\[
HE+Y+(EY)^{2/3},\qquad Y=H^2EG^2/(BF),
\]
on the effective range. The handling of subunit frequency length uses the retained transformed-weight tail bounds, not a sieve at a fictitious subunit scale.

The substitutions in Theorem 4.1 are correct. An arbitrary fixed outer divisor-bounded coefficient remains a bounded e-vector after freezing f and g, so the weaker theorem has the stated multiplier stability. The proof invokes the source's uniform logarithmic derivative bounds before Mellin separation; the arithmetic Gauss coefficients themselves are not differentiated.

## 3. The moving e-exclusion operator

The key new Lemma 5.1 is valid. For each term of the finite Euler-product expansion, put \(r=\operatorname{rad}d\) and \(e=re'\). The original moving mask \((k,e')=1\) remains. The factor \(\chi_n(r)^4\) belongs to the n-vector, and \((k,r)=1\) is a fixed row restriction. The coefficient depending on d and the row has modulus at most one.

The normalization changes by exactly \((Nr)^{-1/2}\). The two-sieve expression is increasing in its e-length, so applying it at \(E/Nr\) gives a norm at most \((Nr)^{-1/2}\) times the expression at E. The resulting operator sum is controlled by
\[
\sum_d(Nd)^{-\sigma}(N\operatorname{rad}d)^{-1/2}
=\prod_p\left(1+\frac{(Np)^{-\sigma-1/2}}{1-(Np)^{-\sigma}}\right),
\]
which converges for every fixed \(\sigma>1/2\). The finite support handles empty or bounded e-lengths. No uncontrolled row-dependent multiplier is inserted into the cubic sieve.

## 4. The angular Mellin step

The character in (5.1) has infinity type \(-3\). The pinned PR #920 Theorem 6.2 explicitly supplies conductor-uniform reciprocal bounds for that infinity type and moving imprimitive finite masks in \(\Re s>11/12\). A theorem only for fixed finite-order characters would not suffice, and the note does not make that substitution.

The identity (6.1) has the correct direction of the Euler correction: excluding primes dividing e from a Möbius Dirichlet series multiplies the reciprocal L-function by the inverse local factors. The base masks at k, f, h, and S remain in the L-function. There is no artificial coprimality condition between g and the reflected n or b.

Given the retained uniform transformed-weight bounds and reciprocal theorem, Mellin separation permits a contour at fixed \(11/12<\sigma<1\). The reciprocal is a row scalar and Lemma 5.1 handles the residual e-dependence. The g-label cost therefore changes from G to \(G^\sigma\), with the explicit \(G^{-1/2}\) amplitude unchanged. The squared factor is exactly \(G^{2\sigma-2}\). This proves the displayed block estimate and the three terms in (6.3).

The endpoint exponent \(5/12\) is used only after choosing a positive fixed margin in terms of the final epsilon. No uniform assertion on the line \(\sigma=11/12\) is made. The stronger theorem correctly excludes a general outer coefficient \(v(efg)\), which would destroy the Möbius Dirichlet-series identity. Original coprimality masks are explicitly supported.

## 5. Numerical exponents and remaining interfaces

For \(A=B=D\), the stronger expression is
\[
HD+H^2D^{5/12}+H^{4/3}D^{2/3}.
\]
It is at most \(D^{2+\epsilon}\) through \(H\le D^{19/24}\). The examples at \(H=D^{1/2}\) and \(H=D^{3/4}\) give respectively \(D^{3/2+\epsilon}\) and \(D^{23/12+\epsilon}\). These computations are correct.

I also checked the classical comparison using the physical cube expansion from PR #918. Its squarefree-row envelope is \(H+AB+(HAB)^{2/3}\), with a harmonic H-term and convergent remaining cube sums. It already reaches the balanced diagonal size through \(H\le D\). The new estimates therefore improve the value of the bound in specified short-row regimes; they do not extend that classical diagonal-size range.

The A2/cube child lengths in (7.1) are consistent with the exact source composition, and their row height is unchanged. The new range is not closed under arbitrary such shortening. The final note correctly leaves the growing auxiliary/exclusion adapter and the unrestricted-row adapter unproved. During final review an unsupported particular explanation involving inactive-prime periods was removed. This review binds the corrected text: it makes no claim that such periods necessarily create a growing obstruction.

The distinction between the squarefree dual-row height H here and the physical original moment height must be retained in any synthesis. The exponent 19/24 is a row-range exponent for this completed family, not a zeta boundary. The companion raw corollary has a separate review because a raw bound requires an additional cube-inverse argument.

No source file was changed by this review. Later substantive edits require review of the affected deductions and an updated byte binding.
