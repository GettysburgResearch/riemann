# Mellin normalization audit

## Verdict

`NOT_INTEGRATION_READY`.

Reviewer A correctly formalized several generic Mathlib Mellin identities, but the two conclusion-facing open propositions do **not** state the reviewed `L-99270/L-99272` transforms. Both are stronger than the reviewed theorems and false at their written generality.

## Convention table

| Object | Domain and measure | Kernel | Half-plane direction |
|---|---|---|---|
| Mathlib `mellin f s` | `(0,∞)`, `dx` | `x^(s-1) f(x)` | lower boundary is governed by behavior at `0`; upper boundary by `∞` |
| Reviewed `L-99272` | `[1,∞)`, `dx` | `f(x) x^(-s-1)` | convergence for `Re(s)` to the **right** of the tail abscissa |
| Reviewed negative mass | `[1,X]`, `dx/x` | `h_-(x)` | controls the tail transform on `[1,∞)` |
| Multiplicative box | `[1,A]`, `du/u` | `h(X/u)` | multiplier `K_A(s)=(1-A^(-s))/s` |

Reviewer A's `mellin_dilation` is correct for Mathlib's convention:

\[
\mathcal M[f(a\cdot)](s)=a^{-s}\mathcal M[f](s),\qquad a>0.
\]

The two-term linear-combination theorem, compact power kernel, and strip-holomorphy adapter also have the correct Mathlib hypotheses.

## Missing tail-Mellin adapter

The reviewed tail transform can be embedded into Mathlib's convention by defining

\[
g(t)=\mathbf 1_{(0,1]}(t)\,f(1/t).
\]

Then the change of variables \(x=1/t\) gives

\[
\operatorname{mellin}(g,s)
=\int_0^1 t^{s-1}f(1/t)\,dt
=\int_1^\infty f(x)x^{-s-1}\,dx.
\]

PR #734 contains neither this inversion/indicator theorem nor a direct `TailMellin` definition.

## `MellinLandauBoundarySingularity`

The delivered proposition asks for:

* local integrability on `(0,∞)`;
* nonnegativity only for `x≥1`;
* a finite **lower** abscissa for Mathlib's full Mellin transform;
* a singularity at that lower boundary.

This is not the reviewed theorem, where the density is nonnegative on the actual tail support `[1,∞)` and the transform is `x^(-s-1)`.

The written proposition is false. A model counterexample at `σc=0` is:

\[
f(x)=
\begin{cases}
\sin(1/x),&0<x<1,\\
e^{-x},&x\ge1.
\end{cases}
\]

The standard Mellin integral from the first piece becomes

\[
\int_1^\infty u^{-s-1}\sin u\,du.
\]

It is absolutely convergent exactly for `Re(s)>0`, but integration by parts extends it holomorphically through `s=0` (indeed to `Re(s)>-1`). The positive tail makes the function nonzero and nonnegative on `[1,∞)`. Thus the stated hypotheses can hold while the claimed nonremovable boundary singularity fails.

Verdict: `STATEMENT_TOO_STRONG`.

## `SubpowerNegativeMassHolomorphy`

The mass condition controls only

\[
\int_1^X h_-(t)\,\frac{dt}{t},
\]

but the conclusion concerns Mathlib's full Mellin transform on `(0,∞)`. No support condition controls the interval `(0,1)`.

A direct counterexample is

\[
f(x)=
\begin{cases}
-x^{-1},&0<x<1,\\
0,&x\ge1.
\end{cases}
\]

Its logarithmic negative mass on `[1,X]` is zero, and it is locally integrable on the open set `(0,∞)`. Yet the standard Mellin transform has the right-side expression `1/(s-1)` and is not analytic at `s=1`, contradicting the claimed `Re(s)>0` conclusion.

Verdict: `STATEMENT_TOO_STRONG`.

## Fixed defects and nonvanishing multipliers

The local theorems

* `fixed_holomorphic_defect_transfer`;
* `nonvanishing_multiplier_preserves_nonremovable`;
* `fixed_mellin_singularity_transfer`

are exact and useful. Their source-specific use must still require:

1. a detector fixed independently of the hypothetical zero and proof horizon;
2. a fixed multiplier;
3. analyticity of the defect at the candidate pole;
4. nonvanishing of the multiplier at that pole;
5. an exact identity in the initial convergence half-plane before continuation.

PR #734 does not formalize the actual logarithmic-box multiplier `K_A(s)=(1-A^(-s))/s` or its nonvanishing on `Re(s)>0`; it records this honestly as a blocker.

## Multiplicity/order

The reciprocal meromorphic-order identity is proved. The missing adapter is: at a nontrivial zero `ρ≠1`, identify the finite `analyticOrderAt riemannZeta ρ` used by Zeta23 with `meromorphicOrderAt riemannZeta ρ`, then transport its natural multiplicity to a reciprocal pole of the same order. Without that bridge, the API is an order theorem conditional on an already supplied meromorphic order, not a completed zeta-multiplicity theorem.

## Analytic continuation versus convergence

The generic Mellin API correctly retains convergence hypotheses. The defect arises only where the wrong full-axis transform is substituted for the reviewed tail transform. No analytic continuation should be used to assert integral convergence without the exact Landau theorem and its correctly stated nonnegative density.

## Required corrected boundary

The acceptable open proposition should quantify the exact tail transform, for example:

```text
TailMellin f s := ∫ x in Ici 1, (f x : ℂ) * (x : ℂ)^(-s-1)
```

and require:

* `f≥0` almost everywhere on `Ici 1`;
* `f` not a.e. zero there;
* local integrability on the tail;
* finite tail abscissa;
* agreement of `F` with `TailMellin` in the initial convergence half-plane.

The negative-mass proposition should use the same tail transform or a proved inversion/zero-extension adapter.
