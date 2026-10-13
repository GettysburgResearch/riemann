# Principal-zeta bridge: a structural rethink of the moment program

**Status:** proposed proved source identities, operator estimates, conditional capture theorems, and obstructions to specific positive estimates. The missing arithmetic capture inequality is **OPEN**. This packet proves no new full moment, no `17/24` zero-free result, no height-dependent shrinking band, and no RH theorem.

**Main change of direction.** The old cofinal all-row moment hierarchy controls an entire moving family of Hecke L-functions. This packet constructs an exact transformation whose principal row is the ordinary integer Möbius detector. It then proves that a fixed positive fraction of bounded **principal sixth-power replicas**, observed only at a sparse predetermined scale grid, suffices for ordinary zeta zero exclusion. The rest of those replicas need no moment bound, and the bounded fraction can change at every sample.

This is a narrower sufficient arithmetic statement. Its critical cofinal version is equivalent to ordinary RH, so the reformulation does not manufacture an easy estimate or a numerical improvement. The source-conditional boundary `139999/160000` inherited from the earlier packet remains unchanged and remains dependent on the imported OpenAI analytic machinery. The new elementary bridge and capture implications do not use that machinery.

## 1. Results and their exact limits

| Result | What is proved in this packet | Remaining limitation |
| --- | --- | --- |
| [Exact ordinary-zeta bridge](EXACT_ZETA_BRIDGE_AND_SPARSE_CAPTURE.md), Theorem 2.1 | A fixed `chi_{-3}` dilation filter and the complete finite bad-prime restoration turn the principal Eisenstein ideal sum into `sum mu(n) W(n/D)` exactly. | General filtered Hecke rows are not claimed to have a nonvanishing Mellin numerator. |
| [Periodic transfer](PERIODIC_DILATION_TRANSFER.md), Proposition 1 and Corollary 2 | Bounded periodic partial sums preserve every power `D^alpha`, `alpha>0`, when one logarithmic derivative is controlled at the same row height. | A derivative-window/common-height bound is an explicit premise; absolute coefficient summation would fail below exponent one. |
| [Abelian-field extension](ABELIAN_COMPANION_FILTERS.md), Theorems 1–2 | For a fixed abelian field of degree `d`, remove its `d-1` nonprincipal companion factors with `d-1` scale derivatives and no exponent loss. | No growing-field uniformity or new row-replica construction is asserted. The field factorization is classical. |
| [Sparse fractional capture](EXACT_ZETA_BRIDGE_AND_SPARSE_CAPTURE.md), Theorem 5.1 | A fixed positive fraction of bounded principal replicas at each prescribed grid node implies the ordinary detector bound `D^(alpha+epsilon)` and no zeta zeros with real part `>alpha`. | The required fraction bound is unproved. Finite observations do not establish it. |
| [Signed-quantile capture](SIGN_QUANTILE_CAPTURE_FOLLOWUP.md), Theorem 1.1 | On a slightly denser grid, two possibly disjoint signed fractions imply the exact bound `B_1(D)=O(D^alpha)`. No small absolute value is required. | Both signed-fraction estimates remain open; the fixed-test mesh costs one extra logarithm. |
| [Principal averages and converse](PRINCIPAL_REPLICA_AVERAGES_AND_CONVERSE.md), Theorems 2.1, 3.1, 5.1 | Exact rough-annulus densities, a quantitative invertible limiting average, and ordinary RH implying boundedness of all polynomially sized principal replicas with any exponent `>1/2`. | Averaging has a nonvanishing Mellin multiplier and preserves the reciprocal-zeta difficulty. There is no same-endpoint converse at a single fixed exponent. |
| [Native heat defect](NATIVE_HEAT_DEFECT_AND_PRIME_REMOVAL.md), Sections 2–6 | Positive prime innovations miss the entire coprime off-product sector; its exact contribution is a physical-measure defect with a signed shorter-factor prime-removal formula. | The defect bound is equivalent to the centered covariance at this aggregation level and remains open. General heat-bath algebra is classical; the source diagnosis is the contribution. |
| [Independent-frequency collision growth](ANTI_CONJUGATE_COLLISION_GROWTH.md), Theorem 3.1 | At every fixed order `2k>=4`, an explicit total-frequency-zero configuration makes the exact finite collision factor grow like `exp(c Y^(1-2 sigma)/log Y)` for `1/3<sigma<1/2`, uniformly over polynomial row and mask ranges. | This is a modulus statement about one factor, not a lower bound on the signed physical trace or a refutation of the desired moment. |
| [Literal short factors on the growing frequency set](SHIFTED_COLLISION_AND_LITERAL_SHORT_FACTORS.md), Theorem 4.1 | The growth survives multiplication by all actual short Möbius factors on one common set of small shifts of positive measure, for any polynomially sized collection of polynomially bounded rows and masks. | Exterior weights may vanish; the signed row sum and the coupled physical integral may still cancel. |

All proofs retain prime-ideal multiplicities, the original nonunit zero masks where relevant, the fixed test, and the quantifiers needed by the claimed implication. The full proofs are in the linked files. Agreement between reviewers and finite diagnostics is not a substitute for those proofs.

## 2. Why the existing attack keeps returning to the same gap

The audit includes current source pins through the newly published #911 continuation and the #929 conductor-average branch. Its full account is in [RESEARCH_AUDIT.md](RESEARCH_AUDIT.md).

Three recurring losses matter. First, two square-root axes plus pointwise bounds on the other `2k-2` axes produce excess `(2b-1)(k-1)`. With the old replica extraction, the resulting boundary tends to `b`, rather than `1/2`, as the moment order grows. This obstruction was already proved in #913; it is credited rather than counted again.

Second, #927's complete signed auxiliary reunion returns the original native centered product-column energy. Another complete Poisson round trip does not by itself reduce that energy. The new conductor windows and the all-shared-prime reductions improve specified parts of the problem while leaving the primitive coprime signed remainder.

Third, complete-residue probabilistic models hide the special Möbius signs: a primewise sextic phase change turns the unsigned coefficient vector into the Möbius vector while preserving Haar measure and the positive heat geometry. The original short physical row density is not preserved. The new heat calculation identifies exactly the extra signed term that an actual arithmetic transfer would have to bound.

The new collision-growth proof adds a distinct analytic warning: once there are at least four independent Mellin frequencies, their total can be zero while the collision factor grows faster than every power. The companion minimum-modulus proof retains that growth after multiplication by all actual short Möbius polynomials, simultaneously on a common set of frequencies for a polynomial collection of rows and masks. Scale averaging therefore cannot turn the proved decay near the conjugately paired frequency tube into an absolute bound over its complement. Cancellation across rows or the coupled physical integral must remain available.

The imported native second-moment adapter is not simply a reciprocal-L hypothesis in disguise: its shorter-scale range is justified from the stated canonical and Poisson propositions. That remains a source-conditional deduction. This pass does not independently certify the imported canonical theorem, theta reflection, or the entire upstream Lean development.

## 3. The exact transformation

For the literal trivial-coefficient Eisenstein family, let

\[
A_u(D;W)=\sum_{(\mathfrak n,S)=1}\mu_K(\mathfrak n)
\chi_{\mathfrak n}(u)W(N\mathfrak n/D),
\qquad \mathsf S_aF(D)=F(D/a).
\]

Define

\[
B_u(D;W)=
\prod_{\mathfrak p\in S}(I-\mathsf S_{N\mathfrak p})
\sum_{m\ge1}\chi_{-3}(m)A_u(D/m;W).
\]

The product is over prime **ideals**; repeated norms from distinct split ideals are retained. The fixed window makes every physical sum finite. Since

\[
\zeta_K(s)=\zeta(s)L(s,\chi_{-3}),
\]

the principal row is exactly

\[
B_1(D;W)=\sum_{n\ge1}\mu(n)W(n/D).
\]

The exact sixth-power exclusion recurrence commutes with every filter:

\[
B_{w^6}(D;W)=
\sum_{\operatorname{rad}(\mathfrak r)\mid w}B_1(D/N\mathfrak r;W),
\qquad (w,S)=1.
\]

This is the source-level connection to the repository's integer Möbius, compact-wavelet, and fixed Mellin programs. Their particular kernels, positivity, and critical derivative bounds still have to be matched explicitly. Section 7 of the bridge gives the exact square-root normalization and factor-67 adapter; it does not import an unavailable critical SHARP sign.

## 4. A precise arithmetic target for the next strike

Fix `alpha>0`, `h>0`, and any fixed retained fraction `gamma` in `(0,1]`. Choose the fixed roughness set `Q` supplied by Proposition 3.2 of the bridge, and use the source's fixed universal Mellin test `W_*`. On each dyadic interval `[X,2X]`, put

\[
Y_X=X^{h/6},\qquad
\mathcal V_Q(Y_X)=\{w:(w,Q)=1,\ Y_X/2<Nw\le Y_X\}.
\]

At the prescribed grid nodes

\[
D_{X,i}=X\exp(i\log2/N_X),\qquad
N_X=\left\lceil(\log X)^2\omega(X)\right\rceil,
\quad\omega(X)\longrightarrow\infty,
\]

prove the following single-threshold estimate with one fixed constant `C_0`:

\[
\boxed{
\#\{w\in\mathcal V_Q(Y_X):
|B_{w^6}(D_{X,i};W_*)|\le C_0D_{X,i}^{\alpha}\}
\ge\gamma|\mathcal V_Q(Y_X)|.
}
\]

It is required at every node of every sufficiently large dyadic interval. The row set stays fixed inside that interval. The good bases may vary between nodes. The theorem proves that this estimate implies zeta zero-freeness in `Re s>alpha`.

At `alpha=17/24`, this is an explicit alternative arithmetic route to that target. Proving it for every fixed `alpha>1/2` would prove ordinary RH; the converse also holds at this cofinal scope. No uniformity as `alpha` tends to `1/2` is claimed. A different fixed universal test, constructed in #926, permits the still sparser mesh stated in the bridge.

There is a second target which needs only signed quantiles. Fix any `0<gamma<=1/2` and use `N_X=ceil((log X)^3 omega(X))` for the same fixed test. At every node, require at least a `gamma` fraction of replicas with `B_{w^6}<=C_0 D^alpha`, and at least a `gamma` fraction with `B_{w^6}>=-C_0 D^alpha`. These two fractions may be disjoint, so every value could have large absolute size. [The signed-quantile theorem](SIGN_QUANTILE_CAPTURE_FOLLOWUP.md) proves that these observations imply the exact endpoint `B_1(D)=O(D^alpha)`. At an absolute record, the positive replica recurrence forces almost every sufficiently rough replica to share its sign. Taylor approximation and the polynomial Markov inequality preserve that sign at one common preceding grid node, where the opposite quantile gives a contradiction. This theorem supplies no arithmetic proof of either quantile.

The difficult next result would be a proof of this fraction bound for the actual transformed source, or a new signed prime-removal estimate that bounds the surviving native defect. Another rearrangement with an unestimated reciprocal factor, another finite grid check, or another positive energy with the same excluded coprime sector would not close that gap.

## 5. Validation and review

The packet includes exact finite arithmetic diagnostics for the quadratic bridge, restoration multiplicities, replica powers, interpolation and incidence counting, the periodic Abel boundary/sign identity, a degree-four abelian example, and the heat-defect identities with nonunit masks. Their declared primitive inputs and coverage are kept separate from the infinite analytic proofs.

[VALIDATION.md](VALIDATION.md) records exactly what was run. [SOURCES.json](SOURCES.json) pins the consulted repository interfaces. The publication's review files identify the exact frozen source commit and file hashes they checked. These are independent AI-agent mathematical reviews, not an external peer-review claim or Lean formalization.

The packet is stacked on #928 and leaves the earlier source packets unchanged. It is standalone proposed research and has not been promoted to the integrated results.
