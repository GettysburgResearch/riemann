# R-91007 — Diagonal Cauchy gates cannot replace the fixed-scale Lévy Gram

Claim ID: `R-91007`  
Status: **EXACT POLARIZATION FIREWALL**  
Created: 2026-08-11  
Depends on: `L-91031`, `L-91032`, `T-91007`  
RH status: **unproved**

## 1. The recurrence sees only a diagonal

At a fixed safe scale `a_0>1/2`, the normalized sixteenfold Cauchy route tests

\[
 \mathbb K_{a_0}((+,x),(+,x))
 =a_0^4\mathcal R_x(a_0).
\]

Even adding the anti-causal diagonal gives only

\[
 \mathbb K(i,i)\ge0
 \qquad(i\in\mathfrak I).
\]

## 2. Exact finite countermodel

Positive diagonal entries do not imply kernel positivity.  The matrix

\[
 \boxed{
 H=\begin{pmatrix}1&7/4\\7/4&1\end{pmatrix}
 }
\]

has positive diagonal but eigenvalues

\[
 \frac{11}{4},\qquad-\frac34.
\]

The same phenomenon occurs for continuous Hermitian kernels: nonnegative
pointwise diagonal values do not exclude a negative two-point Pick matrix.

## 3. Why both Hardy orientations and the bridge are load-bearing

The causal family spans the positive-half-line functions with zero half-line
integral.  The anti-causal family supplies the reflected negative-half-line
space.  Their cross terms reconstruct tests with support on both sides of the
origin.

Even both orientations together miss one direction: functions whose two
half-line integrals are nonzero and cancel globally.  The bridge of `L-91032`
fills exactly that defect.

Deleting any of these pieces prevents recovery of Suzuki's complete mean-zero
screw form.

Therefore the inference

```text
all scalar dyadic residuals are nonnegative
 -> full screw kernel is positive
 -> RH
```

is invalid without an additional exact polarization theorem.

## 4. The source environment must not be traced out too early

`L-91020` proves the inherited Jordan multiplier is a completely positive
correlation channel and contracts negative trace mass.  Forward CP contraction
does not let a positive diagonal output be pulled backward to a positive
input.

The Poisson Fock realization of `L-91030/L-91033` retains the full Stinespring
phase vectors.  Tracing out that environment before matching the causal,
anti-causal and bridge outputs recreates the same gap.

A valid finish must provide one of:

1. full fixed-scale cross-Gram positivity;
2. an exact source-ordered polarization identity for every cross entry;
3. the conservative completed Fock/Hardy colligation of `T-91007`.

## 5. Boundary

```text
diagonal residual positivity                    INSUFFICIENT EXACTLY
causal-only fixed-scale family                   INCOMPLETE
causal+anti-causal without bridge                CODIMENSION ONE TOO SMALL
full two-Hardy-channel plus bridge family        COMPLETE FORM CORE
conservative source/output polarization          OPEN / RH-EQUIVALENT
Riemann Hypothesis                               UNPROVED
```
