# Independent review: mixed cubic replication

**Verdict: PASS for the stated source-qualified component theorems.** The unequal-scale correction, fractional row norm, explicit sixth-moment incidence bound, restricted Hölder optimality statement, and Hermitian extension are consistent at the exact reviewed hash. The reviewer did not author the addendum. This is an internal AI-agent mathematical review, not external peer review or formal proof verification.

## 1. Exact review scope

Reviewed manuscript: `/workspace/scratch/6ec6134c1535/pass2_mixed_cubic_replication.md`.

SHA-256: `fb32d3a63704950be1d30228ec03a0ee1f157f23d1c7b24a8793886160fbb30b`.

Size: 19625 bytes.

Its frozen component dependency is `/workspace/scratch/6ec6134c1535/pass2_higher_balanced_cubic_pools.md`, SHA-256 `622cf846a961aed28ac0363f91766045f328c99700931621f123c17347c6bc23`. I checked the relevant physical-product lemma, all-row reduction, mixed-sign correction, fixed-test separation, exact incidence definitions, and the native-input scope in that file.

For the native second moment, pointwise premise, and test quantifiers, I also read the actual PR #921 file `standalone/2026-10-10-sextic-centered-covariance/HERMITIAN_INCIDENCE.md`, commit `4e6d4aa57ae4cb04d76b2b31279ac367951b469a`, SHA-256 `5c1844409097959a772916e1658ec61dfa747da857dd48321869d0a38cbc66e9`.

I independently fetched these pinned repository objects through GitHub during this review:

- PR #917, commit `6b4723042b3d250024eef45cb1924f88f28e902c`, `standalone/2026-10-10-oscillating-overlaps-and-averaged-moments/OSCILLATING_OVERLAPS.md`, Git blob `aa3137869abcee4b380bb0b621e56e93e2072d71`. Its Theorem 2.1 is the all-row cubic sieve with the actual cube-copy term and nonunit mask.
- PR #923, commit `1a1152008706f7e24fa1efe4990588f8f99c5d8d`, `standalone/2026-10-10-sextic-separated-cores/SUBSET_PRODUCT_INCIDENCE.md`, Git blob `f3e4eb59a3f8ffb1c742de5a627704f169d7cc00`. Its Section 5 fixes the same triangle and proves the predecessor excess \(623/720\) for the entire one-sided portion, after summing its shared pair ideals.

The classical squarefree cubic large sieve, imported native second moment, and optional uniform pointwise premise remain analytic dependencies. The review checks the new deduction from them; it does not independently prove those analytic foundations. In particular, \(\beta=7/8\) retains the stated uniform reciprocal/zero-free premise. No native inverse moment above order two is assumed.

The earlier review `pass2_spectral_root_review.md` is unchanged. This report concerns the separate mixed-replication addendum only.

## 2. Physical products and the exact Hölder identity

The relevant cubic polynomials have the actual positive squarefree coefficient and literal row character \(\chi_n(u)^2\), or uniformly its conjugate power four. For every fixed integer exponent vector \(e\), their physical product includes collisions between copies. Freezing repeated incidence ideals leaves a disjoint singleton product with squarefree column, row-independent coefficient, and squared coefficient mass bounded by its product length times a divisor loss.

The all-row cubic sieve then gives, at product length \(M\),
\[
\|P_e\|_{2,H}^2
\ll D^\epsilon[HM+H^{1/3}M^2+H^{2/3}M^{5/3}].
\]
The square-root length weights are \(1/2,1,5/6\). Repeated ideals of multiplicity at least two therefore have summable weights, except for the first term's pair incidences, whose finite harmonic logarithms are absorbed. This applies to every fixed number of integer copies and does not assert a new higher native Möbius moment.

For cyclic replication entries \(m_j\ge0\), total \(d\ge s\), every column of the replication matrix has sum \(d\). Consequently
\[
\prod_{t=0}^{s-1}P_t=U^d,
\qquad
\prod_{t=0}^{s-1}M_t=R^d,
\qquad U=\prod_{j=1}^sU_j.
\]
Both are algebraic identities, including when some polynomial value is zero. Hölder applied to \(\prod_t|P_t|^{2/s}\) gives
\[
\|U\|_{2d/s,H}
\le\prod_t\|P_t\|_{2,H}^{1/d}.
\]
Applying the physical-product lemma gives exactly
\[
\|U\|_{2d/s,H}^2
\ll D^\epsilon H^{s/d}R^2
\prod_t\rho(H,M_t)^{1/d},
\]
with \(\rho(H,M)=M^{-1}+H^{-2/3}+H^{-1/3}M^{-1/3}\). This proof is valid for unequal physical scales. Equality of the original pair scales is used only in the later numerical corollary.

All row classes supplied by the cubic source remain included: six units, repeated good and bad prime powers, and cube copies. At a cube prime the character is a principal nonunit mask; it is never replaced by the constant one. The argument also preserves all collisions in each of the three five-factor products in the triangle example.

## 3. Native interpolation and the arithmetic correction

For \(d>s\), set \(p=2d/(d-s)\). Interpolating a native second moment with its separately assumed pointwise bound gives
\[
\|A(Y)\|_{p,H}
\ll D^\epsilon H^{(d-s)/(2d)}Y^{1/2+as/(2d)},
\qquad a=2\beta-1.
\]
The reciprocal row exponents add correctly:
\[
\frac1p+\frac{s}{2d}=\frac12.
\]
At \(d=s\), this is the pointwise endpoint and requires no native second moment. The estimate remains at the same ambient physical row height for every shortened scale; no different or selected-row native theorem is being inserted.

The original singleton and pair variables must be mutually coprime. Their prime signs differ: \(-1\) on native singleton axes and \(+1\) on positive squarefree pair axes. The exact local correction is
\[
\frac{1+\sum_j\sigma_jz_j}{\prod_j(1+\sigma_jz_j)}.
\]
For a nonconstant monomial of support \(I\), its coefficient is
\[
(1-|I|)\prod_j(-\sigma_j)^{e_j}.
\]
At an excluded prime the numerator is one. Thus one-axis correction terms vanish outside the moving exclusion, and the absolute coefficient family is the same one used in the frozen finite-horizon correction lemma. The exterior character phases retain their nonunit zeros. Applying a norm contraction to those exterior factors is valid; deleting the original arithmetic columns from a native sum is not asserted to be a contraction.

Fixing a correction vector shortens every scale separately. For the \(t\)-th physical-product norm, choose one of its three length exponents \(\alpha_t\in\{1/2,1,5/6\}\). The exact correction weight of pair variable \(j\) is
\[
w_j=\frac1d\sum_t m_{j+t}\alpha_t
\ge\frac1{2d}\sum_t m_{j+t}=\frac12.
\]
This verifies every one of the \(3^s\) terms, including all 27 terms when \(s=3,d=5\). The selected singleton weight is \(1/2+as/(2d)\), and the others have weight \(\beta\); all are at least one half. The finite-horizon correction therefore costs only \(D^\epsilon\), even at the critical weights. This is not a claim of absolute Euler-product convergence at one half: the proof increases the weights slightly, pays the finite polynomial horizon, and bounds the moving mask by a subpower factor.

After summing the correction by Minkowski, the finite expansion can be recombined into the original unshifted brackets up to a fixed constant. The identities \(\prod_tM_t=R^d\) and \(R^2XT=D^k\) then give
\[
\|F_{\mathbf c,\mathbf R}\|_{2,H}^2
\ll D^\epsilon HD^kT^{-1}
X^aX_i^{-a(1-s/d)}
\prod_t\rho(H,M_t)^{1/d}.
\]
This confirms the general theorem, not merely its equal-scale specialization.

## 4. Fixed tests and moving parameters

I checked the location of the Mellin separation. Before the arithmetic correction, the original fixed coupled weights are separated with smooth singleton cutoffs equal to one on their entire forced support. The resulting native tests are smooth, with finite seminorms growing polynomially in the Mellin frequencies. The pair tests have hard dyadic endpoints but only their sup norms enter the classical cubic lemma.

Every physical replication is a literal copy of one of these separated tests. After extracting a correction ideal, the normalized test is unchanged and only its scale is shortened. No hard endpoint is inserted into a native inverse test, and no unbounded moving infinity type is silently supplied to a native theorem. Rapid decay of the original Mellin transforms integrates all fixed frequency costs.

The number of copies, the moment order, and the replication vector are fixed independently of \(D\). Therefore all resulting product lengths, conductors, divisor orders, seminorm orders, and finite correction horizons remain within fixed polynomial bounds. Empty shortened scales vanish; nonempty subunit scales lie in a fixed compact interval and cost constants only.

## 5. Exact triangle and comparison

For \(s=3,d=5\), the vectors \((1,2,2),(2,1,2),(2,2,1)\) each describe a genuine five-factor cubic product. The pair product is estimated in \(L^{10/3}\); the selected native factor is estimated in \(L^5\), by interpolation only. Its scale exponent at \(\beta=7/8\) is \(29/40\), and its height exponent is \(1/5\).

At
\[
h=\frac{21}{20},\qquad r=\frac5{24},\qquad
\beta=\frac78,
\]
one has \(X_i\asymp D^{7/12}\), \(X\asymp D^{7/4}\), and \(M_t\asymp D^{25/24}\). The three \(\rho\)-exponents are
\[
-\frac{25}{24},\qquad-\frac7{10},\qquad-\frac{251}{360}.
\]
The third is largest. The resulting normalized excess is exactly
\[
\frac{21}{16}-\frac7{40}-\frac{251}{600}
=\frac{863}{1200}.
\]
The gains are
\[
\frac{119}{160}-\frac{863}{1200}=\frac{59}{2400},
\qquad
\frac{623}{720}-\frac{863}{1200}=\frac{263}{1800}.
\]
The comparison is between complete one-sided triangle portions and their entire squared row norms. The preceding \(623/720\) quantity was checked against its actual pinned source, including that source's summation over the pair ideals. It is not a comparison with an unsummed fixed core.

The excess is still positive. This is a stronger estimate for a genuine sixth-moment incidence portion, not a diagonal bound for the entire sixth moment.

## 6. Review of the restricted optimality statement

The addendum's Section 5 restricts its comparison to direct Hölder products of physical integer-monomial cubic \(L^2\) bounds, optional cubic pointwise counting, and interpolated native second moments. I independently derived its optimization formula in this precise class.

Let \(t_e\) be the exponents placed on the cubic monomial norms, and let their degrees be \(n=|e|\). Pair-variable coverage gives \(\sum_e t_e e_j\le1\), with any remaining part bounded by pointwise counting. Hence \(\sum_e t_en\le3\). The native Hölder budget depends only on \(\sum_e t_e\), because all three native scales are equal in this example. Dividing by the target normalization, the excess is
\[
\frac78+\sum_e t_e\left(\frac7{16}+\delta_{|e|}\right),
\]
where \(\delta_n=\max(-5n/24,-7/10,-7/20-5n/72)\). This is exactly the convex combination in the addendum:
\[
\sum_e\frac{t_e|e|}{3}E_{|e|}
+\left(1-\sum_e\frac{t_e|e|}{3}\right)\frac78.
\]
The three integer-degree formulas are correct. Degrees 1 and 2 give \(1/4+21/(16n)\); degrees 3,4,5 give \(2/3+21/(80n)\); and degrees at least 6 give \(7/8-63/(80n)\). Their minimum is \(E_5=863/1200\). Treating degrees 1 and 2 as algebraic ingredients in a mixed allocation, rather than standalone inadmissible native exponents, is appropriate.

The formal real-\(q\) bracket has its minimum at \(q=42/25\), with value \(23/32\), but that substitution is not supplied by the integer physical-product theorem. Its gap from the proved value is \(1/2400\), as stated. Interpolation between the full product's integer norm endpoints gives a geometric mean of the complete endpoint costs and cannot establish that lower formal value.

Thus the restricted optimality claim passes. It is not a general impossibility theorem for additional arithmetic cancellation, a new row partition, or a different treatment of the incidence pattern.

## 7. General selectors, Hermitian blocks, and Schwartz rows

For a fixed finite list of replication vectors, minimizing the proved costs on complete incidence portions is legitimate. The pair ideals remain inside the physical sums, so only their dyadic profiles are counted externally. The frozen higher-incidence weights are \((Nc_I)^{-|I|/2}\) with \(|I|\ge3\), and their ideal sums converge. This gives the claimed selector bound. No arbitrary subfamily of a signed native polynomial is removed.

For the Hermitian version, the row exponents are exactly
\[
\frac12+\frac{d-s}{2d}+\frac{s}{2d}=1.
\]
They correspond to one native \(L^2\), one interpolated native \(L^p\), and the fractional cubic-product norm. The pair correction weights above are unchanged, the full native axis has weight one half, other odd axes have their stipulated pointwise weight, and other even axes are counted. The finite correction still applies. The selected cubic group has a common orientation modulo six; opposite cubic orientations are not merged into one squarefree column.

Relative to the earlier two-native bound, the new factor is precisely
\[
\left[Q_L^{as}\prod_t\rho(H,M_t)\right]^{1/(2d)}.
\]
No third full native second-moment saving is hidden in this formula, and a quadratic odd pattern is not granted an eligible sextic native second moment.

The squared one-sided monomial height powers are \(1-s/d+\sum_t\tau_t/d\), \(\tau_t\in\{1,1/3,2/3\}\), hence at most one. The analogous Hermitian powers are \(1-s/(2d)+\sum_t\tau_t/(2d)\), also at most one. The source's annular reference-scale adapter therefore applies with the original columns, masks, and selectors fixed, and with sufficiently decaying fixed Schwartz row majorants. It requires the inherited native and pointwise uniformity at every enlarged reference scale, as stated.

## 8. Finite diagnostic and final scope

The complete independent producer is `/workspace/scratch/6ec6134c1535/pass2_spectral_mixed_replication_checks.md`, SHA-256 `282af81c7416443499cc1cce5c6a1ea78bd4bafa370c13cb2d8c88c8fee0c60a` (5655 bytes). It checks:

- All 27 triangle monomials and all 81 pair-weight inequalities before any equal-shortened-scale assumption.
- All 1458 truncated mixed-sign Euler coefficients, for six axes through exponent two, with and without a mask prime.
- Three finite Hölder data sets including zeros, and a negative control showing that an imbalanced replication matrix fails the critical pair-weight requirement.
- The exact excess, both displayed gains, the native interpolation exponents, and agreement between the monomial maximum and the normalized \(\rho\) formula.

Ordinary Python and `python -O` produced identical report bytes, SHA-256 `56ddde4b1ef81cc48ebe599632a0b8ed11a580066eea5a6998e6b91494b9646c` (5372 bytes). These are finite algebraic checks, not certification of an analytic theorem or a complete residue census.

No defect remains at the reviewed manuscript hash. The native and pointwise premises retain their exact source qualifications and height/test domains. The strengthened incidence selector does not control the all-singleton balanced core, the full sixth moment, the signed long-range first-Poisson covariance, the cofinal generalized moment hierarchy, or a new zeta zero-free boundary. The addendum states those limits accurately.
