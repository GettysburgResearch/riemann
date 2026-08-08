# L-27603 — Ordinary-prime annulus and deterministic commutator gauge

Claim ID: `L-27603`  
Title: The pole-preserving commutator differs from one ordinary-prime top-quarter wavelet only by an explicit exponentially decaying gauge  
Status: **PROPOSED COMPLETE EXACT ANALYTIC LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-08`  
Created: 2026-08-08  
Dependencies: `L-27601`, `L-27602`  
Scope: exact reduction to the ordinary von Mangoldt sequence; no asymptotic estimate and no RH conclusion

## 1. Ordinary-prime wavelet output

Let

\[
 \lambda
 =\sum_{q\ge1}\frac{\Lambda(q)}{\sqrt q}\delta_{\log q}
\]

and retain the compact two-band kernel `z_omega` of `L-27601`. Define

\[
\boxed{
 \mathcal P_\omega=\lambda*z_\omega.
}
\tag{L-27603.1}
\]

Its Laplace transform is

\[
\boxed{
 \widehat{\mathcal P_\omega}(z)
 =-E(\sigma)R(\sigma)
   \frac{\zeta'}\zeta(\sigma),
 \qquad
 \sigma=z+\frac12,
}
\tag{L-27603.2}
\]

where

\[
 E(\sigma)=(1-2^{-\sigma})(1-2^{-\sigma-1}),
 \qquad
 R(\sigma)=\frac{\sigma-1}{\sigma(\sigma+1)}.
\]

Every nontrivial zero of `zeta` remains an uncancelled pole.

## 2. Exact ordinary-prime top-quarter formula

For `X=e^t>4`, compact support gives

\[
\boxed{
\begin{aligned}
 \mathcal P_\omega(\log X)
 =\frac1{\sqrt X}\Bigg[&
 \sum_{X/2<q\le X}
 \Lambda(q)\left(\frac{2q}{X}-1\right)\\
 &+\sum_{X/4<q\le X/2}
 \Lambda(q)\left(\frac12-\frac{4q}{X}\right)
 \Bigg].
\end{aligned}}
\tag{L-27603.3}
\]

Thus the complete RH-sensitive boundary is a fixed ordinary-prime-power contrast on one top-quarter annulus. No generalized coefficient, carry inverse, or infinite packet is required to state it.

## 3. Relation to the first carry commutator

Let `C_omega` be the first logarithmic commutator of `L-27602`. Its transform is

\[
 \widehat{\mathcal C_\omega}
 =-E R\frac{\zeta'}\zeta-ER'.
\]

Therefore

\[
\boxed{
 \mathcal C_\omega
 =\mathcal P_\omega-d_E,
}
\tag{L-27603.4}
\]

where `d_E` is the explicit causal function with transform `E(sigma)R'(sigma)`.

Put `L=log 2` and

\[
 h(u)=u e^{-u/2}-2u e^{-3u/2}.
\]

Then

\[
\boxed{
 d_E
 =\left(
 I-\frac{3}{2\sqrt2}\tau_L
 +\frac14\tau_{2L}
 \right)h.
}
\tag{L-27603.5}
\]

In particular, for `u>=2L`,

\[
\boxed{
 d_E(u)
 =\frac L2e^{-u/2}+2Le^{-3u/2}.
}
\tag{L-27603.6}
\]

Hence `d_E` is elementary and exponentially decaying. Any subexponential or subpower estimate for `C_omega` is equivalent to the same estimate for `P_omega`.

## 4. Chebyshev-error form

Let

\[
 \psi(x)=\sum_{q\le x}\Lambda(q),
 \qquad
 \Psi_1(x)=\sum_{q\le x}q\Lambda(q),
\]

and put

\[
 G(x)=\frac{2\Psi_1(x)}x-\psi(x).
\tag{L-27603.7}
\]

The unnormalised bracket in (L-27603.3) is exactly

\[
\boxed{
 G(X)-\frac32G(X/2)+\frac12G(X/4).
}
\tag{L-27603.8}
\]

The smooth main density `psi(x)=x` is annihilated identically. A zero contribution `x^rho` is multiplied by

\[
 E(\rho)\frac{\rho-1}{\rho(\rho+1)},
\]

which is nonzero for every nontrivial zero. Thus the annular contrast retains the complete rightmost-zero exponent.

## 5. Proof boundary

Closed exactly, subject to review:

- reduction to ordinary von Mangoldt weights;
- top-quarter finite formula;
- explicit exponentially decaying gauge;
- Chebyshev-error dyadic difference and noncancellation factor.

Open:

- a subpower bound or local critical energy estimate for `P_omega`;
- RH.
