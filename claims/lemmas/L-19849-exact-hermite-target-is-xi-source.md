# L-19849 — The repaired Hermite target is exactly the completed-xi source

Claim ID: `L-19849`  
Status: **PROPOSED EXACT TARGET-IDENTIFICATION LEMMA**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-07  
Scope: supplies the load-bearing target-image statement (T-19810.8)

## 1. The positive Fourier-sector target

Let `h_0,h_4` be the first two even Hermite functions with Fourier eigenvalue
`+1` in the CCM Fourier convention, and put

\[
 q_j=h_j(0).
 \tag{L-19849.1}
\]

Define

\[
 p_+=\frac{h_0}{q_0}-\frac{h_4}{q_4}.
 \tag{L-19849.2}
\]

Then

\[
 p_+(0)=0.
 \tag{L-19849.3}
\]

Because both modes have Fourier eigenvalue `+1`,

\[
 \int_{\mathbb R}p_+(x)\,dx
 =\widehat p_+(0)
 =p_+(0)=0.
 \tag{L-19849.4}
\]

Thus `p_+` satisfies both exact arithmetic-source constraints without a second
sector.

## 2. Mellin polynomial

For an even Hermite mode of index at most four, its positive-half Mellin
transform has the form

\[
 \mathcal Mh_j(s)
 =\pi^{-s/2}\Gamma(s/2)P_j(s),
 \tag{L-19849.5}
\]

where `P_j` is a polynomial of degree `j/2`. Consequently

\[
 \mathcal Mp_+(s)
 =\pi^{-s/2}\Gamma(s/2)P(s)
 \tag{L-19849.6}
\]

with `deg P<=2`.

The condition `p_+(0)=0` makes the Mellin transform regular at `s=0`. Since
`Gamma(s/2)` has a simple pole there,

\[
 P(0)=0.
 \tag{L-19849.7}
\]

The integral condition is

\[
 \mathcal Mp_+(1)=0,
 \tag{L-19849.8}
\]

and the gamma factor is nonzero at `s=1`, so

\[
 P(1)=0.
 \tag{L-19849.9}
\]

The combination (L-19849.2) is nonzero and its degree-two coefficient is
nonzero. Hence for one nonzero real constant `C_H`,

\[
 \boxed{
 \mathcal Mp_+(s)
 =C_Hs(s-1)\pi^{-s/2}\Gamma(s/2).}
 \tag{L-19849.10}
\]

This argument fixes the polynomial without relying on a convention-sensitive
closed formula for `h_4`.

## 3. Arithmetic image

The arithmetic map satisfies

\[
 \mathcal M(Ef)(s)=\zeta(s)\mathcal Mf(s).
 \tag{L-19849.11}
\]

Therefore

\[
 \boxed{
 \mathcal M(Ep_+)(s)
 =2C_H\,\xi(s),}
 \tag{L-19849.12}
\]

where

\[
 \xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
 \tag{L-19849.13}
\]

Thus the positive-sector repaired Hermite vector is not merely analogous to the
xi source: its arithmetic image is exactly a nonzero scalar multiple of the
completed zeta function.

## 4. Signed exact-radical correction

At finite prolate parameter, let

\[
 p_{+,R}=\frac{e_{0,R}}{q_{0,R}}-rac{e_{4,R}}{q_{4,R}},
 \qquad
 p_{-,R}=\frac{e_{2,R}}{q_{2,R}}-rac{e_{6,R}}{q_{6,R}},
 \tag{L-19849.14}
\]

and let

\[
 u_R=p_{+,R}-\frac{r_{+,R}}{r_{-,R}}p_{-,R}
 \tag{L-19849.15}
\]

be the normalized exact two-constraint target of `L-19823`. The fixed-mode
Fuchs hierarchy gives

\[
 \frac{r_{+,R}}{r_{-,R}}
 =O(d_4/d_6)\longrightarrow0.
 \tag{L-19849.16}
\]

Uniform low-mode prolate-to-Hermite convergence gives

\[
 p_{+,R}\to p_+,
 \qquad
 p_{-,R}\to p_-
 \tag{L-19849.17}
\]

in every fixed source Sobolev/Mellin norm. Therefore

\[
 u_R\to p_+
 \tag{L-19849.18}
\]

and

\[
 E(u_R)\to 2C_H\xi
 \tag{L-19849.19}
\]

locally uniformly after Mellin transform.

## 5. Moving Hardy norm

Choose

\[
 \tau_R=\frac12-\frac1{\sqrt{\log\lambda}}.
 \tag{L-19849.20}
\]

The quadratic-log finite Fourier cutoff of `L-16213`, together with the uniform
prolate-to-Hermite estimate and (L-19849.16), gives

\[
 \left\|
 c_RS_Ru_R-k_R^\Xi
 \right\|_{\lambda,\tau_R}
 \longrightarrow0
 \tag{L-19849.21}
\]

for nonzero real normalizations `c_R`, where the transforms of `k_R^Xi`
converge locally uniformly to `Xi`.

The source map may be ill-conditioned on other packet directions; only the
fixed target convergence in (L-19849.21) is used.

## 6. Proof boundary

- The polynomial identification (L-19849.10) and arithmetic identity
  (L-19849.12) are exact.
- The finite signed correction vanishes at the ratio `d_4/d_6`.
- The moving-Hardy convergence uses the existing quadratic-log cutoff and the
  uniform fixed-mode prolate-to-Hermite estimate; it does not follow from generic
  source surjectivity.
- No RH conclusion is claimed by this lemma alone.
