# L-91804 — The gamma beta source is a C1 Hellinger path with diffuse radial Fisher energy

Claim ID: `L-91804`  
Status: **PROVED EXACT GAMMA-SOURCE NON-ATOMICITY**  
Created: 2026-08-13  
Depends on: the beta/Laplace representation in `L-91631`  
RH status: **unproved**

## 1. Normalized gamma source

Fix

\[
 \sigma>\omega>0.
\]

The gamma factor has the positive Laplace representation

\[
 \pi^\omega
 \frac{\Gamma((s-\omega)/2)}
      {\Gamma((s+\omega)/2)}
 =\frac{2\pi^\omega}{\Gamma(\omega)}
  \int_0^\infty
  e^{-(s-\omega)t}(1-e^{-2t})^{\omega-1}dt.
\]

At the real anchor `s=sigma`, put

\[
 Z_{\sigma,\omega}
 =\int_0^\infty
  e^{-(\sigma-\omega)t}
  (1-e^{-2t})^{\omega-1}dt
\]

and define the probability density

\[
\boxed{
 p_{\sigma,\omega}(t)
 =Z_{\sigma,\omega}^{-1}
  e^{-(\sigma-\omega)t}
  (1-e^{-2t})^{\omega-1},
 \qquad t>0.
}
\tag{L-91804.1}
\]

Let

\[
 v_{\sigma,\omega}=\sqrt{p_{\sigma,\omega}}
 \in L^2(0,\infty).
\]

## 2. Exact score

Define

\[
 Y(t)=t+\log(1-e^{-2t}).
\]

Differentiating the log density gives

\[
\boxed{
 \partial_\omega\log p_{\sigma,\omega}(t)
 =Y(t)-\mathbb E_{\sigma,\omega}Y.
}
\tag{L-91804.2}
\]

Consequently

\[
\boxed{
 \partial_\omega v_{\sigma,\omega}
 =\frac12
  \left(Y-\mathbb E_{\sigma,\omega}Y\right)
  v_{\sigma,\omega}.
}
\tag{L-91804.3}
\]

## 3. Square integrability of the score

As `t downarrow 0`,

\[
 Y(t)=\log(2t)+O(t),
\]

while

\[
 p_{\sigma,\omega}(t)
 \asymp t^{\omega-1}.
\]

Thus the squared logarithmic singularity is integrable for every
`omega>0`.

As `t -> infinity`,

\[
 Y(t)=t+O(e^{-2t}),
\]

and the density decays like

\[
 e^{-(\sigma-\omega)t}.
\]

Hence

\[
 \operatorname{Var}_{\sigma,\omega}(Y)<\infty.
\]

On compact parameter rectangles

\[
 0<\omega_0\le\omega\le\omega_1<\sigma,
\]

the same estimates provide a common integrable majorant.  Therefore

\[
\boxed{
 \omega\longmapsto v_{\sigma,\omega}
 \text{ is }C^1\text{ in }L^2.
}
\tag{L-91804.4}
\]

## 4. Diffuse Fisher depth measure

The radial Fisher energy is

\[
\boxed{
 d\mathcal I_\Gamma(\omega)
 =\left\|\partial_\omega v_{\sigma,\omega}\right\|_2^2d\omega
 =\frac14
  \operatorname{Var}_{\sigma,\omega}(Y)d\omega.
}
\tag{L-91804.5}

It is absolutely continuous in horizontal depth.  In particular,

\[
 \mathcal I_\Gamma(\{\omega_0\})=0
\]

for every positive depth.

The Hellinger overlap obeys

\[
 1-\langle v_{\sigma,\omega},
          v_{\sigma,\omega+h}\rangle
 =\frac{h^2}{8}
  \operatorname{Var}_{\sigma,\omega}(Y)
  +o(h^2).
\]

Thus the gamma source cannot hide a jump coordinate in an infinitesimal
radial section.

## 5. Amplitude and phase coordinates

The omitted normalization

\[
 \frac{2\pi^\omega Z_{\sigma,\omega}}{\Gamma(\omega)}
\]

is a smooth deterministic amplitude/connection coordinate on every compact
safe parameter interval.  It introduces no positive-depth atom.

Carrier vectors `e^{-ixt}` and physical-delay phases are unitary multipliers
in the common `t` variable and commute with the Hellinger radial derivative.
The conclusion therefore holds with full carrier polarization and delays.

## 6. Consequence for `L-91800`

Together with the exact prime, eta and compact-bridge radial formulas, the
gamma source now has a proved non-atomic radial realization.  The only
remaining issue in the completed diffuse source claim is the bookkeeping of
the factorwise direct integrals inside one interval-natural product-system
morphism; there is no gamma atom obstruction.

## 7. Exact boundary

```text
gamma beta probability source             EXACT
gamma score and Fisher energy              EXACT
gamma Hellinger path C1                    EXACT
gamma positive-depth atoms                 ABSENT EXACTLY
full interval-natural source/model map      OPEN / RH-BEARING
Riemann Hypothesis                         UNPROVED
```
