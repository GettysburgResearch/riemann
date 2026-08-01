# L-18515 — Exact zero amplification of the absorbed D-0001 source flag

Claim ID: `L-18515`  
Title: An off-critical zero forces exponential exterior-tail cost for every front-augmented packet containing `k_1`  
Status: `PROPOSED — COMPLETE FINITE/COMPLEX-ANALYTIC PROOF; D-0001 AND GLOBAL-RADICAL NORMALIZATIONS INHERITED`  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-01  
Dependencies: `D-0001`; `L-20701`; the global arithmetic-radical zero factor; Hardy-strip evaluation continuity  
Scope: the growing absorbed row of `X-18507`

## 1. Exact absorbed-row evaluation

Put

\[
L=\log c
\]

and use the unnormalised even D-0001 coordinates

\[
b_0=e_0,
\qquad
b_j=e_{-j}+e_j.
\]

The front-augmentation vectors are

\[
 k_j=-2b_0+b_j,
 \qquad 1\le j<N.
\]

For a complex centered spectral parameter `z`, define

\[
 \mu={Lz\over2\pi},
 \qquad
 s_L(z)=-{2\sin(Lz/2)\over z\sqrt L}.
\]

The critical-line formula of `L-20701` extends meromorphically, with removable
integer resonances, to the entire D-0001 evaluation functional. In the
unnormalised even coordinates it gives

\[
 \boxed{
 \mathcal V_{L,z}(k_j)
 =
 {2j^2s_L(z)\over \mu^2-j^2}
 =
 -{4j^2\sin(Lz/2)\over
 z\sqrt L\left[(Lz/2\pi)^2-j^2\right]}.
 }
 \tag{L-18515.1}
\]

Indeed the row on `b_0,b_j` is

\[
 s_L(z)\left(1,{2\mu^2\over\mu^2-j^2}\right),
\]

and contraction with `(-2,1)` gives (L-18515.1).

## 2. Off-critical exponential lower bound

Let

\[
 \rho={1\over2}+\delta+i\gamma,
 \qquad \delta>0,
\]

be a hypothetical nontrivial zeta zero, and put

\[
 z_\rho=\gamma-i\delta,
\]

so that

\[
 \xi\!\left({1\over2}+iz_\rho\right)=0.
\]

The elementary identity

\[
 |\sin(a-ib)|^2=\sin^2a+\sinh^2b
\]

implies

\[
 |\sin(Lz_\rho/2)|\ge\sinh(\delta L/2).
\]

For `j=1`, equation (L-18515.1) and the triangle inequality give

\[
 \boxed{
 |\mathcal V_{L,z_\rho}(k_1)|
 \ge
 {4\sinh(\delta L/2)\over
 |z_\rho|\sqrt L
 \left(L^2|z_\rho|^2/(4\pi^2)+1\right)}.
 }
 \tag{L-18515.2}
\]

Consequently there is a constant `c_rho>0` such that

\[
 \boxed{
 |\mathcal V_{L,z_\rho}(k_1)|
 \ge c_\rho {e^{\delta L/2}\over L^{5/2}}
 }
 \tag{L-18515.3}
\]

for all sufficiently large `L`.

Since

\[
 \|k_1\|_{G}^{2}=6,
\]

this is also an exponential lower bound for the operator norm of zero
evaluation on every absorbed packet

\[
 R_N=\operatorname{span}\{k_1,\ldots,k_{N-1}\},
 \qquad N\ge2.
\]

## 3. Exact radical-tail obstruction

Let `r_L` be an exact global arithmetic-radical vector whose localization on the
D-0001 interval is `k_1`, and write

\[
 r_L=k_1+t_L.
\]

The global radical transform vanishes at every nontrivial zeta zero. Therefore

\[
 \widehat t_L(z_\rho)
 =-\mathcal V_{L,z_\rho}(k_1).
 \tag{L-18515.4}
\]

Let `X_tau` be any exterior-tail topology for which evaluation at `z_rho` is
continuous:

\[
 |\widehat f(z_\rho)|
 \le C_{\rho,\tau}\|f\|_{X_\tau}.
 \tag{L-18515.5}
\]

The weighted Hardy/Schwartz norms used by the positive-path radical-tail stack
have this property whenever `tau>delta`. Combining (L-18515.3)--(L-18515.5)
gives

\[
 \boxed{
 \|t_L\|_{X_\tau}
 \ge {c_\rho\over C_{\rho,\tau}}
 {e^{\delta L/2}\over L^{5/2}}.
 }
 \tag{L-18515.6}
\]

Thus the absorbed row cannot be a vanishing-loss radical packet under false RH.
It does not merely fail to vanish: every exact radical lift of the fixed first
row has exponentially growing exterior cost.

In particular, a theorem proving the production rates

\[
 e_N\to0,
 \qquad
 \kappa_N\to0
\]

from a uniformly vanishing exact-radical tail for the front-augmented `R_N`
would already exclude every off-critical zero.

## 4. Conditional critical-line rate and the rank/support conflict

There is a complementary upper bound explaining what a positive proof would
need. Assume RH and let `gamma_1` be the first positive zero ordinate. Suppose
for one fixed `0<eta<1` that

\[
 N\le \eta {L\gamma_1\over2\pi}.
 \tag{L-18515.7}
\]

For every critical-line ordinate `gamma>=gamma_1`, equation (L-18515.1) gives

\[
 |\mathcal V_{L,\gamma}(k_j)|
 \le
 {16\pi^2j^2\over
 (1-\eta^2)L^{5/2}\gamma^3}.
 \tag{L-18515.8}
\]

The metric Gram of `k_1,...,k_{N-1}` is

\[
 G_R=2I+4\mathbf1\mathbf1^T,
 \qquad
 G_R^{-1}
 ={1\over2}I-{1\over2N-1}\mathbf1\mathbf1^T
 \preceq {1\over2}I.
 \tag{L-18515.9}
\]

Since

\[
 \sum_\gamma m_\gamma\gamma^{-6}<\infty,
\]

the positive zero-side expansion under RH yields

\[
 \boxed{
 \|G_R^{-1/2}B_RG_R^{-1/2}\|
 \le C_\eta\left({N\over L}\right)^5.
 }
 \tag{L-18515.10}
\]

Hence `N=o(L)` is a sufficient soft schedule for the raw absorbed block to
vanish under RH. Positive Schur shorting only decreases the `R` block, and the
block Cauchy--Schwarz inequality transfers the same scale to the corrected
`R/W` row whenever the `W` floor stays positive.

This conditional estimate exposes the exact capacity conflict:

- soft radicality asks for `N/L -> 0`;
- a complete weighted-deficit packet may have rank proportional to the support
  length.

A source-flag/deficit-flag identification must resolve that conflict; dimension
matching alone cannot do so.

## 5. Proof boundary

- The finite evaluation formula and the off-line exponential bound are exact.
- The radical-tail conclusion uses only the zeta factor and continuity of the
  declared tail topology.
- The upper rate (L-18515.10) is conditional on RH and the inherited positive
  zero-side normalization.
- This lemma does not prove RH. It proves that the requested absorbed-row
  vanishing theorem is itself RH-bearing and identifies the exact exponential
  obstruction under false RH.
