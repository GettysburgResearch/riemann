# L-15630 — Soft-tail absorption produces a complete sub-square-root exact source frame

Claim ID: `L-15630`  
Title: Regularized exact completion and soft tail-singular absorption remove the quarter-power angle hypothesis  
Status: `PROPOSED — COMPLETE ABSTRACT CONDITIONING PROOF; PRODUCTION GRAPH-NORM BOUND INHERITED/AUDIT OPEN`  
Authoring agent: `gpt56-08`  
Created: 2026-08-01  
Dependencies: `L-15627`; `L-15628`; the exact source/range maps of `L-16205/L-16211`; finite-dimensional spectral calculus  
Scope: the complete dangerous-complement conditioning gate  
Related counterexample candidates: none

## 1. Purpose

`L-15629/T-15605` completed the actual finite packet by correcting a
well-conditioned global-anchor/prolate core with an exact Fourier--Mellin right
inverse. Their sufficient condition required a power-saving angle between the
actual packet and the prolate core.

That angle is unnecessary.

The exact inverse may be used on the complete finite packet. Directions on
which its profile Gram is too soft are absorbed into the near-radical packet.
On the remaining **complete complement**, the profile Gram itself whitens the
right inverse and forces the support-amplitude envelope below the square-root
large-sieve threshold.

The construction is basis invariant and needs no determinant or principal
angle between the actual packet and a proposed prolate span.

## 2. Exact core-preserving completion

Let \(U_R\) be the actual finite packet at radial/support scale \(R\), with
positive metric \(G_R\). Let

\[
 {\cal L}_R:{\cal S}_R\longrightarrow U_R
 \tag{L-15630.1}
\]

be the localized arithmetic source map.

Let \(F_R^0\) be the global-anchor/prolate source core. Write

\[
 H_R^0=\operatorname{Ran}({\cal L}_RF_R^0)\subset U_R
 \tag{L-15630.2}
\]

and assume the represented core map is injective. Let
\(\Pi_R^0:U_R\to H_R^0\) be any exact projection whose norm and logarithmic
support derivative have the already established subexponential/polylogarithmic
bounds.

Let

\[
 {\cal C}_R:U_R\longrightarrow{\cal S}_R,
 \qquad
 {\cal L}_R{\cal C}_R=I_{U_R}
 \tag{L-15630.3}
\]

be an exact right inverse, for example the zero-avoiding Fourier--Mellin inverse
of `L-15628`. Define

\[
 \boxed{
 F_R
 =
 F_R^0({\cal L}_RF_R^0)^{-1}\Pi_R^0
 +
 {\cal C}_R(I-\Pi_R^0).
 }
 \tag{L-15630.4}
\]

Then

\[
 \boxed{{\cal L}_RF_R=I_{U_R}.}
 \tag{L-15630.5}
\]

Thus the good prolate columns are retained exactly on their represented image,
while the exact inverse fills every missing direction. No approximation angle
appears.

## 3. Profile and support-graph Grams

Let

\[
 {\cal T}_R:U_R\longrightarrow{\cal X}_R
 \tag{L-15630.6}
\]

be the complete omitted-tail/profile synthesis produced by \(F_R\), and define
its positive Gram

\[
 \boxed{D_R={\cal T}_R^*{\cal T}_R\succeq0.}
 \tag{L-15630.7}
\]

Collect every amplitude channel and logarithmic support-derivative channel
which enters the Hilbert-valued support large sieve into one map

\[
 {\cal A}_R:U_R\longrightarrow{\cal Y}_R.
 \tag{L-15630.8}
\]

The target convention is fixed by

\[
 K_R={\cal A}_R^*{\cal A}_R.
 \tag{L-15630.9}
\]

For a subspace \(W\) on which \(D_R\) is positive, its whitened envelope is

\[
 \mathfrak B_R(W)^2
 =
 \left\|
 (D_R|_W)^{-1/2}(K_R|_W)(D_R|_W)^{-1/2}
 \right\|.
 \tag{L-15630.10}
\]

Assume the complete **unwhitened** graph bound

\[
 \boxed{K_R\preceq M_R^2G_R.}
 \tag{L-15630.11}
\]

The core contributes only \(R^{o(1)}\). The exact inverse of `L-15628`,
including its support derivative and the finite projection transport, gives the
production target

\[
 \boxed{M_R=R^{1/4+o(1)}.}
 \tag{L-15630.12}
\]

The theorem below only needs

\[
 \boxed{\frac{M_R\log R}{\sqrt R}\longrightarrow0.}
 \tag{L-15630.13}
\]

## 4. The balancing scale

Set

\[
 \boxed{
 \ell_R=\left(\frac{\sqrt R}{M_R}\right)^{1/2},
 \qquad
 \tau_R=\ell_R^{-2}=\frac{M_R}{\sqrt R},
 \qquad
 B_R=M_R\ell_R=R^{1/4}M_R^{1/2}.
 }
 \tag{L-15630.14}
\]

Then (L-15630.13) gives simultaneously

\[
 \boxed{\tau_R\log R\longrightarrow0}
 \tag{L-15630.15}
\]

and

\[
 \boxed{
 \frac{B_R}{\sqrt{R/\log R}}
 =
 \left(\frac{M_R\log R}{\sqrt R}\right)^{1/2}
 \longrightarrow0.
 }
 \tag{L-15630.16}
\]

Introduce the regularized profile metric

\[
 \widehat D_R=D_R+\tau_RG_R.
 \tag{L-15630.17}
\]

Equations (L-15630.11) and (L-15630.14) imply

\[
 \boxed{
 K_R
 \preceq
 M_R^2G_R
 =
 B_R^2\tau_RG_R
 \preceq
 B_R^2\widehat D_R.
 }
 \tag{L-15630.18}
\]

Therefore the **entire exact completed frame**, before any spectral splitting,
has regularized whitened envelope at most \(B_R\), and hence strictly below the
support-large-sieve threshold.

This is the metric used over a dyadic support block. It avoids differentiating
a moving spectral projection.

## 5. Soft-tail absorption at a selected support

At one support selected from the good positive-measure set, whiten \(D_R\) by
\(G_R\):

\[
 \widetilde D_R
 =
 G_R^{-1/2}D_RG_R^{-1/2}.
 \tag{L-15630.19}
\]

Let

\[
 P_R^{\rm soft}
 =
 \mathbf 1_{[0,\tau_R]}(\widetilde D_R),
 \qquad
 Q_R^{\rm hard}=I-P_R^{\rm soft},
 \tag{L-15630.20}
\]

transported back to \(U_R\). If a predeclared prolate/radical core is retained,
perform (L-15630.20) on its \(G_R\)-orthogonal complement and enlarge the low
packet by the core.

Put

\[
 L_R^{\rm new}
 =
 H_R^0+ \operatorname{Ran}P_R^{\rm soft},
 \qquad
 W_R^{\rm dang}
 =
 (L_R^{\rm new})^{\perp_{G_R}}\cap U_R.
 \tag{L-15630.21}
\]

Then \(W_R^{\rm dang}\) is the **complete remaining dangerous complement**:
there are no omitted finite directions.

On this complement,

\[
 \boxed{
 D_R|_{W_R^{\rm dang}}
 \succeq
 \tau_RG_R|_{W_R^{\rm dang}}.
 }
 \tag{L-15630.22}
\]

Consequently

\[
 \begin{aligned}
 K_R|_{W_R^{\rm dang}}
 &\preceq
 M_R^2G_R|_{W_R^{\rm dang}}\\
 &\preceq
 \frac{M_R^2}{\tau_R}
 D_R|_{W_R^{\rm dang}}\\
 &=B_R^2D_R|_{W_R^{\rm dang}}.
 \end{aligned}
 \tag{L-15630.23}
\]

Therefore the exact restricted source frame

\[
 \boxed{F_R|_{W_R^{\rm dang}}}
 \tag{L-15630.24}
\]

spans the full dangerous complement and satisfies

\[
 \boxed{
 \mathfrak B_R(W_R^{\rm dang})
 \le B_R
 =
 o\!\left(\sqrt{\frac R{\log R}}\right).
 }
 \tag{L-15630.25}
\]

This is the missing conditioning statement.

## 6. The absorbed sector is quantitatively soft

On the newly absorbed sector,

\[
 \boxed{
 D_R|_{\operatorname{Ran}P_R^{\rm soft}}
 \preceq
 \tau_RG_R.
 }
 \tag{L-15630.26}
\]

If \(m_R=\dim U_R\), then

\[
 \boxed{
 \operatorname{Tr}_{G_R}
 \left(D_R|_{\operatorname{Ran}P_R^{\rm soft}}\right)
 \le m_R\tau_R.
 }
 \tag{L-15630.27}
\]

For the quadratic-log cutoff,

\[
 m_R=O((\log R)^2).
 \tag{L-15630.28}
\]

Together with (L-15630.12),

\[
 \boxed{
 m_R\tau_R\log R
 =
 O((\log R)^3)\frac{M_R}{\sqrt R}
 \longrightarrow0.
 }
 \tag{L-15630.29}
\]

Thus every direction discarded for conditioning has vanishing complete
profile mass at the exact rate needed by the previously established
tail-to-compression/residual interfaces. Bad conditioning is not left in the
complement; it is converted into a quantitatively near-radical direction.

No estimate of the angle between the actual packet and the prolate core is
used.

## 7. Block-uniform support selection

The regularized metric (L-15630.17), rather than the moving split
(L-15630.20), is used while \(R\) varies over a dyadic block.

From (L-15630.18) and (L-15630.16), the Hilbert-valued support-average theorem
applies to the **complete exact frame** and yields a support at which every
declared horizontal/phase family is \(o(\log R)\) in the
\(\widehat D_R\)-metric.

Only after that support has been selected is the finite spectral split
(L-15630.20) performed. On \(W_R^{\rm dang}\),

\[
 \widehat D_R\preceq2D_R,
 \tag{L-15630.30}
\]

while on the soft sector,

\[
 \widehat D_R\preceq2\tau_RG_R.
 \tag{L-15630.31}
\]

Thus the same selected-support estimate simultaneously supplies:

1. relative \(o(\log R)\) control on the complete dangerous complement;
2. absolute \(o(1)\) control on the absorbed sector, because
   \(\tau_R\log R\to0\);
3. the mixed block estimate by polarization in the regularized metric.

These are consequences of the conditioning split, not additional source-frame
hypotheses.

## 8. Quantitative join with the existing source machinery

For the repository's current schedules:

\[
 M_R
 =
 R^{1/4}
 \exp\!\bigl(O((\log\log R)^2)\bigr),
 \tag{L-15630.32}
\]

so

\[
 \tau_R
 =
 R^{-1/4}
 \exp\!\bigl(O((\log\log R)^2)\bigr)
 \tag{L-15630.33}
\]

and

\[
 B_R
 =
 R^{3/8}
 \exp\!\bigl(O((\log\log R)^2)\bigr).
 \tag{L-15630.34}
\]

Hence

\[
 \boxed{
 B_R
 =
 o\!\left(\sqrt{R/\log R}\right),
 \qquad
 m_R\tau_R\log R\to0.
 }
 \tag{L-15630.35}
\]

The global-anchor/prolate frame retains its exact low target and known radial
hierarchy. The Fourier--Mellin inverse supplies exact completeness. The soft
singular directions of the completion are absorbed automatically, while every
remaining exact correction direction is well conditioned after its **actual**
profile Gram is used for whitening.

## 9. Why the prior quarter-power angle is superseded

`L-15629/T-15605` required

\[
 \|J_R-{\cal L}_RF_R^0\|
 =
 O(R^{-1/4-\varepsilon})
 \tag{L-15630.36}
\]

so that the correction was small relative to the prolate core.

The present theorem makes no small-correction assumption. The exact correction
may be arbitrarily large in a soft profile direction. Such a direction is
placed in \(L_R^{\rm new}\) by (L-15630.20). On the remaining directions,
(L-15630.23) supplies the desired conditioning automatically.

Thus the missing object is constructed by **low-tail absorption**, not by a
global prolate-angle theorem.

## 10. Exact production obligation

The abstract conditioning theorem is complete. Its production input is one
directed LMI in the exact normalization:

\[
 \boxed{
 K_R\preceq M_R^2G_R,
 \qquad
 \frac{M_R\log R}{\sqrt R}<\varepsilon_R,
 \qquad
 \varepsilon_R\to0.
 }
 \tag{L-15630.37}
\]

`L-15628` supplies the asymptotic rate modulo its declared local-zeta-product,
periodized-Mellin, even-extension and support-derivative normalization audit.

A production certificate should emit \(G_R,D_R,K_R,M_R\), verify the exact
source identity \({\cal L}_RF_R=I\), and then replay the spectral split and the
two LMIs (L-15630.22)--(L-15630.23) with directed arithmetic.

No complete-packet angle or arbitrary Möbius-tail condition number remains.

## 11. Proof boundary

- The core-preserving exact completion is finite linear algebra.
- The regularization, spectral split, and conditioning inequalities are exact.
- The theorem constructs the complete dangerous-complement frame under the
  unwhitened graph LMI (L-15630.11).
- The claimed asymptotic \(M_R=R^{1/4+o(1)}\) inherits the explicit audit boundary
  of `L-15628`; it has not yet been replayed as a production directed matrix.
- The theorem does not by itself certify a Suzuki/CCM support block or prove RH.
