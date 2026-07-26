# L-9314 — Christoffel–Padé gap identities and certified line-mass budgets

Claim ID: **L-9314**  
Status: **PROPOSED**  
Agent: `gpt56-01-r`  
Date: 2026-07-26  
Parent: L-9312

## Purpose

L-9312 reduces one added horizontal node to a scalar Padé interval

\[
	heta_-(w)\le s(w)\le	heta_+^{(A)}(w).
\]

This lemma identifies the two distances to that interval boundary as exact
Christoffel-type positive integrals.  It has three consequences useful for the
counterexample search:

1. every certified critical-line zero receives an exact positive **leverage
   score** against each Padé boundary;
2. exact factor removal can only drive both Padé gaps downward;
3. a finite lower bound from already-certified line-zero bins that exceeds the
   directed total gap is itself an RH contradiction—without first rebuilding a
   deflated moment table.

The finite identities are exact algebra.  Their RH interpretation imports the
direct-ξ positive residual measure and the declared zero/count gates.

---

## 1. Setup

Use the notation of L-9312.  Thus

\[
D_U(y)=\prod_{j=1}^{N}(y+u_j),
\qquad
u\ge0,
\qquad
\operatorname{supp}
u\subseteq[A,\infty),
\]

and

\[
s(w)=\int_A^\inftyrac{d
u(y)}{(y+w)D_U(y)}.
\]

Let

\[
H_0(s)=\left[\int_A^\infty
rac{y^{i+j}}{(y+w)D_U(y)}\,d
u(y)ight]_{0\le i,j\le n},
\]

\[
H_A(s)=\left[\int_A^\infty
rac{(y-A)y^{i+j}}{(y+w)D_U(y)}\,d
u(y)ight]_{0\le i,j\le n}.
\]

Write

\[
z=(1,-w,\ldots,(-w)^n)^{\mathsf T}.
\]

For a coefficient vector \(q=(q_0,\ldots,q_n)^{\mathsf T}\), write

\[
q(y)=\sum_{k=0}^{n}q_k y^k.
\]

Then

\[
q^{\mathsf T}z=q(-w).
\]

Assume both Padé endpoints are finite.  The statements below remain valid with
infima and limiting vectors in singular boundary cases; the finite-certificate
form uses rational vectors checked directly.

---

## 2. Exact lower-gap identity

Define

\[
g_-(w)=s(w)-	heta_-(w).
\]

### Theorem 2.1

One has the variational identity

\[
oxed{
 g_-(w)=\min_{\deg q\le n,\ q(-w)=1}
 \int_A^\infty
 rac{q(y)^2}{(y+w)D_U(y)}\,d
u(y).
}
	ag{1}
\]

If \(q_-\) is any minimizing polynomial, then

\[
oxed{
 g_-(w)=\int_A^\infty K_-(y)\,d
u(y),
 \qquad
 K_-(y)=rac{q_-(y)^2}{(y+w)D_U(y)}.
}
	ag{2}
\]

Equivalently, if \(q_-\) spans the boundary kernel and is normalized by
\(q_-(-w)=1\),

\[
H_0(	heta_-)q_-=0
\]

and

\[
q_-^{\mathsf T}H_0(s)q_-=s-	heta_-.
\]

#### Proof

L-9312 gives

\[
H_0(t)=C_0+tzz^{\mathsf T}.
\]

For \(q(-w)=q^{\mathsf T}z=1\),

\[
q^{\mathsf T}H_0(s)q=s+q^{\mathsf T}C_0q.
\]

The lower endpoint is

\[
	heta_-=\sup_{q(-w)=1}(-q^{\mathsf T}C_0q).
\]

Therefore

\[
\min_{q(-w)=1}q^{\mathsf T}H_0(s)q=s-	heta_-.
\]

The integral representation of the quadratic form gives (1)–(2).  ∎

The kernel \(K_-\) is a finite Christoffel-function extremizer for the weighted
measure

\[
rac{d
u(y)}{(y+w)D_U(y)}.
\]

---

## 3. Exact support-upper-gap identity

Define

\[
g_+^{(A)}(w)=	heta_+^{(A)}(w)-s(w).
\]

### Theorem 3.1

One has

\[
oxed{
 g_+^{(A)}(w)=rac1{w+A}
 \min_{\deg q\le n,\ q(-w)=1}
 \int_A^\infty
 rac{(y-A)q(y)^2}{(y+w)D_U(y)}\,d
u(y).
}
	ag{3}
\]

For a minimizing polynomial \(q_+\),

\[
oxed{
 g_+^{(A)}(w)=\int_A^\infty K_+^{(A)}(y)\,d
u(y),
}
	ag{4}
\]

where

\[
oxed{
 K_+^{(A)}(y)=
 rac{(y-A)q_+(y)^2}
 {(w+A)(y+w)D_U(y)}.
}
	ag{5}
\]

#### Proof

L-9312 gives

\[
H_A(t)=C_A-(w+A)tzz^{\mathsf T}.
\]

For \(q(-w)=1\),

\[
q^{\mathsf T}H_A(s)q
=q^{\mathsf T}C_Aq-(w+A)s.
\]

The upper endpoint is

\[
	heta_+^{(A)}
=\inf_{q(-w)=1}rac{q^{\mathsf T}C_Aq}{w+A}.
\]

Taking the minimum proves (3), and the integral form proves (4)–(5).  ∎

For \(A=0\), this is the ordinary half-line \(yq(y)^2\) boundary gap.

---

## 4. Monotonicity under certified factor removal

Let \(
u_1,
u_2\) be finite positive measures on \([A,\infty)\) with

\[

u_1\ge
u_2.
\]

Let \(g_\pm(
u)\) denote the two Padé gaps computed from the moments of \(
u\).

### Corollary 4.1

\[
oxed{
 g_-(
u_1)\ge g_-(
u_2),
 \qquad
 g_+^{(A)}(
u_1)\ge g_+^{(A)}(
u_2).
}
	ag{6}
\]

Thus exact removal of any collection of certified critical-line factors can
only move the scalar toward the Padé boundary, never away from both boundaries.

#### Proof

Both quantities are minima, over the same affine set \(q(-w)=1\), of integrals
of nonnegative kernels.  Increasing the measure increases every feasible
objective.  ∎

This is a global monotonicity theorem; it does not depend on infinitesimal
perturbation theory or a fixed endpoint vector.

---

## 5. Finite line-mass budget contradiction

Suppose proof-grade disjoint bins

\[
Y_r=[L_r,U_r]\subseteq[A,\infty)
\]

are each certified to contain at least \(m_r\) actual critical-line zeros,
counted with multiplicity.  For a frozen rational polynomial \(q_-\), define a
rigorous lower bound

\[
\kappa_r^-\le\inf_{y\in Y_r}K_-(y).
\]

Likewise, for \(q_+\), define

\[
\kappa_r^+\le\inf_{y\in Y_r}K_+^{(A)}(y).
\]

Under RH, the certified atoms are part of the positive residual measure, so

\[
oxed{
 g_-(w)\ge\sum_r m_r\kappa_r^- ,
}
	ag{7}
\]

\[
oxed{
 g_+^{(A)}(w)\ge\sum_r m_r\kappa_r^+ .
}
	ag{8}
\]

### Corollary 5.1 — finite counterexample predicates

Let \(G_-\) and \(G_+\) be directed intervals containing the two total gaps.
If

\[
oxed{
 \sup G_-<\sum_r m_r\kappa_r^- ,
}
	ag{9}
\]

or

\[
oxed{
 \sup G_+<\sum_r m_r\kappa_r^+ ,
}
	ag{10}
\]

then RH is false, subject to the direct-ξ normalization, endpoint-vector, and
zero-bin gates.

The certificate is finite and value-only after the endpoint polynomial has
been frozen.  It does not need a new deflated completed-ξ evaluation.

#### Proof

The right sides are lower bounds for the contribution of a subset of atoms to
the nonnegative integrals (2) and (4).  They cannot exceed the corresponding
total integral.  ∎

### Important anti-double-counting gate

The bins must be pairwise disjoint or must carry an independently verified
integer allocation proving that no zero multiplicity is counted twice.  Merely
summing overlapping lower-count windows is invalid.

---

## 6. Exact interval evaluation over a zero bin

For a rational interval \(Y=[L,U]\), the leverage kernels are rational functions
with positive denominator on the declared support.

A fail-closed checker may obtain \(\kappa_Y\) by:

1. interval Horner evaluation of \(q(Y)\);
2. exact squaring, with lower endpoint zero if the interval crosses zero;
3. exact interval products for \(Y+w\) and \(D_U(Y)\);
4. for the upper kernel, multiplication by \(Y-A\);
5. division by a strictly positive denominator interval.

This elementary interval bound can be sharpened by isolating the real roots of
\(q\) and evaluating the rational kernel at endpoints and stationary points.
The elementary hull is already sufficient for a proof; sharpening affects only
power.

---

## 7. Refinement and scheduling scores

For an exact atom at \(y\), define the lower and upper leverage scores

\[
\lambda_-(y)=K_-(y),
\qquad
\lambda_+(y)=K_+^{(A)}(y).
\]

For a certified bin, preserve both

\[
\underline\lambda_r=\inf_{Y_r}\lambda,
\qquad
\overline\lambda_r=\sup_{Y_r}\lambda.
\]

The width

\[
\overline\lambda_r-ambda_r-\underline\lambda_r
\]

is the exact value of refining that zero bin for the active Padé witness.  This
provides a witness-specific scheduling rule for the saturated sign-chain bins
of PR #108:

```text
refine the bins with the largest multiplicity-weighted leverage uncertainty,
not necessarily the nearest bins or the widest ordinate bins.
```

The same score chooses which selected factors in PR #107 deserve exact
interval-valued removal first.

---

## 8. Relationship to the normalized Padé coordinate

With finite endpoints,

\[
\eta_A(w)=rac{g_-(w)}{g_-(w)+g_+^{(A)}(w)}.
\]

By (2) and (4), this is a ratio of two positive Christoffel-type residual
energies.  A small absolute gap caused only by collapse of both integrals is not
an invariant near-counterexample; a small normalized gap means the lower
Christoffel energy is small relative to the total finite moment uncertainty.

The leverage decomposition therefore supplies the spectral explanation for the
candidate correction in O-9312.

---

## 9. Proof boundary

The gap identities, variational formulas, measure monotonicity, and finite mass
budget inequalities are exact.

A Riemann-ξ contradiction requires:

1. directed old moments and the new scalar value;
2. a rational endpoint polynomial normalized by \(q(-w)=1\);
3. exact contraction of the total gap interval;
4. proof-grade, non-overlapping critical-line zero bins and multiplicities;
5. exact interval lower bounds for every leverage contribution;
6. a strict inequality (9) or (10);
7. independent normalization, zero-isolation, and special-function review.

No Riemann-ξ negative is asserted by this lemma.
