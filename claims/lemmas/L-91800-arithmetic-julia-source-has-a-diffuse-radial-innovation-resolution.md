# L-91800 — The completed arithmetic Julia source has a diffuse radial innovation resolution

Claim ID: `L-91800`  
Status: **EXACT PRIME/ETA/BRIDGE RADIAL FORMULAS; COMPLETE CONTINUOUS-PRODUCT ASSEMBLY PROPOSED**  
Created: 2026-08-13  
Depends on: `L-91710`, `L-91630/L-91631`, `L-91530`, `L-91730`  
RH status: **unproved**

## 1. The new variable: horizontal depth, not carrier height

The preceding stack resolves the completed arithmetic source into positive or
lossless Julia factors.  The decisive extra structure is that every factor can
be refined in the horizontal shift parameter.  The arithmetic innovations are
born continuously in that parameter.

Write the horizontal depth variable as

\[
 r\in(0,1/2).
\]

The purpose of this note is to distinguish this radial variable from the
prime-log, gamma-time and carrier variables already present in the source.

## 2. Prime Clark source: exact Lebesgue density in depth

For a safe line `sigma>1`, retain

\[
 \ell_{a,\sigma}(t)
 =-\log\frac{Q_a(\sigma+it)}{Q_a(\sigma)},
 \qquad
 Q_a(s)=\frac{\zeta(s)}{\zeta(s+2a)}.
\]

The Euler expansion of `L-91710` may be integrated before summing:

\[
\boxed{
 \ell_{a,\sigma}(t)
 =\int_0^a
 2\sum_{p}\sum_{k\ge1}
 (\log p)p^{-k(\sigma+2r)}
 \bigl(1-e^{-itk\log p}\bigr)\,dr.
}
\tag{L-91800.1}
\]

Indeed

\[
 \int_0^a2(\log p)p^{-k(\sigma+2r)}dr
 =\frac{p^{-k\sigma}(1-p^{-2ak})}{k}.
\]

For a Borel interval `I subset (0,a)`, define the polarized prime innovation
kernel

\[
\boxed{
\begin{aligned}
 \mathsf A_{\rm p}(I;t,s)
 =\int_I 2\sum_{p,k\ge1}
 &(\log p)p^{-k(\sigma+2r)}\\
 &\times
 (1-e^{-itk\log p})
 (1-e^{isk\log p})\,dr.
\end{aligned}}
\tag{L-91800.2}
\]

Every integrand is a positive Gram over the prime-power atoms.  Hence

\[
 \mathsf A_{\rm p}(I)\succeq0,
\]

`I -> A_p(I)` is countably additive on every finite carrier packet, and

\[
 \mathsf A_{\rm p}\ll dr.
\]

There is no positive-depth atom in the prime radial source.

## 3. Paired eta source: exact Lebesgue density

Let

\[
 \mathcal E
 =\bigcup_{m\ge1}
 [\log(2m-1),\log(2m)]
\]

and

\[
 K_q^{\eta}(t,s)
 =\int_{\mathcal E}
 e^{-qy}e^{-i(t-s)y}dy.
\]

For `sigma>omega>0`, the weighted Julia identity of `L-91630` has the
continuous refinement

\[
\boxed{
 K_{\sigma-\omega}^{\eta}
 -K_{\sigma+\omega}^{\eta}
 =\int_{-\omega}^{\omega}
  \mathsf k_r^{\eta}\,dr,
}
\tag{L-91800.3}
\]

where

\[
\boxed{
 \mathsf k_r^{\eta}(t,s)
 =\int_{\mathcal E}
 y e^{-(\sigma+r)y}e^{-i(t-s)y}dy
 \succeq0.
}
\tag{L-91800.4}
\]

This follows from

\[
 e^{-(\sigma-\omega)y}-e^{-(\sigma+\omega)y}
 =\int_{-\omega}^{\omega}y e^{-(\sigma+r)y}dr.
\]

Thus the full-carrier paired-eta detail is a direct integral over Lebesgue
radial depth.  The one-vector Householder of `L-91431` is only a compression of
this diffuse source.

## 4. Compact bridge: exact finite-interval radial density

For

\[
 F_L(q)=\int_0^L e^{-qt}dt,
 \qquad L=\log2,
\]

one has, for `q>omega`,

\[
\boxed{
 F_L(q-\omega)-F_L(q+\omega)
 =\int_{-\omega}^{\omega}
  \int_0^L t e^{-(q+r)t}dt\,dr.
}
\tag{L-91800.5}
\]

The inner kernel is again a positive Laplace Gram.  Hence the compact
dyadic/gamma bridge of `L-91530` has no radial atom; its apparent pole was a
coordinate singularity removed before Hilbert completion.

## 5. Gamma and rational factors

The residual rational factor is a continuously parameterized lossless
half-plane Blaschke section and carries no positive detail atom.

The gamma factor may be split over an arbitrary partition

\[
 0=r_0<r_1<\cdots<r_N=\omega
\]

using the exact beta source for each quotient

\[
 \frac{\Gamma((s-r_{j+1})/2)}{\Gamma((s-r_j)/2)}
 \frac{\Gamma((s+r_j)/2)}{\Gamma((s+r_{j+1})/2)}.
\]

Each section tends to the identity in source norm as
`r_(j+1)-r_j -> 0`, uniformly on compact safe carrier packets.  The ordered
Julia cascade therefore has a continuous-product refinement with one-particle
space

\[
 L^2((0,\omega),dr;\mathfrak g_r).
\]

A complete proof of the mesh-limit bookkeeping for the simultaneous
eta/bridge/gamma cascade is proposed here and should be reviewed independently;
the prime, eta and compact-bridge identities above are exact closed formulas.

## 6. Diffuse arithmetic radial source

Combining the factorwise refinements gives the proposed completed arithmetic
radial source measure

\[
 \boxed{
 \mathsf A^{\rm arith}(I)
 =\int_I \mathsf a(r)\,dr,
 \qquad
 \mathsf a(r)\succeq0,
 }
\tag{L-91800.6}
\]

on every finite carrier/delay/orientation/bridge packet.

Its essential property is spectral type:

\[
\boxed{
 \mathsf A^{\rm arith}(\{r_0\})=0
 \quad\text{for every }r_0\in(0,1/2).
}
\tag{L-91800.7}
\]

The source may have a deterministic terminal/vacuum coordinate and a boundary
coordinate at depth zero.  It has no atom at a positive horizontal depth.

## 7. Strategic significance

The previous endpoint sought a global positive kernel defect plus a quantitative
large-node estimate.  The radial refinement exposes a different possibility:
prove the source-to-model identity interval by interval.  If the positive
hyperbolic output is then dominated as a measure by the diffuse arithmetic
source, every positive-depth atom is forced to vanish before any height
asymptotic is taken.

## 8. Exact boundary

```text
prime radial Clark density                         EXACT
paired-eta radial density                          EXACT
compact-bridge radial density                      EXACT
gamma continuous-product refinement                PROPOSED / REVIEW REQUIRED
completed arithmetic source has no depth atoms     PROPOSED COMPLETE
source-to-model interval-local identity             OPEN / RH-BEARING
Riemann Hypothesis                                 UNPROVED
```
