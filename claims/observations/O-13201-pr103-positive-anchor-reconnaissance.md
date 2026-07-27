# O-13201 — Positive-anchor reconnaissance on the PR #103 direct-xi table

Claim ID: O-13201  
Title: Moderate positive anchors produce a degree-21 candidate table with no empirical negative  
Status: EMPIRICAL  
Authoring agent: `gpt56-03-i`  
Created: 2026-07-26  
Dependencies: L-13201, L-13202, PR #103 atomized table, PR #112 directed old moments  
Scope: one exact ordinate and ordinary-high-precision new-anchor values  
Related counterexample candidates: none

> Canonical-ID note: this observation supersedes temporary `O-12101`, withdrawn
> after the concurrent `L-1210x/X-1210x` allocation was discovered.

## Source table

The scan uses

\[
 T=\frac{20225875608343133989267}{2^{32}}
\]

and old nodes

\[
 u=2^{-40},2^{-38},\ldots,2^{-10}.
\]

The directed old moment basis has Git blob

```text
174db078d3442e89d3be458a306b1122025cfd51
```

and the atomized primitive certificate has Git blob

```text
a02e20c083db8da00a9bd3629179b25c6469ea00.
```

Old intervals were replaced by their midpoints for discovery. New completed-xi
values used ordinary 50--60 digit Riemann--Siegel arithmetic. No displayed sign
is directed.

## Consistency control

At the zero anchor, the implementation reproduces PR #117's reported midpoint
values:

```text
b0                 451708942.5161826304...
Schur threshold    451708930.0045504368...
gap                        12.5116321936...
```

This checks normalization conventions only.

## Candidate PA-1

For `w=1`, equivalently `x=1`, the two empirical boundary distances are
approximately

```text
lower  4.0503336772e-6
upper  1.4585952792e-5.
```

This is the cheapest two-sided proof control; the new point has real part
`3/2`.

## Candidate PA-3

For

\[
 W_3=(1/8,3/16,1/4),
\]

three new values raise the complete degree from 14 to 17. The diagonally
normalized midpoint minima are approximately

```text
H0  3.7035390171e-11
H1  1.7756286345e-10.
```

No matrix is negative. PA-3 is the recommended first multi-anchor directed
packet.

## Candidate PA-7

For

\[
 W_7=(1/8,3/16,1/4,3/8,1/2,3/4,1),
\]

seven new values raise the complete degree to 21. Both final matrices are
`11 x 11`. Ordinary midpoint arithmetic gives

```text
raw min H0          1.0255423430e-8
raw min H1          3.1927594705e-8
normalized min H0   3.8037205202e-13
normalized min H1   2.6692027329e-12.
```

PA-7 is a candidate table, not a counterexample candidate.

## Priority correction from independent work

Concurrent PR #134 independently confirms the one-positive-anchor theorem and
reports the strongest scale-invariant single-anchor row in the combined scans:

```text
x=1/20, w=1/400,
relative lower-wall position about 0.0018744703.
```

Concurrent PRs #124/#128 nominate `x=2`, `w=4`, whose new point has real part
`5/2` and is attractive for an independent right-half-plane backend.

The revised production order is:

1. finish the already implemented `w=1` theorem regression;
2. run `w=1/400` as the scale-free one-anchor finalist;
3. run `w=4` with two distinct completed-xi implementations;
4. validate PA-3;
5. use L-13203 line-mass budgets on frozen PA-3 directions;
6. escalate PA-7 only after source-survival bookkeeping is complete.

## Guard against false progress

Raw boundary gaps shrink rapidly for large anchors because the rank-one vector
contains powers of `w`. This algebraic collapse is not evidence for an off-line
zero. Even diagonally normalized minimum eigenvalues are scheduling statistics,
not theorem quantities: higher-degree moment matrices can become naturally
ill-conditioned.

Production accepts only a strict directed rational fixed-vector sign, a complete
interval positive-definiteness proof, or an L-13203 certified line-mass budget
reversal.

## Proof boundary

- No new anchor primitive in this observation is directed.
- No negative matrix or response was found.
- No counterexample or `Z-####` identifier is allocated.
- A future negative or positive-budget reversal requires independent primitive
  reproduction and review of all inherited response and count-deflation gates.
