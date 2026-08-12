# L-91322 — Raw Hardy delays have a canonical compressed-model-space dilation with explicit leakage

Claim ID: `L-91322`  
Status: **PROVED EXACT DELAY DILATION AND FULL CROSS-PACKET GRAM DECOMPOSITION**  
Created: 2026-08-13  
Depends on: `L-91316`, `R-91011`  
Corrects: the false raw-invariance shortcut isolated in `R-91011`  
RH status: **unproved**

## 1. Hardy shift semigroup

Let

\[
 H^2_+=H^2(\mathbb C_+),
 \qquad
 H^2_-=L^2(\mathbb R)\ominus H^2_+,
\]

with Riesz projections `P_+` and `P_-`.  For `tau>=0`,

\[
 m_\tau(z)=e^{i\tau z}
\]

is inner on the upper half-plane.  Hence

\[
 S_\tau=M_{m_\tau}:H^2_+\to H^2_+
 \tag{L-91322.1}
\]

is a strongly continuous isometric semigroup, and

\[
 S_\tau^*f=P_+\left(e^{-i\tau\,\cdot}f\right).
 \tag{L-91322.2}
\]

Fix an inner function `Theta` and its model space

\[
 K_\Theta=H^2_+\ominus\Theta H^2_+.
 \tag{L-91322.3}
\]

Because multiplication operators commute,

\[
 S_\tau(\Theta H^2_+)\subseteq\Theta H^2_+.
\]

Taking orthogonal complements gives the load-bearing invariance

\[
 \boxed{S_\tau^*K_\Theta\subseteq K_\Theta.}
 \tag{L-91322.4}
\]

Thus the canonical resident delay is

\[
 \boxed{
 T_{\Theta,\tau}
 =S_\tau^*|_{K_\Theta}
 =P_+M_{e^{-i\tau\,\cdot}}|_{K_\Theta}
 =P_{K_\Theta}M_{e^{-i\tau\,\cdot}}|_{K_\Theta}.
 }
 \tag{L-91322.5}
\]

The family `T_(Theta,tau)` is a strongly continuous contraction semigroup on
`K_Theta`.

## 2. The escaped Hardy prefix

Define

\[
 \boxed{
 L_{\Theta,\tau}
 =P_-M_{e^{-i\tau\,\cdot}}|_{K_\Theta}:
 K_\Theta\to H^2_-.
 }
 \tag{L-91322.6}
\]

For every `g in K_Theta`, the raw boundary delay splits orthogonally as

\[
 \boxed{
 e^{-i\tau\,\cdot}g
 =T_{\Theta,\tau}g+L_{\Theta,\tau}g,
 \qquad
 T_{\Theta,\tau}g\perp L_{\Theta,\tau}g.
 }
 \tag{L-91322.7}
\]

No component in `Theta H^2_+` is missing: by (L-91322.4), the complete positive
Hardy projection already lies in `K_Theta`.

Consequently

\[
 \boxed{
 T_{\Theta,\tau}^*T_{\Theta,\tau}
 +L_{\Theta,\tau}^*L_{\Theta,\tau}=I_{K_\Theta}.
 }
 \tag{L-91322.8}
\]

The map

\[
 g\longmapsto
 \bigl(T_{\Theta,\tau}g,L_{\Theta,\tau}g\bigr)
 \tag{L-91322.9}
\]

is therefore an explicit isometry from the model space into
$K_\Theta\oplus H^2_-$.  Raw delay invariance is unnecessary; the escaped
part is retained as a positive auxiliary channel.

## 3. Every cross-delay Gram entry is retained

For arbitrary `tau,sigma>=0` and `g,h in K_Theta`,

\[
 \boxed{
 \left\langle
  e^{-i\tau\,\cdot}g,
  e^{-i\sigma\,\cdot}h
 \right\rangle_{L^2}
 =
 \langle T_{\Theta,\tau}g,T_{\Theta,\sigma}h\rangle
 +\langle L_{\Theta,\tau}g,L_{\Theta,\sigma}h\rangle.
 }
 \tag{L-91322.10}
\]

Equivalently,

\[
 T_{\Theta,\tau}^*T_{\Theta,\sigma}
 +L_{\Theta,\tau}^*L_{\Theta,\sigma}
 =P_{K_\Theta}
  M_{e^{-i(\sigma-\tau)\,\cdot}}
  |_{K_\Theta}.
 \tag{L-91322.11}
\]

For every finite packet `(tau_j,g_j,c_j)`, polarization gives the exact
Pythagorean identity

\[
\boxed{
\begin{aligned}
 \left\|
  \sum_jc_je^{-i\tau_j\,\cdot}g_j
 \right\|_{L^2}^2
 ={}&
 \left\|
  \sum_jc_jT_{\Theta,\tau_j}g_j
 \right\|_{K_\Theta}^2\\
 &+
 \left\|
  \sum_jc_jL_{\Theta,\tau_j}g_j
 \right\|_{H^2_-}^2.
\end{aligned}}
 \tag{L-91322.12}
\]

This is a full matrix identity, not a diagonal energy statement.

## 4. Conservative delay-line cocycle

Let `U^-_tau` denote multiplication by $e^{-i\tau\,\cdot}$ on $H^2_-$; it
preserves $H^2_-$.  Decomposing a delay in two stages gives

\[
 \boxed{
 T_{\Theta,\tau+\sigma}
 =T_{\Theta,\tau}T_{\Theta,\sigma},
 }
 \tag{L-91322.13}
\]

and

\[
 \boxed{
 L_{\Theta,\tau+\sigma}
 =L_{\Theta,\tau}T_{\Theta,\sigma}
  +U^-_\tau L_{\Theta,\sigma}.
 }
 \tag{L-91322.14}
\]

Thus the resident model state and escaped prefix form a conservative
continuous-time delay line.  In Paley--Wiener coordinates, `T` is the backward
translation semigroup and `L` stores exactly the interval that exits the
positive Hardy half-line.

## 5. Composition with the Fisher--Hankel tangent

Now take `Theta=Theta_a` and retain `A_a`, `C_a`, `J_a` from `L-91316`.  The
completed density is nondegenerate, so $V_a=\operatorname{Var}_a(Y)>0$.  Put

\[
 s_a(Y)=\frac{Y-\mathbb E_aY}
 {\sqrt{\operatorname{Var}_a(Y)}}.
 \tag{L-91322.15}
\]

The score observation is

\[
 \mathcal C_aF=\mathbb E_a[s_a(Y)F(Y)].
\]

It is not merely contractive: its adjoint is

\[
 (\mathcal C_a^*v)(Y)=s_a(Y)v,
\]

so

\[
 \boxed{
 \mathcal C_a\mathcal C_a^*=I,
 \qquad
 \Pi_a:=\mathcal C_a^*\mathcal C_a
 =|s_a\rangle\langle s_a|\otimes I_{H^2}.
 }
 \tag{L-91322.16}
\]

Hence the `L-91316` factorization is an exact score-channel orthogonal
splitting.  On its declared form domain,

\[
\boxed{
 2a^2V_a\,\mathcal A_a^*\mathcal A_a
 =\mathcal J_a^*\mathcal J_a
 +2a^2V_a\,
  \mathcal A_a^*(I-\Pi_a)\mathcal A_a,
}
 \tag{L-91322.17}
\]

where $V_a=\operatorname{Var}_a(Y)$.

For a finite packet for which

\[
 h=\sum_jc_jT_{\Theta_a,\tau_j}g_j
 \in\operatorname{Dom}(\mathcal A_a),
\]

one obtains

\[
\boxed{
\begin{aligned}
 2a^2V_a\|\mathcal A_ah\|^2
 ={}&\|\mathcal J_ah\|^2\\
 &+2a^2V_a
 \|(I-\Pi_a)\mathcal A_ah\|^2.
\end{aligned}}
 \tag{L-91322.18}
\]

Together with (L-91322.12), this retains every delay cross term in two explicit
positive reserves:

```text
escaped Hardy-prefix reserve L_(Theta,tau);
Fisher feature orthogonal to the score channel (I-Pi_a)A_a.
```

After the scalar factor $a\sqrt{2V_a}$ is placed on the Fisher source leg,
the fixed observation on all delay packets is $\operatorname{diag}(\mathcal
C_a,I)$; it is independent of $\tau$.

## 6. Reflected orientation

Any fixed unitary reflection carrying `H^2_+` to `H^2_-` transports
(L-91322.4)--(L-91322.18) to the anti-causal orientation.  Thus each Hardy side
has a canonical compressed-delay colligation.  This theorem does not by itself
sign the mixed-orientation screw entries; those remain part of the completed
arithmetic source comparison.

## 7. Consequence for the live endgame

`R-91011` correctly rejected the statement that raw delays preserve
`K_(Theta_a)`.  The exact replacement is now available:

```text
raw delay
 = resident compressed model-space delay
 + explicit orthogonal Hardy leakage.
```

Therefore arbitrary delay invariance is no longer needed.  Once the resident
operator inequality

\[
 C_a^{\rm source}
 \succeq
 2a^2V_a\mathcal A_a^*\mathcal A_a
 \tag{L-91322.19}
\]

is proved on a domain stable under the compressed shift semigroup, all
same-orientation cross-delay packets follow from one application of that
inequality to `h=sum_j c_jT_(tau_j)g_j`; the leakage channel is already exact
and positive.

The identification of the physical Cauchy tests with the resident base
model-space vectors, invariance of the chosen `A_a` form core, mixed
orientations, the canonical bridge row/column, and (L-91322.19) remain open.

## 8. Exact boundary

```text
raw delay preserves K_Theta                         FALSE in general
compressed backward-shift delay preserves K_Theta  EXACT
raw delay = resident + leakage                      EXACT ISOMETRY
all cross-delay Gram entries                        EXACT
conservative delay cocycle                          EXACT
Fisher score observation is a coisometry            EXACT
score / orthogonal-feature Pythagorean identity      EXACT
same-orientation delayed Fisher factorization        EXACT ON DOMAIN
physical-test base embedding and domain invariance   OPEN
mixed orientation and bridge source comparison       OPEN
arithmetic source >= Fisher-Hankel norm               OPEN / RH-BEARING
Riemann Hypothesis                                   UNPROVED
```
