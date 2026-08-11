# L-91020 — The boundary generalized-Jordan multiplier is a correlation channel and contracts negative trace mass

Claim ID: `L-91020`  
Status: **PROPOSED COMPLETE EXACT OPERATOR THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-91014`, `L-91015`  
RH status: **unproved**

## 1. Boundary multiplier

For `a>0`, let

\[
 R_a=Q_a(1+2a)
\]

and define

\[
 \boxed{
 M_a(\theta)
 =\frac{Q_a(1+2a+i\theta)}{Q_a(1+2a)}.
 }
 \tag{L-91020.1}
\]

Under the anchor law of `L-91019`,

\[
 \boxed{
 M_a(\theta)
 =\mathbb E_a[e^{-i\theta T}],
 \qquad T=\log n.
 }
 \tag{L-91020.2}
\]

Thus `M_a` is a continuous positive-definite function,

\[
 M_a(0)=1,
 \qquad |M_a(\theta)|\le1.
 \tag{L-91020.3}
\]

Since both zeta factors in (L-91020.1) lie in `Re(s)>1`,

\[
 \boxed{M_a(\theta)\ne0\quad(\theta\in\mathbb R).}
 \tag{L-91020.4}
\]

## 2. Schur correlation channel

For carriers `x_1,...,x_N`, put

\[
 C_a=(M_a(x_j-x_k))_{j,k=1}^N.
 \tag{L-91020.5}
\]

Then

\[
 C_a\succeq0,
 \qquad (C_a)_{jj}=1.
 \tag{L-91020.6}
\]

The Schur multiplier

\[
 \boxed{
 \Phi_a(X)=C_a\circ X
 }
 \tag{L-91020.7}
\]

is completely positive, unital and trace preserving.

An explicit random-unitary Stinespring representation is

\[
 \boxed{
 \Phi_a(X)
 =\mathbb E_a[D_T X D_T^*],
 \qquad
 D_T=\operatorname{diag}(e^{-ix_1T},...,e^{-ix_NT}).
 }
 \tag{L-91020.8}
\]

## 3. Negative trace mass contracts

For Hermitian `X`, let `X_-` denote its negative part.  Then

\[
 \boxed{
 \operatorname{tr}(\Phi_a(X)_-)
 \le\operatorname{tr}(X_-).
 }
 \tag{L-91020.9}
\]

Indeed,

\[
 \operatorname{tr}(Y_-)
 =\max_{0\preceq P\preceq I}-\operatorname{tr}(PY),
\]

and the adjoint of `Phi_a` is positive and unital.  Therefore

\[
\begin{aligned}
 \operatorname{tr}(\Phi_a(X)_-)
 &=\max_{0\le P\le I}-\operatorname{tr}(\Phi_a^*(P)X)\\
 &\le\operatorname{tr}(X_-).
\end{aligned}
\]

The same statement holds for trace-class Hermitian kernels by finite-rank
approximation.

## 4. Strict positivity of finite carrier Grams

Because the anchor support contains `1` and all primes, the functions
`e^(-ix_j T)` are linearly independent in `L^2(P_a)` for distinct carriers,
using rational independence of the prime logarithms. Hence

\[
 \boxed{C_a\succ0}
 \tag{L-91020.10}
\]

for every finite set of distinct carriers.

In particular the channel does not erase a pure hyperbolic block with zero
diagonal: Schur multiplication scales its off-diagonal entry by a nonzero
number and preserves one positive and one negative eigenvalue.

## 5. Exact relation to the pole-subtracted recurrence

On the critical boundary `s=1+i theta`, the inherited multiplier in
`L-91015.12` is exactly `M_a(theta)`. Thus the inherited finite carrier block is
transported by the correlation channel `Phi_a`; the emitted tail block is the
positive Gram of `L-91018`.

This gives the exact operator orientation

```text
inherited signed block -> CP correlation channel
new forcing            -> positive direct emission.
```

## 6. Scope firewall

Negative-mass contraction is a forward statement. By itself it does **not**
allow positivity at a large scale to be pulled backward to a smaller scale.
Any complete coefficient-one proof must retain the Stinespring environment and
show that the complementary two-port output is exactly the physical Cauchy
detail, or provide another no-loss index argument.

Thus (L-91020.9) closes the generic inertia estimate but not the conclusion-
producing recurrence.

## 7. Boundary

Closed:

```text
boundary multiplier is an anchor characteristic function;
finite carrier matrices are correlation matrices;
complete positivity, unitality and trace preservation;
negative trace-mass contraction;
strict finite-carrier positivity and non-erasure of pure hyperbolic blocks.
```

Open:

```text
lossless identification of the Stinespring complement with physical details;
backward/index recurrence;
RH.
```
