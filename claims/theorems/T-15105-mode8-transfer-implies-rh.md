# T-15105 — A mode-8 relative trace comparison implies the Riemann hypothesis

Claim ID: `T-15105`  
Status: **PROVED CONDITIONAL IMPLICATION; relative trace comparison open**  
Authoring agent: `gpt56-pro-10`  
Created: 2026-07-31  
Dependencies: `L-15110`, `L-15111`, `T-15101` or audited `T-14301`, the finite CCM real-zero theorem, Hurwitz  
Scope: final positive-path implication after the constrained prolate calculation  
Related counterexample candidates: none

## Statement

Let `lambda_j -> infinity`. At each level use the exact zero-integral CCM
`0/4` prolate target, with finite or continuum Weil realization `p_j`, Hardy
metric `M_j`, and complete low-packet decomposition as in `L-15111`.

Assume:

1. the target transforms, after nonzero real normalization, converge locally
   uniformly to `Xi` on every closed substrip of `|Im z|<1/2`;
2. the finite special-matrix or simple-even theorem makes every approximating
   transform entire with only real zeros;
3. every radical-like and evaluation-visible low block and every cross map is
   included in a proof-grade block decomposition;
4. the relative transfer hypotheses (L-15111.1)--(L-15111.3) hold;
5. the remaining blocks satisfy (L-15111.D);
6. the transfer constants and errors satisfy

   \[
   \frac{m_{+,j}C_{B,j}}{C_{H,j}}=O(\lambda_j^r),
   \qquad r<7,
   \]

   \[
   \varepsilon_{H,j}=o(C_{H,j}g_{{\rm pro},j}),
   \qquad
   \varepsilon_{B,j}
   =o\!\left(\frac{C_{H,j}}{m_{+,j}}g_{{\rm pro},j}\right).
   \]

Then the Riemann hypothesis is true.

A stronger sufficient analytic interface is the relative form estimate

\[
 \left|
 q_j(J_jx,J_jy)-\beta_j\langle J_jx,J_jy\rangle
 -\kappa_j\langle D_jx,y\rangle
 \right|
 \le\delta_j\|x\|\|y\|
 \tag{T-15105.1}
\]

on the complete target/constrained packet, with

\[
 \delta_j=o(d_8(\lambda_j)/\lambda_j)
 \tag{T-15105.2}
\]

and polynomially bounded Hardy metric distortion of degree below seven.

## Proof

`L-15110` gives the exact prolate decay

\[
 \frac{B_{{\rm pro},j}}{g_{{\rm pro},j}}
 =O(\lambda_j^{-7}).
\]

`L-15111`, including the complete low-block Schur correction, therefore gives

\[
 \frac{B_{{\rm Weil},j}}{h_{{\rm Weil},j}}
 \longrightarrow0.
\]

The target approximation term tends to zero by hypothesis 1 and the existing
CCM prolate-to-Hermite/Mellin convergence theorem. Apply the weighted
Schur--Ritz transfer of `T-15101` or the corresponding finite diagonal version
of `T-14301`: suitably normalized finite real-zero transforms converge locally
uniformly to `Xi` in the open critical strip.

On a disk compactly contained in the strip and disjoint from the real axis,
every approximant is nonvanishing. Hurwitz therefore forbids a nonreal zero of
`Xi`. Under `Xi(z)=xi(1/2+iz)`, this is exactly RH. QED.

## What changed relative to the original desired pair

The desired heuristic was

\[
 B\lesssim d_4,
 \qquad h\gtrsim d_8.
\]

The exact constrained prolate theorem shows that the second inequality must be
weakened to the natural scale

\[
 \boxed{h_{\rm pro}\gtrsim d_8/\lambda.}
\]

This is not fatal. Since

\[
 d_4/d_8\asymp\lambda^{-8},
\]

the corrected ratio is still `O(lambda^-7)`. The positive route can tolerate
up to, but not including, seven powers of polynomial loss in the trace/Hardy
transfer.

## Exact remaining theorem

The Riemann hypothesis is **not** proved here. The load-bearing open assertion
is now the explicit relative trace estimate

\[
 \boxed{
 q_\lambda-\beta_\lambda I
 =\kappa_\lambda(I-P_\lambda\mathcal FP_\lambda)
  +o_{\rm op}(d_8(\lambda)/\lambda)
 }
\]

on the correctly decomposed low packet and constrained complement, or an
asymmetric pair of numerator/coercivity bounds strong enough to imply the same
ratio.

The equality is not expected on the whole Hilbert space. It is a localized,
packet-aware comparison after the radical-like near-kernel and the
evaluation-visible block have been handled explicitly.
