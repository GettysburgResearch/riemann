# R-20202 — The terminal-flat dilation filter has the opposite RH sign

Claim ID: `R-20202`  
Title: The proposed prime-positive terminal-flat filter is RH-nonpositive, not RH-nonnegative  
Status: **PROVED EXACT REFUTATION / SCOPE CORRECTION**  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Dependencies: elementary trigonometry and the definitions of `T-20203/T-20204`  
Scope: refutes the sign assertion in `T-20204` and the resulting nonnegative compact-cell criterion in `T-20205`

## 1. The proposed filter

For an integer `r>=2`, write

\[
 d_r(x)=r^2(1-\cos x)-(1-\cos rx)
\]

for the spectral summand of the RH-nonnegative dilation defect

\[
 \mathcal D_r(t)=r^2\Psi(t)-\Psi(rt).
\]

The terminal-flat draft defined, for `M>=2`,

\[
 \mathfrak F_{r,M}(t)
 =\mathcal D_r(t)-M^{-2}\mathcal D_{Mr}(t)
\]

and claimed that its spectral multiplier

\[
 f_{r,M}(x)=d_r(x)-M^{-2}d_{Mr}(x)
\]

was nonnegative. The inequality is reversed.

## 2. Exact sign

Direct cancellation gives

\[
\begin{aligned}
 M^{-2}d_{Mr}(x)-d_r(x)
 &=1-\cos(rx)-M^{-2}(1-\cos(Mrx)).
\end{aligned}
\]

Using

\[
 |\sin(Mu)|\le M|\sin u|
\]

with `u=rx/2`,

\[
 1-\cos(Mrx)
 =2\sin^2(Mrx/2)
 \le M^2\,2\sin^2(rx/2)
 =M^2(1-\cos rx).
\]

Hence

\[
\boxed{
 M^{-2}d_{Mr}(x)-d_r(x)\ge0,
}
\]

or equivalently

\[
\boxed{
 d_r(x)-M^{-2}d_{Mr}(x)\le0
 \qquad(x\in\mathbb R).
}
\]

The sign is strict for generic `x`. For example, with `r=M=2` and `x=pi/2`,

\[
 d_2(\pi/2)-\frac14d_4(\pi/2)=2-4=-2.
\]

Near zero,

\[
 d_r(x)-M^{-2}d_{Mr}(x)
 =-\frac{(M^2-1)r^4}{24}x^4+O(x^6),
\]

which independently fixes the orientation.

## 3. Function-level collapse

The same correction is visible without the zero expansion:

\[
\begin{aligned}
 \mathfrak F_{r,M}(t)
 &=\bigl(r^2\Psi(t)-\Psi(rt)\bigr)
   -M^{-2}\bigl(M^2r^2\Psi(t)-\Psi(Mrt)\bigr)\\
 &=-\Psi(rt)+M^{-2}\Psi(Mrt)\\
 &=-M^{-2}\mathcal D_M(rt).
\end{aligned}
\]

Therefore under RH,

\[
\boxed{
 \mathfrak F_{r,M}(t)\le0,
}
\]

not `>=0`. The correctly oriented RH-nonnegative quantity is

\[
 M^{-2}\mathcal D_{Mr}(t)-\mathcal D_r(t)
 =M^{-2}\mathcal D_M(rt)\ge0.
\]

This is merely the already-known `M`-adic defect at the rescaled argument; it is not a new terminal-flat family.

## 4. Consequences for the branch

1. `T-20204` is refuted as stated. Its claimed spectral nonnegativity and pole-descent criterion use the wrong orientation.
2. `T-20205` is refuted as a nonnegative compact-cell RH criterion. The exact prime formula belongs to an RH-**nonpositive** quantity.
3. `L-20206` may be retained only as an exact arithmetic identity with the corrected sign interpretation.
4. `L-20207` may be retained only as a cellwise concavity identity. Concavity locates minima at cell endpoints, whereas the corrected proof obligation is an **upper** bound; maxima can occur at interior stationary points. The advertised knot-only reduction does not survive.
5. The prime-positive coefficients in `L-20206` do not provide free RH positivity. They appear precisely because the whole statistic has been oriented opposite to the RH-positive screw square.

## 5. Status boundary

This refutation does not affect:

- `T-20201`, the dyadic Haar criterion;
- `T-20203`, the general `r`-adic dilation-defect criterion;
- `L-20202`, the exact prime formula for `D_r`;
- `L-20203`, the Chebyshev/Riesz reorganization;
- `L-20204`, the Fejer/Gram factorization.

It blocks only the signed terminal-flat continuation and every theorem that imports its incorrect nonnegative orientation.
