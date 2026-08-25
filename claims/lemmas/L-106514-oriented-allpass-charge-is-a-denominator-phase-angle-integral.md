# L-106514 — Oriented all-pass charge is a denominator phase-angle integral

Claim ID: `L-106514`  
Status: **PROVED EXACT FOR CANONICALLY NORMALIZED FINITE INNER QUOTIENTS**  
Created: 2026-08-25  
Depends on: `L-106507`, `L-106512`; the finite model-space trace/residue identity  
RH status: **not assumed**

Let `B_+,B_-` be finite upper-half-plane inner functions canonically
normalized by

\[
B_+(\infty)=B_-(\infty)=1,
\]

and put

\[
U={B_+\over B_-}=B_+\overline{B_-}
\]

on the compactified real boundary.  Write

\[
B_-(t)=e^{i\beta(t)},
\qquad
\beta'(t)\ge0,
\qquad
{1\over2\pi}\int_{\mathbb R}\beta'(t)dt=m_-.
\]

## 1. Cross Dirichlet trace

The finite model-space trace identity is

\[
\boxed{
\operatorname{tr}(P_{K_{B_-}}P_{K_{B_+}})
=\langle B_+,B_-\rangle_{\mathcal D}
={1\over2\pi i}\int_{\mathbb R}{B_+'(t)\over B_-(t)}dt.
}
\tag{L-106514.1}

The quantity is real and nonnegative under the normalization at infinity.
For simple zeros it is equivalently

\[
\sum_{B_-(c)=0}{B_+'(c)\over B_-'(c)},
\]

and the confluent statement is obtained by the usual derivative blocks.
Equation (L-106514.1) follows either from the normalized Cauchy-Gram formula
of `L-106512` or from a Takenaka--Malmquist trace expansion followed by
residues.

## 2. Oriented phase-angle identity

Since

\[
\beta'={1\over i}{B_-'\over B_-}
\]

on the real boundary,

\[
{1\over2\pi}\int \beta' U\,dt
={1\over2\pi i}\int {B_+B_-'\over B_-^2}dt.
\]

The derivative of `B_+/B_-` integrates to zero on the compactified boundary,
so integration by parts gives

\[
{1\over2\pi}\int \beta' U\,dt
={1\over2\pi i}\int {B_+'\over B_-}dt.
\]

Combining this with `L-106512.1` yields

\[
\boxed{
\|H_U\|_{\mathcal S_2}^2
={1\over2\pi}\int_{\mathbb R}
\beta'(t)\left(1-\operatorname{Re}U(t)\right)dt.
}
\tag{L-106514.2}

Because `|U|=1`,

\[
\boxed{
\|H_U\|_{\mathcal S_2}^2
={1\over4\pi}\int_{\mathbb R}
\beta'(t)|1-U(t)|^2dt.
}
\tag{L-106514.3}

This is exact and sharply oriented: only the denominator inner phase density
is charged.

## 3. Endpoint Wronskian form

For the odd endpoint quotient of `L-106501`, normalized at infinity,

\[
|1-U_{K,\lambda}|^2
={4\lambda^2\mathcal L_K^2
 \over
(F^2+\lambda^2F'^2)
((F^{(K)})^2+\lambda^2(F^{(K+1)})^2)}.
\]

If `beta_(K,lambda)'` is the phase density of the reduced denominator inner
factor, then

\[
\boxed{
\|H_{U_{K,\lambda}}\|_{\mathcal S_2}^2
={\lambda^2\over\pi}\int_{
\mathbb R}
\beta_{K,\lambda}'(t)
{\mathcal L_K(t)^2
 \over
(F^2+\lambda^2F'^2)
((F^{(K)})^2+\lambda^2(F^{(K+1)})^2)}dt.
}
\tag{L-106514.4}

Common factors are reduced before `beta'` is formed.

## 4. Relation to the outer Dirichlet defect

Applying (L-106514.3) to `U` and `U^{-1}` gives the exact decomposition

\[
\boxed{
\|B_+-B_-\|_{\mathcal D}^2
=\|H_U\|_{\mathcal S_2}^2
 +\|H_{U^{-1}}\|_{\mathcal S_2}^2.
}
\tag{L-106514.5}

Thus `L-106507` is topology safe but pays both the adverse and favorable
oriented charges.  Equation (L-106514.4) is the sharp conclusion-facing
scalar.

## 5. Scope

No estimate of the positive integral (L-106514.4) is asserted.  The theorem
only removes the matrix notation and the favorable-inner floor.  Entire Xi
passage retains the regular-window, common-zero, confluent and endpoint
ledger.
