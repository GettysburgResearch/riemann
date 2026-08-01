# T-15606 — Cofinal profile-soft LMI from exact completion and joint direct shorting

Claim ID: `T-15606`  
Title: The complete exact frame, regularized support average, actual soft spectral export and direct harmonic short imply a vanishing soft negative part  
Status: `PROPOSED — COMPLETE COMPOSITION THEOREM; PRODUCTION INTERVAL SEQUENCE OPEN`  
Authoring agent: `gpt56-08`  
Created: 2026-08-01  
Dependencies: `L-15630`--`L-15632`; `L-16220`--`L-16226`; `L-18512`; `T-14302`  
Scope: the last finite soft-signature gate after complete-frame conditioning  
Related counterexample candidates: none

## Statement

Let `T_j->infinity` be dyadic radial scales.  On every block `[T_j,2T_j]`,
assume the exact smooth source inverse and core-preserving completion provide a
complete finite joint low/harmonic packet with:

1. exact source identity;
2. finite branch and endpoint representations in the declared CCM/Suzuki
   normalization;
3. regularized graph envelope
   \[
   \mathfrak B_{T_j}
   =o\!\left(\sqrt{T_j/\log T_j}\right);
   \]
4. all directed radial, Airy, endpoint, Poisson and finite-prefix remainders
   included in the support-average ledger.

Then there exist supports

\[
 R_j\in[T_j,2T_j],
 \qquad R_j\to\infty,
 \tag{T-15606.1}
\]

and exact actual-profile soft projections

\[
 P_j^{\rm soft}
 =\mathbf1_{[0,\vartheta_j]}
 \left(G_j^{-1/2}D_jG_j^{-1/2}\right),
 \qquad
 \tau_j\le\vartheta_j\le2\tau_j,
 \tag{T-15606.2}
\]

with

\[
 \tau_j
 =\frac{M_{R_j}}{\sqrt{R_j}},
 \qquad
 M_R=R^{1/4+o(1)},
 \tag{T-15606.3}
\]

such that the fully shorted soft matrix

\[
 \mathscr S_j^{\rm soft}
 =
 P_j^{\rm soft}
 \left(A_j-Z_j^*C_j^{-1}Z_j\right)
 P_j^{\rm soft}
 \tag{T-15606.4}
\]

satisfies

\[
 \boxed{
 \left\|
 \left[
 G_{S,j}^{-1/2}
 \mathscr S_j^{\rm soft}
 G_{S,j}^{-1/2}
 \right]_{-}
 \right\|
 \longrightarrow0.
 }
 \tag{T-15606.5}
\]

More explicitly, if `epsilon_j` is the relative joint remainder in
`L-15632.5`, then

\[
 \boxed{
 \left\|
 \left[
 G_{S,j}^{-1/2}
 \mathscr S_j^{\rm soft}
 G_{S,j}^{-1/2}
 \right]_{-}
 \right\|
 \le
 4(\epsilon_j+4\epsilon_j^2)
 (\log R_j)\tau_j.
 }
 \tag{T-15606.6}
\]

The right side tends to zero because

\[
 \epsilon_j\to0,
 \qquad
 (\log R_j)\tau_j
 =R_j^{-1/4+o(1)}\log R_j\to0.
 \tag{T-15606.7}
\]

## Proof

Apply the support large sieve simultaneously to every line-centered and
off-line cross branch of the complete joint graph packet.  The diagonal branch
counting remainders and endpoint/alias families are smaller than the same
regularized scale.  The positive-measure gate therefore selects `R_j` for which
the joint LMI `L-15632.5` holds with `epsilon_j->0`.

After selection, choose a spectral gap in `[tau_j,2tau_j]` and export the exact
projection `P_j^soft` as in `L-15632.8`--`L-15632.10`.  The compressed profile
satisfies

\[
 D_{S,j}\preceq2\tau_jG_{S,j}.
\]

Use the main-profile harmonic solve

\[
 X_j^0=D_{E,j}^{-1}Y_j.
\]

The leading `(log R_j)mathcal D_j` mixed block cancels exactly.  The actual
harmonic residual consists only of the joint remainder.  The exact direct-short
identity of `L-18512` and the relative LMI then give the bound
`T-15606.6`, which proves `T-15606.5`.

No prime, polar, archimedean or harmonic channel is bounded before the exact
joint matrix and exact pole cancellation have been formed.

## Composition with the full positive route

The hard actual-profile complement has the support-averaged positive floor of
`L-15630/L-15627`.  The soft block has `T-15606.5`.  The already-separated
radical-row and directed assembly losses tend to zero.  Therefore the complete
localized lower envelope tends to zero from below.

Subject to the exact normalization and domain dependencies of the imported
CCM/Suzuki stack, `T-14302` then converts an unbounded production sequence of
these certificates into RH.

This theorem is a composition statement.  It does not claim that the required
production interval matrices have already been emitted or independently
reviewed.

## Proof-producing certificate

At each retained support the certificate records:

```text
exact support/radial parameters;
complete source and basis digests;
G, joint profile D and regularized Dhat;
finite branch and endpoint ledgers;
joint prime/polar/archimedean/harmonic matrix H;
relative LMI endpoint epsilon;
soft threshold and generalized spectral gap;
soft projector/basis enclosure;
main-profile harmonic solve X0;
actual residual and coercive ambient solve;
fully shorted directed matrix;
negative-part or shifted-LDL endpoint;
precision nesting and independent prime-side replay.
```

The level passes only when the directed upper endpoint for the normalized
negative part is below the declared bound in `T-15606.6`.

## Current production status

PR #191 supplies the complete direct-block emitter, one certified actual
`c=5,N=1` positive level, and a real growing source-canonical ladder.  It does
not yet emit the joint profile Gram or the exact soft spectral projector needed
by this theorem.  Therefore the cofinal production sequence remains to be
run, even though the finite and asymptotic composition is now explicit.
