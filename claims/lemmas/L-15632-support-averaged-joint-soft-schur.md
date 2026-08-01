# L-15632 — Support-averaged joint shorting closes the profile-soft block

Claim ID: `L-15632`  
Title: Export the actual soft profile packet after support selection and control its fully shorted Weil matrix by one regularized local-Weyl LMI  
Status: `PROPOSED — COMPLETE ABSTRACT/COFINAL COMPOSITION; PRODUCTION JOINT PROFILE LMI NOT YET EMITTED`  
Authoring agent: `gpt56-08`  
Created: 2026-08-01  
Dependencies: `L-15630`; `L-15631`; `L-16220`--`L-16226`; `L-18512`  
Scope: the finite profile-soft signature left by `L-15630`  
Related counterexample candidates: none

## 1. Purpose

`L-15630` gives an exact complete source frame with sub-square-root regularized
conditioning.  After support selection it splits the finite packet into an
actual-profile hard complement and a profile-soft finite sector.  The hard
sector is already handled by the support-averaged complement floor.  The only
remaining object was the fully shorted Weil matrix on the soft sector.

The key observation is that the support average must be performed **before**
the soft/hard spectral split and on the complete low-plus-harmonic graph
packet.  The positive diagonal radial branches then produce one joint main
profile matrix.  Every line-centered standing wave, every horizontal off-line
cross branch, every terminal-prime/polar interaction and every harmonic cross
is retained in one regularized remainder.  The main-profile harmonic solve
cancels the leading mixed block exactly, so the final Schur penalty is
quadratic in that same remainder.

This yields a direct quantitative bound for the negative part of the actual
soft Schur block.

## 2. Joint low/harmonic matrix

Fix one support scale `R` and put

\[
 L=\log R.
\]

Let `S_R` be a finite low packet with metric `G_R>0`, and let `E_R` be the
finite harmonic/form-core packet used in the direct short of `L-18512`.
Write the complete prime, polar, archimedean and harmonic matrix as

\[
 \mathcal H_R=
 \begin{pmatrix}
 A_R&Z_R^*\\
 Z_R&C_R
 \end{pmatrix}
 \quad\text{on}\quad S_R\oplus E_R.
 \tag{L-15632.1}
\]

The exact Schur block on `S_R` is

\[
 \mathscr S_R=A_R-Z_R^*C_R^{-1}Z_R.
 \tag{L-15632.2}
\]

Let the diagonal-branch/main-density profile Gram of the same joint packet be

\[
 \mathcal D_R=
 \begin{pmatrix}
 D_R&Y_R^*\\
 Y_R&D_{E,R}
 \end{pmatrix}\succeq0,
 \qquad D_{E,R}\succ0.
 \tag{L-15632.3}
\]

The low block `D_R` is the actual positive profile Gram used to define the
soft packet.  No prolate surrogate is substituted.

## 3. Joint regularized local-Weyl LMI

Let `tau_R>0` and define

\[
 \widehat{\mathcal D}_R
 =
 \mathcal D_R+\tau_R
 \begin{pmatrix}
 G_R&0\\0&D_{E,R}
 \end{pmatrix}.
 \tag{L-15632.4}
\]

Assume that at the selected support there is a number
`0<=epsilon_R<=1/4` such that

\[
 \boxed{
 -\epsilon_R L\widehat{\mathcal D}_R
 \preceq
 \mathcal H_R-L\mathcal D_R
 \preceq
 \epsilon_R L\widehat{\mathcal D}_R.
 }
 \tag{L-15632.5}
\]

This is the **soft-signature cofinal LMI**.  It is a single joint matrix
statement; no prime, polar, archimedean or harmonic term is norm-charged
separately.

### Why (L-15632.5) is the correct output of the existing radial stack

Use the finite branch decomposition for the complete graph packet.

1. The diagonal radial branches are positive and their Riemann--von Mangoldt
   main density is exactly `L D_R`.
2. The logarithmic-density correction is a bounded multiplier of the same
   diagonal profile Gram.
3. The diagonal counting remainder and horizontal diagonal displacement cost
   `O(B_T^2 log T/T)` in the regularized metric.
4. Every cross branch on the critical line and every reflected off-line cross
   branch has a nonconstant support action.  Put all of them, including the
   line-centered standing waves, into the Hilbert-valued support large sieve of
   `L-16226`.
5. The endpoint polylogarithm channels, Airy windows, Poisson aliases and
   directed radial remainders are the finite families of `L-16221`--`L-16225`.
6. The exact terminal-prime/polar cancellation and the direct harmonic trial
   lift are retained before the LMI is formed, as required by `L-18512`.

If the complete regularized frame envelope satisfies

\[
 \mathfrak B_T=o\!\left(\sqrt{T/\log T}\right),
 \tag{L-15632.6}
\]

then the sum of the support-average mean-square budgets is `o((log T)^2)`.
Consequently each dyadic block contains a support for which
(L-15632.5) holds with `epsilon_R->0`.  The support may simultaneously avoid all
exact cycle lengths and satisfy every directed radial/endpoint gate.

The smooth exact inverse of `L-15631` and the regularized complete-frame theorem
`L-15630` are designed to supply (L-15632.6).  A production certificate must
still emit the actual matrices in (L-15632.5).

## 4. Exact export of the soft packet

After the good support has been selected, whiten the low profile Gram:

\[
 \widetilde D_R=G_R^{-1/2}D_RG_R^{-1/2}.
 \tag{L-15632.7}
\]

Let `m_R=dim S_R`.  The interval `[tau_R,2 tau_R]` contains at most `m_R`
generalized eigenvalues.  Hence it contains a gap of length at least

\[
 \frac{\tau_R}{m_R+1}.
 \tag{L-15632.8}
\]

Choose the midpoint `vartheta_R` of such a gap.  Then

\[
 \tau_R\le\vartheta_R\le2\tau_R,
 \qquad
 \operatorname{dist}(\vartheta_R,\sigma(\widetilde D_R))
 \ge\frac{\tau_R}{2(m_R+1)}.
 \tag{L-15632.9}
\]

Define the actual profile-soft projection

\[
 \boxed{
 P_R^{\rm soft}
 =\mathbf1_{[0,\vartheta_R]}(\widetilde D_R).
 }
 \tag{L-15632.10}
\]

This is defined only after support selection, so no moving projection is
differentiated in the support-average proof.  Its range is an exact spectral
subspace of the exact finite profile matrix.  The gap in (L-15632.9) gives a
proof-producing export by interval generalized-eigenvalue isolation and a Riesz
projector enclosure.  In general the exact spectral range need not possess a
rational basis.  A production certificate therefore retains either the
projector enclosure itself or an interval graph over a reference coordinate
subspace, with its projector-distance error charged in the final compression.

On the exported packet,

\[
 \boxed{
 P_R^{\rm soft}D_RP_R^{\rm soft}
 \preceq2\tau_R P_R^{\rm soft}G_RP_R^{\rm soft}.
 }
 \tag{L-15632.11}
\]

Write `G_{S,R}`, `D_{S,R}` and `mathscr S_{S,R}` for the corresponding
compressions.

## 5. Main-profile harmonic solve

Suppress `R` temporarily.  Write

\[
 \mathcal D=
 \begin{pmatrix}D_S&Y^*\\Y&D_E\end{pmatrix},
 \qquad
 \mathcal H=L\mathcal D+\mathcal E,
 \tag{L-15632.12}
\]

where (L-15632.5) says

\[
 -\varepsilon L\widehat{\mathcal D}
 \preceq\mathcal E\preceq
 \varepsilon L\widehat{\mathcal D}.
 \tag{L-15632.13}
\]

Choose the main-profile harmonic solve

\[
 X_0=D_E^{-1}Y
 \tag{L-15632.14}
\]

and its graph

\[
 J_0s=(s,-X_0s).
 \tag{L-15632.15}
\]

Positivity of `mathcal D` gives

\[
 J_0^*\mathcal D J_0
 =D_S-Y^*D_E^{-1}Y\succeq0,
 \tag{L-15632.16}
\]

and

\[
 X_0^*D_EX_0\preceq D_S\preceq2\tau G_S.
 \tag{L-15632.17}
\]

Since the ambient regularizer is `tau D_E`,

\[
 \boxed{
 J_0^*\widehat{\mathcal D}J_0
 \preceq4\tau G_S
 }
 \tag{L-15632.18}
\]

for `tau<=1/2`.

## 6. Direct-short estimate

Let

\[
 \mathscr R_0=Z-CX_0
 \tag{L-15632.19}
\]

be the actual harmonic residual.  The main `L mathcal D` part cancels from this
residual, so

\[
 \mathscr R_0=P_E\mathcal E J_0.
 \tag{L-15632.20}
\]

The ambient block satisfies

\[
 C\succeq
 L[1-\varepsilon(1+\tau)]D_E
 \succeq\frac L2D_E
 \tag{L-15632.21}
\]

when `epsilon<=1/4` and `tau<=1/2`.

The relative error LMI gives

\[
 \mathscr R_0^*[(1+\tau)D_E]^{-1}\mathscr R_0
 \preceq
 \varepsilon^2L^2J_0^*\widehat{\mathcal D}J_0.
 \tag{L-15632.22}
\]

Hence

\[
 \mathscr R_0^*C^{-1}\mathscr R_0
 \preceq
 4\varepsilon^2LJ_0^*\widehat{\mathcal D}J_0.
 \tag{L-15632.23}
\]

The exact direct-short identity of `L-18512` now gives

\[
 \begin{aligned}
 \mathscr S_S
 &=J_0^*\mathcal HJ_0
   -\mathscr R_0^*C^{-1}\mathscr R_0\\
 &\succeq
 -\left(\varepsilon+4\varepsilon^2\right)
 L J_0^*\widehat{\mathcal D}J_0.
 \end{aligned}
 \tag{L-15632.24}
\]

Using (L-15632.18),

\[
 \boxed{
 \mathscr S_S
 \succeq
 -4\left(\varepsilon+4\varepsilon^2\right)
 L\tau G_S.
 }
 \tag{L-15632.25}
\]

Equivalently,

\[
 \boxed{
 \left\|
 \left[
 G_S^{-1/2}\mathscr S_SG_S^{-1/2}
 \right]_{-}
 \right\|
 \le
 4\left(\varepsilon+4\varepsilon^2\right)L\tau.
 }
 \tag{L-15632.26}
\]

This estimate includes the complete prime, polar and archimedean diagonal, the
full line-centered and off-line phase matrix, and the harmonic Schur short.
There is no separated terminal norm or separated harmonic-cross charge.

## 7. Cofinal conclusion

For the exact smooth Fourier--Mellin frame, take

\[
 M_R=R^{1/4+o(1)},
 \qquad
 \tau_R=\frac{M_R}{\sqrt R}=R^{-1/4+o(1)}.
 \tag{L-15632.27}
\]

Then

\[
 \tau_R\log R\longrightarrow0.
 \tag{L-15632.28}
\]

The support average supplies an unbounded sequence with
`epsilon_(R_j)->0` and the exported exact projectors
`P_(R_j)^soft`.  Therefore (L-15632.26) proves

\[
 \boxed{
 \left\|
 \left[
 G_{S,j}^{-1/2}\mathscr S_{S,j}G_{S,j}^{-1/2}
 \right]_{-}
 \right\|
 \longrightarrow0.
 }
 \tag{L-15632.29}
\]

Thus, at theorem-interface level, the finite profile-soft gate is closed by one
joint support-averaged LMI and one main-profile harmonic solve.

## 8. Production relation to PR #191

PR #191 now emits the complete prime/archimedean and harmonic direct-block data
for an actual cutoff-free D-0001 level and a genuinely growing source-canonical
ladder.  The real `c=5,N=1` artifact certifies a zero negative part.  The new
production extension is to emit, at each level,

```text
joint profile Gram mathcal D_R;
regularized Gram widehat mathcal D_R;
soft threshold vartheta_R and spectral-gap enclosure;
Riesz-projector or interval graph enclosure;
compressed P,E,Z,C and main-profile solve X_0;
relative joint remainder epsilon_R;
exact direct-short LDL verdict.
```

The existing ladder is a valuable normalization and scaling control, but it is
finite and is not itself the cofinal proof of (L-15632.29).

## 9. Proof boundary

- The spectral export, main-profile solve and direct-short estimate are exact
  finite operator algebra.
- The cofinal support selection follows from `L-16226` once the complete joint
  graph packet satisfies the regularized branch envelope of `L-15630/L-15631`.
- A production directed artifact for the joint LMI (L-15632.5) has not yet been
  emitted.
- The local zeta-product, Mellin normalization and radial/endpoint constants
  retain the explicit audit boundaries already stated in `L-15631` and
  `T-16205`.
- No independent review of those imported normalizations and no RH claim is
  asserted by this file alone.
