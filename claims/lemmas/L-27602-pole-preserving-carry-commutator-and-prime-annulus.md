# L-27602 — Pole-preserving carry commutator and prime-annulus identity

Claim ID: `L-27602`  
Title: The first logarithmic commutator of the averaged carry kernel is exactly one compact generalized-prime output and one explicit top-quarter prime contrast  
Status: **PROPOSED COMPLETE EXACT ANALYTIC/ARITHMETIC LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-08`  
Created: 2026-08-08  
Dependencies: `L-27601`; PR #269 `L-26903/L-26904`; elementary convolution commutators  
Scope: exact pole-preserving boundary construction; no subpower estimate and no RH conclusion

## 1. Generalized-prime measure

Let

\[
 A_\omega(\sigma)=\Omega(\sigma)^{-1}
 =\frac{\zeta(\sigma)}{E(\sigma)}
\]

and define

\[
 \mathcal L_\omega(\sigma)
 =-\frac{A_\omega'}{A_\omega}(\sigma)
 =\frac{\Omega'}{\Omega}(\sigma).
\tag{L-27602.1}
\]

Its coefficient measure is

\[
 \lambda_\omega
 =\sum_{q\ge1}
  \frac{\Lambda_\omega(q)}{\sqrt q}\,
  \delta_{\log q},
\tag{L-27602.2}
\]

where

\[
\boxed{
 \Lambda_\omega(q)
 =\Lambda(q)
  +(\log2)(1+2^{-r})\mathbf1_{q=2^r}
 \ge0.
}
\tag{L-27602.3}
\]

## 2. First logarithmic commutator

Let `U` denote multiplication by the logarithmic variable:

\[
 (Uf)(u)=u f(u).
\]

Define the averaged carry commutator state

\[
\boxed{
 \mathcal C_\omega
 =\beta_\omega*(Uk).
}
\tag{L-27602.4}
\]

Put `Z=widehat z_omega=Omega K`. Since the Laplace transform of `Uk` is `-K'`,

\[
 \widehat{\mathcal C_\omega}(z)
 =-\Omega(\sigma)K'(z).
\tag{L-27602.5}
\]

Differentiating `Z=Omega K` gives the exact commutator identity

\[
\boxed{
 -\Omega K'
 =-Z'
  +\frac{\Omega'}\Omega Z.
}
\tag{L-27602.6}
\]

Returning to physical convolution,

\[
\boxed{
 \mathcal C_\omega
 =U z_\omega
  +\lambda_\omega*z_\omega.
}
\tag{L-27602.7}
\]

Thus the missing boundary of `T-26903` is not an abstract complement:

```text
first logarithmic carry commutator
 = explicit compact coordinate
   + generalized-prime output through the compact omega-wavelet.
```

For `u>2log2`, the compact coordinate vanishes and only the prime output remains.

## 3. Every zeta zero survives with a simple pole

Write

\[
 R(\sigma)=\frac{\sigma-1}{\sigma(\sigma+1)}.
\]

Since `K=zeta R` and `Omega=E/zeta`, equation (L-27602.5) becomes

\[
\boxed{
 \widehat{\mathcal C_\omega}(z)
 =-E(\sigma)R(\sigma)
   \frac{\zeta'}{\zeta}(\sigma)
  -E(\sigma)R'(\sigma).
}
\tag{L-27602.8}
\]

Let `rho` be a nontrivial zeta zero of multiplicity `m_rho`. Then

\[
 \frac{\zeta'}\zeta(\sigma)
 =\frac{m_\rho}{\sigma-\rho}+O(1).
\]

The factors `E(rho)` and `R(rho)` are nonzero for every nontrivial zero. Consequently

\[
\boxed{
 \operatorname*{Res}_{z=\rho-1/2}
 \widehat{\mathcal C_\omega}(z)
 =-m_\rho E(\rho)R(\rho)\ne0.
}
\tag{L-27602.9}
\]

The first commutator therefore retains every zero as a simple pole, irrespective of its multiplicity. This is the minimal correction to the pole-canceling zeroth carry window.

## 4. Exact top-quarter generalized-prime statistic

Let `X=e^t>4`. Since `z_omega(t)=0`, equation (L-27602.7) gives

\[
 \mathcal C_\omega(\log X)
 =\sum_{q\le X}
  \frac{\Lambda_\omega(q)}{\sqrt q}
  z_\omega\!\left(\log\frac Xq\right).
\tag{L-27602.10}
\]

Using the two pieces in `L-27601.14` gives the exact finite formula

\[
\boxed{
\begin{aligned}
 \mathcal C_\omega(\log X)
 =\frac1{\sqrt X}\Bigg[&
 \sum_{X/2<q\le X}
 \Lambda_\omega(q)
 \left(\frac{2q}{X}-1\right)\\
 &+\sum_{X/4<q\le X/2}
 \Lambda_\omega(q)
 \left(\frac12-\frac{4q}{X}\right)
 \Bigg].
\end{aligned}}
\tag{L-27602.11}
\]

The endpoint `q=X/2` belongs to the second band; `q=X/4` contributes zero.

This is one fixed top-quarter statistic. It includes every ordinary prime power and the explicit dyadic generalized-prime correction.

## 5. Exact finite commutator identity

For integer `X>=5`, put

\[
 b_X(n)
 =b(X/n)
 =\frac{k[n(k+1)-X]}X,
 \qquad k=\lfloor X/n\rfloor.
\tag{L-27602.12}
\]

Let `ell` be any completely additive formal logarithm. Then the exact finite identity is

\[
\boxed{
\begin{aligned}
&\sum_{n\le X}
 \omega_2(n)
 [\ell(X)-\ell(n)]
 b_X(n)\\
&=\sum_{X/2<q\le X}
 \Lambda_\omega(q)
 \left(\frac{2q}{X}-1\right)
 +\sum_{X/4<q\le X/2}
 \Lambda_\omega(q)
 \left(\frac12-\frac{4q}{X}\right).
\end{aligned}}
\tag{L-27602.13}
\]

Here

\[
 \Lambda_\omega
 =\omega_2*(a_\omega\ell).
\]

Thus (L-27602.11) is not merely transform algebra: it is a coefficientwise finite identity.

## 6. Second commutator and the Selberg forcing

Define

\[
 C_\omega
 =\omega_2*(a_\omega\log^2)
 =\Lambda_\omega\log
  +\Lambda_\omega*\Lambda_\omega
 \ge0.
\tag{L-27602.14}
\]

Conjugating the second logarithmic moment gives

\[
\boxed{
 \beta_\omega*(U^2k)
 =U^2z_\omega
  +2\lambda_\omega*(Uz_\omega)
  +C_\omega*z_\omega.
}
\tag{L-27602.15}
\]

Indeed, in Laplace variables,

\[
 \Omega(-\partial_z)^2\Omega^{-1}
 =(-\partial_z+\mathcal L_\omega)^2,
\]

and the zeroth-order coefficient is

\[
 -\mathcal L_\omega'
 +\mathcal L_\omega^2,
\]

the generalized Selberg sequence.

For integer `X>=5`, (L-27602.15) becomes the exact finite identity

\[
\boxed{
\begin{aligned}
&\sum_{n\le X}
 \omega_2(n)
 [\ell(X)-\ell(n)]^2b_X(n)\\
&=\sum_{q\le X}
 \Bigl[
 2\Lambda_\omega(q)(\ell(X)-\ell(q))
 +C_\omega(q)
 \Bigr]W_X(q),
\end{aligned}}
\tag{L-27602.16}
\]

where

\[
 W_X(q)=
 \begin{cases}
  2q/X-1,&X/2<q\le X,\\
  1/2-4q/X,&X/4<q\le X/2,\\
  0,&q\le X/4.
 \end{cases}
\tag{L-27602.17}
\]

This is the exact boundary/Selberg bridge: the first commutator is RH-sensitive, while the next commutator contains the coefficientwise nonnegative Selberg forcing on the same fixed annulus.

## 7. Dyadic difference form

Let

\[
 A_\omega(X)=\sum_{q\le X}\Lambda_\omega(q),
 \qquad
 B_\omega(X)=\sum_{q\le X}q\Lambda_\omega(q),
\]

and

\[
 G_\omega(X)=\frac{2B_\omega(X)}X-A_\omega(X).
\]

Then (L-27602.11) is equivalently

\[
\boxed{
 \sqrt X\,\mathcal C_\omega(\log X)
 =G_\omega(X)
  -\frac32G_\omega(X/2)
  +\frac12G_\omega(X/4),
}
\tag{L-27602.18}
\]

with the natural floor convention. The same opposite-parity polynomial reappears in the local prime-density error.

## 8. Proof boundary

Closed exactly, subject to review:

- the first pole-preserving commutator;
- noncancellation at every zero and every multiplicity;
- the compact generalized-prime representation;
- the top-quarter finite formula;
- the second commutator/Selberg tower;
- the dyadic density-error form.

Open:

- a subpower pointwise or local-energy estimate for (L-27602.11);
- a recurrence exploiting (L-27602.15);
- RH.
