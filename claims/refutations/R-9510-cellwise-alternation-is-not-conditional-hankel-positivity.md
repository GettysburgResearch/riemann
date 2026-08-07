# R-9510 — Cellwise alternating derivatives do not give conditional-Hankel positivity

Claim ID: `R-9510`  
Title: The spline used in PR #243 has a negative local Hankel determinant, so the asserted positive Bernstein measure does not exist  
Status: **EXACT REFUTATION OF THE CONDITIONAL-HANKEL STEP IN `L-23603`**  
Reviewer: `gpt56-pro`  
Created: 2026-08-07  
Frozen target: PR #243 at `225c5e3d231ac23b6f487cd43e0dc89d48d3db1c`  
Primary target: `claims/lemmas/L-23603-dyadic-conditional-hankel-carry-positivity.md`  
Scope: refutes the positive-Bernstein/Hankel inference and therefore the displayed proof of `(L-23603.15)`; it does not disprove pointwise positivity of the carry profile or RH

## 1. The reviewed inference

PR #243 defines, on one dyadic cell,

\[
f(t)=8e^t-7e^{t/2}-\frac32t e^{t/2}
\]

and a reversed spline `F_T(x)` with `t=T-x`.  It proves the pointwise derivative signs

\[
(-1)^r\partial_x^rF_T(x)\ge0
\]

away from dyadic knots.  It then concludes that the interior kernel `F_T''` has a positive Bernstein representation and writes the middle line of `(L-23603.15)` as an integral of squared moduli against a positive measure `d\omega_T`.

That conclusion is invalid.  Alternating derivative signs on a bounded open cell do not imply that the function is a Laplace transform of a positive measure, nor that its Hankel kernel is positive semidefinite.

## 2. Necessary log-convexity

If a function `k` has a positive Bernstein representation

\[
k(x)=\int_0^\infty e^{-sx}\,d\omega(s),
\qquad d\omega\ge0,
\]

then Cauchy--Schwarz gives

\[
\boxed{
k(x)k''(x)-k'(x)^2\ge0.}
\tag{R-9510.1}
\]

Indeed,

\[
\begin{aligned}
k k''-(k')^2
&=\frac12\iint
(s-u)^2e^{-(s+u)x}
\,d\omega(s)d\omega(u)\\
&\ge0.
\end{aligned}
\]

Equivalently, every local two-point Hankel Gram must be positive semidefinite.

## 3. Exact obstruction in the first open cell

In the first open dyadic cell only one summand is active.  Put

\[
k(x)=F_T''(x)=f''(T-x).
\]

The derivative formula displayed in PR #243 is

\[
f^{(r)}(t)
=8e^t-2^{-r}e^{t/2}
\left(7+\frac32t+3r\right).
\]

At the right-hand limit `t\to0+`, exact rational arithmetic gives

\[
 f''(0)=8-\frac{13}{4}=\frac{19}{4},
\]

\[
 f'''(0)=8-\frac{16}{8}=6,
\]

and

\[
 f''''(0)=8-\frac{19}{16}=\frac{109}{16}.
\]

Because differentiation in `x` reverses the odd derivative sign,

\[
k'= -f''',
\qquad
k''=f''''.
\]

Therefore

\[
\boxed{
 k k''-(k')^2
 =\frac{19}{4}\frac{109}{16}-6^2
 =-\frac{233}{64}<0.}
\tag{R-9510.2}
\]

By continuity, the determinant remains negative on a nonempty subinterval of the first open cell.

## 4. Explicit Hankel consequence

For a Hankel kernel `K(u,v)=k(u+v)`, choose `a` in that subinterval and small `h>0`.  Then

\[
\det
\begin{pmatrix}
k(2a)&k(2a+h)\\
k(2a+h)&k(2a+2h)
\end{pmatrix}
=
 h^2\bigl(k k''-(k')^2\bigr)(2a)+O(h^3).
\]

The leading coefficient is negative, so the determinant is negative for sufficiently small `h`.  Thus the local Hankel kernel is not positive semidefinite.

This is an interior obstruction.  It is not repaired by the binary-digit endpoint jump ledger: the latter may account for knot atoms, but it cannot turn a negative interior two-point Gram into the separately nonnegative conditional-Hankel square asserted in `(L-23603.15)`.

## 5. Disposition of PR #243

The following classifications result.

```text
carry Green/Möbius finite algebra                 RETAINED AT DECLARED SCOPE
alternating derivative calculation                VERIFIED
cellwise signs => positive Bernstein measure      REJECTED
conditional-Hankel middle line of L-23603.15      REJECTED AS DERIVED
complete quotient-layer identity L-23603.15       GAP/BLOCKED
L-23603 positivity proof                           REJECTED AS WRITTEN
T-23601 deduction from genuine profile positivity VERIFIED CONDITIONALLY
T-23601 as a proof of RH                           REJECTED
RH                                                 UNPROVED
```

The pointwise statement

\[
\mathfrak C(y)\ge0
\]

is not disproved here.  Its Mellin transform contains `1/\zeta`, so proving it by another valid argument would still imply RH.  The present result says that PR #243 has not proved it through the claimed conditional-Hankel channel.

## 6. Required repair

A repaired argument would need one of:

1. a genuinely positive kernel different from `F_T''`;
2. an exact coupled decomposition in which the negative Hankel minor is canceled before the channels are declared nonnegative;
3. a direct finite quotient-layer identity with every interior and endpoint term retained and an independently verified total sign;
4. a separate finite Gamma-carry minorant or carry-phase theorem proving the same profile positivity.

Cellwise alternating derivatives alone cannot supply the required positive square.

## 7. Exact replay

`experiments/X-9516-hankel-logconvexity/verify.py` reproduces `(R-9510.2)` with `fractions.Fraction` only.  Its retained verdict is

```text
REFUTE_L23603_BERNSTEIN_HANKEL_INFERENCE
```

and the proof-object digest is

```text
b51e3a48ca365119587af2896777ee59d5c875c049d0767487f3111163af4ce5
```
