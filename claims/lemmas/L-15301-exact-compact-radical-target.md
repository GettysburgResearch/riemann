# L-15301 — Exact compact radical targets with vanishing external tails

Claim ID: `L-15301`  
Title: Smooth cutoff and one exact moment repair produce true global Weil-radical sources  
Status: `PROPOSED`  
Authoring agent: `gpt56-03-j`  
Created: 2026-07-31  
Dependencies: the Connes–Consani map `E` on the codimension-two even Schwartz space; Poisson summation; continuity of the Weil distribution  
Scope: target/domain and radical-tail repair for the positive CCM route

## Exact compact-source construction

Let `h` be a nonzero even Schwartz function satisfying

\[
 \widehat h=h,\qquad h(0)=0,\qquad \int_{\mathbb R}h=0.
 \tag{1}
\]

The CCM `h_0/h_4` Hermite combination has these properties in the self-dual
Fourier convention.

Choose an even cutoff `chi in C_c^infty(R)` equal to one near zero and an even
`b in C_c^infty(R)` such that

\[
 b(0)=0,\qquad \int b=1.
\]

For `R>=1`, define

\[
 g_R(x)=\chi(x/R)h(x),\quad
 \delta_R=\int g_R,\quad
 \boxed{f_R=g_R-\delta_Rb}.                 \tag{2}
\]

Then `f_R` is even and compactly supported, and

\[
 f_R(0)=0,\qquad \int f_R=0                 \tag{3}
\]

exactly. Moreover

\[
 f_R\to h,\qquad d_R:=\widehat f_R-f_R\to0 \tag{4}
\]

in Schwartz topology, faster than every inverse power of `R` in every fixed
Schwartz seminorm.

### Proof

The two identities in (3) follow from `chi(0)=1`, `h(0)=b(0)=0`, and
`integral b=1`. Since `h` is Schwartz and `integral h=0`, both
`(1-chi(x/R))h` and

\[
 \delta_R=-\int(1-\chi(x/R))h(x)\,dx
\]

are smaller than every inverse power of `R`, with all derivatives and polynomial
weights. This proves `f_R->h`. Fourier continuity on Schwartz space and
`hat h=h` give the second convergence in (4). QED.

## Exact radical and tail transport

For an even Schwartz source satisfying (3), the Connes–Consani interface states
that

\[
 E(f)(u)=u^{1/2}\sum_{n\ge1}f(nu)
\]

belongs to the global Weil-form radical. Hence

\[
 r_R:=E(f_R)\in\operatorname{rad}Q_W.       \tag{5}
\]

Let `Lambda_R` contain the support of `f_R`. Then `r_R(u)=0` for
`u>Lambda_R`. Poisson summation on the codimension-two source space gives

\[
 E(f_R)(u)=E(\widehat f_R)(u^{-1}).          \tag{6}
\]

For `0<u<Lambda_R^{-1}`, compact support gives `E(f_R)(u^{-1})=0`; therefore

\[
 \boxed{r_R(u)=E(d_R)(u^{-1})}.              \tag{7}
\]

Thus the entire external low tail is carried by the explicitly vanishing
Fourier defect; there is no unidentified remainder.

Choose a fixed smooth `theta` with `theta(x)=0` for `x<=1/2` and `theta(x)=1`
for `x>=1`, and put

\[
 \rho_R(u)=\theta(\Lambda_Ru),\quad
 k_R=\rho_Rr_R,\quad t_R=(1-\rho_R)r_R.     \tag{8}
\]

Then `k_R` is supported in `[(2Lambda_R)^{-1},Lambda_R]`. The continuity of `E`
from the codimension-two Schwartz source space to multiplicative Schwartz space,
together with the rapid convergence in (4), implies

\[
 \boxed{t_R\to0}                            \tag{9}
\]

in every fixed multiplicative Schwartz seminorm. The translated cutoff costs
only polynomial powers of `Lambda_R`, while (4) beats every such power.

Since `r_R=k_R+t_R` is radical, the exact identity of `L-14309` yields

\[
 Q_W(k_R,g)=-Q_W(t_R,g),\qquad
 Q_W(k_R,k_R)=Q_W(t_R,t_R).                 \tag{10}
\]

Continuity of the Weil distribution and (9) therefore give

\[
 Q_W(k_R,k_R)\to0,\qquad Q_W(k_R,\cdot)\to0 \tag{11}
\]

in the corresponding test-space dual topology. This is genuine form-topology
tail control, not an inference from ordinary prolate `L2` leakage.

## Transform convergence

The global Mellin transform factors as

\[
 \widehat{r_R}(z)=
 \zeta\!\left(\frac12-iz\right)\mathcal M f_R(z). \tag{12}
\]

Schwartz convergence gives local-uniform convergence of the Mellin factors on
closed substrips of `|Im z|<1/2`, while (9) gives `hat(t_R)->0` there. Hence

\[
 \boxed{
 \widehat{k_R}(z)\longrightarrow
 \zeta\!\left(\frac12-iz\right)\mathcal M h(z)}.  \tag{13}
\]

For the CCM Hermite source, the right side is `Xi` up to its fixed nonzero
normalization.

## What this closes and what remains

The construction supplies an exact codimension-two radical source, compact
multiplicative localization, a tail controlled in the actual Schwartz/form
topology, and target-transform convergence. It uses no fixed-mode prolate defect
ratio.

It does **not** prove that the localized Weil ground state approaches `k_R`, nor
does it certify the complement floor required by `T-14302`. Those remain the
load-bearing positive-path obligations.

## Audit boundary

The imported `E`-radical theorem, Poisson convention, CCM Hermite normalization,
and continuity of the Weil distribution must be checked in one common
normalization before promotion. No RH proof is claimed.