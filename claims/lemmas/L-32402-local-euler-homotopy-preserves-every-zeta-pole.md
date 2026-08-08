# L-32402 — A local-Euler homotopy preserves every off-line zeta pole

Claim ID: `L-32402`  
Title: The ordinary and two-contact atomized Jensen fields lie in one positive dyadic Dirichlet family whose pole residue has a uniform open-strip moat  
Status: **PROPOSED COMPLETE EXACT ANALYTIC/FINITE LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: `L-32401`; PR #302 `L-28011`; elementary Euler products  
Scope: exact deformation and pole preservation; no energy estimate or RH claim

## 1. One real local-Euler parameter

Fix

\[
 0\le\lambda\le1.
\]

Define

\[
 \boxed{
 B_\lambda(s)={1-\lambda2^{-s}\over\zeta(s)},
 \qquad
 A_\lambda(s)={\zeta(s)\over1-\lambda2^{-s}}.
 }
\tag{L-32402.1}
\]

The coefficient sequence of `B_lambda` is

\[
 \boxed{
 b_\lambda=(\varepsilon-\lambda\delta_2)*\mu,
 }
\tag{L-32402.2}
\]

while the coefficients of `A_lambda` are

\[
 \boxed{
 a_\lambda(n)=\sum_{r=0}^{v_2(n)}\lambda^r>0.
 }
\tag{L-32402.3}
\]

Thus the whole path remains inside a positive inverse Dirichlet system. Its
generalized-prime coefficients are

\[
 \boxed{
 \Lambda_\lambda(n)
 =\Lambda(n)
  +(\log2)\sum_{r\ge1}\lambda^r\mathbf1_{n=2^r}
 \ge0.
 }
\tag{L-32402.4}
\]

The endpoints are

```text
lambda=0:  A_0=zeta, B_0=1/zeta;
lambda=1:  A_1=zeta/(1-2^-s), B_1=(1-2^-s)/zeta.
```

## 2. Exact finite carry atom

Because

\[
 \mathbf1*b_\lambda=\varepsilon-\lambda\delta_2,
\tag{L-32402.5}
\]

the source-convolved atomized carry row has the closed form

\[
 \boxed{
 Y^{(\lambda)}_{X,m}(\theta)
 =J_{m/X}(\theta)-\lambda J_{2m/X}(\theta),
 }
\tag{L-32402.6}
\]

with the centered interval `J` of `L-32401`.

Define the physical field

\[
 \boxed{
 \mathfrak P_{\lambda,\theta}(\log X)
 ={1\over\sqrt X}
 \sum_{m\le X}\Lambda_\lambda(m)
 Y^{(\lambda)}_{X,m}(\theta).
 }
\tag{L-32402.7}
\]

This is one finite prime-power sum at every endpoint and every `lambda`.

## 3. Exact generalized-Chebyshev state

Put

\[
 \Psi_\lambda(x)=\sum_{m\le x}\Lambda_\lambda(m).
\]

If `R=floor(log_2 x)`, then

\[
 \Psi_\lambda(x)
 =\psi(x)+(\log2)\sum_{r=1}^{R}\lambda^r.
\tag{L-32402.8}
\]

The source-convolved state is

\[
 C_\lambda(x)=\Psi_\lambda(x)-\lambda\Psi_\lambda(x/2).
\tag{L-32402.9}
\]

For every `x>=2`, the finite geometric sums telescope:

\[
 \boxed{
 C_\lambda(x)
 =\psi(x)-\lambda\psi(x/2)+\lambda\log2.
 }
\tag{L-32402.10}
\]

Consequently

\[
 \boxed{
 \sqrt X\,\mathfrak P_{\lambda,\theta}(\log X)
 =C_\lambda(X)
  -C_\lambda(\theta X)
  -C_\lambda((1-\theta)X),
 }
\tag{L-32402.11}
\]

with the obvious exact small-argument convention inherited from (L-32402.9).
The linear density

\[
 x-\lambda x/2
\]

has zero Jensen defect, so every field in the homotopy is centered before any
asymptotic estimate.

## 4. Transform and pole residue

Let

\[
 N_\theta(s)={1-\theta^s-(1-\theta)^s\over s}.
\]

The atomized carry transform is `zeta(s) N_theta(s)`. Multiplication by the
inverse source and the generalized-prime series gives

\[
 \boxed{
 \widehat{\mathfrak P_{\lambda,\theta}}(z)
 =(1-\lambda2^{-s})N_\theta(s)L_\lambda(s),
 \qquad s=z+\frac12,
 }
\tag{L-32402.12}
\]

where

\[
 L_\lambda=-{A_\lambda'\over A_\lambda}
 =-{\zeta'\over\zeta}
  +(\log2){\lambda2^{-s}\over1-\lambda2^{-s}}.
\tag{L-32402.13}
\]

If `rho` is a nontrivial zeta zero of multiplicity `m_rho`, the local Euler term
in (L-32402.13) is analytic and

\[
 \boxed{
 \operatorname*{Res}_{s=\rho}
 [(1-\lambda2^{-s})N_\theta(s)L_\lambda(s)]
 =-m_\rho(1-\lambda2^{-\rho})N_\theta(\rho).
 }
\tag{L-32402.14}
\]

For `Re rho>1/2`,

\[
 \boxed{
 |1-\lambda2^{-\rho}|
 \ge1-2^{-\operatorname{Re}\rho}
 >1-2^{-1/2}.
 }
\tag{L-32402.15}
\]

Thus the entire homotopy has one uniform local-Euler pole moat. No value of
`lambda in [0,1]` can cancel an off-line zeta zero.

## 5. Vector residue in the carry-position variable

Fix any balanced interval

\[
 I_\eta=[\eta,1-\eta],
 \qquad0<\eta<\frac12.
\]

For every nontrivial `rho`, the analytic function `theta -> N_theta(rho)` is not
identically zero on `I_eta`; otherwise analytic continuation in `theta` would
force the impossible identity

\[
 1-\theta^\rho-(1-\theta)^\rho\equiv0
\]

with `rho!=1`. Hence

\[
 \int_{I_\eta}|N_\theta(\rho)|^2d\theta>0.
\tag{L-32402.16}
\]

Together with (L-32402.15), the `L^2(I_eta)` residue norm of every hypothetical
off-line zero is bounded away from zero uniformly in the local parameter
`lambda` once the zero is fixed.

## 6. Fixed-lambda RH criterion

For every fixed `lambda in [0,1]`, define

\[
 \mathscr E_{\lambda,\eta}(J)
 =\int_J^{J+1}\int_{I_\eta}
 |\mathfrak P_{\lambda,\theta}(t)|^2d\theta dt.
\tag{L-32402.17}
\]

The standard vector-valued Laplace argument used on PR #302 gives

\[
 \boxed{
 \mathrm{RH}
 \iff
 \mathscr E_{\lambda,\eta}(J)=e^{o(J)}
 }
\tag{L-32402.18}
\]

for each fixed `lambda`. The reverse direction uses (L-32402.14)--
(L-32402.16); the forward direction is the classical square-root Chebyshev
error under RH.

Equation (L-32402.18) is a criterion, not an unconditional energy bound.

## 7. Strategic consequence

The ordinary Chebyshev Jensen field (`lambda=0`) and the exact two-contact field
(`lambda=1`) are not different RH mechanisms. They are endpoints of a
pole-preserving positive Dirichlet homotopy. Therefore a successful proof may
optimize the local dyadic Euler factor for finite geometry without risking loss
of the RH mode, provided the parameter remains in the declared compact range and
all source terms are transformed consistently.

Conversely, merely finding a convenient `lambda` does not prove RH: every fixed
member retains the full off-line pole obstruction.

## 8. Proof boundary

Closed exactly here, subject to review:

- the positive local-Euler Dirichlet family;
- the finite carry atom for every parameter;
- the closed generalized-Chebyshev formula;
- uniform preservation of every off-line zeta pole;
- the fixed-parameter vector-valued RH criterion.

Open:

- an unconditional subexponential energy bound for any one member;
- a source-complete adaptive-parameter theorem;
- RH.