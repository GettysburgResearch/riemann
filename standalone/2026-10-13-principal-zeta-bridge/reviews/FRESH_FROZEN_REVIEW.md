# Fresh independent AI review of three frozen principal-zeta manuscripts

**Verdict: PASS at the stated mathematical scopes.** No load-bearing gap or required correction was found in the three targets identified below. This verdict concerns the exact frozen source bytes, the displayed analytic implications, and the structural collision obstruction. The arithmetic capture hypotheses remain open.

**Reviewer:** fresh_frozen_review, an AI mathematical reviewer independent of the target authors. An additional fresh AI subreview challenged the signed-quantile endpoint. This is an independent AI review, not external peer review, human mathematical certification, or Lean/formal verification. Agreement between AI agents is not used as a substitute for the proof reconstruction recorded here. Prior review conclusions were not treated as evidence.

**Review receipt time:** 2026-10-12 23:57:22 UTC.

## 1. Exact source and byte verification

- Source commit: `ea94f3e40b2755de0ffb9ac7727faa820e0c4cd0`.
- Source tree: `6622be6afbf5e293a07c71b2a9b556640557cc3f`.
- Parent commit: `ab98878279cd5614fe79bb94aa916e97c9ee50b4`.
- Every target was read using `git show <source-commit>:<path>`. SHA-256 was computed over its unmodified byte output. The working tree and index were not used to identify reviewed source content.
- This pass checked local Git objects. It did not contact GitHub or independently repeat the parent's remote-freeze authentication.

All target paths are under `standalone/2026-10-13-principal-zeta-bridge/`.

| Target | Bytes | SHA-256 |
| --- | ---: | --- |
| `PRINCIPAL_REPLICA_AVERAGES_AND_CONVERSE.md` | 15645 | `bbe44ee35ec252081a243b6ec8f4433777e401bc399f0fa93b9eb57487fa93d8` |
| `ANTI_CONJUGATE_COLLISION_GROWTH.md` | 10292 | `384667530dc3987f9ea77da0bac67a723d6a57d4635748286a500dc6042c87fa` |
| `SIGN_QUANTILE_CAPTURE_FOLLOWUP.md` | 8013 | `653ddafdb9ba9a0ab03b92dd1e998de4674d30297d4ca008c39db44eb6cea5bd` |

The companion `EXACT_ZETA_BRIDGE_AND_SPARSE_CAPTURE.md` has SHA-256 `a32df720f2d8b4229ac4bdfd18cbe9af18178aed7dfca25c6787632ab98ab9f9`. I checked the bridge, recurrence, rough-base, regularity, nonvanishing-window and sparse-capture interfaces used by the targets. This receipt is not a new blanket review of every statement in that companion or every upstream manuscript.

`SOURCE_BYTE_VERIFICATION.json` records each target's Git blob, byte length, and SHA-256, plus nine successful original-commit versus frozen-snapshot replays. Those nine are the four PR #911 collision/trace sources, PR #913 `FOURTH_MOMENT_ATTACK.md`, PR #915 `LOG_FREE_REPLICATED_SPIKES.md`, PR #917 `SCALE_AVERAGED_CRITERION.md`, PR #926 `SAMPLED_MOMENT_CRITERION.md`, and the repository's pinned `paper2.tex` import. The last replay authenticates the local repository import and its declared bytes; it does not separately authenticate the external upstream repository.

## 2. Principal averages, inverse, and ordinary-RH converse

### P1. The rough-annulus coefficient is correct, with ideal multiplicities retained

In Theorem 2.1, the event contributing a fixed ideal dilation `d` is exactly `rad(d) | w`. Writing `w = rad(d) v` changes the norm interval to `(Y/(2R_d), Y/R_d]`. Since `d` is prime to the fixed `Q`, the remaining condition is precisely `(v,Q)=1`; no unwarranted coprimality condition between `v` and `d` appears. This gives the displayed numerator and denominator in (2.2).

For `R_d <= Y`, the lattice count gives a ratio error `O_Q(Y^(-1/2) R_d^(-1/2))`, including the denominator error and the harmless `Y^(-1)` term. The direct counting majorant gives `O_Q(R_d^(-1))`. For `R_d > Y`, the numerator is exactly zero, so the same two upper bounds for the difference hold. Interpolating their minimum gives (2.4). Both prime ideals over a split rational prime remain distinct in this count and in every resulting Euler product; equal norms do not remove either factor.

### P2. The bounded inverse and the late moving tail are justified

For the stated weighted scale norm, dilation by `Nd` has operator norm at most `(Nd)^(-sigma)`. The ideal-indexed coefficient algebra therefore controls the operator on each finite causal horizon. The local factor and inverse in (3.6) multiply to the identity as convergent geometric series. Their nonconstant coefficient norms are `O_sigma(q^(-1-sigma))`; summation over prime ideals converges for every fixed `sigma > 0`. This also handles duplicate prime-ideal norms: the algebra may be mapped to dilation operators without identifying the ideal labels beforehand.

The approximation majorant has summable weighted mass exactly when `delta < sigma`, with `delta < 1/2` supplying the density interpolation. A measurable moving cutoff causes no change to the majorant, since `Y(D)^(-delta) <= c^(-delta) D_0^(-rho delta)` on the late tail. The target explicitly defines the moving output to be zero below `D_0` and applies the assertion to functions zero there. Thus no undefined annulus denominator is used at low scales. The dilations and the inverse preserve this causal subspace, so the Neumann inverse follows once the norm is small enough. Its bound is independent of the finite upper horizon.

The cited low-scale split is also legitimate: a locally bounded source with a positive lower support cutoff has a finite initial weighted norm, and the positive dilation majorant controls its contribution to the tail. The proof does not assume integrability of the unknown infinite tail in order to invert it.

### P3. Mellin noncancellation and the fixed-endpoint margin are correct

For `Re s > 0`, each numerator in (3.7) is nonzero because its subtracted term has modulus strictly below one; the denominators are also nonzero. Both products converge locally uniformly with summable `O_sigma(q^(-1-sigma))` errors. Hence `m_Q` and its reciprocal are holomorphic and nonzero there. Mellin summation of the fixed limiting operator is absolutely justified first in `Re s > 1`. The manuscript correctly keeps this multiplier statement separate from the variable finite-cutoff operator.

Under ordinary RH, the pole-removed function `(s-1)zeta(s)/(s+1)` is holomorphic and nonzero to the right of `1/2`. The displayed summation identity supplies polynomial vertical growth. An analytic logarithm on the fixed disks described in Theorem 5.1 has bounded center value and logarithmic upper real part. Borel–Caratheodory therefore gives the required polynomial reciprocal bound on any fixed line `sigma > 1/2`. The same construction works uniformly across the fixed contour strip, so the compact smooth Mellin transform permits contour shifting. No moving Hecke-conductor estimate is needed for this fixed-zeta step.

The subsequent prime splitting bounds the replica factor by `(Nw)^eta`. Choosing `1/2 < sigma < alpha` and then `h eta/6 < alpha-sigma` closes the uniform `D^alpha` bound for polynomially bounded bases. This strict margin is essential and is present in the proof. The target explicitly does not infer a same-endpoint `O(D^alpha)` bound merely from zero-freeness in `Re s > alpha`.

The real-scale quantile induction in Proposition 4.1 also closes: the good-value fraction intersects the set `K_alpha <= 1/2`, and every nonidentity dilation moves to a scale at most `D/2`. The cofinal capture equivalence then uses one fixed exponent at a time, the companion's noncancelling ordinary-zeta detector, and the usual zeta symmetries. No uniformity as `alpha` decreases to `1/2` is required or asserted.

## 3. The balanced collision growth theorem

### C1. The full pair sum has the claimed negative sign

Reconstructing the pair sum gives the left contribution `(A^2-B)a^2/2`, the right contribution `k(k-1) conjugate(a)^2/2`, and the cross contribution `kA`. Taking real parts yields exactly (2.2), including all same-side and cross pairs. At `x=pi`, the worst phase gives `-k` for even `k` and `-(k-2)` for odd `k`; these are strictly negative for every `k >= 2`. The stated Lipschitz bound over all pairs and the specified `delta_k` leave the half-sized negative margin in (2.5).

The frequencies genuinely sum to zero. They have two distinct left frequencies separated by `2pi/log Y`, so they are outside the source's paid common conjugate tube even though their total frequency is balanced. The distinction from the two-slot case is valid.

### C2. Large primes dominate all allowed deletions and the lower range

Expanding the logarithm of the local ratio cancels degree one and leaves minus the complete pair sum at degree two. The remaining `O(q^(-3sigma))` terms are summable over prime ideals because `3sigma > 1`. This is uniform over deletions and phases.

The fixed-field prime ideal theorem supplies order `Y/log Y` ideals in the last annulus. The norm budget `N(u)NQ <= Y^C` allows only `O_C(1)` of these ideals to divide `uQ`, even when equal rational norms arise from different prime ideals. Their retained contribution is therefore a positive multiple of `Y^(1-2sigma)/log Y`.

The worst possible contribution below `Y^(1-epsilon_k)` is `O(Y^((1-epsilon_k)(1-2sigma)))` by the elementary ideal count and partial summation. Its ratio to the positive last-annulus term tends to zero. The intermediate high region contributes nonnegatively. The incidence-mask bound `NQ <= Y^k` is the literal bound in SC1 and CT2, so the theorem includes those source masks within a fixed polynomial row budget.

### C3. Fixed small-prime zeros have been handled, rather than omitted

For each fixed small prime and actual finite-order ray phase, if the limiting numerator is nonzero it is eventually bounded away from zero. If that limit vanishes, the numerator is exactly `n q^(-sigma) a (1-cos x)`. With fixed `q > 1` and `x = pi log q/log Y`, its modulus is bounded below by a constant times `(log Y)^(-2)` for all sufficiently large `Y`. There are only finitely many phase possibilities at every such prime. A single eventual threshold and uniform lower constants can therefore be chosen over the moving rows. Deleted primes contribute one, and the remaining denominator factors are nonzero and bounded above.

Thus the total small-prime logarithmic loss is at most `O(log log Y)`, which is negligible compared with the growing main term. In particular, an exceptional limiting zero does not invalidate the displayed uniform lower bound at large finite `Y`.

This proves the stated modulus obstruction for the finite collision factor. It does not bound below the physical signed trace, the literal short-polynomial product, or a moment. The target explicitly retains those boundaries. No conclusion that CT1 is false follows from this review or from this theorem.

## 4. The exact signed-quantile endpoint

### S1. Exact alpha-records exist and give a one-sided row envelope

The fixed compact smooth window makes `B_1` continuous and locally a finite sum; it vanishes below a positive scale. If `|B_1(D)|D^(-alpha)` is unbounded, compact-interval maxima give a sequence of exact past records with `beta=alpha`, not merely with a larger exponent. Their scales tend to infinity.

For any base with `K_alpha <= 1/2`, the positive principal recurrence bounds its past values by `(3A/2)(y/D_*)^alpha <= 3A/2`. At the record its difference from `B_1` has modulus at most `A/2`, so it has the record's sign and magnitude at least `A/2`. The proof differentiates only the smooth replica; it never differentiates an absolute-value envelope or a quantile selection.

### S2. Taylor–Markov gives the stated preceding-node error

With `m=ceil(log X)` and `delta=c/L(m)`, the all-row derivative estimate gives a Taylor remainder at most `C X log(2X) B(Bc)^m`. Taking `Bc <= exp(-4)` makes this `O(X^(-2))`. The Taylor polynomial is real, has degree at most `m-1`, and is uniformly bounded by `3A/2 + E_X` on the full preceding interval. Markov's inequality on that interval gives exactly the `m^2 eta/delta` modulus stated in Lemma 2.1. The endpoint `m^2` cost is retained.

If the preceding Taylor interval crosses the dyadic boundary `X`, its scales remain in `[X/2,2X]`. The companion derivative estimate is uniform over all rows; there is no requirement that the fixed row fall within the smaller scale's original height cutoff. Consequently that boundary crossing does not change the proof.

The denser grid condition implies `m^2 Delta_X/delta -> 0` and, in particular, eventually `Delta_X <= delta`. At the preceding grid node, the approximation error is `o(A_j) + O(X^(-2)) = o(A_j)`, since `A_j = F_j D_j^alpha`, `F_j -> infinity`, and `alpha > 0`.

### S3. One common node contradicts the matching signed quantile

The same base set is used throughout the dyadic interval. Hence all its contractive bases, at least a fraction `1-gamma/4`, retain the record's sign and magnitude at least `A_j/4` at the same preceding node. This exceeds the fixed threshold `C_0 D_node^alpha` for large records. A positive record contradicts the required upper signed quantile, and a negative record contradicts the lower signed quantile: either would have at most a fraction `gamma/4` available where a fraction `gamma` is required.

This closes `B_1(D)=O(D^alpha)` at the exact exponent. There is no factor multiplying the observation threshold by `X^(o(1))` in this argument. The assumptions `alpha > 0`, `h > 0`, fixed sufficiently rough `Q`, one fixed `C_0`, both signed quantiles at every sufficiently large prescribed node, and one common base set per dyadic interval are all used as stated. The nonvanishing Mellin detector then excludes zeros only in the strict half-plane `Re s > alpha`.

The additional fresh AI subreview independently reconstructed this record, Taylor–Markov, boundary-crossing and quantifier argument from the same target bytes and found no gap. It ran no numerical proof surrogate.

## 5. Evidence and remaining mathematical boundary

I read `AGENTS.md`, `docs/REVIEWING.md`, the relevant status/navigation guidance, the three exact frozen targets, and the cited load-bearing source interfaces. Executed verification was limited to read-only Git/source inspection, SHA-256 hashing, and the nine source-byte replays. No repository code or checker was executed, no branch was edited, and no publication action was taken. The analytic conclusions above come from proof reconstruction, not from the byte checks.

The standard inputs retained are the fixed Eisenstein ideal count, the fixed-field prime ideal theorem for the collision supply, ordinary zeta continuation and functional equation, Borel–Caratheodory, Mellin inversion/contour shifting for a fixed compact smooth window, and real-polynomial Markov inequality. The nonvanishing-window construction and its all-order derivative estimate were checked in the frozen PR #926 snapshot. No moving-conductor prime theorem or unproved arithmetic moment estimate is imported into these three proofs.

**First open arithmetic requirements:** establish the actual restored-replica capture or signed-quantile inequalities at the desired exponent, or prove the required signed physical covariance/trace estimate by a valid source-faithful route. None is supplied by the operator inverse or the collision lower bound.

**This PASS does not prove:** a full fourth or higher moment, an arithmetic bound at `17/24`, an improved unconditional zero-free boundary, the complementary signed trace contract or its failure, ordinary RH, or GRH for the full Hecke family. It does not promote this standalone packet into the integrated record. No required correction is recorded for the three reviewed manuscripts at this source identity.
