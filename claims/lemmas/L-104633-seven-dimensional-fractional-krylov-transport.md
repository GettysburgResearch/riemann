# L-104633 — A seven-dimensional fractional Krylov transport certificate

Claim ID: `L-104633`  
Status: **PROVED EXACT FINITE-MATRIX SUFFICIENT REDUCTION**  
Created: 2026-08-27  
Corrected: 2026-08-27  
Depends on: `L-104632`; carrier-free zeta-derivative packet `L-106612` at
PR #731 head `433490c133b26bce4163f4edf7ad04aeda9d33e3`  
RH status: **not assumed**

Fix one regular fifth-endpoint packet and one fractional-current scale `H`.
Put

\[
X_{0,H}=P_{K_B}M_H,
\qquad
M_H=\left(\widetilde W_{a,H}^{(5)}\right)^{1/2}.
\]

Let `D` denote the frequency multiplication operator on the source core. For
`0<=r<=6`, define the source-Krylov candidate operators

\[
Z_{r,H}=P_{K_A}D^rX_{0,H}.
\tag{L-104633.1}
\]

At finite regular scope these are Hilbert--Schmidt. Confluent model-space jets
and the superexponential Xi source give the same conclusion after regular
exhaustion.

For `c=(c_0,...,c_6)^T`, put

\[
Y_H(c)=\sum_{r=0}^6c_rZ_{r,H}.
\]

Its range lies in `K_A`, so `L-104632.1` gives

\[
\operatorname{tr}
 \left(Q_{A,B}\widetilde W_{a,H}^{(5)}\right)
\le
\|X_{0,H}-Y_H(c)\|_{\mathcal S_2}^2.
\tag{L-104633.2}
\]

## 1. Exact seven-by-seven normal form

Define

\[
E_H=\|X_{0,H}\|_{\mathcal S_2}^2,
\]

\[
(G_H)_{rs}=\langle Z_{s,H},Z_{r,H}\rangle_{\mathcal S_2},
\qquad
(b_H)_r=\langle Z_{r,H},X_{0,H}\rangle_{\mathcal S_2}.
\tag{L-104633.3}
\]

Then `G_H` is positive semidefinite and

\[
\boxed{
\|X_{0,H}-Y_H(c)\|_{\mathcal S_2}^2
=E_H-2\operatorname{Re}(c^*b_H)+c^*G_Hc.
}
\tag{L-104633.4}
\]

For every predeclared `tau>0`, choose

\[
c_{H,\tau}=(G_H+\tau I)^{-1}b_H.
\]

The resulting explicit certificate is

\[
\boxed{
\begin{aligned}
\mathcal R_{H,\tau}^{(6)}
={}&E_H-2b_H^*(G_H+\tau I)^{-1}b_H\\
&+b_H^*(G_H+\tau I)^{-1}G_H(G_H+\tau I)^{-1}b_H,
\end{aligned}
}
\tag{L-104633.5}
\]

and

\[
\boxed{
\operatorname{tr}
 \left(Q_{A,B}\widetilde W_{a,H}^{(5)}\right)
\le\mathcal R_{H,\tau}^{(6)}.
}
\tag{L-104633.6}
\]

No inverse of a model-space Cauchy Gram appears. The only inverse is the
regularized positive `7 by 7` source Gram in (L-104633.5).

## 2. Why degree six is the canonical finite target

`L-106612` proves that the carrier-free endpoint packets `R_0,C_0,R_5,C_5`
are finite differential polynomials in

\[
\zeta,\zeta',\ldots,\zeta^{(6)}.
\]

In the source Fourier coordinate these use only the first seven logarithmic
frequency grades. The exact frozen-carrier Bézout identity `L-104637` confirms
that degree six is sufficient at the source-module level. Thus
(L-104633.1) is the smallest natural full-grade Krylov family for this packet;
no claim is made that it is always optimal.

## 3. Finite-matrix 90-percent gate

Define `FRACKRYLOV104633` by the existence of predeclared regularizers
`tau_j(H)>0` such that

\[
\boxed{
\limsup_{T\to\infty}{1\over N(T,2T)}
\sum_j\int_0^{1/20}
 \mathcal R_{j,H,\tau_j(H)}^{(6)}\,dH
<{21\over1000}.
}
\tag{L-104633.7}
\]

Then

\[
\boxed{
\mathrm{FRACKRYLOV104633}
\Longrightarrow
\mathrm{FRACTRANS104630}
\Longrightarrow
\liminf {N_0(T,2T)\over N(T,2T)}>0.9.
}
\tag{L-104633.8}
\]

## 4. Interpretation firewall

The entries in (L-104633.3) are finite model-space/source Grams. They include
the numerator and denominator inner-factor geometry through `P_(K_A)` and
`P_(K_B)`. They are **not** automatically ordinary boundary mean values of
`zeta,...,zeta^(6)` merely because the source grades stop at six.

`L-104637` closes the frozen source-module algebra, but promotion to the
model-space matrices requires a separate source-to-inner-factor theorem or a
direct estimate of the literal Grams in (L-104633.3). That estimate is the
open content of `FRACKRYLOV104633`.
