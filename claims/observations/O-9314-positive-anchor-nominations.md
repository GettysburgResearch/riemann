# O-9314 — Positive-anchor Schur nominations at the PR #103 atomized minimum

Claim ID: `O-9314`  
Title: A rational positive-anchor ladder approaches both degree-15 Schur boundaries, with an operational nomination at `u=4`  
Status: `EMPIRICAL_NOMINATION_ONLY`  
Authoring agent: `gpt56-04-e`  
Created: 2026-07-26  
Dependencies: L-9314, L-9315, the PR #103 atomized table, and ordinary high-precision direct-xi reconnaissance  
Scope: one exact ordinate and one fixed old node table  
Related counterexample candidates: none allocated

## Cross-route motivation

The exact direct-xi ordinate used by PR #103 is

\[
 T_{\xi}=
 \frac{20225875608343133989267}{2^{32}}
 =4709203636353.633829687489196658\ldots.
\]

The independently discovered optimized carrier-Weil basin uses

\[
 T_W=4709203636353.65.
\]

Their separation is only

\[
 \boxed{T_W-T_{\xi}=0.01617031251080334186553955078125.}
\]

This does not establish a theorem connecting the two criteria, but it identifies
one high-height spectral neighborhood independently selected by two very
different finite-witness programs. That coincidence motivated searching the
strongest new direct-xi extension at this ordinate rather than another unrelated
broad grid.

## Method

Use the fifteen exact directed old moment intervals retained in PR #112/PR #116.
For discovery, take their exact rational midpoints and apply L-9314 to an added
node `w`. Compute `b_0` by the L-9315 reduced formula using:

- the committed old moments;
- the old reference `u=2^-40`;
- one ordinary high-precision direct completed-xi value at the new node;
- the same PR #103 atomized deflation shells.

The direct completed-xi values below were evaluated with `mpmath` at 70 decimal
digits. They are not balls, and no displayed gap is a certificate.

## Discovery ladder

| `w` | new `x=sqrt(w)` | midpoint lower gap | midpoint upper gap | `|beta_w|` | lower gap in new-primitive units |
|---:|---:|---:|---:|---:|---:|
| `1/2` | irrational | `7.55719e-4` | `3.84637e-3` | `6.57070e4` | `1.15013e-8` |
| `3/4` | irrational | `4.19566e-5` | `1.72489e-4` | `9.99480e1` | `4.19785e-7` |
| `1` | `1` | `4.05033e-6` | `1.45860e-5` | `1.00130` | `4.04506e-6` |
| `3/2` | irrational | `1.02527e-7` | `3.14392e-7` | `1.52376e-3` | `6.72858e-5` |
| `2` | irrational | `5.87776e-9` | `1.63642e-8` | `1.52687e-5` | `3.84954e-4` |
| `3` | irrational | `7.61889e-11` | `1.89395e-10` | `2.32407e-8` | `3.27826e-3` |
| `4` | `2` | `2.85750e-12` | `6.65248e-12` | `2.32906e-10` | `1.22689e-2` |

Every sampled midpoint lies inside its two-sided gate. Thus none is a midpoint
counterexample.

The first rows are closest after scaling by the new-point coefficient, but they
require irrational `x` or evaluation nearer the critical strip. The node `w=4`
is the cleanest immediate proof target:

- `x=2` is exact and rational;
- `Re(s)=5/2`, where zeta evaluation is much easier;
- the old-moment uncertainty is negligible;
- a new residual interval much narrower than about `0.012` should determine the
  lower-gate side.

## Detailed `w=4` nomination

The exact midpoint Schur gate is

```text
lower = 27375115.777156106833382709427812248840180616454318036053790465...
upper = 27375115.777156106842892683978586165757453355175062709820119909...
width = 9.5099745507739169172727387207446737663e-12.
```

The ordinary 70-digit reduced contraction gave

```text
b0 = 27375115.7771561068362402083762353934903793236139845753700031...
```

so

```text
b0-lower = 2.8574989484231446501987071596665393e-12,
upper-b0 = 6.6524756023507722670740315610781345e-12.
```

The new-point coefficient is

```text
beta_w = -2.3290645462119429955497085867313473e-10.
```

The exact contribution of every old moment-box width to the reduced `b0` box is
below

```text
7.071e-33.
```

Thus the lower midpoint gap corresponds to a new-residual displacement of about

```text
0.01226886971883481047.
```

This is operationally generous for a 512/640-bit completed-xi computation.

The direct reconnaissance residuals used were

```text
F(2^-40) = -7397199774203.28426529438836013577502530347204908870517...
F(4)     = -7397199774188.653968390089146758157030260827621719187847548888...
```

Again, these are midpoint controls only.

## Possible candidate handoff

The following finite computation is worth pursuing immediately:

1. patch the reviewed PR #103 completed-xi producer to emit one point at `x=2`;
2. evaluate at 512 and 640 bits and require nested rectangles;
3. retain the same ordinate, common xi scale, normalization, and atomized count
   profile;
4. compute `b0` through both:
   - the direct seventeen-point response-1 contraction;
   - the L-9315 one-new-point reduced replay;
5. require the two `b0` intervals to overlap;
6. contract both exact L-9314 Schur witnesses;
7. nominate an RH counterexample only if one complete quadratic interval has
   strict negative upper endpoint.

A positive result would still be useful: it would close the full degree-15 cone
for this positive anchor and validate the Geronimus extension pipeline.

## Broader proposed scan

After the exact `w=1` and `w=4` controls, use rational-square anchors

\[
 w=x^2,
 \qquad
 x\in\{1/2,1,3/2,2,5/2,3\}.
\]

Rank centers by the minimum primitive-normalized Schur repair moat from L-9315.
This is far cheaper than regenerating a full old moment table at every node.

## Classification and warnings

- The L-9314/L-9315 algebra is exact; the numerical `b0` values here are not.
- The PR #103 old basin is rigorously positive for degree at most 14. This note
  explores a genuinely new degree-15 primitive, not another optimization inside
  that closed cone.
- No negative directed interval exists and no `Z-####` candidate is allocated.
- The height coincidence with the carrier basin is inspiration, not evidence of
  RH failure.
