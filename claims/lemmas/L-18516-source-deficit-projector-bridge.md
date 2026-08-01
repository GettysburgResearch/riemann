# L-18516 — Exact source-flag to deficit-canonical projector bridge

Claim ID: `L-18516`  
Title: Invariance plus two strict threshold LMIs are necessary and sufficient to identify a proposed source flag with the canonical high-deficit spectral augmentation  
Status: `PROPOSED — COMPLETE FINITE-DIMENSIONAL PROOF`  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-01  
Dependencies: spectral theorem; exact metric whitening; `L-18901`  
Scope: the missing `D_lambda,Q_0,Q_D` production bridge

## 1. Deficit-complement coordinates

Let

\[
 G\succ0,
 \qquad
 D\succeq0
\]

be the declared metric and complete positive deficit at one support. Let

\[
 Q_0:\mathbb C^m\to\mathbb C^n
\]

be a full-rank basis of the metric complement of the pre-existing packet. Put

\[
 G_0=Q_0^*GQ_0,
 \qquad
 D_0=Q_0^*DQ_0.
\]

Fix the threshold

\[
 \theta=g-\Gamma.
\]

The deficit-canonical augmentation of `L-18901` is

\[
 \mathcal D
 =\operatorname{Ran}
 \mathbf1_{(\theta,\infty)}
 \left(G_0^{-1/2}D_0G_0^{-1/2}\right).
 \tag{L-18516.1}
\]

## 2. Exact finite certificate

Let `Y_D` and `Y_C` have respectively `r` and `m-r` columns. Assume

\[
 [Y_D\;Y_C]
\]

is invertible and

\[
 Y_C^*G_0Y_D=0.
 \tag{L-18516.2}
\]

Then

\[
 \boxed{
 Q_D=Q_0Y_D
 }
\]

is exactly the deficit-canonical augmentation if the following three directed
conditions hold:

\[
 \boxed{
 Y_C^*D_0Y_D=0,
 }
 \tag{L-18516.3}
\]

\[
 \boxed{
 Y_D^*(D_0-\theta G_0)Y_D\succ0,
 }
 \tag{L-18516.4}
\]

\[
 \boxed{
 Y_C^*(\theta G_0-D_0)Y_C\succ0.
 }
 \tag{L-18516.5}
\]

### Proof

Equation (L-18516.2) gives a metric-orthogonal complete decomposition. Equation
(L-18516.3) makes both summands invariant for the generalized pair `(D_0,G_0)`.
After whitening each block, (L-18516.4) places every eigenvalue of the first
block strictly above `theta`, while (L-18516.5) places every eigenvalue of the
second strictly below `theta`. The spectral theorem now identifies the first
block with (L-18516.1). QED.

Conversely, if `Q_D` is the spectral range in (L-18516.1) and the threshold is
not an eigenvalue, its metric orthogonal complement satisfies
(L-18516.2)--(L-18516.5). Thus the certificate is necessary and sufficient in
the strict-gap case.

## 3. Identifying the source-canonical flag

Let `Y_S` be the proposed source-canonical absorbed flag in the `Q_0`
coordinates. Once `Y_D` is certified, the source and deficit flags agree exactly
if and only if

\[
 \boxed{
 \operatorname{Ran}Y_S=\operatorname{Ran}Y_D.
 }
 \tag{L-18516.6}
\]

A proof object may verify (L-18516.6) by supplying an invertible exact matrix
`T` such that

\[
 Y_S=Y_DT,
\]

or by exact rank tests in both directions.

The equality cannot be inferred from

\[
 \dim Y_S=\dim Y_D
\]

alone. Nor does the source constraint imply the invariance condition
(L-18516.3): the source flag is chosen from endpoint arithmetic, while `D_0`
depends on the complete weighted symbol deficit.

## 4. Production schema

The exact bridge artifact must bind, at one common support and metric,

```text
G_lambda
D_lambda
g_lambda
Gamma_lambda
Q_0
Y_D, Y_C
source Y_S
```

and the independent consumer must reconstruct

```text
G_0 = Q_0* G Q_0
D_0 = Q_0* D Q_0
cross = Y_C* D_0 Y_D
high  = Y_D* (D_0-theta G_0) Y_D
low   = Y_C* (theta G_0-D_0) Y_C.
```

The accepted result classes are

```text
CERTIFIED_SOURCE_EQUALS_DEFICIT_CANONICAL
CERTIFIED_DEFICIT_CANONICAL_SOURCE_NOT_IDENTIFIED
UNRESOLVED_DEFICIT_PROJECTOR
```

No D-0001 prime matrix may be silently substituted for the positive deficit
`D_lambda`; the lower model and its metric are part of the certificate.

## 5. Proof boundary

The bridge algebra is complete. The repository currently has no production
artifact containing the complete Suzuki `D_lambda`, `Q_0`, and a directed
spectral splitting `Y_D,Y_C` for the same support as `X-18507`. Therefore the
source flag has not been identified with the global deficit-canonical
augmentation.
