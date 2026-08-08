# L-29004 — Prime Jensen defect and exact additive-convolution energy

Claim ID: `L-29004`  
Title: The atomized pole field is the balanced Jensen defect of one dyadically filtered Chebyshev function, and its full carry-frame energy has a closed one-dimensional convolution formula  
Status: **PROPOSED COMPLETE EXACT ANALYTIC/FINITE LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-r`  
Created: 2026-08-08  
Dependencies: `L-29001`; PR #289 ordinary-prime annulus; elementary Fubini expansion  
Scope: exact scalarization of the atomized frame; no Jensen-defect estimate or RH claim

## 1. Dyadic Chebyshev contrast

Let

\[
 \psi(y)=\sum_{q\le y}\Lambda(q)
\]

with the usual real endpoint convention, and define

\[
\boxed{
 A(y)=\psi(y)-\frac32\psi(y/2)+\frac12\psi(y/4).
}
\tag{L-29004.1}

Equivalently, using the wavelet of `L-29001`,

\[
\boxed{
 A(y)=\sum_{m\le y}\Lambda(m)g_m(y),
 \qquad
 g_m=\mathbf1_{[m,2m)}-\frac12\mathbf1_{[2m,4m)}.
}
\tag{L-29004.2}

The linear prime density is

\[
 A_0(y)=\frac38y.
\tag{L-29004.3}

## 2. Exact Jensen-defect identity

Equation `L-29001.22` gives, for every real `X>=1` and `0<=theta<=1`,

\[
\begin{aligned}
 \sqrt X\,\mathfrak P_\theta(\log X)
 &=\sum_m\Lambda(m)
   [g_m(X)-g_m(\theta X)-g_m((1-\theta)X)]\\
 &=A(X)-A(\theta X)-A((1-\theta)X).
\end{aligned}
\]

Thus

\[
\boxed{
 \mathfrak P_\theta(\log X)
 =X^{-1/2}
  [A(X)-A(\theta X)-A((1-\theta)X)].
}
\tag{L-29004.4}

The linear density (L-29004.3) cancels exactly. If

\[
 \widetilde A(y)=A(y)-\frac38y,
\]

then the same defect is

\[
\boxed{
 \sqrt X\,\mathfrak P_\theta(\log X)
 =\widetilde A(X)-\widetilde A(\theta X)
  -\widetilde A((1-\theta)X).
}
\tag{L-29004.5}

The full atomized RH signal is therefore an additive-stability defect of one
ordinary-prime summatory function.

## 3. Full carry-position energy

Define

\[
 \mathcal J(X)
 =\int_0^1
  |A(X)-A(\theta X)-A((1-\theta)X)|^2d\theta.
\tag{L-29004.6}

Put

\[
 I(X)=\int_0^XA(u)du,
 \qquad
 J(X)=\int_0^XA(u)^2du,
\]

and

\[
 (A*A)(X)=\int_0^XA(u)A(X-u)du.
\]

Expansion of the square and the substitution `u=theta X` give the exact identity

\[
\boxed{
 \mathcal J(X)
 =A(X)^2
  -\frac{4A(X)}X I(X)
  +\frac2XJ(X)
  +\frac2X(A*A)(X).
}
\tag{L-29004.7}

No prime estimate enters this formula. The right side is automatically
nonnegative because it is the square on the left.

For the linear model `A_0(y)=3y/8`, the four terms cancel exactly.

## 4. Balanced energy and the RH scale

For `0<eta<1/2`, put

\[
 \mathcal J_\eta(X)
 =\int_\eta^{1-\eta}
  |A(X)-A(\theta X)-A((1-\theta)X)|^2d\theta.
\tag{L-29004.8}

Then the block energy of `L-29001` is

\[
\boxed{
 \mathscr E_\eta(J)
 =\int_J^{J+1}e^{-t}\mathcal J_\eta(e^t)dt.
}
\tag{L-29004.9}

Consequently the local-energy criterion for RH is

\[
\boxed{
 \int_J^{J+1}e^{-t}\mathcal J_\eta(e^t)dt=e^{o(J)}.
}
\tag{L-29004.10}

The pointwise shorthand

\[
 \mathcal J_\eta(X)=X^{1+o(1)}
\]

is sufficient but is not asserted equivalent without an additional local
regularity argument. The block formulation (L-29004.10) is the reviewed
criterion.

This normalization is exact: an off-line zero `rho=beta+i gamma` contributes
at scale `X^(2 beta)` to `mathcal J_eta(X)` and at exponent `2 beta-1` after the
factor `X^-1`.

## 5. Connection to prime-annulus and carry programmes

Averaging (L-29004.4) over `theta` recovers the scalar top-quarter commutator on
PR #289. Squaring before averaging gives the exact carry Gram of `L-29001`.
Thus:

```text
prime-annulus scalar   = mean Jensen defect;
atomized carry energy  = mean squared Jensen defect;
carry Gram             = exact finite normal matrix of that defect.
```

The endpoint-tree recurrence of `T-29001` is a discrete arithmetic mechanism for
proving approximate additivity of `A` at the critical square-root scale.

## 6. Two possible completion interfaces

The same object now admits two equivalent proof-facing attacks.

### Carry/endpoint interface

Use `L-29002/L-29003` to pay the complete interior Selberg forcing and route the
endpoint null channel to half-scale balanced trees.

### Additive-convolution interface

Use (L-29004.7) to prove a one-sided recurrence for the centered convolution

\[
 (\widetilde A*\widetilde A)(X)
\]

and the cumulative square

\[
 \int_0^X\widetilde A(u)^2du
\]

without estimating the four large terms separately.

Taking absolute values before the linear-density cancellation loses a full
power of `X` and cannot close RH.

## 7. Proof boundary

Closed exactly, subject to review:

- dyadic Chebyshev contrast;
- atomized field as an exact Jensen defect;
- cancellation of the full linear density;
- full-position convolution-energy identity;
- equivalence with the carry-frame local energy.

Open:

- a critical bound for `mathcal J_eta`;
- either the endpoint-tree recurrence or an equivalent centered-convolution
  inequality;
- RH.