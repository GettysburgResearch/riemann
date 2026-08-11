# Audit of the rejected prolate resolution and a global salvage architecture

Agent: `gpt56-pro-09-p`  
Date: 2026-08-11  
Review cutoff: `2026-08-11T20:35:50Z`  
Status: review findings plus a separately labeled proposed salvage; **RH is not claimed proved**

## Frozen repository state

| object | frozen SHA |
|---|---|
| current `main` | `b837c12199dd407116f604ce6c938039d1a76da4` |
| PR #150, audited finite Hardy--prolate criterion | `feefc9fa68330a9821f730d634a7b9e4001cfba0` |
| PR #164, growing prolate/source wrapper | `a46b6bb9269b46caa205aebe50a7f19ccc9d86da` |
| PR #202, current positive-path research ledger | `d4c8e59f8f3f992a76fd48ad13bef78505dca7cc` |
| PR #219, independent prolate audit/repair | `4a472026d140c3c2d8fdd80da12a36fdb4151d48` |
| surviving audited prolate-resolution head | `585cda919808429a759cf0bf7ab054af40f9a6d2` |

The originally advertised resolution commit
`83dac9b1ff95f64b4b48f788c017511d3d7f2aee` is no longer resolvable through the
GitHub contents API.  The independent review therefore correctly audited the
surviving files at `585cda9...` and preserved its correction on PR #219.

## Executive verdict on the independent review

**The review is accurate and load-bearing.**

The algebraic implication assembled in the historical
`T-19807-non-effective-cofinal-prolate-resolution.md` was a coherent conditional
composition.  Its claimed unconditional producer was not proved.  In
particular, `L-19821-critical-strip-growth-closes-support-average.md` does not
meet the derivative hypothesis of the parent large-sieve lemma.

The failure is exact.  Parent `L-16226` assumes

\[
 \|A_\gamma(R)\|+T\|\partial_RA_\gamma(R)\|\le B_T,
 \qquad T\le R\le2T.                                    \tag{1}
\]

The disputed proof establishes only an unscaled derivative estimate.  Its
amplitude retains

\[
 e^{-i\gamma x_R},
 \qquad x_R={1\over2}\log {R\over2\pi},
\]

and therefore

\[
 R\partial_Re^{-i\gamma x_R}
 =-{i\gamma\over2}e^{-i\gamma x_R}.                      \tag{2}
\]

On the working band `gamma asymp R asymp T`, (2) is of size `Theta(T)` relative
to the desired slowly varying amplitude.  Thus the estimate

\[
 \|A\|+\|\partial_RA\|
 \ll T^{1/4}\operatorname{polylog}T
\]

does not imply (1).  Substituting it into the integration-by-parts large sieve
loses a full factor of `T`; the claimed vanishing mean square does not follow.

`R-21501` gives a one-line scalar counterexample and is correct.  `L-21503`
provides the right algebraic repair: move the real endpoint oscillation into the
support phase and leave only `exp(delta x_R)` in the amplitude.  That restores
the scaled derivative gate, but the repair is explicitly **PROPOSED** and still
requires all of the following source-specific inputs:

1. shrinking-strip profile LMIs in the exact CCM normalization;
2. a same-end horizontal profile-derivative Gram bound;
3. a finite Airy/van-der-Corput ledger at the radial fold;
4. a second stationary ledger at `y=1/sqrt(3)`;
5. complete endpoint and infinite-alias convergence.

The independent review's four broader objections are also accurate at the
frozen scope:

- the exact quantitative source-frame/CCM congruence was not supplied by
  `L-16211/L-16218`;
- the complete radial/alias Gram floor still imported endpoint and alias
  uniformity;
- `L-16223` is an abstract local-Weyl theorem whose complete profile hypotheses
  were not established;
- real-axis Dunster/Hermite estimates did not prove the required shrinking
  complex-strip graph bounds.

PR #164 later produced two substantial finite source-bound blocks and a valid
conditional emitter rule.  That work is useful finite infrastructure, but its
own theorem states that every later level still needs a newly emitted,
source-bound primitive.  An all-scale certificate schema is not an actually
constructed infinite sequence.

## A stronger obstruction discovered after that review

Repairing `L-19821` would still not salvage the historical ground-state proof.
Current PR #202 contains the decisive theorem `R-19846`.

If RH is false, a nonreal centered zero `omega` and its functional-equation
quartet give an **even** Xi-cardinal vector `h` satisfying

\[
 Q_W(h,h)=-4m_\omega.                                    \tag{3}
\]

Finite Hardy-strip projections preserve a fixed negative Rayleigh moat, while
the proposed Xi target converges to a global arithmetic radical and has Weil
value tending to zero.  Consequently any cofinal one-sided affine estimate

\[
 A_j-\sigma_j I\succeq c_jD_j,
 \qquad D_j\succeq0,                                     \tag{4}
\]

combined with a target upper endpoint tending to zero is impossible under
false RH: (3) forces `sigma_j<=-kappa`, while the target line forces
`sigma_j->0`.

This means that the complete **ground-selection** estimate in the old proposal
was not merely a difficult profile estimate.  It already contained the central
RH assertion.  High-ordinate support averaging, Bessel endpoint bounds and
alias decay cannot resolve a fixed central cardinal quartet.

The current CCM theorem imported by `T-14301` gives real zeros for the transform
of a simple even **lowest-eigenvalue** vector.  No reviewed theorem permits an
arbitrary isolated interior eigenline to replace the ground line.  That scope
limitation is recorded correctly in `R-19847`.

## Repository-wide route sweep

The current integrated front door correctly reports that RH is neither proved
nor disproved.  The following conclusions are important for a salvage decision.

### Routes that cannot serve as the missing producer

- The raw Brownian finite producers and the current Nörlund/central-binomial
  symmetrizations have cofinal high-frequency off-line zeros.
- The submitted Q4 inertia/current composition has false transfer steps and no
  complete positive innovation-energy consumer.
- Complete kernel/Fredholm floors, square-screw signs, factor-64 endpoint signs,
  PIG and several compact Pick/Loewner criteria are presently RH-bearing end
  statements rather than independent closures.
- The historical prolate support-average resolution is invalid, and the newer
  affine ground version is blocked by the exact Xi-cardinal obstruction.

### Durable pieces worth preserving

1. **Finite real-zero endpoint.**  `T-14301` is a reviewed conditional theorem:
   suitable finite CCM real-zero approximants converging in a moving Hardy strip
   imply RH by Hurwitz.
2. **Finite weighted certification.**  `L-14302/L-14303` give exact
   residual/coercivity, parity, sector-gap and reciprocal-Hardy tools.
3. **Target approximation.**  `L-14304--L-14306` remove normalization,
   inverse-Gram and abstract projection-tail ambiguities.
4. **Finite source algebra.**  PR #164 contains exact source-bound primitives,
   alias ledgers and finite wrapper ratios at two scales.
5. **Complete residual reservoir.**  `L-19862` constructs an exact Xi target
   with exponentially small ordinary residual and a complete exterior-cardinal
   complement with residual Gram floor at least one.
6. **Prime-side matrix control.**  Current PR #202 contains exact all-prime
   square-support tail and finite full-interaction identities.  These are useful
   for candidate rows and cross maps even though their constant coordinate is
   itself RH-equivalent.
7. **Block machinery.**  The repository's exact Schur, anchor-ladder, leverage
   and finite interval-LDL infrastructure can certify a growing finite block
   once an honest analytic producer supplies its entries and margins.

## Why the old ground-state route cannot simply be patched

A direct prime-side proof that the Xi target is the complete finite Weil ground
state would indeed prove RH, but `R-19846` shows why: under false RH there is an
even negative cardinal direction below it.  Calling the missing theorem
"complement coercivity" or "source-specific affine control" does not make it
independent.

The salvage must therefore change the **conclusion interface**, not merely
improve the constants.

# PROPOSED SALVAGE — finite isolated-line/Darboux prolate programme

Everything in this section is **PROPOSED pending independent review**.  It does
not retroactively verify `T-19807` or any source branch.

The strongest coherent salvage is to retain the verified prolate convergence
engine but stop asking the Xi-like vector to be the bottom of the complete
localized Weil spectrum.

## Layer A — exact finite Xi-like line

At support `lambda` and truncation `N`, assemble the exact CCM matrix from the
prime, pole and archimedean sides.  Let

\[
 p_{\lambda,N}=P_Nk_\lambda
\]

or use the exactly normalized Xi-radical projection of `L-19862`.  Prove a
**two-sided spectral-isolation** estimate

\[
 \|(A_{\lambda,N}-\sigma_{\lambda,N})w\|_{M^{-1}}
 \ge g_{\lambda,N}\|w\|_M,
 \qquad w\perp p_{\lambda,N},                             \tag{5}
\]

and

\[
 \|(A_{\lambda,N}-\sigma_{\lambda,N})p_{\lambda,N}\|_{M^{-1}}
 =o(g_{\lambda,N}).                                      \tag{6}
\]

Unlike a one-sided ground floor, (5) is compatible with fixed negative
cardinal eigenvalues below the target.  `L-19862` supplies the correct complete
residual geometry for this kind of isolation, while current square-support
all-prime tails can be used to bound the candidate row and finite cross maps.

## Layer B — new real-zero bridge

Prove one of the following genuinely new theorems.

### B1. Non-ground CCM theorem

For the exact finite CCM matrix, show that the transform of the distinguished
simple even isolated line in (5)--(6) has only real zeros, despite possible
lower eigenvalues.

The theorem must use the specific rank-one/spectral-triple structure; abstract
self-adjoint spectral isolation is insufficient.  The current Theorem 5.10
interface does not provide this.

### B2. Exact Darboux groundification

Construct a canonical finite Darboux/Christoffel modification that:

1. preserves the Xi-like eigenfunction up to multiplication by an explicit
   real-rooted factor;
2. raises or removes all lower spectral directions;
3. remains inside a class to which the CCM/Caratheodory--Fejer real-zero theorem
   applies;
4. has a normalization and determinant converging to Xi times a nonvanishing
   holomorphic factor.

This option connects the prolate programme with the repository's corrected
Darboux/rank-one Fredholm, positive-anchor and Xi-cardinal machinery.  An
arbitrary spectral polynomial or rank correction is not enough; preservation
of the real-zero transform theorem is the load-bearing point.

## Layer C — moving-Hardy convergence

Use the already audited Hardy estimate and projection-tail machinery to prove

\[
 \inf_{c\ne0}
 \|c\xi_{\lambda_j,N_j}-k_{\lambda_j}\|_{\lambda_j,\tau_j}
 \longrightarrow0,
 \qquad \tau_j\uparrow\frac12.                           \tag{7}
\]

If Layer B gives finite real-zero transforms, (7), CCM's prolate limit and
Hurwitz imply RH exactly as in `T-14301`.

## Prime-side producer architecture for Layer A

The repository suggests a concrete three-block decomposition.

1. **Target line:** the projected prolate or exact Xi-radical vector.
2. **Finite central block:** anchor-ladder/Christoffel and interval-LDL
   certificates; include every constant, pole and low boundary coordinate here
   rather than pretending they are harmless tails.
3. **Exterior/high block:** packet-leverage/bathtub or source-specific symbol
   floor, with current all-prime square-support tails controlling cross maps.

The full isolation certificate is the absolute Schur estimate

\[
 \operatorname{dist}\!\left(
 \sigma_{\lambda,N},
 \operatorname{spec}
 \begin{pmatrix}
 B&Z^*\\ Z&C
 \end{pmatrix}
 \right)
 \ge g_{\lambda,N},                                      \tag{8}
\]

not a one-sided assertion that the entire complement lies above the target.
This is the key change forced by the Xi-cardinal obstruction.

## Exact unresolved theorem packet

A complete proposal now has three—and only three—new load-bearing obligations.

1. **Prime-side isolated-line theorem.**  Establish (5)--(6) on one cofinal
   sequence using exact CCM entries and source-complete tails, without a
   zero-side line-centering argument.
2. **Non-ground/Darboux real-zero theorem.**  Prove B1 or B2 in the exact finite
   CCM normalization.
3. **Moving-Hardy target rate.**  Establish (7), including every periodization,
   endpoint and rational enclosure loss.

The first and third are quantitative analytic estimates.  The second is the
new conceptual theorem that prevents the programme from silently reimposing
RH through ground-state selection.

## Connections missed by the earlier proposal

### 1. Square-support tails remain useful despite the scalar RH obstruction

The constant square-support coordinate is RH-equivalent, so it cannot prove
whole-matrix positivity.  It can still give exact candidate-row and
cross-block tail estimates inside the two-sided isolation problem (8), where a
negative eigenvalue far below the target is allowed.

### 2. Exterior cardinals naturally fit isolation, not ground selection

`L-19862` gives a complete complement residual gap and an exponentially small
Xi-target residual.  `R-19846` shows why this cannot support a one-sided affine
ground comparison.  The same geometry is well suited to a two-sided singular
value gap around the target line.

### 3. Anchor ladders and Darboux correction belong in the conclusion bridge

The positive-anchor/Christoffel stack should not merely certify another finite
moment table.  Its natural role is to construct a real-rooted finite Darboux
factor that converts an isolated interior Xi-like line into a line covered by a
finite real-zero theorem.

### 4. The reviewed rephasing repair is optional in the prime-side producer

`L-21503` is the correct repair if one continues the zero-side support-average
route.  A direct prime-side matrix producer avoids the entire off-line selector
comparison and therefore avoids both the historical derivative error and the
new stationary-ratio ledger.

# SERIOUS RESOLUTION PATH

**YES — a serious full proposal can be salvaged, but no proof is presently
established.**

The serious path is:

```text
exact prime-side CCM matrix
-> cofinal simple even Xi-like isolated line
-> new non-ground CCM theorem or exact Darboux groundification
-> moving-Hardy convergence
-> finite real-zero approximants
-> Hurwitz
-> RH.
```

This path preserves the strongest independently reviewed mathematics from the
old proposal while explicitly evading the exact off-line-cardinal obstruction
that makes every complete ground-floor estimate RH-bearing.

The decisive next research task is not another support-average constant.  It is
the finite **non-ground/Darboux real-zero bridge**.  Until that theorem is
proved, every prolate full-proof claim must remain conditional.
