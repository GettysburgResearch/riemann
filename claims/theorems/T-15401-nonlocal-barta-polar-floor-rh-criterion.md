# T-15401 — Nonlocal Barta–Birman–Schwinger lower floors imply RH

Claim ID: `T-15401`  
Title: One positive supersolution and one odd polar scalar certify the full ambient localized Weil floor  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-07-31  
Dependencies: L-15401; T-14302; elementary nonlocal ground-state representation; rank-one Birman–Schwinger criterion  
Scope: positive sufficient criterion for RH through Suzuki's localized Weil form  
Related counterexample candidates: none

## Part I — Abstract nonlocal ground-state identity

Let `(X,\mu)` be a measure space.  Let `J` be a symmetric nonnegative measure on
`X\times X`, and let `V:X\to\mathbb R` be measurable.  On a common form core,
define

\[
 \mathfrak h(f)=
 \frac12\int_{X\times X}|f(x)-f(y)|^2\,J(dx,dy)
 +\int_XV(x)|f(x)|^2\,d\mu(x).
\tag{T-15401.1}
\]

Let `\psi>0` almost everywhere and suppose all expressions below are defined.
Set

\[
 b_\psi(x)=V(x)+\frac1{\psi(x)}
 \int_X\bigl(\psi(x)-\psi(y)\bigr)J_x(dy),
\tag{T-15401.2}
\]

where `J_x` denotes the disintegration of `J` with respect to `\mu`.

Then, for every core function `f`, with `g=f/\psi`,

\[
\boxed{
\begin{aligned}
 \mathfrak h(f)
 ={}&\frac12\int_{X\times X}
 \psi(x)\psi(y)|g(x)-g(y)|^2\,J(dx,dy)\\
 &+\int_Xb_\psi(x)|f(x)|^2\,d\mu(x).
\end{aligned}}
\tag{T-15401.3}
\]

Consequently,

\[
\boxed{
 \mathfrak h(f)\ge m_\psi\|f\|_2^2,
 \qquad
 m_\psi=\operatorname*{ess\,inf}_{x\in X}b_\psi(x).}
\tag{T-15401.4}
\]

This is a complete ambient lower bound.  It is not a Ritz value and contains no
omitted-mode assumption.

### Proof

For positive numbers `p,q` and arbitrary complex `u,v`, the exact identity

\[
 |u-v|^2
 =pq\left|\frac up-\frac vq\right|^2
 +(p-q)\left(\frac{|u|^2}{p}-\frac{|v|^2}{q}\right)
\tag{T-15401.5}
\]

holds after expansion.  Apply it with

\[
 p=\psi(x),\quad q=\psi(y),\quad u=f(x),\quad v=f(y),
\]

integrate against the symmetric measure `J`, and symmetrize the second term.
The result is

\[
 \frac12\int|f(x)-f(y)|^2J
 =\frac12\int\psi(x)\psi(y)|g(x)-g(y)|^2J
 +\int\frac{L_J\psi}{\psi}|f|^2d\mu,
\]

where

\[
 L_J\psi(x)=\int(\psi(x)-\psi(y))J_x(dy).
\]

Adding the potential proves (T-15401.3), and (T-15401.4) follows because the
first term is nonnegative.  QED.

The argument is the linear finite-energy case of the nonlocal ground-state
representations used in sharp fractional Hardy inequalities, but the proof above
is self-contained.

## Part II — Finite positive and negative polar channels

Let `H` be the self-adjoint operator associated with `\mathfrak h`, and suppose
`H` commutes with a parity involution.  Let `c` be even, `s` odd, and `\tau>0`.
Define

\[
 A=H+\tau|c\rangle\langle c|-\tau|s\rangle\langle s|.
\tag{T-15401.6}
\]

Let `m` be any rigorous lower bound for `H`, for example `m=m_\psi` from
(T-15401.4).  Fix a real `\lambda<m` and put

\[
 R_s(\lambda)=
 \langle s,(H_{\rm odd}-\lambda I)^{-1}s\rangle.
\tag{T-15401.7}
\]

Then

\[
\boxed{
 \tau R_s(\lambda)\le1
 \quad\Longrightarrow\quad
 A\succeq\lambda I.}
\tag{T-15401.8}
\]

If the inequality is strict, the odd-sector update is strictly above `\lambda`.
At equality, the conclusion is non-strict and the certificate must retain the
boundary status.

### Proof

On the even sector, `s` vanishes and the positive `c` channel can only increase
the form, so

\[
 A_{\rm even}\succeq H_{\rm even}\succeq mI\succ\lambda I.
\]

On the odd sector, `c` vanishes and

\[
 A_{\rm odd}-\lambda I
 =(H_{\rm odd}-\lambda I)-\tau|s\rangle\langle s|.
\]

Since `H_{\rm odd}-\lambda I` is positive and invertible, conjugation by its
inverse square root gives

\[
 A_{\rm odd}-\lambda I\succeq0
 \iff
 I-\tau|u\rangle\langle u|\succeq0,
\]

where

\[
 u=(H_{\rm odd}-\lambda I)^{-1/2}s.
\]

The latter rank-one operator is positive semidefinite exactly when

\[
 \tau\|u\|^2=\tau R_s(\lambda)\le1.
\]

Combining the two parity sectors proves (T-15401.8).  QED.

### Immediate coarse resolvent bound

The Barta floor alone gives

\[
 R_s(\lambda)\le\frac{\|s\|^2}{m-\lambda}.
\tag{T-15401.9}
\]

This bound is often conservative.  A sharper upper enclosure may come from:

1. a block Schur certificate as in L-14308;
2. a verified positive supersolution for the resolvent equation;
3. an exact finite-rank solve plus an ambient complement bound;
4. a continued-fraction or Green-function bound adapted to the odd sector.

Only one scalar upper bound is required.

## Part III — Suzuki specialization

Use the exact decomposition of L-15401.  Let `H_a` denote the Markov
jump–potential operator whose form is `\mathcal E_a`, and write

\[
 A_a=H_a+2a|c_a\rangle\langle c_a|
          -2a|s_a\rangle\langle s_a|,
\tag{T-15401.10}
\]

where

\[
 c_a(x)=\cosh(ax/2),
\qquad
 s_a(x)=\sinh(ax/2).
\]

For a positive admissible function `\psi_a`, define

\[
\begin{aligned}
 b_{a,\psi}(x)={}&V_a(x)\\
 &+\frac1{\psi_a(x)}\int_I
 K_a(|x-y|)\bigl(\psi_a(x)-\psi_a(y)\bigr)\,dy\\
 &+\frac1{\psi_a(x)}\sum_{n\le e^{2a}}c_n
 \Bigl[
  \mathbf1_{x+\delta_n\in I}
   \bigl(\psi_a(x)-\psi_a(x+\delta_n)\bigr)\\
 &\hspace{47mm}+\mathbf1_{x-\delta_n\in I}
   \bigl(\psi_a(x)-\psi_a(x-\delta_n)\bigr)
 \Bigr].
\end{aligned}
\tag{T-15401.11}
\]

Suppose directed analysis proves

\[
 b_{a,\psi}(x)\ge m_a
\quad\text{for almost every }x\in I.
\tag{T-15401.12}
\]

For a proposed floor `\lambda_a<m_a`, suppose also that a rigorous scalar bound

\[
 B_a\ge
 \langle s_a,(H_{a,\rm odd}-\lambda_a I)^{-1}s_a\rangle
\tag{T-15401.13}
\]

satisfies

\[
 2aB_a\le1.
\tag{T-15401.14}
\]

Then

\[
\boxed{
 \inf\sigma(A_a)\ge\lambda_a.}
\tag{T-15401.15}
\]

Because Suzuki identifies the localized Weil ground value with the infimum over
a smooth compactly supported form core, it is enough that the inequalities be
proved uniformly on that core and pass to the closure.

## Part IV — Cofinal RH criterion

Let `a_j\to\infty`.  For each `j`, suppose there are exact or directed objects

\[
 \psi_j>0,\qquad m_j,\qquad \lambda_j<m_j,\qquad B_j
\]

satisfying (T-15401.12)–(T-15401.14), and assume

\[
\boxed{
 \liminf_{j\to\infty}\lambda_j\ge0.}
\tag{T-15401.16}
\]

Then the Riemann hypothesis is true.

### Proof

Equation (T-15401.15) gives a cofinal lower spectral envelope for Suzuki's
localized Weil operators.  T-14302 proves that any such envelope whose lower
limit is nonnegative forces every fixed-support localized form to be
nonnegative.  Weil's positivity criterion then gives RH.  QED.

## Why this is a different positive route

The lower-floor program in PR #152 decomposes the Hilbert space into a growing
finite prolate packet and an infinite complement.  T-15401 offers a logically
different certificate:

```text
one positive continuum supersolution
+ one pointwise residual enclosure
+ one odd rank-one resolvent scalar.
```

The Barta identity controls the complete ambient jump operator directly.  It
cannot miss a negative omitted mode.

## Candidate supersolution families

The following are worth testing, but none is promoted by this theorem:

1. positive rational splines fitted to the lowest finite Markov eigenvector;
2. positive prolate ground functions on the scaled interval;
3. endpoint-weighted functions `(1-x^2)^\alpha p(x)`;
4. positive solutions of a simplified archimedean jump operator;
5. continuation of a certified supersolution from one support to a nearby
   support.

The CCM arithmetic radical target is not known to be positive and must not be
inserted into (T-15401.11) without a separate sign theorem.

## Proof-producing schema

A finite certificate should bind:

1. exact `a` and a complete duplicate-free prime-power manifest;
2. an exact positive rational spline `\psi` and a rational positivity moat;
3. a partition containing every spline knot, prime-shift image, and potential
   discontinuity;
4. directed interval enclosures of `U_a`, the continuous jump residual, and
   every translated residual on each cell;
5. a strict pointwise lower bound `m`;
6. a target `\lambda<m`;
7. one source-bound upper enclosure of the odd resolvent scalar;
8. the comparison `2aB\le1`;
9. a final cofinal symbolic envelope, not merely a finite list of supports.

## Gap audit

- The exact decomposition is useful only if the cancellation-safe kernel and
  potential are evaluated together.
- A finite-grid check of `b_{a,\psi}` does not prove the pointwise bound between
  nodes.
- The supersolution must remain strictly positive on the complete open interval;
  endpoint zeros require a weighted limiting argument.
- A lower bound for a finite resolvent compression is in the wrong direction for
  (T-15401.13); the scalar needs an ambient upper enclosure.
- The crude estimate (T-15401.9) may be far too weak.
- A good finite support does not prove the cofinal condition (T-15401.16).
- This theorem supplies a concrete sufficient route.  It does not establish the
  required supersolution family and therefore does not yet prove RH.
