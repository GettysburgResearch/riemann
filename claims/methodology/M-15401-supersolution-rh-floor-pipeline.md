# M-15401 — Proof-producing supersolution pipeline for the positive RH program

Claim ID: `M-15401`  
Title: Replace a growing omitted-mode audit by one continuum Barta residual and one odd polar scalar  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-07-31  
Dependencies: L-15401; T-15401; T-14302; existing directed prime and interval infrastructure  
Scope: discovery-to-certificate methodology for Suzuki's localized Weil ground floor

## Objective

Produce a rigorous lower bound for the complete localized Weil operator at one
support without claiming that a finite compression captures its ground state.
The certificate has two analytic components:

```text
pointwise Barta floor for the full Markov jump-potential base
+
one ambient upper bound for the negative odd polar resolvent scalar.
```

A cofinal sequence of such floors tending to zero proves RH through T-14302.

## Stage 1 — Freeze the exact source normalization

For every support `a`, retain:

- Suzuki equation and version identifier;
- the constant `A` in the source normalization;
- exact support scaling from `[-a,a]` to `[-1,1]`;
- the prime-power inclusion convention `n<=exp(2a)`;
- a hash-bound complete prime-power manifest;
- explicit definitions of `K_a`, `F_a`, `U_a`, and `V_a` from L-15401.

A source-normalization mismatch is a blocking logical failure and cannot be
repaired by a numerical moat.

## Stage 2 — Choose a positive supersolution

Discovery may use floating eigenvectors, splines, neural approximants, or
prolate functions.  Before certification, freeze one exact positive function
on `(-1,1)`, preferably a rational spline or rational polynomial times an
explicit positive endpoint weight.

The proof object must include a positivity moat on every open cell.  Merely
having positive sampled values is insufficient.

Recommended first families are:

1. piecewise-linear or cubic rational splines fitted to a midpoint Markov
   ground state;
2. `(1-x^2)^alpha p(x)` with rational `alpha` for which all endpoint limits are
   symbolically controlled;
3. positive even splines for the global base floor;
4. separate half-interval positive test functions if a sharper odd-sector
   resolvent comparison is implemented.

## Stage 3 — Build a closed interval partition

The partition must contain:

- every spline knot;
- `0` and both endpoints;
- every point at which a translated spline crosses a knot;
- all points `x=+-1+-delta_n` where a prime neighbor enters or leaves;
- any subdivision required to prove monotonicity of the cancellation-safe
  archimedean integrands.

On each cell, evaluate the complete pointwise residual

\[
 b_{a,\psi}(x)=V_a(x)+(L_a\psi)(x)/\psi(x)
\]

with outward interval arithmetic.  Do not widen the logarithmic and `r_1''`
terms independently; L-15401 proves that their cancellation-safe combination is
`K_a+U_a`.

## Stage 4 — Certify the ambient Barta floor

For each cell, prove a rational lower endpoint.  The minimum over all cells is
`m_a`.  The exact ground-state identity then proves

\[
 H_a\succeq m_a I
\]

on the complete ambient form domain.

This step is stronger than a positive finite Ritz matrix: it rules out every
unrepresented mode of the Markov base.

## Stage 5 — Resolve the sole dangerous polar channel

The positive even `cosh` channel can only help.  The negative odd `sinh` channel
requires an upper enclosure

\[
 B_a(\lambda)\ge
 \langle s_a,(H_{a,odd}-\lambda I)^{-1}s_a\rangle,
 \qquad \lambda<m_a.
\]

Use the cheapest gate that succeeds:

1. coarse Barta bound `||s_a||^2/(m_a-lambda)`;
2. a small exact low packet plus L-14308 complement coercivity;
3. a positive-resolvent supersolution, if positivity of the odd reduced
   resolvent is independently proved;
4. a rational Green or continued-fraction enclosure;
5. an interval finite-element solve with a rigorous dual residual and ambient
   complement bound.

Accept the floor only when

\[
 2aB_a(\lambda)\le1.
\]

Equality is retained as a boundary, not rounded to strictness.

## Stage 6 — Produce one finite support certificate

The support result must report separately:

```text
Barta floor m_a
target floor lambda_a
odd resolvent upper B_a
polar product 2a B_a
pointwise residual moat
source and manifest digests
all interval partitions and directed backends
```

The final verdict is one of:

```text
CERTIFIED_LOCALIZED_FLOOR
UNRESOLVED_POINTWISE_RESIDUAL
UNRESOLVED_POLAR_SCALAR
BLOCKED_NORMALIZATION
```

## Stage 7 — Prove a cofinal envelope

A finite table, however large, does not prove RH.  The terminal analytic object
must be a symbolic statement such as

\[
 \lambda_a\ge-\varepsilon(a),
 \qquad
 \varepsilon(a)\to0,
\]

on an unbounded support sequence or eventually for all supports.

Candidate routes to the cofinal statement:

- continuation estimates for rational supersolutions as `a` grows;
- an explicit asymptotic supersolution based on the archimedean Markov kernel;
- a radical-tail identity converted into a positive pointwise residual;
- exact renormalization of prime-shift residuals by blocks of `log n/a`;
- a hybrid argument in which Barta controls the ambient base and only a fixed
  number of arithmetic moments are treated spectrally.

Once `liminf lambda_a>=0` is established cofinally, T-14302 yields RH.

## Search diagnostics

Rank exploratory candidates by proof-relevant quantities:

1. the minimum normalized pointwise residual, not a sampled matrix eigenvalue;
2. interval sensitivity of `U_a` and translated spline values;
3. contribution of each prime power to the worst residual cell;
4. the polar product `2aB_a(lambda)`;
5. stability of the same supersolution family under support continuation.

A small finite eigenvalue can coexist with a poor pointwise residual, and vice
versa.

## Exact checker boundary

`X-15401` validates only the finite graph analogue:

- positive jump weights;
- exact Barta identity;
- a negative local potential repaired by a nonconstant positive supersolution;
- exact polar signature;
- a strict rank-one Birman–Schwinger gate;
- a final dense-matrix regression.

It does not evaluate `zeta`, `r''`, `U_a`, or a continuum integral.

## Failure modes

- evaluating `1/(2t)` and `K_a(t)` separately near `t=0`;
- ignoring the negative `sinh` channel;
- treating a lower finite resolvent compression as an upper ambient bound;
- checking the Barta residual only at mesh nodes;
- allowing `psi` to cross or touch zero without a weighted endpoint theorem;
- replacing a cofinal proof by curve fitting;
- importing positivity of a prolate or radical target without proving its sign;
- assuming that a positive finite Galerkin matrix gives an ambient floor.

## Immediate production experiment

At several small and moderate supports:

1. assemble the cancellation-safe Markov midpoint operator;
2. compute its positive numerical ground state;
3. freeze a rational positive spline;
4. interval-certify the pointwise Barta residual;
5. compare the crude and block-refined odd polar scalar;
6. record how `m_a`, the polar correction, and the certified floor scale with
   `a`.

The experiment is valuable even if it fails: it will show whether the true
cofinal blocker is the Markov residual, the odd polar scalar, or the arithmetic
support continuation.
