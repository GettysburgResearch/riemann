# Agent report — support-gap Hausdorff residual cone

Agent: `gpt56-08`  
Issue: #93  
Branch: `agent/gpt56-08/93-support-gap-hausdorff`  
Date: 2026-07-26  
Classification: proposed theorem, exact checker, exact synthetic separation; no Riemann counterexample claimed

## Starting obstruction

The PR #71 direct-`xi` geometry becomes extraordinarily close to singular after
nearby critical-line zeros are removed, but increasingly precise ordinary
arithmetic has kept the retained minors positive.  Raw near-null determinants
also contain severe, exactly predictable Vandermonde conditioning.

PR #108 supplies a different asset: a complete multiplicity-aware slab count
and saturated Hardy-`Z` sign chain can isolate all 172 zeros in the containing
slab, not merely the nearest selected subset.

The question for this continuation was:

> What finite RH consequence becomes available only after **every** slab zero
> has been removed?

## Breakthrough

Under RH, complete slab removal leaves a residual zero measure with a known
support gap.

For exact `a<T<b`, after removing all zeros with ordinates in `(a,b)`, every
remaining line zero has

```text
squared distance y >= A = min((T-a)^2,(b-T)^2).
```

This is strictly stronger information than positivity of the residual
Stieltjes measure.

### Value-only separator

For `u0<u1<u2`, define

```text
L1 = log((u1+A)/(u0+A))
L2 = log((u2+A)/(u0+A)).
```

The residual logarithmic modulus must satisfy

```text
L1*(R(u2)-R(u0)) - L2*(R(u1)-R(u0)) >= 0.
```

For one spectral factor at squared distance `y`, the summand has:

```text
y < A   -> negative
y = A   -> zero
y > A   -> positive.
```

Thus this is a signed spectral separator whose sign-change boundary is exactly
the certified support edge.

### Hausdorff moment cone

At a base point `u0`, normalize the residual logarithmic derivatives by

```text
M_n = (-1)^(n+1) R^(n)(u0)/(n-1)!
B_n = (u0+A)^n M_n.
```

Then `B_{r+1}` is a Hausdorff moment sequence on `[0,1]`.  This gives:

- every finite alternating difference of `B_n` is nonnegative;
- every Hankel moment matrix is PSD;
- every `(1-q)` localizing matrix is PSD;
- the first support ratio row is

  ```text
  (-1)^(n+1) [ n R^(n)(u0) + (u0+A) R^(n+1)(u0) ] >= 0.
  ```

## Strict advantage over existing cones

The exact model

```text
A=1
R(u)=log(u+1/2)
```

is an ordinary positive Stieltjes factor.  Its derivative is completely
monotone and its ordinary Hankel moment matrix is rank-one PSD.  Yet its mass
lies inside the declared support gap.

The new checker obtains

```text
chord row          log(2) log(5) - log(3)^2 < 0
first difference  B1-B2 = -2
ordinary Hankel   0
support localizer -2
```

So the support-aware cone strictly separates objects that every ordinary
Stieltjes/Loewner condition accepts.

## Exact implementation

Added `X-9305`:

```text
verify_support_gap.py
certificates/synthetic-inside-gap-factor.json
results/synthetic-summary.json
tests/test_verify_support_gap.py
README.md
```

The checker uses integers and `fractions.Fraction` only after JSON parsing.  It
contains a self-contained rational logarithm enclosure and supports:

1. three-value chord rows;
2. arbitrary Hausdorff finite differences;
3. exact rational Hankel Rayleigh rows;
4. exact rational `(1-q)` localizing Rayleigh rows.

Six adversarial tests pass locally.

## Partial PR71 reconnaissance

Using the existing four direct log-modulus values and only the nearest sixteen
empirical line-zero offsets, the new chord rows are negative, with representative
ordinary high-precision values

```text
(u0,u1,u2) = (2^-40,2^-36,2^-32):  about -3.80e-34
(u0,u1,u2) = (2^-36,2^-32,2^-28):  about -1.56e-30
```

This is not a counterexample and is not even an RH nomination: another 156 slab
zeros remain unremoved, so the certified support-gap hypothesis is false at
that intermediate rung.  The observation is useful because it shows that the
new functional is strongly sensitive to exactly the missing inside-gap mass it
was designed to detect.

The decisive production experiment is the same computation after all 172
PR #108 bins have been removed with directed factor intervals.

## Proof boundary

A strict production negative would still require:

1. the exact multiplicity-aware total count;
2. complete critical-line isolation of every slab zero;
3. directed residual factor subtraction or a directed logarithmic jet;
4. exact support lower bound `A`;
5. completed-`xi` normalization review;
6. an independent special-function and zero-count reproduction.

No `Z-####` candidate is allocated in this branch.

## Immediate continuation

1. Complete the PR #108 172-bin production artifact.
2. Adapt its selected-factor residual table into X-9305.
3. Evaluate every three-point row on the nine existing horizontal nodes.
4. If they remain positive, add an Arb logarithmic jet at the smallest-moat base
   point and search the first Hausdorff localizing matrices.
5. Move the same support-aware test to new count-screened large-gap ordinates;
   do not continue over-optimizing the now-closed PR #71 midpoint geometry.