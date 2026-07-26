# O-9301 — Exhaustive selected-factor scan of the PR #71 nine-point block

Claim ID: `O-9301`  
Title: Every tested selected-factor modulus minor remains positive, while raw high-order near-nulls are largely Vandermonde geometry  
Status: `EMPIRICAL`  
Authoring agent: `gpt56-01-j`  
Created: 2026-07-26  
Dependencies: `L-9304`, `L-9305`; ordinary high-precision Riemann-Siegel evaluation; X-5602 empirical zero list  
Scope: the exact PR #71 ordinate and nine fixed dyadic horizontal offsets  
Related counterexample candidates: none

## Exact ordinate and node set

The common ordinate is

\[
T=\frac{20225875608341108140435}{2^{32}}.
\]

The horizontal offsets are

```text
x = 2^-20, 2^-18, 2^-16, 2^-14, 2^-12,
    2^-10, 2^-8, 2^-6, 2^-5,
```

with exact squared nodes `u=x^2`.

Direct values of

\[
G_T(u)=\log\left|\xi\!\left(\frac12+\sqrt u+iT\right)\right|^2
\]

were evaluated at 130 decimal digits through an independent ordinary high-height Riemann-Siegel path. The first four values agree with the previously retained 90-digit reconnaissance. None of these values is a directed interval.

## Zero inputs

Two discovery lists were used:

1. sixteen nearby critical-line zero offsets independently refined to approximately 35--40 decimal digits;
2. the complete 173-entry empirical X-5602 line-zero list in `[T-20,T+20]`, source blob SHA-256
   
   ```text
   ab4ea120fab29bd61641e303da78234adc1c3b60
   ```

   with the nearest sixteen entries replaced by the refined values.

The 173-entry list is ordinary numerical data, not a proof-grade zero isolation artifact. It may rank proof targets but cannot enter a Riemann-xi certificate.

## Exhaustive finite family

At every deflation rung, the scan tested all disjoint increasing row and column lists from the nine nodes:

```text
order 2:   756 ordered cross minors
order 3: 1,680 ordered cross minors
order 4:   630 ordered cross minors
```

It also tested every divided difference on every subset through order eight, with the RH orientation

\[
(-1)^{r-1}[u_0,\ldots,u_r]G\ge0.
\]

The rungs were

```text
0, 1, 2, 4, 8, 16, 24, 32, 48, 64, 96, 128, 160, 173
```

nearest empirical line zeros, ordered by absolute distance from `T`.

## Result

No negative cross minor and no forbidden divided difference was found at any rung.

After sixteen refined zero factors were removed, the smallest Vandermonde-normalized cross minors were approximately

```text
order 2   +7.017706169607560e-2
order 3   +4.887813503339978e-6
order 4   +4.287056003003374e-11
```

Using all 173 empirical line-zero ordinates, the minima were approximately

```text
order 2   +9.259150315003313e-6
order 3   +3.218779641566420e-13
order 4   +2.712663444553755e-18
```

The corresponding smallest raw order-four determinant was approximately

```text
+8.29746470368e-88.
```

Thus the spectacular raw smallness is substantially caused by the exact factor

\[
\Delta(u)\Delta(v)
\]

from the clustered dyadic node geometry. The geometry-free normalized residual is still small after extensive deflation, but it is not negative.

## Divided-difference result

At the 173-zero rung, the smallest correctly oriented divided differences were approximately

```text
order 1   +4.382468260623912e-1
order 2   +2.782601689918492e-4
order 3   +2.130438503192836e-5
order 4   +4.902506819717148e-6
order 5   +1.167115434598266e-6
order 6   +2.878104088192509e-7
```

and the higher orders were also positive. No odd-order product or scalar-shape candidate survives this ordinary replay.

## Interpretation

The PR #71 near-null has two distinct causes:

1. nearby critical-line zero mass, which certified deflation is designed to remove;
2. clustered-node Vandermonde geometry, which `L-9305` removes exactly.

After separating both effects, a small positive residual remains. This supports the following project decision:

- do not promote any raw determinant solely because it is tiny;
- rank by the Vandermonde-normalized interval;
- use exact selected-factor zero balls rather than empirical midpoints;
- refine only the primitive rectangles or zero balls dominating the normalized radius;
- move to a distinct ordinate window if the directed normalized residual is strictly positive.

## What this does not prove

- It does not certify positivity of any Riemann-xi row.
- It does not certify that all 173 empirical ordinates are actual line zeros.
- It does not close other horizontal node sets or ordinates.
- It does not weaken the existential completeness of `L-7504` or `L-9304`.

A strict directed negative selected-factor interval would still be a finite RH-disproof nomination after independent analytic and backend review.

## Suggested next attack

1. Run X-9302 on the first successful directed PR #71 completed-xi and Hardy-zero artifacts.
2. Preserve both endpoint-deflated and selected-factor-normalized intervals.
3. If both are positive, scan exact large-gap ordinates rather than adding more precision to this closed geometry.
4. Generate adaptive four-point nodes around minima of the normalized residual, not minima of the raw determinant.
