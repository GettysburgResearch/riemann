# L-8502 — One exact direction plus a coarse complement bound closes a Hermitian matrix

Claim ID: L-8502  
Title: A strict fixed-vector moat repairs a coarse operator approximation by a one-dimensional Schur complement  
Status: PROPOSED  
Authoring agent: `gpt56-03-h`  
Created: 2026-07-25  
Dependencies: elementary Hermitian block algebra; the exact fixed-vector interval from X-2805 for the target application  
Scope: finite Hermitian matrices, especially the recovered `c=10^11`, `K=1024` D-0801 carrier matrix  
Related counterexample candidates: none

## Statement

Let `H` and `H_0` be Hermitian operators on a finite-dimensional complex inner-product space. Let `u` be a unit vector and put

\[
 P=I-uu^*.
\]

Assume the following four inequalities:

1. one exact directional moat,
   \[
   u^*Hu\ge a>0;
   \]
2. a lower bound on the reference complement,
   \[
   x^*H_0x\ge\beta\|x\|_2^2
   \quad\text{for every }x\perp u;
   \]
3. a reference residual bound,
   \[
   \|PH_0u\|_2\le r;
   \]
4. a global operator approximation,
   \[
   \|H-H_0\|_2\le\delta.
   \]

If

\[
 \boxed{
 \beta>\delta
 \quad\text{and}\quad
 a(\beta-\delta)>(r+\delta)^2,
 }
\]

then

\[
 \boxed{H\succ0.}
\]

More quantitatively, the lower-right Schur complement is bounded below by

\[
 \left(eta-\delta-rac{(r+\delta)^2}{a}\right)P.
\]

Thus the theorem can close every direction even when the available global
operator moat `delta` is several times larger than the exact fixed-direction
margin `a`.

## Proof

Use the orthogonal decomposition

\[
 \mathbb C^n=\operatorname{span}\{u\}\oplus u^\perp.
\]

In this decomposition write

\[
 H=
 \begin{pmatrix}
 q & b^*\\
 b & C
 \end{pmatrix},
\]

where

\[
 q=u^*Hu,
 \qquad
 b=PHu,
 \qquad
 C=PHP|_{u^\perp}.
\]

The first hypothesis gives `q>=a>0`.

For every `x\perp u`,

\[
 \begin{aligned}
 x^*Cx
 &=x^*Hx\\
 &=x^*H_0x+x^*(H-H_0)x\\
 &\ge(\beta-\delta)\|x\|_2^2.
 \end{aligned}
\]

Hence

\[
 C\succeq(\beta-\delta)I_{u^\perp}.
\]

The off-diagonal block satisfies

\[
 \begin{aligned}
 \|b\|_2
 &=\|PHu\|_2\\
 &\le\|PH_0u\|_2+\|P(H-H_0)u\|_2\\
 &\le r+\delta.
 \end{aligned}
\]

Since `q>0`, the block matrix `H` is positive definite exactly when its Schur
complement

\[
 C-\frac{bb^*}{q}
\]

is positive definite. For every `x\perp u`,

\[
 \begin{aligned}
 x^*\left(C-\frac{bb^*}{q}\right)x
 &\ge
 (\beta-\delta)\|x\|_2^2
 -\frac{|b^*x|^2}{a}\\
 &\ge
 \left(
 \beta-\delta-rac{(r+\delta)^2}{a}
 \right)\|x\|_2^2.
 \end{aligned}
\]

The displayed strict hypothesis makes the coefficient positive. Therefore the
Schur complement, and hence `H`, is positive definite. ∎

## Arbitrary nonzero vector form

Let `w` be a nonzero exact vector and set

\[
 N=w^*w,
 \qquad
 u=\frac{w}{\sqrt N}.
\]

No square root is needed in a rational checker. It may instead verify:

- a raw quadratic lower bound `w^*Hw>=A`, so `a=A/N`;
- a squared residual bound
  \[
  \|PH_0w\|_2^2\le R^2N,
  \]
  where `R` is a supplied rational upper bound;
- the same complement and operator bounds.

The final rational comparison is then

\[
 \boxed{
 A(\beta-\delta)>N(R+\delta)^2.
 }
\]

The projection residual can be computed without irrational normalization:

\[
 \|PH_0w\|_2^2
 =\|H_0w\|_2^2-rac{|w^*H_0w|^2}{N}.
\]

All terms are rational whenever `H_0` and `w` are Gaussian rational.

## Exact coarse target gate

The complete X-2805 192-bit target replay proves for the recovered exact vector

\[
 \frac{w^*Hw}{w^*w}>rac1{4000}.
\]

Therefore the following three additional, deliberately coarse bounds would
already close the entire `K=1024` matrix:

\[
 \boxed{
 \beta>\frac7{1000},
 \qquad
 r<\frac1{5000},
 \qquad
 \delta<\frac1{1000}.
 }
\]

Indeed,

\[
 \frac1{4000}
 \left(\frac7{1000}-\frac1{1000}\right)
 =\frac{3}{2{,}000{,}000},
\]

while

\[
 \left(\frac1{5000}+\frac1{1000}\right)^2
 =\frac{36}{25{,}000{,}000}.
\]

Their difference is exactly

\[
 \boxed{
 \frac{3}{50{,}000{,}000}>0.
 }
\]

Thus this route needs only a `10^-3` operator approximation, not an approximation
at the `2.67*10^-4` smallest-direction scale.

For orientation, the empirical discovery matrix reports

```text
smallest H_0 eigenvalue    about 2.6911845199e-4
second H_0 eigenvalue      about 7.3688948687e-3
frozen-vector residual     about 2.6221e-15
```

so the complement and residual gates have enormous observed slack. These three
decimal values are discovery diagnostics only. The theorem accepts them only
after exact or directed certification.

## Why the theorem is strategically stronger than a global Weyl bound

A direct Weyl proof from `H_0` would require

\[
 \|H-H_0\|_2<\lambda_{\min}(H_0),
\]

which is at the scale `2.7*10^-4` in the current target. L-8502 replaces the
fragile lowest reference eigenvalue by:

- the already certified exact quadratic along its near-null direction; and
- the much larger spectral gap on the orthogonal complement.

The resulting permitted global moat is approximately the positive root of

\[
 a(\beta-\delta)=(r+\delta)^2,
\]

which, at the observed target values, is about `1.276*10^-3`. The simple exact
gate `delta<10^-3` stays comfortably inside that range.

## How to certify the three remaining gates

### Complement gate

Any of the following is sufficient:

1. exact Gaussian-rational `LDL^*` of
   \[
   H_0-\beta I+\tau uu^*
   \]
   for some positive rational `tau`;
2. a directed Lanczos/Krylov lower bound for the second eigenvalue, with a
   separately checked residual theorem;
3. a circulant or trigonometric completion specialized to the orthogonal
   complement;
4. an exact sum-of-squares or rational Gram factorization of the repaired
   reference matrix.

### Residual gate

For Gaussian-rational `H_0,w`, compute

\[
 \|H_0w\|_2^2-rac{|w^*H_0w|^2}{w^*w}
\]

exactly and compare with `N/25,000,000`. This is a cheap matrix-vector audit,
not an eigensolve.

### Operator gate

For the Toeplitz coefficient convention of D-0801, a complete complex
coefficient error ledger gives

\[
 \|S-S_0\|_2
 \le
 |\Delta c_0|+\sum_{d=1}^{K-1}|\Delta c_d|.
\]

Add the scalar-alpha and nonprime operator radii in the same normalized basis.
A target-wide bound below `1/1000` is sufficient.

The fast midpoint architecture of PR #82 already demonstrates a much smaller
fixed-vector global moat. L-8502 identifies the separate operator-norm budget
that a coefficient-producing version must prove.

## Analytic and dependency audit

- L-8502 is finite Hermitian linear algebra and has no RH-specific assumption.
- The target value `a` inherits only the quantitative X-2805 producer and checker
  contracts.
- Interpreting positive definiteness of the finite carrier matrix as an RH-valid
  statement retains D-0801 admissibility and Guinand--Weil normalization
  dependencies.
- A positive result closes only this exact carrier, cutoff, dimension, and test
  family.

## Gap audit

1. The empirical second eigenvalue is not a complement certificate.
2. A tiny floating residual is not an exact residual certificate.
3. A fixed-vector arithmetic moat does not automatically imply an operator moat.
4. `H_0` and every gate must use the same normalization and basis as the exact
   X-2805 quadratic.
5. The Schur inequality must be strict; touching zero is inconclusive.
6. A positive finite matrix does not prove RH.

## Adversarial tests

1. Construct exact `2 x 2` examples on both sides of
   `a(beta-delta)=(r+delta)^2`.
2. Mutate `beta`, `r`, or `delta` so equality holds and require rejection.
3. Compare the theorem with exact eigenvalues on random rational Hermitian
   matrices.
4. Verify the arbitrary-vector projection identity exactly.
5. Mutate the target vector norm or final quadratic endpoint and require the
   coarse gate checker to fail.

## Suggested next attack

Build a proof-producing reference matrix `H_0` from the complete discovery
coefficients, then certify only:

```text
complement lower bound  > 7/1000
normalized residual     < 1/5000
complete operator moat  < 1/1000
```

Together with the already complete X-2805 positive interval, these three coarse
inequalities settle the entire recovered `K=1024` matrix.
