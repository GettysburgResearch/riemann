# L-0304 — Winding-number stability under uniform error

Claim ID: L-0304  
Title: Winding number is stable under a uniform nonvanishing perturbation  
Status: PROPOSED  
Authoring agent: `gpt56-03`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: homotopy invariance of winding number  
Scope: certified polygonal image-loop kernel  
Related counterexample candidates: direct zeta, Speiser, and Newman rectangles

## Statement

Let `gamma, eta:[0,1]->C` be continuous closed loops.  Suppose
\[
 \delta:=\sup_{t\in[0,1]}|\gamma(t)-\eta(t)|
   < m:=\inf_{t\in[0,1]}|\eta(t)|.
\]
Then neither loop passes through `0`, and
\[
 \operatorname{wind}(\gamma,0)=\operatorname{wind}(\eta,0).
\]

Thus, if `eta` is a rational polygonal loop with exactly computable winding
number and a rigorous enclosure proves the displayed inequality, `gamma` has
the same winding number.

## Proof

The lower bound `m>delta>=0` shows `eta(t)!=0`.  Also
\[
 |\gamma(t)|\ge|\eta(t)|-|\gamma(t)-\eta(t)|
              \ge m-\delta>0,
\]
so `gamma` avoids zero.

Define the straight-line homotopy
\[
 H(s,t)=(1-s)\eta(t)+s\gamma(t)
       =\eta(t)+s(\gamma(t)-\eta(t)).
\]
For every `(s,t)`,
\[
 |H(s,t)|
 \ge |\eta(t)|-s|\gamma(t)-\eta(t)|
 \ge m-\delta>0.
\]
Hence `H` is a homotopy through closed loops in `C\setminus\{0\}` from `eta`
to `gamma`.  Winding number about zero is invariant under such a homotopy, so
the two winding numbers agree.  ∎

## Motivation

Certified contour integration can be expensive.  Often it is simpler to
enclose the full image of each contour segment, connect rigorous sample balls
by a rational polygon, and prove that the true image loop stays within a
uniform tube that misses zero.

## Analytic domain audit

This lemma is purely topological.  In applications, analyticity is needed
separately to identify winding number with a zero count through L-0302.

## Dependency audit

Only homotopy invariance of winding number is used.  A reviewer may replace
that imported fact by the standard integral definition for piecewise smooth
loops and a differentiation-under-the-integral proof.

## Gap audit

- `inf |eta|` must be a proved lower bound for the entire polygon, including
  edges, not just vertices.
- The error must cover the entire true image segment.
- Balls overlapping zero invalidate the certificate even if their midpoints do
  not.
- Polygon self-intersection is allowed, but winding must be computed with
  orientation and multiplicity.

## Adversarial tests

- Perturb a unit circle by error `<1`: winding remains one.
- Allow error `=1`: the straight homotopy may hit zero.
- Reverse polygon orientation: winding changes sign.
- Use a figure-eight loop: local visual intuition must be replaced by exact
  winding arithmetic.

## Remaining uncertainty

No mathematical gap is known.  A standard exact polygon-winding verifier
should be added to the repository.

## Suggested next attack

Define a JSON certificate containing rational contour vertices, complex balls
for function images, segment Lipschitz bounds, and the exact polygon winding.
