# Review of the frozen structured-moment packet

Date: 23 October 2026.

**Status:** proposed component mathematics, with independent agent review
within the scopes recorded below. This is not an integration record,
external peer review, or a formal proof certificate.

## Frozen source and changes

- Repository: `GettysburgResearch/riemann`.
- Base main commit: `f99d9e3908dde4865377c75d9ca051c1f545bf4f`.
- Reviewed mathematical commit:
  [`c4332e23826a6c36b86e4f64cbde6cc1a0f641a0`](https://github.com/GettysburgResearch/riemann/commit/c4332e23826a6c36b86e4f64cbde6cc1a0f641a0).
- Reviewed root tree: `37ae75ba30b0ae0fbf93cb1e8ecf3c8be8743189`.
- All mathematical changes are additive under this directory.
- This subsequent commit adds only this review record. It does not change
  the reviewed proofs, checkers, saved outputs, or README.

The inherited external benchmark `B_flat = 0.874886647039964...` remains
unchanged. It is source-qualified to Liu, arXiv:2610.26835v1, Theorem 17.1.
The packet does not independently certify that preprint.

## Independent review records

The reviewer identifiers below identify separate agents in this research
session, not human reviewers or GitHub approval votes. Agreement between
agents does not replace the written arguments. Each reviewer fetched the
specified files at the frozen SHA, checked exact byte equality against the
locally audited versions, and verified the Git blob identities.

### Ordinary components: /root/boundary_sources

**Verdict:** no unresolved substantive finding within the stated ordinary
component scope.

The review covers all three ordinary proof notes and both ordinary
checkers. It reconstructs the finite-cover Gram and evaluation formulas,
the squared evaluation cost of order `R^3`, the explicit squared sieve
tail `96/R`, and the signed constant-term convolution. It also checks the
ordinary Fourier normalization and dilation identities, literal divisor
support, cutoff-uniform coefficient bounds, the Bessel integral with its
spectral-height factors, and the low-frequency lcm Mobius identity.

The frozen finite-cover note includes the required qualification that the
prime set contain every good prime of norm at most `R` when identifying
the Riesz correction with the summatory Mobius function.

Both frozen checkers were independently rerun in normal and optimized
Python. They passed 725 and 78,281 exact predicates, respectively, and
produced byte-identical normal/optimized output.

**Omissions:** the signed constant-term saving assumes the displayed prior
Mobius bound. The ordinary Fourier estimates keep the reciprocal zeta
factor and do not continue through unknown zeros. Their scope is the
specified ordinary spherical sector at cusp infinity. They do not supply
the growing-level metaplectic unfolding or the missing angular,
cross-cusp, puncture, and centered-diagonal terms. The induced series
`E[V_R^2]` is not identified with the product `|E[V_R]|^2`.

### Short-core and Gram/M2 deductions: /root/structural_attack

**Verdict:** no unresolved defect within the stated imported-input scope.

The review covers the arithmetic proof and checker, and the Gram proof.
The actual short-core selector is attached to `k=d'h'` independently of
the signed divisor and residual columns. The reviewer checked that this
preserves the common signed-profile argument. Retaining `d'|k` gives
the required reciprocal divisor density, including shared primes between
the sixth-free core and extracted sixth powers. The fixed excluded-prime
part remains present. All three interpolation weights are nonnegative,
sum to one, and cancel the `D,C,S` exponents, yielding the displayed
conditional bound and the endpoint `H^(2/3)L^(4/3)`.

The frozen arithmetic checker passed in normal and optimized Python with
identical output: 13,824 exact selector cases, 54 rational-boundary
reassemblies, and the displayed local and endpoint identities.

The Gram review covers both unequal overlap orientations, the distinct
sixth-power terminal case, their first and second means, the approximate
functional equation's common profiles and natural zeros, Kummer-row
ordering and sixth-power repetition, spectral-height uniformity, and the
Cauchy step. The last pointwise clarification is valid:
`A_1(p^t) <= C(t+1)` implies `A_1(j) << (Nj)^epsilon`.
The nonprincipal normalization is exactly
`(Q/Y^3) Y P = 1` for `P=Y^2/Q`. The real strips and reflected
boundary restriction are explicit in the frozen proof.

**Omissions:** the review does not independently certify the imported
unmarked M2 theorem, the periodic cubic functional equation, the external
zero-free theorem, or the source's complete inverse construction.
The principal `P^(1/6)` Gram term and the long-core signed complement
remain.

### Coprime Gram and README: /root/arithmetic_closure

**Verdict:** no blocking finding in the reviewed scope.

The review covers the frozen README, Gram proof, and Gram checker. It
rebinds the earlier coprime-pair audit to the exact final bytes and checks
the asymmetric contour choice, complete prime-power overlap factors,
their first and second means, and the M2 consumer in Sections 5--6.
The source comparison uses Liu v1's unmarked `z=0` clause in Theorem
12.14, its coefficient and height uniformity, and the approximate
functional equation and primitive-character identification in Section
14.2. The fourth-moment passage preserves the Kummer-row family, finite
unit sectors, conductor drops, and deleted-prime factors. The extension
through `j=u e^6`, central contours, and final `Q/Y^3` normalization
are consistent.

The frozen Gram checker passed in normal and optimized Python, with
identical output: 2,298 field correlations, 42 independent original-modulus
enumerations, six Euler-factor cases, and the exact direct-exponent example.

The README's Gram formulas, distinction between analytic inputs,
retained principal contribution, and unchanged boundary agree with the
audited note. Its short-core summary agrees with the separately reviewed
theorem and its restricted scope.

**Omissions:** the ordinary-sector proofs were outside this review.
The analytic source theorems are imported, not independently proved.
No smaller half-plane, full inverse estimate, independent certification
of Liu's theorem, or formal proof verification is established by this
audit.

## Root reproduction and finite coverage

The root agent independently ran all four checkers from the final local
bytes before publication:

```text
python3 -I -S -B <checker>
python3 -I -S -B -O <checker>
```

All eight runs succeeded. For each checker, normal and optimized outputs
were byte-identical and matched the saved report. Acceptance uses explicit
exceptions; optimization does not remove the acceptance gates. Relative
Markdown links were checked. Every uploaded blob SHA matched the Git blob
hash independently computed from the selected local UTF-8 content.
The root also verified the frozen commit's parent and tree and fetched its
README for exact content comparison.

| Checker | What the finite execution covers |
| --- | --- |
| Gram | 2,298 exact finite-field correlations, 42 independent original-modulus enumerations, six deleted-prime Euler-factor cases, and rational physical-exponent comparisons |
| Short core | 13,824 divisibility-selector cases, 54 rational-boundary reassemblies, local digit costs, zero masks, and normalization exponents |
| Finite cover | 725 exact rational predicates for finite representatives, orthogonality, evaluation, sieve norms, tails, and local convolution |
| Ordinary Fourier | 78,281 exact rational predicates for section coefficients, literal support, complete lcm cross terms, low-frequency agreement, and coefficient bounds |

The Gram example changes one admissible direct exponent from `1/5` to
`17/120`, a gain of `7/120`; the separate high-side inequalities are
not established by that example. These are finite diagnostics. They do
not certify infinite analytic continuation, imported moment estimates,
or any global zero-free theorem.

## Load-bearing scope and the remaining gaps

1. **Gram.** The deduction depends on the literal full local overlap
   identity and applicability of the source's unmarked ordinary-product
   M2 to the actual approximate-functional-equation columns, with their
   common profiles and natural zeros. Failure of that application would
   invalidate the central-line improvement. M2 is imported, not reproved.
   The surviving principal term is active at the inherited optimizer,
   where the old nonprincipal term was already inactive.

2. **Short core.** The local primitive-twist conductor costs and the
   three estimates must apply to the same signed truncated expression.
   The proof keeps that selector and common profile explicit. It estimates
   the specified nonzero transformed component, including restored
   principal pairs; separate restoration costs for the original inverse
   retain their own estimates. The positive long-core resource still
   returns a term of size `D`. An upper bound for the short-core part
   cannot be subtracted from a full upper bound to control that complement.

3. **Ordinary sector.** The exact divisor support and lcm cancellation
   yield the stated ordinary Fourier results with their reciprocal zeta
   factor. Applying them to the quartic inverse still requires the actual
   bilinear angular and cusp unfolding with the specified finite-section
   coefficients, row punctures, and arithmetic diagonal. No such bridge
   is claimed here.

No review recorded here establishes a smaller fixed zero-free half-plane
or RH. The five proof notes state the imported source versions and
normalization conventions; these source-qualified dependencies remain
part of every verdict.

## Content manifest at the frozen mathematical commit

Paths are relative to this directory. The manifest covers all 14 files
in the frozen mathematical packet; it intentionally excludes this later
review record.

| File | SHA256 |
| --- | --- |
| `README.md` | `b143880bfe16e11c4bfb4beaa40e8f99cae97cf26385dce0929ed0099fea9c6c` |
| `arithmetic/SHORT_CORE_CUBIC_TRANSFER.md` | `e9371c36235b41491dcb6f1a9db5ed085464328e0c842e70fb1e5cabdea39fef` |
| `arithmetic/check_short_core.py` | `76ebe4086d81f527807df1adb9511f09f7a28e83878ee1d8ed6cbb019b97735a` |
| `arithmetic/short_core_check_report.json` | `41cefb30011cbc4138dc32794688a40547a21e01e96106a5288136ffde5f0b99` |
| `gram/SIGNED_COPRIME_GRAM.md` | `a935813cb6e1729f24ca0107c9c0fff72c220c52137ef4d24106c35f3af3d6a8` |
| `gram/SIGNED_COPRIME_GRAM_CHECK.txt` | `9c30d5a930fb8198eb9ded1d64ebae6bf4eb58b3032894c13182366ac973a822` |
| `gram/check_signed_coprime_gram.py` | `9c2ba7710d2cbf5251433b51734b673f32dc4fa55cf3a2687ae62fb0f102cb73` |
| `ordinary/FINITE_COVER_AND_CUSP.md` | `d24f3d5a67ca4e508ee141487d39b9f3d5e84f0b47d0b4d0804f2288bc097ec9` |
| `ordinary/NONCONSTANT_ORDINARY_SECTOR.md` | `65d01c06a09eb5e21a9b6b46371cea7b0f394f778bbd3530a62159ae964e3d31` |
| `ordinary/ORDINARY_SIEVE_TAIL.md` | `5164bdc349ce6bd0a4d4d078369db095c577a4181fe4b6c978955cd9ea8c2a82` |
| `ordinary/ordinary_fourier_verification.json` | `c9fc95be6a52698df1e35192bb6077b65b6d8a9dcf053879539b84ae676e31ab` |
| `ordinary/verification.json` | `9bda0b61aed32259789c30372fb59a58b09b464c3ebe01918eb9793daa687b1c` |
| `ordinary/verify_finite_cover.py` | `5a69de0564c8ce1151a2d551b227b75bc416fd35f3ba6fcf2c6385ccafa5cb71` |
| `ordinary/verify_ordinary_fourier.py` | `6229a8e5fa7139e30e6c142357a948129c1e4db490264a7b9dad375a11ca26f3` |

