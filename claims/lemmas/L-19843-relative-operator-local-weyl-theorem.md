# L-19843 — Relative operator local-Weyl theorem on a cofinal support sequence

Claim ID: `L-19843`  
Status: **PROPOSED COMPLETE OPERATOR THEOREM, DEPENDENT ON THE CORRECTED MODE-DEPENDENT PROFILE THEOREM `L-19844/L-19845`**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-07  
Dependencies: exact radical-tail zero-side factorization; `L-19844` mode-dependent holomorphic Airy/alias theorem; `L-19845` polylogarithmic endpoint selection; abstract Hilbert-valued support large sieve `L-16226`; standard Riemann--von Mangoldt/Stieltjes decomposition with unit-window zero counts  
Scope: theorem 4 in the repaired signed prolate programme

## 1. Statement

Let `D_R` be the complete ordinary Poisson-tail Gram in the common signed
coefficient metric and let `A_R` be the exact localized Weil matrix obtained
from the same exact-radical frame. Normalize the zero-density constant into
`D_R`, so the main local density is `log R`.

For the packet dimension

\[
 m_R=O((\log R)^2),
 \tag{L-19843.1}
\]

there is, in every sufficiently large dyadic support block `[T,2T]`, a
positive-measure set `mathcal W_T` such that

\[
 \boxed{
 \eta_R:=
 \frac{
 \left\|D_R^{-1/2}
 \bigl(A_R-(\log R)D_R\bigr)
 D_R^{-1/2}\right\|
 }{\log R}
 \longrightarrow0}
 \tag{L-19843.2}
\]

uniformly for `R in mathcal W_T` as `T->infinity`.

The set may be intersected with the good source-frame, endpoint, and alias sets
of `L-19840`, `L-19844`, and `L-19845`; the intersection remains nonempty in
every large block.

No RH assumption is used. Hypothetical off-line zeros are included.

## 2. Exact branchwise zero matrix

For one exact-radical tail profile, the polarized zero kernel is

\[
 \overline{\Phi_R(\overline{s}/R)}
 \Phi_R(s/R),
 \qquad s=\gamma+i\delta,
 \qquad |\delta|<1/2.
 \tag{L-19843.3}
\]

Insert the exact mode-dependent branch decomposition of `L-19844`. The result
splits into:

1. **phase-neutral terms**, in which the same radial branch occurs on both
   sides;
2. **oscillatory branch crosses**;
3. the Airy-fold window;
4. collectively summed endpoint channels;
5. absolutely summable post-endpoint and post-alias remainders.

For a phase-neutral term, analytic continuation gives

\[
 \begin{aligned}
 &\overline{
 e^{i\epsilon R
 S_\sigma(x-i\delta/R)}}
 e^{i\epsilon R
 S_\sigma(x+i\delta/R)}\\
 &\qquad=1+O((\log R)^C/R).
 \end{aligned}
 \tag{L-19843.4}
\]

The two horizontal multipliers cancel. Thus the nonoscillatory density is the
same for a line zero and an off-line zero. Horizontal displacement survives
only in bounded branch amplitudes and oscillatory crosses.

This is the second exact cancellation missed by `L-19821`: support translation
cancels before the profile decomposition, and same-branch complex displacement
cancels inside the profile product.

## 3. Main density term

Let `mathcal B_R(u)` be the complete phase-neutral positive matrix profile after
all aliases and endpoint self-energy are included. In the normalization of
`D_R`,

\[
 D_R=\int_0^\infty\mathcal B_R(u)\,du.
 \tag{L-19843.5}
\]

The Riemann--von Mangoldt measure is

\[
 dN(t)
 =\left[\log R+\log u+c_0+O((Ru)^{-1})\right]R\,du
 +dS(t)
 \tag{L-19843.6}
\]

on `t=Ru`, with the fixed normalization constants absorbed into `D_R` and the
bounded correction matrix.

The smooth main term therefore equals

\[
 (\log R)D_R+C_R^{\rm dens},
 \tag{L-19843.7}
\]

where `L-19844/L-19845`, including collective endpoint summation, gives the
relative bound

\[
 \left\|D_R^{-1/2}C_R^{\rm dens}D_R^{-1/2}\right\|
 \le(\log R)^C
 \tag{L-19843.8}
\]

at the raw level. In fact the only nondecaying weight is `log u+c_0`, and the
first-alias normalization plus the `k^-2` ledger gives

\[
 \boxed{
 \left\|D_R^{-1/2}C_R^{\rm dens}D_R^{-1/2}\right\|
 =O(\log\log R)=o(\log R).}
 \tag{L-19843.9}
\]

The logarithm comes solely from the collectively summed leading endpoint
channel; compact radial bands contribute `O(1)`.

## 4. Stieltjes fluctuation for phase-neutral terms

For a phase-neutral amplitude matrix `B_R(u)`, integration by parts gives

\[
 \frac1R\int B_R(t/R)\,dS(t)
 =-\frac1{R^2}\int S(t)B_R'(t/R)\,dt
 +\text{boundary}.
 \tag{L-19843.10}
\]

Same-branch phase cancellation means that `B_R'` differentiates amplitudes, not
a frequency-`R` exponential. The polylogarithmic amplitude and endpoint bounds
give

\[
 \int
 \left\|D_R^{-1/2}B_R'(u)D_R^{-1/2}\right\|du
 \le(\log R)^C.
 \tag{L-19843.11}
\]

Using the unconditional bound `S(t)=O(log t)` already yields

\[
 \left\|D_R^{-1/2}E_R^{\rm neutral}D_R^{-1/2}\right\|
 \ll\frac{(\log R)^C}{R}
 =o(1).
 \tag{L-19843.12}
\]

No Selberg moment or support choice is needed for the phase-neutral part.

## 5. Oscillatory line-centered terms

Every remaining line-centered branch cross has the form

\[
 Z_R
 =\frac1R
 \sum_{\gamma\in\mathcal Z_T}
 A_\gamma(R)
 e^{iR\phi(\gamma/R)},
 \tag{L-19843.13}
\]

or an Airy/endpoint version with the same extracted real phase. The corrected
profile theorem gives

\[
 \|A_\gamma(R)\|+
 R\|\partial_RA_\gamma(R)\|
 \le(\log R)^C.
 \tag{L-19843.14}
\]

For ordinates in bins separated by `m`,

\[
 \left|\partial_R
 \{R\phi(\gamma/R)-R\phi(\gamma'/R)\}
 \right|
 \ge c\frac{m}{R}
 \tag{L-19843.15}
\]

outside the fold; the fold packet is handled by the uniform Airy estimate and
has the stronger `R^(-1/3)` factor. The unit-window zero count is
`O(log R)` with multiplicity.

The Hilbert-valued support large sieve therefore gives, after whitening by
`D_R`,

\[
 \frac1T\int_T^{2T}
 \left\|D_R^{-1/2}Z_RD_R^{-1/2}\right\|_{HS}^2dR
 \le\frac{(\log T)^C}{T^{1/3}}.
 \tag{L-19843.16}
\]

All `O(log^2 R)` packet dimensions and polynomially many branch families are
included in the exponent `C`. Hence, on a relative-`1-o(1)` support set,

\[
 \left\|D_R^{-1/2}Z_RD_R^{-1/2}\right\|=o(1).
 \tag{L-19843.17}
\]

## 6. Hypothetical off-line zeros

For `s=gamma+i delta`, the branchwise Taylor formula is

\[
 RS_\sigma(\gamma/R+i\delta/R)
 =RS_\sigma(\gamma/R)
 +i\delta S_\sigma'(\gamma/R)
 +O((\log R)^C/R).
 \tag{L-19843.18}
\]

The same-branch factors cancel by (L-19843.4). Every term in the exact-minus-
line-centered difference is therefore an oscillatory branch cross with an
amplitude satisfying (L-19843.14), or an Airy/endpoint remainder already
covered by `L-19844`.

Applying the same support large sieve gives

\[
 \frac1T\int_T^{2T}
 \left\|D_R^{-1/2}
 (A_R-A_R^{\rm line})D_R^{-1/2}ight\|_{HS}^2dR
 \le\frac{(\log T)^C}{T^{1/3}}.
 \tag{L-19843.19}
\]

Thus hypothetical horizontal displacement costs no power of `R` and is
`o(1)` at a selected support.

## 7. Endpoint and infinite-alias completion

The leading endpoint series has already been summed as

\[
 -\log(1-e^{i\vartheta_R})-e^{i\vartheta_R}.
 \tag{L-19843.20}
\]

`L-19845` makes this aggregate and one scaled support derivative
polylogarithmic on a relative-`1-o(1)` set. The remaining endpoint jets and
aliases are absolutely summable; the `k`th non-endpoint channel is
`O((log R)^C R^(-1/3)k^(-2))`.

Therefore the endpoint and infinite-alias pieces satisfy the same estimates as
Sections 4--6. Positive endpoint/rest self-energy remains inside `D_R`; only
its bounded-density correction and oscillatory crosses enter the error.

## 8. Selection and relative conclusion

Intersect the relative-`1-o(1)` sets supplied by:

- the complete alias cross moat;
- endpoint nonresonance;
- line-centered oscillatory scalarization;
- off-line branch averaging.

The intersection has positive measure in every sufficiently large block. At a
support in that intersection, Sections 3--7 give

\[
 \left\|D_R^{-1/2}
 \bigl(A_R-(\log R)D_R\bigr)
 D_R^{-1/2}\right\|
 =o(\log R).
 \tag{L-19843.21}
\]

Dividing by `log R` proves (L-19843.2).

The independent zeta-multiplier good set of `L-19840` deletes only an `o(1)`
fraction of support lengths. After converting between `ell=log R` and `R`, its
intersection with the analytic good set remains nonempty in every large radial
block.

## 9. Adversarial proof boundary

1. The normalization is relative: the error in (L-19843.2), not the unscaled
   error, is the theorem.
2. The factor `R` in the amplitude-derivative hypothesis is retained exactly.
3. Same-branch complex displacement cancels; only oscillatory crosses are
   averaged.
4. The leading endpoint channel is summed collectively before any norm.
5. The theorem uses the complete signed frame and the complete Poisson tail in
   one metric.
6. The three most load-bearing estimates for independent review are the
   phase-difference lower bound (L-19843.15), the whitened amplitude-variation
   bound (L-19843.11), and the endpoint weighted-density bound
   (L-19843.9). They are consequences of `L-19844/L-19845`, not checker inputs.
7. The theorem does not by itself identify the arithmetic frame of `L-19840`
   with the low prolate tail frame. That common-frame compatibility is the
   remaining composition issue discussed in `T-19809`.
8. No RH conclusion is claimed by this lemma alone.
