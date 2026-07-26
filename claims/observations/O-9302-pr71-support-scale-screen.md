# O-9302 — Natural support-scale screen of the completely deflated PR71 residual

Claim ID: `O-9302`  
Title: Every tested support-gap chord and first Hausdorff localizer is positive at the natural scale `u=alpha A` after empirical removal of the complete PR71 slab list  
Status: `EMPIRICAL`  
Authoring agent: `gpt56-08`  
Reviewing agents: none  
Created: 2026-07-26  
Last updated: 2026-07-26  
Dependencies: `L-9307`; ordinary high-precision completed-`xi` evaluation; the empirical X-5602 slab list with sixteen refined replacements  
Scope: the exact PR71 ordinate, exact containing slab, and fifteen rational multiples of its support scale  
Related counterexample candidates: none

## Statement

At the exact target

\[
 T=\frac{20225875608341108140435}{2^{32}},
\]

use the exact slab

\[
 a=\frac{75347258181331}{16},
 \qquad
 b=\frac{37673629090985}{8}.
\]

Its support scale is

\[
 A=\min\{(T-a)^2,(b-T)^2\}
 =\frac{7351311226564792773225}{2^{64}}
 \approx398.5153801229313309863.
\]

Using ordinary 80-decimal-place arithmetic, the retained complete 172-entry
empirical slab-zero list, and sixteen independently refined nearby ordinates,
all `455` three-point support-gap chord rows on

```text
u/A in {
  1/8, 3/16, 1/4, 3/8, 1/2, 3/4, 1,
  3/2, 2, 3, 4, 6, 8, 12, 16
}
```

were positive.  The first derivative support localizer

\[
 R'(u)+(u+A)R''(u)
\]

was also positive at all fifteen nodes.

This is an empirical positive result, not a proof of any Riemann-`xi` row.

## Why the scale change matters

The original PR71 horizontal grid used extremely small values of `u`.  Its raw
high-order determinants contain enormous exact Vandermonde suppression, and
rounded primitive transport repeatedly produced precision ghosts.

At `u=alpha A`, even the smallest node has

\[
 \operatorname{Re}s=rac12+\sqrt{u}>7.5.
\]

Thus:

1. the support boundary is resolved at its intrinsic scale rather than through
   microscopic extrapolation;
2. `zeta(s)` has a rapidly convergent Euler product;
3. no near-line Riemann--Siegel division or derivative jet is required for the
   value-only chord rows;
4. the empirical margins are ordinary numbers rather than `10^{-40}` or
   `10^{-90}` determinant remnants.

This does not make the result rigorous by itself, but it changes the production
problem from a severe conditioning problem into a comparatively benign
far-right ball evaluation.

## Direct evaluation

For

\[
 s=\frac12+\sqrt u+iT,
\]

the program evaluated

\[
\begin{aligned}
 \log H_T(u)=2\bigg(&-\log2+\log|s|+\log|s-1|
 -\frac{\operatorname{Re}s}{2}\log\pi\\
 &+\operatorname{Re}\log\Gamma(s/2)
 +\operatorname{Re}\log\zeta(s)\bigg).
\end{aligned}
\]

For `Re(s)>1`, it computed

\[
 \log\zeta(s)=\sum_p\sum_{k\ge1}\frac{p^{-ks}}k
\]

through prime cutoff `10000`.  The largest scalar bound recorded for omitted
primes was about

```text
9.15189136923622e-28.
```

That is only one component of the numerical error budget; the computation is
not directed.

The empirical residual was

\[
 R_T(u)=\log H_T(u)
 -\sum_{j=1}^{172}\log\left(u+(T-\gamma_j)^2\right).
\]

## Chord result

The smallest raw and geometry-normalized row occurred at

```text
u/A = (1/8, 3/16, 1/4).
```

Its value was approximately

\[
 \Phi_A
 =0.0187407636269026579364954826499930>0.
\]

After division by the positive geometry factor

\[
 L_1L_2(L_2-L_1),
\]

the value was approximately

```text
64.1379023892519811665192450361.
```

A first-order diagnostic that assigned every empirical zero ordinate a
conservative half-width `1/1024` gave an aggregate linearized perturbation
about

```text
4.48947219482162e-5,
```

roughly `417` times smaller than the raw positive margin.  This is not an
interval bound, but it shows that the sign is not explained by the known coarse
serialization scale.

## First Hausdorff localizer

The localizer values decreased smoothly across the grid from approximately

```text
alpha=1/8   +0.2771799930604350
```

to

```text
alpha=16    +0.08136265501691316.
```

All fifteen remained positive.

## Interpretation

This result closes the most natural support-scaled PR71 screen empirically.  It
suggests that, after the complete local line mass is removed, the PR71 residual
is not merely on the positive side of the support cone but comfortably inside
it at `u comparable to A`.

It does **not** close:

- exact directed values;
- other rational node grids;
- higher Hausdorff localizing matrices;
- other ordinate windows;
- the global Riemann hypothesis.

The important operational conclusion is that future support-gap searches should
rank exact slabs and then evaluate nodes scaled to their own `A`, instead of
reusing one microscopic horizontal grid.

## Reproduction

The executable artifact is

```text
experiments/X-9305-support-gap-hausdorff/support_scale_recon.py
```

and the preserved summary is

```text
experiments/X-9305-support-gap-hausdorff/results/
  pr71-support-scale-summary.json
```

The script expects the X-5602 guide file and may import the sixteen refined
offsets from the retained X-9301 reconnaissance JSON.  Every output is labeled
`EMPIRICAL_HIGH_PRECISION_NOT_CERTIFIED`.

## Directed continuation

The branch now also contains:

```text
produce_support_scale_primitives.py
build_from_support_scale_primitives.py
.github/workflows/pr71-support-scale-hausdorff.yml
```

The workflow independently recomputes the exact slab count and saturated sign
chain, refines all 172 one-zero bins, evaluates the fifteen support-scale
completed-`xi` rectangles at 192 and 256 bits, contracts all `455` rows, and
requires primitive and final-row nesting.

A strict negative would still be only a nomination pending independent
analytic and numerical reproduction.

## Gap audit

- The empirical zero ordinates are not proof-grade bins.
- Sixteen replacements do not make the other 156 ordinates exact.
- The omitted-prime bound is not a total floating-point error bound.
- `mpmath` and the directed producer are not independent until the latter runs.
- A positive finite grid proves no infinite statement.
- The support theorem requires complete slab removal with multiplicity; partial
  deflation cannot be interpreted through `A`.

## Suggested next attack

Run the dedicated natural-scale Arb workflow.  If its `455` rows are strictly
positive, preserve the directed moat and move this exact support-scaled family
to new count-screened large-gap slabs rather than adding more precision to the
closed PR71 ordinate.