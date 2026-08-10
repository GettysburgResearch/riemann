# R-32403 — The Q=4 physical coefficient must not be passed through a second carry transform

Claim ID: `R-32403`  
Status: **EXACT SOURCE-TYPING CORRECTION**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09

For the `Q=4` system,

\[
 b_4=\mu*e_4,
 \qquad
 c_4=e_4*\Lambda_4=\mathbf1*(b_4*\Lambda_4).
\]

The atomized carry kernel has transform `zeta(s)N_theta(s)`. Source convolution by `b_4` cancels that zeta factor, so the physical transform is

\[
 E_4(s)L_4(s)N_\theta(s).
\]

Therefore the coefficient `c_4` multiplies the inverse transform of `N_theta`, namely the centered-interval/additive-split kernel. At integer parent `n=j+k`,

\[
 \boxed{
 \mathcal Q_4(n,j)
 =G_4(n)-G_4(j)-G_4(k),
 \qquad
 G_4(x)=\sum_{m\le x}c_4(m).
 }
\]

It is **not**

\[
 \sum_qc_4(q)\chi_{n,q}(j).
\]

The latter expression applies another floor/divisor-prefix operator and inserts an extra zeta factor in Dirichlet series. It is the secondary transform retained at corrected scope in `L-32408`, not the pole-preserving physical field.

This correction supersedes the original physical interpretations of `L-32407`, `L-32408`, and `L-32409`. `L-32407` has been rewritten in the correct coordinate; `L-32408/L-32409` are retained only at secondary/firewall scope.

The exact `X-32402` verifier was also rewritten to form the true prefix defect. The corrected finite physical-to-reserve ratio is `<11` on all `2,803,709` balanced rows through endpoint `4734`.
