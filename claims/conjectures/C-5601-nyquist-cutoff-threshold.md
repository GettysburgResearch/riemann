# C-5601 — The D-0801 margin can only collapse once `c >= T/(2 pi)`

Claim ID: C-5601
Title: Nyquist threshold for the piecewise carrier family: the cutoff must reach
`T/(2 pi)` before the leading margin can approach zero
Status: EMPIRICAL (heuristic; the predicted threshold effect has now been
observed directly in certified data — see the second table. **Not** proved.)
Authoring agent: `opus5-01`
Reviewing agents: none
Created: 2026-07-25
Last updated: 2026-07-25
Dependencies: D-0801; T-5601; O-5601
Scope: the D-0801 family at large carrier `T`
Related counterexample candidates: none yet — this claim says *where to look*

## Statement (heuristic)

Let `Delta = log(c)/(2 pi)` and `ell_T = log(T/2 pi)/(2 pi)`.  Then the D-0801
leading margin `ell_T - lambda_max(S_K(T,c))` is bounded away from zero, by an
amount that decreases as `Delta` rises, for every

\[
 \Delta<\ell_T
 \qquad\Longleftrightarrow\qquad
 c<\frac{T}{2\pi},
\]

and only for `c >= T/(2 pi)` can the family drive the exact form close to zero.

At the parameters used throughout Issue #55,

\[
 T=4709203636353.65,
 \qquad
 \frac{T}{2\pi}=749{,}493{,}036{,}752 = 10^{11.8748},
\]

so **the executed target `c = 10^11` sits a factor `7.5` below the threshold**,
and `c = 10^12` is the first decade past it (`Delta = 4.39761` against
`ell_T = 4.35172`).

## Heuristic argument

By T-5601, `sum_rho g_{T,v}(z_rho) = h\,v^{*}(A_K+R_K-S_K)v`, and on the real
axis

\[
 g_{T,v}(r)=\tfrac12\left(|W_v(r-T)|^2+|W_v(-r-T)|^2\right)\ge0 .
\]

Under RH every `z_rho` is real, so the sum is a sum of nonnegative terms.  It can
be small only if `|W_v(\gamma-T)|` is small at *every* zero ordinate `gamma` in
the window where `g` has appreciable mass (the second term is negligible: it is
evaluated near `-2T`).

`W_v` is the Fourier transform of a function supported on an interval of length
`Delta`, hence entire of exponential type `pi Delta` and bounded on the real
axis.  A nonzero function of that class has real-zero density at most `Delta`
per unit length.  The nontrivial zeros near height `T` have density `ell_T` per
unit length by Riemann–von Mangoldt.  So the family simply does not have enough
zeros to place:

\[
 \text{available zero density }\Delta
 \quad\text{vs}\quad
 \text{required zero density }\ell_T .
\]

When `Delta < ell_T` a positive fraction of the zeros must be left un-cancelled,
and the residual margin is what O-5601 measures.  When `Delta >= ell_T` the
counting obstruction disappears and nothing elementary prevents the margin from
collapsing.

The two densities have the *same* functional form, `log(\cdot)/2\pi`, which is
why the threshold is exactly `c = T/2\pi` and not some parameter-dependent
constant.  This is the same counting that governs the Beurling–Selberg extremal
problem and one-level density calculations; the novelty here is only its use as
a *search heuristic* for the D-0801 program.

## Direct test: a carrier low enough to straddle the threshold

The cheap adversarial test suggested below was executed.  Taking

\[
 T=62{,}831{,}853{,}071,\qquad \frac{T}{2\pi}=9.99999999997\times10^{9},
\]

puts the Nyquist threshold at `c^{*} = 10^{10}`, so the whole reachable ladder
`10^7 .. 10^{11}` straddles it.  Certified universal margins (`K = 1024`,
`b \le 1/20` verified at every point, positivity certified at every point):

| `c` | `Delta` | `Delta - ell_T` | certified margin | factor vs previous |
|---|---|---|---|---|
| `10^7`  | 2.565275 | `-1.099403` | `3.87378e-1` | — |
| `10^8`  | 2.931742 | `-0.732936` | `1.93912e-1` | 2.0 |
| `10^9`  | 3.298210 | `-0.366468` | `1.21071e-1` | 1.6 |
| `10^10` | 3.664678 | `+0.000000` | `3.55470e-2` | 3.4 |
| `10^11` | 4.031146 | `+0.366468` | `5.29784e-4` | **67** |

The margin falls by factors of `2.0`, `1.6`, `3.4` while the cutoff is below the
threshold, and then by a factor of **67 in the single decade that crosses it**.
That is the predicted qualitative change, at the predicted place, and it is the
main evidence for this claim.  It is one carrier and five points; it is not a
proof, and the collapse is not to zero.

## A sharper signature: the `K^{-2}` law

`O-5603` sweeps `K` as well as the deficit, at `c = 10^9`.  The leading margin

- **saturates in `K` below the barrier** — at deficit `0` the ratios
  `K = 1024 : 2048 : 4096` are `1.5, 1.1`;
- **falls like `K^{-2}` past it** — at deficits `+0.37, +0.73, +1.10, +1.47` the
  successive ratios cluster tightly on `4`.

This is a cleaner diagnostic than the cutoff ladder, and it is what the counting
argument predicts: below the barrier extra cells cannot buy new zeros to place,
past it they can.  It also means the binding constraint changes character past
the barrier, because the `L-4202` gate grows like `K` while the margin falls
like `K^{-2}` — see `O-5603` and `Q-5605`.

## Supporting certified data (O-5601)

Same carrier, `K = 1024`, certified universal margins:

| `c` | `Delta` | `ell_T - Delta` | certified margin |
|---|---|---|---|
| `10^7` | 2.56655 | 1.78517 | `2.74985e-2` |
| `10^8` | 2.93320 | 1.41852 | `6.64147e-3` |
| `10^9` | 3.29984 | 1.05188 | `2.34871e-3` |
| `10^10` | 3.66649 | 0.68523 | `6.05896e-4` |
| `10^11` | 4.03315 | 0.31857 | `2.67186e-4` |
| `10^12` | 4.39761 | `-0.04589` | **past the threshold; not yet run** |

The margin falls by a factor of roughly `2.3` to `2.6` per decade of `c` while
the deficit `ell_T - Delta` falls linearly.  Naive log-linear extrapolation to
the threshold gives `~1e-4`, i.e. the collapse is *not* predicted to be abrupt
at exactly `c = T/2\pi`; the heuristic locates a barrier, it does not predict the
shape of the curve past it.

## What this changes about the search

1. **Every D-0801 computation so far has been below the threshold.**  PR #37,
   PR #44, the `c=10^11` target of Issue #55 and the ladder of O-5601 are all at
   `c <= 10^11 < T/2\pi`.  A positive margin there is what the counting argument
   predicts, so those results, including O-5601, are *not* evidence that the
   family fails — they are evidence that it was never given enough support.
2. **The decisive experiment is `c >= 10^12` at the same carrier.**  That is
   `pi(10^12) = 37{,}607{,}912{,}018` prime powers, about `9.1x` the executed
   run, so roughly one hour on four cores with the L-5601 producer.  It was
   unreachable with a per-term MPFR kernel and is reachable now.
3. **`K` must grow with `c`.**  L-4202 needs `b = 2\log c/K \le 1/20`, i.e.
   `K \ge 40\log c`.  At `c = 10^{12}` that is `K \ge 1106`, so `K = 2048`.
   The stream cost is independent of `K`; only the `K x K` certificate step
   grows, as `K^3`.
4. **The correction gate becomes load-bearing.**  `B_A \approx 1.66e-10` is the
   resolution floor of the leading screen.  Once a certified margin drops below
   `~1e-8`, `L-4202`'s uniform envelope must be replaced by the exact
   archimedean Toeplitz matrix of `L-4201`, and both L-4202 and L-4203 need
   independent review first.
5. **Under RH the margin stays `>= 0` however far one pushes.**  Crossing the
   threshold does not manufacture a counterexample; it makes the computation a
   *sharp* test rather than a foregone conclusion.  A certified negative value
   past the threshold would be the counterexample; a certified small positive
   value would be a quantitative statement about the zeros near height `T`.

## Interaction with carrier optimization

The two effects are roughly independent and both are large.

- Unoptimized carrier `T = 62831853071`, deficit `Delta - ell_T = -0.366`
  (`c = 10^9`): certified margin `1.21e-1`.
- Optimized carrier `T = 4709203636353.65`, deficit `-0.319` (`c = 10^{11}`):
  certified margin `2.67e-4`.  Same side of the threshold, comparable deficit,
  and `450x` smaller.
- O-5602 measures the carrier effect separately: a `46x` spread over a 51-unit
  carrier window at fixed `c`, with the tuned carrier `16x` below the mean.

Multiplying the observed threshold effect (`~67x` per decade past the barrier)
by the observed carrier effect (`10^2` to `10^3`) puts margins of order
`10^{-8}` to `10^{-9}` within reach of a search that does both.  That is the
scale at which the `L-4202` correction gate `B_A \approx 1.7\times10^{-10}`
stops being negligible, so the exact archimedean block of `L-4201` and an
independent review of `L-4202`/`L-4203` become prerequisites rather than
refinements.  **This is the concrete path from the present state of the project
to a computation whose sign is genuinely in doubt.**

## Gap audit

1. This is a heuristic supported by one five-point ladder and one carrier scan.  The zero-density statement for exponential type
   `pi Delta` is classical, but the step from "cannot vanish at all zeros" to
   "the margin is bounded below by a specific amount" is *not* made rigorous
   here, and the converse direction is pure heuristic.
2. The argument assumes RH in order to say the terms are nonnegative.  Without
   RH the sum has no sign, which is exactly the phenomenon being hunted; the
   heuristic therefore describes where the *test* becomes sensitive, not where
   a counterexample exists.
3. The finite cell count `K` restricts the envelope shape, so the family does
   not realize every function of type `pi Delta`; the threshold is necessary,
   not sufficient.
4. The "effective window" of `g` is not compact — `g` decays like `r^{-2}`, so
   distant zeros contribute a nonzero tail that the counting argument ignores.
5. The extrapolation in the table is a curve fit over five points and must not
   be quoted as a prediction.

## Adversarial tests

1. Run `c = 10^{12}`, `K = 2048` at the same carrier and compare the certified
   margin with the extrapolation.  A margin *far* below the extrapolated `1e-4`
   supports the heuristic; a margin on the extrapolated line refutes its
   sharpness.
2. Move the carrier down so that `T/2\pi` falls below `10^{11}` — e.g.
   `T = 2\pi \cdot 10^{10} \approx 6.28e10` — and check whether the certified
   margin at `c = 10^{11}` (now above threshold) is dramatically smaller than at
   a carrier of the same size with `c` below threshold.  This tests the
   threshold at reachable cost in both directions.
3. Vary `K` at fixed `c` above the threshold; if the heuristic is right, the
   margin should keep falling with `K`, whereas below the threshold it should
   saturate.

## Remaining uncertainty

I am confident about the counting statement and about where the threshold sits.
I am not confident that the margin actually collapses past it: the finite-`K`
constraint, the `r^{-2}` tail, and the archimedean correction all push the other
way, and the five-point ladder is equally consistent with a smooth decay that
never reaches zero.

## Suggested next attack

Adversarial test 2 first — it is the cheap one.  Lowering the carrier to
`T \approx 2\pi\cdot10^{10}` makes `c = 10^{11}` an *above-threshold* cutoff at
`4.1e9` terms, i.e. five minutes, instead of `3.8e10` terms at `c = 10^{12}`.
If the heuristic has any force, that comparison will show it.
