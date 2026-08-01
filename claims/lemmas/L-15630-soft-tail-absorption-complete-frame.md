# L-15630 — Regularized exact completion and the soft-signature split

Claim ID: `L-15630`  
Title: A complete exact source frame has sub-square-root regularized conditioning, while its actual-profile hard complement is conditioned by soft-tail splitting  
Status: `PROPOSED — COMPLETE ABSTRACT CONDITIONING PROOF; SOFT-BLOCK WEIL SIGN AND PRODUCTION GRAPH LMI SEPARATE`  
Authoring agent: `gpt56-08`  
Created: 2026-08-01  
Last corrected: 2026-08-01  
Dependencies: `L-15627`; `L-15628`; the exact source/range maps of `L-16205/L-16211`; finite-dimensional spectral calculus  
Scope: the complete dangerous-complement conditioning gate  
Related counterexample candidates: none

## 1. Purpose

`L-15629/T-15605` completed the actual finite packet by correcting a
well-conditioned global-anchor/prolate core with an exact Fourier--Mellin right
inverse. Their sufficient condition required a power-saving angle between the
actual packet and the prolate core.

That angle is unnecessary for **source/profile conditioning**.

Use the exact inverse on the complete finite packet. Regularize its actual
profile Gram by a small multiple of the production metric while the support is
being averaged. At a selected support, split off the generalized eigenspace on
which the actual profile Gram is soft. The exact frame on the remaining full
complement is then automatically sub-square-root conditioned in its actual
profile metric.

The soft sector has vanishing profile trace, but this fact alone does **not**
determine its Weil sign. The correction at the end of this claim makes that
scope explicit: an off-line Xi-cardinal direction can be profile-soft while
retaining a fixed negative Weil value. Thus this theorem closes the conditioning
problem and isolates, rather than assumes away, the final finite signature
block.

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
\(\Pi_R^0:U_R\to H_R^0\) be an exact projection whose norm and logarithmic
support derivative have the established subexponential/polylogarithmic bounds.

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

## 3. Actual profile and graph Grams

Let

\[
 {\cal T}_R:U_R\longrightarrow{\cal X}_R
 \tag{L-15630.6}
\]

be the complete omitted-tail/profile synthesis produced by \(F_R\), and define
its positive ordinary profile Gram

\[
 \boxed{D_R={\cal T}_R^*{\cal T}_R\succeq0.}
 \tag{L-15630.7}
\]

Collect every amplitude channel and logarithmic support-derivative channel
which enters the Hilbert-valued support large sieve into one map

\[
 {\cal A}_R:U_R\longrightarrow{\cal Y}_R,
 \qquad
 K_R={\cal A}_R^*{\cal A}_R.
 \tag{L-15630.8}
\]

For a subspace \(W\) on which \(D_R\) is positive, its actual-profile whitened
envelope is

\[
 \mathfrak B_R(W)^2
 =
 \left\|
 (D_R|_W)^{-1/2}(K_R|_W)(D_R|_W)^{-1/2}
 \right\|.
 \tag{L-15630.9}
\]

Assume the complete **unwhitened** graph bound

\[
 \boxed{K_R\preceq M_R^2G_R.}
 \tag{L-15630.10}
\]

The exact inverse target of `L-15628`, including the support derivative and the
finite projection transport, is

\[
 \boxed{M_R=R^{1/4+o(1)}.}
 \tag{L-15630.11}
\]

The abstract theorem only needs

\[
 \boxed{\frac{M_R\log R}{\sqrt R}\longrightarrow0.}
 \tag{L-15630.12}
\]

## 4. Balancing and the complete regularized frame

Set

\[
 \boxed{
 \ell_R=\left(\frac{\sqrt R}{M_R}\right)^{1/2},
 \qquad
 \tau_R=\ell_R^{-2}=\frac{M_R}{\sqrt R},
 \qquad
 B_R=M_R\ell_R=R^{1/4}M_R^{1/2}.
 }
 \tag{L-15630.13}
\]

Then

\[
 \boxed{\tau_R\log R\longrightarrow0}
 \tag{L-15630.14}
\]

and

\[
 \boxed{
 \frac{B_R}{\sqrt{R/\log R}}
 =
 \left(\frac{M_R\log R}{\sqrt R}\right)^{1/2}
 \longrightarrow0.
 }
 \tag{L-15630.15}
\]

Introduce the regularized profile metric

\[
 \widehat D_R=D_R+\tau_RG_R.
 \tag{L-15630.16}
\]

Equations (L-15630.10) and (L-15630.13) imply

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
 \tag{L-15630.17}
\]

Therefore the **entire exact completed frame** has regularized whitened envelope
at most

\[
 \boxed{B_R=o\!\left(\sqrt{R/\log R}\right).}
 \tag{L-15630.18}
\]

This fixed regularized metric is used over a dyadic support block. It avoids
differentiating a moving spectral projection.

## 5. Actual-profile hard/soft split at a selected support

Let \(P_R^0\) be the \(G_R\)-orthogonal projection onto the retained declared
low/core packet and put \(Q_R^0=I-P_R^0\). On \(Q_R^0U_R\), whiten the
compressed profile Gram:

\[
 \widetilde D_R
 =
 (G_R|_{Q_R^0U_R})^{-1/2}
 (Q_R^0D_RQ_R^0)
 (G_R|_{Q_R^0U_R})^{-1/2}.
 \tag{L-15630.19}
\]

Define

\[
 P_R^{\rm soft}
 =
 \mathbf1_{[0,\tau_R]}(\widetilde D_R),
 \qquad
 Q_R^{\rm hard}=I-P_R^{\rm soft}.
 \tag{L-15630.20}
\]

Transport these projections back to \(Q_R^0U_R\), and put

\[
 S_R^{\rm soft}=\operatorname{Ran}P_R^{\rm soft},
 \qquad
 W_R^{\rm hard}=\operatorname{Ran}Q_R^{\rm hard}.
 \tag{L-15630.21}
\]

Then

\[
 \boxed{
 U_R
 =
 P_R^0U_R
 \oplus_{G_R}S_R^{\rm soft}
 \oplus_{G_R}W_R^{\rm hard}.
 }
 \tag{L-15630.22}
\]

There are no omitted finite directions.

On the hard complement,

\[
 \boxed{
 D_R|_{W_R^{\rm hard}}
 \succeq
 \tau_RG_R|_{W_R^{\rm hard}}.
 }
 \tag{L-15630.23}
\]

Consequently

\[
 \begin{aligned}
 K_R|_{W_R^{\rm hard}}
 &\preceq M_R^2G_R|_{W_R^{\rm hard}}\\
 &\preceq\frac{M_R^2}{\tau_R}D_R|_{W_R^{\rm hard}}\\
 &=B_R^2D_R|_{W_R^{\rm hard}}.
 \end{aligned}
 \tag{L-15630.24}
\]

Therefore the exact restricted source frame

\[
 \boxed{F_R|_{W_R^{\rm hard}}}
 \tag{L-15630.25}
\]

spans the full actual-profile hard complement and satisfies

\[
 \boxed{
 \mathfrak B_R(W_R^{\rm hard})
 \le B_R
 =o\!\left(\sqrt{\frac R{\log R}}\right).
 }
 \tag{L-15630.26}
\]

This is the conditioning theorem itself.

## 6. Quantitative size of the soft sector

On the soft sector,

\[
 \boxed{
 D_R|_{S_R^{\rm soft}}
 \preceq
 \tau_RG_R|_{S_R^{\rm soft}}.
 }
 \tag{L-15630.27}
\]

If \(m_R=\dim U_R\), then

\[
 \boxed{
 \operatorname{Tr}_{G_R}(D_R|_{S_R^{\rm soft}})
 \le m_R\tau_R.
 }
 \tag{L-15630.28}
\]

For the quadratic-log cutoff,

\[
 m_R=O((\log R)^2).
 \tag{L-15630.29}
\]

Together with (L-15630.11),

\[
 \boxed{
 m_R\tau_R\log R
 =O((\log R)^3)\frac{M_R}{\sqrt R}
 \longrightarrow0.
 }
 \tag{L-15630.30}
\]

This proves that the sector removed for conditioning has vanishing **ordinary
profile mass** at the scalar local-Weyl scale. It does not, without an additional
form estimate, prove that its localized Weil compression is small or positive.

## 7. Support selection in the regularized metric

Equation (L-15630.17) allows the Hilbert-valued support-average theorem to be
run on the complete exact frame in the fixed metric \(\widehat D_R\). At a good
selected support, every oscillatory family covered by the support large sieve
is \(o(\log R)\) relative to \(\widehat D_R\).

Only after selecting that support is the split (L-15630.20) made. On the hard
sector,

\[
 \widehat D_R\preceq2D_R,
 \tag{L-15630.31}
\]

so the selected-support estimate is relative \(o(\log R)\) in the actual
profile metric. On the soft sector,

\[
 \widehat D_R\preceq2\tau_RG_R,
 \tag{L-15630.32}
\]

so every **covered oscillatory family** is absolutely \(o(1)\).

The qualification is essential: a finite low-zero, local, or other deterministic
Weil block which is not controlled by the declared graph map \({\cal A}_R\) does
not become small merely because \(D_R\) is soft. Such blocks must be retained in
an exact finite LMI or added to the graph map with their correct proof-facing
normalization.

## 8. Quantitative join with the current source machinery

For the repository's current exact-inverse target,

\[
 M_R
 =R^{1/4}
 \exp\!\bigl(O((\log\log R)^2)\bigr),
 \tag{L-15630.33}
\]

so

\[
 \tau_R
 =R^{-1/4}
 \exp\!\bigl(O((\log\log R)^2)\bigr)
 \tag{L-15630.34}
\]

and

\[
 B_R
 =R^{3/8}
 \exp\!\bigl(O((\log\log R)^2)\bigr).
 \tag{L-15630.35}
\]

Hence

\[
 \boxed{
 B_R=o\!\left(\sqrt{R/\log R}\right),
 \qquad
 m_R\tau_R\log R\to0.
 }
 \tag{L-15630.36}
\]

The global-anchor/prolate core retains its exact target and known radial
hierarchy. The exact Fourier--Mellin inverse supplies algebraic completeness.
Every remaining correction direction with a nonsoft actual profile denominator
is automatically sub-square-root conditioned after actual-profile whitening.

## 9. Exact remaining soft-signature block

Let \(A_R\) denote the exact localized Weil operator or its already Schur-shortened
finite packet form. Define the soft-sector corrected form

\[
 \boxed{
 \mathscr S_R^{\rm soft}
 =
 P_R^{\rm soft}A_RP_R^{\rm soft}
 -
 Z_R^*C_R^{-1}Z_R,
 }
 \tag{L-15630.37}
\]

in the same production metric, with the Schur term omitted when it has already
been incorporated into \(A_R\).

The conditioning theorem closes the whole hard complement. To promote the soft
sector into the near-radical packet, one still needs

\[
 \boxed{
 \left\|
 \left[
 (G_R|_{S_R^{\rm soft}})^{-1/2}
 \mathscr S_R^{\rm soft}
 (G_R|_{S_R^{\rm soft}})^{-1/2}
 \right]_{-}
 \right\|\longrightarrow0,
 }
 \tag{L-15630.38}
\]

or a stronger two-sided near-radical compression/residual estimate.

This is finite-dimensional and potentially much smaller than the original
complete complement, but it is genuinely RH-bearing. An off-line Xi-cardinal
direction can lie in a profile-soft sector while retaining a fixed negative
Weil value.

Thus the previous quarter-power angle is replaced by the exact dichotomy:

```text
hard actual-profile sector:
    complete and sub-square-root conditioned unconditionally from the graph LMI;

soft actual-profile sector:
    vanishing ordinary profile trace, with its finite Weil sign left explicit.
```

## 10. Exact production obligation

The conditioning theorem requires one directed packet in a common metric:

\[
 \boxed{
 {\cal L}_RF_R=I,
 \qquad
 K_R\preceq M_R^2G_R,
 \qquad
 \frac{M_R\log R}{\sqrt R}\to0.
 }
 \tag{L-15630.39}
\]

A certificate then emits \(D_R\), performs the directed generalized spectral
split, and proves (L-15630.23)--(L-15630.26). The remaining soft matrix
(L-15630.37) is emitted, not hidden.

`L-15628` supplies the target rate modulo its declared local-zeta-product,
periodized-Mellin, smoothness/even-extension, and support-derivative
normalization audit.

## 11. Proof boundary

- The core-preserving exact completion is finite linear algebra.
- The regularization, generalized spectral split, and hard-sector conditioning
  inequalities are exact.
- The entire exact frame has sub-square-root conditioning in the regularized
  metric; the full actual-profile hard complement has it in the actual metric.
- Small ordinary profile mass alone does not imply a small Weil form. The
  earlier unqualified absorption statement is corrected here and by
  `R-15604`.
- The production graph LMI and the finite soft-signature estimate have not been
  emitted for a real Suzuki/CCM packet.
- No RH conclusion is claimed.
