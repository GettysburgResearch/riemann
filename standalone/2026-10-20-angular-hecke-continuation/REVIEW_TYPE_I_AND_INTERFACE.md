# Scoped review of the angular interfaces and Type-I arithmetic

Date: 20 October 2026. Reviewer: `/root/beyond_boundary`.

**Authorship disclosure:** this reviewer authored the Type-I transfer
proof and the mixed-mean precision record. The Type-I checks below are
an author check, not an independent review of that proof. The review of
the other listed analytic adapters is independent of their authorship.

**Conclusion:** no material mathematical objection was found in the
specific extension interfaces reviewed below, after the two recorded
wording/notation corrections. This conclusion is conditional on the
identified upstream inputs. It is not a certification of Liu's complete
136-page preprint, its scalar certificates, or literature-wide priority.

## 1. Exact scope

The reviewed publication files are in
`standalone/2026-10-20-angular-hecke-continuation/`.

| File | SHA-256 reviewed |
|---|---|
| `ANGULAR_THETA_AND_INVERSE.md` | `9ed89b4acf05c6fd35e7edbc0da0f0efa00a7b2b919b766846f01da0b003aa99` |
| `ANGULAR_PRODUCT_MOMENT.md` | `f03592bb707f7341ddabe77c4911ec7abbfcfc37292447f6d7fc6f4d235aaef6` |
| `ANGULAR_BOOTSTRAP.md` | `0315711623796e7f4d17c3c45a921318ab0f580a1314b46b4b423e99ec924b4c` |
| `FAMILY_DESCENT.md` | `737cb82d8ddb4dab21909d0093c81919edd5e6c5384cec9ab72d49191e0aa0be` |
| `ANGULAR_TYPE_I.md` | `e1d81c2a6bd3daa5be7a7603369105780b7d6ca027e8fd4e200b754a5e0eab20` |
| `BALANCED_UNITARY_MOMENT_ADDENDUM.md` | `35448a3f2db447b3d493f39558b414594266ae2eb2bc2359d01193baaacf5636` |
| `BALANCED_UNITARY_INVERSE_ADDENDUM.md` | `590fef51aaf46e11c702099fd145444a58737f41d79607103c61f85c828d5e7c` |
| `verify_local_algebra.py` | `5a5e11da7da78e2b4002189752ffc67cf6dae81be13e8c43f3cff6beea8643ef` |

The final copied radial inverse addendum was read in full at the listed
hash. Its expanded generalized-eigenspace argument and annihilating
polynomial agree with the verification in Section 4 below. Its fixed
Bessel phase and precise source locators introduce no new analytic gap.

The source comparisons used Baiying Liu,
[arXiv:2610.26835v1](https://arxiv.org/abs/2610.26835v1), PDF SHA-256
`5d0fd10274c8444c789b0b7925a1cd3419017fe760be3219b6be51d7fbed9bd5`,
especially Sections 4--5, Lemmas 10.2 and 11.1, and the changed interfaces
in Sections 12--14. The Type-I author check used Dunn--Radziwiłł,
[arXiv:2109.07463v3](https://arxiv.org/html/2109.07463v3), particularly
(5.7), (5.13)--(5.14), Proposition 5.2, and (5.79), with the HTML hash
recorded in the Type-I file.

## 2. Independent checks of the pure-angular adapters

- **Archimedean vectors and constant terms.** The root-derivative
  construction stays in the source representation. The commuting
  holomorphic/antiholomorphic root operators justify the stated Weyl
  reversal. A zero local angular degree uses the spherical vector with
  first Mellin pole at \(-1/3\); every required contour remains strictly
  to its right. One nonzero local degree kills the global weighted
  constant-term integral by a circle action on the actual compact
  quotient. A product-shaped unit fundamental domain is unnecessary.
- **Global unit compatibility.** The definition
  \(L_S=\prod_{v\in S}\vartheta_v^{-1}\) gives
  \(L_S(A)=\vartheta((A)_S)\) and is trivial on S-units. Thus the
  infinity phases are not incorrectly required to be separately trivial
  on units. A common open kernel is needed only on finite local unit
  groups; no finite-order assertion on valuation phases is used.
- **Coefficient closure.** The cube power \(\nu(b)^3\) stays on the
  extracted cube variable. The two residual transforms change \(\nu\)
  only by the displayed finite corrections and whole-side conjugation.
  Source Lemma 11.1 explicitly retains
  \(L((RP)^2/(nb^3))=L(R)^2L(P)^2L(n)^{-1}L(b)^{-3}\), confirming
  separate row, tuple, and column phases. The periodic row matrices
  remain finite Kummer matrices.
- **Product-moment exceptions and conductors.** An infinite coefficient
  group is used only for membership and closure. Injectivity of the fixed
  nonzero infinity vector makes each realized exceptional list finite.
  Fixed-character means have no extra poles in the pure-angular family.
  Ordinary gamma shifts preserve the stated logarithmic small-scale
  bound. Moving primitive conductors and canceled-but-displayed radicals
  retain their charges. The prime bound correctly invokes the larger
  family allowing finite characters of arbitrary conductor.
- **Comparison and quantifiers.** The additive Gram factor in source
  Section 13 has auxiliary coefficient 1 and does not acquire the target
  infinity type. The positive prime normalizer has its target phases
  canceled in the original compensated operation. The reflected
  numerator remains finite order. Fixed infinity parameters can change
  constants and height orders without changing the shared numerical
  continuation boundary; the proof does not assert uniform constants as
  these fixed parameters grow.
- **Descent.** The abelian product identity has positive exponents.
  Nonzero angular type makes all factors entire, so a pole cannot cancel
  a zero. The zero-type case is separately finite order. If the base
  field does not contain the Eisenstein field, invariance under its
  relative Galois group excludes both Eisenstein resonance types.

The terminal cutoff in the inverse note was renamed \(d_0\) to avoid
conflict with the already fixed angular integer \(d\ge2\). Reversing
only that paragraph's change reproduces the formerly reviewed hash
`95a0025a2764c280c521b02e805c32307bd9716bfa32aac874becc312d3915d4`.
No new analytic condition was introduced by this correction.

## 3. Author check of the Type-I local calculation

For every real \(q\ge2\) and \(s\ge1\), each positive term in
\(F_q(s)\) decreases with \(s\), and direct simplification gives

\[
 F_q(1)=2-
 \frac{q^{5/2}-q^2}{q(q^{5/2}-1)}<2.
\]

Thus the printed bound \(F_q(s)\le3\) is valid on the entire stated
domain. This is an analytic inequality, not a finite sample check.

The two DR (5.7) branches give \(L=3n-1\) and \(L=3n\), with
multipliers \(3^{n/2+2}\) and \(3^{n/2+5/2}\). The \(L=-1\)
branches in (5.13)--(5.14) have multiplier 9. All are bounded by
\(3^{5/2}3^{L/6}|h'|\), as claimed. Reading the frequency scaling from
(5.79) avoids the repeated ramified power in the printed (5.67).

The short-divisor reduction's scalar includes the test and coefficient,
so its description was corrected from modulus one to uniformly bounded.
Reversing just that phrase recovers the previous frozen Type-I hash
`4129bc86bbfb786904c8bb2b7595a6c5c8e29845cd8fe7a9378489680b0c2bd2`.
The new hash in Section 1 includes that correction. Its bounds and
exponents are unchanged. Independent review of the Type-I analytic proof
is recorded by its separate reader, not by this author check.

## 4. Independent radial-interface check

The all-spherical angular case needs more than circle averaging. The
radial draft supplies the finite real Jacquet spectrum from the source
representation, and its unit-periodicity is preserved as follows.
For an archimedean norm-one element \(h_t\), define
\(T_t f(y)=f(h_t y)\). Since \(h_t\gamma=\gamma h_t\) for
\(\gamma\in U_S^6\), translation preserves the exact source
unit-invariance. Finite digit coefficients and finite class cutoffs do
not change. Any finite spectral projection polynomial in this
translation therefore preserves that invariance too.

An equivalent argument avoids projections altogether. For the weighted
constant term, choose small norm-one \(t\) with
\(g\cdot t\notin2\pi\mathbb Z\), possible for nonzero balanced
\(g\). Its finitely many Jacquet eigenvalues are
\(\lambda_j=\exp(A_j(t)-ig\cdot t)\ne1\), since \(A_j(t)\) is
real. A finite polynomial
\(P(T_t)=\prod_j(T_t-\lambda_j)^{n_j}\) annihilates the weighted
constant term, including generalized components. Haar invariance on
the compact quotient gives
\(P(1)\int f=0\), while \(P(1)\ne0\). Thus its integral vanishes.
This establishes the needed descent/projection compatibility without
assuming that each local real exponent is a global norm exponent.

The other radial interfaces were also checked: balancing excludes
nonprincipal pure-norm poles from each realized fixed list; the ordinary
gamma quotient has paired imaginary parts \(T+\rho_v\) and
\(-T-\rho_v\), so its exponential factors cancel; its new zero-line
residues have unit-modulus oscillations; and the degree-weighted average
of the real/complex radial parameters commutes with the specified base
change. No uniformity in growing fixed radial parameters is inferred.

These checks do not remove the two excluded balanced resonance types,
complete the mixed inverse/plain norm, or lower the numerical boundary
for the already covered finite-order family.

## 5. Independent inspection of the finite arithmetic checker

The listed `verify_local_algebra.py` was inspected and run once with
ordinary Python. It exited successfully and returned `accepted: true`.
It uses standard-library exact Gaussian rationals and rational interval
arithmetic. Explicit exceptions enforce acceptance; the checks do not
rely on assertions that disappear under Python optimization.

Its verified scope is appropriately finite: root-operator separation
in the two-factor complexified real Lie algebra, specified brackets
and Weyl/compact identities, the Gaussian example's nonzero determinant,
representative Mellin-shift substitutions, one quartic root isolated in
the displayed rational bracket, affine consequence intervals, rational
Type-I substitutions, and the cleared-denominator local-factor identity.
The Gaussian determinant rules out all proportional pairs in that
specific two-dimensional example; it is not sampling finitely many
powers. The derivative interval proves uniqueness inside the displayed
quartic bracket, not an assertion about all roots elsewhere.

For the local factor, the code checks the exact polynomial identity
after setting \(x=\sqrt q\). Positivity of its denominator and the
subtracted term for \(q\ge2\), and monotonicity in \(s\ge1\), are
the elementary analytic reasoning recorded in Section 3, not a claim
that the program sampled every prime. The representative Mellin shifts
do not certify the Bessel transform or its analytic estimates.

Both the program's documentation and its output explicitly exclude
certification of the exceptional representation, the source sieves,
the moment and continuation arguments, the tangent certificates, and
Dunn--Radziwiłł's analytic functional equation. No global analytic
certification is inferred from its successful run.
