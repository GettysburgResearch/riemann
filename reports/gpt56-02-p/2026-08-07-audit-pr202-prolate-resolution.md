# Brief adversarial audit of the PR #202 prolate resolution proposal

Reviewer: `gpt56-02-p`  
Date: 2026-08-07  
Repository: `gfreund123/riemann`  
Requested source SHA: `83dac9b1ff95f64b4b48f788c017511d3d7f2aee`  
Reviewed surviving PR #202 head: `585cda919808429a759cf0bf7ab054af40f9a6d2`  
Review scope: `L-19821-critical-strip-growth-closes-support-average.md`, `T-19807-non-effective-cofinal-prolate-resolution.md`, and their load-bearing PR #164 dependencies.  No expensive computation was rerun.

## 1. Provenance boundary

GitHub no longer resolves the supplied SHA `83dac9b...`.  The proof files named
in the user-facing summary survive on current PR #202 head
`585cda919808429a759cf0bf7ab054af40f9a6d2`, which is the exact commit reviewed
here.

The current head has two claim-namespace collisions:

```text
L-19821
  critical-strip-growth-closes-support-average
  positive-operator-rvm-local-weyl

T-19807
  non-effective-cofinal-prolate-resolution
  whole-matrix-diagonal-lower-envelope
```

These must be renumbered before publication.  They also represent two distinct
positive architectures and must not be cited through one ambiguous ID.

## 2. Executive verdict

| Object | Verdict | Reason |
|---|---|---|
| `T-19807-non-effective-cofinal-prolate-resolution` as a conditional composition | **VERIFIED WITH FIXES** | Once Sections 2–4 are assumed in one exact normalization, the support selection, relative scalarization, target/gap estimate, Hardy convergence, and Hurwitz composition are coherent. |
| The same file as an unconditional proof of RH | **GAP/BLOCKED** | The four decisive growing-frame statements are hypotheses, not proved consequences of the cited PR #164 files. |
| `L-19821-critical-strip-growth-closes-support-average` | **GAP/BLOCKED** | It applies `L-16226` without proving that theorem's scaled derivative hypothesis. |
| Quarter-power magnitude estimate | **VERIFIED** | `|exp(-is x_R)| <= R^(1/4)` follows directly from `|Re rho-1/2|<1/2`. |
| Rephased cross-end repair `L-21503` | **PROPOSED** | It restores the scaled derivative gate and exposes one additional finite stationary ratio.  It does not retroactively verify `L-19821`. |
| Complete PR #164 source/alias/local-Weyl package | **GAP/BLOCKED** | Exact finite algebra and useful asymptotic templates survive, but the complete source-specific profile LMIs and all-channel uniformity are not established. |

No proof of RH is presently obtained.

## 3. Immediate fatal gap in `L-19821`

The parent large sieve `L-16226.5` requires

\[
 \|A_\gamma(R)\|+T\|\partial_RA_\gamma(R)\|\le B_T.
\]

The proposed repair instead proves only

\[
 \|A_\rho(R)\|+\|A_\rho'(R)\|
 \ll R^{1/4}(\log R)^A.
\]

These are not interchangeable.  The endpoint factor contains

\[
 e^{-i\gamma x_R},\qquad x_R={1\over2}\log(R/2\pi),
\]

and

\[
 R\partial_Re^{-i\gamma x_R}=-{i\gamma\over2}e^{-i\gamma x_R}.
\]

On `gamma asymp R asymp T`, leaving that oscillation in the amplitude costs an
extra factor `T`.  The displayed mean-square bound therefore does not follow
from the proof as written.

This is recorded separately as `R-21501`.

## 4. Proposed repair: rephase before differentiating

`L-21503` moves the real endpoint oscillation into the support phase:

\[
 \Theta_{\varepsilon,\gamma}(R)
 =\varepsilon R S(\gamma/R)-\gamma x_R,
\]

and leaves only `exp(delta x_R)` in the amplitude.  If the complex profile
satisfies

\[
 \|a\|+\|\partial_u a\|+R\|\partial_Ra\|
 \le \operatorname{polylog}R,
\]

then the rephased amplitude satisfies exactly

\[
 \|\widetilde A\|+R\|\partial_R\widetilde A\|
 \ll R^{1/4}\operatorname{polylog}R.
\]

For the radial stationary variable `y>0`, with

\[
 \omega=y+y^{-1},
 \qquad S-\omega S'=y,
\]

the combined phase derivative is `epsilon y plus-or-minus omega/2`.  Two sign
families have derivative map

\[
 {y^2+1\over2(y^2-1)},
\]

whose absolute value is at least `1/2` away from the radial fold.  The other
two have one additional nondegenerate critical ratio

\[
 y=1/\sqrt3.
\]

Thus the repair yields a finite phase partition: separated intervals, the old
radial fold, and one additional stationary neighborhood.  The latter needs a
finite van-der-Corput/Airy ledger; it may not be discarded.

Same-end horizontal corrections do not carry the endpoint phase.  They require
a separate holomorphic horizontal-derivative Gram.  Under a polylogarithmic
bound they contribute `O(polylog(R) log(R)/R)` and vanish.

This repairs the derivative mismatch but leaves the source-specific profile
bounds and finite stationary ledgers open.

## 5. Audit of the four claimed load-bearing items

### 5.1 Exact congruence between the global-anchor frame and the complete CCM space

**GAP/BLOCKED.**

- `L-16211` proves generic finite projection surjectivity from the imported
  zeta-cycle theorem.  Its Section 6 explicitly says that no quantitative right
  inverse or source-frame lower bound follows.
- `L-16218` constructs an exact, polynomially conditioned coefficient-space
  basis for two abstract source constraints, assuming uniform point-value
  comparisons.
- Neither file proves that this specific frame, transported through the exact
  arithmetic map, periodization, restriction, projection, endpoint terms, and
  CCM normalization, gives the complete finite matrix used in `T-19807`.
- The later abstract identity `L-19820` correctly identifies the
  alias-and-projection-corrected tail, but its production domain and fold
  convergence are expressly left open.

A dimension count or finite surjectivity statement is not the required
congruence and does not control the frame uniformly over a support block.

### 5.2 Dimension-uniform radial/alias Gram floor

**GAP/BLOCKED.**

- `L-16222` supplies a useful real-axis, real-parameter Bessel normalization
  under Dunster's declared envelope.
- `L-16227` asserts the full infinite-alias Gram floor after stationary-phase
  cancellation.  The proof does not supply the uniform alias-dependent phase
  constants, endpoint-channel bounds, or complete upper-frame estimate in the
  exact source metric.
- In particular, the asserted absolute estimate
  `sum_k ||r_n(k .)/s_n||_2 <= C` is not a consequence of the first-alias
  normalization alone.  Bare dilation gives only a `k^(-1/2)` norm bound.
  Any stronger summability must come from endpoint cancellations or a correlated
  alias identity.
- `L-16221` explicitly labels the prolate jet-corrector asymptotics open.  Those
  open endpoint channels are used by `L-16227` and cannot be treated as already
  closed.

The exact first-alias identity and positivity of self-alias Grams survive.  The
complete uniform lower and upper frame theorem does not yet follow.

### 5.3 The `O((log R)^2)` Selberg/local-Weyl remainder

**GAP/BLOCKED for the production packet; abstract theorem survives.**

`L-16223` gives a plausible dimension-free operator Stieltjes estimate under a
finite-branch WKB representation, uniformly controlled coefficient metric,
mode-derivative multipliers, compact profile support, and an Airy splice.  The
Selberg-moment and Holder bookkeeping is useful.

The complete alias-corrected source profile has not been shown to satisfy those
hypotheses in one common metric.  Central, tail, endpoint-polylogarithm, and
infinite-alias pieces remain external ledgers.  The theorem therefore cannot be
cited as a completed line-centered production LMI.

The later duplicate-ID file `L-19821-positive-operator-rvm-local-weyl` is an
abstract improvement, but it likewise assumes the profile, derivative, and
logarithmic-moment LMIs that production still has to prove.

### 5.4 Shrinking-strip Dunster/Fuchs profile bound

**GAP/BLOCKED.**

The exact bound imported by `L-19821` is

\[
 \sup_{|v|\le1/(2R)}
 \left(
  \|\Phi(u+iv)\|+
  \|\partial_u\Phi(u+iv)\|+
  R\|\partial_R\Phi(u+iv)\|
 \right)
 \le \operatorname{polylog}R.
\]

The cited PR #164 files do not prove this statement:

- `L-16219` treats real angular PSWF/Hermite `L2` and point values;
- `L-16222` treats a real radial Bessel template and a relative real-axis `L2`
  remainder;
- neither establishes holomorphic continuation in the shrinking complex strip,
  the required support derivative, or all endpoint/alias channels.

Dunster's broad uniform real-parameter range is relevant, but the exact complex
strip and differentiated source-profile theorem must be derived rather than
imported by name.

## 6. Further quantifier and integration issues

1. Avoiding the countable exact zeta-cycle set proves only algebraic
   surjectivity.  It does not give a uniform source inverse on the
   positive-measure good-support set.  Near-cycle conditioning can diverge.
2. The large-sieve calculation treats compact ordinate-ratio bands.  The
   central region, unbounded ratio tail, folds, endpoint channels, and aliases
   must be proved jointly exhaustive.
3. `L-19822` correctly separates nonoscillatory same-end horizontal corrections
   from oscillatory cross-end terms.  Its own proof boundary states that the
   same-end derivative channel and complete corrected-tail branch form remain
   source-specific gates.  This is incompatible with treating the quarter-power
   observation alone as closure of the actual-minus-line matrix.
4. The current PR head contains a second, distinct whole-matrix `T-19807` route.
   Its finite-to-global Gevrey diagonal theorem is a serious alternative, but
   its source-profile interfaces A–C are also explicitly unproved.  It does not
   retroactively complete the prolate theorem.

## 7. Conditional composition audit

If one supplies, in one exact normalization,

\[
 c_DG_R\preceq D_R\preceq C_DG_R,
\]

\[
 A_R=(\log R)D_R+E_R,
 \qquad
 \|D_R^{-1/2}E_RD_R^{-1/2}\|\to0,
\]

and the target hierarchy

\[
 \mu_{D,R}\le C_4d_4(R),
\]

\[
 D_R-\mu_{D,R}G_R\succeq c_8d_8(R)G_R,
 \qquad d_4/d_8\to0,
\]

then the algebra in Sections 5–8 of the non-effective `T-19807` is coherent:
there is a cofinal good-support sequence, the finite matrix is eventually
positive, the target-to-gap ratio tends to zero, the Hardy target converges,
and the imported CCM real-zero/Hurwitz interface yields RH.

This is a valid **conditional composition theorem**.  It is not an
unconditional proof because the displayed hypotheses are the unresolved
source-specific arithmetic/analytic theorem.

## 8. Smallest exact obstruction after the repair

The shortest remaining proof object is one complete alias-corrected source
profile theorem.  At every sufficiently large support block it must provide,
in one common metric:

```text
exact source/periodization/restriction/CCM congruence;
two-sided complete profile Gram LMI;
shrinking-strip u, v, and support-derivative Gram LMIs;
line-centered Riemann-von-Mangoldt local-Weyl LMI;
rephased cross-end large-sieve ledger;
same-end horizontal derivative ledger;
central, fold, endpoint, and infinite-alias closure.
```

No subset of those objects may be assembled from unrelated normalizations or
from independently whitened metrics.

## 9. SERIOUS RESOLUTION PATH

A serious positive path is present, but not completed:

1. use `L-19820` to define the **single exact corrected tail** rather than an
   ordinary exterior tail;
2. prove one source right inverse uniformly on a positive-measure subset of each
   support block, quantitatively separated from every zeta-cycle singularity;
3. derive the complete shrinking-strip and derivative profile Gram from the
   exact radial/endpoint/alias representation;
4. apply the positive operator local-Weyl calculation to that same profile;
5. apply the rephased theorem `L-21503` to the cross-end horizontal part and a
   direct derivative LMI to the same-end part;
6. certify all finite stationary/fold and tail ledgers;
7. invoke the conditional `T-19807` composition.

If these steps are proved, the prolate route would prove RH.  At present Steps
2–6 are open.  The repository should therefore classify the proposal as
`GAP/BLOCKED`, preserve the conditional composition, and review `L-21503` as a
separate proposed repair.
