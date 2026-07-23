# Session report — gpt56-05-d — Issue #47

Date: 2026-07-23  
Agent: `gpt56-05-d`  
Branch: `agent/gpt56-05-d/47-xi-derivative-free-witnesses`  
Stacked base: draft PR #43  
Status: proposed lemmas and exact synthetic regression; no counterexample

## Objective

Remove the higher-derivative requirement from the right-side xi witness and look for finite multi-point inequalities that can expose an off-line component using only values of `xi'/xi` at exact points.

## Starting observation

Under RH, with

\[
 F=\xi'/\xi,
 \qquad
 J_T(u)=\sqrt u\,\operatorname{Re}F(1/2+\sqrt u+iT),
\]

one has

\[
 J_T(u)=\sum_\gamma\frac{u}{u+(T-\gamma)^2}.
\]

L-4101 differentiated this representation. The key question was whether its support-localizing sign could be retained without taking a derivative.

## Main result 1: two values are enough

For `u!=v`,

\[
 \frac{J_T(u)-J_T(v)}{u-v}
 =\sum_\gamma
 \frac{(T-\gamma)^2}
 {(u+(T-\gamma)^2)(v+(T-\gamma)^2)}\ge0
\]

under RH. Hence one negative exact secant disproves RH.

For an off-line same-ordinate pair at horizontal displacement `delta`, the pair contributes

\[
 -\frac{2m\delta^2}
 {(u-\delta^2)(v-\delta^2)}
\]

to the right-side secant. It diverges negatively as both nodes approach the pole from the right, while both scalar real parts diverge positively. The analytic background has bounded local secants, so every RH failure creates an open family of value-only witnesses. This proves existential completeness.

The diagonal limit is exactly half of the L-4101 differential expression.

## Main result 2: all finite divided differences

For every order `n>=1`,

\[
 (-1)^{n-1}[u_0,\ldots,u_n]J_T
 =\sum_\gamma
 \frac{(T-\gamma)^2}
 {\prod_k(u_k+(T-\gamma)^2)}\ge0.
\]

Thus RH requires monotonicity, concavity, and all higher alternating finite signs. The formulas use only value balls with exact rational barycentric coefficients.

## Main result 3: total nonnegativity

For ordered disjoint node lists `U,V`, define

\[
 L_{ij}=\frac{J_T(u_i)-J_T(v_j)}{u_i-v_j}.
\]

Under RH,

\[
 L_{ij}=\sum_{a>0}\frac{c_a}{(u_i+a)(v_j+a)}.
\]

Cauchy--Binet expands every minor into products of two positive Cauchy determinants and positive atom weights. Finite truncations are therefore totally nonnegative; absolute entry convergence and determinant continuity give the complete result.

This yielded the strongest discovery insight of the session: a higher minor can be negative even if every sampled scalar secant is positive.

## Exact synthetic experiment

X-4701 uses the symmetry-closed finite multiset

\[
 \{1/2\pm1/10\pm i,\ 1/2\pm2i\}
\]

and exact Gaussian-rational arithmetic.

### Right-side scalar control

At `x=11/100` and `x=3/25`, both `Re F_Z` values are positive, while the exact secant is approximately

```text
-2162.924310296532
```

and is stored as a reduced rational.

### Curvature control

At offsets `3/10,1/2,3/5`, the second divided difference is approximately

```text
+2.3217012575865015
```

where RH requires a nonpositive value.

### Positive-entry negative-minor control

Rows `3/10,1/2` and columns `3/5,7/10` give a `2x2` cross-Loewner matrix with all four entries positive but determinant approximately

```text
-0.10666508108708517
```

The exact determinant is committed.

## Verification performed

```bash
python verify.py certificates/synthetic-offline-value-witnesses.json
python -m unittest discover -s tests -v
python -m compileall -q verify.py tests
```

Eight tests pass. They include exact endpoint reconstruction, numerator mutations, node-order rejection, cross-equality rejection, on-line divided-difference signs, on-line `2x2`/`3x3` minor positivity, and the positive-entry negative-minor phenomenon.

## Proof boundary

No Riemann xi value was evaluated. No interval arithmetic or high-height scan was run. The negative quantities belong only to the finite synthetic model. No `Z-####` candidate is allocated.

All lemmas remain `PROPOSED`, and D-3201's imported normalization remains a dependency requiring independent review.

## Highest-priority review targets

1. Check the denominator `x_2^2-x_1^2` and the factor `1/2` in the diagonal differential limit.
2. Reconstruct the local-pole converse and verify that positive scalar values coexist with a negative secant on the right.
3. Audit `(-1)^(n-1)` in L-4702.
4. Reconstruct the Cauchy determinant orientation and Cauchy--Binet expansion.
5. Verify grouping of repeated squared ordinate offsets.
6. Independently recompute the committed rational determinant.
7. Ensure no producer silently sorts nodes or inserts derivative diagonals.

## Suggested next work

Implement a value-only Arb batch in Issue #39. At each proposed height:

1. evaluate exact dyadic horizontal offsets once;
2. screen negative scalar `Re F` values;
3. screen right-side secants;
4. screen second divided differences;
5. screen frozen `2x2` cross-Loewner minors;
6. escalate only separated anomalies to independent ball reconstruction.

This should precede expensive generic high-order xi-jet work.
