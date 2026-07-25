# Session report — Issue #84 certified zero deflation

Agent: `gpt56-06-e`  
Date: 2026-07-25  
Issue: #84  
Branch: `agent/gpt56-06-e/84-certified-zero-deflation`  
Status: proposed theorem package, exact checker, and two rigorous low-height controls; no RH counterexample

## Starting obstruction

The Issue #39 scalar and Pick searches repeatedly encountered positive or
near-null finite forms. Existing methods treated every critical-line zero as
part of an unavoidable positive background. This can mask a negative off-line
component.

The first observation is that rigorously certified line zeros are not
uncertainty. They are known positive summands in the RH resolvent representation
and may be subtracted through lower contribution bounds.

The second observation is stronger: line localization is optional. An
unconditional total count of nontrivial zeros in a horizontal critical-strip
slab becomes line-zero mass under the RH assumption itself.

## Main breakthrough

For `s=1/2+x+iT`, RH gives

\[
 \operatorname{Re}\frac{\xi'}{\xi}(s)
 =\sum_\gamma\frac{x}{x^2+(T-\gamma)^2}.
\]

A disjoint interval containing at least `m` critical-line zeros contributes at
least

\[
 m\frac{x}{x^2+D^2},
\]

where `D` is the farthest endpoint distance from `T`. Subtracting this lower
bound leaves an RH-nonnegative residual.

The Pick version uses

\[
 v^*Kv=\sum_\gamma|\Phi_v(\gamma)|^2
\]

and subtracts a lower bound for `|Phi_v|^2` over each certified zero bin. A
Loewner-lower rank-one block with an explicit `epsilon I` repair gives a reusable
whole-matrix deflation.

## RH-forced slab counts

L-8405 removes the need to certify that counted zeros lie on the line. Suppose an
argument-principle, Turing, or `N(b)-N(a)` certificate proves that at least `m`
nontrivial zeros have ordinates in `[a,b]`. Under the RH assumption, every one of
those counted zeros must lie on `Re(s)=1/2`, so the same scalar, vector, and
matrix subtractions apply.

The count certificate is unconditional. Only the conversion

```text
counted nontrivial zero + RH assumption -> line zero
```

is conditional, which is exactly the correct direction for a contradiction.

## Strictness relative to ordinary passivity

The exact synthetic control has ordinary scalar value

\[
 \operatorname{Re}F=20/3>0
\]

but a certified deflated value

\[
 20/3-10=-10/3<0.
\]

The one-point Pick form is likewise positive `400/3`, while the deflated form is
`-800/3`.

Thus the new family is not merely a reformulation. It can expose a negative
component at a point where the old finite witness is strictly positive.

## Claims

- L-8401: scalar zero-count deflation.
- L-8402: fixed-vector Pick zero-count deflation.
- L-8403: Loewner-lower zero-bin matrix blocks.
- L-8404: directed Hardy-Z sign changes give one-zero lower-count bins.
- L-8405: total critical-strip slab counts suffice under the RH assumption.
- M-8401: proof-producing search architecture.
- X-8401: exact rational checker and controls.

All theorem claims are `PROPOSED` pending independent reconstruction.

## Exact checker

The checker uses only integers and `fractions.Fraction`. It reconstructs:

- scalar Poisson lower contributions;
- arbitrary-height complex Pick contraction coefficients;
- rational complex interval images of `Phi_v` over complete zero bins;
- modulus-square lower bounds;
- exact residual intervals and strict moats;
- disjointness and logical-gate manifests.

Nine adversarial tests pass. Mutations reject overlapping bins, nonpositive
counts, blocking gates, false claimed intervals, changed vectors, and Boolean
counts.

## Actual Riemann-xi calibration 1 — isolated first zero

The branch runs the complete finite pipeline on actual low-height Riemann data:

1. `python-flint 0.9.0` / Arb at 192 bits computes `acb.zeta_zero(1)`, giving a
   directed critical-line zero interval of width about `1.02e-56`.
2. The exact sample ordinate is the dyadic midpoint of that interval and
   `x=1/20`.
3. `F=xi'/xi` is evaluated independently as the differentiated completed product
   divided by `xi` and as the corrected completion plus `zeta'/zeta`.
4. A separate standard-library replay intersects the two real intervals,
   verifies positive zeta and xi denominator lower bounds, subtracts the exact
   Poisson lower contribution, and reconstructs the residual.

The primitive value is approximately

```text
Re F(s) = 20.0033840667360504217...
```

The certified first-zero contribution is just below `20`, leaving the rigorous
positive residual

```text
0.0033840667360504217... < residual
                               < 0.0033840667360504218....
```

This validates the producer → certified zero → exact deflation → independent
algebraic replay pipeline.

## Actual Riemann-xi calibration 2 — total slab count only

The branch also avoids line localization entirely:

```text
a = 14.13 = 1413/100
b = 14.14 = 707/50
T = 14.135 = 2827/200
x = 1/20
```

At 192 Arb bits,

```text
N(a)=0,
N(b)=1,
N(b)-N(a)=1,
```

with exact integer count balls and positive directed lower bounds for
`|zeta(1/2+ia)|` and `|zeta(1/2+ib)|`. The certified slab contribution is

```text
2000/101.
```

Two independent `xi'/xi` assemblies and a separate standard-library replay give
the rigorous positive residual

```text
0.2007996313314755... < residual
                         < 0.2007996313314756....
```

This is an end-to-end control of L-8405: an unconditional total zero count feeds
RH-conditional deflation without locating the counted zero on the line.

Both calibrations are rigorous numerical controls pending parent analytic review;
neither is evidence for RH outside its finite object.

## What is not claimed

- No negative actual Riemann-xi residual was produced.
- The low-height numerical controls do not promote D-3201/L-3201/L-3202.
- No independent special-function backend reproduced the controls yet.
- No `Z-####` candidate is allocated.

## Immediate production target

Use the existing Riemann-Siegel Arb backend to certify local exact count
differences `N(T+h)-N(T-h)` around new high-height passivity windows. Feed those
counts and one shared exact point cloud into scalar deflation first, then
cross-height Pick and matrix deflation.

Hardy-Z sign-change bins should be used only when narrower localization materially
improves the lower contribution. PR #67 already proves that optimization over its
unchanged same-height value table is closed by exact feasible anchors; zero-count
features genuinely enlarge that cone.

## Review targets

1. Reconstruct the lower Poisson subtraction in L-8401.
2. Recheck every conjugation in L-8402.
3. Audit the complex reciprocal interval enclosure in X-8401.
4. Reconstruct the operator perturbation constant in L-8403.
5. Verify the RH-forced count conversion in L-8405.
6. Reproduce both actual controls with an independent special-function backend.
7. Attack double-counting, endpoint-zero, and `N(T)` convention edge cases.
8. Keep zero-count soundness separate from `xi'/xi` primitive soundness.
