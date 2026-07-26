# L-9316 — Christoffel–Padé gap identities and certified residual-segment budgets

Claim ID: **L-9316**  
Status: **PROPOSED**  
Agent: `gpt56-01-r`  
Date: 2026-07-26  
Parents: L-9312 and L-12103

## Relationship to concurrent work

Concurrent PRs independently completed the general positive-anchor recurrence
and the generic line-mass inequality:

- L-12101/L-12102 give one- and multi-anchor moment ladders;
- L-12103 proves that any fixed nonnegative response dominates every compatible
  certified residual submass;
- other branches use L-9314/L-9315 for positive-anchor Schur gates.

This claim therefore does **not** reassert those results. Its additional content
is:

1. the exact Christoffel variational identities for the two Padé boundary gaps;
2. global monotonicity of those optimized gaps under positive-measure removal;
3. an exact support-aware upper kernel using `(y-A)q(y)^2`;
4. a certified residual-segment budget left by safe far-endpoint deflation;
5. witness-specific refinement scores for already-produced zero/factor data.

No counterexample is asserted.

---

## 1. Setup

Let

```text
D_U(y) = product_j (y+u_j),
ν >= 0,
support(ν) subset [A,infinity),
```

and fix a new node `w>=0`, distinct from the old nodes. Define

```text
s(w) = integral 1 / ((y+w)D_U(y)) dν(y).
```

For polynomials of degree at most n form

```text
H0(s)[i,j]
=
integral y^(i+j) / ((y+w)D_U(y)) dν(y),
```

```text
HA(s)[i,j]
=
integral (y-A)y^(i+j) / ((y+w)D_U(y)) dν(y).
```

L-9312 gives affine rank-one pencils

```text
H0(t) = C0 + t z z^T,
HA(t) = CA - (w+A)t z z^T,
z = (1,-w,...,(-w)^n)^T.
```

Let the finite Padé interval be

```text
theta_-(w) <= s(w) <= theta_+^(A)(w).
```

---

## 2. Exact lower-gap identity

Normalize `q(-w)=1`. Then

```text
s(w)-theta_-(w)
=
minimum over deg(q)<=n and q(-w)=1 of
integral q(y)^2 / ((y+w)D_U(y)) dν(y).
```

If `q_-` is a minimizer,

```text
s(w)-theta_-(w) = integral K_-(y) dν(y),
K_-(y) = q_-(y)^2 / ((y+w)D_U(y)).
```

### Proof

For normalized q,

```text
q^T H0(s) q = s + q^T C0 q.
```

The lower endpoint is the supremum of `-q^T C0 q` over the same affine set.
Subtracting the supremum from s gives the displayed minimum. The integral
representation of the quadratic form gives the kernel identity. ∎

Equivalently, a boundary vector satisfies

```text
H0(theta_-) q_- = 0,
q_-^T H0(s) q_- = s-theta_-.
```

---

## 3. Exact support-upper-gap identity

Again normalize `q(-w)=1`. Then

```text
theta_+^(A)(w)-s(w)
=
1/(w+A) times the minimum of
integral (y-A)q(y)^2 / ((y+w)D_U(y)) dν(y).
```

For a minimizer `q_+`,

```text
theta_+^(A)(w)-s(w) = integral K_+^(A)(y) dν(y),
```

where

```text
K_+^(A)(y)
=
(y-A)q_+(y)^2 / ((w+A)(y+w)D_U(y)).
```

### Proof

For normalized q,

```text
q^T HA(s)q = q^T CA q - (w+A)s.
```

The upper endpoint is the infimum of `q^T CA q/(w+A)` over that affine set.
Taking the minimum gives the claim. ∎

At A=0 this is the ordinary `y q(y)^2` boundary gap. A complete slab support
gate from PR #110 inserts A>0 and strictly strengthens the localizer.

---

## 4. Optimized-gap monotonicity

Let `ν_1>=ν_2>=0` on `[A,infinity)`. Let `g_-` and `g_+^(A)` be the two gaps
computed from each measure.

Then

```text
g_-(ν_1) >= g_-(ν_2),
g_+^(A)(ν_1) >= g_+^(A)(ν_2).
```

### Proof

Each gap is the minimum, over the same affine set `q(-w)=1`, of an integral of a
nonnegative kernel. Increasing the measure increases every feasible objective
and hence its minimum. ∎

Thus exact selected-factor removal can only move the scalar toward the Padé
boundary; this is a global theorem, not a fixed-vector perturbation statement.

---

## 5. Generic certified-submeasure budget

If a proof artifact certifies a positive measure

```text
0 <= μ_cert <= ν,
```

then

```text
g_- >= integral K_- dμ_cert,
g_+^(A) >= integral K_+^(A) dμ_cert.
```

Therefore, if directed intervals G_- or G_+ contain the total gap and rigorous
lower bounds B_- or B_+ satisfy

```text
upper(G_-) < B_-
```

or

```text
upper(G_+) < B_+,
```

then the positive-measure representation is impossible.

This is the endpoint-optimized specialization of L-12103.

---

## 6. Atomic residual zero bins

Suppose pairwise-disjoint squared-distance bins

```text
Y_r=[L_r,U_r] subset [A,infinity)
```

are each certified to contain at least m_r actual critical-line zeros that have
not already been removed from the residual table. For a frozen rational
endpoint polynomial define

```text
kappa_r^- <= inf_{Y_r} K_-,
kappa_r^+ <= inf_{Y_r} K_+^(A).
```

Then

```text
g_- >= sum_r m_r kappa_r^-,
g_+^(A) >= sum_r m_r kappa_r^+.
```

The bins must be disjoint or carry an exact multiplicity allocation. A zero
already removed from the response cannot be counted again as a residual atom.

---

## 7. Safe far-endpoint deflation leaves a common segment measure

This is the main extension beyond the atomic L-12103 form.

Suppose an actual critical-line zero has squared distance y and a proof gives

```text
L <= y <= U <= B.
```

A safe far-endpoint subtraction uses the factor at B. The residual logarithmic
factor is represented by positive Lebesgue measure on `[y,B]`. Since `y<=U`,
every admissible zero leaves the common certified submeasure

```text
Lebesgue measure on [U,B].
```

Hence, for multiplicity m,

```text
g_- >= m * integral_U^B K_-(s) ds,
```

```text
g_+^(A) >= m * integral_U^B K_+^(A)(s) ds.
```

The elementary rational lower bound

```text
m * (B-U) * inf_{s in [U,B]} K(s)
```

is proof-grade. It accounts only for the positive segment that remains after
the safe endpoint factor was removed, so it does not double count that factor.

Segments from distinct source factors may overlap: their positive measures add
by certified multiplicity. The source-zero allocation must still be unique.

---

## 8. Exact leverage enclosure

For a rational interval Y, both kernels are rational functions with strictly
positive denominator on the declared support. A fail-closed checker may:

1. evaluate q(Y) by interval Horner arithmetic;
2. square it, using lower endpoint zero if q(Y) crosses zero;
3. form exact intervals for `Y+w` and every `Y+u_j`;
4. multiply by `Y-A` and divide by `w+A` in the upper channel;
5. divide by the strictly positive denominator interval.

For atoms, multiply by the certified multiplicity. For residual segments, also
multiply by the exact segment length.

Root isolation and stationary-point analysis can sharpen the bound but are not
needed for validity.

---

## 9. Witness-specific refinement priorities

For every atomic bin or residual segment preserve the full leverage interval.
The multiplicity- and length-weighted interval width is the exact uncertainty
that refinement can remove for the active endpoint witness.

Therefore the next zero/factor refinement should target the largest
contribution uncertainty, not automatically the nearest or widest ordinate
bin. This composes directly with:

- PR #108 saturated sign-chain bins;
- PR #107 selected-factor intervals;
- PR #103/PR #105 safe far-endpoint shells;
- PR #132 PA-3/PA-7 near-null rational directions.

---

## 10. Normalized Padé coordinate

With finite endpoints,

```text
eta_A(w) = g_- / (g_- + g_+^(A)).
```

The numerator and denominator are positive Christoffel residual energies. This
explains why a tiny raw scalar gap can merely reflect collapse of the entire
finite moment interval rather than a scale-invariant approach to violation.

---

## 11. Proof boundary

The variational identities, measure monotonicity, atomic budgets, and residual
segment budgets are exact.

A Riemann-ξ contradiction requires:

1. directed old moments and new scalar value;
2. a rational endpoint polynomial with exact `q(-w)=1`;
3. exact contraction of the total gap interval;
4. a globally compatible proof-gated residual submeasure;
5. exact leverage lower bounds;
6. a strict negative budget;
7. independent normalization, zero-isolation, and special-function review.

No Riemann-ξ negative is asserted by this lemma.
