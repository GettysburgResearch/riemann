# Agent report — matched-pole Pick annihilator

Agent ID: `gpt56-02-e`  
Issue: #39  
Branch: `agent/gpt56-02-e/39-xi-passivity-adversarial-scan`  
Date: 2026-07-23  
Status: exact theorem kernel and rational controls complete; directed Riemann-xi producer pending

## Objective

Continue the full counterexample offense after PR #52's scalar, two-channel, barycentric, and high-height precision audits. The immediate question was whether a proposed off-line zero model can be converted into one exact fixed Pick vector that:

1. never enters the proof as a fitted eigenvector;
2. cancels the modeled pair's positive component exactly;
3. preserves a strict negative pair component;
4. suppresses distant critical-line background;
5. can be consumed unchanged by the active Arb certificate checker in PR #56.

## Rank-two geometry of one off-line pair

At one ordinate `T=gamma`, let a reflected off-line pair be

\[
 1/2+\delta+i\gamma,
 \qquad
 1/2-\delta+i\gamma,
 \qquad d=\delta^2.
\]

For same-height horizontal nodes `x_i`, its Pick contribution is

\[
 K^{(d)}_{ij}
 =2m\frac{x_ix_j-d}{(x_i^2-d)(x_j^2-d)}.
\]

Writing

\[
 \alpha_i=\frac{x_i}{x_i^2-d},
 \qquad
 \beta_i=\frac1{x_i^2-d},
\]

gives the exact rank-two split

\[
 K^{(d)}=2m(\alpha\alpha^{\mathsf T}-d\beta\beta^{\mathsf T}).
\]

The constructive target is therefore clear: choose an exact vector orthogonal to `alpha` but not to `beta`.

## Canonical rational construction

For distinct positive rational nodes, use the ordinary barycentric weights

\[
 w_i=1/\prod_{j\ne i}(x_i-x_j).
\]

Put

\[
 S_0=\sum_iw_i\alpha_i,
 \qquad
 S_1=\sum_iw_ix_i\alpha_i,
 \qquad
 D=\prod_i(x_i^2-d),
\]

and define

\[
 c_i=Dw_i(S_1-S_0x_i).
\]

The exact identities are

\[
 \sum_i c_ix_i^k=0
 \quad(0\le k\le n-3),
\]

\[
 \sum_i c_i\alpha_i=0,
 \qquad
 \sum_i c_i\beta_i=-1.
\]

Consequently the modeled pair contributes exactly

\[
 c^{\mathsf T}K^{(d)}c=-2md.
\]

This is `L-3904`. The ID was moved from the initially drafted `L-3903` after the stacked Arb branch independently reserved `L-3903` for its exact ball-contraction theorem.

The beta identity is not numerical. It follows from

\[
 \sum_i\frac{w_i}{z-x_i}=\frac1{\prod_i(z-x_i)}
\]

applied at the two formal square roots of `d`. The resulting expression returns to the rational field and simplifies to `-1` after the `D` scaling.

## Model-mismatch certificate

For an actual squared displacement `q`, define exact rational polynomials

\[
 U(q)=\sum_i c_ix_i\prod_{j\ne i}(x_j^2-q),
\]

\[
 V(q)=\sum_i c_i\prod_{j\ne i}(x_j^2-q),
 \qquad
 D_q=\prod_i(x_i^2-q).
\]

The pair contribution is

\[
 2m\frac{U(q)^2-qV(q)^2}{D_q^2}.
\]

At the model point, `U(d)=0`, `V(d)=-D_d`, so the numerator is strictly negative. A model cell can therefore be checked by exact rational root isolation or directed polynomial intervals before any expensive xi evaluation.

This is a search aid only. It controls the isolated pair component, not the complete Riemann-xi background.

## Distant-zero suppression

The moment cancellations imply

\[
 \left|\sum_i\frac{c_i}{x_i+iy}\right|
 =O(|y|^{-n+1}).
\]

An explicit bound is included in `L-3904`. The corresponding critical-line Pick contribution decays as `O(|y|^{-2n+2})`.

Compared with the model-free L-3901 product localizer, one interpolation degree is spent annihilating the target pair's positive rank-one direction. The remaining degrees suppress remote critical-line background.

## Exact frozen control

The committed control uses

```text
nodes = 1/10, 1/4, 2/3, 5/4
model d = 7/100
```

and reconstructs

```text
c = (
  432/1955,
  -1347/50000,
  -579303/1487500,
  314619/1610000
)
```

with

```text
sum c_i                 = 0
sum c_i x_i             = 0
alpha overlap           = 0
beta overlap            = -1
pair value, m=3         = -21/50
```

The complete same-height real-F contraction coefficients are frozen in

`experiments/X-3901-xi-passivity-adversarial/results/matched-pole-control.json`.

A finite critical-line zero model gives a strictly positive exact quadratic form. Rational mismatch points on both sides of `d` retain a negative isolated-pair contribution.

## Verification performed

The new standard-library test module executed locally:

```bash
python -m unittest -v tests/test_matched_pole.py
```

Six tests pass:

1. canonical moment, alpha, beta, and pair identities for node counts 2 through 6;
2. direct rational-function versus polynomial mismatch reconstruction;
3. an explicit open negative mismatch neighborhood;
4. nonnegative finite critical-line Gram controls;
5. frozen vector and contracted coefficient reproduction;
6. duplicate, nonpositive, too-short, and pole-touching input rejection.

The wider branch test command should now include this module alongside the existing 13 PR #52 tests.

## Relationship to the full objective

Under RH every fixed-vector Pick quadratic form is nonnegative. Therefore a rigorous negative interval for the actual Riemann-xi contraction is a finite unconditional counterexample witness through the parent `L-3202` interface.

`L-3904` improves the nomination and certificate geometry:

- the vector is exact before special-function evaluation;
- the target model is converted into a fixed rational witness rather than an interval eigenvector;
- PR #56's `L-3903` checker needs only its already-supported `real-pick-rayleigh` channel;
- every coefficient and its error amplification are reviewable;
- mismatch cells can be certified algebraically.

## Candidate status

None.

No actual Riemann-xi matched-filter interval was evaluated in this continuation. No midpoint negative, directed negative, or `Z-####` object is claimed.

## Proof boundary

- `L-3904`: `PROPOSED`.
- Vector construction and synthetic controls: exact rational arithmetic.
- The modeled pair is not asserted to exist for Riemann xi.
- A negative isolated-pair contribution does not imply a negative complete value.
- The active Arb producer and an independent producer must both enclose any final Riemann-xi witness.
- Parent `D-3201/L-3202` normalization and zero-resolvent dependencies retain their current statuses.

## Immediate handoff to PR #56

The current PR #56 checker already supports an arbitrary rational same-height `real-pick-rayleigh` vector through its own `L-3903` exact-contraction theorem. No checker schema extension is required.

Add one producer-side mode:

1. accept exact rational nodes and model `d`;
2. reconstruct the L-3904 vector rather than accepting supplied coefficients;
3. verify moments, alpha overlap, and beta overlap exactly;
4. emit the exact contracted coefficients and their `L1` amplification;
5. evaluate all F values in one Arb batch;
6. use the existing exact checker for the final interval;
7. search only model cells whose isolated-pair mismatch polynomial stays negative;
8. independently reproduce any complete negative interval.

## Next offensive experiment

Use the two-channel ratio from L-3902 only as a nomination mechanism. For each stable model cell:

- compare the two-point A/B channels;
- construct three-, four-, and five-point L-3904 vectors;
- rank by predicted target-pair separation divided by exact pointwise-error amplification;
- freeze the winning vector before raising precision;
- require a strict negative complete interval, not merely a negative model score.

This supplies a direct path from a hypothesized pole geometry to a compact proof object while preserving the repository's counterexample boundary.
