# Zeta23 continuation II: finite off-line isolation and conditioning dichotomy

Date: 2026-08-10

## 1. Goal

PR #363 computed the exact negative eigenvalue of one off-line reflected pair in the complete critical Gabor frame. The next missing step was isolation: can that negative pair direction be annihilated against all other zeros in a finite localization window without assuming zero separation?

The answer at finite scope is yes, exactly.

## 2. Exact finite interpolation

For any finite set of distinct centered zero coordinates `Z={z_1,...,z_n}`, the complete critical-frame evaluation Gram is

```text
K_ij=L int v(u) exp(i(z_i-conj(z_j))u)du.
```

It is positive definite because it is the Gram of distinct exponential functions on an interval carrying positive window mass. Hence the evaluation map is onto.

For target values `t`, the minimum-norm coefficient vector is

```text
c_t=E_Z* K_Z^(-1)t,
```

with exact cost

```text
||c_t||^2=t* K_Z^(-1)t.
```

## 3. Exact pair isolation

For a reflected off-line pair of multiplicity `m`, choose target values

```text
1,-1,0,...,0.
```

Every nuisance zero in the finite window vanishes exactly, and the target pair contributes

```text
-2m.
```

Thus finite source binding is automatic. The only issue is the norm cost of the interpolant.

## 4. Tail and floor theorem

If the unseen-zero tail has operator norm at most `epsilon`, the full quadratic obeys

```text
W(c_t,c_t)<=-2m+epsilon C_Z(t),
C_Z(t)=t*K_Z^(-1)t.
```

So

```text
epsilon C_Z(t)<2m
```

certifies a genuine negative full-Weil direction.

If, conversely, an arithmetic theorem claims a lower floor

```text
G>=-delta I,
```

then any off-line pair forces

```text
2m<=(epsilon+delta)C_Z(t).
```

Since `C_Z(t)<=2/lambda_min(K_Z)`, one obtains the exact alternative

```text
lambda_min(K_Z)<=(epsilon+delta)/m.
```

Therefore a counterexample to RH can survive a hierarchy with vanishing tail and vanishing corrected-kernel floor only through collapse of the local zero-evaluation Gram.

## 5. Schur form

Partitioning target pair and nuisance zeros gives

```text
K_Z=[[A,B],[B*,D]],
S=A-BD^(-1)B*.
```

The capture cost is exactly

```text
(1,-1) S^(-1) (1,-1)^T.
```

This is the selected-zero Schur complement in the zero-evaluation metric. It is the finite matrix counterpart of the repository's complete-kernel capture condition.

## 6. What the numerical replay shows

For one rectangular-window control pair, the no-nuisance capture cost is `0.1943`. Successively adding four real nuisance coordinates raises it through

```text
0.2253,
0.4684,
18.1886,
2895.7083.
```

The interpolation remains exact, but the Gram becomes ill-conditioned. This is not evidence that zeta zeros realize such a packet; it demonstrates why existence of cardinal interpolation and a uniform metric bound are radically different statements.

## 7. Revised full-proof target

The finite isolation theorem removes one ambiguity from the kernel program. The remaining RH-bearing statement can be written as a single target:

> For every hypothetical off-line pair, construct a localization hierarchy for which the target-pair evaluation Schur complement stays quantitatively above the combined far-tail and corrected-floor radii.

Equivalent attack coordinates are:

```text
lower-bound the target Schur complement;
upper-bound the inverse-Gram capture cost;
exclude asymptotic Gram collapse;
cluster and recombine every bad nuisance packet.
```

Zeta23's first two moments do not control the smallest Gram eigenvalue. A successful continuation needs a local statistic, higher moment, or arithmetic separation mechanism.

## 8. Honest status

```text
finite distinct-coordinate interpolation      COMPLETE EXACT
finite off-line pair isolation                COMPLETE EXACT
minimum-norm and Schur formulas                COMPLETE EXACT
tail/floor versus Gram-conditioning dichotomy COMPLETE EXACT
uniform zeta-zero Gram lower bound             OPEN / RH-BEARING
Riemann Hypothesis                             UNPROVED
```
