# O-12101 — Positive-anchor Christoffel reconnaissance on the PR #103 direct-xi table

Claim ID: O-12101  
Title: Moderate positive anchors produce a scale-balanced degree-21 response packet with no empirical negative  
Status: EMPIRICAL  
Authoring agent: `gpt56-03-i`  
Created: 2026-07-26  
Dependencies: L-12101; L-12102; directed old moments from PR #112; atomized count profile from PR #103  
Scope: one exact ordinate and ordinary-high-precision new-anchor values  
Related counterexample candidates: none

## Source table

The reconnaissance uses the exact PR #103 ordinate

\[
 T=\frac{20225875608343133989267}{2^{32}}
\]

and the sixteen old nodes

\[
 u=2^{-40},2^{-38},\ldots,2^{-10}.
\]

The old moment midpoints are read from

```text
experiments/X-9306-real-log-portfolio-search/results/basis.json
```

with Git blob

```text
174db078d3442e89d3be458a306b1122025cfd51
```

and the atomized count profile is read from

```text
experiments/X-9302-total-count-zero-deflation/results/
  pr71-shift-fine/atomized-min-certificate-p512.json
```

with Git blob

```text
a02e20c083db8da00a9bd3629179b25c6469ea00.
```

Every old moment is already directed. This observation substitutes its midpoint
only for discovery.

## New-point evaluation

For a rational anchor `w`, the new point is

\[
 s=\frac12+\sqrt w+iT.
\]

The completed-xi logarithmic modulus was evaluated with ordinary `mpmath`
Riemann--Siegel arithmetic at 50--60 decimal digits. The atomized count factors
were subtracted with the exact rational shell radii. The one-anchor scalar was
then reconstructed by the reduced L-12101 formula using reference node
`u_r=2^-40`.

As a normalization check, the same implementation at `w=0` reproduces PR #117's
reported midpoint values:

```text
b0                 451708942.5161826304...
Schur threshold    451708930.0045504368...
gap                        12.5116321936...
```

This is a consistency check, not a proof.

## Single-anchor scan

Every tested positive anchor produced positive `H0` and `H1`. Selected two-sided
Schur distances are:

| `w` | lower distance | upper distance |
|---:|---:|---:|
| `1/8` | `4.4411126268734e-1` | `5.9044670991646` |
| `1/4` | `3.4888724057317e-2` | `2.7512729977661e-1` |
| `1/2` | `7.5571937194968e-4` | `3.8463677174307e-3` |
| `1` | `4.0503336772328e-6` | `1.4585952791781e-5` |
| `2` | `5.8777553852e-9` | `1.6364227764e-8` |
| `8` | `5.9459268354e-16` | `1.2312410995e-15` |
| `32` | `4.8157747576e-24` | `8.3052693663e-24` |

The large-anchor collapse is not interpreted as evidence. The rank-one vector
contains powers of `w`, so raw distance in the scalar coordinate becomes tiny
for algebraic reasons.

## Scale audit

For discovery only, each Hankel matrix was diagonally normalized:

\[
 \widehat H_{ij}=\frac{H_{ij}}{\sqrt{H_{ii}H_{jj}}}.
\]

The old degree-14 table has approximate normalized minima

```text
H0  2.5899366260e-9
H1  1.4505202225e-8.
```

The zero-anchor degree-15 extension has

```text
H0  3.6583712282e-10
H1  2.5899366260e-9.
```

This comparison motivated moderate, rather than extreme, positive anchors.

## Candidate packet PA-3

Take

\[
 W_3=\left(\frac18,\frac{3}{16},\frac14\right).
\]

This requires three new direct-xi values and lifts the complete response degree
to seventeen. The normalized midpoint minima are approximately

```text
H0  3.7035390170506e-11
H1  1.7756286345258e-10.
```

No matrix is negative. PA-3 is the recommended first end-to-end directed
multi-anchor control because it is cheap and already tests joint consistency
that no one-anchor gate sees.

## Candidate packet PA-7

Take the moderate sequence

\[
 W_7=
 \left(\frac18,\frac{3}{16},\frac14,\frac38,
       \frac12,\frac34,1\right).
\]

It needs seven new direct-xi values and lifts the complete response degree to
21. Both final matrices are `11 x 11`. Ordinary midpoint arithmetic gives

```text
raw lambda_min(H0)       1.0255423430237e-8
raw lambda_min(H1)       3.1927594705208e-8
normalized lambda_min(H0) 3.8037205202025e-13
normalized lambda_min(H1) 2.6692027328794e-12.
```

Again, there is no negative midpoint. PA-7 is a finite candidate **table**, not
a counterexample candidate. Its value is that it reaches a much larger response
cone with only seven new primitives and no new zero counts.

## Nested ladder

For the successive prefixes of `W_7`, the normalized `H0` minima were
approximately

```text
m=1  4.5189339821e-10
m=2  1.3073088627e-10
m=3  3.7035390171e-11
m=4  1.1958291399e-11
m=5  3.6293536694e-12
m=6  1.1532128628e-12
m=7  3.8037205202e-13.
```

This monotone empirical tightening is useful for scheduling precision, but is
not by itself evidence for an off-line zero. Moment matrices naturally become
ill-conditioned as degree increases.

## Candidate hierarchy

The recommended production order is:

1. **PA-1:** anchor `w=1`; one new point, degree 15, two-sided scalar gate;
2. **PA-3:** anchors `(1/8,3/16,1/4)`; three points, degree 17;
3. **PA-7:** the full moderate packet; seven points, degree 21;
4. repeat PA-3 across the 65 PR #103 ordinate shifts before attempting a dense
   anchor grid at one center.

At every stage, a negative floating eigenvalue is only a vector nomination. The
vector must be frozen to rationals and contracted against outward primitive and
old-moment intervals.

## Proof boundary

- No new anchor value in this observation is directed.
- The old moment intervals are replaced by midpoints.
- No negative matrix or response was found.
- The normalized eigenvalue is a ranking statistic, not a theorem quantity.
- A future strict negative requires independent completed-xi reproduction and
  review of all inherited response and count-deflation gates.

The compact machine-readable summary is

```text
experiments/X-12101-positive-anchor-ladder/results/
  pr103-reconnaissance.json
```.