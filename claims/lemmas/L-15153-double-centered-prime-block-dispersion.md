# L-15153 — Double-centered prime block dispersion

Claim ID: `L-15153`  
Title: The prime-only safe block kernel annihilates both constant and pole-density modes in each leg, giving an exact finite centered dispersion form  
Status: **PROPOSED EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-07  
Dependencies: the compact prime-only safe window in `T-21502`; elementary Fubini and change of variables  
Scope: orientation-correct source centering for the repaired global proposal

## 1. Safe prime-only window

Let `H` be the compact real window of `T-21502`. Its bilateral Laplace transform satisfies

\[
 \widehat H(0)=0,
 \qquad
 \widehat H(1/2)=0,
 \tag{L-15153.1}
\]

and has no zero in the open counterexample strip.

Write

\[
 \mu_{\mathbb P}
 =\sum_p{\log p\over\sqrt p}\,\delta_{\log p}
 \tag{L-15153.2}
\]

and introduce the continuous pole-density model

\[
 d\mu_0(u)=e^{u/2}du.
 \tag{L-15153.3}
\]

Put

\[
 \nu_{\mathbb P}=\mu_{\mathbb P}-\mu_0.
 \tag{L-15153.4}
\]

For all `x` beyond the fixed initial support boundary,

\[
 \boxed{
 (H*\mu_0)(x)=e^{x/2}\widehat H(1/2)=0,}
 \tag{L-15153.5}
\]

so the actual prime-only signal is exactly

\[
 \boxed{
 Q_H^{\mathbb P}=H*\nu_{\mathbb P}.}
 \tag{L-15153.6}
\]

No asymptotic prime number theorem is used in this centering.

## 2. Finite block Gram kernel

For a unit logarithmic block `I_J=[J,J+1]`, define

\[
 \boxed{
 K_J(u,v)=\int_J^{J+1}H(x-u)H(x-v)dx.}
 \tag{L-15153.7}
\]

Because `H` is compactly supported, only `u,v` in one fixed finite interval around `J` occur. The block energy is

\[
 \mathcal B_J^{\mathbb P}
 =\int_J^{J+1}|Q_H^{\mathbb P}(x)|^2dx.
 \tag{L-15153.8}
\]

Expanding the square gives the exact finite dispersion identity

\[
 \boxed{
 \mathcal B_J^{\mathbb P}
 =\iint K_J(u,v)
 \,d\nu_{\mathbb P}(u)d\nu_{\mathbb P}(v).}
 \tag{L-15153.9}
\]

The integral contains only finitely many prime atoms and one compact continuous rectangle.

## 3. Two exact null modes in each leg

For `alpha in {0,1/2}`, change variables `t=x-v` to obtain

\[
 \begin{aligned}
 \int_{\mathbb R}e^{\alpha v}K_J(u,v)dv
 &=\int_J^{J+1}H(x-u)
   \left(\int_{\mathbb R}e^{\alpha v}H(x-v)dv\right)dx\\
 &=\widehat H(\alpha)
   \int_J^{J+1}H(x-u)e^{\alpha x}dx\\
 &=0.
 \end{aligned}
 \tag{L-15153.10}
\]

For all sufficiently large `J`, the relevant support lies in `v>=0`, so the same identity holds with the half-line continuous model.

By symmetry, the identical null relation holds in the `u` leg. Therefore

\[
 \boxed{
 \int K_J(u,v)dv=0,
 \qquad
 \int e^{v/2}K_J(u,v)dv=0,}
 \tag{L-15153.11}
\]

and the same two equations hold after interchanging `u` and `v`.

Thus both the constant density and the zeta-pole density are removed **before any estimate is applied**.

## 4. Exact equality with the discrete prime Gram

Expanding (L-15153.9) into discrete and continuous pieces, every prime/continuous cross term and the continuous/continuous term vanishes by (L-15153.10). Hence

\[
 \boxed{
 \mathcal B_J^{\mathbb P}
 =\sum_{p,q}
 {\log p\log q\over\sqrt{pq}}
 K_J(\log p,\log q),}
 \tag{L-15153.12}
\]

with the sum restricted automatically to one finite prime interval.

This equality is not a heuristic replacement of the prime measure by a smooth model. It says that the finite prime Gram is already a doubly centered dispersion form for the exact signed measure `nu_P`.

## 5. Diagonal and balanced Type-II sector

Split

\[
 \mathcal B_J^{\mathbb P}=\mathcal D_J^{\mathbb P}+\mathcal O_J^{\mathbb P}.
 \tag{L-15153.13}
\]

The diagonal has a polynomial bound in `J`. The off-diagonal is the exact balanced squarefree-semiprime sum of `L-21504`:

\[
 \boxed{
 \mathcal O_J^{\mathbb P}
 =\sum_{p<q}{2\log p\log q\over\sqrt{pq}}
 K_J(\log p,\log q).}
 \tag{L-15153.14}
\]

The compact support of `K_J` restricts `p/q` to one fixed interval. This is an adjoint/factor-ratio dispersion geometry and is the correct positive-energy orientation.

## 6. Consequence for proof strategy

Any successful Type-II estimate may freely subtract either null density in each factor before applying Cauchy–Schwarz, Vaughan/Heath-Brown decomposition, or a multiplicative large sieve. A derivation that first replaces the signed centered measure by its total variation loses the exact two-mode cancellation and cannot reach the RH scale.

The repaired proposal `M-15111` uses (L-15153.9) rather than the indefinite product-dilation form of `L-15152`.

## 7. Proof boundary

Closed exactly:

- pole-density centering;
- constant-density centering;
- the finite centered block identity;
- vanishing of every continuous cross term;
- the orientation-correct balanced semiprime sector.

Open:

- a subexponential or polynomial upper bound for the centered Type-II form;
- RH.