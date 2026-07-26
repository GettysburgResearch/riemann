# L-9314 — Christoffel–Padé gap identities and certified residual-mass budgets

Claim ID: **L-9314**  
Status: **PROPOSED**  
Agent: `gpt56-01-r`  
Date: 2026-07-26  
Parent: L-9312

## Purpose

L-9312 reduces one added horizontal node to a scalar Padé interval

```text
theta_-(w) ≤ s(w) ≤ theta_+^(A)(w).
```

This lemma identifies the two distances to that interval boundary as exact
Christoffel-type positive integrals. It has four consequences useful for the
counterexample search:

1. every certified positive piece of the residual RH measure receives an exact
   leverage score against each Padé boundary;
2. exact factor removal can only drive both Padé gaps downward;
3. a finite lower bound from already-certified residual mass that exceeds the
   directed total gap is itself an RH contradiction;
4. leverage uncertainty gives a witness-specific priority for zero-bin
   refinement.

The finite identities are exact algebra. Their RH interpretation imports the
direct-ξ positive residual measure and the declared zero/count/factor gates.

---

## 1. Setup

Use the notation of L-9312. Thus

```text
D_U(y) = product_j (y+u_j),
ν is a positive measure supported on [A,infinity),
```

and

```text
s(w) = integral from A to infinity of
       1 / ((y+w)D_U(y)) dν(y).
```

The two true moment matrices are

```text
H0(s)[i,j]
=
integral y^(i+j) / ((y+w)D_U(y)) dν(y),
```

```text
HA(s)[i,j]
=
integral (y-A)y^(i+j) / ((y+w)D_U(y)) dν(y),
```

for `0≤i,j≤n`.

Write

```text
z = (1,-w,w^2,...,(-w)^n)^T.
```

For a coefficient vector q, write

```text
q(y) = q_0 + q_1 y + ... + q_n y^n.
```

Then `q^T z = q(-w)`.

Assume both Padé endpoints are finite. The identities remain valid with infima
and limiting vectors in singular boundary cases; finite certificates use
rational vectors checked directly.

---

## 2. Exact lower-gap identity

Define

```text
g_-(w) = s(w)-theta_-(w).
```

### Theorem 2.1

```text
g_-(w)
=
minimum over deg(q)≤n and q(-w)=1 of
integral q(y)^2 / ((y+w)D_U(y)) dν(y).
```

If q_- is any minimizing polynomial, then

```text
g_-(w) = integral K_-(y) dν(y),
K_-(y) = q_-(y)^2 / ((y+w)D_U(y)).
```

Equivalently, if q_- spans the lower boundary kernel and is normalized by
`q_-(-w)=1`, then

```text
H0(theta_-) q_- = 0,
q_-^T H0(s) q_- = s-theta_-.
```

#### Proof

L-9312 gives

```text
H0(t)=C0+t z z^T.
```

For `q(-w)=q^T z=1`,

```text
q^T H0(s) q = s + q^T C0 q.
```

The lower endpoint is

```text
theta_- = supremum over q(-w)=1 of -q^T C0 q.
```

Taking the minimum proves the scalar identity, and the integral representation
of the quadratic form gives the kernel identity. ∎

The kernel K_- is the finite Christoffel-function extremizer for the weighted
measure `dν/((y+w)D_U(y))`.

---

## 3. Exact support-upper-gap identity

Define

```text
g_+^(A)(w) = theta_+^(A)(w)-s(w).
```

### Theorem 3.1

```text
g_+^(A)(w)
=
1/(w+A) times the minimum over deg(q)≤n and q(-w)=1 of
integral (y-A)q(y)^2 / ((y+w)D_U(y)) dν(y).
```

For a minimizing polynomial q_+,

```text
g_+^(A)(w) = integral K_+^(A)(y) dν(y),
```

where

```text
K_+^(A)(y)
=
(y-A)q_+(y)^2 / ((w+A)(y+w)D_U(y)).
```

#### Proof

L-9312 gives

```text
HA(t)=CA-(w+A)t z z^T.
```

For `q(-w)=1`,

```text
q^T HA(s) q = q^T CA q-(w+A)s.
```

The upper endpoint is the infimum of `q^T CA q/(w+A)` over the same normalized
affine set. Taking the minimum proves the claim. ∎

For A=0 this is the ordinary half-line `y q(y)^2` boundary gap.

---

## 4. Monotonicity under certified factor removal

Let ν_1 and ν_2 be finite positive measures on `[A,infinity)` with
`ν_1≥ν_2`. Let g_-(ν) and g_+^(A)(ν) denote the two Padé gaps computed from ν.

### Corollary 4.1

```text
g_-(ν_1) ≥ g_-(ν_2),
g_+^(A)(ν_1) ≥ g_+^(A)(ν_2).
```

Thus exact removal of any certified positive residual measure can only move the
scalar toward the Padé boundary.

#### Proof

Both gaps are minima, over the same affine set `q(-w)=1`, of integrals of
nonnegative kernels. Increasing the measure increases every feasible objective.
∎

This is a global monotonicity theorem; it does not depend on infinitesimal
perturbation theory or a frozen endpoint vector.

---

## 5. Generic certified-submeasure budget

The most general finite form does not require atomic zeros.

Suppose a proof artifact certifies a positive measure μ_cert satisfying

```text
0 ≤ μ_cert ≤ ν.
```

Then the two exact gap identities imply

```text
g_-(w) ≥ integral K_-(y) dμ_cert(y),
```

```text
g_+^(A)(w) ≥ integral K_+^(A)(y) dμ_cert(y).
```

### Corollary 5.1 — generic finite contradiction

Let G_- and G_+ be directed intervals containing the total gaps, and let B_-
and B_+ be rigorous lower bounds for the two certified-submeasure integrals.
If

```text
upper(G_-) < B_-
```

or

```text
upper(G_+) < B_+,
```

then the positive-measure representation is impossible.

This formulation is the correct anti-double-counting abstraction: every budget
item must be part of one globally certified submeasure of the residual table
being tested.

---

## 6. Atomic line-zero bins

Suppose pairwise-disjoint squared-distance bins

```text
Y_r=[L_r,U_r] subset [A,infinity)
```

are each certified to contain at least m_r actual critical-line zeros that have
**not already been removed from the residual table**.

For a frozen rational endpoint polynomial, define

```text
kappa_r^- ≤ inf_{y in Y_r} K_-(y),
kappa_r^+ ≤ inf_{y in Y_r} K_+^(A)(y).
```

The atomic submeasure is

```text
μ_cert = sum_r m_r delta_{y_r},
```

with unknown `y_r in Y_r`, so

```text
g_-(w) ≥ sum_r m_r kappa_r^-,
g_+^(A)(w) ≥ sum_r m_r kappa_r^+.
```

A strict directed reversal is a finite RH counterexample predicate, subject to
the direct-ξ, endpoint-vector, and zero-bin gates.

### Anti-double-counting gate

The bins must be pairwise disjoint or carry an independently verified integer
allocation proving that no zero multiplicity is counted twice. Merely summing
overlapping lower-count windows is invalid.

A zero factor already subtracted from the table cannot be counted again as an
atom of the residual measure.

---

## 7. Far-endpoint deflation leaves a certified segment measure

This section makes the theorem directly compatible with PR #103/PR #105-style
safe far-endpoint factor subtraction.

Suppose an actual critical-line zero has squared distance y and a proof gives

```text
L ≤ y ≤ U ≤ B.
```

Subtracting the safe factor `log(u+B)` from the actual factor `log(u+y)` leaves

```text
log(u+y)-log(u+B)
=
- integral from y to B of 1/(u+s) ds.
```

With the sign convention used in the positive residual response, the remaining
positive measure is Lebesgue measure on `[y,B]`. Since `y≤U`, every admissible
zero leaves the common certified submeasure

```text
Lebesgue measure restricted to [U,B].
```

Therefore, for multiplicity m,

```text
g_- ≥ m times integral from U to B of K_-(s) ds,
```

```text
g_+^(A) ≥ m times integral from U to B of K_+^(A)(s) ds.
```

A simple rational lower bound is

```text
m (B-U) inf_{s in [U,B]} K(s).
```

This is generally weaker than exact integration but is elementary and
proof-grade. It does not double count the removed endpoint factor: it accounts
only for the positive segment measure that remains after subtraction.

For multiple factors, segment contributions may be summed when their
multiplicity allocation is certified; overlapping segments are allowed because
positive measures add by multiplicity. The zero identities themselves must
still be nonduplicated.

---

## 8. Exact interval evaluation

For a rational interval Y, both leverage kernels are rational functions with a
strictly positive denominator on the declared support.

A fail-closed checker may obtain a leverage interval by:

1. interval Horner evaluation of q(Y);
2. exact squaring, using lower endpoint zero if q(Y) crosses zero;
3. exact interval products for `Y+w` and every `Y+u_j`;
4. for the upper kernel, multiplication by `Y-A` and division by `w+A`;
5. division by the strictly positive denominator interval.

For an atomic bin, multiply the leverage lower bound by the certified
multiplicity. For a certified segment, also multiply by its exact length.

This elementary hull can be sharpened by isolating roots of q and stationary
points of the rational kernel. Sharpening affects power, not validity.

---

## 9. Refinement and scheduling scores

For an exact atom y, define

```text
lambda_-(y)=K_-(y),
lambda_+(y)=K_+^(A)(y).
```

For a certified bin, preserve both the infimum and supremum leverage bounds.
The multiplicity-weighted leverage width is the exact first target for refining
that bin for the active Padé witness.

For a certified segment, preserve

```text
length times leverage interval.
```

This gives a witness-specific scheduling rule for the saturated sign-chain bins
of PR #108 and the selected-factor data of PR #107:

```text
refine the bins or segment endpoints with the largest contribution uncertainty,
not necessarily the nearest bins or the widest ordinate bins.
```

---

## 10. Relationship to the normalized Padé coordinate

With finite endpoints,

```text
eta_A(w) = g_-(w) / (g_-(w)+g_+^(A)(w)).
```

The numerator and denominator are positive Christoffel-type residual energies.
A small absolute gap caused only by collapse of both energies is not an
invariant near-counterexample. A small normalized gap means one residual energy
is small relative to the full finite moment uncertainty.

The leverage decomposition supplies the spectral explanation for the candidate
correction in O-9312.

---

## 11. Proof boundary

The gap identities, variational formulas, measure monotonicity, atomic budgets,
and safe segment budgets are exact.

A Riemann-ξ contradiction requires:

1. directed old moments and new scalar value;
2. a rational endpoint polynomial normalized by `q(-w)=1`;
3. exact contraction of the total gap interval;
4. a globally compatible certified residual submeasure;
5. exact interval lower bounds for every leverage contribution;
6. a strict negative budget;
7. independent normalization, zero-isolation, and special-function review.

No Riemann-ξ negative is asserted by this lemma.
