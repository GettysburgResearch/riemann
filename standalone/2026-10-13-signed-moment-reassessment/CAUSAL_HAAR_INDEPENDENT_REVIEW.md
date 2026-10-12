# Independent review of the causal classification and Haar moment theorems

**Verdict:** PASS at the exact mathematical scope of the source identified
below. I reconstructed the complete argument and found no unresolved
mathematical gap. This verdict also covers the separately authored compact-test
supplement identified below. This is a paper review with exact finite algebra checks,
not a formal verification or a proof of an arithmetic moment estimate.

**Reviewer:** `determinant_independent_review`, a fresh reviewing agent.
The source was authored by `replica_bootstrap_attack`; `root` and
`signed_family_attack` contributed to its constructive converse. I did
not author that source or participate in those constructions. I read the
actual source and derived the load-bearing steps independently. This
disclosure records independence of the review task; it does not represent
human review or independence between model families.

The additional compact-test supplement was authored by `root`. I did not
author or edit it. I reviewed its complete proof and requested the explicit
imprimitive-mask normalization recorded in Section 5 below.

**Review date:** October 12, 2026, UTC.

## 1. Exact source and receipt boundary

| Item | Identity |
|---|---|
| Mathematical source | [CAUSAL_ORBITS_AND_DENSE_LIFTS.md](CAUSAL_ORBITS_AND_DENSE_LIFTS.md) |
| Bytes | 44,355 |
| SHA-256 | `dc8f645731302f2e2059cd115cc70564409af98c08c48a3f30f7d081c917a817` |
| Checkout baseline during review | `97bf40329489992e9384c34d7595af6d01a40774` |
| Source publication status during this pass | Proposed working-tree source; a published-commit receipt is a separate subsequent step |

| Additional source | Identity |
|---|---|
| Compact-test supplement | [COMPACT_TEST_HAAR_MOMENTS.md](COMPACT_TEST_HAAR_MOMENTS.md) |
| Bytes | 7,939 |
| SHA-256 | `49f623d831ae196aab9d1d7e7edd44419999c6995115faa983406da7c3099b23` |
| Scoped editorial synopsis | [README.md](README.md), SHA-256 `a1fdc9f5a7475785a13bda2543006433fec2fcf50737aad12f4d58fd9c930328` |

The synopsis check covers Sections 4 and 5 and the final compact-test
discrepancy comparison in Section 6. I checked these passages against the
reviewed proofs. The trace, collision, moving-contour, and historical
claims elsewhere in that README are not covered by this review.

The review began on the earlier file hash
`a6dcbceeaa4457d87ef17b311284bea56e57ed54f6ce1981d5e27c35b10c417c`.
Before completing it, I read the final source identified above in full,
including the clarification that each *local* mean is nonzero, the PR #911
source credit, and the additional rank-one comparison. The present verdict
is bound to the final hash, not to an unspecified later head. An immutable
local copy was used to check that the proof remained unchanged during the
last verification pass.

I followed the distinction in `AGENTS.md` and `docs/REVIEWING.md` between a
content review, a published exact-commit receipt, and integration. This
report supplies the first of these. It does not declare repository-wide
integration or approve other files by association.

## 2. Approved mathematical scope

The causal theorem classifies fixed dilation measures on `[1,infinity)`
with finite **weighted total variation** at some exponent
`0 < sigma_0 <= 1`. For the fixed radial source, the reachable primitive
characters are precisely the source character and its field conjugate.
The resulting rows occupy at most two Kummer classes, or at most four if
complex conjugation of the sum is additionally permitted, and have
cardinality `O(H^(1/6))`. This does not classify every bounded operator or
exclude an argument exploiting cancellation outside total variation.

For the independently defined local Haar model, every fixed even Gaussian
moment has the stated `D^(k+epsilon)` bound unconditionally when the
representation has no invariant vector. When the invariant multiplicity
`m_0` is positive, the assertion for any one fixed `k >= 1`, with every
positive loss, is equivalent to zero exclusion for the fixed target
Hecke L-function in `Re(s) > 1/2`.

The theorem is neither a transfer to the finite physical row measure nor
an unconditional estimate for the regular sextic representation. The
invariant-free rank-one model includes the Haar comparison for the
original Möbius/sextic coefficients; its arithmetic transfer remains open.

For every fixed smooth compact norm test, the same sufficient moment
bounds hold under the corresponding hypotheses. When `m_0>0`, the
assertion for the **entire compact-test class**, even just the
nonnegative real tests, at one fixed order and every positive loss is
equivalent to target zero exclusion. This permits constants depending on
each test. A converse for one arbitrary compact test is not asserted.

## 3. Reconstruction of the causal argument

### Gaussian source and uniqueness of the measure

I checked the sign and scaling of the Mellin identity directly:
substitution in `G(Nn/D)` produces `(Nn)^(-s) exp(s^2/2)`.
Ideal counting bounds the absolute Gaussian sum by `O(D)`, and the
Gaussian tail gives every positive power of `D` at small scale. Therefore
the double Mellin interchange in Lemma 2.1 is justified at a real
exponent larger than both one and the variation exponent. It does not
assume the sought integrability at a critical exponent.

The Euler quotient has an absolutely convergent Dirichlet series there,
with coefficients grouped by rational-integer norm. Weighting the
difference of candidate measures and pushing it under `t -> 1/t` gives a
finite complex measure on `[0,1]`. Its moments of every nonnegative
integer order vanish, including order zero. Polynomial density then
proves uniqueness. This genuinely rules out an additional continuous
measure with the same transform; it is not merely uniqueness within the
discrete ansatz.

### Prime coefficients and field conjugation

At an undeleted unramified rational prime, the quotient coefficient is
`c_p = a_r(p) - a_u(p)`. I checked the sign against the reciprocal Euler
factors. The coefficient is zero at inert primes and is the difference
of the sums over the two norm-`p` prime ideals at split primes.

Passing to a finite Galois closure over the rationals makes these sums
the characters induced from the two one-dimensional characters of the
index-two subgroup. A nonzero difference of induced characters is
nonzero on some conjugacy class. Chebotarev then forces a prime harmonic
divergence of the absolute coefficients, contradicting the assumed
variation at `sigma_0 <= 1`. Restriction to the subgroup and character
orthogonality identify the two character multisets, including the case
of repeated constituents. Consequently the remaining ambiguity is
exactly field conjugation.

This step must use norm-grouped coefficients. It would be incorrect to
infer individual ideal-character equality directly from the radial
sum. The source correctly retains the conjugate alternative. The
converse follows because the surviving quotient is a finite product of
Euler factors and their inverses, absolutely summable at every positive
weight. Gaussian absolute convergence justifies its coefficient
convolution. I also checked the exponent-one sharpness and the fixed-pair
lower bounds in (3.7); their constants and thresholds are not asserted to
be conductor-uniform.

### Kummer classes, units, and the count

The residue-symbol quotient for two rows is the Kummer character of
their ratio. The unramified Kummer-Artin identity and Chebotarev imply
that equality off finitely many primes is equivalent to the ratio being
a sixth power in `K`. With the coefficient datum fixed, each admissible
primitive character therefore determines at most one Kummer class.

I checked the potentially delicate unit count. In the Eisenstein field,
the class number is one and every unit has sixth power one. Removing
ideal valuations in multiples of six gives a unique integral
representative with valuations between zero and five, retaining its
unit. Its integral rows are exactly `r_0 v^6`. A negative valuation of
`v` cannot give an integral row. Different ideals `(v)` give different
rows, while all six generators of one ideal give the same sixth power.
Thus the count is the ideal count at `(H/Nr_0)^(1/6)`, with the stated
`H^(1/12)` boundary error. No coprimality restriction on `(r_0,v)` is
introduced.

The four-class statement follows by separately conjugating character
values. For `nu=1`, the field-conjugate partner is the class of
`conjugate(r)^(-1)`, not merely the class of `conjugate(r)`. Finally,
the weighted Hölder calculation gives the claimed cardinality cost
`H^(5/(12k))`; the source correctly describes this as a limitation of
that extraction from a moment budget, not a lower bound on actual sums.

## 4. Reconstruction of the determinant and moment argument

### Physical dense product and its masked Haar mean

The six-factor physical product contains the target reciprocal in its
`j=0` factor, including that factor's deletion at a prime dividing the
row. In the open critical strip, the other reciprocal Hecke factors
cannot cancel a target pole: their L-functions have no poles there, and
the finite Euler corrections are nonzero. Repeated twists of order less
than six cause no exception.

For a general finite-group representation, the determinant coefficients
are exterior-power traces. Averaging is projection onto invariants.
Splitting off the invariant subspace produces
`P_rho(x)=(1-x)^m_0 Q_rho(x)`, with `Q_rho(0)=1` and no linear term.
The exact deletion law gives

\[
\frac{\Phi_{\rho,q}(x)}{(1-x)^{m_0}}
=\left(1-\frac1q\right)Q_\rho(x)
 +\frac1q(1-x)^{-m_0}.
\]

Hence its deviation from one is
`O(q^(-1)|x|+|x|^2)`. The resulting error sum converges on each closed
half-plane strictly to the right of one half. A fixed small-prime
deletion ensures local nonvanishing, and normal convergence gives the
nonzero holomorphic factor `H`. I checked the finite Euler correction
and its sign. The mean identity starts in `Re(s)>1`; its continuation
`H/L^m_0` is only meromorphic without zero exclusion when `m_0>0`.

### All normalized even moments

The important centering is exact: for `W_p=Z_p-1`, one has
`E W_p=0` and `|W_p|=O(q^(-Re(s)))`, uniformly in the local outcome.
For every fixed `0 <= j,l <= k`, all degree-one terms in
`E[(1+W_p)^j(1+conjugate(W_p))^l]` vanish. The remaining error is
`O(q^(-2 Re(s)))`. Independence first yields uniform boundedness of the
finite-product `2k`-th moments.

Boundedness alone is not the whole convergence argument. For a product
`Y` over a tail set, I independently expanded
`(Y-1)^k (conjugate(Y)-1)^k`. Its mixed moments are each one plus an
error controlled by the same prime-square tail. The contributions of
all the ones cancel because the signed binomial sum is
`(1-1)^(2k)=0`. This proves the asserted Cauchy estimate

\[
\|X_{\mathcal Q}(s)-X_{\mathcal P}(s)\|_{2k}^{2k}
\ll_{\rho,k,\alpha}
\sum_{\mathfrak p\in\mathcal Q\setminus\mathcal P}
 (N\mathfrak p)^{-2\alpha},\qquad \Re s\ge\alpha>1/2.
\]

Comparison through unions handles different finite-set exhaustions.
Locally uniform convergence in the Banach space preserves holomorphy;
continuity of expectation gives `E X=1`; uniqueness in `L^2` identifies
the limits for different fixed orders. No assertion of uniformity in
unbounded `k`, and no almost-sure convergence theorem, is needed.

### Reciprocal growth and Gaussian Mellin shift

For the fixed character, cancellation of complete residue cells on the
Eisenstein lattice gives an `O(sqrt(x))` ideal-character sum. Partial
summation gives polynomial vertical growth of `L` in the required
half-plane. In the principal case the source first removes the pole by
using `(s-1) zeta_K(s)/(s+1)`. I checked that its value at one is nonzero
and that the rational factor is bounded in the right half-plane.

Under zero exclusion, an analytic logarithm exists. The
Borel--Carathéodory disks in Lemma 7.3 stay strictly within that
half-plane, and their center values on `Re(s)=2` are bounded by the
Euler logarithm. This gives logarithmic growth of the logarithm and
therefore a fixed-character polynomial reciprocal bound. The proof
does not reuse a fixed-character constant for moving conductors.

The function `F=(H/L^m_0) X` agrees with the original Dirichlet series
in `Re(s)>1` and has the required Banach-valued analytic continuation
under exactly the stated hypotheses. The coefficient majorant
`d_(d,K)` justifies absolute Gaussian inversion on that original line.
Polynomial vertical growth makes the horizontal rectangle integrals
vanish against the Gaussian, and both vertical Bochner integrals
converge in norm. The shifted line gives
`||B(D;G)||_(2k) << D^alpha`; taking
`alpha=1/2+epsilon/(2k)` proves sufficiency.

**No convergence of the raw finite Euler products below one is used
when `m_0>0`.** Local mean nonvanishing and convergence of normalized
products do not supply that assertion. This distinction is explicit in
the reviewed source and is essential to the proof's validity.

Conversely, any one fixed even moment implies the second-moment bound
by Hölder. Jensen, the low-scale tail, and all positive losses make the
mean Mellin integral holomorphic for `Re(s)>1/2`. Its meromorphic
identity has numerator `exp(s^2/2) H(s)`, which is nonzero there.
A target zero would therefore force a pole. The principal pole at one
produces a reciprocal zero and is correctly harmless.

### Sextic examples

I verified the regular `C_6` polynomial in two distinct exact ways:
expansion by element orders and counting subsets of the six character
weights whose sum is zero modulo six. They both give coefficients
`[1,-1,2,-4,3,-1,0]` and exterior invariant dimensions
`[1,1,2,4,3,1,0]`. The reduced representation gives dimensions
`[1,0,2,2,1,0]` and polynomial `1+2x^2-2x^3+x^4`.

For the rank-one sextic representation, distinct squarefree ideals have
a prime present on exactly one side, so their mixed coefficient
expectation vanishes. Equal ideals contribute exactly the product of
`1-1/q` over their prime divisors. This checks the mask in (7.24), not
just the unmasked diagonal. Squaring the Gaussian still permits the
elementary `O(D)` ideal-count estimate. The complete-residue CRT law
does not make the actual short row ball uniform.

## 5. Independent review of the compact-test supplement

I read the complete final supplement at the hash in Section 1. Its
Theorems 1.1 and 2.1 and its exact discrepancy reformulation pass at
their stated scope.

### Compact-test sufficiency

For `W` smooth and compactly supported in `(0,infinity)`, substitution
`y=exp(x)` makes its Mellin transform an integral over a fixed compact
interval. Differentiation under that integral proves entire dependence,
and integration by parts gives arbitrary polynomial decay in the
imaginary direction, uniformly on a closed real strip. The coefficient
majorant from the main source justifies Bochner inversion on `c>1`.

The same continued `F` used in the Gaussian proof has polynomial
vertical growth. Choosing the transform's decay order `N>A+2` makes
both vertical integrals norm-convergent and the horizontal rectangle
integrals tend to zero. The shifted line yields `D^alpha` in `L^(2k)`
and hence the stated moment bound. This works for complex tests and
does not require their Mellin transforms to be nonzero.

### Converse for a class of tests

For one fixed compact test, the mean vanishes identically at sufficiently
small `D`. Its assumed even-moment bound supplies the large-scale Mellin
integrability for every real part greater than one half. The resulting
holomorphic integral equals `Mellin(W)(s) H(s)/L(s)^m_0` initially to
the right of one.

Given a hypothetical target zero `z=beta+i gamma`, choose one fixed
nonnegative nonzero bump `phi` on a log interval of radius
`pi/(4(1+abs(gamma)))`, and set `W(y)=phi(log(y))`. On its support
`cos(gamma x)>0`, so

\[
\Re\widehat W(z)
=\int\varphi(x)e^{\beta x}\cos(\gamma x)\,dx>0.
\]

This prevents cancellation of that zero in the Mellin numerator and
gives the required contradiction. Dependence of this test on a
hypothetical zero is legitimate under the premise covering every fixed
test. The test does not change with `D`, and no bound uniform across all
tests is needed. The source correctly refrains from this conclusion for
one arbitrary compact test, whose transform may vanish at a target zero.

### Native normalization and discrepancy

For the rank-one sextic representation every local mean equals one, so
the artificial small-prime deletion needed for general representations
is unnecessary. I requested one explicit normalization clarification:
if the native coefficient datum is imprimitive, all primes where its
zero extension differs from its primitive inducing character must be
included among the fixed exclusions. Adding these primes does not
alter the physical coefficients, because their columns already have
coefficient zero. The final supplement states this and thereby matches
the Haar benchmark to the literal native coefficient source.

For the nonnegative Schwartz row weight, lattice counting gives
`Z_H=O(H)` for `H>=1`. Compact support gives a finite column sum
uniformly in the row, and the row weight is summable, so the displayed
physical moment and discrepancy are well defined. The proved rank-one
Haar bound makes the reference term `O(H D^(k+epsilon))`. Therefore
the physical upper bound and the absolute discrepancy upper bound are
equivalent for precisely the same `W`, `D`, `H`, and row weight: use the
triangle inequality in one direction and add the reference term in the
other. This is an exact reformulation of an open estimate. It is not a
proof that the discrepancy is small. The optional implication to the
hard row ball correctly requires the weight to majorize that ball and
does not claim the reverse implication from one hard cutoff.

The specified README scope passages preserve all these distinctions,
including the compact-test class quantifier, the Gaussian single-test
equivalence, and the absence of a physical discrepancy bound.

## 6. Exact sources inspected and actual checks

I read both complete proposed proof notes, reconstructed the arguments above,
and checked the following necessary inputs or comparison boundaries:

| Source | Exact identity and material checked |
|---|---|
| PR #929, Gaussian source | Commit `97bf40329489992e9384c34d7595af6d01a40774`; Sections 1 and 6, including primitive reciprocal formula (6.14). Both the git blob and resident file have SHA-256 `53625b2fc8da8162792bb40cbb329cd609ddf152d362f05fad32ac7b841d41d4`. |
| PR #913, general moment source | Commit `6498d6cc2eded03159c7332b25fd224ad07f89c1`; Section 6, including the exact replica convention and pure Hölder/cardinality scope. File SHA-256 `a4ca15c0d731ef6000b19507b39b64a4786a7f8af9939864b3176221bf02b499`. |
| PR #913, fourth-moment source | The same commit; Section 8's lattice and analytic-logarithm adapter. File SHA-256 `354e8f7f5f81d0f8821ea6e821f55546f9c9641ac0690def1ae373000b4b3d08`. Only the fixed-character polynomial part is needed here and was reconstructed. |
| PR #911, CRT source | Commit `2f8b6a3898a722d0602a91dea73bac344a3bb7dd`; actual `MOBIUS_CRT_TRANSLATION.md`, SHA-256 `bde2f3a2c15aa514fdf51a5c0956691170633aa6d79427b7dc3a7f7ff6412710`. Checked finite-field/CRT identities and the complete-residue versus short-row distinction. |
| PR #927 comparison | Commit `f9939c957f5aac6b2099b591e4988991700a152b`; inspected the actual physical-polynomial-copy interpretation and Section 7's retained all-singleton obstruction. This is a scope comparison, not a dependency of the new Haar theorem. |
| PR #916 comparison | Commit `dd70e580a5ffdbe5b140784ba6cebd173cb84792`; read `DEFECT_BOOTSTRAP.md`. The reusable fractional saving is an explicit additional arithmetic premise. No such saving is imported into this proof. |

I also opened the cited author-hosted classical sources. Stevenhagen's
[November 7, 2002 notes](https://websites.math.leidenuniv.nl/algebra/cft.pdf),
3.1 and 3.10, give the Kummer duality and unramified Artin-symbol
interpretation used here. Milne's
[Class Field Theory, version 4.03](https://www.jmilne.org/math/CourseNotes/CFT.pdf),
dated August 6, 2020, has Chebotarev at V.3.23 and VIII.7.4, and the
prime-count formulation at VIII.7.5. The statements match the needed
fixed-extension density input. I did not re-prove class field theory or
Chebotarev, and I did not obtain content hashes for those external PDFs.

The executed checks were read-only git/blob inspection, SHA-256 and byte
comparison, and an independent inline Python calculation using exact
integers and `Fraction` for the two `C_6` polynomial derivations. The
signed mixed-moment constant sum was also checked exactly at orders
`k=1,...,16`; the all-order conclusion rests on its algebraic binomial
identity, not that finite check. No contributed numerical or proof
checker was executed.

## 7. Omissions and remaining mathematical obligations

There is no zero census, finite physical-row experiment, proof-assistant
build, or replay of the imported quasi-Riemann theorem in this review.
I have not reviewed the full earlier packets merely because their
comparison passages were inspected. Their unrelated claims retain their
own status and reviews.

The first unresolved arithmetic obligation remains an estimate carrying
the independent Haar benchmark to the literal finite row measure, or a
new source-specific estimate on the invariant part of the dense family.
The present review supplies neither. It also supplies no boundary-line
`Re(s)=1/2` convergence, no constants uniform in an unbounded moment
order or a moving conductor, and no classification of operators outside
the stated weighted-variation class.

Within these boundaries, I found no missing inference in the causal
classification, either direction of the Gaussian Haar-moment theorem,
the compact-test sufficiency and test-class converse, or the exact
physical-discrepancy equivalence. A change to either proof note requires a new exact-source review;
the later published-commit receipt must verify the hashes above.
