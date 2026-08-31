# Proof review dossier: PRs #765, #766, #770, and #781

This directory publishes the complete proof-oriented analytic and structural review packet in theorem-sized files. The underlying live PR heads were audited read-only; this branch adds documentation and proofs only. RH and GRH remain unproved.

## Contents

1. [Generalized-Schur zero-index theorem](GENERALIZED_SCHUR_ZERO_INDEX.md)
2. [First literal-Xi radial heat correction](XI_RADIAL_HEAT_CORRECTION.md)
3. [Source-admissible observation and Epstein wall structure](SOURCE_OBSERVATION_AND_EPSTEIN_WALL.md)
4. [Next lemmas, evidence boundaries, and stop conditions](NEXT_LEMMAS_AND_EVIDENCE_BOUNDARIES.md)

The audit, provenance, imported-result boundary, and novelty classification follow below.

---

# Proof-oriented analytic and structural review packet

## Live Riemann repository PRs #765, #766, #770, and #781

**Audit date:** 2026-08-31  
**Status:** proposed analytic review packet; independent proof review required  
**Analysis mode:** the underlying PRs were audited read-only; this publication adds only this packet  
**Repository-change scope:** no source producer, fixture, certificate, or inherited claim is modified  
**RH/GRH status:** RH and GRH remain unproved.

### Frozen audit boundary

| PR | Exact live head |
|---|---|
| #765 | `8f01064df805624c045877655893c324a220975d` |
| #766 | `17c7624a0bd56c5356d00278b2a846d2efdbdccc` |
| #770 | `9421846721cd788ab01615c8b6d459d9de849df7` |
| #781 | `ea282c4e73ecd2d8cad44587da5ffa135df67e98` |

This packet treats those commits, not earlier snapshots, as the claim boundary.

## Provenance, imports, and novelty boundary

### Imported repository results

The following are inputs, not discoveries of this packet:

* **PR #765:** the raw-Xi-innerness/RH equivalence; the 40 certified fifth-companion zeros; the immutable 26-point transport panel and its 8 successes/18 unresolved points; the compact-\(\kappa\) radial limit; and the exact finite-\(\xi\) semigroup obstruction.
* **PR #766:** the fixed-depth divisor ladder; the Hecke-support lower and zero-free upper regimes; the positive completed matrix/theta-source constructions; and the proper theta-source off-central-zero counterexamples.
* **PR #770:** the pure-prime rank-collapse theorem; the local source matrices and their certified inverse bounds; the full-support Kronecker factorization; the constants \(B=483723248\) and \(L_3=39375/64\); and the certified finite-horizon rank interval.
* **PR #781:** the exact graph certificates and proved mechanisms; the real Epstein sign-change bracket; and the two winding-one complex Epstein rectangles.

Every numerical constant imported from these branches is identified where it is used. No finite certificate is promoted to an infinite theorem.

### Classical analytic inputs

The proofs use standard canonical-product/logarithmic-derivative theory for real entire functions of genus at most one, elementary inertia and Cauchy-matrix arguments, Cauchy--Binet, Gaussian/Bessel-3 heat-kernel identities, covariance monotonicity, Rouché/argument-principle logic already present in the source packets, and the real-analytic implicit-function/Weierstrass preparation principles. These are imported tools, not priority claims. The relation to generalized Nevanlinna and Kreĭn--Langer theory is acknowledged; the packet gives direct source-normalized proofs sufficient for the stated classes.

### New deductions in this packet

Subject to independent review, the genuinely new contributions here are:

1. the exact Pick-kernel congruence and zero-index theorem for real polynomials and a genus-at-most-one real entire class, with the sharp distinction between distinct zeros and algebraic multiplicity;
2. the explicit first two literal-Xi source corrections, their inward monotonicity law, universal radial total-positivity no-go theorem, semigroup-cocycle counterexample, and the larger odd-order rounding obstruction;
3. the product-observation classification, explicit lower frame bounds and conditioning estimates for the source-authenticated full-support family, and the exterior-square explanation of pure-prime alias collapse;
4. the structural Epstein observation that a symmetry-related off-line pair can meet the critical line only through the multiple-zero discriminant, together with the correct derivative target for a wall certificate.

No external novelty or priority claim is made. “Proved in this packet” means a complete written derivation is supplied below; it does not mean the result has received the independent review or machine binding applied to the source PR packets.

---

# 1. Exact live-state audit

## 1.1 PR #765: Xi companion, transport, and current limits

The branch has already proved the decisive firewall. For the centered real entire Xi function \(f\) and every fixed \(\lambda>0\),

\[
\Theta_\lambda(z)=\frac{f(z)-i\lambda f'(z)}
                       {f(z)+i\lambda f'(z)}
\]

is Schur/inner in the upper half-plane if and only if RH holds. Thus raw companion innerness cannot be used as a preliminary lemma without proving RH.

The fixed-\(\lambda\) finite campaigns establish only finite statements:

* 40 certified fifth-companion zeros across the old and held-out boxes;
* the quarter-lower-bound pattern for \(|\Theta_0|\) is refuted;
* the frozen 26-point joint-polynomial transport criterion succeeds at 8 points and leaves 18 unresolved;
* criterion failure is not a nonexistence theorem.

The odd-current analysis proves a compact-\(\kappa\) limit to the noncentral three-dimensional radial Gaussian law and a separated-saddle regime. The associated order-to-radius kernels converge under fixed finite composition to the Bessel-3/radial heat semigroup. This limit is explicitly universal for a broad Gaussian-concentrating class and the finite-\(\xi\) rounded kernels do not form an exact semigroup.

## 1.2 PR #766: divisor ladders, Hecke support, and positivity firewalls

The divisor-ladder theorem is fixed-depth:

* first choose a fixed \(J\);
* then let even weight \(k\to\infty\);
* the nested determinants have one simple real zero near \(c=k(1-s)=12J\);
* adjacent quotient zeros and poles interlace with explicit exponentially small gaps.

It does not yet give a growing \(J(k)\) law for the same quotient.

A different theorem gives proper theta-source quotients with real off-central zeros uniformly for every \(j\ge1\) and even \(k\ge96j\). This is a linear-depth theorem, but each \(j\) defines a different source quotient; it is not a growing divisor census for one fixed quotient.

The Hecke results remain genuinely separated:

* the fixed-depth divisor-ladder nullvectors require \(\gg_J k/\log k\) Hecke lines;
* every Hecke-selected space of rank \(o(k/\log^5 k)\) is endpoint-chamber zero-free.

The completed period and theta-source work proves positive matrix Mellin sources, positive feature kernels, and strict matrix variance, while also proving that the literal period is not Herglotz/positive-real and that source positivity does not force critical-line zeros. The proper theta-source examples are source-exact counterexamples to any inference from positivity, reciprocal symmetry, or a finite Gram matrix alone.

## 1.3 PR #770: finite-prime observation

The original selected 20-row minor is asymptotically singular. Its eight pure-prime rows collapse to at most three limiting directions, forcing limiting rank at most 15. The last five singular values are \(O(H^{-1/2})\), and any inverse, when it exists, has norm at least of order \(H^{1/2}\).

A different, full-support 64-row family is source-authenticated. Its infinite matrix factors as

\[
R_\infty=K_2\otimes K_3\otimes K_5,
\]

and the certified local inverse bounds give

\[
\|R_\infty^{-1}\|_\infty\le
541\cdot752\cdot1189
=483\,723\,248=:B.
\]

The row-dependent source estimate gives

\[
\|R_H-R_\infty\|_\infty\le
\frac{39375}{64\sqrt H}
=:\frac{L_3}{\sqrt H}.
\]

Consequently every integer

\[
H\ge H_3
=354270587548199562597657
\]

has full 64-dimensional rank. Separately, the old 20-row physical observation is certified to have rank 20 for every integer \(450\le H\le2^{48}\). The interval between \(2^{48}\) and \(H_3\) is not filled by those results.

## 1.4 PR #781: graphs and Epstein certificates

The graph layer carefully distinguishes theorem from corpus observation:

* \(GP(n,2)\) is proved positive-end-only for all \(n\ge24\);
* an induced \(2\times15\) ladder forces both-end breach;
* \(\lambda_{\min}\le-3+4f/n\) is proved from frustration;
* the \((h,f)\) phase diagram is exact on the declared finite corpus but not universal.

The Epstein layer proves:

* a real off-line zero of \(Z(s,10i)\) by certified sign change;
* two complex off-line rectangles at one exact modulus, each with winding number \(1\), hence exactly one zero **counting multiplicity** in the rectangle.

Therefore each certified complex zero is simple, even though the artifacts do not contain a numerical lower interval for \(|\partial_s Z|\). The real sign-change zero is only known to have odd multiplicity. No current artifact certifies a modulus derivative, crossing direction, or a connected discriminant wall.

---
