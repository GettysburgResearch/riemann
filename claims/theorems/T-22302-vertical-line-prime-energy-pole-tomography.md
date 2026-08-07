# T-22302 — Vertical-line prime-energy pole tomography

Claim ID: `T-22302`  
Title: The weighted prime-only vertical energy is finite under RH and has an explicit inverse-distance blow-up at every off-critical zero line  
Status: `PROPOSED — COMPLETE LOCAL MEROMORPHIC ANALYSIS; RH REMAINS OPEN`  
Authoring agent: `gpt56-pro-19`  
Created: 2026-08-07  
Dependencies: `T-21502`; the explicit zero set of `widehat H`; standard local meromorphic expansion and fixed-strip logarithmic-derivative bounds  
Scope: the integral requested in `T-22301.16`

## 1. The vertical energy

Let

\[
 F(z)=\widehat H(z)P_1\!\left(\frac12+z\right),
 \]

where `H` is the fixed prime-only window of `T-21502`, and define

\[
 \boxed{
 I_H(\sigma)=\int_{\mathbb R}|F(\sigma+it)|^2\,dt,
 \qquad 0<\sigma<\frac12.
 }
 \tag{T-22302.1}
\]

The exact transform is

\[
 \widehat H(z)
 =e^{-z}{(1-e^{-z})^3\over z^2}
  (1-2\,4^{-z}).
 \tag{T-22302.2}
\]

Its zeros lie only on the boundary lines `Re z=0` and `Re z=1/2`. Hence

\[
 \boxed{
 \widehat H(z)\ne0
 \quad\text{for}\quad 0<\operatorname{Re}z<\frac12.
 }
 \tag{T-22302.3}
\]

## 2. Prime logarithmic derivative near a zeta zero

Möbius inversion gives

\[
 P_1(s)=D(s)+A(s),
 \qquad
 D(s)=-\frac{\zeta'}{\zeta}(s),
 \tag{T-22302.4}
\]

where

\[
 A(s)=\sum_{r\ge2}\mu(r)D(rs)
 \]

is analytic for `Re s>1/2`: for `r=2`, `Re(2s)>1`, and for `r>=3` the series is absolutely and locally uniformly convergent.

Let `rho=beta+i gamma` be a nontrivial zeta zero of multiplicity `m`, with

\[
 \delta=\beta-\frac12\in(0,1/2).
 \]

In a neighborhood of `z_rho=delta+i gamma`,

\[
 P_1\!\left(\frac12+z\right)
 =-\frac{m}{z-z_\rho}+B_\rho(z),
 \tag{T-22302.5}
\]

with `B_rho` analytic. Multiplying by `widehat H`,

\[
 F(z)=-{m\widehat H(z_\rho)\over z-z_\rho}+C_\rho(z),
 \tag{T-22302.6}
\]

where `C_rho` is analytic and `widehat H(z_rho)!=0` by (T-22302.3).

## 3. Exact divergence on the zero line

Set `sigma=delta`. Along that vertical line,

\[
 F(\delta+it)
 ={i m\widehat H(z_\rho)\over t-\gamma}
 +O(1).
 \]

Choose `r>0` so small that the analytic remainder on `|t-gamma|<=r` is at most half the principal part whenever `0<|t-gamma|<=r_0<=r`. Then

\[
 |F(\delta+it)|^2
 \ge {m^2|\widehat H(z_\rho)|^2\over4|t-\gamma|^2}
 \]

on a punctured subinterval. Therefore

\[
 \boxed{I_H(\delta)=+\infty.}
 \tag{T-22302.7}
\]

Thus one off-critical zero forces failure of the requested integral at the exact horizontal displacement of that zero.

## 4. Quantitative inverse-distance blow-up

Let `a=sigma-delta`, and choose `r>0` so that the disk around `z_rho` contains no other pole. Define the local ordinate energy

\[
 I_{\rho,r}(\sigma)
 =\int_{\gamma-r}^{\gamma+r}|F(\sigma+it)|^2dt.
 \tag{T-22302.8}
\]

The principal term integrates exactly as

\[
 \int_{\gamma-r}^{\gamma+r}
 {m^2|\widehat H(z_\rho)|^2\,dt\over a^2+(t-\gamma)^2}
 ={2m^2|\widehat H(z_\rho)|^2\over|a|}
  \arctan{r\over|a|}.
 \tag{T-22302.9}
\]

The analytic remainder contributes at most logarithmic order to the cross term and bounded order to its square. Consequently, as `sigma->delta` through lines not containing the pole,

\[
 \boxed{
 I_{\rho,r}(\sigma)
 ={\pi m^2|\widehat H(z_\rho)|^2\over|\sigma-\delta|}
 +O_{\rho,r}\!\left(\log{1\over|\sigma-\delta|}\right).
 }
 \tag{T-22302.10}
\]

This local statement is unconditional and does not assume that the complementary part of the full-line integral is finite. If several zeros share the same real part but have distinct ordinates, disjoint local neighborhoods give the sum of their positive leading coefficients.

Equation (T-22302.10) is a vertical tomography law: every off-critical zero line creates a positive inverse-distance spike whose leading coefficient cannot be canceled by an analytic remainder.

## 5. Finiteness under RH

Assume RH. For fixed `sigma>0`, every nontrivial zero of zeta lies a horizontal distance exactly `sigma` from

\[
 s=\frac12+\sigma+it.
\]

The symmetric partial-fraction expansion for `xi'/xi`, together with the unit-interval zero count `N(T+1)-N(T)=O(log(2+T))`, gives

\[
 {\zeta'\over\zeta}\!\left(\frac12+\sigma+it\right)
 =O_\sigma\bigl(\log^2(2+|t|)\bigr).
 \tag{T-22302.11}
\]

The terms `D(rs)`, `r>=2`, in (T-22302.4) are uniformly bounded on this line, while

\[
 \widehat H(\sigma+it)=O_\sigma((1+|t|)^{-2}).
 \]

Hence

\[
 |F(\sigma+it)|^2
 \ll_\sigma
 {\log^4(2+|t|)\over(1+|t|)^4},
 \]

which is integrable. Therefore

\[
 \boxed{
 \mathrm{RH}\quad\Longrightarrow\quad
 I_H(\sigma)<\infty
 \text{ for every }\sigma>0.
 }
 \tag{T-22302.12}
\]

Together with (T-22302.7),

\[
 \boxed{
 \mathrm{RH}
 \iff
 I_H(\sigma)<\infty
 \text{ for every }\sigma>0.
 }
 \tag{T-22302.13}
\]

This is a direct vertical-line proof of the equivalence, independent of the time-domain cumulative-energy formulation.

## 6. Uniform compact-strip form

For `0<a<b<1/2`, define

\[
 \mathcal I_H[a,b]=\sup_{a\le\sigma\le b}I_H(\sigma).
 \tag{T-22302.14}
\]

If `mathcal I_H[a,b]<infinity`, then no zeta zero can satisfy

\[
 \frac12+a\le\operatorname{Re}\rho\le\frac12+b.
 \]

Conversely, under RH the supremum is finite on every such compact interval by the fixed-distance version of (T-22302.11). Thus

\[
 \boxed{
 \mathrm{RH}
 \iff
 \mathcal I_H[a,b]<\infty
 \quad\text{for every }0<a<b<1/2.
 }
 \tag{T-22302.15}
\]

A proof-producing positive attack may therefore target locally uniform compact-strip estimates. Pointwise estimates with constants allowed to depend arbitrarily on the exact line cannot be glued across a hypothetical pole line.

## 7. Proof boundary

Closed here:

- the exact uncancelled principal part of the prime-only transform at every off-critical zero;
- divergence of the requested integral on the corresponding vertical line;
- the local inverse-distance blow-up coefficient;
- finiteness under RH;
- equivalence with locally uniform compact-strip bounds.

Open:

- an unconditional arithmetic proof of any compact-strip bound reaching all the way to `a>0`.

The requested integral is therefore not a soft consequence of vertical decay or abstract Dirichlet-Hardy theory. Its finiteness for all `sigma>0` is exactly the zero-exclusion theorem to be proved.
