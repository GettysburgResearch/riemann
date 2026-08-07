# L-23402 — Exact divisor and prime renewal equations for a Mertens shell

Claim ID: `L-23402`  
Title: The fixed-ratio Möbius shell satisfies both a homogeneous divisor-dilation recurrence and a centered von-Mangoldt Volterra equation  
Status: **PROPOSED — COMPLETE ARITHMETIC AND MELLIN ALGEBRA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-07  
Dependencies: `L-23401`; elementary Dirichlet convolution identities  
Scope: every fixed `0<c<1`

## 1. Divisor-dilation recurrence

Retain

\[
I_c(x)=M(x)-M(cx).
\]

For every real `x>=1`, Möbius inversion gives

\[
\sum_{k\ge1}M(x/k)
=\sum_{m\le x}\sum_{d\mid m}\mu(d)
=1.
\tag{L-23402.1}
\]

If also `cx>=1`, subtracting the same identity at `cx` gives

\[
\boxed{
\sum_{k\ge1}I_c(x/k)=0.}
\tag{L-23402.2}
\]

The sum is finite because `I_c(y)=0` for `0<y<1`. Equivalently,

\[
\boxed{
I_c(x)=-\sum_{k\ge2}I_c(x/k),
\qquad x\ge c^{-1}.}
\tag{L-23402.3}
\]

This is an exact cofinal scale recurrence. It contains no asymptotic prime theorem and no error term.

For `c=2/3`, the first Farey-cell increment therefore obeys

\[
M(x)-M(2x/3)
=-\sum_{k\ge2}
\left[M(x/k)-M(2x/(3k))\right].
\tag{L-23402.4}
\]

The recurrence alone is not a contraction after absolute values: it has infinitely many positive dilation coefficients. Its value is as a source identity to be combined before Cauchy--Schwarz.

## 2. Pointwise logarithmic derivative identity

Let `Lambda` be the von Mangoldt function. The Dirichlet-series identity

\[
{d\over ds}{1\over\zeta(s)}
=\left(-{\zeta'\over\zeta}(s)\right){1\over\zeta(s)}
\]

implies, coefficient by coefficient,

\[
\boxed{
\mu(n)\log n
=-(\Lambda*\mu)(n).}
\tag{L-23402.5}
\]

Define the triangularly weighted shell

\[
\boxed{
J_c(x)=
\sum_{cx<n\le x}\mu(n)\log{x\over n}.}
\tag{L-23402.6}
\]

Then

\[
\begin{aligned}
\log x\,I_c(x)-J_c(x)
&=\sum_{cx<n\le x}\mu(n)\log n\\
&=-\sum_{cx<n\le x}(\Lambda*\mu)(n).
\end{aligned}
\]

After interchanging the finite convolution sum,

\[
\sum_{cx<n\le x}(\Lambda*\mu)(n)
=\sum_{a\le x}\Lambda(a)I_c(x/a).
\]

Therefore the shell satisfies the exact centered prime-renewal equation

\[
\boxed{
\log x\,I_c(x)
+\sum_{a\le x}\Lambda(a)I_c(x/a)
=J_c(x).}
\tag{L-23402.7}

The prime and Möbius signs have not been separated or majorized. Equation (L-23402.7) is the scalar fixed-ratio counterpart of the centered Selberg and signed Type-II packet equations in PRs #216, #219, and #165.

## 3. Physical Volterra form of the forcing

Stieltjes partial summation gives

\[
\boxed{
J_c(x)=
\int_{cx}^{x}{M(u)-M(cx)\over u}\,du.}
\tag{L-23402.8}

Indeed, the boundary values of `log(x/u)` vanish at `u=x`, while the cumulative shell sum is zero at `u=cx`.

Thus the forcing in (L-23402.7) is a one-sided triangular average of the same Möbius source. It is smoother, but it is not an external error term.

## 4. Exact Mellin transform of the triangular shell

For `Re(s)>1`, each integer `n` contributes on `n<=x<n/c`. Hence

\[
\begin{aligned}
\int_1^\infty J_c(x)x^{-s-1}dx
&=\sum_{n\ge1}{\mu(n)\over n^s}
  \int_1^{1/c}(\log y)y^{-s-1}dy\\
&={1-c^s(1+sL)\over s^2\zeta(s)},
\end{aligned}
\]

where `L=log(1/c)`. Therefore

\[
\boxed{
\int_1^\infty J_c(x)x^{-s-1}dx
={1-c^s(1+sL)\over s^2\zeta(s)}.}
\tag{L-23402.9}

Writing

\[
F_c(s)={1-c^s\over s\zeta(s)},
\]

one equivalently has

\[
\boxed{
\widehat J_c(s)
=\left[
 {1\over s}-{Lc^s\over1-c^s}
 \right]F_c(s).}
\tag{L-23402.10}

Equation (L-23402.10) is exactly the Mellin image of (L-23402.7): multiplication by `log x` becomes `-d/ds`, while convolution with `Lambda` becomes multiplication by `-zeta'/zeta`.

## 5. Balanced common-cell content

Expanding the block `L2` norm of (L-23402.7) creates:

1. the shell energy of `I_c`;
2. a signed `Lambda`--`mu` Type-II convolution;
3. its reflected prime-pair square;
4. the triangular forcing energy.

The diagonal and terminal one-free-variable pieces can be isolated by the Euler closures of PR #165. The remaining common signed balanced term is exactly the source-specific arithmetic gate, not an arbitrary operator norm.

Consequently, a proof-facing use of (L-23402.7) must preserve the complete sum

\[
\sum_a\Lambda(a)I_c(x/a)
\]

until the reflected quadratic channel has been assembled. Taking absolute values term by term returns the full parity barrier.

## 6. Proof boundary

Closed exactly:

- the divisor-dilation recurrence;
- the pointwise `mu log` convolution identity;
- the centered prime-renewal equation;
- the Volterra forcing formula;
- the Mellin transform.

Open:

- a one-sided energy estimate for (L-23402.7);
- a signed balanced Type-II contraction;
- the shell-energy bound of `T-23401`;
- RH.
