# O-32402 — The constant carry-position mode is the canonical carry-resolvent channel

Claim ID: `O-32402`  
Status: **PROPOSED EXACT CROSS-ROUTE IDENTIFICATION / SCOPE FIREWALL**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: `L-32401`, `L-32402`; PR #252 `L-24501`; PR #302 `L-28011`

## 1. Uniform carry-position average

For the atomized carry kernel

\[
 C(x,\theta)
 =\lfloor x\rfloor
  -\lfloor\theta x\rfloor
  -\lfloor(1-\theta)x\rfloor,
\]

PR #289 / PR #252 use the exact average

\[
 \boxed{
 \int_0^1C(x,\theta)d\theta
 =b(x)
 :={\lfloor x\rfloor(\lfloor x\rfloor+1-x)\over x}.
 }
\tag{O-32402.1}
\]

In logarithmic coordinates

\[
 k(t)=e^{-t/2}b(e^t)
\]

has Mellin/Laplace transform

\[
 \widehat k(s)
 =\zeta(s){s-1\over s(s+1)}
\tag{O-32402.2}
\]

in the unshifted `s` normalization.

## 2. Mean of the local-Euler field

Let

\[
 \overline{\mathfrak P}_\lambda(t)
 =\int_0^1\mathfrak P_{\lambda,\theta}(t)d\theta.
\]

Integrating the exact carry representation before any norm gives

\[
 \boxed{
 \overline{\mathfrak P}_\lambda
 =k*\left(
  \sum_n{q_\lambda(n)\over\sqrt n}\delta_{\log n}
 \right),
 }
\tag{O-32402.3}
\]

where

\[
 q_\lambda=b_\lambda*\Lambda_\lambda=-b_\lambda\log.
\]

Equivalently, with `s=z+1/2`,

\[
 \boxed{
 \widehat{\overline{\mathfrak P}_\lambda}(z)
 =(1-\lambda2^{-s})
 {s-1\over s(s+1)}L_\lambda(s).
 }
\tag{O-32402.4}
\]

Thus the constant carry-position mode is precisely the canonical averaged-carry
resolvent channel, after the exact local-Euler source is inserted.

For every off-line zeta zero, (O-32402.4) retains the pole moat of `L-32402`.
It is therefore not a harmless average which can be discarded.

## 3. Exact real-variable formula

Using the generalized-Chebyshev state of `L-32402`,

\[
 \boxed{
 \begin{aligned}
 \sqrt X\,\overline{\mathfrak P}_\lambda(\log X)
 ={}&C_\lambda(X)
  -{2\over X}\int_0^X C_\lambda(y)dy.
 \end{aligned}}
\tag{O-32402.5}
\]

This follows simply by integrating

\[
 C_\lambda(X)-C_\lambda(\theta X)-C_\lambda((1-\theta)X)
\]

over `theta`. At `lambda=1`,

\[
 C_1(x)=\psi(x)-\psi(x/2)+\log2
\]

for `x>=2`, so the mean mode is one explicit parabolic Riesz discrepancy of the
dyadic Chebyshev shell.

## 4. Orthogonal energy split

For every endpoint,

\[
 \boxed{
 \int_0^1|\mathfrak P_{\lambda,\theta}|^2d\theta
 =|\overline{\mathfrak P}_\lambda|^2
  +\int_0^1
   |\mathfrak P_{\lambda,\theta}
     -\overline{\mathfrak P}_\lambda|^2d\theta.
 }
\tag{O-32402.6}
\]

Both terms are nonnegative. Therefore any subexponential theorem for the full
Brownian energy must in particular prove the same rate for the canonical scalar
carry-resolvent mode.

This identifies the principal state in `NTBR`: it is the constant-`theta` mode.
The transverse mean-zero carry-position sector is where strict Selberg/frame
reserves may legitimately act.

## 5. Consequence for the repository-wide proof graph

The following objects are different coordinates of the same principal channel:

```text
uniform atomized carry average;
canonical continuum carry kernel b(x);
parabolic Riesz/Chebyshev shell discrepancy;
constant-theta component of the two-contact Brownian field;
```

whereas the mean-zero theta sector is additional positive transverse energy.

This explains both sides of the recent scope corrections:

- a strict contraction of the **complete** field is overstrong because the
  principal source contains critical neutral modes;
- proving only transverse positivity cannot establish RH, because the constant
  mode already retains every off-line pole.

## 6. Proof boundary

This is an exact identification and orthogonal decomposition. It does not bound
the principal scalar, prove `NTBR`, or prove RH.